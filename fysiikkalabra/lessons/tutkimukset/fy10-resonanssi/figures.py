"""Figures of the investigation Äänen resonanssi putkessa (scripts/figlib.py); `python scripts/investigations.py figures
fy10-resonanssi` writes them into investigation.md. No force, velocity or acceleration arrows are drawn. The standing
wave is the envelope of the air's oscillation amplitude, in green (no force meaning). The graphs show models only,
never invented measurements."""
import math
from figlib import (Fig, Axes, INK, MUTED, WHITE, GLASS, ALUMINIUM, METAL_EDGE, IRON, SAND, SAND_DARK, GRAIN,
                    HEAT_LIGHT, GOOD, GOOD_LIGHT, n)
import herolib as H
from herolib import grad

WAVE, WAVE_LIGHT = GOOD, GOOD_LIGHT


def tube(f, x0, x1, yc, r, piston=None, rod_to=None, sw=2.5):
    """A horizontal tube open at x0 (left). piston: the x of the piston face; the rod runs right to rod_to."""
    f.rect(x0, yc - r, x1 - x0, 2 * r, GLASS, None)
    f.line(x0, yc - r, x1, yc - r, INK, sw); f.line(x0, yc + r, x1, yc + r, INK, sw)
    if piston is not None:
        f.rect(piston, yc - r + 2, 16, 2 * r - 4, IRON, INK, 2, rx=2)
        f.line(piston + 16, yc, rod_to, yc, INK, 4)
        f.rect(rod_to - 6, yc - 16, 12, 32, IRON, INK, 2, rx=3)


def envelope(f, xa, xb, x_antinode, lam, yc, amp):
    """The standing wave's amplitude envelope |cos| between xa and xb, antinode at x_antinode."""
    pts = [xa + (xb - xa) * i / 120 for i in range(121)]
    up = " L".join(f"{n(x)},{n(yc - amp * abs(math.cos(2 * math.pi * (x - x_antinode) / lam)))}" for x in pts)
    dn = " L".join(f"{n(x)},{n(yc + amp * abs(math.cos(2 * math.pi * (x - x_antinode) / lam)))}" for x in reversed(pts))
    f.path(f"M{up} L{dn} Z", fill=WAVE_LIGHT, stroke=WAVE, w=2.5)


def bracket(f, xa, xb, y, label, color=INK, below=True):
    f.line(xa, y, xb, y, color, 2); f.line(xa, y - 8, xa, y + 8, color, 2); f.line(xb, y - 8, xb, y + 8, color, 2)
    f.tex((xa + xb) / 2, y + (24 if below else -24), label, "middle", color)


