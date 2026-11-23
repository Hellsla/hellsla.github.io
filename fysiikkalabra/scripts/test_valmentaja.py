"""Tests of the FY9 task index (scripts/valmentaja.py, work queue 11b PR 2). Usage: python scripts/test_valmentaja.py
Part 1 copies what `valmentaja.py check` reads into a temporary folder, breaks one thing at a time and expects the check to
name it. Part 2 reads the real project: the index has every FY9 task with its fields, is the same in every build,
is the same set of tasks in every language, and (when site/ is built) every task's href lands on an id of the built page.
Part 3 reads the browser-side keys: the checked-task map's ids repeat across units (work queue 11b R9), and the
index's ids never do. The real project is not touched."""
import json, os, pathlib, re, shutil, subprocess, sys, tempfile
HERE = pathlib.Path(__file__).resolve().parent
SRC = HERE.parent
sys.path.insert(0, str(HERE))
failures = []


def expect(name, cond, detail=""):
    print(("ok   " if cond else "FAIL ") + name + ("" if cond else f"  -> {str(detail)[:600]}"))
    if not cond: failures.append(name)


# ---- part 1: the check names what is broken -------------------------------------------------------------------------
T = pathlib.Path(tempfile.mkdtemp(prefix="fysiikkalabra-valmentaja-"))
for f in ("curriculum.json", "competencies.json", "glossary.json", "local-courses.json"): shutil.copy(SRC / f, T / f)
for d in ("scripts", "content", "lessons", "lang", "kertaus"): shutil.copytree(SRC / d, T / d, ignore=shutil.ignore_patterns("__pycache__", "packet-*", "shots", "review"))
ENV = {**os.environ, "FYSIIKKALABRA_ROOT": str(T)}
SIDE = T / "kertaus/FY9.json"; ORIG = SIDE.read_text(encoding="utf-8")
GOOD = json.loads(ORIG)


def run(side):
    SIDE.write_text(json.dumps(side, ensure_ascii=False), encoding="utf-8")
    r = subprocess.run([sys.executable, str(T / "scripts/valmentaja.py"), "check"], capture_output=True, text=True, cwd=T, env=ENV, timeout=300)
    return r.returncode, r.stdout + r.stderr


def broken(name, edit, needle):
    d = json.loads(ORIG); edit(d)
    code, out = run(d)
    expect(name, code == 1 and needle in out, out[-500:])


def mini(d, mid): return next(m for m in d["minikokeet"] if m["id"] == mid)


