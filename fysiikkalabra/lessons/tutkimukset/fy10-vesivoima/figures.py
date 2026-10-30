"""Figures of the investigation Vesivoimalaitoksen pienoismallin hyötysuhde (scripts/figlib.py); `python
scripts/investigations.py figures fy10-vesivoima` writes them into investigation.md. The meters in the hero show no
readings and the graph shows reference lines only, never invented measurements or an expected result."""
import math
from figlib import Fig, Axes, INK, MUTED, WHITE, RULE, GLASS, WATER_LIGHT, WATER, ALUMINIUM, METAL_EDGE, IRON, SAND, SAND_DARK, \
    SAND_LIGHT, GRAIN, COPPER, HOT, GOOD_LIGHT, n
import herolib as H
from herolib import grad


def wheel(f, cx, cy, r, blades=8, turn=0.0, fill=ALUMINIUM):
    """A turbine wheel seen from the side: a disc with cup-like blades on its rim and a hub."""
    f.circle(cx, cy, r, fill, INK, 2.5)
    for k in range(blades):
        a = turn + k * 2 * math.pi / blades
        c, s = math.cos(a), math.sin(a)
        x0, y0 = cx + c * r * 0.35, cy + s * r * 0.35
        x1, y1 = cx + c * r * 1.12, cy + s * r * 1.12
        f.line(x0, y0, x1, y1, INK, 2.5)
        f.circle(x1, y1, r * 0.13, METAL_EDGE, INK, 2)
    f.circle(cx, cy, r * 0.22, IRON, INK, 2)


def meter(f, x, y, w=96, h=130):
    """A multimeter with an empty display (no reading), a dial and two sockets."""
    f.rect(x, y, w, h, "#ffd43b", INK, 2.5, rx=10)
    f.rect(x + 10, y + 12, w - 20, 34, "#e9f3e1", INK, 2, rx=3)
    f.circle(x + w / 2, y + 78, 18, IRON, INK, 2)
    f.line(x + w / 2, y + 78, x + w / 2 + 10, y + 66, WHITE, 3)
    f.circle(x + w / 2 - 20, y + h - 14, 6, INK)
    f.circle(x + w / 2 + 20, y + h - 14, 6, HOT)


