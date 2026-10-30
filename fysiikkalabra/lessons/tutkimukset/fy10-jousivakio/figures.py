"""Figures of the investigation Jousivakion määrittäminen (scripts/figlib.py); `python scripts/investigations.py figures
fy10-jousivakio` writes them into investigation.md. Forces are red (fbd.FORCE, teacher's rule: force, velocity and
acceleration always in different colours). The graphs show models only, never invented measurements."""
from figlib import Fig, Axes, INK, MUTED, WHITE, RULE, GLASS, ALUMINIUM, METAL_EDGE, IRON, SAND, SAND_DARK, SAND_LIGHT, GRAIN, HEAT_LIGHT, COLD, n
import herolib as H
from herolib import grad

FORCE = "#c92a2a"


def spring(f, x, y_top, y_bot, coils=12, width=34, color=IRON, w=3):
    """A helical spring drawn as a zigzag between y_top and y_bot, with straight ends."""
    end = 14; top, bot = y_top + end, y_bot - end; step = (bot - top) / (2 * coils)
    d = f"M{n(x)},{n(y_top)} L{n(x)},{n(top)}"
    for k in range(2 * coils):
        d += f" L{n(x + (width / 2 if k % 2 == 0 else -width / 2))},{n(top + (k + 0.5) * step)}"
    d += f" L{n(x)},{n(bot)} L{n(x)},{n(y_bot)}"
    return f.path(d, stroke=color, w=w)


def stand(f, x_base, y_floor, x_rod, y_top, arm_to):
    f.rect(x_base, y_floor - 22, 260, 22, IRON, INK, 2.5, rx=4)
    f.rect(x_rod - 7, y_top, 14, y_floor - 22 - y_top, ALUMINIUM, INK, 2.5)
    f.rect(min(x_rod, arm_to) - 6, y_top + 18, abs(arm_to - x_rod) + 12, 12, ALUMINIUM, INK, 2.5, rx=3)
    f.rect(x_rod - 16, y_top + 10, 32, 28, IRON, INK, 2.5, rx=4)


def hero():
    """The opening illustration: a lab bench with a stand, a spring with a mass hanger, a ruler beside it and slotted masses waiting."""
    f = H.hero("fy10j-hero", "Kuvitus: laboratorion työpöydällä on statiivi, jonka varresta riippuu kierrejousi. Jousen alapäässä on "
               "punnusteline, jossa on kaksi punnusta. Jousen vieressä seisoo pystysuora mittanauha. Pöydällä on lisää punnuksia, "
               "vaaka ja vihko, johon mittaustuloksia kirjataan.")
    f.rect(0, 0, 1200, 600, grad(f, "fy10jh-wall", GLASS, "#dfe9ef"))
    f.rect(0, 470, 1200, 130, grad(f, "fy10jh-desk", SAND_DARK, SAND, horizontal=True))
    for k in range(5): f.line(0, 492 + 22 * k, 1200, 488 + 22 * k, GRAIN, 1.5)
    f.line(0, 470, 1200, 470, INK, 3)
    stand(f, 300, 470, 340, 60, 600)
    spring(f, 590, 90, 270, coils=11)
    f.rect(570, 270, 40, 10, IRON, INK, 2.5, rx=2)            # hanger plate
    f.line(590, 280, 590, 300, INK, 3)
    for k, c in enumerate([HEAT_LIGHT, "#f7c58c"]):
        f.rect(548, 300 + 30 * k, 84, 28, c, INK, 2.5, rx=5)
    # the vertical tape beside the spring
    f.rect(670, 70, 46, 400, "#ffe8a3", INK, 2.5, rx=3)
    for k in range(39):
        f.line(670, 82 + 10 * k, 670 + (20 if k % 5 == 0 else 11), 82 + 10 * k, INK, 1.5)
    # masses, a scale and a notebook on the desk
    for k in range(3): f.rect(820 + 6 * k, 440 - 26 * k, 84, 26, HEAT_LIGHT, INK, 2.5, rx=5)
    f.rect(960, 430, 150, 40, IRON, INK, 2.5, rx=6); f.rect(985, 420, 100, 12, ALUMINIUM, INK, 2.5, rx=3)
    f.rect(1000, 440, 70, 20, "#b2f2bb", INK, 2, rx=3)
    f.add('<g transform="translate(120,520) rotate(-6)">'
          f'<rect x="-80" y="-34" width="200" height="66" rx="4" fill="{WHITE}" stroke="{INK}" stroke-width="2.5"/>'
          + "".join(f'<line x1="-64" y1="{-18 + 12 * k}" x2="104" y2="{-18 + 12 * k}" stroke="{COLD}" stroke-width="1.5" stroke-opacity="0.6"/>' for k in range(5))
          + "</g>")
    return f.svg()


