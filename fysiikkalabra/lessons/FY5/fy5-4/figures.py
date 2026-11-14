"""Figures of fy5-4 (scripts/figlib.py, scripts/fbd.py); `python scripts/figures.py fy5-4` writes them into lesson.md.
Uniform circular motion: velocity blue (tangent), acceleration orange (towards the centre), forces red (fbd.py). Every
force diagram is an FBD: the object alone as a plain rectangle (a car seen from behind, a puck seen from the side),
its arrows drawn to scale and its physics checked as it is drawn (the sum of the forces is m a_n towards the centre).
The situation is a separate pictorial situation picture (tilannekuva) behind a dashed rule; no point-particle diagrams."""
import math
from figlib import (Fig, Axes, INK, MUTED, WHITE, RULE, RULE_LIGHT, SAND_LIGHT, SAND, GRAIN, GLASS, ICE, COLD, COLD_LIGHT,
                    GOOD, GOOD_LIGHT, HEAT, HEAT_LIGHT, HOT_LIGHT, IRON, ALUMINIUM, METAL_EDGE, PAPER, n, fi)
from fbd import FBD, ground, VELOCITY, ACCEL, FORCE
import herolib as H
from herolib import grad

g = 9.81
CAR, CAR_EDGE = SAND_LIGHT, INK                         # the car in the situation pictures (not blue: blue is velocity)
ROAD, ROAD_EDGE = ALUMINIUM, METAL_EDGE


def pts(ps): return "M" + " L".join(f"{n(x)},{n(y)}" for x, y in ps)


def thin_arrow(f, x1, y1, x2, y2, col, w=3):
    """A velocity or acceleration arrow in a situation picture: thin, with an open head (fbd.py's style)."""
    L = math.hypot(x2 - x1, y2 - y1); ux, uy = (x2 - x1) / L, (y2 - y1) / L
    f.line(x1, y1, x2 - ux * 2, y2 - uy * 2, col, w)
    for s in (1, -1):
        f.line(x2, y2, x2 - 13 * ux + s * 7 * uy, y2 - 13 * uy - s * 7 * ux, col, w, cap="round")


def car_top(f, x, y, ang, L=46, W=26):
    """A car seen from above, centred at (x, y), heading at ang degrees (0 right, 90 up in the figure)."""
    t = math.radians(ang); ux, uy = math.cos(t), -math.sin(t); px, py = -uy, ux
    P = lambda a, b: (x + a * ux + b * px, y + a * uy + b * py)
    for a in (-0.32, 0.32):
        for b in (-0.5, 0.5):
            cx, cy = P(a * L, b * W)
            f.path(pts([(cx + 6 * ux + 2.5 * px, cy + 6 * uy + 2.5 * py), (cx - 6 * ux + 2.5 * px, cy - 6 * uy + 2.5 * py),
                        (cx - 6 * ux - 2.5 * px, cy - 6 * uy - 2.5 * py), (cx + 6 * ux - 2.5 * px, cy + 6 * uy - 2.5 * py)]) + " Z", INK)
    f.path(pts([P(L / 2, -W / 2 + 3), P(L / 2, W / 2 - 3), P(-L / 2, W / 2 - 1), P(-L / 2, -W / 2 + 1)]) + " Z", CAR, CAR_EDGE, 2.5)
    f.path(pts([P(L * 0.30, -W / 2 + 5), P(L * 0.30, W / 2 - 5), P(L * 0.12, W / 2 - 5), P(L * 0.12, -W / 2 + 5)]) + " Z", GLASS, INK, 1.5)
    f.path(pts([P(-L * 0.30, -W / 2 + 5), P(-L * 0.30, W / 2 - 5), P(-L * 0.18, W / 2 - 5), P(-L * 0.18, -W / 2 + 5)]) + " Z", GLASS, INK, 1.5)


def car_side(f, x, ybot, sc=1.0):
    """A car seen from the side, wheels touching the line y = ybot, centred on x."""
    s = sc
    f.path(f"M{n(x - 40 * s)},{n(ybot - 9 * s)} V{n(ybot - 24 * s)} Q{n(x - 38 * s)},{n(ybot - 28 * s)} {n(x - 26 * s)},{n(ybot - 29 * s)} "
           f"L{n(x - 15 * s)},{n(ybot - 42 * s)} H{n(x + 14 * s)} L{n(x + 27 * s)},{n(ybot - 29 * s)} "
           f"Q{n(x + 40 * s)},{n(ybot - 28 * s)} {n(x + 41 * s)},{n(ybot - 18 * s)} V{n(ybot - 9 * s)} Z", CAR, CAR_EDGE, 2.5)
    f.path(f"M{n(x - 12 * s)},{n(ybot - 38 * s)} H{n(x - 1 * s)} V{n(ybot - 30 * s)} H{n(x - 19 * s)} Z", GLASS, INK, 1.5)
    f.path(f"M{n(x + 3 * s)},{n(ybot - 38 * s)} H{n(x + 12 * s)} L{n(x + 20 * s)},{n(ybot - 30 * s)} H{n(x + 3 * s)} Z", GLASS, INK, 1.5)
    for wx in (-24, 25):
        f.circle(x + wx * s, ybot - 9 * s, 9 * s, INK); f.circle(x + wx * s, ybot - 9 * s, 3.5 * s, ALUMINIUM)


