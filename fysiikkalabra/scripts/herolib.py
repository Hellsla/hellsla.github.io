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
    """A Voyager-style space probe, its dish facing the viewer's left (towards the Earth): a white dish with ribs on a
    ten-sided bus, an RTG boom with its three cylinders, a science boom with cameras and a thin magnetometer boom."""
    s = sc
    f.line(cx + 20 * s, cy - 10 * s, cx + 250 * s, cy - 120 * s, METAL_EDGE, 2 * s)                       # magnetometer boom
    f.line(cx + 30 * s, cy + 10 * s, cx + 150 * s, cy + 110 * s, IRON, 5 * s)                             # RTG boom
    for k in range(3): f.rect(cx + (100 + 22 * k) * s, cy + (62 + 18 * k) * s, 26 * s, 22 * s, IRON, INK, 2 * s, 4 * s)
    f.line(cx + 30 * s, cy - 4 * s, cx + 140 * s, cy - 60 * s, IRON, 5 * s)                               # science boom
    f.rect(cx + 130 * s, cy - 78 * s, 34 * s, 26 * s, ALUMINIUM, INK, 2 * s, 3 * s); f.circle(cx + 140 * s, cy - 82 * s, 7 * s, INK)
    f.path(f"M{n(cx - 4 * s)},{n(cy - 26 * s)} h{n(40 * s)} l{n(12 * s)},{n(13 * s)} v{n(26 * s)} l{n(-12 * s)},{n(13 * s)} h{n(-40 * s)} Z", grad(f, f"probe-bus-{int(cx)}", SAND_DARK, COPPER), INK, 2 * s)
    f.add(f'<ellipse cx="{n(cx - 14 * s)}" cy="{n(cy)}" rx="{n(20 * s)}" ry="{n(74 * s)}" fill="{WHITE}" stroke="{INK}" stroke-width="{n(3 * s)}"/>')
    f.add(f'<ellipse cx="{n(cx - 10 * s)}" cy="{n(cy)}" rx="{n(13 * s)}" ry="{n(56 * s)}" fill="{GLASS}" stroke="{ALUMINIUM}" stroke-width="{n(1.5 * s)}"/>')
    for k in (-1, 1): f.path(f"M{n(cx - 10 * s)},{n(cy)} L{n(cx - 20 * s)},{n(cy + k * 70 * s)}", stroke=ALUMINIUM, w=1.5 * s)
    f.line(cx - 16 * s, cy, cx - 58 * s, cy, INK, 3 * s); f.circle(cx - 60 * s, cy, 5 * s, ALUMINIUM, INK, 1.5 * s)


def planet(f, gid, cx, cy, r, c1, c2, bands=0, rings=False):
    """A shaded planet: a radial gradient from c1 to c2, optional cloud bands and rings."""
    f.defs_add(f'<radialGradient id="{gid}" cx="0.35" cy="0.35" r="0.8"><stop offset="0" stop-color="{c1}"/><stop offset="1" stop-color="{c2}"/></radialGradient>')
    if rings: f.add(f'<ellipse cx="{n(cx)}" cy="{n(cy)}" rx="{n(r * 2.1)}" ry="{n(r * 0.5)}" fill="none" stroke="{SAND_DARK}" stroke-width="{n(r * 0.28)}" transform="rotate(-14 {n(cx)} {n(cy)})"/>')
    f.circle(cx, cy, r, f"url(#{gid})")
    for k in range(bands):
        y = cy - r * 0.6 + k * r * 1.2 / max(1, bands - 1)
        w = math.sqrt(max(0, r * r - (y - cy) ** 2))
        f.path(f"M{n(cx - w * 0.95)},{n(y)} Q{n(cx)},{n(y + r * 0.08)} {n(cx + w * 0.95)},{n(y)}", stroke=GRAIN, w=r * 0.1, extra='stroke-opacity="0.45" stroke-linecap="round"')
    if rings: f.add(f'<path d="M{n(cx - r * 2.1)},{n(cy)} A{n(r * 2.1)},{n(r * 0.5)} 0 0 0 {n(cx + r * 2.1)},{n(cy)}" fill="none" stroke="{SAND_DARK}" stroke-width="{n(r * 0.28)}" transform="rotate(-14 {n(cx)} {n(cy)})"/>')


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


