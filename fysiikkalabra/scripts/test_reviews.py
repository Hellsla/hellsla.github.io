"""Tests for scripts/reviews.py and the publishing rule in scripts/build.py. Usage: python scripts/test_reviews.py
Copies a lesson into a temporary project and checks the hash, the review states and what the build publishes, for the
lesson and for its exercise set (reviewed apart since 2026-10-28), and the carry-over of reviews passed before the split."""
import json, os, pathlib, re, shutil, subprocess, sys, tempfile
HERE = pathlib.Path(__file__).resolve().parent
SRC = HERE.parent
LESSON = "fy3-3"
failures = []


def snapshot():
    paths = sorted((SRC / "content/fi/FY3" / LESSON).rglob("*")) + sorted((SRC / "lessons/FY3" / LESSON).rglob("*")) + [SRC / "tests/sims" / f"{LESSON}.json"]
    return {str(p): p.read_bytes() for p in paths if p.is_file()}
REAL = snapshot()


def project():
    tmp = pathlib.Path(tempfile.mkdtemp())
    (tmp / "content/fi/FY3").mkdir(parents=True); (tmp / "tests/sims").mkdir(parents=True)
    shutil.copytree(SRC / "content/fi/FY3" / LESSON, tmp / "content/fi/FY3" / LESSON, ignore=shutil.ignore_patterns("review"))
    shutil.copytree(SRC / "lessons/FY3" / LESSON, tmp / "lessons/FY3" / LESSON, ignore=shutil.ignore_patterns("__pycache__"))
    for f in ("glossary.json", "curriculum.json", "competencies.json", "CLAUDE.md", "NOTES.md"): shutil.copy(SRC / f, tmp / f)
    shutil.copytree(SRC / "content/_gold", tmp / "content/_gold")
    shutil.copy(SRC / "tests/sims" / f"{LESSON}.json", tmp / "tests/sims")
    shutil.copytree(SRC / "scripts", tmp / "scripts", ignore=shutil.ignore_patterns("__pycache__"))
    shutil.copytree(SRC / "templates", tmp / "templates")
    shutil.copytree(SRC / "lang", tmp / "lang")
    shutil.copytree(SRC / "assets/pics/fy3", tmp / "assets/pics/fy3")  # the lesson's photographs and their credits (photos.json)
    return tmp


def run(tmp, script, *args):
    r = subprocess.run([sys.executable, str(tmp / "scripts" / script), *args], capture_output=True, text=True, cwd=tmp)
    return r.returncode, r.stdout + r.stderr


def h(tmp, lid=LESSON, part="lesson"): return run(tmp, "reviews.py", "hash", lid, *(["--exercises"] if part == "exercises" else []))[1].strip()
def state(tmp, lid=LESSON, part="lesson"):
    """The lesson's half of `reviews.py status` (`fy3-3: reviewed (...)`), or the exercise set's (`exercises: draft (...)`)."""
    lesson, _, ex = run(tmp, "reviews.py", "status", lid)[1].strip().partition("; exercises: ")
    return lesson if part == "lesson" else "exercises: " + ex


def report(tmp, name, verdict="PASS", hash_=None, lid=LESSON, part="lesson"):
    d = tmp / "content/fi/FY3" / lid / ("review" if part == "lesson" else "exercises/review"); d.mkdir(parents=True, exist_ok=True)
    (d / f"{name}.md").write_text(f"VERDICT: {verdict}\nCONTENT-HASH: {hash_ or h(tmp, lid, part)}\n\n## Blocking\nnone\n")


def expect(name, cond, detail=""):
    print(("ok   " if cond else "FAIL ") + name + ("" if cond else f"  -> {detail[:400]}"))
    if not cond: failures.append(name)


# 1. formatting does not change the hash, content does
t = project(); L = t / "content/fi/FY3" / LESSON; before = h(t)
p = L / "lesson.md"; p.write_text(p.read_text().replace("\n\n", "\n\n\n", 3).replace("\n", " \t\n", 5).replace("\n", "\r\n", 3) + "\n\n\n")
expect("blank lines, trailing spaces and CRLF keep the hash", h(t) == before)
e = L / "exercises/exercises.json"; ex_before = h(t, part="exercises"); e.write_text(json.dumps(json.loads(e.read_text()), indent=4, ensure_ascii=False))
expect("JSON re-indent keeps the hash", h(t) == before and h(t, part="exercises") == ex_before)
s = t / "lessons/FY3" / LESSON / "sim.js"; s.write_text(s.read_text().replace(";\n", ";  \n", 3) + "\n\n")
expect("sim.js trailing spaces keep the hash", h(t) == before)
p.write_text(p.read_text().replace("\n- ", "\n  - ", 1))
expect("an indentation change alters the hash (Markdown nesting)", h(t) != before); before = h(t)
p.write_text(p.read_text().replace(" on ", "  on ", 1))
expect("a double space inside a line alters the hash", h(t) != before); before = h(t)
p.write_text(p.read_text().replace("lämpötila", "lämpötilat", 1))
expect("a word change alters the hash", h(t) != before); after_word = h(t)
expect("a lesson edit leaves the exercise set's hash alone", h(t, part="exercises") == ex_before)
ex = json.loads(e.read_text()); ex["level1"][0]["answer"] = ex["level1"][0]["answer"] + 1; e.write_text(json.dumps(ex, ensure_ascii=False))
expect("an exercise's number alters the exercise set's hash, not the lesson's", h(t, part="exercises") != ex_before and h(t) == after_word); after_num = h(t)
a_ = t / "lessons/FY3" / LESSON / "answers.py"; a_.write_text(a_.read_text().replace("\nprint(", "\nyksi = 1\nprint(", 1))
expect("answers.py belongs to the exercise set", h(t) == after_word and h(t, part="exercises") not in (ex_before, ""))
s.write_text(s.read_text() + "\n// kommentti\n")
expect("a sim.js line alters the hash", h(t) != after_num)

# 2. review states
t = project()
expect("no reports: draft", "draft" in state(t) and "science=missing" in state(t), state(t))
report(t, "science"); report(t, "pedagogy"); report(t, "visual")
expect("both PASS on the current hash: reviewed", ": reviewed" in state(t), state(t))
expect("the lesson's reports do not review its exercises", "exercises: draft (science=missing, pedagogy=missing, visual=missing)" in state(t, part="exercises"), state(t, part="exercises"))
report(t, "science", part="exercises"); report(t, "pedagogy", part="exercises"); report(t, "visual", part="exercises")
expect("the exercise set's own two PASS reports: reviewed", "exercises: reviewed" in state(t, part="exercises"), state(t, part="exercises"))
e = t / "content/fi/FY3" / LESSON / "exercises/exercises.json"; ex = json.loads(e.read_text()); ex["level2"][0]["text"] += " Lisälause."; e.write_text(json.dumps(ex, ensure_ascii=False))
expect("an exercise edited: the exercises stale, the lesson still reviewed", ": reviewed" in state(t) and "exercises: draft (science=stale" in state(t, part="exercises"), state(t) + state(t, part="exercises"))
e.write_text((SRC / "content/fi/FY3" / LESSON / "exercises/exercises.json").read_text())
report(t, "pedagogy", "FAIL")
expect("one FAIL: draft", ": draft" in state(t) and "pedagogy=FAIL" in state(t), state(t))
report(t, "pedagogy")
p = t / "content/fi/FY3" / LESSON / "lesson.md"; p.write_text(p.read_text() + "\nUusi lause.\n")
expect("content edit after review: draft, both stale", ": draft" in state(t) and "science=stale" in state(t) and "pedagogy=stale" in state(t), state(t))
p.write_text(p.read_text().rstrip("\n") + "   \n\n\n")
expect("formatting after review: still stale, not re-validated by whitespace", "science=stale" in state(t), state(t))
code, out = run(t, "reviews.py", "legacy", LESSON)
expect("legacy marker: legacy", code == 0 and ": legacy" in state(t), out + state(t))
p.write_text(p.read_text() + "Sisältömuutos.\n")
expect("content edit retires the legacy marker: draft", ": draft" in state(t) and "legacy=stale" in state(t), state(t))
report(t, "science"); report(t, "pedagogy"); report(t, "visual")
code, out = run(t, "reviews.py", "legacy", LESSON)
expect("a reviewed lesson refuses a legacy marker", code != 0, out)
(t / "content/fi/FY3" / LESSON / "review/science.md").write_text("PASS\n")
code, out = run(t, "reviews.py", "verify")
expect("malformed report fails verify", code == 1 and "VERDICT" in out, out)

# 3. what the build publishes
def build(tmp): return run(tmp, "build.py")
t = project(); site = t / "site"
code, out = build(t)
expect("draft is not built", code == 0 and not (site / f"{LESSON}.html").exists() and "skipped" not in out and f'href="{LESSON}.html"' not in (site / "FY3.html").read_text(), out)
report(t, "science"); report(t, "pedagogy"); report(t, "visual"); code, out = build(t); page = (site / f"{LESSON}.html").read_text()
expect("reviewed lesson is built without a notice", code == 0 and "Prototyyppiversio" not in page and f'href="{LESSON}.html"' in (site / "FY3.html").read_text(), out)
expect("its exercises, never reviewed, are not on the page: a note says they are coming", f'id="{LESSON}-L1-01"' not in page and "tarkastettavina" in page and "no version has passed yet" in out, out)
report(t, "science", part="exercises"); report(t, "pedagogy", part="exercises"); report(t, "visual", part="exercises"); code, out = build(t); page = (site / f"{LESSON}.html").read_text()
expect("reviewed exercises are on the page with their solutions", code == 0 and f'id="{LESSON}-L1-01"' in page and "tarkastettavina" not in page and 'class="solution"' in page, out)
p = t / "content/fi/FY3" / LESSON / "lesson.md"; p.write_text(p.read_text() + "\nMuutos.\n"); run(t, "reviews.py", "legacy", LESSON)
code, out = build(t); page = (site / f"{LESSON}.html").read_text()
expect("legacy lesson is built with the prototype notice", code == 0 and "Prototyyppiversio" in page and "prototyyppi" in (site / "FY3.html").read_text(), out)
p.write_text(p.read_text() + "\nToinen muutos.\n")
code, out = build(t)
expect("stale lesson is removed from the site with a warning", code == 0 and not (site / f"{LESSON}.html").exists() and ("WARNING" in out or "::warning::" in out) and LESSON in out and "removes it" in out, out)   # ::warning:: on CI

# 4. atomic build: a build that fails half-way leaves the previous site untouched
t = project(); report(t, "science"); report(t, "pedagogy"); report(t, "visual"); build(t); site = t / "site"
before = {q.name: q.read_bytes() for q in site.glob("*.html")}
other = t / "content/fi/FY3/fy3-9z"; shutil.copytree(t / "content/fi/FY3" / LESSON, other, ignore=shutil.ignore_patterns("review"))
md = json.loads((other / "meta.json").read_text()); md["id"] = "fy3-9z"; (other / "meta.json").write_text(json.dumps(md, ensure_ascii=False))
(other / "exercises/exercises.json").write_text("{ rikki")
report(t, "science", lid="fy3-9z"); report(t, "pedagogy", lid="fy3-9z"); report(t, "visual", lid="fy3-9z")      # reviewed, so the build tries to render it, and crashes
code, out = build(t); after = {q.name: q.read_bytes() for q in site.glob("*.html")}
expect("failed build leaves the previous site complete", code != 0 and after == before and not (t / "site.tmp").exists() and not (t / "site.old").exists(), out)

# 5. scope: full or delta review from git history
def git(tmp, *a): return subprocess.run(["git", *a], cwd=tmp, capture_output=True, text=True).stdout
t = project(); git(t, "init", "-q"); git(t, "config", "user.email", "t@t"); git(t, "config", "user.name", "t"); git(t, "add", "."); git(t, "commit", "-qm", "v1")
code, out = run(t, "reviews.py", "scope", LESSON)
expect("scope without reports: full", "science: full" in out and "no earlier PASS" in out, out)
report(t, "science"); report(t, "pedagogy"); report(t, "visual")
code, out = run(t, "reviews.py", "scope", LESSON)
expect("scope right after a PASS: delta with no changes", "science: delta (0 changed wording" in out and "pedagogy: delta" in out, out)
p = t / "content/fi/FY3" / LESSON / "lesson.md"; p.write_text(p.read_text().replace("lämpötila", "lämpötilat", 1))
code, out = run(t, "reviews.py", "scope", LESSON)
expect("one word changed, no number: delta for all three (the visual reviewer reads the edited sentence)", out.count("delta") == 3 and "wording" in out, out)
p.write_text((SRC / "content/fi/FY3" / LESSON / "lesson.md").read_text())
report(t, "science", part="exercises"); report(t, "pedagogy", part="exercises"); report(t, "visual", part="exercises")
e = t / "content/fi/FY3" / LESSON / "exercises/exercises.json"; ex = json.loads(e.read_text()); ex["level1"][0]["answer"] += 1; e.write_text(json.dumps(ex, ensure_ascii=False, indent=2))
code, out = run(t, "reviews.py", "scope", LESSON, "--exercises")
expect("an answer changed: science and pedagogy review the diff (delta, teacher 2026-11-16)", "science: delta" in out and "pedagogy: delta" in out and "answer" in out, out)
code, out = run(t, "reviews.py", "scope", LESSON)
expect("... and the lesson's reviewers see no change", "science: delta (0 changed" in out and "pedagogy: delta (0 changed" in out, out)
e.write_text(json.dumps(json.loads((SRC / "content/fi/FY3" / LESSON / "exercises/exercises.json").read_text()), ensure_ascii=False, indent=2))
p.write_text(p.read_text().replace("0{,}37", "0{,}38", 1))
code, out = run(t, "reviews.py", "scope", LESSON)
expect("a number in a formula changed: science and pedagogy delta (teacher 2026-11-16)", "science: delta" in out and "pedagogy: delta" in out and "number, formula" in out and "categories=numbers" in out, out)
p.write_text(p.read_text().replace("0{,}38", "0{,}37", 1)); s_ = t / "lessons/FY3" / LESSON / "sim.js"; s_.write_text(s_.read_text() + "\n// yksi rivi\n")
code, out = run(t, "reviews.py", "scope", LESSON)
expect("a comment line in sim.js: no review for any of the three, it is not content", "science: none" in out and "pedagogy: none" in out and "visual: none" in out and "comments" in out, out)
s_.write_text(s_.read_text() + "const yksi = 1;\n")
code, out = run(t, "reviews.py", "scope", LESSON)
expect("one line of sim.js code: full for both", "science: full" in out and "pedagogy: full" in out and "simulation's code" in out, out)
s_.write_text((SRC / "lessons/FY3" / LESSON / "sim.js").read_text())
s_.write_text(s_.read_text().replace("p.text('$600\\\\,\\\\text{K}$', thx - 14", "p.text('$600\\\\,\\\\text{K}$', thx - 20", 1))
code, out = run(t, "reviews.py", "scope", LESSON)
expect("a sim's LaTeX canvas label nudged 6 units: science none, pedagogy delta", "science: none" in out and "pedagogy: delta" in out and "label" in out, out)
s_.write_text(s_.read_text().replace("p.textSize(ts(11)); p.text(", "p.textSize(ts(12)); p.text(", 1))
code, out = run(t, "reviews.py", "scope", LESSON)
expect("the same line with its text size changed too: full for both", "science: full" in out and "pedagogy: full" in out, out)
s_.write_text((SRC / "lessons/FY3" / LESSON / "sim.js").read_text())

