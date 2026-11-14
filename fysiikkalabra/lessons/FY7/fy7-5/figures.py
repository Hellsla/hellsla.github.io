"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy7-5` writes them into lesson.md.
FY7 colours (course brief): force #c92a2a, velocity #1971c2, current #7048e8, magnetic field and flux #2b8a3e, electric
field #8a5f22, N pole #f2a69c, S pole #d0e6fb, field into the page a cross. The induced voltage e is drawn in ink."""
import math
from figlib import (Fig, Axes, fi, INK, MUTED, WHITE, RULE, RULE_LIGHT, HOT, HOT_LIGHT, HEAT, HEAT_LIGHT, COLD, COLD_LIGHT,
                    GOOD, GOOD_LIGHT, IRON, COPPER, ALUMINIUM, METAL_EDGE, SAND, SAND_LIGHT, SAND_DARK, GRAIN, GLASS, PAPER, n)
import herolib as H

FORCE, VEL, CURRENT, FIELD, EFIELD, NPOLE, SPOLE = HOT, COLD, "#7048e8", GOOD, "#8a5f22", HOT_LIGHT, COLD_LIGHT

# the coil of the Kaava graph and of the simulation: N = 10 turns, a square 0,10 m × 0,10 m, B = 0,20 T, v = 0,10 m/s,
# a field region 0,20 m wide; the leading side reaches the field at t = 0,5 s (lesson-answers.py sim-*)
N_COIL, B_COIL, SIDE, V_COIL, D_FIELD, X_START = 10, 0.20, 0.10, 0.10, 0.20, -0.05


def cross(f, x, y, r=8, colour=FIELD, w=2.5):
    """The field into the page: a cross."""
    d = r * 0.75
    f.line(x - d, y - d, x + d, y + d, colour, w, cap="round"); f.line(x + d, y - d, x - d, y + d, colour, w, cap="round")


def bar_magnet(f, x, y, w, h, north_right=True):
    """A bar magnet from the side: two halves, N in the pole colour with its letter."""
    left, right = ("S", "N") if north_right else ("N", "S")
    for k, (x0, p) in enumerate(((x, left), (x + w / 2, right))):
        f.rect(x0, y, w / 2, h, NPOLE if p == "N" else SPOLE, INK, 2.5, 3)
        f.tex(x0 + w / 4, y + h / 2, r"\text{" + p + "}", "middle")


def coil_side(f, x0, x1, cy, ry, turns, w=3):
    """A coil with its axis horizontal: each turn an upright ellipse in copper."""
    step = (x1 - x0) / (turns - 1)
    for k in range(turns):
        f.add(f'<ellipse cx="{n(x0 + k * step)}" cy="{n(cy)}" rx="7" ry="{n(ry)}" fill="none" stroke="{COPPER}" stroke-width="{w:g}"/>')


def meter(f, cx, cy, r, angle):
    """An analogue voltmeter face with its needle turned by angle degrees from the zero mark at the top."""
    f.circle(cx, cy, r, WHITE, INK, 2.5)
    px, py = cx, cy + r * 0.45
    for a in range(-50, 51, 25):
        t = math.radians(a)
        f.line(px + r * 0.72 * math.sin(t), py - r * 0.72 * math.cos(t), px + r * 0.86 * math.sin(t), py - r * 0.86 * math.cos(t),
               INK if a == 0 else MUTED, 2)
    t = math.radians(angle)
    f.line(px, py, px + r * 0.8 * math.sin(t), py - r * 0.8 * math.cos(t), HOT, 2.5, cap="round")
    f.circle(px, py, 4, INK)


