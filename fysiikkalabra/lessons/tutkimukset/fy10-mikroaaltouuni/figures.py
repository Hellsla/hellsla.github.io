"""Figures of the investigation Valonnopeuden määrittäminen mikroaaltouunilla (scripts/figlib.py); `python
scripts/investigations.py figures fy10-mikroaaltouuni` writes them into investigation.md. No forces, velocities or
accelerations are drawn. The hero shows the cheese still evenly spread (it must not answer Ennusta). The schematic
figures and the graph show models only, never invented measurements, and no frequency of the oven is given."""
import math
from figlib import (Fig, Axes, INK, MUTED, WHITE, RULE, GLASS, ALUMINIUM, METAL_EDGE, IRON, SAND, SAND_DARK, SAND_LIGHT,
                    GRAIN, HEAT_LIGHT, WATER_LIGHT, WATER, n)
import herolib as H
from herolib import grad, rnd

CHEESE, CHEESE_EDGE = "#ffe066", "#d9a400"


def shreds(f, cx, cy, rx, ry, count, seed=1, colour=CHEESE_EDGE, length=9):
    """Grated cheese: short strokes spread evenly over an ellipse."""
    for k in range(count):
        a = 2 * math.pi * rnd(k, seed); r = math.sqrt(rnd(k, seed + 7))
        x, y = cx + r * rx * math.cos(a), cy + r * ry * math.sin(a)
        t = math.pi * rnd(k, seed + 3)
        dx, dy = length / 2 * math.cos(t), length / 2 * math.sin(t) * ry / rx
        f.line(x - dx, y - dy, x + dx, y + dy, colour, 2, cap="round")


def hero():
    """The opening illustration: a microwave oven on a lab bench, door closed and the oven off. Through the window: a
    plate with an even layer of grated cheese (not yet heated) and a cup of water beside it. On the bench: a ruler, an
    oven mitt and a bowl of grated cheese."""
    f = H.hero("fy10m-hero", "Kuvitus: mikroaaltouuni laboratorion työpöydällä. Uunin luukku on kiinni ja uuni on pois "
               "päältä. Luukun ikkunasta näkyy uunin pohjalla lautanen, jolle on levitetty tasainen kerros juustoraastetta, "
               "ja sen vieressä kuppi vettä. Pöydällä uunin vieressä on mitta-asteikko, patalappu ja kulho juustoraastetta.")
    f.rect(0, 0, 1200, 600, grad(f, "fy10mh-wall", GLASS, "#dfe9ef"))
    f.rect(0, 470, 1200, 130, grad(f, "fy10mh-desk", SAND_DARK, SAND, horizontal=True))
    for k in range(5): f.line(0, 492 + 22 * k, 1200, 488 + 22 * k, GRAIN, 1.5)
    f.line(0, 470, 1200, 470, INK, 3)
    # the oven body, feet and control panel
    f.rect(300, 456, 30, 14, INK, rx=3); f.rect(830, 456, 30, 14, INK, rx=3)
    f.rect(280, 140, 600, 318, grad(f, "fy10mh-body", "#f1f3f5", ALUMINIUM), INK, 3, rx=14)
    f.rect(700, 160, 160, 278, "#e9ecef", INK, 2.5, rx=8)
    f.rect(720, 182, 120, 44, "#343a40", INK, 2.5, rx=5)          # the display is dark: the oven is off
    for k in range(3):
        for j in range(3): f.circle(745 + 35 * j, 260 + 34 * k, 11, WHITE, METAL_EDGE, 2.5)
    f.circle(780, 392, 22, WHITE, METAL_EDGE, 3); f.line(780, 392, 780, 374, INK, 3)
    # the closed door with its window
    f.rect(296, 156, 392, 286, "#dee2e6", INK, 2.5, rx=8)
    f.rect(648, 210, 18, 176, IRON, INK, 2.5, rx=6)               # the handle
    f.rect(320, 186, 310, 226, "#2b3036", INK, 2.5, rx=6)         # the dark window
    # the oven's interior seen through the window: back wall, floor, plate with cheese and a cup of water
    f.rect(330, 196, 290, 206, "#495057")
    f.path("M330,402 L360,330 L590,330 L620,402 Z", fill="#6c757d")
    f.add('<ellipse cx="460" cy="370" rx="104" ry="24" fill="#f8f9fa" stroke="#ced4da" stroke-width="2.5"/>')
    f.add(f'<ellipse cx="460" cy="368" rx="86" ry="17" fill="{CHEESE}"/>')
    shreds(f, 460, 368, 82, 15, 120, seed=3, length=8)
    f.rect(560, 318, 40, 46, WHITE, "#ced4da", 2.5, rx=4)         # the cup of water
    f.add(f'<ellipse cx="580" cy="320" rx="18" ry="5" fill="{WATER_LIGHT}" stroke="{WATER}" stroke-width="1.5"/>')
    f.path("M600,328 Q614,333 600,350", stroke="#ced4da", w=3)
    # the mesh of the window, drawn as a faint dot pattern over the view
    f.defs_add('<pattern id="fy10mh-mesh" width="8" height="8" patternUnits="userSpaceOnUse">'
               '<circle cx="4" cy="4" r="1.6" fill="#000" fill-opacity="0.35"/></pattern>')
    f.rect(320, 186, 310, 226, "url(#fy10mh-mesh)", rx=6)
    f.rect(320, 186, 310, 226, "none", INK, 2.5, rx=6)
    # on the bench: a ruler, an oven mitt and a bowl of grated cheese
    f.add('<g transform="translate(1030,505) rotate(-4)">'
          f'<rect x="-120" y="-14" width="240" height="28" rx="3" fill="#ffe8a3" stroke="{INK}" stroke-width="2.5"/>'
          + "".join(f'<line x1="{-110 + 10 * k}" y1="-14" x2="{-110 + 10 * k}" y2="{-14 + (12 if k % 5 == 0 else 6)}" stroke="{INK}" stroke-width="1.5"/>' for k in range(23))
          + "</g>")
    f.path("M935,470 L935,400 Q935,372 962,372 L1010,372 Q1036,372 1036,398 L1036,470 Z", fill="#ff8787", stroke=INK, w=2.5)
    f.path("M935,420 Q906,414 906,390 Q906,370 928,372", fill="#ff8787", stroke=INK, w=2.5)
    f.rect(930, 448, 112, 22, "#fa5252", INK, 2.5, rx=4)
    f.path("M110,428 L250,428 Q244,470 180,470 Q116,470 110,428 Z", fill=WHITE, stroke=INK, w=2.5)
    f.add(f'<ellipse cx="180" cy="426" rx="64" ry="12" fill="{CHEESE}" stroke="{CHEESE_EDGE}" stroke-width="2"/>')
    shreds(f, 180, 422, 56, 9, 40, seed=5, length=8)
    return f.svg()


