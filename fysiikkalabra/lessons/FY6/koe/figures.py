"""Figures of the FY6 Esimerkkikoe (scripts/figlib.py); `python scripts/practice.py figures FY6/koe` writes the model
figures into solutions.md. The task figures fy6-k1-switch, fy6-k1-battery, fy6-k1-charging, fy6-k3-circuits and
fy6-k6-setup are shown in the statements by their ids (fy6-koe/<name>). Circuit diagrams use the IEC symbols of the FY6
chapters (resistor a rectangle, lamp a circle with a cross, source a long thin + plate and a short thick − plate, diode a
triangle with a bar, LED the same with two light arrows); every label is LaTeX. Graphs to scale from the task data."""
import math
from figlib import Fig, Axes, INK, MUTED, WHITE, RULE, RULE_LIGHT, COLD, HEAT, HOT, ALUMINIUM, METAL_EDGE, SAND_LIGHT, SAND, GRAIN, n, fi

W = 3                                                    # wire width
dec = lambda d: (lambda v: f"{v:.{d}f}".replace(".", "{,}"))


# ---------------------------------------------------------------- circuit symbols (as in lessons/FY6/fy6-1 and fy6-14)
def wire(f, *pts):
    p = " ".join(f"{n(x)},{n(y)}" for x, y in pts)
    f.add(f'<polyline points="{p}" fill="none" stroke="{INK}" stroke-width="{W}" stroke-linejoin="miter" stroke-linecap="square"/>')


def cell(f, cx, cy, gap=12):
    """A source on a vertical wire: the long thin plate (+) above, the short thick plate (−) below."""
    f.rect(cx - 30, cy - gap / 2 - 2, 60, gap + 4, WHITE)
    f.line(cx - 24, cy - gap / 2, cx + 24, cy - gap / 2, INK, 3)
    f.line(cx - 11, cy + gap / 2, cx + 11, cy + gap / 2, INK, 7)


def lamp(f, cx, cy, r=20):
    f.circle(cx, cy, r, WHITE, INK, W)
    d = r * 0.7071
    f.line(cx - d, cy - d, cx + d, cy + d, INK, 2.5)
    f.line(cx - d, cy + d, cx + d, cy - d, INK, 2.5)


def resistor(f, cx, cy, vertical=False):
    w, h = (22, 54) if vertical else (54, 22)
    f.rect(cx - w / 2, cy - h / 2, w, h, WHITE, INK, W)


def vswitch(f, x, y1, y2):
    """An open switch on a vertical wire between y1 (top) and y2."""
    f.rect(x - 6, y1 + 1, 12, y2 - y1 - 2, WHITE)
    L = y2 - y1
    f.line(x, y2, x - L * math.sin(math.radians(28)), y2 - L * math.cos(math.radians(28)), INK, W, cap="round")
    f.circle(x, y1, 4.5, WHITE, INK, 2.5); f.circle(x, y2, 4.5, WHITE, INK, 2.5)


def node(f, x, y): f.circle(x, y, 5.5, INK)


def led(f, x, y):
    """An LED on a vertical wire at x, centred on y, pointing down (the current can pass downward), two light arrows."""
    f.rect(x - 18, y - 15, 36, 30, WHITE)
    f.path(f"M{n(x - 16)},{n(y - 14)} L{n(x + 16)},{n(y - 14)} L{n(x)},{n(y + 14)} Z", WHITE, INK, 2.5)
    f.line(x - 17, y + 14, x + 17, y + 14, INK, 3)
    for dy in (-8, 4):
        f.arrow(x + 20, y + dy, x + 36, y + dy - 13, INK, 2, 9)


# ---------------------------------------------------------------- Osa 1 task figures (no answer drawn in)
def switch():
    """Osa 1 item d: L1 in series with L2 parallel to (switch K + L3)."""
    f = Fig("fy6-k1-switch", 340, "Kytkentäkaavio: paristo on vasemmalla pystysuorassa johdossa, plusnapa ylempänä. Pariston "
            "plusnavasta johto kulkee ylhäällä oikealle lampun L1 kautta haarautumispisteeseen. Siitä lähtee kaksi rinnakkaista "
            "haaraa alas: vasemmassa haarassa on lamppu L2, oikeassa haarassa avoin kytkin K ja sen alla lamppu L3. Haarat "
            "yhdistyvät alhaalla, ja johto palaa pariston miinusnapaan.")
    L, X2, X3, T, B = 90, 360, 520, 74, 296
    wire(f, (L, T), (X3, T), (X3, B), (L, B), (L, T))
    wire(f, (X2, T), (X2, B))
    cell(f, L, 185)
    f.tex(L - 40, 168, "+", "end"); f.tex(L - 40, 204, "-", "end")
    lamp(f, 220, T); f.tex(220, T - 42, "L_1", "middle")
    lamp(f, X2, 185); f.tex(X2 + 32, 185, "L_2", "start")
    vswitch(f, X3, 110, 166); f.tex(X3 + 22, 138, "K", "start")
    lamp(f, X3, 230); f.tex(X3 + 32, 230, "L_3", "start")
    node(f, X2, T); node(f, X2, B)
    return f.svg()


