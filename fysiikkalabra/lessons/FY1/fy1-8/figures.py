"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy1-8` writes them into lesson.md."""
from figlib import Fig, Axes, INK, MUTED, WHITE, RULE, SAND, SAND_DARK, SAND_LIGHT, ALUMINIUM, METAL_EDGE, COLD, GOOD, GOOD_LIGHT, HEAT, fi
from figlib import GLASS, HEAT_LIGHT, HOT, PAPER
import herolib as H


def hero():
    """The chapter's opening illustration: one toy car on a track, two groups timing it with their own tape and stopwatch."""
    f = H.hero("fy18-hero", "Kuvitus: lattialla rata, jolla leluauto kulkee mittanauhan vieressä. Radan molemmin puolin seisoo ryhmä, "
               "ja kummallakin ryhmällä on oma sekuntikello; kellojen viisarit ovat pysähtyneet eri kohtiin.")
    f.rect(0, 0, 1200, 600, PAPER)
    f.path("M0,330 H1200 V600 H0 Z", SAND_LIGHT)
    for k in range(7): f.line(-200 + k * 260, 600, 80 + k * 200, 330, SAND, 2)
    f.line(0, 330, 1200, 330, SAND_DARK, 3)
    # track and tape
    f.path("M120,470 L1080,470 L1040,420 L160,420 Z", ALUMINIUM, INK, 3)
    f.rect(140, 476, 920, 28, HEAT_LIGHT, INK, 2, 3)
    for k in range(47): f.line(150 + k * 19.6, 476, 150 + k * 19.6, 476 + (16 if k % 5 == 0 else 8), INK, 1.5)
    # toy car
    x, y = 600, 446
    f.path(f"M{x - 70},{y + 6} V{y - 18} Q{x - 64},{y - 26} {x - 40},{y - 28} L{x - 22},{y - 56} H{x + 30} L{x + 52},{y - 28} Q{x + 72},{y - 26} {x + 74},{y - 12} V{y + 6} Z", HOT, INK, 3)
    f.path(f"M{x - 14},{y - 48} H{x + 26} L{x + 40},{y - 30} H{x - 26} Z", GLASS, INK, 2)
    for wx in (x - 40, x + 44): f.circle(wx, y + 8, 15, INK); f.circle(wx, y + 8, 6, ALUMINIUM)
    f.line(x - 120, y - 10, x - 84, y - 10, MUTED, 3, cap="round"); f.line(x - 130, y - 30, x - 90, y - 30, MUTED, 3, cap="round")
    # two groups with their stopwatches
    H.person(f, 90, 400, COLD, INK, 0.62); H.person(f, 200, 404, GOOD, INK, 0.6)
    H.person(f, 1000, 400, HEAT, INK, 0.62); H.person(f, 1110, 404, COLD, INK, 0.6)
    H.stopwatch(f, 250, 140, 56, 0.27); H.stopwatch(f, 950, 140, 56, 0.33)
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
