"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy1-2` writes them into lesson.md."""
import math
from figlib import (Fig, INK, MUTED, WHITE, RULE, RULE_LIGHT, HEAT, HEAT_LIGHT, HOT, HOT_LIGHT, COLD, COLD_LIGHT, GOOD, GOOD_LIGHT,
                    ALUMINIUM, WATER, WATER_LIGHT, SAND, SAND_LIGHT, GRAIN, GLASS, n)
from figlib import SAND_DARK
import herolib as H


def hero():
    """The chapter's opening illustration: one distance from the Sun to Voyager 2, measured against three rulers of different steps."""
    f = H.hero("fy12-hero", "Kuvitus: avaruudessa Aurinko vasemmalla ja Voyager 2 -luotain oikealla, välissä katkoviiva. "
               "Viivan alla kolme samanpituista viivainta, joiden jakoviivat ovat eri tiheässä: sama matka kolmella eri yksiköllä.")
    H.space(f, seed=3, count=80)
    f.defs_add(f'<radialGradient id="fy12h-sun" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="{HEAT_LIGHT}"/><stop offset="0.6" stop-color="{HEAT}"/><stop offset="1" stop-color="{HEAT}" stop-opacity="0"/></radialGradient>')
    f.circle(90, 200, 150, "url(#fy12h-sun)")
    f.circle(90, 200, 62, HEAT_LIGHT)
    for r, (rr, c) in zip((150, 205, 290), ((6, WATER_LIGHT), (5, HOT_LIGHT), (12, SAND_DARK))):
        f.add(f'<path d="M{n(90 + r)},{n(200)} A{r},{r} 0 0 0 {n(90 + r * math.cos(-0.9))},{n(200 + r * math.sin(-0.9))}" fill="none" stroke="{MUTED}" stroke-width="1.5" stroke-dasharray="4 6"/>')
        f.circle(90 + r * math.cos(-0.5), 200 + r * math.sin(-0.5), rr, c)
    f.line(160, 200, 990, 200, WHITE, 3, dash="12 10")
    H.probe(f, 1030, 200, 0.85)
    for k, (y, step, c) in enumerate(((340, 17, COLD_LIGHT), (428, 85, HEAT_LIGHT), (516, 212.5, GOOD_LIGHT))):
        f.rect(160, y - 26, 850, 52, c, WHITE, 2.5, 6)
        f.line(160, y - 50, 160, y - 32, WHITE, 2); f.line(1010, y - 50, 1010, y - 32, WHITE, 2)
        x, i = 160.0, 0
        while x <= 1010.5:
            long_ = (i % 5 == 0) if k == 0 else True
            f.line(x, y - 26, x, y - 26 + (30 if long_ else 16), INK, 2.5 if long_ else 1.5)
            x += step; i += 1
    return f.svg()


def bracket(f, x0, x1, y, up=True, color=INK, w=2.5):
    """A square bracket under (up=True: the arms point up) or over a label, from x0 to x1."""
    d = -9 if up else 9
    f.path(f"M{n(x0)},{n(y + d)} V{n(y)} H{n(x1)} V{n(y + d)}", stroke=color, w=w)


