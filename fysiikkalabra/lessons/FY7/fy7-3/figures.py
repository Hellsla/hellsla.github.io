"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy7-3` writes them into lesson.md.
Colours (FY7 brief): current #7048e8, magnetic field #2b8a3e, N pole fill #f2a69c, S pole fill #d0e6fb, both labelled."""
import math
from figlib import (Fig, Axes, fi, n, INK, MUTED, WHITE, RULE, RULE_LIGHT, GLASS, COPPER, IRON, ALUMINIUM, METAL_EDGE,
                    GOOD, GOOD_LIGHT, HOT_LIGHT, COLD_LIGHT, SAND, SAND_LIGHT, SAND_DARK, HEAT, HEAT_LIGHT, WATER_LIGHT, ICE, COLD, HOT)
import herolib as H

CURRENT, FIELD, NPOLE, SPOLE = "#7048e8", GOOD, HOT_LIGHT, COLD_LIGHT


def head(f, x, y, ang, color, s=13):
    """A filled arrowhead with its tip at (x, y) pointing at the angle ang (radians, SVG y down)."""
    c, si = math.cos(ang), math.sin(ang)
    bx, by = x - c * s, y - si * s
    hw = s * 0.45
    f.path(f"M{n(x)},{n(y)} L{n(bx - si * hw)},{n(by + c * hw)} L{n(bx + si * hw)},{n(by - c * hw)} Z", color)


def dot_out(f, x, y, r=13, color=CURRENT):
    """Current out of the page: a circle with a dot."""
    f.circle(x, y, r, WHITE, color, 2.5)
    f.circle(x, y, r * 0.28, color)


def cross_in(f, x, y, r=13, color=CURRENT):
    """Current into the page: a circle with a cross."""
    f.circle(x, y, r, WHITE, color, 2.5)
    d = r * 0.55
    f.line(x - d, y - d, x + d, y + d, color, 2.5)
    f.line(x - d, y + d, x + d, y - d, color, 2.5)


def pole(f, x, y, letter, r=19):
    f.circle(x, y, r, NPOLE if letter == "N" else SPOLE, INK, 2)
    f.tex(x, y, r"\text{" + letter + "}", "middle")


def needle(f, cx, cy, ang, L=24):
    """A compass: a white dial and a needle along ang, its N half light red and its S half light blue."""
    f.circle(cx, cy, L + 6, WHITE, INK, 2)
    c, s = math.cos(ang), math.sin(ang)
    w = 6
    tip, tail = (cx + c * L, cy + s * L), (cx - c * L, cy - s * L)
    left, right = (cx - s * w, cy + c * w), (cx + s * w, cy - c * w)
    f.path(f"M{n(tip[0])},{n(tip[1])} L{n(left[0])},{n(left[1])} L{n(right[0])},{n(right[1])} Z", NPOLE, INK, 1.5)
    f.path(f"M{n(tail[0])},{n(tail[1])} L{n(left[0])},{n(left[1])} L{n(right[0])},{n(right[1])} Z", SPOLE, INK, 1.5)
    f.circle(cx, cy, 2.5, INK)


