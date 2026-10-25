"""Tests for scripts/gate.py. Usage: python scripts/test_gate.py
Copies a lesson into a temporary project root and checks that the gate opens only when it should."""
import json, os, pathlib, shutil, subprocess, sys, tempfile
HERE = pathlib.Path(__file__).resolve().parent
SRC = HERE.parent
LESSON = "fy3-3"
failures = []

def snapshot():
    """Content of every file the gate could touch in the real project, to prove the tests never write there."""
    paths = sorted((SRC / "content/FY3" / LESSON).rglob("*")) + [SRC / "tests/sims" / f"{LESSON}.json", SRC / "glossary.json", SRC / "curriculum.json"]
    return {str(p): p.read_bytes() for p in paths if p.is_file()}
REAL = snapshot()

def project():
    tmp = pathlib.Path(tempfile.mkdtemp())
    (tmp / "content/FY3").mkdir(parents=True)
    shutil.copytree(SRC / "content/FY3" / LESSON, tmp / "content/FY3" / LESSON, ignore=shutil.ignore_patterns("review"))
    (tmp / "tests/sims").mkdir(parents=True)
    for f in ("glossary.json", "curriculum.json"): shutil.copy(SRC / f, tmp / f)
    t = SRC / "tests/sims" / f"{LESSON}.json"
    if t.exists(): shutil.copy(t, tmp / "tests/sims" / t.name)
    shutil.copytree(SRC / "scripts", tmp / "scripts", ignore=shutil.ignore_patterns("__pycache__"))
    return tmp

def gate(tmp, *args):
    env = dict(os.environ, FYSIIKKALABRA_ROOT=str(tmp))
    r = subprocess.run([sys.executable, str(tmp / "scripts/gate.py"), *args, "--skip-checks"], capture_output=True, text=True, env=env)
    return r.returncode, r.stdout + r.stderr

def h(tmp):
    return subprocess.run([sys.executable, str(tmp / "scripts/gate.py"), "--hash", LESSON], capture_output=True, text=True, env=dict(os.environ, FYSIIKKALABRA_ROOT=str(tmp))).stdout.strip()

def reports(tmp, verdict="PASS", hash_=None, skip=()):
    d = tmp / "content/FY3" / LESSON / "review"; d.mkdir(exist_ok=True)
    for r in ["tester", "physics-expert", "mathematician", "educator", "proofreader", "editor", "web-designer"]:
        if r in skip: continue
        (d / f"{r}.md").write_text(f"VERDICT: {verdict}\nCONTENT-HASH: {hash_ or h(tmp)}\n\nfindings\n")

def expect(name, cond, detail=""):
    print(("ok   " if cond else "FAIL ") + name + ("" if cond else f"  -> {detail[:300]}"))
    if not cond: failures.append(name)

