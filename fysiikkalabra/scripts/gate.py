"""Publication gate: a lesson is published only when every reviewer has passed its CURRENT content.

  python scripts/gate.py --hash <id>              print the full content hash of a lesson
  python scripts/gate.py --hash <id> --for <reviewer>   print the hash of the files that reviewer judges
  python scripts/gate.py <id>                     check only; exit 1 if the lesson is not publishable
  python scripts/gate.py <id> --publish           check, then set status "reviewed" and rebuild site/
  python scripts/gate.py <id> --log-round         append one line with this round's verdicts to review/history.log
  python scripts/gate.py <id> --reopen            start revising a published lesson: its live page stays the reviewed render
  python scripts/gate.py --verify                 CI: every published lesson still matches its recorded hash (or, under
                                                  revision, its live page still matches the render the gate published)
  --skip-checks                                   (tests only) skip the lint, latex, build and simulation runs

Hashes. The full content hash covers lesson.md, exercises.json, solutions.md, exit-ticket.json, sim.js,
sim-spec.md, answers.py, tests/sims/<id>.json and meta.json without its status fields. Each reviewer has a
domain, the subset of those files it judges (DOMAINS below), and its own domain hash. A report must start
with `VERDICT: PASS` and carry `CONTENT-HASH: <hash>` within its first three lines, where the hash is either
the reviewer's domain hash or the full hash. So after a fix only the reviewers whose files changed have to
run again: a wording fix in lesson.md does not invalidate the tester's verdict on sim.js.
The gate writes review/gate.md as its audit trail."""
import datetime, hashlib, json, os, pathlib, subprocess, sys

ROOT = pathlib.Path(os.environ.get("FYSIIKKALABRA_ROOT") or pathlib.Path(__file__).resolve().parents[1])
SCRIPTS = pathlib.Path(__file__).resolve().parent
REVIEWERS = ["tester", "physics-expert", "mathematician", "educator", "proofreader", "editor", "web-designer"]
HASHED = ["lesson.md", "exercises.json", "solutions.md", "exit-ticket.json", "sim.js", "sim-spec.md", "answers.py"]
# "meta" is meta.json without the status fields, "test" is tests/sims/<id>.json
DOMAINS = {
    "tester":         ["sim.js", "sim-spec.md", "test"],
    "web-designer":   ["lesson.md", "exercises.json", "solutions.md", "exit-ticket.json", "sim.js", "sim-spec.md"],
    "physics-expert": ["lesson.md", "exercises.json", "solutions.md", "exit-ticket.json", "sim.js", "sim-spec.md", "answers.py"],
    "mathematician":  ["lesson.md", "exercises.json", "solutions.md", "exit-ticket.json", "answers.py"],
    "educator":       ["lesson.md", "exercises.json", "exit-ticket.json", "meta"],
    "editor":         ["lesson.md", "exercises.json", "exit-ticket.json", "sim-spec.md", "meta"],
    "proofreader":    ["lesson.md", "exercises.json", "solutions.md", "exit-ticket.json", "sim-spec.md", "sim.js", "meta"],
}
STATUS_KEYS = ("status", "reviewed_by", "reviewed_on", "reviewed_hash", "revision")
GATE_NAME = "gate (automaattinen tarkistus)"


def find_lesson(lid):
    for f in sorted((ROOT / "content").glob(f"*/{lid}")):
        if f.parent.name != "_gold" and (f / "meta.json").exists(): return f
    sys.exit(f"no lesson folder for id {lid!r}")