code, out = run(GOOD)
expect("the committed kertaus/FY9.json passes", code == 0, out)
broken("an item for a task that does not exist", lambda d: d["items"].update({"fy9-voimat#ei-ole": {"minutes": 3}}), "is not a task of FY9")
broken("an unknown item field", lambda d: d["items"]["fy9-koe#testi-1"].update(colour="red"), "unknown field 'colour'")
broken("a diagnostic task without its unit", lambda d: d["items"].pop("fy9-koe#testi-7"), "diagnostic task fy9-koe#testi-7 needs")
broken("a diagnostic task in a unit that does not exist", lambda d: d["items"]["fy9-koe#testi-7"].update(unit="fy9-ei"), "is not a FY9 unit")
broken("an unknown competency", lambda d: d["items"].update({"fy9-voimat#nosturi": {"competencies": ["physics"]}}), "competencies must be a list")
broken("competencies on a long task", lambda d: d["items"].update({"fy9-voimat-s1": {"competencies": ["math"]}}), "come from its criteria")
broken("a followup that does not exist", lambda d: d["items"].update({"fy9-voimat#nosturi": {"followups": ["fy9-voimat#ei-ole"]}}), "followup 'fy9-voimat#ei-ole'")
broken("minutes out of range", lambda d: d["items"].update({"fy9-voimat#nosturi": {"minutes": 0}}), "minutes must be an integer")
broken("a misconception pointing at a missing option", lambda d: d.update(misconceptions={"x": {"items": ["fy9-voimat#lt-1/9", "fy9-liike#lt-1/0"]}}), "is not <task>/<option index>")
broken("a misconception with one item", lambda d: d.update(misconceptions={"x": {"items": ["fy9-voimat#lt-1/0"]}}), "needs at least two items")
broken("a minikoe with wrong points", lambda d: mini(d, "m30-osa1-1").update(points=12), "differ from the budget 10")
broken("a minikoe with wrong minutes", lambda d: mini(d, "m30-osa1-1").update(minutes=45), "differ from 10 points x 3 min")
broken("a minikoe with a task that does not exist", lambda d: mini(d, "m30-osa1-1")["short"].__setitem__(0, "fy9-voimat#ei-ole"), "is not a short task")
broken("a long task among the short ones", lambda d: mini(d, "m30-osa1-1")["short"].__setitem__(0, "fy9-voimat-s1"), "is not a short task")
broken("a short task among the long ones", lambda d: mini(d, "m60-osa2-1")["long"].__setitem__(0, "fy9-voimat#nosturi"), "is not a long task")
broken("long tasks worth different points", lambda d: mini(d, "m60-osa2-1")["long"].__setitem__(0, "fy9-lampo-s3"), "worth the same points")
broken("a topic minikoe with a task of another chapter", lambda d: mini(d, "m30-aihe-3")["short"].__setitem__(0, "fy9-moderni#rontgen"), "not all of its chapter")
broken("an Osa II minikoe with 20-point tasks", lambda d: mini(d, "m60-osa2-1").update(long=["fy9-lampo-s3", "fy9-tasavirta-s3"], points=26), "Osa II type")
broken("answering more short tasks than listed", lambda d: mini(d, "m30-osa1-1").update(answer=7), "answer is the number")
broken("a duplicate minikoe id", lambda d: mini(d, "m30-osa1-2").update(id="m30-osa1-1"), "id must be a unique slug")
broken("a plan whose days are not its weeks", lambda d: d["plans"].update({"2": {"days": 10}}), "plans.2")
broken("an unknown top-level key", lambda d: d.update(extra=1), "unknown key 'extra'")
SIDE.unlink()
code, out = subprocess.run([sys.executable, str(T / "scripts/valmentaja.py"), "check"], capture_output=True, text=True, cwd=T, env=ENV).returncode, ""
expect("a missing kertaus/FY9.json fails", code == 1)
shutil.rmtree(T, ignore_errors=True)

# ---- part 2: the index of the real project --------------------------------------------------------------------------
import i18n, units, valmentaja as v
all_pub = {u: set(units.holders(u)) for u in v.fy9_units()}
idx = {l: v.build(l, all_pub) for l in v.languages()}
fi = idx[i18n.SOURCE]
expect("the index is built for fi, en and fi-easy", set(idx) >= {"fi", "en", "fi-easy"}, sorted(idx))
NEED = ("id", "unit", "kind", "stage", "check", "comp", "min", "href", "part", "title", "review")
bad = [t["id"] for t in fi["tasks"] if any(k not in t for k in NEED) or t["check"] not in ("auto", "self") or not t["min"] or "#" not in t["href"] and not t["id"].startswith("fy9-")]
expect("every task has an id, unit, kind, check, competency, minutes and href", not bad, bad[:5])
expect("task ids are unique", len({t["id"] for t in fi["tasks"]}) == len(fi["tasks"]))
expect("short ids are <unit>#<id>, long ids are the task's own", all(("#" in t["id"]) == (t["kind"] != "long") for t in fi["tasks"]))
comps = set(json.loads((SRC / "competencies.json").read_text())["competencies"])
expect("every competency is one of the six", all(set(t["comp"]) <= comps and t["comp"] for t in fi["tasks"]))
expect("a numeric and a choice task are checked by the page, the explanations and long tasks by the student",
       all((t["check"] == "auto") == (t["kind"] in ("choice", "numeric")) or t["kind"] == "interpret" for t in fi["tasks"]))
expect("every long task has its parts, points and a competency weight that sums to them",
       all(t["points"] == sum(p["points"] for p in t["parts"]) == sum(t["comp"].values()) for t in fi["tasks"] if t["kind"] == "long"))
expect("a long task's minutes are 3 per point", all(t["min"] == 3 * t["points"] for t in fi["tasks"] if t["kind"] == "long"))
expect("the 24 diagnostic tasks are filed under the units they revise", len([t for t in fi["tasks"] if t["id"].startswith("fy9-koe#testi-")]) == 24
       and all(t["unit"] != "fy9-koe" for t in fi["tasks"] if t["id"].startswith("fy9-koe#testi-")))
