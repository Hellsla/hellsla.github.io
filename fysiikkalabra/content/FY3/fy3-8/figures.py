"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy3-8` writes them into lesson.md."""
import math
from figlib import (Fig, INK, MUTED, WHITE, RULE, COLD, COLD_LIGHT, HOT, HOT_LIGHT, HEAT, GLASS, METAL_EDGE)
import herolib as H


def particles():
    f = Fig("fy38-particles", 316, "Sama hiukkasrivi kylmänä ja lämpimänä. Lämpimänä hiukkaset värähtelevät voimakkaammin "
            "ja niiden keskimääräinen etäisyys d on suurempi kuin kylmän rivin etäisyys d₀, mutta hiukkaset ovat yhtä "
            "suuria. Etäisyyden muutos on piirretty liioiteltuna.")
    for y0, gap, amp, fill, col, name in ((100, 70, 6, COLD_LIGHT, COLD, r"\text{kylmä}"),
                                          (222, 90, 18, HOT_LIGHT, HOT, r"\text{lämmin}")):
        f.tex(20, y0, name, "start")
        bx = 180
        by = y0 - 28
        f.line(bx, by, bx + gap, by, INK, 2)
        f.line(bx, by - 8, bx, by + 8, INK, 2)
        f.line(bx + gap, by - 8, bx + gap, by + 8, INK, 2)
        f.tex(bx + gap / 2, by - 24, r"d_0" if gap == 70 else r"d > d_0", "middle")
        for i in range(4):
            cx = bx + gap * i
            f.circle(cx, y0, 16, fill, INK, 2)
            f.arrow(cx, y0 + 32, cx - amp - 8, y0 + 32, col, 2, 11)
            f.arrow(cx, y0 + 32, cx + amp + 8, y0 + 32, col, 2, 11)
    f.tex(588, 296, r"\text{hiukkaset yhtä suuria, välit liioiteltu}", "end", MUTED)
    return f.svg()


def rod_expansion():
    f = Fig("fy38-rod", 300, "Sama sauva kylmänä ja lämpimänä: lämmin sauva on pidempi, ja pituuden muutos ΔL on merkitty "
            "sauvan päähän. Sauva on kiinni seinässä vasemmassa päässä. Laajeneminen on piirretty liioiteltuna.")
    f.defs_add('<pattern id="fy38-hatch" width="10" height="10" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">'
               f'<line x1="0" y1="0" x2="0" y2="10" stroke="{MUTED}" stroke-width="1.5"/></pattern>')
    f.defs_add(f'<linearGradient id="fy38-cold" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{WHITE}"/><stop offset="1" stop-color="{COLD_LIGHT}"/></linearGradient>')
    f.defs_add(f'<linearGradient id="fy38-warm" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{WHITE}"/><stop offset="1" stop-color="{HOT_LIGHT}"/></linearGradient>')
    f.rect(36, 56, 14, 164, "url(#fy38-hatch)")
    f.line(50, 56, 50, 220, INK, 3)
    f.tex(66, 38, r"\text{kylmä, lämpötila } T_0", "start", COLD)
    f.rect(50, 60, 400, 40, "url(#fy38-cold)", INK, 2)
    f.tex(250, 80, r"L_0", "middle")
    f.tex(66, 126, r"\text{lämmin, lämpötila } T_0 + \Delta T", "start", HOT)
    f.rect(50, 148, 470, 40, "url(#fy38-warm)", INK, 2)
    f.tex(285, 168, r"L_0 + \Delta L", "middle")
    f.line(450, 54, 450, 218, MUTED, 1.5, "6 5")
    f.arrow(485, 206, 450, 206, INK, 2, 12)
    f.arrow(485, 206, 520, 206, INK, 2, 12)
    f.tex(485, 236, r"\Delta L", "middle")
    f.tex(588, 286, r"\text{laajeneminen liioiteltu}", "end", MUTED)
    return f.svg()


def bracket(f, x, y1, y2, side, color, w):
    """A vertical bracket at x from y1 to y2, its ends pointing towards the thing (side -1: left of it, +1: right)."""
    f.line(x, y1, x, y2, color, w)
    f.line(x, y1, x - side * 8, y1, color, w)
    f.line(x, y2, x - side * 8, y2, color, w)


