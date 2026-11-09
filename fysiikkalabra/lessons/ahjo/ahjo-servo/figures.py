"""Figure of the Ahjo guide Servo ja potentiometri (scripts/figlib.py), drawn for this guide after nobody's picture: the
wiring of the Arduino IDE's example Knob, a potentiometer between 5V and GND with its wiper to A0 and a hobby servo on
5V, GND and pin 9. The board and the servo are generic boxes (Ahjo uses the Arduino Uno)."""
from figlib import Fig, INK, WHITE, GLASS, n


def wire(f, *pts, w=3, colour=INK):
    f.add('<polyline points="' + " ".join(f"{n(x)},{n(y)}" for x, y in pts) + f'" fill="none" stroke="{colour}" '
          f'stroke-width="{w:g}" stroke-linejoin="round" stroke-linecap="round"/>')


def kytkenta():
    f = Fig("ahjo-servo-kytkenta", 360, "Kytkentäkaavio, ei mittakaavassa. Vasemmalla on Arduino-levy laatikkona, jonka "
            "oikeassa reunassa on neljä liitäntää ylhäältä alas: 5V, A0, GND ja pinni 9. Keskellä on potentiometri: sen "
            "yläpää on kytketty 5V:iin ja alapää GND:hen, ja keskimmäinen liitäntä eli liukuri on kytketty A0-tuloon. "
            "Oikealla on servo laatikkona, jossa on kolme johtoa: punainen 5V:iin, ruskea tai musta GND:hen ja oranssi tai "
            "keltainen ohjausjohto pinniin 9.")
    f.rect(30, 46, 160, 290, GLASS, INK, 2.5, rx=12)
    f.tex(110, 74, r"\text{Arduino}", "middle", size=22)
    y5, ya, yg, y9 = 100, 180, 260, 310
    for y, lab in ((y5, r"\text{5V}"), (ya, r"\text{A0}"), (yg, r"\text{GND}"), (y9, r"\text{9}")):
        f.rect(182, y - 8, 16, 16, WHITE, INK, 2)
        f.tex(172, y, lab, "end", size=22)
    xp = 290    # potentiometer: a resistor box with an arrow (the wiper) pointing at it
    wire(f, (198, y5), (480, y5)); f.circle(xp, y5, 5, INK)
    wire(f, (xp, y5), (xp, 156)); f.rect(xp - 10, 156, 20, 48, WHITE, INK, 3); wire(f, (xp, 204), (xp, yg))
    wire(f, (198, ya), (xp - 48, ya)); f.arrow(xp - 50, ya, xp - 13, ya, INK, 3, 10)
    f.tex(xp + 18, 226, r"\text{potentiometri}", "start", size=20)
    wire(f, (198, yg), (510, yg)); f.circle(xp, yg, 5, INK)
    f.rect(450, 150, 120, 70, WHITE, INK, 3, rx=8); f.tex(510, 185, r"\text{servo}", "middle", size=22)
    wire(f, (480, y5), (480, 150), colour="#c92a2a")
    wire(f, (510, 220), (510, yg), colour="#5c3b1e")
    wire(f, (545, 220), (545, y9), (198, y9), colour="#e8590c")
    return f.svg()


FIGURES = {"kytkenta": kytkenta}
