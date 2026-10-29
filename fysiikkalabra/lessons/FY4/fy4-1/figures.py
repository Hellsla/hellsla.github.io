"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy4-1` writes them into lesson.md."""
from figlib import (Fig, Axes, INK, MUTED, RULE_LIGHT, WHITE, COLD, HEAT, SAND_LIGHT, COPPER, ALUMINIUM, HEAT_LIGHT, fi)
import math
from figlib import GOOD, GOOD_LIGHT, HOT, IRON, SAND, SAND_DARK, WATER, WATER_LIGHT
import herolib as H
from figlib import GRAIN, METAL_EDGE, n
from herolib import grad, rnd


def hero():
    """The chapter's opening illustration: a cyclist rides once round a lake and comes back to the start flag: a long path, no change of place."""
    f = H.hero("fy41-hero", "Kuvitus: järvi metsän keskellä vinosti ylhäältä nähtynä, ja sen ympäri kiertää hiekkapolku. Polun lähtöpaikalla "
               "on lippu ja lähtöviiva. Etualalla pyöräilijä ajaa polkua kohti lähtöpaikkaa: hän on kiertänyt järven ympäri. "
               "Nuolet polulla näyttävät kiertosuunnan.")
    H.sky(f, "fy41h", 200)
    H.cloud(f, 220, 70, 0.7); H.cloud(f, 980, 50, 0.55)
    H.hills(f, "fy41h", 150, [ALUMINIUM, METAL_EDGE], amp=40, seed=3)
    H.forest(f, 196, 34, 22, IRON, seed=5, depth=20)
    H.forest(f, 216, 40, 26, GOOD, seed=8, depth=12)
    f.rect(0, 226, 1200, 374, grad(f, "fy41h-grass", GOOD_LIGHT, SAND_LIGHT, y1=226, y2=600))
    cx, cy = 600, 360
    # gravel path round the lake, its edges and texture
    f.add(f'<ellipse cx="{cx}" cy="{cy}" rx="500" ry="168" fill="{SAND}" stroke="{GRAIN}" stroke-width="3"/>')
    f.add(f'<ellipse cx="{cx}" cy="{cy}" rx="452" ry="132" fill="{GOOD_LIGHT}" stroke="{GRAIN}" stroke-width="3"/>')
    for k in range(90):
        t = k / 90 * 2 * math.pi; rr = 476 + 16 * (rnd(k, 3) - 0.5)
        f.circle(cx + rr * math.cos(t), cy + rr * 150 / 476 * math.sin(t), 2 + 1.5 * rnd(k, 7), GRAIN)
    # lake with shore sand, reeds and ripples
    f.add(f'<ellipse cx="{cx}" cy="{cy - 6}" rx="420" ry="112" fill="{SAND_LIGHT}"/>')
    f.add(f'<ellipse cx="{cx}" cy="{cy - 8}" rx="400" ry="100" fill="{grad(f, "fy41h-lake", WATER_LIGHT, WATER)}" stroke="{WATER}" stroke-width="3"/>')
    for x, y, w in ((360, 320, 110), (560, 300, 140), (760, 340, 120), (480, 380, 90), (690, 395, 100)):
        f.path(f"M{x},{y} q{w / 4},-6 {w / 2},0 t{w / 2},0", stroke=WHITE, w=3, extra='stroke-linecap="round" stroke-opacity="0.75"')
    for k in range(9):
        x = 250 + k * 14 if k < 5 else 880 + (k - 5) * 14; y = 352 + 18 * (k % 3)
        f.line(x, y, x - 4, y - 34, GOOD, 3, cap="round"); f.add(f'<ellipse cx="{n(x - 4)}" cy="{n(y - 34)}" rx="4" ry="10" fill="{COPPER}"/>')
    # spruces around, larger nearer
    for k, (x, yb, h) in enumerate(((60, 300, 110), (130, 330, 130), (1080, 300, 110), (1150, 340, 140), (40, 470, 170), (1130, 500, 180),
                                    (200, 270, 80), (980, 262, 80), (330, 230, 60), (860, 232, 64))):
        H.spruce(f, x, yb, h)
    # direction arrows along the path (clockwise on the page)
    for t in (1.25, 2.6, 3.7, 4.6, 5.5):
        x, y = cx + 476 * math.cos(t), cy + 150 * math.sin(t)
        dx, dy = -math.sin(t) * 476, math.cos(t) * 150; L = math.hypot(dx, dy)
        f.arrow(x - dx / L * 30, y - dy / L * 30, x + dx / L * 30, y + dy / L * 30, INK, 4, 16)
    # start line and flag at the front of the path
    sx, sy = 600, cy + 150
    f.path(f"M{sx - 6},{sy - 22} L{sx + 6},{sy + 22}", stroke=WHITE, w=10)
    f.line(sx + 20, sy + 30, sx + 20, sy - 90, INK, 5)
    f.path(f"M{sx + 20},{sy - 90} Q{sx + 60},{sy - 104} {sx + 96},{sy - 82} Q{sx + 60},{sy - 64} {sx + 20},{sy - 60} Z", HOT, INK, 3)
    f.add(f'<ellipse cx="{sx + 20}" cy="{sy + 30}" rx="18" ry="6" fill="{GRAIN}"/>')
    # the cyclist on the near path, riding towards the start (to the left: mirrored)
    f.add('<g transform="translate(1760,0) scale(-1,1)">')
    H.rider(f, 780, 920, 492, 40, COLD, HEAT, HOT)
    f.add("</g>")
    return f.svg()


