"""Figures of fy4-5 (scripts/figlib.py, scripts/fbd.py); `python scripts/figures.py fy4-5` writes them into lesson.md.
Every force diagram is an FBD: its arrows are drawn to scale and its physics is checked as it is drawn."""
import math
from figlib import Fig, INK, MUTED, WHITE, RULE, RULE_LIGHT, SAND_LIGHT, SAND, COPPER, ICE, ICE_EDGE, COLD_LIGHT, GLASS, fi
from fbd import FBD, ground, MOTION, FORCE

g = 9.81
BOX, BOX_EDGE = SAND_LIGHT, "#a97a35"


def box(f, cx, cy, w, h):
    f.rect(cx - w / 2, cy - h / 2, w, h, BOX, BOX_EDGE, 2.5, rx=3)


def hand(f, x, y): f.circle(x, y, 8, "#6b7480")


def rope(f, x1, y1, x2, y2): f.line(x1, y1, x2, y2, "#a97a35", 3, cap="round")


def person(f, cx, yfoot, h=120, fill="#d0e6fb"):
    """A simple standing person: body, head, legs; the centre of mass about at mid-height."""
    f.rect(cx - 18, yfoot - h * 0.72, 36, h * 0.48, fill, INK, 2.5, rx=10)
    f.circle(cx, yfoot - h * 0.84, h * 0.11, fill, INK, 2.5)
    f.line(cx - 9, yfoot - h * 0.26, cx - 9, yfoot, INK, 4, cap="round"); f.line(cx + 9, yfoot - h * 0.26, cx + 9, yfoot, INK, 4, cap="round")


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
            "ja siihen vaikuttavat voimat punaisina nuolina. Paino G osoittaa keskipisteestä suoraan alas, lattian tukivoima N "
            "alapinnasta suoraan ylös ja on lyhyempi kuin paino, narun jännitysvoima T lähtee narun kiinnityskohdasta vinosti "
            "ylös oikealle ja lattian kitkavoima alapinnasta vasemmalle. Nopeutta ei piirretä voimakuvioon.")
    # left: the situation
    f.tex(150, 22, r"\text{tilannekuva}", "middle", MUTED)
    ground(f, 20, 280, 200)
    box(f, 120, 170, 80, 60)
    rope(f, 160, 160, 160 + 100 * math.cos(math.radians(30)), 160 - 100 * math.sin(math.radians(30)))
    hand(f, 160 + 100 * math.cos(math.radians(30)), 160 - 100 * math.sin(math.radians(30)))
    FBD(f, 1).motion(r"\mathbf{v}", (1, 0), (90, 110), 70)
    f.line(300, 20, 300, 320, RULE, 1.5, "6 6")
    # right: the force diagram of the box alone
    f.tex(450, 22, r"\text{voimakuvio}", "middle", MUTED)
    m, T, a30, Fmu = 10.0, 50.0, math.radians(30), 30.0
    G = m * g; N = G - T * math.sin(a30)
    cx, cy = 440, 170
    box(f, cx, cy, 80, 60)
    d = FBD(f, 1.15, a_dir=(1, 0))
    d.force("G", (0, -G), (cx, cy), "gravity", lab=(20, -4))
    d.force("N", (0, N), (cx + 20, cy + 30), "normal", surface=0, lab=(20, 4))
    d.force("T", (T * math.cos(a30), T * math.sin(a30)), (cx + 40, cy - 10), "tension", rope=(math.cos(a30), math.sin(a30)))
    d.force("F_mu", (-Fmu, 0), (cx - 22, cy + 30), "friction", surface=0, lab=(-14, -16))
    d.draw()
    return f.svg()


