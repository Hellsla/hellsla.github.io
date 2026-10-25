"""Tests for scripts/gate.py. Usage: python scripts/test_gate.py
Copies a lesson into a temporary project root and checks that the gate opens only when it should."""
import json, os, pathlib, shutil, subprocess, sys, tempfile
HERE = pathlib.Path(__file__).resolve().parent
SRC = HERE.parent
LESSON = "fy3-3"
failures = []

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
expect("verify: human-reviewed lesson is not hash-checked", gate(t, "--verify")[0] == 0)
# 11. status fields do not affect the hash
t = project(); before = h(t); m = t / "content/FY3" / LESSON / "meta.json"; md = json.loads(m.read_text()); md["status"] = "reviewed"; md["reviewed_on"] = "2030-01-01"; m.write_text(json.dumps(md, ensure_ascii=False))
expect("status fields excluded from hash", h(t) == before)
# 12. running the gate under FYSIIKKALABRA_ROOT never changes the real project
def snapshot():
    return {str(f.relative_to(SRC)): f.read_bytes() for f in sorted((SRC / "content").rglob("*")) if f.is_file()}
before = snapshot()
t = project(); reports(t); gate(t, LESSON, "--publish"); gate(t, "--verify")
expect("real project untouched", snapshot() == before)
print("\n" + ("all gate tests passed" if not failures else f"{len(failures)} FAILED: " + ", ".join(failures)))
sys.exit(1 if failures else 0)
