"""Figures of fy4-5 (scripts/figlib.py, scripts/fbd.py); `python scripts/figures.py fy4-5` writes them into lesson.md.
Every force diagram is an FBD: the object alone as a plain rectangle, its arrows drawn to scale and its physics checked
as it is drawn. The situation is a separate pictorial situation picture (tilannekuva); no point-particle diagrams."""
import math
from figlib import Fig, INK, MUTED, WHITE, RULE, RULE_LIGHT, SAND_LIGHT, SAND, COPPER, ICE, ICE_EDGE, COLD_LIGHT, GLASS, fi
from fbd import FBD, ground, FORCE, VELOCITY
from figlib import GOOD, HEAT, HOT, HOT_LIGHT, IRON, n
import herolib as H
from figlib import COLD, METAL_EDGE
from herolib import grad, rnd
from figlib import ALUMINIUM
from figstyle import limb

SKIN = "#f3d2b3"

g = 9.81
BOX, BOX_EDGE = SAND_LIGHT, "#a97a35"


def hero():
    """The chapter's opening illustration: a sled pulled by a rope slanting up leaves a shallower track than an identical sled standing still."""
    f = H.hero("fy45-hero", "Kuvitus: talvinen piha. Vasemmalla pulkka seisoo paikallaan ja on painunut syvälle lumeen. Oikealla lapsi vetää "
               "samanlaista pulkkaa narusta vinosti ylöspäin, ja sen jättämä jälki lumessa on matalampi.")
    H.sky(f, "fy45h", 330, ICE, GLASS)
    H.sun(f, "fy45h", 1040, 90, 40, rays=False)
    H.hills(f, "fy45h", 230, [WHITE, GLASS], amp=36, seed=4)
    H.forest(f, 300, 70, 30, GOOD, seed=3, depth=40)
    for k in range(12): f.path(f"M{n(rnd(k, 4) * 1200)},{n(300 - 40 * rnd(k, 6))} l8,-14 l8,14 Z", WHITE)
    H.red_house(f, 60, 352, 300, 130, snow=True)
    for k in range(30):                                     # a picket fence along the yard
        x = 380 + k * 28
        if x > 1200: break
        f.path(f"M{x},{352} V{312} l9,-10 l9,10 V352 Z", WHITE, METAL_EDGE, 2)
    f.rect(370, 322, 830, 8, WHITE, METAL_EDGE, 2)
    H.birch(f, 1150, 360, 250, leaves=False)
    f.path("M0,350 Q300,336 600,350 T1200,346 V600 H0 Z", grad(f, "fy45h-snow", WHITE, COLD_LIGHT, y1=340, y2=600))
    for k in range(26): f.path(f"M{n(rnd(k, 9) * 1200)},{n(370 + rnd(k, 2) * 220)} q14,-4 28,0", stroke=ICE, w=2, extra='stroke-linecap="round"')
    for k in range(4): f.add(f'<ellipse cx="{885 + k * 42}" cy="{n(522 + (k % 2) * 12)}" rx="14" ry="6" fill="{COLD_LIGHT}" stroke="{ICE_EDGE}" stroke-width="1.5"/>')   # the child's footprints
    def sled(x, y, sink, tid):
        """A plastic sled, front to the right, its bottom `sink` below the snow surface at y."""
        w, h = 300, 74; top = y + sink - h
        f.add(f'<ellipse cx="{x}" cy="{y + 4}" rx="{w / 2 + 34}" ry="{14 + sink * 0.5}" fill="{COLD_LIGHT}"/>')
        f.path(f"M{x - w / 2},{top + 8} Q{x - w / 2 - 6},{y + sink} {x - w / 2 + 30},{y + sink} H{x + w / 2 - 50} "
               f"Q{x + w / 2 + 10},{y + sink} {x + w / 2 + 18},{top - 10} L{x + w / 2 - 8},{top - 12} Q{x + w / 2 - 20},{top + 20} {x + w / 2 - 60},{top + 20} "
               f"H{x - w / 2 + 26} L{x - w / 2 + 20},{top} Z", grad(f, tid, HOT_LIGHT, HOT), INK, 3)
        f.path(f"M{x - w / 2 + 30},{top + 30} H{x + w / 2 - 70}", stroke=HOT_LIGHT, w=5, extra='stroke-linecap="round" stroke-opacity="0.8"')
        for hx in (x - w / 2 + 44, x + w / 2 - 92): f.rect(hx, top + 38, 34, 14, WHITE, INK, 2, 7)
        # the snow in front of the sled covers its sunken bottom
        f.path(f"M{x - w / 2 - 50},{y} Q{x - w / 2 - 20},{y - 14} {x - w / 2 + 10},{y - 4} H{x + w / 2 - 10} Q{x + w / 2 + 20},{y - 14} {x + w / 2 + 50},{y} "
               f"V{y + 60} H{x - w / 2 - 50} Z", "url(#fy45h-snow)")
        f.path(f"M{x - w / 2 - 50},{y} Q{x - w / 2 - 20},{y - 14} {x - w / 2 + 10},{y - 4} H{x + w / 2 - 10} Q{x + w / 2 + 20},{y - 14} {x + w / 2 + 50},{y}", stroke=ICE_EDGE, w=2.5)
        return x + w / 2 + 4, top - 8
    # the sled standing still: deep in the snow
    sled(250, 470, 40, "fy45h-s1")
    # the pulled sled: shallow, a faint shallow track behind it
    for dy in (-6, 8): f.path(f"M440,{470 + dy} H{560}", stroke=ICE_EDGE, w=3, extra='stroke-linecap="round" stroke-opacity="0.7"')
    fx, fy = sled(700, 470, 6, "fy45h-s2")
    hand = (1010, 330)
    f.line(fx, fy, *hand, COPPER, 5, cap="round")
    H.walker(f, 1050, 520, COLD, INK, 0.62, lean=26, hand=hand, winter=True, stride=0.9)
    return f.svg()


