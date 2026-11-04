"""Käsitekartat (teacher 2026-11-04): one Novak-style concept map per module on its module page.

A concept map answers a focus question: the module's concepts in boxes, from the most general at the top to the most
specific below, joined by lines whose short linking phrase makes each pair a proposition that reads as a sentence
("mittaustulos — sisältää aina → mittausvirhe"). Cross-links between branches are dashed; examples (a formula, a
unit, a case) hang under a concept in a dashed box. Upper-secondary level: 18–26 concepts, the words of the
chapters and the concept cards.

The data is `kasitekartat/<MODULE>.json`, written by hand (the layout is part of the map's meaning):

    {"module": "FY1", "width": 1200, "height": 900,
     "focus": {"fi": "...?", "en": "...?", "fi-easy": "...?"},
     "nodes": [{"id": "fysiikka", "x": 600, "y": 60, "kind": "root" | "concept" | "example",
                "label": {"fi": "fysiikka", "en": "physics"}, "chapter": "fy1-1", "quantity": "velocity"}],
     "links": [{"from": "fysiikka", "to": "ilmio", "label": {"fi": "tutkii", "en": "studies"},
                "cross": false, "via": [[x, y]], "at": 0.5, "dx": 0, "dy": 0}]}

A label is a LaTeX string inside `$…$` or plain words (drawn as `\\text{}`); `\\n` breaks a box onto two lines.
fi-easy falls back to fi, any other language to its own text and then to fi (the check reports a missing one).
`quantity` colours a box's border by the course rule (velocity blue, acceleration orange, force red, CLAUDE.md).
`chapter` is the chapter that teaches the concept: on the page the box links to it when it is published.

`python scripts/conceptmaps.py check` validates every map; `python scripts/conceptmaps.py svg FY1 [lang]` prints one.
The build calls section(code, T, lang, built) for the module page.
"""
import html, json, math, re, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from figlib import n, visible_len, INK, MUTED, WHITE   # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
DIR = ROOT / "kasitekartat"
VELOCITY, ACCEL, FORCE = "#1971c2", "#e8590c", "#c92a2a"   # scripts/fbd.py: the course's colours for v, a and F
QUANTITY = {"velocity": VELOCITY, "acceleration": ACCEL, "force": FORCE}
ACCENT, ACCENT_SOFT, PAPER, LINK, CROSS = "#1a4d2e", "#ecf5ee", "#f6f1e6", "#5b6472", "#8a5a1f"
SIZE = {"root": 22, "concept": 19, "example": 17}
LINK_SIZE = 15.5
PAD_X, LINE_H = 16, 26


def load(code):
    p = DIR / f"{code}.json"
    return json.loads(p.read_text()) if p.is_file() else None


def modules():
    return sorted(p.stem for p in DIR.glob("FY*.json"))


def text_of(label, lang):
    if isinstance(label, str): return label
    return label.get(lang) or (label.get("fi") if lang in ("fi-easy",) or lang not in label else None) or label.get("fi", "")


def tex(s):
    """A label as LaTeX: `$…$` parts as they are, words in \\text{}."""
    out = []
    for i, part in enumerate(re.split(r"\$([^$]*)\$", s)):
        if i % 2: out.append(part)
        elif part:
            esc = part.replace("\\", r"\textbackslash ").replace("{", r"\{").replace("}", r"\}").replace("%", r"\%").replace("&", r"\&").replace("#", r"\#")
            out.append(r"\text{" + esc + "}")
    return "".join(out)


def width_of(s, size):
    """About the rendered width of a label line (KaTeX Main); the browser check measures the real one."""
    words = len(re.sub(r"\$[^$]*\$", "", s))
    maths = sum(visible_len(m) for m in re.findall(r"\$([^$]*)\$", s))
    return (words * 0.5 + maths * 0.55) * size


def box(node, lang):
    lines = text_of(node["label"], lang).split("\n")
    size = SIZE[node.get("kind", "concept")]
    w = max(width_of(l, size) for l in lines) + 2 * PAD_X + (8 if node.get("kind") == "root" else 0)
    w = max(w, node.get("min_w", 0))
    h = len(lines) * size * 1.35 + (22 if node.get("kind") == "root" else 16)
    return lines, size, w, h


