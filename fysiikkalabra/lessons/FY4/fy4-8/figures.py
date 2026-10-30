"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy4-8` writes them into lesson.md."""
import math
from figlib import (Fig, INK, MUTED, WHITE, RULE, RULE_LIGHT, HEAT, HEAT_LIGHT, HOT, HOT_LIGHT, COLD, COLD_LIGHT, GOOD,
                    GOOD_LIGHT, ALUMINIUM, METAL_EDGE, IRON, SAND_LIGHT, SAND, GLASS, ICE, PAPER, n)
import herolib as H

RED = "#c92a2a"        # forces
BLUE = COLD            # velocity (#1971c2)
GREEN = GOOD           # potential energy
HEATC = HEAT           # work of friction: energy to internal energy (#e8590c)


def car(f, x, y, ang, L=36, Hh=15, body=HOT):
    """A coaster car standing on the track point (x, y), tilted by ang (radians, y up): wheels, a red body, two heads."""
    c, s = math.cos(ang), math.sin(ang)
    def P(u, v): return (x + u * c + v * s, y - u * s + v * c)       # u along the track, v down from the track (screen y)
    for u in (-L * 0.3, L * 0.3):
        wx, wy = P(u, -Hh * 0.22); f.circle(wx, wy, Hh * 0.24, INK)
    pts = [P(-L / 2, -Hh * 0.35), P(L / 2, -Hh * 0.35), P(L / 2, -Hh * 1.3), P(-L / 2, -Hh * 1.3)]
    f.path("M" + " L".join(f"{n(a)},{n(b)}" for a, b in pts) + " Z", body, INK, 2)
    for u in (-L * 0.15, L * 0.2):
        hx, hy = P(u, -Hh * 1.65); f.circle(hx, hy, Hh * 0.32, SAND_LIGHT, INK, 1.5)


