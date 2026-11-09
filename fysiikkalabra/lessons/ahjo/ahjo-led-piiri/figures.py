"""Figures of the Ahjo guide LED-piiri ilman ohjelmaa (scripts/figlib.py), drawn for this guide after nobody's picture:
an LED and its series resistor powered from the Arduino's 5V pin (no program), and the same LED twice, in series and in
parallel, each parallel branch with its own resistor. The board is a generic box (Ahjo uses the Arduino Uno)."""
from figlib import Fig, INK, WHITE, HOT, GLASS, n

CUR = "#7048e8"     # conventional current, as in FY6


def wire(f, *pts, w=3):
    f.add('<polyline points="' + " ".join(f"{n(x)},{n(y)}" for x, y in pts) + f'" fill="none" stroke="{INK}" '
          f'stroke-width="{w:g}" stroke-linejoin="round" stroke-linecap="round"/>')


def led(f, x, y):
    """An LED on a vertical wire at x, centred on y, pointing down (anode above), with its two light arrows."""
    f.path(f"M{n(x - 14)},{n(y - 12)} L{n(x + 14)},{n(y - 12)} L{n(x)},{n(y + 12)} Z", HOT, INK, 2.5)
    f.line(x - 15, y + 12, x + 15, y + 12, INK, 3)
    for dy in (-8, 3):
        f.arrow(x + 20, y + dy, x + 36, y + dy - 13, INK, 2, 8)


def res(f, x, y):
    """A resistor (IEC box) on a vertical wire at x, centred on y."""
    f.rect(x - 10, y - 24, 20, 48, WHITE, INK, 3)


def kytkenta():
    f = Fig("ahjo-led-kytkenta", 300, "Kytkentäkaavio, ei mittakaavassa. Vasemmalla on Arduino-levy laatikkona, jonka "
            "oikeassa reunassa on kaksi liitäntää: ylempänä 5V ja alempana maa GND. 5V-liitännästä johdin vie 330 ohmin "
            "vastukseen R ja siitä punaiseen LEDiin, jonka kolmio osoittaa alaspäin: anodi on ylhäällä vastuksen puolella "
            "ja katodi alhaalla. LEDiltä johdin palaa GND-liitäntään. Violetti nuoli näyttää virran I suunnan. Ohjelmaa ei "
            "tarvita, sillä 5V-liitännässä on jännite aina, kun USB-johto on kytketty.")
    f.rect(30, 46, 160, 208, GLASS, INK, 2.5, rx=12)
    f.tex(110, 74, r"\text{Arduino}", "middle", size=22)
    yp, yg, xl = 110, 214, 430
    for y, lab in ((yp, r"\text{5V}"), (yg, r"\text{GND}")):
        f.rect(182, y - 8, 16, 16, WHITE, INK, 2)
        f.tex(172, y, lab, "end", size=22)
    wire(f, (198, yp), (290, yp)); f.rect(290, yp - 10, 56, 20, WHITE, INK, 3); wire(f, (346, yp), (xl, yp), (xl, 150))
    f.tex(318, yp + 34, r"R = 330\ \Omega", "middle", size=22)
    led(f, xl, 162)
    wire(f, (xl, 174), (xl, yg), (198, yg))
    f.tex(xl + 26, 196, r"\text{LED}", "start", size=22)
    f.path(f"M{n(258)},{n(yp)} L{n(244)},{n(yp - 9)} L{n(244)},{n(yp + 9)} Z", CUR)
    f.tex(244, yp - 26, r"I", "middle", CUR, w=24)
    return f.svg()


def sarja_rinnan():
    f = Fig("ahjo-led-sarja-rinnan", 330, "Kaksi kytkentäkaaviota vierekkäin, ei mittakaavassa. Vasemmalla sarjaankytkentä: "
            "5V-liitännästä virta kulkee yhden 330 ohmin vastuksen ja kahden peräkkäisen LEDin kautta GND-liitäntään, eli "
            "virralla on vain yksi reitti. Oikealla rinnankytkentä: 5V-liitännästä lähtee kaksi haaraa, ja kummassakin haarassa "
            "on oma 330 ohmin vastus ja oma LED ennen kuin haarat yhdistyvät GND-liitäntään.")
    # series, left
    x = 150
    f.tex(x, 30, r"\text{sarjaan}", "middle", size=22)
    f.tex(x - 40, 62, r"\text{5V}", "end", size=20); wire(f, (x - 34, 62), (x, 62), (x, 86))
    res(f, x, 110); f.tex(x + 20, 110, r"330\ \Omega", "start", size=20)
    wire(f, (x, 134), (x, 166)); led(f, x, 178); wire(f, (x, 190), (x, 226)); led(f, x, 238); wire(f, (x, 250), (x, 292), (x - 34, 292))
    f.tex(x - 40, 292, r"\text{GND}", "end", size=20)
    # parallel, right
    a, b = 380, 500
    f.tex((a + b) / 2, 30, r"\text{rinnan}", "middle", size=22)
    f.tex(a - 40, 62, r"\text{5V}", "end", size=20); wire(f, (a - 34, 62), (b, 62))
    for xb in (a, b):
        wire(f, (xb, 62), (xb, 86)); res(f, xb, 110); f.tex(xb + 16, 146, r"330\ \Omega", "start", size=18)
        wire(f, (xb, 134), (xb, 186)); led(f, xb, 198); wire(f, (xb, 210), (xb, 292))
    wire(f, (a - 34, 292), (b, 292)); f.tex(a - 40, 292, r"\text{GND}", "end", size=20)
    for xb in (a, b): f.circle(xb, 62, 5, INK)
    for xb in (a, b): f.circle(xb, 292, 5, INK)
    return f.svg()


FIGURES = {"kytkenta": kytkenta, "sarja-rinnan": sarja_rinnan}