def standing():
    """A one-dimensional standing wave between two metal walls: the extreme positions of the field's oscillation,
    nodes at the walls, antinodes halfway between, the cheese melting under the antinodes, and lambda/2 between two
    neighbouring antinodes."""
    f = Fig("fy10m-standing", 360, "Kaaviokuva yksinkertaisesta mallista. Kahden metalliseinän välissä on seisova aalto. "
            "Kiinteä viiva ja katkoviiva näyttävät sähkökentän värähtelyn ääriasennot. Solmukohdissa, myös seinien kohdalla, "
            "kenttä ei värähtele. Kupukohdissa, solmukohtien puolivälissä, värähtely on suurin. Alla olevassa juustokerroksessa "
            "on sulanut kohta jokaisen kupukohdan alla. Kahden vierekkäisen kupukohdan välinen etäisyys on puolet "
            "aallonpituudesta, lambda per kaksi.")
    xa, xb, yc, A = 70, 530, 150, 62
    half = (xb - xa) / 4
    for x in (xa - 22, xb):
        f.rect(x, 70, 22, 210, ALUMINIUM, INK, 2.5)
        for k in range(7): f.line(x, 84 + 28 * k, x + 22, 72 + 28 * k, METAL_EDGE, 1.5)
    pts = [(xa + (xb - xa) * i / 240, A * math.sin(math.pi * 4 * i / 240)) for i in range(241)]
    f.path("M" + " L".join(f"{n(x)},{n(yc - y)}" for x, y in pts), stroke=INK, w=3)
    f.path("M" + " L".join(f"{n(x)},{n(yc + y)}" for x, y in pts), stroke=MUTED, w=2.5, extra='stroke-dasharray="7 6"')
    f.line(xa, yc, xb, yc, RULE, 1.5)
    # the cheese layer: melted spots under the antinodes
    f.rect(xa, 252, xb - xa, 16, CHEESE, CHEESE_EDGE, 2)
    for k in range(4):
        x = xa + half * (k + 0.5)
        f.add(f'<ellipse cx="{n(x)}" cy="260" rx="26" ry="8" fill="{HEAT_LIGHT}" stroke="{CHEESE_EDGE}" stroke-width="1.5"/>')
        f.line(x, yc + A + 8, x, 248, MUTED, 1.5, "4 4")
    # labels
    xk, xs = xa + half * 1.5, xa + half * 3
    f.line(xk, yc - A - 4, xk, 44, MUTED, 1.5); f.tex(xk, 30, r"\text{kupukohta}", "middle")
    f.line(xs, yc - 6, xs, 44, MUTED, 1.5); f.tex(xs, 30, r"\text{solmukohta}", "middle")
    # lambda/2 between two neighbouring antinodes
    x1, x2 = xa + half * 2.5, xa + half * 3.5
    f.line(x1, 292, x2, 292, INK, 2); f.line(x1, 282, x1, 302, INK, 2); f.line(x2, 282, x2, 302, INK, 2)
    f.tex((x1 + x2) / 2, 326, r"\dfrac{\lambda}{2}", "middle")
    f.tex(xa, 312, r"\text{juustokerros}", "start", MUTED)
    return f.svg()


