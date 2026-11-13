"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy7-8` writes them into lesson.md.
FY7 colours (course brief): current #7048e8, magnetic field and flux #2b8a3e, heat (losses) #ffc078 -> #e8590c."""
import math
from figlib import (Fig, Axes, fi, INK, MUTED, WHITE, RULE, RULE_LIGHT, HOT, HEAT, HEAT_LIGHT, GOOD, IRON, COPPER,
                    ALUMINIUM, METAL_EDGE, SAND, SAND_LIGHT, GRAIN, GLASS, PAPER, WATER, WATER_LIGHT, COLD, COLD_LIGHT, n)
import herolib as H

CURRENT, FIELD = "#7048e8", GOOD


def ac_source(f, x, y, r=24):
    """An AC source: a circle with a sine wave inside."""
    f.circle(x, y, r, WHITE, INK, 2.5)
    f.path(f"M{n(x - r * 0.6)},{n(y)} C{n(x - r * 0.3)},{n(y - r * 0.7)} {n(x)},{n(y - r * 0.7)} {n(x)},{n(y)} "
           f"C{n(x)},{n(y + r * 0.7)} {n(x + r * 0.3)},{n(y + r * 0.7)} {n(x + r * 0.6)},{n(y)}", stroke=INK, w=2.5)


def trafo_symbol(f, x, y, r=15):
    """The circuit symbol of a transformer: two overlapping circles."""
    f.circle(x - r * 0.55, y, r, WHITE, INK, 2.5)
    f.circle(x + r * 0.55, y, r, "none", INK, 2.5)


def transformer():
    f = Fig("fy78-transformer", 360, "Periaatekuva muuntajasta, ei mittakaavassa. Suljetun rautasydämen vasempaan "
            "haaraan on kierretty ensiökäämi, jossa on enemmän kierroksia, ja oikeaan haaraan toisiokäämi, jossa on "
            "vähemmän kierroksia. Ensiökäämi on kytketty vaihtojännitelähteeseen, jonka jännite on U1, ja toisiokäämi "
            "lamppuun, jonka jännite on U2. Vihreä katkoviiva nuolineen kiertää rautasydämen sisällä: ensiövirran "
            "synnyttämä muuttuva magneettivuo kulkee sydäntä pitkin myös toisiokäämin läpi.")
    # the laminated iron core: a closed frame
    f.path("M150,60 H450 V300 H150 Z M200,110 V250 H400 V110 Z", IRON, INK, 2.5, extra='fill-rule="evenodd"')
    for k in range(1, 5):
        d = 10 * k
        f.path(f"M{150 + d},{60 + d} H{450 - d} V{300 - d} H{150 + d} Z", stroke=METAL_EDGE, w=1)
    # the magnetic flux in the core: a dashed loop along the core's middle line, clockwise
    f.add(f'<path d="M175,85 H425 V275 H175 Z" fill="none" stroke="{FIELD}" stroke-width="3" stroke-dasharray="9 7"/>')
    for x, y, dx, dy in ((300, 85, 1, 0), (425, 180, 0, 1), (300, 275, -1, 0), (175, 180, 0, -1)):
        f.path(f"M{x + 9 * dx},{y + 9 * dy} L{x - 7 * dx - 7 * dy},{y - 7 * dy + 7 * dx} L{x - 7 * dx + 7 * dy},{y - 7 * dy - 7 * dx} Z", FIELD)
    f.tex(300, 34, r"\Phi", "middle", FIELD)
    # primary coil: 8 turns on the left leg; secondary: 4 turns on the right leg
    for k in range(8):
        f.rect(136, 124 + 15 * k, 78, 9, COPPER, INK, 1.5, 4)
    for k in range(4):
        f.rect(386, 146 + 20 * k, 78, 9, COPPER, INK, 1.5, 4)
    # leads: primary to the AC source, secondary to the lamp
    f.path("M136,128 H70 V156", stroke=INK, w=2.5)
    f.path("M136,233 H70 V204", stroke=INK, w=2.5)
    ac_source(f, 70, 180)
    f.tex(40, 180, r"U_1", "end", w=46)
    f.path("M464,150 H545 V162", stroke=INK, w=2.5)
    f.path("M464,213 H545 V200", stroke=INK, w=2.5)
    f.circle(545, 181, 19, HEAT_LIGHT, INK, 2.5)
    f.line(533, 169, 557, 193, INK, 1.5); f.line(557, 169, 533, 193, INK, 1.5)
    f.tex(545, 232, r"U_2", "middle")
    # current arrows on the leads
    f.arrow(112, 120, 84, 120, CURRENT, 2.5, 11)
    f.tex(98, 98, r"I_1", "middle", CURRENT)
    f.arrow(488, 142, 520, 142, CURRENT, 2.5, 11)
    f.tex(504, 120, r"I_2", "middle", CURRENT)
    f.tex(222, 180, r"N_1", "start")
    f.tex(378, 180, r"N_2", "end")
    f.tex(150, 332, r"\text{ensiökäämi}", "middle")
    f.tex(300, 332, r"\text{rautasydän}", "middle")
    f.tex(450, 332, r"\text{toisiokäämi}", "middle")
    return f.svg()


