"""A picture file as the base of a figure (work queue 24, teacher 2026-11-19: the redrawn pictures of FY1–FY10 and FY14).

A figure that has a row in its module's `lessons/<COURSE>/ASETTELU.tsv` is drawn by its figures.py as before, and then
this module swaps the drawing for the picture: the SVG keeps its viewBox, aria-label and `data-fig`, the shapes are
replaced by one `<image href="pics/<course>/<file>.webp">` placed at the row's x, y, width and height (in the figure's
own units), and the labels stay what they were, LaTeX `foreignObject`s from figures.py, each moved by the row's
shifts. Nothing in figures.py changes, so the words, their translations (figures.json) and every check that reads the
labels work as for a drawn figure; the picture itself carries no text.

ASETTELU.tsv (tab separated, one row per figure; the teacher's layout file with two columns of its own at the end):
  kuvan tunniste     <owner>/<name>, the figure's id (fy2-4/grid)
  tyyppi             diagram | illustration
  tiedosto           the file in assets/pics/<course>/ (WebP, at most 1600 px)
  x y leveys korkeus the picture's place in the figure's units; empty: the whole figure (an opening illustration)
  siirrot            {"1": [dx, dy], ...} the labels moved, by their order in the figure (1 = the first label drawn)
  ilman taustaa      [n, ...] the labels whose white background (Fig.tex bg=True) is dropped because the picture is
                     one flat colour under them; a label over a pattern (squared paper, hatching) keeps it
                     (teacher 2026-11-15; `figimage.py flat <COURSE>` writes the column from the pixels)

  python scripts/figimage.py convert <COURSE> <dir of the teacher's package>   WebP files + ASETTELU.tsv from the package
  python scripts/figimage.py flat <COURSE>      fill the "ilman taustaa" column from the pictures (needs Pillow)
  python scripts/figimage.py check [<COURSE>]   every row has its file and its figure; every file is used (exit 1 if not)
  python scripts/figimage.py size               the size of every module's pictures
"""
import functools, json, pathlib, re, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import courses

ROOT = courses.ROOT
NAME = "ASETTELU.tsv"
COLS = ["kuvan tunniste", "tyyppi", "tiedosto", "x", "y", "leveys", "korkeus",
        "merkintöjen siirrot (järjestysnumero: dx, dy)", "ilman taustaa (merkintöjen järjestysnumerot)"]
MAX_PX = 1600
WHITE_BG = re.compile(r'<span style="background:#ffffff;padding:0 5px;border-radius:3px">(.*?)</span>', re.S)
LABEL = re.compile(r"<foreignObject\b.*?</foreignObject>", re.S)
FIG_REF = re.compile(r'"(?:model_)?figure"\s*:\s*"([^"]+)"|<svg data-fig=\\?"([a-z0-9-]+/[A-Za-z0-9_-]+)\\?"></svg>')


def layout_file(code): return ROOT / "lessons" / code / NAME


@functools.lru_cache(maxsize=None)
def layout(code):
    """{figure id: row} of a module; {} for a module with no layout file."""
    f = layout_file(code); out = {}
    if not f.is_file(): return out
    lines = [l for l in f.read_text(encoding="utf-8").splitlines() if l.strip()]
    head = lines[0].split("\t")
    for l in lines[1:]:
        c = (l.split("\t") + [""] * len(COLS))[:len(COLS)]
        r = dict(zip(head + [""] * len(COLS), c))
        g = lambda k: r.get(k, "")
        box = [float(g(k)) if g(k) else None for k in ("x", "y", "leveys", "korkeus")]
        out[g("kuvan tunniste")] = {"type": g("tyyppi"), "file": g("tiedosto"), "box": None if None in box else box,
                                    "shift": {int(k): v for k, v in json.loads(g(COLS[7]) or "{}").items()},
                                    "flat": set(json.loads(g(COLS[8]) or "[]")), "code": code}
    return out


def code_of(fid):
    """The module a figure id belongs to (fy2-4/grid -> FY2), or None (a Sovella set, a unit, an investigation)."""
    owner = (fid or "").split("/")[0]
    try: return courses.course_of(owner)
    except Exception: return None