def box(f, cx, cy, w, h):
    f.rect(cx - w / 2, cy - h / 2, w, h, BOX, BOX_EDGE, 2.5, rx=3)


def hand(f, x, y): f.circle(x, y, 8, "#6b7480")


def rope(f, x1, y1, x2, y2): f.line(x1, y1, x2, y2, "#a97a35", 3, cap="round")


def person(f, cx, yfoot, h=120, coat="#1971c2"):
    """The lift passenger, seen from the front, in the house style (fy7-11/observer, figstyle.limb): shaped legs, coat and
    arms, a head with hair, shoes on the floor at yfoot; h is the height to the top of the head, the centre of mass about at
    mid-height. One drawing for every lift figure of the chapter."""
    s = h / 120
    for dx in (-7, 7):                                             # legs and shoes
        limb(f, (cx + dx * s, yfoot - 54 * s), (cx + dx * s * 1.1, yfoot - 6 * s), 13 * s, 10 * s, "#3a4350", sw=1.25)
        f.rect(cx + dx * s * 1.1 - 7 * s + (3 * s if dx > 0 else -3 * s), yfoot - 7 * s, 14 * s, 7 * s, INK, None, 0, 3 * s)
    f.rect(cx - 4 * s, yfoot - 104 * s, 8 * s, 10 * s, SKIN)                                                 # the neck
    limb(f, (cx, yfoot - 80 * s), (cx, yfoot - 64 * s), 31 * s, 29 * s, coat, sw=1.25)                     # the coat
    for sx in (-1, 1):                                             # arms along the sides, hands
        limb(f, (cx + sx * 15 * s, yfoot - 88 * s), (cx + sx * 18 * s, yfoot - 58 * s), 9 * s, 8 * s, coat, sw=1.25)
        f.circle(cx + sx * 18 * s, yfoot - 54 * s, 4.5 * s, SKIN, "#b98a5e", 1)
    hx, hy, r = cx, yfoot - 111 * s, 11 * s
    f.circle(hx, hy, r, SKIN, "#b98a5e", 1.25)
    f.path(f"M{n(hx - r)},{n(hy - 2 * s)} Q{n(hx - r)},{n(hy - r - 4 * s)} {n(hx)},{n(hy - r - 2 * s)} "
           f"Q{n(hx + r)},{n(hy - r - 4 * s)} {n(hx + r)},{n(hy - 2 * s)} Q{n(hx)},{n(hy - r + 7 * s)} {n(hx - r)},{n(hy - 2 * s)} Z", "#3a4350")  # hair


def cabin(f, x, y, w, h):
    """A lift car (fy4-16's, copied; outlined in soft ink like the house style's glass): the cable from above, the walls, a
    handrail and the floor (its top at y + h - 12)."""
    f.line(x + w / 2, y - 10, x + w / 2, y, IRON, 3)
    f.rect(x, y, w, h, GLASS, "#3a4350", 1.75, rx=4)
    f.rect(x + 6, y + h - 12, w - 12, 8, ALUMINIUM, METAL_EDGE, 1.5)
    f.line(x + w - 14, y + h * 0.45, x + w - 14, y + h * 0.62, METAL_EDGE, 3)
    return y + h - 12


def axes_hint(f, x, y, label_x=r"x", label_y=r"y", ang=0):
    """Small coordinate axes (positive directions) in the corner of a force diagram."""
    ux, uy = math.cos(math.radians(ang)), math.sin(math.radians(ang))
    f.arrow(x, y, x + 46 * ux, y - 46 * uy, MUTED, 2, 10); f.arrow(x, y, x - 46 * uy, y - 46 * ux, MUTED, 2, 10)
    f.tex(x + 58 * ux, y - 58 * uy, label_x, "middle", MUTED); f.tex(x - 58 * uy, y - 58 * ux, label_y, "middle", MUTED)


