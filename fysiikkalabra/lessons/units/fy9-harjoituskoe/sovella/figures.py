"""Model figures of the fy9-harjoituskoe Tehtävät (scripts/figlib.py, scripts/fbd.py); `python scripts/practice.py figures
units/fy9-harjoituskoe` writes them into content/fi/units/fy9-harjoituskoe/sovella/solutions.md. The data are those of
tasks.json and answers.py. Force red, velocity blue, acceleration orange (fbd.py)."""
from figlib import Fig, Axes, INK, MUTED, COLD, HEAT, SAND_LIGHT, GRAIN, n
from fbd import FBD, ground

g = 9.81


def _fit(x, y):
    mx, my = sum(x) / len(x), sum(y) / len(y)
    k = sum((a - mx) * (b - my) for a, b in zip(x, y)) / sum((a - mx) ** 2 for a in x)
    return k, my - k * mx


def _fit0(x, y): return sum(a * b for a, b in zip(x, y)) / sum(a * a for a in x)


def dec(v, d):
    """A number with a decimal comma for a tick label."""
    return f"{v:.{d}f}".replace(".", "{,}")


def crate_fbd():
    """fy9-harjoituskoe-s2 a: the crate on the trailer bed while the trailer brakes. The crate a plain rectangle on the
    bed; weight from the centre, normal force from the bottom face, static friction from the rear bottom corner
    backwards. Drawn with a braking of 4,0 m/s² (below the limit), mass 40 kg; velocity and acceleration beside it."""
    m, a = 40.0, 4.0
    G = m * g; N = G; F = m * a
    f = Fig("fy9-harjoituskoe-s2-fbd", 330, "Voimakuvio: työkalulaatikko suorakulmiona peräkärryn vaakasuoralla lavalla, kun kärry "
            "jarruttaa ja liikkuu oikealle. Paino G osoittaa laatikon keskipisteestä suoraan alas, tukivoima N alapinnasta "
            "suoraan ylös ja on yhtä pitkä kuin paino, ja lepokitka F μ0 osoittaa alapinnan vasemmasta kulmasta vasemmalle eli "
            "taaksepäin. Laatikon yläpuolella sininen nopeusnuoli v osoittaa oikealle ja oranssi kiihtyvyysnuoli a vasemmalle.")
    cx, cy, w, h = 330, 196, 150, 90
    bottom = cy + h / 2
    ground(f, 150, 520, bottom)
    s = 0.30                                              # figure units per newton
    d = FBD(f, s, body=(cx, cy, w, h), m=m, a=(-a, 0))
    d.force("G", (0, -G), (cx, cy), "gravity", lab=(30, 0))
    d.force("N", (0, N), (cx + 40, bottom), "normal", surface=0, lab=(30, 4))
    d.force("F_mu0", (-F, 0), (cx - w / 2, bottom), "friction", surface=0, tex=r"\overline{F}_{\mu 0}", lab=(-6, -26))
    d.draw()
    d.motion(r"\overline{v}", (1, 0), (440, 40), 70, lab=(24, 0))
    d.motion(r"\overline{a}", (-1, 0), (220, 40), 60, lab=(-22, 0))
    return f.svg()


# s8: the coffee filters
M_F = 1.20e-3
N_F = [1, 2, 3, 4, 5, 6]
V_T = [1.06, 1.45, 1.84, 2.08, 2.39, 2.54]


