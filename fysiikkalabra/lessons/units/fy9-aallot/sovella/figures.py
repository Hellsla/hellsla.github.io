"""Model graphs of the Tehtävät of fy9-aallot (scripts/figlib.py); `python3 scripts/practice.py figures units/fy9-aallot`
writes them into content/fi/units/fy9-aallot/sovella/solutions.md. The data are the same as in answers.py."""
import math
from figlib import Fig, Axes, INK, MUTED, HEAT, COLD, GOOD, fi

# fy9-aallot-s3 (answers.py): invented pendulum data, g 9,81 m/s^2, the true length 1,5 cm longer than measured
L = [0.200, 0.350, 0.500, 0.650, 0.800, 0.950]           # m
T10 = [9.36, 12.07, 14.44, 16.29, 18.14, 19.76]          # s
T = [t / 10 for t in T10]
T2 = [t * t for t in T]


def _fit(x, y):
    mx, my = sum(x) / len(x), sum(y) / len(y)
    k = sum((a - mx) * (b - my) for a, b in zip(x, y)) / sum((a - mx) ** 2 for a in x)
    return k, my - k * mx


def period_graph():
    """fy9-aallot-s3 a: the period against the length, the six points and a smooth dashed curve of the fitted model
    through them, clearly bending down (the period grows like the square root of the length)."""
    k, b = _fit(L, T2)
    f = Fig("fy9aa-s3-T", 440, "Kuvaaja: heilurin jaksonaika T sekunteina langan pituuden l funktiona metreinä. Kuusi mustaa "
            "pistettä pituuksilla 0,20–0,95 m, jaksonajat 0,94 sekunnista 1,98 sekuntiin. Pisteiden kautta kulkee alaspäin "
            "loivenevaa katkoviivakäyrä: nelinkertainen pituus antaa vain noin kaksinkertaisen jaksonajan, joten pisteisiin ei "
            "sovi origon kautta kulkeva suora.", size=30)
    ax = Axes(f, (96, 380), (430, 76), x=(0, 1.0), y=(0, 2.5), xticks=[0.1 * i for i in range(1, 11)], yticks=[0.25 * i for i in range(1, 11)],
              xlabel=r"l\ (\text{m})", ylabel=r"T\ (\text{s})",
              xfmt=lambda v: fi(round(v, 1), 1) if round(v * 10) % 5 == 0 else "", yfmt=lambda v: fi(round(v, 1), 1) if abs(v * 2 - round(v * 2)) < 1e-9 else "")
    ax.curve(lambda l: math.sqrt(max(k * l + b, 0)), 0, 1.0, INK, 2.5, dash="8 6")
    for l, t in zip(L, T): ax.point(l, t)
    f.tex(ax.X(0.42), ax.Y(0.55), r"\text{loivenee}", "start", MUTED)
    return f.svg()


def linear_graph():
    """fy9-aallot-s3 b, c and d: T^2 against the length, the points, the fitted line (solid over the data, dashed back to
    the T^2 axis and on to the l axis), the two circled line points the slope is read from, and the intercepts."""
    k, b = _fit(L, T2)
    line = lambda l: k * l + b
    f = Fig("fy9aa-s3-lin", 440, "Kuvaaja: jaksonajan neliö T toiseen sekunnin neliöinä langan pituuden l funktiona metreinä. Kuusi "
            "mustaa pistettä pituuksilla 0,20–0,95 m, arvot 0,88:sta 3,90:een. Pisteisiin on sovitettu nouseva suora, jota on "
            "jatkettu katkoviivana pystyakselille, jonka se leikkaa noin arvossa 0,055 s², hieman origon yläpuolella. Suoralta on "
            "ympyröity kaksi pistettä, (0,10 m; 0,46 s²) ja (0,90 m; 3,69 s²), joista luetaan kulmakerroin noin 4,04 s² per metri.", size=30)
    ax = Axes(f, (96, 380), (430, 76), x=(0, 1.0), y=(0, 4.5), xticks=[0.1 * i for i in range(1, 11)], yticks=[0.5 * i for i in range(1, 10)],
              xlabel=r"l\ (\text{m})", ylabel=r"T^2\ (\text{s}^2)",
              xfmt=lambda v: fi(round(v, 1), 1) if round(v * 10) % 5 == 0 else "", yfmt=lambda v: fi(round(v)) if abs(v - round(v)) < 1e-9 else "")
    ax.line([(L[0], line(L[0])), (L[-1], line(L[-1]))], INK, 3)
    ax.line([(0, line(0)), (L[0], line(L[0]))], INK, 2.5, dash="8 6")
    for l, t in zip(L, T2): ax.point(l, t)
    for x, y in ((0.10, 0.46), (0.90, 3.69)):
        f.circle(ax.X(x), ax.Y(y), 11, "none", INK, 1.5)
        ax.guide(x, y, COLD)
    f.circle(ax.X(0), ax.Y(line(0)), 6, GOOD)
    f.tex(ax.X(0.30), ax.Y(0.55), r"b \approx 0{,}055\,\text{s}^2", "start", GOOD, bg=True)
    f.tex(ax.X(0.04), ax.Y(4.1), r"k \approx 4{,}04\,\text{s}^2/\text{m}", "start")
    return f.svg()


FIGURES = {"fy9-aallot-s3-T": period_graph, "fy9-aallot-s3-lin": linear_graph}
