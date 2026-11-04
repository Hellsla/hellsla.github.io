"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy6-15` writes them into lesson.md.
Colours, one meaning each, as in the other FY6 chapters: the conventional current and a fault current are violet
filled arrows (#7048e8); the insulation of the conductors has the Finnish colours: phase brown (#8a5f22), neutral blue
(#1971c2), protective earth striped green and pale yellow (#2b8a3e / #f1dfb5); metal is aluminium grey, the soil sand,
danger and a spark red and orange. Circuit diagrams use the IEC symbols (a source with ~ in a circle, a fuse as a
rectangle with a line through it, a resistor as a rectangle) with ink wires 3 px. Every label is LaTeX.
The numbers are those of lesson-answers.py and answers.py."""
import math
from figlib import (Fig, Axes, fi, n, INK, MUTED, WHITE, RULE, RULE_LIGHT, GLASS, SAND_LIGHT, SAND, SAND_DARK, GRAIN,
                    HEAT_LIGHT, HEAT, HOT, HOT_LIGHT, COLD, COLD_LIGHT, ALUMINIUM, METAL_EDGE, IRON, COPPER, ICE, GOOD,
                    GOOD_LIGHT, PAPER)
import herolib as H
from herolib import grad

CURRENT = "#7048e8"     # conventional current and fault currents (FY6)
PHASE = "#8a5f22"       # brown insulation of the phase conductor L
NEUTRAL = COLD          # blue insulation of the neutral conductor N
W = 3                   # wire width in diagrams


# --- circuit-diagram symbols (IEC) ---------------------------------------------------------------------------------
def wire(f, pts, w=W, color=INK):
    p = " ".join(f"{n(x)},{n(y)}" for x, y in pts)
    f.add(f'<polyline points="{p}" fill="none" stroke="{color}" stroke-width="{w}" stroke-linejoin="miter" stroke-linecap="square"/>')


def ac_source(f, cx, cy, r=26):
    """An AC source: a circle with a sine wave in it."""
    f.circle(cx, cy, r, WHITE, INK, W)
    d = f"M{n(cx - 14)},{n(cy)} C{n(cx - 9)},{n(cy - 14)} {n(cx - 3)},{n(cy - 14)} {n(cx)},{n(cy)} S{n(cx + 9)},{n(cy + 14)} {n(cx + 14)},{n(cy)}"
    f.path(d, "none", INK, 2.5)


def fuse(f, cx, cy, vertical=False):
    """A fuse: a rectangle with the conductor drawn through its length."""
    w, h = (20, 50) if vertical else (50, 20)
    f.rect(cx - w / 2, cy - h / 2, w, h, WHITE, INK, W)
    if vertical: f.line(cx, cy - h / 2, cx, cy + h / 2, INK, 2)
    else: f.line(cx - w / 2, cy, cx + w / 2, cy, INK, 2)


def resistor(f, cx, cy, vertical=True):
    w, h = (20, 50) if vertical else (50, 20)
    f.rect(cx - w / 2, cy - h / 2, w, h, WHITE, INK, W)


def lamp(f, cx, cy, r=20):
    f.circle(cx, cy, r, WHITE, INK, W)
    d = r * 0.7071
    f.line(cx - d, cy - d, cx + d, cy + d, INK, 2.5)
    f.line(cx - d, cy + d, cx + d, cy - d, INK, 2.5)


def node(f, x, y): f.circle(x, y, 5.5, INK)


def ground(f, x, y, sc=1.0):
    """The earth symbol: a stem from (x, y) down and three shortening bars."""
    f.line(x, y, x, y + 14 * sc, INK, W)
    for k, half in enumerate((18, 11, 4)):
        yy = y + (14 + 7 * k) * sc
        f.line(x - half * sc, yy, x + half * sc, yy, INK, 3)


def i_arrow(f, x1, y1, x2, y2, label=None, lx=None, ly=None, anchor="middle"):
    f.arrow(x1, y1, x2, y2, CURRENT, 3, 15)
    if label: f.tex(lx, ly, label, anchor, CURRENT)


def spark(f, cx, cy, r=13):
    """A small eight-point spark: the place of a fault."""
    pts = []
    for k in range(16):
        a = k * math.pi / 8
        rr = r if k % 2 == 0 else r * 0.45
        pts.append((cx + rr * math.cos(a), cy + rr * math.sin(a)))
    f.path("M" + " L".join(f"{n(x)},{n(y)}" for x, y in pts) + " Z", HEAT_LIGHT, HEAT, 2)


def earth_stripes(f):
    """The protective-earth insulation pattern: green and pale yellow stripes (defined once per figure)."""
    pid = f"{f.fid}-pe"
    f.defs_add(f'<pattern id="{pid}" patternUnits="userSpaceOnUse" width="14" height="14" patternTransform="rotate(45)">'
               f'<rect width="14" height="14" fill="{SAND_LIGHT}"/><rect width="7" height="14" fill="{GOOD}"/></pattern>')
    return f"url(#{pid})"


def cable(f, pts, colour, w=10):
    """An insulated conductor: an ink outline and the insulation colour (a fill or a pattern)."""
    p = " ".join(f"{n(x)},{n(y)}" for x, y in pts)
    f.add(f'<polyline points="{p}" fill="none" stroke="{INK}" stroke-width="{w + 4}" stroke-linejoin="round" stroke-linecap="round"/>')
    f.add(f'<polyline points="{p}" fill="none" stroke="{colour}" stroke-width="{w}" stroke-linejoin="round" stroke-linecap="round"/>')


# --- Ydinajatus 1: a group with its fuse and three loads in parallel ------------------------------------------------
def ryhma():
    f = Fig("fy615-ryhma", 340, "Kytkentäkaavio, ei mittakaavassa: kodin yksi sähköryhmä. Vasemmalla vaihtojännitelähde 230 V. "
            "Ylempi johdin kulkee lähteestä sulakkeen kautta oikealle, ja siihen on kytketty rinnan kolme laitetta: kaksi "
            "vastusta, joiden tehot ovat P1 ja P2, ja lamppu, jonka teho on P3. Laitteiden alapäät on yhdistetty alempaan "
            "johtimeen, joka palaa lähteeseen. Violetit nuolet: sulakkeen läpi kulkee koko virta I, ja se jakautuu laitteiden "
            "virroiksi I1, I2 ja I3. Alla yhtälö I = I1 + I2 + I3.")
    T, B = 92, 262
    xs = (300, 410, 520)
    wire(f, [(70, 152), (70, T), (xs[2], T), (xs[2], 155)])
    wire(f, [(70, 204), (70, B), (xs[2], B), (xs[2], 195)])
    for x in xs[:2]:
        wire(f, [(x, T), (x, B)])
        node(f, x, T); node(f, x, B)
    ac_source(f, 70, 178)
    f.tex(70, 36, r"230\,\text{V}", "middle", w=90)
    fuse(f, 170, T)
    f.tex(170, 56, r"\text{sulake}", "middle", w=100)
    i_arrow(f, 220, 72, 262, 72, "I", 240, 46)
    resistor(f, xs[0], 177); resistor(f, xs[1], 177); lamp(f, xs[2], 175)
    for k, x in enumerate(xs):
        f.tex(x - 22, 177, f"P_{k + 1}", "end", w=42)
        i_arrow(f, x + 20, 112, x + 20, 150, f"I_{k + 1}", x + 30, 131, "start")
    f.line(30, 288, 570, 288, RULE, 1.5, "6 5")
    f.tex(300, 316, r"I = I_1 + I_2 + I_3", "middle", w=220)
    return f.svg()


# --- Ydinajatus 2: the socket, the plug and the three conductors of the cable --------------------------------------
def pistorasia():
    f = Fig("fy615-pistorasia", 330, "Kaavakuva, ei mittakaavassa, kaksi osaa. Vasemmalla maadoitettu pistorasia edestä: "
            "pyöreässä syvennyksessä on kaksi reikää vaihe- ja nollajohtimelle sekä ylä- ja alareunassa metalliset "
            "suojamaadoituskoskettimet, merkitty PE. Oikealla sähköjohto, jonka kuoresta tulee kolme eristettyä johdinta: "
            "ruskea vaihejohdin L, sininen nollajohdin N ja keltavihreä suojamaadoitusjohdin PE.")
    pe = earth_stripes(f)
    # the socket
    f.tex(136, 26, r"\text{pistorasia}", "middle", w=140)
    f.rect(28, 58, 216, 216, grad(f, "fy615-plate", WHITE, RULE_LIGHT), INK, 3, rx=22)
    f.circle(136, 166, 78, GLASS, INK, 3)
    f.add(f'<circle cx="136" cy="166" r="66" fill="none" stroke="{RULE}" stroke-width="2"/>')
    for x in (102, 170): f.circle(x, 166, 10, INK)
    for y in (96, 236):
        f.rect(116, y - 7, 40, 14, grad(f, f"fy615-clip{y}", WHITE, METAL_EDGE), INK, 2, rx=3)
    f.tex(178, 80, r"\text{PE}", "start", w=44)
    f.tex(178, 252, r"\text{PE}", "start", w=44)
    f.line(270, 40, 270, 300, RULE, 1.5, "6 5")
    # the cable
    f.tex(430, 26, r"\text{johto}", "middle", w=90)
    ys = (100, 166, 232)
    for y, col in zip(ys, (PHASE, NEUTRAL, pe)):
        cable(f, [(312, 166 + (y - 166) * 0.2), (342, 166 + (y - 166) * 0.45), (374, y), (392, y)], col)
        f.rect(392, y - 4, 16, 8, COPPER, INK, 1.5, rx=2)
    f.rect(286, 140, 44, 52, grad(f, "fy615-sheath", WHITE, RULE), INK, 3, rx=10)
    for y, lab in zip(ys, (r"\text{vaihe}\ \text{L}", r"\text{nolla}\ \text{N}", r"\text{maadoitus}\ \text{PE}")):
        f.tex(418, y, lab, "start", w=168)
    return f.svg()


# --- Ydinajatus 3: a fault to the casing without and with the protective earth -------------------------------------
def _fault_panel(f, x0, earthed):
    """One panel: a person touching the metal casing of a device whose phase conductor touches the casing."""
    pe = earth_stripes(f) if earthed else None
    gy = 316
    bx0, bx1, by0, by1 = x0 + 126, x0 + 254, 150, gy
    # soil
    f.rect(x0 + 14, gy, 272, 28, grad(f, f"fy615-soil{x0}", SAND, SAND_DARK), None, 0)
    f.line(x0 + 14, gy, x0 + 286, gy, INK, 2.5)
    # the device: a metal casing in cut-away, a heater inside
    f.rect(bx0, by0, bx1 - bx0, by1 - by0 - 6, GLASS, ALUMINIUM, 9, rx=8)
    f.rect(bx0 - 4.5, by0 - 4.5, bx1 - bx0 + 9, by1 - by0 + 3, "none", INK, 2, rx=11)
    # the phase (brown) and neutral (blue) conductors enter from above and feed the heater; the worn phase conductor
    # touches the casing at the fault
    cable(f, [(bx0 + 22, 48), (bx0 + 22, 284), (bx0 + 100, 284), (bx0 + 100, 262)], PHASE, 7)
    cable(f, [(bx0 + 46, 48), (bx0 + 46, 176), (bx0 + 100, 176), (bx0 + 100, 200)], NEUTRAL, 7)
    f.rect(bx0 + 91, 198, 18, 66, HEAT_LIGHT, INK, 2, rx=3)
    cable(f, [(bx0 + 22, 232), (bx0 + 6, 232)], PHASE, 7)
    spark(f, bx0 + 2, 232)
    f.tex(bx0 + 36, 226, r"\text{vika}", "start", w=60)
    if earthed:
        cable(f, [(bx0 + 80, 48), (bx0 + 80, by0 - 2)], pe, 7)
        i_arrow(f, bx0 + 96, by0 - 10, bx0 + 96, 74, r"I_\text{v}", bx0 + 100, 110, "start")
    # the person touching the casing
    H.walker(f, x0 + 62, gy, COLD, INK, 0.4, hand=(bx0 - 6, 240))
    if not earthed:
        path = [(bx0 - 12, 232), (x0 + 70, 200), (x0 + 62, 256), (x0 + 48, 306)]
        f.add('<polyline points="' + " ".join(f"{n(x)},{n(y)}" for x, y in path[:-1]) + f'" fill="none" stroke="{CURRENT}" '
              f'stroke-width="4" stroke-linejoin="round" stroke-dasharray="9 6"/>')
        f.arrow(path[-2][0], path[-2][1], path[-1][0], path[-1][1] + 18, CURRENT, 4, 16)
        f.tex(x0 + 26, 248, "I", "middle", CURRENT, w=26)


def maadoitus():
    f = Fig("fy615-maadoitus", 380, "Kaavakuva, ei mittakaavassa, kaksi paneelia. Kummassakin on laite, jonka metallirunko on "
            "piirretty auki: ruskea vaihejohdin tulee ylhäältä laitteen vastukselle, mutta sen kulunut kohta koskettaa runkoa, "
            "mikä on merkitty kipinällä ja sanalla vika. Ihminen seisoo maassa ja koskettaa kädellään laitteen runkoa. "
            "Vasemmalla, ilman maadoitusta, violetti katkoviiva ja nuoli näyttävät virran I kulkevan rungosta ihmisen käden ja "
            "kehon kautta jalkoihin ja maahan. Oikealla runkoon on kytketty keltavihreä suojamaadoitusjohdin, ja violetti "
            "nuoli näyttää vikavirran kulkevan sitä pitkin; teksti: sulake laukeaa. Ihmisen kautta kulkee vain pieni virta, kunnes sulake katkaisee virran.")
    f.tex(150, 24, r"\text{ei maadoitusta}", "middle", w=200)
    f.tex(450, 24, r"\text{suojamaadoitettu}", "middle", w=220)
    _fault_panel(f, 0, False)
    f.line(300, 14, 300, 366, RULE, 1.5, "6 5")
    _fault_panel(f, 300, True)
    f.tex(150, 362, r"\text{virta ihmisen kautta}", "middle", w=260)
    f.tex(450, 362, r"\text{sulake laukeaa}", "middle", w=200)
    return f.svg()


# --- Ydinajatus 4: the symbols of the protection classes -----------------------------------------------------------
def sym_class1(f, cx, cy, s=1.0):
    f.circle(cx, cy, 44 * s, WHITE, INK, 4 * s)
    f.line(cx, cy - 28 * s, cx, cy + 2 * s, INK, 4 * s)
    for k, half in enumerate((22, 14, 6)):
        yy = cy + (2 + 11 * k) * s
        f.line(cx - half * s, yy, cx + half * s, yy, INK, 4 * s)


def sym_class2(f, cx, cy, s=1.0):
    for a in (44, 24):
        f.rect(cx - a * s, cy - a * s, 2 * a * s, 2 * a * s, WHITE if a == 44 else "none", INK, 4 * s)


def sym_class3(f, cx, cy, s=1.0):
    r = 50 * s
    f.path(f"M{n(cx)},{n(cy - r)} L{n(cx + r)},{n(cy)} L{n(cx)},{n(cy + r)} L{n(cx - r)},{n(cy)} Z", WHITE, INK, 4 * s)
    for dx in (-10, 0, 10):
        f.line(cx + dx * s, cy - 15 * s, cx + dx * s, cy + 15 * s, INK, 4 * s)
    for dy in (-15, 15):
        f.line(cx - 17 * s, cy + dy * s, cx + 17 * s, cy + dy * s, INK, 3 * s)


def luokat():
    f = Fig("fy615-luokat", 300, "Suojausluokkien merkit kolmessa sarakkeessa. Vasemmalla luokka I: maadoitusmerkki, eli pystyviiva "
            "ja kolme lyhenevää vaakaviivaa, ympyrän sisällä; suojamaadoitus, esimerkiksi pesukone. Keskellä luokka II: kaksi "
            "sisäkkäistä neliötä; kaksoiseristys, esimerkiksi hiustenkuivaaja. Oikealla luokka III: vinoneliö, jonka sisällä "
            "on roomalainen numero kolme; suojajännite, esimerkiksi akkuporakone.")
    xs = (100, 300, 500)
    sym_class1(f, xs[0], 96); sym_class2(f, xs[1], 96); sym_class3(f, xs[2], 96)
    rows = [(r"\text{luokka I}", r"\text{maadoitus}", r"\text{pesukone}"),
            (r"\text{luokka II}", r"\text{kaksoiseristys}", r"\text{hiustenkuivaaja}"),
            (r"\text{luokka III}", r"\text{suojajännite}", r"\text{akkuporakone}")]
    for x, (a, b, c) in zip(xs, rows):
        f.tex(x, 180, a, "middle", w=140)
        f.tex(x, 216, b, "middle", w=190)
        f.tex(x, 256, c, "middle", MUTED, w=190)
    return f.svg()


def merkki(k):
    labels = {1: "Merkki: ympyrä, jonka sisällä on pystyviiva ja sen alapäässä kolme lyhenevää vaakaviivaa.",
              2: "Merkki: kaksi sisäkkäistä neliötä.",
              3: "Merkki: vinoneliö, jonka sisällä on roomalainen numero kolme."}
    f = Fig(f"fy615-merkki{k}", 200, labels[k], width=300)
    {1: sym_class1, 2: sym_class2, 3: sym_class3}[k](f, 150, 100, 1.5)
    return f.svg()


# --- Ydinajatus 5: the residual current device compares the outgoing and the returning current ---------------------
def vikavirtasuoja():
    f = Fig("fy615-vvs", 360, "Kytkentäkaavio, ei mittakaavassa. Vasemmalla vaihtojännitelähde 230 V. Ylempi johdin on vaihejohdin "
            "L ja alempi nollajohdin N. Molemmat kulkevat katkoviivalla rajatun vikavirtasuojan läpi, jossa ne kulkevat saman "
            "rautarenkaan läpi. Vaihejohtimessa on sen jälkeen sulake. Oikealla laite, jonka metallirungon sisällä on vastus "
            "vaihe- ja nollajohtimen välissä; vaihejohtimen ja rungon välissä on vika, merkitty kipinällä. Rungosta kulkee "
            "virtatie ihmisen resistanssin R keho kautta maahan. Violetit nuolet: vaihejohtimessa virta I L laitteeseen, "
            "nollajohtimessa virta I N takaisin ja ihmisen kautta maahan vikavirta I v. Ylhäällä oikealla yhtälö "
            "I L miinus I N on I v.")
    L, N = 110, 270
    wire(f, [(60, 152), (60, L), (450, L), (450, 163)])
    wire(f, [(60, 204), (60, N), (450, N), (450, 213)])
    ac_source(f, 60, 178)
    f.tex(16, 40, r"230\,\text{V}", "start", w=90)
    f.tex(84, L - 18, r"\text{L}", "middle", w=26)
    f.tex(84, N + 18, r"\text{N}", "middle", w=26)
    # the RCD: a dashed box with a toroidal core around both conductors
    f.rect(105, 80, 100, 220, "none", INK, 2, rx=10, extra='stroke-dasharray="7 5"')
    f.add(f'<ellipse cx="155" cy="190" rx="16" ry="96" fill="none" stroke="{IRON}" stroke-width="8"/>')
    f.line(147, L, 163, L, INK, W); f.line(147, N, 163, N, INK, W)
    f.tex(155, 326, r"\text{vikavirtasuoja}", "middle", w=200)
    fuse(f, 257, L)
    f.tex(257, 80, r"\text{sulake}", "middle", w=96)
    i_arrow(f, 305, 92, 355, 92, r"I_\text{L}", 330, 64)
    i_arrow(f, 355, 290, 305, 290, r"I_\text{N}", 330, 316)
    # the device: a metal casing, the heater inside, a fault to the casing
    f.rect(360, 138, 120, 104, "none", ALUMINIUM, 6, rx=8)
    resistor(f, 450, 188)
    f.tex(400, 190, r"\text{laite}", "middle", w=70)
    f.line(450, 150, 474, 150, INK, 2)
    spark(f, 476, 150, 11)
    # the path through a person to earth
    wire(f, [(483, 210), (540, 210), (540, 244)])
    resistor(f, 540, 270)
    wire(f, [(540, 295), (540, 306)])
    ground(f, 540, 306)
    f.tex(524, 272, r"R_\text{keho}", "end", w=76)
    i_arrow(f, 492, 192, 530, 192, r"I_\text{v}", 552, 182, "start")
    f.tex(590, 32, r"I_\text{L} - I_\text{N} = I_\text{v}", "end", w=170)
    return f.svg()


# --- Ydinajatus 6: a fallen conductor and the step voltage -----------------------------------------------------------
def askel():
    f = Fig("fy615-askel", 340, "Kaavakuva, ei mittakaavassa: maahan pudonnut sähköjohto ja askeljännite. Vasemmalla puupylväs, "
            "jonka katkennut johdin on pudonnut maahan; putoamiskohdassa on kipinä. Maan sisällä putoamiskohdan ympärillä on "
            "sisäkkäisiä katkoviivakaaria, joilla potentiaali on sama; väri vaalenee punertavasta hiekanväriseksi kauemmas "
            "mentäessä, ja nuoli kertoo, että potentiaali pienenee. Keskellä ihminen ottaa pitkän askeleen: hänen jalkansa "
            "ovat eri kaarilla, ja jalkojen välillä on askeljännite U askel. Oikealla ihminen seisoo jalat yhdessä, ja hänen "
            "jalkojensa välinen jännite on lähes nolla.")
    gy, cx = 196, 132
    # soil with potential bands that fade with distance
    f.defs_add('<clipPath id="fy615-soilclip"><rect x="14" y="196" width="572" height="134"/></clipPath>')
    f.rect(14, gy, 572, 134, grad(f, "fy615-soil", SAND_LIGHT, SAND))
    bands = [(330, SAND_LIGHT, 0.0), (250, HOT_LIGHT, 0.18), (175, HOT_LIGHT, 0.35), (110, HOT_LIGHT, 0.55), (55, HOT_LIGHT, 0.8)]
    for r, col, op in bands:
        if op: f.add(f'<circle cx="{cx}" cy="{gy}" r="{r}" fill="{col}" fill-opacity="{op}" clip-path="url(#fy615-soilclip)"/>')
    for r in (55, 110, 175, 250, 330):
        f.add(f'<circle cx="{cx}" cy="{gy}" r="{r}" fill="none" stroke="{MUTED}" stroke-width="1.5" stroke-dasharray="6 5" clip-path="url(#fy615-soilclip)"/>')
    f.line(14, gy, 586, gy, INK, 2.5)
    # the pole and the fallen conductor
    f.rect(30, 34, 16, gy - 34, grad(f, "fy615-pole", SAND_DARK, GRAIN, horizontal=True), INK, 2)
    f.rect(18, 46, 48, 8, IRON, INK, 1.5, rx=2)
    f.path(f"M60,50 Q100,70 112,130 Q118,170 {cx},{gy - 2}", "none", INK, 3)
    spark(f, cx, gy - 4, 15)
    # the person with a long stride: feet on different arcs
    H.walker(f, 300, gy, COLD, INK, 0.36, stride=1.7)
    f.line(270, gy + 14, 270, gy + 26, INK, 2); f.line(331, gy + 14, 331, gy + 26, INK, 2)
    f.line(270, gy + 20, 331, gy + 20, INK, 2)
    f.tex(300, gy + 46, r"U_\text{askel}", "middle", w=90, bg=True)
    # the person with feet together
    H.person(f, 490, gy, HOT, INK, 0.5)
    f.tex(490, gy + 46, r"U \approx 0", "middle", w=90, bg=True)
    f.arrow(200, 304, 560, 304, INK, 2.5, 14)
    f.tex(380, 282, r"\text{potentiaali pienenee}", "middle", w=250, bg=True)
    return f.svg()


# --- Kaava: the effects of a 50 Hz current through the body on a logarithmic scale -----------------------------------
def vaikutukset():
    f = Fig("fy615-vaikutukset", 360, "Asteikko, ei lineaarinen: kehon läpi kulkevan 50 hertsin vaihtovirran I suuruus "
            "milliampeereina logaritmisella pystyakselilla 0,1 mA:sta 1000 mA:iin, jokainen kymmenkertaistus yhtä pitkä väli. "
            "Akselin vieressä väripalkki: alle 0,5 mA vihreä, 0,5–10 mA vaaleanoranssi, 10–50 mA oranssi ja yli 50 mA punainen. "
            "Merkinnät: 0,5 mA virta tuntuu, 10 mA ote ei irtoa, 30 mA hengitys vaikeutuu, 50 mA kammiovärinän "
            "vaara. Suuntaa antavat arvot.")
    y0, per = 330, 66.0                    # y of 0,1 mA and the length of one decade

    def Y(mA): return y0 - per * (math.log10(mA) + 1)
    xb = 140
    f.line(xb, Y(0.1) + 4, xb, Y(1000) - 22, INK, 2.5)
    f.path(f"M{xb},{n(Y(1000) - 34)} L{xb - 7},{n(Y(1000) - 18)} L{xb + 7},{n(Y(1000) - 18)} Z", INK)
    f.tex(xb, 18, r"I\ (\text{mA})", "middle", w=90)
    for v, lab in ((0.1, "0{,}1"), (1, "1"), (10, "10"), (100, "100"), (1000, "1000")):
        f.line(xb - 6, Y(v), xb, Y(v), INK, 2)
        f.tex(xb - 12, Y(v), lab, "end", MUTED, w=70)
    zones = [(0.1, 0.5, GOOD_LIGHT), (0.5, 10, HEAT_LIGHT), (10, 50, HEAT), (50, 1000, HOT)]
    for a, b, col in zones:
        f.rect(xb + 6, Y(b), 26, Y(a) - Y(b), col, INK, 1.5)
    marks = [(0.5, Y(0.5), r"0{,}5\,\text{mA}\ \ \text{virta tuntuu}"),
             (10, Y(10) + 14, r"10\,\text{mA}\ \ \text{ote ei irtoa}"),
             (30, Y(30) + 6, r"30\,\text{mA}\ \ \text{hengitys vaikeutuu}"),
             (50, Y(50) - 26, r"50\,\text{mA}\ \ \text{kammiovärinän vaara}")]
    for v, ly, lab in marks:
        f.line(xb + 32, Y(v), xb + 50, Y(v), INK, 2)
        f.line(xb + 50, Y(v), xb + 62, ly, INK, 2)
        f.tex(xb + 70, ly, lab, "start", w=370)
    return f.svg()


# --- task figure: the potential of the ground around a fallen conductor (a model) ----------------------------------
def ex_askel():
    f = Fig("fy615-ex-askel", 360, "Kuvaaja mittakaavassa, laskettu malli: maan potentiaali V voltteina etäisyyden r funktiona "
            "metreinä maahan pudonneen johtimen kosketuskohdasta, kun maaperä on tasalaatuista. Ruudukon välit ovat 1 m ja "
            "200 V. Käyrä laskee jyrkästi lähellä kosketuskohtaa ja loivenee kauempana; se kulkee ruudukon risteyskohtien "
            "(1 m; 1200 V), (2 m; 600 V), (3 m; 400 V) ja (6 m; 200 V) sekä pisteen (4 m; 300 V) kautta.")
    ax = Axes(f, (96, 310), (480, 64), x=(0, 8), y=(0, 1300), xticks=list(range(1, 9)), yticks=[200 * k for k in range(1, 7)],
              xlabel=r"r\ (\text{m})", ylabel=r"V\ (\text{V})",
              yfmt=lambda v: fi(v))
    ax.curve(lambda r: 1200 / r, 1.0, 8.0, INK, 3)
    return f.svg()


# --- the opening illustration: a kitchen in the evening, the group panel with one breaker tripped -------------------
def hero():
    f = H.hero("fy615-hero", "Kuvitus: keittiö iltaisin. Työtasolla ovat vedenkeitin, josta nousee höyryä, kahvinkeitin, "
               "leivänpaahdin ja mikroaaltouuni, kaikki kytkettyinä seinän pistorasioihin. Vasemmalla seinällä on avattu "
               "sähkökeskus, jossa on rivi johdonsuojakatkaisijoita; yksi niistä on lauennut alas. Ikkunasta näkyy iltataivas "
               "ja kaukana voimajohtopylväitä.")
    f.rect(0, 0, 1200, 600, PAPER)
    H.tiles(f, 600, 60, RULE_LIGHT, WHITE)
    f.rect(0, 0, 1200, 600, PAPER, extra='fill-opacity="0.55"')
    # window with the evening sky and power lines
    wx, wy, ww, wh = 860, 70, 260, 210
    f.rect(wx, wy, ww, wh, grad(f, "fy615h-sky", COLD, HEAT_LIGHT, y1=wy, y2=wy + wh), INK, 4, 4)
    f.path(f"M{wx},{wy + 170} Q{wx + 90},{wy + 150} {wx + 160},{wy + 166} T{wx + ww},{wy + 160} V{wy + wh} H{wx} Z", GOOD)
    arms1 = H.pylon(f, wx + 70, wy + 168, 92, 0.7)
    arms2 = H.pylon(f, wx + 200, wy + 164, 84, 0.65)
    for a, b in zip(arms1, arms2): H.wire(f, a, b, 10, INK, 1.5)
    f.line(wx + ww / 2, wy, wx + ww / 2, wy + wh, INK, 4)
    f.rect(wx - 14, wy + wh, ww + 28, 16, RULE, INK, 3, 3)
    # the group panel on the left wall, door open, one breaker down
    px, py, pw, ph = 70, 90, 230, 280
    f.rect(px, py, pw, ph, grad(f, "fy615h-panel", WHITE, ALUMINIUM), INK, 4, 8)
    f.path(f"M{px},{py} L{px - 50},{py + 26} L{px - 50},{py + ph - 26} L{px},{py + ph} Z", grad(f, "fy615h-door", ALUMINIUM, METAL_EDGE), INK, 3)
    for row, yy in enumerate((140, 230, 320)):
        f.rect(px + 20, yy - 30, pw - 40, 60, IRON, INK, 2, 4)
        for k in range(6):
            bx = px + 30 + k * 30
            f.rect(bx, yy - 24, 24, 48, WHITE, INK, 2, 3)
            tripped = row == 1 and k == 3
            f.rect(bx + 6, yy + (2 if tripped else -18), 12, 16, HOT if tripped else IRON, INK, 1.5, 2)
    # worktop and cupboards
    f.rect(0, 430, 1200, 22, grad(f, "fy615h-top", SAND, SAND_DARK), INK, 3)
    f.rect(0, 452, 1200, 148, grad(f, "fy615h-cab", WHITE, RULE_LIGHT), INK, 3)
    for x in range(200, 1200, 200):
        f.line(x, 452, x, 600, INK, 3)
        f.rect(x - 34, 476, 8, 40, METAL_EDGE, rx=3)
    # sockets on the wall above the worktop and the cords behind the appliances
    kx, cxm, tx, mx0 = 420, 560, 700, 790
    for sx in (kx, cxm, tx, mx0 + 95):
        f.path(f"M{sx},400 V{258}", "none", INK, 4)
        f.rect(sx - 26, 206, 52, 52, WHITE, INK, 3, rx=8)
        f.circle(sx, 232, 17, GLASS, INK, 2)
        f.circle(sx - 7, 232, 3, INK); f.circle(sx + 7, 232, 3, INK)
    # kettle with steam
    f.path(f"M{kx - 50},430 L{kx - 42},352 Q{kx},336 {kx + 42},352 L{kx + 50},430 Z", H.steel(f, "fy615h-kettle"), INK, 3)
    f.rect(kx - 56, 424, 112, 10, INK, rx=3)
    f.path(f"M{kx + 42},360 Q{kx + 84},372 {kx + 50},420", "none", INK, 9, 'stroke-linecap="round"')
    f.path(f"M{kx - 42},372 L{kx - 74},350 L{kx - 46},398 Z", H.steel(f, "fy615h-spout"), INK, 2.5)
    f.circle(kx + 30, 414, 5, HOT)
    for k in range(2):
        d = f"M{kx - 76 + k * 14},344 c-12,-18 12,-32 0,-50 s12,-32 0,-50"
        f.path(d, "none", RULE, 15, 'stroke-linecap="round" stroke-opacity="0.5"'); f.path(d, "none", WHITE, 9, 'stroke-linecap="round"')
    # coffee maker
    f.rect(cxm - 44, 300, 88, 130, grad(f, "fy615h-coffee", IRON, INK, horizontal=True), INK, 3, 8)
    f.rect(cxm - 32, 370, 64, 54, GLASS, INK, 2.5, 8)
    f.rect(cxm - 30, 396, 60, 26, "#8a5f22", None, 0, 6)
    f.circle(cxm + 26, 316, 5, HOT)
    # toaster
    f.rect(tx - 54, 368, 108, 62, H.steel(f, "fy615h-toaster"), INK, 3, 16)
    for dx in (-22, 10): f.rect(tx + dx, 362, 14, 8, INK, rx=3)
    f.add(f'<path d="M{tx - 40},360 q-6,-18 4,-30 M{tx + 14},360 q-6,-18 4,-30" fill="none" stroke="{HEAT}" stroke-width="3" stroke-linecap="round" stroke-opacity="0.6"/>')
    # microwave
    f.rect(mx0, 330, 190, 100, grad(f, "fy615h-mw", WHITE, ALUMINIUM), INK, 3, 8)
    f.rect(mx0 + 14, 344, 124, 72, H.glow(f, "fy615h-mwglow", HEAT_LIGHT, SAND), INK, 2.5, 6)
    for k in range(4): f.rect(mx0 + 150, 346 + k * 16, 26, 9, IRON, rx=2)
    # ceiling lamp off
    f.line(600, 0, 600, 60, INK, 3)
    f.path("M560,96 Q600,40 640,96 Z", grad(f, "fy615h-shade", ALUMINIUM, METAL_EDGE), INK, 3)
    return f.svg()


FIGURES = {"hero": hero, "ryhma": ryhma, "pistorasia": pistorasia, "maadoitus": maadoitus, "luokat": luokat,
           "vikavirtasuoja": vikavirtasuoja, "askel": askel, "vaikutukset": vaikutukset, "ex-askel": ex_askel,
           "merkki-1": lambda: merkki(1), "merkki-2": lambda: merkki(2), "merkki-3": lambda: merkki(3)}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "hero": "decorative",
    "ryhma": "reveals: the loads of a group are in parallel and the fuse carries their sum I = I1 + I2 + I3 (a theory figure)",
    "pistorasia": "reveals: an earthed socket's PE contacts and the colours of L, N and PE (a theory figure)",
    "maadoitus": "reveals: without earthing the fault current goes through the person, with PE through the earth conductor (a theory figure)",
    "luokat": "reveals: the symbols of protection classes I, II and III with their names (a theory figure)",
    "vikavirtasuoja": "reveals: the RCD compares I_L and I_N; the difference I_v goes through the person to earth (a theory figure)",
    "askel": "reveals: a long stride across the potential gradient gives a step voltage, feet together almost none (a theory figure)",
    "vaikutukset": "reveals: the approximate effects of 0,5 / 10 / 30 / 50 mA through the body (a theory figure)",
    "ex-askel": "safe: a model V(r) = 1200 V·m / r around a fallen conductor on a 1 m and 200 V grid; no step voltage drawn",
    "merkki-1": "safe: the class I symbol (earth in a circle) without its name",
    "merkki-2": "safe: the class II symbol (two nested squares) without its name",
    "merkki-3": "safe: the class III symbol (III in a diamond) without its name",
}
