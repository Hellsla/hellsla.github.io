"""Shared pieces of the chapters' opening illustrations (NOTES.md §3 "Opening illustration"): flat shapes in the
figure palette, no text. A lesson's figures.py draws its scene with these on a Fig(..., width=1200, hero=True)."""
import math
from figlib import (Fig, INK, MUTED, RULE, RULE_LIGHT, WHITE, GLASS, WATER_LIGHT, WATER, SAND_LIGHT, SAND, SAND_DARK, GRAIN,
                    HEAT_LIGHT, HEAT, HOT, HOT_LIGHT, COLD, COLD_LIGHT, ALUMINIUM, METAL_EDGE, IRON, COPPER, ICE, ICE_EDGE,
                    GOOD, GOOD_LIGHT, PAPER, n)


def hero(fid, label): return Fig(fid, 600, label, width=1200, hero=True)


def scene(fid, label):
    """A second, smaller everyday scene (600 × 360, `data-fig="scene"`) beside the summary list."""
    return Fig(fid, 360, label)


def rnd(k, seed=1):
    """A fixed pseudo-random number in [0, 1) for the k-th item, so a figure redraws identically."""
    return (math.sin(k * 12.9898 + seed * 78.233) * 43758.5453) % 1


def grad(f, gid, c1, c2, horizontal=False, y1=None, y2=None):
    """A linear gradient in the figure's defs; y1/y2 make it span fixed figure units instead of the shape."""
    if y1 is not None:
        f.defs_add(f'<linearGradient id="{gid}" gradientUnits="userSpaceOnUse" x1="0" y1="{y1}" x2="0" y2="{y2}"><stop offset="0" stop-color="{c1}"/><stop offset="1" stop-color="{c2}"/></linearGradient>')
    else:
        x2, y2_ = ("1", "0") if horizontal else ("0", "1")
        f.defs_add(f'<linearGradient id="{gid}" x1="0" y1="0" x2="{x2}" y2="{y2_}"><stop offset="0" stop-color="{c1}"/><stop offset="1" stop-color="{c2}"/></linearGradient>')
    return f"url(#{gid})"


def sky(f, pre, bottom=600, c1=ICE, c2=GLASS):
    f.rect(0, 0, 1200, bottom, grad(f, f"{pre}-sky", c1, c2))


def space(f, seed=1, count=70):
    f.rect(0, 0, 1200, 600, INK)
    for k in range(count):
        f.circle(rnd(k, seed) * 1200, rnd(k + 500, seed) * 600, 1 + 1.6 * rnd(k + 900, seed), WHITE)


def sun(f, pre, cx, cy, r=58, rays=True):
    f.add(f'<circle cx="{n(cx)}" cy="{n(cy)}" r="{n(r * 1.6)}" fill="{WHITE}" fill-opacity="0.5"/>')
    if rays:
        for k in range(12):
            a = k * math.pi / 6 + math.pi / 12
            c, s = math.cos(a), math.sin(a)
            r0, r1, hw = r * 1.24, r * 1.74, 7
            f.path(f"M{n(cx + c * r0 - s * hw)},{n(cy + s * r0 + c * hw)} L{n(cx + c * r1)},{n(cy + s * r1)} L{n(cx + c * r0 + s * hw)},{n(cy + s * r0 - c * hw)} Z", HEAT_LIGHT)
    f.defs_add(f'<radialGradient id="{pre}-sun" cx="0.4" cy="0.4" r="0.7"><stop offset="0" stop-color="{HEAT_LIGHT}"/><stop offset="1" stop-color="{HEAT}"/></radialGradient>')
    f.circle(cx, cy, r, f"url(#{pre}-sun)")


def cloud(f, cx, cy, sc=1.0, fill=WHITE, extra=""):
    f.path(f"M{n(cx - 90 * sc)},{n(cy + 20 * sc)} Q{n(cx - 92 * sc)},{n(cy - 14 * sc)} {n(cx - 52 * sc)},{n(cy - 10 * sc)} "
           f"Q{n(cx - 36 * sc)},{n(cy - 46 * sc)} {n(cx + 4 * sc)},{n(cy - 34 * sc)} Q{n(cx + 40 * sc)},{n(cy - 54 * sc)} {n(cx + 60 * sc)},{n(cy - 16 * sc)} "
           f"Q{n(cx + 96 * sc)},{n(cy - 12 * sc)} {n(cx + 92 * sc)},{n(cy + 20 * sc)} Z", fill, extra=extra)