def quantity():
    f = Fig("fy12-q", 322, "Kaavakuva: suureen arvo on lukuarvo kertaa yksikkö. Kynän pituutta mitataan viivaimella: kynän kärki on nollakohdassa "
            "ja päätyreuna 12,0 cm:n kohdalla, joten pituuden arvo on $l = 12{,}0\\,\\text{cm}$. Alla arvo on jaettu osiin: $l$ on suure, "
            "$12{,}0$ lukuarvo ja $\\text{cm}$ yksikkö. Viivain ja kynä on piirretty mittakaavassa, vaakasuunnassa 1 cm on 40 yksikköä.")
    f.defs_add(f'<linearGradient id="fy12-wood" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{SAND_LIGHT}"/><stop offset="1" stop-color="{SAND}"/></linearGradient>')
    f.defs_add(f'<linearGradient id="fy12-pencil" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{HEAT_LIGHT}"/><stop offset="1" stop-color="{HEAT}"/></linearGradient>')
    # pencil, 12,0 cm long: tip at the 0 mark, eraser end at 12 cm (40 units per cm)
    f.path("M60,46 L110,28 V64 Z", "url(#fy12-wood)", INK, 2.5)
    f.path("M60,46 L78,39.5 V52.5 Z", INK)
    f.rect(110, 28, 392, 36, "url(#fy12-pencil)", INK, 2.5)
    f.line(110, 46, 502, 46, HEAT, 2)
    f.rect(502, 28, 22, 36, ALUMINIUM, INK, 2.5)
    f.line(510, 28, 510, 64, MUTED, 1.5); f.line(516, 28, 516, 64, MUTED, 1.5)
    f.path("M524,28 H532 Q540,28 540,36 V56 Q540,64 532,64 H524 Z", HOT_LIGHT, INK, 2.5)
    f.line(60, 50, 60, 100, MUTED, 1.5, "5 4"); f.line(540, 50, 540, 100, MUTED, 1.5, "5 4")
    # ruler
    f.rect(40, 76, 520, 54, SAND_LIGHT, INK, 2.5, 4)
    for i in range(121):
        x = 60 + 4 * i
        f.line(x, 76, x, 76 + (22 if i % 10 == 0 else 14 if i % 5 == 0 else 8), INK, 2 if i % 10 == 0 else 1.5)
    for c in range(0, 13, 2):
        f.tex(60 + 40 * c, 116, str(c), "middle", w=34)
    # the value, split into its parts
    f.tex(168, 204, "l", "middle", size=36, w=40)
    f.tex(224, 204, "=", "middle", size=36, w=40)
    f.tex(312, 204, r"12{,}0", "middle", HEAT, size=36, w=110)
    f.tex(428, 204, r"\text{cm}", "middle", GOOD, size=36, w=90)
    bracket(f, 262, 474, 176, up=False, color=INK)
    f.tex(368, 152, r"\text{suureen arvo}", "middle", w=190)
    for x0, x1, tex, colour in ((152, 184, r"\text{suure}", INK), (258, 366, r"\text{lukuarvo}", HEAT), (394, 462, r"\text{yksikkö}", GOOD)):
        bracket(f, x0, x1, 240, up=True, color=colour)
    f.tex(168, 270, r"\text{suure}", "middle", w=100)
    f.tex(312, 270, r"\text{lukuarvo}", "middle", HEAT, w=120)
    f.tex(428, 270, r"\text{yksikkö}", "middle", GOOD, w=110)
    return f.svg()


def prefixes():
    f = Fig("fy12-p", 290, "Etuliitteet ovat kymmenpotenssien lyhenteitä. Kahdeksan laatikkoa kuvaa kerrointa nano $10^{-9}$, mikro $10^{-6}$, milli "
            "$10^{-3}$, ei etuliitettä $10^{0}$, kilo $10^{3}$, mega $10^{6}$, giga $10^{9}$ ja tera $10^{12}$. Nuolten välillä kerroin "
            "kasvaa joka askeleella tuhatkertaiseksi. Alimmalla rivillä etuliite on yhdistetty metriin.")
    cols = [(r"\text{n}", -9, "nano", r"\text{nm}"), (r"\text{µ}", -6, "mikro", r"\text{µm}"), (r"\text{m}", -3, "milli", r"\text{mm}"), ("1", 0, "", r"\text{m}"),
            (r"\text{k}", 3, "kilo", r"\text{km}"), (r"\text{M}", 6, "mega", r"\text{Mm}"), (r"\text{G}", 9, "giga", r"\text{Gm}"), (r"\text{T}", 12, "tera", r"\text{Tm}")]
    xs = [48 + 72 * i for i in range(8)]
    for i, (sym, e, name, unit) in enumerate(cols):
        x = xs[i]
        fill = COLD_LIGHT if e < 0 else WHITE if e == 0 else HEAT_LIGHT
        f.rect(x - 26, 54, 52, 58, fill, INK, 2.5, 8)
        f.tex(x, 84, sym, "middle", size=32, w=48)
        f.tex(x, 146, f"10^{{{e}}}", "middle", w=70)
        if name: f.tex(x, 184, rf"\text{{{name}}}", "middle", w=70)
        f.tex(x, 232, unit, "middle", w=60)
        if i < 7:
            f.arrow(x + 28, 83, xs[i + 1] - 28, 83, INK, 2.5, 9)
            f.tex((x + xs[i + 1]) / 2, 28, r"\cdot 10^{3}", "middle", MUTED, w=70)
    f.line(12, 208, 588, 208, RULE_LIGHT, 1.5)
    f.tex(300, 268, r"\text{yksi askel oikealle = tuhat kertaa suurempi}", "middle", w=560)
    return f.svg()