# ---------------------------------------------------------------- the opening illustration
def hero():
    """The chapter's opening illustration: a car in a curve of a snowy country road (no hint of where it would go
    without grip: that is the chapter's prediction)."""
    f = H.hero("fy54-hero", "Kuvitus: talvinen maantie kaartaa metsän läpi oikealle ja katoaa kauas mäkien taakse. Kaarteen keskellä "
               "ajaa henkilöauto takaapäin nähtynä. Tien reunoilla on lumipenkat ja kuusia.")
    H.sky(f, "fy54h", 330, ICE, GLASS)
    H.sun(f, "fy54h", 1060, 92, 38, rays=False)
    H.cloud(f, 250, 86, 1.0); H.cloud(f, 700, 60, 0.75)
    f.path("M0,300 Q220,220 470,262 T900,236 T1200,250 V340 H0 Z", WHITE, RULE, 2)                      # distant snowy hills
    H.forest(f, 300, 46, 30, GOOD, seed=3, x0=0, x1=1200, depth=30)
    f.rect(0, 318, 1200, 282, grad(f, "fy54h-snow", WHITE, GLASS))                                    # the snowy field
    # the road: a centre line (quadratic Bézier) bending right into the distance, its width narrowing with distance
    P0, P1, P2 = (330, 640), (430, 360), (1010, 322)
    def B(t): return ((1 - t) ** 2 * P0[0] + 2 * (1 - t) * t * P1[0] + t * t * P2[0], (1 - t) ** 2 * P0[1] + 2 * (1 - t) * t * P1[1] + t * t * P2[1])
    def T(t):
        dx = 2 * (1 - t) * (P1[0] - P0[0]) + 2 * t * (P2[0] - P1[0]); dy = 2 * (1 - t) * (P1[1] - P0[1]) + 2 * t * (P2[1] - P1[1])
        L = math.hypot(dx, dy); return dx / L, dy / L
    def wid(t): return 470 * (1 - t) ** 1.6 + 22
    left, right, bankL, bankR = [], [], [], []
    for i in range(41):
        t = i / 40; x, y = B(t); tx, ty = T(t); nx, ny = ty, -tx; w = wid(t) / 2
        left.append((x - nx * w, y - ny * w)); right.append((x + nx * w, y + ny * w))
        bankL.append((x - nx * w * 1.18, y - ny * w * 1.18)); bankR.append((x + nx * w * 1.18, y + ny * w * 1.18))
    f.path(pts(bankL + bankR[::-1]) + " Z", WHITE, RULE, 2)
    f.path(pts(left + right[::-1]) + " Z", grad(f, "fy54h-asf", METAL_EDGE, ROAD), IRON, 2)
    for i in range(0, 40, 3):                                                                          # the dashed centre line
        t0, t1 = i / 40, (i + 1.3) / 40
        a, b = B(t0), B(t1); f.line(a[0], a[1], b[0], b[1], WHITE, max(2, wid(t0) * 0.03), cap="round")
    # spruces beside the road, smaller far away
    for (sx, sy, sh) in [(90, 520, 210), (190, 420, 150), (40, 380, 120), (1120, 470, 190), (980, 400, 120), (760, 350, 70), (870, 345, 60)]:
        H.spruce(f, sx, sy, sh)
    # the car seen from behind in the curve
    t = 0.42; x, y = B(t); s = wid(t) / 330
    cw, ch = 150 * s, 92 * s
    f.rect(x - cw / 2, y - ch, cw, ch * 0.78, CAR, CAR_EDGE, 3, 14)
    f.path(f"M{n(x - cw * 0.36)},{n(y - ch)} L{n(x - cw * 0.28)},{n(y - ch * 1.42)} H{n(x + cw * 0.28)} L{n(x + cw * 0.36)},{n(y - ch)} Z", CAR, CAR_EDGE, 3)
    f.path(f"M{n(x - cw * 0.27)},{n(y - ch * 1.04)} L{n(x - cw * 0.22)},{n(y - ch * 1.33)} H{n(x + cw * 0.22)} L{n(x + cw * 0.27)},{n(y - ch * 1.04)} Z", GLASS, INK, 2)
    for k in (-1, 1):
        f.rect(x + k * cw * 0.40 - 9 * s * (k + 1), y - ch * 0.82, 18 * s, 12 * s, HOT_LIGHT, INK, 1.5, 2)
        f.rect(x + k * cw * 0.33 - 13 * s, y - ch * 0.24, 26 * s, 30 * s, INK, None, 0, 5)
    f.rect(x - 24 * s, y - ch * 0.55, 48 * s, 14 * s, WHITE, INK, 1.5, 2)
    return f.svg()


