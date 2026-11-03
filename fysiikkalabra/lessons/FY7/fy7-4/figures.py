"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy7-4` writes them into lesson.md.
FY7 colours (course brief): force #c92a2a, current #7048e8, magnetic field #2b8a3e, N pole #f2a69c, S pole #d0e6fb,
field into the page a cross, out of the page a dot in a circle."""
import math
from figlib import (Fig, Axes, fi, INK, MUTED, WHITE, RULE, RULE_LIGHT, HOT, HOT_LIGHT, COLD_LIGHT, GOOD, IRON, COPPER,
                    ALUMINIUM, METAL_EDGE, SAND, SAND_LIGHT, SAND_DARK, GRAIN, GLASS, PAPER, n)
import herolib as H

FORCE, CURRENT, FIELD, NPOLE, SPOLE = HOT, "#7048e8", GOOD, HOT_LIGHT, COLD_LIGHT


def into(f, x, y, r=13, colour=CURRENT):
    """A current or a quantity into the page: a cross in a circle."""
    f.circle(x, y, r, WHITE, colour, 2.5)
    d = r * 0.55
    f.line(x - d, y - d, x + d, y + d, colour, 2.5); f.line(x + d, y - d, x - d, y + d, colour, 2.5)


def out(f, x, y, r=13, colour=CURRENT):
    """Out of the page: a dot in a circle."""
    f.circle(x, y, r, WHITE, colour, 2.5)
    f.circle(x, y, r * 0.32, colour)


def pole(f, x, y, w, h, kind, label=True):
    f.rect(x, y, w, h, NPOLE if kind == "N" else SPOLE, INK, 2.5, 4)
    if label: f.tex(x + w / 2, y + h / 2, r"\text{" + kind + "}", "middle")


def swing():
    f = Fig("fy74-swing", 360, "Kaksi periaatekuvaa, ei mittakaavassa. Vasemmalla johdin nähdään päästä päin kahden "
            "magneetin navan välissä: N-napa on ylhäällä ja S-napa alhaalla, joten magneettikenttä osoittaa alaspäin. Virta "
            "kulkee johtimessa paperiin päin, ja magneettikentän voima työntää johdinta vasemmalle, kohtisuoraan sekä virtaa "
            "että kenttää vastaan. Oikealla oikean käden sääntö: peukalo osoittaa virran suuntaan, muut sormet kentän "
            "suuntaan (vinosti piirretty nuoli tulee kohti katsojaa), ja voima osoittaa kämmenestä ulos, tässä alaspäin. Kolme nuolta ovat keskenään kohtisuorassa.")
    # left: the wire between the poles, seen end-on
    pole(f, 70, 40, 180, 56, "N")
    pole(f, 70, 268, 180, 56, "S")
    for x in (84, 236):
        f.arrow(x, 104, x, 258, FIELD, 2.5, 13)
    f.tex(246, 180, r"\overline{B}", "start", FIELD)
    into(f, 160, 180, 16)
    f.arrow(140, 180, 98, 180, FORCE, 3.5, 14)
    f.tex(120, 152, r"\overline{F}", "middle", FORCE)
    f.tex(160, 222, r"I", "middle", CURRENT)
    f.line(300, 24, 300, 340, RULE, 2, "6 6")
    # right: the right-hand rule as three perpendicular arrows (a pseudo-3D corner; the oblique arrow comes towards the viewer)
    ox, oy = 400, 120
    f.arrow(ox, oy, ox + 150, oy, CURRENT, 3.5, 15)            # thumb: current to the right
    f.arrow(ox, oy, ox - 70, oy + 64, FIELD, 3.5, 15)          # fingers: field towards the viewer
    f.arrow(ox, oy, ox, oy + 170, FORCE, 3.5, 15)              # palm: force down
    f.circle(ox, oy, 5, INK)
    f.tex(ox + 150, oy - 24, r"I", "middle", CURRENT)
    f.tex(ox + 120, oy + 26, r"\text{peukalo}", "middle", w=110)
    f.tex(ox - 80, oy + 66, r"\overline{B}", "end", FIELD)
    f.tex(ox - 66, oy + 104, r"\text{sormet}", "middle", w=96)
    f.tex(ox + 16, oy + 160, r"\overline{F}", "start", FORCE)
    f.tex(ox + 16, oy + 198, r"\text{kämmen}", "start", w=110)
    f.tex(450, 28, r"\text{oikean käden sääntö}", "middle", w=280)
    return f.svg()


def angle():
    f = Fig("fy74-angle", 340, "Periaatekuva ylhäältä, ei mittakaavassa. Vaakasuorat vihreät kenttäviivat osoittavat "
            "oikealle. Johdin on kulmassa alfa kenttään nähden, ja virta kulkee johdinta pitkin yläoikealle. Kentän "
            "johtimeen kohtisuora komponentti B sin alfa on piirretty katkoviivalla. Voima osoittaa paperiin päin, mitä "
            "kuvaa risti ympyrän sisällä johtimen keskellä.")
    for y in (60, 120, 180, 240, 300):
        f.line(30, y, 570, y, FIELD, 2)
        f.path(f"M{n(470)},{y} l-14,-7 v14 Z", FIELD)
    f.tex(560, 34, r"\overline{B}", "end", FIELD)
    cx, cy, a = 300, 180, math.radians(40)
    L = 190
    dx, dy = math.cos(a), -math.sin(a)
    f.line(cx - L * dx, cy - L * dy, cx + L * dx, cy + L * dy, COPPER, 7, cap="round")
    # the current beside the wire
    nx, ny = -math.sin(a), -math.cos(a)                     # the normal on the upper-left side
    f.arrow(cx - 120 * dx + 22 * nx, cy - 120 * dy + 22 * ny, cx + 120 * dx + 22 * nx, cy + 120 * dy + 22 * ny, CURRENT, 3, 14)
    f.tex(cx - 40 * dx + 46 * nx, cy - 40 * dy + 46 * ny, "I", "middle", CURRENT)
    # the angle between the wire and the field
    f.line(cx, cy, cx + 150, cy, MUTED, 1.5, "6 5")
    r = 70
    f.path(f"M{cx + r},{cy} A{r},{r} 0 0 0 {n(cx + r * math.cos(a))},{n(cy - r * math.sin(a))}", stroke=INK, w=2)
    f.tex(cx + 92 * math.cos(a / 2), cy - 92 * math.sin(a / 2), r"\alpha", "middle")
    # the component of B perpendicular to the wire, at a point further along the wire
    px, py = cx + 150 * dx, cy + 150 * dy
    pl = 64
    perp = (math.sin(a), math.cos(a))                       # unit vector perpendicular to the wire, down-right
    f.add(f'<line x1="{n(px)}" y1="{n(py)}" x2="{n(px + pl * perp[0])}" y2="{n(py + pl * perp[1])}" stroke="{FIELD}" stroke-width="2.5" stroke-dasharray="7 5"/>')
    tipx, tipy = px + pl * perp[0], py + pl * perp[1]
    f.path(f"M{n(tipx + 6 * perp[0])},{n(tipy + 6 * perp[1])} L{n(tipx - 9 * perp[0] - 6 * perp[1])},{n(tipy - 9 * perp[1] + 6 * perp[0])} "
           f"L{n(tipx - 9 * perp[0] + 6 * perp[1])},{n(tipy - 9 * perp[1] - 6 * perp[0])} Z", FIELD)
    f.tex(tipx + 14, tipy + 22, r"B \sin\alpha", "start", FIELD, w=110, bg=True)
    # the force into the page
    into(f, cx, cy, 15, FORCE)
    f.tex(cx + 20, cy + 36, r"\overline{F}", "start", FORCE, bg=True)
    return f.svg()


def wires():
    f = Fig("fy74-wires", 360, "Kaksi periaatekuvaa rinnakkaisista johtimista päästä päin, ei mittakaavassa. Vasemmalla "
            "kummassakin johtimessa virta kulkee paperista ulos. Vasemman johtimen magneettikenttä kiertää sitä "
            "vastapäivään, ja oikean johtimen kohdalla kenttä osoittaa ylöspäin. Voimat osoittavat johtimesta toiseen: "
            "johtimet vetävät toisiaan puoleensa. Oikealla virrat ovat vastakkaissuuntaiset, oikean johtimen virta "
            "kulkee paperiin päin, ja voimat osoittavat poispäin toisistaan: johtimet hylkivät toisiaan.")
    f.tex(150, 28, r"\text{samansuuntaiset virrat}", "middle", w=270)
    f.tex(450, 28, r"\text{vastakkaiset virrat}", "middle", w=250)
    f.line(300, 20, 300, 340, RULE, 2, "6 6")
    for x0, same in ((150, True), (450, False)):
        x1, x2, y, d = x0 - 45, x0 + 45, 190, 90
        # the field of the left wire: a circle through the right wire, anticlockwise, and its direction at the right wire
        f.circle(x1, y, d, "none", FIELD, 2)
        f.path(f"M{x1},{y - d} l12,-7 v14 Z", FIELD)          # anticlockwise: at the top the field points left
        f.arrow(x2, y - 18, x2, y - 62, FIELD, 3, 12)
        f.tex(x2 + 12, y - 54, r"\overline{B}_1", "start", FIELD)
        out(f, x1, y, 14)
        (out if same else into)(f, x2, y, 14)
        f.tex(x1, y + 38, r"I_1", "middle", CURRENT)
        f.tex(x2 + 14, y + 42, r"I_2", "start", CURRENT)
        if same:
            f.arrow(x1 + 17, y, x1 + 41, y, FORCE, 3.5, 12); f.arrow(x2 - 17, y, x2 - 41, y, FORCE, 3.5, 12)
        else:
            f.arrow(x1 - 17, y, x1 - 47, y, FORCE, 3.5, 12); f.arrow(x2 + 17, y, x2 + 47, y, FORCE, 3.5, 12)
        f.tex(x0, y - 26, r"\overline{F}", "middle", FORCE) if same else f.tex(x1 - 34, y - 26, r"\overline{F}", "middle", FORCE)
        f.tex(x0, 336, r"\text{vetävät}" if same else r"\text{hylkivät}", "middle", w=120)
    return f.svg()


def motor():
    f = Fig("fy74-motor", 380, "Kaksi periaatekuvaa tasavirtamoottorista, ei mittakaavassa. Vasemmalla virtasilmukka "
            "nähdään akselin suunnasta N- ja S-navan välissä; magneettikenttä osoittaa vasemmalta oikealle. Silmukan "
            "toisessa sivussa virta kulkee paperiin päin, toisessa paperista ulos. Sivuihin kohdistuvat voimat ovat "
            "vastakkaissuuntaiset, toinen alaspäin ja toinen ylöspäin, ja ne kääntävät silmukkaa vastapäivään. "
            "Oikealla kommutaattori: akselin ympärillä on kahteen osaan halkaistu rengas, jota kaksi hiiliharjaa "
            "koskettaa. Harjat on kytketty virtalähteen plus- ja miinusnapaan.")
    pole(f, 20, 110, 52, 170, "N")
    pole(f, 288, 110, 52, 170, "S")
    for y in (130, 260):
        f.arrow(82, y, 278, y, FIELD, 2, 12)
    f.tex(276, 284, r"\overline{B}", "end", FIELD)
    cx, cy, R, t = 180, 195, 70, math.radians(25)
    ax, ay = cx - R * math.cos(t), cy + R * math.sin(t)       # the side with the current into the page
    bx, by = cx + R * math.cos(t), cy - R * math.sin(t)       # the side with the current out of the page
    f.circle(cx, cy, R, "none", RULE, 1.5)
    f.line(ax, ay, bx, by, COPPER, 4)
    f.circle(cx, cy, 6, INK)
    into(f, ax, ay, 13); out(f, bx, by, 13)
    f.arrow(ax, ay + 16, ax, ay + 76, FORCE, 3.5, 13)
    f.arrow(bx, by - 16, bx, by - 76, FORCE, 3.5, 13)
    f.tex(ax + 14, ay + 66, r"\overline{F}", "start", FORCE)
    f.tex(bx - 14, by - 66, r"\overline{F}", "end", FORCE)
    # the sense of rotation: an arc arrow round the axle, anticlockwise
    rr = 98
    a0, a1 = math.radians(105), math.radians(150)
    f.path(f"M{n(cx + rr * math.cos(a0))},{n(cy - rr * math.sin(a0))} A{rr},{rr} 0 0 0 {n(cx + rr * math.cos(a1))},{n(cy - rr * math.sin(a1))}", stroke=INK, w=2.5)
    tx_, ty_ = cx + rr * math.cos(a1), cy - rr * math.sin(a1)
    ux, uy = -math.sin(a1), -math.cos(a1)                  # the direction of motion on the screen at the arc's end
    f.path(f"M{n(tx_ + 12 * ux)},{n(ty_ + 12 * uy)} L{n(tx_ - 4 * ux - 7 * uy)},{n(ty_ - 4 * uy + 7 * ux)} L{n(tx_ - 4 * ux + 7 * uy)},{n(ty_ - 4 * uy - 7 * ux)} Z", INK)
    f.tex(180, 360, r"\text{virtasilmukka}", "middle", w=170)
    f.line(370, 30, 370, 350, RULE, 2, "6 6")
    # the commutator: a split ring and two brushes
    kx, ky, kr = 482, 190, 38
    f.path(f"M{kx - 6},{ky - kr} A{kr},{kr} 0 0 0 {kx - 6},{ky + kr} V{ky + kr - 14} A{kr - 14},{kr - 14} 0 0 1 {kx - 6},{ky - kr + 14} Z", COPPER, INK, 2)
    f.path(f"M{kx + 6},{ky - kr} A{kr},{kr} 0 0 1 {kx + 6},{ky + kr} V{ky + kr - 14} A{kr - 14},{kr - 14} 0 0 0 {kx + 6},{ky - kr + 14} Z", COPPER, INK, 2)
    f.circle(kx, ky, 8, INK)
    f.rect(kx - kr - 28, ky - 14, 28, 28, IRON, INK, 2, 3)
    f.rect(kx + kr, ky - 14, 28, 28, IRON, INK, 2, 3)
    f.line(kx - kr - 28, ky, kx - kr - 40, ky, INK, 2.5); f.line(kx + kr + 28, ky, kx + kr + 40, ky, INK, 2.5)
    f.tex(kx - kr - 44, ky, "+", "end")
    f.tex(kx + kr + 44, ky, "-", "start")
    f.tex(kx, 92, r"\text{kommutaattori}", "middle", w=180)
    f.tex(kx, 290, r"\text{hiiliharjat}", "middle", w=150)
    f.line(kx - kr - 14, ky + 18, kx - 40, 272, MUTED, 1.5); f.line(kx + kr + 14, ky + 18, kx + 40, 272, MUTED, 1.5)
    return f.svg()


def speaker():
    f = Fig("fy74-speaker", 360, "Kaiuttimen poikkileikkaus, periaatekuva, ei mittakaavassa. Vasemmalla on rautainen "
            "keskinapa ja sen ympärillä rengasmagneetti ja etulevy. Keskinapa on N-napa ja etulevy S-napa, joten "
            "kapeassa raossa magneettikenttä osoittaa säteittäin ulospäin, yläraossa ylös ja alaraossa alas. Raossa on "
            "puhekela: sen poikkileikkauksessa virta kulkee yläpuolella paperiin päin ja alapuolella paperista ulos. "
            "Kummallakin puolella voima osoittaa oikealle, kohti kartiota, joka on kiinnitetty kelaan.")
    ay = 180
    # back plate and centre pole (iron), ring magnet, front plate; the gap between the front plate and the centre pole
    f.rect(40, 60, 24, 240, IRON, INK, 2, 3)
    f.rect(64, 150, 176, 60, IRON, INK, 2, 3)
    f.rect(64, 60, 56, 54, METAL_EDGE, INK, 2, 3); f.rect(64, 246, 56, 54, METAL_EDGE, INK, 2, 3)
    f.rect(120, 60, 56, 54, SPOLE, INK, 2, 3); f.rect(120, 246, 56, 54, SPOLE, INK, 2, 3)
    f.tex(208, ay, r"\text{N}", "middle", WHITE)
    f.tex(148, 87, r"\text{S}", "middle"); f.tex(148, 273, r"\text{S}", "middle")
    # the voice coil on its former, which runs to the cone
    f.rect(126, 141, 142, 4, SAND_DARK); f.rect(126, 215, 142, 4, SAND_DARK)
    for x in (134, 152):
        into(f, x, 130, 7); out(f, x, 230, 7)
    f.tex(112, 130, "I", "end", CURRENT); f.tex(112, 230, "I", "end", CURRENT)
    # radial field in the gaps: from the N pole outwards
    f.arrow(168, 148, 168, 116, FIELD, 2.5, 10); f.arrow(168, 212, 168, 244, FIELD, 2.5, 10)
    f.tex(186, 98, r"\overline{B}", "start", FIELD)
    # the cone and the dust cap
    f.path("M268,141 L420,40 L434,40 L282,143 Z", SAND_LIGHT, INK, 2)
    f.path("M268,219 L420,320 L434,320 L282,217 Z", SAND_LIGHT, INK, 2)
    f.path("M268,141 Q306,180 268,219", stroke=INK, w=2)
    # the forces on the coil, towards the cone
    f.arrow(184, 126, 246, 126, FORCE, 3.5, 13)
    f.arrow(184, 234, 246, 234, FORCE, 3.5, 13)
    f.tex(252, 112, r"\overline{F}", "start", FORCE)
    f.tex(252, 248, r"\overline{F}", "start", FORCE)
    f.tex(446, 40, r"\text{kartio}", "start", w=90)
    f.tex(40, 330, r"\text{rengasmagneetti}", "start", w=190)
    f.tex(440, 180, r"I \text{ vaihtelee}", "middle", w=150)
    f.tex(440, 222, r"\Rightarrow F \text{ vaihtelee}", "middle", w=230)
    return f.svg()


def balance_points():
    """Task figure: a current balance, reading change Δm against the current I, five measured points and the line
    through the origin fitted to them, passing (5,0 A; 1,50 g). No B or slope written."""
    f = Fig("fy74-balance-points", 340, "Kuvaaja mittakaavassa: virtavaa'an lukeman muutos delta m grammoina virran I "
            "funktiona ampeereina. Viisi mittauspistettä virroilla 1,0; 2,0; 3,0; 4,0 ja 5,0 A, muutokset 0,30; 0,60; "
            "0,91; 1,19 ja 1,50 g, sekä pisteisiin sovitettu origon kautta kulkeva suora, joka kulkee pisteen (5,0 A; "
            "1,50 g) kautta. Ruudukon väli on 0,5 A ja 0,15 g.")
    ax = Axes(f, (96, 290), (470, 56), x=(0, 6), y=(0, 1.8), xticks=[0.5 * k for k in range(1, 13)],
              yticks=[0.15 * k for k in range(1, 13)], xlabel=r"I\ (\text{A})", ylabel=r"\Delta m\ (\text{g})",
              xfmt=lambda v: fi(v) if abs(v - round(v)) < 1e-9 else "",
              yfmt=lambda v: fi(round(v, 2), 1) if round(v / 0.15) % 2 == 0 else "")
    ax.line([(0, 0), (6, 1.8)], HOT, 3)
    for I, dm in ((1, 0.30), (2, 0.60), (3, 0.91), (4, 1.19), (5, 1.50)):
        ax.point(I, dm, CURRENT)
    return f.svg()


def hero():
    """The opening illustration: a loudspeaker playing on a desk, its cone in motion, and a desk fan spinning beside it."""
    f = H.hero("fy74-hero", "Kuvitus: työpöydällä on puinen kaiutin, jonka kartiosta lähtee ääniaaltoja, ja sen vieressä "
               "pöytätuuletin, jonka siivet pyörivät. Kumpaakaan ei kosketa, mutta kartio värähtelee ja siivet pyörivät, "
               "kun laitteisiin kytketään sähkövirta.")
    f.rect(0, 0, 1200, 600, PAPER)
    f.rect(0, 430, 1200, 170, H.grad(f, "fy74h-desk", SAND_LIGHT, SAND))
    f.line(0, 430, 1200, 430, GRAIN, 3)
    # wall: a window with a light sky
    f.rect(120, 60, 220, 260, H.grad(f, "fy74h-sky", H.ICE, GLASS), INK, 3, 6)
    f.line(230, 60, 230, 320, INK, 3); f.line(120, 190, 340, 190, INK, 3)
    # cable from the speaker and the fan to a socket strip
    f.path("M520,420 C520,470 600,480 700,486", stroke=INK, w=4)
    f.path("M840,424 C840,476 760,480 700,486", stroke=INK, w=4)
    f.rect(660, 476, 110, 26, WHITE, INK, 3, 6)
    # loudspeaker box
    f.rect(400, 150, 240, 280, H.grad(f, "fy74h-wood", "#b8622d", "#8a5f22"), INK, 3, 10)
    f.circle(520, 330, 78, IRON, INK, 3)
    f.circle(520, 330, 64, ALUMINIUM, INK, 2)
    f.circle(520, 330, 40, METAL_EDGE, INK, 2)
    f.circle(520, 330, 18, IRON, INK, 2)
    f.circle(520, 205, 34, IRON, INK, 3)
    f.circle(520, 205, 20, ALUMINIUM, INK, 2)
    # sound waves leaving the cone
    for k, r in enumerate((150, 180, 210)):
        c, s_ = math.cos(math.radians(30)), math.sin(math.radians(30))
        op = f'stroke-linecap="round" stroke-opacity="{0.8 - 0.2 * k:.1f}"'
        f.path(f"M{n(520 - r * c)},{n(310 - r * s_)} A{r},{r} 0 0 0 {n(520 - r * c)},{n(310 + r * s_)}", stroke=MUTED, w=4, extra=op)
        f.path(f"M{n(520 + r * c)},{n(310 - r * s_)} A{r},{r} 0 0 1 {n(520 + r * c)},{n(310 + r * s_)}", stroke=MUTED, w=4, extra=op)
    # desk fan: base, stand, motor housing, guard and blurred blades
    f.path("M770,430 Q840,400 910,430 Z", IRON, INK, 3)
    f.rect(830, 300, 20, 120, ALUMINIUM, INK, 3, 4)
    f.circle(840, 250, 118, GLASS, INK, 3)
    for k in range(3):
        a = math.radians(90 + 120 * k)
        f.path(f"M840,250 Q{n(840 + 120 * math.cos(a - 0.5))},{n(250 - 120 * math.sin(a - 0.5))} {n(840 + 100 * math.cos(a + 0.3))},{n(250 - 100 * math.sin(a + 0.3))} Z",
               H.COLD, extra='fill-opacity="0.75"')
    for r in (60, 90):
        f.circle(840, 250, r, "none", METAL_EDGE, 2)
    f.circle(840, 250, 22, IRON, INK, 3)
    # motion lines round the blades
    for a0 in (20, 140, 260):
        a, b = math.radians(a0), math.radians(a0 + 50)
        f.path(f"M{n(840 + 134 * math.cos(a))},{n(250 - 134 * math.sin(a))} A134,134 0 0 0 {n(840 + 134 * math.cos(b))},{n(250 - 134 * math.sin(b))}", stroke=MUTED, w=4,
               extra='stroke-linecap="round"')
    return f.svg()


def scene():
    """A second everyday scene: headphones on a desk beside a phone playing music."""
    f = H.scene("fy74-scene", "Kuvitus: kuulokkeet ja älypuhelin pöydällä. Kuulokkeiden kummassakin kuvussa on pieni "
                "kaiutin, ja kuvuista lähtee ääniaaltoja.")
    f.rect(0, 0, 600, 360, PAPER)
    f.rect(0, 270, 600, 90, H.grad(f, "fy74s-desk", SAND_LIGHT, SAND))
    # headphones: band and two cups
    f.path("M180,230 C180,60 420,60 420,230", stroke=INK, w=14, extra='stroke-linecap="round"')
    f.path("M180,230 C180,60 420,60 420,230", stroke=IRON, w=8, extra='stroke-linecap="round"')
    for x in (180, 420):
        f.rect(x - 34, 196, 68, 96, IRON, INK, 3, 26)
        f.rect(x - 22, 210, 44, 68, METAL_EDGE, INK, 2, 18)
    for k, r in enumerate((60, 84)):
        f.path(f"M{n(180 - r * 0.7)},{n(244 - r * 0.7)} A{r},{r} 0 0 0 {n(180 - r * 0.7)},{n(244 + r * 0.7)}", stroke=MUTED, w=3,
               extra=f'stroke-linecap="round" stroke-opacity="{0.8 - 0.3 * k:.1f}"')
        f.path(f"M{n(420 + r * 0.7)},{n(244 - r * 0.7)} A{r},{r} 0 0 1 {n(420 + r * 0.7)},{n(244 + r * 0.7)}", stroke=MUTED, w=3,
               extra=f'stroke-linecap="round" stroke-opacity="{0.8 - 0.3 * k:.1f}"')
    # phone
    f.rect(270, 236, 70, 108, INK, rx=10)
    f.rect(276, 246, 58, 86, H.grad(f, "fy74s-screen", H.ICE, H.COLD), rx=4)
    f.path("M296,270 v34 a8,8 0 1 1 -4,-7 v-27 l22,-6 v28 a8,8 0 1 1 -4,-7 v-18 Z", WHITE)
    return f.svg()


FIGURES = {"hero": hero, "swing": swing, "angle": angle, "wires": wires, "motor": motor, "speaker": speaker,
           "scene": scene, "balance-points": balance_points}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "swing": "reveals: the force on a wire is perpendicular to both the current and the field (direction drawn)",
    "angle": "reveals: only the component B sin α perpendicular to the wire matters; force into the page",
    "wires": "reveals: parallel currents attract, opposite currents repel",
    "motor": "reveals: the forces on the loop's sides and the sense of rotation",
    "speaker": "reveals: the force on the voice coil points along the axis",
    "balance-points": "safe: current balance readings Δm against I with a fitted line through the origin, no B or slope",
}
