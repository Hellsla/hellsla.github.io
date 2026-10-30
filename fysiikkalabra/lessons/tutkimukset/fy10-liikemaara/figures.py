"""Figures of the investigation Liikemäärän säilyminen törmäyksissä (scripts/figlib.py); `python scripts/investigations.py
figures fy10-liikemaara` writes them into investigation.md. Velocity arrows are blue (COLD, teacher's rule: force,
velocity and acceleration always in different colours); the sensors' own positive directions are muted arrows, not
velocities. The graphs show models only, never invented measurements."""
import math
from figlib import (Fig, Axes, INK, MUTED, WHITE, RULE_LIGHT, GLASS, ALUMINIUM, METAL_EDGE, IRON, SAND, SAND_DARK,
                    SAND_LIGHT, GRAIN, HEAT_LIGHT, COLD, COLD_LIGHT, n)
import herolib as H
from herolib import grad

VELOCITY = COLD


def track(f, x0, x1, y, h=14):
    """The cart track seen from the side, its top surface at y, with end stops."""
    f.rect(x0, y, x1 - x0, h, ALUMINIUM, METAL_EDGE, 2, 2)
    f.line(x0 + 4, y + h / 2, x1 - 4, y + h / 2, METAL_EDGE, 1.5)


def bumper(f, x, y, direction, length=22, amp=6, turns=3):
    """A spring bumper sticking out of a cart end at x, height y, towards direction (+1 right, -1 left)."""
    pts = [(x, y)] + [(x + direction * length * (i + 0.5) / (2 * turns), y + (amp if i % 2 else -amp)) for i in range(2 * turns)]
    pts.append((x + direction * length, y))
    f.path("M" + " L".join(f"{n(a)},{n(b)}" for a, b in pts), stroke=IRON, w=2.5)
    f.line(x + direction * length, y - 9, x + direction * length, y + 9, INK, 3)


def cart(f, x, y, w, h, body, opacity=1.0, load=False, bump=0, wheel=None):
    """A cart with its wheels on the track surface y, centred at x; bump: the side of a spring bumper (+1 / -1 / 0)."""
    r = wheel or h * 0.22
    g = [f'<g opacity="{opacity:g}">']
    f.body.append("".join(g))
    f.rect(x - w / 2, y - 2 * r - h, w, h, body, INK, 2.5, rx=5)
    if load: f.rect(x - w * 0.3, y - 2 * r - h - h * 0.55, w * 0.6, h * 0.55, HEAT_LIGHT, INK, 2.5, rx=4)
    for dx in (-w * 0.3, w * 0.3): f.circle(x + dx, y - r, r, IRON, INK, 2)
    if bump: bumper(f, x + bump * w / 2, y - 2 * r - h / 2, bump, length=w * 0.16, amp=h * 0.12)
    f.body.append("</g>")


def sensor(f, x, y, w, h, facing):
    """An optical motion sensor standing on the track end at x, its lens towards facing (+1 right, -1 left)."""
    f.rect(x - w / 2, y - h, w, h, IRON, INK, 2.5, rx=5)
    lx = x + facing * (w / 2 - 3)
    f.rect(lx - 4 if facing > 0 else lx - 4, y - h * 0.72, 8, h * 0.44, "#343a40", INK, 1.5, rx=2)