# ---------------------------------------------------------------- theory figures
def tilanne():
    """Ydinajatus: the situation picture beside the force diagram of the same box (pulled at 30°, friction, speeding up)."""
    f = Fig("fy45-tilanne", 340, "Kaksi kuvaa samasta tilanteesta. Vasemmalla tilannekuva: laatikkoa vedetään lattiaa pitkin narulla, joka "
            "nousee vinosti ylöspäin, ja laatikon yllä ohut sininen nuoli näyttää nopeuden oikealle. Oikealla voimakuvio: vain laatikko "
            "suorakulmiona ja siihen vaikuttavat voimat punaisina nuolina. Paino G osoittaa keskipisteestä suoraan alas, lattian tukivoima N "
            "alapinnasta suoraan ylös ja on lyhyempi kuin paino, narun jännitysvoima T lähtee narun kiinnityskohdasta vinosti "
            "ylös oikealle ja lattian kitkavoima lähtee alapinnan takakulmasta vasemmalle. Nopeutta ei piirretä voimakuvioon.")
    # left: the situation
    f.tex(150, 22, r"\text{tilannekuva}", "middle", MUTED)
    ground(f, 20, 280, 200)
    box(f, 120, 170, 80, 60)
    rope(f, 160, 160, 160 + 100 * math.cos(math.radians(30)), 160 - 100 * math.sin(math.radians(30)))
    hand(f, 160 + 100 * math.cos(math.radians(30)), 160 - 100 * math.sin(math.radians(30)))
    FBD(f, 1).motion(r"\overline{v}", (1, 0), (90, 110), 70)
    f.line(300, 20, 300, 320, RULE, 1.5, "6 6")
    # right: the force diagram of the box alone
    f.tex(450, 22, r"\text{voimakuvio}", "middle", MUTED)
    m, T, a30, Fmu = 10.0, 50.0, math.radians(30), 30.0
    G = m * g; N = G - T * math.sin(a30)
    cx, cy = 440, 170
    d = FBD(f, 1.15, body=(cx, cy, 80, 60), a_dir=(1, 0))
    d.force("G", (0, -G), (cx, cy), "gravity", lab=(20, -4))
    d.force("N", (0, N), (cx + 20, cy + 30), "normal", surface=0, lab=(20, 4))
    d.force("T", (T * math.cos(a30), T * math.sin(a30)), (cx + 40, cy - 10), "tension", rope=(math.cos(a30), math.sin(a30)))
    d.force("F_mu", (-Fmu, 0), (cx - 40, cy + 30), "friction", surface=0, lab=(-14, -18))
    d.draw()
    return f.svg()


def suunnat():
    """Guide step 3: the directions of the common forces, four panels, each a small situation picture (pictorial) with
    the object's force diagram (a rectangle, no surfaces) beside it."""
    f = Fig("fy45-suunnat", 620, "Neljä tilannetta. Kussakin on vasemmalla pieni tilannekuva ja oikealla kappaleen voimakuvio, jossa "
            "kappale on suorakulmio eikä pintoja piirretä. Vasemmalla ylhäällä laatikko lepää vaakasuoralla lattialla: paino G "
            "keskipisteestä alas ja yhtä pitkä tukivoima N alapinnasta ylös. Oikealla ylhäällä laatikko on paikallaan kaltevalla "
            "rinteellä: voimakuviossa suorakulmio on kallellaan kuten rinteellä, paino G suoraan alas, tukivoima N kohtisuoraan "
            "alapintaa vastaan ja kitkavoima alapinnan ylemmästä kulmasta rinteen suuntaisesti ylös. Vasemmalla alhaalla lamppu "
            "roikkuu johdon varassa: paino G alas ja johdon jännitysvoima T yläpinnasta ylös. Oikealla alhaalla heliumilmapallo "
            "painuu kattoa vasten ja on paikallaan: noste keskipisteestä ylös, paino keskipisteestä alas ja katon tukivoima N, "
            "joka painaa yläpintaa alaspäin, pois katon pinnasta. Nosteen nuoli on yhtä pitkä kuin painon ja tukivoiman nuolet yhteensä.")
    f.line(300, 10, 300, 610, RULE, 1.5, "6 6"); f.line(10, 310, 590, 310, RULE, 1.5, "6 6")
    # 1 floor: situation left, diagram right
    f.tex(150, 24, r"\text{lattia}", "middle", MUTED)
    ground(f, 20, 120, 190); box(f, 70, 168, 56, 44)
    G1 = 80.0
    (FBD(f, 1.1, body=(215, 160, 60, 44), a_dir=(0, 0)).force("G", (0, -G1), (215, 160), "gravity", lab=(20, -4))
     .force("N", (0, G1), (230, 182), "normal", surface=0, lab=(20, 4)).draw())
    # 2 slope 25°: situation left, the tilted rectangle right
    th = math.radians(25)
    f.tex(450, 24, r"\text{rinne}", "middle", MUTED)
    t, nrm = (math.cos(th), math.sin(th)), (-math.sin(th), math.cos(th))
    x0, y0 = 312, 230
    ground(f, x0, x0 + 120 * math.cos(th), y0, angle=25)
    bx, by = x0 + 64 * t[0], y0 - 64 * t[1]
    pts = [(bx - 22 * t[0], by + 22 * t[1]), (bx + 22 * t[0], by - 22 * t[1])]
    f.path(f"M{pts[0][0]:.1f},{pts[0][1]:.1f} L{pts[1][0]:.1f},{pts[1][1]:.1f} L{pts[1][0] + 34 * nrm[0]:.1f},{pts[1][1] - 34 * nrm[1]:.1f} "
           f"L{pts[0][0] + 34 * nrm[0]:.1f},{pts[0][1] - 34 * nrm[1]:.1f} Z", BOX, BOX_EDGE, 2.5)
    G2 = 80.0
    cx, cy, w, h = 492, 150, 60, 44
    fx, fy = cx - (h / 2) * nrm[0], cy + (h / 2) * nrm[1]           # middle of the bottom face (figure coordinates)
    d = FBD(f, 1.1, body=(cx, cy, w, h, 25), a_dir=(0, 0))
    d.force("G", (0, -G2), (cx, cy), "gravity", lab=(20, 4))
    d.force("N", (G2 * math.cos(th) * nrm[0], G2 * math.cos(th) * nrm[1]), (fx + 12 * t[0], fy - 12 * t[1]), "normal", surface=25, lab=(-16, -6))
    d.force("F_mu", (G2 * math.sin(th) * t[0], G2 * math.sin(th) * t[1]), (fx + w / 2 * t[0], fy - w / 2 * t[1]), "friction", surface=25, lab=(0, 24))
    d.draw()
    # 3 hanging lamp: situation left, diagram right
    f.tex(150, 334, r"\text{lamppu}", "middle", MUTED)
    ground(f, 30, 110, 360, below=False)
    f.line(70, 360, 70, 440, INK, 2.5)
    f.path("M48,470 L92,470 L81,440 L59,440 Z", "#e9c98a", INK, 2.5)
    G3 = 70.0
    (FBD(f, 1.1, body=(215, 470, 50, 36), a_dir=(0, 0)).force("G", (0, -G3), (215, 470), "gravity", lab=(22, -4))
     .force("T", (0, G3), (215, 452), "tension", rope=(0, 1), lab=(22, 20)).draw())
    # 4 helium balloon under the ceiling: situation left, diagram right
    f.tex(450, 334, r"\text{heliumpallo}", "middle", MUTED)
    ground(f, 316, 430, 360, below=False)
    f.circle(372, 402, 40, "#f2a69c", INK, 2.5)
    f.line(372, 442, 368, 520, MUTED, 1.5)
    B = (515, 490, 70, 40)
    Gp, Fb = 40.0, 100.0
    d = FBD(f, 1.0, body=B, a_dir=(0, 0))
    d.force("F_noste", (0, Fb), (B[0], B[1]), "buoyancy", tex=r"\overline{F}_\text{noste}", lab=(40, 12))
    d.force("G", (0, -Gp), (B[0], B[1]), "gravity", lab=(18, 4))
    d.force("N", (0, -(Fb - Gp)), (B[0] - 20, B[1] - B[3] / 2), "normal", surface=0, outward=(0, -1), push=True, lab=(-20, -6))
    d.draw()
    return f.svg()


