"""Figures of the investigation Planckin vakio LEDien avulla (scripts/figlib.py); `python scripts/investigations.py
figures fy10-planck` writes them into investigation.md. No force, velocity or acceleration arrows are drawn. The graphs
show models only, never invented measurements; the hero shows no reading, graph or result."""
import math
from figlib import Fig, Axes, INK, MUTED, WHITE, GLASS, ALUMINIUM, METAL_EDGE, IRON, SAND, SAND_DARK, GRAIN, \
    HEAT_LIGHT, HOT_LIGHT, COLD, COLD_LIGHT, GOOD, GOOD_LIGHT, RULE, n
import herolib as H
from herolib import grad

DISPLAY = "#2b3a42"       # a switched-on display without numbers
METER = "#f4c542"


def meter(f, x, y, w, h):
    """A multimeter: a box with a dark display (no digits), a selector knob and two sockets."""
    f.rect(x, y, w, h, METER, INK, 2.5, rx=10)
    f.rect(x + 12, y + 12, w - 24, h * 0.34, DISPLAY, INK, 2, rx=4)
    f.circle(x + w / 2, y + h * 0.66, h * 0.14, IRON, INK, 2.5)
    f.line(x + w / 2, y + h * 0.66, x + w / 2, y + h * 0.66 - h * 0.12, WHITE, 3)
    f.circle(x + w * 0.3, y + h - 12, 5, INK); f.circle(x + w * 0.7, y + h - 12, 5, INK)


def led(f, x, ybase, body, lit=False, glow=None, sc=1.0):
    """A through-hole LED standing on its two legs: a coloured dome on a rim; lit adds a soft glow."""
    if lit:
        f.add(f'<circle cx="{n(x)}" cy="{n(ybase - 62 * sc)}" r="{n(46 * sc)}" fill="{glow or body}" fill-opacity="0.35"/>')
        f.add(f'<circle cx="{n(x)}" cy="{n(ybase - 62 * sc)}" r="{n(30 * sc)}" fill="{glow or body}" fill-opacity="0.45"/>')
    f.line(x - 6 * sc, ybase - 34 * sc, x - 6 * sc, ybase, METAL_EDGE, 3 * sc)
    f.line(x + 6 * sc, ybase - 34 * sc, x + 6 * sc, ybase - 6 * sc, METAL_EDGE, 3 * sc)
    f.rect(x - 17 * sc, ybase - 42 * sc, 34 * sc, 8 * sc, body, INK, 2, rx=2)
    f.path(f"M{n(x - 14 * sc)},{n(ybase - 42 * sc)} L{n(x - 14 * sc)},{n(ybase - 70 * sc)} "
           f"A{n(14 * sc)},{n(14 * sc)} 0 0 1 {n(x + 14 * sc)},{n(ybase - 70 * sc)} L{n(x + 14 * sc)},{n(ybase - 42 * sc)} Z",
           body, INK, 2)


