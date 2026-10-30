"""Figures of the investigation Pallon muotokertoimen määrittäminen (scripts/figlib.py); `python scripts/investigations.py
figures fy10-muotokerroin` writes them into investigation.md. Forces are red, velocity blue (fbd: FORCE, VELOCITY; the
teacher's rule: force, velocity and acceleration always in different colours). The force diagram is an FBD: the ball as
a plain rectangle, the weight from its centre, the buoyancy and the air resistance together as long as the weight at the terminal speed. The
graphs show models only, never invented measurements.

The falling ball follows the quadratic-drag model: v = v_r tanh(t/tau), s = v_r tau ln cosh(t/tau), tau = v_r/g."""
import math
from figlib import Fig, Axes, INK, MUTED, WHITE, RULE, RULE_LIGHT, GLASS, IRON, SAND, SAND_DARK, GRAIN, GOOD, GOOD_LIGHT, n
from fbd import FBD, VELOCITY
import herolib as H
from herolib import grad


def ball(f, cx, cy, r, opacity=1.0):
    """A light balloon-like ball with a small knot at the bottom and a highlight."""
    f.add(f'<g opacity="{opacity}"><circle cx="{n(cx)}" cy="{n(cy)}" r="{n(r)}" fill="{GOOD_LIGHT}" stroke="{GOOD}" stroke-width="2.5"/>'
          f'<path d="M{n(cx - r * 0.18)},{n(cy + r + 5)} L{n(cx)},{n(cy + r - 1)} L{n(cx + r * 0.18)},{n(cy + r + 5)} Z" fill="{GOOD}"/>'
          f'<path d="M{n(cx - r * 0.55)},{n(cy - r * 0.2)} Q{n(cx - r * 0.5)},{n(cy - r * 0.6)} {n(cx - r * 0.1)},{n(cy - r * 0.65)}" '
          f'fill="none" stroke="{WHITE}" stroke-width="3" stroke-linecap="round"/></g>')


def fall(t_rel):
    """Distance fallen from rest in units of v_r * tau, at time t_rel = t / tau."""
    return math.log(math.cosh(t_rel))


def hero():
    """The opening illustration: a light ball dropped beside a tall wall scale, drawn at equal time steps: the gaps grow at
    first and then become equal (the terminal speed); a phone on a tripod films it from far away, at the height of the
    lower, steady part of the fall."""
    f = H.hero("fy10m-hero", "Kuvitus: kevyt pallo putoaa seinällä olevan pitkän mitta-asteikon edessä. Pallon paikka on piirretty "
               "tasaisin aikavälein. Kauempana kolmijalan päällä oleva puhelin kuvaa putoamista videolle.")
    f.rect(0, 0, 1200, 600, grad(f, "fy10mh-wall", GLASS, "#dfe9ef"))
    f.rect(0, 530, 1200, 70, grad(f, "fy10mh-floor", SAND_DARK, SAND, horizontal=True))
    for k in range(3): f.line(0, 550 + 20 * k, 1200, 547 + 20 * k, GRAIN, 1.5)
    f.line(0, 530, 1200, 530, INK, 3)
    # the scale on the wall, behind the ball
    f.rect(380, 30, 50, 500, "#ffe8a3", INK, 2.5, rx=3)
    for k in range(49):
        f.line(380, 520 - 10 * k, 380 + (24 if k % 5 == 0 else 12), 520 - 10 * k, INK, 1.5)
    # the ball at equal time steps t/tau = 0, 0.6, ..., 4.8: the last gaps are nearly equal (v close to v_r)
    r, y0, y_end = 19, 60, 530 - 19 - 8
    steps = [0.6 * k for k in range(9)]
    L = (y_end - y0) / fall(steps[-1])
    for i, t in enumerate(steps):
        ball(f, 410, y0 + L * fall(t), r, 1.0 if i in (0, len(steps) - 1) else 0.45)
    # a phone on a tripod, far away, at the height of the steady part
    f.line(1000, 530, 975, 420, INK, 4); f.line(1000, 530, 1025, 420, INK, 4); f.line(972, 530, 1000, 420, INK, 4)
    f.line(1000, 420, 1000, 380, INK, 4)
    f.rect(992, 300, 16, 100, IRON, INK, 2.5, rx=4)        # seen from the side, the camera towards the ball
    f.circle(992, 318, 5, INK)
    return f.svg()


