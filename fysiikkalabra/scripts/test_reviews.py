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
expect("an answer changed: full science review of the exercises, pedagogy judges the diff", "science: full" in out and "pedagogy: delta" in out and "answer" in out, out)
code, out = run(t, "reviews.py", "scope", LESSON)
expect("... and the lesson's reviewers see no change", "science: delta (0 changed" in out and "pedagogy: delta (0 changed" in out, out)
e.write_text(json.dumps(json.loads((SRC / "content/fi/FY3" / LESSON / "exercises/exercises.json").read_text()), ensure_ascii=False, indent=2))
p.write_text(p.read_text().replace("0{,}37", "0{,}38", 1))
code, out = run(t, "reviews.py", "scope", LESSON)
expect("a number in a formula changed: full science review, pedagogy delta", "science: full" in out and "pedagogy: delta" in out and "number, formula" in out, out)
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
expect("an experiment's initial value changed: full science review", "science: full" in out, out)
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
expect("exercise developer packet: rules, brief and current exercises, a fraction of the lesson's size",
       code == 0 and "Complete solutions" in xd and "Exercise brief" in xd and "### exercises.json" in xd and "### lesson.md" not in xd
       and len(xd) < 0.6 * sum(f.stat().st_size for f in (t / "content/fi/FY3" / LESSON).rglob("*") if f.is_file() and "review" not in f.parts), out)
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
expect("a number changed on the way: not a split, the science reviewer looks", "science: full" in out and "answers" in out, out)
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
expect("... but a changed number in a formula is not typography: science full", "science: full" in out and "typography" not in out, out)
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
expect("real project untouched", snapshot() == REAL)
print("\n" + ("all review tests passed" if not failures else f"{len(failures)} FAILED: " + ", ".join(failures)))
sys.exit(1 if failures else 0)
