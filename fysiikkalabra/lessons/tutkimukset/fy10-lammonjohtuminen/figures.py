"""Figures of the investigation Lämmön johtuminen lämpökameralla (scripts/figlib.py); `python scripts/investigations.py
figures fy10-lammonjohtuminen` writes them into investigation.md. Radiation is drawn as wavy lines in the heat colours
of fy3-12; no force, velocity or acceleration arrows. The graph shows a model only, never invented measurements, and
no figure shows which material conducts best."""
import math
from figlib import (Fig, Axes, INK, MUTED, WHITE, GLASS, WATER_LIGHT, WATER, SAND, SAND_DARK, GRAIN, HEAT, HEAT_LIGHT,
                    ALUMINIUM, METAL_EDGE, IRON, COPPER, RULE, RULE_LIGHT, n)
import herolib as H
from herolib import grad

TAPE = "#3b4148"          # matte tape: a dark grey a little lighter than the ink outline


def wave(f, x1, y1, x2, y2, colour, w=4, amp=7, period=26, head=14):
    """A wavy line (thermal radiation) from (x1, y1) to an arrowhead at (x2, y2)."""
    L = math.hypot(x2 - x1, y2 - y1); ux, uy = (x2 - x1) / L, (y2 - y1) / L; px, py = -uy, ux
    end = L - head; steps = max(8, int(end / 3))
    pts = [(x1 + ux * s + px * amp * math.sin(2 * math.pi * s / period), y1 + uy * s + py * amp * math.sin(2 * math.pi * s / period))
           for s in (end * i / steps for i in range(steps + 1))]
    f.path("M" + " L".join(f"{n(a)},{n(b)}" for a, b in pts), stroke=colour, w=w, extra='stroke-linecap="round"')
    bx, by = x2 - ux * head, y2 - uy * head; hw = head * 0.5
    f.path(f"M{n(x2)},{n(y2)} L{n(bx + px * hw)},{n(by + py * hw)} L{n(bx - px * hw)},{n(by - py * hw)} Z", fill=colour)


def camera(f, x, y, sc=1.0, facing=-1):
    """A handheld thermal camera seen from the side: body, lens towards `facing` (-1 left), pistol grip below."""
    w, h = 110 * sc, 62 * sc
    f.rect(x - w / 2, y - h / 2, w, h, IRON, INK, 3, 10 * sc)
    lens = x + facing * w / 2
    f.rect(lens - (14 * sc if facing < 0 else 0), y - 22 * sc, 14 * sc, 44 * sc, INK, INK, 2, 3)
    f.rect(x - 16 * sc, y + h / 2 - 2, 32 * sc, 56 * sc, IRON, INK, 3, 6 * sc)
    f.rect(x - facing * (w / 2 - 6 * sc) - 4 * sc, y - 18 * sc, 8 * sc, 36 * sc, METAL_EDGE)


