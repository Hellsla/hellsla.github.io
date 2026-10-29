"""Figures of fy2-6 (scripts/figlib.py); `python scripts/figures.py fy2-6` writes them into lesson.md."""
import math
from figlib import (Fig, INK, MUTED, WHITE, RULE, RULE_LIGHT, HEAT, HEAT_LIGHT, GLASS, WATER, WATER_LIGHT, n)
from figlib import ALUMINIUM, COLD_LIGHT, GOOD, GOOD_LIGHT, HOT_LIGHT, IRON, SAND_DARK, SAND_LIGHT
import herolib as H


def hero():
    """The chapter's opening illustration: a nuclear plant, a hydro plant, wind turbines and a combined heat and power plant feed one grid to a town."""
    f = H.hero("fy26-hero", "Kuvitus: suomalainen maisema, jossa on ydinvoimala meren rannalla, vesivoimala joen padolla, tuulivoimaloita ja "
               "savupiipullinen polttoainevoimala. Kaikista lähtevät voimalinjat samaan verkkoon, joka vie sähkön kaupunkiin.")
    H.sky(f, "fy26h", 420); H.cloud(f, 300, 80, 0.7); H.cloud(f, 900, 60, 0.6)
    H.forest(f, 330, 46, 30, GOOD, seed=7)
    f.rect(0, 340, 1200, 260, GOOD_LIGHT)
    f.path("M0,430 Q120,420 260,440 L260,600 H0 Z", WATER_LIGHT)
    # nuclear plant by the sea: a domed reactor hall and a turbine hall
    f.rect(40, 330, 150, 80, ALUMINIUM, INK, 3)
    f.rect(150, 300, 60, 110, WHITE, INK, 3)
    f.path("M150,300 Q180,250 210,300 Z", WHITE, INK, 3)
    f.rect(70, 290, 18, 40, IRON, INK, 2)
    # hydro plant: river through a dam
    f.path("M330,600 Q360,500 420,440 L470,440 Q440,520 470,600 Z", WATER)
    f.rect(380, 400, 110, 50, SAND_LIGHT, INK, 3)
    f.path("M380,400 H490 L470,380 H400 Z", IRON, INK, 2)
    for k in range(3): f.rect(394 + k * 32, 414, 18, 26, GLASS, INK, 2)
    f.path("M330,400 Q360,380 380,400", stroke=WATER, w=4)
    # wind turbines
    for k, (x, h) in enumerate(((600, 210), (690, 180), (770, 200))): H.wind_turbine(f, x, 400, h, 0.4 + 1.3 * k, 0.9)
    # CHP plant with chimney
    f.rect(840, 330, 120, 80, SAND_DARK, INK, 3)
    f.rect(930, 180, 26, 150, HOT_LIGHT, INK, 3)
    for k in range(3): f.rect(930, 200 + k * 40, 26, 8, WHITE)
    H.smoke(f, 950, 160, 0.8, RULE, 0.8)
    # town on the right
    for k, (x, w, h, c) in enumerate(((1020, 50, 120, COLD_LIGHT), (1074, 40, 160, SAND_LIGHT), (1118, 60, 100, HOT_LIGHT))):
        f.rect(x, 410 - h, w, h, c, INK, 3)
        for j in range(int(h / 34)): f.rect(x + 10, 410 - h + 12 + j * 32, w - 20, 14, GLASS, INK, 1.5)
    # one grid joining them, from the plants to the town
    pts = [(250, 540), (530, 540), (810, 540), (1000, 540)]
    arms = [H.pylon(f, x, y, 110, 0.7) for x, y in pts]
    for a, b in zip(arms, arms[1:]):
        for p, q in zip(a, b): H.wire(f, p, q, 14, INK, 1.5)
    for a, b in ((arms[0][2], (205, 410)), (arms[1][2], (490, 430)), (arms[2][3], (900, 410)), (arms[3][3], (1040, 410))): H.wire(f, a, b, 6, INK, 1.5)
    return f.svg()


def plants():
    f = Fig("fy26-pl", 366, "Kaavakuva: viisi tapaa tuottaa sähköä. Putoava vesi pyörittää vesiturbiinia, tuuli roottoria, ja kummankin "
            "akseli pyörittää generaattoria G. Auringonsäteily osuu aurinkopaneeliin, joka tuottaa sähköä suoraan ilman generaattoria. "
            "Uraanin ydinenergia lämmittää reaktorissa höyryn ja polttoaineen kemiallinen energia kattilassa höyryn, ja höyry pyörittää "
            "turbiinia ja generaattoria. Harmaat nuolet ovat luonnonvaran energiaa, tummat nuolet sähköä, ja jokaisesta laitoksesta "
            "lähtee alaspäin oranssi nuoli: osa energiasta päätyy lämpönä ympäristöön. Kuva on kaavamainen, nuolten pituus ei kuvaa tehoa.")
    rows = [("vesi", "vesiturbiini", True), ("tuuli", "roottori", True), ("säteily", "aurinkopaneeli", False),
            ("uraani", "reaktori, turbiini", True), ("polttoaine", "kattila, turbiini", True)]
    top, step, bh = 14, 66, 44
    f.rect(496, top, 88, step * 4 + bh, GLASS, INK, 3, 10)
    f.tex(540, top + (step * 4 + bh) / 2, r"\text{sähkö}", "middle", size=24, w=80)
    for i, (src, dev, gen) in enumerate(rows):
        y = top + step * i; cy = y + bh / 2
        f.rect(16, y, 132, bh, WHITE, INK, 2.5, 10)
        f.tex(82, cy, r"\text{" + src + "}", "middle", size=24, w=124)
        f.block_arrow(150, cy, 174, cy, MUTED, 12, 24, 14)
        f.rect(176, y, 236, bh, GLASS, INK, 2.5, 10)
        f.tex(294, cy, r"\text{" + dev + "}", "middle", size=24, w=228)
        f.block_arrow(390, y + bh + 1, 390, y + bh + 19, HEAT, 8, 18, 10)
        if gen:
            f.arrow(414, cy, 438, cy, INK, 3, 12)
            f.circle(456, cy, 16, WHITE, INK, 2.5)
            f.tex(456, cy, "G", "middle", size=24, w=26)
            f.arrow(474, cy, 494, cy, INK, 3, 12)
        else:
            f.arrow(414, cy, 494, cy, INK, 3, 12)
    yb = top + step * 4 + bh + 16
    f.tex(16, yb, r"G\text{: generaattori}", "start", size=24, w=200)
    f.tex(380, yb, r"\text{lämpö}", "end", size=24, w=80)
    return f.svg()