# 1. no reports: gate stays closed
t = project(); code, out = gate(t, LESSON); expect("no reports: closed", code == 1 and "no report" in out, out)
# 2. all PASS for the current hash: gate opens and publish sets the status
t = project(); reports(t); code, out = gate(t, LESSON, "--publish")
meta = json.loads((t / "content/FY3" / LESSON / "meta.json").read_text())
expect("all PASS on current hash: open", code == 0, out)
expect("publish sets status, reviewer and hash", meta["status"] == "reviewed" and meta["reviewed_by"].startswith("gate") and meta["reviewed_hash"] == h(t), str(meta))
expect("publishing does not change the content hash", h(t) == meta["reviewed_hash"])
expect("verify passes after publishing", gate(t, "--verify")[0] == 0)
# 3. a single FAIL blocks
t = project(); reports(t); r = t / "content/FY3" / LESSON / "review/educator.md"; r.write_text(r.read_text().replace("PASS", "FAIL"))
code, out = gate(t, LESSON); expect("one FAIL: closed", code == 1 and "educator" in out and "not PASS" in out, out)
# 4. stale hash blocks (lesson edited after the reviews)
t = project(); reports(t); p = t / "content/FY3" / LESSON / "lesson.md"; p.write_text(p.read_text() + "\nUusi lause.\n")
code, out = gate(t, LESSON); expect("edit after review: closed", code == 1 and "older version" in out, out)
# 5. missing hash line blocks
t = project(); reports(t); r = t / "content/FY3" / LESSON / "review/editor.md"; r.write_text("VERDICT: PASS\n\nno hash\n")
code, out = gate(t, LESSON); expect("report without hash: closed", code == 1 and "no CONTENT-HASH" in out, out)
# 6. one reviewer missing blocks
t = project(); reports(t, skip=("web-designer",)); code, out = gate(t, LESSON); expect("missing reviewer: closed", code == 1 and "web-designer: no report" in out, out)
# 7. broken exercises block even when every report passes
t = project(); reports(t); e = t / "content/FY3" / LESSON / "exercises.json"; ex = json.loads(e.read_text()); ex["level1"].pop(); e.write_text(json.dumps(ex, ensure_ascii=False))
code, out = gate(t, LESSON); expect("wrong exercise count: closed", code == 1 and "level1 has 4" in out, out)
# 8. missing solution blocks
t = project(); reports(t); s = t / "content/FY3" / LESSON / "solutions.md"; s.write_text(s.read_text().replace("## fy3-3-L3-03", "## other"))
code, out = gate(t, LESSON); expect("missing solution: closed", code == 1 and "no solution for fy3-3-L3-03" in out, out)
# 9. unknown glossary term blocks
t = project(); reports(t); m = t / "content/FY3" / LESSON / "meta.json"; md = json.loads(m.read_text()); md["glossary"].append("olematon"); m.write_text(json.dumps(md, ensure_ascii=False))
code, out = gate(t, LESSON); expect("unknown glossary term: closed", code == 1 and "olematon" in out, out)
# 10. verify catches an edit after publishing, and ignores human-published lessons
t = project(); reports(t); gate(t, LESSON, "--publish"); p = t / "content/FY3" / LESSON / "lesson.md"; p.write_text(p.read_text() + "\nMuutos.\n")
code, out = gate(t, "--verify"); expect("verify: edit after gate publish detected", code == 1 and "edited after" in out, out)
m = t / "content/FY3" / LESSON / "meta.json"; md = json.loads(m.read_text()); md["reviewed_by"] = "Hellsla"; m.write_text(json.dumps(md, ensure_ascii=False))
expect("verify: a hand-published lesson with a recorded hash is checked too", gate(t, "--verify")[0] == 1)
md.pop("reviewed_hash"); m.write_text(json.dumps(md, ensure_ascii=False))
code, out = gate(t, "--verify"); expect("verify: hand-published lesson without a hash only gets a note", code == 0 and "without a reviewed_hash" in out, out)
# 11. status fields do not affect the hash
t = project(); before = h(t); m = t / "content/FY3" / LESSON / "meta.json"; md = json.loads(m.read_text()); md["status"] = "reviewed"; md["reviewed_on"] = "2030-01-01"; m.write_text(json.dumps(md, ensure_ascii=False))
expect("status fields excluded from hash", h(t) == before)
# 12. the gate never writes into the real project when FYSIIKKALABRA_ROOT is set
expect("real project untouched", snapshot() == REAL, "a file under content/, tests/sims or the json indexes changed while the tests ran")

# 13. domain hashes: a report may carry the hash of the reviewer's own files
def dh(tmp, who):
    return subprocess.run([sys.executable, str(tmp / "scripts/gate.py"), "--hash", LESSON, "--for", who], capture_output=True, text=True, env=dict(os.environ, FYSIIKKALABRA_ROOT=str(tmp))).stdout.strip()
t = project(); reports(t)
d = t / "content/FY3" / LESSON / "review"
for r in ["tester", "physics-expert", "mathematician", "educator", "proofreader", "editor", "web-designer"]:
    (d / f"{r}.md").write_text(f"VERDICT: PASS\nCONTENT-HASH: {dh(t, r)}\n\nfindings\n")
