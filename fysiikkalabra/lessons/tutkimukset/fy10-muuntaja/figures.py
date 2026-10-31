"""Figures of the investigation Muuntajan tutkiminen (scripts/figlib.py); `python scripts/investigations.py figures
fy10-muuntaja` writes them into investigation.md. No force, velocity or acceleration arrows are drawn, and wires are
neutral colours. The graph shows the ideal model only, never invented measurements; the hero shows no reading or
result on any display."""
from figlib import Fig, Axes, INK, MUTED, WHITE, GLASS, ALUMINIUM, METAL_EDGE, IRON, COPPER, SAND, SAND_DARK, \
    SAND_LIGHT, GRAIN, COLD, GOOD, n
import herolib as H
from herolib import grad

DISPLAY = "#2b3a42"       # a switched-on display without numbers
BOBBIN = "#495057"        # the plastic flanges of a coil
WIRE2 = "#2b8a3e"         # the second wire colour (green), no meaning beyond telling the wires apart


def meter(f, x, y, w, h):
    """A multimeter: a box with a dark display (no digits), a selector knob and two sockets."""
    f.rect(x, y, w, h, "#f4c542", INK, 2.5, rx=10)
    f.rect(x + 12, y + 12, w - 24, h * 0.34, DISPLAY, INK, 2, rx=4)
    f.circle(x + w / 2, y + h * 0.66, h * 0.13, IRON, INK, 2.5)
    f.line(x + w / 2, y + h * 0.66, x + w / 2, y + h * 0.66 - h * 0.11, WHITE, 3)
    f.circle(x + w * 0.3, y + h - 12, 5, INK); f.circle(x + w * 0.7, y + h - 12, 5, INK)
    return (x + w * 0.3, y + h - 12), (x + w * 0.7, y + h - 12)


def coil_on_limb(f, x, y_top, y_bot, w, turns):
    """A coil seen from the front on a vertical core limb: flanges, a copper body and its windings."""
    f.rect(x - 10, y_top - 12, w + 20, 12, BOBBIN, INK, 2.5, rx=3)
    f.rect(x - 10, y_bot, w + 20, 12, BOBBIN, INK, 2.5, rx=3)
    f.rect(x, y_top, w, y_bot - y_top, COPPER, INK, 2.5)
    step = (y_bot - y_top) / turns
    for k in range(1, turns):
        f.line(x + 2, y_top + k * step, x + w - 2, y_top + k * step, "#8a4a20", 2)