def volume_expansion():
    f = Fig("fy38-volume", 350, "Nesteen tilavuuden lämpölaajeneminen. Sama nestemäärä kolvissa, jonka kaulana on ohut putki: "
            "kylmänä nesteen tilavuus on V₀ ja pinta on alempana, lämpimänä neste on laajentunut ja pinta nousee ohuessa "
            "putkessa. Tilavuuden muutos ΔV on merkitty putkeen. Laajeneminen on piirretty liioiteltuna.")
    f.defs_add(f'<linearGradient id="fy38-liq-c" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#a9d1f0"/><stop offset="1" stop-color="#2f74b5"/></linearGradient>')
    f.defs_add(f'<linearGradient id="fy38-liq-w" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f2a69c"/><stop offset="1" stop-color="#c92a2a"/></linearGradient>')
    R, hw, cy, top = 50, 10, 282, 64
    dy = math.sqrt(R * R - hw * hw)
    lvl = {"c": 190, "w": 130}

    def vessel(cx, level, grad, tag):
        join = cy - dy
        outline = f"M{cx - hw},{top} V{join:.1f} A{R},{R} 0 1 0 {cx + hw},{join:.1f} V{top}"
        f.path(outline + " Z", GLASS)
        f.path(f"M{cx - hw},{level} V{join:.1f} A{R},{R} 0 1 0 {cx + hw},{join:.1f} V{level} Z", f"url(#{grad})")
        f.line(cx - hw, level, cx + hw, level, INK, 1.5)
        f.path(outline, stroke=INK, w=2.5)
        for y in range(top + 20, 170, 20):                       # scale ticks on the tube
            f.line(cx + hw, y, cx + hw + 7, y, MUTED, 1.5)

    cc, cw = 150, 430
    vessel(cc, lvl["c"], "fy38-liq-c", "c")
    vessel(cw, lvl["w"], "fy38-liq-w", "w")
    f.tex(cc, 26, r"\text{kylmä, } T_0", "middle", COLD)
    f.tex(cw, 26, r"T_0 + \Delta T", "middle", HOT)
    # V0: the liquid below the cold level, bracket on the left of the cold vessel
    bx = cc - R - 18
    bracket(f, bx, lvl["c"], cy + R - 6, -1, INK, 2)
    f.tex(bx - 10, (lvl['c'] + cy + R - 6) / 2, r"V_0", "end")
    f.tex(cc + 40, lvl["c"], r"\text{pinta}", "start", MUTED)
    # the same V0 bracket on the warm vessel, and the cold level as a dashed rule
    bx2 = cw - R - 18
    bracket(f, bx2, lvl["c"], cy + R - 6, -1, INK, 2)
    f.tex(bx2 - 10, (lvl['c'] + cy + R - 6) / 2, r"V_0", "end")
    f.line(cw - 42, lvl["c"], cw + 60, lvl["c"], MUTED, 1.5, "6 5")
    # DeltaV: the rise in the tube
    ex = cw + hw + 22
    bracket(f, ex, lvl["w"], lvl["c"], 1, HOT, 2.5)
    f.tex(ex + 12, (lvl['w'] + lvl['c']) / 2, r"\Delta V", "start", HOT)
    return f.svg()


def hero():
    """The chapter's opening illustration: a car driving over a bridge's comb-shaped expansion joint."""
    f = H.hero("fy38-hero", "Kuvitus: auto ajaa pitkää siltaa pitkin poispäin katsojasta. Etualalla tien poikki kulkee "
               "kampamainen teräsliitos, jonka hampaat lomittuvat ja jättävät väliinsä raon sillan lämpölaajenemista varten.")
    H.sky(f, "fy38h", 300)
    H.cloud(f, 260, 90, 0.8); H.cloud(f, 980, 120, 0.6)
    H.forest(f, 300, 34, 22, H.METAL_EDGE, seed=6, depth=20)
    f.rect(0, 300, 1200, 300, H.grad(f, "fy38h-river", H.WATER_LIGHT, H.WATER))
    # the road narrows to the horizon
    f.path("M560,300 H640 L1000,600 H200 Z", H.IRON)
    f.path("M598,300 H602 L612,600 H588 Z", H.WHITE)
    for side in (-1, 1):
        f.path(f"M{600 + side * 40},300 L{600 + side * 400},600", stroke=H.ALUMINIUM, w=10)
        for k in range(1, 12):
            t = (k / 12) ** 1.6; x = 600 + side * (40 + 360 * t); y = 300 + 300 * t
            f.line(x, y, x, y - 14 - 50 * t, H.ALUMINIUM, 2 + 3 * t)
        f.path(f"M{600 + side * 40},288 L{600 + side * 400},540", stroke=H.ALUMINIUM, w=6)
    # comb joint across the road: two steel plates with interlocking teeth
    y0, y1 = 500, 540
    f.path(f"M{264},{y0} H{936} L{960},{y1} H{240} Z", H.METAL_EDGE)
    for k in range(24):
        x = 270 + k * 28
        f.path(f"M{x},{y0} h12 l2,{y1 - y0 - 10} h-16 Z", H.ALUMINIUM, H.INK, 1.5)
        f.path(f"M{x + 14},{y1} h12 l-2,{-(y1 - y0 - 10)} h-8 Z", H.IRON, H.INK, 1.5)
    f.line(240, y1, 960, y1, H.INK, 3); f.line(264, y0, 936, y0, H.INK, 3)
    # the car, from behind
    f.rect(536, 360, 128, 70, H.COLD, H.INK, 3, 14)
    f.path("M552,360 L566,322 H634 L648,360 Z", H.GLASS, H.INK, 3)
    f.rect(546, 400, 26, 12, H.HOT, rx=3); f.rect(628, 400, 26, 12, H.HOT, rx=3)
    f.rect(544, 428, 26, 22, H.INK, rx=4); f.rect(630, 428, 26, 22, H.INK, rx=4)
    return f.svg()


FIGURES = {"hero": hero, "particles": particles, "rod-expansion": rod_expansion, "volume-expansion": volume_expansion}
