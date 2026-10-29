"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy4-1` writes them into lesson.md."""
from figlib import (Fig, Axes, INK, MUTED, RULE_LIGHT, WHITE, COLD, HEAT, SAND_LIGHT, COPPER, ALUMINIUM, HEAT_LIGHT, fi)
import math
from figlib import GOOD, GOOD_LIGHT, HOT, IRON, SAND, SAND_DARK, WATER, WATER_LIGHT
import herolib as H


def hero():
    """The chapter's opening illustration: a cyclist rides once round a lake and comes back to the start flag: a long path, no change of place."""
    f = H.hero("fy41-hero", "Kuvitus: ylhäältä vinosti nähty järvi, jonka ympäri kiertää polku. Lähtöpaikalla on lippu, ja polulla ajaa "
               "pyöräilijä, joka on kiertämässä järven ympäri takaisin lähtöpaikkaan. Nuolet näyttävät kiertosuunnan.")
    f.rect(0, 0, 1200, 600, GOOD_LIGHT)
    for k in range(34):
        x, y = 60 + H.rnd(k, 2) * 1080, 120 + H.rnd(k, 6) * 450
        if (x - 600) ** 2 / 480 ** 2 + (y - 340) ** 2 / 230 ** 2 > 1: f.circle(x, y, 14 + 10 * H.rnd(k, 8), GOOD, INK, 2)
    f.add(f'<ellipse cx="600" cy="340" rx="430" ry="200" fill="none" stroke="{SAND}" stroke-width="40"/>')
    f.add(f'<ellipse cx="600" cy="340" rx="430" ry="200" fill="none" stroke="{SAND_DARK}" stroke-width="2" stroke-dasharray="2 10"/>')
    f.add(f'<ellipse cx="600" cy="340" rx="370" ry="156" fill="{WATER_LIGHT}" stroke="{WATER}" stroke-width="3"/>')
    for k in range(5): f.path(f"M{430 + k * 70},{300 + 18 * (k % 2)} q16,-8 32,0", stroke=WHITE, w=3)
    for t in (1.0, 2.3, 3.6, 4.9, 5.9):
        x, y = 600 + 430 * math.cos(t), 340 + 200 * math.sin(t)
        dx, dy = -math.sin(t) * 430, math.cos(t) * 200; L = math.hypot(dx, dy)
        f.arrow(x - dx / L * 34, y - dy / L * 34, x + dx / L * 34, y + dy / L * 34, INK, 4, 16)
    # start flag at the bottom
    fx, fy = 600, 540
    f.line(fx, fy, fx, fy - 90, INK, 4); f.path(f"M{fx},{fy - 90} l50,14 l-50,14 Z", HOT, INK, 2)
    f.add(f'<ellipse cx="{fx}" cy="{fy}" rx="16" ry="6" fill="{IRON}"/>')
    # cyclist on the path, seen from the side, on the right
    x, y = 980, 452
    for wx in (x - 36, x + 36): f.circle(wx, y, 22, "none", INK, 4)
    f.path(f"M{x - 36},{y} L{x - 8},{y} L{x + 18},{y - 36} L{x - 18},{y - 36} Z M{x - 8},{y} L{x - 22},{y - 46} M{x + 36},{y} L{x + 22},{y - 50}", stroke=HOT, w=4, extra='stroke-linejoin="round"')
    f.path(f"M{x - 22},{y - 50} L{x - 2},{y - 100}", stroke=COLD, w=18, extra='stroke-linecap="round"')
    f.path(f"M{x - 4},{y - 92} L{x + 24},{y - 54}", stroke=COLD, w=8, extra='stroke-linecap="round"')
    f.path(f"M{x - 22},{y - 50} L{x - 4},{y - 24} L{x - 8},{y}", stroke=INK, w=8, extra='stroke-linecap="round" stroke-linejoin="round"')
    f.circle(x + 6, y - 116, 13, SAND_LIGHT)
    f.path(f"M{x - 8},{y - 120} Q{x + 4},{y - 136} {x + 20},{y - 120} Z", HOT, INK, 2)
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
