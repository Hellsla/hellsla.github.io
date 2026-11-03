"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy6-2` writes them into lesson.md.
Circuit diagrams with IEC symbols: a battery as a long thin (+) and a short thick (−) plate, a lamp as a circle with a
cross, a resistor as a rectangle, meters as circles with V or A; conventional current arrows from + to − in their own
colour (violet), every label in LaTeX."""
import math
from figlib import (Fig, INK, MUTED, WHITE, RULE, RULE_LIGHT, GLASS, HEAT_LIGHT, HEAT, ALUMINIUM, METAL_EDGE, IRON, COPPER,
                    SAND, SAND_LIGHT, SAND_DARK, GRAIN, HOT, PAPER, fi, n)
import herolib as H

CURRENT = "#7048e8"      # conventional current arrows (the palette's violet; FY6 has no momentum arrows)
LEAD_RED = HOT           # the meter's red lead, as on a real multimeter


# --- circuit symbols ---------------------------------------------------------------------------------------------
def wire(f, *pts, w=3):
    f.add(f'<polyline points="{" ".join(f"{n(x)},{n(y)}" for x, y in pts)}" fill="none" stroke="{INK}" stroke-width="{w}" '
          f'stroke-linejoin="round" stroke-linecap="round"/>')


def battery(f, cx, y):
    """A cell on a horizontal wire at (cx, y): + plate (long, thin) on the left, − plate (short, thick) on the right."""
    f.line(cx - 7, y - 24, cx - 7, y + 24, INK, 3)
    f.line(cx + 7, y - 12, cx + 7, y + 12, INK, 7)
    f.tex(cx - 18, y - 34, "+", "end")
    f.tex(cx + 18, y - 34, "-", "start")


def lamp(f, cx, cy, on, pre, r=20):
    if on:
        f.defs_add(f'<radialGradient id="{pre}-glow"><stop offset="0" stop-color="{HEAT_LIGHT}" stop-opacity="0.95"/>'
                   f'<stop offset="1" stop-color="{HEAT_LIGHT}" stop-opacity="0"/></radialGradient>')
        f.circle(cx, cy, r + 26, f"url(#{pre}-glow)")
    f.circle(cx, cy, r, WHITE, INK, 3)
    d = r * 0.7
    col = HEAT if on else INK
    f.line(cx - d, cy - d, cx + d, cy + d, col, 2.5)
    f.line(cx - d, cy + d, cx + d, cy - d, col, 2.5)


def meter(f, cx, cy, letter, r=22):
    f.circle(cx, cy, r, WHITE, INK, 3)
    f.tex(cx, cy, r"\text{" + letter + "}", "middle")


def current_arrow(f, x, y, dx, dy, label=None, side="start", big=False):
    """A filled arrowhead with a short shaft along a wire, pointing (dx, dy)."""
    L, w = (22, 10) if big else (16, 7)
    f.line(x - dx * 16, y - dy * 16, x, y, CURRENT, 5 if big else 3)
    f.path(f"M{n(x + dx * L)},{n(y + dy * L)} L{n(x - dy * w)},{n(y + dx * w)} L{n(x + dy * w)},{n(y - dx * w)} Z", CURRENT)
    if label:
        f.tex(x + (16 if side == "start" else -16), y, label, side, CURRENT)


def node(f, x, y):
    f.circle(x, y, 5, INK)


# --- figures -----------------------------------------------------------------------------------------------------
def connections():
    """Ammeter in series with the lamp (left), voltmeter across the lamp (right)."""
    f = Fig("fy62-conn", 344, "Kaksi kytkentäkaaviota. Vasemmalla paristo, lamppu ja virtamittari A ovat samassa silmukassa "
            "peräkkäin: virtamittari on sarjassa lampun kanssa, ja sama virta I kulkee pariston, mittarin ja lampun läpi. "
            "Oikealla paristo ja lamppu muodostavat silmukan, ja jännitemittari V on kytketty lampun napojen väliin "
            "lampun rinnalle. Violetit nuolet näyttävät virran suunnan pariston plusnavasta miinusnapaan.")
    f.line(300, 16, 300, 328, RULE, 2, "6 6")
    # left: battery at the bottom, ammeter and lamp on the top wire
    x0, x1, yt, yb = 40, 260, 100, 236
    wire(f, (138, yb), (x0, yb), (x0, yt), (78, yt)); wire(f, (122, yt), (174, yt)); wire(f, (214, yt), (x1, yt), (x1, yb), (162, yb))
    meter(f, 100, yt, "A")
    lamp(f, 194, yt, True, "fy62-c1")
    battery(f, 150, yb)
    current_arrow(f, x0, 176, 0, -1, "I")
    current_arrow(f, x1, 160, 0, 1)
    f.tex(150, 290, r"\text{virtamittari}", "middle")
    f.tex(150, 320, r"\text{sarjaan}", "middle")
    # right: battery at the bottom, lamp on the top wire, voltmeter bridging the lamp's terminals
    x0, x1 = 340, 560
    wire(f, (438, yb), (x0, yb), (x0, yt), (430, yt)); wire(f, (470, yt), (x1, yt), (x1, yb), (462, yb))
    lamp(f, 450, yt, True, "fy62-c2")
    wire(f, (398, yt), (398, 44), (428, 44)); wire(f, (472, 44), (502, 44), (502, yt))
    node(f, 398, yt); node(f, 502, yt)
    meter(f, 450, 44, "V")
    battery(f, 450, yb)
    current_arrow(f, x0, 176, 0, -1, "I")
    current_arrow(f, x1, 160, 0, 1)
    f.tex(450, 290, r"\text{jännitemittari}", "middle")
    f.tex(450, 320, r"\text{rinnalle}", "middle")
    return f.svg()


def multimeter():
    """A digital multimeter: display, selector with the ranges, jacks; callouts on the right."""
    f = Fig("fy62-dmm", 360, "Piirros digitaalisesta yleismittarista. Ylhäällä näyttö, jossa on lukema 1,500 V. Keskellä "
            "valitsin, jonka ympärillä ovat mittausalueet 2 V, 20 V, 200 mA ja 10 A; osoitin on alueella 2 V. Alhaalla "
            "kolme liitintä: COM, V mA ja 10 A. Mustan johdon paikka on COM ja punaisen V mA tai 10 A. Oikealla "
            "selitteet näyttö, valitsin ja liittimet.")
    bx, by, bw, bh = 52, 14, 256, 332
    f.rect(bx, by, bw, bh, ALUMINIUM, INK, 3, 22)
    f.rect(bx + 10, by + 10, bw - 20, bh - 20, IRON, None, 0, 14)
    f.rect(84, 34, 192, 78, RULE_LIGHT, INK, 2, 8)
    f.tex(222, 74, r"1{,}500", "end", size=40, w=150)
    f.tex(228, 82, r"\text{V}", "start")
    cx, cy, r = 180, 206, 32
    f.circle(cx, cy, r, METAL_EDGE, INK, 2.5)
    f.circle(cx, cy, 14, INK)
    ranges = [(-80, r"2\,\text{V}"), (-35, r"20\,\text{V}"), (35, r"200\,\text{mA}"), (80, r"10\,\text{A}")]
    for k, (deg, lab) in enumerate(ranges):
        a = math.radians(deg)
        f.line(cx + (r + 3) * math.sin(a), cy - (r + 3) * math.cos(a), cx + (r + 10) * math.sin(a), cy - (r + 10) * math.cos(a), WHITE, 2)
        f.tex(cx + 72 * math.sin(a), cy - 72 * math.cos(a), lab, "middle", HEAT_LIGHT if k == 0 else WHITE)
    a = math.radians(-80)
    f.line(cx, cy, cx + (r - 4) * math.sin(a), cy - (r - 4) * math.cos(a), WHITE, 5, cap="round")
    for k, (jx, lab) in enumerate(((110, r"\text{COM}"), (180, r"\text{V}\ \text{mA}"), (250, r"10\,\text{A}"))):
        f.circle(jx, 290, 12, INK, WHITE if k == 0 else LEAD_RED, 3)
        f.tex(jx, 322, lab, "middle", WHITE)
    for y, x_from, lab in ((73, 308, r"\text{näyttö}"), (206, 308, r"\text{valitsin}"), (290, 308, r"\text{liittimet}")):
        f.line(x_from + 4, y, 350, y, MUTED, 1.5)
        f.tex(358, y, lab, "start")
    return f.svg()


def wrong():
    """Two wrong connections: an ammeter across the lamp (left), a voltmeter in series (right)."""
    f = Fig("fy62-wrong", 352, "Kaksi väärää kytkentää. Vasemmalla virtamittari A on kytketty lampun rinnalle. Virta kulkee "
            "lähes kokonaan pienen resistanssin virtamittarin kautta, mitä kuvaa paksu violetti nuoli: lamppu ei pala, ja "
            "virta on suuri. Oikealla jännitemittari V on sarjassa lampun kanssa. Mittarin suuri resistanssi pienentää virran "
            "lähes nollaan, joten lamppu ei pala eikä virtanuolia ole.")
    f.line(300, 16, 300, 336, RULE, 2, "6 6")
    x0, x1, yt, yb = 40, 260, 112, 236
    wire(f, (138, yb), (x0, yb), (x0, yt), (130, yt)); wire(f, (170, yt), (x1, yt), (x1, yb), (162, yb))
    lamp(f, 150, yt, False, "fy62-w1")
    wire(f, (98, yt), (98, 50), (128, 50)); wire(f, (172, 50), (202, 50), (202, yt))
    node(f, 98, yt); node(f, 202, yt)
    meter(f, 150, 50, "A")
    current_arrow(f, 98, 84, 0, -1, None, big=True)
    current_arrow(f, 202, 76, 0, 1, None, big=True)
    battery(f, 150, yb)
    current_arrow(f, x0, 158, 0, -1, r"\text{suuri } I", big=True)
    f.tex(150, 298, r"\text{virtamittari}", "middle")
    f.tex(150, 328, r"\text{rinnalle}", "middle")
    x0, x1 = 340, 560
    wire(f, (438, yb), (x0, yb), (x0, yt), (378, yt)); wire(f, (422, yt), (464, yt)); wire(f, (504, yt), (x1, yt), (x1, yb), (462, yb))
    meter(f, 400, yt, "V")
    lamp(f, 484, yt, False, "fy62-w2")
    battery(f, 450, yb)
    f.tex(450, 156, r"I \approx 0", "middle")
    f.tex(450, 298, r"\text{jännitemittari}", "middle")
    f.tex(450, 328, r"\text{sarjaan}", "middle")
    return f.svg()


def error_bands():
    """The same lamp voltage read on the 20 V and the 2 V range, each reading with its error limit, to scale."""
    f = Fig("fy62-bands", 312, "Kuva mittakaavassa: jännitteen akseli välillä 1,46 V–1,54 V. Ylempi jana näyttää alueella 20 V "
            "saadun lukeman 1,50 V ja sen virherajan ±0,028 V eli välin 1,472 V–1,528 V. Alempi jana näyttää alueella 2 V "
            "saadun lukeman 1,500 V ja sen virherajan ±0,0095 V eli välin 1,4905 V–1,5095 V. Alemman alueen jana on noin "
            "kolmasosa ylemmän pituudesta.")
    x0, x1, lo, hi = 60, 540, 1.46, 1.54
    X = lambda u: x0 + (u - lo) / (hi - lo) * (x1 - x0)
    ya = 252
    for u in (1.47, 1.48, 1.49, 1.50, 1.51, 1.52, 1.53):
        f.line(X(u), 40, X(u), ya, RULE_LIGHT, 1.5)
    f.arrow(x0 - 20, ya, x1 + 26, ya, INK, 2.5, 13)
    for k, u in enumerate((1.46, 1.47, 1.48, 1.49, 1.50, 1.51, 1.52, 1.53, 1.54)):
        f.line(X(u), ya, X(u), ya + 7, INK, 2)
        if k % 2 == 0: f.tex(X(u), ya + 26, fi(round(u, 2), 2), "middle")
    f.tex(x1 + 10, ya - 26, r"U\ (\text{V})", "end")
    rows = [(78, 1.50, 0.0275, r"\text{alue } 20\,\text{V}", r"\pm 0{,}028\,\text{V}"),
            (176, 1.500, 0.0095, r"\text{alue } 2\,\text{V}", r"\pm 0{,}0095\,\text{V}")]
    for y, u, d, name, pm in rows:
        f.tex(x0, y - 36, name, "start")
        f.rect(X(u - d), y - 12, X(u + d) - X(u - d), 24, GLASS, INK, 2, 4)
        f.line(X(u - d), y - 20, X(u - d), y + 20, INK, 2.5)
        f.line(X(u + d), y - 20, X(u + d), y + 20, INK, 2.5)
        f.circle(X(u), y, 7, INK, WHITE, 2)
        f.tex(X(u + d) + 12, y, pm, "start")
    return f.svg()


def hero():
    """The chapter's opening illustration: a lab bench with a lamp circuit and a multimeter whose leads touch the lamp."""
    f = Fig("fy62-hero", 600, "Kuvitus: koulun laboratorion työpöytä. Pöydällä on kytkentälevy, jossa paristokotelo ja "
            "lampunpidike ovat johdoilla samassa piirissä, ja lamppu palaa. Vieressä on harmaa digitaalinen yleismittari, "
            "jonka punainen ja musta mittajohto koskettavat lampunpidikkeen kahta napaa.", width=1200, hero=True)
    # wall and the bench
    f.rect(0, 0, 1200, 600, PAPER)
    f.rect(0, 0, 1200, 330, H.grad(f, "fy62h-wall", GLASS, PAPER))
    for x in range(60, 1200, 180): f.rect(x, 60, 120, 150, WHITE, RULE_LIGHT, 3, 6)          # a pinboard of sheets
    f.rect(0, 330, 1200, 270, H.grad(f, "fy62h-bench", SAND_LIGHT, SAND))
    f.rect(0, 322, 1200, 16, SAND_DARK)
    for k in range(7):
        y = 360 + 34 * k
        f.path(f"M0,{y} C300,{y - 6} 700,{y + 8} 1200,{y - 2}", stroke=GRAIN, w=2, extra='stroke-opacity="0.35"')
    # the circuit board
    f.rect(250, 380, 470, 170, WHITE, INK, 3, 10)
    f.rect(262, 392, 446, 146, GLASS, None, 0, 6)
    # battery holder with three cells
    f.rect(290, 420, 190, 76, IRON, INK, 3, 8)
    for k in range(3):
        x = 302 + 58 * k
        f.rect(x, 432, 52, 52, COPPER, INK, 2.5, 6)
        f.rect(x + 40, 446, 12, 24, ALUMINIUM, INK, 2, 3)
    # lamp holder and the glowing lamp
    f.rect(570, 444, 100, 52, IRON, INK, 3, 8)
    f.circle(580, 470, 9, ALUMINIUM, INK, 2.5); f.circle(660, 470, 9, ALUMINIUM, INK, 2.5)
    f.defs_add(f'<radialGradient id="fy62h-glow"><stop offset="0" stop-color="{HEAT_LIGHT}" stop-opacity="0.95"/>'
               f'<stop offset="1" stop-color="{HEAT_LIGHT}" stop-opacity="0"/></radialGradient>')
    f.circle(620, 392, 110, "url(#fy62h-glow)")
    f.rect(600, 418, 40, 30, ALUMINIUM, INK, 3, 4)
    f.path("M592,420 C580,370 594,344 620,344 C646,344 660,370 648,420 Z", WHITE, INK, 3)
    f.path("M608,418 L612,388 L620,398 L628,388 L632,418", stroke=HEAT, w=3)
    # circuit wires on the board
    f.path("M480,458 C520,458 540,470 580,470", stroke=INK, w=6, extra='stroke-linecap="round"')
    f.path("M660,470 C700,470 700,530 520,530 C380,530 300,530 290,470", stroke=INK, w=6, extra='stroke-linecap="round"')
    # the multimeter, standing on the bench, right of the board
    f.rect(800, 210, 250, 350, ALUMINIUM, INK, 4, 26)
    f.rect(814, 224, 222, 322, IRON, None, 0, 18)
    f.rect(842, 248, 166, 74, "#e3dccb", INK, 3, 8)
    for k in range(4):                                                                 # display segments, no digits
        f.rect(858 + 36 * k, 266, 26, 38, "none", INK, 5, 3)
    f.circle(925, 410, 50, METAL_EDGE, INK, 3); f.circle(925, 410, 20, INK)
    f.line(925, 410, 900, 372, WHITE, 8, cap="round")
    for k, a in enumerate((-80, -35, 35, 80)):
        r = math.radians(a)
        f.line(925 + 58 * math.sin(r), 410 - 58 * math.cos(r), 925 + 72 * math.sin(r), 410 - 72 * math.cos(r), WHITE, 4)
    for k, x in enumerate((860, 925, 990)):
        f.circle(x, 508, 15, INK, WHITE if k == 0 else HOT, 4)
    # the leads from the meter to the lamp holder's terminals
    f.path("M860,508 C860,600 720,600 700,560 C686,530 662,510 662,486", stroke=INK, w=7, extra='stroke-linecap="round"')
    f.path("M925,508 C930,620 600,620 560,560 C540,530 574,500 578,486", stroke=HOT, w=7, extra='stroke-linecap="round"')
    f.rect(652, 474, 20, 30, INK, None, 0, 4); f.rect(568, 474, 20, 30, HOT, None, 0, 4)
    return f.svg()


FIGURES = {"hero": hero, "connections": connections, "multimeter": multimeter, "wrong": wrong, "error-bands": error_bands}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "connections": "safe: how an ammeter (series) and a voltmeter (across the lamp) are connected",
    "multimeter": "safe: a multimeter's display, selector ranges 2 V, 20 V, 200 mA, 10 A and jacks COM, V mA, 10 A",
    "wrong": "reveals: an ammeter across the lamp short-circuits it and a voltmeter in series stops the current",
    "error-bands": "reveals: the error limits ±0,028 V (20 V range) and ±0,0095 V (2 V range) of a 1,50 V reading",
}
