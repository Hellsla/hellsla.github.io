"""Figures of the investigation Leikkiauton nopeus ja lähtökorkeus (scripts/figlib.py); `python scripts/investigations.py
figures fy10-leikkiauto` writes them into investigation.md. No arrows of force, velocity or acceleration are drawn. The
graphs show models only, never invented measurements."""
import math
from figlib import Fig, Axes, INK, MUTED, WHITE, GLASS, ALUMINIUM, METAL_EDGE, IRON, SAND, SAND_DARK, GRAIN, HEAT_LIGHT, n
import herolib as H
from herolib import grad

BODY, CABIN = HEAT_LIGHT, "#dbe4ea"


def car(f, x, y, angle=0.0, sc=1.0, opacity=1.0, mark=False, flag=12):
    """A toy car whose wheels stand on the point (x, y) of the track surface, tilted by angle (degrees, positive =
    nose down to the right). A thin flag on the roof cuts the photogate beam; mark: a round tape mark on the side."""
    s = sc
    g = (f'<g transform="translate({n(x)},{n(y)}) rotate({angle:.2f})" opacity="{opacity}">'
         f'<rect x="{n(-flag / 2 * s)}" y="{n(-74 * s)}" width="{n(flag * s)}" height="{n(26 * s)}" fill="{WHITE}" stroke="{INK}" stroke-width="2"/>'
         f'<path d="M{n(-26 * s)},{n(-34 * s)} L{n(-16 * s)},{n(-50 * s)} H{n(20 * s)} L{n(30 * s)},{n(-34 * s)} Z" fill="{CABIN}" stroke="{INK}" stroke-width="2.5" stroke-linejoin="round"/>'
         f'<rect x="{n(-46 * s)}" y="{n(-36 * s)}" width="{n(92 * s)}" height="{n(22 * s)}" rx="{n(6 * s)}" fill="{BODY}" stroke="{INK}" stroke-width="2.5"/>'
         + "".join(f'<circle cx="{n(cx * s)}" cy="{n(-10 * s)}" r="{n(10 * s)}" fill="{INK}"/><circle cx="{n(cx * s)}" cy="{n(-10 * s)}" r="{n(4 * s)}" fill="{ALUMINIUM}"/>'
                   for cx in (-28, 28))
         + (f'<circle cx="0" cy="{n(-25 * s)}" r="{n(5 * s)}" fill="{WHITE}" stroke="{INK}" stroke-width="2"/>' if mark else "")
         + "</g>")
    f.add(g)


def gate(f, x, y_track, y_beam, w=26):
    """A photogate seen from the side: one arm of the fork stands behind the track and carries the sensor head at the
    height of the car's flag; drawn before the car, so the car hides the arm's foot. The beam is a small muted dot."""
    f.rect(x - 5, y_beam - 10, 10, y_track - y_beam + 10, METAL_EDGE, INK, 1.5)
    f.rect(x - w / 2, y_beam - 18, w, 30, IRON, INK, 2.5, rx=4)
    f.circle(x, y_beam, 3.5, WHITE)


