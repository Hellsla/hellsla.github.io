"""Figures of the investigation Valaistusvoimakkuuden riippuvuus etäisyydestä (scripts/figlib.py); `python
scripts/investigations.py figures fy10-valaistus` writes them into investigation.md. No arrows of force, velocity or
acceleration are drawn. The graph shows models only, never invented measurements."""
from figlib import (Fig, Axes, INK, MUTED, WHITE, GLASS, ALUMINIUM, METAL_EDGE, IRON, SAND, SAND_DARK, GRAIN,
                    HEAT_LIGHT, SAND_LIGHT, RULE, n)
import herolib as H
from herolib import grad, glow

SCALE = "#ffe8a3"     # the yellow of a measuring tape, as in the sibling investigations


def bulb(f, cx, cy, r, w=2.5):
    """A clear bulb in a socket: glass, a small filament in the centre and the socket below."""
    f.circle(cx, cy, r, WHITE, INK, w)
    k = r * 0.28
    f.path(f"M{n(cx - k)},{n(cy + r * 0.55)} L{n(cx - k)},{n(cy)} L{n(cx - k / 2)},{n(cy - k / 2)} L{n(cx)},{n(cy)} "
           f"L{n(cx + k / 2)},{n(cy - k / 2)} L{n(cx + k)},{n(cy)} L{n(cx + k)},{n(cy + r * 0.55)}", stroke=INK, w=1.8)
    f.rect(cx - r * 0.5, cy + r * 0.85, r, r * 0.55, IRON, INK, w, rx=2)


def sensor(f, x, cy, h, w=2.5):
    """A light sensor seen from the side: a body whose sensitive face (white) points left, towards the lamp."""
    f.rect(x, cy - h / 2, h * 0.5, h, IRON, INK, w, rx=4)
    f.rect(x - 6, cy - h * 0.32, 8, h * 0.64, WHITE, INK, w * 0.8, rx=2)


def hero():
    """The opening illustration: a darkened room, a small clear lamp on a stand and a light sensor on its own stand at
    the same height, its face towards the lamp; a measuring stick on the desk, the sensor's cable to a logger, a notebook."""
    f = H.hero("fy10v-hero", "Kuvitus: pimennetyssä huoneessa pöydällä palaa pieni kirkas lamppu telineessään. Samalla korkeudella "
               "on valoanturi omassa telineessään, ja sen herkkä pinta on suunnattu lamppua kohti. Pöydän reunalla on mittatikku, "
               "joka ulottuu lampun kohdalta anturin ohi. Anturin johto kulkee pöydällä olevaan mittauslaitteeseen, ja "
               "vieressä on vihko.")
    f.rect(0, 0, 1200, 600, grad(f, "fy10vh-wall", INK, MUTED))
    f.rect(0, 440, 1200, 160, grad(f, "fy10vh-desk", SAND_DARK, SAND, horizontal=True))
    for k in range(6): f.line(0, 462 + 22 * k, 1200, 458 + 22 * k, GRAIN, 1.5)
    f.line(0, 440, 1200, 440, INK, 3)
    # the lamp's glow, then the lamp on its stand
    f.circle(250, 270, 230, glow(f, "fy10vh-glow", SAND_LIGHT, HEAT_LIGHT))
    f.rect(190, 426, 120, 16, IRON, INK, 2.5, rx=4)
    f.rect(243, 310, 14, 118, ALUMINIUM, INK, 2.5)
    bulb(f, 250, 266, 34)
    # the sensor on its stand at the bulb's height, its face towards the lamp
    f.rect(720, 426, 100, 16, IRON, INK, 2.5, rx=4)
    f.rect(763, 300, 14, 128, ALUMINIUM, INK, 2.5)
    sensor(f, 756, 266, 64)
    # the cable to a logger whose screen is blank
    f.path("M788,280 C840,300 820,400 900,410", stroke=INK, w=3)
    f.rect(890, 390, 150, 52, IRON, INK, 2.5, rx=6)
    f.rect(904, 400, 90, 32, GLASS, INK, 2, rx=3)
    f.circle(1016, 416, 8, ALUMINIUM, INK, 2)
    # the measuring stick along the desk's front edge
    f.rect(220, 470, 640, 26, SCALE, INK, 2.5, rx=3)
    for k in range(64):
        f.line(230 + 10 * k, 470, 230 + 10 * k, 470 + (14 if k % 10 == 0 else 8 if k % 5 == 0 else 5), INK, 1.5)
    # a notebook
    f.add('<g transform="translate(1040,535) rotate(-5)">'
          f'<rect x="-90" y="-34" width="190" height="66" rx="4" fill="{WHITE}" stroke="{INK}" stroke-width="2.5"/>'
          + "".join(f'<line x1="-74" y1="{-18 + 12 * k}" x2="84" y2="{-18 + 12 * k}" stroke="{MUTED}" stroke-width="1.5" stroke-opacity="0.6"/>' for k in range(5))
          + "</g>")
    return f.svg()


