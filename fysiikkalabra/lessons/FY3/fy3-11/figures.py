"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy3-11` writes them into lesson.md."""
from figlib import (Fig, Axes, INK, MUTED, WHITE, RULE, GLASS, HEAT, HEAT_LIGHT, HOT, HOT_LIGHT, COLD, COLD_LIGHT,
                    ALUMINIUM, IRON)

import herolib as H

def heat_engine():
    f = Fig("fy311-engine", 340, "Lämpövoimakoneen energiavirrat nuolina, joiden leveys kuvaa energiavirtaa eli tehoa: "
            "kuumasta lähteestä, jonka lämpötila on T_1, tulee koneeseen lämpö Q_1. Kone tekee työn W, joka on 40 "
            "prosenttia Q_1:stä, ja luovuttaa loput, lämmön Q_2, kylmään ympäristöön, jonka lämpötila on T_2. "
            "Nuolten leveydet ovat mittakaavassa: Q_1 60, W 24 ja Q_2 36 yksikköä, joten Q_1-nuoli on yhtä leveä "
            "kuin W- ja Q_2-nuolet yhteensä.")
    f.rect(150, 12, 300, 52, HOT_LIGHT, HOT, 2.5, 10)
    f.tex(300, 38, r"\text{kuuma lähde}\quad T_1", "middle")
    f.rect(150, 276, 300, 52, COLD_LIGHT, COLD, 2.5, 10)
    f.tex(300, 302, r"\text{kylmä ympäristö}\quad T_2", "middle")
    f.rect(225, 118, 150, 98, GLASS, INK, 3, 12)
    f.tex(300, 167, r"\text{kone}", "middle")
    f.block_arrow(300, 64, 300, 118, HEAT, 60, 84, 24)       # Q1: width 60
    f.block_arrow(300, 216, 300, 274, HEAT_LIGHT, 36, 60, 24)  # Q2: width 36
    f.block_arrow(375, 167, 560, 167, INK, 24, 46, 26)        # W: width 24
    f.tex(354, 92, r"Q_1", "start")
    f.tex(342, 244, r"Q_2", "start")
    f.tex(470, 134, r"W", "middle")
    f.tex(16, 152, r"\text{nuolen leveys}", "start")
    f.tex(16, 182, r"\text{kuvaa tehoa}", "start")
    return f.svg()


def heat_pump():
    f = Fig("fy311-pump", 270, "Lämpöpumpun energiavirrat nuolina, joiden leveys kuvaa tehoa: sähköenergia E_s ja "
            "ulkoilmasta otettu lämpö Q_ulko tulevat pumppuun, ja pumppu luovuttaa sisälle lämmön Q_sisälle, joka on "
            "niiden summa. Nuolten leveydet ovat mittakaavassa: E_s 20, Q_ulko 40 ja Q_sisälle 60 yksikköä, joten "
            "sisälle lähtevä nuoli on yhtä leveä kuin kaksi tulevaa nuolta yhteensä ja kolme kertaa niin leveä "
            "kuin sähkön nuoli.")
    f.rect(230, 76, 130, 126, GLASS, INK, 3, 12)
    f.tex(295, 139, r"\text{pumppu}", "middle")
    f.block_arrow(16, 110, 230, 110, INK, 20, 28, 22)          # Es: width 20
    f.block_arrow(16, 158, 230, 158, HEAT_LIGHT, 40, 48, 22)   # Qulko: width 40
    f.block_arrow(360, 139, 560, 139, HEAT, 60, 70, 28)        # Qsisälle: width 60
    f.tex(16, 74, r"\text{sähkö}\ E_\text{s}", "start")
    f.tex(16, 206, r"\text{ulkoilman lämpö}", "start")
    f.tex(16, 238, r"Q_\text{ulko}", "start")
    f.tex(460, 92, r"\text{lämpö sisälle}", "middle")
    f.tex(460, 192, r"Q_\text{sisälle}", "middle")
    f.tex(588, 252, r"\text{leveys kuvaa tehoa}", "end")
    return f.svg()


