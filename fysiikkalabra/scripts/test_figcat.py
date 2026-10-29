"""Tests of the figure catalog and of figures in tasks (scripts/figcat.py). Usage: python scripts/test_figcat.py
Copies the project's sources into a temporary folder and changes one thing at a time there; the real project is not
touched. Checks: the committed catalog is current and deterministic, every figure is found without reading a lesson,
a reference resolves and renders in a task, a wrong or decorative reference fails the lint, the exercise set's hash
follows the referenced figure's data and drawing but not another figure of the same figures.py nor the lesson's hash,
a changed figure is the review category "figure", and a translation draws the same figure with its own words."""
import json, os, pathlib, re, shutil, subprocess, sys, tempfile
HERE = pathlib.Path(__file__).resolve().parent
SRC = HERE.parent
failures = []


def expect(name, cond, detail=""):
    print(("ok   " if cond else "FAIL ") + name + ("" if cond else f"  -> {str(detail)[:600]}"))
    if not cond: failures.append(name)


T = pathlib.Path(tempfile.mkdtemp(prefix="fysiikkalabra-figcat-"))
for f in ("curriculum.json", "competencies.json", "glossary.json"): shutil.copy(SRC / f, T / f)
for d in ("scripts", "templates", "content", "lessons", "lang", "assets", "docs"):
    shutil.copytree(SRC / d, T / d, ignore=shutil.ignore_patterns("__pycache__", "packet-*", "shots*", "lops2019"))
ENV = {**os.environ, "FYSIIKKALABRA_ROOT": str(T)}


def run(*args):
    r = subprocess.run([sys.executable, *map(str, args)], capture_output=True, text=True, cwd=T, env=ENV, timeout=600)
    return r.returncode, r.stdout + r.stderr


S = T / "scripts"
code, out = run(S / "figcat.py", "build", "--check")
expect("the committed catalog is a fresh build", code == 0, out)
a = (T / "docs/figures/catalog.json").read_text(); run(S / "figcat.py", "build"); b = (T / "docs/figures/catalog.json").read_text()
expect("building twice gives the same bytes", a == b)
cat = json.loads(b)
expect("no SVG or base64 in the catalog", "<svg" not in b and "base64" not in b)
ids = {f["id"] for f in cat["figures"]}
expect("lesson, Sovella and task-only figures are indexed", {"fy1-4/scatter", "fy3-sovella/fy3-s1-graph", "fy3-9/boyle-points"} <= ids, sorted(ids)[:10])
kinds = {f["id"]: f["kind"] for f in cat["figures"]}
expect("kinds are derived: graph, diagram, illustration", (kinds.get("fy1-4/scatter"), kinds.get("fy3-9/iso-processes"), kinds.get("fy3-9/hero")) == ("graph", "diagram", "illustration"), kinds)
used = {f["id"]: f.get("used_in", []) for f in cat["figures"]}
expect("where a figure is used is found (lesson section, exercises)", any("lesson.md § " in u for u in used["fy1-4/scatter"]) and any("exercises.json" in u for u in used["fy1-4/scatter-points"]), used["fy1-4/scatter-points"])
code, out = run(S / "figcat.py", "find", "boyle")
expect("find by words without reading a lesson", code == 0 and "fy3-9/boyle-graphs" in out and "<svg" not in out, out)
code, out = run(S / "figcat.py", "find", "--course", "FY3", "--reusable")
expect("--reusable leaves out what reveals an answer", "fy3-9/iso-processes" in out and "fy3-9/boyle-graphs" not in out, out)
code, out = run(S / "figcat.py", "show", "fy1-4/scatter-points")
expect("show prints the entry and only the code that draws it", "def scatter_points" in out and "def kettle" not in out and "CART" in out, out)

EX = T / "content/fi/FY1/fy1-4/exercises/exercises.json"; ORIG = EX.read_text()
code, out = run(S / "build.py", "fy1-4")
html = (T / "preview/fy1-4.html").read_text()
expect("a referenced figure renders inside its exercise", re.search(r'<li id="fy1-4-L2-02"[^>]*>.*?data-fig="fy1-4/scatter-points".*?</li>', html, re.S) is not None, out)
expect("the rendered figure has its accessible description", 'aria-label="Kuvaaja mittakaavassa: kärryn' in html)


