"""Figures of FY6 Sovella itsenäisesti (scripts/figlib.py); `python scripts/practice.py figures FY6` writes them into
solutions.md. Three are task figures (the measuring circuit of s1, the lamp circuit of s2, the plates of s3) that carry
no answer; fy6-s1-graph is the model graph of s1 a. Circuit diagrams with IEC symbols: resistor a rectangle, cell a long
thin (+) and a short thick (-) plate, lamp a circle with a cross, meters circles with their letter, fuse a rectangle with
a line through it; conventional current + -> - in violet (#7048e8) as in the other FY6 chapters; field lines green."""
from figlib import Fig, Axes, fi, INK, MUTED, WHITE, RULE, HOT, HOT_LIGHT, COLD, GLASS, GOOD, n

CUR = "#7048e8"     # conventional current
POT = COLD          # voltages and potentials
FIELD = GOOD        # electric field lines and arrows (#2b8a3e)


def wire(f, *pts):
    f.add('<polyline points="' + " ".join(f"{n(x)},{n(y)}" for x, y in pts) + f'" fill="none" stroke="{INK}" '
          'stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>')


def resistor(f, x, y, vertical=False, length=64, width=24):
    w, h = (width, length) if vertical else (length, width)
    f.rect(x - w / 2, y - h / 2, w, h, WHITE, INK, 3)


def fuse(f, x, y, length=64, width=24):
    f.rect(x - length / 2, y - width / 2, length, width, WHITE, INK, 3)
    f.line(x - length / 2, y, x + length / 2, y, INK, 2)


def lamp(f, x, y, r=22):
    f.circle(x, y, r, WHITE, INK, 3)
    d = r * 0.7071
    f.line(x - d, y - d, x + d, y + d, INK, 3); f.line(x - d, y + d, x + d, y - d, INK, 3)


def cell(f, x, y, gap=16):
    """Plates of a source on a vertical wire at x, centred on y: long thin (+) above, short thick (-) below."""
    f.line(x - 26, y - gap / 2, x + 26, y - gap / 2, INK, 3)
    f.line(x - 13, y + gap / 2, x + 13, y + gap / 2, INK, 7)


def node(f, x, y):
    f.circle(x, y, 6, INK)


def meter(f, x, y, letter):
    f.circle(x, y, 20, WHITE, INK, 3)
    f.tex(x, y, r"\text{" + letter + "}", "middle", w=30)


def head(f, x, y, d, colour=CUR):
    s = 10
    pts = {"r": [(x + s, y), (x - s, y - s * 0.8), (x - s, y + s * 0.8)], "l": [(x - s, y), (x + s, y - s * 0.8), (x + s, y + s * 0.8)],
           "d": [(x, y + s), (x - s * 0.8, y - s), (x + s * 0.8, y - s)], "u": [(x, y - s), (x - s * 0.8, y + s), (x + s * 0.8, y + s)]}[d]
    f.path("M" + " L".join(f"{n(a)},{n(b)}" for a, b in pts) + " Z", colour)


def new(fid, h, label):
    f = Fig(fid, h, label)
    f.wcover = 10
    return f


# --- fy6-s1 task figure: the measuring circuit -------------------------------------------------------------------
def circuit1():
    f = new("fy6-s1-circuit", 310, "Kytkentäkaavio, ei mittakaavassa: pariston mittaus. Vasemmalla on tutkittava paristo, plusnapa ylhäällä. "
            "Plusnavalta johdin kulkee ylhäällä ampeerimittarin A kautta oikealle ja alas säädettävän vastuksen R kautta takaisin "
            "miinusnavalle. Jännitemittari V on kytketty suoraan pariston napojen väliin. Violetit nuolet näyttävät virran I "
            "suunnan plusnavalta kuorman kautta miinusnavalle.")
    xb, xv, xr, top, bot = 90, 200, 500, 70, 270
    wire(f, (xb, top), (xr, top), (xr, 135)); wire(f, (xr, 195), (xr, bot), (xb, bot), (xb, 160)); wire(f, (xb, top), (xb, 134))
    cell(f, xb, 147)
    f.tex(xb - 30, 128, "+", "end", w=24); f.tex(xb - 30, 166, "-", "end", w=24)
    node(f, xv, top); node(f, xv, bot)
    wire(f, (xv, top), (xv, 150)); wire(f, (xv, 190), (xv, bot))
    meter(f, xv, 170, "V")
    f.tex(xv + 30, 170, "U", "start", POT, w=30)
    meter(f, 340, top, "A")
    resistor(f, xr, 165, True, 60)
    f.arrow(xr - 30, 200, xr + 30, 130, INK, 2.5, 12)
    f.tex(xr + 40, 165, "R", "start", w=30)
    head(f, 270, top, "r"); f.tex(270, top - 24, "I", "middle", CUR, w=24)
    head(f, xr, 100, "d"); head(f, 340, bot, "l")
    return f.svg()


