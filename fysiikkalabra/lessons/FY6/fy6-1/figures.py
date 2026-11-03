"""Figures of fy6-1 (scripts/figlib.py); `python scripts/figures.py fy6-1` writes them into lesson.md.
Colours, one meaning each: the conventional current I is a violet filled arrow (#7048e8, used for nothing else in
this chapter), free electrons are blue dots (#1971c2) with their own blue arrow, energy flow is the orange block
arrow, copper is #b8622d, the insulation and glass are light. Circuit diagrams use the IEC symbols of Finnish
textbooks (battery: long thin plate + and short thick plate −; lamp: a circle with a cross; resistor: a rectangle;
meters: circles with A or V) with ink wires 3 px on whole pixels. Every label is LaTeX."""
import math
from figlib import (Fig, Axes, INK, MUTED, WHITE, RULE, RULE_LIGHT, GLASS, SAND_LIGHT, SAND, GRAIN, HEAT_LIGHT, HEAT,
                    COLD, COLD_LIGHT, ALUMINIUM, METAL_EDGE, IRON, COPPER, PAPER, n)
import herolib as H
from herolib import grad

CURRENT = "#7048e8"     # the conventional current I
ELECTRON = COLD         # free electrons and their motion
W = 3                   # wire width in diagrams


# --- circuit-diagram symbols (IEC) ---------------------------------------------------------------------------------
def wire(f, pts, w=W, color=INK):
    p = " ".join(f"{n(x)},{n(y)}" for x, y in pts)
    f.add(f'<polyline points="{p}" fill="none" stroke="{color}" stroke-width="{w}" stroke-linejoin="miter" stroke-linecap="square"/>')


def cell(f, cx, cy, vertical=True, plus_first=True, gap=12):
    """One cell on a wire through (cx, cy): the long thin plate is +, the short thick plate −. vertical: the wire runs
    up and down and the plates lie across it; plus_first: + is the upper (or the left) plate."""
    if vertical:
        f.rect(cx - 30, cy - gap / 2 - 2, 60, gap + 4, WHITE)
        yp, ym = (cy - gap / 2, cy + gap / 2) if plus_first else (cy + gap / 2, cy - gap / 2)
        f.line(cx - 24, yp, cx + 24, yp, INK, 3)
        f.line(cx - 11, ym, cx + 11, ym, INK, 7)
    else:
        f.rect(cx - gap / 2 - 2, cy - 30, gap + 4, 60, WHITE)
        xp, xm = (cx - gap / 2, cx + gap / 2) if plus_first else (cx + gap / 2, cx - gap / 2)
        f.line(xp, cy - 24, xp, cy + 24, INK, 3)
        f.line(xm, cy - 11, xm, cy + 11, INK, 7)


def lamp(f, cx, cy, r=20):
    f.circle(cx, cy, r, WHITE, INK, W)
    d = r * 0.7071
    f.line(cx - d, cy - d, cx + d, cy + d, INK, 2.5)
    f.line(cx - d, cy + d, cx + d, cy - d, INK, 2.5)


def resistor(f, cx, cy, vertical=False):
    w, h = (20, 50) if vertical else (50, 20)
    f.rect(cx - w / 2, cy - h / 2, w, h, WHITE, INK, W)


def meter(f, cx, cy, letter, r=21):
    f.circle(cx, cy, r, WHITE, INK, W)
    f.tex(cx, cy, letter, "middle", w=30)


def switch(f, x1, x2, y, closed=False):
    """A switch on a horizontal wire between x1 and x2: two terminals and a lever, open at 30°."""
    f.rect(x1 + 1, y - 6, x2 - x1 - 2, 12, WHITE)
    L = x2 - x1
    if closed: f.line(x1, y, x2, y, INK, W)
    else: f.line(x1, y, x1 + L * math.cos(math.radians(28)), y - L * math.sin(math.radians(28)), INK, W, cap="round")
    f.circle(x1, y, 4.5, WHITE, INK, 2.5); f.circle(x2, y, 4.5, WHITE, INK, 2.5)


