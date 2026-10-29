"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy1-8` writes them into lesson.md."""
from figlib import Fig, Axes, INK, MUTED, WHITE, RULE, SAND, SAND_DARK, SAND_LIGHT, ALUMINIUM, METAL_EDGE, COLD, GOOD, GOOD_LIGHT, HEAT, fi
from figlib import GLASS, HEAT_LIGHT, HOT, PAPER
import herolib as H
from figlib import GRAIN, HOT_LIGHT
from herolib import grad


def hero():
    """The chapter's opening illustration: one toy car on a track, two groups timing it with their own tape and stopwatch."""
    f = H.hero("fy18-hero", "Kuvitus: luokan lattialla rata, jolla leluauto kulkee mittanauhan vieressä. Radan molemmin puolin on ryhmä: "
               "kummallakin on oma sekuntikello, ja kellojen viisarit ovat pysähtyneet eri kohtiin.")
    f.rect(0, 0, 1200, 600, PAPER)
    H.window(f, 120, 40, 200, 170, "fy18h-w1"); H.window(f, 880, 40, 200, 170, "fy18h-w2")
    f.rect(0, 300, 1200, 300, grad(f, "fy18h-floor", SAND, SAND_DARK, y1=300, y2=600))
    for k in range(13): f.line(600 + (k - 6) * 60, 300, 600 + (k - 6) * 240, 600, GRAIN, 1.5)
    f.line(0, 300, 1200, 300, INK, 3)
    # track board in perspective with the tape along its front
    f.path("M180,500 L1020,500 L940,400 L260,400 Z", grad(f, "fy18h-track", ALUMINIUM, METAL_EDGE), INK, 3)
    f.path("M260,400 H940", stroke=WHITE, w=2)
    for x in (300, 900): f.line(x, 400, x - 24, 500, HOT, 4, dash="10 8")         # start and finish marks
    f.rect(170, 504, 860, 30, HEAT_LIGHT, INK, 2.5, 4)
    for k in range(87): f.line(178 + k * 9.8, 504, 178 + k * 9.8, 504 + (18 if k % 10 == 0 else 12 if k % 5 == 0 else 7), INK, 1.5)
    # toy car with its motion lines
    x, y = 610, 466
    f.path(f"M{x - 80},{y + 8} V{y - 22} Q{x - 72},{y - 32} {x - 44},{y - 34} L{x - 24},{y - 66} H{x + 34} L{x + 58},{y - 34} Q{x + 82},{y - 30} {x + 84},{y - 14} V{y + 8} Z", grad(f, "fy18h-car", HOT_LIGHT, HOT), INK, 3)
    f.path(f"M{x - 16},{y - 58} H{x + 30} L{x + 46},{y - 36} H{x - 30} Z", GLASS, INK, 2)
    f.line(x + 8, y - 58, x + 8, y - 36, INK, 2)
    f.rect(x + 70, y - 22, 12, 8, HEAT_LIGHT, INK, 1.5, 2)
    for wx in (x - 46, x + 50): f.circle(wx, y + 10, 18, INK); f.circle(wx, y + 10, 8, ALUMINIUM)
    for k, (dx, dy) in enumerate(((150, -20), (130, -2), (160, 14))): f.line(x - dx, y + dy, x - dx + 40, y + dy, MUTED, 3, cap="round")
    # two groups, each with its own stopwatch held up
    for gx, shirts, turn in ((150, (COLD, GOOD), 0.27), (1050, (HEAT, COLD), 0.34)):
        sgn = 1 if gx < 600 else -1
        H.person(f, gx - 40 * sgn, 390, shirts[1], INK, 0.66)
        H.person(f, gx + 40 * sgn, 396, shirts[0], INK, 0.7)
        wx = gx + 110 * sgn
        f.line(gx + 40 * sgn + 20 * sgn, 396 - 236 * 0.7, wx, 276, shirts[0], 16, cap="round")   # the arm holds the watch out
        f.rect(wx - 12, 262, 24, 30, SAND_LIGHT, INK, 2, 10)
        H.stopwatch(f, wx, 222, 44, turn)
    return f.svg()