def plant(f, x, y):
    """A small power plant: a turbine hall with a chimney and a generator (local origin at the lower-left corner)."""
    f.rect(x + 44, y - 104, 14, 40, IRON, INK, 2)
    f.rect(x, y - 64, 64, 64, SAND_LIGHT, INK, 2.5)
    f.path(f"M{x - 5},{y - 64} H{x + 69} L{x + 52},{y - 80} H{x + 12} Z", IRON, INK, 2.5)
    f.circle(x + 32, y - 30, 16, ALUMINIUM, INK, 2.5)
    f.circle(x + 32, y - 30, 5, INK)


def grid():
    f = Fig("fy78-grid", 372, "Kaavakuva sähköverkosta yksiviivaesityksenä, ei mittakaavassa: todellisissa kolmivaiheisissa johdoissa on kolme vaihejohdinta. Ylärivillä voimalaitoksen generaattorin "
            "jännite 20 kV nostetaan muuntajalla 400 kilovoltiksi, ja kantaverkon suuret pylväät vievät sähkön "
            "sähköasemalle. Sähköasemalla muuntaja laskee jännitteen, ja alarivillä jakeluverkon pienet pylväät vievät "
            "20 kV:n jännitteen muuntamolle, joka laskee sen pienjänniteverkon jännitteeksi: kotien pistorasioissa on 230 volttia.", width=640)
    # top row: plant -> step-up transformer -> 400 kV line -> substation
    plant(f, 16, 170)
    f.line(80, 150, 152, 150, INK, 2.5)
    trafo_symbol(f, 168, 150)
    f.tex(132, 118, r"20\,\text{kV}", "middle", w=86)
    for x in (270, 380):
        f.path(f"M{x - 20},170 L{x - 4},70 H{x + 4} L{x + 20},170", stroke=IRON, w=3)
        f.line(x - 30, 80, x + 30, 80, IRON, 3)
        f.line(x - 10, 120, x + 10, 140, IRON, 1.5); f.line(x + 10, 120, x - 10, 140, IRON, 1.5)
    f.path("M186,150 Q228,96 270,84 Q325,104 380,84 Q430,100 470,132", stroke=INK, w=2.5)
    f.tex(325, 44, r"400\,\text{kV}", "middle", w=100)
    f.tex(325, 196, r"\text{kantaverkko}", "middle")
    trafo_symbol(f, 488, 150)
    f.rect(460, 120, 56, 56, "none", MUTED, 1.5, 4, extra='stroke-dasharray="5 4"')
    f.tex(496, 198, r"\text{sähköasema}", "start")   # right of the line down to the bottom row (visual r1)
    # down to the bottom row: 20 kV distribution line to the transformer kiosk and a house
    f.path("M488,176 V300 H420", stroke=INK, w=2.5)
    for x in (400, 300):
        f.rect(x - 4, 282, 8, 46, SAND, INK, 2)
        f.line(x - 18, 286, x + 18, 286, INK, 2.5)
    f.path("M420,300 Q410,300 400,286 Q350,302 300,286 Q262,292 232,300", stroke=INK, w=2.5)
    f.tex(350, 254, r"20\,\text{kV}", "middle", w=86)
    f.tex(350, 350, r"\text{jakeluverkko}", "middle")
    f.rect(196, 278, 36, 46, ALUMINIUM, INK, 2.5, 3)
    trafo_symbol(f, 214, 300, 10)
    f.line(196, 300, 150, 300, INK, 2.5)
    f.tex(214, 248, r"\text{muuntamo}", "middle")
    H.house(f, 66, 334, 84, 62)
    f.tex(96, 212, r"230\,\text{V}", "middle", w=90)
    return f.svg()


