"""Figures of the unit fy12-koe (scripts/figlib.py, herolib.py); `python3 scripts/units.py figures fy12-koe` writes
them into content/fi/units/fy12-koe/unit.md. The unit is written in Finnish (decimal comma).

hero    the opening illustration: an exam desk with a laptop showing a fitted graph, a calculator, a squared
        notebook with a sketch, a pencil, a water bottle and a wall clock (no text, no people)
steps   the seven steps of a complete solution as a ladder of numbered cards (overview figure of the theory)
graph   what a graph in an answer contains: axis titles with units, the measured points, a fitted line through them
        and the slope read from two points of the line far apart (to scale; the data are invented)
"""
import math
import figlib
from figlib import (Fig, Axes, fi, INK, MUTED, WHITE, RULE, RULE_LIGHT, GLASS, ALUMINIUM, METAL_EDGE, IRON, COLD,
                    COLD_LIGHT, HOT, HEAT, HEAT_LIGHT, SAND, SAND_LIGHT, GRAIN, GOOD, GOOD_LIGHT, WATER, WATER_LIGHT, PAPER, n)
import herolib as H

figlib.set_language({}, ",")

# graph: a trolley's position read every second (invented example data, small scatter around x = 0,62 t + 0,40)
T_DATA = [0, 1, 2, 3, 4, 5, 6]
X_DATA = [0.42, 0.98, 1.68, 2.25, 2.88, 3.47, 4.14]


def fit(x, y):
    mx, my = sum(x) / len(x), sum(y) / len(y)
    k = sum((a - mx) * (b - my) for a, b in zip(x, y)) / sum((a - mx) ** 2 for a in x)
    return k, my - k * mx


