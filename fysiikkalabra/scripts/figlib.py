"""Figure helpers for lesson figures (NOTES.md §3): textbook-quality inline SVG with every label in LaTeX.

A lesson keeps the source of its figures in `figures.py` in its folder; `python scripts/figures.py <id>` writes each
figure into lesson.md in place of the `<svg data-fig="<name>" ...>...</svg>` block of the same name, so lesson.md
stays the page's single source and the figure code stays editable. Coordinates are in the 600-unit-wide viewBox.

    from figlib import Fig, Axes, INK, MUTED, HEAT, WATER
    def force_extension():
        f = Fig("fy31-graph", 340, "Kuvaaja mittakaavassa: ...")
        ax = Axes(f, (96, 286), (548, 40), x=(0, 12), y=(0, 5), xticks=[0, 2.5, 5, 10], yticks=[1, 2, 4],
                  xlabel=r"F\\ (\\text{N})", ylabel=r"x\\ (\\text{cm})")
        ax.line([(0, 0), (11, 4.4)], INK)
        for p in [(2.5, 1), (5, 2), (10, 4)]: ax.guide(*p); ax.point(*p)
        f.tex(400, 230, r"\\text{suora origon kautta}")
        return f.svg()
    FIGURES = {"force-extension": force_extension}

Labels: `Fig.tex(x, y, tex, anchor)` puts a KaTeX label whose box is centred vertically on y; anchor start | middle |
end says whether x is its left edge, centre or right edge (like SVG text-anchor). Words go in \\text{}.

Languages: figures.py is written once, in Finnish. For another language `python scripts/figures.py <id> --lang en`
calls set_language() first with content/en/<COURSE>/<id>/figures.json, {Finnish text: translation}: the words of
every \\text{} and every figure's description (Fig label) are looked up there, and the decimal comma {,} becomes the
language's decimal sign. Formulas, symbols and numbers stay as figures.py draws them.
"""
import html, re

INK, MUTED, RULE, RULE_LIGHT, WHITE = "#1f2933", "#6b7480", "#c9c2b2", "#e3dccb", "#ffffff"
GLASS, WATER_LIGHT, WATER = "#eef5f9", "#a9d1f0", "#2f74b5"
SAND_LIGHT, SAND, SAND_DARK, GRAIN = "#f1dfb5", "#d9b26a", "#e9c98a", "#a97a35"
HEAT_LIGHT, HEAT, HOT, HOT_LIGHT, COLD, COLD_LIGHT = "#ffc078", "#e8590c", "#c92a2a", "#f2a69c", "#1971c2", "#d0e6fb"
ALUMINIUM, METAL_EDGE, IRON, COPPER, ICE, ICE_EDGE = "#c4ccd4", "#8a96a3", "#6c757d", "#b8622d", "#a5d8ff", "#4f8fbf"
GOOD, GOOD_LIGHT = "#2b8a3e", "#b2f2bb"
PAPER = "#f6f1e6"   # the warm paper behind a chapter's opening illustration (Fig(..., hero=True))


TEXTS = {}          # Finnish text -> the text in the language being drawn (set_language)
DECIMAL = "{,}"     # a number's decimal sign in LaTeX: {,} in Finnish
UNITS = set("kg g mg m s N J K Pa kPa MPa kJ MJ W kW Wh kWh h min cm mm km l dl ml dm mol Hz °C".split()) | {""}   # the same in every language
MISSING = []        # Finnish texts drawn without a translation (figures.py reports them)


def set_language(texts, decimal=","):
    global TEXTS, DECIMAL
    TEXTS, DECIMAL = dict(texts), "{,}" if decimal == "," else decimal; MISSING.clear()


def translate(text, tex=True):
    """A label in the language being drawn: in LaTeX the contents of each \\text{} and the decimal comma, a plain
    description as a whole. In Finnish it is the text as it is."""
    if not TEXTS and DECIMAL == "{,}": return text
    def word(t):
        if t.strip() not in UNITS and t not in TEXTS and re.search(r"[A-Za-zÄÖÅäöå]{2,}", t) and t not in MISSING: MISSING.append(t)
        return TEXTS.get(t, t)
    if not tex: return word(text)
    text = re.sub(r"(\\(?:text|mathrm|textsf)\{)([^{}]*)\}", lambda m: m.group(1) + word(m.group(2)) + "}", text)
    return text.replace("{,}", DECIMAL)


def n(v):
    """A coordinate on a half pixel at most, without trailing zeros."""
    v = round(v * 2) / 2
    return str(int(v)) if v == int(v) else f"{v:.1f}"


def fi(v, digits=None):
    """A number for a LaTeX label: decimal comma as {,}, true minus."""
    s = f"{v:.{digits}f}" if digits is not None else (f"{v:g}" if not float(v).is_integer() else str(int(v)))
    return s.replace(".", DECIMAL)