def loss_graph():
    f = Fig("fy78-loss-graph", 340, "Kuvaaja mittakaavassa: siirtojohdossa lämmöksi muuttuvan tehon osuus siirretystä "
            "tehosta prosentteina siirtojännitteen funktiona kilovoltteina, kun siirretty teho on 200 MW ja johdon "
            "resistanssi 6,0 ohmia yksinkertaistetussa kaksijohtimisessa mallissa. Käyrä laskee jyrkästi: 100 kV:lla osuus on 12 %, 200 kV:lla 3,0 % ja 400 kV:lla "
            "0,75 %. Kun jännite kaksinkertaistuu, osuus pienenee neljäsosaan.")
    ax = Axes(f, (96, 290), (470, 60), x=(0, 400), y=(0, 25), xticks=[50 * k for k in range(1, 9)],
              yticks=[5 * k for k in range(1, 6)], xlabel=r"U\ (\text{kV})", ylabel=r"P_\text{h} : P\ (\%)",
              xfmt=lambda v: fi(v) if v % 100 == 0 else "")
    share = lambda u: 6.0 * 200e6 / (u * 1e3) ** 2 * 100           # 100 % · R P / U², P = 200 MW, R = 6,0 Ω
    ax.curve(share, 70, 400, HEAT, 3)
    for u in (100, 200, 400):
        ax.guide(u, share(u))
        ax.point(u, share(u), HEAT)
    f.tex(ax.X(100) + 14, ax.Y(12), r"12\,\%", "start", HEAT, bg=True)
    f.tex(ax.X(200) + 6, ax.Y(3) - 26, r"3{,}0\,\%", "start", HEAT, bg=True)
    f.tex(ax.X(400) - 4, ax.Y(0.75) - 26, r"0{,}75\,\%", "end", HEAT, bg=True)
    f.tex(470, 92, r"P = 200\,\text{MW}", "end", w=170)
    f.tex(470, 130, r"R = 6{,}0\,\Omega", "end", w=150)
    return f.svg()


def loss_current():
    """Task figure: a model line (resistance wire) in the lab, heating power P_h against the current I: five measured
    points and the fitted curve P_h = k I² through the grid point (5,0 A; 20 W), dashed beyond 5 A. No R written."""
    f = Fig("fy78-loss-current", 340, "Kuvaaja mittakaavassa: pienoismallin siirtojohdossa lämmöksi muuttuva teho "
            "P_h watteina virran I funktiona ampeereina. Viisi mittauspistettä virroilla 1,0; 2,0; 3,0; 4,0 ja 5,0 A, "
            "tehot 0,9; 3,1; 7,4; 12,6 ja 20,1 W, sekä pisteisiin sovitettu paraabeli, joka alkaa origosta, kulkee "
            "ruudukon pisteen (5,0 A; 20 W) kautta ja jatkuu katkoviivana viimeisen mittauspisteen jälkeen. Ruudukon "
            "väli on 0,5 A ja 2 W.")
    ax = Axes(f, (96, 290), (470, 56), x=(0, 6), y=(0, 24), xticks=[0.5 * k for k in range(1, 13)],
              yticks=[2 * k for k in range(1, 13)], xlabel=r"I\ (\text{A})", ylabel=r"P_\text{h}\ (\text{W})",
              xfmt=lambda v: fi(v) if abs(v - round(v)) < 1e-9 else "", yfmt=lambda v: fi(v) if v % 4 == 0 else "")
    ax.curve(lambda i: 0.8 * i * i, 0, 5, HEAT, 3)
    ax.curve(lambda i: 0.8 * i * i, 5, 5.45, HEAT, 3, dash="7 5")
    for i, p in ((1, 0.9), (2, 3.1), (3, 7.4), (4, 12.6), (5, 20.1)):
        ax.point(i, p, CURRENT)
    return f.svg()


def hero():
    """The opening illustration: a power plant by a river, a line of pylons crossing the land, a town far away."""
    f = H.hero("fy78-hero", "Kuvitus: vasemmalla joen varrella voimalaitos ja sen muuntaja, josta lähtee pitkä "
               "voimajohto. Suuret ristikkopylväät kantavat johtimia peltojen ja metsän yli kohti oikealla kaukana "
               "näkyvää kaupunkia, jonka ikkunoissa palaa valo.")
    H.sky(f, "fy78h")
    H.hills(f, "fy78h-hill", 380, [COLD_LIGHT, "#b2f2bb"], amp=30, seed=3)
    f.rect(0, 430, 1200, 170, H.grad(f, "fy78h-field", SAND_LIGHT, "#e9c98a"))
    H.forest(f, 430, 50, 26, GOOD, seed=4, x0=0, x1=1200, depth=12)
    # river at the left
    f.path("M0,520 C120,500 180,470 260,440 L300,440 C230,480 160,540 80,600 L0,600 Z", H.grad(f, "fy78h-river", WATER_LIGHT, WATER))
    # power plant and its step-up transformer
    f.rect(70, 300, 200, 140, SAND_LIGHT, INK, 3)
    f.path("M60,300 L170,250 L280,300 Z", IRON, INK, 3)
    for k in range(4):
        f.rect(90 + 44 * k, 330, 26, 40, GLASS, INK, 2)
    f.rect(290, 380, 70, 60, ALUMINIUM, INK, 3, 4)
    for k in range(3):
        f.rect(298 + 20 * k, 362, 10, 20, WHITE, INK, 2, 3)
    # pylons getting smaller towards the town
    arms = [H.pylon(f, x, 440 - d, h, sc) for x, d, h, sc in ((470, 0, 300, 1.4), (720, 10, 210, 1.0), (920, 16, 140, 0.7))]
    H.wire(f, (360, 370), arms[0][0], sag=14)
    for a, b in zip(arms, arms[1:]):
        for k in range(4):
            H.wire(f, a[k], b[k], sag=26)
    # the town
    for x, w, h in ((1010, 60, 50), (1080, 50, 70), (1135, 50, 44)):
        f.rect(x, 424 - h, w, h, SAND_LIGHT, INK, 2.5)
        f.rect(x + 12, 424 - h + 12, 14, 14, HEAT_LIGHT, INK, 1.5)
        f.rect(x + w - 24, 424 - h + 12, 14, 14, HEAT_LIGHT, INK, 1.5)
    H.wire(f, arms[2][0], (1010, 400), sag=10)
    return f.svg()


