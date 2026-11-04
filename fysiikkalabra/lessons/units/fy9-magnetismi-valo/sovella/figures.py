"""Model graphs of the Tehtävät of fy9-magnetismi-valo (scripts/figlib.py); `python3 scripts/practice.py figures
units/fy9-magnetismi-valo` writes them into content/fi/units/fy9-magnetismi-valo/sovella/solutions.md. The data are
the same as in answers.py. The magnetic field is green (FY7 colours)."""
from figlib import Fig, Axes, INK, MUTED, GOOD, COLD, fi

# fy9-magnetismi-valo-s3 (answers.py): invented data, mu0 I/(2 pi) = 2,40 uT m, a background of about 11 uT
R = [0.020, 0.030, 0.040, 0.060, 0.080, 0.120]          # m
B = [132, 90, 72, 50, 41, 31]                          # uT
INV = [1 / r for r in R]
FIELD = GOOD


def _fit(x, y):
    mx, my = sum(x) / len(x), sum(y) / len(y)
    k = sum((a - mx) * (b - my) for a, b in zip(x, y)) / sum((a - mx) ** 2 for a in x)
    return k, my - k * mx


def field_graph():
    """fy9-magnetismi-valo-s3 a: B against r, the six points and a smooth dashed curve of the fitted model k/r + b
    through them; the curve levels off above the r axis, not towards zero."""
    k, b = _fit(INV, B)
    f = Fig("fy9mv-s3-B", 440, "Kuvaaja: magneettivuon tiheys B mikrotesloina etäisyyden r funktiona senttimetreinä. Kuusi "
            "mustaa pistettä etäisyyksillä 2–12 cm, arvot 132 mikroteslasta 31 mikroteslaan. Pisteiden kautta kulkee "
            "katkoviivakäyrä, joka laskee jyrkästi ja loivenee. Kun etäisyys kaksinkertaistuu 2 senttimetristä 4 "
            "senttimetriin, kenttä pienenee vain 132:sta 72:een eikä puoleen.", size=30)
    ax = Axes(f, (96, 380), (430, 76), x=(0, 13), y=(0, 150), xticks=list(range(1, 14)), yticks=[10 * i for i in range(1, 16)],
              xlabel=r"r\ (\text{cm})", ylabel=r"B\ (\mu\text{T})",
              xfmt=lambda v: fi(v) if v % 2 == 0 else "", yfmt=lambda v: fi(v) if v % 50 == 0 else "")
    ax.curve(lambda r: k / (r / 100) + b, 1.8, 13, INK, 2.5, dash="8 6")
    for r, bb in zip(R, B): ax.point(100 * r, bb)
    f.tex(ax.X(6.5), ax.Y(95), r"\text{loivenee}", "start", MUTED)
    return f.svg()


def linear_graph():
    """fy9-magnetismi-valo-s3 b, c and d: B against 1/r, the points, the fitted line (solid over the data, dashed back
    to the B axis), the two circled line points the slope is read from, and the intercept b on the B axis."""
    k, b = _fit(INV, B)
    line = lambda x: k * x + b
    f = Fig("fy9mv-s3-lin", 440, "Kuvaaja: magneettivuon tiheys B mikrotesloina etäisyyden käänteisluvun 1 per r funktiona "
            "yksikössä 1 per metri. Kuusi mustaa pistettä välillä 8–50 per metri, arvot 31:stä 132 mikroteslaan. "
            "Pisteisiin on sovitettu nouseva suora, jota on jatkettu katkoviivana pystyakselille, jonka se leikkaa noin "
            "arvossa 11 mikroteslaa, selvästi origon yläpuolella. Suoralta on ympyröity kaksi pistettä, (5,0; 23) ja "
            "(50; 132), joista luetaan kulmakerroin noin 2,42 mikroteslaa kertaa metri.", size=30)
    ax = Axes(f, (96, 380), (430, 76), x=(0, 55), y=(0, 150), xticks=[5 * i for i in range(1, 12)], yticks=[10 * i for i in range(1, 16)],
              xlabel=r"\tfrac{1}{r}\ (\tfrac{1}{\text{m}})", ylabel=r"B\ (\mu\text{T})",
              xfmt=lambda v: fi(v) if v % 10 == 0 else "", yfmt=lambda v: fi(v) if v % 50 == 0 else "")
    ax.line([(INV[-1], line(INV[-1])), (INV[0], line(INV[0]))], INK, 3)
    ax.line([(0, line(0)), (INV[-1], line(INV[-1]))], INK, 2.5, dash="8 6")
    for x, y in zip(INV, B): ax.point(x, y)
    for x, y in ((5.0, 23.0), (50.0, 132.0)):
        f.circle(ax.X(x), ax.Y(y), 11, "none", INK, 1.5)
        ax.guide(x, y, MUTED)
    f.circle(ax.X(0), ax.Y(line(0)), 6, FIELD)
    f.line(ax.X(0) + 5, ax.Y(line(0)) - 5, ax.X(3), ax.Y(62), FIELD, 2)
    f.tex(ax.X(1.5), ax.Y(72), r"b \approx 11\,\mu\text{T}", "start", FIELD, bg=True)
    f.tex(ax.X(2), ax.Y(140), r"k \approx 2{,}42\,\mu\text{T}\cdot\text{m}", "start")
    return f.svg()


FIGURES = {"fy9-magnetismi-valo-s3-B": field_graph, "fy9-magnetismi-valo-s3-lin": linear_graph}