def hero():
    """The opening illustration: a lab bench with a low-voltage supply, an adjustable resistor, two meters and one LED
    lit in the circuit; LEDs of other colours wait unlit in a tray, beside a datasheet and a notebook."""
    f = H.hero("fy10pl-hero", "Kuvitus: laboratorion työpöydällä on pienjännitelähde, säädettävä liukuvastus ja kaksi "
               "yleismittaria, joiden näytöissä ei ole lukemia. Johdot kulkevat kytkentäalustalle, jossa yksi LED loistaa "
               "himmeästi. Pöydällä on rasia, jossa on erivärisiä sammuneita LEDejä, sekä LEDien tietolehti ja vihko.")
    f.rect(0, 0, 1200, 600, grad(f, "fy10plh-wall", GLASS, "#dfe9ef"))
    f.rect(0, 470, 1200, 130, grad(f, "fy10plh-desk", SAND_DARK, SAND, horizontal=True))
    for k in range(5): f.line(0, 492 + 22 * k, 1200, 488 + 22 * k, GRAIN, 1.5)
    f.line(0, 470, 1200, 470, INK, 3)
    # low-voltage supply with a knob and two sockets
    f.rect(60, 300, 220, 170, ALUMINIUM, INK, 2.5, rx=10)
    f.rect(84, 324, 120, 46, DISPLAY, INK, 2, rx=4)
    f.circle(240, 347, 20, IRON, INK, 2.5); f.line(240, 347, 252, 333, WHITE, 3)
    f.circle(110, 430, 9, INK, INK, 2); f.circle(230, 430, 9, "#e9ecef", INK, 2.5)
    # adjustable (slide) resistor: a wound tube on two end blocks, a rod with a slider
    f.rect(340, 400, 26, 70, IRON, INK, 2.5, rx=3); f.rect(574, 400, 26, 70, IRON, INK, 2.5, rx=3)
    f.rect(366, 412, 208, 46, "#d9a066", INK, 2.5, rx=8)
    for k in range(26): f.line(372 + 8 * k, 413, 372 + 8 * k, 457, "#a5653a", 2)
    f.rect(350, 384, 240, 8, ALUMINIUM, INK, 2, rx=3)
    f.rect(468, 376, 30, 36, IRON, INK, 2.5, rx=4)
    # two meters
    meter(f, 640, 330, 120, 140)
    meter(f, 800, 330, 120, 140)
    # breadboard with the lit LED
    f.rect(960, 430, 200, 40, WHITE, INK, 2.5, rx=4)
    for r in range(2):
        for c in range(16): f.rect(972 + 11.5 * c, 440 + 13 * r, 5, 5, RULE)
    led(f, 1060, 440, HOT_LIGHT, lit=True)
    f.rect(1090, 430, 40, 10, "#d9a066", INK, 2, rx=4)        # a fixed series resistor on the board
    # wires (no current direction shown)
    def wire(d, c=INK): f.path(d, stroke=c, w=3.5)
    wire("M230,430 C230,520 350,500 353,470")                     # supply + to the resistor end
    wire("M483,376 C483,300 640,290 676,458")                    # slider to meter 1
    wire("M724,458 C780,492 1060,492 1110,440")                  # meter 1 to series resistor
    wire("M1054,410 C1000,300 840,300 836,458", IRON)             # voltmeter across the LED
    wire("M1066,410 C1080,320 900,320 884,458", IRON)
    wire("M110,430 C110,488 1000,488 1040,470")                  # supply - back to the board
    # tray of unlit LEDs of other colours
    f.rect(420, 500, 230, 50, WHITE, INK, 2.5, rx=6)
    for k, c in enumerate([HEAT_LIGHT, GOOD_LIGHT, COLD_LIGHT, "#ffe066", "#ffd8a8"]):
        led(f, 450 + 42 * k, 540, c, sc=0.55)
    # datasheet and notebook
    f.add('<g transform="translate(790,535) rotate(4)">'
          f'<rect x="-60" y="-40" width="120" height="70" rx="3" fill="{WHITE}" stroke="{INK}" stroke-width="2.5"/>'
          + "".join(f'<line x1="-46" y1="{-26 + 11 * k}" x2="{46 - 18 * (k % 2)}" y2="{-26 + 11 * k}" stroke="{MUTED}" stroke-width="2"/>' for k in range(5))
          + "</g>")
    f.add('<g transform="translate(130,530) rotate(-6)">'
          f'<rect x="-80" y="-34" width="200" height="66" rx="4" fill="{WHITE}" stroke="{INK}" stroke-width="2.5"/>'
          + "".join(f'<line x1="-64" y1="{-18 + 12 * k}" x2="104" y2="{-18 + 12 * k}" stroke="{COLD}" stroke-width="1.5" stroke-opacity="0.6"/>' for k in range(5))
          + "</g>")
    return f.svg()


def resistor(f, x1, x2, y, variable=False):
    """A resistor symbol (a rectangle) on a horizontal wire from x1 to x2; variable adds a diagonal arrow."""
    m = (x1 + x2) / 2
    f.line(x1, y, m - 34, y, INK, 2.5); f.line(m + 34, y, x2, y, INK, 2.5)
    f.rect(m - 34, y - 13, 68, 26, WHITE, INK, 2.5)
    if variable: f.arrow(m - 40, y + 26, m + 42, y - 28, INK, 2, 12)


def meter_symbol(f, x, y, letter):
    f.circle(x, y, 22, WHITE, INK, 2.5); f.tex(x, y, r"\mathrm{" + letter + "}", "middle", size=22)


def led_symbol(f, x, y1, y2):
    """An LED on a vertical wire from y1 (top) to y2: triangle pointing down (forward direction), bar, two arrows out."""
    m = (y1 + y2) / 2
    f.line(x, y1, x, m - 18, INK, 2.5); f.line(x, m + 18, x, y2, INK, 2.5)
    f.path(f"M{n(x - 20)},{n(m - 18)} L{n(x + 20)},{n(m - 18)} L{n(x)},{n(m + 16)} Z", WHITE, INK, 2.5)
    f.line(x - 22, m + 17, x + 22, m + 17, INK, 3)
    for d in (0, 16):
        f.arrow(x + 22, m - 10 + d, x + 46, m - 26 + d, INK, 2, 10)