def setup():
    f = Fig("fy18-setup", 330, "Kaavakuva kokeen asetelmasta: leluauto ajaa pöydän tasaisella radalla lähtöviivalta maaliviivalle. "
            "Radan vieressä on matka-asteikko metreinä, ja lähtöviivan ja maaliviivan väli on muutettava muuttuja, matka s. "
            "Käsikello mittaa aikaa t, joka on mitattava muuttuja. Vakioina pysyvät auto, alusta ja paristot. "
            "Asteikko on mittakaavassa: 150 yksikköä kuvassa vastaa metriä.")
    f.defs_add(f'<linearGradient id="fy18-wood" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{SAND_LIGHT}"/><stop offset="1" stop-color="{SAND}"/></linearGradient>')
    # key of the three kinds of variable
    f.tex(24, 28, r"\text{muutettava: } s", "start")
    f.tex(24, 62, r"\text{mitattava: } t", "start")
    f.tex(24, 96, r"\text{vakiona: auto, alusta, paristot}", "start", w=420)
    # stopwatch
    cx, cy = 520, 66
    f.rect(cx - 6, cy - 46, 12, 12, WHITE, INK, 2, 2)
    f.circle(cx, cy, 30, WHITE, INK, 3)
    for k in range(12):
        import math
        a = k * math.pi / 6
        f.line(cx + 22 * math.sin(a), cy - 22 * math.cos(a), cx + 27 * math.sin(a), cy - 27 * math.cos(a), MUTED, 1.5)
    f.line(cx, cy, cx + 16, cy - 14, HEAT, 3, cap="round")
    f.circle(cx, cy, 3.5, INK)
    f.tex(cx, 118, "t", "middle")
    # table and ruler (150 units per metre, 0 at x = 72)
    x0, per = 72, 150
    f.rect(40, 200, 520, 16, "url(#fy18-wood)", INK, 2.5)
    for k in range(6):
        x = x0 + per * 0.5 * k
        f.line(x, 216, x, 224, INK, 2)
        f.tex(x, 242, fi(0.5 * k), "middle")
    f.tex(x0 + per * 2.5 + 28, 242, r"s\ (\text{m})", "start")
    # start and finish lines
    for x, name in ((x0, r"\text{lähtö}"), (x0 + per * 2.0, r"\text{maali}")):
        f.line(x, 140, x, 200, MUTED, 2, "6 5")
        f.tex(x, 126, name, "middle")
    # car, moving right
    f.rect(92, 166, 68, 22, ALUMINIUM, INK, 2.5, 6)
    f.rect(108, 148, 36, 18, "#eef5f9", INK, 2.5, 5)
    for wx in (110, 144):
        f.circle(wx, 191, 9, INK, WHITE, 2)
    f.arrow(176, 160, 250, 160, INK, 3, 14)
    f.tex(264, 160, "v", "start")
    # bracket for the distance
    xe = x0 + per * 2.0
    f.line(x0, 268, xe, 268, COLD, 2.5)
    f.line(x0, 258, x0, 278, COLD, 2.5)
    f.line(xe, 258, xe, 278, COLD, 2.5)
    f.tex((x0 + xe) / 2, 300, r"s = 2{,}00\,\text{m}", "middle", color=COLD)
    return f.svg()


def epavarmuus():
    f = Fig("fy18-eps", 340, "Kuvaaja suhteellisesta epävarmuudesta ajan funktiona, kun ajan epävarmuus on 0,2 s: "
            "kun aika on 1 s, epävarmuus on 20 %, kun aika on 4 s, se on 5,0 %, ja kun aika on 10 s, se on 2,0 %. "
            "Vihreä alue kuvaa mittauksia, joiden epävarmuus on enintään 5,0 %: ne vaativat vähintään 4 s:n ajan. "
            "Kuvaaja on mittakaavassa.")
    ax = Axes(f, (96, 286), (496, 54), x=(0, 10), y=(0, 24), xticks=[2, 4, 6, 8, 10], yticks=[5, 10, 15, 20],
              xlabel=r"t\ (\text{s})", ylabel=r"\varepsilon\ (\%)")
    ax.area([(4, 0), (10, 0), (10, 5), (4, 5)], GOOD_LIGHT, 0.7)
    f.line(ax.X(0), ax.Y(5), ax.X(10), ax.Y(5), GOOD, 2, "8 6")
    ax.curve(lambda t: 0.2 / t * 100, 1, 10, COLD, 3)
    ax.guide(4, 5)
    ax.point(4, 5, COLD)
    f.tex(ax.X(5.2), ax.Y(8.6), r"\varepsilon \le 5\,\%", "start", color=GOOD)
    f.tex(ax.X(2.2), ax.Y(19), r"\varepsilon = \dfrac{0{,}2\,\text{s}}{t}", "start", color=COLD, w=180)
    return f.svg()


FIGURES = {"hero": hero, "setup": setup, "epavarmuus": epavarmuus}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "setup": "safe: the setup with its variables, no results",
    "epavarmuus": "reveals: the relative uncertainty for 1, 4 and 10 s",
}