# 5b. change categories decide who looks again; a PASS carries over only what its reviewer need not see
svg = [l for l in p.read_text().splitlines() if l.lstrip().startswith(("<text ", "<foreignObject ")) and ' x="' in l]   # labels are fig-tex foreignObjects since 2026-10-26
txt = svg[0]; nudged = re.sub(r' x="(-?[\d.]+)"', lambda m: f' x="{float(m.group(1)) + 6:g}"', txt, count=1)
p.write_text(p.read_text().replace(txt, nudged, 1))
code, out = run(t, "reviews.py", "scope", LESSON)
expect("a figure label nudged 6 units: science none, pedagogy and visual delta", "science: none" in out and "pedagogy: delta" in out and "visual: delta" in out and "label" in out, out)
code, out = run(t, "reviews.py", "carry", LESSON)
expect("carry records science only; the lesson stays a draft until pedagogy looks", "science: carried over" in out and ": draft" in out and "science=PASS (carried over: label-position)" in out, out)
report(t, "pedagogy"); report(t, "visual")      # the nudged label: the visual reviewer looks (delta), the science PASS carries
expect("pedagogy and visual PASS on the new hash + science carried: reviewed", ": reviewed" in state(t) and "carried over" in state(t), state(t))
git(t, "add", "."); git(t, "commit", "-qm", "nudge")
code, out = run(t, "reviews.py", "verify")
expect("verify re-derives the carry from history and accepts it", code == 0 and "ERROR" not in out, out)
rows = (t / "content/fi/FY3" / LESSON / "review/carry.tsv").read_text().splitlines()
p.write_text(p.read_text().replace(nudged, txt.replace(">", ' fill="red">', 1) if False else re.sub(r"(</div>|</text>)", r"X\1", nudged, count=1), 1))   # new label text: a figure change
cat = (t / "content/fi/FY3" / LESSON / "review/carry.tsv")
cat.write_text(rows[0] + "\n" + "\t".join(rows[1].split("\t")[:3] + [h(t)] + rows[1].split("\t")[4:]) + "\n")   # a forged carry to the new hash
code, out = run(t, "reviews.py", "verify")
expect("a carry over a real figure change fails verify", code == 1 and "must review" in out, out)
t = project(); git(t, "init", "-q"); git(t, "config", "user.email", "t@t"); git(t, "config", "user.name", "t"); git(t, "add", "."); git(t, "commit", "-qm", "v1")
report(t, "science"); report(t, "pedagogy"); report(t, "visual")
ts = t / "tests/sims" / f"{LESSON}.json"; tests = json.loads(ts.read_text())
ts.write_text(json.dumps(tests + [{"expr": "1", "expected": 1, "tol": 0.001}], ensure_ascii=False, indent=2))
code, out = run(t, "reviews.py", "scope", LESSON)
expect("a simulation assertion added: no review", "science: none" in out and "pedagogy: none" in out and "visual: none" in out, out)
tests[0]["tol"] = tests[0].get("tol", 0.01) * 10; ts.write_text(json.dumps(tests, ensure_ascii=False, indent=2))
code, out = run(t, "reviews.py", "scope", LESSON)
expect("a simulation assertion loosened: full science review", "science: full" in out and "loosened" in out, out)
ts.write_text(json.dumps(json.loads((SRC / "tests/sims" / f"{LESSON}.json").read_text()), ensure_ascii=False, indent=2))
p = t / "content/fi/FY3" / LESSON / "lesson.md"; style = next(l for l in re.sub(r'<svg[^>]*data-fig="hero".*?</svg>', "", p.read_text(), flags=re.S).splitlines() if 'stroke-width="' in l)   # a theory figure, not the opening illustration
p.write_text(p.read_text().replace(style, re.sub(r'stroke-width="[\d.]+"', 'stroke-width="9"', style, count=1), 1))
code, out = run(t, "reviews.py", "scope", LESSON)
expect("a stroke width changed: science none, pedagogy and visual delta", "science: none" in out and "pedagogy: delta" in out and "visual: delta" in out and "styling" in out, out)
p.write_text(re.sub(r"^## Kaava.*$", "## Kaava: Testilaki", (SRC / "content/fi/FY3" / LESSON / "lesson.md").read_text(), count=1, flags=re.M))
code, out = run(t, "reviews.py", "scope", LESSON)
expect("the formula section named after its law: delta for all three, nothing else", out.count("delta") == 3 and "section-name" in out and "structure" not in out, out)
p.write_text((SRC / "content/fi/FY3" / LESSON / "lesson.md").read_text())
i = t / "content/fi/FY3" / LESSON / "inquiry.json"; d = json.loads(i.read_text()); simact = next(a for a in d["activities"] if a["type"] == "sim")
whole = " ".join(simact.pop(k, "") for k in ("text", "howto", "model", "calc")).strip(); first, _, rest_ = whole.partition(". "); simact["text"], simact["model"] = first + ".", rest_
i.write_text(json.dumps(d, ensure_ascii=False, indent=2))
code, out = run(t, "reviews.py", "scope", LESSON)
expect("the sim text moved word for word into a box: science none, pedagogy delta", "science: none" in out and "pedagogy: delta" in out and "relocated" in out, out)
simact["model"] = rest_.replace("a", "e", 1); i.write_text(json.dumps(d, ensure_ascii=False, indent=2))
code, out = run(t, "reviews.py", "scope", LESSON)
expect("a word changed on the way: not relocated", "relocated" not in out and "science: none" not in out, out)
i.write_text((SRC / "content/fi/FY3" / LESSON / "inquiry.json").read_text())
d = json.loads(i.read_text())
exp = next(a for a in d["activities"] if a["type"] == "experiment"); k = next(iter(exp["initial"])); exp["initial"][k] = exp["initial"][k] + 1 if isinstance(exp["initial"][k], (int, float)) else exp["initial"][k]
i.write_text(json.dumps(d, ensure_ascii=False, indent=2))
code, out = run(t, "reviews.py", "scope", LESSON)
expect("an experiment's initial value changed: the science reviewer looks (numbers: delta, teacher 2026-11-16)", "science: delta" in out and "numbers" in out, out)
# 6. packets: what each role receives
t = project(); git(t, "init", "-q"); git(t, "config", "user.email", "t@t"); git(t, "config", "user.name", "t"); git(t, "add", "."); git(t, "commit", "-qm", "v1")
code, out = run(t, "review_packet.py", LESSON, "--role", "science"); ps = (t / "content/fi/FY3" / LESSON / "review/packet-science.md").read_text()
expect("science packet: full, with answers.py and sim.js, without curriculum.json", code == 0 and "### answers.py" in ps and "### sim.js" in ps and '"FY1": {' not in ps and "Role: **science**" in ps, out)   # the slot only, not curriculum.json
expect("a new lesson: one run reviews the exercises too and writes their report", f"/{LESSON}/exercises/exercises.json" in ps and "Second report" in ps and "exercises/review/science.md" in ps, out)
code, out = run(t, "review_packet.py", LESSON, "--role", "pedagogy"); pp = (t / "content/fi/FY3" / LESSON / "review/packet-pedagogy.md").read_text()
expect("pedagogy packet: figures collapsed, no answers.py, no sim.js", "figure body omitted" in pp and "### answers.py" not in pp and "### sim.js" not in pp and "Screenshots" in pp, out)
expect("a packet is a file the agent reads, never pasted: the script prints its path and size", "packet-pedagogy.md: full," in out and "tokens" in out, out)
expect("packets carry the course's LOPS goals, the slot and the glossary terms, and point to CLAUDE.md instead of repeating it",
       "## Course FY3: Energia ja lämpö" in ps and "Keskeiset sisällöt" in ps and "Lesson slot" in ps and "Glossary terms" in ps and "CLAUDE.md" in ps and "Physics and maths conventions" not in ps)
report(t, "science"); report(t, "pedagogy"); report(t, "visual"); p = t / "content/fi/FY3" / LESSON / "lesson.md"; p.write_text(p.read_text().replace("lämpötila", "lämpötilat", 1))
code, out = run(t, "review_packet.py", LESSON, "--role", "science"); ps = (t / "content/fi/FY3" / LESSON / "review/packet-science.md").read_text()
expect("delta packet: previous report and the diff, not the whole lesson", "Mode: **delta**" in ps and "Your previous report" in ps and "+" in ps.split("```diff")[1] and "### answers.py" not in ps, out)
code, out = run(t, "review_packet.py", LESSON, "--role", "science", "--exercises"); xs = (t / "content/fi/FY3" / LESSON / "exercises/review/packet-science.md").read_text()
expect("exercise packet: the brief (formula sections, worked example) and the exercise files, not the lesson or the simulation",
       code == 0 and "Exercise brief" in xs and "## Esimerkki" in xs and "## Kaava" in xs and "### answers.py" in xs and "### lesson.md" not in xs and "### sim.js" not in xs
       and "### inquiry.json" not in xs and "exercises/review/science.md" in xs and "--exercises" in xs and "<svg" not in xs, out)
code, out = run(t, "review_packet.py", LESSON, "--role", "developer", "--exercises"); xd = (t / "content/fi/FY3" / LESSON / "exercises/review/packet-developer.md").read_text()
# 0.95: the exercise bank (20+ tasks with complete solutions per chapter, 2026-11) makes the exercise files most of a lesson folder, and a
# lesson whose figures sit on picture files (work queue 24) has no inline SVG in lesson.md, so the folder is about a quarter smaller (0.63 -> 0.85)
expect("exercise developer packet: rules, brief and current exercises, a fraction of the lesson's size",
       code == 0 and "Complete solutions" in xd and "Exercise brief" in xd and "### exercises.json" in xd and "### lesson.md" not in xd
       and len(xd) < 0.95 * sum(f.stat().st_size for f in (t / "content/fi/FY3" / LESSON).rglob("*") if f.is_file() and "review" not in f.parts), out)
code, out = run(t, "review_packet.py", "--batch", LESSON, "--role", "pedagogy"); bf = t / "review-batch/packet-pedagogy.md"; pb = bf.read_text() if bf.exists() else ""
expect("batch packet: one file for many lessons, each with its diff and its own report", code == 0 and f"## {LESSON}" in pb and "```diff" in pb and "review/pedagogy.md" in pb, out)
code, out = run(t, "review_packet.py", LESSON, "--role", "developer", "--fix"); pd = (t / "content/fi/FY3" / LESSON / "review/packet-developer.md").read_text()
expect("developer fix packet: both reports, the rules and the file list, not the file bodies",
       "Findings to resolve" in pd and "### science" in pd and "### lesson.md" not in pd and f"content/fi/FY3/{LESSON}/lesson.md" in pd and "1. Maths in LaTeX" in pd, out)
code, out = run(t, "review_packet.py", LESSON, "--role", "developer"); pd = (t / "content/fi/FY3" / LESSON / "review/packet-developer.md").read_text()
expect("developer draft packet: where files go for this course and the reference lesson", "Where files go" in pd and "Reference lesson" in pd, out)
code, out = run(t, "usage.py", "log", LESSON, "--agent", "x", "--model", "sonnet", "--effort", "medium", "--mode", "full", "--round", "1", "--context", "100", "--seconds", "1", "--calls", "1", "--verdict", "PASS")
expect("a manual usage row is marked reported, not measured", code == 0 and "reported" in run(t, "usage.py", "report", LESSON)[1] and "unknown" in run(t, "usage.py", "report", LESSON)[1], out)
# 7. the split of 2026-10-28: a PASS on the one hash of the lesson before the split carries over to both parts when
# the files only moved (answers.py cut line for line into answers.py and lesson-answers.py), and only then
t = project(); L = t / "content/fi/FY3" / LESSON; A = t / "lessons/FY3" / LESSON / "answers.py"
git(t, "init", "-q"); git(t, "config", "user.email", "t@t"); git(t, "config", "user.name", "t")
for n in ("exercises.json", "solutions.md"): (L / "exercises" / n).rename(L / n)          # the layout before the split
(L / "exercises").rmdir(); exercise_answers = A.read_text()
INQ = 'a["inq-test"] = 2.5 * 4.0                            # an inquiry number, not an exercise\n'
A.write_text(exercise_answers.replace("\nprint(", "\n" + INQ + "print(", 1)); git(t, "add", "."); git(t, "commit", "-qm", "before the split")
old = subprocess.run([sys.executable, "-c", "import sys; sys.path.insert(0, 'scripts'); import reviews as r, courses; print(r.hash_at('HEAD', courses.find_lesson(sys.argv[1]), 'all'))", LESSON],
                     cwd=t, capture_output=True, text=True).stdout.strip()
report(t, "science", hash_=old); report(t, "pedagogy", hash_=old); report(t, "visual", hash_=old); git(t, "add", "."); git(t, "commit", "-qm", "reviews")
(L / "exercises/review").mkdir(parents=True)
for n in ("exercises.json", "solutions.md"): (L / n).rename(L / "exercises" / n)
for n in ("science", "pedagogy", "visual"): (L / "exercises/review" / f"{n}.md").write_text((L / "review" / f"{n}.md").read_text())
A.write_text(exercise_answers); first = next(l for l in exercise_answers.splitlines() if l.startswith("import"))   # `import json` (and more)
(A.parent / "lesson-answers.py").write_text(f'"""Lesson numbers."""\n{first}\n\na = {{}}\n{INQ}print(json.dumps(a))\n')
code, out = run(t, "reviews.py", "carry", LESSON); code2, out2 = run(t, "reviews.py", "carry", LESSON, "--exercises")
expect("files moved and answers.py split line for line: both PASS reports carry over, for the lesson and for the exercises",
       "science: carried over" in out and "pedagogy: carried over" in out and "science: carried over" in out2 and ": reviewed" in state(t) and "exercises: reviewed" in state(t, part="exercises")
       and "split" in out, out + out2)
git(t, "add", "."); git(t, "commit", "-qm", "split")
code, out = run(t, "reviews.py", "verify")
expect("verify re-derives both carries from history", code == 0 and "ERROR" not in out, out)
(A.parent / "lesson-answers.py").write_text((A.parent / "lesson-answers.py").read_text().replace("2.5 * 4.0", "2.5 * 4.1"))
code, out = run(t, "reviews.py", "scope", LESSON)
expect("a number changed on the way: not a split, the science reviewer looks", "science: delta" in out and "answers" in out, out)
rows = (L / "review/carry.tsv").read_text().splitlines()
(L / "review/carry.tsv").write_text(rows[0] + "\n" + "\n".join("\t".join(r.split("\t")[:3] + [h(t)] + r.split("\t")[4:]) for r in rows[1:]) + "\n")   # forged
code, out = run(t, "reviews.py", "verify")
expect("a forged split carry over that change fails verify", code == 1 and "must review" in out, out)
git(t, "checkout", "--", ".")
(L / "exercises/exercises.json").write_text((L / "exercises/exercises.json").read_text().replace('"level": 1', '"level": 1, "uusi": 1', 1))
code, out = run(t, "reviews.py", "scope", LESSON, "--exercises"); code2, out2 = run(t, "reviews.py", "scope", LESSON)
expect("after the split an exercise change is the exercises' alone", "science: none" not in out and "split" in out and "science: none" in out2, out + out2)
git(t, "checkout", "--", ".")
ex = json.loads((L / "exercises/exercises.json").read_text()); old_text = ex["level1"][0]["text"]; ex["level1"][0]["text"] = "Uusi tehtäväteksti, jota kukaan ei ole tarkastanut?"
(L / "exercises/exercises.json").write_text(json.dumps(ex, ensure_ascii=False, indent=2)); git(t, "add", "."); git(t, "commit", "-qm", "new exercise text")
code, out = run(t, "build.py"); page = (t / "site" / f"{LESSON}.html").read_text() if (t / "site" / f"{LESSON}.html").exists() else ""
expect("exercises edited, not yet reviewed: the lesson stays on the site with the exercises last reviewed", code == 0 and "Uusi tehtäväteksti" not in page
       and f'id="{LESSON}-L1-01"' in page and old_text.split(".")[0][:30] in page and "keeps the exercises last reviewed" in out, out)


# 8. the visual & editorial review (teacher 2026-10-31): a third PASS for new and changed content, a hash-bound
# baseline for what was published before, formulas re-set without a change of meaning seen by the visual reviewer alone
def init_git(tmp):
    git(tmp, "init", "-q"); git(tmp, "config", "user.email", "t@t"); git(tmp, "config", "user.name", "t"); git(tmp, "add", "."); git(tmp, "commit", "-qm", "v1")
