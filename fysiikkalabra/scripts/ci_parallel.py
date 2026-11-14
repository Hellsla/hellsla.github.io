"""Runs the three browser checks of CI in parallel, unchanged: the same scripts, pages, widths and verdicts.

  python scripts/ci_parallel.py plan    --pages "<full | page ids | empty>"     the jobs of a run, as GitHub outputs
  python scripts/ci_parallel.py sims    [--pages ...] [--shard i/n] [--workers N] [--report f.json]
  python scripts/ci_parallel.py layout  --widths "360 390 ..." [--pages ...] [--shard i/n] [--workers N] [--report f.json]
  python scripts/ci_parallel.py inquiry [--pages ...] [--shard i/n] [--workers N] [--report f.json]
  python scripts/ci_parallel.py simtext [--pages ...] [--shard i/n] [--workers N] [--report f.json]   test_sim_text.py: the picture's text at 1366×650
  python scripts/ci_parallel.py gate <reports-dir> --pages "<the same>"         every planned page was tested and passed

Why (2026-11-11): test_sims.py, check_layout.py at eight widths and the per-lesson test_inquiry.py runs need about
20 core-hours for the whole site and ran one page at a time on one core of a four-core runner; a full run did not fit
into the six hours a job may take, and a failing simulation hid every later check. This script changes how the checks
are run, not what they check:

  unit      one page id (fy4-3; it covers the page in every language, as the scripts' own page argument does), for the
            layout check one page id at one width. A unit is tested by the unchanged script:
              sims     python scripts/test_sims.py <id>
              layout   python scripts/check_layout.py <id> --site --width <w>
              inquiry  python scripts/test_inquiry.py <id>
  universe  the units of a full run are listed exactly as the scripts list their pages (every page with a simulation in
            preview/ or site/, every lesson page of site/, every content/fi/<COURSE>/<id>/inquiry.json); a pull request's
            run takes from them the pages scripts/ci_scope.py names
  shard     --shard i/n takes every n-th unit of the sorted universe, starting from the i-th: the n jobs of a matrix
            test each unit exactly once
  workers   N units at a time, each in its own process and browser. Default: half the machine's cores, because the
            checks wait fixed times for a page to settle and the simulations run in real time: one test's browser used
            0.9-1.3 cores when it had the whole four-core runner (measured 2026-11-11), so two at a time leave every
            browser the room it had alone. With four at a time the runner was saturated (3.8 of 4 cores) and inquiry
            tests that pass alone failed (fy4-14, fy8-12: "simState gives ..."). More speed comes from more jobs,
            never from more workers than that.

A unit passes when its script exits 0 AND printed its verdict line for every page file it had to test (a page a script
skipped without a word fails here). Nothing is retried to turn a failure into a pass. One thing is run again, to judge
more, never less: test_sims.py does not judge an assertion that failed while frames were late ("slow: not judged",
2026-11-10); a unit with such lines is run once more alone after the others, when the machine is idle, and it passes
only if both runs passed.

A browser that hangs gives no verdict (2026-11-11: check_layout.py on fy8-5 at 390 px stood still for 55 minutes on a
runner and ran in seconds elsewhere). A unit is stopped after TIMEOUT seconds, several times what the slowest unit
needs, and run once more alone; that second run is its verdict, and a second hang fails it. The log and the gate's
summary name every unit that hung.

The inquiry test builds its page into preview/ (build.py <id>, which also copies the shared files again), so its
workers do not share a folder: each gets its own git work tree of HEAD (the same files and the same history, which the
build reads for the exercises' reviewed version) and runs the test there. With uncommitted changes in the folder the
work trees would not show what is being tested, so the tests then run one at a time in place.

The report (JSON) lists the universe and every unit's verdict; `gate` reads the reports of all jobs of a run and fails
unless every planned check reported, the jobs agree on the universe, every unit of it was tested exactly once and every
unit passed. So a page no job tested fails the run."""
import argparse, concurrent.futures as cf, json, math, os, pathlib, re, shutil, signal, subprocess, sys, tempfile, threading, time

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
PY = sys.executable
WIDTHS = "360 390 640 768 1024 1280 1440 1920"   # the eight widths of the layout check (NOTES.md §8)
SIMS_SHARDS, INQUIRY_SHARDS, LAYOUT_SHARDS, SIMTEXT_SHARDS, SMALL = 8, 4, 2, 2, 12   # the jobs of a full run (layout: per width); up to SMALL pages run in one job per check
SLOW = "slow: not judged"
TIMEOUT = {"simtext": 300, "sims": 2400, "layout": 600, "inquiry": 1500}   # seconds a unit may take; the slowest measured: 750, 60 and 410 (fy3-10)


