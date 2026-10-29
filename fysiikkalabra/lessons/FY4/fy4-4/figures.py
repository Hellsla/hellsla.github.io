"""Figures of fy4-4 (scripts/figlib.py, scripts/fbd.py, scripts/herolib.py); `python scripts/figures.py fy4-4` writes them into
lesson.md. Every force diagram is an FBD: the object alone as a plain rectangle, its arrows drawn to scale and its physics
checked as it is drawn; the situation is a separate pictorial situation picture (tilannekuva); no point-particle diagrams.
Velocity is blue, acceleration orange and forces red in every figure (FBD.motion, FBD.force)."""
import math
from figlib import (Fig, Axes, INK, MUTED, WHITE, RULE, RULE_LIGHT, SAND_LIGHT, SAND, SAND_DARK, GRAIN, COPPER, ICE, GLASS,
                    COLD, COLD_LIGHT, HOT, HOT_LIGHT, HEAT, HEAT_LIGHT, GOOD, GOOD_LIGHT, IRON, ALUMINIUM, METAL_EDGE, n)
from fbd import FBD, ground
import herolib as H
from herolib import grad, rnd

g = 9.81
BOX, BOX_EDGE = SAND_LIGHT, GRAIN


# ---------------------------------------------------------------- opening illustration
def _truck(f, xf, yg, loaded, pre):
    """A timber truck in side view facing right: the cab's front at xf, the wheels on the road at yg. loaded: a stack of logs."""
    cab_w, bed_x0 = 120, xf - 500
    # chassis and the timber bunks
    f.rect(bed_x0 - 10, yg - 74, 500, 16, INK, rx=3)
    for k in range(4):
        bx = bed_x0 + 30 + k * 105
        f.rect(bx, yg - 96, 30, 22, IRON, INK, 2, 2)
        f.rect(bx + 2, yg - 210, 8, 116, METAL_EDGE, INK, 2); f.rect(bx + 20, yg - 210, 8, 116, METAL_EDGE, INK, 2)
    if loaded:   # three rows of logs: the long sides, the cut ends at the back
        for row in range(3):
            y = yg - 112 - row * 30
            x0, x1 = bed_x0 + 8 - row * 4, bed_x0 + 372 + row * 6
            f.rect(x0, y - 14, x1 - x0, 30, grad(f, f"{pre}-log{row}", SAND_DARK, COPPER), INK, 2.5, 13)
            f.path(f"M{n(x0 + 30)},{n(y - 2)} H{n(x1 - 40)}", stroke=GRAIN, w=1.5, extra='stroke-opacity="0.7"')
            f.path(f"M{n(x0 + 60)},{n(y + 8)} H{n(x1 - 90)}", stroke=GRAIN, w=1.5, extra='stroke-opacity="0.5"')
            for j in range(3):
                cx = x0 + 4 + j * 9
                f.circle(cx + 6, y + 1, 15 - j * 0.5, SAND_LIGHT, GRAIN, 2)
                f.circle(cx + 6, y + 1, 8, "none", GRAIN, 1.5)
        f.path(f"M{bed_x0 + 10},{yg - 184} Q{bed_x0 + 200},{yg - 196} {bed_x0 + 380},{yg - 182}", stroke=INK, w=2.5)   # the binding strap
    # the cab
    cx0 = xf - cab_w
    f.path(f"M{cx0},{yg - 58} V{yg - 190} Q{cx0},{yg - 206} {cx0 + 16},{yg - 206} H{xf - 30} Q{xf - 10},{yg - 206} {xf - 6},{yg - 180} "
           f"L{xf},{yg - 120} V{yg - 58} Z", grad(f, f"{pre}-cab", COLD_LIGHT, COLD), INK, 3)
    f.path(f"M{cx0 + 50},{yg - 196} H{xf - 30} Q{xf - 16},{yg - 196} {xf - 13},{yg - 178} L{xf - 8},{yg - 140} H{cx0 + 50} Z", grad(f, f"{pre}-glass", WHITE, GLASS), INK, 2.5)
    f.rect(cx0 + 10, yg - 196, 30, 56, GLASS, INK, 2.5, 3)
    f.line(cx0 + 46, yg - 196, cx0 + 46, yg - 62, INK, 2)
    f.rect(cx0 + 54, yg - 128, 18, 6, INK, rx=3)                       # the door handle
    f.rect(xf - 8, yg - 84, 16, 26, ALUMINIUM, INK, 2, 3)               # the bumper
    f.circle(xf - 2, yg - 100, 7, HEAT_LIGHT, INK, 2)                   # a headlight
    f.rect(cx0 - 14, yg - 230, 10, 120, ALUMINIUM, INK, 2, 4)           # the exhaust pipe behind the cab
    # the wheels: two at the back, one under the cab
    for wx in (bed_x0 + 70, bed_x0 + 150, bed_x0 + 330, xf - 70):
        f.circle(wx, yg - 32, 32, INK)
        f.circle(wx, yg - 32, 14, ALUMINIUM, METAL_EDGE, 2)
        for k in range(5):
            a = k * 2 * math.pi / 5
            f.circle(wx + 8 * math.cos(a), yg - 32 + 8 * math.sin(a), 2, METAL_EDGE)
    return cx0 - 9, yg - 230