def vswitch(f, x, y1, y2):
    """An open switch on a vertical wire between y1 (top) and y2."""
    f.rect(x - 6, y1 + 1, 12, y2 - y1 - 2, WHITE)
    L = y2 - y1
    f.line(x, y2, x - L * math.sin(math.radians(28)), y2 - L * math.cos(math.radians(28)), INK, W, cap="round")
    f.circle(x, y1, 4.5, WHITE, INK, 2.5); f.circle(x, y2, 4.5, WHITE, INK, 2.5)


def node(f, x, y): f.circle(x, y, 6, INK)


def i_arrow(f, x1, y1, x2, y2, label=None, lx=None, ly=None, anchor="middle"):
    """The conventional current: a violet filled arrow beside the wire, with its label I."""
    f.arrow(x1, y1, x2, y2, CURRENT, 3, 15)
    if label: f.tex(lx, ly, label, anchor, CURRENT)


# --- realistic parts --------------------------------------------------------------------------------------------------
def aa_cell(f, x, y, w=96, h=34, gid=None):
    """An AA cell lying horizontally, + to the right: a metal body, a light band and the + nub."""
    body = grad(f, gid, ALUMINIUM, METAL_EDGE) if gid else ALUMINIUM
    f.rect(x, y - h / 2, w, h, body, INK, 2.5, rx=5)
    f.rect(x + w * 0.62, y - h / 2 + 1.5, w * 0.3, h - 3, SAND_LIGHT)
    f.rect(x + w, y - 6, 7, 12, METAL_EDGE, INK, 2, rx=2)


def bulb(f, cx, cy, on=True, gid=None):
    """A small lamp in a socket on a horizontal wire at y = cy: the socket on the wire, the glass above it."""
    if on:
        f.circle(cx, cy - 40, 46, grad(f, gid, HEAT_LIGHT, SAND_LIGHT) if gid else HEAT_LIGHT)
    f.circle(cx, cy - 40, 26, GLASS, INK, 2.5)
    f.path(f"M{n(cx - 9)},{n(cy - 18)} L{n(cx - 9)},{n(cy - 40)} L{n(cx - 4)},{n(cy - 46)} L{n(cx)},{n(cy - 40)} L{n(cx + 4)},{n(cy - 46)} L{n(cx + 9)},{n(cy - 40)} L{n(cx + 9)},{n(cy - 18)}",
           "none", HEAT if on else MUTED, 2)
    f.rect(cx - 16, cy - 18, 32, 26, IRON, INK, 2.5, rx=3)


def copper_wire(f, pts, gid_w=8):
    """A wire with its insulation: a thick light outline (the insulation) and a copper core."""
    p = " ".join(f"{n(x)},{n(y)}" for x, y in pts)
    f.add(f'<polyline points="{p}" fill="none" stroke="{INK}" stroke-width="{gid_w + 5}" stroke-linejoin="round" stroke-linecap="round"/>')
    f.add(f'<polyline points="{p}" fill="none" stroke="{COPPER}" stroke-width="{gid_w}" stroke-linejoin="round" stroke-linecap="round"/>')


def toggle(f, x1, x2, y, closed=True):
    """A real switch on a base: two screws and a copper lever."""
    f.rect(x1 - 18, y - 2, x2 - x1 + 36, 22, grad(f, "fy61-piiri-base", SAND_LIGHT, SAND), GRAIN, 2, rx=4)
    for x in (x1, x2): f.circle(x, y, 7, IRON, INK, 2)
    if closed: f.line(x1, y - 3, x2, y - 3, COPPER, 6, cap="round")
    else: f.line(x1, y - 3, x1 + (x2 - x1) * 0.88, y - 3 - (x2 - x1) * 0.47, COPPER, 6, cap="round")


