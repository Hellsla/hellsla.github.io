"""Figures of the investigation Hiuksen paksuuden määrittäminen (scripts/figlib.py); `python scripts/investigations.py
figures fy10-hiuksen-paksuus` writes them into investigation.md. The laser's light is drawn white and neutral: its
wavelength is read from the school laser's label, so no colour is implied. The model graph shows a model only, never
invented measurements; the pattern sketch is schematic, not to scale."""
import math
from figlib import Fig, Axes, INK, MUTED, WHITE, RULE, GLASS, ALUMINIUM, METAL_EDGE, IRON, SAND, SAND_DARK, SAND_LIGHT, GRAIN, PAPER, COLD, n
import herolib as H
from herolib import grad


def hero():
    """Side view of a dim classroom: a laser on a stand, a hair taped across a card holder in the beam, a white screen
    standing at the far end. Seen from the side the pattern spreads across the screen, out of the picture plane, so
    the drawing shows no pattern and does not answer the predictions."""
    f = H.hero("fy10h-hero", "Kuvitus sivulta katsottuna: hämärässä luokassa pöydän vasemmassa päässä on jalustalle kiinnitetty "
               "laser. Sen kapea säde kulkee vaakasuoraan pidikkeen kohdalta, johon on pingotettu hius, ja osuu pöydän oikeassa "
               "päässä seisovaan valkoiseen varjostimeen. Ikkunan sälekaihtimet ovat kiinni. Pöydällä on mittanauha, viivain "
               "ja vihko.")
    f.rect(0, 0, 1200, 600, grad(f, "fy10hh-wall", "#2c3a47", "#4a5866"))
    # a window with closed blinds
    f.rect(120, 50, 300, 230, "#3a4856", INK, 3, rx=4)
    for k in range(14): f.rect(128, 58 + 16 * k, 284, 12, "#7d8b98", None, rx=2)
    f.line(270, 50, 270, 280, INK, 2)
    # the desk
    f.rect(0, 430, 1200, 170, grad(f, "fy10hh-desk", SAND_DARK, SAND, horizontal=True))
    for k in range(6): f.line(0, 452 + 24 * k, 1200, 448 + 24 * k, GRAIN, 1.5)
    f.line(0, 430, 1200, 430, INK, 3)
    beam_y = 340
    # laser on a small stand
    f.rect(150, 390, 120, 40, IRON, INK, 2.5, rx=4)
    f.rect(200, 360, 20, 30, ALUMINIUM, INK, 2.5)
    f.rect(110, beam_y - 22, 170, 44, grad(f, "fy10hh-laser", "#9aa5b1", IRON), INK, 3, rx=10)
    f.rect(280, beam_y - 10, 18, 20, METAL_EDGE, INK, 2.5, rx=3)
    f.rect(140, beam_y - 12, 60, 24, "#ffe8a3", INK, 2, rx=3)          # the label (left blank: read it on the real laser)
    f.rect(232, beam_y - 30, 16, 10, INK, None, rx=3)                    # switch
    # the hair holder: a clamp stand with a card, the hair across its hole (seen edge-on, the hair as a thin line)
    hx = 520
    f.rect(hx - 50, 418, 100, 12, IRON, INK, 2.5, rx=3)
    f.rect(hx - 4, 260, 8, 158, ALUMINIUM, INK, 2)
    f.rect(hx - 9, 270, 18, 140, SAND_LIGHT, INK, 2.5, rx=2)
    f.rect(hx - 9, beam_y - 18, 18, 36, "#2c3a47", INK, 2)              # the hole in the card
    f.line(hx, beam_y - 18, hx, beam_y + 18, INK, 2)                     # the hair
    # the screen at the far end, edge-on
    sx = 1060
    f.rect(sx - 60, 418, 120, 12, IRON, INK, 2.5, rx=3)
    f.rect(sx - 10, 170, 20, 248, WHITE, INK, 3, rx=2)
    # the beam: faint, white, ending in a soft glow on the screen
    f.defs_add('<radialGradient id="fy10hh-glow"><stop offset="0" stop-color="#ffffff" stop-opacity="0.9"/>'
               '<stop offset="1" stop-color="#ffffff" stop-opacity="0"/></radialGradient>')
    f.line(298, beam_y, sx - 10, beam_y, WHITE, 3)
    f.add(f'<line x1="298" y1="{beam_y}" x2="{sx - 10}" y2="{beam_y}" stroke="{WHITE}" stroke-width="12" stroke-opacity="0.15"/>')
    f.add(f'<circle cx="{sx - 12}" cy="{beam_y}" r="34" fill="url(#fy10hh-glow)"/>')
    # a tape measure, a ruler and a notebook on the desk
    f.circle(720, 470, 30, "#ffd43b", INK, 3); f.circle(720, 470, 10, IRON, INK, 2)
    f.rect(748, 488, 120, 10, "#ffe8a3", INK, 2)
    f.add('<g transform="translate(330,520) rotate(-4)">'
          f'<rect x="-120" y="-12" width="260" height="24" rx="3" fill="#ffe8a3" stroke="{INK}" stroke-width="2.5"/>'
          + "".join(f'<line x1="{-110 + 12 * k}" y1="-12" x2="{-110 + 12 * k}" y2="{-4 if k % 5 else 2}" stroke="{INK}" stroke-width="1.5"/>' for k in range(21))
          + "</g>")
    f.add('<g transform="translate(980,520) rotate(5)">'
          f'<rect x="-90" y="-34" width="190" height="66" rx="4" fill="{WHITE}" stroke="{INK}" stroke-width="2.5"/>'
          + "".join(f'<line x1="-74" y1="{-18 + 12 * k}" x2="84" y2="{-18 + 12 * k}" stroke="{COLD}" stroke-width="1.5" stroke-opacity="0.6"/>' for k in range(5))
          + "</g>")
    return f.svg()