def pv_work():
    f = Fig("fy311-pv", 330, "(V, p)-kuvaaja vakiopaineessa laajenevasta kaasusta: paine p pysyy vakiona, kun "
            "tilavuus kasvaa arvosta V_1 arvoon V_2, joten kuvaaja on vaakasuora jana, jonka nuoli osoittaa "
            "laajenemisen suuntaa. Janan ja V-akselin väliin jäävä varjostettu suorakulmio, jonka leveys on "
            "tilavuuden muutos ΔV ja korkeus p, on kaasun tekemä työ W_k = p ΔV. Kaaviokuva.")
    ax = Axes(f, (96, 270), (470, 60), x=(0, 7), y=(0, 4), xticks=[2, 5], yticks=[3],
              xlabel=r"V\ (\text{m}^3)", ylabel=r"p\ (\text{Pa})",
              xfmt=lambda v: "V_1" if v == 2 else "V_2", yfmt=lambda v: "p", origin_label=True)
    ax.area([(2, 0), (5, 0), (5, 3), (2, 3)], HEAT, 0.35)
    ax.line([(2, 3), (5, 3)], INK, 4.5)
    for v in (2, 5):
        f.line(ax.X(v), ax.Y(3), ax.X(v), ax.y0, MUTED, 1.5, "6 5")
    f.arrow(ax.X(3.5) - 14, ax.Y(3), ax.X(3.5) + 14, ax.Y(3), INK, 4.5, 20)
    f.tex(ax.X(3.5), ax.Y(3) - 26, r"\text{kaasu laajenee}", "middle")
    f.tex(ax.X(3.5), ax.Y(1.9), r"W_\text{k} = p\,\Delta V", "middle")
    yd = ax.Y(0.8)
    f.arrow(ax.X(3.5) - 26, yd, ax.X(2) + 3, yd, INK, 2, 13)
    f.arrow(ax.X(3.5) + 26, yd, ax.X(5) - 3, yd, INK, 2, 13)
    f.tex(ax.X(3.5), yd, r"\Delta V", "middle")
    return f.svg()


def piston_work():
    f = Fig("fy311-piston", 330, "Kaasun tekemä työ männälle, periaatekuva. Sylinterin poikkipinta-ala on A. Kaasun "
            "paine p työntää mäntää voimalla F = pA, ja mäntä siirtyy matkan Δs oikealle. Kaasun tilavuus kasvaa "
            "varjostetun osan verran, ΔV = AΔs. Työ on W_k = FΔs = pAΔs = pΔV. Kuva ei ole mittakaavassa.")
    f.defs_add('<pattern id="fy311-dv" width="12" height="12" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">'
               f'<rect width="12" height="12" fill="{HEAT_LIGHT}"/><line x1="0" y1="0" x2="0" y2="12" stroke="{HEAT}" stroke-width="2"/></pattern>')
    top, bot, x0, p1, p2 = 70, 190, 110, 250, 420
    f.rect(x0, top, p1 - x0, bot - top, HEAT_LIGHT, extra='fill-opacity="0.3"')       # gas before
    f.rect(p1, top, p2 - p1, bot - top, "url(#fy311-dv)")                              # the added volume
    f.line(p1, top, p1, bot, MUTED, 2, "7 5")                                          # the piston's first place
    f.rect(x0 - 6, top - 6, 6, bot - top + 12, ALUMINIUM, INK, 2.5)
    f.rect(x0 - 6, top - 6, 458, 6, ALUMINIUM, INK, 2.5)
    f.rect(x0 - 6, bot, 458, 6, ALUMINIUM, INK, 2.5)
    f.rect(p2 - 7, top + 1, 14, bot - top - 2, IRON, INK, 2.5)
    f.arrow(p2 + 9, 130, 536, 130, HEAT, 5, 22)
    f.tex(478, 100, r"F = pA", "middle")
    f.tex(180, 130, r"\text{kaasu},\ p", "middle")
    f.tex(335, 130, r"\Delta V", "middle", bg=True)
    # A: the piston's area, as the height of the cylinder
    f.arrow(76, 130, 76, top + 1, INK, 2, 12); f.arrow(76, 130, 76, bot - 1, INK, 2, 12)
    f.tex(66, 130, r"A", "end", bg=True)
    # delta s below
    ys = 226
    f.line(p1, bot + 8, p1, ys + 8, MUTED, 1.5); f.line(p2, bot + 8, p2, ys + 8, MUTED, 1.5)
    f.arrow(335 - 24, ys, p1 + 1, ys, INK, 2, 12); f.arrow(335 + 24, ys, p2 - 1, ys, INK, 2, 12)
    f.tex(335, ys, r"\Delta s", "middle")
    f.tex(300, 290, r"W_\text{k} = F\,\Delta s = pA\,\Delta s = p\,\Delta V", "middle")
    return f.svg()


