"""Figures of the investigation Pariston kuormituskäyrä (scripts/figlib.py); `python scripts/investigations.py figures
fy10-paristo` writes them into investigation.md. No force, velocity or acceleration arrows are drawn; current and
voltage marks are ink or muted. The graph shows a model only, never invented measurements; the hero shows no reading,
no result and no wired circuit (how the meters are connected is the student's design in modes OO and I)."""
from figlib import Fig, Axes, INK, MUTED, WHITE, GLASS, ALUMINIUM, METAL_EDGE, IRON, COPPER, SAND, SAND_DARK, \
    GRAIN, HOT, COLD, n
import herolib as H
from herolib import grad

DISPLAY = "#2b3a42"       # a switched-on display without numbers
CELL = "#2f9e44"          # the body of the AA cell in the hero (a colour of an object, not of a quantity)


def meter(f, x, y, w, h):
    """A multimeter: a yellow box, a dark display without digits, a selector knob and two sockets."""
    f.rect(x, y, w, h, "#f4c542", INK, 2.5, rx=10)
    f.rect(x + 12, y + 12, w - 24, h * 0.34, DISPLAY, INK, 2, rx=4)
    f.circle(x + w / 2, y + h * 0.68, h * 0.14, IRON, INK, 2.5)
    f.line(x + w / 2, y + h * 0.68, x + w / 2, y + h * 0.68 - h * 0.12, WHITE, 3)
    f.circle(x + w * 0.3, y + h - 12, 5, INK); f.circle(x + w * 0.7, y + h - 12, 5, HOT)


def plug(f, x, y, colour):
    f.rect(x - 7, y - 4, 14, 22, colour, INK, 2, rx=3)


def hero():
    """The opening illustration: a lab bench with an AA cell in its holder, a slide rheostat, two multimeters with their
    leads lying loose beside them, a few wires and a notebook. Nothing is wired into a circuit and no display shows a value."""
    f = H.hero("fy10pa-hero", "Kuvitus: laboratorion työpöydällä on pidikkeessä oleva paristo, liukuvastus, kaksi yleismittaria "
               "ja niiden mittajohdot, muutama johdin sekä vihko mittaustulosten kirjaamiseen. Osia ei ole vielä kytketty "
               "yhteen, eikä mittareiden näytöissä ole lukemia.")
    f.rect(0, 0, 1200, 600, grad(f, "fy10pah-wall", GLASS, "#dfe9ef"))
    f.rect(0, 420, 1200, 180, grad(f, "fy10pah-desk", SAND_DARK, SAND, horizontal=True))
    for k in range(7): f.line(0, 444 + 22 * k, 1200, 440 + 22 * k, GRAIN, 1.5)
    f.line(0, 420, 1200, 420, INK, 3)
    # the cell in its holder, two leads with plugs lying on the desk
    f.rect(150, 410, 210, 52, IRON, INK, 2.5, rx=6)
    f.rect(170, 416, 160, 40, CELL, INK, 2.5, rx=8)
    f.rect(182, 416, 26, 40, ALUMINIUM, INK, 2, rx=4)
    f.rect(330, 427, 10, 18, ALUMINIUM, INK, 2, rx=2)
    f.path("M150,436 C110,436 100,500 150,520 S240,540 250,560", stroke=HOT, w=4); plug(f, 250, 556, HOT)
    f.path("M360,436 C400,436 420,500 380,530 S330,560 320,575", stroke=INK, w=4); plug(f, 320, 571, INK)
    # the slide rheostat: a wound tube between two end blocks, a rail and a slider
    f.rect(470, 330, 30, 120, IRON, INK, 2.5, rx=4); f.rect(800, 330, 30, 120, IRON, INK, 2.5, rx=4)
    f.rect(500, 370, 300, 56, COPPER, INK, 2.5, rx=10)
    for k in range(1, 30): f.line(500 + 10 * k, 372, 500 + 10 * k, 424, "#8f4a1f", 1.5)
    f.rect(500, 338, 300, 10, ALUMINIUM, INK, 2, rx=3)
    f.rect(610, 326, 34, 50, "#343a40", INK, 2.5, rx=5)
    for x in (485, 815): f.circle(x, 322, 8, HOT, INK, 2)
    # two multimeters with coiled leads
    meter(f, 880, 260, 130, 190); meter(f, 1040, 280, 120, 170)
    f.path("M920,438 C900,500 980,520 960,560 S880,575 860,560", stroke=INK, w=3)
    f.path("M971,438 C1000,490 1060,500 1040,550", stroke=HOT, w=3)
    f.path("M1076,438 C1060,500 1120,520 1100,570", stroke=INK, w=3)
    f.path("M1124,438 C1150,480 1180,520 1160,560", stroke=HOT, w=3)
    # a few loose wires and the notebook
    f.path("M560,500 C620,470 700,540 760,505", stroke=COLD, w=4); plug(f, 560, 496, COLD); plug(f, 760, 501, COLD)
    f.path("M590,560 C650,530 720,590 790,555", stroke=INK, w=4)
    f.add('<g transform="translate(100,250) rotate(-5)">'
          f'<rect x="-70" y="-60" width="200" height="120" rx="4" fill="{WHITE}" stroke="{INK}" stroke-width="2.5"/>'
          + "".join(f'<line x1="-54" y1="{-40 + 16 * k}" x2="114" y2="{-40 + 16 * k}" stroke="{COLD}" stroke-width="1.5" stroke-opacity="0.6"/>' for k in range(7))
          + "</g>")
    return f.svg()


