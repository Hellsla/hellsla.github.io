"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy6-5` writes them into lesson.md.
Circuit diagrams with IEC symbols: resistor a rectangle, source two plates (long +, short −), meters circles with
their letter; conventional current from + to − as violet arrows (#7048e8, as in the other FY6 chapters); potentials in blue; every label LaTeX."""
from figlib import Fig, Axes, fi, INK, MUTED, WHITE, RULE, RULE_LIGHT, HEAT, HEAT_LIGHT, COLD, COLD_LIGHT, GLASS, ICE, \
    ALUMINIUM, METAL_EDGE, IRON, GOOD, GOOD_LIGHT, SAND, SAND_LIGHT, WATER_LIGHT, n
import herolib as H

CUR = "#7048e8"     # current arrows and their labels (FY6: conventional current is violet)
POT = COLD          # potentials (labels, the potential graph)


# --- circuit pieces -------------------------------------------------------------------------------------------
def wire(f, *pts):
    f.add('<polyline points="' + " ".join(f"{n(x)},{n(y)}" for x, y in pts) + f'" fill="none" stroke="{INK}" '
          'stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>')


def resistor(f, x, y, vertical=False, length=64, width=24):
    """A resistor centred on (x, y): a white rectangle over the wire."""
    w, h = (width, length) if vertical else (length, width)
    f.rect(x - w / 2, y - h / 2, w, h, WHITE, INK, 3)


def source(f, x, y, gap=16):
    """A source on a vertical wire at x, centred on y: the long thin plate (+) above, the short thick plate (−) below.
    The wire is drawn up to the plates by the caller."""
    f.line(x - 26, y - gap / 2, x + 26, y - gap / 2, INK, 3)
    f.line(x - 13, y + gap / 2, x + 13, y + gap / 2, INK, 7)


def node(f, x, y):
    f.circle(x, y, 6, INK)


def meter(f, x, y, letter):
    f.circle(x, y, 20, WHITE, INK, 3)
    f.tex(x, y, r"\text{" + letter + "}", "middle", w=30)


def current_head(f, x, y, d):
    """A filled current arrowhead on a wire at (x, y) pointing in direction d (r, l, u, d)."""
    s = 10
    pts = {"r": [(x + s, y), (x - s, y - s * 0.8), (x - s, y + s * 0.8)], "l": [(x - s, y), (x + s, y - s * 0.8), (x + s, y + s * 0.8)],
           "d": [(x, y + s), (x - s * 0.8, y - s), (x + s * 0.8, y - s)], "u": [(x, y - s), (x - s * 0.8, y + s), (x + s * 0.8, y + s)]}[d]
    f.path("M" + " L".join(f"{n(a)},{n(b)}" for a, b in pts) + " Z", CUR)


def new(fid, h, label):
    f = Fig(fid, h, label)
    f.wcover = 10
    return f


# --- Ydinajatus: the current law at a junction ---------------------------------------------------------------
def junction(values=True):
    """A junction: I1 = 0,30 A comes in from the left, splits into two branches through 30 ohm and 60 ohm.
    values=False: the variant for the prediction, branch currents as question marks and arrows of equal width."""
    lab = ("Kaavakuva haarautumispisteestä, ei mittakaavassa. Vasemmalta johdinta pitkin tulee virta I1 = 0,30 A "
           "haarautumispisteeseen. Siitä lähtee kaksi haaraa: ylähaarassa on 30 ohmin vastus ja alahaarassa 60 ohmin vastus, "
           "ja haarat yhtyvät oikealla uudelleen. ")
    lab += ("Violettien virtanuolten leveys on verrannollinen virtaan: ylähaarassa I2 = 0,20 A, alahaarassa I3 = 0,10 A, "
            "ja yhteensä haaroista lähtee yhtä paljon virtaa kuin pisteeseen tulee, 0,30 A." if values else
            "Haarojen virtoja ei ole merkitty, vaan niiden kohdalla on kysymysmerkki.")
    f = new("fy65-junction" + ("" if values else "-q"), 330, lab)
    jx, jy, ky, ly, ex = 200, 170, 72, 268, 520
    wire(f, (24, jy), (jx, jy)); wire(f, (jx, jy), (jx, ky), (ex, ky), (ex, ly), (jx, ly), (jx, jy))
    wire(f, (ex, jy), (576, jy))
    resistor(f, 380, ky); resistor(f, 380, ly)
    node(f, jx, jy); node(f, ex, jy)
    f.tex(380, ky + 34, r"30\,\Omega", "middle")
    f.tex(380, ly - 34, r"60\,\Omega", "middle")
    # block arrows whose width is the current: 0,30 A = 24 units
    f.block_arrow(40, jy - 30, 150, jy - 30, CUR, 24, 40, 26)
    f.tex(100, jy - 62, r"I_1 = 0{,}30\,\text{A}", "middle", CUR, w=170)
    if values:
        f.block_arrow(230, ky - 28, 320, ky - 28, CUR, 16, 32, 22)
        f.block_arrow(230, ly + 28, 320, ly + 28, CUR, 8, 22, 18)
        f.tex(334, ky - 30, r"I_2 = 0{,}20\,\text{A}", "start", CUR, w=170)
        f.tex(334, ly + 30, r"I_3 = 0{,}10\,\text{A}", "start", CUR, w=170)
    else:
        f.arrow(230, ky - 28, 320, ky - 28, CUR, 3, 16)
        f.arrow(230, ly + 28, 320, ly + 28, CUR, 3, 16)
        f.tex(334, ky - 30, r"I_2 = \,?", "start", CUR, w=110)
        f.tex(334, ly + 30, r"I_3 = \,?", "start", CUR, w=110)
    f.tex(jx + 16, jy, r"\text{haarautumispiste}", "start", w=230)
    return f.svg()


# --- the simulation's circuit with its points and potentials --------------------------------------------------
TOP, BOT, XS, XR1, XB, XJ, XR3 = 90, 280, 72, 196, 286, 330, 470


def sim_circuit(f, pots=True):
    """The circuit of the simulation: source 9,0 V, R1 = 10 ohm, then R2 = 30 ohm and R3 = 60 ohm in parallel."""
    ym = (TOP + BOT) / 2
    wire(f, (XS, ym - 8), (XS, TOP), (XR3, TOP), (XR3, BOT), (XS, BOT), (XS, ym + 8))
    wire(f, (XJ, TOP), (XJ, BOT))
    source(f, XS, ym)
    resistor(f, XR1, TOP); resistor(f, XJ, ym, True); resistor(f, XR3, ym, True)
    node(f, XJ, TOP); node(f, XJ, BOT)
    f.tex(XS - 34, ym - 18, "+", "middle", w=24)
    f.tex(XS - 34, ym + 22, "-", "middle", w=24)
    f.tex(XS + 28, ym, r"U = 9{,}0\,\text{V}", "start", w=150)
    f.tex(XR1, TOP + 36, r"R_1 = 10\,\Omega", "middle", w=140)
    f.tex(XJ + 22, ym - 18, r"R_2", "start", w=40); f.tex(XJ + 22, ym + 18, r"30\,\Omega", "start", w=64)
    f.tex(XR3 + 22, ym - 18, r"R_3", "start", w=40); f.tex(XR3 + 22, ym + 18, r"60\,\Omega", "start", w=64)
    pts = [("A", 112, TOP, "9{,}0"), ("B", XB, TOP, "6{,}0"), ("C", XR3, TOP, "6{,}0"),
           ("D", XR3, BOT, "0"), ("E", XJ, BOT, "0"), ("F", 112, BOT, "0")]
    for name, x, y, v in pts:
        up = y == TOP
        f.circle(x, y, 5, WHITE, INK, 2.5)
        f.tex(x, y - 24 if up else y + 24, name, "middle", w=28)
        if pots: f.tex(x, y - 56 if up else y + 56, v + r"\,\text{V}", "middle", POT, w=80)


def circuit():
    f = new("fy65-circuit", 368, "Kytkentäkaavio, ei mittakaavassa: jännitelähde 9,0 V, sen plusnavalta vastus R1 = 10 ohmia ja "
            "sen jälkeen kaksi rinnakkaista vastusta R2 = 30 ohmia ja R3 = 60 ohmia, jotka palaavat lähteen miinusnapaan. "
            "Johtimiin on merkitty pisteet A–F ja niiden potentiaalit, kun lähteen miinusnapa on nollakohta: A 9,0 V, "
            "B ja C 6,0 V sekä D, E ja F 0 V. Saman johtimen kaikissa kohdissa potentiaali on sama; se muuttuu vain "
            "lähteessä ja vastuksissa.")
    sim_circuit(f)
    return f.svg()


def circuit_q():
    """The circuit of the prediction (ennuste-2): the points A-F, the voltmeter with its black lead on the minus pole's
    wire and a red probe lead, no potentials written."""
    f = new("fy65-circuit-q", 404, "Kytkentäkaavio, ei mittakaavassa: jännitelähde 9,0 V, sen plusnavalta vastus R1 = 10 ohmia ja "
            "sen jälkeen kaksi rinnakkaista vastusta R2 = 30 ohmia ja R3 = 60 ohmia, jotka palaavat lähteen miinusnapaan. "
            "Johtimiin on merkitty pisteet A–F: A heti plusnavan jälkeen, B ja C vastuksen R1 jälkeen, D ja E vastusten "
            "R2 ja R3 alapuolella ja F miinusnavan johtimessa. Jännitemittarin musta johto on kiinni miinusnavan johtimessa, "
            "ja punainen johto on vapaa kosketettavaksi eri kohtiin. Potentiaaleja ei ole merkitty.")
    sim_circuit(f, pots=False)
    my, bx, rx = 366, 330, 430
    f.circle(150, BOT, 6, INK)
    f.add(f'<polyline points="{bx - 20},{my} 150,{my} 150,{BOT}" fill="none" stroke="{INK}" stroke-width="2.5" '
          'stroke-linejoin="round" stroke-linecap="round"/>')
    f.add(f'<polyline points="{bx + 20},{my} {rx},{my} {rx},{BOT + 50}" fill="none" stroke="#c92a2a" stroke-width="2.5" '
          'stroke-linejoin="round" stroke-linecap="round"/>')
    f.path(f"M{rx},{BOT + 38} L{rx - 7},{BOT + 52} L{rx + 7},{BOT + 52} Z", "#c92a2a")
    meter(f, bx, my, "V")
    f.tex(240, my - 22, r"\text{musta}", "middle", w=90)
    f.tex(rx + 14, my - 22, r"\text{punainen}", "start", w=120)
    return f.svg()


# --- Kaava: the potential graph of the loop through R1 and R2 --------------------------------------------------
def pot_graph(fid, label, path, ticks, regions, ymax, yticks, steps=None, every=1):
    """A potential graph along a loop: path = [(position, V)], ticks = [(position, letter)],
    regions = [(x0, x1, tex)] shaded and named above the plot."""
    f = new(fid, 360, label)
    ax = Axes(f, (96, 290), (500, 70), x=(0, path[-1][0]), y=(0, ymax), xticks=[], yticks=yticks,
              xlabel=r"\text{kohta}", ylabel=r"V\ (\text{V})", grid=True, origin_label=False,
              yfmt=lambda v: fi(v) if v % every == 0 else "")
    for x0, x1, t in regions:
        f.rect(ax.X(x0), ax.Y(ymax), ax.X(x1) - ax.X(x0), ax.Y(0) - ax.Y(ymax), GLASS)
        f.tex((ax.X(x0) + ax.X(x1)) / 2, ax.Y(ymax) + 16, t, "middle", w=44)
    for t in yticks:                    # the gridlines again over the shaded parts
        f.line(97, ax.Y(t), 500, ax.Y(t), RULE_LIGHT, 1.5)
    f.tex(84, 284, "0", "end")
    ax.line(path, POT, 3)
    for x, name in ticks:
        f.line(ax.X(x), 290, ax.X(x), 297, INK, 2)
        f.tex(ax.X(x), 318, name, "middle", w=28)
    for x, v in path:
        if any(abs(x - t[0]) < 1e-9 for t in ticks):
            ax.point(x, v, POT, 5.5)
    for x, y, t in steps or []:
        f.tex(ax.X(x) + 8, ax.Y(y), t, "start", INK, w=110)
    return f.svg()


def potential_graph():
    path = [(0, 0), (1, 0), (1, 9), (2, 9), (3, 9), (4, 6), (5, 6), (6, 6), (7, 0), (8, 0), (9, 0)]
    return pot_graph("fy65-pgraph", "Potentiaalikuvaaja, pystyakseli mittakaavassa, vaaka-akseli kaavamainen: potentiaali V "
                     "volteissa, kun kierretään kuvan virtapiirin silmukka lähteen miinusnavasta F lähteen ja vastusten R1 ja R2 "
                     "kautta takaisin F:ään. Lähteessä potentiaali nousee 0 voltista 9,0 volttiin. Johdinta pitkin pisteeseen A se "
                     "pysyy 9,0 voltissa, vastuksessa R1 se laskee 3,0 V arvoon 6,0 V pisteessä B ja vastuksessa R2 6,0 V nollaan "
                     "pisteessä E. Pisteestä E pisteeseen F potentiaali pysyy nollassa. Nousujen ja laskujen summa on nolla.",
                     path, [(0, "F"), (2, "A"), (5, "B"), (8, "E"), (9, "F")],
                     [(0.7, 1.3, r"U"), (3, 4, r"R_1"), (6, 7, r"R_2")], 11, [3, 6, 9],
                     [(1.0, 4.5, r"+9{,}0\,\text{V}"), (4.0, 7.5, r"-3{,}0\,\text{V}"), (7.0, 3.0, r"-6{,}0\,\text{V}")])


def ex_graph():
    """Task figure (L1-05): a series loop of three resistors on 9,0 V, the potential graph on 1 V gridlines, no values written."""
    path = [(0, 0), (1, 0), (1, 9), (2, 9), (3, 7), (4, 7), (5, 3), (6, 3), (7, 0), (8, 0)]
    return pot_graph("fy65-exgraph", "Potentiaalikuvaaja, pystyakseli mittakaavassa, vaaka-akseli kaavamainen: sarjaankytkentä, "
                     "jossa on jännitelähde ja kolme vastusta R1, R2 ja R3. Potentiaali V volteissa, ruudukon väli 1 V. Lähteen "
                     "miinusnavalla potentiaali on 0 V, ja lähteessä se nousee 9 volttiin pisteessä A. Vastuksessa R1 se laskee "
                     "pisteen B arvoon 7 V, vastuksessa R2 pisteen C arvoon 3 V ja vastuksessa R3 nollaan pisteessä D.",
                     path, [(0, "D"), (2, "A"), (4, "B"), (6, "C"), (8, "D")],
                     [(0.7, 1.3, r"U"), (2, 3, r"R_1"), (4, 5, r"R_2"), (6, 7, r"R_3")], 11, [1, 2, 3, 4, 5, 6, 7, 8, 9], every=2)


# --- task circuits ---------------------------------------------------------------------------------------------
def two_branches(fid, label, U, r_series, r2, r3, ammeter):
    """A source on the left, an ammeter (and an optional series resistor) on the top wire, two resistors in parallel."""
    f = new(fid, 340, label)
    top, bot, xs, xa, xr1, xj, xr3 = 86, 286, 80, 168, 260, 370, 510
    ym = (top + bot) / 2
    wire(f, (xs, ym - 8), (xs, top), (xr3, top), (xr3, bot), (xs, bot), (xs, ym + 8))
    wire(f, (xj, top), (xj, bot))
    source(f, xs, ym)
    f.tex(xs - 34, ym - 18, "+", "middle", w=24); f.tex(xs - 34, ym + 22, "-", "middle", w=24)
    f.tex(xs + 28, ym, U, "start", w=130)
    meter(f, xa, top, "A")
    f.tex(xa, top - 40, ammeter, "middle", w=170)
    current_head(f, xa + 44, top, "r")
    if r_series:
        resistor(f, xr1, top)
        f.tex(xr1 + 6, top + 36, r_series, "middle", w=150)
    node(f, xj, top); node(f, xj, bot)
    resistor(f, xj, ym, True); resistor(f, xr3, ym, True)
    f.tex(xj + 22, ym - 18, r"R_2", "start", w=40); f.tex(xj + 22, ym + 18, r2, "start", w=70)
    f.tex(xr3 + 22, ym - 18, r"R_3", "start", w=40); f.tex(xr3 + 22, ym + 18, r3, "start", w=70)
    return f.svg()


def ex_branch():
    return two_branches("fy65-exbranch", "Kytkentäkaavio: 6,0 voltin jännitelähde, jonka pääjohtimessa on virtamittari. Lähteeseen on "
                        "kytketty rinnan kaksi vastusta, R2 = 20 ohmia ja R3 = 30 ohmia. Virtamittarin lukemaa ei ole merkitty.",
                        r"U = 6{,}0\,\text{V}", None, r"20\,\Omega", r"30\,\Omega", r"I = \,?")


def ex_branch2():
    return two_branches("fy65-exbranch2", "Kytkentäkaavio: 12 voltin jännitelähde, pääjohtimessa virtamittari, joka näyttää 0,20 A, ja "
                        "vastus R1 = 40 ohmia. Sen jälkeen rinnan vastus R2 = 60 ohmia ja vastus R3, jonka resistanssia ei tunneta.",
                        r"U = 12\,\text{V}", r"R_1 = 40\,\Omega", r"60\,\Omega", r"?", r"I_1 = 0{,}20\,\text{A}")


# --- opening illustration: birds on a power line ---------------------------------------------------------------
def bird(f, x, y, sc=1.0, flip=False):
    """A small perching bird whose feet stand on the line at (x, y)."""
    s = -1 if flip else 1
    X = lambda dx: n(x + s * dx * sc)
    Y = lambda dy: n(y + dy * sc)
    f.line(x - 5 * sc, y, x - 5 * sc, y - 12 * sc, INK, 2 * sc); f.line(x + 5 * sc, y, x + 5 * sc, y - 12 * sc, INK, 2 * sc)
    f.path(f"M{X(-26)},{Y(-30)} Q{X(-24)},{Y(-12)} {X(0)},{Y(-11)} Q{X(22)},{Y(-12)} {X(24)},{Y(-34)} "
           f"Q{X(20)},{Y(-46)} {X(6)},{Y(-44)} Q{X(-10)},{Y(-44)} {X(-26)},{Y(-30)} Z", IRON, INK, 2)
    f.path(f"M{X(-26)},{Y(-30)} L{X(-46)},{Y(-22)} L{X(-42)},{Y(-34)} Z", INK)
    f.circle(x + s * 26 * sc, y - 44 * sc, 12 * sc, IRON, INK, 2)
    f.path(f"M{X(36)},{Y(-46)} L{X(46)},{Y(-42)} L{X(36)},{Y(-40)} Z", H.HEAT)
    f.circle(x + s * 29 * sc, y - 47 * sc, 2.5 * sc, WHITE)
    f.path(f"M{X(-12)},{Y(-30)} Q{X(4)},{Y(-22)} {X(18)},{Y(-30)}", stroke=METAL_EDGE, w=2.5 * sc)


def hero():
    f = H.hero("fy65-hero", "Kuvitus: suurjännitelinja peltomaiseman yllä kesäpäivänä. Kahden ristikkopylvään välissä riippuu "
               "johtimet, ja yhdellä johtimella istuu rivissä neljä pikkulintua. Taustalla on metsän reuna ja "
               "kumpuileva pelto.")
    H.sky(f, "fy65h")
    H.sun(f, "fy65h", 1020, 110, 50)
    H.cloud(f, 300, 110, 1.0); H.cloud(f, 760, 70, 0.7)
    H.hills(f, "fy65h", 400, [GOOD_LIGHT], amp=46, seed=4)
    H.forest(f, 402, 50, 24, GOOD, seed=6)
    f.rect(0, 430, 1200, 170, H.grad(f, "fy65h-field", SAND_LIGHT, SAND, y1=430, y2=600))
    for k in range(9):
        f.path(f"M{-60 + k * 150},600 L{240 + k * 150},430", stroke=SAND, w=3, extra='stroke-opacity="0.6"')
    left = H.pylon(f, 150, 470, 360, 1.25)
    right = H.pylon(f, 1080, 470, 360, 1.25)
    for (a, b) in zip(left, right):
        H.wire(f, (a[0] + 4, a[1]), (b[0] - 4, b[1]), sag=70, colour=INK, w=3)
    # the birds on the lower right conductor: the quadratic's points at t
    a, b = left[1], right[1]
    a = (a[0] + 4, a[1]); b = (b[0] - 4, b[1])
    mx, my = (a[0] + b[0]) / 2, (a[1] + b[1]) / 2 + 70
    for k, t in enumerate((0.38, 0.44, 0.52, 0.60)):
        x = (1 - t) ** 2 * a[0] + 2 * (1 - t) * t * mx + t * t * b[0]
        y = (1 - t) ** 2 * a[1] + 2 * (1 - t) * t * my + t * t * b[1]
        bird(f, x, y, 1.15, flip=(k == 2))
    return f.svg()


FIGURES = {"hero": hero, "junction": junction, "junction-q": lambda: junction(False), "circuit": circuit, "circuit-q": circuit_q,
           "potential-graph": potential_graph, "ex-graph": ex_graph, "ex-branch": ex_branch, "ex-branch2": ex_branch2}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "junction": "reveals: how 0,30 A splits into 0,20 A and 0,10 A through 30 and 60 ohm",
    "junction-q": "safe: a junction with 0,30 A in and branches of 30 and 60 ohm, branch currents unknown",
    "circuit": "reveals: the potentials of points A-F in the 9,0 V circuit with 10, 30 and 60 ohm",
    "circuit-q": "safe: the 9,0 V circuit with 10, 30 and 60 ohm, points A-F and a voltmeter, no potentials written",
    "potential-graph": "reveals: the potential graph of the 9,0 V circuit with its drops 3,0 V and 6,0 V",
    "ex-graph": "safe: a potential graph of a three-resistor series loop on 1 V gridlines, no drops written",
    "ex-branch": "safe: 6,0 V source with 20 and 30 ohm in parallel, ammeter reading unknown",
    "ex-branch2": "safe: 12 V source, ammeter 0,20 A, R1 = 40 ohm, then 60 ohm in parallel with an unknown R3",
}