# --- Ydinajatus ---------------------------------------------------------------------------------------------------------
def piiri():
    """Ydinajatus: a real closed circuit (two AA cells, a switch, a lamp, copper wires) with the conventional current."""
    f = Fig("fy61-piiri", 340, "Suljettu virtapiiri pöydällä. Alhaalla vasemmalla kaksi AA-paristoa peräkkäin pidikkeessä, plusnapa oikealla. "
            "Pariston plusnavasta johto kulkee oikealle suljetun kytkimen kautta, nousee oikeaan yläkulmaan ja kulkee ylhäällä vasemmalle "
            "lampun kautta. Lamppu palaa. Johto palaa vasenta reunaa alas pariston miinusnapaan. Violetit nuolet näyttävät sovitun virran "
            "suunnan: plusnavasta ulkoisen piirin kautta miinusnapaan. Kaavakuva, ei mittakaavassa.")
    L, R, T, B = 60, 540, 128, 268
    copper_wire(f, [(156, B), (L, B), (L, T), (R, T), (R, B), (436, B)])
    copper_wire(f, [(300, B), (364, B)])
    toggle(f, 364, 436, B)
    # the cells, + to the right
    f.rect(140, B - 26, 168, 52, grad(f, "fy61-piiri-holder", RULE_LIGHT, RULE), INK, 2, rx=6)
    aa_cell(f, 150, B, 70, 30, "fy61-piiri-c1"); aa_cell(f, 228, B, 70, 30, "fy61-piiri-c2")
    bulb(f, 300, T, True, "fy61-piiri-glow")
    # current arrows: up the right side, left along the top, down the left side, right along the bottom
    i_arrow(f, R + 30, 236, R + 30, 166, r"I", R + 30, 136 + 0, "middle")
    i_arrow(f, 462, T - 22, 400, T - 22)
    i_arrow(f, L - 30 + 60, 152, L - 30 + 60, 222)
    i_arrow(f, 316, B + 32, 346, B + 32)
    f.tex(224, 310, r"\text{paristo}", "middle", MUTED)
    f.tex(404, 310, r"\text{kytkin}", "middle", MUTED)
    f.tex(380, 50, r"\text{lamppu}", "start", MUTED)
    f.tex(160, 96, r"\text{johdin}", "middle", MUTED)
    f.tex(326, B - 24, "+", "middle", INK, w=22)
    f.tex(122, B - 24, "-", "middle", INK, w=22)
    return f.svg()


def johdin():
    """Ydinajatus: a wire cut open: the insulation, the copper with its ions and the free electrons; the electrons drift
    one way, the conventional current points the other way."""
    f = Fig("fy61-johdin", 330, "Johdon pala suurennettuna. Uloinna on muovinen eristekuori, jonka sisällä on kuparijohdin. Kuparissa on "
            "säännöllisessä hilassa positiivisia metalli-ioneja ja niiden välissä vapaita elektroneja. Sininen nuoli osoittaa vasemmalle: "
            "vapaat elektronit liikkuvat vasemmalle. Violetti nuoli osoittaa oikealle: sovittu virran suunta on elektronien liikkeelle "
            "vastakkainen. Kaavakuva, ei mittakaavassa.")
    y0, y1 = 112, 236                     # the copper core
    f.rect(24, y0 - 22, 552, y1 - y0 + 44, grad(f, "fy61-johdin-ins", RULE_LIGHT, RULE), INK, 2.5, rx=22)
    f.rect(24, y0, 552, y1 - y0, grad(f, "fy61-johdin-cu", "#e9c98a", COPPER), INK, 2)
    for i in range(10):
        for j in range(3):
            x, y = 58 + i * 54 + (27 if j % 2 else 0), y0 + 22 + j * 40
            if x > 560: continue
            f.circle(x, y, 11, COPPER, INK, 1.5)
            f.line(x - 5, y, x + 5, y, WHITE, 2); f.line(x, y - 5, x, y + 5, WHITE, 2)
    for k in range(18):
        x = 44 + k * 29.5 + 8 * H.rnd(k, 3); y = y0 + 42 + 40 * (k % 2) + 4 * H.rnd(k, 5)
        f.circle(x, y, 6, ELECTRON, WHITE, 1.5)
    f.arrow(470, 290, 340, 290, ELECTRON, 3.5, 16)
    f.tex(326, 290, r"\text{elektronit}", "end", ELECTRON)
    f.arrow(340, 46, 470, 46, CURRENT, 3.5, 16)
    f.tex(482, 46, "I", "start", CURRENT)
    f.tex(40, 46, r"\text{eriste}", "start", MUTED)
    f.tex(40, 290, r"\text{kupari}", "start", MUTED)
    return f.svg()


