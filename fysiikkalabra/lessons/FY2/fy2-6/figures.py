"""Figures of fy2-6 (scripts/figlib.py); `python scripts/figures.py fy2-6` writes them into lesson.md."""
import math
from figlib import (Fig, INK, MUTED, WHITE, RULE, RULE_LIGHT, HEAT, HEAT_LIGHT, GLASS, WATER, WATER_LIGHT, n)


def plants():
    f = Fig("fy26-pl", 330, "Kaavakuva: viisi tapaa tuottaa sähköä. Putoava vesi pyörittää turbiinia, tuuli roottoria, auringonsäteily "
            "osuu aurinkopaneeliin, ydinpolttoaineen energia lämmittää höyryn höyryturbiinille ja polttoaineen kemiallinen energia "
            "lämmittää höyryn höyryturbiinille. Jokaisesta laitoksesta lähtee nuoli sähköverkkoon. Kuva on kaavamainen, nuolten "
            "pituus ei kuvaa tehoa.")
    f.defs_add(f'<linearGradient id="fy26-heat" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{HEAT_LIGHT}"/><stop offset="1" stop-color="{HEAT}"/></linearGradient>')
    rows = [("putoava vesi", "turbiini"), ("tuuli", "roottori"), ("säteily", "paneeli"),
            ("ydinpolttoaine", "höyryturbiini"), ("polttoaine", "höyryturbiini")]
    f.rect(468, 18, 116, 294, GLASS, INK, 3, 10)
    f.tex(526, 165, r"\text{sähkö}", "middle", size=24, w=108)
    for i, (src, dev) in enumerate(rows):
        y = 18 + 60 * i
        f.rect(16, y, 196, 54, WHITE, INK, 2.5, 10)
        f.tex(114, y + 27, r"\text{" + src + "}", "middle", size=24, w=188)
        f.block_arrow(214, y + 27, 250, y + 27, "url(#fy26-heat)", 12, 26, 18)
        f.rect(252, y, 176, 54, GLASS, INK, 2.5, 10)
        f.tex(340, y + 27, r"\text{" + dev + "}", "middle", size=24, w=168)
        f.block_arrow(430, y + 27, 466, y + 27, "url(#fy26-heat)", 12, 26, 18)
    return f.svg()


def fi_bars():
    f = Fig("fy26-fi", 330, "Vaakapylväskaavio Suomen sähköntuotannosta vuonna 2024 energialähteittäin teravattitunteina (Tilastokeskus), "
            "mittakaavassa: ydinvoima 31, tuulivoima 20,2, vesivoima 14,1, bioperäiset polttoaineet 9,5, fossiiliset polttoaineet ja "
            "turve 3,4 ja aurinkosähkö 0,9. Ydinvoiman pylväs on noin kolmannes kokonaistuotannosta 79,9.")
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
    f = Fig("fy26-up", 372, "Vaakapylväskaavio yksittäisten voimalaitosten tehoista logaritmisella asteikolla, jossa jokainen ruutu on "
            "kymmenkertainen: omakotitalon aurinkopaneelit noin 5 kW, tuulivoimala noin 5 MW, suuri vesivoimalaitos noin 100 MW "
            "ja Olkiluoto 3 noin 1600 MW. Pylväiden pituudet ovat tehon logaritmin mukaiset, joten Olkiluoto 3 on noin 320 kertaa "
            "tuulivoimalaa suurempi, vaikka pylväs on vain vähän pidempi.")
    x0, per = 40, 70                    # one decade = 70 units, the axis starts at 10^3 W
    f.tex(x0, 18, r"P\ (\text{W})", "start", size=24, w=330)
    for k in range(0, 7):
        f.line(x0 + k * per, 44, x0 + k * per, 300, RULE_LIGHT, 1.5)
    rows = [("omakotitalon aurinkopaneelit", 5e3, "5\\,\\text{kW}"), ("tuulivoimala", 5e6, "5\\,\\text{MW}"),
            ("suuri vesivoimalaitos", 1e8, "100\\,\\text{MW}"), ("Olkiluoto 3", 1.6e9, "1600\\,\\text{MW}")]
    for i, (name, p, lab) in enumerate(rows):
        y = 44 + 64 * i
        w = (math.log10(p) - 3) * per
        f.tex(x0 + 4, y + 12, r"\text{" + name + "}", "start", size=24, w=300)
        f.rect(x0, y + 28, w, 24, HEAT_LIGHT, HEAT, 1.5, 3)
        f.tex(x0 + w + 8, y + 40, lab, "start", size=24, w=110)
    f.arrow(x0, 300, x0 + 6 * per + 40, 300, INK, 2.5, 13)
    f.line(x0, 42, x0, 302, INK, 2.5)
    for k in range(0, 7):
        if k: f.line(x0 + k * per, 300, x0 + k * per, 307, INK, 2)
        f.tex(x0 + k * per, 328, "10^{" + str(3 + k) + "}", "middle", MUTED, size=24, w=60)
    return f.svg()


FIGURES = {"plants": plants, "fi-bars": fi_bars, "unit-power": unit_power}