t = project(); init_git(t); L = t / "content/fi/FY3" / LESSON; site = t / "site"
report(t, "science"); report(t, "pedagogy"); report(t, "science", part="exercises"); report(t, "pedagogy", part="exercises")
expect("new content with science and pedagogy PASS but no visual report: a draft", ": draft" in state(t) and "visual=missing" in state(t), state(t))
code, out = build(t)
expect("... and not published", code == 0 and not (site / f"{LESSON}.html").exists(), out)
report(t, "visual", "FAIL"); code, out = build(t)
expect("a visual FAIL blocks new content", ": draft" in state(t) and "visual=FAIL" in state(t) and not (site / f"{LESSON}.html").exists(), state(t) + out)
(L / "review/visual.md").unlink()
code, out = run(t, "reviews.py", "baseline", "init")
rows = (t / "docs/visual-baseline.tsv").read_text() if (t / "docs/visual-baseline.tsv").exists() else ""
expect("baseline init: one hash-bound row per part both reviewers passed, no PASS report written",
       code == 0 and f"lesson\tfi\t{LESSON}\tlesson\t{h(t)}" in rows and f"lesson\tfi\t{LESSON}\texercises\t{h(t, part='exercises')}" in rows
       and not (L / "review/visual.md").exists(), out + rows)
code, out = run(t, "reviews.py", "baseline", "init")
expect("the baseline is written once", code != 0 and "written once" in out, out)
code, out = build(t); page = (site / f"{LESSON}.html").read_text() if (site / f"{LESSON}.html").exists() else ""
expect("content published before the gate stays published under its baseline, exercises too", code == 0 and page and f'id="{LESSON}-L1-01"' in page
       and "visual baseline" in state(t) and "exercises: reviewed" in state(t, part="exercises"), state(t) + out)
code, out = run(t, "reviews.py", "baseline")
expect("the baseline report lists what still awaits its first visual review", code == 0 and "2 published part(s) await" in out and LESSON in out, out)
report(t, "visual", "FAIL"); code, out = build(t)
expect("an audit's visual FAIL on baseline content does not unpublish it, and the report says it is audited",
       (site / f"{LESSON}.html").exists() and ": reviewed" in state(t) and "audited" in run(t, "reviews.py", "baseline")[1], state(t))
code, out = run(t, "reviews.py", "scope", LESSON)
expect("baseline content not yet reviewed: the visual review is full, the others are not asked", "visual: full (visual baseline" in out and "science: delta (0 changed" in out, out)
git(t, "add", "."); git(t, "commit", "-qm", "baseline")
code, out = run(t, "reviews.py", "verify")
expect("verify accepts the committed baseline", code == 0 and "ERROR" not in out, out)
ts = t / "tests/sims" / f"{LESSON}.json"; tests = json.loads(ts.read_text()); ts.write_text(json.dumps(tests + [{"expr": "1", "expected": 1, "tol": 0.001}], ensure_ascii=False, indent=2))
code, out = run(t, "reviews.py", "scope", LESSON)
expect("a change no reviewer need see on baseline content: the baseline carries over like a PASS", "visual: none" in out and "visual baseline carried over" in out, out)
code, out = run(t, "reviews.py", "carry", LESSON)
expect("... recorded in carry.tsv: still published", "visual: carried over" in out and ": reviewed" in state(t) and "visual baseline" in state(t), out + state(t))
git(t, "add", "."); git(t, "commit", "-qm", "a test added")
code, out = run(t, "reviews.py", "verify")
expect("verify re-derives the baseline's carry from history", code == 0 and "ERROR" not in out, out)
p = L / "lesson.md"; p.write_text(p.read_text().replace("lämpötila", "lämpötilat", 1))
code, out = run(t, "reviews.py", "scope", LESSON)
expect("a material change to baseline content: its first genuine visual review, in full; the others by their rules",
       "visual: full (visual baseline: the content changed" in out and "science: delta" in out and "pedagogy: delta" in out and ": draft" in state(t), out + state(t))
report(t, "science"); report(t, "pedagogy")
expect("the baseline does not authorise the changed version: science and pedagogy PASS alone leave it a draft", ": draft" in state(t) and "visual=stale" in state(t), state(t))
code, out = build(t)
expect("... so the build leaves it out with a warning", not (site / f"{LESSON}.html").exists() and LESSON in out, out)
report(t, "visual"); code, out = build(t)
expect("a genuine visual PASS of the changed version publishes it", ": reviewed" in state(t) and "visual baseline" not in state(t) and (site / f"{LESSON}.html").exists(), state(t))
git(t, "checkout", "--", "."); git(t, "clean", "-fdq", "content")
e = L / "exercises/exercises.json"; ex = json.loads(e.read_text()); old_text = ex["level1"][0]["text"]; ex["level1"][0]["text"] = "Uusi tehtäväteksti, jota visuaalinen tarkastaja ei ole nähnyt?"
e.write_text(json.dumps(ex, ensure_ascii=False, indent=2)); report(t, "science", part="exercises"); report(t, "pedagogy", part="exercises")
git(t, "add", "."); git(t, "commit", "-qm", "exercise edited, science and pedagogy passed")
code, out = build(t); page = (site / f"{LESSON}.html").read_text()
expect("exercises edited after the gate, only two reviews: the page keeps the exercises published under the baseline",
       "visiaalinen" not in page and "visuaalinen tarkastaja" not in page and old_text.split(".")[0][:30] in page and "keeps the exercises last reviewed" in out, out)
bl = t / "docs/visual-baseline.tsv"; bl.write_text(bl.read_text() + f"lesson\tfi\t{LESSON}\texercises\t{h(t, part='exercises')}\t2026-11-01\n")
code, out = run(t, "reviews.py", "verify")
expect("a baseline row added later fails verify: the baseline only shrinks", code == 1 and "added after the baseline" in out, out)
expect("... (and the forged row would have published the edited exercises: verify is what stops it)", "exercises: reviewed" in state(t, part="exercises"), state(t, part="exercises"))
git(t, "checkout", "--", "docs")
lines = bl.read_text().splitlines(); bl.write_text("\n".join(l for l in lines if "\texercises\t" not in l) + "\n")
code, out = run(t, "reviews.py", "verify")
expect("removing baseline rows is allowed", code == 0 and "ERROR" not in out, out)

# 8b. a formula re-set (spacing, \dfrac/\frac, {,}) is the category typography: no science or pedagogy review
t = project(); init_git(t); L = t / "content/fi/FY3" / LESSON; p = L / "lesson.md"
for n in ("science", "pedagogy", "visual"): report(t, n)
src_md = p.read_text(); line = next(l for l in src_md.splitlines() if "$" in l and "\\,\\text" in l and not l.lstrip().startswith("<"))
p.write_text(src_md.replace(line, line.replace("\\,\\text", "\\;\\text", 1), 1))
code, out = run(t, "reviews.py", "scope", LESSON)
expect("a formula re-set without a change of meaning: science and pedagogy none, visual delta", "science: none" in out and "pedagogy: none" in out and "visual: delta" in out and "typography" in out, out)
p.write_text(src_md.replace(line, re.sub(r"(\$[^$]*?)(\d)", lambda m: m.group(1) + str((int(m.group(2)) + 1) % 10), line, count=1), 1))
code, out = run(t, "reviews.py", "scope", LESSON)
expect("... but a changed number in a formula is not typography: science delta", "science: delta" in out and "typography" not in out and "numbers" in out, out)
p.write_text(src_md.replace(line, line + " Lisäsana.", 1))
code, out = run(t, "reviews.py", "scope", LESSON)
expect("... and a sentence added outside the maths is not typography", "typography" not in out and "science: none" not in out, out)
plain = next(l for l in src_md.splitlines() if l.strip() and "$" not in l and not l.lstrip().startswith(("<", "#", "-", "`")) and len(l.split()) > 3)
w = plain.split()[1]
p.write_text(src_md.replace(plain, plain.replace(" " + w + " ", " $" + w + "$ ", 1), 1))
code, out = run(t, "reviews.py", "scope", LESSON)
expect("a symbol in the text set as maths, nothing else, is typography: science and pedagogy none", "science: none" in out and "pedagogy: none" in out and "visual: delta" in out, out)
ls = src_md.split("\n"); k = next(i for i in range(1, len(ls)) if ls[i - 1].strip() and ls[i].strip() and not ls[i - 1].lstrip().startswith(("<", "`", "{")) and not ls[i].lstrip().startswith(("<", "`", "{")))
p.write_text("\n".join(ls[:k] + [""] + ls[k:]))
code, out = run(t, "reviews.py", "scope", LESSON)
expect("a blank line added (a list builds as a list) is typography: science and pedagogy none", "science: none" in out and "pedagogy: none" in out and "visual: delta" in out, out)
p.write_text(src_md.replace(plain, plain.replace(" " + w + " ", " $" + w + "2$ ", 1), 1))
code, out = run(t, "reviews.py", "scope", LESSON)
expect("... but a symbol changed while set as maths is not typography", "science: none" not in out, out)

numline = next(l for l in src_md.splitlines() if re.search(r"\d", l) and not l.lstrip().startswith(("<", "#", "-", "`", "|", "{")) and len(l.split()) > 6)
words = [x for x in numline.split() if x.isalpha() and len(x) > 3]
p.write_text(src_md.replace(numline, numline.replace(" " + words[0] + " ", " " + words[0] + "kin ", 1), 1))
code, out = run(t, "reviews.py", "scope", LESSON)
expect("a prose line with a number reworded, its numbers and formulas the same: wording (science delta, not full)", "science: delta" in out and "wording" in out, out)
p.write_text(src_md)

# 8b2. a calculation chain only re-broken into rows is the category reflow (teacher 2026-11-15): science and pedagogy carry
# over, the visual reviewer always looks again; any other change in the same text is reviewed as usual
t = project(); init_git(t); L = t / "content/fi/FY3" / LESSON; p = L / "lesson.md"
CH = "$F = m a = 2{,}0\\,\\text{kg} \\cdot 3{,}0\\,\\text{m/s}^2 = 6{,}0\\,\\text{N}$"
src_md = p.read_text().rstrip("\n") + "\n\nSijoitus: " + CH + "\n"
p.write_text(src_md)
for n in ("science", "pedagogy", "visual"): report(t, n)
git(t, "add", "."); git(t, "commit", "-qm", "chain added, all passed")
def reflow(new_text):
    p.write_text(src_md.replace(CH, new_text, 1)); return run(t, "reviews.py", "scope", LESSON)[1]
ROWS = "$F = m a$\n$= 2{,}0\\,\\text{kg} \\cdot 3{,}0\\,\\text{m/s}^2$\n\n$= 6{,}0\\,\\text{N}$"
out = reflow(ROWS)
expect("a chain split into rows, nothing else: science and pedagogy none, visual delta, category reflow",
       "science: none" in out and "pedagogy: none" in out and "visual: delta" in out and "reflow" in out, out)
for what, new_text in (("a number", ROWS.replace("3{,}0", "3{,}1")), ("a sign", ROWS.replace("\\cdot", "+")), ("a unit", ROWS.replace("m/s}^2", "m/s}^3")),
                       ("the order", "$F = m a$\n$= 3{,}0\\,\\text{m/s}^2 \\cdot 2{,}0\\,\\text{kg}$\n\n$= 6{,}0\\,\\text{N}$")):
    out = reflow(new_text)
    expect(f"... but a changed {what} in the rows is not reflow: science is not none", "science: delta" in out and "pedagogy: delta" in out and "numbers" in out, out)
out = reflow(ROWS + " Lisäsana.")
expect("... a word added next to the re-broken chain is reviewed as usual: science is not none", "science: none" not in out, out)
out = reflow(ROWS.replace("6{,}0", "6{,}1"))
expect("... a number changed while the chain is also re-broken: science delta, not none", "science: delta" in out and "numbers" in out, out)
p.write_text(src_md); code, out = run(t, "reviews.py", "carry", LESSON)
expect("no carry is written when nothing changed", "carried over" not in out, out)
reflow(ROWS); code, out = run(t, "reviews.py", "carry", LESSON)
expect("carry records reflow for science and pedagogy only", "science: carried over" in out and "pedagogy: carried over" in out and "visual: delta review needed" in out, out)
code, out = run(t, "reviews.py", "verify")
expect("verify re-derives the reflow carry in CI", code == 0 and "ERROR" not in out, out)

sys.path.insert(0, str(SRC / "scripts")); import reviews as _rv
_j = lambda x: json.dumps({"solution": x}, ensure_ascii=False, indent=1)
expect("reflow in an exercise set's JSON (a line break is \\n in the string): same chain, same view",
       _rv.chain_view(_j("Sij: $a = b = c$"), "x.json") == _rv.chain_view(_j("Sij: $a = b$\n$= c$"), "x.json")
       and _rv.chain_view(_j("Sij: $a = b = c$"), "x.json") != _rv.chain_view(_j("Sij: $a = b$\n$= d$"), "x.json"))

# the teacher's fy2-3 case (2026-11-15): a long inline formula lifted into its own display formula, aligned at the equals signs
CH2 = "$E = 1500 \\cdot 3{,}0\\,\\text{kWh} = 4500\\,\\text{kWh}$"
src2 = src_md.replace(CH, "Hän kirjoittaa " + CH2 + " ja hinnaksi $900\\,\\text{€}$.", 1); p.write_text(src2)
git(t, "add", "."); git(t, "commit", "-qm", "the fy2-3 formula as an inline formula")
for n in ("science", "pedagogy", "visual"): report(t, n)
git(t, "add", "."); git(t, "commit", "-qm", "reviewed")
AL = "Hän kirjoittaa\n\n$$\\begin{aligned} E &= 1500 \\cdot 3{,}0\\,\\text{kWh} \\\\ &= 4500\\,\\text{kWh} \\end{aligned}$$\n\nja hinnaksi $900\\,\\text{€}$."
def lift(new_text):
    p.write_text(src2.replace("Hän kirjoittaa " + CH2 + " ja hinnaksi $900\\,\\text{€}$.", new_text, 1)); return run(t, "reviews.py", "scope", LESSON)[1]
out = lift(AL)
expect("an inline formula lifted into an aligned display formula (fy2-3): science and pedagogy none, visual delta, reflow",
       "science: none" in out and "pedagogy: none" in out and "visual: delta" in out and "reflow" in out, out)
for what, new_text in (("a number", AL.replace("4500", "4501")), ("a sign", AL.replace("\\cdot", "+")), ("a unit", AL.replace("kWh} \\\\", "Wh} \\\\")),
                       ("the order", AL.replace("1500 \\cdot 3{,}0", "3{,}0 \\cdot 1500"))):
    out = lift(new_text)
    expect(f"... but a changed {what} in the aligned rows is not reflow: science delta", "science: delta" in out and "pedagogy: delta" in out and "numbers" in out, out)
out = lift(AL.replace("ja hinnaksi", "ja lisäksi hinnaksi"))
expect("... a word added next to the lifted formula is reviewed as usual", "science: none" not in out, out)
p.write_text(src_md)