def _numberline(f, y, x0, step, label):
    """An x axis in metres drawn to scale: 0-10 m, ticks and numbers every 2 m. Returns the X(m) function."""
    X = lambda m: x0 + m * step
    f.arrow(X(0) - 20, y, X(10) + 24, y, INK, 2.5, 13)
    for m in range(0, 11, 2):
        f.line(X(m), y - 4, X(m), y + 6, INK, 2)
        f.tex(X(m), y + 26, fi(m), "middle")
    f.tex(X(10) + 32, y, label, "start")
    return X


def displacement():
    f = Fig("fy41-disp", 392, "Kaavakuva kahdesta siirtymästä x-akselilla, akseli piirretty mittakaavassa. Ylhäällä kappale "
            "siirtyy paikasta x1 = 2 m paikkaan x2 = 8 m, joten siirtymä on +6 m ja osoittaa oikealle. Alhaalla kappale "
            "siirtyy paikasta x1 = 8 m paikkaan x2 = 3 m, joten siirtymä on −5 m ja osoittaa vasemmalle.")
    lab = r"x\ (\text{m})"
    # upper panel
    X = _numberline(f, 104, 70, 40, lab)
    f.tex(X(5), 26, r"\Delta x = +6\,\text{m}", "middle", COLD)
    f.arrow(X(2), 62, X(8), 62, COLD, 5, 20)
    f.circle(X(2), 104, 9, COLD, WHITE, 2); f.circle(X(8), 104, 9, COLD, WHITE, 2)
    f.tex(X(2), 162, "x_1", "middle"); f.tex(X(8), 162, "x_2", "middle")
    f.line(24, 198, 576, 198, MUTED, 1.5, "8 6")
    # lower panel
    X = _numberline(f, 304, 70, 40, lab)
    f.tex(X(5.5), 226, r"\Delta x = -5\,\text{m}", "middle", HEAT)
    f.arrow(X(8), 262, X(3), 262, HEAT, 5, 20)
    f.circle(X(8), 304, 9, HEAT, WHITE, 2); f.circle(X(3), 304, 9, HEAT, WHITE, 2)
    f.tex(X(8), 362, "x_1", "middle"); f.tex(X(3), 362, "x_2", "middle")
    return f.svg()