def forest(f, y0, h, step, colour, seed=1, x0=0, x1=1200, depth=30):
    """A line of spruce tops along y0 (the far shore or the edge of a field)."""
    d, x, k = f"M{x0},{y0}", x0, 0
    while x < x1:
        r = rnd(k, seed); w = step * (0.7 + 0.6 * r)
        d += f" L{n(x + w / 2)},{n(y0 - h * (0.45 + 0.55 * r))} L{n(x + w)},{y0}"
        x += w; k += 1
    f.path(d + f" V{y0 + depth} H{x0} Z", colour)


def shimmer(f, xs, ybot, length=96, colour=HEAT):
    """Heat shimmering up from a hot surface."""
    for x in xs:
        f.path(f"M{n(x)},{n(ybot)} q-12,{n(-length / 6)} 0,{n(-length / 3)} t0,{n(-length / 3)} t0,{n(-length / 3)}", stroke=colour, w=4,
               extra='stroke-linecap="round" stroke-opacity="0.75"')


def thermometer(f, x, ybot, level, colour=HOT, length=150):
    f.rect(x - 9, ybot - length, 18, length, WHITE, INK, 3, 9)
    f.circle(x, ybot, 16, colour, INK, 3)
    f.rect(x - 4, ybot - level, 8, level, colour)
    for k in range(1, int(length / 22)):
        f.line(x + 9, ybot - 22 * k, x + 17, ybot - 22 * k, MUTED, 2)


def person(f, x, yfeet, shirt=COLD, trousers=INK, sc=1.0, arms="down"):
    """A simple standing figure without facial features: feet at (x, yfeet). arms: down | up (holding something
    above the head, hands at about yfeet - 330 sc)."""
    s = sc
    f.path(f"M{n(x - 26 * s)},{n(yfeet)} L{n(x - 20 * s)},{n(yfeet - 150 * s)} H{n(x + 20 * s)} L{n(x + 26 * s)},{n(yfeet)} H{n(x + 6 * s)} L{n(x)},{n(yfeet - 100 * s)} L{n(x - 6 * s)},{n(yfeet)} Z", trousers)
    f.path(f"M{n(x - 34 * s)},{n(yfeet - 140 * s)} Q{n(x - 38 * s)},{n(yfeet - 250 * s)} {n(x)},{n(yfeet - 256 * s)} Q{n(x + 38 * s)},{n(yfeet - 250 * s)} {n(x + 34 * s)},{n(yfeet - 140 * s)} Z", shirt)
    if arms == "up":
        for sgn in (-1, 1):
            f.path(f"M{n(x + sgn * 26 * s)},{n(yfeet - 236 * s)} L{n(x + sgn * 40 * s)},{n(yfeet - 330 * s)}", stroke=shirt, w=22 * s, extra='stroke-linecap="round"')
            f.circle(x + sgn * 40 * s, yfeet - 334 * s, 11 * s, SAND_LIGHT)
    else:
        for sgn in (-1, 1):
            f.path(f"M{n(x + sgn * 30 * s)},{n(yfeet - 236 * s)} L{n(x + sgn * 40 * s)},{n(yfeet - 140 * s)}", stroke=shirt, w=22 * s, extra='stroke-linecap="round"')
            f.circle(x + sgn * 40 * s, yfeet - 132 * s, 11 * s, SAND_LIGHT)
    f.rect(x - 9 * s, yfeet - 276 * s, 18 * s, 24 * s, SAND_LIGHT)
    f.circle(x, yfeet - 296 * s, 30 * s, SAND_LIGHT)
    f.path(f"M{n(x - 31 * s)},{n(yfeet - 296 * s)} Q{n(x - 30 * s)},{n(yfeet - 332 * s)} {n(x)},{n(yfeet - 330 * s)} Q{n(x + 32 * s)},{n(yfeet - 330 * s)} {n(x + 31 * s)},{n(yfeet - 300 * s)} Q{n(x + 6 * s)},{n(yfeet - 312 * s)} {n(x - 31 * s)},{n(yfeet - 296 * s)} Z", INK)