def walker(f, x, yf, coat=COLD, trousers=INK, sc=1.0, lean=0.0, hand=None, winter=False, stride=1.0):
    """A person in side view walking to the right (fy3-6's walker): feet on yf, hips at x. lean tips the upper body
    forward (in figure units at the head); hand=(hx, hy) stretches the front arm to that point; winter adds a cap with a
    bobble, a scarf, mittens and boots."""
    s = sc; hip = (x, yf - 160 * s); sh = (x + 8 * s + lean * 0.6, yf - 300 * s); head = (x + 6 * s + lean, yf - 386 * s)
    boot = IRON if not winter else INK
    def leg(dx):
        f.path(f"M{n(hip[0])},{n(hip[1])} L{n(x + dx * s * stride)},{n(yf - 6 * s)}", stroke=trousers, w=30 * s, extra='stroke-linecap="round"')
        f.path(f"M{n(x + dx * s * stride - (20 if dx < 0 else -16) * s)},{n(yf)} h{n(44 * s)}", stroke=boot, w=(20 if winter else 16) * s, extra='stroke-linecap="round"')
    leg(-50)
    if hand: f.path(f"M{n(sh[0] - 6 * s)},{n(sh[1] + 4 * s)} L{n(hand[0])},{n(hand[1])}", stroke=coat, w=24 * s, extra='stroke-linecap="round"')
    f.path(f"M{n(x - 34 * s + lean * 0.5)},{n(yf - 320 * s)} Q{n(x + 40 * s + lean * 0.6)},{n(yf - 350 * s)} {n(x + 30 * s + lean * 0.4)},{n(yf - 260 * s)} "
           f"L{n(x + 24 * s)},{n(yf - 150 * s)} H{n(x - 36 * s)} Z", coat, INK, 3)
    leg(50)
    if hand:
        f.path(f"M{n(sh[0])},{n(sh[1])} L{n(hand[0])},{n(hand[1])}", stroke=coat, w=24 * s, extra='stroke-linecap="round"')
        f.circle(hand[0], hand[1], 13 * s, HOT if winter else SAND_LIGHT, INK if winter else None, 2)
    else:
        f.path(f"M{n(sh[0])},{n(sh[1])} L{n(sh[0] + 36 * s)},{n(sh[1] + 90 * s)}", stroke=coat, w=24 * s, extra='stroke-linecap="round"')
        f.circle(sh[0] + 38 * s, sh[1] + 98 * s, 12 * s, HOT if winter else SAND_LIGHT)
    f.rect(head[0] - 10 * s, head[1] + 26 * s, 20 * s, 30 * s, SAND_LIGHT)
    if winter: f.path(f"M{n(head[0] - 26 * s)},{n(head[1] + 46 * s)} Q{n(head[0])},{n(head[1] + 62 * s)} {n(head[0] + 26 * s)},{n(head[1] + 46 * s)} L{n(head[0] + 22 * s)},{n(head[1] + 30 * s)} H{n(head[0] - 22 * s)} Z", HOT, INK, 2)
    f.circle(head[0], head[1], 34 * s, SAND_LIGHT)
    if winter:
        f.path(f"M{n(head[0] - 36 * s)},{n(head[1] - 2 * s)} Q{n(head[0] - 34 * s)},{n(head[1] - 52 * s)} {n(head[0])},{n(head[1] - 52 * s)} Q{n(head[0] + 34 * s)},{n(head[1] - 52 * s)} {n(head[0] + 36 * s)},{n(head[1] - 2 * s)} Z", COLD, INK, 3)
        f.rect(head[0] - 38 * s, head[1] - 12 * s, 76 * s, 14 * s, WHITE, INK, 2, 6 * s)
        f.circle(head[0] - 6 * s, head[1] - 58 * s, 12 * s, WHITE, INK, 2)
    else:
        f.path(f"M{n(head[0] - 34 * s)},{n(head[1] + 6 * s)} Q{n(head[0] - 36 * s)},{n(head[1] - 38 * s)} {n(head[0] + 2 * s)},{n(head[1] - 36 * s)} "
               f"Q{n(head[0] + 34 * s)},{n(head[1] - 34 * s)} {n(head[0] + 34 * s)},{n(head[1] - 10 * s)} Q{n(head[0])},{n(head[1] - 18 * s)} {n(head[0] - 34 * s)},{n(head[1] + 6 * s)} Z", INK)
    return head


