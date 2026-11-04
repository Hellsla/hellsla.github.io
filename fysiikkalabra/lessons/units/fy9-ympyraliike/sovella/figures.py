"""Model graphs of the Tehtävät of fy9-ympyraliike (scripts/figlib.py); `python3 scripts/practice.py figures units/fy9-ympyraliike`
writes them into content/fi/units/fy9-ympyraliike/sovella/solutions.md. The data are the same as in answers.py."""
from figlib import Fig, Axes, INK, MUTED, HEAT, COLD, fi

# fy9-ympyraliike-s3 (answers.py): invented data, m 0,200 kg at r 0,250 m on a rotating platform, noise about 1,5 %
T10 = [6.0, 7.0, 8.0, 9.5, 11.0, 13.0, 15.0]                      # s, ten rounds
F = [5.42, 4.07, 3.05, 2.21, 1.65, 1.19, 0.88]                    # N
T = [t / 10 for t in T10]
X = [1 / t ** 2 for t in T]


def _fit(x, y):
    mx, my = sum(x) / len(x), sum(y) / len(y)
    k = sum((a - mx) * (b - my) for a, b in zip(x, y)) / sum((a - mx) ** 2 for a in x)
    return k, my - k * mx


def force_period():
    """fy9-ympyraliike-s3 a: the force against the period, the points and the smooth curve of the fitted model through
    them (dashed), falling steeply at short periods and flattening at long ones."""
    k, b = _fit(X, F)
    f = Fig("fy9yl-s3-ft", 440, "Kuvaaja: langan voima F newtoneina kierrosajan T funktiona sekunteina. Seitsemän mustaa pistettä "
            "kierrosajoilla 0,60–1,50 s, voimat 5,42 N:sta 0,88 N:iin. Pisteiden kautta kulkee katkoviivakäyrä, joka laskee jyrkästi "
            "lyhyillä kierrosajoilla ja loivenee pitkillä: voima pienenee nopeammin kuin kierrosaika kasvaa, joten pisteisiin ei sovi suora.",
            size=30)
    ax = Axes(f, (96, 380), (430, 76), x=(0, 1.6), y=(0, 6), xticks=[0.2 * i for i in range(1, 9)], yticks=list(range(1, 7)),
              xlabel=r"T\ (\text{s})", ylabel=r"F\ (\text{N})",
              xfmt=lambda v: fi(round(v, 1), 1) if round(v * 10) % 4 == 0 else "", yfmt=lambda v: fi(v) if v % 2 == 0 else "")
    ax.curve(lambda t: k / t ** 2 + b, 0.57, 1.58, INK, 2.5, dash="8 6")
    for t, y in zip(T, F): ax.point(t, y)
    f.tex(ax.X(0.95), ax.Y(4.6), r"\text{ei suora}", "start", MUTED)
    return f.svg()


def linear_graph():
    """fy9-ympyraliike-s3 b, c and d: the force against 1/T^2, the points, the fitted line (solid over the data, dashed
    back to zero and on to the 8,0 N limit), the two circled line points the slope is read from."""
    k, b = _fit(X, F)
    line = lambda x: k * x + b
    xlim = (8.0 - b) / k
    f = Fig("fy9yl-s3-lin", 440, "Kuvaaja: langan voima F newtoneina suureen yksi jaettuna T toiseen funktiona yksikössä yksi jaettuna "
            "sekunti toiseen. Seitsemän mustaa pistettä välillä 0,44–2,78, voimat 0,88 N:sta 5,42 N:iin. Pisteisiin on sovitettu "
            "nouseva suora, joka kulkee lähes origon kautta. Suoraa on jatkettu katkoviivana voimaan 8,0 N asti, joka on langan "
            "kestävyys; se saavutetaan, kun yksi jaettuna T toiseen on noin 4,1. Suoralta on ympyröity kaksi pistettä, (0,50; 1,01) "
            "ja (2,50; 4,91), joista luetaan kulmakerroin noin 1,95 N s².", size=30)
    ax = Axes(f, (96, 380), (390, 76), x=(0, 4.5), y=(0, 9), xticks=[0.5 * i for i in range(1, 10)], yticks=list(range(1, 10)),
              xlabel=r"1/T^2\ (1/\text{s}^2)", ylabel=r"F\ (\text{N})",
              xfmt=lambda v: fi(v) if abs(v - round(v)) < 1e-9 else "", yfmt=lambda v: fi(v) if v % 2 == 0 else "")
    ax.line([(X[-1], line(X[-1])), (X[0], line(X[0]))], INK, 3)
    ax.line([(0, line(0)), (X[-1], line(X[-1]))], INK, 2.5, dash="8 6")
    ax.line([(X[0], line(X[0])), (xlim, 8.0)], INK, 2.5, dash="8 6")
    for x, y in zip(X, F): ax.point(x, y)
    for x, y in ((0.50, 1.01), (2.50, 4.91)):
        f.circle(ax.X(x), ax.Y(y), 11, "none", INK, 1.5)
        ax.guide(x, y, COLD)
    ax.guide(xlim, 8.0, HEAT)
    f.tex(ax.X(0.15), ax.Y(8.0) - 22, r"8{,}0\,\text{N}", "start", HEAT, bg=True)
    f.tex(ax.X(2.7), ax.Y(2.2), r"k \approx 1{,}95\,\text{N}\cdot\text{s}^2", "start", INK, bg=True)
    return f.svg()


FIGURES = {"fy9-ympyraliike-s3-ft": force_period, "fy9-ympyraliike-s3-lin": linear_graph}