def suunnat():
    """Guide step 3: the directions of the common forces, four small force diagrams."""
    f = Fig("fy45-suunnat", 620, "Neljä pientä voimakuviota. Vasemmalla ylhäällä laatikko lepää vaakasuoralla lattialla: paino G "
            "keskipisteestä alas ja yhtä pitkä tukivoima N alapinnasta ylös. Oikealla ylhäällä laatikko on paikallaan kaltevalla "
            "rinteellä: paino G suoraan alas, tukivoima N kohtisuoraan rinnettä vastaan ja kitkavoima rinteen suuntaisesti ylös. "
            "Vasemmalla alhaalla lamppu roikkuu johdon varassa: paino G alas ja johdon jännitysvoima T johtoa pitkin ylös. Oikealla "
            "alhaalla heliumilmapallo painuu kattoa vasten ja on paikallaan. Sen vieressä pallon voimakuvio pisteenä: noste ylös, "
            "paino alas ja sen vieressä katon tukivoima N alas, pois katon pinnasta. Nosteen nuoli on yhtä pitkä kuin painon ja tukivoiman nuolet yhteensä.")
    f.line(300, 10, 300, 610, RULE, 1.5, "6 6"); f.line(10, 310, 590, 310, RULE, 1.5, "6 6")
    # 1 floor
    f.tex(150, 24, r"\text{lattia}", "middle", MUTED)
    ground(f, 40, 260, 200); box(f, 150, 170, 76, 60)
    G1 = 90.0
    (FBD(f, 1.1, a_dir=(0, 0)).force("G", (0, -G1), (150, 170), "gravity", lab=(20, -4))
     .force("N", (0, G1), (168, 200), "normal", surface=0, lab=(20, 4)).draw())
    # 2 slope 25°
    th = math.radians(25)
    f.tex(450, 24, r"\text{rinne}", "middle", MUTED)
    x0, y0 = 316, 262
    ground(f, x0, x0 + 268 * math.cos(th), y0, angle=25)
    t, nrm = (math.cos(th), math.sin(th)), (-math.sin(th), math.cos(th))
    s = 130
    bx, by = x0 + s * t[0], y0 - s * t[1]                          # middle of the contact face (figure coordinates)
    cxs, cys = bx + 30 * nrm[0], by - 30 * nrm[1]
    pts = [(bx - 36 * t[0], by + 36 * t[1]), (bx + 36 * t[0], by - 36 * t[1])]
    f.path(f"M{pts[0][0]:.1f},{pts[0][1]:.1f} L{pts[1][0]:.1f},{pts[1][1]:.1f} L{pts[1][0] + 60 * nrm[0]:.1f},{pts[1][1] - 60 * nrm[1]:.1f} "
           f"L{pts[0][0] + 60 * nrm[0]:.1f},{pts[0][1] - 60 * nrm[1]:.1f} Z", BOX, BOX_EDGE, 2.5)
    G2 = 90.0
    d = FBD(f, 1.1, a_dir=(0, 0))
    d.force("G", (0, -G2), (cxs, cys), "gravity", lab=(20, 4))
    d.force("N", (G2 * math.cos(th) * nrm[0], G2 * math.cos(th) * nrm[1]), (bx - 14 * t[0], by + 14 * t[1]), "normal", surface=25, lab=(-16, -6))
    d.force("F_mu", (G2 * math.sin(th) * t[0], G2 * math.sin(th) * t[1]), (bx + 16 * t[0], by - 16 * t[1]), "friction", surface=25, lab=(4, 22))
    d.draw()
    # 3 hanging lamp
    f.tex(150, 334, r"\text{lamppu}", "middle", MUTED)
    ground(f, 70, 230, 360, below=False)
    f.line(150, 360, 150, 450, INK, 2.5)
    f.path("M124,480 L176,480 L163,450 L137,450 Z", "#e9c98a", INK, 2.5)
    G3 = 80.0
    (FBD(f, 1.1, a_dir=(0, 0)).force("G", (0, -G3), (150, 468), "gravity", lab=(22, -4))
     .force("T", (0, G3), (150, 450), "tension", rope=(0, 1), lab=(22, 20)).draw())
    # 4 helium balloon under the ceiling: the situation and, beside it, the balloon as a point
    f.tex(450, 334, r"\text{heliumpallo}", "middle", MUTED)
    ground(f, 316, 430, 360, below=False)
    f.circle(372, 402, 40, "#f2a69c", INK, 2.5)
    f.line(372, 442, 368, 520, MUTED, 1.5)
    P = (505, 495)                                                 # the point; N is drawn beside G so both show
    f.circle(*P, 6, INK)
    Gp, Fb = 40.0, 100.0
    d = FBD(f, 1.0, a_dir=(0, 0))
    d.force("F_noste", (0, Fb), P, "buoyancy", tex=r"\mathbf{F}_\text{noste}", lab=(40, 12))
    d.force("G", (0, -Gp), (P[0] + 8, P[1]), "gravity", lab=(18, -2))
    d.force("N", (0, -(Fb - Gp)), (P[0] - 8, P[1]), "normal", surface=0, outward=(0, -1), lab=(-20, -8))
    d.draw()
    return f.svg()