def visible_len(tex):
    """A rough count of the characters KaTeX draws, for the label box (the layout check measures the real one)."""
    t = re.sub(r"\\(?:text|mathrm|textsf|mathbf)\{([^{}]*)\}", r"\1", tex)
    t = re.sub(r"\\[dt]?frac\{([^{}]*)\}\{([^{}]*)\}", lambda m: max(m.group(1), m.group(2), key=len), t)
    t = re.sub(r"\\[a-zA-Z]+", "x", t)
    return len(re.sub(r"[{}^_\\ ]", "", t)) + t.count("\\ ") * 0.3


class Fig:
    def __init__(self, fid, height, label, width=600, size=24, hero=False):
        """hero: the chapter's opening illustration, 1200 wide, full column width under the Miksi question (site.css .fig-hero)."""
        self.fid, self.w, self.h, self.label, self.size, self.hero = fid, width, height, translate(label, tex=False), size, hero
        self.defs, self.body = [], []

    # drawing
    def add(self, s): self.body.append(s); return self
    def defs_add(self, s): self.defs.append(s); return self

    def line(self, x1, y1, x2, y2, color=INK, w=2, dash=None, cap="butt"):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        return self.add(f'<line x1="{n(x1)}" y1="{n(y1)}" x2="{n(x2)}" y2="{n(y2)}" stroke="{color}" stroke-width="{w:g}" stroke-linecap="{cap}"{d}/>')

    def path(self, d, fill="none", stroke=None, w=2, extra=""):
        s = f' stroke="{stroke}" stroke-width="{w:g}"' if stroke else ""
        return self.add(f'<path d="{d}" fill="{fill}"{s} stroke-linejoin="round"{(" " + extra) if extra else ""}/>')

    def rect(self, x, y, w, h, fill="none", stroke=None, sw=2, rx=0, extra=""):
        s = f' stroke="{stroke}" stroke-width="{sw:g}"' if stroke else ""
        r = f' rx="{rx:g}"' if rx else ""
        return self.add(f'<rect x="{n(x)}" y="{n(y)}" width="{n(w)}" height="{n(h)}"{r} fill="{fill}"{s}{(" " + extra) if extra else ""}/>')

    def circle(self, cx, cy, r, fill=INK, stroke=None, sw=2):
        s = f' stroke="{stroke}" stroke-width="{sw:g}"' if stroke else ""
        return self.add(f'<circle cx="{n(cx)}" cy="{n(cy)}" r="{r:g}" fill="{fill}"{s}/>')

    def arrow(self, x1, y1, x2, y2, color=INK, w=3, head=14):
        """A straight arrow from (x1, y1) to the tip (x2, y2): a shaft and a filled head (NOTES 3)."""
        import math
        L = math.hypot(x2 - x1, y2 - y1); ux, uy = (x2 - x1) / L, (y2 - y1) / L
        bx, by = x2 - ux * head, y2 - uy * head
        hw = head * 0.45
        self.line(x1, y1, bx + ux, by + uy, color, w)
        return self.path(f"M{n(x2)},{n(y2)} L{n(bx - uy * hw)},{n(by + ux * hw)} L{n(bx + uy * hw)},{n(by - ux * hw)} Z", fill=color)

    def block_arrow(self, x1, y1, x2, y2, fill, shaft=16, head=34, headlen=28):
        """A wide filled arrow (energy or heat flow, a force with a width that means its size)."""
        import math
        L = math.hypot(x2 - x1, y2 - y1); ux, uy = (x2 - x1) / L, (y2 - y1) / L
        px, py = -uy, ux
        bx, by = x2 - ux * headlen, y2 - uy * headlen
        pts = [(x1 + px * shaft / 2, y1 + py * shaft / 2), (bx + px * shaft / 2, by + py * shaft / 2), (bx + px * head / 2, by + py * head / 2),
               (x2, y2), (bx - px * head / 2, by - py * head / 2), (bx - px * shaft / 2, by - py * shaft / 2), (x1 - px * shaft / 2, y1 - py * shaft / 2)]
        return self.path("M" + " L".join(f"{n(a)},{n(b)}" for a, b in pts) + " Z", fill=fill)

    def tex(self, x, y, tex, anchor="start", color=INK, size=None, w=None, bg=False):
        """A LaTeX label centred vertically on y; x is its left edge, centre or right edge (anchor). bg puts the
        figure's white under the label, for a label that sits on gridlines."""
        size = size or self.size; tex = translate(tex)
        tall = re.search(r"\\d?frac|\\sqrt|\\sum|\\int", tex)
        h = round(size * (2.4 if tall else 1.2))            # about the rendered height: check_layout.py measures the box
        w = w or round(visible_len(tex) * size * 0.52 + 8)
        x0 = x if anchor == "start" else x - w / 2 if anchor == "middle" else x - w
        just = {"start": "flex-start", "middle": "center", "end": "flex-end"}[anchor]
        style = f"display:flex;align-items:center;justify-content:{just};height:100%;font-size:{size:g}px" + (f";color:{color}" if color != INK else "")
        return self.add(f'<foreignObject x="{n(x0)}" y="{n(y - h / 2)}" width="{n(w)}" height="{h}" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="{style}">{f'<span style="background:{WHITE};padding:0 5px;border-radius:3px">${tex}$</span>' if bg else f'${tex}$'}</div></foreignObject>')

    def svg(self, name=None):
        attrs = (f' data-fig="{name}"' if name else "") + (' class="fig-hero"' if self.hero else "")
        defs = f"\n  <defs>{''.join(self.defs)}</defs>" if self.defs else ""
        body = "\n  ".join(self.body)
        return (f'<svg viewBox="0 0 {self.w} {self.h}" role="img" aria-label="{html.escape(self.label, quote=True)}"{attrs} '
                f'style="max-width:100%;font-size:{self.size}px">{defs}\n  {body}\n</svg>')


