"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy6-3` writes them into lesson.md.
Circuit diagrams use the IEC symbols (resistor a rectangle, lamp a circle with a cross, meters circles with A and V);
conventional current I is violet everywhere (figures and simulation), from + to −."""
import math
from figlib import (Fig, Axes, fi, INK, MUTED, WHITE, RULE, RULE_LIGHT, HEAT, HEAT_LIGHT, COLD, COLD_LIGHT, ALUMINIUM,
                    METAL_EDGE, COPPER, SAND, SAND_LIGHT, SAND_DARK, GLASS, n)
import herolib as H

CURRENT = "#7048e8"          # conventional current I (its own colour, NOTES §3)
LAMP = HEAT                  # the lamp's characteristic: the hot filament
R_RES, RK, RN, UN = 10.0, 1.0, 12.0, 3.0      # the simulation's resistor and lamp (lesson-answers.py)


def lamp_I(U):
    return U / (RK + (RN - RK) * (U / UN) ** 0.6) if U > 0 else 0.0


# ---- small circuit helpers (IEC symbols), only for this lesson ----
def wire(f, pts, w=2.5):
    f.path("M" + " L".join(f"{n(x)},{n(y)}" for x, y in pts), stroke=INK, w=w)


def node(f, x, y):
    f.circle(x, y, 5, INK)


def meter(f, cx, cy, letter, r=22):
    f.circle(cx, cy, r, WHITE, INK, 2.5)
    f.tex(cx, cy, r"\text{" + letter + "}", "middle", w=30)


def resistor_v(f, x, y0, y1, w=26):
    """A resistor on a vertical wire between y0 and y1 (the wire is broken there)."""
    f.rect(x - w / 2, y0, w, y1 - y0, WHITE, INK, 2.5)


def cell_v(f, x, y, long_top=True):
    """A battery on a vertical wire: the long plate (+) above, the short plate (−) below, centred on y."""
    f.rect(x - 22, y - 9, 44, 4, INK)          # long plate
    f.rect(x - 11, y + 5, 22, 6, INK)          # short, thick plate


def current_arrow(f, x, y, direction):
    """A filled arrowhead on a wire, pointing right / left / up / down."""
    d = {"right": (1, 0), "left": (-1, 0), "down": (0, 1), "up": (0, -1)}[direction]
    ux, uy = d; px, py = -uy, ux
    tip = (x + ux * 9, y + uy * 9); b1 = (x - ux * 9 + px * 8, y - uy * 9 + py * 8); b2 = (x - ux * 9 - px * 8, y - uy * 9 - py * 8)
    f.path(f"M{n(tip[0])},{n(tip[1])} L{n(b1[0])},{n(b1[1])} L{n(b2[0])},{n(b2[1])} Z", CURRENT)


def measure_circuit():
    f = Fig("fy63-mc", 350, "Kytkentäkaavio resistanssin mittaamiseen, periaatekuva. Paristo, virtamittari ja vastus R ovat "
            "samassa virtapiirissä peräkkäin eli sarjassa, joten virtamittarin läpi kulkee sama virta I kuin vastuksen läpi. "
            "Jännitemittari on kytketty vastuksen napoihin eli rinnan vastuksen kanssa, ja se mittaa vastuksen jännitteen U. "
            "Violetit nuolet näyttävät virran suunnan pariston plusnavasta piirin kautta miinusnapaan.")
    L, R, T, B = 90, 400, 90, 250
    wire(f, [(L, 162), (L, T), (223, T)])
    meter(f, 245, T, "A")
    wire(f, [(267, T), (R, T), (R, 135)])
    resistor_v(f, R, 135, 205)
    wire(f, [(R, 205), (R, B), (L, B), (L, 178)])
    cell_v(f, L, 167)
    f.tex(L - 30, 152, "+", "end", w=24)
    f.tex(L - 30, 188, "-", "end", w=24)
    # the voltmeter across the resistor
    node(f, R, 115); node(f, R, 225)
    wire(f, [(R, 115), (500, 115), (500, 148)], 2)
    wire(f, [(R, 225), (500, 225), (500, 192)], 2)
    meter(f, 500, 170, "V")
    f.tex(374, 170, "R", "end", w=26)
    f.tex(532, 170, "U", "start", w=26)
    # conventional current, + to −
    current_arrow(f, 150, T, "right")
    current_arrow(f, 340, T, "right")
    current_arrow(f, 245, B, "left")
    f.tex(150, T - 26, "I", "middle", CURRENT, w=24)
    f.tex(245, B + 26, "I", "middle", CURRENT, w=24)
    f.tex(245, 50, r"\text{virtamittari}", "middle")
    f.tex(500, 262, r"\text{jännitemittari}", "middle")
    f.line(12, 296, 588, 296, RULE_LIGHT, 1.5)
    f.tex(300, 324, r"I = \text{virta},\ U = \text{jännite},\ R = \text{resistanssi}", "middle", w=420)
    return f.svg()


def micro():
    f = Fig("fy63-micro", 330, "Kaavakuva metallilangan sisältä, ei mittakaavassa. Positiiviset metalli-ionit ovat säännöllisessä "
            "hilassa, ja vapaat elektronit kulkevat niiden lomassa vasemmalle, kun sovittu virran suunta on oikealle. "
            "Vasemmassa paneelissa lanka on huoneenlämpöinen: ionit värähtelevät vähän, ja elektroni törmää harvoin. "
            "Oikeassa paneelissa lanka on kuuma: ionit värähtelevät voimakkaasti, mitä kuvaavat leveämmät renkaat, ja "
            "elektronin reitti katkeaa useammin törmäyksiin. Kuuman langan resistanssi on suurempi.")
    f.line(300, 14, 300, 316, RULE, 2, "6 6")
    for k, (x0, hot) in enumerate(((22, False), (322, True))):
        f.tex(x0 + 128, 26, r"\text{huoneenlämpöinen}" if not hot else r"\text{kuuma lanka}", "middle")
        f.rect(x0, 52, 256, 178, ALUMINIUM, METAL_EDGE, 2.5, 14)
        for i in range(5):
            for j in range(3):
                cx, cy = x0 + 32 + 48 * i, 86 + 55 * j
                if hot: f.add(f'<circle cx="{cx}" cy="{cy}" r="21" fill="{HEAT_LIGHT}" fill-opacity="0.55"/>')
                else: f.add(f'<circle cx="{cx}" cy="{cy}" r="15" fill="{WHITE}" fill-opacity="0.5"/>')
                f.circle(cx, cy, 11, METAL_EDGE, INK, 1.5)
                f.line(cx - 5, cy, cx + 5, cy, WHITE, 2); f.line(cx, cy - 5, cx, cy + 5, WHITE, 2)
        # one electron's path: straight stretches between collisions, from right to left
        pts = ([(x0 + 244, 112), (x0 + 170, 120), (x0 + 120, 106), (x0 + 40, 118)] if not hot else
               [(x0 + 244, 112), (x0 + 214, 128), (x0 + 186, 104), (x0 + 152, 126), (x0 + 120, 102), (x0 + 88, 128), (x0 + 58, 106), (x0 + 30, 120)])
        f.path("M" + " L".join(f"{n(a)},{n(b)}" for a, b in pts), stroke=COLD, w=2, extra='stroke-dasharray="5 4"')
        for a, b in pts[1:-1]:
            f.circle(a, b, 3, COLD)
        f.circle(pts[-1][0], pts[-1][1], 7, COLD, WHITE, 2)
        for i, (ex, ey) in enumerate(((x0 + 60, 168), (x0 + 156, 196), (x0 + 210, 160), (x0 + 108, 64))):
            f.circle(ex, ey, 6, COLD, WHITE, 1.5)
        # below the wire: electrons drift left, the conventional current points right
        f.arrow(x0 + 116, 252, x0 + 30, 252, COLD, 3, 13)
        f.tex(x0 + 124, 252, r"\text{elektronit}", "start", COLD)
        f.arrow(x0 + 140, 286, x0 + 226, 286, CURRENT, 3, 13)
        f.tex(x0 + 132, 286, "I", "end", CURRENT, w=24)
    return f.svg()


def curves():
    f = Fig("fy63-curves", 360, "Kuvaaja mittakaavassa: jännite U voltteina virran I funktiona ampeereina. Vastuksen "
            "ominaiskäyrä on origon kautta kulkeva suora, joka kulkee pisteen (0,30 A; 3,0 V) kautta, joten sen resistanssi "
            "on 10 ohmia joka kohdassa. Hehkulampun ominaiskäyrä on kaareva: pienillä jännitteillä se nousee loivasti ja "
            "suurilla jyrkästi, ja jännitteellä 3,0 V lampun virta on 0,25 A. Katkoviiva origosta lampun pisteeseen "
            "kuvaa lampun resistanssia U : I = 12 ohmia tällä jännitteellä. Ruudukon väli on 0,05 A ja 0,5 V.")
    ax = Axes(f, (96, 306), (464, 56), x=(0, 0.35), y=(0, 3.5), xticks=[0.05 * k for k in range(1, 8)],
              yticks=[0.5 * k for k in range(1, 8)], xlabel=r"I\ (\text{A})", ylabel=r"U\ (\text{V})",
              xfmt=lambda v: fi(round(v, 2)) if round(v * 100) % 10 == 0 else "",
              yfmt=lambda v: fi(round(v, 1)) if round(v * 10) % 10 == 0 else "")
    ax.line([(0, 0), (0.325, 3.25)], INK, 3)
    pts = [(lamp_I(3.0 * k / 120), 3.0 * k / 120) for k in range(121)]
    ax.line(pts, LAMP, 3)
    ax.line([(0, 0), (0.25, 3.0)], MUTED, 1.5, "6 5")
    ax.point(0.25, 3.0, LAMP)
    ax.point(0.30, 3.0, INK)
    f.tex(ax.X(0.325) + 8, ax.Y(3.25), r"\text{vastus}", "start")
    f.tex(ax.X(0.25) - 14, ax.Y(3.0) - 10, r"\text{hehkulamppu}", "end", LAMP)
    return f.svg()


def cylinder(f, x, y, length, r, gid):
    """A wire seen from the side: a copper cylinder with its cut face (the cross-section A) at the left end."""
    f.rect(x, y - r, length, 2 * r, f"url(#{gid})")
    f.line(x, y - r, x + length, y - r, INK, 2); f.line(x, y + r, x + length, y + r, INK, 2)
    f.add(f'<ellipse cx="{n(x + length)}" cy="{n(y)}" rx="{n(r * 0.42)}" ry="{n(r)}" fill="{COPPER}" stroke="{INK}" stroke-width="2"/>')
    f.add(f'<ellipse cx="{n(x)}" cy="{n(y)}" rx="{n(r * 0.42)}" ry="{n(r)}" fill="{HEAT_LIGHT}" stroke="{INK}" stroke-width="2"/>')


def wire_fig():
    f = Fig("fy63-wire", 340, "Kaavakuva kolmesta saman aineen langasta, pituudet mittakaavassa. Ylimpänä lanka, jonka pituus on l "
            "ja poikkipinta-ala A, ja sen resistanssi on R. Keskellä kaksi kertaa pidempi lanka, jonka poikkipinta-ala on "
            "sama: resistanssi on 2R. Alimpana yhtä pitkä lanka, jonka poikkipinta-ala on kaksinkertainen: resistanssi on "
            "puolet eli R jaettuna kahdella. Poikkipinta on korostettu oranssilla langan vasemmassa päässä.")
    f.defs_add(f'<linearGradient id="fy63-cu" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{HEAT_LIGHT}"/>'
               f'<stop offset="0.4" stop-color="{COPPER}"/><stop offset="1" stop-color="{COPPER}"/></linearGradient>')
    x0, L = 96, 190
    rows = [(62, L, 12, "A", "l", "R"), (166, 2 * L, 12, "A", "2l", "2R"), (272, L, 12 * math.sqrt(2), "2A", "l", r"\dfrac{R}{2}")]
    for y, length, r, a_lab, l_lab, r_lab in rows:
        cylinder(f, x0, y, length, r, "fy63-cu")
        f.tex(x0 - 18, y, a_lab, "end", w=40)
        # the length as a dimension line under the wire
        yd = y + r + 18
        f.line(x0, yd - 7, x0, yd + 7, MUTED, 1.5); f.line(x0 + length, yd - 7, x0 + length, yd + 7, MUTED, 1.5)
        f.arrow(x0 + length / 2 - 20, yd, x0 + 2, yd, MUTED, 1.5, 10); f.arrow(x0 + length / 2 + 20, yd, x0 + length - 2, yd, MUTED, 1.5, 10)
        f.tex(x0 + length / 2, yd, l_lab, "middle", bg=True, w=36)
        f.tex(x0 + length + 22, y, r_lab, "start", w=60)
    return f.svg()


def lamp_curve():
    """Task figure: the lamp's characteristic alone, U against I, on a 0,05 A / 0,5 V grid. No values marked: the
    student reads the current at a given voltage off the curve (at 1,0 V it is 0,15 A)."""
    f = Fig("fy63-lampcurve", 340, "Kuvaaja mittakaavassa: hehkulampun jännite U voltteina virran I funktiona ampeereina. "
            "Käyrä alkaa origosta, nousee aluksi loivasti ja sitten yhä jyrkemmin ja päättyy pisteeseen (0,25 A; 3,0 V). "
            "Ruudukon väli on 0,05 A ja 0,5 V.")
    ax = Axes(f, (96, 290), (464, 54), x=(0, 0.30), y=(0, 3.0), xticks=[0.05 * k for k in range(1, 7)],
              yticks=[0.5 * k for k in range(1, 7)], xlabel=r"I\ (\text{A})", ylabel=r"U\ (\text{V})",
              xfmt=lambda v: fi(round(v, 2)) if round(v * 100) % 10 == 0 else "",
              yfmt=lambda v: fi(round(v, 1)) if round(v * 10) % 10 == 0 else "")
    ax.line([(lamp_I(3.0 * k / 120), 3.0 * k / 120) for k in range(121)], LAMP, 3)
    return f.svg()


PTS = [(0.020, 0.47), (0.040, 0.86), (0.060, 1.34), (0.080, 1.74), (0.100, 2.21)]   # measured (I in A, U in V)


def resistor_points():
    """Task figure: five measured points of a resistor, (I, U), with small scatter; no line drawn, so the student fits
    one through the origin (the best line passes (0,100 A; 2,20 V), slope 22 Ω)."""
    f = Fig("fy63-points", 330, "Kuvaaja mittakaavassa: vastuksen mittauspisteet, jännite U voltteina virran I funktiona "
            "ampeereina. Pisteet ovat (0,020 A; 0,47 V), (0,040 A; 0,86 V), (0,060 A; 1,34 V), (0,080 A; 1,74 V) ja "
            "(0,100 A; 2,21 V). Suoraa ei ole piirretty. Ruudukon väli on 0,01 A ja 0,25 V.")
    ax = Axes(f, (96, 284), (464, 52), x=(0, 0.12), y=(0, 2.5), xticks=[0.01 * k for k in range(1, 13)],
              yticks=[0.25 * k for k in range(1, 11)], xlabel=r"I\ (\text{A})", ylabel=r"U\ (\text{V})",
              xfmt=lambda v: fi(round(v, 2)) if round(v * 100) % 4 == 0 else "",
              yfmt=lambda v: fi(round(v, 1)) if round(v * 100) % 50 == 0 else "")
    for a, b in PTS:
        ax.point(a, b, INK)
    return f.svg()


def hero():
    """The chapter's opening illustration: a toaster glowing on a kitchen counter, plugged in through an extension cord."""
    f = H.hero("fy63-hero", "Kuvitus: keittiön työtaso. Leivänpaahdin on päällä, ja sen leipäaukoista hohtaa oranssi valo, "
               "kun ohuet lämmityslangat hehkuvat. Paahtimen johto on kytketty paksuun jatkojohtoon, joka kulkee pistorasiaan. "
               "Jatkojohto ei hehku.")
    H.tiles(f, 400, 80, RULE_LIGHT, WHITE)
    # wall socket on the left
    f.rect(96, 196, 104, 104, WHITE, INK, 3, 14)
    f.circle(148, 248, 32, RULE_LIGHT, INK, 2.5)
    f.circle(136, 248, 5, INK); f.circle(160, 248, 5, INK)
    # counter: worktop and cabinet doors
    f.rect(0, 400, 1200, 34, H.grad(f, "fy63h-top", SAND_LIGHT, SAND), INK, 3)
    f.rect(0, 434, 1200, 166, SAND_DARK)
    for x in (20, 420, 820):
        f.rect(x, 452, 360, 160, SAND_LIGHT, INK, 3, 8)
        f.rect(x + 160, 476, 40, 10, METAL_EDGE, INK, 2, 4)
    # the extension cord: a thick cable from the wall socket over the counter to its socket box
    f.path("M148,282 C150,340 170,392 230,404 C300,418 330,392 372,396", stroke=INK, w=16, extra='stroke-linecap="round"')
    f.path("M148,282 C150,340 170,392 230,404 C300,418 330,392 372,396", stroke=MUTED, w=8, extra='stroke-linecap="round"')
    f.rect(360, 366, 120, 38, WHITE, INK, 3, 8)
    f.circle(392, 385, 9, RULE_LIGHT, INK, 2); f.circle(448, 385, 9, RULE_LIGHT, INK, 2)
    # the toaster's own thin cord
    f.path("M448,385 C470,372 500,380 520,392", stroke=INK, w=6, extra='stroke-linecap="round"')
    # glow from the slots
    f.add(f'<ellipse cx="700" cy="196" rx="190" ry="96" fill="{H.glow(f, "fy63h-glow")}" fill-opacity="0.75"/>')
    # bread slices in the slots
    for x in (604, 712):
        f.path(f"M{x},218 V150 Q{x},126 {x + 22},124 Q{x + 42},112 {x + 62},124 Q{x + 84},126 {x + 84},150 V218 Z", SAND_LIGHT, SAND, 4)
    # toaster body (brushed steel), its slots and a dark window showing the glowing heating wires
    f.rect(520, 210, 360, 190, H.steel(f, "fy63h-steel"), INK, 3, 34)
    f.rect(590, 206, 112, 18, INK, rx=6); f.rect(698, 206, 112, 18, INK, rx=6)
    f.rect(586, 262, 228, 84, INK, INK, 3, 12)
    for k in range(4):
        y = 278 + 18 * k
        d = f"M600,{y}" + "".join(f" L{612 + 12 * j},{y + (6 if j % 2 == 0 else -6)}" for j in range(17))
        f.path(d, stroke=HEAT, w=4, extra='stroke-linecap="round"')
        f.path(d, stroke=HEAT_LIGHT, w=1.5, extra='stroke-linecap="round"')
    # the lever and the dial
    f.rect(878, 270, 30, 18, INK, rx=4)
    f.circle(560, 372, 13, WHITE, INK, 2.5)
    f.rect(546, 398, 30, 10, INK, rx=3); f.rect(824, 398, 30, 10, INK, rx=3)
    # heat shimmer above the slots
    for x in (640, 700, 760):
        f.path(f"M{x},104 q-10,-14 0,-28 t0,-28", stroke=HEAT, w=4, extra='stroke-linecap="round" stroke-opacity="0.7"')
    return f.svg()


