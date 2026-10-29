"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy2-7` writes them into lesson.md."""
from figlib import (Fig, INK, MUTED, RULE, RULE_LIGHT, WHITE, GLASS, COLD, COLD_LIGHT, HEAT, HEAT_LIGHT, HOT, HOT_LIGHT, ALUMINIUM,
                    METAL_EDGE, IRON, GOOD, GOOD_LIGHT, WATER, WATER_LIGHT, SAND, SAND_LIGHT, n)
from figlib import GRAIN
import herolib as H


def hero():
    """The chapter's opening illustration: a high-voltage line across the land and, in a cut through the ground, a thickly insulated district heating pipe to a house."""
    f = H.hero("fy27-hero", "Kuvitus: maisemassa korkeat voimalinjapylväät, joiden johdot kulkevat kauas. Etualalla maan läpi leikattu näkymä: "
               "kaukolämpöputket, joiden ympärillä on paksu eristekerros, vievät lämpöä talolle.")
    H.sky(f, "fy27h", 400); H.cloud(f, 220, 70, 0.6)
    H.forest(f, 300, 40, 28, GOOD, seed=8)
    f.rect(0, 310, 1200, 110, GOOD_LIGHT)
    pts = [(80, 400, 230, 0.95), (420, 360, 180, 0.75), (680, 335, 140, 0.58), (860, 320, 110, 0.45)]
    arms = [H.pylon(f, x, y, h, s) for x, y, h, s in pts]
    for a, b in zip(arms, arms[1:]):
        for p, q in zip(a, b): H.wire(f, p, q, 26, INK, 2)
    H.house(f, 960, 420, 170, 110, SAND_LIGHT, HOT)
    # the ground cut open: soil, a pipe pair in thick insulation running to the house
    f.rect(0, 420, 1200, 180, SAND, None)
    for k in range(40): f.circle(H.rnd(k, 3) * 1200, 440 + H.rnd(k, 9) * 150, 2 + 2 * H.rnd(k, 5), GRAIN)
    f.line(0, 420, 1200, 420, INK, 3)
    f.rect(0, 476, 860, 88, WHITE, INK, 3, 0)
    f.rect(0, 486, 860, 68, SAND_LIGHT, None)
    f.rect(0, 497, 860, 14, HOT, INK, 2); f.rect(0, 529, 860, 14, COLD, INK, 2)
    f.path("M860,476 H1020 V420", stroke=INK, w=3)
    f.rect(980, 420, 50, 144, SAND_LIGHT, INK, 3)
    f.rect(988, 420, 12, 144, HOT, INK, 2); f.rect(1010, 420, 12, 144, COLD, INK, 2)
    f.rect(860, 476, 120, 88, SAND_LIGHT, INK, 3)
    f.rect(860, 497, 128, 14, HOT, INK, 2); f.rect(860, 529, 150, 14, COLD, INK, 2)
    return f.svg()


def wire(f, x1, y1, x2, y2, sag=10, w=2):
    """A sagging power line between two points (a quadratic curve)."""
    return f.path(f"M{n(x1)},{n(y1)} Q{n((x1 + x2) / 2)},{n((y1 + y2) / 2 + 2 * sag)} {n(x2)},{n(y2)}", stroke=INK, w=w)


def pylon(f, cx, base=206, top=112):
    """A lattice tower with two cross arms."""
    f.path(f"M{n(cx - 20)},{base} L{n(cx - 5)},{top} L{n(cx + 5)},{top} L{n(cx + 20)},{base}", stroke=INK, w=2.5)
    for y, hw in ((172, 14), (140, 10)):
        f.line(cx - hw, y, cx + hw, y, INK, 1.5)
    f.line(cx - 13, 172, cx + 10, 140, INK, 1.5); f.line(cx + 13, 172, cx - 10, 140, INK, 1.5)
    f.line(cx - 30, 124, cx + 30, 124, INK, 3)
    for dx in (-26, 26):
        f.line(cx + dx, 124, cx + dx, 132, INK, 2.5)