def lint_with(fid):
    d = json.loads(ORIG); d["level2"][1]["figure"] = fid; EX.write_text(json.dumps(d, ensure_ascii=False))
    c, o = run(S / "lint_lesson.py", "fy1-4"); EX.write_text(ORIG); return c, o


c, o = lint_with("fy1-4/no-such-figure")
expect("an unknown figure id fails the lint", c == 1 and "names no figure" in o, o[-400:])
c, o = lint_with("fy3-9/hero")
expect("a decorative illustration cannot carry a task", c == 1 and "decorative" in o, o[-400:])
code, out = run(S / "lint_lesson.py", "fy1-4")
expect("a figure id is not taken for a chapter reference", "fy1-4/scatter-points" not in out, out[-400:])


def hashes():
    return run(S / "reviews.py", "hash", "fy1-4", "--exercises")[1].strip(), run(S / "reviews.py", "hash", "fy1-4")[1].strip()


FIG = T / "lessons/FY1/fy1-4/figures.py"; FORIG = FIG.read_text()
h0, l0 = hashes()
FIG.write_text(FORIG.replace("ax.point(0, 1, HEAT)", "ax.point(0, 1, COLD)")); h1, l1 = hashes()
expect("another figure of the same figures.py leaves the exercise hash alone", h1 == h0, (h0, h1))
FIG.write_text(FORIG.replace("CART = [(1, 0.6)", "CART = [(1, 0.7)")); h2, l2 = hashes()
expect("the referenced figure's data changes the exercise hash", h2 != h0, (h0, h2))
expect("and leaves the lesson's hash alone", l2 == l0, (l0, l2))
FIG.write_text(FORIG)
SOV = T / "lessons/FY3/sovella/figures.py"; SORIG = SOV.read_text()
p0 = run(S / "practice.py", "status")[1]
SOV.write_text(SORIG.replace('"reveals: the model graph', '"safe: the model graph'))
expect("a Sovella set's hash ignores the REUSE note", run(S / "practice.py", "status")[1] == p0, p0)
SOV.write_text(SORIG)
sys.path.insert(0, str(S)); os.environ["FYSIIKKALABRA_ROOT"] = str(T)
import reviews
expect("a changed figure slice is the review category figure", reviews.classify("figure:fy1-4/scatter-points", ["-x", "+y"], "fy1-4") == {"figure"})

# a translation: the same figure, its words from content/<lang>/…/figures.json, its decimal sign from lang/<lang>.json
lang = json.loads((T / "lang/fi.json").read_text()); lang["format"]["decimal"] = "."
(T / "lang/xx.json").write_text(json.dumps(lang, ensure_ascii=False))
tr = T / "content/xx/FY1/fy1-4"; tr.mkdir(parents=True)
(tr / "figures.json").write_text(json.dumps({"Kuvaaja mittakaavassa: kärryn kulkema matka s ajan t funktiona, kuusi mittauspistettä ilman sovitettua suoraa. "
                                             "Pisteet ovat (1 s; 0,6 m), (2 s; 0,8 m), (3 s; 1,6 m), (4 s; 2,1 m), (5 s; 2,4 m) ja (6 s; 2,9 m). Aika-akseli jatkuu 9 sekuntiin "
                                             "ja matka-akseli 4,5 metriin, ruudukon väli on 1 s ja 0,5 m.": "A graph to scale: six points."}))
code, out = run(S / "figcat.py", "render", "fy1-4/scatter-points", "--lang", "xx")
expect("a translation draws the same figure with its own description", code == 0 and 'aria-label="A graph to scale: six points."' in out, out[:400])
shutil.rmtree(T / "content/xx"); (T / "lang/xx.json").unlink()

shutil.rmtree(T, ignore_errors=True)
print("all figure catalog tests passed" if not failures else f"{len(failures)} FAILED: {', '.join(failures)}")
sys.exit(1 if failures else 0)
