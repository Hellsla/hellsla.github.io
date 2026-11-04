"""Model graphs of the Tehtävät of fy9-voimat (scripts/figlib.py); `python3 scripts/practice.py figures units/fy9-voimat`
writes them into content/fi/units/fy9-voimat/sovella/solutions.md. The data are the same as in answers.py."""
from figlib import Fig, Axes, INK, MUTED, HEAT, COLD

# fy9-voimat-s3 (answers.py): invented data, a = (F - 0,24 N) / 0,850 kg plus noise
F = [0.40, 0.60, 0.80, 1.00, 1.20, 1.40, 1.60]
A = [0.20, 0.41, 0.67, 0.88, 1.14, 1.35, 1.61]


def _fit(x, y):
    mx, my = sum(x) / len(x), sum(y) / len(y)
    k = sum((a - mx) * (b - my) for a, b in zip(x, y)) / sum((a - mx) ** 2 for a in x)
    return k, my - k * mx


def cart_graph():
    """fy9-voimat-s3: the points, the fitted line over the data (solid), extended down to the F axis (dashed), the two
    line points the slope is read from (circled) and the intercept with the F axis (the friction force)."""
    k, b = _fit(F, A)
    line = lambda x: k * x + b
    F0 = -b / k
    f = Fig("fy9vo-s3-graph", 440, "Kuvaaja: vaunun kiihtyvyys a vetävän voiman F funktiona. Seitsemän mustaa pistettä voimilla "
            "0,40–1,60 N. Pisteisiin on sovitettu nouseva suora, jota on jatkettu katkoviivana alas vaaka-akselille asti. Suora "
            "kulkee pisteiden (0,40 N; 0,19 m/s²) ja (1,60 N; 1,60 m/s²) kautta; nämä kaksi suoran pistettä on ympyröity. Suora "
            "leikkaa vaaka-akselin noin kohdassa F = 0,24 N, eikä se kulje origon kautta.")
    ax = Axes(f, (96, 380), (500, 60), x=(0, 1.8), y=(0, 1.8), xticks=[0.2 * i for i in range(1, 10)],
              yticks=[0.2 * i for i in range(1, 10)], xlabel=r"F\ (\text{N})", ylabel=r"a\ (\text{m/s}^2)",
              xfmt=lambda v: (r"{:.1f}".format(v).replace(".", "{,}")) if round(v * 10) % 4 == 0 else "",
              yfmt=lambda v: (r"{:.1f}".format(v).replace(".", "{,}")) if round(v * 10) % 4 == 0 else "")
    ax.line([(0.40, line(0.40)), (1.60, line(1.60))], INK, 3)
    ax.line([(F0, 0), (0.40, line(0.40))], INK, 2.5, dash="8 6")
    for x, y in zip(F, A): ax.point(x, y)
    for x, y in ((0.40, 0.19), (1.60, 1.60)):
        f.circle(ax.X(x), ax.Y(y), 11, "none", INK, 1.5)
    f.circle(ax.X(F0), ax.Y(0), 7, HEAT)
    f.tex(ax.X(F0) + 10, ax.Y(0) - 28, r"F_0 \approx 0{,}24\,\text{N}", "start", HEAT)
    f.tex(ax.X(0.95), ax.Y(1.45), r"k \approx 1{,}18\,\tfrac{1}{\text{kg}}", "end", COLD)
    return f.svg()


FIGURES = {"fy9-voimat-s3-graph": cart_graph}
