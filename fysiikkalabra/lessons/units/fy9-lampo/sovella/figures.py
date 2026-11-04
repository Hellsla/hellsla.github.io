"""Model graphs of the Tehtävät of fy9-lampo (scripts/figlib.py); `python3 scripts/practice.py figures units/fy9-lampo`
writes them into content/fi/units/fy9-lampo/sovella/solutions.md. The data are the same as in answers.py."""
from figlib import Fig, Axes, INK, MUTED, HEAT, COLD, fi

# fy9-lampo-s3 (answers.py): invented data, r = 2,26 MJ/kg, 70 W lost to the room, 300 s per run, plus noise
P = [200, 400, 600, 800, 1000]          # W
DM = [17.9, 43.1, 70.8, 96.4, 123.8]   # g in 5,00 min


def _fit(x, y):
    mx, my = sum(x) / len(x), sum(y) / len(y)
    k = sum((a - mx) * (b - my) for a, b in zip(x, y)) / sum((a - mx) ** 2 for a in x)
    return k, my - k * mx


def evaporation_graph():
    """fy9-lampo-s3: the five points, the fitted line over the data (solid) and extended to the P axis and to
    1100 W (dashed), the two line points the slope is read from (circled) and the intercept on the P axis."""
    k, b = _fit(P, DM)
    line = lambda p: k * p + b
    p0 = -b / k
    f = Fig("fy9la-s3-graph", 420, "Kuvaaja: höyrystyneen veden massa Δm viidessä minuutissa uppokuumentimen tehon P funktiona. "
            "Viisi mustaa pistettä tehoilla 200–1000 W. Pisteisiin on sovitettu nouseva suora, jota on jatkettu katkoviivana "
            "vaaka-akselille ja tehoon 1100 W asti. Suora kulkee pisteiden (100 W; 4 g) ja (1100 W; 137 g) kautta; nämä kaksi "
            "suoran pistettä on ympyröity, ja niistä luetaan kulmakerroin noin 0,133 g/W. Suora leikkaa vaaka-akselin noin "
            "teholla 70 W. Suora ei kulje origon kautta.", width=480, size=26)
    ax = Axes(f, (84, 370), (364, 60), x=(0, 1200), y=(0, 150), xticks=list(range(100, 1201, 100)), yticks=list(range(10, 151, 10)),
              xlabel=r"P\ (\text{W})", ylabel=r"\Delta m\ (\text{g})",
              xfmt=lambda v: fi(v) if v % 400 == 0 else "", yfmt=lambda v: fi(v) if v % 50 == 0 else "")
    ax.line([(200, line(200)), (1000, line(1000))], INK, 3)
    ax.line([(p0, 0), (200, line(200))], INK, 2.5, dash="8 6")
    ax.line([(1000, line(1000)), (1100, line(1100))], INK, 2.5, dash="8 6")
    for a, m in zip(P, DM): ax.point(a, m)
    for a, m in ((100, 4.0), (1100, 137.0)):                               # the points the slope is read from
        f.circle(ax.X(a), ax.Y(m), 11, "none", INK, 1.5)
    f.add(f'<circle cx="{ax.X(p0):.1f}" cy="{ax.y0}" r="7" fill="{HEAT}" stroke="#ffffff" stroke-width="2"/>')
    f.add(f'<line x1="{ax.X(p0) + 6:.1f}" y1="{ax.y0 - 6}" x2="{ax.X(260):.1f}" y2="{ax.Y(9):.1f}" stroke="{HEAT}" stroke-width="1.5"/>')
    f.tex(ax.X(260) + 4, ax.Y(9), r"P_\text{h} \approx 70\,\text{W}", "start", HEAT, bg=True)
    f.tex(ax.X(660), ax.Y(118), r"k \approx 0{,}133\,\text{g/W}", "end", bg=True)
    return f.svg()


FIGURES = {"fy9-lampo-s3-graph": evaporation_graph}