# 8c. investigations, TVT guides and Sovella sets: three reports, or a baseline row for exactly this hash
sys.path.insert(0, str(HERE)); import reviews as rv
expect("a value with its unit set as maths is typography", rv._typography_pair("paksuus on 82 µm.", r"paksuus on $82\,\mu\text{m}$."))
expect("... the litre \\text{l} → \\textsf{l} is typography", rv._typography_pair(r"$3{,}0\,\text{l}$", r"$3{,}0\,\textsf{l}$"))
expect("... but $m$ → $\\text{m}$ (mass → metre) is not", not rv._typography_pair(r"massa $m$ on", r"massa $\text{m}$ on"))
expect("... nor a changed value set as maths", not rv._typography_pair("on 82 µm.", r"on $83\,\mu\text{m}$."))
expect("... an area with a Unicode square set as maths is typography", rv._typography_pair("ala on 45 m² ja", r"ala on $45\,\text{m}^2$ ja"))
expect("... a temperature with °C and a header symbol too", rv._typography_pair("| θ (°C) | 95 kPa", r"| $\theta$ (°C) | $95\,\text{kPa}$"))
expect("... but not when the power changes", not rv._typography_pair("ala on 45 m² ja", r"ala on $45\,\text{m}^3$ ja"))
expect("... nor a changed sign", not rv._typography_pair("on -15 °C", r"on $+15\,{}^\circ\text{C}$"))
_po = '  "text": "Tausta $\\\\nu = 2$. Oppilas laski. Laske $d$.",'
expect("a task text given paragraph breaks, word for word the same, is paragraphs", rv._paragraph_pair(_po, _po.replace("$. Oppilas", "$.\\n\\nOppilas").replace(". Laske", ".\\n\\nLaske")))
expect("... but not when a word changes too", not rv._paragraph_pair(_po, _po.replace(". Laske", ".\\n\\nLaskekaa")))
expect("... nor a LaTeX \\nu read as a newline", not rv._paragraph_pair(_po, _po.replace("\\\\nu", "\\\\n u")))
expect("... nor the same text under another key", not rv._paragraph_pair(_po, _po.replace('"text"', '"answer"').replace(". Laske", ".\\n\\nLaske")))
expect("a paragraphs-only change needs no reviewer", rv.RULES["paragraphs"] == ("none", "none", "none"))
_mo = ["**Tulos.** On $x = 2\\,\\text{m}$. Koska $a$ ja $b$, kaksi numeroa."]
expect("a stage cut into paragraphs and a list, word for word the same, is md-paragraphs", rv._md_paragraphs(_mo, ["**Tulos.** On $x = 2\\,\\text{m}$.", "- Koska $a$ ja", "- $b$, kaksi numeroa."]))
expect("... but not when a word changes", not rv._md_paragraphs(_mo, ["**Tulos.** On $x = 2\\,\\text{m}$.", "Koska $a$ ja $b$, kolme numeroa."]))
expect("... nor when the order changes", not rv._md_paragraphs(_mo, ["Koska $a$ ja $b$, kaksi numeroa.", "**Tulos.** On $x = 2\\,\\text{m}$."]))
expect("... nor a heading", not rv._md_paragraphs(["## A B"], ["## A", "B"]))
expect("... across a stage marker both sides have", rv._md_paragraphs(["A B.", "", "<!-- vaihe -->", "", "C D."], ["A", "", "B.", "", "<!-- vaihe -->", "", "C D."]))
expect("... but not a stage marker moved", not rv._md_paragraphs(["A B.", "<!-- vaihe -->", "C D."], ["A", "<!-- vaihe -->", "B. C D."]))
expect("an md-paragraphs change needs only the visual reviewer", rv.RULES["md-paragraphs"] == ("none", "none", "delta"))
expect("... also when the stage was re-broken too: a chain lifted into an aligned block reads with a space more inside the formula",
       rv._md_paragraphs(["**M:** so $d_\\text{A}\\approx400$. This is it. The value $1{,}5$."], ["**M:** so $d_\\text{A} \\approx400$. This is it.", "", "The value $1{,}5$."]))
expect("... but a space that ends a control word is not left out", not rv._md_paragraphs(["A $a\\cdot x$ b. C"], ["A $a\\cdotx$ b.", "", "C"]))
expect("para_view: a paragraph cut into paragraphs and a list reads as it did", rv.para_view("A $x$ b c.\nD", "s.md") == rv.para_view("A $x$\n\n- b\n- c.\n\nD", "s.md"))
expect("... and not when a word changes", rv.para_view("A b c.", "s.md") != rv.para_view("A\n\n- b\n- d.", "s.md"))
expect("... in JSON a \\n- is a list item, and a LaTeX \\nu stays", rv.para_view(json.dumps({"s": "A.\n\n- b\n- c \\nu"}), "t.json") == rv.para_view(json.dumps({"s": "A. b c \\nu"}), "t.json")
       != rv.para_view(json.dumps({"s": "A. b c u"}), "t.json"))
_lo = r"    label('$t\\ (\\text{s})$', CH.x1 + 10, CH.y0 + ts(36), p.RIGHT, ts(12));"
expect("a LaTeX label moved in a sim's own label() helper is a label nudge", rv._js_label_pair(_lo, _lo.replace("ts(36)", "ts(39)")))
expect("... but not its size", not rv._js_label_pair(_lo, _lo.replace("ts(12)", "ts(14)")))
d = pathlib.Path(tempfile.mkdtemp()); (d / "review").mkdir(); keep = rv.BASELINE, rv.VISUAL_GATE
for n in ("science", "pedagogy"): (d / "review" / f"{n}.md").write_text("VERDICT: PASS\nCONTENT-HASH: 1111111111111111\n")
rv.BASELINE = d / "visual-baseline.tsv"; rv.VISUAL_GATE = True
expect("an investigation with two PASS reports and no baseline: a draft", rv.item_status("investigation", "x", "fi", d, "1111111111111111")["state"] == "draft")
rv.BASELINE.write_text("\t".join(rv.BASELINE_COLS) + "\ninvestigation\tfi\tx\t-\t1111111111111111\t2026-10-31\n")
expect("... on the baseline for its hash: reviewed", rv.item_status("investigation", "x", "fi", d, "1111111111111111")["state"] == "reviewed")
expect("... a changed hash is not covered", rv.item_status("investigation", "x", "fi", d, "2222222222222222")["state"] == "draft")
(d / "review/visual.md").write_text("VERDICT: FAIL\nCONTENT-HASH: 1111111111111111\n")
expect("... a visual FAIL (an audit) leaves the baseline in force", rv.item_status("investigation", "x", "fi", d, "1111111111111111")["state"] == "reviewed")

# item carry (teacher 2026-11-11): an investigation's PASS carries over a carry row for exactly the two hashes, no other
import tempfile as _tf, pathlib as _pl
_d = _pl.Path(_tf.mkdtemp()); (_d / "review").mkdir()
for _n in rv.REVIEWS: (_d / "review" / f"{_n}.md").write_text("VERDICT: PASS\nCONTENT-HASH: aaaaaaaaaaaaaaaa\n")
expect("an item whose hash changed is a draft", rv.item_status("investigation", "y", "fi", _d, "bbbbbbbbbbbbbbbb")["state"] == "draft")
(_d / "review" / "carry.tsv").write_text("\t".join(rv.CARRY_COLS) + "\n" + "".join(
    f"2026-11-11\t{_n}\taaaaaaaaaaaaaaaa\tbbbbbbbbbbbbbbbb\t000000000000\tteacher-figure\n" for _n in rv.REVIEWS))
expect("... with carry rows over teacher-approved figures: reviewed", rv.item_status("investigation", "y", "fi", _d, "bbbbbbbbbbbbbbbb")["state"] == "reviewed")
expect("... the rows carry to that hash only", rv.item_status("investigation", "y", "fi", _d, "cccccccccccccccc")["state"] == "draft")
rv.BASELINE, rv.VISUAL_GATE = keep

hero = '<svg data-fig="hero" viewBox="0 0 1200 600" role="img">\n  <rect x="0" y="0" width="1200" height="600" fill="#f6f1e6"/>\n</svg>'
md = "> **Miksi** x?\n\n" + hero + "\n\n## Ydinajatus\nText.\n"
expect("an opening illustration without labels drops out of the classified text", rv.strip_hero(md) == "> **Miksi** x?\n\n## Ydinajatus\nText.\n")
labelled = md.replace("</svg>", '<foreignObject x="0" y="0" width="9" height="9"><div>$Q$</div></foreignObject>\n</svg>')
expect("an opening illustration with a label stays a figure", rv.strip_hero(labelled) == labelled)
rv.chapter_titles.cache_clear()
tex = next(t for t in rv.chapter_titles() if "\\" in t)            # a current title with LaTeX, e.g. "Teho: $P = \\Delta E/\\Delta t$"
expect("a JSON line's escaped LaTeX title counts as a current chapter reference",
       rv._chapter_refs_renamed('"feedback": "Ks. (luku *Vanha nimi*)."', '"feedback": "Ks. (luku *' + tex.replace("\\", "\\\\") + '*)."'))
# a simulation's change that only places or draws (teacher 2026-11-11): the check, and the recorded approval it needs
_sim = """new p5((p) => {
  const g = 9.81, CH = { x0: 60 }, gx1 = 500;
  let v = 0, running = false, fh = 13;
  const restart = () => { v = 0; running = false; };
  p.draw = () => {
    if (running) v += g * Math.min(p.deltaTime, 100) / 1000;
    for (const e of [0, 1000]) { p.stroke(60); p.line(CH.x0 - 5, Y(e), CH.x0, Y(e)); lab(`$${tj(e)}$`, CH.x0 - 8, Y(e) + fh * 0.36, 'r', fh); }
    lab('$x\\\\ (\\\\text{m})$', gx1 + 24, Y(0) + fh * 0.35, 'l', fh, INKC);
    window.simState = { v, running };
  };
});"""
_tick = "    for (const e of [0, 1000]) { p.stroke(60); p.line(CH.x0 - 5, Y(e), CH.x0, Y(e)); lab(`$${tj(e)}$`, CH.x0 - 8, Y(e) + fh * 0.36, 'r', fh); }"
_axis = "    lab('$x\\\\ (\\\\text{m})$', gx1 + 24, Y(0) + fh * 0.35, 'l', fh, INKC);"
assert _tick in _sim and _axis in _sim
_tick2 = """    for (const e of [0, 1000]) {   // the number ends nearer the axis where it would not fit
      p.textSize(fh); const tickS = `$${tj(e)}$`, tickX = Math.min(Math.max(CH.x0 - 8, 4 + p.textWidth(tickS)), CH.x0 - 2);
      if (tickX <= CH.x0 - 8) { p.stroke(60); p.line(CH.x0 - 5, Y(e), CH.x0, Y(e)); }
      lab(tickS, tickX, Y(e) + fh * 0.36, 'r', fh);
    }"""
_axis2 = """    {   // above the axis end where it would cross the edge
      p.textSize(fh); const axS = '$x\\\\ (\\\\text{m})$', axW = p.textWidth(axS), axFits = gx1 + 24 + axW <= 594;
      lab(axS, axFits ? gx1 + 24 : 594 - axW, axFits ? Y(0) + fh * 0.35 : Y(0) - 10, 'l', fh, INKC);
    }"""
po = rv.presentation_only
expect("presentation-only: a label moved", po(_sim, _sim.replace("gx1 + 24, Y(0)", "gx1 + 12, Y(0)")))
expect("presentation-only: a tick number placed by its measured width, with new local names", po(_sim, _sim.replace(_tick, _tick2)))
expect("presentation-only: an axis name placed by its measured width", po(_sim, _sim.replace(_axis, _axis2)))
expect("presentation-only: both placements at once", po(_sim, _sim.replace(_tick, _tick2).replace(_axis, _axis2)))
expect("not presentation-only: a constant of the model changed", not po(_sim, _sim.replace("g = 9.81", "g = 9.0")))
expect("not presentation-only: the integration changed", not po(_sim, _sim.replace("v += g *", "v += 2 * g *")))
expect("not presentation-only: the state the sim reports changed", not po(_sim, _sim.replace("{ v, running }", "{ v, running, g }")))
expect("not presentation-only: a drawing line that also sets state", not po(_sim, _sim.replace(_axis, _axis + " running = false;")))
expect("not presentation-only: a drawing line that calls the model", not po(_sim, _sim.replace(_axis, _axis + " restart();")))
expect("not presentation-only: a new local that takes the name of an existing one", not po(_sim, _sim.replace(_axis, "    { const v = 3; lab('$x$', v, 0, 'l', fh, INKC); }")))
expect("not presentation-only: a function defined in the change", not po(_sim, _sim.replace(_axis, "    const f2 = () => 1; " + _axis.strip())))
expect("not presentation-only: a comment alone (that is the category comments)", not po(_sim, _sim.replace(_axis, _axis + "   // the axis name")))
expect("not presentation-only: no change", not po(_sim, _sim))
_new = _sim.replace(_axis, _axis2); _rows = rv.presentation_rows
try:
    rv.presentation_rows = lambda: set()
    expect("presentation-only needs its recorded approval: without the row the change is not approved", not rv.presentation_approved("assets/sims/x/sim.js", _sim, _new))
    rv.presentation_rows = lambda: {("assets/sims/x/sim.js", rv._pres_hash(_sim), rv._pres_hash(_new))}
    expect("... with the row of exactly this change it is", rv.presentation_approved("assets/sims/x/sim.js", _sim, _new))
    expect("... a row does not cover another file", not rv.presentation_approved("assets/sims/y/sim.js", _sim, _new))
    expect("... nor a later edit of the same file", not rv.presentation_approved("assets/sims/x/sim.js", _sim, _new.replace("594", "590")))
    _bad = _sim.replace("g = 9.81", "g = 9.0"); rv.presentation_rows = lambda: {("assets/sims/x/sim.js", rv._pres_hash(_sim), rv._pres_hash(_bad))}
    expect("... and a row cannot approve a change of the model", not rv.presentation_approved("assets/sims/x/sim.js", _sim, _bad))
finally: rv.presentation_rows = _rows
# one row holds for every language version: the approval is of the file as written, not of a language's view of it
class _State(rv.Source):
    """A project state with one simulation file and each language's texts for it."""
    TEXTS = {"fi": "aika", "en": "time", "fi-easy": "kulunut aika"}
    def __init__(self, js, lang): self.js, self.lang = js, lang
    def read(self, rel, binary=False):
        return self.js if rel.endswith(".js") else json.dumps({"sims": {"x": {"nimi": self.TEXTS[self.lang]}}}) if rel == f"lang/{self.lang}.json" else None
_rel = "assets/sims/k/x/sim.js"
_old = _sim.replace(_axis, "    lab(__('nimi'), 20, 20, 'l', fh, INKC);\n" + _axis); _new2 = _old.replace(_axis, _axis2); _bad2 = _old.replace("g = 9.81", "g = 9.0")
_views = {l: _State(_old, l).source(_rel) for l in _State.TEXTS}
expect("a simulation's view differs by language (its texts are put in), the file does not", len(set(_views.values())) == 3 and all("__('nimi')" not in v for v in _views.values()), str({l: v.count("aika") for l, v in _views.items()}))
try:
    rv.presentation_rows = lambda: {(_rel, rv._pres_hash(_old), rv._pres_hash(_new2)), (_rel, rv._pres_hash(_old), rv._pres_hash(_bad2))}
    for _l in _State.TEXTS:
        expect(f"presentation-only in {_l}: the one row of the file's change holds", rv.presentation_change(_State(_old, _l), _State(_new2, _l), _rel))
        expect(f"... and in {_l} a change of the model is not presentation-only, row or no row", not rv.presentation_change(_State(_old, _l), _State(_bad2, _l), _rel))
    rv.presentation_rows = lambda: set()
    expect("... and without the row no language has it", not any(rv.presentation_change(_State(_old, l), _State(_new2, l), _rel) for l in _State.TEXTS))
finally: rv.presentation_rows = _rows
expect("presentation-only still sends the change to the visual reviewer", rv.RULES["presentation-only"][2] == "delta" and rv.MODES.index("delta") > rv.MODES.index("none"))
expect("presentation-only: science and pedagogy carry over, the visual reviewer looks", rv.RULES["presentation-only"] == ("none", "none", "delta"))
expect("a simulation change without approval still needs the full science and pedagogy reviews", rv.RULES["simulation"] == ("full", "full", "delta"))
# 8. added exercises (teacher 2026-11-12): whole exercises added or replaced, every other exercise as passed → a delta
# review for all three; anything else of the set changed as well → the classification as before
t = project(); git(t, "init", "-q"); git(t, "config", "user.email", "t@t"); git(t, "config", "user.name", "t"); git(t, "add", "."); git(t, "commit", "-qm", "v1")
for n in ("science", "pedagogy", "visual"): report(t, n, part="exercises")
git(t, "add", "."); git(t, "commit", "-qm", "exercise reviews"); B0, H0, HL = git(t, "rev-parse", "HEAD").strip(), h(t, part="exercises"), h(t)
X = t / "content/fi/FY3" / LESSON / "exercises"; E, S, A, F = X / "exercises.json", X / "solutions.md", t / "lessons/FY3" / LESSON / "answers.py", t / "lessons/FY3" / LESSON / "figures.py"
ORIG = {f: f.read_text() for f in (E, S, A, F)}
NEW = {"id": f"{LESSON}-L2-90", "level": 2, "kind": ["calculation"], "text": "Suljetun astian kaasun lämpötila nousee arvosta $20\\,{}^\\circ\\text{C}$ arvoon $45\\,{}^\\circ\\text{C}$. Kuinka paljon lämpötila muuttuu kelvineinä?",
       "answer": 25, "unit": "K", "tolerance": 0.02}