def hero():
    """The opening illustration: a resonance tube on a lab bench, a loudspeaker near its open end wired to a signal
    generator with a blank display, a piston rod at the far end, a tape along the tube, a thermometer and a notebook."""
    f = H.hero("fy10r-hero", "Kuvitus: laboratorion työpöydällä on vaakasuora läpinäkyvä putki kahden tuen varassa. Putken "
               "vasemman, avoimen pään edessä on pieni kaiutin, joka on johdoilla kytketty taajuusgeneraattoriin. "
               "Generaattorin näyttö on tyhjä. Putken sisällä on mäntä, jonka varsi tulee ulos oikeasta päästä. Putken "
               "alla kulkee mittanauha. Pöydällä on myös lämpömittari ja vihko mittaustuloksia varten.")
    f.rect(0, 0, 1200, 600, grad(f, "fy10rh-wall", GLASS, "#dfe9ef"))
    f.rect(0, 470, 1200, 130, grad(f, "fy10rh-desk", SAND_DARK, SAND, horizontal=True))
    for k in range(5): f.line(0, 492 + 22 * k, 1200, 488 + 22 * k, GRAIN, 1.5)
    f.line(0, 470, 1200, 470, INK, 3)
    # supports and the tube (open on the left, piston inside)
    for x in (420, 820):
        f.rect(x - 10, 330, 20, 140, ALUMINIUM, INK, 2.5)
        f.rect(x - 50, 456, 100, 14, IRON, INK, 2.5, rx=3)
        f.path(f"M{x - 30},330 Q{x},356 {x + 30},330", fill=ALUMINIUM, stroke=INK, w=2.5)
    f.rect(330, 270, 620, 60, grad(f, "fy10rh-tube", "#ffffff", GLASS), None)
    f.add('<rect x="330" y="270" width="620" height="60" fill="#a9d1f0" fill-opacity="0.18"/>')
    f.line(330, 270, 950, 270, INK, 3); f.line(330, 330, 950, 330, INK, 3)
    f.line(950, 270, 950, 330, INK, 3)
    f.add('<ellipse cx="330" cy="300" rx="9" ry="30" fill="none" stroke="#1f2933" stroke-width="3"/>')
    f.line(345, 280, 930, 280, WHITE, 4)                                   # a highlight on the glass
    f.rect(700, 273, 22, 54, IRON, INK, 2.5, rx=3)                          # the piston
    f.line(722, 300, 1050, 300, INK, 6, cap="round")
    f.rect(1046, 280, 18, 40, IRON, INK, 2.5, rx=4)
    # the tape under the tube
    f.rect(330, 372, 620, 24, "#ffe8a3", INK, 2.5, rx=3)
    for k in range(63):
        f.line(335 + 10 * k, 372, 335 + 10 * k, 372 + (14 if k % 5 == 0 else 8), INK, 1.5)
    # the loudspeaker on a small stand, a short gap before the open end
    f.rect(258, 340, 14, 130, ALUMINIUM, INK, 2.5)
    f.rect(225, 456, 80, 14, IRON, INK, 2.5, rx=3)
    f.rect(220, 252, 70, 96, IRON, INK, 2.5, rx=8)
    f.path("M290,262 L312,276 L312,324 L290,338 Z", fill=ALUMINIUM, stroke=INK, w=2.5)
    f.circle(255, 300, 22, METAL_EDGE, INK, 2.5); f.circle(255, 300, 8, INK)
    # the signal generator with a blank display, wired to the speaker
    f.rect(40, 380, 160, 90, ALUMINIUM, INK, 2.5, rx=8)
    f.rect(56, 394, 92, 34, WHITE, INK, 2, rx=3)
    for k, x in enumerate((70, 104, 138)): f.circle(x, 448, 10, IRON, INK, 2)
    f.circle(176, 410, 13, IRON, INK, 2); f.line(176, 410, 182, 400, WHITE, 2.5)
    f.path("M188,452 C230,452 236,330 222,320", stroke=INK, w=3)
    f.path("M188,462 C244,462 252,340 232,328", stroke="#c4ccd4", w=3)
    # a thermometer and a notebook on the desk
    H.thermometer(f, 1120, 452, 70, colour=HEAT_LIGHT, length=150)
    f.add('<g transform="translate(560,530) rotate(-4)">'
          f'<rect x="-90" y="-34" width="200" height="66" rx="4" fill="{WHITE}" stroke="{INK}" stroke-width="2.5"/>'
          + "".join(f'<line x1="-74" y1="{-18 + 12 * k}" x2="94" y2="{-18 + 12 * k}" stroke="#1971c2" stroke-width="1.5" stroke-opacity="0.5"/>' for k in range(5))
          + "</g>")
    return f.svg()


