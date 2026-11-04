"""Model graphs of the Tehtävät of fy9-liike (scripts/figlib.py); `python3 scripts/practice.py figures units/fy9-liike`
writes them into content/fi/units/fy9-liike/sovella/solutions.md. The data are the same as in answers.py."""
from figlib import Fig, Axes, INK, MUTED, WHITE, COLD, HEAT, GOOD, GOOD_LIGHT, fi

# fy9-liike-s3 (answers.py): invented data, 90 km/h until 10 s, then 0,65 m/s^2 of braking, rounded with +-1 km/h noise
T = [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40]
V = [91, 89, 90, 84, 77, 67, 56, 49, 39, 28, 21]


def _fit(x, y):
    mx, my = sum(x) / len(x), sum(y) / len(y)
    k = sum((a - mx) * (b - my) for a, b in zip(x, y)) / sum((a - mx) ** 2 for a in x)
    return k, my - k * mx


def train_graph():
    """fy9-liike-s3: the points, the constant 90 km/h level, the braking line fitted to the points from 12 s on and
    extended (dashed) to the time axis, the triangle under it shaded (the braking distance), the two points the slope
    is read from, and the read-offs of the start (about 10 s) and the stop (about 48,5 s)."""
    c = sum(V[:3]) / 3
    k, b = _fit(T[3:], V[3:])
    line = lambda t: k * t + b
    t0, t1 = (c - b) / k, -b / k
    f = Fig("fy9li-s3-graph", 400, "Kuvaaja: junan nopeus v kilometreinä tunnissa ajan t funktiona. Yksitoista mustaa pistettä hetkistä 0–40 s. "
            "Kolmen ensimmäisen pisteen kohdalla on vaakasuora suora tasolla 90 km/h. Muihin pisteisiin on sovitettu laskeva suora, joka "
            "leikkaa vaakasuoran suoran noin hetkellä 10 s ja jota on jatkettu katkoviivana aika-akselille noin hetkeen 48,5 s. Suoran "
            "pisteet (12 s; 85 km/h) ja (40 s; 20 km/h) on ympyröity, ja niistä luetaan kulmakerroin noin −2,3 km/h sekunnissa. Laskevan "
            "suoran ja aika-akselin väliin jäävä kolmio on väritetty vihreäksi: sen pinta-ala on jarrutusmatka.", width=440, size=24)
    ax = Axes(f, (64, 356), (336, 52), x=(0, 56), y=(0, 100), xticks=list(range(4, 57, 4)), yticks=list(range(10, 101, 10)),
              xlabel=r"t\ (\text{s})", ylabel=r"v\ (\text{km/h})", xfmt=lambda v: fi(v) if v % 8 == 0 else "",
              yfmt=lambda v: fi(v) if v % 20 == 0 else "")
    ax.area([(t0, c), (t1, 0), (t0, 0)], GOOD_LIGHT, 0.75)
    ax.line([(0, c), (t0, c)], INK, 3)
    ax.line([(t0, c), (40, line(40))], INK, 3)
    ax.line([(40, line(40)), (t1, 0)], INK, 2.5, dash="8 6")
    for a, v in zip(T, V): ax.point(a, v)
    for a, v in ((12, 85), (40, 20)):
        f.circle(ax.X(a), ax.Y(v), 11, "none", INK, 1.5)
    f.line(ax.X(t0), ax.Y(c), ax.X(t0), ax.y0, MUTED, 1.5, "6 5")
    f.tex(ax.X(t0) + 6, ax.Y(8), r"10\,\text{s}", "start", MUTED)
    f.tex(ax.X(t1) + 6, ax.Y(15), r"48{,}5\,\text{s}", "start", MUTED)
    f.tex(ax.X(27), ax.Y(76), r"k \approx -2{,}3\,\tfrac{\text{km/h}}{\text{s}}", "start")
    f.tex(ax.X(21), ax.Y(22), r"\text{jarrutusmatka}", "middle", GOOD)
    return f.svg()


FIGURES = {"fy9-liike-s3-graph": train_graph}