def filters_graph():
    """fy9-harjoituskoe-s8 c and d: the drag force (= weight at terminal speed) against the square of the terminal
    speed, the six points, the line through the origin and the point of the line the slope is read from."""
    F = [k * M_F * g * 1000 for k in N_F]                 # mN
    v2 = [v ** 2 for v in V_T]
    k = _fit0(v2, F)                                      # mN s²/m²
    f = Fig("fy9-harjoituskoe-s8-graph", 430, "Kuvaaja: ilmanvastus F v millinewtoneina vakionopeuden neliön v² funktiona. Kuusi "
            "mittauspistettä välillä 1,1–6,5 m²/s² ja 12–71 mN asettuu origon kautta kulkevalle suoralle. Suoralta on luettu "
            "katkoviivoin piste (6,00 m²/s²; 64,2 mN). Kulmakerroin on noin 10,7 mN·s²/m² eli 0,0107 kg/m.")
    ax = Axes(f, (90, 380), (430, 60), x=(0, 7), y=(0, 80), xticks=[0, 1, 2, 3, 4, 5, 6, 7],
              yticks=[0, 10, 20, 30, 40, 50, 60, 70, 80], xlabel=r"v^2\ (\text{m}^2/\text{s}^2)",
              ylabel=r"F_\text{v}\ (\text{mN})", yfmt=lambda v: "" if v % 20 else str(int(v)))
    ax.line([(0, 0), (7, 7 * k)], COLD, 3)
    ax.guide(6.0, 6.0 * k)
    f.circle(ax.X(6.0), ax.Y(6.0 * k), 10, "none", INK, 1.5)
    for x, y in zip(v2, F): ax.point(x, y)
    f.tex(ax.X(6.0) - 16, ax.Y(6.0 * k) - 32, r"(6{,}00\,\text{m}^2/\text{s}^2;\ 64{,}2\,\text{mN})", "end", MUTED, size=20, bg=True)
    f.tex(ax.X(3.4), ax.Y(52), r"F_\text{v} = kv^2", "end", COLD, bg=True)
    return f.svg()


# s9: the geothermal test well
Z = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0]
T_Z = [15.4, 23.3, 32.5, 41.3, 49.2, 58.0]


def well_graph():
    """fy9-harjoituskoe-s9 a–c: rock temperature against depth, the six points, the fitted line over the measured range
    (solid) and its extrapolation to 6,0 km (dashed), the two points the slope is read from and the extrapolated value."""
    k, b = _fit(Z, T_Z)
    f = Fig("fy9-harjoituskoe-s9-graph", 430, "Kuvaaja: kallion lämpötila T celsiusasteina syvyyden z funktiona kilometreinä. Kuusi "
            "mittauspistettä syvyyksillä 0,5–3,0 km nousee suoraan 15 asteesta 58 asteeseen. Sovitettu suora alkaa "
            "pystyakselilta noin 6,7 asteesta ja on yhtenäinen mitatulla välillä ja katkoviiva syvyydestä 3 km syvyyteen 6 km, "
            "jossa se on noin 109 astetta. Suoralta luetut pisteet (0 km; 6,7 °C) ja (3,0 km; 58,0 °C) on ympyröity.")
    ax = Axes(f, (90, 380), (480, 60), x=(0, 6.5), y=(0, 120), xticks=[0, 1, 2, 3, 4, 5, 6],
              yticks=[0, 20, 40, 60, 80, 100, 120], xlabel=r"z\ (\text{km})", ylabel=r"T\ ({}^\circ\text{C})")
    ax.line([(0, b), (3.0, b + 3.0 * k)], COLD, 3)
    ax.line([(3.0, b + 3.0 * k), (6.0, b + 6.0 * k)], COLD, 3, dash="10 8")
    ax.guide(6.0, b + 6.0 * k)
    for x in (0.0, 3.0):
        f.circle(ax.X(x), ax.Y(b + k * x), 10, "none", INK, 1.5)
    for x, y in zip(Z, T_Z): ax.point(x, y)
    f.tex(ax.X(0.9), ax.Y(8), r"(0;\ 6{,}7\,{}^\circ\text{C})", "start", MUTED, size=20, bg=True)
    f.tex(ax.X(3.0) + 16, ax.Y(b + 3.0 * k) + 26, r"(3{,}0\,\text{km};\ 58{,}0\,{}^\circ\text{C})", "start", MUTED, size=20, bg=True)
    f.tex(ax.X(6.0) - 16, ax.Y(b + 6.0 * k) - 26, r"\approx 109\,{}^\circ\text{C}", "end", MUTED, size=20, bg=True)
    f.tex(ax.X(5.0), ax.Y(72), r"\text{ekstrapolaatio}", "middle", COLD, size=20, bg=True)
    return f.svg()


