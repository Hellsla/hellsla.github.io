"""Figures of the FY9 unit fy9-tasavirta (scripts/figlib.py, herolib.py); `python3 scripts/units.py figures fy9-tasavirta`
writes them into content/fi/units/fy9-tasavirta/unit.md. The unit is Finnish, so the decimal sign is a comma.
Circuit diagrams use the IEC symbols of FY6 (lessons/FY6/fy6-5/figures.py): a resistor is a rectangle, a source two
plates (long +, short -), a lamp a circle with a cross; conventional current from + to - as violet arrows (#7048e8).

hero        the Why scene: a red summer cottage by a lake at dusk, one window lit, a solar panel on a stand in the yard
            with its cable to a battery box at the wall, a cool box on the porch steps, spruces, a birch, a jetty
            with a rowing boat and the lit window reflected in the water (no text, no people)
kartta      the concept map of the review: the circuit at the top, then current and resistance, connections,
            power and energy, and the source, each with three laws
mokki       the hook answered: the 12 V battery with the LED lights (6,0 W) and the cool box (48 W) in parallel;
            the currents 0,50 A and 4,0 A join into 4,5 A
piiri       the source model for "Johda itse": a battery (dashed box) as an emf E and an internal resistance R_s in
            series, its terminals connected to an external resistor R; the current I and the terminal voltage U
napa        the source model as a graph: the terminal voltage falls linearly with the current, from E on the U axis
            to the short-circuit current on the I axis; the slope is -R_s (schematic, no numbers)
"""
import math
import figlib
from figlib import (Fig, Axes, INK, MUTED, WHITE, RULE, RULE_LIGHT, GLASS, SAND_LIGHT, SAND, HEAT, HEAT_LIGHT, HOT,
                    COLD, COLD_LIGHT, WATER, WATER_LIGHT, IRON, METAL_EDGE, ALUMINIUM, COPPER, GOOD, n, fi)
import herolib as H

figlib.set_language({}, ",")

CUR = "#7048e8"     # conventional current (FY6: violet)

# the hook (computed here and quoted in unit.md and inquiry.json)
U_BAT = 12.0                 # V
P_LED, P_BOX = 6.0, 48.0     # W
I_LED, I_BOX = P_LED / U_BAT, P_BOX / U_BAT     # 0,50 A and 4,0 A
I_ALL = I_LED + I_BOX                           # 4,5 A
Q_BAT = 100.0                # Ah
T_ALL, T_LED = Q_BAT / I_ALL, Q_BAT / I_LED     # 22,2 h and 200 h


# --- circuit pieces (as in lessons/FY6/fy6-5/figures.py) ------------------------------------------------------
def wire(f, *pts):
    f.add('<polyline points="' + " ".join(f"{n(x)},{n(y)}" for x, y in pts) + f'" fill="none" stroke="{INK}" '
          'stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>')


def resistor(f, x, y, vertical=False, length=64, width=24):
    w, h = (width, length) if vertical else (length, width)
    f.rect(x - w / 2, y - h / 2, w, h, WHITE, INK, 3)


def lamp(f, x, y, r=20):
    f.circle(x, y, r, WHITE, INK, 3)
    d = r * 0.7071
    f.line(x - d, y - d, x + d, y + d, INK, 3); f.line(x - d, y + d, x + d, y - d, INK, 3)


def source(f, x, y, gap=16):
    f.line(x - 26, y - gap / 2, x + 26, y - gap / 2, INK, 3)
    f.line(x - 13, y + gap / 2, x + 13, y + gap / 2, INK, 7)


def node(f, x, y): f.circle(x, y, 6, INK)


def current_head(f, x, y, d):
    s = 10
    pts = {"r": [(x + s, y), (x - s, y - s * 0.8), (x - s, y + s * 0.8)], "l": [(x - s, y), (x + s, y - s * 0.8), (x + s, y + s * 0.8)],
           "d": [(x, y + s), (x - s * 0.8, y - s), (x + s * 0.8, y - s)], "u": [(x, y - s), (x - s * 0.8, y + s), (x + s * 0.8, y + s)]}[d]
    f.path("M" + " L".join(f"{n(a)},{n(b)}" for a, b in pts) + " Z", CUR)