def conversion():
    f = Fig("fy12-c", 372, "Kaavakuva, ei mittakaavassa: sama etäisyys Auringosta Maahan voidaan ilmoittaa kolmella tavalla. Ylhäällä valonsäde kulkee "
            "Auringosta Maahan. Alla etäisyys $s$ on $1{,}496\\cdot10^{8}\\,\\text{km}$, joka on yksi astronominen yksikkö $1\\,\\text{AU}$ ja jonka "
            "valo kulkee 499 sekunnissa eli 8,32 minuutissa. Auringon ja Maan koot ja etäisyys eivät ole mittakaavassa.")
    f.defs_add(f'<radialGradient id="fy12-sun" cx="0.4" cy="0.4" r="0.7"><stop offset="0" stop-color="{HEAT_LIGHT}"/><stop offset="1" stop-color="{HEAT}"/></radialGradient>')
    f.defs_add(f'<radialGradient id="fy12-earth" cx="0.4" cy="0.35" r="0.75"><stop offset="0" stop-color="{WATER_LIGHT}"/><stop offset="1" stop-color="{WATER}"/></radialGradient>')
    f.defs_add(f'<linearGradient id="fy12-ray" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{HEAT_LIGHT}"/><stop offset="1" stop-color="{HEAT}"/></linearGradient>')
    for k in range(12):
        a = k * math.pi / 6 + math.pi / 12
        f.path(f"M{n(76 + math.cos(a) * 54 - math.sin(a) * 6)},{n(140 + math.sin(a) * 54 + math.cos(a) * 6)} L{n(76 + math.cos(a) * 72)},{n(140 + math.sin(a) * 72)} "
               f"L{n(76 + math.cos(a) * 54 + math.sin(a) * 6)},{n(140 + math.sin(a) * 54 - math.cos(a) * 6)} Z", HEAT_LIGHT)
    f.circle(76, 140, 46, "url(#fy12-sun)", INK, 2.5)
    f.circle(530, 140, 20, "url(#fy12-earth)", INK, 2.5)
    f.path("M134,130 H430 V118 L478,140 L430,162 V150 H134 Z", "url(#fy12-ray)")
    f.tex(76, 216, r"\text{Aurinko}", "middle", w=110)
    f.tex(530, 216, r"\text{Maa}", "middle", w=70)
    f.tex(300, 100, r"\text{valo}", "middle", HEAT, w=80)
    f.line(76, 190, 76, 206, INK, 2); f.line(530, 190, 530, 206, INK, 2)
    f.arrow(300, 198, 76, 198, INK, 2.5, 12); f.arrow(300, 198, 530, 198, INK, 2.5, 12)
    f.tex(300, 198, "s", "middle", bg=True, w=40)
    f.line(12, 244, 588, 244, RULE_LIGHT, 1.5)
    f.tex(300, 282, r"s = 1{,}496\cdot10^{8}\,\text{km}", "middle", w=330)
    f.tex(300, 322, r"= 1\,\text{AU}", "middle", w=140)
    f.tex(300, 356, r"= 499\,\text{s} = 8{,}32\,\text{min}\ \text{(valon kulkuaika)}", "middle", w=530)
    return f.svg()


def ruler_read():
    """A task-only picture: a rod beside a ruler, its left end NOT at zero, so the length is a difference of two readings."""
    f = Fig("fy12-ruler", 190, "Kuva mittakaavassa: alumiinitanko viivaimen vieressä. Viivain näyttää 0 cm – 15 cm, numerot joka senttimetrin kohdalla ja "
            "pienet viivat joka millimetrin kohdalla. Tangon vasen pää on kohdassa 2,0 cm ja oikea pää kohdassa 13,6 cm; tanko ei siis ala nollakohdasta.")
    x0, u = 28, 36                                    # 36 units per cm
    X = lambda c: x0 + u * c
    f.rect(X(2.0), 24, X(13.6) - X(2.0), 36, ALUMINIUM, INK, 2.5)
    f.line(X(2.0) + 8, 30, X(13.6) - 8, 30, WHITE, 3)
    f.line(X(2.0), 62, X(2.0), 90, MUTED, 1.5, "5 4"); f.line(X(13.6), 62, X(13.6), 90, MUTED, 1.5, "5 4")
    f.rect(x0 - 12, 64, 15 * u + 24, 58, SAND_LIGHT, INK, 2.5, 4)
    for i in range(151):
        c = i / 10
        f.line(X(c), 64, X(c), 64 + (24 if i % 10 == 0 else 16 if i % 5 == 0 else 9), INK, 2 if i % 10 == 0 else 1.5)
    for c in range(0, 16):
        f.tex(X(c), 108, str(c), "middle", w=34)
    f.tex(X(15) + 4, 160, r"\text{cm}", "end", MUTED, w=50)
    return f.svg()


FIGURES = {"hero": hero, "quantity": quantity, "prefixes": prefixes, "conversion": conversion, "ruler-read": ruler_read}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "quantity": "reveals: the reading l = 12,0 cm",
    "prefixes": "reveals: every prefix's power of ten",
    "conversion": "reveals: 1 AU = 1,496·10^8 km and the light time 499 s",
    "ruler-read": "safe: a rod beside a ruler, both ends to be read (quantity is the lesson figure)",
}
