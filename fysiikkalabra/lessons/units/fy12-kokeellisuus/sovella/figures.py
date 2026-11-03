"""Model graphs of the fy12-kokeellisuus task set (scripts/figlib.py); `python3 scripts/practice.py figures
units/fy12-kokeellisuus` writes them into content/fi/units/fy12-kokeellisuus/sovella/solutions.md.

The data are the task data (answers.py): s4 simulated from T = 2 pi sqrt((l + r)/g) with r = 2,5 cm and g = 9,81 m/s^2
plus small noise in t10; s6 simulated from s = v^2/(2a) with a = 4,2 m/s^2 plus noise in s."""
from figlib import Fig, Axes, fi, INK, MUTED, WHITE, HOT, COLD

L4 = [0.250, 0.400, 0.550, 0.700, 0.850, 1.000]
T10 = [10.55, 13.04, 15.23, 17.06, 18.81, 20.28]
VK = [10, 15, 20, 25, 30]
S6 = [1.0, 2.0, 3.8, 5.6, 8.5]


def _fit(x, y):
    mx, my = sum(x) / len(x), sum(y) / len(y)
    k = sum((a - mx) * (b - my) for a, b in zip(x, y)) / sum((a - mx) ** 2 for a in x)
    return k, my - k * mx


def pendulum():
    """s4: T^2 against l, the six points, the fitted line extended (dashed) to the vertical axis, the two points the
    slope is read from and the intercept b."""
    T2 = [(t / 10) ** 2 for t in T10]
    k, b = _fit(L4, T2)
    f = Fig("fy12ko-s4-graph", 440, "Kuvaaja: heilurin jaksonajan neliö T² langan pituuden l funktiona. Kuusi mittauspistettä "
            "pituuksilla 0,25–1,00 m on lähes suoralla. Pisteisiin sovitettu suora on jatkettu katkoviivana pystyakselille, ja se "
            "leikkaa pystyakselin kohdassa noin 0,10 s², ei origossa. Suoralta on merkitty kaksi pistettä, joista kulmakerroin "
            "luetaan: (0,200 m; 0,91 s²) ja (1,000 m; 4,12 s²). Kulmakerroin on noin 4,01 s²/m.")
    ax = Axes(f, (80, 390), (490, 70), x=(0, 1.1), y=(0, 4.5), xticks=[0, 0.2, 0.4, 0.6, 0.8, 1.0], yticks=[0, 1, 2, 3, 4],
              xlabel=r"l\ (\text{m})", ylabel=r"T^2\ (\text{s}^2)")
    ax.line([(0, b), (0.2, b + 0.2 * k)], INK, 2.5, dash="8 6")
    ax.line([(0.2, b + 0.2 * k), (1.06, b + 1.06 * k)], INK, 3)
    for l, t in zip(L4, T2): ax.point(l, t)
    for a, v in [(0.200, 0.91), (1.000, 4.12)]:
        f.circle(ax.X(a), ax.Y(v), 11, "none", COLD, 2)
    f.line(ax.X(0.2), ax.Y(0.91), ax.X(1.0), ax.Y(0.91), COLD, 2, "6 5")
    f.line(ax.X(1.0), ax.Y(0.91), ax.X(1.0), ax.Y(4.12), COLD, 2, "6 5")
    f.tex(ax.X(0.62), ax.Y(0.91) - 20, r"\Delta l = 0{,}80\,\text{m}", "middle", COLD)
    f.tex(ax.X(1.0) - 10, ax.Y(2.0), r"\Delta (T^2) = 3{,}21\,\text{s}^2", "end", COLD)
    f.circle(ax.X(0), ax.Y(b), 7, HOT, WHITE, 2)
    f.line(ax.X(0) + 8, ax.Y(b) - 4, ax.X(0.3) - 6, ax.Y(0.42), HOT, 1.5)
    f.tex(ax.X(0.3), ax.Y(0.42), r"b \approx 0{,}10\,\text{s}^2", "start", HOT)
    return f.svg()


def braking():
    """s6: braking distance against v^2 (v in m/s), five points, a line through the origin and the point it is read at."""
    v2 = [(v / 3.6) ** 2 for v in VK]
    k = sum(x * y for x, y in zip(v2, S6)) / sum(x * x for x in v2)
    f = Fig("fy12ko-s6-graph", 430, "Kuvaaja: polkupyörän jarrutusmatka s nopeuden neliön v² funktiona, kun nopeus on muunnettu "
            "yksikköön metriä sekunnissa. Viisi mittauspistettä nopeuden neliöillä 7,7–69,4 m²/s² on lähellä origon kautta "
            "kulkevaa suoraa. Suoralta on luettu piste (60 m²/s²; 7,2 m), joten kulmakerroin on 0,12 s²/m.")
    ax = Axes(f, (80, 380), (430, 70), x=(0, 80), y=(0, 10), xticks=[0, 10, 20, 30, 40, 50, 60, 70, 80], yticks=[0, 2, 4, 6, 8, 10],
              xlabel=r"v^2\ (\text{m}^2/\text{s}^2)", ylabel=r"s\ (\text{m})", xfmt=lambda v: fi(v) if v % 20 == 0 else "")
    ax.line([(0, 0), (77, 77 * k)], INK, 3)
    for x, s in zip(v2, S6): ax.point(x, s)
    ax.guide(60, 7.2, COLD)
    f.circle(ax.X(60), ax.Y(7.2), 9, "none", COLD, 2)
    f.tex(ax.X(60) + 14, ax.Y(7.2) + 26, r"(60\,\tfrac{\text{m}^2}{\text{s}^2};\ 7{,}2\,\text{m})", "start", COLD, bg=True)
    f.tex(ax.X(4), ax.Y(9.2), r"k = \tfrac{7{,}2\,\text{m}}{60\,\text{m}^2/\text{s}^2} = 0{,}12\,\tfrac{\text{s}^2}{\text{m}}", "start", COLD, bg=True)
    return f.svg()


FIGURES = {"fy12ko-s4-graph": pendulum, "fy12ko-s6-graph": braking}
REUSE = {"fy12ko-s4-graph": "reveals: the fitted line, its slope and intercept", "fy12ko-s6-graph": "reveals: the line and its slope"}
