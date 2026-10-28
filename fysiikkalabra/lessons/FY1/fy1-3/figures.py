"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy1-3` writes them into lesson.md."""
from figlib import (Fig, INK, MUTED, WHITE, RULE_LIGHT, HOT, COLD, GOOD, ALUMINIUM, METAL_EDGE, IRON, GLASS, GOOD_LIGHT, fi)


def _dots(f, X, ya, values, binw, color=COLD, step=16, r=7):
    """Readings stacked in bins of binw on the axis at height ya; returns the highest stack's top y."""
    bins = {}
    for v in values:
        bins.setdefault(round(v / binw), []).append(v)
    top = ya
    for b, vs in bins.items():
        for j, v in enumerate(vs):
            cy = ya - 12 - j * step
            f.circle(X(b * binw), cy, r, color, WHITE, 2)
            top = min(top, cy - r)
    return top


def _axis(f, X, ya, lo, hi, ticks, title=r"t\ (\text{s})", ext=24):
    """A time axis with an arrowhead, ticks with LaTeX numbers (decimal comma) and the title at the arrow end."""
    f.arrow(X(lo) - 12, ya, X(hi) + ext, ya, INK, 2.5, 13)
    for t in ticks:
        f.line(X(t), ya, X(t), ya + 7, INK, 2)
        f.tex(X(t), ya + 26, fi(t), "middle")
    if title:
        f.tex(X(hi) + ext + 6, ya, title, "start")


def error_types():
    f = Fig("fy13-err", 400, "Kaavakuva samasta mittauksesta kahdella tavalla, aikaakseli mittakaavassa. Ylhäällä on satunnaisvirhe: "
            "kymmenen tulosta hajaantuu oikean arvon 2,40 s molemmin puolin, ja keskiarvo 2,41 s on lähellä oikeaa arvoa. "
            "Alhaalla on systemaattinen virhe: kymmenen tulosta on tiiviissä ryhmässä, mutta ryhmä on kokonaan oikean arvon "
            "oikealla puolella ja keskiarvo 2,59 s on noin 0,19 s liian suuri.")
    X = lambda t: 60 + (t - 2.2) / 0.6 * 430
    A = [2.30, 2.34, 2.36, 2.38, 2.40, 2.41, 2.43, 2.45, 2.48, 2.52]
    B = [2.55, 2.57, 2.58, 2.58, 2.59, 2.60, 2.60, 2.61, 2.62, 2.64]
    for ya, vals, title, sys_ in ((158, A, r"\text{Satunnaisvirhe: tulokset hajaantuvat}", False),
                                  (354, B, r"\text{Systemaattinen virhe: tulokset siirtyvät}", True)):
        f.tex(14, ya - 132, title, "start")
        m = sum(vals) / len(vals)
        f.line(X(2.4), ya, X(2.4), ya - 86, GOOD, 2.5, "7 6")
        f.line(X(m), ya, X(m), ya - 86, INK, 2.5)
        _dots(f, X, ya, vals, 0.02)
        _axis(f, X, ya, 2.2, 2.8, [2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8])
        f.tex(X(2.4) - 9, ya - 100, r"\text{oikea arvo}", "end", GOOD)
        f.tex(X(m) + 9, ya - 100, r"\text{keskiarvo}", "start")
        if sys_:
            f.arrow(X(2.4) + 2, ya - 66, X(m) - 2, ya - 66, HOT, 3.5, 14)
            f.tex((X(2.4) + X(m)) / 2, ya - 84, r"\Delta t_\text{sys}", "middle", HOT)
    f.line(24, 206, 576, 206, MUTED, 1.5, "8 6")
    return f.svg()