def languages():
    sys.path.insert(0, str(HERE)); import i18n
    return i18n.languages()


def page_files(out):
    """The pages as test_sims.py and check_layout.py walk them: <out>/*.html, then <out>/<lang>/*.html."""
    return sorted(out.glob("*.html")) + [f for lang in languages()[1:] for f in sorted((out / lang).glob("*.html"))]


def universe(kind, root=ROOT):
    """{unit id: [verdict keys the script must print for it]} of a full run."""
    units = {}
    if kind in ("sims", "simtext"):
        out = root / "preview" if (root / "preview" / "index.html").exists() else root / "site"
        for f in page_files(out):
            if 'id="sim-root"' in f.read_text(): units.setdefault(f.stem, []).append(f"{out.name}/{f.relative_to(out).with_suffix('').as_posix()}")
    elif kind == "layout":
        out = root / "site"
        for f in page_files(out):
            if f.stem != "index" and "-" in f.stem: units.setdefault(f.stem, []).append(f"{out.name}/{f.relative_to(out).with_suffix('').as_posix()}")
    elif kind == "inquiry":
        for f in sorted((root / "content/fi").glob("*/*/inquiry.json")):
            if f.parts[-3] != "units": units[f.parent.name] = []   # course units are checked by units.py check
    return units


def select(units, pages, shard):
    ids = sorted(units)
    if pages != "full": ids = [i for i in ids if i in set(pages.split())]
    i, n = (int(x) for x in shard.split("/"))
    if not 0 <= i < n: sys.exit(f"--shard {shard}: not i/n with 0 <= i < n")
    return ids, ids[i::n]


def command(kind, uid, width, root):
    s = root / "scripts"
    if kind == "sims": return [PY, s / "test_sims.py", uid]
    if kind == "simtext": return [PY, s / "test_sim_text.py", uid]
    if kind == "layout": return [PY, s / "check_layout.py", uid, "--site", "--width", str(width)]
    return [PY, s / "test_inquiry.py", uid]


def verdict(kind, keys, width, rc, text):
    """(ok, problems): the script's exit status, and its verdict line for every page file of the unit."""
    problems = []
    if kind == "inquiry":
        m = re.search(r"^(\d+) passed, (\d+) failed\s*$", text, re.M)
        if not m: problems.append("no 'N passed, N failed' line")
        elif rc == 0 and (m.group(2) != "0" or m.group(1) == "0"): problems.append(f"exit 0 with '{m.group(0).strip()}'")
    else:
        word, tail = ("PASS|FAIL", "") if kind in ("sims", "simtext") else ("OK|FAIL", f" at {width} px")
        seen = re.findall(rf"^(?:{word})\s+(\S+){re.escape(tail)}(?= |$)", text, re.M)
        for k in keys:
            if seen.count(k) != 1: problems.append(f"{k}: {seen.count(k)} verdict lines, expected 1")
        problems += [f"{k}: a verdict for a page outside the unit" for k in sorted(set(seen) - set(keys))]
    return rc == 0 and not problems, problems


def cpu_seconds():
    try:
        v = [int(x) for x in open("/proc/stat").readline().split()[1:9]]
        return (sum(v) - v[3] - v[4]) / os.sysconf("SC_CLK_TCK")
    except Exception: return 0.0