# --- fy6-s1 a: the model graph ------------------------------------------------------------------------------------
I1 = [0.10, 0.20, 0.30, 0.40, 0.50, 0.60]
U1 = [4.48, 4.37, 4.22, 4.13, 3.99, 3.89]


def graph1():
    f = new("fy6-s1-graph", 380, "Kuvaaja: pariston napajännite U voltteina virran I funktiona ampeereina. Kuusi mustaa pistettä "
            "virroilla 0,10–0,60 A; jännite pienenee arvosta 4,48 V arvoon 3,89 V. Pisteisiin on sovitettu suora, joka kulkee "
            "pisteiden lomitse, ja sitä on jatkettu katkoviivana pystyakselille kohtaan 4,60 V. Suoralta on merkitty pisteet "
            "(0,10 A; 4,48 V) ja (0,60 A; 3,88 V) sekä niiden väliin kulmakertoimen kolmio, jossa virran muutos on 0,50 A ja "
            "jännitteen muutos −0,60 V. Pystyakselin asteikko alkaa arvosta 3,6 V.")
    ax = Axes(f, (96, 320), (500, 66), x=(0, 0.8), y=(3.6, 4.8), xticks=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8],
              yticks=[3.8, 4.0, 4.2, 4.4, 4.6, 4.8], xlabel=r"I\ (\text{A})", ylabel=r"U\ (\text{V})",
              xfmt=lambda v: fi(v, 1), yfmt=lambda v: fi(v, 1), origin_label=False)
    f.tex(ax.x0 - 12, ax.y0 - 4, "3{,}6", "end"); f.tex(ax.x0, ax.y0 + 24, "0", "middle")
    E, Rs = 4.60, 1.2
    ax.line([(0.06, E - Rs * 0.06), (0.77, E - Rs * 0.77)], INK, 2.5)
    ax.line([(0, E), (0.06, E - Rs * 0.06)], INK, 2.5, dash="8 6")
    for i, u in zip(I1, U1): ax.point(i, u)
    # slope triangle between the line's points at 0,10 A and 0,60 A
    ua, ub = 4.48, 3.88
    f.line(ax.X(0.10), ax.Y(ua), ax.X(0.60), ax.Y(ua), MUTED, 1.5, "6 5")
    f.line(ax.X(0.60), ax.Y(ua), ax.X(0.60), ax.Y(ub), MUTED, 1.5, "6 5")
    for i, u in ((0.10, ua), (0.60, ub)): f.circle(ax.X(i), ax.Y(u), 11, "none", INK, 1.5)
    f.tex((ax.X(0.10) + ax.X(0.60)) / 2, ax.Y(ua) + 24, r"\Delta I = 0{,}50\,\text{A}", "middle", w=150, bg=True)
    f.tex(ax.X(0.60) + 12, (ax.Y(ua) + ax.Y(ub)) / 2, r"\Delta U = -0{,}60\,\text{V}", "start", w=170, bg=True)
    f.circle(ax.X(0), ax.Y(E), 6.5, WHITE, INK, 2.5)
    f.tex(ax.X(0) + 16, ax.Y(E) - 22, r"E = 4{,}60\,\text{V}", "start", w=130)
    return f.svg()