def range_half():
    f = Fig("fy13-half", 330, "Kaavakuva, ei lukuarvoja: kuusi mittaustulosta aika-akselilla. Suurin tulos t_max ja pienin tulos "
            "t_min rajaavat vaihteluvälin, jonka pituus on t_max − t_min. Keskiarvo on merkitty pystyviivalla. Vaihteluvälin "
            "puolikas Δt on arvio satunnaisvirheestä, ja tulos ilmoitetaan muodossa keskiarvo plus miinus Δt.")
    X = lambda t: 70 + (t - 3.0) / 0.4 * 420
    vals = [3.07, 3.12, 3.15, 3.19, 3.25, 3.31]
    m = sum(vals) / len(vals)
    ya = 170
    _dots(f, X, ya, vals, 0.01)
    # the range above the dots
    f.line(X(3.07), ya - 26, X(3.07), ya - 66, MUTED, 1.5, "6 5"); f.line(X(3.31), ya - 26, X(3.31), ya - 66, MUTED, 1.5, "6 5")
    f.arrow(X(3.07) + 8, ya - 56, X(3.31) - 8, ya - 56, MUTED, 2.5, 12); f.arrow(X(3.31) - 8, ya - 56, X(3.07) + 8, ya - 56, MUTED, 2.5, 12)
    f.tex(X(3.19), ya - 88, r"t_\text{max} - t_\text{min}", "middle")
    _axis(f, X, ya, 3.0, 3.4, [], title=r"t")
    f.tex(X(3.07), ya + 26, r"t_\text{min}", "middle"); f.tex(X(3.31), ya + 26, r"t_\text{max}", "middle")
    f.path(f"M{X(m)},{ya + 7} L{X(m) - 8},{ya + 22} L{X(m) + 8},{ya + 22} Z", INK)      # the mean, a marker under the axis
    f.tex(X(m), ya + 44, r"\bar{t}", "middle")
    # the result bar: mean plus and minus the half-range
    d = (3.31 - 3.07) / 2
    f.rect(X(m - d), 236, X(m + d) - X(m - d), 16, GOOD_LIGHT, GOOD, 2.5)
    f.line(X(m), 230, X(m), 258, INK, 2.5)
    f.tex(X(m - d) - 10, 244, r"\bar{t} - \Delta t", "end"); f.tex(X(m + d) + 10, 244, r"\bar{t} + \Delta t", "start")
    f.tex(300, 292, r"\Delta t = \dfrac{t_\text{max} - t_\text{min}}{2}", "middle")
    return f.svg()


def _scale(f, x0, reading, empty, obj_label=None):
    """A kitchen scale: body, pan and a display with the reading. x0 is the left edge of the 200 px wide body."""
    f.rect(x0, 206, 200, 100, ALUMINIUM, INK, 2.5, 10)
    f.rect(x0 + 24, 188, 152, 18, METAL_EDGE, INK, 2.5, 6)
    f.rect(x0 + 40, 238, 120, 44, GLASS, INK, 2)
    f.tex(x0 + 100, 260, reading, "middle")
    if not empty:
        f.rect(x0 + 62, 128, 76, 60, IRON, INK, 2.5, 6)
        f.line(x0 + 74, 142, x0 + 126, 142, ALUMINIUM, 2)


def zero_scale():
    f = Fig("fy13-zero", 392, "Kaavakuva, ei mittakaavassa: keittiövaaka kahdesti. Vasemmalla pannu on tyhjä, mutta vaaka näyttää "
            "1,2 g, joten nollakohta on väärin. Oikealla pannulla on rautakappale ja vaaka näyttää 48,7 g. Kappaleen massa "
            "saadaan vähentämällä nollalukema lukemasta: 48,7 g miinus 1,2 g on 47,5 g.")
    _scale(f, 50, r"1{,}2\,\text{g}", True)
    _scale(f, 350, r"48{,}7\,\text{g}", False)
    f.tex(150, 336, r"\text{tyhjä: } m_0", "middle"); f.tex(450, 336, r"\text{lukema } m_\text{lukema}", "middle")
    f.line(300, 48, 300, 352, MUTED, 1.5, "8 6")
    f.tex(300, 28, r"\text{systemaattinen virhe: nollakohta}", "middle")
    f.tex(300, 372, r"m = m_\text{lukema} - m_0", "middle")
    return f.svg()


def example_plot():
    f = Fig("fy13-ex", 330, "Mittaustulokset (t, aika) mittakaavassa: kuusi tulosta väliltä 3,07 s – 3,31 s, keskiarvo 3,18 s ja "
            "tulos 3,18 s ± 0,12 s vihreällä palkilla.")
    X = lambda t: 70 + (t - 3.0) / 0.4 * 420
    vals = [3.12, 3.25, 3.07, 3.31, 3.19, 3.15]
    m = sum(vals) / len(vals)
    ya = 150
    f.line(X(m), ya, X(m), ya - 88, INK, 2.5)
    _dots(f, X, ya, vals, 0.01)
    _axis(f, X, ya, 3.0, 3.4, [3.0, 3.1, 3.2, 3.3, 3.4])
    f.tex(X(m) - 10, ya - 100, r"\bar{t} = 3{,}18\,\text{s}", "end")
    f.rect(X(m - 0.12), 236, X(m + 0.12) - X(m - 0.12), 16, GOOD_LIGHT, GOOD, 2.5)
    f.line(X(m), 230, X(m), 258, INK, 2.5)
    f.tex(300, 292, r"t = 3{,}18\,\text{s} \pm 0{,}12\,\text{s}", "middle")
    return f.svg()


FIGURES = {"error-types": error_types, "range-half": range_half, "zero-scale": zero_scale, "example-plot": example_plot}