def setup():
    """The circuit: supply, a resistor that limits the current, an ammeter in series and a voltmeter across the LED only."""
    f = Fig("fy10pl-setup", 400, "Kytkentäkaavio. Tasajännitelähteen plusnavasta virta kulkee kiinteän suojavastuksen R s ja "
            "säädettävän vastuksen R kautta LEDiin ja siitä virtamittarin kautta takaisin miinusnapaan. LED on kytketty "
            "päästösuuntaan. Vastukset rajoittavat virtaa, ja virtamittari on sarjassa LEDin kanssa ja mittaa sähkövirran I. Jännitemittari on kytketty suoraan "
            "LEDin napoihin eli rinnan LEDin kanssa, ja se mittaa LEDin jännitteen U.")
    # supply on the left
    f.rect(30, 140, 130, 110, ALUMINIUM, INK, 2.5, rx=6)
    f.tex(95, 170, r"\text{tasa-}", "middle", size=20); f.tex(95, 196, r"\text{jännite-}", "middle", size=20)
    f.tex(95, 222, r"\text{lähde}", "middle", size=20)
    f.circle(160, 80, 5, INK); f.circle(160, 320, 5, INK)
    f.line(140, 140, 140, 80, INK, 2.5); f.line(140, 80, 160, 80, INK, 2.5)
    f.line(140, 250, 140, 320, INK, 2.5); f.line(140, 320, 160, 320, INK, 2.5)
    f.tex(130, 104, r"+", "end", size=22); f.tex(130, 296, r"-", "end", size=22)
    # top wire: the fixed protective resistor and the adjustable resistor; bottom wire: the ammeter
    resistor(f, 160, 290, 80)
    f.tex(225, 40, r"R_\text{s}", "middle")
    resistor(f, 290, 420, 80, variable=True)
    f.tex(355, 34, r"R", "middle")
    f.tex(290, 362, r"I", "middle")
    # LED on the right branch
    f.line(420, 80, 420, 140, INK, 2.5)
    led_symbol(f, 420, 140, 260)
    f.line(420, 260, 420, 320, INK, 2.5); f.line(160, 320, 268, 320, INK, 2.5); f.line(312, 320, 420, 320, INK, 2.5)
    meter_symbol(f, 290, 320, "A")
    # voltmeter directly across the LED
    f.circle(420, 140, 5, INK); f.circle(420, 260, 5, INK)
    f.line(420, 140, 530, 140, INK, 2.5); f.line(530, 140, 530, 178, INK, 2.5)
    meter_symbol(f, 530, 200, "V")
    f.line(530, 222, 530, 260, INK, 2.5); f.line(420, 260, 530, 260, INK, 2.5)
    f.tex(562, 200, r"U", "start")
    f.tex(372, 200, r"\text{LED}", "end", MUTED, size=20)
    return f.svg()


def iu():
    """The model of an LED's current against voltage: almost no current, then a steep nearly straight rise; the straight
    part extended to the voltage axis gives the threshold voltage (no measured points)."""
    f = Fig("fy10pl-iu", 330, "Kuvaaja: LEDin sähkövirta I jännitteen U funktiona mallin mukaan. Pienillä jännitteillä virta "
            "on lähes nolla. Tietyn jännitteen jälkeen virta kasvaa jyrkästi ja lähes suoraviivaisesti. Jyrkän osan suora on "
            "jatkettu katkoviivalla vaaka-akselille, ja leikkauskohta on merkitty kynnysjännitteeksi U k. Kuvaajassa ei ole "
            "mittauspisteitä.")
    ax = Axes(f, (90, 280), (470, 50), x=(0, 10), y=(0, 10), xticks=[], yticks=[], xlabel=r"U", ylabel=r"I", grid=False)
    u0, s, a = 5.5, 0.35, 3.2
    ax.curve(lambda u: a * s * math.log1p(math.exp((u - u0) / s)), 0, 8.4, INK)
    ax.line([(u0, 0), (8.6, a * (8.6 - u0))], MUTED, 2.5, "7 5")
    f.line(ax.X(u0), ax.y0 - 8, ax.X(u0), ax.y0 + 8, INK, 2.5)
    f.tex(ax.X(u0), ax.y0 + 24, r"U_\text{k}", "middle")
    f.tex(ax.X(4.6), ax.Y(7.2), r"\text{jyrkän osan suora}", "end", MUTED, size=20)
    f.line(ax.X(4.7), ax.Y(7.0), ax.X(7.2), ax.Y(5.6), MUTED, 1.5)
    return f.svg()