def hero():
    """The opening illustration: a pot of hot water with an insulating lid; five rods of the same shape stand through
    the lid, all wrapped in the same matte tape, their different materials showing only at the top ends; steam rises
    from the pot's edge; a thermal camera on a tripod looks at the rods from the side; a stopwatch lies on the table.
    No colours of heat on the rods: the figure does not tell which material warms first."""
    f = H.hero("fy10l-hero", "Kuvitus: pöydällä on kattila kuumaa vettä, ja sen päällä on lämpöä eristävä kansi. Kannen läpi "
               "nousee viisi samanmuotoista sauvaa, jotka on päällystetty samanlaisella tummalla mattapintaisella teipillä; "
               "sauvojen yläpäistä näkyy, että ne ovat eri materiaaleista: kuparia, alumiinia, terästä, puuta ja muovia. "
               "Kattilan reunalta nousee höyryä. Kolmijalan päällä oleva lämpökamera kuvaa sauvoja sivulta, ja pöydällä "
               "on sekuntikello.")
    f.rect(0, 0, 1200, 600, grad(f, "fy10lh-wall", GLASS, "#dfe9ef"))
    f.rect(0, 470, 1200, 130, grad(f, "fy10lh-table", SAND_DARK, SAND, horizontal=True))
    for k in range(4): f.line(0, 492 + 24 * k, 1200, 488 + 24 * k, GRAIN, 1.5)
    f.line(0, 470, 1200, 470, INK, 3)
    # the pot
    f.rect(330, 330, 380, 140, H.steel(f, "fy10lh-pot"), INK, 3, 8)
    f.rect(312, 352, 22, 14, IRON, INK, 2.5, 4); f.rect(706, 352, 22, 14, IRON, INK, 2.5, 4)
    # the insulating lid with holes for the rods
    f.rect(318, 312, 404, 26, WHITE, INK, 3, 6)
    for k in range(9): f.circle(340 + 45 * k, 325, 2.2, RULE)
    H.shimmer(f, [336, 704], 306, 80, HEAT_LIGHT)
    # five rods of equal size, wrapped in the same tape; the material shows only at the top
    tops = [COPPER, ALUMINIUM, IRON, SAND, WHITE]
    for k, top in enumerate(tops):
        x = 382 + 69 * k
        f.rect(x - 11, 110, 22, 204, TAPE, INK, 3, 3)
        f.rect(x - 11, 96, 22, 22, top, INK, 3, 3)
        if top == SAND: f.line(x - 4, 100, x - 2, 116, GRAIN, 1.5); f.line(x + 4, 99, x + 5, 115, GRAIN, 1.5)
    # a stopwatch on the table
    H.stopwatch(f, 170, 418, 40, 0.2)
    # a thermal camera on a tripod, lens towards the rods
    f.line(990, 330, 948, 470, INK, 4); f.line(990, 330, 1032, 470, INK, 4); f.line(990, 330, 1004, 470, INK, 4)
    f.line(990, 330, 990, 286, INK, 4)
    camera(f, 990, 214, 1.0, -1)
    return f.svg()


def emission():
    """Why the surface matters: one metal piece at one temperature, its upper half bare and shiny, its lower half
    taped. The taped half sends much radiation to the camera; the shiny half sends little of its own and reflects
    radiation from the surroundings."""
    f = Fig("fy10l-emission", 345, "Kaaviokuva. Vasemmalla on metallikappale, jonka koko kappale on samassa lämpötilassa. "
            "Sen yläosa on paljasta kiiltävää metallia ja alaosa on päällystetty mattapintaisella teipillä. Teipatusta "
            "osasta lähtee lämpökameraa kohti voimakas lämpösäteily, kiiltävästä osasta vain heikko oma säteily. Kiiltävä "
            "pinta heijastaa lisäksi kameraan ympäristöstä tulevaa säteilyä. Oikealla on lämpökamera.")
    x0, x1 = 120, 200
    f.rect(x0, 70, x1 - x0, 110, H.steel(f, "fy10le-steel", vertical=False), INK, 3, 3)
    f.rect(x0, 180, x1 - x0, 110, TAPE, INK, 3, 3)
    f.tex(x0 - 10, 125, r"\text{kiiltävä}", "end", size=20); f.tex(x0 - 10, 235, r"\text{matta}", "end", size=20)
    # strong emission from the taped half, weak from the shiny half
    wave(f, x1 + 10, 235, 440, 235, HEAT, 6)
    wave(f, x1 + 10, 120, 440, 180, HEAT, 2, amp=5)
    # radiation from the surroundings reflected by the shiny surface
    wave(f, 300, 18, x1 + 6, 92, HEAT_LIGHT, 3, amp=5, head=12)
    wave(f, x1 + 6, 98, 440, 150, HEAT_LIGHT, 3, amp=5)
    f.tex(312, 20, r"\text{ympäristöstä}", "start", MUTED, size=20)
    f.tex(x0, 322, r"\text{sama lämpötila koko kappaleessa}", "start", MUTED, size=20)
    camera(f, 520, 190, 0.9, -1)
    f.tex(520, 290, r"\text{lämpökamera}", "middle", size=20)
    return f.svg()