def symbolit():
    """Ydinajatus, Kytkentäkaavio: the IEC symbols of the chapter, each with its name."""
    f = Fig("fy61-symbolit", 360, "Kytkentäkaavion piirrosmerkit kahdessa sarakkeessa. Vasemmalla ylhäältä alas: paristo, jossa pitkä ohut "
            "viiva on plusnapa ja lyhyt paksu viiva miinusnapa; lamppu, ympyrä jonka sisällä on risti; vastus, suorakulmio; "
            "ampeerimittari, ympyrä jonka sisällä on A. Oikealla: avoin kytkin, johdin, liitoskohta pisteenä ja volttimittari, ympyrä "
            "jonka sisällä on V.")
    f.line(306, 22, 306, 338, RULE, 1.5, "6 6")
    rows = [62, 140, 218, 296]
    c1, c2 = 64, 362
    # column 1
    y = rows[0]; wire(f, [(c1 - 44, y), (c1 + 44, y)]); cell(f, c1, y, vertical=False, plus_first=True)
    f.tex(c1 - 22, y - 32, "+", "middle", w=22); f.tex(c1 + 18, y - 32, "-", "middle", w=22)
    f.tex(120, y, r"\text{paristo}", "start")
    y = rows[1]; wire(f, [(c1 - 44, y), (c1 + 44, y)]); lamp(f, c1, y); f.tex(120, y, r"\text{lamppu}", "start")
    y = rows[2]; wire(f, [(c1 - 44, y), (c1 + 44, y)]); resistor(f, c1, y); f.tex(120, y, r"\text{vastus}", "start")
    y = rows[3]; wire(f, [(c1 - 44, y), (c1 + 44, y)]); meter(f, c1, y, r"\text{A}"); f.tex(120, y, r"\text{ampeerimittari}", "start")
    # column 2
    y = rows[0]; wire(f, [(c2 - 44, y), (c2 + 44, y)]); switch(f, c2 - 26, c2 + 26, y); f.tex(416, y, r"\text{kytkin}", "start")
    y = rows[1]; wire(f, [(c2 - 44, y), (c2 + 44, y)]); f.tex(416, y, r"\text{johdin}", "start")
    y = rows[2]; wire(f, [(c2 - 44, y), (c2 + 44, y)]); wire(f, [(c2, y), (c2, y + 34)]); node(f, c2, y); f.tex(416, y, r"\text{liitoskohta}", "start")
    y = rows[3]; wire(f, [(c2 - 44, y), (c2 + 44, y)]); meter(f, c2, y, r"\text{V}"); f.tex(416, y, r"\text{volttimittari}", "start")
    return f.svg()


def kaavio():
    """Ydinajatus, Kytkentäkaavio: the circuit of the figure piiri as a diagram."""
    f = Fig("fy61-kaavio", 320, "Edellisen kuvan virtapiiri kytkentäkaaviona. Suorakulmion muotoinen silmukka. Alareunassa vasemmalla kaksi "
            "paristokennoa peräkkäin, pitkä viiva eli plusnapa oikealla. Alareunassa oikealla suljettu kytkin, "
            "yläreunan keskellä lamppu, ympyrä jossa on risti. Violetti nuoli oikean reunan vieressä osoittaa ylöspäin ja on merkitty I: "
            "virta kulkee plusnavasta kytkimen ja lampun kautta miinusnapaan.")
    L, R, T, B = 90, 500, 70, 250
    wire(f, [(L, T), (R, T), (R, B), (L, B), (L, T)])
    cell(f, 186, B, vertical=False, plus_first=False); cell(f, 236, B, vertical=False, plus_first=False)
    switch(f, 370, 430, B, closed=True)
    lamp(f, 295, T)
    f.tex(248, B + 44, "+", "middle", w=22); f.tex(174, B + 44, "-", "middle", w=22)
    f.tex(211, B + 44, r"U", "middle", w=24)
    i_arrow(f, R + 36, 196, R + 36, 124, "I", R + 58, 160, "start")
    f.tex(400, B + 44, r"\text{kytkin}", "middle", MUTED)
    f.tex(295, T - 40, r"\text{lamppu}", "middle", MUTED)
    return f.svg()