def hero():
    """The opening illustration: a toy car rolls from rest down an inclined track onto a level part, where a photogate
    stands over the track. Positions at equal time steps: on the incline the gaps grow (constant acceleration), on the
    level part they are equal; the car is drawn sharp at the start and at the gate."""
    f = H.hero("fy10l-hero", "Kuvitus: leikkiauto on kaltevan radan yläpäässä. Auton paikka on piirretty tasaisin aikavälein: "
               "rinteessä välit kasvavat, kun auton vauhti kasvaa. Radan alapäässä on vaakasuora osa, jolla auto kulkee "
               "valoportin läpi. Valoportti on kytketty pöydällä olevaan tietokoneeseen. Radan päässä on pysäytin.")
    f.rect(0, 0, 1200, 600, grad(f, "fy10lh-wall", GLASS, "#dfe9ef"))
    desk = 470
    f.rect(0, desk, 1200, 130, grad(f, "fy10lh-desk", SAND_DARK, SAND, horizontal=True))
    for k in range(5): f.line(0, 492 + 22 * k, 1200, 488 + 22 * k, GRAIN, 1.5)
    f.line(0, desk, 1200, desk, INK, 3)
    # the track: incline from P0 down to P1, then level to the stopper; the top end rests on a stack of books
    p0, p1, top_flat = (70, 196), (690, 440), 440
    L = math.hypot(p1[0] - p0[0], p1[1] - p0[1]); ux, uy = (p1[0] - p0[0]) / L, (p1[1] - p0[1]) / L
    ang = math.degrees(math.atan2(uy, ux))
    th = 14
    for k, c in enumerate(["#a9d1f0", "#f2a69c", "#b2f2bb", "#ffe8a3", "#c4ccd4", "#a9d1f0"]):
        f.rect(30 + 4 * (k % 2), desk - 44 * (k + 1), 150, 44, c, INK, 2.5, rx=4)
    f.path(f"M{p0[0]},{p0[1]} L{p1[0]},{p1[1]} H1150 V{top_flat + th} H{p1[0] + 4} L{p0[0] + 30},{p0[1] + th + 12} L{p0[0]},{p0[1] + th} Z", ALUMINIUM, INK, 2.5)
    f.rect(1150, top_flat - 30, 22, 44, IRON, INK, 2.5, rx=3)                   # the stopper
    for x in (760, 1000):
        f.rect(x - 10, top_flat + th, 20, desk - top_flat - th, IRON, INK, 2)
    # the car: from rest at s0, constant acceleration a along the incline, reaching the corner at t = 1
    # equal time steps dt: the car reaches the corner at tc = 0.95 (between frames), then runs on the level part at the
    # corner speed v, so the frames at t = 1.0 and 1.2 lie on the level part and the gaps keep growing until the corner
    s0, tc, dt = 70, 0.95, 0.2
    a = 2 * (L - s0) / tc ** 2; v = a * tc
    poses = [(p0[0] + ux * (s0 + 0.5 * a * (k * dt) ** 2), p0[1] + uy * (s0 + 0.5 * a * (k * dt) ** 2), ang) for k in range(5)]
    x_level = p1[0] + v * (1.0 - tc)                       # the frame at t = 1.0
    xg = p1[0] + v * (1.2 - tc)                            # the frame at t = 1.2, at the photogate
    for i, (x, y, an) in enumerate(poses):
        car(f, x, y, an, 1.0, 1.0 if i == 0 else 0.35)
    car(f, x_level, top_flat, 0, 1.0, 0.35)
    gate(f, xg, top_flat, top_flat - 62)
    car(f, xg, top_flat, 0, 1.0, 1.0)
    # the gate's cable to a laptop on the desk
    f.path(f"M{n(xg + 13)},{top_flat - 70} C{n(xg + 90)},{top_flat - 70} 1110,{top_flat + 10} 1090,488", stroke=INK, w=2.5)
    f.rect(1020, 488, 140, 80, IRON, INK, 2.5, rx=6); f.rect(1030, 498, 120, 60, "#d0e6fb", INK, 2, rx=3)   # laptop in front
    f.path("M1010,568 H1170 L1160,580 H1020 Z", ALUMINIUM, INK, 2.5)
    return f.svg()