def setup():
    """The measurement: the spring alone (length l0) and with a hanging mass (length l), the extension x, the forces on the mass."""
    f = Fig("fy10j-setup", 470, "Kaaviokuva. Vasemmalla jousi riippuu ilman kuormaa, ja sen pituus on l nolla. Oikealla jouseen on "
            "ripustettu kappale, ja jousen pituus on l. Pituuksien erotus on venymä x. Kappaleeseen vaikuttaa ylöspäin jousivoima "
            "F jousen kiinnityskohdasta ja alaspäin paino G kappaleen keskipisteestä. Kappale on levossa, joten voimat ovat "
            "yhtä suuret.")
    f.rect(40, 30, 520, 16, ALUMINIUM, INK, 2.5, rx=3)
    # unloaded spring
    spring(f, 150, 46, 216, coils=9, width=30)
    f.line(108, 46, 108, 216, MUTED, 1.5); f.line(98, 46, 118, 46, MUTED, 2); f.line(98, 216, 118, 216, MUTED, 2)
    f.tex(96, 131, r"l_0", "end")
    # loaded spring
    spring(f, 400, 46, 296, coils=9, width=30)
    f.rect(350, 296, 100, 70, HEAT_LIGHT, INK, 2.5, rx=4)       # the body: a rectangle (teacher's rule)
    f.line(470, 46, 470, 296, MUTED, 1.5); f.line(460, 46, 480, 46, MUTED, 2); f.line(460, 296, 480, 296, MUTED, 2)
    f.tex(484, 171, r"l", "start")
    # extension x between the two lower ends
    f.line(118, 216, 520, 216, MUTED, 1.5, "6 5")
    f.line(530, 216, 530, 296, INK, 2); f.line(520, 216, 540, 216, INK, 2); f.line(520, 296, 540, 296, INK, 2)
    f.tex(546, 256, r"x", "start")
    # forces on the body: spring force from the attachment point up, weight from the centre down
    f.arrow(400, 296, 400, 206, FORCE, 4, 16); f.tex(388, 262, r"\overline{F}", "end", FORCE)
    f.circle(400, 331, 4, INK)
    f.arrow(400, 331, 400, 421, FORCE, 4, 16); f.tex(388, 406, r"\overline{G}", "end", FORCE)
    f.tex(150, 300, r"\text{ilman kuormaa}", "middle", MUTED); f.tex(262, 331, r"\text{kuormitettuna}", "middle", MUTED)
    return f.svg()


def model():
    """The model graph: F against x is a line through the origin, slope k (no measured points)."""
    f = Fig("fy10j-model", 330, "Kuvaaja: jousivoima F venymän x funktiona Hooken lain mallin mukaan. Kuvaaja on origon kautta "
            "kulkeva suora. Suoralle on merkitty kaksi pistettä ja niiden välinen muutos: vaakasuunnassa delta x ja "
            "pystysuunnassa delta F. Kulmakerroin k on delta F jaettuna delta x:llä. Kuvaajassa ei ole mittauspisteitä.")
    ax = Axes(f, (90, 280), (470, 50), x=(0, 10), y=(0, 10), xticks=[], yticks=[], xlabel=r"x", ylabel=r"F", grid=False)
    ax.line([(0, 0), (9.5, 8.55)], INK)
    a, b = (3, 2.7), (8, 7.2)
    f.line(ax.X(a[0]), ax.Y(a[1]), ax.X(b[0]), ax.Y(a[1]), MUTED, 2, "6 5")
    f.line(ax.X(b[0]), ax.Y(a[1]), ax.X(b[0]), ax.Y(b[1]), MUTED, 2, "6 5")
    f.tex((ax.X(a[0]) + ax.X(b[0])) / 2, ax.Y(a[1]) + 20, r"\Delta x", "middle", MUTED)
    f.tex(ax.X(b[0]) + 10, (ax.Y(a[1]) + ax.Y(b[1])) / 2, r"\Delta F", "start", MUTED)
    f.tex(ax.X(3.2), ax.Y(7.6), r"k = \dfrac{\Delta F}{\Delta x}", "middle")
    return f.svg()


def oscillation():
    """The extension's linearised model: T squared against m is a line, slope 4 pi squared over k (no measured points)."""
    f = Fig("fy10j-oscillation", 330, "Kuvaaja: värähdysajan neliö T toiseen massan m funktiona mallin mukaan. Kuvaaja on suora, jonka "
            "kulmakerroin on neljä pii toiseen jaettuna k:lla. Suora ei välttämättä kulje tarkasti origon kautta, koska jousen oma "
            "massa värähtelee osittain mukana. Kuvaajassa ei ole mittauspisteitä.")
    ax = Axes(f, (90, 280), (470, 50), x=(0, 10), y=(0, 10), xticks=[], yticks=[], xlabel=r"m", ylabel=r"T^2", grid=False)
    ax.line([(0, 0.6), (9.5, 8.7)], INK)
    f.tex(ax.X(3.4), ax.Y(7.8), r"\text{kulmakerroin } \dfrac{4\pi^2}{k}", "middle")
    f.tex(ax.X(0.3), ax.Y(1.7), r"\text{vakiotermi}", "start", MUTED)
    return f.svg()


FIGURES = {"hero": hero, "setup": setup, "model": model, "oscillation": oscillation}
