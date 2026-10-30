"""Figures of fy4-6 (scripts/figlib.py, scripts/fbd.py); `python scripts/figures.py fy4-6` writes them into lesson.md.
Every force diagram is an FBD: the object alone as a plain rectangle (rotated with its surface on a slope), its arrows
drawn to scale and its physics checked as it is drawn. The situation is a separate pictorial situation picture
(tilannekuva), apart behind a dashed rule; no point-particle diagrams. On a slope the components of the weight are dashed."""
import math
from figlib import (Fig, Axes, INK, MUTED, WHITE, RULE, RULE_LIGHT, SAND_LIGHT, SAND, SAND_DARK, GRAIN, COPPER, ICE, GLASS,
                    COLD, COLD_LIGHT, GOOD, GOOD_LIGHT, HOT, HOT_LIGHT, HEAT, HEAT_LIGHT, IRON, ALUMINIUM, METAL_EDGE, n, fi)
from fbd import FBD, ground, FORCE
import herolib as H
from herolib import grad, rnd

g = 9.81
BOX, BOX_EDGE = SAND_LIGHT, GRAIN                       # a cardboard box in the situation pictures
WOOD, WOOD_DARK = SAND_DARK, "#a97a35"


def _dir(deg): return math.cos(math.radians(deg)), math.sin(math.radians(deg))


def slope_frame(cx, cy, w, h, deg):
    """Points of a rectangle (cx, cy, w, h) rotated deg anticlockwise, in figure coordinates (y down): the middle of its
    bottom face, its uphill and downhill bottom corners and the middle of its uphill face; t up the slope, nrm out of it
    (both y up)."""
    t = _dir(deg); nrm = (-t[1], t[0])
    bx, by = cx - h / 2 * nrm[0], cy + h / 2 * nrm[1]
    up = (bx + w / 2 * t[0], by - w / 2 * t[1]); down = (bx - w / 2 * t[0], by + w / 2 * t[1])
    face = (cx + w / 2 * t[0], cy - w / 2 * t[1])
    return t, nrm, (bx, by), up, down, face


def box_on_slope(f, x0, y0, s, w, h, deg, fill=BOX, edge=BOX_EDGE):
    """A box of size w × h resting on a slope that starts at (x0, y0) and rises at deg; its bottom centre s along it."""
    t = _dir(deg); nrm = (-t[1], t[0])
    bx, by = x0 + s * t[0], y0 - s * t[1]
    p = [(bx - w / 2 * t[0], by + w / 2 * t[1]), (bx + w / 2 * t[0], by - w / 2 * t[1])]
    q = [(p[1][0] + h * nrm[0], p[1][1] - h * nrm[1]), (p[0][0] + h * nrm[0], p[0][1] - h * nrm[1])]
    f.path("M" + " L".join(f"{n(a)},{n(b)}" for a, b in p + q) + " Z", fill, edge, 2.5)
    # the tape across the lid
    m1 = ((p[0][0] + p[1][0]) / 2 + h * nrm[0], (p[0][1] + p[1][1]) / 2 - h * nrm[1])
    m0 = ((p[0][0] + p[1][0]) / 2 + h * 0.55 * nrm[0], (p[0][1] + p[1][1]) / 2 - h * 0.55 * nrm[1])
    f.line(m0[0], m0[1], m1[0], m1[1], edge, 2)
    return (bx + h / 2 * nrm[0], by - h / 2 * nrm[1])


def plank(f, x0, y0, L, deg, thick=12):
    """A wooden plank of length L from (x0, y0) rising at deg, its top surface on the line."""
    t = _dir(deg); nrm = (-t[1], t[0])
    x1, y1 = x0 + L * t[0], y0 - L * t[1]
    pts = [(x0, y0), (x1, y1), (x1 - thick * nrm[0], y1 + thick * nrm[1]), (x0 - thick * nrm[0], y0 + thick * nrm[1])]
    f.path("M" + " L".join(f"{n(a)},{n(b)}" for a, b in pts) + " Z", WOOD, WOOD_DARK, 2.5)
    return x1, y1