def setup():
    """The measurement: the distance r is measured from the glowing filament to the sensor's sensitive face, on the line
    between them; the face is perpendicular to that line."""
    f = Fig("fy10v-setup", 320, "Kaaviokuva. Vasemmalla on lamppu telineessään ja oikealla valoanturi telineessään samalla korkeudella. "
            "Anturin herkkä pinta on kohtisuorassa lampun ja anturin väliseen suoraan nähden. Etäisyys r mitataan lampun "
            "hehkulangasta anturin herkkään pintaan.")
    y = 160
    # stands
    f.rect(50, 278, 100, 14, IRON, INK, 2.5, rx=3); f.rect(93, y + 38, 14, 82, ALUMINIUM, INK, 2.5)
    f.rect(430, 278, 100, 14, IRON, INK, 2.5, rx=3); f.rect(475, y + 32, 14, 88, ALUMINIUM, INK, 2.5)
    bulb(f, 100, y, 28)
    sensor(f, 468, y, 64)
    # the line between them
    f.line(100, y, 460, y, MUTED, 1.5, "6 5")
    # dimension line r above, from the filament to the sensor face
    f.line(100, y - 32, 100, 70, MUTED, 1.5, "4 4"); f.line(462, y - 22, 462, 70, MUTED, 1.5, "4 4")
    f.line(100, 80, 462, 80, INK, 2)
    f.line(100, 70, 100, 90, INK, 2); f.line(462, 70, 462, 90, INK, 2)
    f.tex(281, 58, r"r", "middle")
    f.tex(100, 306, r"\text{lamppu}", "middle", MUTED)
    f.tex(480, 306, r"\text{anturi}", "middle", MUTED)
    f.tex(300, 186, r"\text{herkkä pinta lamppua kohti}", "middle", MUTED, size=20)
    return f.svg()


def spread():
    """The principle: the light that passes through an area A at distance r spreads over 4A at distance 2r."""
    f = Fig("fy10v-spread", 380, "Kaaviokuva. Pistemäisestä valonlähteestä lähtevä valo kulkee suorina viivoina. Etäisyydellä r se "
            "valaisee neliön, jonka pinta-ala on A. Kaksinkertaisella etäisyydellä 2r sama valo leviää neliöön, jonka sivu on "
            "kaksinkertainen ja pinta-ala neljä kertaa suurempi, 4A. Suurempi neliö on jaettu neljään A:n kokoiseen osaan.")
    sx, sy = 50, 190
    P = lambda x, yy, z: (sx + x - 0.4 * z, sy - yy + 0.4 * z)
    def square(r, s):
        return [P(r, -s / 2, -s / 2), P(r, s / 2, -s / 2), P(r, s / 2, s / 2), P(r, -s / 2, s / 2)]
    r1, s1, r2, s2 = 190, 70, 380, 140
    q1, q2 = square(r1, s1), square(r2, s2)
    poly = lambda q: "M" + " L".join(f"{n(a)},{n(b)}" for a, b in q) + " Z"
    f.path(poly(q2), HEAT_LIGHT, INK, 2.5, 'fill-opacity="0.45"')
    a, b = P(r2, 0, -s2 / 2), P(r2, 0, s2 / 2); f.line(*a, *b, INK, 1.5)
    a, b = P(r2, -s2 / 2, 0), P(r2, s2 / 2, 0); f.line(*a, *b, INK, 1.5)
    for c in q2: f.line(sx, sy, *c, MUTED, 1.5, "6 5")
    f.path(poly(q1), HEAT_LIGHT, INK, 2.5, 'fill-opacity="0.85"')
    f.circle(sx, sy, 7, INK)
    f.tex(P(r1, s1 / 2, -s1 / 2)[0] + 4, P(r1, s1 / 2, -s1 / 2)[1] - 16, r"A", "middle")
    f.tex(P(r2, s2 / 2, -s2 / 2)[0] + 36, P(r2, s2 / 2, -s2 / 2)[1] + 8, r"4A", "start")
    # distances along the bottom
    for x_end, yy, lab in ((sx + r1, 326, r"r"), (sx + r2, 360, r"2r")):
        f.line(sx, yy, x_end, yy, INK, 2); f.line(sx, yy - 9, sx, yy + 9, INK, 2); f.line(x_end, yy - 9, x_end, yy + 9, INK, 2)
        f.tex(x_end + 10, yy, lab, "start")
    f.line(sx, sy + 12, sx, 352, MUTED, 1.5, "4 4")
    return f.svg()


def model():
    """The model graph: E against 1/r^2 is a line through the origin with slope I when the background light has been
    subtracted, and a parallel line raised by the background when it has not (no measured points)."""
    f = Fig("fy10v-model", 340, "Kuvaaja: valaistusvoimakkuus E etäisyyden neliön käänteisarvon, yksi per r toiseen, funktiona "
            "mallin mukaan. Kun taustavalo on vähennetty, kuvaaja on origon kautta kulkeva suora, jonka kulmakerroin on valovoima I. "
            "Kun taustavaloa ei ole vähennetty, kuvaaja on samansuuntainen suora, joka leikkaa pystyakselin taustavalon "
            "valaistusvoimakkuuden kohdalla. Kuvaajassa ei ole mittauspisteitä.")
    ax = Axes(f, (120, 290), (470, 50), x=(0, 10), y=(0, 10), xticks=[], yticks=[], xlabel=r"1/r^2", ylabel=r"E", grid=False)
    ax.line([(0, 0), (9.5, 7.6)], INK)
    ax.line([(0, 1.8), (9.5, 9.4)], MUTED, 3, "8 6")
    f.tex(ax.X(0) - 10, ax.Y(1.8), r"E_\text{tausta}", "end", MUTED, size=20)
    f.line(ax.X(0) - 6, ax.Y(1.8), ax.X(0), ax.Y(1.8), INK, 2)
    f.tex(ax.X(0.6), ax.Y(8.4), r"\text{taustavalo mukana}", "start", MUTED)
    f.tex(ax.X(5.4), ax.Y(2.2), r"\text{taustavalo vähennetty}", "start")
    f.tex(ax.X(7.0), ax.Y(4.4), r"\text{kulmakerroin } I", "start")
    return f.svg()


FIGURES = {"hero": hero, "setup": setup, "spread": spread, "model": model}