def bicycle(f, x0, x1, y, r, frame=COLD):
    """A side-view bicycle (fy3-3's): wheels centred at (x0, y) and (x1, y); returns (saddle, bars, crank) points."""
    for cx in (x0, x1):
        f.circle(cx, y, r, "none", INK, max(4, r * 0.15))
        f.circle(cx, y, r * 0.9, "none", METAL_EDGE, 2)
        for k in range(12):
            a = k * math.pi / 6
            f.line(cx, y, cx + r * 0.86 * math.cos(a), y + r * 0.86 * math.sin(a), METAL_EDGE, 1.5)
        f.circle(cx, y, r * 0.09, INK)
    L = x1 - x0; cr = (x0 + L * 0.36, y); top = (x0 + L * 0.79, y - L * 0.42); seat = (x0 + L * 0.29, y - L * 0.42)
    saddle = (seat[0] - L * 0.05, y - L * 0.53); bars = (top[0] - L * 0.03, y - L * 0.53)
    for d in (f"M{n(x0)},{n(y)} L{n(cr[0])},{n(y)} L{n(top[0])},{n(top[1])} L{n(seat[0])},{n(seat[1])} Z", f"M{n(cr[0])},{n(y)} L{n(saddle[0] + L * 0.04)},{n(saddle[1])}",
              f"M{n(top[0])},{n(top[1])} L{n(x1)},{n(y)}", f"M{n(top[0])},{n(top[1])} L{n(bars[0])},{n(bars[1])}"):
        f.path(d, stroke=frame, w=max(4, r * 0.12), extra='stroke-linecap="round" stroke-linejoin="round"')
    f.path(f"M{n(saddle[0] - L * 0.08)},{n(saddle[1])} H{n(saddle[0] + L * 0.07)}", stroke=INK, w=max(5, r * 0.15), extra='stroke-linecap="round"')
    f.path(f"M{n(bars[0] - L * 0.07)},{n(bars[1] + L * 0.01)} Q{n(bars[0])},{n(bars[1] - L * 0.03)} {n(bars[0] + L * 0.09)},{n(bars[1] + L * 0.01)}", stroke=INK, w=max(4, r * 0.1), extra='stroke-linecap="round"')
    f.circle(cr[0], y, r * 0.2, ALUMINIUM, INK, 3)
    return saddle, bars, cr


def rider(f, x0, x1, y, r, frame=COLD, shirt=HOT, helmet=HEAT):
    """A cyclist riding to the right on bicycle(): legs to the pedals, torso leaning to the bars, helmet."""
    saddle, bars, cr = bicycle(f, x0, x1, y, r, frame)
    L = x1 - x0; hip = (saddle[0], saddle[1] - L * 0.04); sh = (hip[0] + L * 0.3, hip[1] - L * 0.3)
    knee = (hip[0] + L * 0.22, hip[1] + L * 0.12)
    f.path(f"M{n(hip[0])},{n(hip[1])} L{n(knee[0])},{n(knee[1])} L{n(cr[0] + L * 0.06)},{n(y + L * 0.06)}", stroke=INK, w=L * 0.075, extra='stroke-linecap="round" stroke-linejoin="round"')
    f.path(f"M{n(cr[0] + L * 0.02)},{n(y + L * 0.08)} h{n(L * 0.08)}", stroke=IRON, w=L * 0.045, extra='stroke-linecap="round"')
    f.path(f"M{n(hip[0] - L * 0.03)},{n(hip[1] + L * 0.02)} L{n(sh[0])},{n(sh[1])}", stroke=shirt, w=L * 0.11, extra='stroke-linecap="round"')
    f.path(f"M{n(sh[0])},{n(sh[1])} L{n(bars[0])},{n(bars[1] - L * 0.01)}", stroke=shirt, w=L * 0.06, extra='stroke-linecap="round"')
    f.circle(bars[0], bars[1] - L * 0.01, L * 0.03, SAND_LIGHT)
    hd = (sh[0] + L * 0.1, sh[1] - L * 0.08)
    f.circle(hd[0], hd[1], L * 0.075, SAND_LIGHT)
    f.path(f"M{n(hd[0] - L * 0.09)},{n(hd[1] - L * 0.005)} Q{n(hd[0] - L * 0.06)},{n(hd[1] - L * 0.11)} {n(hd[0] + L * 0.04)},{n(hd[1] - L * 0.095)} "
           f"Q{n(hd[0] + L * 0.1)},{n(hd[1] - L * 0.07)} {n(hd[0] + L * 0.085)},{n(hd[1] - L * 0.02)} Z", helmet, INK, 3)