# Graph choice of task fy6-3-L1-09: four (I, U) graphs on one grid, R = 2,0 kΩ given and Ohm's law holding; only
# "pick-k2" is right (U = 2,0 kΩ · I: 8,0 V at 4,0 mA). The names say the drawn line or curve, not the answer.
PICK_DESC = ("(I,U)-kuvaaja mittakaavassa: vaaka-akselilla virta I milliampeereina nollasta viiteen milliampeeriin, apuviivat "
             "0,5 mA:n välein ja lukuarvot milliampeerin välein; pystyakselilla jännite U voltteina nollasta 12 volttiin, "
             "apuviivat voltin välein ja lukuarvot kahden voltin välein. ")


def pick_axes(fid, label):
    """One option of the graph choice: the same (I, U) axes, I 0–5 mA and U 0–12 V, for every option."""
    f = Fig(fid, 360, PICK_DESC + label)
    a = Axes(f, (96, 320), (464, 54), x=(0, 5.0), y=(0, 12.0), xticks=[0.5 * k for k in range(1, 11)],
             yticks=list(range(1, 13)), xlabel=r"I\ (\text{mA})", ylabel=r"U\ (\text{V})",
             xfmt=lambda v: fi(v) if float(v).is_integer() else "", yfmt=lambda v: fi(v) if v % 2 == 0 else "")
    return f, a


