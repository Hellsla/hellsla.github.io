"""Model graphs of the Tehtävät of fy9-sailymislait (scripts/figlib.py); `python3 scripts/practice.py figures units/fy9-sailymislait`
writes them into content/fi/units/fy9-sailymislait/sovella/solutions.md. The data are the same as in answers.py."""
from figlib import Fig, Axes, INK, MUTED, HEAT, COLD, fi

# fy9-sailymislait-s3 (answers.py): invented braking data, t_r 0,90 s and a 6,4 m/s^2 plus noise
V = [30, 40, 50, 60, 70, 80, 90]                          # km/h
SP = [12.5, 20.0, 27.5, 36.5, 46.5, 58.5, 72.0]           # m
X = [v / 3.6 for v in V]                                  # m/s
Y = [s / x for s, x in zip(SP, X)]                        # s


def _fit(x, y):
    mx, my = sum(x) / len(x), sum(y) / len(y)
    k = sum((a - mx) * (b - my) for a, b in zip(x, y)) / sum((a - mx) ** 2 for a in x)
    return k, my - k * mx


def stopping_graph():
    """fy9-sailymislait-s3 a: the stopping distance against the initial speed in km/h, the points and a smooth curve
    of the fitted model through them (dashed), clearly bending upwards."""
    k, b = _fit(X, Y)
    f = Fig("fy9sl-s3-sp", 440, "Kuvaaja: pysähtymismatka s p metreinä lähtönopeuden v 0 funktiona kilometreinä tunnissa. Seitsemän mustaa "
            "pistettä nopeuksilla 30–90 km/h, matkat 12,5 m:stä 72 m:iin. Pisteiden kautta kulkee ylöspäin kaartuva katkoviivakäyrä: "
            "matka kasvaa nopeammin kuin nopeus, joten pisteisiin ei sovi suora.", size=30)
    ax = Axes(f, (96, 380), (410, 76), x=(0, 100), y=(0, 80), xticks=list(range(0, 101, 10)), yticks=list(range(0, 81, 10)),
              xlabel=r"v_0\ (\text{km/h})", ylabel=r"s_\text{p}\ (\text{m})",
              xfmt=lambda v: fi(v) if v % 20 == 0 else "", yfmt=lambda v: fi(v) if v % 20 == 0 else "")
    ax.curve(lambda vk: (vk / 3.6) * b + (vk / 3.6) ** 2 * k, 0, 95, INK, 2.5, dash="8 6")
    for vk, s in zip(V, SP): ax.point(vk, s)
    f.tex(ax.X(6), ax.Y(66), r"\text{kaartuu ylöspäin}", "start", MUTED)
    return f.svg()


def linear_graph():
    """fy9-sailymislait-s3 b and c: s_p / v_0 against v_0 in m/s, the points, the fitted line (solid over the data,
    dashed back to v_0 = 0), the two circled line points the slope is read from, and the intercept read at v_0 = 0."""
    k, b = _fit(X, Y)
    line = lambda v: k * v + b
    f = Fig("fy9sl-s3-lin", 440, "Kuvaaja: suure s p jaettuna v 0:lla sekunteina lähtönopeuden v 0 funktiona metreinä sekunnissa. Seitsemän "
            "mustaa pistettä nopeuksilla 8,3–25 m/s, arvot 1,50 s:sta 2,88 s:iin. Pisteisiin on sovitettu nouseva suora, jota on "
            "jatkettu katkoviivana nopeuteen nolla, jossa se leikkaa pystyakselin noin arvossa 0,86 s. Suoralta on ympyröity kaksi "
            "pistettä, (10 m/s; 1,66 s) ja (25 m/s; 2,86 s), joista luetaan kulmakerroin noin 0,080 s²/m.", size=30)
    ax = Axes(f, (96, 380), (410, 76), x=(0, 30), y=(0, 3.5), xticks=list(range(0, 31, 5)), yticks=[0.5 * i for i in range(8)],
              xlabel=r"v_0\ (\text{m/s})", ylabel=r"s_\text{p}/v_0\ (\text{s})",
              xfmt=lambda v: fi(v) if v % 10 == 0 else "", yfmt=lambda v: fi(v, 1) if abs(v - round(v)) < 1e-9 else "")
    ax.line([(X[0], line(X[0])), (X[-1], line(X[-1]))], INK, 3)
    ax.line([(0, line(0)), (X[0], line(X[0]))], INK, 2.5, dash="8 6")
    for x, y in zip(X, Y): ax.point(x, y)
    for x, y in ((10, 1.66), (25, 2.86)):
        f.circle(ax.X(x), ax.Y(y), 11, "none", INK, 1.5)
    ax.guide(10, 1.66, COLD)
    ax.guide(25, 2.86, COLD)
    f.tex(ax.X(12), ax.Y(0.55), r"t_\text{r} \approx 0{,}86\,\text{s}", "start", HEAT, bg=True)
    f.circle(ax.X(0), ax.Y(line(0)), 6, HEAT)
    f.tex(ax.X(1), ax.Y(3.25), r"k \approx 0{,}080\,\text{s}^2/\text{m}", "start")
    return f.svg()


FIGURES = {"fy9-sailymislait-s3-sp": stopping_graph, "fy9-sailymislait-s3-lin": linear_graph}
