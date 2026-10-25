"""Publication gate: a lesson is published only when every reviewer has passed its CURRENT content.

  python scripts/gate.py --hash <id>              print the content hash of a lesson
  python scripts/gate.py <id>                     check only; exit 1 if the lesson is not publishable
  python scripts/gate.py <id> --publish           check, then set status "reviewed" and rebuild site/
  python scripts/gate.py --verify                 CI: every gate-published lesson still matches its recorded hash
  --skip-checks                                   (tests only) skip the latex, build and simulation runs

The content hash covers lesson.md, exercises.json, solutions.md, exit-ticket.json, sim.js, sim-spec.md,
tests/sims/<id>.json and meta.json without its status fields. Each reviewer report must start with
`VERDICT: PASS` and carry `CONTENT-HASH: <hash>` within its first three lines. Any edit to the lesson changes
the hash, so every reviewer has to pass again before the gate opens. The gate writes review/gate.md as its audit trail."""
import datetime, hashlib, json, os, pathlib, subprocess, sys

ROOT = pathlib.Path(os.environ.get("FYSIIKKALABRA_ROOT") or pathlib.Path(__file__).resolve().parents[1])
SCRIPTS = pathlib.Path(__file__).resolve().parent
REVIEWERS = ["tester", "physics-expert", "mathematician", "educator", "proofreader", "editor", "web-designer"]
HASHED = ["lesson.md", "exercises.json", "solutions.md", "exit-ticket.json", "sim.js", "sim-spec.md"]
STATUS_KEYS = ("status", "reviewed_by", "reviewed_on", "reviewed_hash")
GATE_NAME = "gate (automaattinen tarkistus)"


def find_lesson(lid):
    for f in sorted((ROOT / "content").glob(f"*/{lid}")):
        if f.parent.name != "_gold" and (f / "meta.json").exists(): return f
    sys.exit(f"no lesson folder for id {lid!r}")


def content_hash(folder):
    h = hashlib.sha256()
    lid = folder.name
    for name in HASHED:
        f = folder / name
        if f.exists(): h.update(name.encode() + b"\0" + f.read_bytes() + b"\0")
    meta = {k: v for k, v in json.loads((folder / "meta.json").read_text()).items() if k not in STATUS_KEYS}
    h.update(b"meta.json\0" + json.dumps(meta, sort_keys=True, ensure_ascii=False).encode() + b"\0")
    t = ROOT / "tests" / "sims" / f"{lid}.json"
    if t.exists(): h.update(b"test\0" + t.read_bytes() + b"\0")
    return h.hexdigest()[:16]


def check_report(folder, reviewer, want):
    f = folder / "review" / f"{reviewer}.md"
    if not f.exists(): return f"{reviewer}: no report"
    lines = f.read_text().splitlines()
    if not lines or lines[0].strip() != "VERDICT: PASS":
        return f"{reviewer}: verdict is not PASS ({lines[0].strip() if lines else 'empty report'})"
    got = next((l.split(":", 1)[1].strip() for l in lines[:3] if l.startswith("CONTENT-HASH:")), None)
    if got is None: return f"{reviewer}: report has no CONTENT-HASH line"
    if got != want: return f"{reviewer}: report is for an older version of the lesson (hash {got}, lesson {want})"
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
    r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
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
        for name, cmd in (("check_latex", [sys.executable, str(SCRIPTS / "check_latex.py"), str(folder)]),
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
        meta.update({"status": "reviewed", "reviewed_by": GATE_NAME, "reviewed_on": str(datetime.date.today()), "reviewed_hash": h})
        (folder / "meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2) + "\n")
        with open(review / "history.log", "a") as log: log.write(f"{datetime.date.today()} {lid} PUBLISHED {h}\n")
        if not skip_checks:
            okb, out = run([sys.executable, str(SCRIPTS / "build.py")])
            print("\npublished: site/ rebuilt" if okb else f"\nBUILD FAILED after publishing: {out}")
            return 0 if okb else 1
        print("\npublished (build skipped)")
    return 0 if ok else 1


def verify():
    bad = []
    for f in sorted((ROOT / "content").glob("*/*/meta.json")):
        if f.parent.parent.name == "_gold": continue
        meta = json.loads(f.read_text())
        if meta.get("status") != "reviewed" or not str(meta.get("reviewed_by", "")).startswith("gate"): continue
        if meta.get("reviewed_hash") != content_hash(f.parent):
            bad.append(f"{meta['id']}: edited after the gate published it (re-run the review and the gate)")
    print("\n".join(bad) if bad else "all gate-published lessons match their recorded hash")
    return 1 if bad else 0


if __name__ == "__main__":
    a = sys.argv[1:]
    if "--verify" in a: sys.exit(verify())
    if "--hash" in a: print(content_hash(find_lesson(a[a.index("--hash") + 1]))); sys.exit(0)
    ids = [x for x in a if not x.startswith("--")]
    if len(ids) != 1: sys.exit(__doc__)
    sys.exit(gate(ids[0], "--publish" in a, "--skip-checks" in a))