def setup():
    """One possible set-up: rods through an insulating lid into hot water, the measuring point at height x above the
    lid, the camera beside the rods at a fixed distance."""
    f = Fig("fy10l-setup", 400, "Kaaviokuva yhdestä mahdollisesta koejärjestelystä sivulta. Astiassa on kuumaa vettä ja "
            "sen päällä lämpöä eristävä kansi. Kannen läpi nousee neljä samanmuotoista sauvaa, jotka ulottuvat yhtä syvälle "
            "veteen; ne on teipattu vain vedenpinnan yläpuolelta. Ensimmäisen sauvan vierellä on merkitty mittauskohta, jonka korkeus kannen yläpinnasta "
            "on x. Oikealla jalustan päällä oleva lämpökamera kuvaa kaikkia sauvoja samasta kohdasta. Veteen on "
            "upotettu lämpömittari.")
    f.rect(40, 250, 280, 120, GLASS, INK, 3, 6)
    f.rect(43, 268, 274, 99, WATER_LIGHT)
    f.line(43, 268, 317, 268, WATER, 2)
    f.rect(30, 236, 300, 16, WHITE, INK, 2.5, 4)
    xs = [90, 150, 210, 270]
    for x, bare in zip(xs, [COPPER, ALUMINIUM, IRON, SAND]):
        f.rect(x - 8, 70, 16, 270, bare, INK, 2, 2)          # bare material under water
        f.rect(x - 8, 70, 16, 198, TAPE, INK, 2, 2)          # tape only above the water line (y 268)
    # thermometer in the water
    f.line(298, 196, 298, 350, INK, 3); f.circle(298, 352, 6, HEAT, INK, 2)
    # height x of the measuring point above the lid
    yx = 150
    f.line(62, yx, 62, 236, INK, 2); f.line(54, yx, 70, yx, INK, 2); f.line(54, 236, 70, 236, INK, 2)
    f.tex(50, (yx + 236) / 2, "x", "end")
    f.circle(90, yx, 5, WHITE, INK, 2.5)
    f.tex(90, 40, r"\text{teipatut sauvat}", "start", MUTED, size=20)
    f.tex(336, 320, r"\text{kuuma vesi}", "start", MUTED, size=20)
    f.tex(336, 244, r"\text{eristävä kansi}", "start", MUTED, size=20)
    # the camera on a stand, looking left; its field of view covers all rods
    f.line(478, 140, 74, 62, MUTED, 1.2, "4 5"); f.line(478, 140, 74, 236, MUTED, 1.2, "4 5")
    f.line(530, 370, 530, 180, INK, 3); f.line(500, 370, 560, 370, INK, 3)
    camera(f, 530, 140, 0.75, -1)
    f.tex(530, 82, r"\text{lämpökamera}", "middle", size=20)
    return f.svg()


def model():
    """Model shapes of temperature against time at one point on two rods: both start at room temperature T0, the
    temperature starts to rise only after a delay, and it rises sooner and faster where heat spreads faster."""
    f = Fig("fy10l-model", 340, "Kuvaaja: lämpötila T ajan t funktiona samassa kohdassa kahdessa sauvassa mallin mukaan. "
            "Molemmat alkavat huoneen lämpötilasta T nolla. Sauvassa, jossa lämpö etenee nopeasti, lämpötila alkaa nousta lyhyen "
            "viiveen jälkeen ja nousee nopeammin; sauvassa, jossa lämpö etenee hitaasti, nousu alkaa myöhemmin ja on loivempi. "
            "Kuvaajassa ei ole mittauspisteitä.")
    ax = Axes(f, (90, 290), (470, 50), x=(0, 10), y=(0, 9), xticks=[], yticks=[], xlabel="t", ylabel="T", grid=False,
              origin_label=False)
    ax.line([(0, 1), (10, 1)], MUTED, 2, "6 5")
    f.tex(ax.x0 - 10, ax.Y(1), "T_0", "end")
    ax.curve(lambda t: 1 + 8 * math.erfc(1.6 / math.sqrt(t)) if t > 0 else 1, 0, 10, INK)
    ax.curve(lambda t: 1 + 8 * math.erfc(4.0 / math.sqrt(t)) if t > 0 else 1, 0, 10, INK, dash="9 6")
    f.tex(ax.X(9.8), ax.Y(5.9), r"\text{lämpö etenee nopeasti}", "end", size=20)
    f.tex(ax.X(9.8), ax.Y(2.5), r"\text{lämpö etenee hitaasti}", "end", size=20)
    return f.svg()


FIGURES = {"hero": hero, "emission": emission, "setup": setup, "model": model}