def grid():
    f = Fig("fy27-grid", 332, "Kaavakuva sähköverkon reitistä voimalaitokselta kotiin. Vasemmalta oikealle: voimalaitos ja sen muuntaja, kantaverkon "
            "voimalinja (jännite 110 kV:sta 400 kV:iin), sähköasema, jakeluverkon pylväät (20 kV) ja koti (0,4 kV, pistorasiassa 230 V). "
            "Alla oranssi nuoli kuvaa energian kulkua voimalaitokselta kotiin. Kuva ei ole mittakaavassa.")
    g = 206
    f.line(12, g, 588, g, MUTED, 2)
    # power plant with chimney and smoke
    f.rect(30, 150, 76, 56, ALUMINIUM, INK, 2.5)
    f.rect(44, 96, 16, 54, IRON, INK, 2.5)
    f.add(f'<ellipse cx="58" cy="82" rx="14" ry="9" fill="{GLASS}" stroke="{RULE}" stroke-width="1.5"/>'
          f'<ellipse cx="72" cy="66" rx="12" ry="8" fill="{GLASS}" stroke="{RULE}" stroke-width="1.5"/>')
    f.rect(76, 166, 18, 22, WHITE, INK, 2)
    # step-up transformer: a box with two coils
    f.rect(118, 172, 34, 34, IRON, INK, 2.5)
    f.circle(130, 189, 8, "none", WHITE, 2); f.circle(141, 189, 8, "none", WHITE, 2)
    wire(f, 106, 160, 164, 124, 4)
    wire(f, 152, 178, 164, 124, 2)
    # transmission line, two pylons
    pylon(f, 190); pylon(f, 300)
    wire(f, 164, 124, 270, 124, 14); wire(f, 216, 124, 274, 124, 10); wire(f, 326, 124, 372, 150, 10)
    wire(f, 190, 124, 270, 124, 12, 1.5)
    # substation: fence and transformer
    f.rect(372, 164, 54, 42, GLASS, INK, 2.5)
    f.rect(382, 176, 18, 30, IRON, INK, 2); f.rect(406, 176, 14, 30, ALUMINIUM, INK, 2)
    f.line(396, 164, 396, 150, INK, 2.5); f.line(380, 150, 412, 150, INK, 3)
    # distribution poles
    for px in (452, 500):
        f.line(px, 206, px, 142, INK, 4); f.line(px - 14, 150, px + 14, 150, INK, 3)
    wire(f, 412, 150, 452, 150, 6); wire(f, 452, 150, 500, 150, 8); wire(f, 500, 150, 538, 168, 4)
    # house
    f.rect(528, 172, 54, 34, SAND_LIGHT, INK, 2.5)
    f.path("M520,174 L555,142 L590,174 Z", HOT_LIGHT, INK, 2.5)
    f.rect(536, 182, 14, 24, WHITE, INK, 2); f.rect(558, 182, 16, 14, GLASS, INK, 2)
    # voltage labels above
    f.tex(245, 62, r"110\text{–}400\,\text{kV}", "middle", w=170)
    f.tex(476, 116, r"20\,\text{kV}", "middle", w=100)
    f.tex(556, 62, r"0{,}4\,\text{kV}", "middle", w=100)
    f.tex(130, 100.5, r"\text{muuntaja}", "middle", w=90)
    f.line(130, 118, 130, 171, MUTED, 1.5, "4 4")
    f.line(556, 82, 556, 130, RULE, 1.5, "5 5")
    # names below
    f.tex(88, 262, r"\text{voimalaitos}", "middle", w=140)
    f.tex(250, 262, r"\text{kantaverkko}", "middle", w=150)
    f.tex(400, 296, r"\text{sähköasema}", "middle", w=150)
    f.tex(520, 262, r"\text{jakeluverkko}", "middle", w=140)
    # the energy flow underneath, to scale of nothing: a schematic arrow
    f.block_arrow(30, 228, 570, 228, HEAT, 14, 30, 26)
    return f.svg()


