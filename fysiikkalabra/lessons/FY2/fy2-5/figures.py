"""Figures of fy2-5 (scripts/figlib.py); `python scripts/figures.py fy2-5` writes them into lesson.md."""
from figlib import (Fig, INK, MUTED, WHITE, RULE, RULE_LIGHT, HEAT, HEAT_LIGHT, HOT, SAND, SAND_LIGHT, GRAIN, GLASS, GOOD, n)
from figlib import ALUMINIUM, COPPER, GOOD_LIGHT, HOT_LIGHT, METAL_EDGE, PAPER, SAND_DARK
import herolib as H


def hero():
    """The chapter's opening illustration: a kilogram of petrol and a kilogram of firewood on equal scales, the petrol's flame much larger."""
    f = H.hero("fy25-hero", "Kuvitus: kaksi samanlaista vaakaa, joiden lukemat ovat samat. Vasemmalla vaa'alla bensiinikanisteri, oikealla "
               "halkoja. Kummankin yläpuolella liekki: bensiinin liekki on selvästi suurempi.")
    f.rect(0, 0, 1200, 600, PAPER)
    f.rect(0, 470, 1200, 130, SAND, None); f.line(0, 470, 1200, 470, GRAIN, 3)
    def flame(cx, base, sc):
        f.path(f"M{n(cx - 60 * sc)},{base} Q{n(cx - 80 * sc)},{n(base - 90 * sc)} {n(cx - 10 * sc)},{n(base - 190 * sc)} Q{n(cx)},{n(base - 110 * sc)} {n(cx + 30 * sc)},{n(base - 120 * sc)} "
               f"Q{n(cx + 84 * sc)},{n(base - 60 * sc)} {n(cx + 60 * sc)},{base} Z", HEAT, INK, 2)
        f.path(f"M{n(cx - 30 * sc)},{base} Q{n(cx - 40 * sc)},{n(base - 50 * sc)} {n(cx)},{n(base - 104 * sc)} Q{n(cx + 40 * sc)},{n(base - 40 * sc)} {n(cx + 30 * sc)},{base} Z", HEAT_LIGHT)
    for cx in (340, 860):
        f.rect(cx - 150, 430, 300, 40, ALUMINIUM, INK, 3, 8)
        f.rect(cx - 170, 416, 340, 16, METAL_EDGE, INK, 2, 4)
        f.rect(cx - 40, 438, 80, 24, INK, None, 0, 4)
        for k in range(3): f.rect(cx - 32 + 22 * k, 442, 18, 16, GOOD_LIGHT, None, 0, 2)
    # petrol can
    cx = 340
    f.path(f"M{cx - 90},416 V250 L{cx - 50},210 H{cx + 90} V416 Z", HOT, INK, 3)
    f.rect(cx - 10, 214, 70, 20, INK, None, 0, 6)
    f.path(f"M{cx - 76},250 L{cx - 106},196 L{cx - 86},188 L{cx - 58},236", ALUMINIUM, INK, 3)
    f.path(f"M{cx - 60},300 L{cx + 60},390 M{cx + 60},300 L{cx - 60},390", stroke=HOT_LIGHT, w=8)
    flame(cx, 170, 0.95)
    # firewood
    cx = 860
    for k, (dx, dy) in enumerate(((-70, 0), (0, 0), (70, 0), (-35, -56), (35, -56), (0, -112))):
        f.add(f'<ellipse cx="{cx + dx - 70}" cy="{386 + dy}" rx="16" ry="28" fill="{SAND_DARK}" stroke="{INK}" stroke-width="2"/>')
        f.rect(cx + dx - 70, 358 + dy, 140, 56, COPPER, INK, 3)
        f.add(f'<ellipse cx="{cx + dx + 70}" cy="{386 + dy}" rx="16" ry="28" fill="{SAND_LIGHT}" stroke="{INK}" stroke-width="3"/>')
        f.add(f'<ellipse cx="{cx + dx + 70}" cy="{386 + dy}" rx="7" ry="13" fill="none" stroke="{GRAIN}" stroke-width="2"/>')
    flame(cx, 230, 0.5)
    return f.svg()