def komponentit():
    """Kaava: a force F at the angle α on an object, and its components F_x, F_y (dashed), with the right triangle."""
    f = Fig("fy45-komponentit", 300, "Kappaleeseen vaikuttaa voima F, joka lähtee kappaleen oikeasta yläkulmasta vinosti ylös oikealle "
            "kulmassa alfa vaakasuoraan nähden. Katkoviivoin piirretyt komponentit lähtevät samasta kulmasta: vaakasuora F x pitkin "
            "x-akselia ja pystysuora F y pitkin y-akselia. Komponentit ja voima muodostavat suorakulmaisen kolmion, jonka hypotenuusa "
            "on F. Merkinnät: F x on F kertaa kosini alfa ja F y on F kertaa sini alfa.")
    P, F, al = (110, 230), 200.0, math.radians(35)
    d = FBD(f, 1, body=(P[0] - 40, P[1] + 28, 80, 56))
    d.force("F", (F * math.cos(al), F * math.sin(al)), P, "applied", lab=(-6, -18))
    d.component("F_x", "F", (1, 0), lab=(0, 22)); d.component("F_y", "F", (0, 1), lab=(-24, 0))
    d.draw()
    ex, ey = P[0] + F * math.cos(al), P[1] - F * math.sin(al)
    f.line(ex, P[1], ex, ey, RULE, 1.5, "4 4"); f.line(P[0], ey, ex, ey, RULE, 1.5, "4 4")
    f.path(f"M{P[0] + 52},{P[1]} A52,52 0 0 0 {P[0] + 52 * math.cos(al):.1f},{P[1] - 52 * math.sin(al):.1f}", "none", INK, 2)
    f.tex(P[0] + 64, P[1] - 18, r"\alpha", "start")
    f.tex(390, 120, r"F_x = F\cos\alpha", "start", w=190); f.tex(390, 170, r"F_y = F\sin\alpha", "start", w=190)
    return f.svg()


EX = dict(m=12.0, F=80.0, al=35.0, Fmu=30.0)       # the worked example's data (lesson-answers.py computes the same)