def angle_arc(f, x, y, r, a0, a1, label, lab_r=None, color=INK):
    """An arc at (x, y) from the direction a0 to a1 (degrees anticlockwise, y up) with its label."""
    p0 = (x + r * math.cos(math.radians(a0)), y - r * math.sin(math.radians(a0)))
    p1 = (x + r * math.cos(math.radians(a1)), y - r * math.sin(math.radians(a1)))
    f.path(f"M{n(p0[0])},{n(p0[1])} A{r},{r} 0 0 0 {n(p1[0])},{n(p1[1])}", "none", color, 2)
    am = math.radians((a0 + a1) / 2); R = lab_r or r + 18
    f.tex(x + R * math.cos(am), y - R * math.sin(am), label, "middle", color)


def axes_slope(f, x, y, deg, lx=r"x", ly=r"y", L=46):
    """Small axes on a slope: x down the slope, y out of the surface."""
    t = _dir(deg); nrm = (-t[1], t[0])
    f.arrow(x, y, x - L * t[0], y + L * t[1], MUTED, 2, 10); f.arrow(x, y, x + L * nrm[0], y - L * nrm[1], MUTED, 2, 10)
    f.tex(x - (L + 14) * t[0], y + (L + 14) * t[1], lx, "middle", MUTED); f.tex(x + (L + 14) * nrm[0], y - (L + 14) * nrm[1], ly, "middle", MUTED)