def defs(f):
    f.defs_add(f'<linearGradient id="fy25-heat" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{HEAT_LIGHT}"/><stop offset="1" stop-color="{HEAT}"/></linearGradient>')
    f.defs_add(f'<linearGradient id="fy25-heatv" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{HEAT_LIGHT}"/><stop offset="1" stop-color="{HEAT}"/></linearGradient>')


def log(f, x, y, w=150, h=40):
    """A log seen from the side with its end grain at the left."""
    f.rect(x, y, w, h, SAND, INK, 2.5, h / 2)
    f.add(f'<ellipse cx="{n(x + h / 2)}" cy="{n(y + h / 2)}" rx="{n(h / 2 - 4)}" ry="{n(h / 2 - 4)}" fill="{SAND_LIGHT}" stroke="{GRAIN}" stroke-width="2"/>')
    f.circle(x + h / 2, y + h / 2, 6, "none", GRAIN, 1.5)


def flame(f, cx, base, h=120, w=84):
    top = base - h
    f.path(f"M{n(cx)},{n(top)} C{n(cx + w * 0.15)},{n(top + h * 0.3)} {n(cx + w / 2)},{n(base - h * 0.45)} {n(cx + w / 2)},{n(base - h * 0.2)} "
           f"C{n(cx + w / 2)},{n(base + 6)} {n(cx - w / 2)},{n(base + 6)} {n(cx - w / 2)},{n(base - h * 0.2)} "
           f"C{n(cx - w / 2)},{n(base - h * 0.45)} {n(cx - w * 0.1)},{n(top + h * 0.35)} {n(cx)},{n(top)} Z", HEAT, INK, 2.5)
    iw, ih = w * 0.5, h * 0.5
    f.path(f"M{n(cx)},{n(base - ih)} C{n(cx + iw * 0.2)},{n(base - ih * 0.65)} {n(cx + iw / 2)},{n(base - ih * 0.45)} {n(cx + iw / 2)},{n(base - ih * 0.15)} "
           f"C{n(cx + iw / 2)},{n(base)} {n(cx - iw / 2)},{n(base)} {n(cx - iw / 2)},{n(base - ih * 0.15)} "
           f"C{n(cx - iw / 2)},{n(base - ih * 0.45)} {n(cx - iw * 0.2)},{n(base - ih * 0.65)} {n(cx)},{n(base - ih)} Z", HEAT_LIGHT)


def energia():
    f = Fig("fy25-ener", 330, "Periaatekuva, ei mittakaavassa: kasa polttopuuta sisältää kemiallista energiaa. Palaessaan puu muuttuu "
            "liekiksi, jossa kemiallinen energia vapautuu lämpönä ja valona. Vapautuva energia saadaan kertomalla polttoaineen massa "
            "lämpöarvolla.")
    defs(f)
    # logs: two below, one on top
    log(f, 28, 188, 150, 40)
    log(f, 28, 144, 150, 40)
    log(f, 28, 100, 150, 40)
    f.tex(103, 262, r"\text{kemiallinen}", "middle", w=190)
    f.tex(103, 292, r"\text{energia}", "middle", w=190)
    # arrow
    f.block_arrow(214, 190, 372, 190, "url(#fy25-heat)", 22, 46, 34)
    f.tex(293, 136, r"\text{palaminen}", "middle", w=170)
    f.tex(293, 244, r"E = Hm", "middle", w=110)
    # flame on a hearth
    flame(f, 484, 232, 130, 90)
    f.rect(420, 238, 128, 10, INK, None, 0, 3)
    f.tex(484, 276, r"\text{lämpö ja valo}", "middle", w=200)
    return f.svg()


