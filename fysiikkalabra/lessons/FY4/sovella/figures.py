"""Figures of FY4 Sovella itsenäisesti (scripts/figlib.py, scripts/fbd.py); `python scripts/practice.py figures FY4` writes them
into solutions.md. The force diagram is an FBD (the object a plain rectangle, arrows to scale, physics checked as drawn),
apart from its pictorial situation picture. Velocity is blue, acceleration orange, force red and momentum purple."""
import math
from figlib import Fig, Axes, INK, MUTED, WHITE, RULE, ICE, ICE_EDGE, COLD_LIGHT, HEAT_LIGHT, SAND_LIGHT, GRAIN, IRON, ALUMINIUM, METAL_EDGE, n
from fbd import FBD, ground, open_head, VELOCITY

g = 9.81
MOMENTUM = "#7048e8"                     # momentum arrows (FY4): apart from velocity, force and acceleration
SNOW, SNOW_EDGE = "#f8fbfd", "#9fb8c8"

# fy4-s1 data (answers.py): simulated, constant acceleration plus small noise
t = list(range(9))
vA = [2.10, 2.52, 2.86, 3.31, 3.63, 4.06, 4.40, 4.86, 5.23]
vB = [1.90, 2.12, 2.42, 2.62, 2.90, 3.09, 3.40, 3.59, 3.86]


def _fit(x, y):
    mx, my = sum(x) / len(x), sum(y) / len(y)
    k = sum((a - mx) * (b - my) for a, b in zip(x, y)) / sum((a - mx) ** 2 for a in x)
    return k, my - k * mx


def wax_graph():
    """The model graph of fy4-s1: both runs as points, a straight line fitted to each, and the two points each slope is read from."""
    kA, bA = _fit(t, vA); kB, bB = _fit(t, vB)
    f = Fig("fy4-s1-graph", 430, "Kuvaaja: hiihtäjän nopeus v ajan t funktiona kahdella voiteella. Voiteen A pisteet ovat mustia ympyröitä ja "
            "voiteen B pisteet harmaita neliöitä. Kumpaankin pisteistöön on sovitettu oma nouseva suora. Voiteen A suora kulkee pisteiden "
            "(0 s; 2,10 m/s) ja (8 s; 5,22 m/s) kautta, ja sen kulmakerroin on 0,39 m/s². Voiteen B suora kulkee pisteiden (0 s; 1,90 m/s) "
            "ja (8 s; 3,86 m/s) kautta, ja sen kulmakerroin on 0,245 m/s².")
    ax = Axes(f, (80, 380), (480, 70), x=(0, 9), y=(0, 6), xticks=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], yticks=[0, 1, 2, 3, 4, 5, 6],
              xlabel=r"t\ (\text{s})", ylabel=r"v\ (\text{m/s})",
              xfmt=lambda v: str(v) if v % 2 == 0 else "")
    ax.line([(0, bA), (8.6, bA + 8.6 * kA)], INK, 2.5)
    ax.line([(0, bB), (8.6, bB + 8.6 * kB)], MUTED, 2.5, dash="9 6")
    for a, b in zip(t, vA): ax.point(a, b)
    for a, b in zip(t, vB):
        x, y = ax.X(a), ax.Y(b); f.rect(x - 6, y - 6, 12, 12, WHITE, MUTED, 2.5)
    for a, b in [(0, 2.10), (8, 5.22), (0, 1.90), (8, 3.86)]:             # the points the slopes are read from
        f.circle(ax.X(a), ax.Y(b), 11, "none", INK, 1.5)
    f.tex(ax.X(5.6), ax.Y(5.5), r"\text{voide A: } 0{,}39\,\tfrac{\text{m}}{\text{s}^2}", "end")
    f.tex(ax.X(8.9), ax.Y(2.85), r"\text{voide B: } 0{,}245\,\tfrac{\text{m}}{\text{s}^2}", "end", MUTED)
    return f.svg()


def _along(x0, y0, deg, s, h):
    """A point s along a slope that descends to the right from (x0, y0) at deg, and h above it (perpendicular)."""
    c, si = math.cos(math.radians(deg)), math.sin(math.radians(deg))
    return x0 + s * c + h * si, y0 + s * si - h * c


def _poly(f, pts, fill, edge, w=2.5):
    f.path("M" + " L".join(f"{n(a)},{n(b)}" for a, b in pts) + " Z", fill, edge, w)