def malli():
    """Representations: the same forces as a point-particle diagram, with the coordinate axes."""
    f = Fig("fy45-malli", 320, "Pistemallin voimakuvio samasta laatikosta kuin edellä: kaikki neljä voimaa lähtevät yhdestä pisteestä. "
            "Paino G alas, tukivoima N ylös ja painoa lyhyempi, narun jännitysvoima T vinosti ylös oikealle ja kitkavoima vasemmalle. "
            "Nurkassa koordinaattiakselit: x oikealle ja y ylös.")
    m, T, a30, Fmu = 10.0, 50.0, math.radians(30), 30.0
    G = m * g; N = G - T * math.sin(a30)
    P = (300, 150)
    f.circle(*P, 7, INK)
    d = FBD(f, 1.15, a_dir=(1, 0), particle=P)
    d.force("G", (0, -G), None, "gravity", lab=(20, -4))
    d.force("N", (0, N), None, "normal", surface=0, lab=(20, 4))
    d.force("T", (T * math.cos(a30), T * math.sin(a30)), None, "tension", rope=(math.cos(a30), math.sin(a30)))
    d.force("F_mu", (-Fmu, 0), None, "friction", surface=0, lab=(-16, -14))
    d.draw()
    axes_hint(f, 80, 270)
    return f.svg()


def komponentit():
    """Kaava: a force F at the angle α and its components F_x, F_y (dashed), with the right triangle."""
    f = Fig("fy45-komponentit", 300, "Voima F lähtee pisteestä vinosti ylös oikealle kulmassa alfa vaakasuoraan nähden. Katkoviivoin "
            "piirretyt komponentit: vaakasuora F x pitkin x-akselia ja pystysuora F y pitkin y-akselia. Komponentit ja voima "
            "muodostavat suorakulmaisen kolmion, jonka hypotenuusa on F. Merkinnät: F x on F kertaa kosini alfa ja F y on F kertaa sini alfa.")
    P, F, al = (110, 240), 200.0, math.radians(35)
    d = FBD(f, 1)
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
    """The worked example's force diagram: sled pulled at 35°, 80 N, friction 30 N, 12 kg (point model with axes)."""
    m, F, al, Fmu = EX["m"], EX["F"], math.radians(EX["al"]), EX["Fmu"]
    G = m * g; N = G - F * math.sin(al); a = (F * math.cos(al) - Fmu) / m
    f = Fig("fy45-esimerkki", 360, "Pulkan voimakuvio pistemallina. Paino G alas, lumen tukivoima N ylös ja painoa lyhyempi, narun "
            "jännitysvoima T vinosti ylös oikealle kulmassa 35 astetta, sen komponentit katkoviivoin, ja lumen kitkavoima vasemmalle. "
            "Nurkassa akselit: x oikealle eli liikkeen suuntaan ja y ylös.")
    P = (290, 180)
    f.circle(*P, 7, INK)
    d = FBD(f, 1.15, m=m, a=(a, 0), particle=P)
    d.force("G", (0, -G), None, "gravity", lab=(20, -4))
    d.force("N", (0, N), None, "normal", surface=0, lab=(22, 6))
    d.force("T", (F * math.cos(al), F * math.sin(al)), None, "tension", rope=(math.cos(al), math.sin(al)), lab=(16, -10))
    d.force("F_mu", (-Fmu, 0), None, "friction", surface=0, lab=(-16, -16))
    d.component("T_x", "T", (1, 0), lab=(0, 24)); d.component("T_y", "T", (0, 1), lab=(-28, 4))
    d.draw()
    f.path(f"M{P[0] + 40},{P[1]} A40,40 0 0 0 {P[0] + 40 * math.cos(al):.1f},{P[1] - 40 * math.sin(al):.1f}", "none", MUTED, 1.5)
    f.tex(P[0] + 48, P[1] - 14, r"35^\circ", "start", MUTED)
    axes_hint(f, 70, 320)
    return f.svg()


