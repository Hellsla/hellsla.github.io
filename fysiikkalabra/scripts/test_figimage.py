"""figimage.py: a figure drawn on a picture file (work queue 24).

  python scripts/test_figimage.py

Checks the swap on a made-up figure (the picture in, the shapes out, the labels kept in order, moved by the row's shifts,
the white background dropped only where the row says), that a figure with no row is left alone, that the picture
reaches the build, the review hash and the lint, and that every real row of every module has its file, its figure, its
labels and a picture of at most 1600 px; and that all the pictures together stay under 100 MB."""
import pathlib, re, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import courses, figcat, figimage, figlib, lint_lesson

fails = 0
def check(name, ok, detail=""):
    global fails
    print(("ok   " if ok else "FAIL ") + name + ("" if ok else f": {detail}")); fails += not ok

def drawn():
    f = figlib.Fig("t-fig", 300, "Test figure.")
    f.rect(10, 10, 100, 100, "#a9d1f0", "#1f2933"); f.circle(50, 50, 20)
    f.tex(40, 40, r"E_\text{o}", "start", w=60)
    f.tex(40, 120, r"\text{lämpö}", "start", w=90, bg=True)
    f.tex(300, 200, r"\text{sähkö}", "middle", w=90, bg=True)
    return f.svg()

ROW = {"type": "diagram", "file": "t-fig.webp", "box": [0.0, -1.2, 600.0, 401.2], "shift": {0: (9, 0), 2: (0, 5)}, "flat": {1}, "code": "FY2"}
real_row, real_pic = figimage.row, figimage.pic
figimage.row = lambda fid: ROW if fid == "fy2-1/t" else None
figimage.pic = lambda fid: "pics/fy2/t-fig.webp" if fid == "fy2-1/t" else None
svg = drawn(); out = figimage.apply(svg, "fy2-1/t")
check("the picture is the only drawn thing", out.count("<image ") == 1 and "<rect" not in out and "<circle" not in out, out[:200])
check("the picture sits where the row says", 'href="pics/fy2/t-fig.webp" x="0" y="-1.2" width="600" height="401.2"' in out, out[:200])
check("the opening tag, viewBox and aria-label are the figure's own", out.startswith(svg[:svg.index(">") + 1]), out[:120])
check("every label is kept, in order", out.count("<foreignObject") == 3 and out.index("E_\\text{o}") < out.index("lämpö") < out.index("sähkö"))
lab = figimage.LABEL.findall(out)
orig = figimage.LABEL.findall(svg)
at = lambda t, k: float(re.search(rf'\b{k}="(-?[\d.]+)"', t).group(1))
check("label 0 is moved right by its shift", at(lab[0], "x") == at(orig[0], "x") + 9 and at(lab[0], "y") == at(orig[0], "y"), lab[0][:80])
check("label 2 is moved down", at(lab[2], "y") == at(orig[2], "y") + 5 and at(lab[2], "x") == at(orig[2], "x"))
check("the white background goes where the row says (label 1)", "background:#ffffff" not in lab[1] and "background:#ffffff" in lab[2], lab[1][-120:])
check("a figure with no row is returned as it is", figimage.apply(svg, "fy2-1/other") == svg)
check("a row with no box fills the figure (an opening illustration)",
      (lambda r: figimage.apply(figlib.Fig("h", 600, "Hero.", width=1200, hero=True).svg(), "fy2-1/t").count('width="1200" height="600"') == 1
       if not r.update(box=None) else False)(ROW))
ROW["box"] = [0.0, 0.0, 600.0, 300.0]
figimage.row, figimage.pic = real_row, real_pic
check("a picture reference in a figure's own SVG is a picture of the lesson (hash, build, dependencies)",
      courses.pic_refs_in(['<svg><image href="pics/fy2/fy2-1-hero.webp"/></svg>']) == ["pics/fy2/fy2-1-hero.webp"])
mono = '<svg viewBox="0 0 600 300" role="img" aria-label="x">\n  <image href="pics/fy2/a.webp" x="0" y="0" width="600" height="300"/>\n  <foreignObject><div>$a$</div></foreignObject></svg>'
class L:                                            # what lint_lesson.check_figures reports to
    def __init__(self): self.found = []
    def page(self, *a): self.found.append(a)
    def warn(self, *a): self.found.append(a)
    def err(self, *a): self.found.append(a)
l = L(); lint_lesson.check_figures(l, mono)
check("a figure on a picture is not a monochrome sketch", not l.found, l.found)

check("code_of: a lesson, the exam and the Sovella set of a module",
      [figimage.code_of(f) for f in ("fy4-3/x", "fy4-koe/fy4-k1-fbd", "fy4-sovella/fy4-s3-collision", "fy5-sovella/a")] == ["FY4", "FY4", "FY4", "FY5"])