def pattern():
    """Schematic of the pattern behind a narrow slit or a hair (not to scale): bright regions between dark minima,
    the minima numbered m = 1, 2, 3 on both sides of the centre."""
    f = Fig("fy10h-pattern", 260, "Kaaviokuva varjostimelle syntyvästä diffraktiokuviosta, ei mittakaavassa: todellisuudessa sivujen valoisat alueet ovat paljon himmeämpiä. Tummalla taustalla on "
            "vaakasuora rivi valoisia alueita. Keskimmäinen valoisa alue on kirkkain ja kaksi kertaa niin leveä kuin muut, ja "
            "sivuille päin valoisat alueet himmenevät. Valoisien alueiden välissä ovat tummat kohdat eli minimit, jotka on "
            "numeroitu keskikohdasta lähtien molempiin suuntiin luvuilla m yhtä kuin 1, 2 ja 3.")
    c, s, y0, y1 = 300, 66, 40, 120
    f.rect(30, y0, 540, y1 - y0, INK, None, rx=6)
    ym = (y0 + y1) / 2
    f.defs_add('<radialGradient id="fy10hp-spot"><stop offset="0" stop-color="#ffffff"/>'
               '<stop offset="0.6" stop-color="#ffffff" stop-opacity="0.7"/><stop offset="1" stop-color="#ffffff" stop-opacity="0"/></radialGradient>')
    f.add(f'<ellipse cx="{c}" cy="{n(ym)}" rx="{n(s * 0.95)}" ry="30" fill="url(#fy10hp-spot)"/>')
    for k, op in ((1, 0.75), (2, 0.5), (3, 0.32)):
        for sign in (1, -1):
            cx = c + sign * (k + 0.5) * s
            f.add(f'<ellipse cx="{n(cx)}" cy="{n(ym)}" rx="{n(s * 0.4)}" ry="20" fill="url(#fy10hp-spot)" fill-opacity="{op}"/>')
    f.line(c, y0 - 10, c, 176, MUTED, 1.5, "5 4")
    for k in (1, 2, 3):
        for sign in (1, -1):
            x = c + sign * k * s
            f.line(x, y1 + 4, x, y1 + 16, INK, 2)
            f.tex(x, y1 + 32, str(k), "middle")
    f.tex(40, y1 + 32, r"m", "start")
    f.tex(c, 196, r"\text{keskikohta}", "middle", MUTED)
    f.tex(c, 238, r"\text{kaaviokuva, ei mittakaavassa}", "middle", MUTED, size=20)
    return f.svg()


