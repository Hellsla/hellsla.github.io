"""A future course through the whole pipeline, in a temporary copy of the project. Usage: python scripts/test_courses.py

Nothing is written to the real project and nothing is published: the copy holds the scripts, templates, curriculum,
glossary, the LOPS texts and one FY3 lesson. In it, FY4 is initialized with new_course.py; fy4-1 gets its meta.json
from the FY4 slot; the fixture lesson body is fy3-2's (relabelled fy4-1, its simulation moved to assets/sims/fy4/fy4-1/
with a sim.css, plus a picture in assets/pics/fy4/), because the point is the structure, not the physics. Then:
lint and its course rules, the preview build and its asset paths, the simulation, inquiry, answer-position and
layout checks, packets with FY4's LOPS context, the site build with stand-in PASS reports (course page, assets),
the hash and review scope over the simulation folder and the picture, a second lesson reusing the simulation and
the dependency and impact reports, usage collected from a synthetic transcript, and FY3 unchanged throughout.
With --keep <dir> the copy is made there and left in place after the run, for a dry run of an agent on fy4-1."""
import hashlib, json, os, pathlib, re, shutil, subprocess, sys, tempfile
HERE = pathlib.Path(__file__).resolve().parent
SRC = HERE.parent
failures = []


def expect(name, cond, detail=""):
    print(("ok   " if cond else "FAIL ") + name + ("" if cond else f"  -> {str(detail)[:600]}"))
    if not cond: failures.append(name)


def snapshot():
    files = [SRC / "curriculum.json", SRC / "glossary.json"] + sorted((SRC / "content").rglob("*")) + sorted((SRC / "lessons").rglob("*")) + sorted((SRC / "assets").rglob("*")) + sorted((SRC / "site").glob("*.html"))
    return hashlib.sha256(b"".join(p.as_posix().encode() + p.read_bytes() for p in files if p.is_file() and "/review/" not in p.as_posix())).hexdigest()
REAL = snapshot()

KEEP = sys.argv[sys.argv.index("--keep") + 1] if "--keep" in sys.argv else None
T = pathlib.Path(KEEP) if KEEP else pathlib.Path(tempfile.mkdtemp(prefix="fysiikkalabra-fy4-"))
if KEEP: shutil.rmtree(T, ignore_errors=True); T.mkdir(parents=True)
for f in ("curriculum.json", "glossary.json", "CLAUDE.md", "NOTES.md"): shutil.copy(SRC / f, T / f)
for d in ("scripts", "templates", "content/_gold", "lang"): shutil.copytree(SRC / d, T / d, ignore=shutil.ignore_patterns("__pycache__"))
shutil.copytree(SRC / "assets", T / "assets", ignore=shutil.ignore_patterns("fy4"))   # FY4 starts from scratch here, whatever the real project has
c0 = json.loads((T / "curriculum.json").read_text()); c0["FY4"].pop("initialized", None)
(T / "curriculum.json").write_text(json.dumps(c0, ensure_ascii=False, indent=2) + "\n")
(T / "docs/lops2019").mkdir(parents=True)
for f in (SRC / "docs/lops2019").glob("*.txt"): shutil.copy(f, T / "docs/lops2019")
shutil.copytree(SRC / "content/fi/FY3/fy3-2", T / "content/fi/FY3/fy3-2")
shutil.copytree(SRC / "lessons/FY3/fy3-2", T / "lessons/FY3/fy3-2", ignore=shutil.ignore_patterns("__pycache__"))
(T / "tests/sims").mkdir(parents=True); shutil.copy(SRC / "tests/sims/fy3-2.json", T / "tests/sims")
ENV = {**os.environ, "FYSIIKKALABRA_ROOT": str(T), "CLAUDE_CONFIG_DIR": str(T / ".claude-config")}


def run(script, *args):
    r = subprocess.run([sys.executable, str(T / "scripts" / script), *map(str, args)], capture_output=True, text=True, cwd=T, env=ENV, timeout=900)
    return r.returncode, r.stdout + r.stderr