def row(fid):
    code = code_of(fid)
    return layout(code).get(fid) if code else None


def pic(fid):
    """The picture reference a figure with a row uses (pics/fy2/fy2-4-grid.webp), or None."""
    r = row(fid)
    return f"pics/{courses.course(r['code'])['slug']}/{r['file']}" if r else None


@functools.lru_cache(maxsize=None)
def bases():
    """{picture reference: [figure ids]} of every module that has a layout file."""
    out = {}
    for code in courses.codes():
        if layout_file(code).is_file():
            for fid in layout(code): out.setdefault(pic(fid), []).append(fid)
    return out


def is_base(ref): return ref in bases()


def pics_of(text):
    """The base pictures of the figures a text refers to by id (`"figure": "fy2-4/grid"`, an embedded `<svg data-fig="…">`)."""
    out = []
    for m in FIG_REF.finditer(text or ""):
        p = pic(m.group(1) or m.group(2))
        if p and p not in out: out.append(p)
    return out


def source(fid, read=None):
    """What a figure's picture adds to its drawing for a hash: the layout row's text and the picture's bytes, or None."""
    r = row(fid)
    if not r: return None
    f = layout_file(r["code"]); rel = f.relative_to(ROOT).as_posix()
    text = (read(rel) if read else f.read_text(encoding="utf-8")) or ""
    mine = next((l for l in text.splitlines() if l.split("\t")[0] == fid), "")
    return mine, courses.pic_source(pic(fid))


def apply(svg, fid):
    """The SVG of figure `fid` with its picture as the base, or `svg` itself for a figure with no row."""
    r = row(fid)
    if not r: return svg
    head = re.match(r"<svg\b[^>]*>", svg)
    if not head: return svg
    labels = LABEL.findall(svg)
    x, y, w, h = r["box"] or (0, 0, *map(float, re.search(r'viewBox="0 0 ([\d.]+) ([\d.]+)"', head.group(0)).groups()))
    num = lambda v: f"{v:.1f}".rstrip("0").rstrip(".")
    out = [head.group(0), f'  <image href="{pic(fid)}" x="{num(x)}" y="{num(y)}" width="{num(w)}" height="{num(h)}" preserveAspectRatio="none"/>']
    for i, lab in enumerate(labels, 1):
        dx, dy = r["shift"].get(i, (0, 0))
        if dx or dy:
            lab = re.sub(r'\bx="(-?[\d.]+)"', lambda m: f'x="{num(float(m.group(1)) + dx)}"', lab, count=1)
            lab = re.sub(r'\by="(-?[\d.]+)"', lambda m: f'y="{num(float(m.group(1)) + dy)}"', lab, count=1)
        if i in r["flat"]: lab = WHITE_BG.sub(r"\1", lab)
        out.append("  " + lab)
    out.append("</svg>")
    return "\n".join(out)


# --- the tools ------------------------------------------------------------------------------------------------------
def _write(code, rows):
    lines = ["\t".join(COLS)]
    for fid, r in rows.items():
        box = r["box"] or ["", "", "", ""]
        lines.append("\t".join([fid, r["type"], r["file"], *[("" if v == "" else f"{v:g}") for v in box],
                                json.dumps({str(k): v for k, v in sorted(r["shift"].items())}, separators=(",", ":")) if r["shift"] else "",
                                json.dumps(sorted(r["flat"])) if r["flat"] else ""]))
    layout_file(code).write_text("\n".join(lines) + "\n", encoding="utf-8"); layout.cache_clear(); bases.cache_clear()