# ---------------------------------------------------------------- theory figures
def muutos():
    """Ydinajatus: the velocity's direction changes; Δv = v2 − v1 points towards the centre (to scale for |v| = 70)."""
    f = Fig("fy54-muutos", 340, "Kaksi kuvaa. Vasemmalla kappale kiertää ympyrärataa vastapäivään tasaisella vauhdilla. Kahdessa kohdassa "
            "radan yläosassa sininen nopeusnuoli v 1 ja v 2 on radan tangentin suuntainen; nuolet ovat yhtä pitkiä mutta eri suuntiin. "
            "Radan ylimmässä kohdassa näiden välissä oranssi kiihtyvyysnuoli a n osoittaa suoraan alas radan keskipisteeseen. "
            "Oikealla samat nopeusnuolet on piirretty samasta pisteestä. Nuolten kärkien välinen nuoli, nopeuden muutos delta v, "
            "osoittaa suoraan alas eli samaan suuntaan kuin kiihtyvyys, kohti radan keskipistettä. Nopeusnuolet ovat molemmissa kuvissa "
            "yhtä pitkiä, samassa mittakaavassa.")
    f.tex(150, 22, r"\text{kappaleen rata}", "middle", MUTED)
    cx, cy, R, L = 160, 200, 105, 70
    f.circle(cx, cy, R, "none", RULE, 2.5)
    f.circle(cx, cy, 5, INK)
    f.tex(cx, cy + 24, r"\text{keskipiste}", "middle", MUTED)
    for deg, lab, d in ((30, r"\overline{v}_1", (22, -10)), (150, r"\overline{v}_2", (-4, 22))):
        t = math.radians(deg); px, py = cx + R * math.cos(t), cy - R * math.sin(t)
        vx, vy = -math.sin(t), -math.cos(t)                                # anticlockwise tangent in figure coordinates
        f.circle(px, py, 11, COLD_LIGHT, INK, 2)
        thin_arrow(f, px + vx * 13, py + vy * 13, px + vx * (13 + L), py + vy * (13 + L), VELOCITY)
        f.tex(px + vx * (13 + L) + d[0], py + vy * (13 + L) + d[1], lab, "middle", VELOCITY)
    f.circle(cx, cy - R, 11, COLD_LIGHT, INK, 2)
    thin_arrow(f, cx, cy - R + 16, cx, cy - R + 72, ACCEL)
    f.tex(cx + 14, cy - R + 56, r"\overline{a}_\text{n}", "start", ACCEL)
    f.line(318, 20, 318, 320, RULE, 1.5, "6 6")
    f.tex(460, 22, r"\text{nopeuden muutos}", "middle", MUTED)
    qx, qy = 540, 150
    a1, a2 = math.radians(30), math.radians(150)
    t1 = (qx - math.sin(a1) * L, qy - math.cos(a1) * L); t2 = (qx - math.sin(a2) * L, qy - math.cos(a2) * L)   # the same length L as on the left
    thin_arrow(f, qx, qy, *t1, VELOCITY); thin_arrow(f, qx, qy, *t2, VELOCITY)
    f.tex(t1[0] + 34, t1[1] - 4, r"\overline{v}_1", "middle", VELOCITY)
    f.tex(t2[0] + 34, t2[1] + 8, r"\overline{v}_2", "middle", VELOCITY)
    f.line(t1[0], t1[1] + 4, t2[0], t2[1] - 16, VELOCITY, 3, "8 6")
    f.path(pts([(t2[0], t2[1] - 2), (t2[0] - 7, t2[1] - 16), (t2[0] + 7, t2[1] - 16)]) + " Z", VELOCITY)
    f.tex(t1[0] - 14, (t1[1] + t2[1]) / 2, r"\Delta\overline{v}", "end", VELOCITY)
    return f.svg()


