"""Figures of the guide Suoran sovittaminen mittauspisteisiin (scripts/figlib.py); `python scripts/guides.py figures
tvt-suoran-sovitus` writes them into guide.md. Schematic graphs without numbers: the points are an invented example,
the line through them is their least-squares line computed here, and the curved model is v = sqrt(2gh)."""
from figlib import Fig, Axes, INK, MUTED, RULE

# keksitty esimerkki ilman lukuarvoja: pisteet suoran y = x + 0,6 ympärillä
PTS = [(1, 2.45), (2, 1.85), (3, 4.25), (4, 3.95), (5, 6.5), (6, 6.1), (7, 7.15)]


def lsq(pts):
    """Least-squares line y = k x + b through the points."""
    n = len(pts); sx = sum(p[0] for p in pts); sy = sum(p[1] for p in pts)
    sxx = sum(p[0] ** 2 for p in pts); sxy = sum(p[0] * p[1] for p in pts)
    k = (n * sxy - sx * sy) / (n * sxx - sx ** 2)
    return k, (sy - k * sx) / n


def fit():
    """Points scattered about their least-squares line; dashed vertical residuals from each point to the line."""
    f = Fig("tvts-fit", 340, "Kaaviokuva ilman lukuarvoja: seitsemän mittauspistettä ja niihin sovitettu suora. Jokaisesta "
            "pisteestä on pystysuora katkoviiva suoralle; viivan pituus on pisteen poikkeama suorasta. Pisteitä on suoran "
            "kummallakin puolella, eikä suora kulje ensimmäisen ja viimeisen pisteen kautta. Pienimmän neliösumman "
            "menetelmä valitsee suoran, jolla poikkeamien neliöiden summa on pienin.")
    ax = Axes(f, (80, 290), (460, 80), x=(0, 8), y=(0, 9), xticks=[], yticks=[], xlabel=r"x", ylabel=r"y", grid=False)
    k, b = lsq(PTS)
    for x, y in PTS: f.line(ax.X(x), ax.Y(y), ax.X(x), ax.Y(k * x + b), MUTED, 2, "5 4")
    ax.line([(0.3, k * 0.3 + b), (7.7, k * 7.7 + b)], INK)
    for p in PTS: ax.point(*p)
    f.tex(ax.X(7.7) + 10, ax.Y(k * 7.7 + b), r"y = kx + b", "start")
    # the residual of the point at x = 2 named, to the lower right where no point or line is
    f.tex(ax.X(2.6), ax.Y(1.1), r"\text{poikkeama}", "start", MUTED)
    f.line(ax.X(2.6) - 3, ax.Y(1.1) - 12, ax.X(2) + 4, ax.Y(2.35), MUTED, 1.5)
    return f.svg()


def linearise():
    """Left: v against h curves (v = sqrt(2gh)) and a straight line misses it systematically. Right: v^2 against h is
    straight. No numbers: the shapes of the model only."""
    f = Fig("tvts-linearise", 330, "Kaksi kaaviokuvaa ilman lukuarvoja. Vasemmalla nopeus v korkeuden h funktiona: pisteet "
            "kaartuvat, ja niihin piirretty suora kulkee päissä pisteiden yläpuolella ja keskellä alapuolella. Oikealla "
            "samoista mittauksista laskettu nopeuden neliö v toiseen korkeuden h funktiona: pisteet ovat suoralla, joka "
            "kulkee origon kautta.")
    hs = [0.04, 0.08, 0.16, 0.3, 0.5, 0.75, 1.0]
    left = Axes(f, (80, 250), (220, 80), x=(0, 1.05), y=(0, 1.15), xticks=[], yticks=[],
                xlabel=r"h\ (\text{m})", ylabel=r"v\ (\text{m/s})", grid=False, origin_label=False)
    pts = [(h, h ** 0.5) for h in hs]
    k, b = lsq(pts)
    left.line([(0.05, k * 0.05 + b), (1.03, k * 1.03 + b)], MUTED, 2.5, "7 5")
    for p in pts: left.point(*p)
    right = Axes(f, (370, 250), (490, 80), x=(0, 1.05), y=(0, 1.15), xticks=[], yticks=[],
                 xlabel=r"h\ (\text{m})", ylabel=r"v^2\ (\text{m}^2/\text{s}^2)", grid=False, origin_label=False)
    right.line([(0, 0), (1.05, 1.05)], INK)
    for h in hs: right.point(h, h)
    f.line(337, 40, 337, 270, RULE, 1.5, "6 5")
    f.tex(150, 296, r"\text{pisteet kaartuvat}", "middle", MUTED)
    f.tex(450, 296, r"\text{pisteet suoralla}", "middle", MUTED)
    return f.svg()


FIGURES = {"fit": fit, "linearise": linearise}