SOL = f"## {LESSON}-L2-90\n**Annettu:** $\\theta_1 = 20\\,{{}}^\\circ\\text{{C}}$, $\\theta_2 = 45\\,{{}}^\\circ\\text{{C}}$\n**Kysytty:** $\\Delta T$\n**Vastaus:** $\\Delta T = 25\\,\\text{{K}}$\n"
def put(entries=(NEW,), level="level2", drop=None, edit=None, sol=SOL, ans=f'a["{LESSON}-L2-90"] = 45 - 20\n', fig=None):
    """The exercise set as passed, with `entries` added to `level`, `drop` removed, `edit(ex)` applied, `fig` (old, new) in figures.py."""
    for f in (E, S, A, F): f.write_text(ORIG[f])
    ex = json.loads(ORIG[E]); ex[level] += [dict(e) for e in entries]
    if drop: ex = {k: [e for e in v if e["id"] != drop] for k, v in ex.items()}
    if edit: edit(ex)
    old_sol = re.sub(rf"^## {drop}\n.*?(?=^## |\Z)", "", ORIG[S], flags=re.S | re.M) if drop else ORIG[S]
    E.write_text(json.dumps(ex, ensure_ascii=False, indent=2)); S.write_text(old_sol.rstrip("\n") + "\n\n" + sol)
    head, _, tail = ORIG[A].rpartition("\nprint("); A.write_text(head + "\n" + ans + "print(" + tail)
    if fig: F.write_text(ORIG[F].replace(*fig, 1))
def ex_scope(): return run(t, "reviews.py", "scope", LESSON, "--exercises")[1]
put(); out = ex_scope()
expect("one exercise added: delta for all three, category added-exercise", out.count(": delta") == 3 and "categories=added-exercise" in out and "full" not in out, out)
expect("... and the lesson's own hash is unchanged", h(t) == HL)
code, o2 = run(t, "review_packet.py", LESSON, "--role", "science", "--exercises"); xs = (X / "review/packet-science.md").read_text()
expect("added-exercise science packet: the new exercise in full, answers.py, the whole set listed, the previous report, the scope line, no SVG",
       code == 0 and "Delta review: whole exercises added" in xs and f"#### {LESSON}-L2-90" in xs and "## " + LESSON + "-L2-90" in xs and "answers.py (now" in xs
       and "The whole set now" in xs and f"`{LESSON}-L1-01`" in xs and "Your previous report" in xs and f"SCOPE: delta added-exercise from {H0} base {B0[:12]}" in xs and "<svg" not in xs, o2 + xs[:300])
code, o2 = run(t, "review_packet.py", LESSON, "--role", "pedagogy", "--exercises"); xp = (X / "review/packet-pedagogy.md").read_text()
expect("... pedagogy packet: the same exercise and list, no answers.py", code == 0 and "whole exercises added" in xp and "The whole set now" in xp and "answers.py (now" not in xp, o2)
code, o2 = run(t, "review_packet.py", LESSON, "--role", "visual", "--exercises"); xv = (X / "review/packet-visual.md").read_text()
expect("... visual packet: the same delta", code == 0 and "Mode: **delta**" in xv and "whole exercises added" in xv and "SCOPE: delta added-exercise" in xv, o2)
put(drop=f"{LESSON}-L2-07"); out = ex_scope()   # its solution goes with it
expect("one exercise replaced (an id removed, another added): delta for all three", out.count(": delta") == 3 and "categories=added-exercise" in out, out)
def rewrite(ex): ex["level3"][-1]["text"] = "Täysin uusi tehtävä: polkupyörän renkaan ilmanpaine mitataan aamulla ja iltapäivällä, ja tulos selitetään hiukkasmallilla."
sol5 = re.search(rf"^## {LESSON}-L3-05\n.*?(?=^## |\Z)", ORIG[S], re.S | re.M).group(0)
put(entries=(), sol="", ans="", edit=rewrite); S.write_text(ORIG[S].replace(sol5, f"## {LESSON}-L3-05\nUusi ratkaisu: renkaan tilavuus pysyy lähes vakiona, joten paine kasvaa lämpötilan mukana.\n\n"))
out = ex_scope()
expect("an exercise rewritten as a whole under its own id: a replacement, delta", out.count(": delta") == 3 and "categories=added-exercise" in out, out)
put(edit=lambda ex: ex["level1"][0].update(text=ex["level1"][0]["text"].replace("a", "e", 1))); out = ex_scope()
expect("one added AND one character of another exercise changed: as before (not added-exercise; pedagogy full)", "pedagogy: full" in out and "added-exercise" not in out, out)
put(sol=SOL, ans=f'a["{LESSON}-L2-90"] = 45 - 20\na["{LESSON}-L1-01"] = -1\n'); out = ex_scope()
expect("one added and a surviving exercise's answer changed in answers.py: as before", "answers" in out and "added-exercise" not in out, out)
VAR = ('\n\nFIGURES = {', '\n\ndef few_points():\n    f = Fig("fy33-few", 330, "Kolme mittauspistettä.")\n    return f.svg()\n\n\nFIGURES = {"few-points": few_points, ')
put(entries=(dict(NEW, figure=f"{LESSON}/few-points"),), fig=VAR); out = ex_scope()
expect("an added exercise that shows a new figure variant: delta for all three", out.count(": delta") == 3 and "categories=added-exercise" in out, out)
put(fig=("(100, 102.5)]:", "(100, 103.0)]:")); out = ex_scope()
expect("one added and the figure a surviving exercise shows changed: as before (figure, full)", "science: full" in out and "pedagogy: full" in out and "added-exercise" not in out, out)
# 8p: a new exercise beside a change of a surviving exercise's wording is no change of a level or id; a surviving exercise's level or id is
def reword(ex): ex["level1"][0]["text"] = ex["level1"][0]["text"].replace("a", "e", 1)
def relevel(ex): ex["level3"].append(dict(ex["level2"].pop(0), level=3))
put(edit=reword); out = ex_scope()
expect("8p: one added and a surviving exercise's wording changed: not a change of a level or id", "levels" not in out, out)
put(edit=relevel); out = ex_scope()
expect("8p: one added and a surviving exercise moved to another level: still a level change, pedagogy full", "levels" in out and "pedagogy: full" in out and "added-exercise" not in out, out)
put(entries=(), sol="", ans="", edit=lambda ex: ex["level2"][0].update(id=f"{LESSON}-L2-77")); out = ex_scope()
expect("8p: a surviving exercise's id changed: still a level or id change, pedagogy full", "levels" in out and "pedagogy: full" in out, out)
def scoped(name, frm=H0, base=B0):
    (X / "review" / f"{name}.md").write_text(f"VERDICT: PASS\nCONTENT-HASH: {h(t, part='exercises')}\nSCOPE: delta added-exercise from {frm} base {base[:12]}\n\n## Blocking\nnone\n")
put()
for n in ("science", "pedagogy", "visual"): scoped(n)
git(t, "add", "."); git(t, "commit", "-qm", "an exercise added, delta reviews")
code, out = run(t, "reviews.py", "verify")
expect("verify accepts the delta PASS of an added exercise", code == 0 and "ERROR" not in out and "exercises: reviewed" in out, out[-600:])
(X / "review" / "science.md").write_text(f"VERDICT: FAIL\nCONTENT-HASH: {h(t, part='exercises')}\n\n## Blocking\n- the added exercise is out of scope\n")
git(t, "add", "."); git(t, "commit", "-qm", "science FAIL, round 1")
N2 = dict(NEW, id=f"{LESSON}-L2-91")
put(entries=(NEW, N2), sol=SOL + "\n" + SOL.replace("L2-90", "L2-91"), ans=f'a["{LESSON}-L2-90"] = 45 - 20\na["{LESSON}-L2-91"] = 45 - 20\n'); out = ex_scope()
expect("after a FAIL the fix round is measured from the reviewer's last PASS: still a delta (added-exercise)", "science: delta" in out and "added-exercise" in out and "no earlier PASS" not in out, out)
scoped("science"); git(t, "add", "."); git(t, "commit", "-qm", "science PASS, round 2")
put(entries=(NEW, N2), sol=SOL + "\n" + SOL.replace("L2-90", "L2-91"), ans=f'a["{LESSON}-L2-90"] = 45 - 20\na["{LESSON}-L2-91"] = 46 - 20\n'); out = ex_scope()
expect("an added exercise passed and then fixed: measured from the earlier PASS it is still only added exercises (delta)", "science: delta" in out and "added-exercise" in out, out)
put(edit=lambda ex: ex["level1"][0].update(text=ex["level1"][0]["text"].replace("a", "e", 1)))
for n in ("science", "pedagogy", "visual"): scoped(n)
code, out = run(t, "reviews.py", "verify")
expect("verify rejects a delta PASS when another exercise changed too", code == 1 and "pedagogy's delta PASS covers changes that need its full review" in out, out[-600:])
put()
for n in ("science", "pedagogy", "visual"): scoped(n, frm="0" * 16)
code, out = run(t, "reviews.py", "verify")
expect("verify rejects a scope line whose base does not hold the hash it names", code == 1 and "does not hold hash" in out, out[-600:])
# 8c. the marker "(esimerkkiaineisto)" taken out of table captions (teacher 2026-11-15): all three reviewers carry over; any
# other change in the same file, a changed caption word included, is reviewed as usual
t = project(); X = t / "content/fi/FY3" / LESSON / "exercises"; E = X / "exercises.json"
E.write_text(re.sub(r'("caption": ")([^"]*)(")', r'\1\2 (esimerkkiaineisto)\3', E.read_text()))   # the passed version has the marker, whatever the real content has now
init_git(t)
for n in ("science", "pedagogy", "visual"): report(t, n, part="exercises")
git(t, "add", "."); git(t, "commit", "-qm", "exercise reviews")
E0 = E.read_text(); LAB = " (esimerkkiaineisto)"
expect("the passed exercise set has captions with the marker", E0.count(LAB + '"') >= 2, E0.count(LAB))
def cap(text): E.write_text(text); return run(t, "reviews.py", "scope", LESSON, "--exercises")[1]
out = cap(E0.replace(LAB + '"', '"'))
expect("the marker taken out of every caption: none for all three, category caption-label", out.count(": none") == 3 and "caption-label" in out, out)
out = cap(E0.replace(LAB + '"', '"', 1))
expect("... also out of one caption only", out.count(": none") == 3 and "caption-label" in out, out)
out = cap(E0.replace("Lämpömittarin A kalibrointi (esimerkkiaineisto)", "Lämpömittarin A kalibrointi"))
expect("... and the marker of a caption whose other words are kept", out.count(": none") == 3, out)
out = cap(E0.replace(LAB + '"', '"').replace("Lämpömittarin A kalibrointi", "Lämpömittarin B kalibrointi"))
expect("... but a changed caption word as well is reviewed as usual (not none)", "science: none" not in out and "caption-label" in out, out)
first = json.loads(E0)["level1"][0]["text"]
out = cap(E0.replace(LAB + '"', '"').replace(first[:12], first[:11] + "x", 1))
expect("... or another character of the file (a task text): reviewed as usual", "science: none" not in out, out)
out = cap(E0.replace('"unit": "K"', '"unit": "C"', 1) if '"unit": "K"' in E0 else E0.replace('"answer": ', '"answer": 1', 1))
expect("... an answer changed alone has no caption-label", "caption-label" not in out and "science: none" not in out, out)
_cj = lambda c: json.dumps({"data": {"caption": c}}, indent=1)
expect("... a label added to a caption, or a word changed beside it, is not the category", rv.caption_removed(_cj("A"), _cj("A (esimerkkiaineisto)")) == _cj("A") and rv.caption_removed(_cj("A (esimerkkiaineisto)"), _cj("B")) == _cj("A (esimerkkiaineisto)") and rv.caption_removed(_cj("A (esimerkkiaineisto)"), _cj("A")) == _cj("A"))
out = cap(E0.replace("(esimerkkiaineisto)", "(luonnos)"))
expect("... another parenthesis in its place is a changed caption, not none", "science: none" not in out, out)
cap(E0.replace(LAB + '"', '"')); code, out = run(t, "reviews.py", "carry", LESSON, "--exercises")
expect("carry records caption-label for all three reviewers", sum(l.endswith("(the marker \"esimerkkiaineisto\" taken out of table captions, nothing else (teacher 2026-11-15, 2026-11-16))") for l in out.splitlines()) == 3, out)
code, out = run(t, "reviews.py", "verify")
expect("verify re-derives the caption-label carry in CI", code == 0 and "ERROR" not in out, out[-400:])
cap(E0.replace(LAB + '"', '"').replace("Lämpömittarin A kalibrointi", "Lämpömittarin B kalibrointi"))
code, out = run(t, "reviews.py", "verify")
expect("... and the carry no longer holds once the same file also changed a caption word", "exercises: draft" in out, out[-400:])
expect("... the new forms are the category line for line too", rv.caption_removed(_cj("Kärryn nopeus, esimerkkiaineisto"), _cj("Kärryn nopeus")) == _cj("Kärryn nopeus") and rv.caption_removed(_cj("Esimerkkiaineisto: sama jännite"), _cj("Sama jännite")) == _cj("Sama jännite") and rv.caption_removed(_cj("Example data: three boiler options"), _cj("Three boiler options")) == _cj("Three boiler options"))
expect("... but not with a changed letter beside it, or a lower-case start kept", rv.caption_removed(_cj("Esimerkkiaineisto: sama jännite"), _cj("sama jännite")) == _cj("Esimerkkiaineisto: sama jännite") and rv.caption_removed(_cj("Kärryn nopeus, esimerkkiaineisto"), _cj("Kärryn vauhti")) == _cj("Kärryn nopeus, esimerkkiaineisto"))
# 8l-b. the same without parentheses (teacher 2026-11-16): "…, esimerkkiaineisto" and "Esimerkkiaineisto: …"
t = project(); E = t / "content/fi/FY3" / LESSON / "exercises" / "exercises.json"; _n = iter(range(99))
E.write_text(re.sub(r'("caption": ")([^"]*)(")', lambda m: m.group(1) + (m.group(2) + ", esimerkkiaineisto" if next(_n) % 2 else "Esimerkkiaineisto: " + m.group(2)[:1].lower() + m.group(2)[1:]) + m.group(3), E.read_text()))
init_git(t)
for n in ("science", "pedagogy", "visual"): report(t, n, part="exercises")
git(t, "add", "."); git(t, "commit", "-qm", "exercise reviews")
E1 = E.read_text()
expect("the passed set has both forms", ', esimerkkiaineisto"' in E1 and '"Esimerkkiaineisto: ' in E1, E1[:300])
E.write_text(re.sub(r'("caption": ")([^"]*)(")', lambda m: m.group(1) + rv.caption_label_free(m.group(2)) + m.group(3), E1))
out = run(t, "reviews.py", "scope", LESSON, "--exercises")[1]
expect("both forms taken out: none for all three, category caption-label", out.count(": none") == 3 and "caption-label" in out, out)
code, out = run(t, "reviews.py", "carry", LESSON, "--exercises"); code, out = run(t, "reviews.py", "verify")
expect("... and verify re-derives that carry", code == 0 and "ERROR" not in out, out[-400:])
E.write_text(E1.replace("Esimerkkiaineisto: l", "l", 1))
out = run(t, "reviews.py", "scope", LESSON, "--exercises")[1]
expect("... a marker taken out without its capital letter is a changed caption (not none)", "science: none" not in out, out)
expect("the marker is a caption's alone: a text mention is no caption", rv.caption_free(json.dumps({"text": "Taulukko (esimerkkiaineisto)."})) == json.dumps({"text": "Taulukko (esimerkkiaineisto)."}, indent=1))
for old, new in (("Taulukko (esimerkkiaineisto)", "Taulukko"), ("Table (example data)", "Table"), ("Table (example data set)", "Table"),
                 ("Energiat (esimerkkiaineisto, NNDC NuDat 3)", "Energiat (NNDC NuDat 3)"), ("A (esimerkkiaineisto) B", "A B"),
                 # without parentheses too (teacher 2026-11-16, work queue 8l-b): fi, fi-easy and en
                 ("Kärryn nopeus, esimerkkiaineisto", "Kärryn nopeus"), ("Velocity of the cart, example data", "Velocity of the cart"),
                 ("Pisteen $P$ potentiaali eri kuormilla, esimerkkiaineisto", "Pisteen $P$ potentiaali eri kuormilla"),
                 ("Esimerkkiaineisto: sama jännite kolmella mittausalueella", "Sama jännite kolmella mittausalueella"),
                 ("Esimerkkiaineisto: öljypisaroiden leijumisjännitteet", "Öljypisaroiden leijumisjännitteet"),
                 ("Example data: three boiler options", "Three boiler options"),
                 ("Lasien taitekertoimet (tyypillisiä arvoja, esimerkkiaineisto)", "Lasien taitekertoimet (tyypillisiä arvoja)"),
                 ("Refractive indices of the glasses (typical values, example data)", "Refractive indices of the glasses (typical values)"),
                 ("Ilman lämpötila vuorokauden aikana (keksitty esimerkkiaineisto)", "Ilman lämpötila vuorokauden aikana"),
                 ("R-luku yhdellä mittausasemalla (keksitty esimerkkiaineisto, ei mittaustulos)", "R-luku yhdellä mittausasemalla"),
                 ("R number at one measuring station (an invented example data set, not a measurement)", "R number at one measuring station"),
                 # a word of its own is no marker: it stays
                 ("Esimerkkiaineiston keruu", "Esimerkkiaineiston keruu"), ("Esimerkkiaineisto ja malli", "Esimerkkiaineisto ja malli"),
                 ("Mittaus, esimerkkiaineisto ja malli", "Mittaus, esimerkkiaineisto ja malli"), ("Example data sets compared", "Example data sets compared")):
    expect(f"caption_free: {old!r} → {new!r}", json.loads(rv.caption_free(json.dumps({"data": [{"caption": old}]})))["data"][0]["caption"] == new)
