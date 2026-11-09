"""Figure of the Ahjo guide Anturi ja sarjaplotteri (scripts/figlib.py), drawn for this guide after nobody's picture: a
light-dependent resistor and a 10 kilo-ohm resistor as a voltage divider between 5V and GND, its middle point to the
analog input A0. The board is a generic box (Ahjo uses the Arduino Uno)."""
from figlib import Fig, INK, MUTED, WHITE, GLASS, n


def wire(f, *pts, w=3):
    f.add('<polyline points="' + " ".join(f"{n(x)},{n(y)}" for x, y in pts) + f'" fill="none" stroke="{INK}" '
          f'stroke-width="{w:g}" stroke-linejoin="round" stroke-linecap="round"/>')


def kytkenta():
    f = Fig("ahjo-plot-kytkenta", 330, "Kytkentäkaavio, ei mittakaavassa. Vasemmalla on Arduino-levy laatikkona, jonka "
            "oikeassa reunassa on kolme liitäntää: ylhäällä 5V, keskellä analogiatulo A0 ja alhaalla GND. Oikealla on "
            "pystysuora jännitteenjako: 5V-liitännästä johdin vie valovastukseen, jonka symbolina on laatikko ja kaksi "
            "siihen osoittavaa valonuolta. Valovastuksen alapäästä johdin jatkuu 10 kilo-ohmin vastukseen ja siitä "
            "GND-liitäntään. Valovastuksen ja 10 kilo-ohmin vastuksen välisestä kohdasta lähtee johdin A0-tuloon.")
    f.rect(30, 46, 160, 238, GLASS, INK, 2.5, rx=12)
    f.tex(110, 74, r"\text{Arduino}", "middle", size=22)
    y5, ya, yg, xr = 100, 165, 250, 430
    for y, lab in ((y5, r"\text{5V}"), (ya, r"\text{A0}"), (yg, r"\text{GND}")):
        f.rect(182, y - 8, 16, 16, WHITE, INK, 2)
        f.tex(172, y, lab, "end", size=22)
    wire(f, (198, y5), (xr, y5), (xr, 108))
    f.rect(xr - 10, 108, 20, 44, WHITE, INK, 3)                 # the LDR
    for dy in (0, 16):
        f.arrow(xr + 56, 104 + dy, xr + 16, 124 + dy, INK, 2, 8)
    f.tex(xr + 62, 96, r"\text{valovastus}", "start", size=20)
    wire(f, (xr, 152), (xr, 186)); f.circle(xr, ya, 5, INK); wire(f, (198, ya), (xr, ya))
    f.rect(xr - 10, 186, 20, 44, WHITE, INK, 3)                 # 10 kohm
    f.tex(xr + 20, 208, r"10\ \text{k}\Omega", "start", size=20)
    wire(f, (xr, 230), (xr, yg), (198, yg))
    f.tex(300, ya - 18, r"\text{jännitteenjaon keskikohta}", "middle", MUTED, size=18)
    return f.svg()


FIGURES = {"kytkenta": kytkenta}