# ---------------------------------------------------------------- task figures (shown by id from inquiry.json and exercises.json)
def virhe_liukuva():
    """Find the error: a box sliding right after the push ended, drawn WITH a forward force."""
    f = Fig("fy45-virhe", 300, "Opiskelijan piirtämä voimakuvio lattialla liukuvasta laatikosta. Laatikon keskipisteestä lähtee "
            "nuoli G alas ja alapinnasta yhtä pitkä nuoli N ylös. Alapinnasta lähtee kitkavoiman nuoli vasemmalle ja laatikon "
            "oikeasta kyljestä nuoli F oikealle. Nuoli F on pidempi kuin kitkavoiman nuoli.")
    ground(f, 140, 460, 190)
    box(f, 300, 160, 90, 60)
    d = FBD(f, 1.0, wrong="a forward force F is drawn although nothing pushes the sliding box any more (the error to find)")
    d.force("G", (0, -100), (300, 160), "gravity", lab=(20, -4))
    d.force("N", (0, 100), (320, 190), "normal", surface=0, lab=(20, 4))
    d.force("F_mu", (-40, 0), (276, 190), "friction", surface=0, lab=(-14, -16))
    d.force("F", (70, 0), (345, 150), "applied")
    d.draw()
    return f.svg()


def _lift(name, N_over_G, desc, wrong=None, v_force=False):
    """An option of the lift question: a small lift with the person (left) and the person's force diagram as a point (right)."""
    f = Fig(f"fy45-hissi-{name}", 300, desc, width=300)
    f.rect(16, 50, 104, 200, "none", RULE, 3, rx=4)
    ground(f, 19, 117, 230)
    person(f, 68, 230, 112)
    P = (214, 150)
    f.circle(*P, 6, INK)
    G = 70.0
    d = FBD(f, 1.15, a_dir=(0, 1) if not wrong else None, wrong=wrong, particle=P)
    d.force("G", (0, -G), None, "gravity", lab=(20, -4))
    d.force("N", (0, G * N_over_G), None, "normal", surface=0, lab=(22, 6))
    d.draw()
    if v_force:                                                    # the error: the velocity drawn as one more red force arrow
        FBD(f, 1.15, wrong="velocity as a force").force("v", (0, 45), (P[0] + 26, P[1] - 10), "other", tex=r"\mathbf{v}", lab=(18, 8)).draw()
    return f.svg()


def hissi_a():
    return _lift("a", 1.3, "Hissikori ja siinä seisova ihminen sekä ihmisen voimakuvio pisteenä: paino G alas ja lattian tukivoima N "
                 "ylös. Nuoli N on pidempi kuin nuoli G.")


