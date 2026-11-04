"""Model figures of the Tehtävät of fy9-kaasut (scripts/figlib.py, scripts/fbd.py); `python3 scripts/practice.py figures
units/fy9-kaasut` writes them into content/fi/units/fy9-kaasut/sovella/solutions.md. The data are the same as in answers.py.
Force red, acceleration orange (fbd.py)."""
from figlib import Fig, Axes, INK, MUTED, WHITE, HEAT, COLD, fi
from fbd import FBD

g = 9.81

# fy9-kaasut-s3 (answers.py): invented data, V = 37,5 ml at 0 °C and proportional to the kelvin temperature, plus noise
TH = [5, 15, 25, 35, 45, 55, 65, 75]
V = [38.2, 39.9, 41.1, 42.5, 43.8, 45.1, 46.5, 47.8]
E = 0.3                                                   # ml, the reading uncertainty the task gives
STEEP = ((15, 39.6), (75, 48.1))                          # the extreme lines through the ends of the reading ranges
FLAT = ((5, 38.5), (75, 47.5))


def _fit(x, y):
    mx, my = sum(x) / len(x), sum(y) / len(y)
    k = sum((a - mx) * (b - my) for a, b in zip(x, y)) / sum((a - mx) ** 2 for a in x)
    return k, my - k * mx


def _line(p, q):
    k = (q[1] - p[1]) / (q[0] - p[0])
    return k, p[1] - k * p[0]


def syringe_graph():
    """fy9-kaasut-s3 a: the points with their ±0,3 ml reading ranges and the fitted rising line; the two points of the
    line the slope is read from are circled. The volume axis starts at 36 ml."""
    k, b = _fit(TH, V)
    f = Fig("fy9ka-s3-graph", 360, "Kuvaaja: ruiskun ilman tilavuus V lämpötilan θ funktiona, kun θ on 0–80 °C. Pystyakseli alkaa "
            "36 millilitrasta. Kahdeksan mustaa pistettä lämpötiloissa 5, 15, …, 75 °C, ja jokaisella pystysuora epävarmuusjana "
            "±0,3 ml. Pisteisiin on sovitettu nouseva suora, joka kulkee pisteiden lomitse. Suoralta on ympyröity kaksi kaukana "
            "toisistaan olevaa pistettä, (0 °C; 37,7 ml) ja (80 °C; 48,5 ml), joista kulmakerroin luetaan: noin 0,135 ml asteelta.", width=420)
    ax = Axes(f, (62, 306), (316, 62), x=(0, 80), y=(36, 50), xticks=list(range(0, 81, 10)), yticks=list(range(36, 51, 2)),
              xlabel=r"\theta\ ({}^\circ\text{C})", ylabel=r"V\ (\text{ml})", origin_label=False,
              xfmt=lambda v: str(v) if v % 20 == 0 else "", yfmt=lambda v: str(v) if v % 4 == 0 else "")
    yb = ax.Y(36) - 12                                    # the axis break: the volume axis does not start at zero
    f.rect(ax.X(0) - 9, yb - 4, 18, 8, WHITE)
    for dy in (-4, 4): f.line(ax.X(0) - 9, yb + dy + 3, ax.X(0) + 9, yb + dy - 3, INK, 2)
    ax.line([(0, b), (80, b + 80 * k)], INK, 2.5)
    for t, v in zip(TH, V):
        f.line(ax.X(t), ax.Y(v - E), ax.X(t), ax.Y(v + E), MUTED, 2)
        for e in (-E, E): f.line(ax.X(t) - 4, ax.Y(v + e), ax.X(t) + 4, ax.Y(v + e), MUTED, 2)
        ax.point(t, v, r=4)
    for t, v in ((0, 37.7), (80, 48.5)):
        f.circle(ax.X(t), ax.Y(v), 10, "none", INK, 1.5)
    f.tex(ax.X(3), ax.Y(47.3), r"k \approx 0{,}135\,\text{ml}/{}^\circ\text{C}", "start", size=22)
    f.tex(ax.X(5), ax.Y(36.9), r"(0;\ 37{,}7)", "start", MUTED)
    f.tex(ax.X(75), ax.Y(49.4), r"(80;\ 48{,}5)", "end", MUTED)
    return f.svg()