def convert(code, package):
    """WebP files in assets/pics/<course>/ and lessons/<COURSE>/ASETTELU.tsv from the teacher's package folder
    (kuvat/, ASETTELU.tsv): the longest side at most 1600 px, lossy WebP, the name `<owner>-<name>.webp`."""
    from PIL import Image
    package = pathlib.Path(package); slug = courses.course(code)["slug"]
    dest = ROOT / "assets" / "pics" / slug; dest.mkdir(parents=True, exist_ok=True)
    src = [l.split("\t") for l in (package / NAME).read_text(encoding="utf-8").splitlines() if l.strip()][1:]
    rows, total = {}, 0
    for c in src:
        c += [""] * (8 - len(c)); fid, typ, png = c[:3]
        name = fid.replace("/", "-") + ".webp"
        im = Image.open(package / "kuvat" / png).convert("RGB"); im.thumbnail((MAX_PX, MAX_PX), Image.LANCZOS)
        im.save(dest / name, "WEBP", quality=82, method=6); total += (dest / name).stat().st_size
        box = [float(v) for v in c[3:7]] if c[3] != "" else None
        rows[fid] = {"type": typ, "file": name, "box": box, "shift": {int(k): v for k, v in json.loads(c[7] or "{}").items()}, "flat": set()}
    _write(code, rows)
    print(f"{code}: {len(rows)} pictures, {total / 1e6:.1f} MB in assets/pics/{slug}/")


def flat(code):
    """Fill the "ilman taustaa" column: a label with a white background whose box lies on one flat colour in the picture
    loses the background, one over squared paper or hatching keeps it (teacher 2026-11-15)."""
    from PIL import Image
    import figcat
    rows = layout(code)
    for fid, r in rows.items():
        r["flat"] = set()
        if r["box"] is None: continue
        svg = figcat.render(fid, raw=True)
        im = Image.open(courses.pic_source(pic(fid))).convert("L"); sx, sy = im.width / r["box"][2], im.height / r["box"][3]
        for i, lab in enumerate(LABEL.findall(svg), 1):
            if not WHITE_BG.search(lab): continue
            g = lambda k: float(re.search(rf'\b{k}="(-?[\d.]+)"', lab).group(1))
            dx, dy = r["shift"].get(i, (0, 0))
            x0, y0 = g("x") + dx - r["box"][0], g("y") + dy - r["box"][1]
            px = im.crop((max(0, int(x0 * sx)), max(0, int(y0 * sy)), min(im.width, int((x0 + g("width")) * sx)), min(im.height, int((y0 + g("height")) * sy))))
            vals = sorted(px.tobytes())
            if vals and vals[int(len(vals) * 0.98)] - vals[int(len(vals) * 0.02)] <= 10: r["flat"].add(i)
        print(f"{fid}: labels without background: {sorted(r['flat']) or '-'}")
    _write(code, rows)


def check(codes):
    import figcat
    bad = []
    for code in codes:
        slug = courses.course(code)["slug"]
        for fid, r in layout(code).items():
            if not (ROOT / "assets" / "pics" / slug / r["file"]).is_file(): bad.append(f"{fid}: assets/pics/{slug}/{r['file']} is missing")
            if not figcat.exists(fid): bad.append(f"{fid}: no such figure in figures.py")
            elif r["box"] is None and r["type"] != "illustration": bad.append(f"{fid}: a figure with labels needs x, y, width and height")
        used = {r["file"] for r in layout(code).values()}
        for f in sorted((ROOT / "assets" / "pics" / slug).glob("*.webp")):
            if f.name not in used and re.match(r"fy\d+-\d+-", f.name): bad.append(f"assets/pics/{slug}/{f.name}: no row in {NAME}")
    for b in bad: print(b)
    print("ok   every picture of a figure has its row and its figure" if not bad else f"{len(bad)} problem(s)")
    return not bad


if __name__ == "__main__":
    a = sys.argv[1:]
    if a[:1] == ["convert"] and len(a) == 3: convert(a[1].upper(), a[2])
    elif a[:1] == ["flat"] and len(a) == 2: flat(a[1].upper())
    elif a[:1] == ["check"]: sys.exit(0 if check([x.upper() for x in a[1:]] or [c for c in courses.codes() if layout_file(c).is_file()]) else 1)
    elif a[:1] == ["size"]:
        tot = 0
        for d in sorted((ROOT / "assets" / "pics").iterdir()):
            s = sum(f.stat().st_size for f in d.rglob("*") if f.is_file()); tot += s; print(f"{d.name:10} {s / 1e6:7.1f} MB")
        print(f"{'all':10} {tot / 1e6:7.1f} MB")
    else: sys.exit(__doc__)
