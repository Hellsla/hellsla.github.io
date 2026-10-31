"""Figures of the guide Kulmakertoimen ja vakiotermin tulkinta (scripts/figlib.py); `python scripts/guides.py figures
tvt-kulmakerroin` writes them into guide.md. A schematic graph without numbers: invented points scattered about
y = 0,7 x + 0,8, their least-squares line computed here, two points read off that line far apart, the slope triangle
and the constant term."""
from figlib import Fig, Axes, INK, MUTED, WHITE

DATA = [(1.0, 1.2), (3.0, 3.2), (4.2, 3.44), (5.5, 4.3), (6.7, 5.79), (8.6, 6.57)]   # keksitty, suoran ympärillä


def least_squares(pts):
    """Slope and constant term of the least-squares line through pts."""
    n = len(pts); mx = sum(x for x, _ in pts) / n; my = sum(y for _, y in pts) / n
    k = sum((x - mx) * (y - my) for x, y in pts) / sum((x - mx) ** 2 for x, _ in pts)
    return k, my - k * mx


K, B = least_squares(DATA)
X1, X2 = 2.0, 8.0


def slope():
    f = Fig("tvtk-slope", 340, "Kaaviokuva ilman lukuarvoja: mittauspisteet ja niihin sovitettu suora. Suoralta on valittu "
            "kaksi kaukana toisistaan olevaa pistettä, joiden koordinaatit x yksi, y yksi ja x kaksi, y kaksi on merkitty "
            "akseleille. Pisteiden välissä on suorakulmainen kolmio: vaakasivu on delta x ja pystysivu delta y. Kulmakerroin "
            "k on delta y jaettuna delta x:llä. Suoran ja pystyakselin leikkauskohta on merkitty vakiotermiksi b.")
    ax = Axes(f, (90, 290), (460, 70), x=(0, 9), y=(0, 7.5), xticks=[], yticks=[], xlabel=r"x", ylabel=r"y", grid=False)
    y1, y2 = K * X1 + B, K * X2 + B
    ax.guide(X1, y1); ax.guide(X2, y2)
    ax.line([(0, B), (9, K * 9 + B)], INK)
    for p in DATA: ax.point(*p)
    f.line(ax.X(X1), ax.Y(y1), ax.X(X2), ax.Y(y1), MUTED, 2.5)
    f.line(ax.X(X2), ax.Y(y1), ax.X(X2), ax.Y(y2), MUTED, 2.5)
    for x, y in [(X1, y1), (X2, y2)]: f.circle(ax.X(x), ax.Y(y), 7, WHITE, INK, 3)
    f.circle(ax.X(0), ax.Y(B), 6, INK)
    f.tex(ax.X(X1), 314, r"x_1", "middle"); f.tex(ax.X(X2), 314, r"x_2", "middle")
    f.tex(78, ax.Y(y1), r"y_1", "end"); f.tex(78, ax.Y(y2), r"y_2", "end"); f.tex(78, ax.Y(B), r"b", "end")
    f.tex((ax.X(X1) + ax.X(X2)) / 2, ax.Y(y1) + 20, r"\Delta x", "middle", MUTED)
    f.tex(ax.X(X2) + 10, (ax.Y(y1) + ax.Y(y2)) / 2, r"\Delta y", "start", MUTED)
    f.tex(ax.X(2.6), ax.Y(5), r"k = \dfrac{\Delta y}{\Delta x}", "middle")
    return f.svg()


FIGURES = {"slope": slope}