def syringe_extrapolation():
    """fy9-kaasut-s3 b: the same line extended (dashed) down to V = 0 at about -279 °C, with the steepest and the
    shallowest line that still pass through every reading range (grey); they reach V = 0 at about -265 °C and -294 °C."""
    k, b = _fit(TH, V)
    f = Fig("fy9ka-s3-extra", 350, "Kuvaaja: sama suora koko alueella θ = −300…100 °C ja V = 0…50 ml. Mittauspisteet ovat vain "
            "alueella 5–75 °C. Sovitettua suoraa on jatkettu katkoviivana, ja se leikkaa lämpötila-akselin noin kohdassa −279 °C. "
            "Kaksi harmaata ääriviivaa, jyrkin ja loivin suora, jotka vielä kulkevat kaikkien epävarmuusjanojen kautta, leikkaavat "
            "akselin kohdissa noin −265 °C ja −294 °C. Hyväksytty arvo −273 °C on niiden välissä.", width=420)
    ax = Axes(f, (56, 300), (314, 60), x=(-300, 100), y=(0, 50), xticks=list(range(-300, 101, 50)), yticks=list(range(0, 51, 10)),
              xlabel=r"\theta\ ({}^\circ\text{C})", ylabel=r"V\ (\text{ml})", origin_label=False,
              xfmt=lambda v: (r"{-}" + str(-v) if v < 0 else str(v)) if v % 100 == 0 else "",
              yfmt=lambda v: str(v) if v % 20 == 0 else "")
    f.line(ax.X(0), ax.y0, ax.X(0), ax.y1, MUTED, 1.5)
    for (p, q) in (STEEP, FLAT):
        kk, bb = _line(p, q)
        ax.line([(-bb / kk, 0), (80, bb + 80 * kk)], MUTED, 2, dash="4 5")
    th0 = -b / k
    ax.line([(th0, 0), (5, b + 5 * k)], INK, 2.5, dash="8 6")
    ax.line([(5, b + 5 * k), (75, b + 75 * k)], INK, 3)
    for t, v in zip(TH, V): ax.point(t, v, r=4)
    f.line(ax.X(th0) + 6, ax.Y(0) - 4, ax.X(-205), ax.Y(4), HEAT, 1.5)
    f.circle(ax.X(th0), ax.Y(0), 6, HEAT, WHITE, 2)
    f.tex(ax.X(-202), ax.Y(4.5), r"\theta_0 \approx {-}279\,{}^\circ\text{C}", "start", HEAT, bg=True)
    f.tex(ax.X(-292), ax.Y(45), r"\text{ääriviivat:}", "start", MUTED)
    f.tex(ax.X(-292), ax.Y(39), r"{-}265\ \text{ja}\ {-}294\,{}^\circ\text{C}", "start", MUTED)
    return f.svg()


# fy9-kaasut-s6 (answers.py): the pane, its mass and the lift's acceleration
M6 = 2.40 * 1.20 * 0.010 * 2500          # 72,0 kg
A6 = 1.2                                 # m/s^2 upwards
MU = 0.60