def fi_bars():
    f = Fig("fy26-fi", 330, "Vaakapylväskaavio Suomen sähköntuotannosta vuonna 2024 energialähteittäin teravattitunteina (Tilastokeskus), "
            "mittakaavassa: ydinvoima 31, tuulivoima 20,2, vesivoima 14,1, bioperäiset polttoaineet 9,5, fossiiliset polttoaineet ja "
            "turve 3,4 ja aurinkosähkö 0,9. Ydinvoiman pylväs on noin kaksi viidesosaa kokonaistuotannosta 79,9.")
    f.tex(168, 20, r"E\ (\text{TWh})", "start", w=120)
    x0, per = 170, 10.5                 # 10 TWh = 105 units
    rows = [("ydinvoima", 31), ("tuulivoima", 20.2), ("vesivoima", 14.1), ("bioperäiset", 9.5), ("fossiiliset", 3.4), ("aurinko", 0.9)]
    for t in (10, 20, 30):
        f.line(x0 + t * per, 42, x0 + t * per, 262, RULE_LIGHT, 1.5)
    for i, (name, v) in enumerate(rows):
        y = 46 + 36 * i
        f.rect(x0, y, v * per, 26, HEAT_LIGHT, HEAT, 1.5, 3)
        f.tex(x0 - 10, y + 13, r"\text{" + name + "}", "end", size=24, w=150)
        lab = f"{v:g}".replace(".", "{,}")
        f.tex(x0 + v * per + 8, y + 13, lab, "start", size=24)
    f.arrow(x0, 262, x0 + 3 * 105 + 60, 262, INK, 2.5, 13)
    f.line(x0, 40, x0, 264, INK, 2.5)
    for t in (10, 20, 30):
        f.line(x0 + t * per, 262, x0 + t * per, 269, INK, 2)
        f.tex(x0 + t * per, 288, str(t), "middle", MUTED, size=24)
    f.tex(x0 - 10, 288, "0", "end", MUTED, size=24)
    return f.svg()


def unit_power():
    f = Fig("fy26-up", 372, "Pistekuvaaja yksittäisten voimalaitosten tehoista logaritmisella asteikolla, jossa jokainen pystyviiva on "
            "kymmenkertainen edelliseen: omakotitalon aurinkopaneelit noin 5 kW, tuulivoimala noin 5 MW, suuri vesivoimalaitos noin "
            "100 MW ja Olkiluoto 3 noin 1600 MW. Pisteen paikka kertoo tehon kymmenen potenssin, joten Olkiluoto 3 on noin 320 kertaa "
            "tuulivoimalaa suurempi, vaikka sen piste on vain kaksi ja puoli askelta oikeammalla.")
    x0, per = 40, 70                    # one decade = 70 units, the axis starts at 10^3 W
    f.tex(x0, 18, r"P\ (\text{W})", "start", size=24, w=330)
    for k in range(0, 7):
        f.line(x0 + k * per, 44, x0 + k * per, 300, RULE_LIGHT, 1.5)
    rows = [("omakotitalon aurinkopaneelit", 5e3, "5\\,\\text{kW}"), ("tuulivoimala", 5e6, "5\\,\\text{MW}"),
            ("suuri vesivoimalaitos", 1e8, "100\\,\\text{MW}"), ("Olkiluoto 3", 1.6e9, "1600\\,\\text{MW}")]
    for i, (name, p, lab) in enumerate(rows):
        y = 44 + 64 * i
        x = x0 + (math.log10(p) - 3) * per
        f.tex(x0 + 4, y + 12, r"\text{" + name + "}", "start", size=24, w=300)
        f.circle(x, y + 40, 6.5, HEAT, WHITE, 2)
        f.tex(x + 14, y + 40, lab, "start", size=24, w=110)
    f.arrow(x0, 300, x0 + 6 * per + 40, 300, INK, 2.5, 13)
    f.line(x0, 42, x0, 302, INK, 2.5)
    for k in range(0, 7):
        if k: f.line(x0 + k * per, 300, x0 + k * per, 307, INK, 2)
        f.tex(x0 + k * per, 328, "10^{" + str(3 + k) + "}", "middle", MUTED, size=24, w=60)
    return f.svg()


FIGURES = {"hero": hero, "plants": plants, "fi-bars": fi_bars, "unit-power": unit_power}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "fi-bars": "safe: the 2024 production of each source printed at its bar (TWh); the total 79,9 TWh is only in the description, shares are not shown",
}
