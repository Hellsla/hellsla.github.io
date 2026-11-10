"""The house illustration style (docs/illustration-style.md): a layer over figlib that every course's figures.py can opt
into with `from figstyle import Fig, Axes, hero, scene`. Same drawing calls as figlib; what changes is how they look:

- one arrow for every vector and axis: a concave "stealth" head whose size follows the stroke, tip exactly on the point;
- stroke tokens: object outlines 1.75, details 1.0, guide lines 1.25 dashed "5 4", axes 1.75, grid 1.0 in GRID,
  vectors 3.25 (600-unit figures; an opening illustration keeps its own widths);
- outlines of filled shapes in a darker tint of their own fill instead of black ink (a white or glass shape gets
  SOFT_INK), so a drawing reads as an illustration, not an icon;
- helpers the guide asks for: vec, leader, dim_v, ball, hatch_ground, shade/light tints.
Labels are unchanged: every label is LaTeX, words in \\text{} (serif, like the formulas; teacher 2026-11-10)."""
import math, re
import figlib
from figlib import n, INK, MUTED, WHITE, RULE_LIGHT, GLASS, PAPER

W_OBJ, W_DETAIL, W_GUIDE, W_AXIS, W_DATA, W_VEC = 1.75, 1.0, 1.25, 1.75, 3.0, 3.25
GRID, GUIDE_DASH, SOFT_INK = "#e7e2d7", "5 4", "#3a4350"
LIGHT_FILLS = {WHITE, "#fff", "#ffffff", GLASS, PAPER, "#eef0f2"}


def mix(c, d, t):
    a = [int(c[i:i + 2], 16) for i in (1, 3, 5)]; b = [int(d[i:i + 2], 16) for i in (1, 3, 5)]
    return "#" + "".join(f"{round(x + (y - x) * t):02x}" for x, y in zip(a, b))


def dark(c, t=0.22): return mix(c, "#000000", t)
def light(c, t=0.55): return mix(c, "#ffffff", t)


def _outline_for(fill):
    """The outline colour of a filled shape: a darker tint of a solid fill, soft ink for light, gradient or no fill."""
    if fill and re.fullmatch(r"#[0-9a-fA-F]{6}", fill) and fill.lower() not in LIGHT_FILLS:
        lum = sum(int(fill[i:i + 2], 16) for i in (1, 3, 5)) / 3
        return dark(fill, 0.45 if lum > 170 else 0.38)
    return SOFT_INK


_EL = re.compile(r"<(rect|circle|ellipse|path|polygon|polyline|line)\b[^>]*>")


def _restyle(el, hero):
    """One SVG element in the house style: tinted outlines and the stroke tokens."""
    stroke = re.search(r'stroke="([^"]+)"', el); sw = re.search(r'stroke-width="([\d.]+)"', el)
    if not stroke: return el
    s, w = stroke.group(1), float(sw.group(1)) if sw else 1.0
    fill = re.search(r'fill="([^"]+)"', el); fill = fill.group(1) if fill else None
    tag = el[1:el.index(" ")]
    if s == INK and tag not in ("line", "polyline") and fill not in (None, "none"):
        el = el.replace(f'stroke="{INK}"', f'stroke="{_outline_for(fill)}"', 1)
        if not hero and 2 <= w <= 3: el = el.replace(f'stroke-width="{sw.group(1)}"', f'stroke-width="{W_OBJ:g}"', 1)
    elif s == INK and not hero and 2 <= w <= 2.5:
        el = el.replace(f'stroke-width="{sw.group(1)}"', f'stroke-width="{W_OBJ:g}"', 1)
    elif s == RULE_LIGHT and tag == "line" and not hero:
        el = el.replace(f'stroke="{RULE_LIGHT}"', f'stroke="{GRID}"', 1).replace(f'stroke-width="{sw.group(1)}"', f'stroke-width="{W_DETAIL:g}"', 1) if sw else el
    elif s == MUTED and not hero and "stroke-dasharray" in el and w <= 1.5:
        el = re.sub(r'stroke-dasharray="[^"]+"', f'stroke-dasharray="{GUIDE_DASH}"', el)
        el = el.replace(f'stroke-width="{sw.group(1)}"', f'stroke-width="{W_GUIDE:g}"', 1) if sw else el
    return el


