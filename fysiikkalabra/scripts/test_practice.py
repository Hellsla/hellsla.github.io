"""Tests of Sovella itsenäisesti and the self-assessment components (scripts/practice.py). Usage: python scripts/test_practice.py
Copies the parts of the project the checks read into a temporary folder, breaks one thing at a time and expects
practice.py check to name it; then checks a trial English translation and the rendered components. The real project
is not touched."""
import json, os, pathlib, shutil, subprocess, sys, tempfile
HERE = pathlib.Path(__file__).resolve().parent
SRC = HERE.parent
failures = []


def expect(name, cond, detail=""):
    print(("ok   " if cond else "FAIL ") + name + ("" if cond else f"  -> {str(detail)[:600]}"))
    if not cond: failures.append(name)


T = pathlib.Path(tempfile.mkdtemp(prefix="fysiikkalabra-practice-"))
for f in ("curriculum.json", "competencies.json", "glossary.json"): shutil.copy(SRC / f, T / f)
for d in ("scripts", "templates", "content", "lessons", "lang"): shutil.copytree(SRC / d, T / d, ignore=shutil.ignore_patterns("__pycache__", "packet-*", "shots*"))
for p in [*(T / "lang").glob("*.json"), *(T / "content").iterdir()]:     # Finnish only: the test adds its own "en"
    if p.stem not in ("fi", "_gold"): shutil.rmtree(p) if p.is_dir() else p.unlink()
ENV = {**os.environ, "FYSIIKKALABRA_ROOT": str(T)}
TASKS = T / "content/fi/FY1/sovella/tasks.json"; SOL = T / "content/fi/FY1/sovella/solutions.md"; LANG = T / "lang/fi.json"
ORIG = {p: p.read_text() for p in (TASKS, SOL, LANG)}


def check():
    r = subprocess.run([sys.executable, str(T / "scripts/practice.py"), "check"], capture_output=True, text=True, cwd=T, env=ENV, timeout=300)
    return r.returncode, r.stdout + r.stderr


def broken(name, edit, needle):
    """Apply edit(data) to tasks.json (or a text edit to solutions.md / lang), expect a failing check that names needle."""
    for p, t in ORIG.items(): p.write_text(t)
    edit()
    code, out = check()
    expect(name, code == 1 and needle in out, out[-500:])


def tasks_edit(fn):
    def go():
        d = json.loads(ORIG[TASKS]); fn(d); TASKS.write_text(json.dumps(d, ensure_ascii=False))
    return go


code, out = check()
expect("the committed tasks pass", code == 0, out)
broken("a part's points differ from its criteria", tasks_edit(lambda d: d["tasks"][0]["parts"][0].update(points=4)), "differ from the sum of its criteria")
broken("an unknown competency tag", tasks_edit(lambda d: d["tasks"][0]["parts"][1]["criteria"][0].update(tag="physics")), "competency tag 'physics'")
broken("an unknown shared criterion", tasks_edit(lambda d: d["tasks"][0]["parts"][0]["criteria"][0].update(key="graph_colour")), "unknown shared criterion")
broken("a criterion without text or key", tasks_edit(lambda d: d["tasks"][0]["parts"][0]["criteria"].append({"points": 1})), "needs a shared `key`")
broken("duplicate task ids", tasks_edit(lambda d: d["tasks"][1].update(id="fy1-s1")), "duplicate task id")
broken("a link to a chapter that does not exist", tasks_edit(lambda d: d["tasks"][0]["links"].update(graph="fy1-9")), "not a lesson of curriculum.json")
broken("a competency without a chapter to practise it", tasks_edit(lambda d: d["tasks"][0]["links"].pop("experiment")), "no link for the competency 'experiment'")
broken("an answer answers.py does not give", tasks_edit(lambda d: d["tasks"][0]["parts"][1]["answer"].update(value=0.95)), "differs from answers.py")
broken("a list of answers without names", tasks_edit(lambda d: d["tasks"][0]["parts"][1].update(answer=[d["tasks"][0]["parts"][1]["answer"]] * 2)), "needs its own `name`")
broken("a named answer answers.py does not give", tasks_edit(lambda d: d["tasks"][0]["parts"][1].update(answer=[dict(d["tasks"][0]["parts"][1]["answer"], name="x")])), "does not compute this part's answer")
broken("a skill from a chapter that does not exist", tasks_edit(lambda d: d["tasks"][0].update(skills=["fy1-4", "fy1-9"])), "skills: 'fy1-9' is not a lesson")
broken("a missing worked solution", lambda: SOL.write_text(ORIG[SOL].replace("### c)\n", "### x)\n", 1)), "no worked solution")
broken("an incomplete calculation", lambda: SOL.write_text(ORIG[SOL].replace("**Järkevyys:** Pallo kulkee", "Pallo kulkee", 1)), "no '**Järkevyys:**' step")
broken("no common mistakes", lambda: SOL.write_text(ORIG[SOL].replace("### Yleisiä virheitä", "### Virheitä", 1)), "no `### Yleisiä virheitä`")
broken("a shared criterion without its text", lambda: LANG.write_text(json.dumps({k: v for k, v in json.loads(ORIG[LANG]).items() if k != "criteria"}, ensure_ascii=False)), "has no criteria.graph_axes")
for p, t in ORIG.items(): p.write_text(t)