def earth(f, pre, cx, cy, r):
    """The Earth seen from space: oceans, land, clouds and a thin atmosphere."""
    f.defs_add(f'<radialGradient id="{pre}-ocean" cx="0.35" cy="0.35" r="0.8"><stop offset="0" stop-color="{WATER_LIGHT}"/><stop offset="1" stop-color="{WATER}"/></radialGradient>')
    f.defs_add(f'<clipPath id="{pre}-clip"><circle cx="{n(cx)}" cy="{n(cy)}" r="{n(r)}"/></clipPath>')
    f.add(f'<circle cx="{n(cx)}" cy="{n(cy)}" r="{n(r * 1.07)}" fill="{ICE}" fill-opacity="0.35"/>')
    f.circle(cx, cy, r, f"url(#{pre}-ocean)")
    u = r / 100
    f.add(f'<g clip-path="url(#{pre}-clip)">')
    f.path(f"M{n(cx - 70 * u)},{n(cy - 60 * u)} Q{n(cx - 30 * u)},{n(cy - 90 * u)} {n(cx + 5 * u)},{n(cy - 62 * u)} Q{n(cx + 20 * u)},{n(cy - 30 * u)} {n(cx - 10 * u)},{n(cy - 10 * u)} "
           f"Q{n(cx - 5 * u)},{n(cy + 30 * u)} {n(cx - 30 * u)},{n(cy + 60 * u)} Q{n(cx - 50 * u)},{n(cy + 20 * u)} {n(cx - 60 * u)},{n(cy - 5 * u)} Q{n(cx - 90 * u)},{n(cy - 30 * u)} {n(cx - 70 * u)},{n(cy - 60 * u)} Z", SAND_DARK)
    f.path(f"M{n(cx + 30 * u)},{n(cy + 10 * u)} Q{n(cx + 70 * u)},{n(cy - 5 * u)} {n(cx + 85 * u)},{n(cy + 30 * u)} Q{n(cx + 70 * u)},{n(cy + 70 * u)} {n(cx + 40 * u)},{n(cy + 60 * u)} Q{n(cx + 20 * u)},{n(cy + 40 * u)} {n(cx + 30 * u)},{n(cy + 10 * u)} Z", SAND_DARK)
    for k, (dx, dy, w) in enumerate(((-40, -80, 70), (40, -40, 60), (-80, 30, 50), (10, 80, 80), (60, 70, 40))):
        f.path(f"M{n(cx + dx * u)},{n(cy + dy * u)} q{n(w * u / 2)},{n(-8 * u)} {n(w * u)},0", stroke=WHITE, w=7 * u, extra='stroke-linecap="round" stroke-opacity="0.85"')
    f.add("</g>")


def stopwatch(f, cx, cy, r, turn, face=WHITE, hand=HOT):
    """A stopwatch without numerals: the hand at `turn` of a full round (0 = up, clockwise)."""
    f.rect(cx - r * 0.16, cy - r * 1.32, r * 0.32, r * 0.24, IRON, INK, 2, 3)
    f.rect(cx - r * 0.07, cy - r * 1.1, r * 0.14, r * 0.14, IRON)
    f.circle(cx, cy, r, ALUMINIUM, INK, 3)
    f.circle(cx, cy, r * 0.82, face, INK, 2)
    for k in range(12):
        a = k * math.pi / 6; c, s = math.sin(a), -math.cos(a)
        f.line(cx + c * r * 0.68, cy + s * r * 0.68, cx + c * r * 0.78, cy + s * r * 0.78, MUTED, 2)
    a = turn * 2 * math.pi
    f.line(cx, cy, cx + math.sin(a) * r * 0.66, cy - math.cos(a) * r * 0.66, hand, max(2, r * 0.07), cap="round")
    f.circle(cx, cy, r * 0.08, INK)


def probe(f, cx, cy, sc=1.0):
    """A Voyager-style space probe: a white dish facing the viewer's left, a body and two booms."""
    s = sc
    f.line(cx, cy, cx + 150 * s, cy - 40 * s, METAL_EDGE, 4 * s)
    f.line(cx, cy, cx + 110 * s, cy + 70 * s, METAL_EDGE, 4 * s)
    f.circle(cx + 150 * s, cy - 40 * s, 9 * s, IRON)
    f.rect(cx + 100 * s, cy + 64 * s, 22 * s, 14 * s, IRON, INK, 2)
    f.rect(cx - 6 * s, cy - 14 * s, 44 * s, 28 * s, COPPER, INK, 2, 3)
    f.add(f'<ellipse cx="{n(cx - 10 * s)}" cy="{n(cy)}" rx="{n(16 * s)}" ry="{n(62 * s)}" fill="{WHITE}" stroke="{INK}" stroke-width="{n(2.5 * s)}"/>')
    f.add(f'<ellipse cx="{n(cx - 8 * s)}" cy="{n(cy)}" rx="{n(10 * s)}" ry="{n(44 * s)}" fill="{GLASS}"/>')
    f.line(cx - 10 * s, cy, cx - 44 * s, cy, INK, 2.5 * s)