expect("caption-label: nobody needs to look", rv.RULES["caption-label"] == ("none", "none", "none"))
# an item (koe, sovella, unit): its view leaves the marker out, so a carry-item over a pure marker removal is accepted
class _Src:
    def __init__(self, txt): self.txt = txt
    def read(self, rel, binary=False): return self.txt if rel.endswith("tasks.json") else None
_T = json.dumps({"tasks": [{"data": {"caption": "Mittaukset (esimerkkiaineisto)"}}]}); _T2 = json.dumps({"tasks": [{"data": {"caption": "Mittaukset"}}]})
_T3 = json.dumps({"tasks": [{"data": {"caption": "Muut mittaukset"}}]})
import practice as _pr
_fk, _fl = None, None
expect("item_view: a sovella set's tasks.json with and without the marker has one view; another caption has another",
       rv.item_view("sovella", "FY3", "fi", _Src(_T)) == rv.item_view("sovella", "FY3", "fi", _Src(_T2)) != rv.item_view("sovella", "FY3", "fi", _Src(_T3)))
# an item's solutions.md cut into paragraphs or a list (work queue 8c): one view with `paragraphs`, and only with it
class _SrcMd:
    def __init__(self, md): self.md = md
    def read(self, rel, binary=False): return self.md if rel.endswith("solutions.md") else _T2 if rel.endswith("tasks.json") else None
_M1 = "## FY3-1\n**Vastaus:** $2\\,\\text{m}$, kaksi numeroa. Koska $a$ ja $b$ tunnetaan.\n"
_M2 = "## FY3-1\n**Vastaus:** $2\\,\\text{m}$, kaksi numeroa.\n\n- Koska $a$ ja\n- $b$ tunnetaan.\n"
_M3 = "## FY3-1\n**Vastaus:** $2\\,\\text{m}$, kolme numeroa.\n\nKoska $a$ ja $b$ tunnetaan.\n"
_iv = lambda md, **kw: rv.item_view("sovella", "FY3", "fi", _SrcMd(md), **kw)
expect("item_view: a solution step cut into paragraphs and a list has the view it had with paragraphs=True", _iv(_M1, paragraphs=True) == _iv(_M2, paragraphs=True))
expect("... not without it, and not when a word changes", _iv(_M1) != _iv(_M2) and _iv(_M1, paragraphs=True) != _iv(_M3, paragraphs=True))
expect("... a list is no re-broken chain: the reflow view alone tells them apart", _iv(_M1, reflow=True) != _iv(_M2, reflow=True))
# 9. a translated exercise set (teacher 2026-11-12): numerically equivalent to the Finnish set, whose science PASS is
# current → the science review carries over; pedagogy and visual review the language; anything numeric differs → as before
_p = []
expect("translation compare: {,} and . and whitespace are the same formula", rv._tr_text("Massa on $m = 4{,}2\\,\\text{kg}$.", "The mass is $m=4.2\\,\\text{kg}$.", _p))
expect("... a sub- or superscript label may be translated, and is recorded for the one-to-one check",
       rv._tr_text("$E_\\text{sähkö} = 216\\,\\text{kJ}$", "$E_\\text{elec} = 216\\,\\text{kJ}$", _p) and ("sähkö", "elec") in _p)
expect("... a unit inside \\text{} may not change", not rv._tr_text("$t = 230\\,\\text{vrk}$", "$t = 230\\,\\text{s}$", []))
expect("... formulas in another order are equivalent (0c: where a language puts a formula in its sentence is no science)", rv._tr_text("$4{,}0\\,\\text{s}$ ja $18\\,\\text{m}$", "$18\\,\\text{m}$ in $4.0\\,\\text{s}$", []))
expect("... nor another number outside a formula", not rv._tr_text("Haaran 3 virta", "The current of branch 2", []))
expect("... an option's text keeps its labels in order", not rv._tr_text("Kappale B", "Body D", [], labels=True) and rv._tr_text("Kappale B", "A body B", [], labels=True))
expect("8p: a translated \\text{} word outside a sub- or superscript is the same formula (fy8-11 L3-05)", rv._tr_text("$m_\\text{hiili}=\\dfrac{E}{\\text{lämpöarvo}}$", "$m_\\text{carbon}=\\dfrac{E}{\\text{heating value}}$", []))
expect("... a changed number, operator or symbol beside it still differs", not rv._tr_text("$m=\\dfrac{E}{\\text{lämpöarvo}}$", "$m=\\dfrac{2E}{\\text{heating value}}$", []) and not rv._tr_text("$m=\\dfrac{E}{\\text{lämpöarvo}}$", "$m=E\\cdot\\text{heating value}$", []))
expect("8q: a lone label formula is a known pair (ka / avg; fy8-13 L2-03)", rv._tr_text("alaindeksi $\\text{ka}$ tarkoittaa keskiarvoa", "the subscript $\\text{avg}$ means the average", []) and rv._tr_text("$H_\\text{ka}$ ja $\\text{ka}$", "$H_\\text{avg}$ and $\\text{mean}$", []))
expect("8q: a unit written as a formula in one text and as a word in the other is the same unit (fy8-13 L2-09)", rv._tr_text("Annos on 5 mSv.", "Annos on 5 $\\text{mSv}$.", []) and rv._tr_text("Yksikkö $\\text{mSv}$.", "Yksikkö mSv.", []))
expect("8s: a capital inside a word is no option label (fy8-14 L1-06: X-radiation / röntgensäteilyä)", rv._tr_text("röntgensäteilyä", "X-radiation", [], labels=True) and rv._tr_text("Kappale B", "A body B", [], labels=True))
expect("8s: real labels stay strict: (A), a), X:", not rv._tr_text("(A) kappale", "(B) body", [], labels=True) and not rv._tr_text("X: kappale", "Y: body", [], labels=True))
expect("8q: a lone unit formula beside the unit's name in words (fy8-13 L2-09: millisieverteinä)", rv._tr_text("Anna tulos millisieverteinä.", "Tulos on millisieverteinä ($\\text{mSv}$).", []) and not rv._tr_text("Anna tulos millisieverteinä.", "Tulos on ($\\text{Sv}$).", []))
expect("8q: a lone label formula without a known pair or another unit still differs", not rv._tr_text("$\\text{ka}$", "$\\text{foo}$", []) and not rv._tr_text("Yksikkö mSv.", "Yksikkö $\\text{Sv}$.", []) and not rv._tr_text("$\\text{mSv}$", "$\\text{Sv}$", []) and not rv._tr_text("$\\text{kg}$", "$\\text{g}$", []))
expect("8q: a unit with a number still stays strict (kg → g, mSv → Sv, the number or symbol changes)", not rv._tr_text("$m = 4\\,\\text{kg}$", "$m = 4\\,\\text{g}$", []) and not rv._tr_text("$4\\,\\text{mSv}$", "$4\\,\\text{Sv}$", []) and not rv._tr_text("$H_\\text{ka}=5$", "$H_\\text{avg}=6$", []) and not rv._tr_text("$H_\\text{ka}=5$", "$c_\\text{avg}=5$", []))
def _ch(ans, a, b, ca=True, n=None): return {"kind": ["concept"], "answer": ans, "unit": "", "tolerance": 0.02, "choices": [{"text": a, **({"correct": True} if ca else {})}, {"text": b, **({} if ca else {"correct": True})}]}
_cf = _ch("Positroni annihiloituu.", "Positroni annihiloituu.", "Se kasvaa.")
_ce = _ch("The positron annihilates.", "The positron annihilates.", "It grows.")
_td = lambda x, y: rv._tr_data(rv._choice_answer(x), rv._choice_answer(y), [])
expect("8r: a translated choice answer (the correct option's text) is no difference (fy8-14 L1-06)", _td(_cf, _ce))
expect("8r: another correct option differs", not _td(_cf, _ch("It grows.", "The positron annihilates.", "It grows.", ca=False)))
expect("8r: a numeric answer that differs still differs", not _td({"answer": 4.2, "unit": "m"}, {"answer": 4.3, "unit": "m"}))
expect("8r: an answer naming no option is compared as text as before (a changed number differs)", not _td({**_cf, "answer": "Muu 3"}, {**_ce, "answer": "Other 4"}))
t = project(); FI = t / "content/fi/FY3" / LESSON; EN = t / "content/en/FY3" / LESSON
shutil.copytree(FI, EN, ignore=shutil.ignore_patterns("review"))
XE = EN / "exercises"; _ej = XE / "exercises.json"; _ex = json.loads(_ej.read_text())
_ex["level1"][0]["text"] = "Translated: " + _ex["level1"][0]["text"]; _ej.write_text(json.dumps(_ex, ensure_ascii=False, indent=2))
_sol = XE / "solutions.md"; SOL_EN = _sol.read_text().replace("**Vastaus:**", "**Answer:**"); _sol.write_text(SOL_EN)
git(t, "init", "-q"); git(t, "config", "user.email", "t@t"); git(t, "config", "user.name", "t"); git(t, "add", "."); git(t, "commit", "-qm", "fi and en")
for n in ("science", "pedagogy", "visual"): report(t, n, part="exercises")
git(t, "add", "."); git(t, "commit", "-qm", "fi exercise reviews")
def en(*a): return run(t, "reviews.py", *a, LESSON, "--exercises", "--lang", "en")[1]
def en_report(name, verdict="PASS"):
    (XE / "review").mkdir(exist_ok=True); (XE / "review" / f"{name}.md").write_text(f"VERDICT: {verdict}\nCONTENT-HASH: {en('hash').strip()}\n\n## Blocking\nnone\n")
out = en("scope")
expect("(a) fi science PASS current, en numerically equivalent: en science none (translation-of-passed), pedagogy and visual as usual",
       "science: none" in out and "categories=translation-of-passed" in out and "pedagogy: full" in out and "visual: full" in out, out)
out = en("carry")
expect("... carry writes the science row from the Finnish hash", "science: carried over" in out and "translation-of-passed" in (XE / "review/carry.tsv").read_text()
       and h(t, part="exercises") in (XE / "review/carry.tsv").read_text(), out)
en_report("pedagogy"); en_report("visual"); git(t, "add", "."); git(t, "commit", "-qm", "en carried, en pedagogy and visual")
out = en("status")
expect("... en exercises reviewed, science carried over from the Finnish set", "exercises: reviewed" in out and "science=PASS (carried over: translation-of-passed)" in out, out)
code, out = run(t, "reviews.py", "verify")
expect("... verify accepts the carry", code == 0 and "ERROR" not in out, out[-600:])
en_report("science", "FAIL"); out = en("scope")
expect("an en science FAIL for its current hash is never overridden by the Finnish PASS", "science: none" not in out and "translation-of-passed" not in en("status"), out)
(XE / "review/science.md").unlink()
_b = re.search(r"\$[^$]*\d[^$]*\$", SOL_EN.split("**Answer:**", 1)[1]).group(0); _sol.write_text(SOL_EN.replace(_b, _b.replace(re.search(r"\d", _b).group(0), "7" if re.search(r"\d", _b).group(0) != "7" else "8", 1), 1))
out = en("scope")
expect("(b) en with a different number in one solution's formula: science not none", "science: none" not in out and "translation-of-passed" not in out, out)
_rows = (XE / "review/carry.tsv").read_text().splitlines()
(XE / "review/carry.tsv").write_text("\n".join(_rows + ["\t".join(_rows[-1].split("\t")[:3] + [en("hash").strip()] + _rows[-1].split("\t")[4:])]) + "\n")   # forged
code, out = run(t, "reviews.py", "verify")
expect("... and verify rejects a carry row forged for that version", code == 1 and "not numerically equivalent" in out, out[-600:])
_sol.write_text(SOL_EN); git(t, "checkout", "-q", "--", "content/en"); expect("... restored: reviewed again", "exercises: reviewed" in en("status"), en("status"))
_fs = FI / "exercises/solutions.md"; _fs.write_text(_fs.read_text().replace("**Vastaus:**", "**Vastaus (uusi):**", 1))
out = en("status")
# the invariant: the row binds the Finnish hash it was carried from, so once the Finnish set changes (its science report no
# longer current) the row counts for nothing and the en science review is no longer passed; verify has nothing to re-derive
expect("(c) the fi set changed after the carry (fi hash new, fi science stale): the en science carry no longer counts",
       "exercises: draft" in out and "science=missing" in out and "translation-of-passed" not in en("scope"), out)
code, out = run(t, "reviews.py", "verify")
expect("... verify: no error, the en exercise set is simply not reviewed", code == 0 and "ERROR" not in out, out[-600:])

# 8n. an item's reflow carry (work queue 5f, teacher 2026-11-15): a unit's (or a Sovella set's or an example exam's)
# calculation chain re-broken into an aligned display formula carries its science and pedagogy PASS, never the visual one;
# a changed number, word or sign carries nothing, and verify re-derives the rows
UNIT = "fy9-kokeellisuus"
def unit_project():
    tmp = pathlib.Path(tempfile.mkdtemp())
    skip = lambda d, names: [n for n in names if n in ("__pycache__", "review")]
    for d in ("scripts", "lang", "templates", "docs/fy9", f"content/fi/units/{UNIT}", f"lessons/units/{UNIT}"):
        if (SRC / d).is_dir(): shutil.copytree(SRC / d, tmp / d, ignore=skip)
    for f in ("local-courses.json", "curriculum.json", "glossary.json", "competencies.json", "CLAUDE.md", "NOTES.md",
              "docs/teacher-figures.tsv", "docs/presentation-only.tsv"):
        if (SRC / f).is_file(): (tmp / f).parent.mkdir(parents=True, exist_ok=True); shutil.copy(SRC / f, tmp / f)
    return tmp