def red_house(f, x, ybase, w, h, snow=False):
    """A Finnish red wooden house: board lines, white corners and window frames, a dark roof (snow on it if snow)."""
    f.rect(x, ybase - h, w, h, HOT, INK, 3)
    for k in range(1, int(w / 14)): f.line(x + k * 14, ybase - h + 3, x + k * 14, ybase - 3, HOT_LIGHT, 1)
    f.rect(x, ybase - h, 10, h, WHITE, INK, 2); f.rect(x + w - 10, ybase - h, 10, h, WHITE, INK, 2)
    f.path(f"M{n(x - 20)},{n(ybase - h)} L{n(x + w / 2)},{n(ybase - h - h * 0.55)} L{n(x + w + 20)},{n(ybase - h)} Z", IRON if not snow else WHITE, INK, 3)
    if snow: f.path(f"M{n(x - 20)},{n(ybase - h)} L{n(x + w / 2)},{n(ybase - h - h * 0.55)} L{n(x + w + 20)},{n(ybase - h)} l-8,8 L{n(x + w / 2)},{n(ybase - h - h * 0.44)} L{n(x - 12)},{n(ybase - h + 8)} Z", ICE)
    for k in range(int((w - 40) / 70)):
        wx = x + 30 + k * 70
        f.rect(wx, ybase - h * 0.72, 40, h * 0.4, GLASS, WHITE, 5); f.rect(wx, ybase - h * 0.72, 40, h * 0.4, "none", INK, 2)
        f.line(wx + 20, ybase - h * 0.72, wx + 20, ybase - h * 0.32, WHITE, 3)


def birch(f, x, ybase, h, leaves=True):
    """A birch: a white trunk with black marks, thin branches, a light crown in summer."""
    f.rect(x - h * 0.03, ybase - h, h * 0.06, h, WHITE, INK, 2)
    for k in range(7): f.rect(x - h * 0.03 + (h * 0.03 if k % 2 else 0), ybase - h * (0.12 + 0.12 * k), h * 0.03, h * 0.015, INK)
    for sgn, y0 in ((-1, 0.62), (1, 0.75), (-1, 0.85)):
        f.line(x, ybase - h * y0, x + sgn * h * 0.18, ybase - h * (y0 + 0.12), INK, 2, cap="round")
    if leaves:
        for k, (dx, dy, r) in enumerate(((0, 0.95, 0.2), (-0.15, 0.8, 0.16), (0.15, 0.82, 0.17), (0, 0.72, 0.15))):
            f.add(f'<circle cx="{n(x + dx * h)}" cy="{n(ybase - dy * h)}" r="{n(r * h)}" fill="{GOOD}" fill-opacity="0.85"/>')