def wire_field():
    f = Fig("fy73-wire", 372, "Kaavakuva, ei mittakaavassa, kaksi osaa. Vasemmalla pystysuora virtajohdin pöytälevyn läpi sivulta "
            "katsottuna: violetti nuoli osoittaa virran ylöspäin, ja johtimen ympärillä on kolme vihreää ympyränmuotoista "
            "kenttäviivaa, joiden nuolet kiertävät ylhäältä katsottuna vastapäivään. Oikealla sama tilanne ylhäältä: johdin "
            "on piste ympyrän sisällä, koska virta tulee kohti katsojaa, ja sen ympärillä on kolme samankeskistä "
            "kenttäviivaa vastapäivään. Neljä kompassia kenttäviivalla: jokaisen neulan pohjoispää, vaaleanpunainen, "
            "osoittaa kenttäviivan suuntaan.")
    f.tex(150, 24, r"\text{sivulta}", "middle")
    f.tex(450, 24, r"\text{ylhäältä}", "middle")
    f.line(300, 48, 300, 356, RULE, 2, "6 6")
    # left: wire through a board, field circles drawn as ellipses
    cx = 150
    f.path("M30,236 L270,236 L246,276 L54,276 Z", SAND_LIGHT, SAND, 2)
    ell = [(196, 92, 22), (256, 112, 26), (128, 64, 15)]
    for y, rx, ry in ell:   # back halves first, behind the wire
        f.path(f"M{cx - rx},{y} A{rx},{ry} 0 0 1 {cx + rx},{y}", stroke=FIELD, w=2.5, extra='stroke-opacity="0.55"')
    f.rect(cx - 5, 64, 10, 286, COPPER, INK, 2, 3)
    for y, rx, ry in ell:   # front halves with the arrow: counter-clockwise seen from above, so rightwards in front
        f.path(f"M{cx + rx},{y} A{rx},{ry} 0 0 1 {cx - rx},{y}", stroke=FIELD, w=3)
        head(f, cx - 22, y + ry, 0, FIELD, 14)
    f.arrow(cx + 26, 300, cx + 26, 240, CURRENT, 3, 14)
    f.tex(cx + 36, 282, "I", "start", CURRENT)
    f.tex(cx + 100, 160, r"\overline{B}", "start", FIELD)
    # right: the same from above, current out of the page
    cx, cy = 450, 200
    for r in (52, 96, 136):
        f.circle(cx, cy, r, "none", FIELD, 3 if r == 96 else 2.5)
        for k in range(4):
            a = k * math.pi / 2 + math.pi / 4          # arrows: counter-clockwise on the page (SVG y down: decreasing angle)
            x, y = cx + r * math.cos(a), cy - r * math.sin(a)
            head(f, x, y, -a - math.pi / 2, FIELD, 13)
    dot_out(f, cx, cy, 14)
    f.tex(cx + 20, cy + 24, "I", "start", CURRENT)
    for k in range(4):                                  # compasses on the middle circle, tangent to it
        a = k * math.pi / 2
        x, y = cx + 96 * math.cos(a), cy - 96 * math.sin(a)
        needle(f, x, y, -a - math.pi / 2, 20)
    f.tex(cx + 104, cy - 120, r"\overline{B}", "start", FIELD)
    return f.svg()


def coil_field():
    f = Fig("fy73-coil", 360, "Kaavakuva, ei mittakaavassa: pitkä käämi pituussuunnassa leikattuna. Ylärivin johdinpoikkileikkauksissa "
            "on piste (virta kohti katsojaa) ja alarivin poikkileikkauksissa risti (virta poispäin katsojasta). Käämin "
            "sisällä vihreät kenttäviivat ovat suoria, tasavälisiä ja oikealle osoittavia, eli kenttä on lähes homogeeninen. "
            "Ulkona kenttäviivat kaartuvat oikeasta päästä takaisin vasempaan. Oikea pää on pohjoisnapa N ja vasen "
            "eteläpää S, kuten sauvamagneetissa.")
    x0, x1, yt, yb = 150, 450, 116, 236
    # outside field lines: from the right end round to the left end, above and below
    for s in (-1, 1):
        for k, (dy, out) in enumerate(((24, 90), (44, 122))):
            ya = 176 + s * dy
            yo = 176 + s * out + s * 2
            f.path(f"M{x1 + 6},{ya} C{x1 + 92},{ya + s * 6} {x1 + 70},{yo} 300,{yo} C{x0 - 70},{yo} {x0 - 92},{ya + s * 6} {x0 - 6},{ya}",
                   stroke=FIELD, w=2.5)
            head(f, 292, yo, math.pi, FIELD, 14)
    for y in (146, 176, 206):
        f.line(x0 - 24, y, x1 + 24, y, FIELD, 3)
        head(f, 320, y, 0, FIELD, 14)
    for k in range(9):
        x = x0 + 18 + k * 33
        dot_out(f, x, yt, 12)
        cross_in(f, x, yb, 12)
    pole(f, x1 + 58, 176, "N")
    pole(f, x0 - 58, 176, "S")
    f.tex(372, 162, r"\overline{B}", "start", FIELD, bg=True)
    f.tex(300, 24, r"\text{virta: } \odot \text{ kohti katsojaa, } \otimes \text{ poispäin}", "middle", w=420)
    f.tex(300, 336, r"\text{sisällä lähes homogeeninen kenttä}", "middle", w=400)
    return f.svg()