# ---------------------------------------------------------------- the opening illustration
def hero():
    """The chapter's opening illustration: a moving box rests on a sloping loading ramp behind a van; a mover lifts the
    ramp's foot, so the ramp gets steeper."""
    f = H.hero("fy46-hero", "Kuvitus: muuttopäivä kerrostalon pihalla. Pakettiauton takaovet ovat auki, ja auton lattialta laskeutuu "
               "puinen lastaussilta vinosti maahan. Sillan keskellä on pahvinen muuttolaatikko, joka pysyy paikallaan. Auton sisällä "
               "on lisää laatikoita, ja muuttaja kantaa yhtä laatikkoa sillan vieressä. Taivaalla olevassa pienessä kuvassa jyrkempi silta, jolla laatikko liukuu alas, ja sininen nuoli osoittaa liikkeen suunnan.")
    H.sky(f, "fy46h", 470, ICE, GLASS)
    H.sun(f, "fy46h", 1080, 90, 40, rays=False)
    H.cloud(f, 300, 90, 1.1); H.cloud(f, 760, 60, 0.8)
    # an apartment block behind the yard
    f.rect(40, 120, 470, 350, RULE_LIGHT, METAL_EDGE, 2)
    for i in range(6):
        for j in range(4):
            f.rect(70 + i * 72, 150 + j * 76, 40, 46, GLASS, METAL_EDGE, 2)
            f.line(90 + i * 72, 150 + j * 76, 90 + i * 72, 196 + j * 76, METAL_EDGE, 1.5)
    f.rect(40, 112, 470, 12, IRON)
    H.forest(f, 470, 60, 34, GOOD, seed=5, x0=500, x1=1200, depth=40)
    H.birch(f, 1150, 480, 230)
    # the yard: grass strip and asphalt
    f.rect(0, 462, 1200, 20, GOOD_LIGHT)
    f.rect(0, 480, 1200, 120, grad(f, "fy46h-asf", ALUMINIUM, METAL_EDGE))
    for k in range(18): f.path(f"M{n(rnd(k, 3) * 1200)},{n(500 + rnd(k, 7) * 90)} h22", stroke=METAL_EDGE, w=2, extra='stroke-linecap="round"')
    # the van: cargo box with the rear doors open, the cab to the right
    y_floor, x_rear = 392, 600
    f.rect(x_rear, 190, 430, 238, WHITE, INK, 3, 10)
    f.rect(x_rear + 4, 196, 92, 196, IRON)                   # the dark cargo space seen through the open rear
    for (bx, by, bw, bh) in [(612, 330, 60, 62), (648, 268, 44, 62), (612, 270, 34, 58)]:
        f.rect(bx, by, bw, bh, SAND, GRAIN, 2)
    f.rect(x_rear - 30, 196, 26, 196, GLASS, INK, 2.5, 3)       # the open door, folded back
    f.rect(1030, 262, 120, 166, WHITE, INK, 3, 10)
    f.path("M1040,272 H1110 Q1138,272 1142,330 H1040 Z", GLASS, INK, 2.5)
    f.rect(x_rear, 392, 430, 36, ALUMINIUM, INK, 2.5)
    f.rect(700, 250, 230, 50, COLD_LIGHT, None); f.rect(700, 250, 230, 50, "none", COLD, 2, 6)
    for wx in (700, 960):
        f.circle(wx, 440, 42, INK); f.circle(wx, 440, 20, ALUMINIUM, METAL_EDGE, 2)
    # the loading ramp from the van floor to the asphalt
    L = math.hypot(x_rear - 210, 500 - (y_floor + 6))
    ang = math.degrees(math.atan2(500 - (y_floor + 6), x_rear - 210))
    # the steeper case of the Miksi question, as an inset in the sky: a steeper ramp, the box slides down it (blue v, not a force)
    f.rect(540, 22, 220, 158, WHITE, INK, 2, 10)
    f.line(556, 160, 744, 160, WOOD_DARK, 3)
    a2 = 30; t2 = _dir(a2); n2 = (-t2[1], t2[0])
    plank(f, 560, 160, 170, a2, thick=9)
    box_on_slope(f, 560, 160, 112, 50, 38, a2)
    bx, by = 560 + 112 * t2[0] + 19 * n2[0] + 36 * n2[0], 160 - 112 * t2[1] - 19 * n2[1] - 36 * n2[1]
    ex, ey = bx - 56 * t2[0], by + 56 * t2[1]
    f.line(bx, by, ex, ey, "#1971c2", 4)
    hd = [(ex, ey), (ex + 14 * t2[0] + 7 * n2[0], ey - 14 * t2[1] - 7 * n2[1]), (ex + 14 * t2[0] - 7 * n2[0], ey - 14 * t2[1] + 7 * n2[1])]
    f.path("M" + " L".join(f"{n(u)},{n(w)}" for u, w in hd) + " Z", "#1971c2", None, 0)
    plank(f, 210, 500, L, ang)
    for k in range(1, 6):                                          # the grain of the wood
        tt = k / 6; x = 210 + tt * (x_rear - 210); y = 500 - tt * (500 - y_floor - 6)
        f.line(x - 30, y + 6 + 30 * math.tan(math.radians(ang)), x - 6, y + 6 + 6 * math.tan(math.radians(ang)), WOOD_DARK, 1.5)
    box_on_slope(f, 210, 500, 220, 96, 76, ang)
    # the mover beside the ramp, carrying a box
    H.person(f, 140, 540, shirt=HOT, sc=0.9, arms="down")
    f.rect(100, 400, 82, 64, SAND, GRAIN, 2.5); f.line(141, 400, 141, 430, GRAIN, 2)
    return f.svg()


