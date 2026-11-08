"""Figures of the Ahjo guide Arduino: ensimmäinen kytkentä (scripts/figlib.py); scripts/ahjo.py draws them into the
guide page in place of each `<svg data-fig="name"></svg>`, in the page's language (content/<lang>/ahjo/
ahjo-arduino.figures.json). Drawn for this guide, after nobody's picture: the circuit with the IEC symbols and the
violet conventional current of FY6 (fy6-14), and the same circuit on a breadboard, seen from above. The board is a
generic drawing of a board (Ahjo uses the Arduino Uno, teacher 2026-11-08), so no board's real layout is copied."""
from figlib import Fig, INK, MUTED, WHITE, RULE, HOT, COLD, COLD_LIGHT, GLASS, METAL_EDGE, n

CUR = "#7048e8"     # conventional current, as in FY6
LEAD = "#868e96"    # a component's metal leg


def wire(f, *pts, w=3, colour=INK):
    f.add('<polyline points="' + " ".join(f"{n(x)},{n(y)}" for x, y in pts) + f'" fill="none" stroke="{colour}" '
          f'stroke-width="{w:g}" stroke-linejoin="round" stroke-linecap="round"/>')


def head(f, x, y, d, colour=CUR):
    s = 10
    pts = {"r": [(x + s, y), (x - s, y - s * 0.8), (x - s, y + s * 0.8)], "l": [(x - s, y), (x + s, y - s * 0.8), (x + s, y + s * 0.8)],
           "d": [(x, y + s), (x - s * 0.8, y - s), (x + s * 0.8, y - s)]}[d]
    f.path("M" + " L".join(f"{n(a)},{n(b)}" for a, b in pts) + " Z", colour)


def led_symbol(f, x, y):
    """An LED on a vertical wire at x, centred on y, pointing down (anode above), with its two light arrows."""
    f.path(f"M{n(x - 16)},{n(y - 14)} L{n(x + 16)},{n(y - 14)} L{n(x)},{n(y + 14)} Z", HOT, INK, 2.5)
    f.line(x - 17, y + 14, x + 17, y + 14, INK, 3)
    for dy in (-9, 3):
        f.arrow(x + 22, y + dy, x + 40, y + dy - 15, INK, 2, 9)


def kytkenta():
    f = Fig("ahjo-ard-kytkenta", 300, "Kytkentäkaavio, ei mittakaavassa. Vasemmalla on Arduino-levy laatikkona, jonka "
            "oikeassa reunassa on kaksi liitäntää: ylempänä digitaalipinni D13 ja alempana maa GND. Pinnistä D13 johdin vie "
            "330 ohmin etuvastukseen R ja siitä punaiseen LEDiin, jonka kolmio osoittaa alaspäin: anodi on ylhäällä vastuksen "
            "puolella ja katodi eli poikkiviiva alhaalla. LEDin katodilta johdin palaa Arduinon GND-liitäntään. Violetit "
            "nuolet näyttävät virran I kulkevan pinnistä D13 vastuksen ja LEDin kautta maahan, kun pinni on tilassa HIGH.")
    f.rect(30, 46, 160, 208, GLASS, INK, 2.5, rx=12)
    f.tex(110, 74, r"\text{Arduino}", "middle", size=22)
    yp, yg, xl = 110, 214, 470
    for y, lab in ((yp, r"\text{D13}"), (yg, r"\text{GND}")):
        f.rect(182, y - 8, 16, 16, WHITE, INK, 2)
        f.tex(172, y, lab, "end", size=22)
    wire(f, (198, yp), (272, yp))
    f.rect(272, yp - 12, 60, 24, WHITE, INK, 3)
    f.tex(302, yp + 34, r"R = 330\ \Omega", "middle", size=22)
    wire(f, (332, yp), (xl, yp), (xl, 148))
    led_symbol(f, xl, 162)
    wire(f, (xl, 176), (xl, yg), (198, yg))
    f.tex(xl - 26, 146, r"\text{anodi}", "end", size=20)
    f.tex(xl - 26, 180, r"\text{katodi}", "end", size=20)
    f.tex(xl + 30, 194, r"\text{LED}", "start", size=22)
    head(f, 236, yp, "r"); f.tex(236, yp - 26, r"I", "middle", CUR, w=24)
    head(f, xl, 202, "d")
    head(f, 330, yg, "l")
    return f.svg()