code, out = gate(t, LESSON); expect("domain hashes accepted: open", code == 0, out)
# 14. editing sim.js invalidates the tester and the physics expert, not the educator or the mathematician
s = t / "content/FY3" / LESSON / "sim.js"; s.write_text(s.read_text() + "\n// muutos\n")
code, out = gate(t, LESSON)
expect("sim edit: tester and physics-expert stale", code == 1 and "tester: report is for an older" in out and "physics-expert: report is for an older" in out, out)
expect("sim edit: educator and mathematician still valid", "educator:" not in out and "mathematician:" not in out, out)
# 15. editing lesson.md keeps the tester's verdict
t = project(); reports(t)
for r in ["tester", "physics-expert", "mathematician", "educator", "proofreader", "editor", "web-designer"]:
    (t / "content/FY3" / LESSON / "review" / f"{r}.md").write_text(f"VERDICT: PASS\nCONTENT-HASH: {dh(t, r)}\n\nfindings\n")
p = t / "content/FY3" / LESSON / "lesson.md"; p.write_text(p.read_text() + "\nUusi lause.\n")
code, out = gate(t, LESSON); expect("lesson edit: tester still valid, editor stale", code == 1 and "tester:" not in out and "editor: report is for an older" in out, out)
# 16. --log-round appends one line with every verdict
t = project(); reports(t); (t / "content/FY3" / LESSON / "review/educator.md").write_text("VERDICT: FAIL\nCONTENT-HASH: x\n")
code, out = gate(t, LESSON, "--log-round"); log = (t / "content/FY3" / LESSON / "review/history.log").read_text()
expect("log-round writes verdicts", code == 0 and "round 1:" in log and "educator=FAIL(stale)" in log and "tester=PASS" in log, log)
gate(t, LESSON, "--log-round"); expect("log-round counts rounds", "round 2:" in (t / "content/FY3" / LESSON / "review/history.log").read_text())
# 17. --reopen: only a gate-published lesson with a live page can be reopened
t = project(); m = t / "content/FY3" / LESSON / "meta.json"; md = json.loads(m.read_text()); md["status"] = "draft"; md.pop("reviewed_hash", None); m.write_text(json.dumps(md, ensure_ascii=False))
code, out = gate(t, LESSON, "--reopen"); expect("reopen a draft: refused", code == 1 and "only a lesson the gate published" in out, out)
reports(t); gate(t, LESSON, "--publish")
code, out = gate(t, LESSON, "--reopen"); expect("reopen without a live page: refused", code == 1 and "missing" in out, out)
# 18. under revision the source may change: verify checks the live page instead and stays green
site = t / "site"; site.mkdir(); (site / f"{LESSON}.html").write_text("<p>julkaistu sivu</p>"); (site / f"{LESSON}-sim.js").write_text("// sim")
code, out = gate(t, LESSON, "--reopen"); expect("reopen a published lesson", code == 0 and "under revision" in out, out)
p = t / "content/FY3" / LESSON / "lesson.md"; p.write_text(p.read_text() + "\nMuokkaus julkaisun jälkeen.\n")
code, out = gate(t, "--verify"); expect("verify: source edits allowed under revision", code == 0 and "under revision since" in out, out)
expect("reopen is logged", "REOPENED" in (t / "content/FY3" / LESSON / "review/history.log").read_text())
# 19. ... but the live page may not change without the gate
(site / f"{LESSON}.html").write_text("<p>muutettu käsin</p>")
code, out = gate(t, "--verify"); expect("verify: live page changed under revision: red", code == 1 and "live page changed" in out, out)
(site / f"{LESSON}.html").write_text("<p>julkaistu sivu</p>")
# 20. the edited source cannot be published on the old reports (stale), and a fresh pass clears the revision
code, out = gate(t, LESSON, "--publish"); expect("under revision: stale reports keep the gate closed", code == 1 and "older version" in out, out)
reports(t); code, out = gate(t, LESSON, "--publish"); md = json.loads((t / "content/FY3" / LESSON / "meta.json").read_text())
expect("fresh reviews publish the revision and clear the flag", code == 0 and "revision" not in md and md["reviewed_hash"] == h(t), out)
expect("verify green after republish", gate(t, "--verify")[0] == 0)
# 21. the plain build keeps the live page of a lesson under revision and still lists it as published
t = project(); shutil.copytree(SRC / "templates", t / "templates"); reports(t); gate(t, LESSON, "--publish")
site = t / "site"; site.mkdir(); (site / f"{LESSON}.html").write_text("<p>julkaistu sivu</p>"); (site / f"{LESSON}-sim.js").write_text("// sim")
gate(t, LESSON, "--reopen"); p = t / "content/FY3" / LESSON / "lesson.md"; p.write_text(p.read_text() + "\nKesken.\n")
r = subprocess.run([sys.executable, str(t / "scripts/build.py")], capture_output=True, text=True, cwd=t)
expect("plain build keeps the live page", r.returncode == 0 and "kept " + LESSON in r.stdout and (site / f"{LESSON}.html").read_text() == "<p>julkaistu sivu</p>" and (site / f"{LESSON}-sim.js").read_text() == "// sim", r.stdout + r.stderr)
expect("plain build still lists it as published", f'href="{LESSON}.html"' in (site / "FY3.html").read_text())
# 22. reopen refuses a source that drifted after publication (the live page could not be certified)
t = project(); reports(t); gate(t, LESSON, "--publish"); site = t / "site"; site.mkdir(); (site / f"{LESSON}.html").write_text("<p>julkaistu</p>")
p = t / "content/FY3" / LESSON / "lesson.md"; p.write_text(p.read_text() + "\nMuokattu ennen avaamista.\n")
code, out = gate(t, LESSON, "--reopen"); expect("reopen a drifted source: refused", code == 1 and "edited after publication" in out, out)
# 23. the plain build refuses to render a drifted published lesson that is not under revision
shutil.copytree(SRC / "templates", t / "templates")
r = subprocess.run([sys.executable, str(t / "scripts/build.py")], capture_output=True, text=True, cwd=t)
expect("plain build refuses a drifted published lesson", r.returncode != 0 and "unreviewed" in (r.stdout + r.stderr) and (site / f"{LESSON}.html").read_text() == "<p>julkaistu</p>", r.stdout + r.stderr)
# 24. atomic build: a failure in the middle of the plain build leaves the previous complete site byte for byte
OTHER = "fy3-4"
def project_two():
    """Temporary project with two lessons and the templates, both marked reviewed (the second sorts after the first)."""
    t = project(); shutil.copytree(SRC / "templates", t / "templates")
    shutil.copytree(SRC / "content/FY3" / OTHER, t / "content/FY3" / OTHER, ignore=shutil.ignore_patterns("review"))
    for lid in (LESSON, OTHER):
        f = t / "content/FY3" / lid / "meta.json"; m = json.loads(f.read_text()); m["status"] = "reviewed"; m.pop("revision", None); m.pop("reviewed_hash", None)
        f.write_text(json.dumps(m, ensure_ascii=False, indent=2) + "\n")
    return t