# --- Kaava ------------------------------------------------------------------------------------------------------------
def virta():
    """Kaava: the current as the charge that passes a cross-section of the wire per unit time."""
    f = Fig("fy61-virta", 320, "Kuparijohdin suurennettuna. Johdon keskellä on katkoviivalla piirretty poikkileikkaus. Sinisiä elektroneja "
            "on koko johdossa, ja ne liikkuvat vasemmalle poikkileikkauksen läpi. Oikealla ylhäällä sekuntikello. Violetti nuoli "
            "johdon yläpuolella osoittaa oikealle ja on merkitty I. Merkinnät: ajassa t poikkileikkauksen läpi kulkee varaus Q. "
            "Kaavakuva, ei mittakaavassa.")
    y0, y1 = 118, 222
    f.rect(26, y0, 548, y1 - y0, grad(f, "fy61-virta-cu", "#e9c98a", COPPER), INK, 2.5, rx=8)
    cx = 300
    f.add(f'<ellipse cx="{cx}" cy="{(y0 + y1) / 2:g}" rx="22" ry="{(y1 - y0) / 2:g}" fill="{WHITE}" fill-opacity="0.35" stroke="{INK}" stroke-width="2" stroke-dasharray="7 5"/>')
    for k in range(18):
        x = 52 + k * 29 + 9 * H.rnd(k, 7); y = y0 + 22 + (k % 3) * 28 + 6 * H.rnd(k, 9)
        if abs(x - cx) < 14: x += 18
        f.circle(x, y, 7, ELECTRON, WHITE, 1.5)
    f.arrow(250, 252, 120, 252, ELECTRON, 3.5, 16)
    f.tex(262, 252, r"\text{elektronit}", "start", ELECTRON)
    i_arrow(f, 250, 80, 380, 80, "I", 396, 80, "start")
    f.tex(cx, 34, r"\text{poikkileikkaus}", "middle", MUTED)
    H.stopwatch(f, 520, 62, 30, 0.3)
    f.tex(470, 62, "t", "end", w=20)
    f.tex(cx, 294, r"Q\ \text{kulkee ajassa}\ t", "middle", w=240)
    return f.svg()