def hissi_b():
    return _lift("b", 1.0, "Hissikori ja siinä seisova ihminen sekä ihmisen voimakuvio pisteenä: paino G alas ja lattian tukivoima N "
                 "ylös. Nuolet N ja G ovat yhtä pitkät.", wrong="N = G although the person accelerates upward")


def hissi_c():
    return _lift("c", 1.3, "Hissikori ja siinä seisova ihminen sekä ihmisen voimakuvio pisteenä: paino G alas, lattian tukivoima N "
                 "ylös ja pidempi kuin G, sekä niiden vieressä punainen nuoli v ylös.", wrong="the velocity v drawn as a force", v_force=True)


def hissi_d():
    return _lift("d", 0.75, "Hissikori ja siinä seisova ihminen sekä ihmisen voimakuvio pisteenä: paino G alas ja lattian tukivoima N "
                 "ylös. Nuoli N on lyhyempi kuin nuoli G.", wrong="N < G: the net force points down, against the acceleration")


def malli_tyonto():
    """Model diagram for the drawing task: a box pushed along the floor at 30° below the horizontal at constant velocity."""
    m, F, al = 12.0, 60.0, math.radians(30)
    G = m * g; Fx, Fy = F * math.cos(al), -F * math.sin(al); N = G - Fy
    f = Fig("fy45-malli-tyonto", 360, "Mallikuvio: laatikko liukuu lattialla tasaisella nopeudella, kun sitä työnnetään kahvasta vinosti "
            "alaspäin. Kuviossa on vain laatikko. Keskipisteestä paino G alas. Alapinnasta lattian tukivoima N ylös, ja se on pidempi kuin "
            "paino. Kahvan voima F lähtee laatikon takayläkulmasta, jossa kahva on kiinni, ja osoittaa vinosti alas eteenpäin. Alapinnasta kitkavoima taaksepäin, "
            "yhtä pitkä kuin voiman F vaakakomponentti.")
    s = 0.9
    ground(f, 120, 480, 250)
    box(f, 300, 210, 140, 80)
    hx, hy = 234, 174                                              # where the handle is fixed; the handle itself is not drawn
    d = FBD(f, s, a_dir=(0, 0))
    d.force("G", (0, -G), (300, 210), "gravity", lab=(20, -4))
    d.force("N", (0, N), (330, 250), "normal", surface=0, lab=(20, 4))
    d.force("F", (Fx, Fy), (hx, hy), "applied", lab=(-62, -46))
    d.force("F_mu", (-Fx, 0), (270, 250), "friction", surface=0, lab=(-10, 20))
    d.draw()
    return f.svg()


def malli_pulkka():
    """Model diagram for exercise L2-01: a sled pulled at 30° at constant velocity (rope 60 N, 15 kg)."""
    m, T, al = 15.0, 60.0, math.radians(30)
    G = m * g; N = G - T * math.sin(al)
    f = Fig("fy45-malli-pulkka", 360, "Mallikuvio: pulkka liukuu lumella tasaisella nopeudella, kun sitä vedetään narulla 30 asteen kulmassa. "
            "Pistemallissa paino G alas, lumen tukivoima N ylös ja painoa lyhyempi, narun jännitysvoima T vinosti ylös eteenpäin ja "
            "lumen kitkavoima taaksepäin, yhtä pitkä kuin jännitysvoiman vaakakomponentti, joka on piirretty katkoviivalla.")
    P = (300, 160)
    f.circle(*P, 7, INK)
    d = FBD(f, 1.0, a_dir=(0, 0), particle=P)
    d.force("G", (0, -G), None, "gravity", lab=(20, -4))
    d.force("N", (0, N), None, "normal", surface=0, lab=(20, 6))
    d.force("T", (T * math.cos(al), T * math.sin(al)), None, "tension", rope=(math.cos(al), math.sin(al)))
    d.force("F_mu", (-T * math.cos(al), 0), None, "friction", surface=0, lab=(-16, -16))
    d.component("T_x", "T", (1, 0), lab=(0, 24))
    d.draw()
    axes_hint(f, 70, 320)
    return f.svg()