def model():
    """The linearised model: threshold voltage against 1/lambda is a line, slope hc/e (no measured points)."""
    f = Fig("fy10pl-model", 330, "Kuvaaja: kynnysjännite U k aallonpituuden käänteisluvun yksi per lambda funktiona mallin "
            "mukaan. Kuvaaja on origon kautta kulkeva suora, jonka kulmakerroin on h kertaa c jaettuna e:llä. Kuvaajassa ei "
            "ole mittauspisteitä.")
    ax = Axes(f, (90, 280), (470, 50), x=(0, 10), y=(0, 10), xticks=[], yticks=[], xlabel=r"\dfrac{1}{\lambda}",
              ylabel=r"U_\text{k}", grid=False)
    ax.line([(0, 0), (9.5, 8.55)], INK)
    f.tex(ax.X(3.4), ax.Y(7.6), r"\text{kulmakerroin } \dfrac{hc}{e}", "middle")
    return f.svg()


def grating():
    """The extension, seen from above: an LED behind a slit and a scale, a grating at distance L, the eye behind it;
    the eye sees the first-order image of the slit at distance x along the scale (angle theta)."""
    f = Fig("fy10pl-grating", 360, "Kaaviokuva ylhäältä. Vasemmalla on kapea rako, jonka takana on LED, ja raon kohdalla "
            "poikittainen mitta-asteikko. Oikealla etäisyydellä L asteikosta on hila ja sen takana silmä. Valo kulkee raosta "
            "suoraan hilaan. Silmä näkee raon värillisen kuvan asteikolla etäisyydellä x raosta, suunnassa, joka poikkeaa "
            "kulman theta verran raon suunnasta.")
    xs, xg, ys = 110, 470, 250
    # scale across the slit, LED behind it
    f.rect(xs - 6, 40, 12, 280, "#ffe8a3", INK, 2)
    for k in range(14): f.line(xs + 6, 52 + 20 * k, xs + (16 if k % 5 == 0 else 12), 52 + 20 * k, INK, 1.5)
    f.rect(xs - 8, ys - 5, 16, 10, WHITE, INK, 2)
    f.rect(48, ys - 16, 34, 32, HOT_LIGHT, INK, 2, rx=6); f.tex(40, ys, r"\text{LED}", "end", MUTED, size=18)
    # grating and the eye
    f.line(xg, ys - 90, xg, ys + 50, INK, 4)
    for k in range(10): f.line(xg - 4, ys - 84 + 13 * k, xg + 4, ys - 84 + 13 * k, WHITE, 1.5)
    f.tex(xg + 10, ys - 104, r"\text{hila}", "start", MUTED, size=20)
    f.path(f"M{xg + 30},{ys - 14} Q{xg + 56},{ys - 30} {xg + 82},{ys} Q{xg + 56},{ys + 30} {xg + 30},{ys + 14}", WHITE, INK, 2.5)
    f.circle(xg + 46, ys, 8, INK)
    f.tex(xg + 70, ys + 44, r"\text{silmä}", "middle", MUTED, size=20)
    # light from the slit straight to the grating, and the apparent direction of the first-order image
    f.arrow(xs + 8, ys, xg - 2, ys, GOOD, 3, 14)
    xi = 110
    yi = ys - 150
    f.line(xg, ys, xs + 8, yi, GOOD, 2, "8 6")
    f.circle(xs, yi, 7, GOOD_LIGHT, GOOD, 2)
    # angle theta at the grating
    r = 70; a = math.atan2(ys - yi, xg - xs - 8)
    f.path(f"M{n(xg - r)},{ys} A{r},{r} 0 0 1 {n(xg - r * math.cos(a))},{n(ys - r * math.sin(a))}", stroke=INK, w=2)
    f.tex(xg - r - 14, ys - 22, r"\theta", "end")
    # dimensions L and x
    f.line(xs, ys + 70, xg, ys + 70, MUTED, 1.5); f.line(xs, ys + 60, xs, ys + 80, MUTED, 2); f.line(xg, ys + 60, xg, ys + 80, MUTED, 2)
    f.tex((xs + xg) / 2, ys + 92, r"L", "middle")
    f.line(xs - 28, yi, xs - 28, ys, MUTED, 1.5); f.line(xs - 38, yi, xs - 18, yi, MUTED, 2); f.line(xs - 38, ys, xs - 18, ys, MUTED, 2)
    f.tex(xs - 42, (yi + ys) / 2, r"x", "end")
    return f.svg()


FIGURES = {"hero": hero, "setup": setup, "iu": iu, "model": model, "grating": grating}