def pick_graph(fid, label, pts):
    """The option's line or curve, in the same colour and weight for every option."""
    f, a = pick_axes(fid, label)
    a.line(pts, INK, 3.5)
    return f.svg()


def pick_k2():
    return pick_graph("fy63-pick-k2", "Origosta lähtevä nouseva suora kulkee pisteiden (2,0 mA; 4,0 V) ja (4,0 mA; 8,0 V) "
                      "kautta ja päättyy pisteeseen (4,5 mA; 9,0 V).", [(0, 0), (4.5, 9.0)])


def pick_k05():
    """The slope inverted: R taken as I : U, 0,5 V per mA."""
    return pick_graph("fy63-pick-k05", "Origosta lähtevä loivasti nouseva suora kulkee pisteen (4,0 mA; 2,0 V) kautta ja "
                      "päättyy pisteeseen (4,5 mA; 2,25 V).", [(0, 0), (4.5, 2.25)])


def pick_curve():
    """Not ohmic: U = 0,5 V · (I / mA)², so U : I = 2,0 kΩ only at 4,0 mA and the resistance grows with the voltage."""
    return pick_graph("fy63-pick-curve", "Origosta lähtevä käyrä nousee aluksi loivasti ja sitten yhä jyrkemmin. Se kulkee "
                      "pisteiden (2,0 mA; 2,0 V) ja (4,0 mA; 8,0 V) kautta ja päättyy pisteeseen (4,5 mA; noin 10,1 V).",
                      [(4.5 * k / 60, 0.5 * (4.5 * k / 60) ** 2) for k in range(61)])