def hero():
    """The opening illustration: a water tank high on a stand feeds a hose to a small turbine and generator; the water
    runs on into a bucket on a scale; wires lead to a load and two meters with blank displays; a stopwatch waits."""
    f = H.hero("fy10v-hero", "Kuvitus: laboratorion työpöydän vieressä on korkea teline, jonka päällä on vesisäiliö. Säiliön "
               "pohjasta lähtee letku alas pienen vesiturbiinin luo. Turbiinin akselilla on generaattori, josta johdot kulkevat "
               "kuormavastukselle ja kahdelle yleismittarille, joiden näytöt ovat tyhjät. Turbiinin läpi kulkenut vesi valuu "
               "ämpäriin, joka on vaa'an päällä. Pöydällä on sekuntikello ja kuivausliina.")
    f.rect(0, 0, 1200, 600, grad(f, "fy10vh-wall", GLASS, "#dfe9ef"))
    f.rect(0, 470, 1200, 130, grad(f, "fy10vh-desk", SAND_DARK, SAND, horizontal=True))
    for k in range(5): f.line(0, 492 + 22 * k, 1200, 488 + 22 * k, GRAIN, 1.5)
    f.line(0, 470, 1200, 470, INK, 3)
    # the tall stand and the upper tank
    f.rect(130, 150, 16, 320, ALUMINIUM, INK, 2.5); f.rect(274, 150, 16, 320, ALUMINIUM, INK, 2.5)
    f.rect(120, 140, 180, 16, IRON, INK, 2.5, rx=3)
    f.line(146, 300, 274, 300, METAL_EDGE, 4)
    f.rect(140, 40, 140, 100, GLASS, INK, 3, rx=6)
    f.rect(143, 62, 134, 75, WATER_LIGHT, None, rx=4)
    f.line(143, 62, 277, 62, WATER, 3)
    # the hose from the bottom of the tank down to the turbine nozzle
    f.path("M262,140 C262,230 330,260 420,268 C470,272 500,268 510,262", stroke=INK, w=16, extra='stroke-linecap="round"')
    f.path("M262,140 C262,230 330,260 420,268 C470,272 500,268 510,262", stroke=WATER_LIGHT, w=10, extra='stroke-linecap="round"')
    # the turbine in a clear housing, cantilevered on the shaft of the generator, which stands on a pillar
    f.rect(668, 352, 48, 118, IRON, INK, 2.5, rx=4)
    f.circle(560, 290, 62, GLASS, INK, 3)
    wheel(f, 560, 290, 42, turn=0.3)
    f.rect(620, 282, 40, 16, METAL_EDGE, INK, 2)                  # shaft
    f.rect(652, 256, 80, 96, "#4a6fa5", INK, 2.5, rx=10)            # generator
    f.rect(662, 270, 60, 10, "#6f8fbf", None, rx=3)
    # water leaving the turbine falls into the bucket on the scale
    f.path("M556,352 C556,370 558,388 560,404", stroke=WATER, w=8, extra='stroke-linecap="round" stroke-opacity="0.75"')
    f.path("M500,392 L512,450 L608,450 L620,392 Z", "#e9ecef", INK, 2.5)
    f.path("M505,416 L512,450 L608,450 L615,416 Z", WATER_LIGHT)
    f.line(505, 416, 615, 416, WATER, 2.5)
    f.rect(480, 450, 160, 20, IRON, INK, 2.5, rx=4)
    f.rect(536, 454, 48, 12, "#e9f3e1", INK, 1.5, rx=2)
    # wires from the generator to the load and the meters
    f.path("M730,280 C770,250 800,260 840,335", stroke=HOT, w=4)
    f.path("M730,330 C770,370 800,400 840,375", stroke=INK, w=4)
    f.rect(820, 330, 110, 50, "#f1f3f5", INK, 2.5, rx=4)            # load board
    f.rect(846, 346, 58, 18, SAND_LIGHT, INK, 2, rx=8)              # resistor
    for k, c in enumerate([COPPER, INK, HOT]): f.rect(856 + 14 * k, 346, 6, 18, c)
    meter(f, 960, 300); meter(f, 1080, 300)
    f.path("M930,345 C945,345 950,420 985,418", stroke=HOT, w=3)
    f.path("M930,365 C960,365 1000,440 1028,418", stroke=INK, w=3)
    f.path("M904,330 C940,250 1080,250 1105,418", stroke=HOT, w=3)
    f.path("M876,380 C900,460 1130,460 1148,418", stroke=INK, w=3)
    # a stopwatch and a towel on the desk
    H.stopwatch(f, 800, 520, 36, 0.0)
    f.add('<g transform="translate(980,530) rotate(-4)">'
          f'<rect x="-90" y="-24" width="180" height="48" rx="8" fill="{GOOD_LIGHT}" stroke="{INK}" stroke-width="2.5"/>'
          + "".join(f'<line x1="{-70 + 35 * k}" y1="-24" x2="{-70 + 35 * k}" y2="24" stroke="{WHITE}" stroke-width="4"/>' for k in range(5))
          + "</g>")
    return f.svg()