# ---------------------------------------------------------------- theory figures
def kitka():
    """Ydinajatus: friction on a box on a level floor as the horizontal pull F grows (N = 100 N, mu0 = 0,50, mu = 0,35)."""
    N, mu0, mu = 100.0, 0.50, 0.35
    f = Fig("fy46-kitka", 360, "Kuvaaja mittakaavassa: vaaka-akselilla laatikkoa vetävä vaakasuora voima F newtoneina nollasta 80:een, "
            "pystyakselilla lattian kitkavoima newtoneina nollasta 60:een. Laatikkoa painaa lattiaa vasten tukivoima 100 newtonia. "
            "Aluksi kitkavoima kasvaa yhtä suureksi kuin veto: suora nousee origosta pisteeseen, jossa veto ja kitka ovat 50 newtonia. "
            "Se on lepokitkan suurin arvo, myy nolla kertaa N. Siinä laatikko lähtee liikkeelle, ja kitkavoima putoaa katkoviivaa pitkin "
            "35 newtoniin, myy kertaa N, ja pysyy siinä vedon kasvaessa.")
    ax = Axes(f, (92, 300), (496, 70), x=(0, 80), y=(0, 60), xticks=[20, 40, 60, 80], yticks=[10, 20, 30, 40, 50, 60],
              xlabel=r"F\ (\text{N})", ylabel=r"F_\mu\ (\text{N})")
    ax.line([(0, 0), (mu0 * N, mu0 * N)], HOT)
    f.line(ax.X(50), ax.Y(50), ax.X(50), ax.Y(35), HOT, 2.5, "7 5")
    ax.line([(mu0 * N, mu * N), (80, mu * N)], COLD)
    ax.point(50, 50, HOT)
    f.tex(ax.X(3), ax.Y(30), r"\text{lepokitka}", "start", HOT)
    f.tex(ax.X(55), ax.Y(42), r"\text{liikekitka}", "start", COLD)
    f.tex(ax.X(46), ax.Y(56), r"\mu_0 N", "end", HOT)
    f.tex(ax.X(68), ax.Y(29), r"\mu N", "middle", COLD)
    return f.svg()


def kuorma():
    """Ydinajatus, example J: a box on the bed of a pickup that speeds up; static friction pushes the box forward."""
    m, a = 20.0, 2.0
    f = Fig("fy46-kuorma", 360, "Kaksi kuvaa. Vasemmalla tilannekuva: avolava-auto lähtee liikkeelle oikealle ja kiihtyy, ja sen lavalla "
            "on laatikko, joka ei liu'u lavalla. Laatikon yllä ohut oranssi nuoli a osoittaa oikealle. Oikealla laatikon voimakuvio "
            "suorakulmiona: paino G keskipisteestä alas, lavan tukivoima N alapinnasta ylös ja yhtä pitkä kuin paino, ja lavan "
            "kitkavoima alapinnan etukulmasta oikealle eli liikkeen suuntaan. Kitkavoima on paljon lyhyempi kuin paino.")
    f.tex(150, 22, r"\text{tilannekuva}", "middle", MUTED)
    ground(f, 14, 286, 268)
    # the pickup: cab right, bed left, wheels
    f.path("M30,200 H196 V160 Q200,146 214,146 H246 Q262,148 270,176 L282,200 V236 H30 Z", COLD_LIGHT, INK, 2.5)
    f.path("M206,156 H240 Q252,158 258,186 H206 Z", GLASS, INK, 2)
    f.line(196, 200, 196, 236, INK, 2)
    for wx in (76, 232):
        f.circle(wx, 246, 21, INK); f.circle(wx, 246, 9, ALUMINIUM, METAL_EDGE, 1.5)
    f.rect(84, 150, 70, 50, BOX, BOX_EDGE, 2.5); f.line(119, 150, 119, 172, BOX_EDGE, 2)
    FBD(f, 1).motion(r"\overline{a}", (1, 0), (84, 112), 70)
    f.line(300, 20, 300, 340, RULE, 1.5, "6 6")
    f.tex(450, 22, r"\text{voimakuvio}", "middle", MUTED)
    cx, cy, w, h = 410, 186, 90, 64
    G = m * g
    d = FBD(f, 0.72, body=(cx, cy, w, h), m=m, a=(a, 0))
    d.force("G", (0, -G), (cx, cy), "gravity", lab=(22, -4))
    d.force("N", (0, G), (cx - 20, cy + h / 2), "normal", surface=0, lab=(-24, 6))
    d.force("F_mu", (m * a, 0), (cx + w / 2, cy + h / 2), "friction", surface=0, lab=(4, 22))
    d.draw()
    d.motion(r"\overline{a}", (1, 0), (cx + w / 2 + 34, cy - 30), 60)
    return f.svg()