# a trial English translation: the same tasks with translated texts pass; a changed point or formula fails
en = json.loads((T / "lang/fi.json").read_text()); (T / "lang/en.json").write_text(json.dumps(en, ensure_ascii=False))
(T / "content/en/FY1/sovella").mkdir(parents=True); shutil.copy(SOL, T / "content/en/FY1/sovella/solutions.md")
d = json.loads(ORIG[TASKS]); d["tasks"][0]["title"] = "Rolling ball on video"; (T / "content/en/FY1/sovella/tasks.json").write_text(json.dumps(d, ensure_ascii=False))
code, out = check()
expect("a translation with the same structure passes", code == 0 and "en/FY1" in out, out[-400:])
d["tasks"][0]["parts"][0]["criteria"][0]["points"] = 2; d["tasks"][0]["parts"][0]["points"] = 4
(T / "content/en/FY1/sovella/tasks.json").write_text(json.dumps(d, ensure_ascii=False))
code, out = check()
expect("a translation must keep the points", code == 1 and "differs from Finnish" in out, out[-400:])
shutil.rmtree(T / "content/en"); (T / "lang/en.json").unlink()

# the components as rendered
sys.path.insert(0, str(T / "scripts")); os.environ["FYSIIKKALABRA_ROOT"] = str(T)
import practice, i18n
md = lambda s: f"<p>{s}</p>"
task = practice.load("FY1")["tasks"][0]
h = practice.rubric_html(task, md)
expect("the rubric has one point group per criterion, 0..max each", h.count('class="crit"') == sum(len(p["criteria"]) for p in task["parts"]) and h.count('type="radio"') == sum(c["points"] + 1 for p in task["parts"] for c in p["criteria"]), h[:300])
expect("the rubric says the points are self-assessed and not YTL's", "oma arviosi" in h and "ei YTL:n virallinen" in h.replace("eikä se ole YTL:n virallinen", "ei YTL:n virallinen"), h[-600:])
expect("weak-competency links name chapters, never ids", ">Graafinen esitys ja suoran sovittaminen</a>" in h and ">fy1-4<" not in h, h[-600:])
task = dict(task, skills=["fy1-4"])
body, _ = practice.render("FY1", "fi", md, md, "x", embedded=True)
expect("an embedded task set has no page header, only task cards", "practice-head" not in body and body.count('class="activity task-card practice-task"') == len(practice.load("FY1")["tasks"]), body[:300])
expect("skills name the chapters, never ids", '>Graafinen esitys ja suoran sovittaminen</a>' in practice.skills_html(task) and ">fy1-4<" not in practice.skills_html(task), practice.skills_html(task))

# a unit's task set: key units/<id>, ids <id>-s<n>, found by unit_sets and checked like a course's
U = T / "content/fi/units/fy12-test/sovella"; U.mkdir(parents=True); (T / "lessons/units/fy12-test/sovella").mkdir(parents=True)
U.joinpath("tasks.json").write_text(ORIG[TASKS].replace("fy1-s", "fy12-test-s")); U.joinpath("solutions.md").write_text(ORIG[SOL].replace("fy1-s", "fy12-test-s"))
(T / "lessons/units/fy12-test/sovella/answers.py").write_text((T / "lessons/FY1/sovella/answers.py").read_text().replace("fy1-s", "fy12-test-s"))
if (T / "lessons/FY1/sovella/figures.py").is_file(): (T / "lessons/units/fy12-test/sovella/figures.py").write_text((T / "lessons/FY1/sovella/figures.py").read_text())
code, out = check()
expect("a unit's task set is found and passes", code == 0 and "fi/units/fy12-test" in out, out[-400:])
U.joinpath("tasks.json").write_text(ORIG[TASKS])
code, out = check()
expect("a unit's task ids are <unit id>-s<n>", code == 1 and "id must be fy12-test-s<n>" in out, out[-400:])
shutil.rmtree(T, ignore_errors=True)
print(f"\n{'FAILED: ' + ', '.join(failures) if failures else 'all practice tests passed'}")
sys.exit(1 if failures else 0)
