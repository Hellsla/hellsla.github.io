"""Figures of the investigation Äänen nopeus kulkuajasta (scripts/figlib.py); `python scripts/investigations.py figures
fy10-aanennopeus` writes them into investigation.md. The sound pulse is drawn as muted arcs (no velocity arrow is
needed). The signal sketch and the graph show models only, never invented measurements."""
import math
from figlib import Fig, Axes, INK, MUTED, WHITE, GLASS, ALUMINIUM, IRON, SAND, SAND_DARK, SAND_LIGHT, GRAIN, COLD, n
import herolib as H
from herolib import grad

TAPE = "#ffe8a3"


def arcs(f, cx, cy, radii, half_angle, color=MUTED, w=3, opacity=(1.0,)):
    """Parts of circles round (cx, cy) opening to the right: the front of one sound pulse."""
    for k, r in enumerate(radii):
        a = math.radians(half_angle)
        x1, y1 = cx + r * math.cos(a), cy - r * math.sin(a)
        x2, y2 = cx + r * math.cos(a), cy + r * math.sin(a)
        op = opacity[min(k, len(opacity) - 1)]
        f.add(f'<path d="M{n(x1)},{n(y1)} A{n(r)},{n(r)} 0 0 1 {n(x2)},{n(y2)}" fill="none" stroke="{color}" '
              f'stroke-width="{w:g}" stroke-linecap="round" stroke-opacity="{op:g}"/>')


def mic_stand(f, x, y_floor, y_mic, sc=1.0):
    """A microphone on a tripod stand, the microphone pointing left towards the source."""
    s = sc
    f.line(x, y_floor, x - 34 * s, y_floor - 2, INK, 4 * s); f.line(x, y_floor - 40 * s, x - 30 * s, y_floor, INK, 4 * s)
    f.line(x, y_floor - 40 * s, x + 30 * s, y_floor, INK, 4 * s)
    f.line(x, y_floor - 40 * s, x, y_mic + 10 * s, INK, 4 * s)
    f.rect(x - 46 * s, y_mic - 9 * s, 52 * s, 18 * s, IRON, INK, 2.5, rx=8 * s)
    f.circle(x - 46 * s, y_mic, 11 * s, ALUMINIUM, INK, 2.5)


def hero():
    """The opening illustration, neutral about the method: in a long school corridor a student claps two boards
    together, the front of the sound pulse spreads out along the corridor, a tape measure lies along the floor and a
    thermometer hangs on the wall. No detector or wiring is drawn: choosing the method is the student's task."""
    f = H.hero("fy10a-hero", "Kuvitus: pitkällä koulun käytävällä oppilas lyö kaksi puulautaa yhteen. Äänen rintama leviää "
               "lyöntikohdasta käytävää pitkin. Lattialla käytävän suuntaisesti on mittanauha, ja seinällä on lämpömittari.")
    f.rect(0, 0, 1200, 600, grad(f, "fy10ah-wall", GLASS, "#dfe9ef"))
    f.rect(0, 470, 1200, 130, grad(f, "fy10ah-floor", SAND_DARK, SAND, horizontal=True))
    for k in range(4): f.line(0, 494 + 26 * k, 1200, 490 + 26 * k, GRAIN, 1.5)
    f.line(0, 470, 1200, 470, INK, 3)
    f.rect(0, 380, 1200, 10, "#dfe9ef", MUTED, 1.5)            # a wall rail
    for x in (800, 1040):                                      # doors along the corridor
        f.rect(x, 150, 110, 320, SAND_LIGHT, INK, 2.5, rx=3); f.circle(x + 92, 320, 6, INK)
    H.thermometer(f, 420, 170, 60, length=120)
    floor = 540
    # the student with the clapper boards held in front
    H.walker(f, 150, floor, sc=0.9, hand=(278, 300))
    clap = (300, 292)
    f.add(f'<g transform="translate(270,292) rotate(-14)"><rect x="0" y="-16" width="92" height="14" rx="3" fill="{SAND_DARK}" stroke="{INK}" stroke-width="2.5"/></g>')
    f.add(f'<g transform="translate(270,292) rotate(4)"><rect x="0" y="0" width="92" height="14" rx="3" fill="{SAND_DARK}" stroke="{INK}" stroke-width="2.5"/></g>')
    # the front of one sound pulse spreading along the corridor
    arcs(f, clap[0], clap[1], [392, 404, 416], 30, MUTED, 3, (0.35, 0.65, 1.0))
    # the tape measure along the floor
    x0, x1 = 300, 1160
    f.rect(x0, floor + 8, x1 - x0, 16, TAPE, INK, 2, rx=2)
    for k in range(int((x1 - x0) / 20) + 1):
        f.line(x0 + 20 * k, floor + 8, x0 + 20 * k, floor + (18 if k % 5 == 0 else 14), INK, 1.5)
    f.rect(x0 - 40, floor + 2, 44, 28, IRON, INK, 2.5, rx=6)    # the tape's case
    return f.svg()


