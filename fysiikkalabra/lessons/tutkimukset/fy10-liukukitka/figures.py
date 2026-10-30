"""Figures of the investigation Liukukitkakertoimen määrittäminen (scripts/figlib.py, scripts/fbd.py); `python
scripts/investigations.py figures fy10-liukukitka` writes them into investigation.md. Forces are red, velocity blue and
acceleration orange (fbd: never confused, velocity and acceleration beside the body). The force diagram is an FBD with
the cart as a plain rectangle, its physics checked as it is drawn. The graphs show models only, never invented
measurements."""
from figlib import Fig, Axes, INK, MUTED, WHITE, GLASS, ALUMINIUM, METAL_EDGE, IRON, SAND, SAND_DARK, GRAIN, COLD, COLD_LIGHT, n
from fbd import FBD, VELOCITY
import herolib as H
from herolib import grad

g = 9.81
BRAKE = "#495057"


def cart(f, x, y_track, w=110, h=46, r=13, opacity=1.0, brake=True):
    """A dynamics cart whose left edge is at x and whose wheels stand on the track top y_track; a brake pad between
    the wheels presses on the track."""
    body_bot = y_track - r * 2 + 4
    s = f'<g opacity="{opacity}">'
    s += f'<rect x="{n(x)}" y="{n(body_bot - h)}" width="{n(w)}" height="{n(h)}" rx="6" fill="{COLD_LIGHT}" stroke="{INK}" stroke-width="2.5"/>'
    s += f'<rect x="{n(x + 12)}" y="{n(body_bot - h + 10)}" width="{n(w - 24)}" height="{n(h - 22)}" rx="3" fill="{WHITE}" stroke="{COLD}" stroke-width="1.5" opacity="0.7"/>'
    if brake:
        s += f'<rect x="{n(x + w / 2 - 14)}" y="{n(body_bot - 2)}" width="28" height="{n(y_track - body_bot + 2)}" rx="2" fill="{BRAKE}" stroke="{INK}" stroke-width="1.5"/>'
    for cx in (x + 22, x + w - 22):
        s += f'<circle cx="{n(cx)}" cy="{n(y_track - r)}" r="{r}" fill="{INK}"/><circle cx="{n(cx)}" cy="{n(y_track - r)}" r="{n(r * 0.45)}" fill="{ALUMINIUM}"/>'
    f.add(s + "</g>")


def sensor(f, x, y_track, sc=1.0):
    """An optical motion sensor standing on the track at x, its round face towards the right."""
    w, h = 44 * sc, 54 * sc
    f.rect(x, y_track - h, w, h, IRON, INK, 2.5, rx=5)
    f.circle(x + w - 2, y_track - h / 2, 15 * sc, ALUMINIUM, INK, 2)
    f.circle(x + w - 2, y_track - h / 2, 7 * sc, INK)


def hero():
    """The opening illustration: a long level track on a lab bench, a motion sensor at its left end and a braking
    cart drawn at equal time steps. It slows down evenly, so the gaps shrink steadily, and it stops well before the
    end stop. A laptop shows a straight, falling velocity line."""
    f = H.hero("fy10l-hero", "Kuvitus: laboratorion työpöydällä on pitkä vaakasuora vaunurata. Radan vasemmassa päässä on "
               "liikeanturi. Vaunu liukuu radalla oikealle jarru radan pintaa vasten, ja sen paikka on piirretty tasaisin "
               "aikavälein: välit lyhenevät tasaisesti, kunnes vaunu pysähtyy ennen radan päätä. Pöydällä olevan "
               "kannettavan tietokoneen näytöllä on laskeva suora.")
    f.rect(0, 0, 1200, 600, grad(f, "fy10lh-wall", GLASS, "#dfe9ef"))
    f.rect(0, 440, 1200, 160, grad(f, "fy10lh-desk", SAND_DARK, SAND, horizontal=True))
    for k in range(6): f.line(0, 462 + 22 * k, 1200, 458 + 22 * k, GRAIN, 1.5)
    f.line(0, 440, 1200, 440, INK, 3)
    yt = 392                                                  # track top
    for x in (110, 1080):                                     # adjustable feet
        f.rect(x - 8, yt + 16, 16, 440 - yt - 16, IRON, INK, 2)
        f.rect(x - 18, 432, 36, 8, IRON, INK, 2, rx=2)
    f.rect(60, yt, 1080, 16, ALUMINIUM, INK, 2.5, rx=3)
    f.line(64, yt + 8, 1136, yt + 8, METAL_EDGE, 1.5)
    f.rect(1120, yt - 34, 14, 34, IRON, INK, 2.5, rx=2)        # end stop
    sensor(f, 70, yt, 1.2)
    # the cart decelerates evenly: x = x0 + D(2τ − τ²) at equal steps τ = k/7, so the gaps shrink linearly
    x0, D = 220, 640
    xs = [x0 + D * (2 * t - t * t) for t in [k / 7 for k in range(8)]]
    for i, x in enumerate(xs):
        cart(f, x, yt, opacity=1.0 if i == len(xs) - 1 else 0.28)
    # a laptop on the desk, its screen showing a straight falling line (the braking phase of v(t))
    f.path("M840,560 L1100,560 L1130,586 L810,586 Z", IRON, INK, 2.5)
    f.rect(860, 452, 220, 108, INK, INK, 2.5, rx=6)
    f.rect(872, 462, 196, 88, WHITE)
    f.line(886, 540, 1056, 540, MUTED, 2); f.line(886, 540, 886, 470, MUTED, 2)
    f.line(886, 540, 904, 486, VELOCITY, 3); f.line(904, 486, 1014, 540, VELOCITY, 3); f.line(1014, 540, 1056, 540, VELOCITY, 3)
    return f.svg()