def setup():
    """Schematic: the upper tank, the fall height h from its water surface to the turbine, the collector on a scale,
    and the generator circuit with the load R, the ammeter in series and the voltmeter in parallel."""
    f = Fig("fy10v-setup", 470, "Kaaviokuva. Vasemmalla ylhäällä on vesiastia. Sen pohjasta letku vie veden alas turbiinille. "
            "Putouskorkeus h on merkitty astian vedenpinnasta turbiinin akselin tasolle. Turbiinin läpi kulkenut vesi valuu "
            "keräysastiaan, joka on vaa'an päällä. Turbiinin akselilla on generaattori G. Generaattorin virtapiirissä on "
            "kuormavastus R, sen kanssa sarjassa virtamittari A ja sen rinnalla jännitemittari V.")
    # upper tank and water surface
    f.rect(80, 40, 130, 90, GLASS, INK, 2.5, rx=4)
    f.rect(82, 70, 126, 58, WATER_LIGHT, None, rx=3)
    f.line(82, 70, 208, 70, WATER, 2.5)
    # hose to the turbine
    f.path("M190,130 L190,236 Q190,262 216,264", stroke=INK, w=12)
    f.path("M190,130 L190,236 Q190,262 216,264", stroke=WATER_LIGHT, w=6)
    wheel(f, 255, 300, 36, turn=0.2)
    f.tex(198, 352, r"\text{turbiini}", "end", MUTED)
    # water to the collector on the scale
    f.path("M255,346 L255,382", stroke=WATER, w=5)
    f.path("M205,372 L215,430 L295,430 L305,372", stroke=INK, w=2.5)
    f.path("M210,400 L215,430 L295,430 L300,400 Z", WATER_LIGHT)
    f.rect(195, 430, 120, 16, IRON, INK, 2, rx=3)
    f.tex(322, 438, r"\text{vaaka}", "start", MUTED)
    # fall height h
    f.line(30, 70, 78, 70, MUTED, 1.5, "6 5")
    f.line(30, 300, 214, 300, MUTED, 1.5, "6 5")
    f.arrow(48, 185, 48, 74, INK, 2, 12); f.arrow(48, 185, 48, 296, INK, 2, 12)
    f.tex(58, 185, r"h", "start")
    # shaft and generator
    f.rect(291, 295, 54, 10, METAL_EDGE, INK, 1.5)
    gx, gy = 372, 300
    # circuit: generator on the left side of the loop, ammeter on top, load R on the right, voltmeter beside R
    f.line(gx, 160, gx, gy - 26, INK, 2.5); f.line(gx, gy + 26, gx, 400, INK, 2.5)
    f.line(gx, 160, 500, 160, INK, 2.5); f.line(gx, 400, 500, 400, INK, 2.5)
    f.line(500, 160, 500, 240, INK, 2.5); f.line(500, 320, 500, 400, INK, 2.5)
    f.rect(488, 240, 24, 80, WHITE, INK, 2.5)
    f.tex(482, 280, r"R", "end")
    f.line(500, 210, 566, 210, INK, 2.5); f.line(500, 350, 566, 350, INK, 2.5)
    f.line(566, 210, 566, 258, INK, 2.5); f.line(566, 302, 566, 350, INK, 2.5)
    for (x, y) in [(500, 210), (500, 350)]: f.circle(x, y, 4.5, INK)
    f.circle(gx, gy, 26, WHITE, INK, 2.5); f.tex(gx, gy, r"G", "middle")
    f.circle(436, 160, 20, WHITE, INK, 2.5); f.tex(436, 160, r"A", "middle")
    f.circle(566, 280, 20, WHITE, INK, 2.5); f.tex(566, 280, r"V", "middle")
    return f.svg()


def eta_graph():
    """Reading a P_s–P_o graph: the line eta = 1 bounds what is possible, and every line from the origin is one
    constant efficiency (reference lines only, no measured points)."""
    f = Fig("fy10v-eta", 380, "Kuvaaja: vaaka-akselilla veden teho P o ja pystyakselilla sähköteho P s, samassa mittakaavassa. "
            "Katkoviiva origosta on suora, jolla hyötysuhde on yksi eli sata prosenttia; sen yläpuolelle ei voi päätyä, "
            "koska energia säilyy. Toinen origon kautta kulkeva suora näyttää, että kaikilla saman origon kautta kulkevan "
            "suoran pisteillä on sama hyötysuhde. Kuvaajassa ei ole mittauspisteitä.")
    ax = Axes(f, (150, 330), (410, 70), x=(0, 10), y=(0, 10), xticks=[], yticks=[], xlabel=r"P_\text{o}",
              ylabel=r"P_\text{s}", grid=False)
    ax.area([(0, 0), (10, 10), (0, 10)], RULE, 0.35)
    ax.line([(0, 0), (10, 10)], MUTED, 2.5, "8 6")
    f.tex(ax.X(0.6), ax.Y(8.6), r"\text{mahdoton alue}", "start", MUTED)
    f.tex(ax.X(7.0), ax.Y(5.9), r"\eta = 1", "start", MUTED)
    ax.line([(0, 0), (10, 5)], INK, 3)
    f.tex(ax.X(10) + 8, ax.Y(5), r"\text{sama } \eta", "start")
    return f.svg()


FIGURES = {"hero": hero, "setup": setup, "eta": eta_graph}