def hero():
    """Opening illustration of the Why question: the desk of a digital exam, everything a complete answer is made with."""
    f = H.hero("fy12koe-hero", "Kuvitus: koepöytä ylhäältä vinosti nähtynä. Pöydällä on kannettava tietokone, jonka näytöllä on "
               "kuvaaja: mittauspisteet ja niihin sovitettu nouseva suora. Tietokoneen vieressä ovat laskin, ruutuvihko, jossa on "
               "lyijykynällä piirretty kappale ja nuolia, lyijykynä ja vesipullo. Seinällä on kello. Kuvassa ei ole tekstiä.")
    f.rect(0, 0, 1200, 600, PAPER)
    # the wall and the desk top
    f.rect(0, 0, 1200, 330, H.grad(f, "fy12koe-h-wall", "#eef5f9", "#e3dccb"))
    f.rect(0, 330, 1200, 270, H.grad(f, "fy12koe-h-desk", SAND, "#c79a52"))
    f.line(0, 330, 1200, 330, "#a97a35", 4)
    # the wall clock
    f.circle(1040, 120, 62, ALUMINIUM, INK, 3)
    f.circle(1040, 120, 52, WHITE, INK, 2)
    for k in range(12):
        a = k * math.pi / 6
        f.line(1040 + math.sin(a) * 42, 120 - math.cos(a) * 42, 1040 + math.sin(a) * 48, 120 - math.cos(a) * 48, MUTED, 2.5)
    f.line(1040, 120, 1040 + math.sin(math.radians(300)) * 26, 120 - math.cos(math.radians(300)) * 26, INK, 5, cap="round")
    f.line(1040, 120, 1040 + math.sin(math.radians(60)) * 40, 120 - math.cos(math.radians(60)) * 40, INK, 3, cap="round")
    f.circle(1040, 120, 5, HOT)
    # the laptop: screen with a graph, keyboard base
    f.path("M380,92 L820,92 Q832,92 832,104 L832,372 L368,372 L368,104 Q368,92 380,92 Z", IRON, INK, 3)
    f.rect(388, 112, 424, 244, WHITE, None, 0, 4)
    ox, oy, w, h = 430, 330, 350, 190                       # the graph on the screen
    for i in range(1, 6):
        f.line(ox + i * w / 6, oy, ox + i * w / 6, oy - h, RULE_LIGHT, 1.5)
    for i in range(1, 5):
        f.line(ox, oy - i * h / 5, ox + w, oy - i * h / 5, RULE_LIGHT, 1.5)
    f.arrow(ox - 1, oy, ox + w + 16, oy, INK, 2.5, 11)
    f.arrow(ox, oy + 1, ox, oy - h - 16, INK, 2.5, 11)
    k, b = fit(T_DATA, X_DATA)
    X = lambda t: ox + t / 6.5 * w
    Y = lambda x: oy - x / 4.6 * h
    f.line(X(0), Y(b), X(6.4), Y(b + 6.4 * k), COLD, 3.5, cap="round")
    for t, x in zip(T_DATA, X_DATA):
        f.circle(X(t), Y(x), 7, INK, WHITE, 2)
    f.path("M330,372 L870,372 L920,420 L280,420 Z", ALUMINIUM, INK, 3)
    for r in range(3):
        y = 381 + r * 12
        f.line(330 + r * 12, y, 870 - r * 12, y, METAL_EDGE, 3, "18 6")
    f.rect(560, 404, 80, 10, METAL_EDGE, None, 0, 3)
    # the squared notebook with a pencil sketch of a body and arrows
    f.path("M70,430 L300,402 L330,560 L96,590 Z", WHITE, INK, 2.5)
    for i in range(1, 9):
        t = i / 9
        f.line(70 + (96 - 70) * t, 430 + (590 - 430) * t, 300 + (330 - 300) * t, 402 + (560 - 402) * t, COLD_LIGHT, 1.5)
    for i in range(1, 8):
        t = i / 8
        f.line(70 + (300 - 70) * t, 430 + (402 - 430) * t, 96 + (330 - 96) * t, 590 + (560 - 590) * t, COLD_LIGHT, 1.5)
    f.path("M165,478 L225,470 L232,512 L172,520 Z", "none", INK, 2.5)
    f.arrow(199, 495, 205, 548, HOT, 3.5, 13)
    f.arrow(199, 495, 192, 446, HOT, 3.5, 13)
    f.arrow(199, 495, 268, 486, HOT, 3.5, 13)
    # the pencil
    f.path("M318,452 L352,410 L362,418 L328,460 Z", HEAT_LIGHT, INK, 2)
    f.path("M318,452 L328,460 L312,470 Z", SAND_LIGHT, INK, 2)
    f.path("M352,410 L362,418 L368,410 L358,402 Z", HOT, INK, 2)
    # the calculator
    f.path("M930,440 L1060,424 L1082,566 L952,582 Z", INK, INK, 2.5)
    f.path("M948,452 L1046,440 L1052,478 L954,490 Z", GOOD_LIGHT, None, 0)
    for r in range(3):
        for c in range(4):
            x0 = 958 + c * 24 + r * 3.2; y0 = 502 + r * 22 - c * 3
            f.rect(x0, y0, 17, 14, ALUMINIUM if c < 3 else HEAT, None, 0, 3)
    # the water bottle
    f.rect(1118, 330, 46, 200, H.grad(f, "fy12koe-h-bottle", WATER_LIGHT, WATER), INK, 2.5, 12)
    f.rect(1126, 300, 30, 32, COLD, INK, 2.5, 5)
    f.line(1126, 380, 1156, 380, WHITE, 3, cap="round")
    return f.svg()


STEPS = [
    (r"\text{Annettu ja kysytty}", r"\text{suureet yksiköineen}"),
    (r"\text{Periaate}", r"\text{laki ja miksi se pätee}"),
    (r"\text{Kaava ratkaistuna}", r"\text{kysytty symboleilla}"),
    (r"\text{Muunnokset}", r"\text{perusyksiköihin}"),
    (r"\text{Sijoitus}", r"\text{luvut yksiköineen}"),
    (r"\text{Vastaus}", r"\text{yksikkö ja tarkkuus}"),
    (r"\text{Järkevyys}", r"\text{arvio tai vertailu}"),
]