def kalteva(deg=30.0, name="kalteva"):
    """Kaava: a box at rest on a slope, the situation picture and the force diagram with the weight's components dashed."""
    G = 100.0
    f = Fig("fy46-" + name, 380, "Kaksi kuvaa. Vasemmalla tilannekuva: laatikko on paikallaan puisella lankulla, joka nousee oikealle "
            "kulmassa alfa vaakatasoon nähden. Oikealla laatikon voimakuvio, laatikko kallistettuna suorakulmiona kuten lankulla: "
            "paino G keskipisteestä suoraan alas, tukivoima N alapinnasta kohtisuoraan pintaa vastaan ulospäin ja lepokitka alapinnan "
            "ylemmästä kulmasta pinnan suuntaisesti ylös rinnettä. Painon komponentit on piirretty katkoviivoin keskipisteestä: "
            "G x rinnettä alas ja G y kohtisuoraan pintaa kohti. Painon ja komponentin G y välinen kulma on alfa. Komponentti G y on "
            "yhtä pitkä kuin tukivoima ja G x yhtä pitkä kuin kitkavoima.")
    f.tex(130, 22, r"\text{tilannekuva}", "middle", MUTED)
    x0, y0 = 22, 300
    f.rect(214, 300 - 128, 30, 128, WOOD, WOOD_DARK, 2.5)            # the support under the plank's upper end
    ground(f, 12, 262, 312)
    plank(f, x0, y0, 250, deg)
    box_on_slope(f, x0, y0, 130, 70, 52, deg)
    angle_arc(f, x0, y0, 56, 0, deg, r"\alpha", lab_r=74)
    f.line(x0, y0, x0 + 80, y0, MUTED, 1.5, "4 4")
    f.line(270, 20, 270, 360, RULE, 1.5, "6 6")
    f.tex(440, 22, r"\text{voimakuvio}", "middle", MUTED)
    cx, cy, w, h = 430, 168, 96, 64
    t, nrm, bc, up, down, face = slope_frame(cx, cy, w, h, deg)
    s = 1.3
    th = math.radians(deg)
    d = FBD(f, s, body=(cx, cy, w, h, deg), a_dir=(0, 0))
    d.force("G", (0, -G), (cx, cy), "gravity", lab=(-14, 20))
    d.force("N", (G * math.cos(th) * nrm[0], G * math.cos(th) * nrm[1]), (bc[0] + 18 * t[0], bc[1] - 18 * t[1]), "normal", surface=deg, lab=(-10, -12))
    d.force("F_mu", (G * math.sin(th) * t[0], G * math.sin(th) * t[1]), up, "friction", surface=deg, lab=(18, 6))
    d.component("G_x", "G", (-t[0], -t[1]), lab=(-22, 6))
    d.component("G_y", "G", (t[1], -t[0]), lab=(26, 4))
    d.draw()
    angle_arc(f, cx, cy, 44, -90, -90 + deg, r"\alpha", lab_r=58)
    return f.svg()


EX = dict(m=18.0, deg=25.0, mu=0.30)       # the worked example's data (lesson-answers.py computes the same)