def wax_fbd():
    """fy4-s1 b: the situation picture (a skier gliding down a gentle slope) and the skier's force diagram, the skier a
    rectangle on the slope. Drawn steeper and with more friction than in the task so that the arrows can be told apart."""
    deg, m, mu = 20.0, 72.0, 0.25                                # drawn values; the task's slope is 4,0° and mu ≈ 0,03
    th = math.radians(deg)
    G = m * g; N = G * math.cos(th); Fmu = mu * N; a = g * (math.sin(th) - mu * math.cos(th))
    f = Fig("fy4-s1-fbd", 400, "Kaksi kuvaa. Vasemmalla tilannekuva: hiihtäjä liukuu suorana seisten lumista rinnettä alas oikealle, ja "
            "sininen nopeusnuoli v osoittaa rinnettä alas. Oikealla hiihtäjän voimakuvio, hiihtäjä suorakulmiona rinteen suuntaisesti "
            "kallistettuna: paino G keskipisteestä suoraan alas, tukivoima N alapinnasta kohtisuoraan rinteestä ulospäin ja liikekitka "
            "alapinnan ylemmästä kulmasta rinnettä ylös. Painon komponentit katkoviivoin keskipisteestä: G x rinnettä alas ja G y "
            "kohtisuoraan rinnettä kohti; G y on yhtä pitkä kuin tukivoima ja G x pidempi kuin kitka. Erillään oranssi kiihtyvyysnuoli a "
            "rinnettä alas. Akselit: x rinnettä alas ja y kohtisuoraan rinteestä ulos. Rinne on piirretty jyrkemmäksi ja kitka "
            "suuremmaksi kuin tehtävässä, jotta nuolet erottuvat.")
    # --- the situation picture
    f.tex(140, 22, r"\text{tilannekuva}", "middle", MUTED)
    x0, y0 = 14, 170
    _poly(f, [(x0, y0), _along(x0, y0, deg, 290, 0), (x0 + 290 * math.cos(th), 380), (x0, 380)], SNOW, SNOW_EDGE, 2)
    s0 = 120                                                     # the skier's middle along the slope
    _poly(f, [_along(x0, y0, deg, s0 - 70, 2), _along(x0, y0, deg, s0 + 62, 2), _along(x0, y0, deg, s0 + 72, 9),
              _along(x0, y0, deg, s0 + 60, 7), _along(x0, y0, deg, s0 - 70, 7)], "#c92a2a", INK, 1.5)       # the skis
    f.line(*_along(x0, y0, deg, s0 - 4, 8), *_along(x0, y0, deg, s0 - 8, 62), INK, 9, cap="round")         # legs
    f.line(*_along(x0, y0, deg, s0 - 8, 62), *_along(x0, y0, deg, s0 - 4, 118), "#2f74b5", 22, cap="round")  # body
    hx, hy = _along(x0, y0, deg, s0 - 2, 140); f.circle(hx, hy, 14, HEAT_LIGHT, INK, 2)
    f.line(*_along(x0, y0, deg, s0 - 4, 104), *_along(x0, y0, deg, s0 - 46, 6), IRON, 3, cap="round")       # pole, trailing
    vx, vy = _along(x0, y0, deg, s0 + 40, 100)
    FBD(f, 1).motion(r"\overline{v}", (math.cos(th), -math.sin(th)), (vx, vy), 72, kind="velocity")
    f.line(300, 20, 300, 390, RULE, 1.5, "6 6")
    # --- the force diagram
    f.tex(450, 22, r"\text{voimakuvio}", "middle", MUTED)
    cx, cy, w, h = 440, 190, 110, 62
    tdn = (math.cos(th), -math.sin(th)); nrm = (math.sin(th), math.cos(th))      # down the slope, out of it (y up)
    bc = (cx - h / 2 * nrm[0], cy + h / 2 * nrm[1])                              # the middle of the bottom face (figure coords)
    upc = (bc[0] - w / 2 * tdn[0], bc[1] + w / 2 * tdn[1])                         # its uphill corner
    s = 0.17                                                                       # figure units per newton
    d = FBD(f, s, body=(cx, cy, w, h, -deg), m=m, a=(a * tdn[0], a * tdn[1]))
    d.force("G", (0, -G), (cx, cy), "gravity", lab=(24, 2))
    d.force("N", (N * nrm[0], N * nrm[1]), (bc[0] - 20 * tdn[0], bc[1] + 20 * tdn[1]), "normal", surface=-deg, lab=(16, -6))
    d.force("F_mu", (-Fmu * tdn[0], -Fmu * tdn[1]), upc, "friction", surface=-deg, lab=(-6, -24))
    d.component("G_x", "G", tdn, lab=(16, 18))
    d.component("G_y", "G", (-nrm[0], -nrm[1]), lab=(-26, 2))
    d.draw()
    d.motion(r"\overline{a}", tdn, (346, 330), 60)
    ax0 = (520, 92); L = 40                                                        # small axes: x down the slope, y out of it
    f.arrow(ax0[0], ax0[1], ax0[0] + L * tdn[0], ax0[1] - L * tdn[1], MUTED, 2, 10)
    f.arrow(ax0[0], ax0[1], ax0[0] + L * nrm[0], ax0[1] - L * nrm[1], MUTED, 2, 10)
    f.tex(ax0[0] + (L + 12) * tdn[0], ax0[1] - (L + 12) * tdn[1] + 4, "x", "middle", MUTED)
    f.tex(ax0[0] + (L + 12) * nrm[0], ax0[1] - (L + 12) * nrm[1], "y", "middle", MUTED)
    return f.svg()


