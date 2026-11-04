"""Model graphs of the Tehtävät of fy9-energia (scripts/figlib.py); `python3 scripts/practice.py figures units/fy9-energia`
writes them into content/fi/units/fy9-energia/sovella/solutions.md. The data are the same as in answers.py."""
from figlib import Fig, Axes, INK, MUTED, WHITE, HEAT, COLD, fi

# fy9-energia-s3 (answers.py): invented data, 12 kWh other use + 4,8 kWh per kelvin below 17 °C, plus noise
T = [-4, -10, -16, -19, -13, -7, -1, 2]
E = [112, 139, 174, 186, 155, 126, 100, 83]


def _fit(x, y):
    mx, my = sum(x) / len(x), sum(y) / len(y)
    k = sum((a - mx) * (b - my) for a, b in zip(x, y)) / sum((a - mx) ** 2 for a in x)
    return k, my - k * mx


def heating_graph():
    """fy9-energia-s3: the points, the fitted line over the data (solid) and extended both ways (dashed), the two
    points the slope is read from, and the read-offs at -28 °C (c) and at 12 kWh (d)."""
    k, b = _fit(T, E)
    line = lambda t: k * t + b
    t_bal = (12 - b) / k
    f = Fig("fy9en-s3-graph", 440, "Kuvaaja: talon sähkönkulutus vuorokaudessa E ulkolämpötilan T funktiona. Kahdeksan mustaa pistettä "
            "lämpötiloissa −19…2 °C. Pisteisiin on sovitettu laskeva suora, jota on jatkettu katkoviivana molempiin suuntiin. Suora kulkee "
            "pisteiden (−20 °C; 191 kWh) ja (0 °C; 93 kWh) kautta; nämä kaksi suoran pistettä on ympyröity, ja niistä luetaan kulmakerroin noin −4,9 kWh asteelta. Lämpötilassa "
            "−28 °C suoralta luetaan noin 230 kWh. Suora laskee muun kulutuksen tasolle 12 kWh noin lämpötilassa 17 °C.")
    ax = Axes(f, (84, 390), (500, 70), x=(-30, 20), y=(0, 250), xticks=list(range(-30, 21, 5)), yticks=list(range(0, 251, 50)),
              xlabel=r"T\ ({}^\circ\text{C})", ylabel=r"E\ (\text{kWh})", origin_label=False,
              xfmt=lambda v: (r"-" + str(-v) if v < 0 else str(v)) if v % 10 == 0 else "")
    f.line(ax.X(0), ax.y0, ax.X(0), ax.y1, MUTED, 1.5)                  # T = 0 °C
    ax.line([(-19, line(-19)), (2, line(2))], INK, 3)
    ax.line([(-29, line(-29)), (-19, line(-19))], INK, 2.5, dash="8 6")
    ax.line([(2, line(2)), (18, line(18))], INK, 2.5, dash="8 6")
    for a, e in zip(T, E): ax.point(a, e)
    for a, e in ((-20, 191), (0, 93)):                                    # the points the slope is read from
        f.circle(ax.X(a), ax.Y(e), 11, "none", INK, 1.5)
    ax.guide(-28, line(-28), HEAT)
    ax.guide(t_bal, 12, COLD)
    f.tex(ax.X(-24), ax.Y(240), r"230\,\text{kWh}", "start", HEAT)
    f.tex(ax.X(-25), ax.Y(27), r"12\,\text{kWh}", "start", COLD)
    f.tex(ax.X(-6), ax.Y(200), r"k \approx -4{,}9\,\text{kWh}/{}^\circ\text{C}", "start")
    return f.svg()


FIGURES = {"fy9-energia-s3-graph": heating_graph}