def hero():
    """The chapter's opening illustration: a condensing power plant by a lake, electricity out on the lines, waste heat into the air and the lake."""
    f = H.hero("fy311-hero", "Kuvitus: lauhdevoimalaitos järven rannalla. Voimalinjat vievät sähköä pois, jäähdytystornista nousee "
               "suuri höyrypilvi, ja lauhdevesi purkautuu järveen lämpimänä, mikä näkyy oranssina vyöhykkeenä vedessä. Suurin osa "
               "polttoaineen energiasta lähtee lämpönä ilmaan ja veteen.")
    H.sky(f, "fy311h", 420)
    H.forest(f, 380, 44, 24, H.ALUMINIUM, seed=9, depth=40)
    f.rect(0, 420, 1200, 180, H.grad(f, "fy311h-lake", H.WATER_LIGHT, H.WATER))
    f.path("M0,400 H900 Q860,420 820,440 H0 Z", H.RULE)
    # cooling tower with its plume
    f.path("M120,420 Q160,300 140,190 H300 Q280,300 320,420 Z", H.grad(f, "fy311h-tower", H.WHITE, H.ALUMINIUM, horizontal=True), H.INK, 3)
    for x, y, sc in ((220, 170, 1.0), (300, 110, 1.3), (430, 70, 1.4), (580, 60, 1.1)):
        H.cloud(f, x, y, sc, H.WHITE, extra=f'stroke="{H.RULE}" stroke-width="2.5"')
    # boiler house, turbine hall, chimney
    f.rect(360, 250, 140, 170, H.RULE_LIGHT, H.INK, 3)
    f.rect(500, 310, 220, 110, H.ALUMINIUM, H.INK, 3)
    for x in range(520, 700, 44): f.rect(x, 340, 26, 40, H.GLASS, H.INK, 2)
    f.rect(400, 120, 36, 130, H.grad(f, "fy311h-chimney", H.WHITE, H.ALUMINIUM, horizontal=True), H.INK, 3)
    f.rect(380, 290, 30, 40, H.HEAT_LIGHT, H.INK, 2); f.rect(440, 290, 30, 40, H.HEAT_LIGHT, H.INK, 2)
    # warm cooling water into the lake
    f.rect(690, 420, 30, 24, H.IRON, H.INK, 2)
    f.add(f'<ellipse cx="760" cy="480" rx="150" ry="40" fill="{H.HEAT_LIGHT}" fill-opacity="0.55"/>')
    f.add(f'<ellipse cx="740" cy="468" rx="80" ry="22" fill="{H.HEAT}" fill-opacity="0.45"/>')
    # electricity out on the power lines
    for x in (880, 1060):
        f.path(f"M{x - 30},420 L{x},230 L{x + 30},420 M{x - 40},270 H{x + 40} M{x - 30},300 H{x + 30}", stroke=H.INK, w=4)
    f.path("M720,320 Q800,290 840,270 M840,270 Q960,300 1020,270 M1100,270 Q1150,290 1200,285", stroke=H.INK, w=2)
    f.path("M720,330 Q800,320 850,300 M850,300 Q960,330 1030,300 M1090,300 Q1150,320 1200,315", stroke=H.INK, w=2)
    return f.svg()


FIGURES = {"hero": hero, "piston-work": piston_work, "heat-engine": heat_engine, "heat-pump": heat_pump, "pv-work": pv_work}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "piston-work": "reveals: the derivation W = pΔV",
    "heat-engine": "reveals: the efficiency 40 %",
    "heat-pump": "reveals: Q_sisälle = 3 E_s",
    "pv-work": "reveals: the work is the area under the line",
}