def _car(f, x, y, w, body, label):
    """A side view of a car facing right, its bottom-left at (x, y), length w."""
    h = w * 0.30
    f.path(f"M{n(x)},{n(y - 10)} V{n(y - h * 0.62)} Q{n(x + 4)},{n(y - h * 0.70)} {n(x + w * 0.18)},{n(y - h * 0.72)} "
           f"L{n(x + w * 0.30)},{n(y - h)} H{n(x + w * 0.66)} L{n(x + w * 0.80)},{n(y - h * 0.70)} "
           f"Q{n(x + w)},{n(y - h * 0.64)} {n(x + w)},{n(y - h * 0.40)} V{n(y - 10)} Z", body, INK, 2.5)
    f.path(f"M{n(x + w * 0.33)},{n(y - h * 0.92)} H{n(x + w * 0.47)} V{n(y - h * 0.70)} H{n(x + w * 0.24)} Z", COLD_LIGHT, INK, 1.5)
    f.path(f"M{n(x + w * 0.51)},{n(y - h * 0.92)} H{n(x + w * 0.64)} L{n(x + w * 0.74)},{n(y - h * 0.70)} H{n(x + w * 0.51)} Z", COLD_LIGHT, INK, 1.5)
    for wx in (x + w * 0.20, x + w * 0.80):
        f.circle(wx, y - 8, w * 0.085, INK); f.circle(wx, y - 8, w * 0.035, ALUMINIUM, METAL_EDGE, 1.5)
    f.tex(x + w * 0.5, y - h * 0.40, label, "middle")


def _momentum(f, x, y, L, lab):
    f.line(x, y, x + L - 3, y, MOMENTUM, 4)
    open_head(f, x + L, y, 1, 0, MOMENTUM, 4, 16)
    f.tex(x + L + 10, y, lab, "start", MOMENTUM)


def collision():
    """fy4-s3 b: before and after the rear-end collision, velocities (blue) and momenta (purple) to scale; A at rest before."""
    mA, mB, vAfter = 1250.0, 1700.0, math.sqrt(2 * 0.75 * g * 4.2)
    vB = (mA + mB) * vAfter / mB
    sv, sp = 9.0, 9.0 / 1000                                                       # px per m/s, px per kg·m/s
    f = Fig("fy4-s3-collision", 420, "Kaksi tilannekuvaa. Ylhäällä ennen törmäystä: auto B tulee vasemmalta kohti paikallaan olevaa autoa A. "
            "Auton B yläpuolella sininen nopeusnuoli v B oikealle ja violetti liikemääränuoli p B oikealle; auton A nopeus on nolla. "
            "Alhaalla heti törmäyksen jälkeen: autot ovat kiinni toisissaan ja liikkuvat yhdessä oikealle. Niiden yläpuolella sininen "
            "nopeusnuoli v pilkku, joka on lyhyempi kuin v B, ja violetti liikemääränuoli p pilkku, joka on yhtä pitkä kuin p B. "
            "Positiivinen suunta on oikealle. Nuolet ovat mittakaavassa.")
    f.tex(20, 26, r"\text{ennen}", "start", MUTED)
    ground(f, 10, 590, 186)
    _car(f, 40, 186, 190, "#ffd8a8", r"\text{B}")
    _car(f, 390, 186, 170, SAND_LIGHT, r"\text{A}")
    FBD(f, 1).motion(r"\overline{v}_\text{B}", (1, 0), (60, 62), vB * sv, kind="velocity", lab=(34, -4))
    _momentum(f, 60, 98, mB * vB * sp, r"\overline{p}_\text{B}")
    f.tex(475, 92, r"v_\text{A} = 0", "middle")
    f.line(10, 214, 590, 214, RULE, 1.5, "6 6")
    f.tex(20, 238, r"\text{jälkeen}", "start", MUTED)
    ground(f, 10, 590, 396)
    _car(f, 160, 396, 190, "#ffd8a8", r"\text{B}")
    _car(f, 348, 396, 170, SAND_LIGHT, r"\text{A}")
    FBD(f, 1).motion(r"\overline{v}{}'", (1, 0), (180, 272), vAfter * sv, kind="velocity", lab=(30, -4))
    _momentum(f, 180, 308, (mA + mB) * vAfter * sp, r"\overline{p}{}'")
    f.arrow(500, 250, 570, 250, MUTED, 2, 10); f.tex(574, 250, r"+", "start", MUTED)
    return f.svg()


FIGURES = {"fy4-s1-graph": wax_graph, "fy4-s1-fbd": wax_fbd, "fy4-s3-collision": collision}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "fy4-s1-graph": "reveals: the model graph of task fy4-s1 (its solution)",
    "fy4-s1-fbd": "reveals: the model force diagram of task fy4-s1 b (its solution)",
    "fy4-s3-collision": "reveals: the momentum picture of task fy4-s3 b (its solution)",
}
