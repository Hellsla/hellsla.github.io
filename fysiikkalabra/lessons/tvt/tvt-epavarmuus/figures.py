"""Figures of the guide Kulmakertoimen epävarmuus (scripts/figlib.py); `python scripts/guides.py figures tvt-epavarmuus`
writes them into guide.md. A schematic graph without numbers: invented points with equal error bars, their
least-squares line, and the steepest and the shallowest line that still pass through every error bar (found here by a
search over slopes, so the drawn lines really do pass through all the bars)."""
from figlib import Fig, Axes, INK, MUTED

XS = [1, 2, 3, 4, 5, 6]
YS = [1.7, 2.25, 3.65, 4.4, 5.75, 6.3]      # keksitty esimerkki suoran y = x + 0,5 ympärillä
D = 0.5                                     # epävarmuusjanan puolikas


def lsq():
    n = len(XS); sx, sy = sum(XS), sum(YS); sxx = sum(x * x for x in XS); sxy = sum(x * y for x, y in zip(XS, YS))
    k = (n * sxy - sx * sy) / (n * sxx - sx ** 2)
    return k, (sy - k * sx) / n


def extremes():
    """(k, b) of the shallowest and the steepest line through every bar, each with b in the middle of its range."""
    found = []
    for i in range(4001):
        k = 0.5 + i * 0.00025
        lo = max(y - D - k * x for x, y in zip(XS, YS)); hi = min(y + D - k * x for x, y in zip(XS, YS))
        if lo <= hi: found.append((k, (lo + hi) / 2))
    return found[0], found[-1]


def lines():
    f = Fig("tvte-lines", 340, "Kaaviokuva ilman lukuarvoja: kuusi mittauspistettä, joissa kussakin on yhtä pitkä "
            "pystysuora epävarmuusjana. Pisteisiin on sovitettu suora, jonka kulmakerroin on k. Katkoviivoilla on piirretty "
            "jyrkin ja loivin suora, jotka vielä kulkevat jokaisen epävarmuusjanan kautta; niiden kulmakertoimet ovat k max "
            "ja k min. Suorat leikkaavat toisensa pisteiden keskivaiheilla ja erkanevat päitä kohti.")
    ax = Axes(f, (80, 300), (450, 70), x=(0, 7), y=(0, 8), xticks=[], yticks=[], xlabel=r"x", ylabel=r"y", grid=False)
    (kmin, bmin), (kmax, bmax) = extremes(); k, b = lsq()
    ax.line([(0.4, kmax * 0.4 + bmax), (6.6, kmax * 6.6 + bmax)], MUTED, 2.5, "8 6")
    ax.line([(0.2, kmin * 0.2 + bmin), (6.6, kmin * 6.6 + bmin)], MUTED, 2.5, "8 6")
    ax.line([(0.3, k * 0.3 + b), (6.9, k * 6.9 + b)], INK)
    for x, y in zip(XS, YS):
        X, y1, y2 = ax.X(x), ax.Y(y - D), ax.Y(y + D)
        f.line(X, y1, X, y2, INK, 2); f.line(X - 7, y1, X + 7, y1, INK, 2); f.line(X - 7, y2, X + 7, y2, INK, 2)
        ax.point(x, y)
    f.tex(ax.X(6.9) + 8, ax.Y(k * 6.9 + b), r"k", "start")
    f.tex(ax.X(4.2), ax.Y(7.0), r"k_\text{max}", "end", MUTED)
    f.line(ax.X(4.2) + 4, ax.Y(7.0) + 6, ax.X(5.6) - 2, ax.Y(kmax * 5.6 + bmax) - 3, MUTED, 1.5)
    f.tex(ax.X(5.4), ax.Y(3.4), r"k_\text{min}", "start", MUTED)
    f.line(ax.X(5.4) + 4, ax.Y(3.4) - 16, ax.X(4.7), ax.Y(kmin * 4.7 + bmin) + 4, MUTED, 1.5)
    return f.svg()


FIGURES = {"lines": lines}