def kaarre():
    """Ydinajatus: a car in a level left-hand curve; the road's friction is the only horizontal force, towards the centre."""
    m, a = 1000.0, 4.9
    G = m * g
    f = Fig("fy54-kaarre", 380, "Kaksi kuvaa. Vasemmalla tilannekuva ylhäältä: tie kaartaa vasemmalle, ja auto on kaarteessa. Kaarteen "
            "keskipiste on vasemmalla, ja katkoviiva r yhdistää sen autoon. Auton vieressä sininen nopeusnuoli v osoittaa ylös tien "
            "suuntaisesti ja oranssi kiihtyvyysnuoli a n vasemmalle kohti keskipistettä. Oikealla auton voimakuvio takaa katsottuna, "
            "auto suorakulmiona tien päällä: paino G keskipisteestä alas, tien tukivoima N alapinnasta ylös yhtä pitkänä ja tien "
            "kitkavoima alapinnan vasemmasta kulmasta vasemmalle kohti kaarteen keskipistettä, noin puolet painon pituudesta. "
            "Erillään oranssi kiihtyvyysnuoli a n vasemmalle.")
    f.tex(150, 22, r"\text{tilannekuva ylhäältä}", "middle", MUTED)
    cx, cy, R = 40, 200, 175
    f.rect(12, 40, 276, 320, GOOD_LIGHT, None, 0, 10)
    a0, a1 = math.radians(-58), math.radians(58)
    def arc(r, k=24): return [(cx + r * math.cos(a0 + (a1 - a0) * i / k), cy - r * math.sin(a0 + (a1 - a0) * i / k)) for i in range(k + 1)]
    f.path(pts(arc(R + 24) + arc(R - 24)[::-1]) + " Z", ROAD, ROAD_EDGE, 2)
    mid = arc(R)
    for i in range(0, 24, 3): f.line(*mid[i], *mid[i + 1], WHITE, 2.5)
    f.circle(cx, cy, 6, INK)
    f.tex(cx + 4, cy + 26, r"\text{keskipiste}", "start", INK)
    f.line(cx + 8, cy, cx + R - 26, cy, INK, 2, "6 5")
    f.tex(cx + 70, cy - 18, "r", "middle")
    car_top(f, cx + R, cy, 90)
    thin_arrow(f, cx + R + 40, cy + 34, cx + R + 40, cy - 46, VELOCITY)
    f.tex(cx + R + 64, cy - 40, r"\overline{v}", "middle", VELOCITY)
    thin_arrow(f, cx + R - 6, cy + 54, cx + R - 76, cy + 54, ACCEL)
    f.tex(cx + R - 60, cy + 80, r"\overline{a}_\text{n}", "middle", ACCEL)
    f.line(300, 20, 300, 360, RULE, 1.5, "6 6")
    f.tex(450, 22, r"\text{voimakuvio takaa}", "middle", MUTED)
    bx, by, w, h = 470, 196, 110, 60
    ground(f, 360, 588, by + h / 2)
    d = FBD(f, 108 / G, body=(bx, by, w, h), m=m, a=(-a, 0))
    d.force("G", (0, -G), (bx, by), "gravity", lab=(24, -6))
    d.force("N", (0, G), (bx + 22, by + h / 2), "normal", surface=0, lab=(24, 6))
    d.force("F_mu", (-m * a, 0), (bx - w / 2, by + h / 2), "friction", surface=0, lab=(-6, 22))
    d.draw()
    d.motion(r"\overline{a}_\text{n}", (-1, 0), (bx - 30, by - 64), 64)
    return f.svg()


def kuvaaja():
    """Kaava: a_n = v²/r against v for r = 50 m (solid) and r = 100 m (dashed); points at v = 10 and 20 m/s for r = 50 m."""
    f = Fig("fy54-kuvaaja", 360, "Kuvaaja mittakaavassa: vaaka-akselilla ratanopeus v metreinä sekunnissa nollasta 30:een, pystyakselilla "
            "normaalikiihtyvyys a n metreinä sekunnissa toiseen nollasta 18:aan. Kaksi oranssia käyrää nousee origosta yhä jyrkemmin. "
            "Säteellä 50 metriä yhtenäinen käyrä: nopeudella 10 kiihtyvyys on 2, nopeudella 20 se on 8 ja nopeudella 30 se on 18. "
            "Säteellä 100 metriä katkoviivakäyrä on puolet alempana: nopeudella 20 kiihtyvyys on 4 ja nopeudella 30 se on 9. "
            "Pisteet nopeuksilla 10 ja 20 on merkitty yhtenäiselle käyrälle apuviivoin.")
    ax = Axes(f, (86, 300), (420, 60), x=(0, 30), y=(0, 18), xticks=[5, 10, 15, 20, 25, 30], yticks=[3, 6, 9, 12, 15, 18],
              xlabel=r"v\ (\text{m/s})", ylabel=r"a_\text{n}\ (\text{m/s}^2)")
    ax.curve(lambda v: v * v / 50, 0, 30, HEAT, 3)
    ax.curve(lambda v: v * v / 100, 0, 30, HEAT, 3, dash="9 7")
    for v in (10, 20):
        ax.guide(v, v * v / 50); ax.point(v, v * v / 50, HEAT)
    f.tex(ax.X(30) + 10, ax.Y(18), r"r = 50\,\text{m}", "start", HEAT)
    f.tex(ax.X(30) + 10, ax.Y(9), r"r = 100\,\text{m}", "start", HEAT)
    return f.svg()