def git(*a): return subprocess.run(["git", *a], cwd=T, capture_output=True, text=True).stdout
git("init", "-q"); git("config", "user.email", "t@t"); git("config", "user.name", "t")
(T / ".gitignore").write_text("preview/\nsite.tmp/\nsite.old/\n**/review/packet-*.md\n**/review/shots/\n**/review/shots.md\n__pycache__/\n.claude-config/\n")
git("add", "."); git("commit", "-qm", "base")
fy3_hash = run("reviews.py", "hash", "fy3-2")[1].strip()
expect("FY3 lesson keeps its hash in the copy", fy3_hash == subprocess.run([sys.executable, str(HERE / "reviews.py"), "hash", "fy3-2"], capture_output=True, text=True).stdout.strip(), fy3_hash)

# 1. /new-course FY4
code, out = run("new_course.py", "FY4", "--check")
expect("FY4 validates against LOPS 2019 before initialization", code == 0 and "17/17 LOPS items found" in out and "not initialized" in out, out)
code, out = run("new_course.py", "FY4")
cur = json.loads((T / "curriculum.json").read_text())
expect("new_course creates FY4's content, picture and simulation folders", code == 0 and all((T / d).is_dir() for d in ("content/fi/FY4", "lessons/FY4", "assets/pics/fy4", "assets/sims/fy4")), out)
expect("FY4 marked initialized; FY3's entry untouched", cur["FY4"].get("initialized") and cur["FY3"] == json.loads((SRC / "curriculum.json").read_text())["FY3"], cur["FY4"].get("initialized"))
code, out = run("new_course.py", "FY4")
expect("running it again only validates", code == 0 and "already initialized" in out, out)
c2 = json.loads((T / "curriculum.json").read_text()); del c2["FY4"]["tavoitteet"]; (T / "curriculum.json").write_text(json.dumps(c2, ensure_ascii=False, indent=2))
code, out = run("new_course.py", "FY4", "--check")
expect("a course without its LOPS goals is reported missing, nothing invented", code == 1 and "'tavoitteet' is missing" in out, out)
(T / "curriculum.json").write_text(json.dumps(cur, ensure_ascii=False, indent=2) + "\n")
code, out = run("courses.py", "init-lesson", "fy5-1")
expect("a lesson of an uninitialized course is refused", code != 0 and "not initialized" in out, out)
code, out = run("courses.py", "init-lesson", "fy4-99")
expect("a lesson without a slot is refused", code != 0 and "not a lesson slot" in out, out)

# 2. /lesson fy4-1 step 0: meta.json from the FY4 slot
code, out = run("courses.py", "init-lesson", "fy4-1")
L = T / "content/fi/FY4/fy4-1"; C = T / "lessons/FY4/fy4-1"; C.mkdir(parents=True); meta = json.loads((L / "meta.json").read_text())
slot = next(l for l in cur["FY4"]["lessons"] if l["id"] == "fy4-1")
expect("init-lesson writes FY4's slot into meta.json", code == 0 and meta["course"] == "FY4" and meta["title"] == slot["title"] and meta["goals"] == slot["goals"], meta)

# 3. the fixture body: fy3-2 relabelled, simulation and picture in FY4's folders
src = T / "content/fi/FY3/fy3-2"; src_code = T / "lessons/FY3/fy3-2"
for n in ("lesson.md", "inquiry.json", "exercises.json", "solutions.md", "exit-ticket.json"):
    (L / n).write_text((src / n).read_text().replace("fy3-2", "fy4-1"))