def scene():
    """A second everyday scene: a phone charging from a wall socket."""
    f = H.scene("fy78-scene", "Kuvitus: seinäpistorasiaan on kytketty pieni puhelimen laturi, ja sen johto vie "
                "pöydällä olevaan puhelimeen, joka latautuu.")
    f.rect(0, 0, 600, 360, PAPER)
    f.rect(0, 270, 600, 90, H.grad(f, "fy78s-desk", SAND_LIGHT, SAND))
    # wall socket and the charger plugged in
    f.rect(120, 60, 120, 120, WHITE, INK, 3, 14)
    f.circle(180, 120, 42, RULE_LIGHT, INK, 2)
    f.rect(150, 100, 60, 64, WHITE, INK, 3, 10)
    f.rect(166, 116, 28, 8, IRON, rx=3)
    # cable to the phone
    f.path("M180,164 C180,240 300,200 330,290", stroke=INK, w=5, extra='stroke-linecap="round"')
    f.rect(300, 286, 150, 54, INK, rx=10)
    f.rect(310, 292, 130, 42, H.grad(f, "fy78s-screen", H.ICE, COLD, horizontal=True), rx=4)
    f.rect(360, 304, 30, 18, "none", WHITE, 2, 2)
    f.rect(364, 308, 16, 10, GOOD_FILL, rx=1)
    return f.svg()


def loss_graph_curve():
    """Task figure: the loss share of a 200 MW line against the transmission voltage, the curve only (no marked points,
    no values, no R), a fine grid of 25 kV and 1 %. The curve passes the grid point (200 kV; 3,0 %)."""
    f = Fig("fy78-loss-graph-curve", 340, "Kuvaaja mittakaavassa: siirtojohdossa lämmöksi muuttuvan tehon osuus siirretystä "
            "tehosta prosentteina siirtojännitteen funktiona kilovoltteina, kun siirretty teho on 200 MW "
            "yksinkertaistetussa kaksijohtimisessa mallissa. Laskeva käyrä alkaa jännitteestä 70 kV ja päättyy "
            "jännitteeseen 400 kV, ja se kulkee ruudukon pisteen (200 kV; 3,0 %) kautta. Ruudukon väli on 25 kV ja 1 %.")
    ax = Axes(f, (96, 290), (470, 60), x=(0, 400), y=(0, 25), xticks=[25 * k for k in range(1, 17)],
              yticks=[k for k in range(1, 25)], xlabel=r"U\ (\text{kV})", ylabel=r"P_\text{h} : P\ (\%)",
              xfmt=lambda v: fi(v) if v % 100 == 0 else "", yfmt=lambda v: fi(v) if v % 5 == 0 else "")
    ax.curve(lambda u: 6.0 * 200e6 / (u * 1e3) ** 2 * 100, 70, 400, HEAT, 3)
    f.tex(470, 92, r"P = 200\,\text{MW}", "end", w=170)
    return f.svg()


GOOD_FILL = "#2b8a3e"

FIGURES = {"hero": hero, "transformer": transformer, "grid": grid, "loss-graph": loss_graph, "scene": scene,
           "loss-current": loss_current, "loss-graph-curve": loss_graph_curve}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "transformer": "reveals: the changing flux in the iron core links the primary and secondary coils",
    "grid": "reveals: the voltage levels of the grid (20 kV, 400 kV, 20 kV, 230 V) and where transformers sit",
    "loss-graph": "reveals: the loss share falls as 1/U² (12 %, 3,0 %, 0,75 % at 100, 200, 400 kV for 200 MW and 6,0 Ω)",
    "loss-current": "safe: heating power P_h of a model line against I with a fitted parabola through (5,0 A; 20 W), no R",
    "loss-graph-curve": "safe: loss share of a 200 MW model line against U as a bare curve through the grid point (200 kV; 3,0 %), no R, no marked values",
}