t = unit_project(); init_git(t); U = t / "content/fi/units" / UNIT; um = U / "unit.md"
CH3 = "$v = s : t = 12{,}0\\,\\text{m} : 4{,}0\\,\\text{s} = 3{,}0\\,\\text{m/s}$"
src3 = um.read_text().rstrip("\n") + "\n\nEsimerkiksi " + CH3 + ", joten nopeus on pieni.\n"; um.write_text(src3)
uh = lambda: run(t, "units.py", "hash", UNIT)[1].strip()
def ureport(name, verdict="PASS"):
    (U / "review").mkdir(exist_ok=True); (U / "review" / f"{name}.md").write_text(f"VERDICT: {verdict}\nCONTENT-HASH: {uh()}\n\n## Blocking\nnone\n")
for n in ("science", "pedagogy", "visual"): ureport(n)
git(t, "add", "."); git(t, "commit", "-qm", "unit reviewed")
AL3 = "Esimerkiksi $$\n\\begin{aligned}\nv &= s : t \\\\\n&= 12{,}0\\,\\text{m} : 4{,}0\\,\\text{s} \\\\\n&= 3{,}0\\,\\text{m/s}\n\\end{aligned}\n$$, joten nopeus on pieni."
def ulift(new_text):
    um.write_text(src3.replace("Esimerkiksi " + CH3 + ", joten nopeus on pieni.", new_text, 1)); (U / "review/carry.tsv").unlink(missing_ok=True)
    return run(t, "reviews.py", "carry-item", "unit", UNIT)[1]
out = ulift(AL3)
expect("a unit's inline chain lifted into an aligned display formula: science and pedagogy carried over (reflow), visual needed",
       "science: carried over" in out and "pedagogy: carried over" in out and "visual: calculation chains re-broken into rows: delta review needed" in out
       and "reflow" in (U / "review/carry.tsv").read_text() and "draft" in out, out)
ureport("visual"); out = run(t, "reviews.py", "carry-item", "unit", UNIT)[1]
expect("... and with the visual reviewer's PASS of the new hash the unit is reviewed", out.rstrip().endswith("reviewed"), out)
git(t, "add", "."); git(t, "commit", "-qm", "reflow carried, visual passed")
code, out = run(t, "reviews.py", "verify")
expect("... verify re-derives the unit's reflow carry", not re.search(rf"ERROR \S*{UNIT}", out), out[-600:])
for what, new_text in (("a number", AL3.replace("4{,}0", "4{,}1")), ("a sign", AL3.replace("s : t", "s \\cdot t")),
                       ("a word", AL3.replace("nopeus on pieni", "nopeus on melko pieni"))):
    git(t, "checkout", "-q", "HEAD~1", "--", "content"); (U / "review/visual.md").write_text((U / "review/visual.md").read_text())
    out = ulift(new_text)
    expect(f"... but a changed {what} with the re-break carries nothing", "science: carried over" not in out and "review needed" in out, out)
git(t, "checkout", "-q", "HEAD", "--", "content")
rows = (U / "review/carry.tsv").read_text().splitlines()
(U / "review/carry.tsv").write_text("\n".join(rows + ["\t".join([rows[-1].split("\t")[0], "visual"] + rows[-1].split("\t")[2:])]) + "\n")   # forged
(U / "review/visual.md").write_text((U / "review/visual.md").read_text().replace(uh(), rows[-1].split("\t")[2]))   # the visual PASS of the version before the re-break
code, out = run(t, "reviews.py", "verify")
expect("... and verify rejects a visual carry row over a reflow", code == 1 and "does not carry the visual review" in out, out[-600:])
# a unit's text cut into paragraphs and a list, word for word the same (work queue 8c): science and pedagogy carry over
# (md-paragraphs), the visual reviewer looks; a changed word with it carries nothing
git(t, "checkout", "-q", "HEAD", "--", "content"); (U / "review/carry.tsv").unlink(missing_ok=True)
for n in ("science", "pedagogy", "visual"): ureport(n)
git(t, "add", "."); git(t, "commit", "-qm", "unit reviewed again")
src4 = um.read_text()
PA = ", joten nopeus on pieni."   # after the aligned chain the re-break test left
def usplit(new_text):
    um.write_text(src4.replace(PA, new_text, 1)); (U / "review/carry.tsv").unlink(missing_ok=True)
    return run(t, "reviews.py", "carry-item", "unit", UNIT)[1]
expect("... (the chain is there to cut after)", PA in src4)
out = usplit(",\n\n- joten nopeus\n- on pieni.")
expect("a unit's text cut into paragraphs and a list: science and pedagogy carried over (md-paragraphs), visual needed",
       "science: carried over" in out and "pedagogy: carried over" in out and "visual: texts cut into paragraphs or lists: delta review needed" in out
       and "md-paragraphs" in (U / "review/carry.tsv").read_text() and "reflow" not in (U / "review/carry.tsv").read_text(), out)
ureport("visual"); git(t, "add", "."); git(t, "commit", "-qm", "paragraphs carried, visual passed")
code, out = run(t, "reviews.py", "verify")
expect("... verify re-derives the unit's md-paragraphs carry", not re.search(rf"ERROR \S*{UNIT}", out), out[-600:])
git(t, "checkout", "-q", "HEAD~1", "--", "content")
out = usplit(",\n\n- joten nopeus\n- on melko pieni.")
expect("... but a changed word with the paragraph breaks carries nothing", "science: carried over" not in out and "review needed" in out, out)

# 8o. options rewritten around an unchanged "correct": true (work queue 8o, coordinator 2026-11-17; 8j FY5, #661): the
# JSON of an inquiry or an exercise set is compared key by key, so an unchanged key-value pair is no change; a changed
# "correct", a numeric answer or a new correct option is still "experiment" (full science and pedagogy reviews)
# the other activities make the file as long as a real inquiry: over 200 lines difflib's autojunk takes the frequent lines
# ("correct": true, braces) for junk, aligns the rewritten options around them and so reports the unchanged line (fy5-11)
_REST = [{"id": f"tutki-{i}", "stage": "tutki", "type": "choice", "prompt": f"Kysymys {i}?",
          "choices": [{"text": f"Vaihtoehto {i}a.", "correct": True, "feedback": "Oikein."}, {"text": f"Vaihtoehto {i}b.", "feedback": "Ei."}]} for i in range(12)]
def _inq(prompt, opts, **kw):
    return rv._view(json.dumps({"activities": [{"id": "herata-1", "stage": "herata", "type": "choice", "title": "Kertaa", "prompt": prompt, "choices": opts, **kw}] + _REST}, ensure_ascii=False), "x/inquiry.json", False)
_O = [{"text": "Aallonpituus puolittuu.", "correct": True, "feedback": "Oikein, koska nopeus pysyy samana."},
      {"text": "Aallonpituus kaksinkertaistuu.", "feedback": "Taajuus kertoo, kuinka monta harjaa lähtee sekunnissa."},
      {"text": "Aallonpituus pysyy samana.", "feedback": "Yhtälössä on kaksi muuta suuretta."}]
_N = [{"text": "Aallonpituus on pitkä.", "correct": True, "feedback": "Oikein, nopeus jaettuna taajuudella."},
      {"text": "Aallonpituus on lyhyt.", "feedback": "Kerroit nopeuden taajuudella, ja yksikkö ei ole metri."},
      {"text": "Aallonpituutta ei voi tietää.", "feedback": "Jaoit taajuuden nopeudella."}]
_A, _B = _inq("Aaltokone tekee aaltoja. Mitä aallonpituudelle tapahtuu?", _O), _inq("Avomereltä tulevat aallot osuvat aallonmurtajaan. Millainen on aallonpituus?", _N)
_cl = lambda a, b, rel="content/fi/FY5/fy5-11/inquiry.json": rv.classify(rel, rv._class_diff(rel, a, b), "fy5-11")
_ln = lambda a, b, rel="content/fi/FY5/fy5-11/inquiry.json": rv.classify(rel, list(rv.difflib.unified_diff(a.splitlines(), b.splitlines(), lineterm="", n=2)), "fy5-11")
expect("8o: the line diff took the unchanged \"correct\": true for a changed experiment (the bug)", "experiment" in _ln(_A, _B), str(_ln(_A, _B)))
expect("8o: compared key by key, options and prompt rewritten with \"correct\" where it was are wording alone (delta reviews)", _cl(_A, _B) == {"wording"}, str(_cl(_A, _B)))
_sc = lambda cats: {r: max((rv.RULES[c][i] for c in cats), key=("none", "delta", "full").index) for i, r in enumerate(("science", "pedagogy", "visual"))}
expect("... and so no reviewer is full", "full" not in _sc(_cl(_A, _B)).values(), str(_sc(_cl(_A, _B))))
_N2 = [dict(o) for o in _N]; del _N2[0]["correct"]; _N2[1]["correct"] = True
expect("8o: \"correct\" moved to another option is still experiment (full science and pedagogy)",
       "experiment" in _cl(_A, _inq("Avomereltä tulevat aallot osuvat aallonmurtajaan. Millainen on aallonpituus?", _N2)) and _sc({"experiment"})["science"] == "full")
expect("... even when every text stays as it was", _cl(_inq("Q?", _O), _inq("Q?", [dict(_O[0], correct=False), dict(_O[1], correct=True), _O[2]])) == {"experiment"})
expect("8o: a new option that is correct is experiment", "experiment" in _cl(_inq("Q?", _O), _inq("Q?", _O + [{"text": "Uusi.", "correct": True}])))
expect("8o: a changed numeric answer of an inquiry task is experiment", _cl(_inq("Q?", _O, answer=0.25), _inq("Q?", _O, answer=0.5)) == {"experiment"})
_num = _cl(_inq("Q?", _O), _inq("Q?", [dict(_O[0], text="Aallonpituus on $20\\,\\text{m}$."), _O[1], _O[2]]))
expect("8o: a number in an option's text is numbers (science delta), as on a line of its own, never experiment", "numbers" in _num and "experiment" not in _num, str(_num))
_two = lambda ids: rv._view(json.dumps({"activities": [{"id": i, "stage": "tutki", "type": "choice", "prompt": "P " + i} for i in ids]}), "x/inquiry.json", False)
expect("8o: activities found by their id; their order is still a structure change", _cl(_two(["a", "b"]), _two(["b", "a"])) == {"structure"}, str(_cl(_two(["a", "b"]), _two(["b", "a"]))))
expect("8o: an exercise's answer stays answers when the texts around it are rewritten",
       _cl(json.dumps({"level1": [{"id": "e1", "text": "Vanha.", "answer": 2.0}]}, indent=1), json.dumps({"level1": [{"id": "e1", "text": "Uusi.", "answer": 3.0}]}, indent=1),
           "content/fi/FY5/fy5-11/exercises/exercises.json") == {"wording", "answers"})
expect("8o: a file that is not JSON falls back to the line diff", rv._class_diff("x/inquiry.json", "{", "{]") == list(rv.difflib.unified_diff(["{"], ["{]"], lineterm="", n=2)))

# 8o. the same, when the change also re-breaks a calculation chain in the JSON (work queue 8o; fy5-11 and fy5-17 in #671):
# the reflow view is made of the JSON's string values, so the file is still compared key by key and an unchanged
# "correct": true is no change; a moved "correct" with the re-break is still experiment
t = project(); init_git(t); IQ = t / "content/fi/FY3" / LESSON / "inquiry.json"
for n in ("science", "pedagogy", "visual"): report(t, n)
git(t, "add", "."); git(t, "commit", "-qm", "lesson reviewed")
_IQ0 = json.loads(IQ.read_text())
def _rebreak_and_rewrite(move_correct=False):
    d = json.loads(json.dumps(_IQ0)); acts = {a["id"]: a for a in d["activities"]}
    hint = next(x for a in d["activities"] for x in a.get("hints", []) if isinstance(x, str) and " = \\dfrac{100}" in x)
    h_i = [a for a in d["activities"] if hint in a.get("hints", [])][0]; h_i["hints"][h_i["hints"].index(hint)] = hint.replace(" = \\dfrac{100}", "$\n$= \\dfrac{100}", 1)
    ch = acts["pr-pumppu"]["choices"]
    for i, c in enumerate(ch): c["text"] = f"Uusi vaihtoehto {'ABCD'[i]} renkaan ilmasta."; c["feedback"] = f"Uusi palaute {'ABCD'[i]} ilman määrästä."
    if move_correct: ch[0].pop("correct"); ch[1]["correct"] = True
    IQ.write_text(json.dumps(d, ensure_ascii=False, indent=2))
    return run(t, "reviews.py", "scope", LESSON)[1]
expect("8o: (the fixture has the chain to re-break and the option set)", any(" = \\dfrac{100}" in x for a in _IQ0["activities"] for x in a.get("hints", []) if isinstance(x, str)))
out = _rebreak_and_rewrite()
expect("8o: a chain re-broken and options rewritten around an unchanged \"correct\" in one inquiry.json: reflow and wording, no experiment",
       "reflow" in out and "wording" in out and "experiment" not in out and "science: full" not in out and "pedagogy: full" not in out, out)
out = _rebreak_and_rewrite(move_correct=True)
expect("8o: ... and with \"correct\" moved to another option, experiment and full science and pedagogy reviews",
       "experiment" in out and "science: full" in out and "pedagogy: full" in out, out)
_pr = lambda items: json.dumps({"prior": items, "vary": ["m"]}, ensure_ascii=False, indent=1)
_t = next(iter(rv.chapter_titles()))
expect("8o: a list of strings is one line per item, so a chapter reference renamed in one item is chapter-ref, as on its own line",
       _cl(_pr(["Teho kertoo energiasta (luku *Vanha nimi*)", "Toinen"]), _pr([f"Teho kertoo energiasta (luku *{_t}*)", "Toinen"])) == {"chapter-ref"},
       str(_cl(_pr(["Teho kertoo energiasta (luku *Vanha nimi*)", "Toinen"]), _pr([f"Teho kertoo energiasta (luku *{_t}*)", "Toinen"]))))
expect("8o: ... and an item of a list under an experiment key (vary) is still experiment",
       _cl(json.dumps({"vary": ["m", "v"]}, indent=1), json.dumps({"vary": ["m", "h"]}, indent=1)) == {"experiment"})
expect("8o: a JSON view of the string values keeps non-strings and keys", rv._json_strings('{"a": ["x", 1, true], "b": {"c": "y"}}', str.upper) == json.dumps({"a": ["X", 1, True], "b": {"c": "Y"}}, indent=1)
       and rv._json_strings("{", str.upper) is None)