def wind_turbine(f, x, ybase, h, turn=0.0, sc=1.0):
    """A three-bladed wind turbine: tower foot at (x, ybase), hub h above it."""
    f.path(f"M{n(x - 7 * sc)},{n(ybase)} L{n(x - 3 * sc)},{n(ybase - h)} H{n(x + 3 * sc)} L{n(x + 7 * sc)},{n(ybase)} Z", WHITE, INK, 2)
    hy, L = ybase - h, h * 0.62
    for k in range(3):
        a = turn + k * 2 * math.pi / 3; c, s = math.sin(a), -math.cos(a)
        px, py = -s, c
        f.path(f"M{n(x + px * 5 * sc)},{n(hy + py * 5 * sc)} Q{n(x + c * L * 0.3 + px * 12 * sc)},{n(hy + s * L * 0.3 + py * 12 * sc)} {n(x + c * L)},{n(hy + s * L)} "
               f"L{n(x - px * 5 * sc)},{n(hy - py * 5 * sc)} Z", WHITE, INK, 2)
    f.circle(x, hy, 7 * sc, ALUMINIUM, INK, 2)


def pylon(f, x, ybase, h, sc=1.0):
    """A lattice transmission-line pylon; returns the points where its three conductors hang."""
    w = 34 * sc
    f.path(f"M{n(x - w)},{n(ybase)} L{n(x - 6 * sc)},{n(ybase - h)} H{n(x + 6 * sc)} L{n(x + w)},{n(ybase)}", stroke=IRON, w=3 * sc)
    for k in range(1, 5):
        y = ybase - h * k / 5; hw = w - (w - 6 * sc) * k / 5; y2 = ybase - h * (k - 1) / 5; hw2 = w - (w - 6 * sc) * (k - 1) / 5
        f.line(x - hw2, y2, x + hw, y, IRON, 1.5 * sc); f.line(x + hw2, y2, x - hw, y, IRON, 1.5 * sc)
    arms = []
    for yy, half in ((ybase - h * 0.8, 52 * sc), (ybase - h, 34 * sc)):
        f.line(x - half, yy, x + half, yy, IRON, 3 * sc)
        arms += [(x - half, yy + 14 * sc), (x + half, yy + 14 * sc)]
        for xx in (x - half, x + half): f.line(xx, yy, xx, yy + 14 * sc, INK, 2 * sc)
    return arms


def wire(f, a, b, sag=30, colour=INK, w=2):
    mx, my = (a[0] + b[0]) / 2, (a[1] + b[1]) / 2 + sag
    f.path(f"M{n(a[0])},{n(a[1])} Q{n(mx)},{n(my)} {n(b[0])},{n(b[1])}", stroke=colour, w=w)


def house(f, x, ybase, w, h, wall=SAND_LIGHT, roof=HOT, window=GLASS):
    """A small detached house: lower-left corner at (x, ybase)."""
    f.rect(x, ybase - h, w, h, wall, INK, 3)
    f.path(f"M{n(x - 14)},{n(ybase - h)} L{n(x + w / 2)},{n(ybase - h - h * 0.62)} L{n(x + w + 14)},{n(ybase - h)} Z", roof, INK, 3)
    f.rect(x + w * 0.14, ybase - h * 0.72, w * 0.26, h * 0.3, window, INK, 2)
    f.rect(x + w * 0.58, ybase - h * 0.6, w * 0.24, h * 0.6, IRON, INK, 2)


def smoke(f, x, y, sc=1.0, colour=MUTED, opacity=0.55):
    for k, (dx, dy, r) in enumerate(((0, 0, 22), (26, -34, 30), (62, -70, 38), (108, -100, 46))):
        f.add(f'<circle cx="{n(x + dx * sc)}" cy="{n(y + dy * sc)}" r="{n(r * sc)}" fill="{colour}" fill-opacity="{opacity}"/>')