def cell(f, x, y, long_up=True):
    """The circuit symbol of a cell on a vertical wire at x, centred on y: the long thin plate is the + pole."""
    f.rect(x - 30, y - 10, 60, 20, WHITE)          # clears the wire between the plates
    top, bot = y - 8, y + 8
    f.line(x - 26, top, x + 26, top, INK, 2.5)       # long thin plate (+) on top
    f.rect(x - 12, bot - 4, 24, 8, INK)              # short thick plate (−) below


def model():
    """The battery as an ideal source E in series with the internal resistance R_s inside a dashed outline, the terminal
    voltage U across the poles and a load outside."""
    f = Fig("fy10pa-model", 400, "Kaaviokuva pariston mallista. Katkoviivalla rajatun pariston sisällä on lähdejännite E "
            "ja sen kanssa sarjassa sisäinen resistanssi R s. Pariston plusnapa on ylhäällä ja miinusnapa alhaalla. Navoista "
            "johtimet menevät pariston ulkopuolella olevaan kuormaan. Ylemmässä johtimessa kulkee virta I plusnavasta "
            "kuormaan päin. Napojen välinen jännite on napajännite U.")
    f.rect(70, 46, 170, 300, "none", MUTED, 2, rx=8, extra='stroke-dasharray="8 6"')
    f.tex(155, 372, r"\text{paristo}", "middle", MUTED)
    # inside: the source and the internal resistance on one vertical wire
    f.line(145, 90, 145, 300, INK, 2.5)
    f.line(145, 90, 280, 90, INK, 2.5); f.line(145, 300, 280, 300, INK, 2.5)
    cell(f, 145, 140)
    f.tex(110, 140, r"E", "end"); f.tex(178, 120, r"+", "start")
    f.rect(132, 200, 26, 64, WHITE, INK, 2.5)
    f.tex(118, 232, r"R_\text{s}", "end")
    # the poles
    for y in (90, 300): f.circle(280, y, 7, WHITE, INK, 2.5)
    # outside: the load
    f.line(287, 90, 500, 90, INK, 2.5); f.line(287, 300, 500, 300, INK, 2.5)
    f.line(500, 90, 500, 300, INK, 2.5)
    f.rect(487, 160, 26, 70, WHITE, INK, 2.5)
    f.tex(526, 195, r"\text{kuorma}", "start", MUTED, size=20)
    # the current in the top wire, the terminal voltage between the poles
    f.arrow(370, 90, 430, 90, INK, 3, 16); f.tex(400, 66, r"I", "middle")
    f.arrow(330, 195, 330, 104, MUTED, 2, 12); f.arrow(330, 195, 330, 286, MUTED, 2, 12)
    f.tex(344, 195, r"U", "start")
    return f.svg()