def setup():
    """What is measured: the cart where the push has ended (speed v0) and where it stops; the stopping distance s
    between the same point of the cart in both positions."""
    f = Fig("fy10l-setup", 320, "Kaaviokuva. Vaakasuoran vaunuradan vasemmassa päässä on liikeanturi. Vaunu on piirretty "
            "kahteen kohtaan. Vasemmalla, himmeämpänä, vaunu on kohdassa, jossa työntö on loppunut ja vaunun nopeus on "
            "alkunopeus v nolla, oikealle. Oikealla vaunu on pysähtynyt. Kohtien välinen matka, mitattuna vaunun samasta "
            "kohdasta, on pysähtymismatka s. Vaunun jarru painuu radan pintaa vasten.")
    yt = 210
    f.rect(20, yt, 560, 12, ALUMINIUM, INK, 2.5, rx=3)
    sensor(f, 26, yt, 0.9)
    f.tex(22, yt + 42, r"\text{liikeanturi}", "start", MUTED)
    xa, xb, w = 130, 400, 110
    cart(f, xa, yt, w=w, opacity=0.45); cart(f, xb, yt, w=w)
    # v0 beside the first cart (velocity: blue, thin, open head, never on the body)
    FBD(f, 1).motion(r"\overline{v}_0", (1, 0), (xa + 20, yt - 100), 80, lab=(22, 0))
    f.tex(xb + w / 2, yt - 100, r"v = 0", "middle", VELOCITY)
    # s between the front edges
    for x in (xa + w, xb + w):
        f.line(x, yt - 64, x, yt + 72, MUTED, 1.5, "5 4")
    f.line(xa + w, yt + 66, xb + w, yt + 66, INK, 2)
    f.line(xa + w, yt + 56, xa + w, yt + 76, INK, 2); f.line(xb + w, yt + 56, xb + w, yt + 76, INK, 2)
    f.tex((xa + xb) / 2 + w, yt + 88, r"s", "middle")
    f.tex(xb + w / 2, yt + 34, r"\text{jarru}", "middle", MUTED)
    f.line(xb + w / 2, yt + 22, xb + w / 2, yt + 13, MUTED, 1.5)
    return f.svg()


def forces():
    """The force diagram of the braking cart on a level track (illustrative mu = 0.30, m = 1 kg; no numbers shown):
    weight from the centre, normal force from the contact surface beside it, friction from the rear lower corner
    backwards, velocity forwards and acceleration backwards beside the body."""
    m, mu = 1.0, 0.30
    G = m * g; Fm = mu * G
    f = Fig("fy10l-forces", 330, "Voimakuvio: radalla oikealle liukuva ja hidastuva vaunu suorakulmiona. Paino G osoittaa "
            "keskipisteestä alas. Radan tukivoima N osoittaa alapinnasta ylös, ja se on yhtä pitkä kuin paino. Liikekitka "
            "F myy osoittaa alapinnan takakulmasta vasemmalle eli liikettä vastaan, ja se on paljon lyhyempi kuin paino. "
            "Kappaleen yläpuolella sininen nopeusnuoli v osoittaa oikealle ja oranssi kiihtyvyysnuoli a vasemmalle.")
    cx, cy, w, h = 330, 160, 130, 64
    f.line(150, cy + h / 2, 510, cy + h / 2, MUTED, 1.5, "6 5")       # the track surface, for orientation only
    d = FBD(f, 10.5, body=(cx, cy, w, h), m=m, a=(-Fm / m, 0))
    d.force("G", (0, -G), (cx, cy), "gravity", lab=(24, -6))
    d.force("N", (0, G), (cx + 34, cy + h / 2), "normal", surface=0, lab=(24, 8))
    d.force("F_mu", (-Fm, 0), (cx - w / 2, cy + h / 2), "friction", surface=0, lab=(-6, 22))
    d.draw()
    d.motion(r"\overline{v}", (1, 0), (cx + w / 2 + 22, cy - 36), 70)
    d.motion(r"\overline{a}", (-1, 0), (cx - w / 2 - 22, cy - 36), 50)
    return f.svg()


