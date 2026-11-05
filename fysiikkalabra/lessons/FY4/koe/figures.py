"""Figures of the FY4 Esimerkkikoe (scripts/figlib.py, scripts/fbd.py); `python scripts/practice.py figures FY4/koe` writes the
model figures into solutions.md. The task figures fy4-k1-graphs, fy4-k1-fbd, fy4-k1-impulse and fy4-k7-pulse are shown in
the statements by their ids (fy4-koe/<name>). Every force diagram is an FBD: the object alone as a plain rectangle, forces
red, velocity blue, acceleration orange; no point-particle diagrams."""
import math
from figlib import Fig, Axes, INK, MUTED, RULE, RULE_LIGHT, COLD, COLD_LIGHT, HOT_LIGHT, fi
from fbd import FBD

g = 9.81
dec = lambda d: (lambda v: f"{v:.{d}f}".replace(".", "{,}"))


def _dir(deg): return math.cos(math.radians(deg)), math.sin(math.radians(deg))


def slope_frame(cx, cy, w, h, deg):
    """A rectangle (cx, cy, w, h) rotated deg anticlockwise (figure y down): t up the slope and nrm out of it (y up), the
    middle of its bottom face, its uphill and downhill bottom corners and the middle of its uphill face."""
    t = _dir(deg); nrm = (-t[1], t[0])
    bx, by = cx - h / 2 * nrm[0], cy + h / 2 * nrm[1]
    up = (bx + w / 2 * t[0], by - w / 2 * t[1]); down = (bx - w / 2 * t[0], by + w / 2 * t[1])
    face = (cx + w / 2 * t[0], cy - w / 2 * t[1])
    return t, nrm, (bx, by), up, down, face