def esimerkki():
    """The worked example's force diagram: sled pulled at 35°, 80 N, friction 30 N, 12 kg (the sled a rectangle, with axes)."""
    m, F, al, Fmu = EX["m"], EX["F"], math.radians(EX["al"]), EX["Fmu"]
    G = m * g; N = G - F * math.sin(al); a = (F * math.cos(al) - Fmu) / m
    f = Fig("fy45-esimerkki", 360, "Pulkan voimakuvio, pulkka suorakulmiona. Paino G keskipisteestä alas, lumen tukivoima N alapinnasta ylös "
            "ja painoa lyhyempi, narun jännitysvoima T etuyläkulmasta vinosti ylös oikealle kulmassa 35 astetta, sen komponentit "
            "katkoviivoin, ja lumen kitkavoima alapinnan takakulmasta vasemmalle. Nurkassa akselit: x oikealle eli liikkeen suuntaan ja y ylös.")
    cx, cy, w, h = 270, 185, 120, 44
    P = (cx + w / 2, cy - h / 2)                                   # the rope's attachment: the front top corner
    d = FBD(f, 1.15, body=(cx, cy, w, h), m=m, a=(a, 0))
    d.force("G", (0, -G), (cx, cy), "gravity", lab=(20, -4))
    d.force("N", (0, N), (cx + 20, cy + h / 2), "normal", surface=0, lab=(-30, 6))
    d.force("T", (F * math.cos(al), F * math.sin(al)), P, "tension", rope=(math.cos(al), math.sin(al)), lab=(16, -10))
    d.force("F_mu", (-Fmu, 0), (cx - w / 2, cy + h / 2), "friction", surface=0, lab=(-10, -16))
    d.component("T_x", "T", (1, 0), lab=(0, 24)); d.component("T_y", "T", (0, 1), lab=(-4, -16))
    d.draw()
    f.path(f"M{P[0] + 40},{P[1]} A40,40 0 0 0 {P[0] + 40 * math.cos(al):.1f},{P[1] - 40 * math.sin(al):.1f}", "none", MUTED, 1.5)
    f.tex(P[0] + 48, P[1] - 14, r"35^\circ", "start", MUTED)
    axes_hint(f, 70, 320)
    return f.svg()


# ---------------------------------------------------------------- task figures (shown by id from inquiry.json and exercises.json)
def virhe_liukuva():
    """Find the error: a box sliding right after the push ended, drawn WITH a forward force."""
    f = Fig("fy45-virhe", 300, "Opiskelijan piirtämä voimakuvio lattialla liukuvasta laatikosta, laatikko suorakulmiona. Keskipisteestä "
            "lähtee nuoli G alas ja alapinnasta yhtä pitkä nuoli N ylös. Alapinnan takakulmasta lähtee kitkavoiman nuoli vasemmalle ja "
            "laatikon oikeasta kyljestä nuoli F oikealle. Nuoli F on pidempi kuin kitkavoiman nuoli.")
    d = FBD(f, 1.0, body=(300, 150, 90, 60), wrong="a forward force F is drawn although nothing pushes the sliding box any more (the error to find)")
    d.force("G", (0, -100), (300, 150), "gravity", lab=(20, -4))
    d.force("N", (0, 100), (320, 180), "normal", surface=0, lab=(20, 4))
    d.force("F_mu", (-40, 0), (255, 180), "friction", surface=0, lab=(-6, -16))
    d.force("F", (70, 0), (345, 140), "applied")
    d.draw()
    return f.svg()


def _lift(name, N_over_G, desc, wrong=None, v_force=False):
    """An option of the lift question: the lift with the person (situation picture, left) and the person's force diagram,
    the person a rectangle (right)."""
    f = Fig(f"fy45-hissi-{name}", 300, desc, width=300)
    floor = cabin(f, 16, 50, 104, 200)
    person(f, 68, floor, 112)
    f.line(140, 30, 140, 270, RULE, 1.5, "6 6")
    cx, cy, w, h = 214, 150, 48, 80
    G = 70.0
    d = FBD(f, 1.15, body=(cx, cy, w, h), a_dir=(0, 1) if not wrong else None, wrong=wrong)
    d.force("G", (0, -G), (cx, cy), "gravity", lab=(20, -4))
    d.force("N", (0, G * N_over_G), (cx - 12, cy + h / 2), "normal", surface=0, lab=(-22, 6))
    d.draw()
    if v_force:                                                    # the error: the velocity drawn as one more red force arrow
        (FBD(f, 1.15, body=(cx, cy, w, h), draw_body=False, wrong="velocity as a force")
         .force("v", (0, 45), (cx + w / 2, cy - 10), "other", tex=r"\overline{v}", lab=(18, 8)).draw())
    return f.svg()


LIFT = "Hissikori ja siinä seisova ihminen sekä ihmisen voimakuvio, jossa ihminen on suorakulmio: paino G keskipisteestä alas ja lattian tukivoima N alapinnasta ylös."


def hissi_a():
    return _lift("a", 1.3, LIFT + " Nuoli N on pidempi kuin nuoli G.")


def hissi_b():
    return _lift("b", 1.0, LIFT + " Nuolet N ja G ovat yhtä pitkät.", wrong="N = G although the person accelerates upward")


def hissi_c():
    return _lift("c", 1.3, LIFT + " Nuoli N on pidempi kuin G, ja kappaleen kyljestä lähtee lisäksi punainen nuoli v ylös.",
                 wrong="the velocity v drawn as a force", v_force=True)


def hissi_d():
    return _lift("d", 0.75, LIFT + " Nuoli N on lyhyempi kuin nuoli G.", wrong="N < G: the net force points down, against the acceleration")