def round_trip():
    f = Fig("fy41-trip", 322, "Kaavakuva, ei mittakaavassa: pyöräilijä ajaa kotoa kauppaan, kaksi kilometriä, ja takaisin kotiin, "
            "toiset kaksi kilometriä. Kuljettu matka on s = 2 km + 2 km = 4 km, mutta loppupaikka on sama kuin alkupaikka, "
            "joten siirtymä on nolla.")
    x0, step, y = 110, 150, 120
    X = lambda km: x0 + km * step
    f.arrow(X(0) - 60, y, X(2) + 70, y, INK, 2.5, 13)
    for km in (0, 1, 2):
        f.line(X(km), y - 4, X(km), y + 6, INK, 2)
        f.tex(X(km), y + 26, fi(km), "middle")
    f.tex(X(2) + 78, y, r"x\ (\text{km})", "start")
    # home and shop
    f.rect(X(0) - 20, y - 24, 40, 24, SAND_LIGHT, INK, 2.5)
    f.path(f"M{X(0) - 26},{y - 24} L{X(0)},{y - 44} L{X(0) + 26},{y - 24} Z", COPPER, INK, 2.5)
    f.rect(X(2) - 24, y - 30, 48, 30, ALUMINIUM, INK, 2.5)
    f.rect(X(2) - 28, y - 30, 56, 10, HEAT_LIGHT, INK, 2.5)
    # the trip
    f.arrow(X(0), 64, X(2), 64, COLD, 5, 20)
    f.tex(X(1), 30, r"\text{menomatka } 2\,\text{km}", "middle", COLD)
    f.arrow(X(2), 184, X(0), 184, HEAT, 5, 20)
    f.tex(X(1), 214, r"\text{paluumatka } 2\,\text{km}", "middle", HEAT)
    f.line(24, 238, 576, 238, MUTED, 1.5, "8 6")
    f.tex(300, 266, r"s = 2\,\text{km} + 2\,\text{km} = 4\,\text{km}", "middle")
    f.tex(300, 300, r"\Delta x = x_2 - x_1 = 0", "middle")
    return f.svg()


def graph_slope():
    f = Fig("fy41-slope", 330, "Kaavakuva kahdesta (t,x)-kuvaajasta, ei lukuarvoja. Vasemmalla suora nousee alkupaikasta x0, ja "
            "suoralta on valittu kaksi pistettä: aikaväli Δt ja paikan muutos Δx muodostavat kolmion, jonka avulla "
            "nopeus v on Δx jaettuna Δt:lla. Oikealla kolme suoraa samasta alkupaikasta: nouseva suora on nopeus v "
            "suurempi kuin nolla, vaakasuora suora nopeus nolla ja laskeva suora nopeus pienempi kuin nolla.")
    kw = dict(x=(0, 10), y=(0, 10), xticks=[], yticks=[], grid=False, origin_label=False)
    a = Axes(f, (50, 290), (250, 70), xlabel="t", ylabel="x", **kw)
    a.line([(0, 2), (10, 8)], COLD, 4)
    p1, p2 = (3, 3.8), (8, 6.8)
    a.line([p1, (p2[0], p1[1]), p2], MUTED, 2, "8 6")
    a.point(0, 2, COLD); a.point(*p1, COLD); a.point(*p2, COLD)
    f.tex(a.X(5.5), a.Y(p1[1]) + 24, r"\Delta t", "middle")
    f.tex(a.X(p2[0]) + 12, a.Y(5.3), r"\Delta x", "start")
    f.tex(a.x0 - 10, a.Y(2), "x_0", "end")
    f.tex(a.X(0.6), a.Y(8.4), r"v = \dfrac{\Delta x}{\Delta t}", "start")
    b = Axes(f, (340, 290), (490, 70), xlabel="t", ylabel="x", **kw)
    for end, col, tx in ((8, COLD, "v > 0"), (5, MUTED, "v = 0"), (2, HEAT, "v < 0")):
        b.line([(0, 5), (10, end)], col, 4)
        f.tex(b.X(10) + 10, b.Y(end), tx, "start", col)
    b.point(0, 5, INK)
    f.tex(b.x0 - 10, b.Y(5), "x_0", "end")
    return f.svg()


def jogger_graph():
    f = Fig("fy41-jogger", 340, "(t,x)-kuvaaja mittakaavassa: suora nousee paikasta 20 metriä hetkellä 0 paikkaan 120 metriä "
            "hetkellä 40 sekuntia ja jatkuu katkoviivana paikkaan 170 metriä hetkellä 60 sekuntia.")
    ax = Axes(f, (92, 296), (470, 62), x=(0, 70), y=(0, 200), xticks=[20, 40, 60], yticks=[20, 120, 170],
              xlabel=r"t\ (\text{s})", ylabel=r"x\ (\text{m})")
    ax.line([(0, 20), (40, 120)], COLD, 3.5)
    ax.line([(40, 120), (60, 170)], COLD, 3.5, "10 8")
    ax.guide(40, 120); ax.guide(60, 170)
    ax.point(0, 20, COLD); ax.point(40, 120, COLD)
    f.circle(ax.X(60), ax.Y(170), 7, WHITE, COLD, 3)
    return f.svg()


FIGURES = {"hero": hero, "displacement": displacement, "round-trip": round_trip, "graph-slope": graph_slope, "jogger-graph": jogger_graph}