# s10: the spring
M_S = [0.100, 0.200, 0.300, 0.400, 0.500, 0.600]
T10 = [4.37, 5.86, 7.13, 8.19, 9.03, 9.90]


def spring_graph():
    """fy9-harjoituskoe-s10 a–c: the square of the period against the hanging mass, the six points, the fitted line
    (not forced through the origin, meeting the T² axis a little above it) and the two points the slope is read from."""
    T2 = [(t / 10) ** 2 for t in T10]
    k, b = _fit(M_S, T2)
    f = Fig("fy9-harjoituskoe-s10-graph", 430, "Kuvaaja: värähdysjakson neliö T² neliösekunteina punnuksen massan m funktiona "
            "kilogrammoina. Kuusi mittauspistettä massoilla 0,100–0,600 kg nousee suoraan. Sovitettu suora leikkaa "
            "pystyakselin hieman origon yläpuolella, noin arvossa 0,032 s². Suoralta luetut pisteet (0 kg; 0,032 s²) ja "
            "(0,600 kg; 0,979 s²) on ympyröity. Kulmakerroin on noin 1,58 s²/kg.")
    ax = Axes(f, (90, 380), (480, 60), x=(0, 0.7), y=(0, 1.2), xticks=[0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7],
              yticks=[0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2], xlabel=r"m\ (\text{kg})", ylabel=r"T^2\ (\text{s}^2)",
              xfmt=lambda v: "" if round(v * 10) % 2 else ("0" if v == 0 else dec(v, 1)),
              yfmt=lambda v: dec(v, 1))
    ax.line([(0, b), (0.7, b + 0.7 * k)], COLD, 3)
    for x in (0.0, 0.600):
        f.circle(ax.X(x), ax.Y(b + k * x), 10, "none", INK, 1.5)
    ax.guide(0.600, b + 0.600 * k)
    for x, y in zip(M_S, T2): ax.point(x, y)
    f.line(ax.X(0.0) + 10, ax.Y(b) + 2, ax.X(0.09) - 4, ax.Y(0.075), MUTED, 1.5)  # leader below the line, clear of the m = 0,1 kg point
    f.tex(ax.X(0.09), ax.Y(0.075), r"(0;\ 0{,}032\,\text{s}^2)", "start", MUTED, size=22, bg=True)
    f.tex(ax.X(0.600) - 16, ax.Y(b + 0.600 * k) - 30, r"(0{,}600\,\text{kg};\ 0{,}979\,\text{s}^2)", "end", MUTED, size=20, bg=True)
    f.tex(ax.X(0.70), ax.Y(0.30), r"\text{kulmakerroin} \approx 1{,}58\,\tfrac{\text{s}^2}{\text{kg}}", "end", COLD, bg=True)
    return f.svg()


FIGURES = {"fy9-harjoituskoe-s2-fbd": crate_fbd, "fy9-harjoituskoe-s8-graph": filters_graph,
           "fy9-harjoituskoe-s9-graph": well_graph, "fy9-harjoituskoe-s10-graph": spring_graph}
REUSE = {"fy9-harjoituskoe-s2-fbd": "reveals: the model force diagram of task fy9-harjoituskoe-s2 (its solution)",
         "fy9-harjoituskoe-s8-graph": "reveals: the model graph of task fy9-harjoituskoe-s8 (its solution)",
         "fy9-harjoituskoe-s9-graph": "reveals: the model graph of task fy9-harjoituskoe-s9 (its solution)",
         "fy9-harjoituskoe-s10-graph": "reveals: the model graph of task fy9-harjoituskoe-s10 (its solution)"}