def laakso():
    """Ydinajatus: a car rolls without friction through a curved valley; four positions and their energy bars."""
    f = Fig("fy48-laakso", 380, "Kaavakuva, ei mittakaavassa: vuoristoradan vaunu kaarevassa laaksossa ilman kitkaa ja ilmanvastusta. "
            "Vaunu lähtee levosta vasemmalta korkeudelta h (kohta 1), ohittaa puolen korkeuden (kohta 2) ja laakson pohjan (kohta 3) ja "
            "pysähtyy oikealla samalle korkeudelle h (kohta 4). Siniset nuolet ovat vaunun nopeus, pohjalla suurin. Alla kunkin kohdan "
            "energiapalkit: vihreä potentiaalienergia ja sininen liike-energia. Kohdassa 1 ja 4 on vain potentiaalienergiaa, kohdassa 3 "
            "vain liike-energiaa ja kohdassa 2 puolet kumpaakin. Palkkien summa on joka kohdassa yhtä suuri.")
    r, cy0, bl, br, bot = 150, 72, 250, 350, 222
    def pt(side, th):                     # side −1 left, +1 right; th from the bottom of the arc
        x0 = bl if side < 0 else br
        return x0 + side * r * math.sin(th), bot - r * (1 - math.cos(th))
    # ground and supports
    f.rect(14, bot + 14, 572, 10, SAND_LIGHT)
    for k in range(9):
        th = 0.15 + k * 0.17
        for side in (-1, 1):
            x, y = pt(side, th)
            if th < 1.37: f.line(x, y + 5, x, bot + 14, ALUMINIUM, 3)
    d = [pt(-1, 1.37 - i * 1.37 / 40) for i in range(41)] + [pt(1, i * 1.37 / 40) for i in range(41)]
    f.path("M" + " L".join(f"{n(a)},{n(b)}" for a, b in d), stroke=METAL_EDGE, w=6)
    f.path("M" + " L".join(f"{n(a)},{n(b - 1)}" for a, b in d), stroke=WHITE, w=1.5)
    # start height h: dashed line, dimension on the left
    th1 = math.acos(1 - 100 / r)
    xA, yA = pt(-1, th1); xD, yD = pt(1, th1)
    f.line(78, yA, 540, yA, MUTED, 1.5, "6 5")
    f.line(52, bot, 52, yA, INK, 2)
    f.path(f"M52,{n(yA)} l-6,12 h12 Z", INK); f.path(f"M52,{bot} l-6,-12 h12 Z", INK)
    f.tex(38, (yA + bot) / 2, "h", "end")
    f.line(40, bot, 78, bot, MUTED, 1.5, "6 5")
    # four positions: 1 start (rest), 2 half height, 3 bottom, 4 the same height on the right (rest)
    th2 = math.acos(1 - 50 / r)
    P = [(pt(-1, th1), -th1, 0.0), (pt(-1, th2), -th2, math.sqrt(0.5)), ((300, bot), 0.0, 1.0), (pt(1, th1), th1, 0.0)]
    for i, ((x, y), ang, v) in enumerate(P):
        car(f, x, y, ang if i != 3 else th1, 30, 13)
        if v:
            c, s = math.cos(ang), math.sin(ang)
            # velocity along the track, drawn above the car; down the slope at 2 means to the right and down
            ox, oy = (x + 8, y - 34) if i == 1 else (x, y - 30)
            L = 58 * v
            dx, dy = (math.cos(th2), math.sin(th2)) if i == 1 else (1, 0)
            f.arrow(ox, oy, ox + dx * L, oy + dy * L, BLUE, 3, 12)
    labels = [(xA - 22, yA - 34), (P[1][0][0] - 34, P[1][0][1] - 6), (274, bot - 46), (xD + 24, yD - 34)]
    for i, (lx, ly) in enumerate(labels): f.tex(lx, ly, str(i + 1), "middle")
    f.tex(392, bot - 34, r"\overline{v}", "start", BLUE)
    # energy bars: one group per position, the total the same height everywhere
    base, tot = 352, 70
    f.line(70, base, 560, base, INK, 2)
    for i, x in enumerate((130, 250, 370, 490)):
        ep = (1.0, 0.5, 0.0, 1.0)[i]
        if ep: f.rect(x - 22, base - tot * ep, 20, tot * ep, GREEN)
        if 1 - ep: f.rect(x + 2, base - tot * (1 - ep), 20, tot * (1 - ep), BLUE)
        f.tex(x, base - tot - 18, str(i + 1), "middle")
    f.rect(24, 290, 16, 16, GREEN); f.tex(46, 298, r"E_\text{p}", "start", GREEN)
    f.rect(24, 326, 16, 16, BLUE); f.tex(46, 334, r"E_\text{k}", "start", BLUE)
    return f.svg()