# --- fy6-s2 task figure: cable, fuse and two lamps ---------------------------------------------------------------
def circuit2():
    f = new("fy6-s2-circuit", 310, "Kytkentäkaavio, ei mittakaavassa: mökin valaistus. Vasemmalla on 12 voltin akku, plusnapa ylhäällä. "
            "Plusnavalta johdin kulkee ylhäällä sulakkeen ja kaapelin resistanssin Rk kautta kahteen rinnan kytkettyyn lamppuun. "
            "Lamppu A on merkitty 12 V, 24 W ja lamppu B 12 V, 12 W. Alajohdin palaa lampuilta akun miinusnavalle. Violetit nuolet "
            "näyttävät virran suunnan.")
    xb, xa, xl, top, bot, yl = 80, 360, 480, 70, 270, 165
    wire(f, (xb, top), (xl, top), (xl, yl - 22)); wire(f, (xl, yl + 22), (xl, bot), (xb, bot), (xb, 160)); wire(f, (xb, top), (xb, 134))
    wire(f, (xa, top), (xa, yl - 22)); wire(f, (xa, yl + 22), (xa, bot))
    cell(f, xb, 147)
    f.tex(xb - 30, 128, "+", "end", w=24); f.tex(xb - 30, 166, "-", "end", w=24)
    f.tex(xb + 34, 147, r"E", "start", POT, w=30)
    fuse(f, 170, top, 60)
    f.tex(170, top - 30, r"\text{sulake}", "middle", w=90)
    resistor(f, 290, top, False, 64)
    f.tex(290, top - 30, r"R_\text{k}", "middle", w=44)
    node(f, xa, top); node(f, xa, bot)
    lamp(f, xa, yl); lamp(f, xl, yl)
    for x, name, v, w in ((xa, "A", r"12\,\text{V}", r"24\,\text{W}"), (xl, "B", r"12\,\text{V}", r"12\,\text{W}")):
        f.tex(x + 34, yl - 28, r"\text{" + name + "}", "start", INK, w=30)
        f.tex(x + 34, yl, v, "start", MUTED, 21, w=70)
        f.tex(x + 34, yl + 26, w, "start", MUTED, 21, w=70)
    head(f, 232, top, "r"); f.tex(232, top - 28, "I", "middle", CUR, w=24)
    head(f, 338, top, "r")
    head(f, 200, bot, "l")
    return f.svg()


# --- fy6-s3 task figure: the plates of the spray gun -------------------------------------------------------------
def field3():
    f = new("fy6-s3-field", 350, "Kaaviokuva, ei mittakaavassa: ruiskumaalauksen sähkökenttä. Ylhäällä on vaakasuora suutinlevy, jonka "
            "potentiaali on +60 kV, ja alhaalla maadoitettu työkappale. Levyjen etäisyys on d. Levyjen välissä homogeenisen "
            "sähkökentän kenttäviivat ovat vihreitä suoria viivoja ylhäältä alas, ja kenttä on merkitty E-vektorilla. Suutinlevyn "
            "vieressä on positiivisesti varautunut maalipisara varauksella q, joka lähtee levyltä.")
    xl, xr, yt, yb = 150, 500, 70, 290
    f.rect(xl, yt - 12, xr - xl, 12, "#adb5bd", INK, 2.5); f.rect(xl, yb, xr - xl, 12, "#adb5bd", INK, 2.5)
    for x in (200, 280, 360, 440):
        f.arrow(x, yt + 4, x, yb - 4, FIELD, 2.5, 13)
    f.tex(xl - 22, yt - 6, r"+60\,\text{kV}", "end", w=100); f.tex(xl - 22, yb + 6, r"0\,\text{V}", "end", w=70)
    f.tex(xl + 4, yt - 40, r"\text{suutinlevy}", "start", MUTED, w=120); f.tex(xl + 4, yb + 40, r"\text{työkappale}", "start", MUTED, w=130)
    f.tex(xr - 4, 180, r"\overline{E}", "end", FIELD, w=40)
    f.arrow(40, 180, 40, yt + 6, MUTED, 2, 11); f.arrow(40, 180, 40, yb - 6, MUTED, 2, 11)
    f.tex(54, 180, "d", "start", MUTED, w=24)
    f.circle(280, yt + 22, 16, HOT_LIGHT, INK, 2.5)
    f.tex(280, yt + 22, "+", "middle", w=24)
    f.tex(306, yt + 22, "q", "start", w=24)
    return f.svg()


FIGURES = {"fy6-s1-circuit": circuit1, "fy6-s1-graph": graph1, "fy6-s2-circuit": circuit2, "fy6-s3-field": field3}
REUSE = {
    "fy6-s1-circuit": "safe: the measuring circuit of the battery experiment (task fy6-s1)",
    "fy6-s1-graph": "reveals: the model graph, line and values of task fy6-s1 a and b (its solution)",
    "fy6-s2-circuit": "safe: the cable, fuse and two lamps with their ratings, no results (task fy6-s2)",
    "fy6-s3-field": "safe: the plates and the uniform field of the spray gun, symbols only (task fy6-s3)",
}
