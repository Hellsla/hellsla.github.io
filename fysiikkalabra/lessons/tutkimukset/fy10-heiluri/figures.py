"""Figures of the investigation Putoamiskiihtyvyyden määrittäminen heilurin avulla (scripts/figlib.py); `python
scripts/investigations.py figures fy10-heiluri` writes them into investigation.md. No arrows of force, velocity or
acceleration are drawn; the swing is a muted dashed arc. The graph shows the model only, never invented measurements."""
import math
from figlib import Fig, Axes, INK, MUTED, WHITE, GLASS, ALUMINIUM, IRON, SAND, SAND_DARK, GRAIN, HEAT_LIGHT, COLD, n
import herolib as H
from herolib import grad

BOB, BOB_EDGE = "#adb5bd", "#495057"
THREAD = "#495057"


def bob(f, cx, cy, r, opacity=1.0):
    """A metal pendulum bob with a small eyelet on top."""
    f.add(f'<g opacity="{opacity}"><circle cx="{n(cx)}" cy="{n(cy)}" r="{n(r)}" fill="{BOB}" stroke="{BOB_EDGE}" stroke-width="2.5"/>'
          f'<circle cx="{n(cx - r * 0.35)}" cy="{n(cy - r * 0.35)}" r="{n(r * 0.25)}" fill="{WHITE}" fill-opacity="0.6"/></g>')


def stand(f, x_base, y_floor, x_rod, y_top, arm_to):
    f.rect(x_base, y_floor - 22, 260, 22, IRON, INK, 2.5, rx=4)
    f.rect(x_rod - 7, y_top, 14, y_floor - 22 - y_top, ALUMINIUM, INK, 2.5)
    f.rect(min(x_rod, arm_to) - 6, y_top + 18, abs(arm_to - x_rod) + 12, 12, ALUMINIUM, INK, 2.5, rx=3)
    f.rect(x_rod - 16, y_top + 10, 32, 28, IRON, INK, 2.5, rx=4)


def hero():
    """The opening illustration: a pendulum hanging from a stand on a lab bench. The bob is drawn at equal time steps
    over half a swing (angle = amplitude times cos of the phase): the positions crowd together at the turning points,
    where the bob is slowest. The amplitude is small, as the procedure asks. A tape measure, a stopwatch, a reel of
    thread and scissors lie on the desk."""
    f = H.hero("fy10h-hero", "Kuvitus: laboratorion työpöydällä on statiivi, jonka varresta riippuu langan varassa metallikuula. "
               "Kuula on piirretty useaan kohtaan pienen heilahduksen aikana. Pöydällä ovat rullamitta, sekuntikello, "
               "lankarulla ja sakset.")
    f.rect(0, 0, 1200, 600, grad(f, "fy10hh-wall", GLASS, "#dfe9ef"))
    f.rect(0, 470, 1200, 130, grad(f, "fy10hh-desk", SAND_DARK, SAND, horizontal=True))
    for k in range(5): f.line(0, 492 + 22 * k, 1200, 488 + 22 * k, GRAIN, 1.5)
    f.line(0, 470, 1200, 470, INK, 3)
    px, py, L, r = 600, 92, 330, 20
    stand(f, 300, 470, 340, 50, px + 20)
    f.rect(px - 10, py - 14, 20, 16, IRON, INK, 2.5, rx=2)            # the clamp that holds the thread
    th0 = math.radians(9)
    f.path(f"M{n(px - L * math.sin(th0))},{n(py + L * math.cos(th0))} A{L},{L} 0 0 0 {n(px + L * math.sin(th0))},{n(py + L * math.cos(th0))}",
           stroke=MUTED, w=2, extra='stroke-dasharray="6 6"')
    angles = [th0 * math.cos(k * math.pi / 6) for k in range(7)]       # equal time steps over half a period
    for i, a in enumerate(angles):
        last = i == len(angles) - 1
        x, y = px + (L - r) * math.sin(a), py + (L - r) * math.cos(a)
        f.add(f'<line x1="{px}" y1="{py}" x2="{n(x)}" y2="{n(y)}" stroke="{THREAD}" stroke-width="{2 if last else 1.5}" stroke-opacity="{1 if last else 0.25}"/>')
        bob(f, px + L * math.sin(a), py + L * math.cos(a), r, 1.0 if last else 0.3)
    # a tape measure, a stopwatch, a reel of thread and scissors on the desk
    f.rect(820, 418, 70, 52, "#ffd43b", INK, 2.5, rx=10); f.circle(855, 444, 10, IRON, INK, 2)
    f.rect(888, 456, 90, 10, "#ffe8a3", INK, 2)
    H.stopwatch(f, 1070, 425, 34, 0.18)
    f.rect(90, 430, 46, 40, COLD, INK, 2.5, rx=4); f.rect(82, 424, 62, 10, IRON, INK, 2, rx=3); f.rect(82, 466, 62, 8, IRON, INK, 2, rx=3)
    f.add(f'<g transform="translate(190,446) rotate(-12)" fill="none" stroke="{INK}" stroke-width="3">'
          f'<circle cx="0" cy="0" r="10"/><circle cx="0" cy="26" r="10"/>'
          f'<line x1="9" y1="5" x2="70" y2="20"/><line x1="9" y1="21" x2="70" y2="8"/></g>')
    return f.svg()


