"""Figures of the investigation Uppokuumentimen hyötysuhteen määrittäminen (scripts/figlib.py); `python
scripts/investigations.py figures fy10-uppokuumennin` writes them into investigation.md. No force, velocity or
acceleration arrows are drawn. The graphs show models only, never invented measurements; the hero shows no reading
or result on any display."""
from figlib import Fig, Axes, INK, MUTED, WHITE, GLASS, WATER_LIGHT, WATER, ALUMINIUM, METAL_EDGE, IRON, COPPER, \
    SAND, SAND_DARK, GRAIN, HOT, COLD, RULE, n
import herolib as H
from herolib import grad

DISPLAY = "#2b3a42"       # a switched-on display without numbers


def coil(f, x1, x2, y, turns=5, h=16, color=COPPER, w=4):
    """The heating element: a horizontal zigzag coil from x1 to x2 at height y."""
    step = (x2 - x1) / (2 * turns)
    d = f"M{n(x1)},{n(y)}" + "".join(f" L{n(x1 + (k + 0.5) * step)},{n(y + (h if k % 2 == 0 else -h))}" for k in range(2 * turns)) + f" L{n(x2)},{n(y)}"
    return f.path(d, stroke=color, w=w)


def meter(f, x, y, w, h, knob=True):
    """A multimeter: a box with a dark display (no digits) and a selector knob."""
    f.rect(x, y, w, h, "#f4c542", INK, 2.5, rx=10)
    f.rect(x + 12, y + 12, w - 24, h * 0.34, DISPLAY, INK, 2, rx=4)
    if knob:
        f.circle(x + w / 2, y + h * 0.68, h * 0.14, IRON, INK, 2.5)
        f.line(x + w / 2, y + h * 0.68, x + w / 2, y + h * 0.68 - h * 0.12, WHITE, 3)
    f.circle(x + w * 0.3, y + h - 12, 5, INK); f.circle(x + w * 0.7, y + h - 12, 5, HOT)


def hero():
    """The opening illustration: a lab bench with a calorimeter (cut open to show the water), an immersion heater whose
    coil is fully under water, a thermometer and a stirrer through the lid, a low-voltage supply and two meters wired
    to the heater, a scale and a notebook. Displays are dark and show nothing."""
    f = H.hero("fy10u-hero", "Kuvitus: laboratorion työpöydällä on kalorimetri, joka on piirretty puoliksi auki leikattuna. "
               "Sen sisällä on vettä, ja uppokuumentimen kierukka on kokonaan veden alla. Kannen läpi veteen ulottuvat "
               "myös lämpömittari ja sekoitin. Kuumennin on kytketty johtimilla virtalähteeseen ja kahteen "
               "yleismittariin. Pöydällä on lisäksi vaaka ja vihko.")
    f.rect(0, 0, 1200, 600, grad(f, "fy10uh-wall", GLASS, "#dfe9ef"))
    f.rect(0, 470, 1200, 130, grad(f, "fy10uh-desk", SAND_DARK, SAND, horizontal=True))
    for k in range(5): f.line(0, 492 + 22 * k, 1200, 488 + 22 * k, GRAIN, 1.5)
    f.line(0, 470, 1200, 470, INK, 3)
    # power supply on the left
    f.rect(70, 330, 230, 140, ALUMINIUM, INK, 3, rx=10)
    f.rect(92, 350, 120, 46, DISPLAY, INK, 2, rx=4)
    for x in (240, 275): f.circle(x, 372, 14, IRON, INK, 2.5)
    f.circle(110, 435, 9, HOT, INK, 2.5); f.circle(150, 435, 9, INK, INK, 2.5)
    # two meters
    meter(f, 360, 360, 110, 110)
    meter(f, 860, 360, 110, 110)
    # the calorimeter, cut open: outer jacket, inner vessel, water
    cx, top, bot = 640, 230, 470
    f.rect(cx - 130, top, 260, bot - top, ALUMINIUM, INK, 3, rx=8)
    f.rect(cx - 110, top + 14, 220, bot - top - 26, WHITE, METAL_EDGE, 2.5, rx=6)
    f.rect(cx - 108, top + 60, 216, bot - top - 74, grad(f, "fy10uh-water", WATER_LIGHT, "#7fb8e6"), None, 0, rx=5)
    f.line(cx - 108, top + 60, cx + 108, top + 60, WATER, 2.5)
    f.rect(cx - 145, top - 16, 290, 18, IRON, INK, 3, rx=5)          # lid
    # heater: two leads through the lid, coil near the bottom, fully under water
    for x in (cx - 50, cx + 10):
        f.rect(x - 6, 150, 12, 64, "#495057", INK, 2, rx=3)
        f.line(x, 214, x, 400, COPPER, 4)
    coil(f, cx - 50, cx + 10, 410, turns=4, h=14)
    # thermometer and stirrer through the lid
    H.thermometer(f, cx + 70, 420, 120, HOT, length=290)
    f.line(cx - 90, 165, cx - 90, 438, METAL_EDGE, 5, cap="round")
    f.line(cx - 104, 438, cx - 76, 438, METAL_EDGE, 5, cap="round")
    f.circle(cx - 90, 161, 10, IRON, INK, 2.5)
    # wires: supply - meter (series) - heater, return to supply; second meter across the heater leads
    def wire(d, c=INK): f.path(d, stroke=c, w=3.5)
    wire(f"M110,435 C110,520 393,520 393,458", HOT)                   # supply + to ammeter
    wire(f"M437,458 C437,320 590,90 590,150", HOT)                    # ammeter to heater lead 1
    wire(f"M150,435 C200,200 470,20 650,150")                        # heater lead 2 back to supply -
    wire(f"M590,150 C610,40 880,60 893,458", HOT)                     # voltmeter across the leads
    wire(f"M650,150 C680,10 930,30 937,458")
    # scale and notebook on the right
    f.rect(1010, 430, 150, 40, IRON, INK, 2.5, rx=6); f.rect(1035, 420, 100, 12, ALUMINIUM, INK, 2.5, rx=3)
    f.rect(1050, 440, 70, 20, DISPLAY, INK, 2, rx=3)
    f.add('<g transform="translate(1080,535) rotate(-5)">'
          f'<rect x="-90" y="-36" width="190" height="66" rx="4" fill="{WHITE}" stroke="{INK}" stroke-width="2.5"/>'
          + "".join(f'<line x1="-74" y1="{-20 + 12 * k}" x2="84" y2="{-20 + 12 * k}" stroke="{COLD}" stroke-width="1.5" stroke-opacity="0.6"/>' for k in range(5))
          + "</g>")
    return f.svg()