def hero():
    """The opening illustration: a lab bench with a demountable transformer (closed iron core, a coil on each limb), a
    low-voltage AC supply and meters wired to the primary, meters and a load resistor wired to the secondary, spare
    coils and a notebook. Displays are dark and show nothing."""
    f = H.hero("fy10m-hero", "Kuvitus: laboratorion työpöydällä on muuntaja. Suljetun rautasydämen kummassakin "
               "pystyhaarassa on käämi. Vasemmanpuoleinen käämi on kytketty johtimilla virtalähteeseen ja kahteen "
               "yleismittariin, oikeanpuoleinen kahteen yleismittariin ja kuormitusvastukseen. Mittarien näytöt ovat "
               "tyhjiä. Pöydällä on lisäksi kaksi irrallista käämiä ja vihko.")
    f.rect(0, 0, 1200, 600, grad(f, "fy10mh-wall", GLASS, "#dfe9ef"))
    f.rect(0, 470, 1200, 130, grad(f, "fy10mh-desk", SAND_DARK, SAND, horizontal=True))
    for k in range(5): f.line(0, 492 + 22 * k, 1200, 488 + 22 * k, GRAIN, 1.5)
    f.line(0, 470, 1200, 470, INK, 3)
    # the low-voltage AC supply on the left: dark display, knob, two sockets and a sine mark
    f.rect(40, 330, 200, 140, ALUMINIUM, INK, 3, rx=10)
    f.rect(60, 350, 100, 44, DISPLAY, INK, 2, rx=4)
    f.circle(200, 372, 16, IRON, INK, 2.5)
    s1, s2 = (90, 435), (190, 435)
    for p in (s1, s2): f.circle(*p, 9, INK, INK, 2.5)
    f.path("M120,435 q7.5,-14 15,0 t15,0", stroke=INK, w=2.5)
    # the transformer: closed core (bottom bar, two limbs, top yoke) on the desk
    f.rect(470, 420, 300, 40, IRON, INK, 3, rx=3)
    f.rect(470, 460, 300, 10, BOBBIN, INK, 2, rx=2)
    for xl in (495, 695):
        f.rect(xl, 240, 50, 180, IRON, INK, 3)
    f.rect(470, 200, 300, 40, IRON, INK, 3, rx=3)
    for k in range(1, 5):
        f.line(472, 200 + 8 * k, 768, 200 + 8 * k, METAL_EDGE, 1.2)
        f.line(472, 420 + 8 * k, 768, 420 + 8 * k, METAL_EDGE, 1.2)
    f.rect(600, 196, 40, 48, ALUMINIUM, INK, 2.5, rx=4)         # the clamp that holds the yoke
    coil_on_limb(f, 480, 270, 400, 80, 9)
    coil_on_limb(f, 680, 270, 400, 80, 15)
    # coil terminals on the front of the upper flanges
    p1, p2, q1, q2 = (492, 264), (548, 264), (692, 264), (748, 264)
    for p in (p1, p2, q1, q2): f.circle(*p, 6, WHITE, INK, 2.5)
    # meters: two for the primary, two for the secondary
    a1 = meter(f, 270, 380, 90, 90); v1 = meter(f, 370, 380, 90, 90)
    a2 = meter(f, 790, 380, 90, 90); v2 = meter(f, 890, 380, 90, 90)
    # the load resistor on a base, on the right
    f.rect(1010, 440, 160, 30, IRON, INK, 2.5, rx=5)
    f.rect(1030, 395, 120, 45, SAND_LIGHT, INK, 2.5, rx=18)
    for x in (1060, 1080, 1100, 1120): f.line(x, 397, x, 438, GRAIN, 4)
    r1, r2 = (1025, 455), (1155, 455)
    for p in (r1, r2): f.circle(*p, 6, WHITE, INK, 2.5)

    def wire(a, b, lift, c=INK):
        f.path(f"M{n(a[0])},{n(a[1])} C{n(a[0])},{n(a[1] - lift)} {n(b[0])},{n(b[1] - lift)} {n(b[0])},{n(b[1])}", stroke=c, w=3.5)
    # primary: supply - ammeter - coil, coil back to supply; voltmeter across the coil terminals
    wire(s1, a1[0], 70); wire(a1[1], p1, 260)
    wire(p2, s2, 330, WIRE2)
    wire(v1[0], p1, 200); wire(v1[1], p2, 240, WIRE2)
    # secondary: coil - ammeter - resistor - coil; voltmeter across the coil terminals
    wire(q2, a2[0], 230); wire(a2[1], r1, 90)
    wire(r2, q1, 360, WIRE2)
    wire(v2[0], q1, 250, WIRE2); wire(v2[1], q2, 200)
    # two spare coils lying on the desk front, and a notebook
    for x, t in ((300, 8), (450, 13)):
        f.rect(x, 520, 110, 50, COPPER, INK, 2.5)
        f.rect(x - 10, 516, 12, 58, BOBBIN, INK, 2.5, rx=3); f.rect(x + 108, 516, 12, 58, BOBBIN, INK, 2.5, rx=3)
        for k in range(1, t): f.line(x + k * 110 / t, 522, x + k * 110 / t, 568, "#8a4a20", 2)
    f.add('<g transform="translate(1000,535) rotate(-5)">'
          f'<rect x="-90" y="-36" width="190" height="66" rx="4" fill="{WHITE}" stroke="{INK}" stroke-width="2.5"/>'
          + "".join(f'<line x1="-74" y1="{-20 + 12 * k}" x2="84" y2="{-20 + 12 * k}" stroke="{COLD}" stroke-width="1.5" stroke-opacity="0.6"/>' for k in range(5))
          + "</g>")
    return f.svg()