def tree(d):
    return {str(f.relative_to(d)): f.read_bytes() for f in sorted(d.rglob("*")) if f.is_file()}
def leftovers(t): return [x.name for x in t.iterdir() if x.name.startswith((".site-build-", ".site-old"))]
def plain_build(t): return subprocess.run([sys.executable, str(t / "scripts/build.py")], capture_output=True, text=True, cwd=t)
t = project_two(); r = plain_build(t); good = tree(t / "site")
expect("plain build writes a complete site", r.returncode == 0 and "replaced atomically" in r.stdout and f"{LESSON}.html" in good and f"{OTHER}.html" in good and "index.html" in good, r.stdout + r.stderr)
expect("plain build leaves no temporary folder", not leftovers(t), str(leftovers(t)))
(t / "content/FY3" / OTHER / "exit-ticket.json").write_text("{ not json")       # fails after the first lesson was already rendered
r = plain_build(t)
expect("mid-build failure: build fails", r.returncode != 0 and f"built {LESSON}" in r.stdout, r.stdout + r.stderr)
expect("mid-build failure: previous complete site preserved", tree(t / "site") == good)
expect("mid-build failure: temporary folder removed", not leftovers(t), str(leftovers(t)))
(t / "content/FY3" / OTHER / "exit-ticket.json").unlink()                       # a missing file skips the lesson; the build must still be complete or refuse
r = plain_build(t); expect("a skipped lesson never produces a half site", r.returncode == 0 and tree(t / "site").keys() >= {"index.html", f"{LESSON}.html"} and not leftovers(t), r.stdout + r.stderr)

