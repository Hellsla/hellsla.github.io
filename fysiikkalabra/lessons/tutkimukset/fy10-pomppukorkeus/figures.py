"""Figures of the investigation Pudotus- ja pomppukorkeus (scripts/figlib.py); `python scripts/investigations.py figures
fy10-pomppukorkeus` writes them into investigation.md. No arrows of force, velocity or acceleration are drawn; the
motion paths are muted dashes. The graph shows the model only, never invented measurements."""
from figlib import Fig, Axes, INK, MUTED, WHITE, GLASS, ALUMINIUM, IRON, SAND, SAND_DARK, GRAIN, n
import herolib as H
from herolib import grad

BALL, BALL_EDGE = "#c0eb75", "#5c940d"


def ball(f, cx, cy, r, opacity=1.0):
    f.add(f'<g opacity="{opacity}"><circle cx="{n(cx)}" cy="{n(cy)}" r="{n(r)}" fill="{BALL}" stroke="{BALL_EDGE}" stroke-width="2.5"/>'
          f'<path d="M{n(cx - r * 0.9)},{n(cy - r * 0.35)} Q{n(cx)},{n(cy + r * 0.25)} {n(cx + r * 0.9)},{n(cy - r * 0.35)}" '
          f'fill="none" stroke="{WHITE}" stroke-width="2"/></g>')


def hero():
    """The opening illustration: a stroboscopic sequence of a ball dropped beside a wall scale; it falls with growing
    gaps (constant time steps, distance grows with the square of time), bounces and rises to a lower top point; a
    phone on a small tripod films it."""
    f = H.hero("fy10p-hero", "Kuvitus: pallo putoaa seinällä olevan mitta-asteikon vieressä. Pallon paikka on piirretty "
               "tasaisin aikavälein: putoamisen aikana välit kasvavat. Lattiasta pompattuaan pallo nousee lakikorkeuteen, "
               "joka on alempana kuin kohta, josta se pudotettiin. Kolmijalan päällä oleva puhelin kuvaa pomppua videolle.")
    f.rect(0, 0, 1200, 600, grad(f, "fy10ph-wall", GLASS, "#dfe9ef"))
    f.rect(0, 490, 1200, 110, grad(f, "fy10ph-floor", SAND_DARK, SAND, horizontal=True))
    for k in range(4): f.line(0, 512 + 24 * k, 1200, 508 + 24 * k, GRAIN, 1.5)
    f.line(0, 490, 1200, 490, INK, 3)
    # the scale on the wall
    f.rect(300, 60, 50, 430, "#ffe8a3", INK, 2.5, rx=3)
    for k in range(42):
        f.line(300, 480 - 10 * k, 300 + (24 if k % 5 == 0 else 12), 480 - 10 * k, INK, 1.5)
    # the ball: dropped from rest it falls straight down; after the bounce it drifts slowly sideways (as real balls
    # often do), rises to a lower top point (60 % of the drop) and falls again
    r, floor = 22, 490
    y0 = 110; drop = floor - r - y0; g = 2 * drop       # time unit: the fall lasts 1
    up = (2 * g * 0.6 * drop) ** 0.5; flight = 2 * up / g
    pts = [(330, y0 + 0.5 * g * t * t) for t in [k / 8 for k in range(9)]]
    for k in range(1, 20):
        tau = k / 8
        if tau > flight: break
        pts.append((330 + 150 * tau, floor - r - (up * tau - 0.5 * g * tau * tau)))
    for i, (x, y) in enumerate(pts):
        ball(f, x, y, r, 1.0 if i in (0, len(pts) - 1) else 0.4)
    # a phone on a small tripod
    f.line(1060, 490, 1040, 400, INK, 4); f.line(1060, 490, 1080, 400, INK, 4); f.line(1060, 400, 1060, 330, INK, 4)
    f.line(1035, 490, 1060, 400, INK, 4)
    f.rect(1052, 250, 16, 100, IRON, INK, 2.5, rx=4)     # seen from the side, the camera towards the ball
    f.circle(1052, 268, 5, INK)
    return f.svg()


def setup():
    """What is measured: drop height h0 and bounce height h1, both from the floor to the bottom of the ball."""
    f = Fig("fy10p-setup", 440, "Kaaviokuva. Vasemmalla pallo on pudotuskohdassa: sen alapinnan korkeus lattiasta on "
            "pudotuskorkeus h nolla. Katkoviiva kulkee alas lattiaan, jossa pallo pomppaa. Oikealla pallo on pompun "
            "ylimmässä kohdassa: sen alapinnan korkeus lattiasta on pomppukorkeus h yksi, ja se on pienempi kuin "
            "pudotuskorkeus. Molemmat korkeudet mitataan samasta kohdasta palloa, lattiasta pallon alapintaan.")
    floor, r = 400, 26
    f.rect(30, floor, 540, 14, ALUMINIUM, INK, 2.5)
    xa, xb, ya, yb = 210, 400, 80, 196                      # bottom of the ball at release and at the top of the bounce
    ball(f, xa, ya - r, r); ball(f, xb, yb - r, r); ball(f, xa, floor - r, r, 0.4)
    f.line(xa, ya + 4, xa, floor - 2 * r - 6, MUTED, 2, "6 5")      # dropped from rest: straight down
    f.path(f"M{xa + r},{floor - r} Q{xb - 30},{yb - 10} {xb},{yb}", stroke=MUTED, w=2, extra='stroke-dasharray="6 5"')
    for x, y, lab, side in [(130, ya, r"h_0", "end"), (480, yb, r"h_1", "start")]:
        f.line(x, y, x, floor, INK, 2); f.line(x - 10, y, x + 10, y, INK, 2); f.line(x - 10, floor, x + 10, floor, INK, 2)
        f.tex(x - 12 if side == "end" else x + 12, (y + floor) / 2, lab, side)
    f.line(140, ya, xa - 4, ya, MUTED, 1.5, "4 4"); f.line(xb + 4, yb, 470, yb, MUTED, 1.5, "4 4")
    f.tex(xa, ya - 2 * r - 22, r"\text{pudotus}", "middle", MUTED); f.tex(xb, yb - 2 * r - 22, r"\text{pompun lakikohta}", "middle", MUTED)
    return f.svg()


def model():
    """The model graph: h1 against h0 is a line through the origin with slope a < 1; the line h1 = h0 for comparison."""
    f = Fig("fy10p-model", 360, "Kuvaaja: pomppukorkeus h yksi pudotuskorkeuden h nolla funktiona mallin mukaan. Kuvaaja "
            "on origon kautta kulkeva suora, jonka kulmakerroin a on pienempi kuin yksi. Vertailuksi katkoviivalla on "
            "suora h yksi yhtä kuin h nolla, joka vastaisi pomppua ilman energiahäviöitä. Kuvaajassa ei ole "
            "mittauspisteitä.")
    ax = Axes(f, (90, 310), (470, 50), x=(0, 10), y=(0, 10), xticks=[], yticks=[], xlabel=r"h_0", ylabel=r"h_1", grid=False)
    ax.line([(0, 0), (9.5, 9.5)], MUTED, 2, "6 5")
    ax.line([(0, 0), (9.5, 5.7)], INK)
    f.tex(ax.X(7.4), ax.Y(9.3), r"h_1 = h_0", "end", MUTED)
    f.tex(ax.X(9.6), ax.Y(5.7) + 70, r"h_1 = a h_0", "end")
    f.tex(ax.X(0.6), ax.Y(9.2), r"a = \dfrac{h_1}{h_0} < 1", "start")
    return f.svg()


FIGURES = {"hero": hero, "setup": setup, "model": model}