def faraday():
    f = Fig("fy75-faraday", 340, "Periaatekuva, ei mittakaavassa: Faradayn koe kolmessa vaiheessa. Jokaisessa kuvassa "
            "johdinkäämi on kytketty jännitemittariin. Vasemmalla sauvamagneetti työnnetään pohjoisnapa edellä kohti käämiä "
            "ja käämin sisään, ja mittarin neula kääntyy oikealle. Keskellä magneetti on paikallaan käämin sisällä, ja neula "
            "on nollassa. Oikealla magneetti vedetään käämistä pois, ja neula kääntyy vasemmalle.")
    for k, (title, mx, v, needle) in enumerate(((r"\text{sisään}", 10, 1, 34), (r"\text{paikallaan}", 72, 0, 0),
                                               (r"\text{ulos}", 10, -1, -34))):
        ox = 200 * k
        f.tex(ox + 100, 30, title, "middle")
        meter(f, ox + 146, 112, 40, needle)
        cy = 262
        # leads from the coil's ends up to the meter
        f.path(f"M{ox + 112},{cy + 30} C{ox + 104},{cy + 56} {ox + 96},{cy - 60} {ox + 128},{150}", stroke=INK, w=2)
        f.path(f"M{ox + 182},{cy + 30} C{ox + 192},{cy + 56} {ox + 192},{cy - 60} {ox + 164},{150}", stroke=INK, w=2)
        bar_magnet(f, ox + mx, cy - 16, 84, 32)
        coil_side(f, ox + 112, ox + 182, cy, 30, 6)
        if v:
            x1, x2 = (ox + 18, ox + 86) if v > 0 else (ox + 86, ox + 18)
            f.arrow(x1, 212, x2, 212, VEL, 3.5, 14)
            f.tex(ox + 52, 186, r"\overline{v}", "middle", VEL)
        if k < 2: f.line(ox + 200, 20, ox + 200, 320, RULE, 2, "6 6")
    return f.svg()


def flux():
    f = Fig("fy75-flux", 340, "Periaatekuva sivulta, kolme osaa: vaakasuorat vihreät kenttäviivat osoittavat vasemmalta "
            "oikealle, ja johdinsilmukka nähdään syrjästä kapeana soikiona. Vasemmalla silmukan taso on kohtisuorassa kenttää "
            "vastaan, ja viisi kenttäviivaa kulkee silmukan läpi: vuo on B kertaa A. Keskellä silmukka on vinossa, ja sen läpi "
            "kulkee vain kolme viivaa: vuo on pienempi. Oikealla silmukan taso on kentän suuntainen, eikä yksikään viiva kulje "
            "sen läpi: vuo on nolla.")
    ys = [78 + 30 * k for k in range(7)]
    for k, (tilt, label) in enumerate(((0, r"\Phi = BA"), (55, r"\Phi < BA"), (90, r"\Phi = 0"))):
        ox, cx, cy = 200 * k, 200 * k + 100, 183 if tilt == 90 else 168     # the parallel loop lies between two lines
        for y in ys:
            f.line(ox + 18, y, ox + 182, y, FIELD, 2)
            f.path(f"M{ox + 166},{y} l-12,-6 v12 Z", FIELD)
        f.add(f'<ellipse cx="{cx}" cy="{cy}" rx="13" ry="76" fill="{GOOD_LIGHT}" fill-opacity="0.35" stroke="{COPPER}" '
              f'stroke-width="5" transform="rotate({-tilt} {cx} {cy})"/>')
        f.tex(cx, 300, label, "middle")
        if k < 2: f.line(ox + 200, 30, ox + 200, 320, RULE, 2, "6 6")
    f.tex(28, 40, r"\overline{B}", "start", FIELD)
    f.tex(100, 40, r"A", "middle")
    return f.svg()


def coil_overlap(t, v=V_COIL):
    """The part of the coil's length (m) inside the field at time t (the leading side starts at X_START)."""
    x = X_START + v * t
    return max(0.0, min(x, D_FIELD) - max(x - SIDE, 0.0))


