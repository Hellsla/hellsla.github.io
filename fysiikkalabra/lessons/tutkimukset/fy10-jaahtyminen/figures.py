"""Figures of the investigation Kuuman veden jäähtyminen (scripts/figlib.py); `python scripts/investigations.py figures
fy10-jaahtyminen` writes them into investigation.md. No arrows of force, velocity or acceleration are drawn. The graphs
show the model (Newton's law of cooling) only, never invented measurements."""
import math
from figlib import (Fig, Axes, INK, MUTED, WHITE, RULE, GLASS, WATER_LIGHT, ALUMINIUM, METAL_EDGE, IRON, SAND, SAND_DARK,
                    SAND_LIGHT, GRAIN, HOT, COLD, GOOD, n)
import herolib as H
from herolib import grad


def steam(f, xs, ybot, length=70, w=4):
    """Faint wisps of vapour rising from the water surface."""
    for k, x in enumerate(xs):
        f.path(f"M{n(x)},{n(ybot)} q-10,{n(-length / 6)} 0,{n(-length / 3)} t0,{n(-length / 3)} t0,{n(-length / 3)}", stroke=MUTED, w=w,
               extra='stroke-linecap="round" stroke-opacity="0.45"')


def beaker(f, x, ytop, w, h, level, sw=3):
    """A glass beaker: x is its left edge; the water fills it up to `level` below the rim."""
    f.rect(x + 3, ytop + level, w - 6, h - level - 3, WATER_LIGHT, None)
    f.path(f"M{n(x)},{n(ytop)} V{n(ytop + h - 8)} Q{n(x)},{n(ytop + h)} {n(x + 8)},{n(ytop + h)} H{n(x + w - 8)} "
           f"Q{n(x + w)},{n(ytop + h)} {n(x + w)},{n(ytop + h - 8)} V{n(ytop)}", stroke=INK, w=sw)
    f.line(x - 6, ytop, x, ytop, INK, sw)
    for k in range(1, 4): f.line(x + w - 4, ytop + level + (h - level) * k / 4, x + w - 18, ytop + level + (h - level) * k / 4, METAL_EDGE, 1.5)


def hero():
    """The opening illustration: a beaker of steaming water on a cork mat on a lab bench, a temperature probe in it wired to
    a data logger with a blank display, a thermometer standing apart in the room air, a kettle and a window behind."""
    f = H.hero("fy10jt-hero", "Kuvitus: laboratorion työpöydällä on korkkialustan päällä lasiastia, jossa on kuumaa vettä. Vedestä "
               "nousee höyryä. Veteen on upotettu lämpötila-anturi, jonka johto kulkee pöydällä olevaan mittauslaitteeseen. "
               "Sivummalla pöydällä seisoo toinen lämpömittari huoneilmassa. Taustalla on ikkuna, ja pöydän reunalla on "
               "vedenkeitin.")
    f.rect(0, 0, 1200, 600, grad(f, "fy10jth-wall", GLASS, "#dfe9ef"))
    H.window(f, 80, 50, 260, 190, "fy10jth-win")
    f.rect(0, 440, 1200, 160, grad(f, "fy10jth-desk", SAND_DARK, SAND, horizontal=True))
    for k in range(6): f.line(0, 462 + 22 * k, 1200, 458 + 22 * k, GRAIN, 1.5)
    f.line(0, 440, 1200, 440, INK, 3)
    # the kettle on the left
    f.path("M150,440 L165,330 Q170,310 195,310 H265 Q290,310 295,330 L310,440 Z", ALUMINIUM, INK, 3)
    f.path("M295,345 Q345,350 330,410 Q325,425 305,425", stroke=INK, w=10)
    f.path("M165,345 L120,320 L128,312 L172,330", ALUMINIUM, INK, 3)
    f.rect(205, 298, 50, 14, IRON, INK, 2.5, rx=4)
    # cork mat and beaker
    f.rect(470, 428, 240, 14, "#d9a66a", INK, 2.5, rx=4)
    beaker(f, 500, 230, 180, 198, 46, sw=4)
    steam(f, [545, 590, 640], 262, 110)
    # the probe in the middle of the water, held by a small clamp of a stand
    f.rect(780, 120, 12, 320, ALUMINIUM, INK, 2.5)
    f.rect(740, 428, 100, 14, IRON, INK, 2.5, rx=4)
    f.rect(600, 150, 190, 12, ALUMINIUM, INK, 2.5, rx=3)
    f.rect(588, 140, 28, 30, IRON, INK, 2.5, rx=4)
    f.rect(596, 170, 12, 200, METAL_EDGE, INK, 2.5, rx=5)
    f.path("M602,140 Q600,90 680,80 Q800,70 900,120 Q960,150 990,300", stroke=INK, w=4)
    # the data logger: its display shows no reading and no graph
    f.rect(930, 300, 170, 140, IRON, INK, 3, rx=12)
    f.rect(950, 318, 130, 64, "#dfe9ef", INK, 2.5, rx=4)
    for k in range(3): f.circle(970 + 45 * k, 410, 9, ALUMINIUM, INK, 2)
    # the room thermometer, standing apart in the air
    H.thermometer(f, 1140, 420, 70, HOT, 200)
    f.rect(1118, 428, 44, 12, IRON, INK, 2, rx=3)
    return f.svg()


