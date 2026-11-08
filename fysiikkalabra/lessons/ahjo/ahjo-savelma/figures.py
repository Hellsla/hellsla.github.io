"""Figure of the Ahjo guide Summerin sävelmä (scripts/figlib.py): the passive piezo buzzer between pin 8 and ground,
with the IEC-style buzzer symbol, drawn for this guide after nobody's picture; the board is a generic box."""
from figlib import Fig, INK, MUTED, WHITE, GLASS, n


def wire(f, *pts, w=3):
    f.add('<polyline points="' + " ".join(f"{n(x)},{n(y)}" for x, y in pts) + f'" fill="none" stroke="{INK}" '
          f'stroke-width="{w:g}" stroke-linejoin="round" stroke-linecap="round"/>')


def kytkenta():
    f = Fig("ahjo-savel-kytkenta", 300, "Kytkentäkaavio, ei mittakaavassa. Vasemmalla on Arduino-levy laatikkona, jonka "
            "oikeassa reunassa on kaksi liitäntää: ylempänä digitaalipinni D8 ja alempana maa GND. Pinnistä D8 johdin vie "
            "pietsosummerin plusliitäntään. Summeri on piirretty laatikkona, jonka kyljessä on puoliympyrä, ja sen "
            "kaarevalta puolelta lähtee ääniaaltoja. Summerin toinen liitäntä palaa Arduinon GND-liitäntään.")
    f.rect(30, 46, 160, 208, GLASS, INK, 2.5, rx=12)
    f.tex(110, 74, r"\text{Arduino}", "middle", size=22)
    yp, yg, xs = 110, 214, 420
    for y, lab in ((yp, r"\text{D8}"), (yg, r"\text{GND}")):
        f.rect(182, y - 8, 16, 16, WHITE, INK, 2)
        f.tex(172, y, lab, "end", size=22)
    wire(f, (198, yp), (xs, yp), (xs, 140))
    wire(f, (xs, 188), (xs, yg), (198, yg))
    # buzzer: a box with a half disc, sound waves to the right
    f.rect(xs - 26, 140, 52, 48, WHITE, INK, 3, rx=3)
    f.path(f"M{xs + 26},{140} A24,24 0 0 1 {xs + 26},{188}", WHITE, INK, 3)
    for r in (40, 56):
        f.path(f"M{xs + 26 + r * 0.55},{164 - r * 0.6} A{r},{r} 0 0 1 {xs + 26 + r * 0.55},{164 + r * 0.6}", "none", MUTED, 2.5)
    f.tex(xs - 14, 124, r"+", "end", size=24)
    f.tex(xs - 40, 164, r"\text{summeri}", "end", size=22)
    return f.svg()


FIGURES = {"kytkenta": kytkenta}