# --- hero -----------------------------------------------------------------------------------------------------
def hero():
    """A red summer cottage by a lake at dusk. The sky fades from deep blue to a warm band at the horizon, a crescent
    moon and a few stars; the far shore is a dark line of spruces. The cottage stands on the near shore, its windows
    lit warm yellow; on a stand in the yard a solar panel faces the last light, its cable running to a grey battery box
    at the wall. A blue cool box sits on the porch steps. A jetty runs into the lake with a rowing boat beside it."""
    f = H.hero("fy9tv-hero", "Kuvitus: punainen kesämökki järven rannalla iltahämärässä. Taivas on ylhäällä tummansininen ja "
               "taivaanrannassa lämpimän oranssi, ja siellä on kuunsirppi ja muutama tähti. Mökin ikkunoista loistaa lämmin "
               "keltainen valo. Pihalla on telineen varassa aurinkopaneeli, jonka johto "
               "kulkee mökin seinällä olevaan harmaaseen akkulaatikkoon. Kuistin portailla on sininen kylmälaukku. Rannassa "
               "on laituri ja soutuvene, taustalla vastarannan kuusimetsä, ja mökin vieressä kasvaa koivu ja kuusia.")
    # the sky and the moon
    f.rect(0, 0, 1200, 380, H.grad(f, "fy9tv-sky", "#2c3a6b", "#f2a65a", y1=0, y2=380))
    for k in range(26):
        x, y = H.rnd(k, 4) * 1200, H.rnd(k + 300, 4) * 170
        f.circle(x, y, 1.2 + 1.4 * H.rnd(k + 700, 4), WHITE)
    f.path("M1021.5,50 A34,34 0 1 0 1021.5,114 A36,36 0 0 1 1021.5,50 Z", "#fff3bf")
    # the far shore and the lake
    H.forest(f, 372, 46, 26, "#26372f", seed=3)
    f.rect(0, 380, 1200, 220, H.grad(f, "fy9tv-lake", "#46618c", "#1e2f48"))
    for k in range(9):
        y = 396 + k * 22
        f.line(60 + 90 * H.rnd(k, 2), y, 260 + 120 * H.rnd(k + 40, 2), y, "#7d93b8", 2, cap="round")
        f.line(820 + 80 * H.rnd(k + 80, 2), y, 1000 + 110 * H.rnd(k + 90, 2), y, "#7d93b8", 2, cap="round")
    # the near shore: a grassy bank under the cottage
    f.path("M0,452 Q180,420 360,428 Q560,436 760,446 Q860,452 920,500 Q960,560 1000,600 L0,600 Z", "#3e6b47")
    f.path("M0,470 Q200,446 420,454 Q760,476 860,520 Q900,560 930,600 L0,600 Z", "#355d3e")
    # the cottage
    x0, yb, w, h = 300, 440, 330, 150
    H.red_house(f, x0, yb, w, h)
    for k in range(int((w - 40) / 70)):
        wx = x0 + 30 + k * 70
        f.rect(wx + 3, yb - h * 0.72 + 3, 34, h * 0.4 - 6, H.grad(f, f"fy9tv-win{k}", "#fff3bf", "#ffc078"))
        f.line(wx + 20, yb - h * 0.72, wx + 20, yb - h * 0.32, WHITE, 3)
        f.rect(wx, yb - h * 0.72, 40, h * 0.4, "none", INK, 2)
    f.add(f'<ellipse cx="{x0 + w / 2}" cy="{yb - h * 0.52}" rx="200" ry="70" fill="#ffd43b" fill-opacity="0.10"/>')
    # porch steps and the cool box
    f.rect(x0 + w - 70, yb, 80, 12, "#c9a46a", INK, 2)
    f.rect(x0 + w - 60, yb + 12, 90, 12, "#c9a46a", INK, 2)
    f.rect(x0 + w - 48, yb - 34, 56, 34, COLD, INK, 2.5, 5)
    f.rect(x0 + w - 52, yb - 42, 64, 12, WHITE, INK, 2.5, 4)
    f.rect(x0 + w - 30, yb - 50, 20, 8, WHITE, INK, 2, 3)
    # the battery box on the wall, left of the windows
    f.rect(x0 + 14, yb - 50, 44, 34, ALUMINIUM, INK, 2.5, 4)
    f.rect(x0 + 20, yb - 58, 8, 8, INK); f.rect(x0 + 44, yb - 58, 8, 8, HOT)
    # the solar panel on its stand in the yard, left of the cottage, and its cable to the battery box
    px, py = 120, 352
    f.line(px + 20, py + 46, px + 10, 448, IRON, 6, cap="round")
    f.line(px + 120, py + 10, px + 136, 446, IRON, 6, cap="round")
    f.path(f"M{px},{py + 52} L{px + 40},{py - 34} L{px + 168},{py - 52} L{px + 140},{py + 28} Z", "#1f3b6e", INK, 3)
    for t in (0.25, 0.5, 0.75):
        a = (px + 40 * t, py + 52 - 86 * t); b = (px + 140 + 28 * t, py + 28 - 80 * t)
        f.line(a[0], a[1], b[0], b[1], "#5c7cb5", 1.5)
    for t in (0.2, 0.4, 0.6, 0.8):
        a = (px + 140 * t, py + 52 - 24 * t); b = (px + 40 + 128 * t, py - 34 - 18 * t)
        f.line(a[0], a[1], b[0], b[1], "#5c7cb5", 1.5)
    f.path(f"M{px + 136},{py + 40} Q{px + 170},{yb - 6} {x0 + 14},{yb - 26}", "none", INK, 3)
    # trees: spruces at the left edge and behind the cottage's right corner, a birch beside the porch
    H.spruce(f, 46, 462, 210, "#2f5d3a")
    H.spruce(f, 690, 452, 230, "#2f5d3a")
    H.birch(f, 790, 470, 170)
    # the jetty and the rowing boat
    f.path("M840,476 L1110,500 L1110,512 L840,490 Z", "#b08850", INK, 2.5)
    for x in (880, 960, 1040, 1100): f.line(x, 480 + (x - 840) * 0.09, x, 540 + (x - 840) * 0.09, "#6b4f2e", 5)
    f.path("M1000,540 Q1060,566 1150,548 L1162,532 Q1080,540 990,528 Z", "#e9e4d8", INK, 2.5)
    f.line(1040, 538, 1110, 536, IRON, 3)
    return f.svg()


