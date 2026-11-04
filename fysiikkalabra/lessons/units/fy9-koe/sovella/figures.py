"""Model graphs of the fy9-koe Tehtävät (scripts/figlib.py); `python scripts/practice.py figures units/fy9-koe` writes
them into content/fi/units/fy9-koe/sovella/solutions.md. The data are those of tasks.json and answers.py."""
from figlib import Fig, Axes, INK, MUTED, COLD, n

L = [0.200, 0.350, 0.500, 0.650, 0.800, 0.950]                # m, to the top of the bob
t10 = [9.33, 12.08, 14.42, 16.41, 18.08, 19.72]                # s, ten periods
T2 = [(x / 10) ** 2 for x in t10]                              # s^2


def _fit(x, y):
    mx, my = sum(x) / len(x), sum(y) / len(y)
    k = sum((a - mx) * (b - my) for a, b in zip(x, y)) / sum((a - mx) ** 2 for a in x)
    return k, my - k * mx


def pendulum():
    """fy9-koe-s2 b and c: T^2 against L, the six points, the fitted line (not forced through the origin) and the two
    points of the line the slope is read from (L = 0,100 m and 0,900 m), with dashed guides to the axes."""
    k, b = _fit(L, T2)
    f = Fig("fy9-koe-s2-graph", 430, "Kuvaaja: heilahdusjakson neliö T² neliösekunteina langan pituuden L funktiona metreinä. "
            "Kuusi mittauspistettä pituuksilla 0,200–0,950 m nousee suoraan. Pisteisiin on sovitettu suora, joka leikkaa "
            "pystyakselin hieman origon yläpuolella, noin arvossa 0,06 s². Suoralta on luettu kaksi pistettä katkoviivoin: "
            "(0,100 m; 0,46 s²) ja (0,900 m; 3,68 s²). Kulmakerroin on noin 4,03 s²/m.")
    ax = Axes(f, (90, 380), (480, 60), x=(0, 1.0), y=(0, 4.5), xticks=[0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
              yticks=[0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5], xlabel=r"L\ (\text{m})", ylabel=r"T^2\ (\text{s}^2)",
              xfmt=lambda v: "" if round(v * 10) % 2 else ("0" if v == 0 else f"{v:.1f}".replace(".", "{,}")),
              yfmt=lambda v: "" if (v * 2) % 2 else str(int(v)))
    ax.line([(0, b), (1.0, b + k)], COLD, 3)
    for x in (0.100, 0.900):
        ax.guide(x, b + k * x)
        f.circle(ax.X(x), ax.Y(b + k * x), 10, "none", INK, 1.5)
    for x, y in zip(L, T2): ax.point(x, y)
    f.tex(ax.X(0.100) + 14, ax.Y(0.30), r"(0{,}100\,\text{m};\ 0{,}46\,\text{s}^2)", "start", MUTED, size=20, bg=True)
    f.tex(ax.X(0.900) - 14, ax.Y(b + 0.9 * k) - 30, r"(0{,}900\,\text{m};\ 3{,}68\,\text{s}^2)", "end", MUTED, size=20, bg=True)
    f.tex(ax.X(0.86), ax.Y(1.5), r"k \approx 4{,}03\,\tfrac{\text{s}^2}{\text{m}}", "end", COLD, bg=True)
    return f.svg()


FIGURES = {"fy9-koe-s2-graph": pendulum}
REUSE = {"fy9-koe-s2-graph": "reveals: the model graph of task fy9-koe-s2 (its solution)"}