def esimerkki():
    """The worked example's force diagram: a box sliding down a 25° ramp, mu = 0,30, 18 kg; x down the slope, y out of it."""
    m, deg, mu = EX["m"], EX["deg"], EX["mu"]
    th = math.radians(deg); G = m * g; N = G * math.cos(th); Fmu = mu * N; a = g * (math.sin(th) - mu * math.cos(th))
    f = Fig("fy46-esimerkki", 420, "Laatikon voimakuvio, laatikko suorakulmiona kallistettuna 25 asteen rinteen suuntaisesti. Paino G "
            "keskipisteestä suoraan alas. Tukivoima N alapinnasta kohtisuoraan pintaa vastaan ulospäin. Liikekitka alapinnan ylemmästä "
            "kulmasta rinnettä ylös, koska laatikko liukuu alas. Painon komponentit katkoviivoin keskipisteestä: G x rinnettä alas ja "
            "G y kohtisuoraan pintaa kohti. G x on pidempi kuin kitkavoima. Erillään ohut oranssi kiihtyvyysnuoli a rinnettä alas. "
            "Nurkassa akselit: x rinnettä alas ja y kohtisuoraan pinnasta ulos.")
    cx, cy, w, h = 300, 170, 130, 76
    t, nrm, bc, up, down, face = slope_frame(cx, cy, w, h, deg)
    s = 0.95
    d = FBD(f, s, body=(cx, cy, w, h, deg), m=m, a=(-a * t[0], -a * t[1]))
    d.force("G", (0, -G), (cx, cy), "gravity", lab=(-16, 18))
    d.force("N", (N * nrm[0], N * nrm[1]), (bc[0] + 18 * t[0], bc[1] - 18 * t[1]), "normal", surface=deg, lab=(-12, -12))
    d.force("F_mu", (Fmu * t[0], Fmu * t[1]), up, "friction", surface=deg, lab=(18, 8))
    d.component("G_x", "G", (-t[0], -t[1]), lab=(-20, 10))
    d.component("G_y", "G", (t[1], -t[0]), lab=(28, 2))
    d.draw()
    d.motion(r"\overline{a}", (-t[0], -t[1]), (120, 120), 70)
    angle_arc(f, cx, cy, 60, -90, -90 + deg, r"25^\circ", lab_r=84)
    axes_slope(f, 520, 330, deg)
    return f.svg()


# ---------------------------------------------------------------- task figures (shown by id from inquiry.json and exercises.json)
def virhe():
    """Find the error: a box sliding down a slope with friction, its normal force drawn vertically up (the error)."""
    deg, G, mu = 30.0, 100.0, 0.30
    th = math.radians(deg)
    f = Fig("fy46-virhe", 340, "Opiskelijan piirtämä voimakuvio rinnettä alas liukuvasta laatikosta, laatikko suorakulmiona kallistettuna "
            "rinteen suuntaisesti. Keskipisteestä nuoli G suoraan alas. Alapinnasta nuoli N suoraan ylös, pystysuoraan. Alapinnan "
            "ylemmästä kulmasta nuoli rinteen suuntaisesti ylös rinnettä.")
    cx, cy, w, h = 300, 170, 110, 66
    t, nrm, bc, up, down, face = slope_frame(cx, cy, w, h, deg)
    d = FBD(f, 1.3, body=(cx, cy, w, h, deg), wrong="the normal force is drawn vertically up instead of perpendicular to the slope (the error to find)")
    d.force("G", (0, -G), (cx, cy), "gravity", lab=(22, 10))
    d.force("N", (0, G * math.cos(th)), (bc[0] + 18 * t[0], bc[1] - 18 * t[1]), "normal", surface=deg, lab=(-22, 0))
    d.force("F_mu", (mu * G * math.cos(th) * t[0], mu * G * math.cos(th) * t[1]), up, "friction", surface=deg, lab=(16, 10))
    d.draw()
    return f.svg()


VALITSE = ("Laatikon voimakuvio, laatikko suorakulmiona kallistettuna rinteen suuntaisesti. ")