def content_hash(folder, reviewer=None):
    """Full hash by default; with a reviewer name, the hash of that reviewer's domain files only."""
    parts = HASHED + ["meta", "test"] if reviewer is None else DOMAINS[reviewer]
    h = hashlib.sha256()
    lid = folder.name
    for name in parts:
        if name == "meta":
            meta = {k: v for k, v in json.loads((folder / "meta.json").read_text()).items() if k not in STATUS_KEYS}
            h.update(b"meta.json\0" + json.dumps(meta, sort_keys=True, ensure_ascii=False).encode() + b"\0")
        elif name == "test":
            t = ROOT / "tests" / "sims" / f"{lid}.json"
            if t.exists(): h.update(b"test\0" + t.read_bytes() + b"\0")
        else:
            f = folder / name
            if f.exists(): h.update(name.encode() + b"\0" + f.read_bytes() + b"\0")
    return h.hexdigest()[:16]


def site_hash(lid):
    """Hash of the published render of a lesson (site/<id>.html and its sim), or None if it is not published."""
    page = ROOT / "site" / f"{lid}.html"
    if not page.exists(): return None
    h = hashlib.sha256(page.read_bytes())
    sim = ROOT / "site" / f"{lid}-sim.js"
    if sim.exists(): h.update(sim.read_bytes())
    return h.hexdigest()[:16]


def reopen(lid):
    """Mark a published lesson as under revision. Its source may now change while the live page stays exactly
    the render the gate published; --verify checks that page instead of the source until --publish runs again."""
    folder = find_lesson(lid)
    meta = json.loads((folder / "meta.json").read_text())
    if meta.get("status") != "reviewed" or not meta.get("reviewed_hash"):
        print(f"{lid}: only a lesson the gate published can be reopened"); return 1
    sh = site_hash(lid)
    if sh is None:
        print(f"{lid}: site/{lid}.html is missing, nothing to keep live"); return 1
    if "revision" in meta:
        print(f"{lid}: already under revision since {meta['revision']['opened']}"); return 0
    meta["revision"] = {"opened": str(datetime.date.today()), "site_hash": sh, "reviewed_hash": meta["reviewed_hash"]}
    (folder / "meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2) + "\n")
    review = folder / "review"; review.mkdir(exist_ok=True)
    with open(review / "history.log", "a") as log: log.write(f"{datetime.date.today()} {lid} REOPENED (live page {sh} kept until the next publish)\n")
    print(f"{lid}: under revision; the live page ({sh}) stays as reviewed until `gate.py {lid} --publish` passes again")
    return 0


def report_lines(folder, reviewer):
    f = folder / "review" / f"{reviewer}.md"
    return f.read_text().splitlines() if f.exists() else None


def check_report(folder, reviewer, full):
    lines = report_lines(folder, reviewer)
    if lines is None: return f"{reviewer}: no report"
    if not lines or lines[0].strip() != "VERDICT: PASS":
        return f"{reviewer}: verdict is not PASS ({lines[0].strip() if lines else 'empty report'})"
    got = next((l.split(":", 1)[1].strip() for l in lines[:3] if l.startswith("CONTENT-HASH:")), None)
    if got is None: return f"{reviewer}: report has no CONTENT-HASH line"
    want = content_hash(folder, reviewer)
    if got not in (want, full):
        return f"{reviewer}: report is for an older version of its files (hash {got}, now {want})"
    return None


def check_structure(folder):
    problems, lid = [], folder.name
    meta = json.loads((folder / "meta.json").read_text())
    for k in ("id", "course", "title", "goals", "prerequisites", "glossary", "sim", "status"):
        if k not in meta: problems.append(f"meta.json: missing {k}")
    if meta.get("id") != lid: problems.append(f"meta.json: id {meta.get('id')!r} does not match folder {lid!r}")
    if meta.get("course") != folder.parent.name: problems.append("meta.json: course does not match folder")
    if not meta.get("goals"): problems.append("meta.json: no goals")
    glossary = {e["term"] for e in json.loads((ROOT / "glossary.json").read_text())}
    for term in meta.get("glossary", []):
        if term not in glossary: problems.append(f"glossary term {term!r} missing from glossary.json")
    for f in ("lesson.md", "exercises.json", "solutions.md", "exit-ticket.json"):
        if not (folder / f).exists(): problems.append(f"missing {f}")
    if meta.get("sim") and not (folder / "sim.js").exists(): problems.append("meta.sim is true but sim.js is missing")
    if problems: return problems
    ex = json.loads((folder / "exercises.json").read_text())
    want = {"level1": 5, "level2": 4, "level3": 3}
    seen = set()
    for lvl, n in want.items():
        items = ex.get(lvl, [])
        if len(items) != n: problems.append(f"exercises.json: {lvl} has {len(items)} tasks, expected {n}")
        for e in items:
            for k in ("id", "level", "text", "answer", "unit", "tolerance"):
                if k not in e: problems.append(f"exercise {e.get('id', '?')}: missing {k}")
            if e.get("id") in seen: problems.append(f"duplicate exercise id {e.get('id')}")
            seen.add(e.get("id"))
            if not str(e.get("id", "")).startswith(f"{lid}-L{lvl[-1]}-"): problems.append(f"exercise id {e.get('id')} does not match {lid}-L{lvl[-1]}-NN")
            if isinstance(e.get("tolerance"), (int, float)) and e["tolerance"] <= 0: problems.append(f"exercise {e.get('id')}: tolerance must be positive")
    solutions = (folder / "solutions.md").read_text()
    for i in seen:
        if f"## {i}" not in solutions: problems.append(f"solutions.md: no solution for {i}")
    if len(json.loads((folder / "exit-ticket.json").read_text())) != 3: problems.append("exit-ticket.json: expected 3 questions")
    return problems


def run(cmd):
    r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, env=dict(os.environ, FYSIIKKALABRA_ROOT=str(ROOT)))
    return r.returncode == 0, (r.stdout + r.stderr).strip()[-600:]