def battery():
    """Osa 1 item f: a battery's terminal voltage, a line from (0; 1,60 V) to (1,0 A; 1,20 V)."""
    f = Fig("fy6-k1-battery", 400, "Kuvaaja: pariston napajännite U voltteina paristosta otetun virran I funktiona ampeereina. "
            "Laskeva suora alkaa pystyakselilta kohdasta 1,60 V ja päättyy pisteeseen, jossa virta on 1,0 A ja jännite 1,20 V. "
            "Ruudukko on 0,1 ampeerin ja 0,1 voltin välein.")
    lab2 = lambda v: f"{v:.1f}".replace(".", "{,}") if round(v * 10) % 2 == 0 else ""
    ax = Axes(f, (100, 350), (470, 70), x=(0, 1.2), y=(0, 1.8), xticks=[round(0.1 * i, 1) for i in range(1, 13)],
              yticks=[round(0.1 * i, 1) for i in range(1, 19)], xlabel=r"I\ (\text{A})", ylabel=r"U\ (\text{V})", xfmt=lab2, yfmt=lab2)
    ax.line([(0, 1.60), (1.0, 1.20)], INK, 3.5)
    return f.svg()


def charging():
    """Osa 1 item i: four (t, I) graphs for charging a capacitor through a resistor; C is right."""
    f = Fig("fy6-k1-charging", 520, "Neljä kuvaajaa A–D, kussakin virta I ajan t funktiona latauksen alusta. "
            "A: virta on koko ajan sama vakio. B: virta alkaa nollasta, kasvaa ensin nopeasti ja sitten yhä hitaammin ja lähestyy "
            "vakioarvoa. C: virta alkaa suurimmasta arvostaan, pienenee ensin nopeasti ja sitten yhä hitaammin ja lähestyy nollaa. "
            "D: virta alkaa nollasta ja kasvaa tasaisesti suorana.", size=28)
    f.line(300, 20, 300, 500, RULE, 1.5, "6 6"); f.line(20, 262, 580, 262, RULE, 1.5, "6 6")
    shapes = {
        "A": lambda ax: ax.line([(0, 0.7), (1, 0.7)], INK, 3.5),
        "B": lambda ax: ax.curve(lambda t: 0.9 * (1 - math.exp(-4 * t)), 0, 1, INK, 3.5),
        "C": lambda ax: ax.curve(lambda t: 0.95 * math.exp(-4 * t), 0, 1, INK, 3.5),
        "D": lambda ax: ax.line([(0, 0), (1, 0.9)], INK, 3.5),
    }
    for i, (name, draw) in enumerate(shapes.items()):
        px, py = 300 * (i % 2), 262 * (i // 2)
        ax = Axes(f, (px + 62, py + 225), (px + 222, py + 75), x=(0, 1), y=(0, 1), xticks=[], yticks=[],
                  xlabel=r"t", ylabel=r"I", grid=False, origin_label=False)
        draw(ax)
        f.tex(px + 14, py + 40, r"\text{" + name + "}", "start")
    return f.svg()


def circuits():
    """fy6-k3 c: connection 1 (two LED branches, each with 220 ohm, in parallel) and connection 2 (two LEDs and 68 ohm in series)."""
    f = Fig("fy6-k3-circuits", 400, "Kaksi kytkentäkaaviota vierekkäin. Vasemmalla kytkentä 1: jännitelähde 5,0 V vasemmalla, "
            "ja sen rinnalla kaksi pystysuoraa haaraa. Kummassakin haarassa on ylhäällä 220 ohmin vastus ja sen alla LED, jonka "
            "kolmio osoittaa alas. Oikealla kytkentä 2: jännitelähde 5,0 V vasemmalla, ylhäällä vaakasuorassa johdossa 68 ohmin "
            "vastus, ja oikeassa pystysuorassa johdossa kaksi LEDiä peräkkäin, kolmiot alaspäin. Kummankin lähteen plusnapa on ylempänä.")
    f.line(300, 20, 300, 390, RULE, 1.5, "6 6")
    T, B = 92, 330
    # connection 1
    L, A, Bx = 36, 150, 245
    wire(f, (L, T), (Bx, T), (Bx, B), (L, B), (L, T)); wire(f, (A, T), (A, B))
    cell(f, L, 210); f.tex(L + 30, 250, r"5{,}0\,\text{V}", "start")
    f.tex(L + 30, 188, "+", "start"); f.tex(L + 30, 222, "-", "start")
    for x in (A, Bx):
        resistor(f, x, 160, vertical=True); led(f, x, 262)
    f.tex(A - 16, 160, r"220\,\Omega", "end")
    f.tex(Bx - 16, 160, r"220\,\Omega", "end")
    node(f, A, T); node(f, A, B)
    f.tex(150, 40, r"\text{kytkentä 1}", "middle")
    # connection 2
    L2, R2 = 346, 520
    wire(f, (L2, T), (R2, T), (R2, B), (L2, B), (L2, T))
    cell(f, L2, 210); f.tex(L2 + 30, 250, r"5{,}0\,\text{V}", "start")
    f.tex(L2 + 30, 188, "+", "start"); f.tex(L2 + 30, 222, "-", "start")
    resistor(f, 433, T); f.tex(433, T + 34, r"68\,\Omega", "middle")
    led(f, R2, 176); led(f, R2, 270)
    f.tex(450, 40, r"\text{kytkentä 2}", "middle")
    return f.svg()


def setup():
    """fy6-k6 task figure: the lower charged ball on an insulating rod on a digital balance, the upper ball above it."""
    f = Fig("fy6-k6-setup", 420, "Koejärjestely sivulta. Pöydällä on digitaalivaaka, jonka päällä seisoo pystysuora eristetanko. "
            "Tangon yläpäässä on pieni metallipinnoitettu pallo. Sen yläpuolella on samanlainen pallo, joka on kiinnitetty "
            "vaakasuoran eristetangon päähän; tanko on kiinni telineessä vaa'an vieressä. Pallojen keskipisteiden välinen etäisyys "
            "on merkitty kirjaimella r.")
    f.rect(40, 368, 520, 14, SAND, GRAIN, 2)                                 # table
    f.rect(150, 318, 240, 50, ALUMINIUM, INK, 2.5, rx=6)                     # balance
    f.rect(176, 332, 74, 24, WHITE, INK, 2, rx=3)
    f.rect(200, 306, 140, 12, METAL_EDGE, INK, 2, rx=2)                      # pan
    f.rect(262, 196, 16, 110, SAND_LIGHT, INK, 2, rx=3)                      # insulating rod
    by, ty = 178, 88
    f.circle(270, by, 18, ALUMINIUM, INK, 2.5)
    f.circle(270, ty, 18, ALUMINIUM, INK, 2.5)
    f.rect(470, 40, 14, 328, METAL_EDGE, INK, 2)                             # stand
    f.rect(288, 82, 182, 12, SAND_LIGHT, INK, 2, rx=3)                       # horizontal insulating rod
    f.rect(458, 74, 38, 28, IRONLIKE, INK, 2, rx=3)                          # clamp
    for y in (by, ty): f.line(196, y, 250, y, MUTED, 1.5, "5 4")
    f.arrow(210, by - 2, 210, ty + 2, INK, 2.5, 12); f.arrow(210, ty + 2, 210, by - 2, INK, 2.5, 12)
    f.tex(196, (by + ty) / 2, "r", "end")
    f.tex(296, 250, r"\text{eristetanko}", "start", MUTED, size=20)
    f.tex(390, 344, r"\text{vaaka}", "start", MUTED, size=20)
    return f.svg()


IRONLIKE = "#9aa3ad"

# ---------------------------------------------------------------- Osa 2 and 3 model figures
U2 = [0.0, 0.50, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
IR2 = [0, 28, 55, 112, 166, 223, 277, 334]
IL2 = [0, 76, 112, 165, 204, 241, 270, 300]
I2D = 189                                                 # mA, the series current (answers.py)


def characteristics():
    f = Fig("fy6-k2-graph", 460, "Kuvaaja: jännite U voltteina virran I funktiona milliampeereina. Vastuksen mittauspisteet ovat "
            "sinisiä ympyröitä origon kautta kulkevalla suoralla, joka kulkee pisteen 300 mA ja 5,4 V kautta. Lampun mittauspisteet ovat "
            "oransseja ympyröitä origosta alkavalla, ylöspäin kaartuvalla käyrällä, joka päättyy pisteeseen 300 mA ja 6,0 V. "
            "Käyrät leikkaavat noin 260 milliampeerin kohdalla. Pystysuora katkoviiva virran 189 mA kohdalla osoittaa sarjaankytkennän: "
            "vastuksen jännite 3,4 V ja lampun jännite 2,6 V, yhteensä 6,0 V.")
    ax = Axes(f, (90, 400), (470, 70), x=(0, 350), y=(0, 7), xticks=[50 * i for i in range(1, 8)], yticks=list(range(1, 8)),
              xlabel=r"I\ (\text{mA})", ylabel=r"U\ (\text{V})")
    ax.line([(0, 0), (350, 350 * 0.018)], COLD, 3)
    ax.curve(lambda i: 6.0 * (i / 300) ** (1 / 0.55), 0, 300, HEAT, 3)
    ax.guide(300, 5.4)
    ax.line([(I2D, 0), (I2D, 6.0)], MUTED, 1.5, dash="6 5")
    for u, i in zip(U2, IR2): ax.point(i, u, COLD)
    for u, i in zip(U2, IL2): ax.point(i, u, HEAT)
    f.tex(ax.X(345), ax.Y(6.8), r"\text{vastus}", "end", COLD)
    f.tex(ax.X(300) - 14, ax.Y(6.0), r"\text{lamppu}", "end", HEAT, bg=True)          # at the end of its curve
    # the two readings at 189 mA, each at the height it is read and joined to its point by a thin leader: there is no
    # room for a label between the 189 mA line and the 300 mA guide
    for u, x_lab, anchor, tex, col in ((3.4, ax.X(0) + 12, "start", r"U_R \approx 3{,}4\,\text{V}", COLD),
                                       (2.6, ax.X(300) + 12, "start", r"U_\text{L} \approx 2{,}6\,\text{V}", HEAT)):
        x0, y0 = ax.X(I2D), ax.Y(u)
        x_end = x_lab - 4 if x_lab > x0 else x_lab + 125                  # the leader stops short of the label's box
        f.line(x0 + (6 if x_lab > x0 else -6), y0, x_end, y0, MUTED, 1)
        f.circle(x0, y0, 3, MUTED)
        f.tex(x_lab, y0, tex, anchor, col, bg=True)
    f.tex(ax.X(I2D) + 8, ax.Y(0.45), r"189\,\text{mA}", "start", MUTED, bg=True)
    return f.svg()


R6 = [3.0, 4.0, 5.0, 6.0, 8.0, 10.0, 12.0]
M6 = [0.558, 0.339, 0.228, 0.160, 0.090, 0.057, 0.041]
g = 9.81


def coulomb():
    f = Fig("fy6-k6-graph", 440, "Kuvaaja: sähköinen voima F millinewtoneina etäisyyden neliön käänteisluvun funktiona, "
            "vaaka-akselilla yksi per neliömetri. Seitsemän mittauspistettä. Viisi pistettä pienimmillä vaaka-akselin arvoilla eli "
            "suurimmilla etäisyyksillä on origon kautta kulkevalla suoralla, joka kulkee pisteen 400 ja 2,24 mN kautta. Kaksi "
            "pistettä suurimmilla arvoilla, etäisyyksillä 4 ja 3 cm, ovat suoran alapuolella; ero kasvaa etäisyyden pienetessä.")
    ax = Axes(f, (90, 380), (445, 70), x=(0, 1200), y=(0, 7), xticks=[200 * i for i in range(1, 7)], yticks=list(range(1, 8)),
              xlabel=r"r^{-2}\ (\text{m}^{-2})", ylabel=r"F\ (\text{mN})")
    ax.line([(0, 0), (1200, 1200 * 5.6e-3)], INK, 3)
    ax.guide(400, 2.24)
    for r, m in zip(R6, M6): ax.point(1 / (r / 100) ** 2, m * g, HOT if r < 5 else INK)
    f.tex(ax.X(400) + 10, ax.Y(2.24) + 22, r"(400;\ 2{,}24)", "start", INK, size=20, bg=True)
    f.tex(ax.X(1111), ax.Y(5.47) + 28, r"3{,}0\,\text{cm}", "middle", HOT, size=20, bg=True)
    f.tex(ax.X(625) + 14, ax.Y(3.33) + 22, r"4{,}0\,\text{cm}", "start", HOT, size=20, bg=True)
    return f.svg()


FIGURES = {"fy6-k1-switch": switch, "fy6-k1-battery": battery, "fy6-k1-charging": charging, "fy6-k3-circuits": circuits,
           "fy6-k6-setup": setup, "fy6-k2-graph": characteristics, "fy6-k6-graph": coulomb}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "fy6-k1-switch": "safe",
    "fy6-k1-battery": "safe",
    "fy6-k1-charging": "safe",
    "fy6-k3-circuits": "safe",
    "fy6-k6-setup": "safe",
    "fy6-k2-graph": "reveals: the model graph of exam task fy6-k2 (its solution)",
    "fy6-k6-graph": "reveals: the model graph of exam task fy6-k6 (its solution)",
}