check("code_of: a unit, an investigation or nothing is still None",
      [figimage.code_of(f) for f in ("tvt-epavarmuus/a", "fy4-koe-x/a", "", None, "fy99-koe/a")] == [None] * 5)

check("code_of: a figure of a unit module's unit or of its task set (FY14, FY9)",
      [figimage.code_of(f) for f in ("fy14-plasma/hero", "fy14-plasma-sovella/a", "fy9-aallot/x", "fy9-koe/x")] == ["FY14", "FY14", "FY9", "FY9"])
check("code_of: a course that has no unit of that name is still None", figimage.code_of("fy4-plasma/x") is None)
check("a unit module's pictures: slug and layout file", set(figimage.modules()[-2:]) == {"FY9", "FY14"} and figimage.layout_file("FY14").as_posix().endswith("lessons/FY14/ASETTELU.tsv")
      and courses.slug("FY14") == "fy14")

# units.py draws a unit figure with a row on its picture, and the picture's bytes are in the unit's hash
import units
UROW = {"type": "illustration", "file": "t-fig.webp", "box": None, "shift": {}, "flat": set(), "code": "FY14"}
figimage.row, figimage.pic = (lambda fid: UROW if fid == "fy14-plasma/hero" else None), (lambda fid: "pics/fy14/t-fig.webp" if fid == "fy14-plasma/hero" else None)
try: _, new, _ = units.draw("fy14-plasma", "en")
finally: figimage.row, figimage.pic = real_row, real_pic
check("units.draw puts a unit figure with a row on its picture", new is not None and '<image href="pics/fy14/t-fig.webp"' in new)

# a figure written into a Sovella or exam solutions.md by practice.py is drawn on its picture too (the id is the page's: fy4-koe/<name>, fy4-sovella/<name>)
import practice
FAKE = {"type": "diagram", "file": "t-fig.webp", "box": None, "shift": {}, "flat": set(), "code": "FY4"}
figimage.row, figimage.pic = (lambda fid: FAKE if fid == "fy4-sovella/fy4-s3-collision" else None), (lambda fid: "pics/fy4/t-fig.webp" if fid == "fy4-sovella/fy4-s3-collision" else None)
try: stale = not practice.figures("FY4", write=False)
finally: figimage.row, figimage.pic = real_row, real_pic
check("practice.figures writes a figure with a row on its picture (a solutions.md without it is out of date)", stale)
check("practice.figures leaves solutions.md as it is when no figure has a row", practice.figures("FY4", write=False) or figimage.row("fy4-sovella/fy4-s3-collision"))


# the real layouts
tot = 0
for code in courses.codes():
    if not figimage.layout_file(code).is_file(): continue
    slug = courses.course(code)["slug"]
    for fid, r in figimage.layout(code).items():
        f = courses.pic_source(figimage.pic(fid))
        if not f.is_file(): check(f"{fid}: file", False, str(f)); continue
        from PIL import Image
        im = Image.open(f); box = r["box"]
        check(f"{fid}: WebP of at most {figimage.MAX_PX} px", im.format == "WEBP" and max(im.size) <= figimage.MAX_PX, f"{im.format} {im.size}")
        if box: check(f"{fid}: the picture keeps its proportions in the figure", abs(box[2] / box[3] - im.width / im.height) / (im.width / im.height) < 0.01, f"{box[2] / box[3]:.3f} vs {im.width / im.height:.3f}")
        raw, svg = figcat.render(fid, raw=True), figcat.render(fid)
        check(f"{fid}: drawn on its picture, labels kept", "<image " in svg and svg.count("<foreignObject") == raw.count("<foreignObject") and svg.count("<text") == 0, f"{svg.count('<foreignObject')} vs {raw.count('<foreignObject')}")
        check(f"{fid}: every shift and flat label names a label", all(0 <= i < raw.count("<foreignObject") for i in [*r["shift"], *r["flat"]]))
src = (pathlib.Path(__file__).resolve().parent / "build.py").read_text(encoding="utf-8")
check("build.py copies the pictures of a lesson, a Sovella page, an exam page and a unit (copy_pics)",
      len(re.findall(r"^\s+copy_pics\(", src, re.M)) == 4, "copy_pics calls")
import figimage as F
total = sum(p.stat().st_size for p in (courses.ROOT / "assets" / "pics").rglob("*") if p.is_file())
check(f"all the pictures together are under 100 MB ({total / 1e6:.1f} MB)", total < 100e6)
check("the layout files and pictures agree (figimage.py check)", figimage.check([c for c in courses.codes() if figimage.layout_file(c).is_file()]))
sys.exit(1 if fails else 0)