def setup():
    """The two-microphone layout: the source, then microphone 1 and microphone 2 on one line; d between them."""
    f = Fig("fy10a-setup", 330, "Kaaviokuva ylhäältä. Vasemmalla on äänilähde, sen oikealla puolella mikrofoni 1 ja kauempana "
            "mikrofoni 2, kaikki samalla suoralla. Äänen rintama on piirretty mikrofonien väliin. Mikrofonien välinen matka on d. "
            "Molemmat mikrofonit on kytketty samaan mittaustietojen keräimeen.")
    y = 120
    f.line(40, y, 560, y, MUTED, 1.5, "6 5")
    # the source: clapper boards seen from above
    f.rect(46, y - 20, 16, 40, SAND_DARK, INK, 2.5, rx=3); f.rect(66, y - 20, 16, 40, SAND_DARK, INK, 2.5, rx=3)
    f.tex(64, y - 52, r"\text{äänilähde}", "middle")
    for x, lab in [(220, r"\text{mikrofoni 1}"), (470, r"\text{mikrofoni 2}")]:
        f.rect(x - 4, y - 10, 36, 20, IRON, INK, 2.5, rx=8); f.circle(x - 4, y, 12, ALUMINIUM, INK, 2.5)
        f.tex(x + 4, y - 52, lab, "middle")
    arcs(f, 70, y, [300, 310, 320], 8.5, MUTED, 3, (0.35, 0.65, 1.0))
    # the distance d between the microphones
    yd = 180
    f.line(208, y + 14, 208, yd + 10, MUTED, 1.5, "4 4"); f.line(458, y + 14, 458, yd + 10, MUTED, 1.5, "4 4")
    f.line(208, yd, 458, yd, INK, 2); f.line(208, yd - 10, 208, yd + 10, INK, 2); f.line(458, yd - 10, 458, yd + 10, INK, 2)
    f.tex(333, yd - 18, r"d", "middle")
    # the logger
    f.rect(270, 250, 140, 50, IRON, INK, 2.5, rx=6)
    f.tex(340, 275, r"\text{keräin}", "middle", WHITE, size=22)
    f.path(f"M{230},{y + 12} C{230},{230} {270},{240} {300},{250}", stroke=INK, w=2)
    f.path(f"M{482},{y + 12} C{482},{230} {420},{240} {380},{250}", stroke=INK, w=2)
    return f.svg()


def burst(f, x0, y0, amp, length=150, cycles=6):
    """A schematic sound pulse on a trace: an oscillation that starts at x0 and dies away."""
    pts = []
    for i in range(121):
        t = i / 120
        pts.append((x0 + t * length, y0 - amp * math.exp(-3.2 * t) * math.sin(2 * math.pi * cycles * t)))
    return f.add('<polyline points="' + " ".join(f"{n(a)},{n(b)}" for a, b in pts) +
                 f'" fill="none" stroke="{INK}" stroke-width="2.5" stroke-linejoin="round"/>')


def signal():
    """What the logger shows, as a sketch: two traces against time; the pulse reaches microphone 1 at t1 and
    microphone 2 later at t2, read at the onsets."""
    f = Fig("fy10a-signal", 380, "Kaaviokuva, ei mittausdataa: kaksi signaalia saman aika-akselin päällä. Ylempi on mikrofonin 1 "
            "signaali, alempi mikrofonin 2. Kummassakin on ensin tasainen viiva ja sitten äänipulssi, joka alkaa värähdellä ja "
            "vaimenee. Mikrofonin 1 pulssi alkaa hetkellä t yksi ja mikrofonin 2 pulssi myöhemmin hetkellä t kaksi. Aikojen "
            "erotus t kaksi miinus t yksi on merkitty pulssien alkukohtien väliin.")
    x0, x1 = 160, 530
    rows = [(100, r"\text{mikrofoni 1}", 240, 46), (220, r"\text{mikrofoni 2}", 350, 34)]
    for y, lab, start, amp in rows:
        f.line(x0, y, start, y, INK, 2.5)
        burst(f, start, y, amp, length=150)
        f.line(start + 150, y, x1, y, INK, 2.5)
        f.tex(x0 - 10, y, lab, "end", size=20)
    # the time axis with the two onsets
    ya = 320
    f.arrow(x0, ya, x1 + 24, ya, INK, 2.5, 13)
    f.tex(x1 + 30, ya, r"t", "start")
    for x, lab in [(240, r"t_1"), (350, r"t_2")]:
        f.line(x, 44 if x == 240 else 170, x, ya, MUTED, 1.5, "6 5")
        f.line(x, ya, x, ya + 7, INK, 2)
        f.tex(x, ya + 26, lab, "middle")
    yd = 282
    f.line(240, yd, 350, yd, INK, 2); f.line(240, yd - 10, 240, yd + 10, INK, 2); f.line(350, yd - 10, 350, yd + 10, INK, 2)
    f.tex(295, yd - 22, r"t_2 - t_1", "middle", bg=True)
    return f.svg()


def model():
    """The model graph: distance d against the travel time t2 - t1 is a line with slope v; a constant error in the
    distance moves the line up or down without changing its slope."""
    f = Fig("fy10a-model", 360, "Kuvaaja: mikrofonien välinen matka d kulkuajan t kaksi miinus t yksi funktiona mallin mukaan. Kuvaaja on origon kautta "
            "kulkeva suora, jonka kulmakerroin on äänen nopeus v. Katkoviivalla on sen kanssa yhdensuuntainen suora, joka ei kulje "
            "origon kautta: näin käy, jos jokaisessa matkassa on sama vakiovirhe. Kulmakerroin ei silloin muutu. Kuvaajassa ei ole "
            "mittauspisteitä.")
    ax = Axes(f, (90, 310), (470, 50), x=(0, 10), y=(0, 10), xticks=[], yticks=[], xlabel=r"t_2 - t_1", ylabel=r"d", grid=False)
    ax.line([(0, 0), (9.5, 7.6)], INK)
    ax.line([(0, 1.6), (9.5, 9.2)], MUTED, 2, "6 5")
    f.tex(ax.X(5.2), ax.Y(2.4), r"d = v \cdot (t_2 - t_1)", "start")
    f.tex(ax.X(0.4), ax.Y(7.9), r"\text{vakiovirhe matkassa}", "start", MUTED, size=22)
    return f.svg()


FIGURES = {"hero": hero, "setup": setup, "signal": signal, "model": model}