def steps():
    """The seven steps of a complete solution: numbered cards from top to bottom, the step name in ink and what it
    holds in muted grey; all cards the same neutral tint."""
    f = Fig("fy12koe-steps", 452, "Kaavio: täydellisen ratkaisun seitsemän vaihetta allekkain numeroituina kortteina. "
            "1 Annettu ja kysytty: suureet yksiköineen. 2 Periaate: laki ja miksi se pätee. 3 Kaava ratkaistuna: kysytty "
            "symboleilla. 4 Muunnokset: perusyksiköihin. 5 Sijoitus: luvut yksiköineen. 6 Vastaus: yksikkö ja tarkkuus. "
            "7 Järkevyys: arvio tai vertailu. Korttien välissä on nuolet ylhäältä alas.")
    top, step = 14, 62
    for i, (name, hint) in enumerate(STEPS):
        y = top + i * step
        fill = GLASS
        f.rect(16, y, 568, 50, fill, INK, 2, 8)
        f.circle(46, y + 25, 17, INK)
        f.tex(46, y + 25, fi(i + 1), "middle", WHITE, size=22)
        f.tex(76, y + 25, name, "start")
        f.tex(572, y + 25, hint, "end", MUTED, size=21)
        if i < len(STEPS) - 1:
            f.line(46, y + 50, 46, y + step, MUTED, 2)
    return f.svg()


def graph():
    """A model graph of an answer: axis titles with units, the measured points, a fitted line through them (not a broken
    line through the points) and the slope read from two points of the line far apart, shown by a dashed triangle."""
    k, b = fit(T_DATA, X_DATA)
    t1, t2 = 1.0, 5.0
    x1, x2 = b + k * t1, b + k * t2
    f = Fig("fy12koe-graph", 400, "Kuvaaja mittakaavassa: kärryn paikka x metreinä ajan t funktiona sekunteina, keksityt "
            "esimerkkiarvot. Seitsemän mittauspistettä ajanhetkillä 0–6 s nousee lähes suoraan. Pisteisiin on sovitettu "
            "suora, joka kulkee pisteiden lomitse. Kulmakerroin luetaan suoralta kahdesta kaukana toisistaan olevasta "
            "pisteestä, (1,0 s; 1,02 m) ja (5,0 s; 3,50 m), katkoviivakolmion avulla: Δt = 4,0 s ja Δx = 2,48 m, joten "
            "kulmakerroin on noin 0,62 m/s.")
    ax = Axes(f, (80, 350), (470, 60), x=(0, 7), y=(0, 5), xticks=list(range(8)), yticks=[0, 1, 2, 3, 4, 5],
              xlabel=r"t\ (\text{s})", ylabel=r"x\ (\text{m})")
    ax.line([(0, b), (6.6, b + 6.6 * k)], COLD, 3)
    f.line(ax.X(t1), ax.Y(x1), ax.X(t2), ax.Y(x1), MUTED, 2, "7 5")
    f.line(ax.X(t2), ax.Y(x1), ax.X(t2), ax.Y(x2), MUTED, 2, "7 5")
    for t, x in zip(T_DATA, X_DATA): ax.point(t, x)
    for t, x in ((t1, x1), (t2, x2)): f.circle(ax.X(t), ax.Y(x), 10, "none", INK, 1.5)
    f.tex((ax.X(t1) + ax.X(t2)) / 2, ax.Y(x1) + 22, r"\Delta t = 4{,}0\,\text{s}", "middle", MUTED, bg=True)
    f.tex(ax.X(t2) + 12, (ax.Y(x1) + ax.Y(x2)) / 2 + 22, r"\Delta x = " + fi(round(x2 - x1, 2)) + r"\,\text{m}", "start", MUTED, bg=True)
    f.tex(ax.X(1.2), ax.Y(4.5), r"k = \tfrac{\Delta x}{\Delta t} \approx " + fi(round(k, 2)) + r"\,\tfrac{\text{m}}{\text{s}}", "start", COLD, bg=True)
    return f.svg()


FIGURES = {"hero": hero, "steps": steps, "graph": graph}
REUSE = {"hero": "decorative", "steps": "safe", "graph": "safe"}

if __name__ == "__main__":
    k, b = fit(T_DATA, X_DATA); print({"k": k, "b": b, "x1": b + k, "x5": b + 5 * k})