def district():
    f = Fig("fy27-district", 320, "Kaavakuva kaukolämmön kierrosta. Vasemmalla lämpölaitos, oikealla koti. Punainen menoputki vie kuumaa vettä "
            "kotiin ja sininen paluuputki tuo jäähtyneen veden takaisin. Putket ovat yhteisen eristeen sisällä maan alla. Oranssit nuolet "
            "osoittavat, että eristeestäkin pääsee vähän lämpöä maahan. Kuva ei ole mittakaavassa.")
    f.rect(20, 124, 86, 80, ALUMINIUM, INK, 2.5)
    f.rect(34, 80, 16, 44, IRON, INK, 2.5)
    f.add(f'<ellipse cx="46" cy="66" rx="14" ry="9" fill="{GLASS}" stroke="{RULE}" stroke-width="1.5"/>')
    f.rect(64, 150, 30, 54, HOT, INK, 2.5)
    f.path("M492,128 L546,84 L600,128 Z", HOT_LIGHT, INK, 2.5)
    f.rect(500, 128, 90, 76, SAND_LIGHT, INK, 2.5)
    f.rect(512, 140, 22, 26, GLASS, INK, 2)
    # radiator inside the house
    f.rect(548, 144, 32, 52, WHITE, INK, 2)
    for x in (556, 564, 572): f.line(x, 148, x, 192, HOT, 3)
    # the insulation shell around both pipes, then the pipes
    f.rect(106, 120, 394, 78, SAND_LIGHT, INK, 2.5, 8)
    f.rect(106, 138, 394, 14, HOT, INK, 2)
    f.rect(106, 166, 394, 14, COLD, INK, 2)
    for x, d, c in ((300, 1, HOT), (300, -1, COLD)):
        y = 145 if d == 1 else 173
        f.path(f"M{x + 12 * d},{y} L{x - 7 * d},{y - 8} L{x - 7 * d},{y + 8} Z", WHITE, INK, 1.5)
    # losses: small arrows through the insulation into the ground
    for x in (180, 420):
        f.block_arrow(x, 204, x, 236, HEAT, 8, 20, 14)
    f.tex(444, 224, r"\text{häviö}", "start", w=100)
    f.tex(250, 94, r"\text{menovesi}", "middle", w=160)
    f.tex(250, 268, r"\text{paluuvesi}", "middle", w=170)
    f.tex(376, 94, r"\text{eriste}", "middle", w=90)
    f.line(376, 108, 376, 124, MUTED, 1.5)
    f.tex(63, 262, r"\text{lämpölaitos}", "middle", w=140)
    f.tex(545, 262, r"\text{koti}", "middle", w=80)
    return f.svg()


def storage():
    f = Fig("fy27-storage", 300, "Kaavakuva kolmesta energiavarastosta. Vasemmalla akku, jossa energia on kemiallista. Keskellä pumppuvoimala: "
            "ylempi allas, alempi allas ja putki, jossa vesi virtaa alas. Oikealla lämpövarasto, eristetty säiliö täynnä kuumaa vettä. "
            "Kuva ei ole mittakaavassa.")
    f.defs_add(f'<linearGradient id="fy27-water" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{WATER_LIGHT}"/><stop offset="1" stop-color="{WATER}"/></linearGradient>')
    f.defs_add(f'<linearGradient id="fy27-hot" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{HOT_LIGHT}"/><stop offset="1" stop-color="{HOT}"/></linearGradient>')
    # battery
    f.rect(60, 100, 80, 110, GLASS, INK, 3, 8)
    f.rect(84, 88, 32, 12, INK, None, 2)
    f.rect(70, 150, 60, 50, GOOD_LIGHT, GOOD, 2, 4)
    f.line(100, 112, 100, 132, INK, 3); f.line(90, 122, 110, 122, INK, 3)
    f.line(90, 138, 110, 138, INK, 3)
    # pumped storage: upper and lower reservoir, slope and pipe
    f.path("M220,110 L330,110 L330,206 L186,206 Z", SAND, INK, 2.5)
    f.path("M220,110 L300,110 L300,128 L214,128 Z", "url(#fy27-water)", INK, 2)
    f.rect(190, 190, 72, 16, "url(#fy27-water)", INK, 2)
    f.line(290, 128, 290, 190, INK, 4); f.line(290, 190, 262, 198, INK, 4)
    f.circle(290, 160, 9, "none", INK, 3)
    # heat store: an insulated tank
    f.rect(420, 92, 100, 118, SAND_LIGHT, INK, 3, 14)
    f.rect(430, 102, 80, 98, "url(#fy27-hot)", INK, 2, 8)
    f.line(470, 82, 470, 92, INK, 4); f.line(470, 210, 470, 222, INK, 4)
    f.tex(100, 267, r"\text{akku}", "middle", w=90)
    f.tex(255, 267, r"\text{pumppuvoimala}", "middle", w=190)
    f.tex(470, 267, r"\text{lämpövarasto}", "middle", w=190)
    f.tex(100, 40, r"\text{kemiallinen}", "middle", w=150)
    f.tex(283, 28.5, r"\text{potentiaali-}", "middle", w=190)
    f.tex(283, 56.5, r"\text{energia}", "middle", w=190)
    f.tex(470, 40, r"\text{lämpö}", "middle", w=100)
    f.tex(251, 92.5, r"\text{yläallas}", "middle", w=110)
    f.tex(231, 224.5, r"\text{alaallas}", "middle", w=110)
    f.line(184, 20, 184, 280, RULE, 2, "6 6"); f.line(380, 20, 380, 280, RULE, 2, "6 6")
    return f.svg()


