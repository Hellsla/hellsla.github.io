"""Tests for scripts/reviews.py and the publishing rule in scripts/build.py. Usage: python scripts/test_reviews.py
Copies a lesson into a temporary project and checks the hash, the review states and what the build publishes."""
import json, os, pathlib, shutil, subprocess, sys, tempfile
HERE = pathlib.Path(__file__).resolve().parent
SRC = HERE.parent
LESSON = "fy3-3"
failures = []


def snapshot():
    paths = sorted((SRC / "content/FY3" / LESSON).rglob("*")) + [SRC / "tests/sims" / f"{LESSON}.json"]
    return {str(p): p.read_bytes() for p in paths if p.is_file()}
REAL = snapshot()


def project():
    tmp = pathlib.Path(tempfile.mkdtemp())
    (tmp / "content/FY3").mkdir(parents=True); (tmp / "tests/sims").mkdir(parents=True)
    shutil.copytree(SRC / "content/FY3" / LESSON, tmp / "content/FY3" / LESSON, ignore=shutil.ignore_patterns("review"))
    for f in ("glossary.json", "curriculum.json", "CLAUDE.md", "NOTES.md"): shutil.copy(SRC / f, tmp / f)
    shutil.copytree(SRC / "content/_gold", tmp / "content/_gold")
    shutil.copy(SRC / "tests/sims" / f"{LESSON}.json", tmp / "tests/sims")
    shutil.copytree(SRC / "scripts", tmp / "scripts", ignore=shutil.ignore_patterns("__pycache__"))
    shutil.copytree(SRC / "templates", tmp / "templates")
    return tmp


def run(tmp, script, *args):
    r = subprocess.run([sys.executable, str(tmp / "scripts" / script), *args], capture_output=True, text=True, cwd=tmp)
    return r.returncode, r.stdout + r.stderr


def h(tmp, lid=LESSON): return run(tmp, "reviews.py", "hash", lid)[1].strip()
def state(tmp, lid=LESSON): return run(tmp, "reviews.py", "status", lid)[1].strip()


def report(tmp, name, verdict="PASS", hash_=None, lid=LESSON):
    d = tmp / "content/FY3" / lid / "review"; d.mkdir(exist_ok=True)
    (d / f"{name}.md").write_text(f"VERDICT: {verdict}\nCONTENT-HASH: {hash_ or h(tmp, lid)}\n\n## Blocking\nnone\n")


def expect(name, cond, detail=""):
    print(("ok   " if cond else "FAIL ") + name + ("" if cond else f"  -> {detail[:400]}"))
    if not cond: failures.append(name)


# 1. formatting does not change the hash, content does
t = project(); L = t / "content/FY3" / LESSON; before = h(t)
p = L / "lesson.md"; p.write_text(p.read_text().replace("\n\n", "\n\n\n", 3).replace("\n", " \t\n", 5).replace("\n", "\r\n", 3) + "\n\n\n")
expect("blank lines, trailing spaces and CRLF keep the hash", h(t) == before)
e = L / "exercises.json"; e.write_text(json.dumps(json.loads(e.read_text()), indent=4, ensure_ascii=False))
expect("JSON re-indent keeps the hash", h(t) == before)
s = L / "sim.js"; s.write_text(s.read_text().replace(";\n", ";  \n", 3) + "\n\n")
expect("sim.js trailing spaces keep the hash", h(t) == before)
p.write_text(p.read_text().replace("\n- ", "\n  - ", 1))
expect("an indentation change alters the hash (Markdown nesting)", h(t) != before); before = h(t)
p.write_text(p.read_text().replace(" on ", "  on ", 1))
expect("a double space inside a line alters the hash", h(t) != before); before = h(t)
p.write_text(p.read_text().replace("lämpötila", "lämpötilat", 1))
expect("a word change alters the hash", h(t) != before); after_word = h(t)
ex = json.loads(e.read_text()); ex["level1"][0]["answer"] = ex["level1"][0]["answer"] + 1; e.write_text(json.dumps(ex, ensure_ascii=False))
expect("a number change alters the hash", h(t) != after_word); after_num = h(t)
s.write_text(s.read_text() + "\n// kommentti\n")
expect("a sim.js line alters the hash", h(t) != after_num)

