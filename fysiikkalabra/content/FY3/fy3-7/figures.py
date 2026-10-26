"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy3-7` writes them into lesson.md."""
import math
from figlib import (Fig, Axes, INK, MUTED, GLASS, WATER_LIGHT, WATER, HEAT, HEAT_LIGHT, HOT, ICE, COLD_LIGHT, fi)


def micro_model():
    f = Fig("fy37-micro", 306, "Mikromalli, kaavakuva: kiinteässä aineessa hiukkaset ovat säännöllisessä järjestyksessä "
            "toisissaan kiinni, nesteessä ne ovat epäjärjestyksessä mutta yhä kosketuksissa, kaasussa ne ovat kaukana "
            "toisistaan ja liikkuvat vapaasti. Nuolet: kiinteä sulaa nesteeksi, neste höyrystyy kaasuksi.")
    f.defs_add('<radialGradient id="fy37-ball" cx="0.35" cy="0.35" r="0.75"><stop offset="0" stop-color="#ffffff"/>'
               '<stop offset="1" stop-color="#a9d1f0"/></radialGradient>')
    for x in (20, 225, 430):
        f.rect(x, 92, 150, 150, GLASS, INK, 3, 6)
    balls = [(50 + 30 * i, 122 + 30 * j) for j in range(4) for i in range(4)]
    balls += [(247, 226), (275, 224), (303, 227), (331, 224), (357, 226), (261, 200), (289, 199), (318, 202), (346, 198),
              (250, 174), (278, 172), (307, 176), (336, 172)]
    balls += [(458, 120), (545, 130), (500, 172), (462, 218), (552, 212)]
    for cx, cy in balls:
        f.circle(cx, cy, 13, "url(#fy37-ball)", WATER, 2)
    for x1, y1, x2, y2 in [(472, 125, 494, 133), (536, 142, 522, 162), (496, 187, 489, 209), (460, 205, 456, 181), (539, 222, 520, 234)]:
        f.line(x1, y1, x2, y2, MUTED, 2, cap="round")
    f.block_arrow(178, 167, 218, 167, HEAT, 12, 26, 18)
    f.block_arrow(383, 167, 423, 167, HEAT, 12, 26, 18)
    f.tex(198, 62, r"\text{sulaa}", "middle")
    f.tex(403, 62, r"\text{höyrystyy}", "middle")
    for x, w in ((95, r"\text{kiinteä}"), (300, r"\text{neste}"), (505, r"\text{kaasu}")):
        f.tex(x, 274, w, "middle")
    return f.svg()


def heating_curve():
    f = Fig("fy37-curve", 350, "Veden lämpenemiskäyrä, kaavakuva: lämpötila siirretyn energian Q funktiona. Jää lämpenee "
            "jyrkästi, sulaa vaakasuoralla osalla 0 asteessa (Q = sm), vesi lämpenee loivemmin 0:sta 100 asteeseen, "
            "kiehuu pitkällä vaakasuoralla osalla 100 asteessa (Q = rm) ja höyry lämpenee jyrkästi. Jään ja höyryn "
            "osien jyrkkyys on noin kaksinkertainen veden osaan verrattuna; vaakasuorien osien pituudet eivät ole "
            "mittakaavassa.")
    ax = Axes(f, (96, 296), (476, 60), x=(0, 380), y=(-50, 150), xticks=[], yticks=[0, 100],
              xlabel=r"Q", ylabel=r"T\ (^\circ\text{C})", origin_label=False)
    pts = [(0, -30), (18, 0), (54, 0), (174, 100), (360, 100), (372, 120)]
    ax.line(pts, HOT, 3.5)
    f.tex(ax.X(380) + 8, ax.Y(120) - 2, r"\text{höyry}", "start", HOT)
    f.tex(ax.X(3), ax.Y(32), r"\text{jää}", "start", bg=True)
    f.tex(ax.X(60), ax.Y(-17), r"\text{sulaa}\quad Q = sm", "start")
    f.tex(ax.X(150), ax.Y(22), r"\text{vesi}", "start")
    f.tex(ax.X(267), ax.Y(120), r"\text{kiehuu}\quad Q = rm", "middle")
    return f.svg()


def phase_diagram():
    f = Fig("fy37-phase", 350, "Faasikaavio, kaavakuva: paine p lämpötilan T funktiona. Käyrät erottavat kiinteän, "
            "nesteen ja kaasun alueet ja kohtaavat kolmoispisteessä. Kun paine on ilmanpaine, vesi kiehuu 100 "
            "asteessa; vuorella paine on pienempi ja kiehumispiste alempi.")
    ax = Axes(f, (96, 296), (476, 56), x=(0, 100), y=(0, 100), xticks=[], yticks=[], xlabel=r"T", ylabel=r"p",
              grid=False, origin_label=False)
    tp, cp = (30, 12), (88, 70)
    sub = [(T, 12 * (T / 30) ** 2.2) for T in [30 * i / 30 for i in range(0, 31)]]
    vap = [(T, 12 + 58 * ((T - 30) / 58) ** 1.6) for T in [30 + 58 * i / 40 for i in range(41)]]
    melt = [(30, 12), (27, 100)]
    ax.area(sub + melt[1:] + [(0, 100)], COLD_LIGHT, 0.7)
    ax.area(vap + [(100, 70), (100, 100)] + melt[::-1], WATER_LIGHT, 0.55)
    ax.area(sub + vap[1:] + [(100, 70), (100, 0), (0, 0)], HEAT_LIGHT, 0.5)
    ax.line(sub, INK, 3); ax.line(vap, INK, 3); ax.line(melt, INK, 3)
    g = lambda p: 30 + 58 * ((p - 12) / 58) ** (1 / 1.6)
    p0, p1 = 46, 28
    for p, name in ((p0, r"\text{ilmanpaine}"), (p1, r"\text{vuori}")):
        T = g(p)
        ax.guide(T, p)
        ax.point(T, p, HOT)
        f.tex(ax.X(T) + 14, ax.Y(p) + 8, name, "start")
    f.tex(ax.X(g(p0)), ax.y0 + 24, r"100\,{}^\circ\text{C}", "middle", w=100)
    ax.point(*tp, INK)
    f.line(ax.X(tp[0]), ax.Y(tp[1]), ax.X(tp[0]), ax.y0, MUTED, 1.5, "6 5")
    f.tex(ax.X(tp[0]), ax.y0 + 24, r"\text{kolmoispiste}", "middle", w=140)
    f.tex(ax.X(13), ax.Y(66), r"\text{kiinteä}", "middle")
    f.tex(ax.X(58), ax.Y(88), r"\text{neste}", "middle")
    f.tex(ax.X(84), ax.Y(9), r"\text{kaasu}", "middle")
    return f.svg()


FIGURES = {"micro-model": micro_model, "heating-curve": heating_curve, "phase-diagram": phase_diagram}
