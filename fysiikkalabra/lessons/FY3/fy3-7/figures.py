"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy3-7` writes them into lesson.md."""
import math
from figlib import (Fig, Axes, INK, MUTED, GLASS, WATER_LIGHT, WATER, HEAT, HEAT_LIGHT, HOT, ICE, COLD_LIGHT, fi)
import herolib as H


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


def hero():
    """The chapter's opening illustration: water boiling hard on a hot plate, the thermometer stuck at the boiling point."""
    from figlib import WHITE, INK, RULE, RULE_LIGHT, IRON, ALUMINIUM, METAL_EDGE, n
    f = Fig("fy37-hero", 600, "Kuvitus: keittiön liedellä kattila, jossa vesi kiehuu voimakkaasti. Levy hehkuu punaisena ja "
            "siitä siirtyy jatkuvasti energiaa kattilaan, vedessä on kuplia ja siitä nousee höyryä. Veteen upotetun "
            "lämpömittarin pylväs pysyy samalla korkeudella.", width=1200, hero=True)
    f.defs_add(f'<linearGradient id="fy37h-steel" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{METAL_EDGE}"/>'
               f'<stop offset="0.3" stop-color="{WHITE}"/><stop offset="0.65" stop-color="{ALUMINIUM}"/><stop offset="1" stop-color="{METAL_EDGE}"/></linearGradient>')
    f.defs_add(f'<linearGradient id="fy37h-water" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{WATER_LIGHT}"/><stop offset="1" stop-color="{WATER}"/></linearGradient>')
    f.defs_add(f'<radialGradient id="fy37h-glow" cx="0.5" cy="0.5" r="0.5"><stop offset="0.55" stop-color="{HOT}"/><stop offset="0.8" stop-color="{HEAT}"/>'
               f'<stop offset="1" stop-color="{HEAT_LIGHT}" stop-opacity="0"/></radialGradient>')
    f.defs_add(f'<linearGradient id="fy37h-sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{ICE}"/><stop offset="1" stop-color="{COLD_LIGHT}"/></linearGradient>')
    # tiled wall and a window with a winter sky
    f.rect(0, 0, 1200, 600, WHITE)
    for x in range(0, 1201, 75): f.line(x, 0, x, 420, RULE_LIGHT, 2)
    for y in range(0, 421, 75): f.line(0, y, 1200, y, RULE_LIGHT, 2)
    f.rect(70, 50, 230, 270, "url(#fy37h-sky)", INK, 3, 4)
    f.path("M70,282 Q140,250 200,272 T300,262 V320 H70 Z", WHITE)
    f.line(185, 50, 185, 320, INK, 3); f.line(70, 185, 300, 185, INK, 3)
    f.rect(58, 320, 254, 14, RULE, INK, 3, 3)
    # worktop and cupboards
    f.rect(0, 420, 1200, 26, RULE, INK, 3)
    f.rect(0, 446, 1200, 154, RULE_LIGHT)
    for x in (300, 900): f.line(x, 446, x, 600, INK, 2)
    for x in (270, 330, 870, 930): f.rect(x - 4, 470, 8, 44, METAL_EDGE, rx=4)
    # stove: hob and front with knobs
    f.rect(340, 404, 520, 22, IRON, INK, 3, 4)
    f.rect(340, 446, 520, 154, ALUMINIUM, INK, 3)
    f.rect(370, 476, 460, 110, GLASS, INK, 2.5, 6)
    for x in (400, 460, 740, 800): f.circle(x, 461, 9, INK)
    f.add('<ellipse cx="600" cy="404" rx="210" ry="18" fill="url(#fy37h-glow)"/>')     # the hot plate glows around the pot
    # the pot: steel body, handles, the boiling water seen over the rim
    f.path("M440,236 V380 Q440,404 470,404 H730 Q760,404 760,380 V236 Z", "url(#fy37h-steel)", INK, 3)
    for x0, x1 in ((440, 398), (760, 802)):
        f.path(f"M{x0},262 H{x1} Q{x1 + (6 if x1 > x0 else -6)},262 {x1 + (6 if x1 > x0 else -6)},272 V276 Q{x1 + (6 if x1 > x0 else -6)},284 {x1},284 H{x0} Z", INK)
    f.add(f'<ellipse cx="600" cy="236" rx="160" ry="30" fill="{ALUMINIUM}" stroke="{INK}" stroke-width="3"/>')
    f.add(f'<ellipse cx="600" cy="242" rx="146" ry="22" fill="url(#fy37h-water)"/>')
    for x, y, r in ((520, 240, 9), (556, 248, 6), (600, 236, 11), (640, 250, 7), (680, 240, 9), (575, 254, 5), (712, 248, 5), (494, 248, 5)):
        f.circle(x, y, r, WHITE, WATER, 2)
    # steam rising from the pot in soft wisps
    for x, top, sway in ((520, 110, 1), (585, 50, -1), (650, 80, 1), (700, 140, -1)):
        d = f"M{x},214 c{18 * sway},-30 {-18 * sway},-50 0,-80 s{-18 * sway},-50 0,{n(-(134 - top) - 0)}"
        f.path(d, stroke=RULE, w=26, extra='stroke-linecap="round" stroke-opacity="0.55"')
        f.path(d, stroke=WHITE, w=20, extra='stroke-linecap="round"')
    # thermometer leaning in the pot, its column steady
    f.add('<g transform="rotate(18 760 150)">')
    f.rect(751, 40, 18, 230, WHITE, INK, 3, 9)
    f.rect(756, 176, 8, 94, HOT)
    for k in range(6): f.line(769, 70 + 22 * k, 777, 70 + 22 * k, MUTED, 2)
    f.add('</g>')
    f.add(f'<ellipse cx="600" cy="242" rx="146" ry="22" fill="none" stroke="{WHITE}" stroke-width="2" stroke-opacity="0.6"/>')
    return f.svg()


def scene():
    """A second everyday scene: a lake freezing over in early winter, the first snow on the shore."""
    f = H.scene("fy37-scene", "Kuvitus: järvi jäätyy alkutalvella. Rannan puolella on jo ohut jääkansi, ulompana vesi on vielä "
                "sulana, ja rannalla on ensilumi.")
    H.sky(f, "fy37s", 200, H.COLD_LIGHT, H.WHITE)
    H.forest(f, 190, 46, 24, H.METAL_EDGE, seed=3, depth=20)
    f.rect(0, 200, 600, 160, H.grad(f, "fy37s-lake", H.WATER_LIGHT, H.WATER))
    f.path("M0,240 Q200,226 340,252 Q420,268 600,256 V360 H0 Z", H.ICE)
    f.path("M0,240 Q200,226 340,252 Q420,268 600,256", stroke=H.ICE_EDGE, w=3)
    for d in ("M60,290 L120,300 L150,280", "M220,320 L260,296 L320,310", "M400,300 L460,320"):
        f.path(d, stroke=H.ICE_EDGE, w=2)
    f.path("M0,300 Q120,290 220,312 Q320,334 340,360 H0 Z", H.WHITE, H.RULE, 2)
    for k in range(30): f.circle(H.rnd(k, 5) * 600, H.rnd(k + 70, 5) * 190, 2 + 1.5 * H.rnd(k + 9, 5), H.WHITE, H.ICE_EDGE, 1)
    return f.svg()


FIGURES = {"hero": hero, "scene": scene, "micro-model": micro_model, "heating-curve": heating_curve, "phase-diagram": phase_diagram}