def circuit():
    """The guided circuit: cell, switch, ammeter, slide rheostat and protective resistor in series; the voltmeter
    straight across the cell's poles."""
    f = Fig("fy10pa-circuit", 360, "Kytkentäkaavio. Paristo, kytkin, virtamittari A, säädettävä vastus ja opettajan antama "
            "suojavastus on kytketty sarjaan yhdeksi silmukaksi. Jännitemittari V on kytketty rinnan suoraan pariston "
            "napoihin, pariston molemmin puolin olevista liitoskohdista.")
    L, R, T, B = 160, 480, 80, 300
    f.line(L, T, 235, T, INK, 2.5); f.line(285, T, 348, T, INK, 2.5); f.line(392, T, R, T, INK, 2.5)
    f.line(R, T, R, B, INK, 2.5); f.line(L, B, R, B, INK, 2.5); f.line(L, T, L, B, INK, 2.5)
    # the cell on the left side, + up
    cell(f, L, 190); f.tex(L + 34, 170, r"+", "start")
    # the voltmeter straight across the poles
    for y in (130, 250): f.circle(L, y, 5, INK)
    f.line(L, 130, 70, 130, INK, 2.5); f.line(L, 250, 70, 250, INK, 2.5)
    f.line(70, 130, 70, 166, INK, 2.5); f.line(70, 214, 70, 250, INK, 2.5)
    f.circle(70, 190, 24, WHITE, INK, 2.5); f.tex(70, 190, r"\text{V}", "middle")
    # switch on the top wire
    f.circle(235, T, 4, INK); f.circle(285, T, 4, INK); f.line(235, T, 281, T - 22, INK, 2.5)
    f.tex(260, T - 44, r"\text{kytkin}", "middle", MUTED, size=20)
    # ammeter on the top wire
    f.circle(370, T, 22, WHITE, INK, 2.5); f.tex(370, T, r"\text{A}", "middle")
    # the slide rheostat on the right side: a resistor with a diagonal arrow
    f.rect(R - 13, 150, 26, 80, WHITE, INK, 2.5)
    f.arrow(R - 30, 236, R + 28, 146, INK, 2, 12)
    f.tex(R - 40, 190, r"\text{säädettävä vastus}", "end", MUTED, size=20)
    # the protective resistor on the bottom wire
    f.rect(290, B - 13, 80, 26, WHITE, INK, 2.5)
    f.tex(330, B + 32, r"\text{suojavastus}", "middle", MUTED, size=20)
    return f.svg()


def curve():
    """The model U = E - R_s I: a falling line; solid where measurements can be made, dashed where it is extrapolated to
    the axes (E at I = 0, I_k at U = 0). No measured points."""
    f = Fig("fy10pa-curve", 340, "Kuvaaja: napajännite U virran I funktiona mallin U = E miinus R s kertaa I mukaan. Kuvaaja "
            "on laskeva suora. Pienten virtojen osa on piirretty yhtenäisellä viivalla: sillä alueella voidaan mitata. Suoran jatkeet "
            "akseleille on piirretty katkoviivalla. Pystyakselin leikkauskohta on lähdejännite E ja vaaka-akselin "
            "leikkauskohta oikosulkuvirta I k. Suoralle on merkitty muutokset delta I ja delta U; kulmakerroin on miinus "
            "R s. Kuvaajassa ei ole mittauspisteitä.")
    ax = Axes(f, (90, 280), (470, 50), x=(0, 10), y=(0, 10), xticks=[], yticks=[], xlabel=r"I", ylabel=r"U", grid=False)
    E, Ik = 8.0, 9.0
    U = lambda i: E - E / Ik * i
    ax.line([(0, E), (0.3, U(0.3))], INK, 3, "8 7")
    ax.line([(0.3, U(0.3)), (3.6, U(3.6))], INK)
    ax.line([(3.6, U(3.6)), (Ik, 0)], INK, 3, "8 7")
    f.line(ax.X(0) - 7, ax.Y(E), ax.X(0), ax.Y(E), INK, 2); f.tex(ax.X(0) - 12, ax.Y(E), r"E", "end")
    f.line(ax.X(Ik), ax.Y(0), ax.X(Ik), ax.Y(0) + 7, INK, 2); f.tex(ax.X(Ik), ax.Y(0) + 24, r"I_\text{k}", "middle")
    a, b = 0.9, 3.2
    f.line(ax.X(a), ax.Y(U(a)), ax.X(b), ax.Y(U(a)), MUTED, 2, "6 5")
    f.line(ax.X(b), ax.Y(U(a)), ax.X(b), ax.Y(U(b)), MUTED, 2, "6 5")
    f.tex((ax.X(a) + ax.X(b)) / 2, ax.Y(U(a)) - 20, r"\Delta I", "middle", MUTED)
    f.tex(ax.X(b) + 10, (ax.Y(U(a)) + ax.Y(U(b))) / 2, r"\Delta U", "start", MUTED)
    f.tex(ax.X(6.4), ax.Y(9.6), r"\text{kulmakerroin } \dfrac{\Delta U}{\Delta I} = -R_\text{s}", "middle")
    return f.svg()


FIGURES = {"hero": hero, "model": model, "circuit": circuit, "curve": curve}