def tyo():
    """Ydinajatus: the sign of work: a force along the motion, against it, and perpendicular to it."""
    f = Fig("fy48-tyo", 330, "Kaavakuva kolmesta tilanteesta, joissa laatikko liikkuu lattialla oikealle; sininen nuoli on laatikon "
            "nopeus. Vasemmalla laatikkoa vedetään liikkeen suuntaan voimalla F, joten voima tekee positiivista työtä, W > 0. Keskellä "
            "kitkavoima F_μ vaikuttaa lattian pinnasta liikettä vastaan, joten se tekee negatiivista työtä, W < 0. Oikealla lattian "
            "tukivoima N on kohtisuorassa liikettä vastaan, joten se ei tee työtä, W = 0.")
    for k, x0 in enumerate((0, 200, 400)):
        if k: f.line(x0, 20, x0, 310, RULE, 2, "6 6")
        cx = x0 + 100; fy = 210
        f.rect(x0 + 14, fy, 172, 10, SAND_LIGHT); f.line(x0 + 14, fy, x0 + 186, fy, INK, 2)
        f.rect(cx - 36, fy - 56, 72, 56, SAND, INK, 2.5, 3)
        f.line(cx - 36, fy - 28, cx + 36, fy - 28, INK, 1.5)
        f.arrow(cx - 34, 62, cx + 34, 62, BLUE, 3, 12); f.tex(cx + 40, 62, r"\overline{v}", "start", BLUE)
        if k == 0:
            f.arrow(cx + 36, fy - 28, cx + 92, fy - 28, RED, 4, 15); f.tex(cx + 74, fy - 56, r"\overline{F}", "middle", RED)
            f.tex(cx, 262, r"W > 0", "middle")
            f.tex(cx, 296, r"\text{liikkeen suuntaan}", "middle", w=180)
        elif k == 1:
            f.arrow(cx + 20, fy, cx - 54, fy, RED, 4, 15); f.tex(cx - 62, fy - 26, r"\overline{F}_\mu", "middle", RED)
            f.tex(cx, 262, r"W < 0", "middle")
            f.tex(cx, 296, r"\text{liikettä vastaan}", "middle", w=180)
        else:
            f.arrow(cx + 14, fy, cx + 14, fy - 112, RED, 4, 15); f.tex(cx + 28, fy - 96, r"\overline{N}", "start", RED)
            f.tex(cx, 262, r"W = 0", "middle")
            f.tex(cx, 296, r"\text{kohtisuoraan}", "middle", w=180)
    return f.svg()


def palkit():
    """Kaava: the energy principle as bars, schematic but to scale: E_p,1 = 100, W_muut = −40, E_k,2 = 60 units."""
    f = Fig("fy48-palkit", 360, "Energiapalkit, kaavakuva mittakaavassa: alussa kappaleella on vain potentiaalienergiaa E_p,1, "
            "liike-energia E_k,1 on nolla. Kitka tekee negatiivisen työn W_muut, jonka palkki osoittaa nollatasosta alaspäin. Lopussa "
            "kappaleella on vain liike-energiaa E_k,2 ja potentiaalienergia E_p,2 on nolla. Katkoviiva alun mekaanisen energian "
            "korkeudella näyttää, että loppuenergia on alkuenergiaa pienempi juuri kitkan työn verran.")
    zero, k = 232, 1.6
    f.tex(120, 26, r"\text{alussa}", "middle"); f.tex(480, 26, r"\text{lopussa}", "middle")
    f.line(30, zero, 570, zero, INK, 2)
    f.rect(140, zero - 100 * k, 40, 100 * k, GREEN)
    f.rect(280, zero, 40, 40 * k, HEATC)
    f.rect(420, zero - 60 * k, 40, 60 * k, BLUE)
    f.tex(230, 150, "+", "middle"); f.tex(370, 150, "=", "middle")
    f.line(180, zero - 100 * k, 540, zero - 100 * k, MUTED, 1.5, "6 5")
    f.path(f"M470,{n(zero - 100 * k)} h8 V{n(zero - 60 * k)} h-8", stroke=HEATC, w=2.5)
    f.tex(486, zero - 80 * k, r"|W_\text{muut}|", "start", HEATC)
    for x, s, c in ((80, r"E_{\text{k},1}", BLUE), (160, r"E_{\text{p},1}", GREEN), (300, r"W_\text{muut}", HEATC),
                    (440, r"E_{\text{k},2}", BLUE), (520, r"E_{\text{p},2}", GREEN)):
        f.tex(x, 332, s, "middle", c)
    f.tex(80, zero - 18, "0", "middle", MUTED); f.tex(520, zero - 18, "0", "middle", MUTED)
    return f.svg()