def electromagnet():
    f = Fig("fy73-em", 360, "Kaavakuva, ei mittakaavassa: sähkömagneetti. Pystysuoran harmaan rautasydämen ympärille on kierretty "
            "kuparinen käämi, jonka johtimet menevät paristoon ja kytkimeen. Kun kytkin on kiinni, rautasydämen alapää vetää "
            "puoleensa rautanauloja, jotka roikkuvat siinä ketjuna. Oikealla sama sähkömagneetti kytkin auki: naulat ovat "
            "pudonneet pöydälle.")
    f.line(300, 40, 300, 344, RULE, 2, "6 6")
    f.tex(150, 24, r"\text{virta kulkee}", "middle")
    f.tex(450, 24, r"\text{virta katki}", "middle")
    f.line(12, 316, 588, 316, INK, 2.5)
    for cx, on in ((150, True), (450, False)):
        f.rect(cx - 18, 70, 36, 170, IRON, INK, 2.5, 3)
        for k in range(10):
            y = 92 + k * 13
            f.path(f"M{cx - 26},{y} Q{cx},{y + 10} {cx + 26},{y + 4}", stroke=COPPER, w=4, extra='stroke-linecap="round"')
        # leads to a battery
        bx = cx + 74
        f.path(f"M{cx + 26},96 H{bx}  V128", stroke=INK, w=2)
        f.path(f"M{cx + 26},210 H{bx} V182", stroke=INK, w=2)
        f.rect(bx - 16, 128, 32, 54, HEAT_LIGHT, INK, 2, 4)
        f.rect(bx - 7, 122, 14, 6, INK)
        if on:
            f.arrow(cx + 40, 96, cx + 62, 96, CURRENT, 2.5, 11)
            f.tex(cx + 52, 72, "I", "middle", CURRENT)
            for k in range(4):               # a chain of nails stuck to the core's lower end
                y = 246 + k * 17
                f.rect(cx - 3, y, 6, 16, METAL_EDGE, INK, 1.5, 1)
                f.rect(cx - 7, y, 14, 3, METAL_EDGE)
        else:
            f.line(bx + 16, 155, bx + 40, 140, INK, 2.5)   # open switch drawn as a lifted lever
            for k, (x, a) in enumerate(((cx - 40, 0), (cx - 6, 0), (cx + 26, 0), (cx + 54, 0))):
                f.rect(x, 306, 22, 6, METAL_EDGE, INK, 1.5, 1)
        f.tex(cx - 36, 160, r"\text{rauta}", "end")
    return f.svg()


def wire_graph():
    f = Fig("fy73-wgraph", 340, "Kuvaaja mittakaavassa: suoran johtimen magneettivuon tiheys B mikrotesloina etäisyyden r funktiona "
            "senttimetreinä, kun virta on 10 A. Käyrä laskee etäisyyden kasvaessa: 1 cm:n etäisyydellä B on 200 µT, 2 cm:n "
            "etäisyydellä 100 µT ja 4 cm:n etäisyydellä 50 µT. Kun etäisyys kaksinkertaistuu, kenttä puolittuu.")
    ax = Axes(f, (96, 290), (470, 56), x=(0, 5), y=(0, 250), xticks=[1, 2, 3, 4, 5], yticks=[50, 100, 150, 200, 250],
              xlabel=r"r\ (\text{cm})", ylabel=r"B\ (\mu\text{T})")
    ax.curve(lambda r: 200 / r, 0.8, 5, FIELD, 3)
    for r in (1, 2, 4):
        ax.guide(r, 200 / r)
        ax.point(r, 200 / r, FIELD)
    f.tex(ax.X(2.3), ax.Y(205), r"I = 10\,\text{A}", "start", FIELD)
    return f.svg()