expect("a 15-point task is Osa II type, a 20-point task Osa III type", all(t["part"] == {15: "II", 20: "III"}.get(t["points"]) for t in fi["tasks"] if t["kind"] == "long"))
expect("the index is small (plan 3.1: about 80 kB a language)", all(len(v.dumps(i).encode()) < 400_000 for i in idx.values()), {l: len(v.dumps(i)) for l, i in idx.items()})
expect("two builds give the same bytes", v.dumps(v.build("fi", all_pub)) == v.dumps(fi))
for lang in ("en", "fi-easy"):
    src = {t["id"]: t for t in fi["tasks"]}
    same = all(t["id"] in src and all(t[k] == src[t["id"]][k] for k in ("unit", "kind", "check", "comp", "min", "href", "part")) for t in idx[lang]["tasks"])
    expect(f"{lang}: the same tasks with the same fields as the source", same and len(idx[lang]["tasks"]) == len(fi["tasks"]), (len(idx[lang]["tasks"]), len(fi["tasks"])))
only_fi = v.build("en", {u: {"fi"} for u in all_pub})
expect("a language that has published no unit has no task", only_fi["tasks"] == [] and only_fi["minikokeet"] == [])
half = v.build("fi", {u: {"fi"} for u in all_pub if u != "fy9-voimat"})
expect("a minikoe whose task is not published is left out", len(half["minikokeet"]) < len(fi["minikokeet"]) and all(i.split("#")[0] != "fy9-voimat" for m in half["minikokeet"] for i in m.get("short", [])))
tmp = pathlib.Path(tempfile.mkdtemp(prefix="fysiikkalabra-valmentaja-out-"))
name = v.write("fi", tmp, all_pub)
expect("write puts the index at valmentaja/fy9.json and nothing else", name == "valmentaja/fy9.json" and [p.relative_to(tmp).as_posix() for p in tmp.rglob("*") if p.is_file()] == [name])
shutil.rmtree(tmp, ignore_errors=True)
src = (HERE / "valmentaja.py").read_text()
expect("the index code never touches the network (plan 7.1 R5)", not re.search(r"^\s*(?:import|from)\s+(?:[\w, ]*\b)?(?:urllib|requests|http|socket)\b|fetch\(|XMLHttpRequest|sendBeacon", src, re.M))

# hrefs land on an id of the built page (site/ is built before this runs in CI; skipped when it is not there)
site = SRC / "site"
if (site / "fy9-voimat.html").is_file():
    missing = []
    for lang, i in idx.items():
        base = site if lang == i18n.SOURCE else site / lang
        for t in i["tasks"]:
            page, _, frag = t["href"].partition("#")
            f = base / page
            if f.is_file() and f'id="{frag}"' not in f.read_text(encoding="utf-8"): missing.append(f"{lang}/{t['href']}")
    expect("every task's href lands on an id of the built page", not missing, missing[:5])
    for lang in idx:
        f = (site if lang == i18n.SOURCE else site / lang) / "valmentaja/fy9.json"
        if f.is_file():
            expect(f"{lang}: the built index is the one build() makes for the published units", json.loads(f.read_text())["lang"] == lang and json.loads(f.read_text())["version"] == 1)
else:
    print("skip  the built pages are not there (python scripts/build.py first)")

# ---- part 3: the keys the browser uses (work queue 11b R9) ----------------------------------------------------------
# ruukkilabra:tarkistettu keys a task by its bare DOM id. The activity ids of the lessons and units repeat, so the map
# merges them; the index never does, and the later log uses <unit>#<id>.
bare = {}
for u in v.fy9_units():
    for t in v.tasks_of(u, "fi", {}):
        if t["kind"] != "long": bare.setdefault(t["id"].split("#")[1], set()).add(u)
repeat = {k: len(us) for k, us in bare.items() if len(us) > 1}
expect("R9: FY9 activity ids such as lt-1 and tarkistus-2 repeat across units (so the log never keys by a bare id)", repeat.get("lt-1", 0) >= 10 and repeat.get("tarkistus-2", 0) >= 10, sorted(repeat.items())[:4])
expect("R9: the index's keys do not repeat", len({t["id"] for t in fi["tasks"]}) == len(fi["tasks"]))
js = (SRC / "templates/palautus.js").read_text(encoding="utf-8") + (SRC / "templates/padstore.js").read_text(encoding="utf-8")
expect("R9: the work file keeps only ids that start with the module code, so a bare id is never exported", "id.toLowerCase().startsWith(PRE)" in js)

print("\n" + ("FAILED: " + ", ".join(failures) if failures else "all passed"))
sys.exit(1 if failures else 0)
