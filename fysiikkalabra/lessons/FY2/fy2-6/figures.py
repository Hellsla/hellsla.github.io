"""Figures of fy2-6 (scripts/figlib.py); `python scripts/figures.py fy2-6` writes them into lesson.md."""
import math
from figlib import (Fig, INK, MUTED, WHITE, RULE, RULE_LIGHT, HEAT, HEAT_LIGHT, GLASS, WATER, WATER_LIGHT, n)
from figlib import ALUMINIUM, COLD_LIGHT, GOOD, GOOD_LIGHT, HOT_LIGHT, IRON, SAND_DARK, SAND_LIGHT
import herolib as H
from figlib import METAL_EDGE
from herolib import grad, steel


def hero():
    """The chapter's opening illustration: a nuclear plant, a hydro plant, wind turbines and a combined heat and power plant feed one grid to a town."""
    f = H.hero("fy26-hero", "Kuvitus: suomalainen maisema, jossa on ydinvoimala meren rannalla, vesivoimala joen padolla, tuulivoimaloita ja "
               "savupiipullinen polttoainevoimala. Kaikista lähtevät voimalinjat samaan verkkoon, joka vie sähkön kaupunkiin.")
    H.sky(f, "fy26h", 360); H.cloud(f, 300, 70, 0.7); H.cloud(f, 760, 50, 0.6)
    H.hills(f, "fy26h", 250, [ALUMINIUM, METAL_EDGE], amp=34, seed=6)
    H.forest(f, 320, 40, 24, GOOD, seed=7, depth=20)
    f.rect(0, 336, 1200, 264, grad(f, "fy26h-land", GOOD_LIGHT, SAND_LIGHT, y1=336, y2=600))
    # the sea on the left, a nuclear plant on its shore
    f.path("M0,380 Q140,372 300,392 Q250,480 260,600 H0 Z", grad(f, "fy26h-sea", WATER_LIGHT, WATER))
    for x, y in ((40, 420), (120, 470), (60, 530)): f.path(f"M{x},{y} q20,-6 40,0 t40,0", stroke=WHITE, w=3, extra='stroke-opacity="0.7"')
    f.rect(30, 300, 130, 80, steel(f, "fy26h-turb"), INK, 3)
    for k in range(4): f.rect(42 + k * 30, 316, 18, 20, GLASS, INK, 1.5)
    f.path("M150,380 V290 Q190,228 230,290 V380 Z", grad(f, "fy26h-dome", WHITE, ALUMINIUM, horizontal=True), INK, 3)
    f.rect(80, 262, 16, 40, IRON, INK, 2)
    # hydro plant: reservoir, a concrete dam across the river, the power house below it
    f.add(f'<path d="M330,346 Q420,330 520,346 L500,372 H350 Z" fill="{grad(f, "fy26h-res", WATER_LIGHT, WATER)}" stroke="{WATER}" stroke-width="2"/>')
    f.path("M340,372 H510 L520,410 H330 Z", grad(f, "fy26h-dam", RULE_LIGHT, RULE), INK, 3)
    f.rect(380, 410, 90, 44, SAND_LIGHT, INK, 3); f.path("M374,410 H476 L462,396 H388 Z", IRON, INK, 2)
    for k in range(3): f.rect(390 + k * 26, 420, 16, 22, GLASS, INK, 1.5)
    f.path("M400,454 Q370,520 330,600 H470 Q450,520 460,454 Z", grad(f, "fy26h-riv", WATER_LIGHT, WATER))
    # wind turbines on the ridge
    for k, (x, h) in enumerate(((610, 230), (700, 190), (790, 214))): H.wind_turbine(f, x, 380, h, 0.4 + 1.3 * k, 0.95)
    # CHP plant: boiler house, a striped chimney, a light plume
    f.rect(850, 300, 140, 90, grad(f, "fy26h-chp", SAND_LIGHT, SAND_DARK), INK, 3)
    for k in range(3): f.rect(866 + k * 40, 324, 26, 34, GLASS, INK, 1.5)
    f.rect(960, 150, 30, 150, WHITE, INK, 3)
    for k in range(3): f.rect(960, 166 + k * 44, 30, 12, HOT_LIGHT, INK, 1.5)
    H.smoke(f, 976, 132, 0.8, RULE, 0.8)
    # town
    for k, (x, w, h, c) in enumerate(((1030, 54, 140, COLD_LIGHT), (1086, 44, 180, SAND_LIGHT), (1132, 64, 110, HOT_LIGHT))):
        f.rect(x, 390 - h, w, h, c, INK, 3)
        for j in range(int(h / 34)):
            for i in range(int((w - 10) / 18)): f.rect(x + 7 + i * 18, 390 - h + 12 + j * 32, 11, 14, GLASS, INK, 1)
    # one grid joining them
    pts = [(250, 540), (560, 530), (840, 540), (1060, 530)]
    arms = [H.pylon(f, x, y, 120, 0.75) for x, y in pts]
    for a, b in zip(arms, arms[1:]):
        for p, q in zip(a, b): H.wire(f, p, q, 14, INK, 1.5)
    for a, b in ((arms[0][2], (200, 330)), (arms[1][2], (476, 430)), (arms[1][3], (700, 390)), (arms[2][3], (920, 390)), (arms[3][3], (1090, 390))): H.wire(f, a, b, 6, INK, 1.5)
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