def graph():
    f = Fig("fy75-graph", 380, "Kaksi kuvaajaa mittakaavassa samalla aika-akselilla nollasta neljään sekuntiin. Kymmenen "
            "kierroksen neliön muotoinen käämi, sivu 0,10 m, kulkee vauhdilla 0,10 m/s magneettikentän 0,20 T alueen läpi. "
            "Ylempi kuvaaja: magneettivuo millivebereinä on nolla 0,5 sekuntiin asti, kasvaa tasaisesti arvoon 2,0 hetkellä "
            "1,5 s, pysyy vakiona 2,5 sekuntiin ja pienenee tasaisesti nollaan hetkellä 3,5 s. Alempi kuvaaja: "
            "induktiojännite millivoltteina on nolla, kun vuo ei muutu, miinus 20 vuon kasvaessa ja plus 20 vuon pienentyessä. "
            "Katkoviivat hetkillä 0,5; 1,5; 2,5 ja 3,5 s yhdistävät kuvaajat. Kuvan oikeassa yläkulmassa on merkintä "
            "N = 10 kierrosta.")
    T = 4.0
    top = Axes(f, (96, 150), (500, 70), x=(0, 4.5), y=(0, 2.5), xticks=[0.5 * k for k in range(1, 10)],
               yticks=[0.5 * k for k in range(1, 6)], xlabel=r"t\ (\text{s})", ylabel=r"\Phi\ (\text{mWb})",
               xfmt=lambda v: "", yfmt=lambda v: fi(v) if abs(v - round(v)) < 1e-9 else "", origin_label=False)
    bot = Axes(f, (96, 332), (500, 212), x=(0, 4.5), y=(-30, 30), xticks=[0.5 * k for k in range(1, 10)],
               yticks=[-20, -10, 10, 20], xlabel=r"t\ (\text{s})", ylabel=r"e\ (\text{mV})", x_at=0,
               xfmt=lambda v: "", yfmt=lambda v: fi(v) if abs(v) == 20 else "")
    f.tex(86, 150, "0", "end")
    f.tex(86, bot.Y(0), "0", "end")
    f.tex(588, 34, r"N = %d\ \text{kierrosta}" % N_COIL, "end")   # the turns explain 2 mWb/s → 20 mV
    for tt in (0.5, 1.5, 2.5, 3.5):           # the boundary moments through both graphs
        f.line(top.X(tt), top.Y(2.5), top.X(tt), bot.Y(-30), MUTED, 1.5, "6 5")
    for k in range(1, 9):                     # the time numbers once, under the lower graph
        if k % 2 == 0: f.tex(bot.X(0.5 * k), 354, fi(0.5 * k), "middle")
    phi = lambda t: B_COIL * SIDE * coil_overlap(t) * 1e3
    top.line([(t, phi(t)) for t in (0, 0.5, 1.5, 2.5, 3.5, T)], FIELD, 3)
    e = -N_COIL * B_COIL * SIDE * V_COIL * 1e3                 # −20 mV while entering, +20 mV while leaving
    bot.line([(0, 0), (0.5, 0), (0.5, e), (1.5, e), (1.5, 0), (2.5, 0), (2.5, -e), (3.5, -e), (3.5, 0), (T, 0)], INK, 3)
    return f.svg()


def rod():
    f = Fig("fy75-rod", 360, "Periaatekuva ylhäältä, ei mittakaavassa: kaksi vaakasuoraa metallikiskoa, joiden vasemmat päät "
            "on yhdistetty jännitemittariin. Kiskojen päällä on pystysuora kuparitanko, joka liikkuu oikealle nopeudella v. "
            "Magneettikenttä osoittaa paperiin päin, mitä kuvaavat tasavälein piirretyt vihreät ristit. Tangon keskellä on "
            "elektroni, johon magneettinen voima osoittaa alaspäin ja sähköinen voima ylöspäin. Elektroneja on kertynyt tangon "
            "alapäähän, joka on negatiivinen, ja yläpää on positiivinen. Tangossa sähkökenttä osoittaa ylhäältä alas. Kiskojen "
            "välinen etäisyys eli tangon kenttään kuuluva pituus on l.")
    ytop, ybot = 96, 264
    for y in (ytop, ybot):
        f.rect(70, y - 6, 450, 12, ALUMINIUM, INK, 2, 3)
    # the voltmeter across the rails' left ends
    f.line(70, ytop, 52, ytop, INK, 2.5); f.line(70, ybot, 52, ybot, INK, 2.5)
    f.line(52, ytop, 52, 154, INK, 2.5); f.line(52, 206, 52, ybot, INK, 2.5)
    f.circle(52, 180, 26, WHITE, INK, 2.5)
    f.tex(52, 180, r"\text{V}", "middle")
    for x in (120, 180, 230):
        for y in (130, 180, 230):
            cross(f, x, y)
    for x in (440, 490):
        for y in (130, 180, 230):
            cross(f, x, y)
    f.tex(500, 52, r"\overline{B}", "middle", FIELD)
    # the rod, its charges and the field inside it
    rx = 330
    f.rect(rx - 7, ytop - 16, 14, ybot - ytop + 32, COPPER, INK, 2, 3)
    f.tex(rx + 18, ytop - 22, "+", "start")
    f.tex(rx + 18, ybot + 22, "-", "start")
    f.arrow(290, 124, 290, 236, EFIELD, 3, 13)
    f.tex(280, 180, r"\overline{E}", "end", EFIELD)
    f.arrow(rx, 192, rx, 238, FORCE, 3.5, 13)
    f.arrow(rx, 168, rx, 122, FORCE, 3.5, 13)
    f.circle(rx, 180, 9, WHITE, INK, 2)
    f.line(rx - 4.5, 180, rx + 4.5, 180, INK, 2)
    f.tex(rx + 18, 226, r"\overline{F}_\text{m}", "start", FORCE)
    f.tex(rx + 18, 134, r"\overline{F}_\text{s}", "start", FORCE)
    f.arrow(rx - 30, 40, rx + 50, 40, VEL, 3.5, 14)
    f.tex(rx + 60, 40, r"\overline{v}", "start", VEL)
    # the length l between the rails
    f.line(548, ytop, 548, ybot, INK, 2)
    f.line(540, ytop, 556, ytop, INK, 2); f.line(540, ybot, 556, ybot, INK, 2)
    f.tex(562, 180, "l", "start")
    return f.svg()