def hero():
    """The chapter's opening illustration: two identical timber trucks drive off at a green light; the empty one is ahead."""
    f = H.hero("fy44-hero", "Kuvitus: maantien liikennevalot ovat juuri vaihtuneet vihreiksi, ja kaksi samanlaista kuorma-autoa on lähtenyt "
               "liikkeelle vierekkäisiltä kaistoilta. Lähempänä on täyteen tukeilla lastattu auto, joka on vasta päässyt pysäytysviivan yli. "
               "Kauempana oleva tyhjä auto on jo selvästi edellä. Taustalla on metsää ja peltoa.")
    H.sky(f, "fy44h", 330, ICE, GLASS)
    H.sun(f, "fy44h", 1060, 92, 44, rays=False)
    H.cloud(f, 300, 90, 0.9); H.cloud(f, 760, 60, 0.6)
    H.hills(f, "fy44h", 230, [GOOD_LIGHT, SAND_LIGHT], amp=34, seed=7)
    H.forest(f, 292, 70, 30, GOOD, seed=5, depth=40)
    for k in range(6): H.spruce(f, 60 + k * 190 + 50 * rnd(k, 3), 330, 90 + 40 * rnd(k, 8))
    H.red_house(f, 880, 300, 150, 70)                                      # a farmhouse by the field
    H.birch(f, 1080, 336, 150); H.birch(f, 330, 336, 120)
    f.rect(0, 326, 1200, 30, GOOD_LIGHT)                                   # the verge
    for k in range(25): f.rect(10 + k * 50, 322, 6, 26, ALUMINIUM, METAL_EDGE, 1.5)   # the guard rail
    f.rect(0, 326, 1200, 8, ALUMINIUM, METAL_EDGE, 1.5)
    # the road: two lanes, a dashed centre line, the stop line at the lights
    f.rect(0, 352, 1200, 248, grad(f, "fy44h-road", METAL_EDGE, MUTED, y1=352, y2=600))
    f.rect(0, 348, 1200, 8, ALUMINIUM)
    f.rect(0, 588, 1200, 12, ALUMINIUM)
    for k in range(9): f.rect(40 + k * 150, 466, 80, 8, WHITE, rx=2)
    f.rect(212, 360, 14, 226, WHITE)
    # the traffic lights: green
    f.rect(150, 160, 12, 200, IRON, INK, 2)
    f.rect(128, 100, 56, 136, INK, rx=10)
    for k, (c, on) in enumerate(((HOT, False), (HEAT_LIGHT, False), (GOOD, True))):
        f.circle(156, 124 + k * 42, 15, c if on else IRON, INK, 2)
        if on: f.add(f'<circle cx="156" cy="{124 + k * 42}" r="26" fill="{GOOD_LIGHT}" fill-opacity="0.45"/>')
    # the empty truck in the far lane, well ahead; the loaded one in the near lane, just over the stop line
    sc, X, Y = 0.8, 1150, 452                                             # the far truck is smaller: it is further away
    f.add(f'<g transform="translate({X},{Y}) scale({sc}) translate({-X},{-Y})">')
    ex, ey = _truck(f, X, Y, False, "fy44h-e")
    f.add('</g>')
    ex, ey = X + (ex - X) * sc, Y + (ey - Y) * sc
    lx, ly = _truck(f, 700, 576, True, "fy44h-l")
    for (x, y, s) in ((ex, ey, 1.0), (lx, ly, 1.2)):                     # exhaust from both: the engines work equally hard
        for k in range(3): f.add(f'<circle cx="{n(x - 18 - k * 22)}" cy="{n(y - 14 - k * 16)}" r="{n((10 + 6 * k) * s)}" fill="{MUTED}" fill-opacity="{0.45 - 0.12 * k:.2f}"/>')
    # speed lines behind the trucks: longer behind the empty one
    for k in range(3):
        f.line(712 - k * 8, 404 + k * 16, 742 - k * 8, 404 + k * 16, WHITE, 4, cap="round")
        f.line(190 - 60 - k * 10, 500 + k * 24, 190 - 16 - k * 10, 500 + k * 24, WHITE, 4, cap="round")
    return f.svg()