def hero():
    """The opening illustration: a cart track on a lab bench with a motion sensor at each end; a loaded cart moves
    right and a lighter, faster cart left towards it (muted speed lines); a laptop shows the two sensors' distance
    graphs, both rising because each cart moves away from its own sensor."""
    f = H.hero("fy10l-hero", "Kuvitus: laboratorion pöydällä on pitkä vaunurata, jonka kummassakin päässä on liikeanturi. "
               "Radalla kaksi vaunua liikkuu toisiaan kohti, ja vauhtiviivat näyttävät liikkeen. Vasemmanpuoleisessa vaunussa on "
               "lisäpunnus, ja oikeanpuoleinen, kevyempi vaunu liikkuu nopeammin. Vaunujen vastakkaisissa päissä on "
               "jousipuskurit. Pöydällä oleva kannettava tietokone näyttää anturien mittaamat kuvaajat.")
    f.rect(0, 0, 1200, 600, grad(f, "fy10lh-wall", GLASS, "#dfe9ef"))
    f.rect(0, 440, 1200, 160, grad(f, "fy10lh-desk", SAND_DARK, SAND, horizontal=True))
    for k in range(6): f.line(0, 462 + 22 * k, 1200, 458 + 22 * k, GRAIN, 1.5)
    f.line(0, 440, 1200, 440, INK, 3)
    # the track on two feet, its top surface at 360
    ty = 360
    for x in (200, 1000):
        f.rect(x - 8, ty + 20, 16, 60, IRON, INK, 2); f.rect(x - 36, 432, 72, 10, IRON, INK, 2, rx=3)
    track(f, 60, 1140, ty, 20)
    for x in (60, 1124): f.rect(x, ty - 26, 16, 26, IRON, INK, 2, rx=2)     # end stops
    sensor(f, 115, ty, 70, 96, +1); sensor(f, 1085, ty, 70, 96, -1)
    # cart 1 (loaded, slower) moves right, cart 2 (lighter, faster) moves left: muted speed lines behind each,
    # longer behind the faster cart
    w, h = 150, 54
    cart(f, 450, ty, w, h, SAND_LIGHT, load=True, bump=+1)
    cart(f, 760, ty, w, h, COLD_LIGHT, bump=-1)
    for k, y in enumerate((ty - 62, ty - 46, ty - 30)):
        f.line(300 + 12 * k, y, 355, y, MUTED, 3, cap="round")
        f.line(855, y, 960 - 14 * k, y, MUTED, 3, cap="round")
    # a laptop with the two sensors' distance graphs: each cart moves away from its own sensor, so both distances
    # grow, the lighter cart's faster
    f.path("M640,560 L960,560 L990,590 L610,590 Z", fill=ALUMINIUM, stroke=INK, w=2.5)
    f.rect(660, 440, 280, 120, "#343a40", INK, 2.5, rx=6); f.rect(672, 450, 256, 100, WHITE, None)
    f.line(690, 540, 910, 540, MUTED, 2); f.line(690, 540, 690, 458, MUTED, 2)
    f.line(690, 520, 900, 490, HEAT_LIGHT, 4); f.line(690, 530, 900, 462, IRON, 4)
    return f.svg()


def setup():
    """The set-up seen from the side: sensors at both ends, the carts, their velocities (blue) along the track, the
    chosen positive direction, and the direction each sensor counts as positive (muted)."""
    f = Fig("fy10l-setup", 330, "Kaaviokuva sivulta. Vaakasuoran radan vasemmassa päässä on anturi 1 ja oikeassa päässä anturi 2, "
            "ja kumpikin osoittaa radan keskelle. Radalla ovat vaunu 1, jonka massa on m1, ja vaunu 2, jonka massa on m2. "
            "Vaunun 1 nopeus v1 osoittaa oikealle ja vaunun 2 nopeus v2 vasemmalle; nopeusnuolet ovat sinisiä. Radan alla "
            "on valittu positiivinen suunta, oikealle. Harmaat nuolet anturien alla näyttävät, mihin suuntaan kukin anturi "
            "mittaa nopeuden positiiviseksi: anturi 1 oikealle ja anturi 2 vasemmalle, eli anturin 2 suunta on "
            "vastakkainen valittuun positiiviseen suuntaan nähden.")
    ty = 190
    track(f, 20, 580, ty)
    sensor(f, 50, ty, 44, 64, +1); sensor(f, 550, ty, 44, 64, -1)
    cart(f, 200, ty, 120, 50, SAND_LIGHT, bump=+1, wheel=10)
    cart(f, 400, ty, 120, 50, COLD_LIGHT, bump=-1, wheel=10)
    f.tex(200, ty - 45, r"m_1", "middle"); f.tex(400, ty - 45, r"m_2", "middle")
    # velocities, blue
    f.arrow(160, 70, 260, 70, VELOCITY, 4, 15); f.tex(210, 40, r"\overline{v}_1", "middle", VELOCITY)
    f.arrow(440, 70, 360, 70, VELOCITY, 4, 15); f.tex(400, 40, r"\overline{v}_2", "middle", VELOCITY)
    # what each sensor counts as positive (muted, not a velocity)
    f.arrow(30, 232, 110, 232, MUTED, 2.5, 12); f.tex(70, 258, r"\text{anturi 1: }+", "start", MUTED, size=20)
    f.arrow(570, 232, 490, 232, MUTED, 2.5, 12); f.tex(530, 258, r"\text{anturi 2: }+", "end", MUTED, size=20)
    # the chosen positive direction
    f.arrow(230, 300, 370, 300, INK, 3, 14); f.tex(222, 300, r"\text{positiivinen suunta}", "end", INK, size=20)
    f.tex(378, 300, r"+", "start")
    return f.svg()