def _valitse(name, desc, wrong=None, fr=1, g_perp=False, no_friction=False):
    """An option of the diagram-selection task: a box at rest on a 30° slope."""
    deg, G = 30.0, 80.0
    th = math.radians(deg)
    f = Fig(f"fy46-valitse-{name}", 300, desc, width=300)
    cx, cy, w, h = 150, 140, 90, 56
    t, nrm, bc, up, down, face = slope_frame(cx, cy, w, h, deg)
    d = FBD(f, 1.15, body=(cx, cy, w, h, deg), a_dir=None if wrong else (0, 0), wrong=wrong)
    if g_perp: d.force("G", (-G * nrm[0], -G * nrm[1]), (cx, cy), "gravity", lab=(22, 14))
    else: d.force("G", (0, -G), (cx, cy), "gravity", lab=(-14, 18))
    d.force("N", (G * math.cos(th) * nrm[0], G * math.cos(th) * nrm[1]), (bc[0] + 18 * t[0], bc[1] - 18 * t[1]), "normal", surface=deg, lab=(-10, -12))
    if not no_friction:
        if fr > 0: d.force("F_mu", (G * math.sin(th) * t[0], G * math.sin(th) * t[1]), up, "friction", surface=deg, lab=(16, 8))
        else: d.force("F_mu", (-G * math.sin(th) * t[0], -G * math.sin(th) * t[1]), down, "friction", surface=deg, lab=(-18, -6))
    d.draw()
    return f.svg()


def valitse_a():
    return _valitse("a", VALITSE + "Paino G keskipisteestä suoraan alas, tukivoima N alapinnasta kohtisuoraan pintaa vastaan ulospäin ja kitkavoima "
                    "alapinnan ylemmästä kulmasta rinnettä ylös.")


def valitse_b():
    return _valitse("b", VALITSE + "Paino G keskipisteestä suoraan alas, tukivoima N alapinnasta kohtisuoraan pintaa vastaan ulospäin ja kitkavoima "
                    "alapinnan alemmasta kulmasta rinnettä alas.", wrong="friction points down the slope although the box tends to slide down", fr=-1)


def valitse_c():
    return _valitse("c", VALITSE + "Paino G keskipisteestä suoraan alas ja tukivoima N alapinnasta kohtisuoraan pintaa vastaan ulospäin. "
                    "Muita nuolia ei ole.", wrong="friction is missing, so the forces do not cancel", no_friction=True)


def valitse_d():
    return _valitse("d", VALITSE + "Paino G keskipisteestä kohtisuoraan rinnettä kohti, tukivoima N alapinnasta kohtisuoraan pintaa vastaan "
                    "ulospäin ja kitkavoima alapinnan ylemmästä kulmasta rinnettä ylös.", wrong="the weight is drawn perpendicular to the slope instead of vertically down", g_perp=True)


def malli_veto():
    """Model diagram for the drawing task: a box pulled up a 20° slope at constant velocity by a rope along the slope, mu = 0,25."""
    m, deg, mu = 20.0, 20.0, 0.25
    th = math.radians(deg); G = m * g; N = G * math.cos(th); Fmu = mu * N; T = G * math.sin(th) + Fmu
    f = Fig("fy46-malli-veto", 380, "Mallikuvio: laatikkoa vedetään köydellä ylös rinnettä tasaisella nopeudella, köysi rinteen suuntainen. "
            "Kuviossa on vain laatikko suorakulmiona kallistettuna rinteen suuntaisesti. Paino G keskipisteestä suoraan alas. Tukivoima N "
            "alapinnasta kohtisuoraan pintaa vastaan ulospäin. Köyden jännitysvoima T ylemmän sivun keskeltä rinnettä ylös. Liikekitka "
            "alapinnan alemmasta kulmasta rinnettä alas, koska laatikko liukuu ylös. Painon komponentit katkoviivoin. Erillään ohut "
            "sininen nopeusnuoli v rinnettä ylös. Nurkassa akselit: x rinnettä ylös ja y kohtisuoraan pinnasta ulos.")
    cx, cy, w, h = 280, 170, 110, 64
    t, nrm, bc, up, down, face = slope_frame(cx, cy, w, h, deg)
    s = 0.9
    d = FBD(f, s, body=(cx, cy, w, h, deg), a_dir=(0, 0))
    d.force("G", (0, -G), (cx, cy), "gravity", lab=(-16, 18))
    d.force("N", (N * nrm[0], N * nrm[1]), (bc[0] + 10 * t[0], bc[1] - 10 * t[1]), "normal", surface=deg, lab=(-18, -4))
    d.force("T", (T * t[0], T * t[1]), face, "tension", rope=t, lab=(14, -16))
    d.force("F_mu", (-Fmu * t[0], -Fmu * t[1]), down, "friction", surface=deg, lab=(-6, 24))
    d.component("G_x", "G", (-t[0], -t[1]), lab=(-22, -14))
    d.component("G_y", "G", (t[1], -t[0]), lab=(28, 2))
    d.draw()
    d.motion(r"\overline{v}", t, (450, 262), 60)
    # axes: x up the slope, y out of the surface
    ax, ay, L = 60, 340, 46
    f.arrow(ax, ay, ax + L * t[0], ay - L * t[1], MUTED, 2, 10); f.arrow(ax, ay, ax + L * nrm[0], ay - L * nrm[1], MUTED, 2, 10)
    f.tex(ax + (L + 14) * t[0], ay - (L + 14) * t[1], "x", "middle", MUTED); f.tex(ax + (L + 14) * nrm[0], ay - (L + 14) * nrm[1], "y", "middle", MUTED)
    return f.svg()