def edge_point(cx, cy, w, h, tx, ty, gap=3):
    """Where the line from a box's centre towards (tx, ty) leaves the box."""
    dx, dy = tx - cx, ty - cy
    if dx == 0 and dy == 0: return cx, cy
    sx = (w / 2 + gap) / abs(dx) if dx else math.inf
    sy = (h / 2 + gap) / abs(dy) if dy else math.inf
    s = min(sx, sy)
    return cx + dx * s, cy + dy * s


def fo(x, y, w, h, t, size, color=INK, align="center", bg=False, italic=False):
    just = {"start": "flex-start", "center": "center", "end": "flex-end"}[align]
    style = f"display:flex;align-items:center;justify-content:{just};height:100%;font-size:{size:g}px" + (f";color:{color}" if color != INK else "")
    body = f"${tex(t)}$"
    if italic: body = "$" + re.sub(r"\\text\{", r"\\textit{", tex(t)) + "$"
    if bg: body = f'<span style="background:{WHITE};padding:1px 4px;border-radius:3px;line-height:1.1">{body}</span>'
    return (f'<foreignObject x="{n(x)}" y="{n(y)}" width="{n(w)}" height="{n(h)}" overflow="visible">'
            f'<div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="{style}">{body}</div></foreignObject>')


def arrowhead(x2, y2, ux, uy, color, L=11):
    bx, by = x2 - ux * L, y2 - uy * L
    hw = L * 0.42
    return f'<path d="M{n(x2)},{n(y2)} L{n(bx - uy * hw)},{n(by + ux * hw)} L{n(bx + uy * hw)},{n(by - ux * hw)} Z" fill="{color}"/>'


def link_poly(m, ln, lang):
    """A link's line from the edge of its first box to the edge of its last, through its `via` points."""
    nodes = {nd["id"]: nd for nd in m["nodes"]}
    a, b = nodes[ln["from"]], nodes[ln["to"]]
    pts = [(a["x"], a["y"])] + [tuple(p) for p in ln.get("via", [])] + [(b["x"], b["y"])]
    _, _, wa, ha = box(a, lang); _, _, wb, hb = box(b, lang)
    return [edge_point(a["x"], a["y"], wa, ha, *pts[1])] + pts[1:-1] + [edge_point(b["x"], b["y"], wb, hb, *pts[-2], gap=2)]


def label_box(poly, ln, t):
    """The linking phrase on its line: centre, size and lines; at `at` of the line's length (the middle by default),
    moved by dx, dy where two would meet."""
    segs = list(zip(poly, poly[1:])); total = sum(math.dist(p, q) for p, q in segs)
    goal, run = total * ln.get("at", 0.5), 0
    lx, ly = poly[0]
    for p, q in segs:
        s = math.dist(p, q)
        if run + s >= goal:
            f = (goal - run) / s if s else 0
            lx, ly = p[0] + (q[0] - p[0]) * f, p[1] + (q[1] - p[1]) * f; break
        run += s
    parts = t.split("\n")
    lw = max(width_of(x, LINK_SIZE) for x in parts) + 14; lh = len(parts) * LINK_SIZE * 1.3 + 4
    return lx + ln.get("dx", 0), ly + ln.get("dy", 0), lw, lh, parts