def hero():
    """The chapter's opening illustration: an amusement-park roller coaster whose first hill is the highest."""
    f = H.hero("fy48-hero", "Kuvitus: huvipuiston vuoristorata kesäpäivänä. Vasemmalla nousee radan ensimmäinen ja korkein mäki, "
               "jonka huipulle punainen juna on juuri noussut. Sen jälkeen rata laskee syvään laaksoon ja nousee toiselle mäelle, joka "
               "on selvästi matalampi, ja sen jälkeen vielä matalammalle kolmannelle mäelle. Radan alla on valkoiset tukipylväät, ja "
               "taustalla on kuusimetsää.")
    H.sky(f, "fy48h", 540)
    H.sun(f, "fy48h", 1060, 100, 52)
    H.cloud(f, 230, 90, 1.0); H.cloud(f, 760, 70, 0.75)
    H.forest(f, 470, 60, 30, METAL_EDGE, seed=3)
    f.rect(0, 500, 1200, 100, H.grad(f, "fy48h-grass", GOOD_LIGHT, GOOD, y1=500, y2=900))
    # the track: smooth hills by cosine interpolation, heights to scale: 390, 260 and 170 units above the ground
    K = [(40, 500), (500, 110), (690, 470), (850, 240), (970, 440), (1090, 330), (1200, 420)]
    def y_at(x):
        for (x0, y0), (x1, y1) in zip(K, K[1:]):
            if x0 <= x <= x1:
                t = (x - x0) / (x1 - x0); return y0 + (y1 - y0) * (1 - math.cos(math.pi * t)) / 2
        return K[-1][1]
    xs = [40 + i * 4 for i in range(291)]
    # supports and cross bracing
    prev = None
    for x in range(120, 1200, 40):
        y = y_at(x)
        f.line(x, y + 8, x, 508, WHITE, 6); f.line(x, y + 8, x, 508, ALUMINIUM, 2)
        if prev:
            px, py = prev
            top = max(y, py) + 14
            if 508 - top > 40: f.line(px, top, x, 508, ALUMINIUM, 2); f.line(px, 508, x, top, ALUMINIUM, 2)
        prev = (x, y)
    f.path("M" + " L".join(f"{n(x)},{n(y_at(x))}" for x in xs), stroke=INK, w=12)
    f.path("M" + " L".join(f"{n(x)},{n(y_at(x) - 2)}" for x in xs), stroke=HOT, w=5)
    for x in xs[::5]: f.line(x, y_at(x) + 2, x, y_at(x) + 9, IRON, 3)
    # the chain lift's housing at the bottom of the first hill
    f.rect(52, 456, 90, 50, SAND_LIGHT, INK, 3, 4); f.path("M44,456 L97,424 L150,456 Z", IRON, INK, 3)
    f.rect(84, 474, 26, 32, GLASS, INK, 2)
    # the train just over the crest of the first hill
    x, run, targets = 440.0, 0.0, [0, 50, 100]          # car centres 50 units apart along the track, the last just over the crest
    for k, goal in enumerate(targets):
        while run < goal:
            run += math.hypot(0.5, y_at(x + 0.5) - y_at(x)); x += 0.5
        dy = (y_at(x + 2) - y_at(x - 2)) / 4
        car(f, x, y_at(x) - 6, -math.atan(dy), 46, 24, HOT if k != 1 else HEAT)
    # visitors on the ground and two spruces
    for x, c in ((300, COLD), (340, HEAT), (378, GOOD)):
        f.circle(x, 520, 9, SAND_LIGHT); f.rect(x - 8, 530, 16, 30, c, rx=5); f.line(x - 4, 560, x - 4, 578, INK, 4); f.line(x + 4, 560, x + 4, 578, INK, 4)
    H.spruce(f, 1150, 560, 150); H.spruce(f, 640, 540, 110)
    return f.svg()


FIGURES = {"hero": hero, "laakso": laakso, "tyo": tyo, "palkit": palkit}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "laakso": "reveals: mechanical energy is conserved without friction (equal bar totals, the same height on both sides)",
    "tyo": "reveals: the sign of the work of a force along, against and perpendicular to the motion",
    "palkit": "reveals: the energy principle E_k1 + E_p1 + W_muut = E_k2 + E_p2 as bars",
}