def jannite():
    """Kaava, Jännite: the cell gives each coulomb of charge 1,5 J; the lamp turns that energy into light and heat; the
    same charge returns to the cell."""
    f = Fig("fy61-jannite", 350, "Paristo vasemmalla ja lamppu oikealla, välissä oranssi energiavirran nuoli paristosta lamppuun. Paristoon "
            "on merkitty jännite U yhtä suuri kuin 1,5 volttia, nuoleen energia 1,5 joulea jokaista coulombia kohti. Lamppu säteilee "
            "valoa ja lämpöä. Ylhäällä johto kulkee pariston plusnavasta lampun kylkeen, alhaalla johto palaa lampun kannasta pariston "
            "pohjaan, ja violetti nuoli näyttää, että sama varaus kiertää takaisin paristoon. Kaavakuva.")
    # the loop: + up and over to the lamp's side contact, the lamp's base back to the cell's bottom
    copper_wire(f, [(132, 56), (132, 26), (566, 26), (566, 161), (486, 161)], 7)
    copper_wire(f, [(132, 150), (132, 262), (468, 262), (468, 170)], 7)
    # the cell, standing
    f.rect(92, 70, 80, 120, grad(f, "fy61-jannite-cell", ALUMINIUM, METAL_EDGE, horizontal=True), INK, 2.5, rx=8)
    f.rect(92, 70, 80, 36, SAND_LIGHT, INK, 2.5, rx=8)
    f.rect(118, 56, 28, 14, METAL_EDGE, INK, 2, rx=3)
    f.tex(132, 216, r"U = 1{,}5\,\text{V}", "middle", w=136, bg=True)
    # energy flow
    f.block_arrow(196, 120, 392, 120, HEAT, shaft=22, head=46, headlen=32)
    f.tex(294, 74, r"1{,}5\,\text{J}\ \text{/}\ 1\,\text{C}", "middle", w=150)
    f.tex(294, 166, r"\text{energia}", "middle", HEAT)
    # the lamp with light rays
    f.circle(468, 120, 60, grad(f, "fy61-jannite-glow", HEAT_LIGHT, SAND_LIGHT))
    f.circle(468, 120, 32, GLASS, INK, 2.5)
    f.path("M459,148 L459,120 L464,112 L468,120 L472,112 L477,120 L477,148", "none", HEAT, 2.2)
    f.rect(450, 148, 36, 26, IRON, INK, 2.5, rx=3)
    for a in (-70, -35, 35):
        t = math.radians(a - 90)
        f.line(468 + 68 * math.cos(t), 120 + 68 * math.sin(t), 468 + 82 * math.cos(t), 120 + 82 * math.sin(t), HEAT, 3, cap="round")
    i_arrow(f, 360, 288, 240, 288)
    f.tex(300, 318, r"\text{sama varaus palaa paristolle}", "middle", CURRENT)
    return f.svg()


# --- tasks ------------------------------------------------------------------------------------------------------------
def virta_kuvaaja():
    """Exercise L2-04: a (t, I) graph, 0,40 A for 20 s and 0,10 A from 20 s to 50 s, then 0."""
    f = Fig("fy61-kuvaaja", 340, "Kuvaaja virrasta ajan funktiona. Vaaka-akselilla aika t sekunteina 0–60, pystyakselilla virta I ampeereina "
            "0–0,5. Virta on 0,40 ampeeria ajan 0–20 sekuntia, sitten 0,10 ampeeria ajan 20–50 sekuntia ja sen jälkeen nolla.")
    ax = Axes(f, (92, 290), (500, 50), x=(0, 60), y=(0, 0.5), xticks=[10, 20, 30, 40, 50, 60], yticks=[0.1, 0.2, 0.3, 0.4, 0.5],
              xlabel=r"t\ (\text{s})", ylabel=r"I\ (\text{A})")
    ax.line([(0, 0.4), (20, 0.4), (20, 0.1), (50, 0.1), (50, 0), (60, 0)], CURRENT, 3)
    return f.svg()


def kaavio_malli():
    """Exercise L3-03 model: two cells in series, a switch, a lamp and an ammeter in one loop; current from + round to −."""
    f = Fig("fy61-malli", 320, "Mallikaavio. Suorakulmion muotoinen silmukka. Vasemmassa reunassa kaksi paristokennoa peräkkäin pystyssä, "
            "plusnavat ylöspäin. Yläreunassa kytkin ja lamppu, oikeassa reunassa ampeerimittari, ympyrä jossa on A. Violetti nuoli "
            "yläreunan yläpuolella osoittaa oikealle ja on merkitty I.")
    L, R, T, B = 110, 480, 80, 270
    wire(f, [(L, T), (R, T), (R, B), (L, B), (L, T)])
    cell(f, L, 140, vertical=True, plus_first=True); cell(f, L, 200, vertical=True, plus_first=True)
    switch(f, 190, 250, T)
    lamp(f, 360, T)
    meter(f, R, 175, r"\text{A}")
    f.tex(L - 44, 134, "+", "middle", w=22); f.tex(L - 44, 212, "-", "middle", w=22)
    i_arrow(f, 262, T - 34, 322, T - 34, "I", 334, T - 34, "start")
    f.tex(220, T + 44, r"\text{kytkin}", "middle", MUTED)
    f.tex(360, T + 44, r"\text{lamppu}", "middle", MUTED)
    return f.svg()