def svg(m, lang="fi", href=None):
    """The map as inline SVG in the figure conventions (NOTES.md §3: every label LaTeX, print quality). href(chapter)
    gives a published chapter's page or None."""
    W, H = m["width"], m["height"]
    nodes = {nd["id"]: nd for nd in m["nodes"]}
    geo = {k: box(nd, lang) for k, nd in nodes.items()}
    lines_svg, labels_svg, boxes_svg = [], [], []
    for ln in m["links"]:
        a, b = nodes[ln["from"]], nodes[ln["to"]]
        cross = ln.get("cross", False)
        color = CROSS if cross else LINK
        poly = link_poly(m, ln, lang); p1 = poly[-1]
        dash = ' stroke-dasharray="7 5"' if cross else ""
        (ux, uy) = (p1[0] - poly[-2][0], p1[1] - poly[-2][1]); L = math.hypot(ux, uy) or 1
        ux, uy = ux / L, uy / L
        short = (p1[0] - ux * 9, p1[1] - uy * 9)
        d = "M" + " L".join(f"{n(x)},{n(y)}" for x, y in poly[:-1] + [short])
        lines_svg.append(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{2 if cross else 1.75}"{dash} stroke-linejoin="round"/>')
        lines_svg.append(arrowhead(p1[0], p1[1], ux, uy, color))
        t = text_of(ln.get("label", ""), lang)
        if t:
            lx, ly, lw, lh, parts = label_box(poly, ln, t)
            labels_svg.append("".join(fo(lx - lw / 2, ly - lh / 2 + i * LINK_SIZE * 1.3, lw, LINK_SIZE * 1.3 + 4, x, LINK_SIZE, color, bg=True, italic=True)
                                      for i, x in enumerate(parts)))
    for k, nd in nodes.items():
        lines, size, w, h = geo[k]
        kind = nd.get("kind", "concept")
        x, y = nd["x"] - w / 2, nd["y"] - h / 2
        if kind == "root": fill, stroke, sw, color, dash = ACCENT, ACCENT, 2, WHITE, ""
        elif kind == "example": fill, stroke, sw, color, dash = PAPER, "#b9ae95", 1.5, INK, ' stroke-dasharray="5 4"'
        else: fill, stroke, sw, color, dash = WHITE, QUANTITY.get(nd.get("quantity"), INK), 2.5 if nd.get("quantity") else 2, INK, ""
        rect = f'<rect x="{n(x)}" y="{n(y)}" width="{n(w)}" height="{n(h)}" rx="{12 if kind != "example" else 8}" fill="{fill}" stroke="{stroke}" stroke-width="{sw:g}"{dash}/>'
        top = nd["y"] - len(lines) * size * 1.35 / 2
        txt = "".join(fo(x + 4, top + i * size * 1.35, w - 8, size * 1.35, l, size, QUANTITY.get(nd.get("quantity"), color) if kind == "concept" and nd.get("quantity") else color)
                      for i, l in enumerate(lines))
        g = rect + txt
        url = href(nd["chapter"]) if href and nd.get("chapter") else None
        if url:
            g = f'<a href="{html.escape(url)}" class="cmap-node">{g}</a>'
        boxes_svg.append(g)
    focus = text_of(m["focus"], lang)
    label = f"{focus} " + "; ".join(f"{text_of(nodes[l['from']]['label'], lang)} {text_of(l.get('label', ''), lang)} {text_of(nodes[l['to']]['label'], lang)}".replace("\n", " ")
                                   for l in m["links"])
    label = re.sub(r"\$([^$]*)\$", lambda mm: mm.group(1), label)
    return (f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="{html.escape(label, quote=True)}" data-fig="kasitekartta" data-nozoom '
            f'class="cmap-svg" style="max-width:100%;font-size:{SIZE["concept"]}px">\n  '
            + f'<rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="14" fill="{WHITE}" stroke="#e3dccb" stroke-width="1.5"/>\n  '
            + "\n  ".join(lines_svg + labels_svg + boxes_svg) + "\n</svg>")


def propositions(m, lang):
    """The map in words, for a phone and a screen reader: each concept with the propositions that start from it."""
    nodes = {nd["id"]: nd for nd in m["nodes"]}
    def lab(k):
        t = text_of(nodes[k]["label"], lang)
        return t.replace("\n", ", ") if nodes[k].get("kind") == "example" else t.replace("\n", " ")
    out, seen = [], []
    for nd in m["nodes"]:
        rows = [l for l in m["links"] if l["from"] == nd["id"]]
        if not rows: continue
        items = "".join(f'<li><span class="cmap-phrase">{html.escape(text_of(l.get("label", ""), lang).replace(chr(10), " "))}</span> → '
                        f'<strong>{html.escape(lab(l["to"]))}</strong></li>' for l in rows)
        out.append(f'<li><strong>{html.escape(lab(nd["id"]))}</strong><ul>{items}</ul></li>')
    return f'<ul class="cmap-words">{"".join(out)}</ul>'


def section(code, T, lang, href=None):
    """The module page's Käsitekartta section, or "" when the module has no map."""
    m = load(code)
    if not m: return ""
    return (f'<section class="cmap" id="kasitekartta"><h2>{T("cmap.title")}</h2>'
            f'<p class="cmap-focus"><span class="cmap-focus-label">{T("cmap.focus")}</span> {html.escape(text_of(m["focus"], lang))}</p>'
            f'<figure class="cmap-fig"><div class="cmap-scroll" tabindex="0" role="region" aria-label="{T("cmap.region")}">{svg(m, lang, href)}</div>'
            f'<figcaption>{T("cmap.caption")} <span class="cmap-scroll-hint">{T("cmap.scroll")}</span></figcaption></figure>'
            f'<details class="cmap-text"><summary>{T("cmap.words")}</summary>{propositions(m, lang)}</details></section>')


def overlaps(m, lang, room=10):
    """Boxes closer than `room` to each other or to the drawing's edge, by the estimated label widths (the page
    check measures the real ones)."""
    out, rects = [], {}
    for nd in m["nodes"]:
        _, _, w, h = box(nd, lang)
        rects[nd["id"]] = (nd["x"] - w / 2, nd["y"] - h / 2, nd["x"] + w / 2, nd["y"] + h / 2)
    for k, (x0, y0, x1, y1) in rects.items():
        if x0 < 12 or y0 < 12 or x1 > m["width"] - 12 or y1 > m["height"] - 12: out.append(f"{k} is outside the drawing")
    for ln in m["links"]:
        t = text_of(ln.get("label", ""), lang)
        if not t: continue
        lx, ly, lw, lh, _ = label_box(link_poly(m, ln, lang), ln, t)
        rects[f"phrase {ln['from']}>{ln['to']}"] = (lx - lw / 2 + 4, ly - lh / 2 + 2, lx + lw / 2 - 4, ly + lh / 2 - 2)
    ks = list(rects)
    for i, a in enumerate(ks):
        for b in ks[i + 1:]:
            A, B = rects[a], rects[b]
            r = 2 if a.startswith("phrase") or b.startswith("phrase") else room
            if a.startswith("phrase") and b.startswith("phrase") is False and b in a.split(" ")[1].split(">"): continue
            if b.startswith("phrase") and not a.startswith("phrase") and a in b.split(" ")[1].split(">"): continue
            if A[0] < B[2] + r and B[0] < A[2] + r and A[1] < B[3] + r and B[1] < A[3] + r: out.append(f"{a} and {b} overlap")
    return out


def check():
    errors = []
    for code in modules():
        m = load(code)
        ids = [nd["id"] for nd in m["nodes"]]
        if len(ids) != len(set(ids)): errors.append(f"{code}: duplicate node id")
        for nd in m["nodes"]:
            for lang in ("fi", "en"):
                if not isinstance(nd["label"], dict) or not nd["label"].get(lang): errors.append(f"{code}: node {nd['id']} has no {lang} label")
            for lang, t in (nd["label"].items() if isinstance(nd["label"], dict) else []):
                if re.search(r"[×÷→]|\\vec|\\mathbf", t): errors.append(f"{code}: node {nd['id']} {lang}: notation (× ÷ \\vec \\mathbf)")
                if re.search(r"[α-ωΔρ²³]", re.sub(r"\$[^$]*\$", "", t)): errors.append(f"{code}: node {nd['id']} {lang}: Unicode maths outside LaTeX")
            if nd.get("quantity") and nd["quantity"] not in QUANTITY: errors.append(f"{code}: node {nd['id']}: unknown quantity")
        for ln in m["links"]:
            for end in ("from", "to"):
                if ln[end] not in ids: errors.append(f"{code}: link to unknown node {ln[end]}")
            for lang in ("fi", "en"):
                if ln.get("label") and not ln["label"].get(lang): errors.append(f"{code}: link {ln['from']}→{ln['to']} has no {lang} phrase")
        for lang in ("fi", "en", "fi-easy"):
            errors += [f"{code} {lang}: {e}" for e in overlaps(m, lang)]
        linked = {l["from"] for l in m["links"]} | {l["to"] for l in m["links"]}
        for k in ids:
            if k not in linked: errors.append(f"{code}: node {k} is not linked")
        for lang in ("fi", "en"):
            if not text_of(m["focus"], lang): errors.append(f"{code}: no {lang} focus question")
    for e in errors: print(e)
    print(f"conceptmaps: {len(modules())} maps, {len(errors)} errors")
    return not errors


if __name__ == "__main__":
    if sys.argv[1:2] == ["check"]: sys.exit(0 if check() else 1)
    if sys.argv[1:2] == ["svg"]: print(svg(load(sys.argv[2]), sys.argv[3] if len(sys.argv) > 3 else "fi"))