def malli_tyonto():
    """Model diagram for the drawing task: a box pushed along the floor at 30° below the horizontal at constant velocity."""
    m, F, al = 12.0, 60.0, math.radians(30)
    G = m * g; Fx, Fy = F * math.cos(al), -F * math.sin(al); N = G - Fy
    f = Fig("fy45-malli-tyonto", 360, "Mallikuvio: laatikko liukuu lattialla tasaisella nopeudella, kun sitä työnnetään kahvasta vinosti "
            "alaspäin. Kuviossa on vain laatikko suorakulmiona. Keskipisteestä paino G alas. Alapinnasta lattian tukivoima N ylös, ja se on "
            "pidempi kuin paino. Kahvan voima F osoittaa vinosti alas eteenpäin ja päättyy laatikon takayläkulmaan, jossa kahva on "
            "kiinni. Alapinnan takakulmasta kitkavoima taaksepäin, yhtä pitkä kuin voiman F vaakakomponentti.")
    s = 0.9
    cx, cy, w, h = 300, 200, 140, 80
    d = FBD(f, s, body=(cx, cy, w, h), a_dir=(0, 0))
    d.force("G", (0, -G), (cx, cy), "gravity", lab=(20, -4))
    d.force("N", (0, N), (cx + 30, cy + h / 2), "normal", surface=0, lab=(20, 4))
    d.force("F", (Fx, Fy), (cx - w / 2, cy - h / 2), "applied", push=True)
    d.force("F_mu", (-Fx, 0), (cx - w / 2, cy + h / 2), "friction", surface=0, lab=(-10, 20))
    d.draw()
    return f.svg()


def malli_pulkka():
    """Model diagram for exercise L2-01: a sled pulled at 30° at constant velocity (rope 60 N, 15 kg)."""
    m, T, al = 15.0, 60.0, math.radians(30)
    G = m * g; N = G - T * math.sin(al)
    f = Fig("fy45-malli-pulkka", 360, "Mallikuvio: pulkka liukuu lumella tasaisella nopeudella, kun sitä vedetään narulla 30 asteen kulmassa. "
            "Pulkka on suorakulmio. Paino G keskipisteestä alas, lumen tukivoima N alapinnasta ylös ja painoa lyhyempi, narun "
            "jännitysvoima T etuyläkulmasta vinosti ylös eteenpäin ja lumen kitkavoima alapinnan takakulmasta taaksepäin, yhtä pitkä "
            "kuin jännitysvoiman vaakakomponentti, joka on piirretty katkoviivalla.")
    cx, cy, w, h = 280, 170, 120, 44
    d = FBD(f, 1.0, body=(cx, cy, w, h), a_dir=(0, 0))
    d.force("G", (0, -G), (cx, cy), "gravity", lab=(20, -4))
    d.force("N", (0, N), (cx + 24, cy + h / 2), "normal", surface=0, lab=(20, 6))
    d.force("T", (T * math.cos(al), T * math.sin(al)), (cx + w / 2, cy - h / 2), "tension", rope=(math.cos(al), math.sin(al)))
    d.force("F_mu", (-T * math.cos(al), 0), (cx - w / 2, cy + h / 2), "friction", surface=0, lab=(-10, -16))
    d.component("T_x", "T", (1, 0), lab=(0, 24))
    d.draw()
    axes_hint(f, 70, 320)
    return f.svg()


def malli_hissi_jarru():
    """Model diagram for exercise L3-01: a person in a lift moving up and slowing down (70 kg, a = 1,5 m/s² down)."""
    m, a = 70.0, -1.5
    G = m * g; N = m * (g + a)
    f = Fig("fy45-malli-hissi", 340, "Mallikuvio: ihminen hississä, joka liikkuu ylöspäin ja hidastaa. Vasemmalla tilannekuvana hissikori "
            "ja ihminen. Keskellä ihmisen voimakuvio, ihminen suorakulmiona: paino G keskipisteestä alas ja lattian tukivoima N "
            "alapinnasta ylös, lyhyempi kuin paino. Oikealla erillään ohuet nuolet: sininen nopeus v ylös ja oranssi kiihtyvyys a alas. "
            "Ne eivät ole voimia.")
    floor = cabin(f, 30, 60, 130, 240)
    person(f, 95, floor, 140)
    cx, cy, w, h = 300, 170, 44, 90
    d = FBD(f, 0.17, body=(cx, cy, w, h), m=m, a=(0, a))
    d.force("G", (0, -G), (cx, cy), "gravity", lab=(22, -4))
    d.force("N", (0, N), (cx - 12, cy + h / 2), "normal", surface=0, lab=(-26, 2))
    d.draw()
    d.motion(r"\overline{v}", (0, 1), (450, 200), 70)
    d.motion(r"\overline{a}", (0, -1), (520, 120), 50)
    return f.svg()