def sankey():
    f = Fig("fy27-sankey", 330, "Energiavirtakuva mittakaavassa. Ylhäällä sähköverkko: lähtevästä energiasta 96 % tulee perille ja 4 % häviää. "
            "Alhaalla kaukolämpöverkko: 91 % tulee perille ja 9 % häviää. Virran leveys on verrannollinen energiaan; lähtevän energian "
            "leveys on molemmissa sama.")
    H = 80.0
    def flow(yc, share_lost, name):
        top = yc - H / 2; bot = yc + H / 2
        hd, hl = H * (1 - share_lost), H * share_lost
        x0, x1, x2 = 150, 270, 470
        f.tex(12, top - 20, name, "start", w=200)
        f.rect(x0, top, x1 - x0 + 1, H, HEAT, None)
        # delivered band: the upper part continues right with an arrowhead
        f.add(f'<polygon points="{n(x1)},{n(top)} {n(x2)},{n(top)} {n(x2)},{n(top - 8)} {n(x2 + 30)},{n(top + hd / 2)} {n(x2)},{n(top + hd + 8)} {n(x2)},{n(top + hd)} {n(x1)},{n(top + hd)}" fill="{HEAT}"/>')
        # loss band: leaves from the bottom of the input, bends down
        y1 = top + hd; y2 = bot + 26
        f.add(f'<path d="M{n(x1)},{n(y1)} L{n(x1 + 60)},{n(y1)} C{n(x1 + 100)},{n(y1)} {n(x1 + 100)},{n(y2 - hl)} {n(x1 + 140)},{n(y2 - hl)} L{n(x1 + 190)},{n(y2 - hl)} L{n(x1 + 190)},{n(y2 - hl - 8)} L{n(x1 + 220)},{n(y2 - hl / 2)} L{n(x1 + 190)},{n(y2 + 8)} L{n(x1 + 190)},{n(y2)} L{n(x1 + 140)},{n(y2)} C{n(x1 + 100)},{n(y2)} {n(x1 + 100)},{n(bot)} {n(x1 + 60)},{n(bot)} L{n(x1)},{n(bot)} Z" fill="{HEAT_LIGHT}" stroke="{HEAT}" stroke-width="1.5"/>')
        f.tex(x0 - 10, yc, r"100\,\%", "end", w=90)
        f.tex(x2 + 40, top + hd / 2, f"{round((1 - share_lost) * 100)}" + r"\,\%", "start", w=80)
        f.tex(x1 + 236, y2 - hl / 2, f"{round(share_lost * 100)}" + r"\,\%", "start", w=70)
    flow(92, 0.04, r"\text{sähkö}")
    flow(250, 0.09, r"\text{kaukolämpö}")
    return f.svg()


FIGURES = {"hero": hero, "grid": grid, "district": district, "storage": storage, "sankey": sankey}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "sankey": "safe: shows only the shares 96/4 % and 91/9 %, no energies",
}
