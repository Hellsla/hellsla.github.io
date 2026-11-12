"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy6-8` writes them into lesson.md.
Circuit diagrams with IEC symbols: a resistor is a rectangle, a cell a long thin (+) and a short thick (−) plate, a meter
a circle with its letter; wires orthogonal. A battery is drawn as its model: an ideal source E in series with the internal
resistance R_s inside a dashed outline. Conventional current from + to − in the external circuit, violet (#7048e8) as in
the other FY6 chapters; potentials and voltages blue; every label LaTeX. Numbers: lesson-answers.py."""
from figlib import (Fig, Axes, fi, INK, MUTED, WHITE, RULE, RULE_LIGHT, HEAT, HEAT_LIGHT, HOT, COLD, COLD_LIGHT, GLASS,
                    ICE, ALUMINIUM, METAL_EDGE, IRON, GOOD, n)
import herolib as H

CUR = "#7048e8"     # current arrows and their labels (FY6: conventional current is violet)
POT = COLD          # potentials and voltages


# --- circuit pieces -------------------------------------------------------------------------------------------
def wire(f, *pts, w=3):
    f.add('<polyline points="' + " ".join(f"{n(x)},{n(y)}" for x, y in pts) + f'" fill="none" stroke="{INK}" '
          f'stroke-width="{w:g}" stroke-linejoin="round" stroke-linecap="round"/>')


def resistor(f, x, y, vertical=False, length=60, width=24, fill=WHITE):
    w, h = (width, length) if vertical else (length, width)
    f.rect(x - w / 2, y - h / 2, w, h, fill, INK, 3)


def cell(f, x, y, gap=14, half=24):
    """The plates of an ideal source on a vertical wire at x, centred on y: long thin (+) above, short thick (−) below.
    The caller draws the wire up to y - gap/2 and from y + gap/2."""
    f.line(x - half, y - gap / 2, x + half, y - gap / 2, INK, 3)
    f.line(x - half / 2, y + gap / 2, x + half / 2, y + gap / 2, INK, 7)


def terminal(f, x, y):
    f.circle(x, y, 7, WHITE, INK, 3)


def node(f, x, y):
    f.circle(x, y, 6, INK)


def meter(f, x, y, letter):
    f.circle(x, y, 20, WHITE, INK, 3)
    f.tex(x, y, r"\text{" + letter + "}", "middle", w=30)


def head(f, x, y, d, colour=CUR):
    """A filled arrowhead on a wire at (x, y) pointing r, l, u or d."""
    s = 10
    pts = {"r": [(x + s, y), (x - s, y - s * 0.8), (x - s, y + s * 0.8)], "l": [(x - s, y), (x + s, y - s * 0.8), (x + s, y + s * 0.8)],
           "d": [(x, y + s), (x - s * 0.8, y - s), (x + s * 0.8, y - s)], "u": [(x, y - s), (x - s * 0.8, y + s), (x + s * 0.8, y + s)]}[d]
    f.path("M" + " L".join(f"{n(a)},{n(b)}" for a, b in pts) + " Z", colour)


def outline(f, x, y, w, h):
    """The dashed outline of a battery (its inside is the model, not a picture of the can)."""
    f.rect(x, y, w, h, GLASS, MUTED, 2, 12, extra='stroke-dasharray="8 6"')


def new(fid, h, label):
    f = Fig(fid, h, label)
    f.wcover = 10
    return f


# --- Ydinajatus: the model of a battery with a load --------------------------------------------------------------
def model():
    f = new("fy68-model", 344, "Kytkentäkaavio, ei mittakaavassa: pariston malli. Katkoviivalla rajatun pariston sisällä on "
            "ideaalinen jännitelähde, jonka lähdejännite on E, ja sen kanssa sarjassa sisäinen resistanssi Rs. Pariston plusnapa "
            "on oikealla ylhäällä ja miinusnapa oikealla alhaalla. Navoista johtimet kulkevat ulkoiseen kuormitusvastukseen R. "
            "Napojen väliin on kytketty jännitemittari, joka mittaa napajännitteen U. Violetit nuolet näyttävät virran I: "
            "ulkoisessa piirissä plusnavalta kuorman kautta miinusnavalle ja pariston sisällä miinusnavalta plusnavalle.")
    bx, by, bw, bh = 30, 58, 192, 256
    outline(f, bx, by, bw, bh)
    f.tex(bx + bw / 2, 32, r"\text{paristo}", "middle", w=110)
    xi, top, bot, xt = 106, 88, 284, 222
    wire(f, (xt, top), (xi, top), (xi, 134))
    cell(f, xi, 141)
    wire(f, (xi, 148), (xi, 196))
    resistor(f, xi, 226, True)
    wire(f, (xi, 256), (xi, bot), (xt, bot))
    f.tex(xi - 32, 128, "+", "middle", w=24)
    f.tex(xi - 32, 156, "-", "middle", w=24)
    f.tex(xi + 34, 141, "E", "start", w=30)
    f.tex(xi + 22, 226, r"R_\text{s}", "start", w=44)
    head(f, xi, 178, "u")
    f.tex(xi + 14, 178, "I", "start", CUR, w=24)
    # the external circuit: the load on the right, the voltmeter across the terminals
    xr, xv = 530, 352
    wire(f, (xt, top), (xr, top), (xr, bot), (xt, bot))
    terminal(f, xt, top); terminal(f, xt, bot)
    f.tex(xt + 12, top - 22, "+", "start", w=24)
    f.tex(xt + 12, bot + 22, "-", "start", w=24)
    resistor(f, xr, (top + bot) / 2, True)
    f.tex(xr + 22, (top + bot) / 2, "R", "start", w=30)
    node(f, xv, top); node(f, xv, bot)
    wire(f, (xv, top), (xv, 166)); wire(f, (xv, 206), (xv, bot))
    meter(f, xv, 186, "V")
    f.tex(xv + 30, 186, "U", "start", POT, w=30)
    head(f, 288, top, "r"); f.tex(288, top - 24, "I", "middle", CUR, w=24)
    head(f, 448, top, "r")
    head(f, 448, bot, "l")
    return f.svg()


# --- Ydinajatus: the potential round the loop ----------------------------------------------------------------------
def potential():
    """Schematic: E = 1,5, R_s I = 0,4, U = 1,1 (only the symbols are written)."""
    f = new("fy68-potential", 360, "Potentiaalikuvaaja, kaavamainen: potentiaali V, kun kierretään silmukka pariston miinusnavasta "
            "pariston sisäosien ja ulkoisen kuormitusvastuksen R kautta takaisin miinusnapaan. Miinusnavalla potentiaali on nolla. "
            "Ideaalisessa lähteessä se nousee lähdejännitteen E verran, ja pariston sisäisessä resistanssissa Rs se laskee "
            "jännitteen Rs kertaa I verran. Plusnavalla potentiaali on siksi napajännite U, joka on pienempi kuin E. "
            "Kuormitusvastuksessa potentiaali laskee U:n verran takaisin nollaan.")
    E, U = 1.5, 1.1
    ax = Axes(f, (96, 280), (476, 64), x=(0, 7), y=(0, 1.8), xticks=[], yticks=[], xlabel=r"\text{kohta}", ylabel=r"V",
              grid=False, origin_label=False)
    for x0, x1, t in ((0.8, 1.2, "E"), (2.0, 3.0, r"R_\text{s}"), (5.0, 6.0, "R")):
        f.rect(ax.X(x0), ax.Y(1.8), ax.X(x1) - ax.X(x0), ax.Y(0) - ax.Y(1.8), GLASS)
        f.tex((ax.X(x0) + ax.X(x1)) / 2, ax.Y(1.8) + 16, t, "middle", w=44)
    f.tex(84, 274, "0", "end")
    f.line(ax.x0, ax.Y(E), ax.X(1), ax.Y(E), MUTED, 1.5, "6 5")
    f.line(ax.x0, ax.Y(U), ax.X(3), ax.Y(U), MUTED, 1.5, "6 5")
    f.tex(ax.x0 - 12, ax.Y(E), "E", "end", w=30)
    f.tex(ax.x0 - 12, ax.Y(U), "U", "end", POT, w=30)
    path = [(0, 0), (1, 0), (1, E), (2, E), (3, U), (4, U), (5, U), (6, 0), (7, 0)]
    ax.line(path, POT, 3)
    # the internal drop: a bracket right of the resistor
    xb = ax.X(3) + 14
    f.path(f"M{n(xb - 7)},{n(ax.Y(E))} H{n(xb)} V{n(ax.Y(U))} H{n(xb - 7)}", stroke=INK, w=2.5)
    f.tex(xb + 10, (ax.Y(E) + ax.Y(U)) / 2, r"R_\text{s} I", "start", w=60)
    # the terminals on the axis
    for x, t in ((0, "-"), (4, "+"), (7, "-")):
        f.line(ax.X(x), 280, ax.X(x), 287, INK, 2)
        f.tex(ax.X(x), 304, t, "middle", w=24)
        ax.point(x, U if x == 4 else 0, POT, 5.5)
    # the battery spans the poles 0..4
    f.path(f"M{n(ax.X(0))},{n(322)} V{n(330)} H{n(ax.X(4))} V{n(322)}", stroke=MUTED, w=2)
    f.tex((ax.X(0) + ax.X(4)) / 2, 346, r"\text{paristo}", "middle", MUTED, w=110)
    return f.svg()


# --- Kaava: the (I, U) graph of a cell, E = 1,50 V, R_s = 0,30 ohm ---------------------------------------------
def ui_graph():
    E, Rs = 1.50, 0.30
    Ik = E / Rs
    f = new("fy68-ui", 360, "Kuvaaja mittakaavassa: pariston napajännite U voltteina virran I funktiona ampeereina. Suora alkaa "
            "pystyakselilta lähdejännitteen kohdalta 1,50 V ja laskee tasaisesti, kunnes se leikkaa vaaka-akselin "
            "oikosulkuvirran kohdalla 5,0 A. Kulmakertoimen kolmiossa virta kasvaa 1,0 ampeerista 3,0 ampeeriin eli 2,0 A, "
            "ja napajännite pienenee samalla 0,60 V. Sisäinen resistanssi on 0,60 V jaettuna 2,0 A:lla eli 0,30 ohmia.")
    ax = Axes(f, (96, 290), (500, 66), x=(0, 6), y=(0, 1.8), xticks=[1, 2, 3, 4, 5, 6], yticks=[0.3, 0.6, 0.9, 1.2, 1.5, 1.8],
              xlabel=r"I\ (\text{A})", ylabel=r"U\ (\text{V})", yfmt=lambda v: fi(v, 1) if round(v * 10) % 3 == 0 else "")
    # slope triangle from I = 1,0 A to 3,0 A
    u1, u3 = E - Rs * 1, E - Rs * 3
    f.line(ax.X(1), ax.Y(u1), ax.X(3), ax.Y(u1), MUTED, 1.5, "6 5")
    f.line(ax.X(3), ax.Y(u1), ax.X(3), ax.Y(u3), MUTED, 1.5, "6 5")
    f.tex((ax.X(1) + ax.X(3)) / 2, ax.Y(u1) - 20, r"\Delta I", "middle", w=50, bg=True)
    f.tex(ax.X(3) + 10, (ax.Y(u1) + ax.Y(u3)) / 2, r"\Delta U", "start", w=56, bg=True)
    ax.line([(0, E), (Ik, 0)], POT, 3)
    ax.point(0, E, POT, 6.5); ax.point(Ik, 0, POT, 6.5)
    f.tex(ax.X(0) + 16, ax.Y(E) - 20, "E", "start", POT, w=30)
    f.tex(ax.X(Ik) + 4, ax.Y(0) - 22, r"I_\text{k}", "start", POT, w=40)
    return f.svg()


# --- Kaava: cells in series and in parallel -----------------------------------------------------------------------
def boxed_cell(f, x, y, label=True):
    """A cell's model in a dashed outline: plates above, R_s below; the outline is 100 high, centred on y, and reaches
    further right than left so that E and R_s sit inside it, clear of its dashed edge."""
    outline(f, x - 36, y - 50, 104, 100)
    wire(f, (x, y - 50), (x, y - 27))
    cell(f, x, y - 20)
    wire(f, (x, y - 13), (x, y + 2))
    resistor(f, x, y + 24, True, length=40, width=20)
    wire(f, (x, y + 44), (x, y + 50))
    if label:
        f.tex(x + 32, y - 20, "E", "start", w=30)
        f.tex(x + 18, y + 24, r"R_\text{s}", "start", w=44)


def connections():
    f = new("fy68-connections", 360, "Kaksi kytkentäkaaviota vierekkäin, ei mittakaavassa. Kumpikin paristo on piirretty mallinaan: "
            "lähdejännite E ja sisäinen resistanssi Rs katkoviivan sisällä. Vasemmalla kaksi samanlaista paristoa on sarjassa "
            "päällekkäin, ylemmän miinusnapa alemman plusnapaan. Kokonaisuuden lähdejännite on 2E ja sisäinen resistanssi 2Rs. "
            "Oikealla kaksi samanlaista paristoa on rinnan vierekkäin, plusnavat yhdessä ja miinusnavat yhdessä. Kokonaisuuden "
            "lähdejännite on E ja sisäinen resistanssi puolet Rs:stä.")
    f.line(300, 20, 300, 340, RULE, 2, "6 6")
    # series
    x = 130
    f.tex(x, 28, r"\text{sarjaan}", "middle", w=110)
    terminal(f, x, 62); wire(f, (x, 69), (x, 76))
    boxed_cell(f, x, 126)
    boxed_cell(f, x, 226)
    wire(f, (x, 276), (x, 283)); terminal(f, x, 290)
    f.tex(x - 20, 62, "+", "end", w=24); f.tex(x - 20, 290, "-", "end", w=24)
    f.tex(x, 328, r"2E,\ 2R_\text{s}", "middle", w=130)
    # parallel
    xl, xr, xm = 380, 510, 445
    f.tex(xm, 28, r"\text{rinnan}", "middle", w=110)
    terminal(f, xm, 62); wire(f, (xm, 69), (xm, 96)); node(f, xm, 96)
    wire(f, (xl, 126), (xl, 96), (xr, 96), (xr, 126))
    boxed_cell(f, xl, 176, label=True)
    boxed_cell(f, xr, 176, label=True)
    wire(f, (xl, 226), (xl, 256), (xr, 256), (xr, 226))
    node(f, xm, 256); wire(f, (xm, 256), (xm, 283)); terminal(f, xm, 290)
    f.tex(xm - 20, 62, "+", "end", w=24); f.tex(xm - 20, 290, "-", "end", w=24)
    f.tex(xm, 328, r"E,\ \tfrac{1}{2} R_\text{s}", "middle", w=130)
    return f.svg()


# --- task figures --------------------------------------------------------------------------------------------------
def ex_graph():
    """Task figure (L1-05): model points of a 4,5 V battery and the line through them extended to both axes."""
    f = new("fy68-exgraph", 360, "Kuvaaja mittakaavassa: pariston napajännite U voltteina virran I funktiona ampeereina, ruudukon "
            "väli 0,5 A ja 0,5 V. Pisteet ovat (0,40 A; 3,9 V), (0,80 A; 3,3 V), (1,20 A; 2,7 V) ja (1,60 A; 2,1 V). "
            "Pisteiden kautta on piirretty suora, jota on jatkettu katkoviivana molempiin akseleihin asti.")
    ax = Axes(f, (96, 290), (500, 66), x=(0, 3.5), y=(0, 5), xticks=[0.5 * k for k in range(1, 8)],
              yticks=[0.5 * k for k in range(1, 11)], xlabel=r"I\ (\text{A})", ylabel=r"U\ (\text{V})",
              xfmt=lambda v: fi(v, 1) if round(v * 2) % 2 == 0 else "", yfmt=lambda v: fi(v, 0) if round(v * 2) % 2 == 0 else "")
    line = lambda i: 4.5 - 1.5 * i
    ax.line([(0, 4.5), (0.4, line(0.4))], POT, 3, "8 6")
    ax.line([(0.4, line(0.4)), (1.6, line(1.6))], POT, 3)
    ax.line([(1.6, line(1.6)), (3.0, 0)], POT, 3, "8 6")
    for i in (0.4, 0.8, 1.2, 1.6):
        ax.point(i, line(i), INK, 6)
    return f.svg()


CHECK_PTS = [(0.25, 8.52), (0.50, 7.96), (0.75, 7.53), (1.00, 6.98), (1.25, 6.51)]   # lesson-answers.py check2


def check_graph():
    """Task figure (tarkistus-2): five points of a 9 V battery with scatter and the fitted line U = 9,0 V - 2,0 ohm · I."""
    f = new("fy68-checkgraph", 360, "Kuvaaja mittakaavassa: pariston napajännite U voltteina virran I funktiona ampeereina, "
            "ruudukon väli 0,25 A ja 1 V. Mittauspisteet ovat (0,25 A; 8,52 V), (0,50 A; 7,96 V), (0,75 A; 7,53 V), "
            "(1,00 A; 6,98 V) ja (1,25 A; 6,51 V). Pisteisiin on sovitettu suora, joka on piirretty virrasta 0 A virtaan 1,5 A.")
    ax = Axes(f, (96, 290), (500, 66), x=(0, 1.75), y=(0, 10), xticks=[0.25 * k for k in range(1, 8)],
              yticks=list(range(1, 11)), xlabel=r"I\ (\text{A})", ylabel=r"U\ (\text{V})",
              xfmt=lambda v: fi(v, 1) if round(v * 4) % 2 == 0 else "", yfmt=lambda v: fi(v, 0) if v % 2 == 0 else "")
    ax.line([(0, 9.0), (1.5, 6.0)], POT, 3)
    for i, u in CHECK_PTS:
        ax.point(i, u, INK, 6)
    return f.svg()


# --- opening illustration: a car started on a dark winter morning ----------------------------------------------------
def car(f, x, yg):
    """A small car facing right, its wheels on the ground line yg; x is the rear end."""
    X = lambda d: n(x + d)
    Y = lambda d: n(yg + d)
    for dx, dy, r in ((-14, -24, 13), (-40, -44, 19), (-72, -66, 25), (-110, -88, 31)):   # exhaust steam, rising behind
        f.add(f'<circle cx="{X(dx)}" cy="{Y(dy)}" r="{r}" fill="{WHITE}" fill-opacity="0.55"/>')
    f.rect(x - 14, yg - 26, 22, 8, IRON, INK, 2, 3)                                                      # exhaust pipe
    beam = H.grad(f, "fy68h-beam", HEAT_LIGHT, WHITE, horizontal=True)
    f.add(f'<path d="M{X(452)},{Y(-74)} L{X(800)},{Y(-118)} L{X(800)},{Y(2)} L{X(452)},{Y(-58)} Z" fill="{beam}" fill-opacity="0.55"/>')
    f.path(f"M{X(0)},{Y(-18)} L{X(0)},{Y(-68)} Q{X(2)},{Y(-88)} {X(26)},{Y(-92)} L{X(92)},{Y(-98)} L{X(144)},{Y(-154)} "
           f"Q{X(152)},{Y(-164)} {X(168)},{Y(-164)} L{X(300)},{Y(-164)} Q{X(320)},{Y(-164)} {X(332)},{Y(-152)} L{X(382)},{Y(-100)} "
           f"L{X(430)},{Y(-92)} Q{X(454)},{Y(-88)} {X(456)},{Y(-66)} L{X(456)},{Y(-18)} Z", HOT, INK, 3)
    f.path(f"M{X(110)},{Y(-102)} L{X(152)},{Y(-150)} L{X(224)},{Y(-150)} L{X(224)},{Y(-102)} Z", GLASS, INK, 2.5)
    f.path(f"M{X(236)},{Y(-150)} L{X(298)},{Y(-150)} Q{X(310)},{Y(-150)} {X(318)},{Y(-140)} L{X(352)},{Y(-102)} L{X(236)},{Y(-102)} Z",
           GLASS, INK, 2.5)
    f.path(f"M{X(150)},{Y(-164)} Q{X(230)},{Y(-182)} {X(320)},{Y(-164)} Z", WHITE, INK, 2)            # snow on the roof
    f.line(x + 230, yg - 96, x + 230, yg - 30, INK, 2)
    f.rect(x + 196, yg - 84, 22, 6, INK, None, 2, 3)
    f.rect(x + 446, yg - 80, 12, 18, HEAT_LIGHT, INK, 2, 3)                                             # headlight
    f.rect(x - 4, yg - 76, 10, 16, HOT, INK, 2, 3)                                                       # rear light
    for wx in (96, 362):
        f.circle(x + wx, yg - 2, 46, INK)
        f.circle(x + wx, yg - 2, 20, ALUMINIUM, METAL_EDGE, 3)


def hero():
    f = H.hero("fy68-hero", "Kuvitus: pimeä talviaamu. Lumisella pihalla seisoo punainen pikkuauto, jonka ajovalo loistaa "
               "hämärään ja jonka pakoputkesta nousee höyryä: autoa käynnistetään. Taustalla on lumikattoinen punainen talo, "
               "jonka ikkunoista näkyy valoa, ja tummia kuusia.")
    f.rect(0, 0, 1200, 600, H.grad(f, "fy68h-sky", INK, COLD, y1=0, y2=470))
    for k in range(40):
        f.circle(H.rnd(k, 3) * 1200, H.rnd(k + 300, 3) * 300, 1.2 + 1.4 * H.rnd(k + 700, 3), WHITE)
    H.red_house(f, 70, 470, 250, 130, snow=True)
    for wx in (100, 170, 240):                                                    # light in the windows
        f.rect(wx, 470 - 130 * 0.72, 40, 130 * 0.4, HEAT_LIGHT, INK, 2)
    for sx, h in ((930, 230), (1020, 280), (1110, 210), (1180, 250)):
        H.spruce(f, sx, 476, h, GOOD)
    f.rect(0, 466, 1200, 134, H.grad(f, "fy68h-snow", WHITE, ICE, y1=466, y2=600))
    f.path("M0,520 Q300,500 600,516 T1200,512", stroke=WHITE, w=4)
    car(f, 372, 486)
    return f.svg()


FIGURES = {"hero": hero, "model": model, "potential": potential, "ui-graph": ui_graph, "connections": connections,
           "ex-graph": ex_graph, "check-graph": check_graph}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "model": "safe: the model of a battery (E and R_s inside a dashed outline) with a load R and a voltmeter across the terminals",
    "potential": "reveals: the terminal voltage U is E minus the internal drop R_s I (schematic potential graph)",
    "ui-graph": "reveals: E = 1,50 V and I_k = 5,0 A as the intercepts, R_s = 0,30 ohm from the slope triangle",
    "connections": "reveals: two identical cells in series give 2E and 2R_s, in parallel E and R_s/2",
    "ex-graph": "safe: four model (I, U) points of a 4,5 V battery and their line extended to both axes, no intercepts written",
    "check-graph": "safe: five (I, U) points of a 9 V battery with scatter and a fitted line, no slope or intercept written",
}