# ---------------------------------------------------------------- theory figures
def box(f, cx, cy, w, h):
    f.rect(cx - w / 2, cy - h / 2, w, h, BOX, BOX_EDGE, 2.5, rx=3)
    f.line(cx - w / 2 + 6, cy, cx + w / 2 - 6, cy, BOX_EDGE, 1.5)


def kokonaisvoima():
    """Ydinajatus: the same box at rest on the floor and pulled with friction; the situation pictures above, the force diagrams
    (case A and a horizontal acceleration) below, and the net force as its own hollow arrow."""
    f = Fig("fy44-kokonaisvoima", 420, "Kaksi tilannetta. Vasemmalla laatikko lepää lattialla. Sen voimakuviossa laatikko on suorakulmio: paino G "
            "keskipisteestä alas ja lattian tukivoima N alapinnasta ylös, yhtä pitkinä. Oikealla samaa laatikkoa vedetään narulla "
            "vaakasuoraan oikealle, ja tilannekuvassa laatikon yllä on oranssi kiihtyvyysnuoli oikealle. Sen voimakuviossa on paino ja "
            "tukivoima yhtä pitkinä, narun jännitysvoima T oikealle ja lattian kitkavoima alapinnan takakulmasta vasemmalle, kolmasosa "
            "jännitysvoiman pituudesta. Erillään on vihreä ontto nuoli, kokonaisvoima, oikealle: jännitysvoiman ja kitkan erotus. Nuolet ovat mittakaavassa.")
    f.line(300, 10, 300, 410, RULE, 1.5, "6 6")
    f.line(20, 140, 580, 140, RULE_LIGHT, 1.5, "4 6")
    # left: at rest
    f.tex(150, 20, r"\text{levossa}", "middle", MUTED)
    ground(f, 50, 250, 112)
    box(f, 150, 88, 70, 48)
    m, s = 8.0, 0.95
    G = m * g
    d = FBD(f, s, body=(150, 270, 70, 48), m=m, a=(0, 0))
    d.force("G", (0, -G), (150, 270), "gravity", lab=(20, -4))
    d.force("N", (0, G), (167, 294), "normal", surface=0, lab=(20, 4))
    d.draw()
    # right: pulled to the right, friction to the left, speeding up
    T, Fmu = 60.0, 20.0
    f.tex(450, 20, r"\text{vedetään}", "middle", MUTED)
    ground(f, 330, 580, 112)
    box(f, 410, 88, 70, 48)
    f.line(445, 88, 520, 88, GRAIN, 3, cap="round"); f.circle(524, 88, 8, MUTED)
    cx, cy = 420, 270
    d = FBD(f, s, body=(cx, cy, 70, 48), m=m, a=((T - Fmu) / m, 0))
    d.force("G", (0, -G), (cx, cy), "gravity", lab=(20, -4))
    d.force("N", (0, G), (cx + 17, cy + 24), "normal", surface=0, lab=(20, 4))
    d.force("T", (T, 0), (cx + 35, cy), "tension", rope=(1, 0), lab=(22, -2))
    d.force("F_mu", (-Fmu, 0), (cx - 35, cy + 24), "friction", surface=0, lab=(-10, 22))
    d.draw()
    d.motion(r"\overline{a}", (1, 0), (378, 52), 54)
    d.net((470, 360), lab=(28, 0))
    return f.svg()