def run(kind, args):
    units = universe(kind)
    ids, mine = select(units, args.pages, args.shard)
    widths = [int(w) for w in args.widths.split()] if kind == "layout" else [None]
    tasks = [(u, w) for w in widths for u in mine]
    workers = max(1, min(args.workers or (os.cpu_count() or 2) // 2, len(tasks) or 1))
    lock, results, t0, c0 = threading.Lock(), [], time.time(), cpu_seconds()
    limit = args.timeout or TIMEOUT[kind]
    tmp, top = None, None
    if kind == "inquiry" and workers > 1 and tasks:   # a folder of its own for every worker (see the docstring)
        g = lambda *a: subprocess.run(["git", *a], cwd=ROOT, capture_output=True, text=True)
        top = g("rev-parse", "--show-toplevel").stdout.strip()
        if not top or g("status", "--porcelain", "--", ".").stdout.strip():
            workers = 1; print("uncommitted changes (or no git): the inquiry tests run one at a time in this folder", flush=True)
        else:
            tmp = pathlib.Path(tempfile.mkdtemp(prefix="fl-inquiry-", dir=os.environ.get("RUNNER_TEMP")))
            for n in range(workers):
                r = g("worktree", "add", "--detach", "--force", str(tmp / f"w{n}"), "HEAD")
                if r.returncode: sys.exit(f"git worktree add failed: {r.stderr}")
            print(f"{workers} work trees of HEAD in {time.time() - t0:.0f} s", flush=True)
    rel = ROOT.relative_to(top) if tmp else None
    free = list(range(workers))

    def one(task, alone=False):
        uid, w = task
        with lock: n = free.pop()
        root = tmp / f"w{n}" / rel if tmp else ROOT
        t = time.time()
        proc = subprocess.Popen(command(kind, uid, w, root), cwd=root, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True,
                                env={**os.environ, "PYTHONUNBUFFERED": "1"}, start_new_session=True)   # its own process group: a hung browser is stopped with it
        try:
            text, rc = proc.communicate(timeout=limit)[0], proc.returncode
        except subprocess.TimeoutExpired:
            try: os.killpg(proc.pid, signal.SIGKILL)
            except ProcessLookupError: pass
            rc, text = 124, f"{proc.communicate()[0] or ''}\nno verdict: stopped after {limit} s"
        ok, problems = verdict(kind, units[uid], w, rc, text)
        res = {"id": uid, "width": w, "rc": rc, "ok": ok, "seconds": round(time.time() - t, 1), "problems": problems,
               "pages": len(units[uid]) or 1, "slow": text.count(SLOW), "alone": alone, "hung": rc == 124}
        with lock:
            free.append(n); results.append(res)
            name = uid + (f" at {w} px" if w else "") + (" (again, alone)" if alone else "")
            if kind == "inquiry" and ok: print(f"{name}: {text.strip().splitlines()[-1]}  [{res['seconds']:.0f} s]")
            else:
                if not ok: print(f"::error::{kind} failed for {name}" if os.environ.get("GITHUB_ACTIONS") else f"FAILED {name}")
                shown = text.rstrip() if kind != "inquiry" else "\n".join([l for l in text.splitlines() if l.startswith("FAIL")] or text.splitlines()[-20:])
                print(shown); [print(f"     ci_parallel: {p}") for p in problems]
            sys.stdout.flush()
        return res

    print(f"{kind}: {len(tasks)} of {len(ids) * len(widths)} units (shard {args.shard}), {workers} workers", flush=True)
    with cf.ThreadPoolExecutor(workers) as ex: first = list(ex.map(one, tasks))
    again = [(r["id"], r["width"]) for r in first if r["hung"] or (kind == "sims" and r["slow"])]
    hung = [r["id"] + (f"@{r['width']}" if r["width"] else "") for r in first if r["hung"]]
    if again:
        print(f"{len(again)} units gave no verdict ({len(hung)} hung) or had assertions not judged on a busy machine; once more, one at a time", flush=True)
        if hung: print(f"{'::warning::' if os.environ.get('GITHUB_ACTIONS') else 'WARNING: '}no verdict in {limit} s, run again alone: {' '.join(hung)}", flush=True)
        for t in again: one(t, alone=True)
    if tmp:
        for n in range(workers): subprocess.run(["git", "worktree", "remove", "--force", str(tmp / f"w{n}")], cwd=ROOT, capture_output=True)
        shutil.rmtree(tmp, ignore_errors=True)
    wall, cpu = time.time() - t0, cpu_seconds() - c0
    failed = sorted({r["id"] + (f"@{r['width']}" if r["width"] else "") for r in results if not r["ok"] and (r["alone"] or not r["hung"])})
    still = sum(r["slow"] for r in results if r["alone"])
    report = {"kind": kind, "shard": args.shard, "pages": args.pages, "widths": [w for w in widths if w], "universe": ids, "units": results,
              "workers": workers, "cores": os.cpu_count(), "wall": round(wall, 1), "cpu": round(cpu, 1), "failed": failed, "hung": hung}
    if args.report:
        p = pathlib.Path(args.report); p.parent.mkdir(parents=True, exist_ok=True); p.write_text(json.dumps(report, indent=1))
    pages = sum(r["pages"] for r in results if not r["alone"])
    print(f"\n{kind} shard {args.shard}: {len(tasks)} units, {pages} page checks, {len(failed)} failed; {wall / 60:.1f} min wall, "
          f"{cpu / 60:.1f} core-min ({cpu / wall if wall else 0:.1f} of {os.cpu_count()} cores busy on average), {workers} workers"
          + (f"; {len(again)} units run again alone, {still} assertions still not judged" if again else ""))
    if failed: print("failed: " + " ".join(failed))
    sys.exit(1 if failed else 0)


def plan(pages):
    """The jobs of a run. A full run: SIMS_SHARDS simulation jobs, LAYOUT_SHARDS layout jobs for each width,
    INQUIRY_SHARDS inquiry jobs. A few pages: one job per check. No page: no browser job."""
    n = None if pages == "full" else len(pages.split())
    if n == 0: return {"sims": [], "layout": [], "inquiry": [], "simtext": []}
    if n is not None and n <= SMALL:
        return {"sims": ["0/1"], "layout": [{"name": "all widths", "widths": WIDTHS, "shard": "0/1"}], "inquiry": ["0/1"], "simtext": ["0/1"]}
    sims = SIMS_SHARDS if n is None else min(SIMS_SHARDS, math.ceil(n / 12))
    inq = INQUIRY_SHARDS if n is None else min(INQUIRY_SHARDS, math.ceil(n / 30))
    stx = SIMTEXT_SHARDS if n is None else 1
    lay = LAYOUT_SHARDS if n is None else min(LAYOUT_SHARDS, math.ceil(n / 140))
    return {"sims": [f"{i}/{sims}" for i in range(sims)], "inquiry": [f"{i}/{inq}" for i in range(inq)], "simtext": [f"{i}/{stx}" for i in range(stx)],
            "layout": [{"name": f"{w} px {i}/{lay}", "widths": w, "shard": f"{i}/{lay}"} for w in WIDTHS.split() for i in range(lay)]}


def gate(args):
    want, bad, rows, notes = plan(args.pages), [], [], []
    reports = [json.loads(f.read_text()) for f in sorted(pathlib.Path(args.dir).rglob("*.json"))]
    groups = [("sims", None, want["sims"]), ("simtext", None, want["simtext"]), ("inquiry", None, want["inquiry"])] + \
             [("layout", int(w), [j["shard"] for j in want["layout"] if w in j["widths"].split()]) for w in WIDTHS.split() if want["layout"]]
    for kind, width, shards in groups:
        name = kind + (f" {width} px" if width else "")
        rs = [r for r in reports if r["kind"] == kind and (width is None or width in r["widths"])]
        if not shards:
            if rs: bad.append(f"{name}: a report although nothing was planned")
            continue
        if any(r["pages"] != args.pages for r in rs): bad.append(f"{name}: a job tested another page list than the run's")
        got = sorted(r["shard"] for r in rs)
        if got != sorted(shards): bad.append(f"{name}: reports of shards {got}, planned {sorted(shards)}"); continue
        uni = rs[0]["universe"]
        if any(r["universe"] != uni for r in rs): bad.append(f"{name}: the jobs list different pages")
        units = [u for r in rs for u in r["units"] if not u["alone"] and (width is None or u["width"] == width)]
        tested = sorted(u["id"] for u in units)
        if tested != sorted(uni):
            miss, dup = sorted(set(uni) - set(tested)), sorted({t for t in tested if tested.count(t) > 1})
            bad.append(f"{name}: {len(tested)} units tested, {len(uni)} listed" + (f"; not tested: {' '.join(miss[:20])}" if miss else "") + (f"; twice: {' '.join(dup[:20])}" if dup else ""))
        every = [u for r in rs for u in r["units"] if width is None or u["width"] == width]
        fails = sorted({u["id"] for u in every if not u["ok"] and (u["alone"] or not u.get("hung"))}
                       | {u["id"] for u in units if u.get("hung") and not any(v["alone"] and v["id"] == u["id"] for v in every)})   # a hang without its second run
        hangs = sorted({u["id"] for u in units if u.get("hung")})
        if hangs: notes.append(f"{name}: no verdict at first (hung), run again alone: {' '.join(hangs)}")
        if fails: bad.append(f"{name}: failed: {' '.join(fails)}")
        rows.append((name, len(rs), len(uni), sum(u["pages"] for u in units), len(fails), sum(u["seconds"] for u in every) / 60, max(r["wall"] for r in rs) / 60))
    if args.pages == "full":   # a full run's lists are compared with the committed site and sources, read here again
        for kind in ("layout", "inquiry"):
            mine = sorted(universe(kind))
            for r in reports:
                if r["kind"] == kind and r["universe"] != mine: bad.append(f"{kind} shard {r['shard']}: lists {len(r['universe'])} pages, the checkout has {len(mine)}"); break
    out = ["### Browser checks: " + ("every planned page tested and passed" if not bad else "FAILED"), "",
           "| check | jobs | units | page checks | failed units | script time (min) | longest job (min) |", "|---|--:|--:|--:|--:|--:|--:|"]
    out += [f"| {a} | {b} | {c} | {d} | {e} | {f:.1f} | {g:.1f} |" for a, b, c, d, e, f, g in rows]
    if rows: out.append(f"| total | {sum(r[1] for r in rows)} | {sum(r[2] for r in rows)} | {sum(r[3] for r in rows)} | {sum(r[4] for r in rows)} | {sum(r[5] for r in rows):.1f} | {max(r[6] for r in rows):.1f} |")
    if not any(want.values()): out.append("no page changed: the browser checks had nothing to test")
    out += [""] + [f"- {b}" for b in bad] + [f"- note: {n}" for n in notes]
    text = "\n".join(out); print(text)
    if os.environ.get("GITHUB_STEP_SUMMARY"): open(os.environ["GITHUB_STEP_SUMMARY"], "a").write(text + "\n")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("kind", choices=["plan", "sims", "simtext", "layout", "inquiry", "gate"])
    ap.add_argument("dir", nargs="?")
    ap.add_argument("--pages", default="full"); ap.add_argument("--shard", default="0/1"); ap.add_argument("--widths", default=WIDTHS)
    ap.add_argument("--workers", type=int, default=0); ap.add_argument("--report"); ap.add_argument("--timeout", type=int, default=0)
    a = ap.parse_args()
    a.pages = " ".join(a.pages.split())
    if a.kind == "plan":
        for k, v in plan(a.pages).items(): print(f"{k}={json.dumps(v)}")
    elif a.kind == "gate": gate(a)
    else: run(a.kind, a)
