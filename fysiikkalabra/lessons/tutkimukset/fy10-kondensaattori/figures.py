"""Figures of the investigation Kondensaattorin kapasitanssin määrittäminen (scripts/figlib.py); `python
scripts/investigations.py figures fy10-kondensaattori` writes them into investigation.md. No force, velocity or
acceleration arrows are drawn; the current direction is a neutral ink arrow. The graphs show models only, never
invented measurements, and the hero's screen shows an empty grid, not a result."""
import math
from figlib import (Fig, Axes, INK, MUTED, WHITE, RULE_LIGHT, GLASS, ALUMINIUM, METAL_EDGE, IRON, COPPER, SAND, SAND_DARK,
                    SAND_LIGHT, GRAIN, HOT, COLD, COLD_LIGHT, GOOD, n)
import herolib as H
from herolib import grad


def resistor_body(f, x, y, w=90, h=24):
    """A through-hole resistor seen from the side: a beige body with colour bands."""
    f.rect(x, y, w, h, SAND_LIGHT, INK, 2.5, rx=10)
    for k, c in enumerate([COPPER, INK, HOT, SAND_DARK]):
        f.rect(x + 16 + 15 * k + (8 if k == 3 else 0), y + 2, 7, h - 4, c)


def hero():
    """The opening illustration: a lab bench with a low-voltage supply, a breadboard holding an electrolytic capacitor,
    a resistor and a switch, a voltage sensor whose leads reach the board, and a laptop with an empty graph grid."""
    f = H.hero("fy10k-hero", "Kuvitus: laboratorion työpöydällä on tasajännitelähde, jonka navoista johtimet kulkevat "
               "kytkentäalustalle. Alustalla on sininen sylinterin muotoinen elektrolyyttikondensaattori, jonka kyljessä "
               "on vaalea raita, sekä vastus ja vaihtokytkin. Jänniteanturin johdot ulottuvat kondensaattorin luo, ja "
               "anturi on kytketty kannettavaan tietokoneeseen, jonka näytöllä on tyhjä kuvaajaruudukko.")
    f.rect(0, 0, 1200, 600, grad(f, "fy10kh-wall", GLASS, "#dfe9ef"))
    f.rect(0, 470, 1200, 130, grad(f, "fy10kh-desk", SAND_DARK, SAND, horizontal=True))
    for k in range(5): f.line(0, 492 + 22 * k, 1200, 488 + 22 * k, GRAIN, 1.5)
    f.line(0, 470, 1200, 470, INK, 3)
    # low-voltage supply: a box with a blank display, a knob and two terminals
    f.rect(60, 300, 250, 170, ALUMINIUM, INK, 3, rx=10)
    f.rect(85, 325, 130, 56, "#2b3a42", INK, 2.5, rx=4)
    f.circle(262, 352, 24, IRON, INK, 2.5); f.line(262, 352, 262, 332, WHITE, 3)
    f.circle(110, 430, 15, HOT, INK, 2.5); f.circle(170, 430, 15, INK, INK, 2.5)
    # breadboard
    f.rect(400, 420, 400, 50, WHITE, INK, 2.5, rx=4)
    for r in range(3):
        for c in range(36): f.circle(416 + 10.5 * c, 432 + 12 * r, 1.8, RULE_LIGHT)
    # wires from the supply to the board
    H.wire(f, (110, 430), (430, 424), sag=28, colour=HOT, w=4)
    H.wire(f, (170, 430), (450, 448), sag=18, colour=INK, w=4)
    # electrolytic capacitor: blue sleeve with a light stripe, two legs into the board
    f.line(560, 420, 560, 404, METAL_EDGE, 3); f.line(590, 420, 590, 404, METAL_EDGE, 3)
    f.rect(540, 270, 70, 136, COLD, INK, 2.5, rx=8)
    f.rect(586, 272, 16, 132, COLD_LIGHT)
    for k in range(5): f.line(590, 290 + 24 * k, 598, 290 + 24 * k, COLD, 3)
    f.add(f'<ellipse cx="575" cy="276" rx="33" ry="7" fill="{ALUMINIUM}" stroke="{INK}" stroke-width="2"/>')
    # resistor with bent legs
    f.path("M650,426 L650,392 L662,392", stroke=METAL_EDGE, w=3); f.path("M770,426 L770,392 L758,392", stroke=METAL_EDGE, w=3)
    resistor_body(f, 662, 380, 96, 24)
    # changeover switch
    f.rect(460, 380, 54, 40, IRON, INK, 2.5, rx=4)
    f.line(487, 380, 474, 350, INK, 6, cap="round")
    # voltage sensor and its leads to the capacitor legs
    f.rect(850, 400, 110, 60, GOOD, INK, 2.5, rx=8); f.rect(866, 414, 78, 10, WHITE, None, rx=3)
    H.wire(f, (860, 440), (566, 418), sag=40, colour=HOT, w=3)
    H.wire(f, (870, 450), (596, 420), sag=55, colour=INK, w=3)
    # laptop with an empty grid on screen
    f.path("M930,470 L1170,470 L1150,452 L950,452 Z", fill=IRON, stroke=INK, w=2.5)
    f.rect(960, 290, 180, 162, INK, INK, 2.5, rx=6)
    f.rect(970, 300, 160, 140, WHITE)
    for k in range(1, 7): f.line(970, 300 + 20 * k, 1130, 300 + 20 * k, RULE_LIGHT, 1.5)
    for k in range(1, 8): f.line(970 + 20 * k, 300, 970 + 20 * k, 440, RULE_LIGHT, 1.5)
    f.line(984, 430, 1124, 430, MUTED, 2); f.line(984, 430, 984, 310, MUTED, 2)
    H.wire(f, (960, 440), (930, 455), sag=10, colour=INK, w=3)
    return f.svg()