def ruutu():
    """Exercise L1-02: four forces on an object (a rectangle) drawn on a grid, 1 square = 10 N; the student reads them off."""
    f = Fig("fy45-ruutu", 400, "Voimakuvio ruudukolla, yksi ruutu vastaa 10 newtonia. Kappale on kahden ruudun levyinen ja korkuinen "
            "neliö, ja siihen vaikuttaa neljä voimaa, jotka lähtevät kappaleen sivujen keskeltä: F1 oikealle neljän ruudun mittaisena, "
            "F2 vasemmalle kahden ja puolen ruudun mittaisena, F3 ylös kolmen ruudun mittaisena ja F4 alas kolmen ruudun mittaisena.")
    sq, P = 32, (284, 200)
    for i in range(-7, 9):
        f.line(P[0] + i * sq, 8, P[0] + i * sq, 392, RULE_LIGHT, 1.2)
    for j in range(-6, 7):
        f.line(P[0] - 7 * sq, P[1] + j * sq, P[0] + 8 * sq, P[1] + j * sq, RULE_LIGHT, 1.2)
    d = FBD(f, sq / 10, body=(P[0], P[1], 2 * sq, 2 * sq), a_dir=(1, 0))
    d.force("F_1", (40, 0), (P[0] + sq, P[1]), "applied", lab=(16, -16))
    d.force("F_2", (-25, 0), (P[0] - sq, P[1]), "applied", lab=(-8, -18))
    d.force("F_3", (0, 30), (P[0], P[1] - sq), "applied", lab=(24, 6))
    d.force("F_4", (0, -30), (P[0], P[1] + sq), "applied", lab=(24, -6))
    d.draw()
    f.rect(P[0] + 5 * sq, 372, sq, 4, INK); f.tex(P[0] + 6 * sq + 8, 374, r"10\,\text{N}", "start")
    return f.svg()


def ruutu_vinot():
    """Exercise L2-08: two oblique forces on a block seen from above on a 2,0 N grid; the student reads the components off
    the grid crossings and finds the net force and the acceleration. F_1 = (10, 12) N, F_2 = (-4, -4) N."""
    f = Fig("fy45-ruutu-vinot", 400, "Kappale ylhäältä katsottuna ruudukolla, yksi ruutu vastaa 2,0 newtonia. Kappale on kahden ruudun levyinen ja korkuinen "
            "neliö, ja siihen vaikuttaa kaksi vinoa voimaa. F1 lähtee kappaleen oikeasta yläkulmasta ja päättyy ruudukon risteykseen viisi ruutua "
            "oikealle ja kuusi ruutua ylös lähtöpisteestä. F2 lähtee kappaleen vasemmasta alakulmasta ja päättyy risteykseen kaksi ruutua "
            "vasemmalle ja kaksi ruutua alas lähtöpisteestä.")
    sq, P = 28, (240, 250)
    for i in range(-8, 12):
        f.line(P[0] + i * sq, 8, P[0] + i * sq, 392, RULE_LIGHT, 1.2)
    for j in range(-8, 6):
        f.line(P[0] - 8 * sq, P[1] + j * sq, P[0] + 11 * sq, P[1] + j * sq, RULE_LIGHT, 1.2)
    d = FBD(f, sq / 2.0, body=(P[0], P[1], 2 * sq, 2 * sq), a_dir=(3, 4))
    d.force("F_1", (10, 12), (P[0] + sq, P[1] - sq), "applied", lab=(-22, -8))
    d.force("F_2", (-4, -4), (P[0] - sq, P[1] + sq), "applied", lab=(-10, -18))
    d.draw()
    f.rect(P[0] + 6 * sq, 372, 2 * sq, 4, INK); f.tex(P[0] + 8 * sq + 8, 374, r"4{,}0\,\text{N}", "start")
    return f.svg()


# Voimakuvion valinta (task fy4-5-L1-09, docs/exercise-types.md type 3): a box pushed horizontally to the right slides at
# constant velocity, so G = N and the push F = the friction F_mu. Four option diagrams to one scale (0,9 units per
# newton, G = 98,1 N, F = 40 N); only "pick-tasainen" is right, each other has one error.
PK_G, PK_F, PK_S = 10.0 * g, 40.0, 0.9
PK_BODY = (175, 106, 110, 84)
PK_DESC = "Voimakuvio mittakaavassa: laatikko suorakulmiona. Keskipisteestä alaspäin osoittaa paino G ja alapinnasta ylöspäin yhtä pitkä tukivoima N. "


def pick_push(fid, label, push=PK_F, extra=False, v_force=False, wrong=None):
    """One option: the box as a rectangle; G from the centre, N from the bottom face, the push F ending at the left face
    (the pusher stands on the left), friction from the bottom left corner to the left; extra adds F_k, the box's force on
    the pusher (it acts on the pusher, not on the box); v_force draws the velocity into the diagram as if it were a force (in velocity blue)."""
    cx, cy, w, h = PK_BODY
    f = Fig(fid, 240, label, width=300)
    d = FBD(f, PK_S, body=PK_BODY, a_dir=(0, 0), wrong=wrong)
    d.force("G", (0, -PK_G), (cx, cy), "gravity", lab=(-20, 6))
    d.force("N", (0, PK_G), (cx + 24, cy + h / 2), "normal", surface=0, lab=(24, -14))   # above the body's top edge, clear of the head
    d.force("F", (push, 0), (cx - w / 2, cy - 26), "applied", push=True, lab=(-14, -16))
    d.force("F_mu", (-PK_F, 0), (cx - w / 2, cy + h / 2), "friction", surface=0, lab=(-12, 18))
    if extra:
        d.force("F_k", (-PK_F, 0), (cx - w / 2, cy + 8), "other", tex=r"\overline{F}_\text{k}", lab=(-14, -14))
    d.draw()
    if v_force:                                                    # the error: the velocity drawn into the force diagram
        x1, y = cx + w / 2, cy - 10                                # like a force, but in velocity blue (it is no force)
        f.arrow(x1, y, x1 + PK_F * PK_S, y, VELOCITY, 4, 18)
        f.tex(x1 + PK_F * PK_S + 14, y - 16, r"\overline{v}", "middle", VELOCITY)
    return f.svg()