# --- the concept map ------------------------------------------------------------------------------------------
def kartta():
    """The concept map, stacked for a phone: the circuit at the top, a spine down the left and four boxes, each with
    the MAFY laws of its topic and a grey word beside each (teacher 2026-11-12: only MAFY's formulas; a result the
    exam asks to derive is a "Johda itse" task in the text, not a row of the map)."""
    groups = [
        ("virta ja resistanssi", "suureet", [(r"I = \Delta Q/\Delta t", "virta"), (r"U = RI", "Ohm"), (r"R = \rho \ell/A", "johdin")]),
        ("kytkennät", "Kirchhoff", [(r"R_\text{kok} = \Sigma R", "sarja"), (r"1/R_\text{kok} = \Sigma 1/R", "rinnan"), (r"\Sigma \Delta V = 0", "silmukka")]),
        ("teho ja energia", "Joule", [(r"P = UI", "teho"), (r"P = W/\Delta t", "energia")]),
        ("lähde", "paristo, akku", [(r"\Sigma \Delta V = 0", "napajännite"), (r"I = \Delta Q/\Delta t", "kapasiteetti")]),
    ]
    hub_y, hub_h, x_box, top, spine, gap = 8, 72, 44, 100, 24, 16
    heights = [56 + 50 * len(rows) for _, _, rows in groups]
    f = Fig("fy9tv-kartta", top + sum(heights) + gap * (len(groups) - 1) + 8, "Käsitekartta. Ylhäällä solmu tasavirtapiiri: jännite U, virta I ja resistanssi R. Siitä lähtee alas neljä "
            "haaraa. Virta ja resistanssi, piirin suureet: virta I = delta Q per delta t, Ohmin laki U = R I ja johtimen "
            "resistanssi R = rho l per A. Kytkennät, Kirchhoffin lait: sarjaankytkentä R kok = summa R, rinnankytkentä 1 per "
            "R kok = summa 1 per R ja silmukan potentiaalin muutosten summa nolla. Teho ja energia, Joulen laki: P = U I ja "
            "P = W per delta t. Lähde, paristo ja akku: napajännite silmukan potentiaalin muutosten summasta ja akun "
            "kapasiteetti virran I = delta Q per delta t avulla.", width=380, size=20)
    ys = [top + sum(heights[:k]) + gap * k for k in range(len(groups))]
    f.line(spine, hub_y + hub_h, spine, ys[-1] + 22, RULE, 3)
    f.rect(8, hub_y, 364, hub_h, SAND_LIGHT, SAND, 2.5, 12)
    f.tex(190, hub_y + 22, r"\text{tasavirtapiiri}", "middle", INK)
    f.tex(190, hub_y + 51, r"U,\ I,\ R", "middle", INK)
    for (head, sub, rows), y, gh in zip(groups, ys, heights):
        f.line(spine, y + 22, x_box, y + 22, RULE, 3)
        f.rect(x_box, y, 372 - x_box, gh, WHITE, MUTED, 2, 10)
        f.tex(x_box + 14, y + 22, r"\textbf{" + head + "}", "start", INK)
        f.tex(362, y + 22, r"\text{" + sub + "}", "end", MUTED, size=17)
        f.line(x_box + 10, y + 42, 362, y + 42, RULE_LIGHT, 1.5)
        for j, (law, word) in enumerate(rows):
            yy = y + 68 + j * 50
            f.tex(x_box + 14, yy, law, "start", INK, size=18 if len(law) > 16 else None)
            f.tex(362, yy, r"\text{" + word + "}", "end", MUTED, size=17)
    return f.svg()