def circuit():
    """The measuring circuit: supply, changeover switch (A charges, B discharges through R), R, C and a voltmeter across C."""
    f = Fig("fy10k-circuit", 330, "Kytkentäkaavio. Vasemmalla on tasajännitelähde, jonka jännite on U nolla. Vaihtokytkimen "
            "asennossa A lähde, vastus R ja kondensaattori C ovat samassa virtapiirissä, jolloin kondensaattori varautuu. "
            "Asennossa B lähde on irti, ja kondensaattori purkautuu vastuksen R kautta. Jännitemittari V on kytketty "
            "kondensaattorin rinnalle. Kondensaattorin plusnapa on vastuksen puolella, joka on asennossa A kytketty "
            "lähteen plusnapaan.")
    W = 3
    # supply on the left, + on top
    f.line(80, 60, 80, 150, INK, W); f.line(54, 150, 106, 150, INK, W); f.line(68, 166, 92, 166, INK, 6)
    f.line(80, 166, 80, 290, INK, W)
    f.tex(46, 158, r"U_0", "end"); f.tex(112, 136, r"+", "start"); f.tex(112, 182, r"-", "start")
    # top wire to contact A, return wire along the bottom
    f.line(80, 60, 230, 60, INK, W); f.line(80, 290, 470, 290, INK, W)
    # contact B down to the bottom wire
    f.line(230, 130, 230, 290, INK, W)
    f.circle(230, 60, 6, WHITE, INK, 2.5); f.circle(230, 130, 6, WHITE, INK, 2.5); f.circle(290, 95, 6, WHITE, INK, 2.5)
    f.line(286, 91, 236, 64, INK, W)                       # the blade, now at A
    f.tex(214, 60, r"\text{A}", "end"); f.tex(214, 130, r"\text{B}", "end")
    f.circle(230, 290, 5, INK)
    # common terminal to the resistor and on to the capacitor
    f.line(296, 95, 320, 95, INK, W); f.rect(320, 80, 90, 30, WHITE, INK, W); f.line(410, 95, 470, 95, INK, W)
    f.tex(365, 56, r"R", "middle")
    f.line(470, 95, 470, 180, INK, W)
    f.line(444, 180, 496, 180, INK, 5); f.path("M444,202 Q470,190 496,202", stroke=INK, w=5)
    f.line(470, 196, 470, 290, INK, W)
    f.tex(436, 191, r"C", "end"); f.tex(500, 166, r"+", "start")
    # voltmeter across the capacitor
    f.circle(470, 140, 5, INK); f.circle(470, 250, 5, INK)
    f.line(470, 140, 550, 140, INK, W); f.line(550, 140, 550, 171, INK, W)
    f.circle(550, 195, 24, WHITE, INK, W); f.tex(550, 195, r"\text{V}", "middle")
    f.line(550, 219, 550, 250, INK, W); f.line(550, 250, 470, 250, INK, W)
    return f.svg()


def model():
    """The discharge model u = U0 e^(-t/tau): the tangent at t = 0 meets the time axis at tau, and at t = tau the
    voltage is U0/e (about 0.37 U0). No measured points."""
    f = Fig("fy10k-model", 340, "Kuvaaja: kondensaattorin jännite u ajan t funktiona purkautumisen mallin mukaan. Jännite "
            "alkaa arvosta U nolla ja pienenee ensin nopeasti, sitten yhä hitaammin kohti nollaa. Alkuhetken tangentti "
            "leikkaa aika-akselin kohdassa tau. Hetkellä tau jännite on noin 0,37 kertaa U nolla. Kuvaajassa ei ole "
            "mittauspisteitä.")
    ax = Axes(f, (90, 290), (470, 50), x=(0, 5), y=(0, 1.15), xticks=[1], yticks=[1], xlabel=r"t", ylabel=r"u",
              grid=False, xfmt=lambda v: r"\tau", yfmt=lambda v: r"U_0")
    ax.curve(lambda t: math.exp(-t), 0, 5)
    ax.line([(0, 1), (1, 0)], MUTED, 2, "6 5")
    ax.guide(1, math.exp(-1)); ax.point(1, math.exp(-1))
    f.tex(ax.X(1) + 14, ax.Y(math.exp(-1)) - 18, r"0{,}37\cdot U_0", "start")
    f.tex(ax.X(3.1), ax.Y(0.78), r"u = U_0\,\mathrm{e}^{-t/\tau}", "middle")
    return f.svg()


def linear():
    """The linearised model: ln u against t is a line with slope -1/tau. No measured points."""
    f = Fig("fy10k-linear", 320, "Kuvaaja: jännitteen luonnollinen logaritmi ln u ajan t funktiona purkautumisen mallin "
            "mukaan. Kuvaaja on laskeva suora, jonka kulmakerroin on miinus yksi jaettuna tau:lla. Kuvaajassa ei ole "
            "mittauspisteitä.")
    ax = Axes(f, (90, 270), (470, 50), x=(0, 10), y=(0, 10), xticks=[], yticks=[], xlabel=r"t", ylabel=r"\ln u",
              grid=False, origin_label=False)
    ax.line([(0, 8.8), (9.5, 1.2)], INK)
    f.tex(ax.X(5.6), ax.Y(7.6), r"\text{kulmakerroin } -\dfrac{1}{\tau}", "middle")
    return f.svg()


FIGURES = {"hero": hero, "circuit": circuit, "model": model, "linear": linear}