def setup():
    """What is measured: the drop h of a fixed mark on the car from the start to the photogate, and the width L of the
    flag that cuts the beam."""
    f = Fig("fy10l-setup", 380, "Kaaviokuva. Vasemmalla ylhäällä leikkiauto on levossa kaltevan radan yläpäässä. Autossa on "
            "merkki. Rata jatkuu alhaalla vaakasuorana, ja sen kohdalla on valoportti, jonka läpi auto kulkee. Korkeus h on "
            "auton merkin pystysuora korkeusero lähtökohdan ja valoportin välillä. Auton katolla oleva liuska katkaisee "
            "valoportin säteen. Liuskan leveys on L.")
    p0, p1 = (40, 120), (300, 300); yflat = 300
    L = math.hypot(p1[0] - p0[0], p1[1] - p0[1]); ux, uy = (p1[0] - p0[0]) / L, (p1[1] - p0[1]) / L
    ang = math.degrees(math.atan2(uy, ux))
    f.path(f"M{p0[0]},{p0[1]} L{p1[0]},{p1[1]} H470 V{yflat + 10} H{p1[0] + 3} L{p0[0]},{p0[1] + 12} Z", ALUMINIUM, INK, 2)
    f.rect(470, yflat - 22, 14, 32, IRON, INK, 2, rx=2)
    sc = 0.75; s0 = 45; fw = 24
    cx, cy = p0[0] + ux * s0, p0[1] + uy * s0
    car(f, cx, cy, ang, sc, mark=True, flag=fw)
    # the mark: 25*sc above the track along the car's normal
    nx, ny = math.sin(math.radians(ang)), -math.cos(math.radians(ang))
    m0 = (cx + nx * 25 * sc, cy + ny * 25 * sc)
    xg = 380; yb = yflat - 62 * sc
    gate(f, xg, yflat, yb, w=22)
    car(f, xg, yflat, 0, sc, mark=True, flag=fw)
    m1 = (xg, yflat - 25 * sc)
    # h: from the mark at the start to the mark at the gate
    xh = 545
    f.line(m0[0] + 8, m0[1], xh + 10, m0[1], MUTED, 1.5, "4 4"); f.line(m1[0] + 8, m1[1], xh + 10, m1[1], MUTED, 1.5, "4 4")
    f.line(xh, m0[1], xh, m1[1], INK, 2); f.line(xh - 10, m0[1], xh + 10, m0[1], INK, 2); f.line(xh - 10, m1[1], xh + 10, m1[1], INK, 2)
    f.tex(xh - 12, (m0[1] + m1[1]) / 2, r"h", "end")
    # L: the width of the flag on the car at the gate, a dimension above the flag
    fx0, fx1, fy = xg - fw / 2 * sc, xg + fw / 2 * sc, yflat - 74 * sc - 30
    f.line(fx0, fy - 8, fx0, yflat - 74 * sc - 4, MUTED, 1.5); f.line(fx1, fy - 8, fx1, yflat - 74 * sc - 4, MUTED, 1.5)
    f.line(fx0, fy, fx1, fy, INK, 2)
    f.tex(fx0 - 6, fy, r"L", "end")
    f.tex(xg, yflat + 46, r"\text{valoportti}", "middle", MUTED)
    f.tex(cx - 20, cy - 80, r"\text{lähtö levosta}", "start", MUTED)
    return f.svg()


def model_v():
    """The model: v against h rises ever more slowly (a square root), so a straight line does not test it well."""
    f = Fig("fy10l-model-v", 330, "Kuvaaja: auton nopeus v lähtökorkeuden h funktiona energiaperiaatteen mallin mukaan. "
            "Kuvaaja alkaa origosta ja kaartuu loivemmaksi korkeuden kasvaessa: nopeus on verrannollinen korkeuden "
            "neliöjuureen. Kuvaajassa ei ole mittauspisteitä.")
    ax = Axes(f, (90, 280), (470, 50), x=(0, 10), y=(0, 10), xticks=[], yticks=[], xlabel=r"h", ylabel=r"v", grid=False)
    ax.curve(lambda h: 2.9 * math.sqrt(h), 0, 9.5, INK)
    f.tex(ax.X(9.6), ax.Y(2.9 * math.sqrt(9.5)) + 40, r"v = \sqrt{2gh}", "end")
    return f.svg()


def model_v2():
    """The linearised model: v squared against h is a line through the origin with slope 2g without losses; with
    losses that grow in proportion to h the slope k is smaller."""
    f = Fig("fy10l-model-v2", 340, "Kuvaaja: nopeuden neliö v toiseen lähtökorkeuden h funktiona mallin mukaan. Katkoviivalla "
            "on origon kautta kulkeva suora v toiseen yhtä kuin 2 g h, joka vastaa liikettä ilman energiahäviöitä. "
            "Yhtenäinen suora on loivempi, ja sen kulmakerroin k on pienempi kuin 2 g: se vastaa tilannetta, jossa osa "
            "energiasta ei näy auton nopeudessa. Kuvaajassa ei ole mittauspisteitä.")
    ax = Axes(f, (90, 290), (470, 60), x=(0, 10), y=(0, 10), xticks=[], yticks=[], xlabel=r"h", ylabel=r"v^2", grid=False)
    ax.line([(0, 0), (9.5, 9.5)], MUTED, 2, "6 5")
    ax.line([(0, 0), (9.5, 6.6)], INK)
    f.tex(ax.X(6.4), ax.Y(9.0), r"v^2 = 2gh", "end", MUTED)
    f.tex(ax.X(9.6), ax.Y(6.6) + 92, r"v^2 = kh,\ k < 2g", "end")
    return f.svg()


FIGURES = {"hero": hero, "setup": setup, "model-v": model_v, "model-v2": model_v2}