# --- the hook answered ----------------------------------------------------------------------------------------
def mokki():
    """The cottage circuit: the 12 V battery on the left, the LED lights (a lamp) and the cool box (a resistor) in
    parallel; violet currents 4,5 A in the main wire, 0,50 A and 4,0 A in the branches. Not to scale."""
    f = Fig("fy9tv-mokki", 356, "Kytkentäkaavio, ei mittakaavassa. Vasemmalla 12 voltin akku, plusnapa ylhäällä. Akkuun on kytketty "
            "rinnan kaksi haaraa: LED-valot, joiden teho on 6,0 wattia, ja kylmälaukku, jonka teho on 48 wattia. Violetit "
            "virtanuolet: akun plusnavasta lähtee 4,5 ampeerin virta, joka jakautuu haarautumispisteessä 0,50 ampeerin virraksi "
            "LED-valoihin ja 4,0 ampeerin virraksi kylmälaukkuun. Haarojen virrat yhtyvät alajohtimessa ja palaavat akun "
            "miinusnapaan.", size=24)
    xb, x1, x2, yt, ybt, yc = 60, 250, 410, 70, 320, 195
    wire(f, (xb, yc - 8), (xb, yt), (x2, yt), (x2, yc - 32))
    wire(f, (x2, yc + 32), (x2, ybt), (xb, ybt), (xb, yc + 8))
    wire(f, (x1, yt), (x1, yc - 20)); wire(f, (x1, yc + 20), (x1, ybt))
    source(f, xb, yc)
    f.tex(xb + 34, yc - 22, r"+", "start", INK, size=24)
    f.tex(xb + 36, yc + 18, r"12\,\text{V}", "start", INK)
    node(f, x1, yt); node(f, x1, ybt)
    lamp(f, x1, yc)
    resistor(f, x2, yc, vertical=True)
    f.tex(x1 + 32, yc - 16, r"\text{LED}", "start", INK)
    f.tex(x1 + 32, yc + 18, r"6{,}0\,\text{W}", "start", INK)
    f.tex(x2 + 26, yc - 16, r"\text{kylmälaukku}", "start", INK)
    f.tex(x2 + 26, yc + 18, r"48\,\text{W}", "start", INK)
    current_head(f, (xb + x1) / 2, yt, "r")
    f.tex((xb + x1) / 2, yt - 30, r"4{,}5\,\text{A}", "middle", CUR)
    current_head(f, x1, yc + 72, "d")
    f.tex(x1 - 14, yc + 72, r"0{,}50\,\text{A}", "end", CUR)
    current_head(f, x2, yc + 72, "d")
    f.tex(x2 - 14, yc + 72, r"4{,}0\,\text{A}", "end", CUR)
    current_head(f, (xb + x1) / 2, ybt, "l")
    f.tex((xb + x1) / 2, ybt + 24, r"4{,}5\,\text{A}", "middle", CUR)
    return f.svg()