def kuvaaja_a():
    """Task fy5-4-L2-09: a_n against v of an unknown level curve (r = 75 m, not stated); the marked point (15, 3,0) is read."""
    f = Fig("fy54-kuvaaja-a", 360, "Kuvaaja mittakaavassa: auton normaalikiihtyvyys a n metreinä sekunnissa toiseen ratanopeuden v funktiona "
            "kaarteessa. Vaaka-akselilla ratanopeus nollasta 30 metriin sekunnissa, apuviivat ja lukuarvot viiden välein; pystyakselilla "
            "normaalikiihtyvyys nollasta 12:een, apuviivat yhden välein ja lukuarvot kahden välein. Oranssi käyrä nousee origosta yhä "
            "jyrkemmin. Käyrälle on merkitty piste apuviivoin: nopeudella 15 normaalikiihtyvyys on 3.")
    ax = Axes(f, (86, 300), (420, 60), x=(0, 30), y=(0, 12), xticks=[5, 10, 15, 20, 25, 30], yticks=list(range(1, 13)),
              xlabel=r"v\ (\text{m/s})", ylabel=r"a_\text{n}\ (\text{m/s}^2)", yfmt=lambda t: fi(t) if t % 2 == 0 else "")
    ax.curve(lambda v: v * v / 75, 0, 29, HEAT, 3)
    ax.guide(15, 3.0); ax.point(15, 3.0, HEAT)
    return f.svg()


def kuvaaja_b():
    """Task fy5-4-L3-06: the friction force a car of 1200 kg needs against v in a level curve (r = 60 m, not stated); point (20, 8,0)."""
    f = Fig("fy54-kuvaaja-b", 360, "Kuvaaja mittakaavassa: kaarteessa ajavan auton tarvitsema kitkavoima F newtoneina tuhansina eli kilonewtoneina "
            "ratanopeuden v funktiona. Vaaka-akselilla ratanopeus nollasta 25 metriin sekunnissa, apuviivat ja lukuarvot viiden välein; "
            "pystyakselilla voima nollasta 12 kilonewtoniin, apuviivat yhden välein ja lukuarvot kahden välein. Punainen käyrä nousee "
            "origosta yhä jyrkemmin. Käyrälle on merkitty piste apuviivoin: nopeudella 20 voima on 8.")
    ax = Axes(f, (86, 300), (420, 60), x=(0, 25), y=(0, 12), xticks=[5, 10, 15, 20, 25], yticks=list(range(1, 13)),
              xlabel=r"v\ (\text{m/s})", ylabel=r"F\ (\text{kN})", yfmt=lambda t: fi(t) if t % 2 == 0 else "")
    ax.curve(lambda v: 1.2 * v * v / 60, 0, 24, FORCE, 3)
    ax.guide(20, 8.0); ax.point(20, 8.0, FORCE)
    return f.svg()


def nyppyla():
    """Kaava: a car at the top of a bump and at the bottom of a dip at the same speed; N < G on the bump, N > G in the dip."""
    m, G, an = 10.0, 100.0, 4.0
    f = Fig("fy54-nyppyla", 420, "Neljä kuvaa kahdessa sarakkeessa. Vasemmalla ylhäällä auto nyppylän huipulla, oikealla ylhäällä auto "
            "notkon pohjalla; kummassakin auto ajaa samalla nopeudella oikealle. Alla kummankin auton voimakuvio, auto suorakulmiona: "
            "paino G keskipisteestä alas ja tien tukivoima N alapinnasta ylös. Nyppylän huipulla tukivoima on lyhyempi kuin paino, "
            "noin kuusi kymmenesosaa siitä, ja oranssi kiihtyvyysnuoli a n osoittaa alas, kohti nyppylän kaaren keskipistettä. "
            "Notkon pohjalla tukivoima on pidempi kuin paino, noin 1,4-kertainen, ja kiihtyvyysnuoli osoittaa ylös, kohti notkon "
            "kaaren keskipistettä. Paino on molemmissa yhtä pitkä.")
    f.tex(150, 22, r"\text{nyppylän huippu}", "middle", MUTED)
    f.tex(450, 22, r"\text{notkon pohja}", "middle", MUTED)
    f.path("M16,132 C80,132 100,84 150,84 C200,84 220,132 284,132 V146 H16 Z", SAND_LIGHT, GRAIN, 2.5)
    car_side(f, 150, 85, 0.9)
    f.path("M316,64 C380,64 400,124 450,124 C500,124 520,64 584,64 V146 H316 Z", SAND_LIGHT, GRAIN, 2.5)
    car_side(f, 450, 125, 0.9)
    f.line(300, 20, 300, 410, RULE, 1.5, "6 6")
    f.line(16, 156, 584, 156, RULE_LIGHT, 1.5)
    s = 1.0
    for bx, Nv, adir in ((150, G - m * an, -1), (450, G + m * an, 1)):
        by, w, h = 290, 100, 36
        ground(f, bx - 90, bx + 90, by + h / 2)
        d = FBD(f, s, body=(bx, by, w, h), m=m, a=(0, adir * an))
        d.force("G", (0, -G), (bx, by), "gravity", lab=(-22, -4))
        d.force("N", (0, Nv), (bx + 20, by + h / 2), "normal", surface=0, lab=(32, 10))
        d.draw()
        d.motion(r"\overline{a}_\text{n}", (0, adir), (bx + 90, by - 56 if adir < 0 else by + 20), 52, lab=(24, 0))
    return f.svg()