def setup():
    """The arrangement: a loudspeaker near the open end, the piston inside, the air column length L to the piston face."""
    f = Fig("fy10r-setup", 300, "Kaaviokuva. Vaakasuoran putken vasen pää on avoin, ja sen edessä on kaiutin, joka on kytketty "
            "taajuusgeneraattoriin. Generaattori antaa taajuuden f. Putken sisällä on mäntä, jota voi siirtää varresta. "
            "Ilmapatsaan pituus L mitataan putken avoimesta päästä männän pintaan.")
    tube(f, 150, 520, 120, 32, piston=380, rod_to=578)
    f.line(520, 88, 520, 152, INK, 2.5)
    # speaker
    f.rect(70, 92, 40, 56, IRON, INK, 2.5, rx=5)
    f.path("M110,98 L132,86 L132,154 L110,142 Z", fill=ALUMINIUM, stroke=INK, w=2.5)
    f.tex(100, 50, r"\text{kaiutin}", "middle", MUTED)
    # generator
    f.rect(30, 214, 150, 62, ALUMINIUM, INK, 2.5, rx=6)
    f.tex(105, 245, r"f", "middle")
    f.path("M90,148 C90,180 92,190 92,214", stroke=INK, w=2.5)
    f.tex(196, 245, r"\text{taajuusgeneraattori}", "start", MUTED)
    f.tex(410, 50, r"\text{mäntä}", "middle", MUTED); f.line(395, 64, 390, 86, MUTED, 1.5)
    # air column length
    f.line(150, 158, 150, 196, MUTED, 1.5, "5 4"); f.line(380, 158, 380, 196, MUTED, 1.5, "5 4")
    bracket(f, 150, 380, 186, r"L", INK, below=False)
    return f.svg()


def standing():
    """All modes: one resonance of a tube closed by the piston. Node at the piston face, antinode just outside the
    open end; adjacent nodes lambda/2 apart. Envelope of the oscillation amplitude only."""
    f = Fig("fy10r-standing", 300, "Kaaviokuva seisovasta aallosta putkessa, jonka vasen pää on avoin ja oikea pää suljettu "
            "männällä. Vihreä alue näyttää, kuinka suurella amplitudilla ilma värähtelee eri kohdissa putkea. Männän "
            "pinnassa ilma ei värähtele: siinä on solmu. Toinen solmu on puolikkaan aallonpituuden päässä männästä. Avoimen pään lähellä, "
            "hieman putken ulkopuolella, ja solmujen puolivälissä on kupu, jossa ilma värähtelee voimakkaimmin. "
            "Vierekkäisten solmujen etäisyys on puolikas aallonpituutta.")
    x_open, lam, e = 70, 576, 14
    x_ant = x_open - e; x_piston = x_ant + 3 * lam / 4
    tube(f, x_open, x_piston + 60, 140, 46, piston=x_piston, rod_to=x_piston + 90)
    envelope(f, x_ant, x_piston, x_ant, lam, 140, 38)
    nodes = [x_piston - lam / 2, x_piston]
    for x in nodes:
        f.circle(x, 140, 5, INK)
    f.tex(nodes[0], 66, r"\text{solmu}", "middle"); f.line(nodes[0], 80, nodes[0], 128, MUTED, 1.5, "4 4")
    f.tex(nodes[1] - 10, 66, r"\text{solmu}", "middle"); f.line(nodes[1], 80, nodes[1], 128, MUTED, 1.5, "4 4")
    for x in (x_ant, x_ant + lam / 2):
        f.line(x, 92, x, 188, MUTED, 1.5, "4 4")
    f.tex(x_ant + lam / 2, 66, r"\text{kupu}", "middle")
    f.tex(x_ant + 8, 66, r"\text{kupu}", "start")
    bracket(f, nodes[0], nodes[1], 228, r"\dfrac{\lambda}{2}")
    return f.svg()