def kuvaaja():
    """Ydinajatus: the acceleration against the net force for two masses (model values of the simulation): straight lines through
    the origin, the heavier cart's line half as steep."""
    f = Fig("fy44-kuvaaja", 360, "Kuvaaja mittakaavassa: vaaka-akselilla kokonaisvoima newtoneina 0–3, pystyakselilla kiihtyvyys 0–6 metriä "
            "sekunnin neliölle. Kaksi suoraa origon kautta, kummallakin kolme pistettä. Massalla 0,50 kilogrammaa pisteet ovat 1 N ja 2, "
            "2 N ja 4 sekä 3 N ja 6. Massalla 1,0 kilogrammaa pisteet ovat 1 N ja 1, 2 N ja 2 sekä 3 N ja 3. Katkoviivat näyttävät, että "
            "kokonaisvoimalla 2 N kevyemmän kärryn kiihtyvyys on 4 ja raskaamman 2.")
    ax = Axes(f, (90, 300), (380, 70), x=(0, 3), y=(0, 6), xticks=[0, 0.5, 1, 1.5, 2, 2.5, 3], yticks=[1, 2, 3, 4, 5, 6],
              xlabel=r"\Sigma F\ (\text{N})", ylabel=r"a\ (\text{m/s}^2)",
              xfmt=lambda v: "" if v != int(v) else str(int(v)))
    ax.guide(2, 4); ax.guide(2, 2)
    ax.line([(0, 0), (3, 6)], INK)
    ax.line([(0, 0), (3, 3)], COPPER)
    for F in (1, 2, 3):
        ax.point(F, F / 0.50, INK); ax.point(F, F / 1.0, COPPER)
    f.tex(ax.X(3) + 14, ax.Y(6), r"m = 0{,}50\,\text{kg}", "start")
    f.tex(ax.X(3) + 14, ax.Y(3), r"m = 1{,}0\,\text{kg}", "start", COPPER)
    return f.svg()


def _hang(f, ox, oy, title, Tk, v, a):
    """One panel of the crane figure: the crate on the crane's rope (situation picture, left) and its force diagram (right), with
    the velocity (blue) and the acceleration (orange) beside the diagram. Tk = T/G; v, a: +1 up, −1 down, 0 none."""
    f.tex(ox + 150, oy + 22, title, "middle", MUTED)
    # situation: the hook on the rope, the crate under it
    f.line(ox + 62, oy + 44, ox + 62, oy + 118, INK, 2.5)
    f.path(f"M{ox + 62},{oy + 118} q-12,4 -10,16 q4,10 14,6", stroke=IRON, w=4)
    f.line(ox + 56, oy + 138, ox + 36, oy + 160, INK, 1.5); f.line(ox + 68, oy + 138, ox + 88, oy + 160, INK, 1.5)
    f.rect(ox + 28, oy + 160, 68, 52, grad(f, f"fy44-crate{ox}{oy}", SAND_DARK, SAND), INK, 2.5, 2)
    for k in (1, 2): f.line(ox + 28, oy + 160 + k * 17, ox + 96, oy + 160 + k * 17, GRAIN, 1.5)
    f.line(ox + 120, oy + 48, ox + 120, oy + 286, RULE_LIGHT, 1.5, "4 5")
    # force diagram
    G = 80.0
    cx, cy, w, h = ox + 180, oy + 186, 56, 40
    d = FBD(f, 1.0, body=(cx, cy, w, h), a_dir=(0, a))
    d.force("G", (0, -G), (cx, cy), "gravity", lab=(22, -2))
    d.force("T", (0, G * Tk), (cx, cy - h / 2), "tension", rope=(0, 1), lab=(22, 12))
    d.draw()
    if v: d.motion(r"\overline{v}", (0, v), (ox + 236, oy + (206 if v > 0 else 146)), 60)
    else: f.tex(ox + 224, oy + 150, r"v = 0", "start", MUTED)
    if a: d.motion(r"\overline{a}", (0, a), (ox + 272, oy + (206 if a > 0 else 146)), 44 if a > 0 else 50)
    else: f.tex(ox + 224, oy + (200 if not v else 244), r"a = 0", "start", MUTED)