EX = dict(m=1200.0, r=45.0, v=54 / 3.6)     # the worked example's data (lesson-answers.py computes the same)


def esimerkki():
    """The worked example's force diagram: a car in a level curve seen from behind, centre to the right; x towards the
    centre (right), y up, as in the exercise solutions."""
    m, r, v = EX["m"], EX["r"], EX["v"]
    an = v * v / r; G = m * g
    f = Fig("fy54-esimerkki", 360, "Auton voimakuvio takaa katsottuna, auto suorakulmiona tien päällä. Kaarteen keskipiste on oikealla. "
            "Paino G keskipisteestä alas, tien tukivoima N alapinnasta ylös yhtä pitkänä ja tien kitkavoima alapinnan oikeasta "
            "kulmasta oikealle kohti kaarteen keskipistettä, noin puolet painon pituudesta. Erillään oranssi kiihtyvyysnuoli a n "
            "oikealle. Nurkassa akselit: x oikealle kohti keskipistettä ja y ylös.")
    bx, by, w, h = 270, 170, 150, 76
    ground(f, 80, 440, by + h / 2)
    d = FBD(f, 130 / G, body=(bx, by, w, h), m=m, a=(an, 0))
    d.force("G", (0, -G), (bx, by), "gravity", lab=(26, -4))
    d.force("N", (0, G), (bx - 24, by + h / 2), "normal", surface=0, lab=(-26, 8))
    d.force("F_mu", (m * an, 0), (bx + w / 2, by + h / 2), "friction", surface=0, lab=(4, 24))
    d.draw()
    d.motion(r"\overline{a}_\text{n}", (1, 0), (bx + 40, by - 80), 70)
    f.tex(580, 40, r"\text{kohti keskipistettä}", "end", MUTED)
    ax, ay, L = 52, 318, 44
    f.arrow(ax, ay, ax + L, ay, MUTED, 2, 10); f.arrow(ax, ay, ax, ay - L, MUTED, 2, 10)
    f.tex(ax + L + 14, ay, "x", "middle", MUTED); f.tex(ax, ay - L - 14, "y", "middle", MUTED)
    return f.svg()


# ---------------------------------------------------------------- task figures (shown by id from inquiry.json)
def virhe():
    """Find the error: a car at the top of a bump, with an extra upward 'centrifugal force' drawn by a student."""
    f = Fig("fy54-virhe", 340, "Opiskelijan piirtämä voimakuvio autosta, joka ajaa nyppylän huipun yli; auto suorakulmiona. "
            "Keskipisteestä nuoli G suoraan alas. Alapinnasta nuoli N suoraan ylös, lyhyempi kuin G. Yläpinnan keskeltä nuoli "
            "F kp suoraan ylös. Nuolet N ja F kp ovat yhteensä yhtä pitkät kuin G.")
    bx, by, w, h = 300, 180, 140, 50
    ground(f, 160, 440, by + h / 2)
    d = FBD(f, 1.1, body=(bx, by, w, h), wrong="an invented upward 'centrifugal force' F_kp: nothing exerts it, and with it the forces sum to zero although the car accelerates down towards the centre")
    d.force("G", (0, -100), (bx, by), "gravity", lab=(-24, -4))
    d.force("N", (0, 60), (bx + 30, by + h / 2), "normal", surface=0, lab=(54, 8))
    d.force("F_kp", (0, 40), (bx - 20, by - h / 2), "other", tex=r"\overline{F}_\text{kp}", lab=(-34, 4))
    d.draw()
    return f.svg()


VALITSE = "Auton voimakuvio, auto suorakulmiona. "


def _valitse(name, desc, Nv, wrong=None, extra=False):
    """An option of the diagram-selection task: a car at the bottom of a dip at constant speed."""
    f = Fig(f"fy54-valitse-{name}", 300, desc, width=300)
    bx, by, w, h = 150, 170, 104, 30
    d = FBD(f, 1.1, body=(bx, by, w, h), a_dir=None if wrong else (0, 1), wrong=wrong)
    d.force("G", (0, -80), (bx, by), "gravity", lab=(22, -4))
    d.force("N", (0, Nv), (bx + 22, by + h / 2), "normal", surface=0, lab=(48, 12))
    if extra: d.force("F_kp", (0, -40), (bx - 34, by + h / 2), "other", tex=r"\overline{F}_\text{kp}", lab=(-40, -6))
    ground(f, 40, 260, by + h / 2)
    d.draw()
    return f.svg()


def valitse_a():
    return _valitse("a", VALITSE + "Paino G keskipisteestä alas ja tukivoima N alapinnasta ylös; tukivoima on noin puolitoista kertaa niin pitkä kuin paino.", 120)