def virhe_kaavio():
    """Etsi virhe: a student's diagram in which both leads of the lamp end at the + terminal, so the loop does not pass
    through the cell (the − terminal is left unconnected)."""
    f = Fig("fy61-virhe", 320, "Opiskelijan piirtämä kytkentäkaavio. Vasemmalla pystyssä paristo, plusnapa ylhäällä. Plusnavasta johto nousee "
            "ja kulkee yläreunaa oikealle kytkimen ja lampun kautta, laskeutuu oikeaa reunaa ja palaa alareunaa vasemmalle. Alareunan "
            "johto kääntyy ylös ja liittyy pisteessä yläreunan johtoon pariston plusnavan yläpuolella. Pariston miinusnavasta lähtee "
            "lyhyt johto alas, ja se päättyy tyhjään.")
    L, R, T, B = 120, 490, 70, 260
    wire(f, [(L, 150), (L, T), (R, T), (R, B), (200, B), (200, T)])
    node(f, 200, T)
    wire(f, [(L, 150), (L, 210)])
    cell(f, L, 180, vertical=True, plus_first=True)
    wire(f, [(L, 210), (L, 236)])
    f.circle(L, 238, 4.5, WHITE, INK, 2.5)
    switch(f, 260, 320, T)
    lamp(f, 410, T)
    f.tex(L - 44, 164, "+", "middle", w=22); f.tex(L - 44, 200, "-", "middle", w=22)
    return f.svg()


def _choice(fid, label, kind):
    f = Fig(fid, 300, label)
    L, R, T, B = 80, 520, 70, 240
    if kind == "branch":                       # the switch on a dead-end branch, outside the loop
        wire(f, [(L, T), (R, T), (R, B), (L, B), (L, T)])
        wire(f, [(300, B), (300, 270), (330, 270)])
        node(f, 300, B)
        switch(f, 330, 380, 270)
    else:
        wire(f, [(L, T), (R, T), (R, B), (L, B), (L, T)])
        switch(f, 270, 330, B)
    cell(f, L, 155, vertical=True, plus_first=True)
    if kind == "resistors":
        resistor(f, 230, T); resistor(f, 370, T)
    else:
        lamp(f, 230, T); lamp(f, 370, T)
    return f.svg()


def valinta_a():
    return _choice("fy61-va", "Kytkentäkaavio. Vasemmassa reunassa paristo. Yläreunassa kaksi lampun merkkiä, ympyrät joissa on risti, peräkkäin. "
                   "Alareunassa avoin kytkin. Kaikki ovat samassa suljetussa silmukassa.", "ok")


def valinta_b():
    return _choice("fy61-vb", "Kytkentäkaavio. Vasemmassa reunassa paristo. Yläreunassa kaksi suorakulmiota peräkkäin. Alareunassa avoin "
                   "kytkin. Kaikki ovat samassa suljetussa silmukassa.", "resistors")


def valinta_c():
    return _choice("fy61-vc", "Kytkentäkaavio. Vasemmassa reunassa paristo. Yläreunassa kaksi lampun merkkiä, ympyrät joissa on risti, peräkkäin. "
                   "Alareunan johto on yhtenäinen. Sen keskeltä lähtee alaspäin lyhyt johto, jonka päässä on avoin kytkin, joka ei johda "
                   "mihinkään.", "branch")


