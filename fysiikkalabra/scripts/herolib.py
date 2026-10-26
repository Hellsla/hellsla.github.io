"""Shared pieces of the chapters' opening illustrations (NOTES.md §3 "Opening illustration"): flat shapes in the
figure palette, no text. A lesson's figures.py draws its scene with these on a Fig(..., width=1200, hero=True)."""
import math
from figlib import (Fig, INK, MUTED, RULE, RULE_LIGHT, WHITE, GLASS, WATER_LIGHT, WATER, SAND_LIGHT, SAND, SAND_DARK, GRAIN,
                    HEAT_LIGHT, HEAT, HOT, HOT_LIGHT, COLD, COLD_LIGHT, ALUMINIUM, METAL_EDGE, IRON, COPPER, ICE, ICE_EDGE,
                    GOOD, GOOD_LIGHT, PAPER, n)


def hero(fid, label): return Fig(fid, 600, label, width=1200, hero=True)


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