def coil_dims():
    f = Fig("fy73-dims", 330, "Kaavakuva, ei mittakaavassa: käämi sivulta. Käämissä on N kierrosta kuparijohdinta pituudella l. "
            "Johtimen päistä kulkee virta I, joka on merkitty violetilla nuolella. Käämin sisällä vihreä nuoli B osoittaa "
            "akselin suuntaan.")
    x0, x1, yc, rr = 120, 410, 150, 58
    xm = (x0 + x1) / 2
    f.rect(x0, yc - rr * 0.8, x1 - x0, rr * 1.6, GLASS, METAL_EDGE, 1.5)
    turns = 14
    st = (x1 - x0) / turns
    for i in range(turns):
        x = x0 + (i + 0.5) * st
        f.add(f'<line x1="{n(x + st * 0.3)}" y1="{yc - rr}" x2="{n(x - st * 0.3)}" y2="{yc + rr}" stroke="{COPPER}" stroke-width="2" stroke-opacity="0.45"/>')
    f.arrow(x0 + 30, yc, x1 - 30, yc, FIELD, 4, 18)
    f.tex(xm, yc - 22, r"\overline{B}", "middle", FIELD, bg=True)
    for i in range(turns):
        x = x0 + (i + 0.5) * st
        f.add(f'<line x1="{n(x - st * 0.3)}" y1="{yc - rr}" x2="{n(x + st * 0.3)}" y2="{yc + rr}" stroke="{COPPER}" stroke-width="4" stroke-linecap="round"/>')
    # leads and current
    f.path(f"M{x0 + st * 0.2},{yc + rr} V{yc + rr + 34} H{x0 - 70}", stroke=INK, w=2)
    f.path(f"M{x1 - st * 0.2},{yc + rr} V{yc + rr + 34} H{x1 + 60}", stroke=INK, w=2)
    f.arrow(x0 - 60, yc + rr + 34, x0 - 16, yc + rr + 34, CURRENT, 3, 13)
    f.tex(x0 - 50, yc + rr + 60, "I", "middle", CURRENT)
    # length
    yd = 52
    f.line(x0, yd, x1, yd, INK, 2)
    f.line(x0, yd - 9, x0, yd + 9, INK, 2)
    f.line(x1, yd - 9, x1, yd + 9, INK, 2)
    f.tex(xm, yd - 22, "l", "middle", bg=True)
    f.tex(x1 + 16, yc, r"N\ \text{kierrosta}", "start", w=150)
    return f.svg()


DATA_I = [0.00, 0.50, 1.00, 1.50, 2.00, 2.50]
DATA_B = [0.04, 1.27, 2.51, 3.69, 4.99, 6.20]
FIT = (2.465143, 0.035238)        # lesson-answers.py fit-slope, fit-intercept


def coil_fit():
    """Task figure for the LOPS measurement: B in the middle of a coil against I, the points and the fitted line."""
    f = Fig("fy73-fit", 340, "Kuvaaja mittakaavassa: käämin keskeltä mitattu magneettivuon tiheys B millitesloina virran I "
            "funktiona ampeereina. Kuusi mittauspistettä virroilla 0; 0,5; 1,0; 1,5; 2,0 ja 2,5 A ovat lähes suoralla, "
            "ja niiden läpi on piirretty sovitettu suora. Ruudukon väli on 0,5 A ja 1 mT.")
    ax = Axes(f, (96, 290), (470, 56), x=(0, 3), y=(0, 7), xticks=[0.5, 1, 1.5, 2, 2.5, 3], yticks=[1, 2, 3, 4, 5, 6, 7],
              xlabel=r"I\ (\text{A})", ylabel=r"B\ (\text{mT})")
    k, b = FIT
    ax.line([(0, b), (2.75, k * 2.75 + b)], FIELD, 3)
    for i, bb in zip(DATA_I, DATA_B):
        ax.point(i, bb, INK)
    return f.svg()