def pane_horizontal():
    """fy9-kaasut-s6 a: the force diagram of the horizontal pane at the least underpressure, when the rim of the pad no
    longer presses on the glass: the weight down from the centre and the pressure-difference force up at the pad."""
    G = M6 * g; Fp = M6 * (g + A6)
    f = Fig("fy9ka-s6-vaaka", 270, "Voimakuvio: vaakasuora lasilevy kapeana suorakulmiona, kun nosto kiihtyy ylöspäin ja alipaine on "
            "pienin mahdollinen. Laikka on harmaana levyn yläpinnan keskellä. Paino G lähtee levyn keskipisteestä suoraan alas. Paine-eron voima F p lähtee levyn yläpinnasta "
            "laikan kohdalta ylös, ja se on painoa pidempi, koska levy kiihtyy ylöspäin. Laikan reunan tukivoima on tässä "
            "rajatapauksessa nolla. Erillään oranssi kiihtyvyysnuoli a ylöspäin.", width=420)
    s = 0.11
    cx, cy, w, h = 180, 135, 260, 20
    f.rect(cx - 36, cy - h / 2 - 12, 72, 12, MUTED, INK, 1.5, 4)        # the suction pad on the upper face
    f.tex(cx - 46, cy - h / 2 - 18, r"\text{laikka}", "end", MUTED, size=18)
    d = FBD(f, s, body=(cx, cy, w, h), m=M6, a=(0, A6))
    d.force("G", (0, -G), (cx, cy), "gravity", lab=(26, 4))
    d.force("F_p", (0, Fp), (cx, cy - h / 2), "other", tex=r"\overline{F}_\text{p}", lab=(30, 6))
    d.draw()
    d.motion(r"\overline{a}", (0, 1), (370, 165), 60, lab=(20, 4))
    return f.svg()


def pane_vertical():
    """fy9-kaasut-s6 b: the force diagram of the vertical pane, the pad on its left face: the outside air pushes the pane
    towards the pad (F_p), the pad's rim pushes it back (N, as large), static friction at the rim holds it up against
    the weight and gives the upward acceleration. Drawn at the least underpressure, F_mu0 = mu0 N."""
    G = M6 * g; Fmu = M6 * (g + A6); N = Fmu / MU
    f = Fig("fy9ka-s6-pysty", 400, "Voimakuvio: pystyasentoon käännetty lasilevy kapeana pystysuorana suorakulmiona, laikka levyn "
            "vasemmalla pinnalla, harmaana. Paino G keskipisteestä suoraan alas. Paine-eron voima F p työntää levyä oikealta vaakasuoraan "
            "vasemmalle kohti laikkaa. Laikan reunan tukivoima N työntää levyä vasemmalta vaakasuoraan oikealle; se on yhtä suuri "
            "kuin F p. Lepokitka F μ0 lähtee levyn vasemmasta yläkulmasta ylös, ja se on painoa pidempi, koska levy kiihtyy "
            "ylöspäin. N on noin 1,7 kertaa kitkan pituinen, koska kitka on pienimmillä alipaineella 0,60 kertaa tukivoima. "
            "Erillään oranssi kiihtyvyysnuoli a ylöspäin.", width=420)
    s = 0.085
    cx, cy, w, h = 200, 210, 24, 250
    left, right = cx - w / 2, cx + w / 2
    f.rect(left - 12, cy - 50, 12, 100, MUTED, INK, 1.5, 4)             # the suction pad on the left face
    f.tex(left - 18, cy + 66, r"\text{laikka}", "end", MUTED, size=18)
    d = FBD(f, s, body=(cx, cy, w, h), m=M6, a=(0, A6))
    d.force("G", (0, -G), (cx, cy), "gravity", lab=(28, 0))
    d.force("F_p", (-N, 0), (right, cy - 20), "other", tex=r"\overline{F}_\text{p}", push=True, lab=(24, -22))
    d.force("N", (N, 0), (left, cy + 20), "normal", surface=90, outward=(1, 0), push=True, lab=(-24, -22))
    d.force("F_mu0", (0, Fmu), (left, cy - h / 2), "friction", surface=90, outward=(1, 0), tex=r"\overline{F}_{\mu 0}", lab=(-30, 8))
    d.draw()
    d.motion(r"\overline{a}", (0, 1), (385, 265), 60, lab=(20, 4))
    return f.svg()


FIGURES = {"fy9-kaasut-s3-graph": syringe_graph, "fy9-kaasut-s3-extra": syringe_extrapolation,
           "fy9-kaasut-s6-vaaka": pane_horizontal, "fy9-kaasut-s6-pysty": pane_vertical}