def geometry():
    """Top view (not to scale): the beam meets the hair, the direction to the m-th minimum makes the angle theta_m
    with the beam's direction, the screen is at distance L, the minimum at x_m from the centre."""
    f = Fig("fy10h-geometry", 330, "Kaaviokuva ylhäältä katsottuna, ei mittakaavassa. Lasersäde tulee vasemmalta ja osuu hiukseen. "
            "Hiuksesta lähtee katkoviiva suoraan eteenpäin varjostimelle ja toinen viiva varjostimella olevaan m:nteen "
            "minimiin. Viivojen välinen kulma on theta m. Hiuksen etäisyys varjostimesta on L, ja minimin etäisyys kuvion "
            "keskikohdasta on x m.")
    hx, hy, sx, ty = 120, 220, 500, 80
    f.arrow(24, hy, hx - 10, hy, INK, 3, 14)
    f.tex(60, hy + 26, r"\text{säde}", "middle", MUTED)
    f.circle(hx, hy, 6, INK)
    f.tex(hx, hy - 34, r"\text{hius}", "middle", MUTED)
    f.line(sx, 30, sx, 280, INK, 4)
    f.tex(sx, 14, r"\text{varjostin}", "middle", MUTED)
    f.line(hx, hy, sx, hy, MUTED, 2, "7 6")
    f.line(hx, hy, sx, ty, INK, 2.5)
    f.circle(sx, ty, 5, INK)
    th = math.atan2(hy - ty, sx - hx); r = 100
    f.path(f"M{n(hx + r)},{hy} A{r},{r} 0 0 0 {n(hx + r * math.cos(th))},{n(hy - r * math.sin(th))}", stroke=INK, w=2)
    f.tex(hx + 1.22 * r * math.cos(th / 2), hy - 1.22 * r * math.sin(th / 2), r"\theta_m", "start")
    # x_m beside the screen
    f.line(sx + 22, ty, sx + 22, hy, INK, 2); f.line(sx + 14, ty, sx + 30, ty, INK, 2); f.line(sx + 14, hy, sx + 30, hy, INK, 2)
    f.tex(sx + 36, (ty + hy) / 2, r"x_m", "start")
    # L under the beam
    f.line(hx, 290, sx, 290, INK, 2); f.line(hx, 282, hx, 298, INK, 2); f.line(sx, 282, sx, 298, INK, 2)
    f.tex((hx + sx) / 2, 312, r"L", "middle")
    return f.svg()


def model():
    """The model graph: x_m against m is a line through the origin with slope lambda L / d (no measured points)."""
    f = Fig("fy10h-model", 330, "Kuvaaja: minimin etäisyys kuvion keskikohdasta x m järjestysluvun m funktiona mallin mukaan. "
            "Kuvaaja on origon kautta kulkeva suora, jonka kulmakerroin a on lambda kertaa L jaettuna d:llä. Suoralle on "
            "merkitty muutokset delta m ja delta x m. Kuvaajassa ei ole mittauspisteitä.")
    ax = Axes(f, (90, 280), (470, 50), x=(0, 5), y=(0, 5), xticks=[1, 2, 3, 4], yticks=[], xlabel=r"m", ylabel=r"x_m", grid=False)
    ax.line([(0, 0), (4.8, 4.32)], INK)
    a, b = (2, 1.8), (4, 3.6)
    f.line(ax.X(a[0]), ax.Y(a[1]), ax.X(b[0]), ax.Y(a[1]), MUTED, 2, "6 5")
    f.line(ax.X(b[0]), ax.Y(a[1]), ax.X(b[0]), ax.Y(b[1]), MUTED, 2, "6 5")
    f.tex((ax.X(a[0]) + ax.X(b[0])) / 2, ax.Y(a[1]) + 20, r"\Delta m", "middle", MUTED)
    f.tex(ax.X(b[0]) + 10, (ax.Y(a[1]) + ax.Y(b[1])) / 2, r"\Delta x_m", "start", MUTED)
    f.tex(ax.X(1.6), ax.Y(4.0), r"a = \dfrac{\Delta x_m}{\Delta m} = \dfrac{\lambda L}{d}", "middle")
    return f.svg()


FIGURES = {"hero": hero, "pattern": pattern, "geometry": geometry, "model": model}
