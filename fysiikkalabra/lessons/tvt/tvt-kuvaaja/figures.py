"""Figures of the guide Mittauspisteiden kuvaaja (scripts/figlib.py); `python scripts/guides.py figures tvt-kuvaaja`
writes them into guide.md. The numbers are an invented example (labelled esimerkkiaineisto in the figure), never a
measurement: a pendulum's T^2 against l, about 4,0 s^2/m times l, with a scatter well inside the error bars."""
from figlib import Fig, Axes, INK, MUTED, RULE, fi

# esimerkkiaineisto: heilurin pituus l (m) ja jaksonajan neliö T^2 (s^2), epävarmuus 0,15 s^2
DATA = [(0.20, 0.86), (0.30, 1.14), (0.40, 1.66), (0.50, 1.97), (0.60, 2.50), (0.70, 2.76)]
DT2 = 0.15


def good_bad():
    """Above: a graph without axis titles, its points joined by a broken line and squashed by a far too large y scale.
    Below: the same example data with quantities and units on the axes, a scale the points fill, and error bars."""
    f = Fig("tvtk-good-bad", 640, "Kaksi kuvaajaa samasta keksitystä esimerkkiaineistosta, heilurin jaksonajan neliöstä "
            "pituuden funktiona. Ylempi kuvaaja on puutteellinen: akseleilla ei ole suureita eikä yksiköitä, vaan "
            "kysymysmerkit, pystyakselin asteikko ulottuu kahteenkymmeneen, joten pisteet ovat litistyneet kuvaajan alareunaan, ja "
            "pisteet on yhdistetty murtoviivalla. Alempi kuvaaja on hyvä: vaaka-akselilla on l metreinä ja pystyakselilla "
            "T toiseen sekunnin neliöinä, asteikot on valittu niin, että pisteet täyttävät kuvaajan, ja jokaisessa "
            "pisteessä on pystysuora epävarmuusjana. Pisteitä ei ole yhdistetty.")
    # the poor graph
    bad = Axes(f, (90, 270), (470, 80), x=(0, 0.8), y=(0, 20), xticks=[0.2, 0.4, 0.6, 0.8], yticks=[5, 10, 15, 20],
               xlabel=None, ylabel=None)
    f.tex(502, 270, r"\text{?}", "start", MUTED)
    f.tex(80, 38, r"\text{?}", "start", MUTED)
    bad.line(DATA, INK, 2.5)
    for p in DATA: bad.point(*p)
    f.tex(300, 205, r"\text{murtoviiva}", "middle", MUTED, bg=True)
    f.tex(588, 40, r"\text{puutteellinen}", "end")
    f.line(30, 322, 570, 322, RULE, 1.5, "6 5")
    # the good graph
    good = Axes(f, (100, 590), (470, 400), x=(0, 0.8), y=(0, 3), xticks=[0.2, 0.4, 0.6, 0.8],
                yticks=[0.5, 1, 1.5, 2, 2.5, 3], xlabel=r"l\ (\text{m})", ylabel=r"T^2\ (\text{s}^2)",
                yfmt=lambda v: fi(v) if v == int(v) else "")
    for l, t2 in DATA:
        x, y1, y2 = good.X(l), good.Y(t2 - DT2), good.Y(t2 + DT2)
        f.line(x, y1, x, y2, INK, 2); f.line(x - 7, y1, x + 7, y1, INK, 2); f.line(x - 7, y2, x + 7, y2, INK, 2)
        good.point(l, t2)
    f.tex(588, 360, r"\text{hyvä}", "end")
    f.tex(478, 560, r"\text{esimerkkiaineisto}", "end", MUTED, bg=True)
    return f.svg()


FIGURES = {"good-bad": good_bad}