def flux_task():
    """Task figure: the flux through a coil of 50 turns against time, piecewise linear: 0 -> 4,0 mWb in 0–0,20 s,
    constant to 0,50 s, 4,0 -> 0 mWb in 0,50–0,60 s, zero to 0,70 s. No voltage drawn or written."""
    f = Fig("fy75-flux-task", 340, "Kuvaaja mittakaavassa: käämin läpi kulkeva magneettivuo millivebereinä ajan funktiona "
            "sekunteina. Vuo kasvaa tasaisesti nollasta arvoon 4,0 hetkestä 0 hetkeen 0,20 s, pysyy arvossa 4,0 hetkeen "
            "0,50 s asti, pienenee tasaisesti nollaan hetkeen 0,60 s mennessä ja on sen jälkeen nolla. Ruudukon väli on "
            "0,1 s ja 1 mWb.")
    ax = Axes(f, (96, 290), (480, 64), x=(0, 0.7), y=(0, 5), xticks=[0.1 * k for k in range(1, 8)],
              yticks=list(range(1, 6)), xlabel=r"t\ (\text{s})", ylabel=r"\Phi\ (\text{mWb})",
              xfmt=lambda v: fi(round(v, 1), 1))
    ax.line([(0, 0), (0.2, 4.0), (0.5, 4.0), (0.6, 0), (0.7, 0)], FIELD, 3)
    return f.svg()


def flux_task_2():
    """Task figure: the flux through a coil against time, piecewise linear and changing sign: 5,0 mWb at 0, falling to
    -3,0 mWb at 0,40 s, constant to 0,60 s, rising to 0 at 0,80 s. No voltage drawn or written."""
    f = Fig("fy75-flux-task-2", 362, "Kuvaaja mittakaavassa: käämin läpi kulkeva magneettivuo millivebereinä ajan funktiona "
            "sekunteina. Vuo on hetkellä 0 arvossa 5,0 ja pienenee tasaisesti arvoon miinus 3,0 hetkeen 0,40 s mennessä. "
            "Sen jälkeen vuo pysyy arvossa miinus 3,0 hetkeen 0,60 s asti ja kasvaa tasaisesti nollaan hetkeen 0,80 s "
            "mennessä. Ruudukon väli on 0,1 s ja 1 mWb.")
    ax = Axes(f, (96, 316), (480, 60), x=(0, 0.9), y=(-3.5, 5.5), xticks=[0.1 * k for k in range(1, 10)],
              yticks=[-3, -2, -1, 1, 2, 3, 4, 5], xlabel=r"t\ (\text{s})", ylabel=r"\Phi\ (\text{mWb})",
              xfmt=lambda v: fi(round(v, 1), 1) if round(v * 10) % 2 == 0 else "", x_at=0, ticks_below=True)
    ax.line([(0, 5.0), (0.4, -3.0), (0.6, -3.0), (0.8, 0), (0.9, 0)], FIELD, 3)
    return f.svg()