class Fig(figlib.Fig):
    def arrow(self, x1, y1, x2, y2, color=INK, w=3, head=14):
        """figlib's arrow in the house style: axes (ink, ≤ 2.5) get the axis token, vectors (≥ 3) the vector token."""
        if not self.hero: w = W_AXIS if (color == INK and w <= 2.5) else W_VEC if w >= 3 else w
        return self.vec(x1, y1, x2, y2, color, w)

    def vec(self, x1, y1, x2, y2, color, w=W_VEC):
        """A vector: shaft and concave head; the tip is exactly at (x2, y2)."""
        L = math.hypot(x2 - x1, y2 - y1)
        if L == 0: return self
        ux, uy = (x2 - x1) / L, (y2 - y1) / L; px, py = -uy, ux
        hl = min(3.6 * w + 5, L * 0.6); hw = hl * 0.4 + 0.2 * w; notch = 0.72
        bx, by = x2 - ux * hl, y2 - uy * hl; nx, ny = x2 - ux * hl * notch, y2 - uy * hl * notch
        self.body.append(f'<line x1="{n(x1)}" y1="{n(y1)}" x2="{n(nx)}" y2="{n(ny)}" stroke="{color}" stroke-width="{w:g}" stroke-linecap="butt"/>')
        return self.add(f'<path d="M{n(x2)},{n(y2)} L{n(bx + px * hw)},{n(by + py * hw)} L{n(nx)},{n(ny)} L{n(bx - px * hw)},{n(by - py * hw)} Z" fill="{color}" stroke-linejoin="round"/>')

    def leader(self, x1, y1, x2, y2):
        """A thin label leader from an object (small dot) to its label."""
        self.body.append(f'<line x1="{n(x1)}" y1="{n(y1)}" x2="{n(x2)}" y2="{n(y2)}" stroke="{MUTED}" stroke-width="{W_DETAIL:g}"/>')
        return self.add(f'<circle cx="{n(x1)}" cy="{n(y1)}" r="2.2" fill="{MUTED}"/>')

    def dim_v(self, x, y1, y2, tex, color=INK, side="right", size=None):
        """A vertical dimension line with end ticks and its label."""
        for a, b, c, d in ((x, y1, x, y2), (x - 6, y1, x + 6, y1), (x - 6, y2, x + 6, y2)):
            self.body.append(f'<line x1="{n(a)}" y1="{n(b)}" x2="{n(c)}" y2="{n(d)}" stroke="{color}" stroke-width="1.25"/>')
        return self.tex(x + 12 if side == "right" else x - 12, (y1 + y2) / 2, tex, "start" if side == "right" else "end", color, size)

    def dim_h(self, x1, x2, y, tex, color=INK, below=True, size=None):
        """A horizontal dimension line with end ticks and its label."""
        for a, b, c, d in ((x1, y, x2, y), (x1, y - 6, x1, y + 6), (x2, y - 6, x2, y + 6)):
            self.body.append(f'<line x1="{n(a)}" y1="{n(b)}" x2="{n(c)}" y2="{n(d)}" stroke="{color}" stroke-width="1.25"/>')
        return self.tex((x1 + x2) / 2, y + 20 if below else y - 20, tex, "middle", color, size)

    def ball(self, gid, cx, cy, r, base):
        """A sphere: flat base, a crescent shadow, a soft highlight; the outline a darker tint of the base."""
        self.defs_add(f'<clipPath id="{gid}"><circle cx="{n(cx)}" cy="{n(cy)}" r="{r:g}"/></clipPath>')
        self.body.append(f'<circle cx="{n(cx)}" cy="{n(cy)}" r="{r:g}" fill="{base}"/>')
        self.body.append(f'<circle cx="{n(cx + r * 0.42)}" cy="{n(cy + r * 0.42)}" r="{n(r * 1.05)}" fill="none" stroke="{dark(base, 0.2)}" '
                         f'stroke-width="{n(r * 0.55)}" clip-path="url(#{gid})" opacity="0.55"/>')
        self.body.append(f'<ellipse cx="{n(cx - r * 0.36)}" cy="{n(cy - r * 0.4)}" rx="{n(r * 0.3)}" ry="{n(r * 0.2)}" '
                         f'transform="rotate(-35 {n(cx - r * 0.36)} {n(cy - r * 0.4)})" fill="{WHITE}" opacity="0.8"/>')
        return self.add(f'<circle cx="{n(cx)}" cy="{n(cy)}" r="{r:g}" fill="none" stroke="{dark(base, 0.38)}" stroke-width="{W_OBJ:g}"/>')

    def hatch_ground(self, x1, x2, y):
        """A fixed surface: a line with short 45° hatching below it (mechanics convention)."""
        for x in range(int(x1) + 6, int(x2), 12):
            self.body.append(f'<line x1="{x}" y1="{n(y + 1)}" x2="{x - 9}" y2="{n(y + 10)}" stroke="{MUTED}" stroke-width="{W_DETAIL:g}"/>')
        return self.add(f'<line x1="{n(x1)}" y1="{n(y)}" x2="{n(x2)}" y2="{n(y)}" stroke="{INK}" stroke-width="{W_OBJ:g}"/>')

    def svg(self, name=None):
        out = super().svg(name).replace("<svg ", '<svg data-style="house" ', 1)
        return _EL.sub(lambda m: _restyle(m.group(0), self.hero), out)


class Axes(figlib.Axes):
    """figlib's graph; its gridlines, axes and ticks come out in the house tokens through Fig."""
    def point(self, a, b, color=INK, r=5.5):
        return self.f.circle(self.X(a), self.Y(b), r, color, WHITE, 2)

    def line(self, pts, color=INK, w=3, dash=None):
        return super().line(pts, color, W_DATA if w >= 3 else w, dash)


def hero(fid, label): return Fig(fid, 600, label, width=1200, hero=True)
def scene(fid, label): return Fig(fid, 360, label)