def valitse_b():
    return _valitse("b", VALITSE + "Paino G keskipisteestä alas ja tukivoima N alapinnasta ylös; nuolet ovat yhtä pitkät.", 80,
                    wrong="N equal to G: the forces cancel although the car accelerates up towards the centre of the dip")


def valitse_c():
    return _valitse("c", VALITSE + "Paino G keskipisteestä alas ja tukivoima N alapinnasta ylös; tukivoima on noin puolet painon pituudesta.", 40,
                    wrong="N smaller than G: the net force points down, away from the centre of the dip")


def valitse_d():
    return _valitse("d", VALITSE + "Paino G keskipisteestä alas, tukivoima N alapinnasta ylös noin puolitoista kertaa painon pituisena ja "
                    "alapinnasta alas nuoli F kp, puolet painon pituudesta.", 120, extra=True,
                    wrong="an invented downward 'centrifugal force' F_kp cancels the net force that points to the centre")


def malli_kiekko():
    """Model diagram for the drawing task: an ice-hockey puck on a cord sliding on smooth ice in a horizontal circle, seen
    from the side; the centre (the peg) to the left. m = 0,17 kg, v = 1,5 m/s, r = 0,50 m (lesson-answers.py)."""
    m, v, r = 0.17, 1.5, 0.50
    an = v * v / r; G = m * g; T = m * an
    f = Fig("fy54-malli-kiekko", 340, "Mallikuvio: jääkiekko liukuu narun varassa vaakasuoraa ympyrää jäällä, kuvattuna sivulta; "
            "naru ja ympyrän keskipiste ovat vasemmalla. Kuviossa on vain kiekko suorakulmiona jään päällä. Paino G keskipisteestä "
            "alas. Jään tukivoima N alapinnasta ylös yhtä pitkänä. Narun jännitysvoima T vasemman sivun keskeltä vaakasuoraan "
            "vasemmalle kohti keskipistettä, vajaa puolet painon pituudesta. Erillään oranssi kiihtyvyysnuoli a n vasemmalle. "
            "Nurkassa akselit: x vasemmalle kohti keskipistettä ja y ylös.")
    bx, by, w, h = 330, 180, 140, 56
    ground(f, 160, 500, by + h / 2)
    d = FBD(f, 120 / G, body=(bx, by, w, h), m=m, a=(-an, 0))
    d.force("G", (0, -G), (bx, by), "gravity", lab=(26, -4))
    d.force("N", (0, G), (bx + 24, by + h / 2), "normal", surface=0, lab=(26, 8))
    d.force("T", (-T, 0), (bx - w / 2, by), "tension", rope=(-1, 0), lab=(-8, -22))
    d.draw()
    d.motion(r"\overline{a}_\text{n}", (-1, 0), (bx - 40, by - 76), 70)
    ax, ay, L = 548, 304, 44
    f.arrow(ax, ay, ax - L, ay, MUTED, 2, 10); f.arrow(ax, ay, ax, ay - L, MUTED, 2, 10)
    f.tex(ax - L - 14, ay, "x", "middle", MUTED); f.tex(ax, ay - L - 14, "y", "middle", MUTED)
    return f.svg()



# Voimakuvion valinta (task fy5-4-L2-08, docs/exercise-types.md type 3): a roller-coaster car passes the top of a
# vertical loop upside down, the track above it, with a_n = 1,5 g, so the track pushes it down with N = 0,5 G and both
# forces point down towards the centre (below). Four option diagrams to one scale (G = 80 units, N = 40 units); only
# "pick-alas" is right, each other has one error.
PK_BODY = (150, 195, 104, 36)
PK_G, PK_N, PK_S = 80, 40, 1.3
PK_DESC = "Vuoristoradan vaunun voimakuvio, vaunu suorakulmiona. Keskipisteestä alaspäin osoittaa paino G. "


def _pick(name, desc, n_up=False, kp=False, v_force=False, wrong=None):
    """An option of task fy5-4-L2-08: G from the centre; the track's normal force N a push from above ending at the top
    face (the track above pushes the car down towards the centre) or, as an error, a push from below ending at the
    bottom face as on a floor; kp adds an invented upward 'centrifugal force' F_kp from the top face; v_force draws the
    velocity into the diagram as if it were a force (in velocity blue)."""
    bx, by, w, h = PK_BODY
    f = Fig(f"fy54-pick-{name}", 320, desc, width=300)
    d = FBD(f, PK_S, body=PK_BODY, a_dir=None if wrong else (0, -1), wrong=wrong)
    d.force("G", (0, -PK_G), (bx, by), "gravity", lab=(-24, -6))
    if n_up: d.force("N", (0, PK_N), (bx + 30, by + h / 2), "normal", surface=0, push=True, lab=(24, 0))
    else: d.force("N", (0, -PK_N), (bx + 30, by - h / 2), "normal", surface=0, outward=(0, -1), push=True, lab=(24, 0))
    if kp: d.force("F_kp", (0, PK_G + PK_N), (bx - 30, by - h / 2), "other", tex=r"\overline{F}_\text{kp}", lab=(-40, 8))
    d.draw()
    if v_force:                                                    # the error: the velocity drawn into the force diagram
        x1, y = bx + w / 2, by                                     # like a force, but in velocity blue (it is no force)
        f.arrow(x1, y, x1 + PK_N * PK_S, y, VELOCITY, 4, 18)
        f.tex(x1 + PK_N * PK_S - 10, y - 26, r"\overline{v}", "middle", VELOCITY)
    return f.svg()