def nosturi():
    """Kaava: a crate on a crane's rope in four states of motion (example situation E), each with its force diagram, the velocity
    and the acceleration beside it: the net force points with the acceleration, not with the velocity."""
    f = Fig("fy44-nosturi", 620, "Neljä tilannetta, joissa nosturin köysi kannattelee laatikkoa. Kussakin on vasemmalla tilannekuva ja oikealla "
            "laatikon voimakuvio, jossa laatikko on suorakulmio: paino G keskipisteestä alas ja köyden jännitysvoima T yläpinnasta ylös. "
            "Voimakuvion vieressä on sininen nopeusnuoli ja oranssi kiihtyvyysnuoli, kun ne eivät ole nollia. Vasemmalla ylhäällä laatikko "
            "on levossa, v ja a ovat nollia ja nuolet T ja G yhtä pitkät. Oikealla ylhäällä laatikko nousee tasaisella nopeudella: nopeus "
            "ylös, a on nolla ja nuolet yhtä pitkät. Vasemmalla alhaalla laatikko nousee kiihtyen: nopeus ja kiihtyvyys ylös, T pidempi "
            "kuin G. Oikealla alhaalla laatikko nousee hidastuen: nopeus ylös mutta kiihtyvyys alas, ja T on lyhyempi kuin G.")
    f.line(300, 10, 300, 610, RULE, 1.5, "6 6"); f.line(10, 310, 590, 310, RULE, 1.5, "6 6")
    _hang(f, 0, 0, r"\text{levossa}", 1.0, 0, 0)
    _hang(f, 300, 0, r"\text{nousee tasaisesti}", 1.0, 1, 0)
    _hang(f, 0, 310, r"\text{nousee kiihtyen}", 1.3, 1, 1)
    _hang(f, 300, 310, r"\text{nousee hidastuen}", 0.7, 1, -1)
    return f.svg()


EX = dict(m=480.0, T=5200.0)      # the worked example's data (lesson-answers.py computes the same)


def esimerkki():
    """The worked example's force diagram: the concrete element on the crane's rope, accelerating up, with the positive direction."""
    m, T = EX["m"], EX["T"]
    G = m * g; a = (T - G) / m
    f = Fig("fy44-esimerkki", 360, "Betonielementin voimakuvio, elementti suorakulmiona. Köyden jännitysvoima T lähtee yläpinnasta ylös, ja "
            "paino G lähtee keskipisteestä alas. Nuoli T on vähän pidempi kuin nuoli G. Oikealla erillään oranssi kiihtyvyysnuoli ylös. "
            "Vasemmalla pieni nuoli y ylös: positiivinen suunta on ylös.")
    cx, cy, w, h = 300, 190, 110, 50
    d = FBD(f, 0.026, body=(cx, cy, w, h), m=m, a=(0, a))
    d.force("T", (0, T), (cx, cy - h / 2), "tension", rope=(0, 1), lab=(26, 12))
    d.force("G", (0, -G), (cx, cy), "gravity", lab=(26, -6))
    d.draw()
    d.motion(r"\overline{a}", (0, 1), (430, 220), 60)
    f.arrow(120, 300, 120, 236, MUTED, 2, 10); f.tex(120, 218, r"y", "middle", MUTED)
    return f.svg()


# ---------------------------------------------------------------- task figures (shown by id from inquiry.json)
LOWER = ("Vasemmalla tilannekuva: nosturin köysi laskee laatikkoa, ja laatikon vieressä sininen nopeusnuoli osoittaa alas. Oikealla "
         "laatikon voimakuvio, laatikko suorakulmiona: köyden jännitysvoima T yläpinnasta ylös ja paino G keskipisteestä alas.")


def _lower(name, Tk, desc, wrong=None, extra=False):
    """An option of the selection task: a crate lowered on a crane's rope, slowing down before the ground."""
    f = Fig(f"fy44-valitse-{name}", 300, desc, width=300)
    f.line(62, 14, 62, 96, INK, 2.5)
    f.path("M62,96 q-12,4 -10,16 q4,10 14,6", stroke=IRON, w=4)
    f.line(56, 116, 36, 138, INK, 1.5); f.line(68, 116, 88, 138, INK, 1.5)
    f.rect(28, 138, 68, 52, grad(f, f"fy44-vcrate-{name}", SAND_DARK, SAND), INK, 2.5, 2)
    f.rect(16, 262, 100, 14, RULE, INK, 2)
    G = 70.0
    cx, cy, w, h = 212, 160, 56, 40
    d = FBD(f, 1.0, body=(cx, cy, w, h), a_dir=None if wrong else (0, 1), wrong=wrong)
    d.force("G", (0, -G), (cx, cy), "gravity", lab=(22, -2))
    d.force("T", (0, G * Tk), (cx, cy - h / 2), "tension", rope=(0, 1), lab=(22, 12))
    if extra: d.force("F", (0, -36), (cx + w / 2, cy - 14), "other", lab=(20, 4))
    d.draw()
    FBD(f, 1.0, body=(62, 164, 68, 52), draw_body=False).motion(r"\overline{v}", (0, -1), (112, 140), 56)
    f.line(144, 20, 144, 280, RULE, 1.5, "6 6")
    return f.svg()