def model():
    """The energy model: half v0 squared against s is a line through the origin with slope mu g (no measured points)."""
    f = Fig("fy10l-model", 340, "Kuvaaja: puolet alkunopeuden neliöstä pysähtymismatkan s funktiona mallin mukaan. Kuvaaja "
            "on origon kautta kulkeva suora. Suoralle on merkitty kaksi pistettä ja niiden välinen muutos vaakasuunnassa "
            "delta s ja pystysuunnassa. Kulmakerroin on myy kertaa g. Kuvaajassa ei ole mittauspisteitä.")
    ax = Axes(f, (100, 290), (470, 70), x=(0, 10), y=(0, 10), xticks=[], yticks=[], xlabel=r"s", ylabel=r"\tfrac{1}{2}v_0^2", grid=False)
    ax.line([(0, 0), (9.5, 8.55)], INK)
    a, b = (3, 2.7), (8, 7.2)
    f.line(ax.X(a[0]), ax.Y(a[1]), ax.X(b[0]), ax.Y(a[1]), MUTED, 2, "6 5")
    f.line(ax.X(b[0]), ax.Y(a[1]), ax.X(b[0]), ax.Y(b[1]), MUTED, 2, "6 5")
    f.tex((ax.X(a[0]) + ax.X(b[0])) / 2, ax.Y(a[1]) + 20, r"\Delta s", "middle", MUTED)
    f.tex(ax.X(b[0]) + 10, (ax.Y(a[1]) + ax.Y(b[1])) / 2, r"\Delta\!\left(\tfrac{1}{2}v_0^2\right)", "start", MUTED)
    f.tex(ax.X(0.6), ax.Y(8.6), r"\text{kulmakerroin } \mu g", "start")
    return f.svg()


def velocity():
    """The extension's model: during braking v against t is a falling straight line, slope -mu g (no measured points)."""
    f = Fig("fy10l-velocity", 340, "Kuvaaja: vaunun nopeus v ajan t funktiona jarrutuksen aikana mallin mukaan. Nopeus "
            "pienenee alkunopeudesta v nolla tasaisesti nollaan, joten kuvaaja on laskeva suora. Suoran kulmakerroin on "
            "miinus myy kertaa g, ja hidastuvuuden suuruus on a yhtä kuin myy kertaa g. Kuvaajassa ei ole mittauspisteitä.")
    ax = Axes(f, (100, 290), (470, 70), x=(0, 10), y=(0, 10), xticks=[], yticks=[], xlabel=r"t", ylabel=r"v", grid=False)
    ax.line([(0, 8.5), (8.0, 0)], INK)
    f.line(ax.x0 - 7, ax.Y(8.5), ax.x0, ax.Y(8.5), INK, 2)
    f.tex(ax.x0 - 12, ax.Y(8.5), r"v_0", "end")
    f.tex(ax.X(8.0), ax.y0 + 24, r"\text{pysähtyy}", "middle", MUTED)
    a, b = (2.0, 8.5 - 2.0 * 8.5 / 8), (6.0, 8.5 - 6.0 * 8.5 / 8)
    f.line(ax.X(a[0]), ax.Y(a[1]), ax.X(b[0]), ax.Y(a[1]), MUTED, 2, "6 5")
    f.line(ax.X(b[0]), ax.Y(a[1]), ax.X(b[0]), ax.Y(b[1]), MUTED, 2, "6 5")
    f.tex((ax.X(a[0]) + ax.X(b[0])) / 2, ax.Y(a[1]) - 20, r"\Delta t", "middle", MUTED)
    f.tex(ax.X(b[0]) + 10, (ax.Y(a[1]) + ax.Y(b[1])) / 2, r"\Delta v", "start", MUTED)
    f.tex(ax.X(5.2), ax.Y(8.6), r"\text{kulmakerroin } \dfrac{\Delta v}{\Delta t} = -\mu g", "start")
    return f.svg()


FIGURES = {"hero": hero, "setup": setup, "forces": forces, "model": model, "velocity": velocity}