def spots():
    """Top view of the cheese plate: melted spots, four of them in a row; the distance L between the centres of the
    first and the last covers three gaps."""
    f = Fig("fy10m-spots", 380, "Kaaviokuva ylhäältä katsottuna. Lautasella on juustokerros, johon on sulanut kohtia. "
            "Neljä sulanutta kohtaa on samalla suoralla. Niiden keskikohdat on merkitty rastilla. Ensimmäisen ja viimeisen "
            "kohdan keskikohtien välinen etäisyys L kattaa kolme kohtien väliä.")
    cx, cy = 300, 160
    f.circle(cx, cy, 148, "#f8f9fa", "#ced4da", 3)
    f.circle(cx, cy, 130, CHEESE, CHEESE_EDGE, 2)
    shreds(f, cx, cy, 124, 124, 150, seed=9, length=9)
    row = [195, 265, 335, 405]
    others = [(230, 92), (300, 88), (370, 92), (230, 228), (300, 232), (370, 228)]
    for k, (x, y) in enumerate([(x, cy) for x in row] + others):
        f.add(f'<ellipse cx="{n(x)}" cy="{n(y)}" rx="{n(19 + 4 * rnd(k, 2))}" ry="{n(16 + 4 * rnd(k, 4))}" '
              f'fill="{HEAT_LIGHT}" stroke="{CHEESE_EDGE}" stroke-width="1.5"/>')
    for x in row:
        f.line(x - 7, cy - 7, x + 7, cy + 7, INK, 2.5); f.line(x - 7, cy + 7, x + 7, cy - 7, INK, 2.5)
    for x in (row[0], row[-1]): f.line(x, cy + 12, x, 318, MUTED, 1.5, "4 4")
    f.line(row[0], 330, row[-1], 330, INK, 2); f.line(row[0], 318, row[0], 342, INK, 2); f.line(row[-1], 318, row[-1], 342, INK, 2)
    f.tex(cx, 356, r"L", "middle")
    f.tex(row[-1] + 20, 330, r"\text{3 väliä}", "start", MUTED)
    return f.svg()


def model():
    """The model graph of the extension: the position of a spot centre along a row against its ordinal number is a
    line whose slope is the spacing d = lambda/2. No measured points."""
    f = Fig("fy10m-model", 360, "Kuvaaja: sulaneen kohdan keskikohdan paikka x k järjestysnumeron k funktiona mallin mukaan. "
            "Kuvaaja on suora, jonka kulmakerroin on vierekkäisten kohtien välinen etäisyys d, joka on mallin mukaan lambda "
            "per kaksi. Suora ei kulje origon kautta, koska ensimmäisen kohdan paikka riippuu siitä, mihin mitan nollakohta "
            "asetetaan. Kuvaajassa ei ole mittauspisteitä.")
    ax = Axes(f, (90, 300), (460, 50), x=(0, 5.5), y=(0, 10), xticks=[1, 2, 3, 4, 5], yticks=[], xlabel=r"k",
              ylabel=r"x_k", grid=False)
    y = lambda k: 1.2 + 1.6 * k
    ax.line([(0.5, y(0.5)), (5.2, y(5.2))], INK)
    f.line(ax.X(2), ax.Y(y(2)), ax.X(3), ax.Y(y(2)), MUTED, 2, "6 5")
    f.line(ax.X(3), ax.Y(y(2)), ax.X(3), ax.Y(y(3)), MUTED, 2, "6 5")
    f.tex(ax.X(3) + 10, ax.Y((y(2) + y(3)) / 2), r"d", "start", MUTED)
    f.tex(ax.X(2.5), ax.Y(y(2)) + 18, r"1", "middle", MUTED)
    f.tex(ax.X(0.4), ax.Y(9.0), r"\text{kulmakerroin } d = \dfrac{\lambda}{2}", "start")
    return f.svg()


FIGURES = {"hero": hero, "standing": standing, "spots": spots, "model": model}