# 0c. one presentation class: reflow, paragraphs, caption label and any mix of them; an order-free translation check;
# a report's own hash and a well-formed scope line (work queue 0c, 2026-11-17)
_fc = rv.format_categories
_MD = "**Tulos.** Lasketaan $a = b + c$ ja saadaan $x = 2{,}5\\,\\text{m}$, koska $m$ on vakio."
_MD2 = "**Tulos.**\n\n- Lasketaan\n$$\\begin{aligned} a &= b + c \\\\ &= d \\end{aligned}$$"
_A = "Lasketaan $a = b$\n$= c$ ja saadaan tulos. Sitten toinen asia."
_B = "Lasketaan\n\n$$\\begin{aligned} a &= b = c \\end{aligned}$$\n\n- ja saadaan tulos.\n- Sitten toinen asia."
expect("0c: reflow and a paragraph cut into a list on the same lines are both categories", _fc(_A, _B, "lesson.md") == {"reflow", "md-paragraphs"}, str(_fc(_A, _B, "lesson.md")))
expect("0c: a paragraph cut alone is md-paragraphs only", _fc("Yksi lause. Toinen lause.", "Yksi lause.\n\nToinen lause.", "lesson.md") == {"md-paragraphs"})
expect("0c: a chain re-broken alone is reflow only", _fc("$a = b$ $= c$", "$a = b = c$", "lesson.md") == {"reflow"})
expect("0c: ... a changed number in the rows is none of them", _fc(_A, _B.replace("= c", "= d"), "lesson.md") is None)
expect("0c: ... a changed word with a paragraph cut is none of them", _fc("Yksi lause. Toinen.", "Yksi lause.\n\nKolmas.", "lesson.md") is None)
expect("0c: ... a swapped sign in a chain is none of them", _fc("$a = b + c$", "$a = b - c$", "lesson.md") is None)
expect("0c: ... a whitespace-only difference is no presentation class", _fc("Sana  yksi.", "Sana yksi.", "lesson.md") is None)
_J = lambda cap, txt: json.dumps({"level1": [{"id": "x", "caption": cap, "text": txt}]}, indent=1, ensure_ascii=False)
expect("0c: the caption marker out, the text cut into paragraphs and a chain re-broken, in one JSON: three classes",
       _fc(_J("Taulukko (esimerkkiaineisto)", "Laske $a = b$ $= c$. Sitten d."), _J("Taulukko", "Laske $a = b = c$.\n\nSitten d."), "exercises.json") == {"caption-label", "reflow", "paragraphs"},
       str(_fc(_J("Taulukko (esimerkkiaineisto)", "Laske $a = b$ $= c$. Sitten d."), _J("Taulukko", "Laske $a = b = c$.\n\nSitten d."), "exercises.json")))
expect("0c: ... a marker added to a caption is no class", _fc(_J("Taulukko", "x"), _J("Taulukko (esimerkkiaineisto)", "x"), "exercises.json") is None)
expect("0c: ... a caption word changed with the marker is no class", _fc(_J("Taulukko (esimerkkiaineisto)", "x"), _J("Kaavio", "x"), "exercises.json") is None)
expect("0c: the same view serves an item: format_view equals chain_view then para_view",
       rv.format_view(_A, "lesson.md") == rv.format_view(_B, "lesson.md"))
_tt = lambda a, b: rv._tr_text(a, b, [])
expect("0c: a translation with an inline formula one place later in the sentence is still equivalent (en L3-05, $820{,}5$)",
       _tt("Massa on $820{,}5\\,\\text{g}$ ja tiheys $\\rho = 2{,}0$.", "Density is $\\rho = 2{,}0$ and the mass is $820{,}5\\,\\text{g}$."))
expect("0c: ... fi-easy L2-01, $0{,}1$ moved", _tt("Jos $x = 0{,}1$, niin $y = 2$.", "Niin $y = 2$, jos $x = 0{,}1$."))
expect("0c: ... but a changed number in a formula is not", not _tt("Massa $820{,}5\\,\\text{g}$.", "Mass $820{,}6\\,\\text{g}$."))
expect("0c: ... a formula lost or added is not", not _tt("Massa $m$ ja $F$.", "Mass $m$.") and not _tt("Massa $m$.", "Mass $m$ and $F$."))
expect("0c: ... a duplicated formula in place of another is not", not _tt("Massa $m$ ja $F$.", "Mass $m$ and $m$."))
expect("0c: ... a prose number that differs is not", not _tt("Massa $m$ on 12 kg.", "Mass $m$ is 13 kg."))
_p = []; rv._tr_text("A $E_\\text{sähkö}$ ja $F_\\text{x}$.", "$F_\\text{x}$ and $E_\\text{electric}$.", _p)
expect("0c: ... the subscript labels still pair one to one when the formulas swap places", sorted(_p) == [("sähkö", "electric"), ("x", "x")], str(_p))
_rt = _pl.Path(_tf.mkdtemp())
def _mk(lang, text):
    d = _rt / f"content/{lang}/FY3/fy3-3/review"; d.mkdir(parents=True, exist_ok=True); (d / "visual.md").write_text(text); return d.parent
_fi, _en = _mk("fi", "VERDICT: PASS\nCONTENT-HASH: aaaaaaaaaaaaaaaa\n"), _mk("en", "VERDICT: PASS\nCONTENT-HASH: bbbbbbbbbbbbbbbb\nSCOPE: vain ulkoasu, ei muuta\n")
_scope = rv.scope_claim(_en, "visual")
expect("0c: a free-form SCOPE line is read as malformed (report_problems turns it into an error)", _scope and _scope[0] == "malformed", str(_scope))
expect("0c: ... a well-formed one is not", rv.scope_claim(_mk("sv", "VERDICT: PASS\nCONTENT-HASH: cccccccccccccccc\nSCOPE: delta reflow from 0123456789abcdef base abcdef1\n"), "visual")[0] == ["reflow"])
expect("0c: report_problems and check-report exist and the CLI says what is wrong", "check-report" in rv.__doc__ and callable(rv.report_problems))

# 0e. a translation's presentation-only change, cut as the Finnish text, whose visual PASS is current: its visual review
# is the Finnish one's (work queue 0e; the rule text awaits the teacher's approval)
expect("0e: layout skeleton: the words are no part of it, the paragraph cut, a list item and the formulas per line are",
       rv.layout_skeleton("Yksi $a$ ja $b$.\n\nToinen.", "x.md") == rv.layout_skeleton("One $c$ and $d$.\n\nSecond.", "x.md")
       and rv.layout_skeleton("Yksi.\n\nToinen.", "x.md") != rv.layout_skeleton("One. Second.", "x.md")
       and rv.layout_skeleton("a\n- b", "x.md") != rv.layout_skeleton("a\nb", "x.md")
       and rv.layout_skeleton("a $x$ ja $y$", "x.md") != rv.layout_skeleton("a $x$", "x.md")
       and rv.layout_skeleton('{"t": "a\\n\\nb"}', "x.json") == rv.layout_skeleton("a\n\nb", "x.md"))
t = project(); FI = t / "content/fi/FY3" / LESSON; EN = t / "content/en/FY3" / LESSON
shutil.copytree(FI, EN, ignore=shutil.ignore_patterns("review"))
_fl, _el = FI / "lesson.md", EN / "lesson.md"
_el.write_text(_el.read_text().replace("Ydinajatus", "Core idea", 1))            # a word the Finnish text does not have
_para = next(m for m in re.finditer(r"^[A-ZÄÖ][^\n$#|<>]{150,}?[a-zä]\. (?=[A-ZÄÖ])", _fl.read_text(), re.M))
def _cut(text): return text.replace(_para.group(0), _para.group(0).rstrip() + "\n\n", 1)           # the paragraph cut in two at a sentence
git(t, "init", "-q"); git(t, "config", "user.email", "t@t"); git(t, "config", "user.name", "t"); git(t, "add", "."); git(t, "commit", "-qm", "fi and en")
def _rep(folder, name, hsh, verdict="PASS"):
    (folder / "review").mkdir(exist_ok=True); (folder / "review" / f"{name}.md").write_text(f"VERDICT: {verdict}\nCONTENT-HASH: {hsh}\n\n## Blocking\nnone\n")
def en0(*a): return run(t, "reviews.py", *a, LESSON, "--lang", "en")[1]
for n in ("science", "pedagogy", "visual"): _rep(FI, n, h(t)); _rep(EN, n, en0("hash").strip())
git(t, "add", "."); git(t, "commit", "-qm", "reviews")
expect("0e: setup: both languages reviewed", "reviewed" in en0("status") and "reviewed" in state(t), en0("status"))
_fl.write_text(_cut(_fl.read_text()))
_rep(FI, "visual", h(t))                                                           # the Finnish layout review of the new cut
out = en0("scope")
expect("0e (a) the paragraph is cut in Finnish only: en is not cut the same, visual is a delta as before", "visual: delta" in out and "fi-layout" not in out, out)
_el.write_text(_cut(_el.read_text()))
out = en0("scope")
expect("0e (b) cut in both, the Finnish visual PASS current: en visual none (fi-layout), science and pedagogy carried as before",
       "visual: none" in out and "fi-layout" in out and "science: none" in out and "pedagogy: none" in out, out)
out = en0("carry")
expect("0e ... carry writes the row and en is reviewed", "visual: carried over" in out and "fi-layout" in (EN / "review/carry.tsv").read_text() and en0("status").startswith("fy3-3: reviewed"), out + en0("status"))
git(t, "add", "."); git(t, "commit", "-qm", "layout in both")
code, out = run(t, "reviews.py", "verify")
expect("0e ... verify accepts it", code == 0 and "ERROR" not in out, out[-600:])
_el.write_text(_el.read_text().replace("Core idea", "Main idea", 1))
out = en0("scope")
expect("0e (c) a changed word with the cut: en visual is a delta again", "visual: none" not in out and "fi-layout" not in out, out)
_el.write_text(_el.read_text().replace("Main idea", "Core idea", 1))
_fl.write_text(_fl.read_text().replace("Ydinajatus", "Ydinajatus ja", 1))
out = en0("status")
expect("0e (d) the Finnish text changed afterwards (its visual PASS stale): the en carry counts for nothing", "visual=PASS" not in out and "draft" in out, out)
code, out = run(t, "reviews.py", "verify")
expect("0e ... verify has nothing to re-derive for it", code == 0 and "ERROR" not in out, out[-600:])
_fl.write_text(_fl.read_text().replace("Ydinajatus ja", "Ydinajatus", 1))
_el.write_text(_el.read_text().replace(_para.group(0).rstrip() + "\n\n", _para.group(0).rstrip() + "\n\n- ", 1))   # en cut into a list item where the Finnish text has a paragraph
_rows = (EN / "review/carry.tsv").read_text().splitlines(); _last = _rows[-1].split("\t")
(EN / "review/carry.tsv").write_text("\n".join(_rows + ["\t".join(_last[:3] + [en0("hash").strip()] + _last[4:])]) + "\n")   # a row forged for that version
code, out = run(t, "reviews.py", "verify")
expect("0e (e) a row forged for an en cut that is not the Finnish cut: verify rejects it", code == 1 and "not cut as the Finnish text" in out, out[-600:])
git(t, "checkout", "-q", "--", "content")
_rep(EN, "visual", en0("hash").strip(), "FAIL")
out = en0("scope")
git(t, "checkout", "-q", "--", "content")
_el.write_text(_cut(_el.read_text()));
(t / "docs/clipped-formulas").mkdir(parents=True, exist_ok=True)
(t / "docs/clipped-formulas/FY3.tsv").write_text(f"# head\nen/{LESSON}\t= \\dfrac{{a}}{{b}}\n")
out = en0("scope")
expect("0e (g) a known clipped formula on the en page is a check_layout warning: no carry, en visual is a delta", "visual: none" not in out and "fi-layout" not in out, out)
(t / "docs/clipped-formulas/FY3.tsv").write_text(f"# head\nfi-easy/{LESSON}\t= x\n")
expect("0e ... a row of another language does not count", "fi-layout" in en0("scope"), en0("scope"))
(t / "docs/clipped-formulas/FY3.tsv").unlink(); git(t, "checkout", "-q", "--", "content")
expect("0e (f) an en visual FAIL for its current hash is never overridden", "fi-layout" not in out, out)

# 8k. a text change the teacher read and approved (work queue 8k): `approve-text` records the exact file before and after
# with the source of the approval; the change is then "teacher-text" (none for all three), carry records it, any later edit
# changes the hash so the row no longer applies, and verify rejects a carry that relied on it
t = project(); init_git(t); L = t / "content/fi/FY3" / LESSON; p = L / "lesson.md"
for n in ("science", "pedagogy", "visual"): report(t, n)
src_md = p.read_text(); numline = next(l for l in src_md.splitlines() if re.search(r"\d", l) and not l.lstrip().startswith(("<", "#", "-", "`", "|", "{")) and len(l.split()) > 6)
edited = src_md.replace(numline, numline + " Lisälause 12 kg:sta.", 1); p.write_text(edited)
out = run(t, "reviews.py", "scope", LESSON)[1]
expect("8k: a text change nobody approved is reviewed as usual", "science: none" not in out and "teacher-text" not in out, out)
code, out = run(t, "reviews.py", "approve-text", LESSON, "--base", "HEAD")
expect("8k: approve-text without the source of the approval refuses and writes nothing", code != 0 and "source" in out and not (t / "docs/teacher-text.tsv").exists(), out)
code, out = run(t, "reviews.py", "approve-text", LESSON, "--base", "HEAD", "--source", "opettaja 2026-11-18, koordinaattorin kautta")
tsv = t / "docs/teacher-text.tsv"
expect("8k: approve-text records the file with its source", code == 0 and tsv.is_file() and "opettaja 2026-11-18, koordinaattorin kautta" in tsv.read_text() and f"{LESSON}\tcontent/fi/FY3/{LESSON}/lesson.md" in tsv.read_text(), out)
expect("8k: the rows are well formed", run(t, "reviews.py", "verify")[1].count("ERROR") == 0, run(t, "reviews.py", "verify")[1])
out = run(t, "reviews.py", "scope", LESSON)[1]
expect("8k: the approved change: none for all three reviewers, category teacher-text", out.count(": none") == 3 and "teacher-text" in out, out)
code, out = run(t, "reviews.py", "approve-text", LESSON, "--base", "HEAD", "--source", "uudelleen")
expect("8k: approving the same change twice adds no row", "0 text change(s) recorded" in out and tsv.read_text().count(f"{LESSON}\t") == 1, out)
run(t, "reviews.py", "carry", LESSON)
expect("8k: carry records teacher-text for all three reviewers", (L / "review/carry.tsv").read_text().count("teacher-text") == 3, (L / "review/carry.tsv").read_text())
git(t, "add", "."); git(t, "commit", "-qm", "approved text change")
expect("8k: verify accepts the carry while the text is as approved", run(t, "reviews.py", "verify")[0] == 0, run(t, "reviews.py", "verify")[1])
p.write_text(edited.replace("12 kg", "13 kg", 1))
out = run(t, "reviews.py", "scope", LESSON)[1]
expect("8k: an edit made after the approval is no longer approved (reviewed as usual)", "science: none" not in out and "teacher-text" not in out, out)
expect("8k: ... and the chapter is a draft again: the carry holds for the approved text only", ": draft" in state(t) and "science=stale" in state(t), state(t))
p.write_text(edited)
tsv_ok = tsv.read_text(); tsv.unlink()
out = run(t, "reviews.py", "verify")
expect("8k: verify rejects a carry in use whose approval row is gone", out[0] != 0 and "covers changes it must review" in out[1], out[1])
tsv.write_text(tsv_ok)
tsv.write_text(tsv.read_text() + "2026-11-18\tfi\tx\tlesson.md\tabc\tdef\t\n")
out = run(t, "reviews.py", "verify")
expect("8k: verify rejects a malformed row (hashes, empty source)", out[0] != 0 and "malformed row" in out[1], out[1])
# the helper: only text files, exact hashes
import reviews as _r8
_r8.teacher_text_rows = lambda: {("content/fi/FY3/x/lesson.md", _r8._pres_hash("a"), _r8._pres_hash("b")), ("content/fi/FY3/x/sim.js", _r8._pres_hash("a"), _r8._pres_hash("b"))}
expect("8k: text_approved: exactly the approved before and after", _r8.text_approved("content/fi/FY3/x/lesson.md", "a", "b") and not _r8.text_approved("content/fi/FY3/x/lesson.md", "a", "c") and not _r8.text_approved("content/fi/FY3/y/lesson.md", "a", "b"))
expect("8k: ... never code (a sim.js row covers nothing)", not _r8.text_approved("content/fi/FY3/x/sim.js", "a", "b") and not _r8.text_eligible("lessons/FY3/x/answers.py") and not _r8.text_eligible("tests/sims/x.json"))

expect("real project untouched", snapshot() == REAL)
print("\n" + ("all review tests passed" if not failures else f"{len(failures)} FAILED: " + ", ".join(failures)))
sys.exit(1 if failures else 0)