# 2. review states
t = project()
expect("no reports: draft", "draft" in state(t) and "science=missing" in state(t), state(t))
report(t, "science"); report(t, "pedagogy")
expect("both PASS on the current hash: reviewed", ": reviewed" in state(t), state(t))
report(t, "pedagogy", "FAIL")
expect("one FAIL: draft", ": draft" in state(t) and "pedagogy=FAIL" in state(t), state(t))
report(t, "pedagogy")
p = t / "content/FY3" / LESSON / "lesson.md"; p.write_text(p.read_text() + "\nUusi lause.\n")
expect("content edit after review: draft, both stale", ": draft" in state(t) and "science=stale" in state(t) and "pedagogy=stale" in state(t), state(t))
p.write_text(p.read_text().rstrip("\n") + "   \n\n\n")
expect("formatting after review: still stale, not re-validated by whitespace", "science=stale" in state(t), state(t))
code, out = run(t, "reviews.py", "legacy", LESSON)
expect("legacy marker: legacy", code == 0 and ": legacy" in state(t), out + state(t))
p.write_text(p.read_text() + "Sisältömuutos.\n")
expect("content edit retires the legacy marker: draft", ": draft" in state(t) and "legacy=stale" in state(t), state(t))
report(t, "science"); report(t, "pedagogy")
code, out = run(t, "reviews.py", "legacy", LESSON)
expect("a reviewed lesson refuses a legacy marker", code != 0, out)
(t / "content/FY3" / LESSON / "review/science.md").write_text("PASS\n")
code, out = run(t, "reviews.py", "verify")
expect("malformed report fails verify", code == 1 and "VERDICT" in out, out)

# 3. what the build publishes
def build(tmp): return run(tmp, "build.py")
t = project(); site = t / "site"
code, out = build(t)
expect("draft is not built", code == 0 and not (site / f"{LESSON}.html").exists() and "skipped" not in out and f'href="{LESSON}.html"' not in (site / "FY3.html").read_text(), out)
report(t, "science"); report(t, "pedagogy"); code, out = build(t); page = (site / f"{LESSON}.html").read_text()
expect("reviewed lesson is built without a notice", code == 0 and "Prototyyppiversio" not in page and f'href="{LESSON}.html"' in (site / "FY3.html").read_text(), out)
p = t / "content/FY3" / LESSON / "lesson.md"; p.write_text(p.read_text() + "\nMuutos.\n"); run(t, "reviews.py", "legacy", LESSON)
code, out = build(t); page = (site / f"{LESSON}.html").read_text()
expect("legacy lesson is built with the prototype notice", code == 0 and "Prototyyppiversio" in page and "prototyyppi" in (site / "FY3.html").read_text(), out)
p.write_text(p.read_text() + "\nToinen muutos.\n")
code, out = build(t)
expect("stale lesson is removed from the site with a warning", code == 0 and not (site / f"{LESSON}.html").exists() and ("WARNING" in out or "::warning::" in out) and LESSON in out and "removes it" in out, out)   # ::warning:: on CI

# 4. atomic build: a build that fails half-way leaves the previous site untouched
t = project(); report(t, "science"); report(t, "pedagogy"); build(t); site = t / "site"
before = {q.name: q.read_bytes() for q in site.glob("*.html")}
other = t / "content/FY3/fy3-9z"; shutil.copytree(t / "content/FY3" / LESSON, other, ignore=shutil.ignore_patterns("review"))
md = json.loads((other / "meta.json").read_text()); md["id"] = "fy3-9z"; (other / "meta.json").write_text(json.dumps(md, ensure_ascii=False))
(other / "exercises.json").write_text("{ rikki")
report(t, "science", lid="fy3-9z"); report(t, "pedagogy", lid="fy3-9z")      # reviewed, so the build tries to render it, and crashes
code, out = build(t); after = {q.name: q.read_bytes() for q in site.glob("*.html")}
expect("failed build leaves the previous site complete", code != 0 and after == before and not (t / "site.tmp").exists() and not (t / "site.old").exists(), out)