def setup():
    """The circuit and the calorimeter: ammeter in series with the heater, voltmeter across the heater's terminals."""
    f = Fig("fy10u-setup", 450, "Kaaviokuva. Virtalähteen napa on kytketty virtamittarin kautta uppokuumentimen toiseen "
            "johtimeen, ja kuumentimen toinen johdin palaa virtalähteen toiseen napaan. Virtamittari on siis sarjassa "
            "kuumentimen kanssa ja mittaa sähkövirran I. Jännitemittari on kytketty kuumentimen kahden johtimen väliin eli "
            "rinnan kuumentimen kanssa, ja se mittaa jännitteen U. Kuumentimen kierukka on kokonaan veden alla "
            "kalorimetrissä. Kannen läpi veteen ulottuvat myös lämpömittari ja sekoitin.")
    # supply
    f.rect(20, 25, 150, 80, ALUMINIUM, INK, 2.5, rx=6)
    f.tex(82, 65, r"\text{virtalähde}", "middle", size=20)
    f.circle(170, 45, 5, INK); f.circle(170, 85, 5, INK)
    f.tex(160, 45, r"-", "end", size=20); f.tex(160, 85, r"+", "end", size=20)
    xl, xr = 250, 350                     # heater leads
    # + wire through the ammeter to the left lead
    f.line(170, 85, xl, 85, INK, 2.5); f.line(xl, 85, xl, 108, INK, 2.5)
    f.circle(xl, 130, 22, WHITE, INK, 2.5); f.tex(xl, 130, r"\mathrm{A}", "middle", size=22)
    f.tex(xl - 30, 130, r"I", "end")
    f.line(xl, 152, xl, 236, INK, 2.5)
    # - wire to the right lead
    f.line(170, 45, xr, 45, INK, 2.5); f.line(xr, 45, xr, 236, INK, 2.5)
    # voltmeter across the leads
    f.circle(xl, 190, 5, INK); f.circle(xr, 190, 5, INK)
    f.line(xl, 190, 278, 190, INK, 2.5); f.line(322, 190, xr, 190, INK, 2.5)
    f.circle(300, 190, 22, WHITE, INK, 2.5); f.tex(300, 190, r"\mathrm{V}", "middle", size=22)
    f.tex(300, 152, r"U", "middle")
    # calorimeter
    f.rect(180, 245, 240, 185, ALUMINIUM, INK, 2.5, rx=6)
    f.rect(196, 252, 208, 170, WHITE, METAL_EDGE, 2, rx=4)
    f.rect(198, 285, 204, 135, WATER_LIGHT, None, 0, rx=3)
    f.line(198, 285, 402, 285, WATER, 2)
    f.rect(170, 232, 260, 14, IRON, INK, 2.5, rx=4)
    f.line(xl, 246, xl, 380, COPPER, 3.5); f.line(xr, 246, xr, 380, COPPER, 3.5)
    coil(f, xl, xr, 385, turns=5, h=12, w=3.5)
    # thermometer and stirrer
    f.rect(377, 175, 14, 175, WHITE, INK, 2, rx=7); f.circle(384, 356, 11, HOT, INK, 2)
    f.rect(381, 250, 6, 106, HOT)
    f.line(218, 200, 218, 405, METAL_EDGE, 4, cap="round"); f.line(206, 405, 230, 405, METAL_EDGE, 4, cap="round")
    # labels
    f.line(400, 300, 438, 300, MUTED, 1.5); f.tex(444, 300, r"\text{lämpömittari}", "start", size=20)
    f.line(420, 255, 438, 255, MUTED, 1.5); f.tex(444, 255, r"\text{kalorimetri}", "start", size=20)
    f.line(xr + 6, 395, 438, 395, MUTED, 1.5); f.tex(444, 395, r"\text{uppokuumennin}", "start", size=20)
    f.line(212, 330, 176, 330, MUTED, 1.5); f.tex(170, 330, r"\text{sekoitin}", "end", size=20)
    f.tex(300, 315, r"\text{vesi}", "middle", MUTED, size=20)
    return f.svg()