# 25. publication status integrity: a failing publication build never leaves the lesson marked reviewed
PUB = "fy3-9"                                                  # lints clean as a draft, so the gate's own checks pass and only the build can fail
LESSON = PUB                                                      # the helpers above read this global
t = project(); shutil.copytree(SRC / "templates", t / "templates")
shutil.copytree(SRC / "content/FY3" / OTHER, t / "content/FY3" / OTHER, ignore=shutil.ignore_patterns("review"))
f = t / "content/FY3" / PUB / "meta.json"; m = json.loads(f.read_text())
for k in ("reviewed_by", "reviewed_on", "reviewed_hash", "revision"): m.pop(k, None)
m["status"] = "draft"; f.write_text(json.dumps(m, ensure_ascii=False, indent=2) + "\n"); reports(t)
g = t / "content/FY3" / OTHER / "meta.json"; m = json.loads(g.read_text()); m["status"] = "reviewed"; m["reviewed_hash"] = "0" * 16; m.pop("revision", None)
g.write_text(json.dumps(m, ensure_ascii=False, indent=2) + "\n")   # a published lesson edited without --reopen: the plain build refuses it
before_meta, before_site = f.read_bytes(), (tree(t / "site") if (t / "site").exists() else {})
def publish(t): return subprocess.run([sys.executable, str(t / "scripts/gate.py"), PUB, "--publish"], capture_output=True, text=True, env=dict(os.environ, FYSIIKKALABRA_ROOT=str(t)))
r = publish(t); log = t / "content/FY3" / PUB / "review/history.log"
expect("failed publication build: gate fails and says so", r.returncode == 1 and "PUBLISH FAILED" in r.stdout and "build --all: ok" in r.stdout, r.stdout + r.stderr)
expect("failed publication build: lesson is not marked reviewed", f.read_bytes() == before_meta and json.loads(f.read_text())["status"] == "draft", f.read_text())
expect("failed publication build: no PUBLISHED line in the history", not log.exists() or "PUBLISHED" not in log.read_text())
expect("failed publication build: site unchanged, nothing left over", (tree(t / "site") if (t / "site").exists() else {}) == before_site and not leftovers(t))
m = json.loads(g.read_text()); m.pop("reviewed_hash"); g.write_text(json.dumps(m, ensure_ascii=False, indent=2) + "\n")   # the cause is removed
r = publish(t)
expect("publication succeeds when the build succeeds", r.returncode == 0 and json.loads(f.read_text())["status"] == "reviewed" and (t / "site" / f"{PUB}.html").exists() and "PUBLISHED" in log.read_text(), r.stdout[-800:] + r.stderr)
LESSON = "fy3-3"
expect("real project untouched after the new tests", snapshot() == REAL)
print("\n" + ("all gate tests passed" if not failures else f"{len(failures)} FAILED: " + ", ".join(failures)))
sys.exit(1 if failures else 0)