def setup():
    """The circuit: AC source, ammeter in series and voltmeter across the primary coil; on the secondary an ammeter in
    series with the load resistor and a voltmeter across the secondary coil. Both coils on one closed iron core."""
    f = Fig("fy10m-setup", 380, "Kaaviokuva. Suljetun rautasydämen vasemmassa haarassa on ensiökäämi, jossa on N yksi "
            "kierrosta, ja oikeassa haarassa toisiokäämi, jossa on N kaksi kierrosta. Ensiökäämi on kytketty "
            "vaihtojännitelähteeseen. Ensiöpiirissä virtamittari on sarjassa käämin kanssa ja mittaa sähkövirran I yksi, "
            "ja jännitemittari on kytketty käämin napoihin ja mittaa jännitteen U yksi. Toisiopiirissä virtamittari on "
            "sarjassa kuormitusvastuksen R kanssa ja mittaa sähkövirran I kaksi, ja jännitemittari on kytketty "
            "toisiokäämin napoihin ja mittaa jännitteen U kaksi.")
    # the core: a frame with a window
    f.rect(210, 90, 180, 210, ALUMINIUM, INK, 2.5)
    f.rect(240, 120, 120, 150, WHITE, INK, 2.5)
    f.tex(300, 64, r"\text{rautasydän}", "middle", MUTED, size=20)

    def windings(xa, xb, y1, y2, turns):
        step = (y2 - y1) / (turns - 1)
        for k in range(turns):
            y = y1 + k * step
            f.line(xa, y + 5, xb, y - 5, COPPER, 3.5, cap="round")
    windings(202, 248, 145, 245, 7)
    windings(352, 398, 140, 250, 11)
    # primary circuit
    f.line(202, 140, 60, 140, INK, 2.5); f.line(60, 140, 60, 171, INK, 2.5)
    f.line(202, 250, 60, 250, INK, 2.5); f.line(60, 250, 60, 219, INK, 2.5)
    f.line(202, 140, 202, 150, INK, 2.5); f.line(202, 240, 202, 250, INK, 2.5)
    f.circle(60, 195, 24, WHITE, INK, 2.5); f.tex(60, 195, r"\sim", "middle")
    f.circle(110, 140, 20, WHITE, INK, 2.5); f.tex(110, 140, r"\mathrm{A}", "middle", size=22)
    f.tex(110, 104, r"I_1", "middle")
    f.circle(170, 140, 5, INK); f.circle(170, 250, 5, INK)
    f.line(170, 140, 170, 175, INK, 2.5); f.line(170, 215, 170, 250, INK, 2.5)
    f.circle(170, 195, 20, WHITE, INK, 2.5); f.tex(170, 195, r"\mathrm{V}", "middle", size=22)
    f.tex(142, 195, r"U_1", "end")
    # secondary circuit
    f.line(398, 140, 550, 140, INK, 2.5); f.line(550, 140, 550, 165, INK, 2.5)
    f.line(398, 250, 550, 250, INK, 2.5); f.line(550, 250, 550, 225, INK, 2.5)
    f.line(398, 140, 398, 145, INK, 2.5); f.line(398, 245, 398, 250, INK, 2.5)
    f.rect(540, 165, 20, 60, WHITE, INK, 2.5)
    f.tex(568, 195, r"R", "start")
    f.circle(490, 140, 20, WHITE, INK, 2.5); f.tex(490, 140, r"\mathrm{A}", "middle", size=22)
    f.tex(490, 104, r"I_2", "middle")
    f.circle(430, 140, 5, INK); f.circle(430, 250, 5, INK)
    f.line(430, 140, 430, 175, INK, 2.5); f.line(430, 215, 430, 250, INK, 2.5)
    f.circle(430, 195, 20, WHITE, INK, 2.5); f.tex(430, 195, r"\mathrm{V}", "middle", size=22)
    f.tex(458, 195, r"U_2", "start")
    # turns and names
    f.tex(225, 322, r"N_1", "middle"); f.tex(375, 322, r"N_2", "middle")
    f.tex(222, 354, r"\text{ensiökäämi}", "middle", MUTED, size=20)
    f.tex(378, 354, r"\text{toisiokäämi}", "middle", MUTED, size=20)
    return f.svg()


def model():
    """The ideal transformer's model graph: U2/U1 against N2/N1 is a line through the origin with slope 1 (no points)."""
    f = Fig("fy10m-model", 330, "Kuvaaja: jännitteiden suhde U kaksi per U yksi kierroslukujen suhteen N kaksi per N yksi "
            "funktiona ideaalisen muuntajan mallin mukaan. Akseleilla on sama mittakaava, ja kummallekin on merkitty arvot "
            "yksi ja kaksi. Kuvaaja on origon kautta kulkeva suora, jonka kulmakerroin on yksi. Kuvaajassa ei ole mittauspisteitä.")
    ax = Axes(f, (90, 280), (320, 50), x=(0, 2.5), y=(0, 2.5), xticks=[1, 2], yticks=[1, 2], xlabel=r"N_2/N_1",
              ylabel=r"U_2/U_1", grid=True)
    ax.line([(0, 0), (2.4, 2.4)], INK)
    f.tex(ax.X(1.5), ax.Y(0.9), r"\text{kulmakerroin } 1", "start", bg=True)
    return f.svg()


FIGURES = {"hero": hero, "setup": setup, "model": model}