def model():
    """The model graph Q against E: a line through the origin, slope eta, below the reference line Q = E (no points)."""
    f = Fig("fy10u-model", 340, "Kuvaaja: veden saama lämpö Q sähköenergian E funktiona mallin mukaan, kun hyötysuhde "
            "pysyy vakiona. Kuvaaja on origon kautta kulkeva suora. Katkoviivalla on vertailun vuoksi piirretty suora "
            "Q yhtä kuin E, jolla kaikki sähköenergia päätyisi veteen. Mallisuoralle on merkitty kahden pisteen väliset "
            "muutokset delta E ja delta Q, ja kulmakerroin eta on delta Q jaettuna delta E:llä. Kuvaajassa ei ole "
            "mittauspisteitä.")
    ax = Axes(f, (90, 290), (470, 50), x=(0, 10), y=(0, 10), xticks=[], yticks=[], xlabel=r"E", ylabel=r"Q", grid=False)
    ax.line([(0, 0), (9.6, 9.6)], RULE, 2.5, "8 6")
    f.tex(ax.X(8.6), ax.Y(9.7), r"Q = E", "end", MUTED)
    eta = 0.72
    ax.line([(0, 0), (9.6, 9.6 * eta)], INK)
    a, b = 4.0, 8.5
    f.line(ax.X(a), ax.Y(a * eta), ax.X(b), ax.Y(a * eta), MUTED, 2, "6 5")
    f.line(ax.X(b), ax.Y(a * eta), ax.X(b), ax.Y(b * eta), MUTED, 2, "6 5")
    f.tex((ax.X(a) + ax.X(b)) / 2, ax.Y(a * eta) + 20, r"\Delta E", "middle", MUTED)
    f.tex(ax.X(b) + 10, ax.Y((a + b) / 2 * eta), r"\Delta Q", "start", MUTED)
    f.tex(ax.X(2.6), ax.Y(7.4), r"\eta = \dfrac{\Delta Q}{\Delta E}", "middle")
    return f.svg()


def heating():
    """The model graph T against t at constant power: a line from T0 with slope a (no points)."""
    f = Fig("fy10u-heating", 340, "Kuvaaja: veden lämpötila T ajan t funktiona mallin mukaan, kun teho ja hyötysuhde "
            "pysyvät vakioina. Kuvaaja on suora, joka alkaa alkulämpötilasta T nolla. Suoralle on merkitty muutokset "
            "delta t ja delta T, ja kulmakerroin a on delta T jaettuna delta t:llä. Kuvaajassa ei ole mittauspisteitä.")
    ax = Axes(f, (90, 290), (470, 50), x=(0, 10), y=(0, 10), xticks=[], yticks=[], xlabel=r"t", ylabel=r"T", grid=False,
              origin_label=False)
    T0, k = 2.2, 0.68
    ax.line([(0, T0), (9.6, T0 + 9.6 * k)], INK)
    f.tex(ax.x0 - 12, ax.Y(T0), r"T_0", "end")
    f.line(ax.x0 - 7, ax.Y(T0), ax.x0, ax.Y(T0), INK, 2)
    a, b = 3.5, 8.0
    f.line(ax.X(a), ax.Y(T0 + a * k), ax.X(b), ax.Y(T0 + a * k), MUTED, 2, "6 5")
    f.line(ax.X(b), ax.Y(T0 + a * k), ax.X(b), ax.Y(T0 + b * k), MUTED, 2, "6 5")
    f.tex((ax.X(a) + ax.X(b)) / 2, ax.Y(T0 + a * k) + 20, r"\Delta t", "middle", MUTED)
    f.tex(ax.X(b) + 10, ax.Y(T0 + (a + b) / 2 * k), r"\Delta T", "start", MUTED)
    f.tex(ax.X(2.4), ax.Y(8.6), r"a = \dfrac{\Delta T}{\Delta t}", "middle")
    return f.svg()


FIGURES = {"hero": hero, "setup": setup, "model": model, "heating": heating}