def setup():
    """Left: the situation (the ball beside a scale of known length, at constant speed at the end, velocity beside it).
    Right: the force diagram at the terminal speed: weight from the centre, air resistance from the bottom surface,
    equal lengths; the velocity beside the body."""
    f = Fig("fy10m-setup", 420, "Kaaviokuva. Vasemmalla tilannekuva: pallo putoaa pystysuoran mitta-asteikon vieressä. Pallon paikat "
            "on piirretty tasaisin aikavälein: ylhäällä välit kasvavat, alhaalla ne ovat yhtä suuret. Alimman pallon vieressä "
            "on sininen nopeusnuoli alaspäin. Oikealla voimakuvio rajanopeudella: pallo on suorakulmio, paino G lähtee "
            "keskipisteestä alas, noste F_noste keskipisteen vierestä ylös ja ilmanvastus F_v alapinnasta ylös. Ilmapallolla "
            "noste on lähes yhtä pitkä kuin paino ja ilmanvastus lyhyt: ylöspäin osoittavat nuolet ovat yhteensä yhtä pitkät "
            "kuin paino, joten voimat kumoavat toisensa, F_v on G miinus F_noste. Nopeusnuoli alas on piirretty suorakulmion viereen.")
    f.line(300, 20, 300, 400, RULE_LIGHT, 1.5, "4 6")
    f.tex(150, 26, r"\text{tilanne}", "middle", MUTED)
    f.tex(450, 26, r"\text{rajanopeudella}", "middle", MUTED)
    # the scale and the ball sequence
    f.rect(70, 60, 30, 330, "#ffe8a3", INK, 2, rx=3)
    for k in range(33):
        f.line(70, 380 - 10 * k, 70 + (16 if k % 5 == 0 else 8), 380 - 10 * k, INK, 1.2)
    r, y0, y_end = 14, 76, 366
    steps = [0.7 * k for k in range(7)]
    L = (y_end - y0) / fall(steps[-1])
    for i, t in enumerate(steps):
        ball(f, 130, y0 + L * fall(t), r, 1.0 if i == len(steps) - 1 else 0.45)
    f.line(178, 300, 178, 372, VELOCITY, 2.5)
    f.path("M170,362 L178,378 L186,362", stroke=VELOCITY, w=2.5)
    f.tex(194, 336, r"\overline{v}", "start", VELOCITY)
    # the force diagram: the ball as a rectangle, at constant velocity (a = 0)
    # a balloon: the rubber about 3 g and the air inside about 10 g, so the buoyancy (the weight of the displaced air) is
    # about 10 g * g and the air resistance at the terminal speed only the rest, G - F_noste
    m, m_air, g = 0.013, 0.010, 9.81
    G, B = m * g, m_air * g; s = 130 / G
    cx, cy, w, h = 430, 185, 90, 56
    d = FBD(f, s, body=(cx, cy, w, h), m=m, a=(0, 0))
    d.force("G", (0, -G), (cx, cy), "gravity", lab=(24, -4))
    d.force("F_noste", (0, B), (cx + 20, cy), "buoyancy", tex=r"\overline{F}_\text{noste}", lab=(52, 4))
    d.force("F_v", (0, G - B), (cx - 22, cy + h / 2), "drag", v_rel=(0, -1), tex=r"\overline{F}_\text{v}", lab=(-34, 0), push=True)
    d.draw()
    d.motion(r"\overline{v}", (0, -1), (540, 200), 80, lab=(22, -10))
    f.tex(450, 380, r"F_\text{v} = G - F_\text{noste}", "middle")
    return f.svg()


def model():
    """The model: distance fallen against time bends at first and becomes a straight line with slope v_r; speed against
    time levels off at v_r (no measured points)."""
    f = Fig("fy10m-model", 330, "Kaksi mallikuvaajaa ilman mittauspisteitä. Vasemmalla pudonnut matka s ajan t funktiona: kuvaaja "
            "kaartuu aluksi ylöspäin ja muuttuu sitten suoraksi. Suoran osan kulmakerroin, "
            "delta s jaettuna delta t:llä, on rajanopeus v_r. Oikealla nopeus v ajan t funktiona: nopeus kasvaa aluksi jyrkästi ja tasaantuu "
            "vaakasuoran katkoviivan v_r tasolle.")
    T = 4.0
    a1 = Axes(f, (60, 280), (230, 60), x=(0, T), y=(0, 4.2), xticks=[], yticks=[], xlabel=r"t", ylabel=r"s", grid=False)
    a1.curve(fall, 0, T, INK)
    p, q = (2.4, fall(2.4)), (3.6, fall(3.6))                 # a slope triangle on the straight part
    a1.line([p, (q[0], p[1]), q], MUTED, 2, "6 5")
    f.tex((a1.X(p[0]) + a1.X(q[0])) / 2, a1.Y(p[1]) + 18, r"\Delta t", "middle", MUTED, size=20)
    f.tex(a1.X(q[0]) + 8, (a1.Y(p[1]) + a1.Y(q[1])) / 2, r"\Delta s", "start", MUTED, size=20)
    f.tex(a1.X(0.1), a1.Y(3.6), r"v_\text{r} = \dfrac{\Delta s}{\Delta t}", "start", size=22)
    a2 = Axes(f, (360, 280), (530, 60), x=(0, T), y=(0, 1.25), xticks=[], yticks=[], xlabel=r"t", ylabel=r"v", grid=False)
    a2.line([(0, 1), (T, 1)], MUTED, 2, "6 5")
    a2.curve(math.tanh, 0, T, INK)
    f.tex(a2.X(T) + 4, a2.Y(1) - 22, r"v_\text{r}", "end", MUTED)
    return f.svg()


def mass():
    """The extension's model: the mass against the square of the terminal speed is a line through the origin when C is
    constant; slope C rho A / (2 g) (no measured points)."""
    f = Fig("fy10m-mass", 330, "Mallikuvaaja ilman mittauspisteitä: pallon massa m rajanopeuden neliön v_r toiseen funktiona. Jos "
            "muotokerroin pysyy samana, kuvaaja on origon kautta kulkeva suora, jonka kulmakerroin on C kertaa rho kertaa A "
            "jaettuna kahdella g:llä.")
    ax = Axes(f, (90, 280), (470, 50), x=(0, 10), y=(0, 10), xticks=[], yticks=[], xlabel=r"v_\text{r}^2", ylabel=r"m", grid=False)
    ax.line([(0, 0), (9.5, 8.6)], INK)
    f.tex(ax.X(6.2), ax.Y(3.6), r"\text{kulmakerroin } \dfrac{C\rho A}{2g}", "start")
    return f.svg()


FIGURES = {"hero": hero, "setup": setup, "model": model, "mass": mass}
