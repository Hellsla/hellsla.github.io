"""Model graphs of the Tehtävät of fy9-tasavirta (scripts/figlib.py); `python3 scripts/practice.py figures units/fy9-tasavirta`
writes them into content/fi/units/fy9-tasavirta/sovella/solutions.md. The data are the same as in answers.py."""
from figlib import Fig, Axes, INK, MUTED, COLD, HOT, GOOD, WHITE, fi

# fy9-tasavirta-s3 (answers.py): invented data, E 4,62 V and R_s 0,72 ohm with meter scatter
I = [0.10, 0.25, 0.40, 0.60, 0.80, 1.00]        # A
U = [4.56, 4.43, 4.34, 4.18, 4.06, 3.89]        # V


def _fit(x, y):
    mx, my = sum(x) / len(x), sum(y) / len(y)
    k = sum((a - mx) * (b - my) for a, b in zip(x, y)) / sum((a - mx) ** 2 for a in x)
    return k, my - k * mx


def ui_graph():
    """fy9-tasavirta-s3 a and b: the six (I, U) points on a U axis cut at 3,6 V (the cut marked with a zigzag), the
    fitted line solid over the data and dashed back to the U axis, and the two circled line points the slope is read
    from: (0 A; 4,63 V) and (1,20 A; 3,75 V)."""
    k, b = _fit(I, U)
    line = lambda i: k * i + b
    f = Fig("fy9tv-s3-ui", 440, "Kuvaaja: paristokotelon napajännite U voltteina virran I funktiona ampeereina. Pystyakseli alkaa "
            "3,6 voltista, ja katkaisu on merkitty akselille. Kuusi mustaa pistettä virroilla 0,10–1,00 A, jännitteet 4,56 voltista "
            "3,89 volttiin. Pisteisiin on sovitettu laskeva suora, jota on jatkettu katkoviivana pystyakselille, jonka se leikkaa "
            "noin arvossa 4,63 V, ja virtaan 1,20 A asti. Suoralta on ympyröity kaksi pistettä, (0 A; 4,63 V) ja (1,20 A; 3,75 V), "
            "joista luetaan kulmakerroin.", size=30)
    ax = Axes(f, (110, 380), (470, 60), x=(0, 1.3), y=(3.6, 4.8), xticks=[0.1 * i for i in range(1, 14)],
              yticks=[3.6 + 0.1 * i for i in range(1, 13)], xlabel=r"I\ (\text{A})", ylabel=r"U\ (\text{V})",
              xfmt=lambda v: fi(round(v, 1), 1) if round(v * 10) % 4 == 0 else "",
              yfmt=lambda v: fi(round(v, 1), 1) if round(v * 10) % 2 == 0 else "", origin_label=False)
    # the cut of the U axis
    y0 = ax.y0
    f.path(f"M{ax.x0 - 9},{y0 - 14} L{ax.x0 + 9},{y0 - 22} M{ax.x0 - 9},{y0 - 24} L{ax.x0 + 9},{y0 - 32}", "none", INK, 2.5)
    f.tex(ax.x0 - 10, y0 + 22, "0", "end")
    ax.line([(I[0], line(I[0])), (I[-1], line(I[-1]))], INK, 3)
    ax.line([(0, line(0)), (I[0], line(I[0]))], INK, 2.5, dash="8 6")
    ax.line([(I[-1], line(I[-1])), (1.2, line(1.2))], INK, 2.5, dash="8 6")
    for a, u in zip(I, U): ax.point(a, u)
    for x, y in ((0.0, 4.63), (1.20, 3.75)):
        f.circle(ax.X(x), ax.Y(y), 11, "none", COLD, 2.5)
    ax.guide(1.20, 3.75, COLD)
    f.tex(ax.X(0.06), ax.Y(4.72), r"E \approx 4{,}63\,\text{V}", "start", COLD, bg=True)
    f.tex(ax.X(0.62), ax.Y(3.75), r"(1{,}20\,\text{A};\ 3{,}75\,\text{V})", "middle", COLD, bg=True)
    return f.svg()


def ik_graph():
    """fy9-tasavirta-s3 c: the whole line on axes from zero, the measured points crowded at the left, the line dashed
    beyond the data down to the I axis at the short-circuit current, about 6,3 A."""
    k, b = _fit(I, U)
    ik = -b / k
    f = Fig("fy9tv-s3-ik", 400, "Kuvaaja: napajännite U voltteina virran I funktiona ampeereina, akselit nollasta. Mittauspisteet ovat "
            "vasemmalla virroilla 0–1 A. Sovitettu suora jatkuu katkoviivana mittausalueen ulkopuolelle ja leikkaa vaaka-akselin "
            "oikosulkuvirran kohdalla noin 6,3 ampeerissa, yli kuusi kertaa suurimman mitatun virran kohdalla.", size=30)
    ax = Axes(f, (90, 340), (480, 60), x=(0, 7), y=(0, 5), xticks=list(range(1, 8)), yticks=list(range(1, 6)),
              xlabel=r"I\ (\text{A})", ylabel=r"U\ (\text{V})")
    ax.area([(0, 0), (1.0, 0), (1.0, 5), (0, 5)], "#d0e6fb", 0.5)
    ax.line([(0, b), (I[-1], k * I[-1] + b)], INK, 3)
    ax.line([(I[-1], k * I[-1] + b), (ik, 0)], INK, 2.5, dash="8 6")
    for a, u in zip(I, U): ax.point(a, u, r=5)
    f.circle(ax.X(ik), ax.Y(0), 7, HOT)
    f.tex(ax.X(6.4), ax.Y(1.2), r"I_\text{k} \approx 6{,}3\,\text{A}", "middle", HOT, bg=True)
    f.tex(ax.X(1.15), ax.Y(1.1), r"\text{mittausalue}", "start", MUTED, bg=True)
    return f.svg()


FIGURES = {"fy9-tasavirta-s3-ui": ui_graph, "fy9-tasavirta-s3-ik": ik_graph}