def pick_tasainen():
    return pick_push("fy45-pick-tasainen", PK_DESC + "Vasemmalta tuleva työntövoima F osoittaa oikealle ja päättyy laatikon "
                     "vasempaan kylkeen. Alapinnan vasemmasta kulmasta lähtee kitkavoima vasemmalle. Nuolet F ja kitkavoima "
                     "ovat yhtä pitkät, kumpikin vajaa puolet painon nuolesta.")


def pick_pitka():
    return pick_push("fy45-pick-pitka", PK_DESC + "Vasemmalta tuleva työntövoima F osoittaa oikealle ja päättyy laatikon "
                     "vasempaan kylkeen. Alapinnan vasemmasta kulmasta lähtee kitkavoima vasemmalle. Nuoli F on kaksi kertaa "
                     "niin pitkä kuin kitkavoiman nuoli.", push=2 * PK_F,
                     wrong="the push is drawn twice the friction although the box slides at constant velocity")


def pick_lisa():
    return pick_push("fy45-pick-lisa", PK_DESC + "Vasemmalta tuleva työntövoima F osoittaa oikealle ja päättyy laatikon "
                     "vasempaan kylkeen. Vasemman kyljen keskeltä lähtee voima F_k vasemmalle, ja alapinnan vasemmasta "
                     "kulmasta lähtee kitkavoima vasemmalle. Nuolet F, F_k ja kitkavoima ovat yhtä pitkät.", extra=True,
                     wrong="an extra force F_k, the box's push on the pusher, acts on the pusher, not on the box")


def pick_nopeus():
    return pick_push("fy45-pick-nopeus", PK_DESC + "Vasemmalta tuleva työntövoima F osoittaa oikealle ja päättyy laatikon "
                     "vasempaan kylkeen. Alapinnan vasemmasta kulmasta lähtee kitkavoima vasemmalle, ja oikeasta kyljestä "
                     "lähtee sininen nopeuden nuoli v oikealle. Nuolet F, v ja kitkavoima ovat yhtä pitkät.", v_force=True,
                     wrong="the velocity v drawn as a force")


FIGURES = {"hero": hero, "tilanne": tilanne, "suunnat": suunnat, "komponentit": komponentit, "esimerkki": esimerkki,
           "virhe": virhe_liukuva, "hissi-a": hissi_a, "hissi-b": hissi_b, "hissi-c": hissi_c, "hissi-d": hissi_d,
           "malli-tyonto": malli_tyonto, "malli-pulkka": malli_pulkka, "malli-hissi": malli_hissi_jarru, "ruutu": ruutu, "ruutu-vinot": ruutu_vinot,
           "pick-tasainen": pick_tasainen, "pick-pitka": pick_pitka, "pick-lisa": pick_lisa, "pick-nopeus": pick_nopeus}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "tilanne": "reveals: the forces on a box pulled at an angle with friction (a theory figure)",
    "suunnat": "reveals: the situation pictures and force diagrams of a box on a floor and on a slope, a hanging lamp and a helium balloon under a ceiling",
    "komponentit": "safe: a force on an object and its components with the trigonometry, no situation",
    "esimerkki": "reveals: the force diagram of the worked example (sled pulled at 35°)",
    "virhe": "safe: a deliberately wrong diagram (forward force on a sliding box) for error-finding; its description lists the arrows, not the error",
    "hissi-a": "reveals: the right diagram for a person in a lift accelerating up (an option figure)",
    "hissi-b": "safe: a wrong option (N = G) for diagram selection",
    "hissi-c": "safe: a wrong option (velocity drawn as a force) for diagram selection",
    "hissi-d": "safe: a wrong option (N < G) for diagram selection",
    "malli-tyonto": "reveals: the model diagram of a box pushed down at 30° at constant velocity (shown after the attempt)",
    "malli-pulkka": "reveals: the model diagram of a sled pulled at 30° at constant velocity (shown in the solution)",
    "malli-hissi": "reveals: the model diagram of a person in a lift slowing down while moving up (shown in the solution)",
    "ruutu": "safe: four forces on a 10 N grid, no net force drawn",
    "ruutu-vinot": "safe: two oblique forces on a block seen from above on a 2,0 N grid, no net force or acceleration drawn (task fy4-5-L2-08)",
    "pick-tasainen": "reveals: the right option of task fy4-5-L1-09 (a box pushed at constant velocity: G = N, F = F_mu)",
    "pick-pitka": "safe: a wrong option of task fy4-5-L1-09 (the push drawn twice the friction)",
    "pick-lisa": "safe: a wrong option of task fy4-5-L1-09 (an extra F_k, the box's push on the pusher)",
    "pick-nopeus": "safe: a wrong option of task fy4-5-L1-09 (the velocity, a blue arrow, drawn into the force diagram as if it were a force)",
}