def pick_alas():
    return _pick("alas", PK_DESC + "Yläpuolelta tuleva tukivoima N osoittaa suoraan alaspäin ja päättyy yläpintaan; se on puolet painon pituudesta.")


def pick_keskipako():
    return _pick("keskipako", PK_DESC + "Yläpuolelta tuleva tukivoima N osoittaa suoraan alaspäin ja päättyy yläpintaan; se on puolet painon pituudesta. Yläpinnan "
                 "vasemmalta puolelta lähtee nuoli F kp suoraan ylöspäin, puolitoista kertaa painon pituisena.", kp=True,
                 wrong="an invented upward 'centrifugal force' F_kp: nothing exerts it, and with it the forces cancel although the car accelerates down towards the centre")


def pick_ylos():
    return _pick("ylos", PK_DESC + "Alapuolelta tuleva tukivoima N osoittaa suoraan ylöspäin ja päättyy alapintaan; se on puolet painon pituudesta.", n_up=True,
                 wrong="the normal force drawn up as on a floor: the track is above the car and pushes it down, and with N up the net force is only 0,5 G, not 1,5 G")


def pick_nopeus():
    return _pick("nopeus", PK_DESC + "Yläpuolelta tuleva tukivoima N osoittaa suoraan alaspäin ja päättyy yläpintaan; se on puolet painon pituudesta. Oikeasta "
                 "kyljestä lähtee sininen nopeuden nuoli v vaakasuoraan oikealle, yhtä pitkänä kuin tukivoima.", v_force=True,
                 wrong="the velocity v drawn as a force")

FIGURES = {"hero": hero, "muutos": muutos, "kaarre": kaarre, "kuvaaja": kuvaaja, "kuvaaja-a": kuvaaja_a, "kuvaaja-b": kuvaaja_b, "nyppyla": nyppyla, "esimerkki": esimerkki,
           "virhe": virhe, "valitse-a": valitse_a, "valitse-b": valitse_b, "valitse-c": valitse_c, "valitse-d": valitse_d,
           "malli-kiekko": malli_kiekko, "pick-alas": pick_alas, "pick-keskipako": pick_keskipako, "pick-ylos": pick_ylos,
           "pick-nopeus": pick_nopeus}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "hero": "decorative",
    "muutos": "reveals: the velocity change and the normal acceleration of uniform circular motion point to the centre (a theory figure)",
    "kaarre": "reveals: the force diagram of a car in a level curve, friction towards the centre (a theory figure)",
    "kuvaaja": "reveals: a_n = v²/r against v for r = 50 m and 100 m (a theory graph)",
    "kuvaaja-a": "safe: a_n(v) of a level curve, point (15 m/s, 3,0 m/s²) marked, radius not stated (task fy5-4-L2-09)",
    "kuvaaja-b": "safe: friction force F(v) of a 1200 kg car in a level curve, point (20 m/s, 8,0 kN) marked, radius not stated (task fy5-4-L3-06)",
    "nyppyla": "reveals: N < G at the top of a bump and N > G at the bottom of a dip (a theory figure)",
    "esimerkki": "reveals: the force diagram of the worked example (car in a level curve)",
    "virhe": "safe: a deliberately wrong diagram (an invented centrifugal force) for error-finding; its description lists the arrows, not the error",
    "valitse-a": "reveals: the right diagram for a car at the bottom of a dip (an option figure)",
    "valitse-b": "safe: a wrong option (N equal to G) for diagram selection",
    "valitse-c": "safe: a wrong option (N smaller than G) for diagram selection",
    "valitse-d": "safe: a wrong option (an extra centrifugal force) for diagram selection",
    "malli-kiekko": "reveals: the model diagram of a puck on a cord in a horizontal circle (shown after the attempt)",
    "pick-alas": "reveals: the right option of task fy5-4-L2-08 (a roller-coaster car at the top of a loop: G and N both down)",
    "pick-keskipako": "safe: a wrong option of task fy5-4-L2-08 (an invented upward centrifugal force F_kp)",
    "pick-ylos": "safe: a wrong option of task fy5-4-L2-08 (the track's normal force drawn up as on a floor)",
    "pick-nopeus": "safe: a wrong option of task fy5-4-L2-08 (the velocity, a blue arrow, drawn into the force diagram as if it were a force)",
}