def hero():
    """The opening illustration: a cyclist at dusk, the front lamp lit by the hub dynamo, its beam on the road."""
    f = H.hero("fy75-hero", "Kuvitus: pyöräilijä ajaa hämärässä metsätiellä. Polkupyörän etupyörän navassa on dynamo, ja "
               "ohjaustangon lamppu loistaa: valokeila osuu tiehen pyörän edessä. Taivas on illan sininen, ja tien reunalla "
               "on kuusia.")
    f.rect(0, 0, 1200, 600, H.grad(f, "fy75h-sky", COLD, COLD_LIGHT))
    for k in range(18):
        f.circle(60 + H.rnd(k, 3) * 1080, 30 + H.rnd(k + 40, 3) * 150, 1.5 + 1.5 * H.rnd(k + 80, 3), WHITE)
    H.forest(f, 380, 150, 70, INK, seed=5, depth=40)
    for x, h in ((90, 210), (210, 260), (1040, 240), (1150, 200)):
        H.spruce(f, x, 420, h)
    f.rect(0, 410, 1200, 190, H.grad(f, "fy75h-road", IRON, INK))
    f.line(0, 470, 1200, 470, METAL_EDGE, 3)
    for x in range(40, 1200, 140):
        f.rect(x, 532, 70, 8, SAND_LIGHT, rx=3)
    # the lamp's beam on the road ahead
    f.path("M742,348 L1110,470 L1160,560 L760,372 Z", H.grad(f, "fy75h-beam", HEAT_LIGHT, PAPER, horizontal=True),
           extra='fill-opacity="0.7"')
    H.rider(f, 470, 700, 520, 92, frame=HOT, shirt=COLD_LIGHT, helmet=HEAT)
    # the hub dynamo, the lamp and its wire
    f.circle(700, 520, 18, METAL_EDGE, INK, 3)
    f.circle(700, 520, 8, IRON)
    f.path("M712,508 C726,470 736,420 742,366", stroke=INK, w=2.5)
    f.rect(728, 340, 30, 24, IRON, INK, 3, 6)
    f.circle(756, 352, 10, H.glow(f, "fy75h-lamp"))
    f.circle(756, 352, 5, HEAT_LIGHT)
    return f.svg()


def scene():
    """A second everyday scene: a shake flashlight, its magnet sliding through the coil and its LED lit."""
    f = H.scene("fy75-scene", "Kuvitus: ravistelutaskulamppu pöydällä. Läpinäkyvän rungon sisällä on lieriön muotoinen "
                "magneetti ja rungon keskellä kuparinen käämi. Kun lamppua ravistellaan, magneetti liukuu käämin läpi edestakaisin, "
                "ja lampun etupään valodiodi loistaa.")
    f.rect(0, 0, 600, 360, PAPER)
    f.rect(0, 270, 600, 90, H.grad(f, "fy75s-desk", SAND_LIGHT, SAND))
    f.line(0, 270, 600, 270, GRAIN, 2)
    # the clear body of the lamp
    f.rect(90, 150, 380, 90, GLASS, INK, 3, 40)
    f.rect(470, 160, 50, 70, IRON, INK, 3, 10)
    f.circle(536, 195, 34, H.glow(f, "fy75s-led"))
    f.circle(524, 195, 10, HEAT_LIGHT, INK, 2)
    # the coil round the middle and the magnet inside
    for k in range(9):
        x = 250 + 10 * k
        f.add(f'<ellipse cx="{x}" cy="195" rx="6" ry="47" fill="none" stroke="{COPPER}" stroke-width="4"/>')
    f.rect(150, 175, 50, 40, SPOLE, INK, 2.5, 4)
    f.rect(200, 175, 50, 40, NPOLE, INK, 2.5, 4)
    # motion lines: the magnet slides back and forth
    for y in (128, 262):
        f.path(f"M150,{y} H250", stroke=MUTED, w=4, extra='stroke-linecap="round"')
        f.path(f"M142,{y} l14,-8 v16 Z", MUTED)
        f.path(f"M258,{y} l-14,-8 v16 Z", MUTED)
    return f.svg()


FIGURES = {"hero": hero, "faraday": faraday, "flux": flux, "graph": graph, "rod": rod, "scene": scene,
           "flux-task": flux_task, "flux-task-2": flux_task_2}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "faraday": "reveals: a moving magnet induces a voltage, a magnet at rest does not, and the sign flips with the motion",
    "flux": "reveals: the flux is largest when the loop is perpendicular to the field and zero when parallel",
    "graph": "reveals: e is zero where Φ(t) is flat and ∓20 mV where Φ changes (the slope gives e)",
    "rod": "reveals: the magnetic and electric forces on an electron in a moving rod and which end is positive",
    "flux-task": "safe: Φ(t) of a 50-turn coil, piecewise linear 0–4,0 mWb, no voltage drawn",
    "flux-task-2": "safe: Φ(t) of a coil, piecewise linear 5,0 → −3,0 → 0 mWb over 0–0,80 s, no voltage drawn",
}