def malli_hissi_jarru():
    """Model diagram for exercise L3-02: a person in a lift moving up and slowing down (70 kg, a = 1,5 m/s² down)."""
    m, a = 70.0, -1.5
    G = m * g; N = m * (g + a)
    f = Fig("fy45-malli-hissi", 340, "Mallikuvio: ihminen hississä, joka liikkuu ylöspäin ja hidastaa. Vasemmalla hissikori ja ihminen. "
            "Keskellä ihmisen voimakuvio pisteenä: paino G alas ja lattian tukivoima N ylös, lyhyempi kuin paino. Oikealla erillään "
            "ohuet siniset nuolet: nopeus v ylös ja kiihtyvyys a alas. Ne eivät ole voimia.")
    f.rect(30, 60, 130, 240, "none", RULE, 3, rx=4)
    ground(f, 33, 157, 280)
    person(f, 95, 280, 140)
    P = (300, 170)
    f.circle(*P, 7, INK)
    d = FBD(f, 0.17, m=m, a=(0, a), particle=P)
    d.force("G", (0, -G), None, "gravity", lab=(22, -4))
    d.force("N", (0, N), None, "normal", surface=0, lab=(22, 6))
    d.draw()
    d.motion(r"\mathbf{v}", (0, 1), (450, 200), 70)
    d.motion(r"\mathbf{a}", (0, -1), (520, 120), 50)
    return f.svg()


def ruutu():
    """Exercise L1-02: four forces on a point drawn on a grid, 1 square = 10 N; the student reads them off."""
    f = Fig("fy45-ruutu", 330, "Voimakuvio ruudukolla, yksi ruutu vastaa 10 newtonia. Pisteestä lähtee neljä voimaa: F1 oikealle "
            "neljän ruudun mittaisena, F2 vasemmalle kahden ja puolen ruudun mittaisena, F3 ylös kolmen ruudun mittaisena ja "
            "F4 alas kolmen ruudun mittaisena.")
    sq, P = 36, (288, 165)
    for i in range(-6, 8):
        f.line(P[0] + i * sq, 21, P[0] + i * sq, 309, RULE_LIGHT, 1.2)
    for j in range(-4, 5):
        f.line(P[0] - 6 * sq, P[1] + j * sq, P[0] + 7 * sq, P[1] + j * sq, RULE_LIGHT, 1.2)
    f.circle(*P, 6, INK)
    d = FBD(f, sq / 10, a_dir=(1, 0), particle=P)
    d.force("F_1", (40, 0), None, "applied", lab=(18, -16))
    d.force("F_2", (-25, 0), None, "applied", lab=(-10, -18))
    d.force("F_3", (0, 30), None, "applied", lab=(22, 4))
    d.force("F_4", (0, -30), None, "applied", lab=(22, -4))
    d.draw()
    f.rect(470, 280, 36, 4, INK); f.tex(514, 282, r"10\,\text{N}", "start")
    return f.svg()


FIGURES = {"tilanne": tilanne, "suunnat": suunnat, "malli": malli, "komponentit": komponentit, "esimerkki": esimerkki,
           "virhe": virhe_liukuva, "hissi-a": hissi_a, "hissi-b": hissi_b, "hissi-c": hissi_c, "hissi-d": hissi_d,
           "malli-tyonto": malli_tyonto, "malli-pulkka": malli_pulkka, "malli-hissi": malli_hissi_jarru, "ruutu": ruutu}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "tilanne": "reveals: the forces on a box pulled at an angle with friction (a theory figure)",
    "suunnat": "reveals: the force diagrams of a box on a floor and on a slope, a hanging lamp and a helium balloon under a ceiling",
    "malli": "reveals: the point-particle diagram of the pulled box",
    "komponentit": "safe: a force and its components with the trigonometry, no situation",
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
}