def lampoarvot():
    f = Fig("fy25-bars", 372, "Vaakapylväskaavio polttoaineiden lämpöarvoista yksikössä MJ/kg, pyöristettyjä arvoja: maakaasu 48, bensiini 43, "
            "diesel 43, kivihiili 26, puupelletti 17, polttopuu (ilmakuiva) 15 ja turve 10. Pylväiden pituudet ovat mittakaavassa: maakaasun pylväs on "
            "noin viisi kertaa turpeen pylvään pituinen.")
    defs(f)
    f.tex(150, 24, r"H\ \left(\text{MJ/kg}\right)", "start", w=190)
    x0, per = 156, 6.8
    top, step, bh = 52, 38, 26
    rows = [("maakaasu", 48), ("bensiini", 43), ("diesel", 43), ("kivihiili", 26), ("puupelletti", 17), ("polttopuu", 15), ("turve", 10)]
    ybase = top + step * len(rows) + 2
    for t in (10, 20, 30, 40, 50):
        f.line(x0 + t * per, top - 4, x0 + t * per, ybase, RULE_LIGHT, 1.5)
    for i, (name, h) in enumerate(rows):
        y = top + step * i
        f.rect(x0, y, h * per, bh, "url(#fy25-heat)", INK, 1.5, 3)
        f.tex(x0 - 12, y + bh / 2, r"\text{" + name + "}", "end", w=140)
        f.tex(x0 + h * per + 10, y + bh / 2, str(h), "start", w=44)
    f.arrow(x0, ybase, x0 + 50 * per + 30, ybase, INK, 2.5, 13)
    f.line(x0, top - 8, x0, ybase + 2, INK, 2.5)
    for t in (10, 20, 30, 40, 50):
        f.line(x0 + t * per, ybase, x0 + t * per, ybase + 7, INK, 2)
        f.tex(x0 + t * per, ybase + 26, str(t), "middle", MUTED, w=40)
    f.tex(x0 - 10, ybase + 22, "0", "end", MUTED, w=30)
    return f.svg()


def etiketti():
    f = Fig("fy25-label", 300, "Periaatekuva ravintoarvomerkinnästä, esimerkki eikä todellinen tuote: pakkauksessa lukee energia 2200 kJ sadassa "
            "grammassa. Kun energia muutetaan megajouleiksi ja massa kilogrammoiksi, saadaan ruoan energiasisältö 22 MJ/kg.")
    defs(f)
    f.rect(30, 30, 230, 220, WHITE, INK, 2.5, 8)
    f.tex(145, 66, r"\text{Ravintoarvo}", "middle", w=200)
    f.line(46, 92, 244, 92, INK, 2.5)
    f.tex(145, 124, r"\text{sadassa grammassa}", "middle", MUTED, w=210)
    f.line(46, 152, 244, 152, RULE, 1.5)
    f.tex(46, 188, r"\text{energia}", "start", w=96)
    f.tex(244, 188, r"2200\,\text{kJ}", "end", w=94)
    f.line(46, 214, 244, 214, RULE, 1.5)
    f.tex(145, 232, r"\text{esimerkki}", "middle", MUTED, w=130)
    f.block_arrow(280, 140, 340, 140, "url(#fy25-heat)", 14, 30, 22)
    f.tex(350, 96, r"2200\,\text{kJ} = 2{,}2\,\text{MJ}", "start", w=230)
    f.tex(350, 140, r"100\,\text{g} = 0{,}100\,\text{kg}", "start", w=230)
    f.tex(350, 204, r"e = 22\,\dfrac{\text{MJ}}{\text{kg}}", "start", GOOD, w=200)
    return f.svg()


FIGURES = {"hero": hero, "energia": energia, "lampoarvot": lampoarvot, "etiketti": etiketti}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "lampoarvot": "safe: rounded heating values of seven fuels printed at the bars (MJ/kg); a task computes E = Hm or compares fuels from them",
}