# --- the same circuit on a breadboard -------------------------------------------------------------------------------
COLS = range(1, 13)
ROWS = "abcde"
def X(c): return 80 + (c - 1) * 40
def Y(r): return 110 + ROWS.index(r) * 30


def koekytkentalevy():
    f = Fig("ahjo-ard-levy", 392, "Piirros koekytkentälevystä ylhäältä päin, ei mittakaavassa. Levyssä on viisi "
            "vaakariviä a–e ja pystyrivit 1–12; saman pystyrivin viisi reikää on kytketty levyn sisällä yhteen. Pystyrivit "
            "5, 6 ja 10 on merkitty keltaisella. Punaisen LEDin lyhyt jalka eli katodi on reiässä a5 ja pitkä jalka eli "
            "anodi reiässä a6. 330 ohmin vastus (värirenkaat oranssi, oranssi, ruskea, kulta) on reikien b6 ja b10 välissä. "
            "Arduinon pinnistä 13 tuleva sininen johdin on reiässä e10, ja GND-liitännästä tuleva musta johdin reiässä e5. "
            "Virta kulkee siis pinnistä 13 pystyriviä 10 pitkin vastukseen, pystyriviä 6 pitkin LEDin anodille ja katodilta "
            "pystyriviä 5 pitkin maahan.")
    f.rect(40, 48, 520, 240, "#f4f1ea", RULE, 2, rx=10)
    for c in (5, 6, 10):
        f.rect(X(c) - 14, 96, 28, 148, "#fff1b8", rx=7)
    for c in COLS:
        f.tex(X(c), 266, str(c), "middle", MUTED, size=18, w=30)
        for r in ROWS:
            f.rect(X(c) - 4.5, Y(r) - 4.5, 9, 9, "#4a4f57", rx=1.5)
    for r in ROWS:
        f.tex(58, Y(r), rf"\text{{{r}}}", "middle", MUTED, size=18, w=24)
    # LED: the short leg (cathode) in a5, the long one (anode) in a6
    f.line(252, 88, X(5), Y("a"), LEAD, 3, cap="round"); f.line(268, 88, X(6), Y("a"), LEAD, 3, cap="round")
    f.circle(260, 78, 17, HOT, INK, 2)
    f.line(244, 70, 244, 86, INK, 2)                       # the flat edge on the cathode's side
    f.tex(232, 66, r"\text{katodi}", "end", size=20)
    f.tex(288, 66, r"\text{anodi}", "start", size=20)
    # resistor b6–b10, 330 ohm: orange, orange, brown, gold
    yb = Y("b")
    f.line(X(6), yb, 324, yb, LEAD, 3, cap="round"); f.line(396, yb, X(10), yb, LEAD, 3, cap="round")
    f.rect(324, yb - 10, 72, 20, "#e6d3a8", INK, 1.5, rx=9)
    for x, col in ((338, "#e8590c"), (350, "#e8590c"), (362, "#7a3e12"), (382, "#c9a227")):
        f.rect(x - 3, yb - 10, 6, 20, col)
    f.tex(520, 22, r"R = 330\ \Omega", "middle", size=20)
    f.line(486, 34, 398, yb - 8, MUTED, 1.5)
    # jumper wires from the Arduino: pin 13 to e10, GND to e5
    for x, dx, col in ((X(10), 20, COLD), (X(5), -20, INK)):     # bent aside so the column numbers stay readable
        wire(f, (x, Y("e")), (x + dx, Y("e") + 20), (x + dx, 338), w=6, colour=col)
        f.circle(x, Y("e"), 5, col)
    f.rect(150, 330, 380, 50, "#2b6f88", INK, 2, rx=8)
    f.rect(190, 336, 300, 14, INK, rx=2)
    for x in range(200, 490, 20):
        f.rect(x - 3, 340, 6, 6, METAL_EDGE)
    f.tex(X(5) - 20, 366, r"\text{GND}", "middle", WHITE, size=18)
    f.tex(X(10) + 20, 366, r"\text{13}", "middle", WHITE, size=18)
    f.tex(340, 366, r"\text{Arduino}", "middle", WHITE, size=18)
    return f.svg()


FIGURES = {"kytkenta": kytkenta, "koekytkentalevy": koekytkentalevy}