def setup():
    """What is measured: the water temperature T by a probe in the middle of the water, the room temperature T_huone by a
    second thermometer in the air away from the vessel, and the time."""
    f = Fig("fy10jt-setup", 380, "Kaaviokuva. Lasiastiassa on kuumaa vettä eristävän alustan päällä. Lämpötila-anturin kärki "
            "on veden keskellä, irti astian pohjasta ja seinistä, ja se mittaa veden lämpötilan T. Anturin johto kulkee "
            "mittauslaitteeseen. Sivussa, irti astiasta, on toinen lämpömittari, joka mittaa huoneen lämpötilan T huone.")
    table = 330
    f.line(20, table, 580, table, INK, 3)
    f.rect(110, table - 12, 200, 12, "#d9a66a", INK, 2, rx=3)
    beaker(f, 130, 140, 160, 178, 40)
    steam(f, [175, 215, 255], 172, 60, 3)
    # the probe: tip in the middle of the water
    f.rect(204, 90, 12, 170, METAL_EDGE, INK, 2, rx=5)
    f.path("M210,90 Q210,50 270,50 H370", stroke=INK, w=3)
    f.rect(370, 30, 90, 46, IRON, INK, 2.5, rx=8); f.rect(382, 40, 66, 26, "#dfe9ef", INK, 2, rx=3)
    f.circle(210, 255, 5, INK)
    f.line(216, 255, 300, 255, MUTED, 1.5, "4 4")
    f.tex(306, 255, r"T", "start")
    f.tex(415, 98, r"\text{mittauslaite}", "middle", MUTED)
    # the room thermometer
    H.thermometer(f, 500, table - 30, 50, HOT, 150)
    f.tex(470, table - 100, r"T_\text{huone}", "end")
    f.tex(210, table + 26, r"\text{eristävä alusta}", "middle", MUTED)
    return f.svg()


T_ROOM, T0, K = 2.0, 9.0, 0.23        # model units only: the figure has no numbers on its axes


def model():
    """The model T(t): the temperature falls fastest at first and approaches the room temperature (dashed line); the
    difference halves in every equal interval t½ (three vertical bars)."""
    f = Fig("fy10jt-model", 400, "Kuvaaja: veden lämpötila T ajan t funktiona Newtonin jäähtymislain mukaan. Lämpötila "
            "lähtee alkulämpötilasta T nolla ja laskee aluksi jyrkästi, sitten yhä loivemmin, ja lähestyy katkoviivalla "
            "merkittyä huoneen lämpötilaa T huone mutta ei laske sen alle. Kolme pystysuoraa janaa näyttää veden ja huoneen "
            "lämpötilaeron kolmena hetkenä, jotka ovat yhtä pitkän ajan t puoli päässä toisistaan: jana on joka kerta "
            "puolet edellisestä. Kuvaajassa ei ole mittauspisteitä.")
    ax = Axes(f, (90, 340), (480, 60), x=(0, 10), y=(0, 10), xticks=[], yticks=[], xlabel=r"t", ylabel=r"T", grid=False)
    T = lambda t: T_ROOM + (T0 - T_ROOM) * math.exp(-K * t)
    ax.line([(0, T_ROOM), (10, T_ROOM)], MUTED, 2, "6 5")
    ax.curve(T, 0, 10)
    f.tex(ax.X(10), ax.Y(T_ROOM) + 22, r"T_\text{huone}", "end", MUTED)
    f.line(ax.x0 - 7, ax.Y(T0), ax.x0, ax.Y(T0), INK, 2); f.tex(ax.x0 - 12, ax.Y(T0), r"T_0", "end")
    half = math.log(2) / K; t1 = 0.8
    xs = [t1 + k * half for k in range(3)]
    for k, t in enumerate(xs):
        f.line(ax.X(t), ax.Y(T_ROOM), ax.X(t), ax.Y(T(t)), GOOD, 3)
    for a, b in zip(xs, xs[1:]):
        y = ax.Y(T_ROOM) - 18
        f.line(ax.X(a) + 4, y, ax.X(b) - 4, y, MUTED, 1.5)
        f.tex((ax.X(a) + ax.X(b)) / 2, y - 18, r"t_{1/2}", "middle", MUTED)
    f.tex(ax.X(xs[0]) + 8, ax.Y(T(xs[0])) - 24, r"\text{lämpötilaero}", "start", GOOD)
    f.tex(ax.X(xs[1]) + 8, ax.Y(T(xs[1])) - 24, r"\text{puolet}", "start", GOOD)
    f.tex(ax.X(xs[2]) + 8, ax.Y(T(xs[2])) - 24, r"\text{neljännes}", "start", GOOD)
    return f.svg()


def linear():
    """The linearised model: ln(T - T_huone) against t is a falling straight line with slope -k."""
    f = Fig("fy10jt-linear", 360, "Kuvaaja: lämpötilaeron T miinus T huone luonnollinen logaritmi ajan t funktiona "
            "Newtonin jäähtymislain mukaan. Kuvaaja on laskeva suora, joka alkaa pystyakselilta kohdasta luonnollinen "
            "logaritmi T nolla miinus T huone ja jonka kulmakerroin on miinus k. Kuvaajassa ei ole mittauspisteitä.")
    ax = Axes(f, (90, 300), (470, 60), x=(0, 10), y=(0, 10), xticks=[], yticks=[], xlabel=r"t",
              ylabel=r"\ln(T - T_\text{huone})", grid=False)
    ax.line([(0, 8.6), (9.5, 2.0)], INK)
    ax.point(0, 8.6, MUTED, 5)
    f.tex(ax.X(0.5), ax.Y(8.6) - 34, r"\ln(T_0 - T_\text{huone})", "start", MUTED)
    f.tex(ax.X(5.4), ax.Y(6.3), r"\text{kulmakerroin } {-k}", "start")
    return f.svg()


FIGURES = {"hero": hero, "setup": setup, "model": model, "linear": linear}
