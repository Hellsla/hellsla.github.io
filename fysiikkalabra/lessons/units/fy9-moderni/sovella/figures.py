"""Model graphs of the Tehtävät of fy9-moderni (scripts/figlib.py); `python3 scripts/practice.py figures units/fy9-moderni`
writes them into content/fi/units/fy9-moderni/sovella/solutions.md. The data are the same as in answers.py."""
from figlib import Fig, Axes, INK, MUTED, HOT, COLD, GOOD, fi

# fy9-moderni-s3 (answers.py): invented photoelectric data, W 2,25 eV, h 6,626e-34 J s, scatter about 0,01 V
c = 2.998e8
L = [365, 405, 436, 470, 505]                    # nm
U = [1.15, 0.80, 0.61, 0.38, 0.21]               # V
F = [c / (l * 1e-9) / 1e14 for l in L]           # 10^14 Hz


def _fit(x, y):
    mx, my = sum(x) / len(x), sum(y) / len(y)
    k = sum((a - mx) * (b - my) for a, b in zip(x, y)) / sum((a - mx) ** 2 for a in x)
    return k, my - k * mx


def points_graph():
    """fy9-moderni-s3 a: the stopping voltage against the frequency, the five measured points on a frame that starts
    at 5,0e14 Hz; the points lie on a rising straight line, which is not drawn here."""
    f = Fig("fy9mo-s3-p", 400, "Kuvaaja: pysäytysjännite U voltteina valon taajuuden f funktiona, taajuusakselin yksikkö 10 "
            "potenssiin 14 hertsiä. Vaaka-akseli alkaa arvosta 5,0 ja päättyy arvoon 8,5, pystyakseli nollasta 1,4 volttiin. Viisi mustaa "
            "pistettä taajuuksilla 5,94–8,21 ja jännitteillä 0,21–1,15 volttia nousevat tasaisesti ja asettuvat likimain "
            "samalle suoralle.", size=28)
    ax = Axes(f, (100, 340), (405, 66), x=(5.0, 8.5), y=(0, 1.4), xticks=[5.0 + 0.5 * i for i in range(8)],
              yticks=[0.2 * i for i in range(1, 8)], xlabel=r"f\ (10^{14}\,\text{Hz})", ylabel=r"U\ (\text{V})",
              xfmt=lambda v: fi(round(v, 1), 1) if abs(v - round(v)) < 1e-9 else "", yfmt=lambda v: fi(round(v, 1), 1) if round(v * 10) % 4 == 0 else "")
    for x, y in zip(F, U): ax.point(x, y)
    return f.svg()


def fit_graph():
    """fy9-moderni-s3 b, c and d: the points, the fitted line (solid over the data, dashed back to the U axis), the two
    circled read-off points (0; -2,24 V) and (8,0e14 Hz; 1,06 V), and the f-axis crossing f0 = 5,43e14 Hz."""
    k, b = _fit(F, U)
    line = lambda x: k * x + b
    f0 = -b / k
    f = Fig("fy9mo-s3-fit", 470, "Kuvaaja: pysäytysjännite U voltteina valon taajuuden f funktiona, taajuusakseli nollasta "
            "9 kertaa 10 potenssiin 14 hertsiin ja jänniteakseli miinus 2,5:stä plus 1,5 volttiin. Viiteen pisteeseen on "
            "sovitettu nouseva suora, jota on jatkettu katkoviivana pystyakselille asti. Suora leikkaa pystyakselin noin "
            "arvossa miinus 2,24 volttia ja vaaka-akselin noin kohdassa 5,43 kertaa 10 potenssiin 14 hertsiä. Suoralta on "
            "ympyröity lukemiseen käytetyt pisteet nolla ja miinus 2,24 volttia sekä 8,0 kertaa 10 potenssiin 14 hertsiä "
            "ja 1,06 volttia.", size=28)
    ax = Axes(f, (96, 410), (405, 70), x=(0, 9.0), y=(-2.5, 1.5), xticks=[1.0 * i for i in range(1, 10)],
              yticks=[-2.5 + 0.5 * i for i in range(0, 9)], xlabel=r"f\ (10^{14}\,\text{Hz})", ylabel=r"U\ (\text{V})",
              xfmt=lambda v: "", yfmt=lambda v: fi(int(round(v))) if abs(v - round(v)) < 1e-9 else "",
              x_at=0)
    for t in (2, 4, 6, 8):   # the f tick numbers below the axis, clear of the data points above it
        f.tex(ax.X(t), ax.Y(0) + 24, fi(t), "middle")
    ax.line([(F[-1] - 0.25, line(F[-1] - 0.25)), (F[0] + 0.3, line(F[0] + 0.3))], INK, 3)
    ax.line([(0, line(0)), (F[-1] - 0.25, line(F[-1] - 0.25))], INK, 2.5, dash="8 6")
    for x, y in zip(F, U): ax.point(x, y)
    for x, y in ((0.0, -2.24), (8.0, 1.06)):
        f.circle(ax.X(x), ax.Y(y), 11, "none", INK, 1.5)
    ax.guide(8.0, 1.06, MUTED)
    f.circle(ax.X(f0), ax.Y(0), 6, GOOD)
    f.tex(ax.X(f0) - 30, ax.Y(-0.85), r"f_0 \approx 5{,}43 \cdot 10^{14}\,\text{Hz}", "start", GOOD, bg=True)
    f.tex(ax.X(0.35), ax.Y(-2.24), r"-\tfrac{W}{e} \approx -2{,}24\,\text{V}", "start", GOOD, bg=True)
    f.tex(ax.X(4.4), ax.Y(-1.4), r"k = \tfrac{h}{e}", "start")
    return f.svg()


FIGURES = {"fy9-moderni-s3-p": points_graph, "fy9-moderni-s3-fit": fit_graph}
