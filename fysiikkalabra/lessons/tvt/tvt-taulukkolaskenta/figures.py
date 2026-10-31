"""Figures of the guide Taulukko ja lasketut sarakkeet (scripts/figlib.py); `python scripts/guides.py figures
tvt-taulukkolaskenta` writes them into guide.md. A schematic data table of a data-analysis program such as Graphical
Analysis Pro (not a copy of its screen): two measured columns and a calculated column with its expression. The numbers
are an invented example (labelled esimerkkiarvoja), and the third column really is the second squared."""
from figlib import Fig, INK, MUTED, RULE, RULE_LIGHT, GLASS, WHITE, fi

ROWS = [(0.200, 0.90), (0.300, 1.10), (0.400, 1.27)]    # esimerkki: heilurin pituus l (m) ja jaksonaika T (s)
COLS = [40, 190, 340, 520]                               # column edges: l, T, T^2
TOP, HEAD, ROW = 120, 44, 40                             # the table's top, header height, a row's height


def sheet():
    f = Fig("tvtt-sheet", 372, "Kaaviokuva mittausohjelman datataulukosta keksityin esimerkkiarvoin. Ensimmäisen sarakkeen "
            "otsikko on l metreinä ja toisen T sekunteina; niissä ovat mitatut arvot. Kolmas sarake on laskettu sarake, "
            "jonka otsikko on T toiseen sekunnin neliöinä. Sen yläpuolella näkyy sarakkeen lauseke: T lainausmerkeissä "
            "potenssiin kaksi. Kolmannella rivillä laskettu arvo näkyy pyöristämättömänä, 1,6129.")
    # the expression of the calculated column
    f.tex(COLS[2], 40, r"\text{laskettu sarake, lauseke:}", "middle", MUTED)
    f.rect(COLS[2], 64, COLS[3] - COLS[2], 38, WHITE, INK, 2, rx=4)
    f.tex(COLS[2] + 14, 83, r'\texttt{"T"\textasciicircum 2}', "start")
    f.line((COLS[2] + COLS[3]) / 2, 102, (COLS[2] + COLS[3]) / 2, TOP, MUTED, 2)
    # header and the computed column's tint
    bottom = TOP + HEAD + ROW * 3
    f.rect(COLS[0], TOP, COLS[-1] - COLS[0], HEAD, RULE_LIGHT)
    f.rect(COLS[2], TOP + HEAD, COLS[3] - COLS[2], ROW * 3, GLASS)
    for x in COLS: f.line(x, TOP, x, bottom, RULE, 1.5)
    for y in [TOP + HEAD + ROW * k for k in range(1, 3)]: f.line(COLS[0], y, COLS[-1], y, RULE, 1.5)
    f.line(COLS[0], TOP + HEAD, COLS[-1], TOP + HEAD, INK, 2)
    f.rect(COLS[0], TOP, COLS[-1] - COLS[0], bottom - TOP, "none", RULE, 2)
    for i, h in enumerate([r"l\ (\text{m})", r"T\ (\text{s})", r"T^2\ (\text{s}^2)"]):
        f.tex((COLS[i] + COLS[i + 1]) / 2, TOP + HEAD / 2, h, "middle")
    for r, (l, t) in enumerate(ROWS):
        y = TOP + HEAD + ROW * (r + 0.5)
        f.tex(COLS[1] - 16, y, fi(l, 3), "end"); f.tex(COLS[2] - 16, y, fi(t, 2), "end")
        t2 = round(t * t, 4)
        f.tex(COLS[3] - 16, y, fi(t2, 2 if t2 == round(t2, 2) else 4), "end")
    # what is measured and what is computed
    yb = bottom + 16
    for a, b, tex in [(COLS[0] + 4, COLS[2] - 4, r"\text{mitatut arvot}"), (COLS[2] + 4, COLS[3] - 4, r"\text{laskettu}")]:
        f.line(a, yb, b, yb, MUTED, 2); f.line(a, yb - 8, a, yb, MUTED, 2); f.line(b, yb - 8, b, yb, MUTED, 2)
        f.tex((a + b) / 2, yb + 22, tex, "middle", MUTED)
    f.tex(COLS[0], 83, r"\text{esimerkkiarvoja}", "start", MUTED)
    return f.svg()


FIGURES = {"sheet": sheet}