# ---------------------------------------------------------------- Osa 1 task figures (no answer drawn in)
def graphs():
    """Osa 1 item a: four (t, v) graphs for a ball that rolls up a ramp, stops and rolls back (positive up the ramp)."""
    f = Fig("fy4-k1-graphs", 520, "Neljä kuvaajaa A–D, kussakin nopeus v ajan t funktiona, ja aika-akseli kulkee kohdassa v = 0. "
            "A: nopeus pienenee tasaisesti nollaan ja kasvaa sitten tasaisesti yhtä suureksi positiiviseksi arvoksi, V-kirjaimen muotoinen. "
            "B: suora alkaa positiivisesta arvosta ja laskee tasaisesti nollan läpi yhtä suureen negatiiviseen arvoon. "
            "C: alaspäin aukeava paraabeli, joka alkaa nollasta, nousee huippuun ja palaa nollaan. "
            "D: suora alkaa negatiivisesta arvosta ja nousee tasaisesti nollan läpi yhtä suureen positiiviseen arvoon.", size=28)
    f.line(300, 20, 300, 500, RULE, 1.5, "6 6"); f.line(20, 262, 580, 262, RULE, 1.5, "6 6")
    shapes = {
        "A": lambda ax: ax.line([(0.05, 1), (0.5, 0), (0.95, 1)], INK, 3.5),
        "B": lambda ax: ax.line([(0.05, 1), (0.95, -1)], INK, 3.5),
        "C": lambda ax: ax.curve(lambda t: 4 * (t - 0.05) * (0.95 - t) / 0.81, 0.05, 0.95, INK, 3.5),
        "D": lambda ax: ax.line([(0.05, -1), (0.95, 1)], INK, 3.5),
    }
    for i, (name, draw) in enumerate(shapes.items()):
        px, py = 300 * (i % 2), 262 * (i // 2)
        ax = Axes(f, (px + 62, py + 235), (px + 222, py + 75), x=(0, 1), y=(-1.25, 1.25), xticks=[], yticks=[],
                  xlabel=r"t", ylabel=r"v", grid=False, origin_label=False, x_at=0)
        draw(ax)
        f.tex(px + 14, py + 40, r"\text{" + name + "}", "start")
    return f.svg()


FB = dict(deg=25.0, G=100.0, mu=0.40)


def _slide_panel(f, px, py, mode):
    """One option of item e: a block sliding up a 25° ramp and slowing down. mode: right | push | up | vertical."""
    deg, G, mu = FB["deg"], FB["G"], FB["mu"]
    th = math.radians(deg)
    cx, cy, w, h = px + 165, py + 120, 96, 58
    t, nrm, bc, up, down, face = slope_frame(cx, cy, w, h, deg)
    N = G * math.cos(th); Fmu = mu * N
    wrong = {"right": None,
             "push": "an invented force F up the slope along the velocity: the hand no longer touches the block",
             "up": "friction points up the slope although the block slides up",
             "vertical": "the normal force is drawn vertically up instead of perpendicular to the ramp"}[mode]
    d = FBD(f, 1.0, body=(cx, cy, w, h, deg), a_dir=None if wrong else (-t[0], -t[1]), wrong=wrong)
    d.force("G", (0, -G), (cx, cy), "gravity", lab=(22, 4))
    if mode == "vertical": d.force("N", (0, N), (bc[0] + 18 * t[0], bc[1] - 18 * t[1]), "normal", surface=deg, lab=(-22, 0))
    else: d.force("N", (N * nrm[0], N * nrm[1]), (bc[0] + 18 * t[0], bc[1] - 18 * t[1]), "normal", surface=deg, lab=(-18, -10))
    if mode == "up": d.force("F_mu", (Fmu * t[0], Fmu * t[1]), up, "friction", surface=deg, lab=(18, 6))
    else: d.force("F_mu", (-Fmu * t[0], -Fmu * t[1]), down, "friction", surface=deg, lab=(-10, 22))
    if mode == "push": d.force("F", (40 * t[0], 40 * t[1]), face, "other", lab=(16, -14))
    d.draw()
    d.motion(r"\overline{v}", t, (px + 212, py + 62), 50, lab=(2, -20))


def slide():
    """Osa 1 item e: four force diagrams of a block that slides up a ramp and slows down (A right, B-D one error each)."""
    f = Fig("fy4-k1-fbd", 520, "Neljä voimakuviota A–D puupalikasta, joka liukuu ylös kaltevaa lautaa ja hidastuu. Palikka on "
            "kussakin suorakulmio kallistettuna rinteen suuntaisesti, ja sen vieressä sininen nopeusnuoli osoittaa rinnettä ylös. "
            "A: paino G keskipisteestä suoraan alas, tukivoima N alapinnasta kohtisuoraan pinnasta ulos ja kitka alapinnan alemmasta "
            "kulmasta rinnettä alas. B: samat kolme voimaa ja lisäksi voima F ylemmästä sivusta rinnettä ylös. C: paino ja tukivoima "
            "kuten A:ssa, mutta kitka alapinnan ylemmästä kulmasta rinnettä ylös. D: paino ja kitka kuten A:ssa, mutta tukivoima N "
            "osoittaa pystysuoraan ylös.", size=28)
    f.line(300, 20, 300, 500, RULE, 1.5, "6 6"); f.line(20, 262, 580, 262, RULE, 1.5, "6 6")
    for i, (name, mode) in enumerate((("A", "right"), ("B", "push"), ("C", "up"), ("D", "vertical"))):
        px, py = 300 * (i % 2), 262 * (i // 2)
        _slide_panel(f, px, py, mode)
        f.tex(px + 16, py + 32, r"\text{" + name + "}", "start")
    return f.svg()


def impulse():
    """Osa 1 item h: the force of a kick on a ball, a triangle 0 -> 1500 N at 4,0 ms -> 0 at 8,0 ms."""
    f = Fig("fy4-k1-impulse", 380, "Kuvaaja: jalan palloon kohdistama voima F newtoneina ajan t funktiona millisekunteina. Voima kasvaa "
            "tasaisesti nollasta 1500 newtoniin hetkeen 4 ms ja pienenee sitten tasaisesti nollaan hetkeen 8 ms. Kuvaaja on kolmio.")
    ax = Axes(f, (100, 330), (480, 60), x=(0, 10), y=(0, 1600), xticks=[0, 2, 4, 6, 8, 10], yticks=[0, 400, 800, 1200, 1600],
              xlabel=r"t\ (\text{ms})", ylabel=r"F\ (\text{N})")
    ax.line([(0, 0), (4, 1500), (8, 0)], INK, 3.5)
    return f.svg()


# ---------------------------------------------------------------- Osa 2 model figures
T2 = [0, 2, 4, 6, 8, 10, 12, 14]; V2 = [0.0, 1.8, 3.9, 5.7, 7.6, 7.7, 7.6, 7.6]


def tram():
    f = Fig("fy4-k2-graph", 420, "Kuvaaja: raitiovaunun nopeus v metreinä sekunnissa ajan t funktiona sekunteina. Kahdeksan mittauspistettä. "
            "Viisi ensimmäistä ovat origosta alkavalla nousevalla suoralla, joka päättyy pisteeseen (8,0 s; 7,6 m/s). Sen jälkeen pisteet "
            "ovat vaakasuoralla suoralla 7,6 m/s. Suorien ja aika-akselin väliin jäävä alue on varjostettu, ja siihen on merkitty kuljettu matka.")
    ax = Axes(f, (80, 370), (470, 70), x=(0, 16), y=(0, 10), xticks=[0, 2, 4, 6, 8, 10, 12, 14, 16], yticks=[0, 2, 4, 6, 8, 10],
              xlabel=r"t\ (\text{s})", ylabel=r"v\ (\tfrac{\text{m}}{\text{s}})")
    ax.area([(0, 0), (8, 7.6), (14, 7.6), (14, 0)], COLD_LIGHT, 0.6)
    ax.line([(0, 0), (8, 7.6), (15.5, 7.6)], INK, 3)
    ax.guide(8, 7.6)
    for t, v in zip(T2, V2): ax.point(t, v)
    f.tex(ax.X(0.4), ax.Y(9.2), r"a = \dfrac{7{,}6\,\tfrac{\text{m}}{\text{s}}}{8{,}0\,\text{s}} \approx 0{,}95\,\tfrac{\text{m}}{\text{s}^2}", "start")
    f.tex(ax.X(10.8), ax.Y(3.2), r"s \approx 76\,\text{m}", "middle", INK, bg=True)
    return f.svg()


def crate():
    """fy4-k3 a: the crate on an accelerating truck bed; static friction forward (m = 40 kg, a = 2,5 m/s² as an example)."""
    m, a = 40.0, 2.5
    G = m * g; F0 = m * a
    f = Fig("fy4-k3-fbd", 340, "Mallikuvio: laatikon voimakuvio, kun auto kiihdyttää ja laatikko pysyy lavalla paikallaan. Laatikko on "
            "suorakulmio. Keskipisteestä paino G suoraan alas ja alapinnasta tukivoima N suoraan ylös, yhtä pitkinä vierekkäin. "
            "Alapinnan etukulmasta lepokitka eteenpäin, selvästi lyhyempänä. Laatikon vieressä ohut sininen nopeusnuoli ja ohut "
            "oranssi kiihtyvyysnuoli, kumpikin eteenpäin.")
    s = 0.33
    cx, cy, w, h = 250, 170, 150, 84
    d = FBD(f, s, body=(cx, cy, w, h), m=m, a=(a, 0))
    d.force("G", (0, -G), (cx, cy), "gravity", lab=(24, -6))
    d.force("N", (0, G), (cx - 34, cy + h / 2), "normal", surface=0, lab=(-26, 6))
    d.force("F_mu0", (F0, 0), (cx + w / 2, cy + h / 2), "friction", surface=0, tex=r"\overline{F}_{\mu 0}", lab=(30, -4))
    d.draw()
    d.motion(r"\overline{v}", (1, 0), (400, 62), 80, lab=(24, 0))
    d.motion(r"\overline{a}", (1, 0), (400, 106), 80, lab=(24, 0))
    return f.svg()


# ---------------------------------------------------------------- Osa 3
T6 = [0.00, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40]
F6 = [687, 1100, 1400, 1520, 1500, 1380, 1100, 600, 0]
G6 = 687


def _spline(xs, ys):
    """A Catmull-Rom curve through the points, as a function of x (xs equally spaced)."""
    hstep = xs[1] - xs[0]
    def fn(x):
        i = min(max(int((x - xs[0]) // hstep), 0), len(xs) - 2); u = (x - xs[i]) / hstep
        p0 = ys[i - 1] if i > 0 else 2 * ys[0] - ys[1]; p1, p2 = ys[i], ys[i + 1]
        p3 = ys[i + 2] if i + 2 < len(ys) else 2 * ys[-1] - ys[-2]
        return 0.5 * (2 * p1 + (-p0 + p2) * u + (2 * p0 - 5 * p1 + 4 * p2 - p3) * u ** 2 + (-p0 + 3 * p1 - 3 * p2 + p3) * u ** 3)
    return fn


def jump():
    f = Fig("fy4-k6-graph", 440, "Kuvaaja: voimalevyn lukema F newtoneina ajan t funktiona sekunteina ponnistuksen aikana. Yhdeksän "
            "mittauspistettä on yhdistetty sileällä käyrällä: voima nousee 687 newtonista noin 1520 newtoniin hetkellä 0,15 s ja laskee "
            "nollaan hetkellä 0,40 s. Vaakasuora katkoviiva kulkee painon kohdalla 687 N. Käyrän ja katkoviivan väliin jäävä alue on "
            "varjostettu harmaalla siellä, missä voima on painoa suurempi, ja punaisella lopussa, missä voima on painoa pienempi.")
    ax = Axes(f, (100, 380), (480, 70), x=(0, 0.45), y=(0, 1600), xticks=[0, 0.1, 0.2, 0.3, 0.4], yticks=[0, 400, 800, 1200, 1600],
              xlabel=r"t\ (\text{s})", ylabel=r"F\ (\text{N})", xfmt=dec(1))
    fn = _spline(T6, F6)
    steps = [0.40 * i / 200 for i in range(201)]
    cross = next(t for t in steps if t > 0.2 and fn(t) < G6)
    ax.area([(0, G6)] + [(t, fn(t)) for t in steps if t <= cross] + [(cross, G6)], "#d5d0c4", 0.8)
    ax.area([(cross, G6)] + [(t, max(fn(t), 0)) for t in steps if t >= cross] + [(0.40, G6)], HOT_LIGHT, 0.8)
    ax.line([(0, G6), (0.44, G6)], MUTED, 2, dash="8 6")
    ax.curve(lambda t: max(fn(t), 0), 0, 0.40, INK, 3)
    for t, F in zip(T6, F6): ax.point(t, F)
    f.tex(ax.X(0.445), ax.Y(G6) - 22, r"G", "end", MUTED)
    f.tex(ax.X(0.17), ax.Y(1050), r"+", "middle")
    f.tex(ax.X(0.375), ax.Y(560), r"-", "middle")
    return f.svg()


def pulse():
    """fy4-k7 task figure: the measured acceleration of the head form, a half sine 950 m/s² peak over 9,0 ms."""
    f = Fig("fy4-k7-pulse", 420, "Kuvaaja: päämallin kiihtyvyyden suuruus a metreinä sekunnin neliössä ajan t funktiona millisekunteina "
            "iskun alusta. Kiihtyvyys kasvaa nollasta tasaisesti kaartuen huippuarvoon 950 metriä sekunnin neliössä hetkellä 4,5 ms "
            "ja pienenee samalla tavalla nollaan hetkeen 9,0 ms, minkä jälkeen se pysyy nollana. Ruudukko on millisekunnin ja "
            "sadan metrin sekunnin neliössä välein.")
    lab3 = lambda v: fi(v) if v % 3 == 0 else ""
    lab200 = lambda v: fi(v) if v % 200 == 0 else ""
    ax = Axes(f, (100, 370), (480, 70), x=(0, 12), y=(0, 1000), xticks=list(range(0, 13)), yticks=list(range(0, 1001, 100)),
              xlabel=r"t\ (\text{ms})", ylabel=r"a\ (\tfrac{\text{m}}{\text{s}^2})", xfmt=lab3, yfmt=lab200)
    ax.curve(lambda t: 950 * math.sin(math.pi * t / 9.0) if t <= 9.0 else 0.0, 0, 11.5, INK, 3.5, steps=230)
    return f.svg()


FIGURES = {"fy4-k1-graphs": graphs, "fy4-k1-fbd": slide, "fy4-k1-impulse": impulse, "fy4-k2-graph": tram, "fy4-k3-fbd": crate,
           "fy4-k6-graph": jump, "fy4-k7-pulse": pulse}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "fy4-k1-graphs": "safe",
    "fy4-k1-fbd": "safe",
    "fy4-k1-impulse": "safe",
    "fy4-k2-graph": "reveals: the model graph of exam task fy4-k2 (its solution)",
    "fy4-k3-fbd": "reveals: the model force diagram of exam task fy4-k3 (its solution)",
    "fy4-k6-graph": "reveals: the model graph of exam task fy4-k6 (its solution)",
    "fy4-k7-pulse": "safe",
}