def pick_flat():
    """The resistance's number drawn as a value of U instead of the slope."""
    return pick_graph("fy63-pick-flat", "Vaakasuora suora kulkee jännitteen 2,0 V kohdalla virrasta 0 mA virtaan 4,5 mA.",
                      [(0, 2.0), (4.5, 2.0)])


FIGURES = {"hero": hero, "measure-circuit": measure_circuit, "micro": micro, "curves": curves, "wire": wire_fig,
           "lamp-curve": lamp_curve, "resistor-points": resistor_points,
           "pick-k2": pick_k2, "pick-k05": pick_k05, "pick-curve": pick_curve, "pick-flat": pick_flat}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "measure-circuit": "safe: how ammeter (series) and voltmeter (parallel) are connected to measure R",
    "micro": "reveals: a hot wire has a larger resistance",
    "curves": "reveals: the lamp's curve bends and its R at 3,0 V is 12 Ω; the resistor is a straight line of 10 Ω",
    "wire": "reveals: R doubles with length and halves with cross-section",
    "lamp-curve": "safe: a lamp's U–I curve on a grid, no values marked (0,15 A at 1,0 V, 0,25 A at 3,0 V)",
    "resistor-points": "safe: five measured U–I points of a resistor, no line (best line 22 Ω)",
    "pick-k2": "reveals: the right option of task fy6-3-L1-09 (R = 2,0 kΩ: U = 8,0 V at 4,0 mA)",
    "pick-k05": "safe: a wrong option of task fy6-3-L1-09 (the slope inverted, R taken as I : U)",
    "pick-curve": "safe: a wrong option of task fy6-3-L1-09 (U : I = 2,0 kΩ at one point only, not ohmic)",
    "pick-flat": "safe: a wrong option of task fy6-3-L1-09 (the number of R drawn as a constant voltage)",
}