# --- the source model, for "Johda itse" ------------------------------------------------------------------------
def piiri():
    """The battery as a model: inside a dashed box the emf E (a source symbol) and the internal resistance R_s in
    series, the terminals + and - on the box's right edge, the voltage U between them; the external resistor R is
    connected to the terminals, and the violet current I runs from + through R back to -. No numbers."""
    f = Fig("fy9tv-piiri", 330, "Kytkentäkaavio, ei lukuarvoja. Vasemmalla katkoviivalaatikko, paristo. Sen sisällä on "
            "sarjassa lähdejännite E, piirretty jännitelähteen merkillä, ja sisäinen resistanssi R s, piirretty vastuksena. "
            "Laatikon oikeassa reunassa ovat pariston navat, plusnapa ylhäällä ja miinusnapa alhaalla, ja niiden välissä "
            "napajännite U. Napoihin on kytketty ulkoinen vastus R. Violetti virta I kulkee plusnavasta vastuksen R kautta "
            "takaisin miinusnapaan.", size=24)
    xs, xt, xR, yt, yb = 150, 310, 470, 60, 290
    f.rect(50, 28, xt - 50, 254, "none", MUTED, 2.5, 12, extra='stroke-dasharray="9 7"')
    f.tex(64, 262, r"\text{paristo}", "start", MUTED, size=18)
    wire(f, (xs, 130), (xs, yt), (xt, yt), (xR, yt), (xR, 140))
    wire(f, (xR, 220), (xR, yb - 30), (xt, yb - 30), (xs, yb - 30), (xs, 240))
    source(f, xs, 150)
    f.tex(xs + 34, 134, r"+", "start", INK, size=22)
    f.tex(xs - 34, 150, r"E", "end", INK)
    resistor(f, xs, 205, vertical=True, length=56)
    f.tex(xs - 26, 205, r"R_\text{s}", "end", INK)
    node(f, xt, yt); node(f, xt, yb - 30)
    f.tex(xt + 14, yt + 24, r"+", "start", INK, size=22)
    f.tex(xt + 14, yb - 30 - 24, r"-", "start", INK, size=22)
    f.arrow(xt - 30, yb - 44, xt - 30, yt + 14, MUTED, 2.5, 12)
    f.tex(xt - 42, (yt + yb - 30) / 2, r"U", "end", MUTED)
    resistor(f, xR, 180, vertical=True, length=80)
    f.tex(xR + 24, 180, r"R", "start", INK)
    current_head(f, (xt + xR) / 2, yt, "r")
    f.tex((xt + xR) / 2, yt - 26, r"I", "middle", CUR)
    current_head(f, (xt + xR) / 2, yb - 30, "l")
    return f.svg()


# --- the source as a graph ------------------------------------------------------------------------------------
def napa():
    """The terminal voltage against the current: a falling straight line from E on the U axis to I_k on the I axis,
    with a slope triangle Delta I, Delta U. Schematic: no numbers on the axes."""
    f = Fig("fy9tv-napa", 380, "Kaavakuva, ei lukuarvoja: pariston napajännite U virran I funktiona. Laskeva suora alkaa "
            "pystyakselilta lähdejännitteen E kohdalta ja leikkaa vaaka-akselin oikosulkuvirran I k kohdalla. Suoralle on "
            "piirretty kulmakertoimen kolmio, jonka vaakasivu on delta I ja pystysivu delta U; kulmakerroin on miinus R s. "
            "Suoran yläpäässä, pienillä virroilla, napajännite on lähes E.", size=24)
    ax = Axes(f, (80, 320), (470, 60), x=(0, 10), y=(0, 6), xticks=[], yticks=[], xlabel=r"I", ylabel=r"U", grid=False,
              origin_label=True)
    E, Ik = 5.0, 9.0
    line = lambda i: E - E / Ik * i
    ax.line([(0, E), (Ik, 0)], INK, 3)
    f.circle(ax.X(0), ax.Y(E), 6, COLD); f.tex(ax.X(0) - 12, ax.Y(E), r"E", "end", COLD)
    f.circle(ax.X(Ik), ax.Y(0), 6, HOT); f.tex(ax.X(Ik), ax.Y(0) + 26, r"I_\text{k}", "middle", HOT)
    a, b = 2.5, 6.0
    f.line(ax.X(a), ax.Y(line(a)), ax.X(b), ax.Y(line(a)), MUTED, 2, "6 5")
    f.line(ax.X(b), ax.Y(line(a)), ax.X(b), ax.Y(line(b)), MUTED, 2, "6 5")
    f.tex((ax.X(a) + ax.X(b)) / 2, ax.Y(line(a)) - 20, r"\Delta I", "middle", MUTED)
    f.tex(ax.X(b) + 12, (ax.Y(line(a)) + ax.Y(line(b))) / 2, r"\Delta U", "start", MUTED)
    f.tex(ax.X(5.6), ax.Y(4.6), r"\text{kulmakerroin } {-R_\text{s}}", "start", INK)
    return f.svg()


FIGURES = {"hero": hero, "kartta": kartta, "mokki": mokki, "piiri": piiri, "napa": napa}
REUSE = {"kartta": "reveals: the key laws of FY6 direct-current circuits, power and sources",
         "mokki": "reveals: 0,50 A + 4,0 A = 4,5 A from a 12 V battery to 6,0 W and 48 W in parallel",
         "piiri": "safe: the source model E and R_s in series with an external R, no numbers",
         "napa": "safe: the (I, U) line of a source with E, I_k and the slope -R_s, no numbers"}
