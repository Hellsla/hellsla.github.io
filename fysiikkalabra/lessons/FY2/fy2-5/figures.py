"""Figures of fy2-5 (scripts/figlib.py); `python scripts/figures.py fy2-5` writes them into lesson.md."""
from figlib import (Fig, INK, MUTED, WHITE, RULE, RULE_LIGHT, HEAT, HEAT_LIGHT, HOT, SAND, SAND_LIGHT, GRAIN, GLASS, GOOD, n)
from figlib import ALUMINIUM, COPPER, GOOD_LIGHT, HOT_LIGHT, METAL_EDGE, PAPER, SAND_DARK
import herolib as H
from herolib import grad, steel


def hero():
    """The chapter's opening illustration: a kilogram of petrol and a kilogram of firewood on equal scales, each beside its own fire; the petrol's fire is far larger."""
    f = H.hero("fy25-hero", "Kuvitus: kaksi samanlaista vaakaa, joiden lukemat ovat samat. Vasemmalla vaa'alla bensiinikanisteri, oikealla halkoja. "
               "Kummankin takana palaa tulisijassa sama aine: bensiinin liekki on selvästi suurempi kuin puun.")
    H.tiles(f, 440, 80, RULE_LIGHT, PAPER)
    f.rect(0, 440, 1200, 26, RULE, INK, 3); f.rect(0, 466, 1200, 134, RULE_LIGHT)
    for x in (400, 800): f.line(x, 466, x, 600, INK, 2)
    def fire(cx, base, sc, gid):
        """A steel fire bowl on legs with a flame of size sc."""
        f.circle(cx, base - 90 * sc, 150 * sc, H.glow(f, gid + "g", HEAT_LIGHT, HEAT))
        f.path(f"M{n(cx - 70 * sc)},{base} Q{n(cx - 100 * sc)},{n(base - 110 * sc)} {n(cx - 14 * sc)},{n(base - 230 * sc)} Q{n(cx - 4 * sc)},{n(base - 130 * sc)} {n(cx + 34 * sc)},{n(base - 150 * sc)} "
               f"Q{n(cx + 100 * sc)},{n(base - 70 * sc)} {n(cx + 70 * sc)},{base} Z", grad(f, gid, HEAT_LIGHT, HEAT), INK, 2)
        f.path(f"M{n(cx - 34 * sc)},{base} Q{n(cx - 46 * sc)},{n(base - 60 * sc)} {n(cx)},{n(base - 126 * sc)} Q{n(cx + 46 * sc)},{n(base - 50 * sc)} {n(cx + 34 * sc)},{base} Z", HEAT_LIGHT)
        f.path(f"M{cx - 80},{base - 6} Q{cx},{base + 40} {cx + 80},{base - 6} Z", steel(f, gid + "s"), INK, 3)
        for dx in (-50, 50): f.line(cx + dx, base + 14, cx + dx * 1.3, base + 54, INK, 4)
    fire(300, 250, 1.0, "fy25h-f1"); fire(900, 250, 0.45, "fy25h-f2")
    for cx in (300, 900):
        f.rect(cx - 160, 410, 320, 30, steel(f, f"fy25h-sc{cx}", vertical=True), INK, 3, 8)
        f.rect(cx - 180, 396, 360, 16, METAL_EDGE, INK, 2, 4)
        f.rect(cx - 44, 416, 88, 20, INK, None, 0, 4)
        for k in range(3): f.rect(cx - 36 + 25 * k, 419, 20, 14, GOOD_LIGHT, None, 0, 2)
    # petrol can: red steel with an X-pressing, a spout and a handle
    cx = 300
    f.path(f"M{cx - 96},396 V270 L{cx - 56},232 H{cx + 96} V396 Z", grad(f, "fy25h-can", HOT_LIGHT, HOT, horizontal=True), INK, 3)
    f.rect(cx - 10, 238, 80, 22, INK, None, 0, 8)
    f.path(f"M{cx - 82},270 L{cx - 114},214 L{cx - 92},204 L{cx - 62},256", grad(f, "fy25h-spout", ALUMINIUM, METAL_EDGE), INK, 3)
    f.path(f"M{cx - 66},300 L{cx + 66},380 M{cx + 66},300 L{cx - 66},380", stroke=HOT_LIGHT, w=10, extra='stroke-linecap="round"')
    f.path(f"M{cx - 70},288 H{cx + 70} V388 H{cx - 70} Z", stroke=INK, w=2, extra='fill="none" stroke-opacity="0.4"')
    # firewood: split birch logs with bark and end grain
    cx = 900
    for k, (dx, dy) in enumerate(((-72, 0), (0, 0), (72, 0), (-36, -60), (36, -60), (0, -120))):
        y = 366 + dy
        f.add(f'<ellipse cx="{cx + dx - 74}" cy="{y}" rx="16" ry="30" fill="{SAND_DARK}" stroke="{INK}" stroke-width="2"/>')
        f.rect(cx + dx - 74, y - 30, 148, 60, WHITE, INK, 3)
        for j in range(4): f.rect(cx + dx - 60 + 34 * j, y - 30 + (j % 2) * 30, 18, 6, INK)
        f.add(f'<ellipse cx="{cx + dx + 74}" cy="{y}" rx="16" ry="30" fill="{SAND_LIGHT}" stroke="{INK}" stroke-width="3"/>')
        f.add(f'<ellipse cx="{cx + dx + 74}" cy="{y}" rx="8" ry="15" fill="none" stroke="{GRAIN}" stroke-width="2"/>')
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
