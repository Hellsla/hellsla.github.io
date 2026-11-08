"""Figure of the Ahjo guide Harjarobotti (scripts/figlib.py): the bristle robot from the side, drawn for this guide
after nobody's picture. The bristles slant with their tips behind their roots, so each shake pushes the robot forward,
to the right."""
from figlib import Fig, INK, MUTED, WHITE, RULE, COLD, ALUMINIUM, METAL_EDGE, IRON, n

BRUSH = "#74c0fc"
BRISTLE = "#4dabf7"


def robotti():
    f = Fig("ahjo-harja-robotti", 330, "Piirros harjarobotista sivulta, ei mittakaavassa. Pöydän päällä on hammasharjan "
            "pää, jonka harjakset ovat vinossa: harjasten kärjet ovat taaempana kuin niiden tyvet. Harjan selässä on "
            "edessä eli oikealla värinämoottori, jonka akselin päässä on puolikkaan kiekon muotoinen epäkeskopaino. "
            "Moottorin takana on nappiparisto plusnapa ylöspäin. Moottorin toinen johto kulkee pariston alle ja toinen "
            "pariston päälle. Oikealle osoittava nuoli näyttää liikesuunnan.")
    f.line(40, 262, 560, 262, RULE, 3)                      # the table
    f.tex(52, 284, r"\text{pöytä}", "start", MUTED, size=18)
    f.rect(130, 168, 320, 30, BRUSH, INK, 2.5, rx=10)        # the brush head, handle cut off
    for x in range(160, 431, 18):                           # bristles: tips behind roots
        f.line(x, 198, x - 24, 260, BRISTLE, 4, cap="round")
    f.tex(110, 226, r"\text{harjakset}", "end", size=20)
    # motor at the front
    f.rect(330, 132, 84, 36, ALUMINIUM, METAL_EDGE, 2.5, rx=8)
    f.line(414, 150, 428, 150, IRON, 4)
    f.path("M428,150 L428,124 A26,26 0 0 1 428,176 Z", IRON)
    f.tex(372, 74, r"\text{värinämoottori}", "middle", size=20)
    f.tex(560, 40, r"\text{epäkeskopaino}", "end", size=20)
    f.line(500, 54, 446, 130, MUTED, 1.5)
    # coin cell behind it, + up, one lead under and one on top
    f.rect(210, 150, 80, 12, METAL_EDGE, INK, 1.5, rx=3)
    f.rect(210, 162, 80, 6, ALUMINIUM, INK, 1.5, rx=2)
    f.tex(230, 120, r"\text{nappiparisto, + ylöspäin}", "middle", size=18)
    f.add('<polyline points="330,160 300,166 236,166" fill="none" stroke="#c92a2a" stroke-width="2.5"/>')
    f.add('<polyline points="330,142 300,142 270,148 260,150" fill="none" stroke="#1f2933" stroke-width="2.5"/>')
    f.arrow(470, 228, 548, 228, COLD, 4, 16)
    f.tex(509, 204, r"\text{liikesuunta}", "middle", COLD, size=20)
    return f.svg()


FIGURES = {"robotti": robotti}