def velocity():
    """The model of one cart's velocity against time: slowly decreasing before (rolling resistance), a quick change
    during the contact, slowly decreasing after; v1 and v1' are read at the edges of the contact (no measured points)."""
    f = Fig("fy10l-velocity", 330, "Kuvaaja: yhden vaunun nopeus v ajan t funktiona mallin mukaan. Ennen törmäystä nopeus "
            "pienenee hyvin hitaasti vierimisvastuksen takia. Törmäyksen aikana, joka on merkitty varjostetulla alueella, "
            "nopeus muuttuu nopeasti pienemmäksi. Törmäyksen jälkeen nopeus taas pienenee hitaasti. Nopeus v1 luetaan "
            "juuri ennen törmäystä ja nopeus v1 pilkku heti törmäyksen jälkeen. Kuvaajassa ei ole mittauspisteitä.")
    ax = Axes(f, (90, 280), (470, 60), x=(0, 10), y=(0, 10), xticks=[], yticks=[], xlabel=r"t", ylabel=r"v", grid=False)
    a, b = 4.4, 5.4
    ax.area([(a, 0), (a, 9.6), (b, 9.6), (b, 0)], RULE_LIGHT, 0.6)
    before = lambda t: 7.6 - 0.09 * t
    after = lambda t: 3.2 - 0.09 * (t - b)
    ax.curve(before, 0.2, a, INK)
    ax.curve(lambda t: before(a) + (after(b) - before(a)) * (1 - math.cos(math.pi * (t - a) / (b - a))) / 2, a, b, INK)
    ax.curve(after, b, 9.6, INK)
    for t, v, lab in ((a, before(a), r"v_1"), (b, after(b), r"v_1'")):
        f.line(ax.x0, ax.Y(v), ax.X(t), ax.Y(v), MUTED, 1.5, "6 5")
        f.tex(ax.x0 - 10, ax.Y(v), lab, "end")
    f.tex(ax.X(2.2), ax.Y(8.8), r"\text{ennen}", "middle", MUTED)
    f.tex(ax.X((a + b) / 2), ax.Y(10.6), r"\text{törmäys}", "middle", MUTED)
    f.tex(ax.X(7.6), ax.Y(4.4), r"\text{jälkeen}", "middle", MUTED)
    return f.svg()


def model():
    """The conservation model: total momentum after against before is the line p' = p through the origin, slope 1."""
    f = Fig("fy10l-model", 330, "Kuvaaja: kokonaisliikemäärä törmäyksen jälkeen kokonaisliikemäärän ennen törmäystä funktiona, "
            "jos liikemäärä säilyy. Kuvaaja on origon kautta kulkeva suora, jonka kulmakerroin on yksi. Kuvassa näkyy "
            "positiivisten liikemäärien osa: jos liikemäärän suuruus pienenee törmäyksessä, piste on suoran alapuolella. "
            "Kuvaajassa ei ole mittauspisteitä.")
    ax = Axes(f, (90, 280), (470, 50), x=(0, 10), y=(0, 10), xticks=[], yticks=[], xlabel=r"p_\text{kok}",
              ylabel=r"p_\text{kok}'", grid=False, arrow_room=20)
    ax.line([(0, 0), (9.5, 9.5)], INK)
    f.tex(ax.X(5.6), ax.Y(8.3), r"p_\text{kok}' = p_\text{kok}", "end")
    f.arrow(ax.X(7.6), ax.Y(7.2), ax.X(7.6), ax.Y(4.4), MUTED, 2, 10)
    f.tex(ax.X(7.6), ax.Y(3.4), r"\text{suuruus pienenee}", "middle", MUTED, size=20)
    return f.svg()


FIGURES = {"hero": hero, "setup": setup, "velocity": velocity, "model": model}