def setup():
    """The quantities: the length l from the suspension point to the centre of the bob, the angle of the swing, the
    lowest point; the swing is a dashed arc and the angle is exaggerated for readability."""
    f = Fig("fy10h-setup", 400, "Kaaviokuva. Kuula riippuu langan varassa ripustuskohdasta. Heilurin pituus l mitataan "
            "ripustuskohdasta kuulan keskipisteeseen. Kuula on vedetty sivuun niin, että lanka on kulmassa theta pystysuoraan "
            "nähden. Katkoviiva näyttää kuulan radan ja pystysuoran, ja haaleampi kuula on radan alimmassa kohdassa. "
            "Kulma on piirretty selvyyden vuoksi suuremmaksi kuin mittauksissa.")
    px, py, L, r = 300, 50, 270, 22
    f.rect(170, 26, 260, 14, ALUMINIUM, INK, 2.5, rx=3)
    f.rect(px - 9, 38, 18, 14, IRON, INK, 2)
    th = math.radians(20)
    f.path(f"M{n(px - L * math.sin(th))},{n(py + L * math.cos(th))} A{L},{L} 0 0 0 {n(px + L * math.sin(th))},{n(py + L * math.cos(th))}",
           stroke=MUTED, w=2, extra='stroke-dasharray="6 6"')
    f.line(px, py, px, py + L, MUTED, 1.5, "6 5")
    bob(f, px, py + L, r, 0.35)
    bx, by = px + L * math.sin(th), py + L * math.cos(th)
    f.line(px, py, px + (L - r) * math.sin(th), py + (L - r) * math.cos(th), THREAD, 2)
    bob(f, bx, by, r)
    f.circle(bx, by, 3.5, INK); f.circle(px, py + L, 3.5, INK)
    # the angle at the suspension point
    ra = 70
    f.path(f"M{px},{py + ra} A{ra},{ra} 0 0 0 {n(px + ra * math.sin(th))},{n(py + ra * math.cos(th))}", stroke=INK, w=2)
    f.tex(px + 12, py + ra + 22, r"\theta", "start")
    # the length l, beside the vertical
    xd = 230
    f.line(xd, py, xd, py + L, INK, 2); f.line(xd - 10, py, xd + 10, py, INK, 2); f.line(xd - 10, py + L, xd + 10, py + L, INK, 2)
    f.line(xd + 10, py + L, px - r - 4, py + L, MUTED, 1.5, "4 4")
    f.tex(xd - 12, py + L / 2, r"l", "end")
    f.tex(px + 24, py - 4, r"\text{ripustuskohta}", "start", MUTED)
    f.tex(px, py + L + r + 22, r"\text{kuulan keskipiste}", "middle", MUTED)
    return f.svg()


def model():
    """The linearised model: T squared against l is a line through the origin, slope 4 pi squared over g (no measured points)."""
    f = Fig("fy10h-model", 330, "Kuvaaja: jaksonajan neliö T toiseen heilurin pituuden l funktiona mallin mukaan. Kuvaaja on "
            "origon kautta kulkeva suora. Suoralle on merkitty kaksi pistettä ja niiden välinen muutos: vaakasuunnassa delta l "
            "ja pystysuunnassa delta T toiseen. Kulmakerroin on delta T toiseen jaettuna delta l:llä, ja se on neljä pii "
            "toiseen jaettuna g:llä. Kuvaajassa ei ole mittauspisteitä.")
    ax = Axes(f, (90, 280), (470, 50), x=(0, 10), y=(0, 10), xticks=[], yticks=[], xlabel=r"l", ylabel=r"T^2", grid=False)
    ax.line([(0, 0), (9.5, 8.55)], INK)
    a, b = (3, 2.7), (8, 7.2)
    f.line(ax.X(a[0]), ax.Y(a[1]), ax.X(b[0]), ax.Y(a[1]), MUTED, 2, "6 5")
    f.line(ax.X(b[0]), ax.Y(a[1]), ax.X(b[0]), ax.Y(b[1]), MUTED, 2, "6 5")
    f.tex((ax.X(a[0]) + ax.X(b[0])) / 2, ax.Y(a[1]) + 20, r"\Delta l", "middle", MUTED)
    f.tex(ax.X(b[0]) + 10, (ax.Y(a[1]) + ax.Y(b[1])) / 2, r"\Delta (T^2)", "start", MUTED)
    f.tex(ax.X(0.4), ax.Y(8.6), r"\dfrac{\Delta (T^2)}{\Delta l} = \dfrac{4\pi^2}{g}", "start")
    return f.svg()


FIGURES = {"hero": hero, "setup": setup, "model": model}