# 5. scope: full or delta review from git history
def git(tmp, *a): return subprocess.run(["git", *a], cwd=tmp, capture_output=True, text=True).stdout
t = project(); git(t, "init", "-q"); git(t, "config", "user.email", "t@t"); git(t, "config", "user.name", "t"); git(t, "add", "."); git(t, "commit", "-qm", "v1")
code, out = run(t, "reviews.py", "scope", LESSON)
expect("scope without reports: full", "science: full" in out and "no earlier PASS" in out, out)
report(t, "science"); report(t, "pedagogy")
code, out = run(t, "reviews.py", "scope", LESSON)
expect("scope right after a PASS: delta with no changes", "science: delta (0 changed wording" in out and "pedagogy: delta" in out, out)
p = t / "content/FY3" / LESSON / "lesson.md"; p.write_text(p.read_text().replace("lämpötila", "lämpötilat", 1))
code, out = run(t, "reviews.py", "scope", LESSON)
expect("one word changed, no number: delta for both", out.count("delta") == 2 and "wording" in out, out)
e = t / "content/FY3" / LESSON / "exercises.json"; ex = json.loads(e.read_text()); ex["level1"][0]["answer"] += 1; e.write_text(json.dumps(ex, ensure_ascii=False, indent=2))
code, out = run(t, "reviews.py", "scope", LESSON)
expect("an answer changed: full for both", out.count("full") == 2 and "answer" in out, out)
e.write_text(json.dumps(json.loads((SRC / "content/FY3" / LESSON / "exercises.json").read_text()), ensure_ascii=False, indent=2))
p.write_text(p.read_text().replace("0{,}37", "0{,}38", 1))
code, out = run(t, "reviews.py", "scope", LESSON)
expect("a number in a formula changed: full", out.count("full") == 2 and "number, formula" in out, out)
p.write_text(p.read_text().replace("0{,}38", "0{,}37", 1)); s_ = t / "content/FY3" / LESSON / "sim.js"; s_.write_text(s_.read_text() + "\n// yksi rivi\n")
code, out = run(t, "reviews.py", "scope", LESSON)
expect("one line of sim.js changed: full", out.count("full") == 2 and "sim.js changed" in out, out)
# 6. packets: what each role receives
t = project(); git(t, "init", "-q"); git(t, "config", "user.email", "t@t"); git(t, "config", "user.name", "t"); git(t, "add", "."); git(t, "commit", "-qm", "v1")
code, out = run(t, "review_packet.py", LESSON, "--role", "science"); ps = (t / "content/FY3" / LESSON / "review/packet-science.md").read_text()
expect("science packet: full, with answers.py and sim.js, without curriculum.json", code == 0 and "### exercises.json" in ps and "### sim.js" in ps and '"FY1": {' not in ps and "Role: **science**" in ps, out)   # the slot only, not curriculum.json
code, out = run(t, "review_packet.py", LESSON, "--role", "pedagogy"); pp = (t / "content/FY3" / LESSON / "review/packet-pedagogy.md").read_text()
expect("pedagogy packet: figures collapsed, no answers.py, no sim.js", "figure body omitted" in pp and "### answers.py" not in pp and "### sim.js" not in pp and "Screenshots" in pp, out)
expect("packets carry the slot, the glossary terms and the conventions", "Curriculum slot" in ps and "Glossary terms" in ps and "Physics and maths conventions" in ps)
report(t, "science"); report(t, "pedagogy"); p = t / "content/FY3" / LESSON / "lesson.md"; p.write_text(p.read_text().replace("lämpötila", "lämpötilat", 1))
code, out = run(t, "review_packet.py", LESSON, "--role", "science"); ps = (t / "content/FY3" / LESSON / "review/packet-science.md").read_text()
expect("delta packet: previous report and the diff, not the whole lesson", "Mode: **delta**" in ps and "Your previous report" in ps and "+" in ps.split("```diff")[1] and "### answers.py" not in ps, out)
code, out = run(t, "review_packet.py", LESSON, "--role", "developer", "--fix"); pd = (t / "content/FY3" / LESSON / "review/packet-developer.md").read_text()
expect("developer fix packet: both reports and the lesson files", "Findings to resolve" in pd and "### science" in pd and "### lesson.md" in pd and "1. Maths in LaTeX" in pd, out)
expect("usage report runs", run(t, "usage.py", "log", LESSON, "--agent", "x", "--model", "sonnet", "--effort", "medium", "--mode", "full", "--round", "1", "--tokens", "100", "--seconds", "1", "--calls", "1", "--verdict", "PASS")[0] == 0 and "baseline" in run(t, "usage.py", "report", LESSON)[1])
expect("real project untouched", snapshot() == REAL)
print("\n" + ("all review tests passed" if not failures else f"{len(failures)} FAILED: " + ", ".join(failures)))
sys.exit(1 if failures else 0)