def gate(lid, publish, skip_checks):
    folder = find_lesson(lid)
    h = content_hash(folder)
    meta = json.loads((folder / "meta.json").read_text())
    needed = [r for r in REVIEWERS if r != "tester" or (folder / "sim.js").exists()]
    problems = check_structure(folder)
    for r in needed:
        p = check_report(folder, r, h)
        if p: problems.append(p)
    ran = []
    if not skip_checks and not problems:
        for name, cmd in (("lint", [sys.executable, str(SCRIPTS / "lint_lesson.py"), str(folder)]),
                          ("check_latex", [sys.executable, str(SCRIPTS / "check_latex.py"), str(folder)]),
                          ("build --all", [sys.executable, str(SCRIPTS / "build.py"), "--all"])) + \
                         ((("sim tests", [sys.executable, str(SCRIPTS / "test_sims.py"), lid]),) if (folder / "sim.js").exists() else ()):
            ok, out = run(cmd); ran.append(f"{name}: {'ok' if ok else 'FAILED'}")
            if not ok: problems.append(f"{name} failed: {out}")
    warn = [f"prerequisite {p} is not published yet" for p in meta.get("prerequisites", [])
            if not any(json.loads((x / "meta.json").read_text()).get("status") == "reviewed" for x in (ROOT / "content").glob(f"*/{p}"))]
    ok = not problems
    review = folder / "review"; review.mkdir(exist_ok=True)
    body = [f"VERDICT: {'PASS' if ok else 'FAIL'}", f"CONTENT-HASH: {h}", "",
            f"Gate for {lid} on {datetime.date.today()}.", "", "Reviewers required: " + ", ".join(needed)]
    body += ["", "Checks run: " + (", ".join(ran) if ran else ("skipped" if skip_checks else "none (stopped earlier)"))]
    body += ["", "Problems:"] + ([f"{i}. {p}" for i, p in enumerate(problems, 1)] if problems else ["none"])
    if warn: body += ["", "Warnings:"] + [f"- {w}" for w in warn]
    (review / "gate.md").write_text("\n".join(body) + "\n")
    print("\n".join(body))
    if ok and publish:
        meta.pop("revision", None)
        meta.update({"status": "reviewed", "reviewed_by": GATE_NAME, "reviewed_on": str(datetime.date.today()), "reviewed_hash": h})
        (folder / "meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2) + "\n")
        with open(review / "history.log", "a") as log: log.write(f"{datetime.date.today()} {lid} PUBLISHED {h}\n")
        if not skip_checks:
            okb, out = run([sys.executable, str(SCRIPTS / "build.py")])
            print("\npublished: site/ rebuilt" if okb else f"\nBUILD FAILED after publishing: {out}")
            return 0 if okb else 1
        print("\npublished (build skipped)")
    return 0 if ok else 1


def log_round(lid):
    """One line per review round in review/history.log, written by the gate so it is never forgotten."""
    folder = find_lesson(lid)
    review = folder / "review"; review.mkdir(exist_ok=True)
    log = review / "history.log"
    previous = log.read_text().splitlines() if log.exists() else []
    n = sum(1 for l in previous if f" {lid} round " in l) + 1
    verdicts = []
    for r in REVIEWERS:
        if r == "tester" and not (folder / "sim.js").exists(): continue
        lines = report_lines(folder, r)
        v = "none" if not lines else lines[0].replace("VERDICT:", "").strip()
        if lines and content_hash(folder, r) != next((l.split(":", 1)[1].strip() for l in lines[:3] if l.startswith("CONTENT-HASH:")), "") != content_hash(folder):
            v += "(stale)"
        verdicts.append(f"{r}={v}")
    fixer = report_lines(folder, "fixer")
    if fixer: verdicts.append("fixer=" + fixer[0].replace("VERDICT:", "").strip())
    line = f"{datetime.date.today()} {lid} round {n}: " + " ".join(verdicts) + f" hash={content_hash(folder)}"
    with open(log, "a") as f: f.write(line + "\n")
    print(line)
    return 0


def verify():
    bad, notes = [], []
    for f in sorted((ROOT / "content").glob("*/*/meta.json")):
        if f.parent.parent.name == "_gold": continue
        meta = json.loads(f.read_text())
        if meta.get("status") != "reviewed": continue
        if not meta.get("reviewed_hash"):
            notes.append(f"{meta['id']}: published by {meta.get('reviewed_by') or 'hand'} without a reviewed_hash, so edits to it are not detected")
            continue
        rev = meta.get("revision")
        if rev:                                   # source under revision: the live page must still be the reviewed render
            if site_hash(meta["id"]) != rev.get("site_hash"):
                bad.append(f"{meta['id']}: under revision, but its live page changed without the gate (restore site/{meta['id']}.html or publish through the gate)")
            else:
                notes.append(f"{meta['id']}: under revision since {rev.get('opened')}; the live page is still the reviewed render")
        elif meta["reviewed_hash"] != content_hash(f.parent):
            bad.append(f"{meta['id']}: edited after it was published (re-run the review and the gate, or run `gate.py {meta['id']} --reopen` to revise it)")
    print("\n".join(bad + notes) if bad or notes else "all published lessons match their recorded hash")
    return 1 if bad else 0


if __name__ == "__main__":
    a = sys.argv[1:]
    if "--verify" in a: sys.exit(verify())
    if "--hash" in a:
        folder = find_lesson(a[a.index("--hash") + 1])
        who = a[a.index("--for") + 1] if "--for" in a else None
        if who and who not in DOMAINS: sys.exit(f"unknown reviewer {who!r}; one of {', '.join(DOMAINS)}")
        print(content_hash(folder, who)); sys.exit(0)
    ids = [x for x in a if not x.startswith("--")]
    if len(ids) != 1: sys.exit(__doc__)
    if "--log-round" in a: sys.exit(log_round(ids[0]))
    if "--reopen" in a: sys.exit(reopen(ids[0]))
    sys.exit(gate(ids[0], "--publish" in a, "--skip-checks" in a))