def hero():
    """The chapter's opening illustration: a scrapyard crane's electromagnet lifting a scrapped car."""
    f = H.hero("fy73-hero", "Kuvitus: romuttamon nosturi. Nosturin puomin päästä riippuu ketjuissa pyöreä, harmaa "
               "sähkömagneetti, joka nostaa ruosteisen autonromun irti romukasan päältä. Taustalla on romukasoja ja "
               "taivas.")
    f.rect(0, 0, 1200, 600, H.grad(f, "fy73h-sky", ICE, GLASS))
    H.cloud(f, 220, 110, 1.0)
    H.cloud(f, 980, 80, 0.7)
    # ground and scrap heaps
    f.rect(0, 470, 1200, 130, SAND_DARK)
    f.path("M0,480 L80,400 L170,430 L260,380 L360,470 Z", METAL_EDGE)
    f.path("M780,480 L860,390 L930,420 L1010,360 L1100,410 L1200,380 L1200,480 Z", METAL_EDGE)
    for x, y, w, h, c in ((40, 440, 70, 30, HOT_LIGHT), (190, 430, 60, 40, COLD_LIGHT), (880, 430, 80, 36, ALUMINIUM), (1040, 420, 90, 44, HEAT_LIGHT)):
        f.rect(x, y, w, h, c, INK, 2.5, 6)
    # crane: tracked base, cab, boom
    f.rect(820, 470, 280, 50, INK, rx=18)
    for x in range(845, 1090, 40): f.circle(x, 495, 14, IRON, METAL_EDGE, 3)
    f.rect(860, 380, 200, 90, HEAT, INK, 3, 6)
    f.rect(980, 330, 80, 60, HEAT, INK, 3, 6)
    f.rect(992, 342, 56, 34, GLASS, INK, 2, 4)
    f.path("M900,400 L560,90 L585,78 L940,392 Z", HEAT_LIGHT, INK, 3)
    for t in (0.2, 0.4, 0.6, 0.8):
        x1, y1 = 900 + (560 - 900) * t, 400 + (90 - 400) * t
        f.line(x1, y1, x1 + 30, y1 - 8, INK, 2)
    # chains and the magnet
    f.line(566, 92, 540, 200, INK, 3)
    f.line(566, 92, 600, 200, INK, 3)
    f.add(f'<ellipse cx="570" cy="206" rx="80" ry="16" fill="{METAL_EDGE}" stroke="{INK}" stroke-width="3"/>')
    f.rect(490, 206, 160, 38, IRON, INK, 3)
    f.add(f'<ellipse cx="570" cy="244" rx="80" ry="16" fill="{IRON}" stroke="{INK}" stroke-width="3"/>')
    f.path("M566,92 C520,140 640,150 600,206", stroke=CURRENT, w=3)
    # the scrapped car hanging under the magnet, a little tilted
    f.add('<g transform="rotate(-6 570 320)">')
    f.path("M440,300 L480,262 L640,262 L690,300 L710,302 L710,348 L430,348 L430,302 Z", HOT_LIGHT, INK, 3)
    f.path("M470,298 L494,272 L560,272 L560,298 Z", GLASS, INK, 2)
    f.path("M574,298 L574,272 L630,272 L660,298 Z", GLASS, INK, 2)
    f.circle(490, 350, 26, INK)
    f.circle(490, 350, 11, ALUMINIUM)
    f.circle(650, 350, 26, INK)
    f.circle(650, 350, 11, ALUMINIUM)
    f.path("M520,320 L540,330 L530,340", stroke=HEAT, w=3)
    f.add('</g>')
    # a pale band of the magnet's field between magnet and car (no text)
    for x in (520, 570, 620):
        f.path(f"M{x},262 q-8,10 0,20 t0,20", stroke=FIELD, w=3, extra='stroke-linecap="round" stroke-opacity="0.7"')
    return f.svg()


FIGURES = {"hero": hero, "wire-field": wire_field, "coil-field": coil_field, "electromagnet": electromagnet,
           "wire-graph": wire_graph, "coil-dims": coil_dims, "coil-fit": coil_fit}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "wire-field": "reveals: the field circles and their direction around a wire (right-hand rule)",
    "coil-field": "reveals: the coil's field inside and outside, which end is N",
    "electromagnet": "reveals: an electromagnet holds iron only while the current flows",
    "wire-graph": "reveals: B of a 10 A wire at 1, 2 and 4 cm (200, 100, 50 µT)",
    "coil-dims": "safe: a coil with N, l, I and B labelled, no values",
    "coil-fit": "safe: example data B against I in a coil (six points and a fitted line), slope not written",
}