# --- the opening illustration ------------------------------------------------------------------------------------------
def hero():
    """A flashlight on a table at night, its body cut open to show two cells and the spring; the lamp lights a cone."""
    f = H.hero("fy61-hero", "Kuvitus: pimeä huone illalla. Pöydällä on taskulamppu, jonka kylki on piirretty auki: sisällä näkyy kaksi "
               "paristoa peräkkäin, jousi ja katkaisija. Lampun valokeila valaisee pöytää ja seinää oikealla.")
    f.rect(0, 0, 1200, 600, grad(f, "fy61h-night", INK, "#2f74b5"))
    f.rect(0, 440, 1200, 160, grad(f, "fy61h-table", SAND, GRAIN))
    f.rect(0, 436, 1200, 8, SAND_LIGHT)
    for k in range(6): f.path(f"M0,{470 + k * 22} Q600,{462 + k * 22 + 10 * H.rnd(k)} 1200,{474 + k * 22}", "none", GRAIN, 2, 'stroke-opacity="0.5"')
    # the light cone and the lit spot
    f.path("M790,390 L1200,170 L1200,440 Z", HEAT_LIGHT, extra='fill-opacity="0.55"')
    f.path("M790,390 L1200,250 L1200,440 Z", SAND_LIGHT, extra='fill-opacity="0.45"')
    f.add('<ellipse cx="1150" cy="300" rx="44" ry="150" fill="#ffffff" fill-opacity="0.35"/>')
    # the flashlight: a tube with a window, the head, the switch button
    f.rect(330, 344, 400, 92, grad(f, "fy61h-tube", "#4f8fbf", COLD), INK, 4, rx=20)
    f.path("M730,350 L790,330 L790,450 L730,430 Z", grad(f, "fy61h-head", ALUMINIUM, METAL_EDGE), INK, 4)
    f.rect(786, 330, 14, 112, METAL_EDGE, INK, 3, rx=4)
    f.circle(788, 390, 30, "#ffffff")
    f.rect(470, 326, 60, 20, IRON, INK, 3, rx=8)
    # the cut-away: two cells, + to the right, and the spring at the back
    f.rect(372, 358, 330, 64, GLASS, INK, 3, rx=10)
    for x0 in (420, 556):
        f.rect(x0, 368, 128, 44, grad(f, f"fy61h-cell{x0}", ALUMINIUM, METAL_EDGE), INK, 3, rx=6)
        f.rect(x0 + 84, 370, 36, 40, SAND_LIGHT)
        f.rect(x0 + 128, 382, 9, 16, METAL_EDGE, INK, 2, rx=2)
    pts = " ".join(f"{378 + k * 5},{370 if k % 2 else 410}" for k in range(9))
    f.add(f'<polyline points="{pts}" fill="none" stroke="{METAL_EDGE}" stroke-width="4" stroke-linejoin="round"/>')
    f.line(694, 390, 730, 390, COPPER, 5)
    return f.svg()


FIGURES = {"hero": hero, "piiri": piiri, "johdin": johdin, "symbolit": symbolit, "kaavio": kaavio, "virta": virta, "jannite": jannite,
           "virta-kuvaaja": virta_kuvaaja, "kaavio-malli": kaavio_malli, "virhe-kaavio": virhe_kaavio,
           "valinta-a": valinta_a, "valinta-b": valinta_b, "valinta-c": valinta_c}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "hero": "decorative",
    "piiri": "reveals: the parts of a closed circuit and the conventional current direction (a theory figure)",
    "johdin": "reveals: electrons drift opposite to the conventional current (a theory figure)",
    "symbolit": "reveals: the IEC symbols with their names (a theory figure)",
    "kaavio": "reveals: the diagram of two cells, a switch and a lamp in one loop (a theory figure)",
    "virta": "reveals: the current as charge through a cross-section per time (a theory figure)",
    "jannite": "reveals: 1,5 V means 1,5 J per coulomb (a theory figure)",
    "virta-kuvaaja": "safe: a (t, I) graph, 0,40 A for 0–20 s, 0,10 A for 20–50 s, then 0; the charge is not shown",
    "kaavio-malli": "reveals: the model diagram of two cells, a switch, a lamp and an ammeter in one loop (an answer)",
    "virhe-kaavio": "safe: a student's diagram whose lamp is connected only to the + terminal; the error is not marked",
    "valinta-a": "safe: a cell, two lamps and a switch in one loop",
    "valinta-b": "safe: a cell, two rectangles (resistor symbols) and a switch in one loop",
    "valinta-c": "safe: a cell and two lamps in one loop, the switch on a dead-end branch",
}