MITTAUS = [(5.0, 1.1), (10.0, 2.1), (15.0, 3.3), (20.0, 4.2), (25.0, 5.4)]   # answers.py uses the same points


def mittaus():
    """Exercise L2-03: measured kinetic friction against the normal force (points only; the student fits the line)."""
    f = Fig("fy46-mittaus", 340, "Kuvaaja mittakaavassa, esimerkkiaineisto. Vaaka-akselilla tukivoima N newtoneina nollasta 30:een, "
            "pystyakselilla kitkavoima newtoneina nollasta 7:ään. Viisi mittauspistettä: tukivoimalla 5 newtonia kitkavoima on 1,1 "
            "newtonia, 10 newtonilla 2,1, 15 newtonilla 3,3, 20 newtonilla 4,2 ja 25 newtonilla 5,4 newtonia. Suoraa ei ole piirretty.")
    ax = Axes(f, (92, 290), (496, 60), x=(0, 30), y=(0, 7), xticks=[5, 10, 15, 20, 25, 30], yticks=[1, 2, 3, 4, 5, 6, 7],
              xlabel=r"N\ (\text{N})", ylabel=r"F_\mu\ (\text{N})")
    for p in MITTAUS: ax.point(*p, COLD)
    return f.svg()


FIGURES = {"hero": hero, "kitka": kitka, "kuorma": kuorma, "kalteva-ydin": lambda: kalteva(40.0, "kalteva-ydin"), "kalteva": kalteva, "esimerkki": esimerkki,
           "virhe": virhe, "valitse-a": valitse_a, "valitse-b": valitse_b, "valitse-c": valitse_c, "valitse-d": valitse_d,
           "malli-veto": malli_veto, "mittaus": mittaus}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "hero": "decorative",
    "kitka": "reveals: static friction growing with the pull up to mu0 N, then kinetic friction mu N (a theory graph)",
    "kuorma": "reveals: static friction pointing forward on a box on an accelerating truck bed (a theory figure)",
    "kalteva-ydin": "reveals: the force diagram of a box at rest on a 40° slope with the weight's components (a theory figure)",
    "kalteva": "reveals: the force diagram of a box at rest on a slope with the weight's components (a theory figure)",
    "esimerkki": "reveals: the force diagram of the worked example (box sliding down a 25° ramp)",
    "virhe": "safe: a deliberately wrong diagram (normal force vertical on a slope) for error-finding; its description lists the arrows, not the error",
    "valitse-a": "reveals: the right diagram for a box at rest on a slope (an option figure)",
    "valitse-b": "safe: a wrong option (friction down the slope) for diagram selection",
    "valitse-c": "safe: a wrong option (friction missing) for diagram selection",
    "valitse-d": "safe: a wrong option (weight perpendicular to the slope) for diagram selection",
    "malli-veto": "reveals: the model diagram of a box pulled up a slope at constant velocity (shown after the attempt)",
    "mittaus": "safe: measured friction against normal force, points only, no fitted line",
}