def resonances():
    """O/OO: the first three resonance lengths at one frequency for a tube closed by a piston; the antinode lies a
    distance e outside the open end; dashed lines mark the piston positions (the spacing is left for the student)."""
    f = Fig("fy10r-resonances", 390, "Kaaviokuva kolmesta peräkkäisestä resonanssista samalla taajuudella. Kolme päällekkäistä "
            "putkea, joiden vasen pää on avoin. Ylimmässä mäntä on lähimpänä avointa päätä, ja ilmapatsaan pituus on L "
            "yksi; seuraavissa mäntä on kauempana, pituudet L kaksi ja L kolme. Kupu on matkan e verran putken suun "
            "ulkopuolella. Katkoviivat näyttävät männän paikat.")
    x0, lam, e = 116, 300, 20
    x_ant = x0 - e
    for k in range(3):
        yc = 70 + 120 * k
        xp = x_ant + (2 * k + 1) * lam / 4
        tube(f, x0, 560, yc, 26, piston=xp, rod_to=588)
        envelope(f, x_ant, xp, x_ant, lam, yc, 21)
        f.tex(14, yc, rf"n = {k + 1}", "start")
        f.line(x0, yc + 32, x0, yc + 50, MUTED, 1.5); f.line(xp, yc + 32, xp, yc + 50, MUTED, 1.5)
        f.line(x0, yc + 44, xp, yc + 44, INK, 2)
        f.tex(xp + 26, yc + 44, rf"L_{k + 1}", "start")
        f.line(xp, 70 + 120 * k + 28, xp, 372, MUTED, 1.5, "5 4")
    f.line(x_ant, 26, x_ant, 98, MUTED, 1.5, "4 4"); f.line(x0, 26, x0, 40, MUTED, 1.5)
    f.line(x_ant, 32, x0, 32, INK, 2)
    f.tex(x0 + 8, 24, r"e", "start")
    return f.svg()


def model():
    """The model graph: resonance length against its ordinal at one frequency is a line, slope lambda/2."""
    f = Fig("fy10r-model", 330, "Kuvaaja: resonanssipituus L järjestysluvun n funktiona mallin mukaan, kun taajuus pysyy "
            "samana. Kuvaaja on suora, jonka kulmakerroin on puolikas aallonpituutta. Kun n kasvaa yhdellä, L kasvaa "
            "puolikkaan aallonpituuden verran. Kuvaajassa ei ole mittauspisteitä.")
    ax = Axes(f, (90, 280), (470, 50), x=(0, 4.6), y=(0, 10), xticks=[1, 2, 3, 4], yticks=[], xlabel=r"n",
              ylabel=r"L", grid=False)
    sl = 2.2
    L = lambda k: sl * k - (sl / 2 + 0.2)          # L_n = n lambda/2 - (lambda/4 + e), e > 0
    ax.line([(0.7, L(0.7)), (4.3, L(4.3))], INK)
    f.line(ax.X(2), ax.Y(L(2)), ax.X(3), ax.Y(L(2)), MUTED, 2, "6 5")
    f.line(ax.X(3), ax.Y(L(2)), ax.X(3), ax.Y(L(3)), MUTED, 2, "6 5")
    f.tex((ax.X(2) + ax.X(3)) / 2, ax.Y(L(2)) + 22, r"1", "middle", MUTED)
    f.tex(ax.X(3) + 10, (ax.Y(L(2)) + ax.Y(L(3))) / 2, r"\dfrac{\lambda}{2}", "start", MUTED)
    f.tex(ax.X(1.3), ax.Y(8.2), r"\text{kulmakerroin } \dfrac{\lambda}{2}", "middle")
    return f.svg()


def frequency():
    """The extension: wavelength against the reciprocal of frequency, a line through the origin with slope v."""
    f = Fig("fy10r-frequency", 330, "Kuvaaja: aallonpituus lambda taajuuden käänteisluvun yksi per f funktiona mallin mukaan, "
            "jos äänen nopeus ei riipu taajuudesta. Kuvaaja on origon kautta kulkeva suora, jonka kulmakerroin on äänen "
            "nopeus v. Kuvaajassa ei ole mittauspisteitä.")
    ax = Axes(f, (90, 280), (470, 50), x=(0, 10), y=(0, 10), xticks=[], yticks=[], xlabel=r"\dfrac{1}{f}",
              ylabel=r"\lambda", grid=False)
    ax.line([(0, 0), (9.5, 8.55)], INK)
    f.tex(ax.X(3.4), ax.Y(7.8), r"\text{kulmakerroin } v", "middle")
    return f.svg()


FIGURES = {"hero": hero, "setup": setup, "standing": standing, "resonances": resonances, "model": model,
           "frequency": frequency}