def hills(f, pre, y, colours, amp=40, seed=1):
    """Layered rolling hills from the back: one band per colour, each lower than the one behind it."""
    for k, c in enumerate(colours):
        y0 = y + k * amp * 0.9; d = f"M0,{n(y0)}"
        for i in range(7):
            x = (i + 1) * 200; d += f" Q{n(x - 100)},{n(y0 - amp * (0.4 + rnd(i + 10 * k, seed)))} {x},{n(y0 + amp * 0.2 * (rnd(i, seed + k) - 0.5))}"
        f.path(d + " V600 H0 Z", c)


def spruce(f, x, ybase, h, colour=GOOD):
    """One spruce with a trunk: three stacked tiers, the right half of each in shade."""
    f.rect(x - h * 0.04, ybase - h * 0.12, h * 0.08, h * 0.12, COPPER)
    for w, top in ((0.36, 0.5), (0.28, 0.72), (0.2, 1.0)):
        yb = ybase - h * (0.1 + 0.22 * ((0.36 - w) / 0.08))
        f.path(f"M{n(x - h * w)},{n(yb)} L{n(x)},{n(ybase - h * top)} L{n(x + h * w)},{n(yb)} Z", colour, INK, 2)
        f.add(f'<path d="M{n(x)},{n(ybase - h * top)} L{n(x + h * w)},{n(yb)} H{n(x)} Z" fill="{INK}" fill-opacity="0.18"/>')


def steel(f, gid, vertical=False):
    """fy3-7's brushed-steel gradient (dark edge, bright band, mid tone, dark edge) across a shape."""
    x2, y2 = ("0", "1") if vertical else ("1", "0")
    f.defs_add(f'<linearGradient id="{gid}" x1="0" y1="0" x2="{x2}" y2="{y2}"><stop offset="0" stop-color="{METAL_EDGE}"/>'
               f'<stop offset="0.3" stop-color="{WHITE}"/><stop offset="0.65" stop-color="{ALUMINIUM}"/><stop offset="1" stop-color="{METAL_EDGE}"/></linearGradient>')
    return f"url(#{gid})"


def glow(f, gid, inner=HEAT_LIGHT, outer=HEAT):
    """A radial glow that fades out at its edge (a sun, a hot plate, a lamp)."""
    f.defs_add(f'<radialGradient id="{gid}" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="{inner}"/><stop offset="0.55" stop-color="{outer}" stop-opacity="0.8"/>'
               f'<stop offset="1" stop-color="{outer}" stop-opacity="0"/></radialGradient>')
    return f"url(#{gid})"


def tiles(f, y1, step=75, colour=RULE_LIGHT, bg=WHITE):
    f.rect(0, 0, 1200, y1, bg)
    for x in range(0, 1201, step): f.line(x, 0, x, y1, colour, 2)
    for y in range(0, y1 + 1, step): f.line(0, y, 1200, y, colour, 2)


def window(f, x, y, w, h, gid, snow=False):
    f.rect(x, y, w, h, grad(f, gid, ICE, COLD_LIGHT), INK, 3, 4)
    if snow: f.path(f"M{x},{y + h * 0.86} Q{x + w * 0.3},{y + h * 0.74} {x + w * 0.56},{y + h * 0.82} T{x + w},{y + h * 0.78} V{y + h} H{x} Z", WHITE)
    else: cloud(f, x + w * 0.4, y + h * 0.42, w / 500)
    f.line(x + w / 2, y, x + w / 2, y + h, INK, 3); f.line(x, y + h / 2, x + w, y + h / 2, INK, 3)
    f.rect(x - 12, y + h, w + 24, 14, RULE, INK, 3, 3)


def wood(f, x, y, w, h, gid, rx=4, horizontal=True):
    """A wooden board with a grain gradient and a few grain lines."""
    f.rect(x, y, w, h, grad(f, gid, SAND_DARK, SAND, horizontal=not horizontal), INK, 3, rx)
    for k in range(1, 4):
        if horizontal: f.path(f"M{n(x + 10)},{n(y + h * k / 4)} q{n(w * 0.25)},{n(-h * 0.06)} {n(w * 0.5)},0 t{n(w * 0.5 - 20)},0", stroke=GRAIN, w=1.5, extra='stroke-opacity="0.6"')