for n in ("answers.py", "sim-spec.md"): (C / n).write_text((src_code / n).read_text().replace("fy3-2", "fy4-1"))
meta.update(sim=True, glossary=json.loads((src / "meta.json").read_text())["glossary"]); (L / "meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2))
S = T / "assets/sims/fy4/fy4-1"; S.mkdir(parents=True)
shutil.copy(src_code / "sim.js", S / "sim.js"); (S / "sim.css").write_text("#sim-root canvas { border-radius: 6px; }\n")
lang = json.loads((T / "lang/fi.json").read_text()); lang["sims"]["fy4-1"] = lang["sims"]["fy3-2"]   # the copied sim keeps its texts
(T / "lang/fi.json").write_text(json.dumps(lang, ensure_ascii=False, indent=2) + "\n")
(T / "tests/sims/fy4-1.json").write_text((T / "tests/sims/fy3-2.json").read_text())
(T / "assets/pics/fy4/kalteva-taso.svg").write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 300"><path d="M40 260 L560 260 L560 80 Z" fill="none" stroke="#333" stroke-width="4"/></svg>\n')
md = (L / "lesson.md").read_text()
(L / "lesson.md").write_text(md.replace("## Ydinajatus\n", "## Ydinajatus\n\n![Kalteva taso, jonka kaltevuus on noin 20°](pics/fy4/kalteva-taso.svg)\n", 1))
# a new lesson meets the page rules of 2026-10-26 in full (lint_lesson.py "page"): the formula section named after its
# law, figures in the palette, no explanation paragraph in the simulation
md = (L / "lesson.md").read_text().replace("\n## Kaava\n", "\n## Kaava: Työ ja teho\n").replace("currentColor", "#1f2933")
(L / "lesson.md").write_text(md)
js = (S / "sim.js").read_text(); (S / "sim.js").write_text(re.sub(r"createP\('[^']{90,}'\)", "createP('Laatikko liikkuu vakiovauhdilla.')", js))
code, out = run("courses.py", "show", "fy4-1")
expect("the resolver places fy4-1's simulation and picture in FY4's folders", '"sim_script": "sims/fy4/fy4-1/sim.js"' in out and "pics/fy4/kalteva-taso.svg" in out, out)

# 4. lint and its course rules
code, out = run("lint_lesson.py", "fy4-1")
expect("fy4-1 lints clean", code == 0 and "0 error(s)" in out, out)
shutil.copy(S / "sim.js", C / "sim.js"); code, out = run("lint_lesson.py", "fy4-1"); (C / "sim.js").unlink()
expect("an FY4 sim.js in the lesson folder is refused", code == 1 and "lives in its own folder" in out, out)
(T / "assets/pics/fy3").mkdir(parents=True, exist_ok=True); (T / "assets/pics/fy3/x.svg").write_text("<svg/>")
(L / "lesson.md").write_text((L / "lesson.md").read_text() + "\n![x](pics/fy3/x.svg)\n"); code, out = run("lint_lesson.py", "fy4-1")
(L / "lesson.md").write_text((L / "lesson.md").read_text().replace("\n![x](pics/fy3/x.svg)\n", "")); (T / "assets/pics/fy3/x.svg").unlink()
expect("a picture from another course's folder is refused", code == 1 and "belongs to another course" in out, out)
(L / "lesson.md").write_text((L / "lesson.md").read_text() + "\n![y](pics/fy4/puuttuu.svg)\n"); code, out = run("lint_lesson.py", "fy4-1")
(L / "lesson.md").write_text((L / "lesson.md").read_text().replace("\n![y](pics/fy4/puuttuu.svg)\n", ""))
expect("a missing picture is refused", code == 1 and "not found" in out, out)

# 5. every deterministic check
code, out = run("check_lesson.py", "fy4-1")
expect("check_lesson: lint, LaTeX, build, sims, inquiry, answer positions, 360 px all ok", code == 0 and all(f"ok   {s}" in out for s in ("lint", "latex", "build", "sims", "inquiry", "answer positions", "layout 360 px")), out)
page = (T / "preview/fy4-1.html").read_text()
expect("the preview refers to FY4's assets by relative paths", 'src="sims/fy4/fy4-1/sim.js"' in page and 'data-base="sims/fy4/fy4-1/"' in page and 'href="sims/fy4/fy4-1/sim.css"' in page and 'src="pics/fy4/kalteva-taso.svg"' in page and "https://" not in re.sub(r'<link rel="canonical"[^>]*>|<meta property="og:url"[^>]*>', "", page), "")
expect("the assets are published at those paths", all((T / "preview" / p).is_file() for p in ("sims/fy4/fy4-1/sim.js", "sims/fy4/fy4-1/sim.css", "pics/fy4/kalteva-taso.svg")))
expect("navigation is FY4's: crumbs and footer point to FY4.html", 'href="FY4.html">FY4</a>' in page and "FY3.html" not in page)

# 6. packets carry FY4's context, not FY3's
code, out = run("review_packet.py", "fy4-1", "--role", "science"); ps = (L / "review/packet-science.md").read_text()
expect("science packet: FY4's LOPS goals and contents, the fy4-1 slot, the sim folder", "## Course FY4: Voima ja liike" in ps and "osaa tutkia kokeellisesti voimaan" in ps and "kappaleiden vuorovaikutus ja voima sekä Newtonin lait" in ps
       and "tasainen suoraviivainen liike" in ps and "### assets/sims/fy4/fy4-1/sim.js" in ps and "## Course FY3" not in ps, out)
code, out = run("review_packet.py", "fy4-1", "--role", "pedagogy"); pp = (L / "review/packet-pedagogy.md").read_text()
expect("pedagogy packet: FY4 context and the screenshot list", "## Course FY4" in pp and "Screenshots" in pp, out)
code, out = run("review_packet.py", "fy4-1", "--role", "developer"); pd = (L / "review/packet-developer.md").read_text()
expect("developer packet: FY4's folders and its simulations for reuse", "assets/sims/fy4/fy4-1/sim.js" in pd and "assets/pics/fy4/" in pd and "Simulations this course already has" in pd, out)
code, out = run("screenshot.py", "fy4-1")
expect("screenshots of fy4-1 in its review folder", code == 0 and (L / "review/shots.md").is_file() and len(list((L / "review/shots").glob("*.png"))) > 5, out)

# 7. the site, with stand-in PASS reports (the fixture is never reviewed for real)
h = run("reviews.py", "hash", "fy4-1")[1].strip()
for n in ("science", "pedagogy"): (L / f"review/{n}.md").write_text(f"VERDICT: PASS\nCONTENT-HASH: {h}\n\n## Blocking\n")
for n in ("science", "pedagogy"): (src / f"review/{n}.md").write_text(f"VERDICT: PASS\nCONTENT-HASH: {fy3_hash}\n\n## Blocking\n")
code, out = run("build.py")
site = T / "site"
expect("site build publishes fy4-1 with its assets", code == 0 and (site / "fy4-1.html").is_file() and all((site / p).is_file() for p in ("sims/fy4/fy4-1/sim.js", "sims/fy4/fy4-1/sim.css", "pics/fy4/kalteva-taso.svg")), out)
expect("FY4.html links fy4-1 and lists the other FY4 slots as coming; FY3.html does not list it",
       'href="fy4-1.html"' in (site / "FY4.html").read_text() and "tulossa" in (site / "FY4.html").read_text() and "fy4-1" not in (site / "FY3.html").read_text())
expect("fy3-2 is built exactly as the real site has it", (site / "fy3-2.html").read_bytes() == (SRC / "site/fy3-2.html").read_bytes() and (site / "fy3-2-sim.js").read_bytes() == (SRC / "site/fy3-2-sim.js").read_bytes())
code, out = run("check_choices.py", "--all", "--site")
expect("answer positions are checked per course on the site", code == 0 and "FY4:" in out and "FY3:" in out, out)
git("add", "."); git("commit", "-qm", "fy4-1 reviewed (stand-in)")

# 8. the hash and the review scope cover the simulation folder and the picture
(S / "sim.css").write_text("#sim-root canvas { border-radius: 8px; }\n")
code, out = run("reviews.py", "scope", "fy4-1")
expect("sim.css changed: science none, pedagogy delta", "science: none" in out and "pedagogy: delta" in out, out)
code, out = run("reviews.py", "carry", "fy4-1")
expect("carry records the science PASS over the styling change", "science: carried over" in out, out)
git("checkout", "--", "."); (L / "review/carry.tsv").unlink(missing_ok=True)
(S / "sim.js").write_text((S / "sim.js").read_text().replace("p.draw = () => {", "p.draw = () => { const k = 1;", 1))
code, out = run("reviews.py", "scope", "fy4-1")
expect("simulation code in the FY4 folder changed: full review for both", out.count(": full") == 2 and "simulation" in out, out)
git("checkout", "--", ".")
(T / "assets/pics/fy4/kalteva-taso.svg").write_text((T / "assets/pics/fy4/kalteva-taso.svg").read_text().replace("560 80", "560 120"))
code, out = run("reviews.py", "scope", "fy4-1")
expect("the picture changed: the hash moved and both review it", run("reviews.py", "hash", "fy4-1")[1].strip() != h and out.count(": full") == 2, out)
git("checkout", "--", ".")

# 9. a second lesson reuses the simulation: dependencies and impact
run("courses.py", "init-lesson", "fy4-2"); L2 = T / "content/fi/FY4/fy4-2"; C2 = T / "lessons/FY4/fy4-2"; C2.mkdir(parents=True)
for n in ("lesson.md", "inquiry.json", "exercises.json", "solutions.md", "exit-ticket.json"): (L2 / n).write_text((L / n).read_text().replace("fy4-1", "fy4-2"))
for n in ("answers.py", "sim-spec.md"): (C2 / n).write_text((C / n).read_text().replace("fy4-1", "fy4-2"))
m2 = json.loads((L2 / "meta.json").read_text()); m2.update(sim="fy4-1", glossary=meta["glossary"], prerequisites=[]); (L2 / "meta.json").write_text(json.dumps(m2, ensure_ascii=False, indent=2))
(T / "tests/sims/fy4-2.json").write_text((T / "tests/sims/fy4-1.json").read_text())
code, out = run("courses.py", "deps")
expect("deps: the FY4 sim folder is used by fy4-1 and fy4-2", '"sims/fy4/fy4-1": [\n  "fy4-1",\n  "fy4-2"' in out, out)
code, out = run("lint_lesson.py", "fy4-2")
expect("the reusing lesson lints clean", code == 0, out)
git("add", "."); git("commit", "-qm", "fy4-2")
h1, h2 = run("reviews.py", "hash", "fy4-1")[1].strip(), run("reviews.py", "hash", "fy4-2")[1].strip()
(S / "sim.js").write_text((S / "sim.js").read_text() + "\nconst muutos = 1;\n")
expect("a change to the shared sim moves both lessons' hashes", run("reviews.py", "hash", "fy4-1")[1].strip() != h1 and run("reviews.py", "hash", "fy4-2")[1].strip() != h2)
code, out = run("reviews.py", "impact", "HEAD")
expect("impact lists both users of the changed sim", "used by fy4-1, fy4-2" in out and "fy4-1: science full" in out and "fy4-2:" in out, out)
git("checkout", "--", ".")

# 10. usage from a synthetic transcript (the format Claude Code writes)
proj = T / ".claude-config/projects/-x"; sub = proj / "s1/subagents"; sub.mkdir(parents=True)
u = lambda i, cr, cw, o: {"input_tokens": i, "cache_read_input_tokens": cr, "cache_creation_input_tokens": cw, "output_tokens": o, "cache_creation": {"ephemeral_1h_input_tokens": cw, "ephemeral_5m_input_tokens": 0}}
turn = lambda mid, model, us, ts, blocks: [json.dumps({"type": "assistant", "timestamp": ts, "message": {"id": mid, "model": model, "usage": us, "content": [b]}}) for b in blocks]
(sub / "agent-a1.jsonl").write_text("\n".join(
    [json.dumps({"type": "user", "timestamp": "2026-10-26T10:00:00Z", "message": {"role": "user", "content": "Read content/fi/FY4/fy4-1/review/packet-science.md and follow it. Lesson: fy4-1. Mode: full. Round: 1."}})]
    + turn("m1", "claude-opus-5-5", u(2, 0, 30000, 500), "2026-10-26T10:00:05Z", [{"type": "text", "text": "x"}, {"type": "tool_use", "name": "Read", "input": {}}])
    + turn("m2", "claude-opus-5-5", u(2, 30000, 2000, 800), "2026-10-26T10:01:00Z", [{"type": "text", "text": "VERDICT: PASS"}])) + "\n")
(sub / "agent-a1.meta.json").write_text(json.dumps({"agentType": "science-reviewer", "model": "opus", "effort": "medium"}))
(proj / "s1.jsonl").write_text("\n".join(
    [json.dumps({"type": "user", "timestamp": "2026-10-26T09:59:00Z", "message": {"role": "user", "content": "Run lesson fy4-1 through the pipeline."}})]
    + turn("o1", "claude-sonnet-5-5", u(10, 5000, 1000, 300), "2026-10-26T09:59:30Z", [{"type": "tool_use", "name": "Bash", "input": {}}])) + "\n")
code, out = run("usage.py", "collect", "fy4-1", "--session", "s1"); run("usage.py", "collect", "fy4-1", "--session", "s1")
rows = [l.split("\t") for l in (L / "review/usage.tsv").read_text().splitlines()]
head = rows[0]; got = {r[head.index("agent")]: dict(zip(head, r)) for r in rows[1:]}
sci, orc = got.get("science-reviewer", {}), got.get("orchestrator", {})
expect("collect: each turn counted once, the served model, cache reads and writes, final context", sci.get("tokens") == str(4 + 30000 + 32000 + 1300) and sci.get("cache_read") == "30000"
       and sci.get("cache_write") == "32000" and sci.get("context") == str(2 + 30000 + 2000 + 800) and sci.get("model") == "claude-opus-5-5" and sci.get("calls") == "1" and sci.get("verdict") == "PASS" and sci.get("mode") == "full", sci)
cost = (4 * 4 + 32000 * 2 * 4 + 30000 * 0.20 + 1300 * 20) / 1e6
expect("collect: list-price cost with 1-hour cache writes; orchestrator row from 'Run lesson'", abs(float(sci.get("cost_usd", 0)) - cost) < 1e-4 and orc.get("model") == "claude-sonnet-5-5" and orc.get("mode") == "lesson-run", (sci.get("cost_usd"), cost, orc))
expect("collect twice: no duplicate rows", len(rows) == 3, len(rows))
code, out = run("usage.py", "report", "FY4")
expect("report separates measured from unmeasured", "measured (2 runs, from transcripts)" in out, out)

# 11. what CI runs, over both courses
for name, args in (("lint --all", ("lint_lesson.py", "--all")), ("build --all", ("build.py", "--all")), ("verify", ("reviews.py", "verify"))):
    code, out = run(*args); expect(f"CI step {name} passes with FY4 present", code == 0, out[-400:])
code, out = run("test_inquiry.py", "fy4-2")
expect("inquiry tests of the reusing lesson pass", code == 0, out[-400:])
expect("FY3 lesson's hash unchanged after everything", run("reviews.py", "hash", "fy3-2")[1].strip() == fy3_hash)

if not KEEP: shutil.rmtree(T, ignore_errors=True)
else: print(f"kept the FY4 fixture project at {T}")
expect("real project untouched", snapshot() == REAL)
print("\n" + ("all course tests passed" if not failures else f"{len(failures)} FAILED: " + ", ".join(failures)))
sys.exit(1 if failures else 0)