def valitse_a(): return _lower("a", 1.3, LOWER + " Nuoli T on pidempi kuin nuoli G.")
def valitse_b(): return _lower("b", 1.0, LOWER + " Nuolet T ja G ovat yhtä pitkät.", wrong="T = G although the crate slows down (accelerates up)")
def valitse_c(): return _lower("c", 0.7, LOWER + " Nuoli T on lyhyempi kuin nuoli G.", wrong="T < G: the net force points down, with the velocity, so the crate would speed up")
def valitse_d(): return _lower("d", 1.3, LOWER + " Nuoli T on pidempi kuin nuoli G, ja laatikon kyljestä lähtee lisäksi punainen nuoli F alas.",
                               wrong="an invented force F along the motion: nothing exerts it", extra=True)


def malli_kirja():
    """Model diagram for the drawing task: a book pushed along a table by a hand, speeding up against friction (case A vertically)."""
    m, F, Fmu = 1.2, 5.0, 3.0
    G = m * g; a = (F - Fmu) / m
    f = Fig("fy44-malli-kirja", 330, "Mallikuvio: kirjaa työnnetään pöydällä vaakasuoraan oikealle, ja se kiihtyy. Kuviossa on vain kirja "
            "suorakulmiona. Keskipisteestä paino G alas ja alapinnasta pöydän tukivoima N ylös, yhtä pitkinä. Käden työntövoima F osoittaa "
            "oikealle ja päättyy kirjan vasempaan kylkeen. Pöydän kitkavoima lähtee alapinnan takakulmasta vasemmalle ja on lyhyempi kuin "
            "työntövoima. Erillään oranssi kiihtyvyysnuoli oikealle.")
    cx, cy, w, h = 330, 150, 120, 44
    d = FBD(f, 12.0, body=(cx, cy, w, h), m=m, a=(a, 0))
    d.force("G", (0, -G), (cx, cy), "gravity", lab=(20, -4))
    d.force("N", (0, G), (cx + 20, cy + h / 2), "normal", surface=0, lab=(20, 6))
    d.force("F", (F, 0), (cx - w / 2, cy - 10), "applied", push=True, lab=(-24, -4))
    d.force("F_mu", (-Fmu, 0), (cx - w / 2, cy + h / 2), "friction", surface=0, lab=(-14, 22))
    d.draw()
    d.motion(r"\overline{a}", (1, 0), (450, 60), 60)
    return f.svg()


FIGURES = {"hero": hero, "kokonaisvoima": kokonaisvoima, "kuvaaja": kuvaaja, "nosturi": nosturi, "esimerkki": esimerkki,
           "valitse-a": valitse_a, "valitse-b": valitse_b, "valitse-c": valitse_c, "valitse-d": valitse_d, "malli-kirja": malli_kirja}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "kokonaisvoima": "reveals: the force diagrams of a box at rest and of a box pulled against friction, with the net force",
    "kuvaaja": "reveals: a against the net force for 0,50 kg and 1,0 kg (lines through the origin)",
    "nosturi": "reveals: the force diagrams of a crate on a crane's rope at rest, rising steadily, speeding up and slowing down",
    "esimerkki": "reveals: the force diagram of the worked example (crane lifting a concrete element, accelerating up)",
    "valitse-a": "reveals: the right diagram for a crate lowered and slowing down (T > G; an option figure)",
    "valitse-b": "safe: a wrong option (T = G) for diagram selection",
    "valitse-c": "safe: a wrong option (T < G) for diagram selection",
    "valitse-d": "safe: a wrong option (an invented force along the motion) for diagram selection",
    "malli-kirja": "reveals: the model diagram of a book pushed along a table, speeding up against friction (shown after the attempt)",
}