class Axes:
    """A graph: origin and top-right corner of the plot area in figure units, data ranges, ticks with LaTeX numbers,
    gridlines on every tick, axes with filled arrowheads and the axis titles at the arrow ends (NOTES 3, Graphs)."""

    def __init__(self, fig, origin, corner, x, y, xticks, yticks, xlabel, ylabel, grid=True, xfmt=None, yfmt=None,
                 arrow_room=26, origin_label=True):
        self.f, (self.x0, self.y0), (self.x1, self.y1) = fig, origin, corner
        self.xr, self.yr = x, y
        X, Y = self.X, self.Y
        if grid:
            for t in xticks:
                if t != x[0]: fig.line(X(t), self.y0, X(t), self.y1, RULE_LIGHT, 1.5)
            for t in yticks:
                if t != y[0]: fig.line(self.x0, Y(t), self.x1, Y(t), RULE_LIGHT, 1.5)
        ax_end, ay_end = self.x1 + arrow_room, self.y1 - arrow_room
        fig.arrow(self.x0 - 1, self.y0, ax_end, self.y0, INK, 2.5, 13)
        fig.arrow(self.x0, self.y0 + 1, self.x0, ay_end, INK, 2.5, 13)
        xf = xfmt or (lambda v: fi(v)); yf = yfmt or (lambda v: fi(v))
        for t in xticks:
            if t == x[0]: continue
            fig.line(X(t), self.y0, X(t), self.y0 + 7, INK, 2)
            if xf(t) != "": fig.tex(X(t), self.y0 + 24, xf(t), "middle")     # an empty format: a tick and gridline without a number
        for t in yticks:
            if t == y[0]: continue
            fig.line(self.x0 - 7, Y(t), self.x0, Y(t), INK, 2)
            if yf(t) != "": fig.tex(self.x0 - 12, Y(t), yf(t), "end")
        if origin_label and x[0] == 0 and y[0] == 0:
            fig.tex(self.x0 - 10, self.y0 + 20, "0", "end")
        # the axis titles beyond the arrow tips, where no data, tick or gridline can reach them: leave about
        # 80 units right of the x arrow and 30 above the y arrow
        fig.tex(ax_end + 6, self.y0, xlabel, "start") if xlabel else None
        fig.tex(self.x0 - 10, ay_end - 16, ylabel, "start") if ylabel else None

    def X(self, v): return self.x0 + (v - self.xr[0]) / (self.xr[1] - self.xr[0]) * (self.x1 - self.x0)
    def Y(self, v): return self.y0 - (v - self.yr[0]) / (self.yr[1] - self.yr[0]) * (self.y0 - self.y1)

    def line(self, pts, color=INK, w=3, dash=None):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        p = " ".join(f"{n(self.X(a))},{n(self.Y(b))}" for a, b in pts)
        return self.f.add(f'<polyline points="{p}" fill="none" stroke="{color}" stroke-width="{w:g}" stroke-linejoin="round" stroke-linecap="round"{d}/>')

    def curve(self, fn, a, b, color=INK, w=3, steps=120, dash=None):
        return self.line([(a + (b - a) * i / steps, fn(a + (b - a) * i / steps)) for i in range(steps + 1)], color, w, dash)

    def point(self, a, b, color=INK, r=6.5):
        return self.f.circle(self.X(a), self.Y(b), r, color, WHITE, 2)

    def guide(self, a, b, color=MUTED):
        """Dashed lines from a point to both axes, where the text reads a value off the graph."""
        self.f.line(self.X(a), self.Y(b), self.X(a), self.y0, color, 1.5, "6 5")
        return self.f.line(self.x0, self.Y(b), self.X(a), self.Y(b), color, 1.5, "6 5")

    def area(self, pts, fill, opacity=0.35):
        p = " ".join(f"{n(self.X(a))},{n(self.Y(b))}" for a, b in pts)
        return self.f.add(f'<polygon points="{p}" fill="{fill}" fill-opacity="{opacity:g}"/>')
