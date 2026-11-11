"""Figures of the FY5 Esimerkkikoe (scripts/figlib.py, scripts/fbd.py); `python scripts/practice.py figures FY5/koe` writes the
model figures into solutions.md. The task figures fy5-k1-osc, fy5-k1-doppler and fy5-k2-board are shown in the statements by
their ids (fy5-koe/<name>) and carry no answer. Every force diagram is an FBD: the object alone as a plain rectangle, forces
red, velocity blue, acceleration orange; no point-particle diagrams."""
import math
from figlib import Fig, Axes, INK, MUTED, RULE, WHITE, COLD, COLD_LIGHT, WATER_LIGHT, SAND_LIGHT, fi
from fbd import FBD, ground
import herolib as H

g = 9.81
gamma = 6.674e-11
dec = lambda d: (lambda v: f"{v:.{d}f}".replace(".", "{,}"))


def _dim(f, x1, x2, y, lab, above=True):
    """A dimension line with arrowheads at both ends and its label."""
    xm = (x1 + x2) / 2
    f.arrow(xm, y, x1, y, MUTED, 2, 11); f.arrow(xm, y, x2, y, MUTED, 2, 11)
    f.tex(xm, y - 18 if above else y + 18, lab, "middle", MUTED)


def _grid4(f, top):
    """The dashed lines between four option panels below y = top (two columns, two rows of 220)."""
    f.line(300, top + 10, 300, top + 430, RULE, 1.5, "6 6"); f.line(20, top + 220, 580, top + 220, RULE, 1.5, "6 6")


# ---------------------------------------------------------------- Osa 1 task figures (no answer drawn in)
def osc():
    """Osa 1 item e: x(t) of a spring oscillator (a cosine, two periods) and four v(t) options; C (−sin) is right."""
    f = Fig("fy5-k1-osc", 710, "Ylhäällä kuvaaja: jousen päässä värähtelevän kappaleen paikka x ajan t funktiona. Käyrä alkaa "
            "suurimmasta positiivisesta arvosta, laskee nollan kautta pienimpään arvoon ja palaa takaisin; kuvassa on kaksi jaksoa. "
            "Sen alla neljä kuvaajaa A–D, kussakin nopeus v ajan t funktiona samalla aika-akselilla. A: käyrä alkaa suurimmasta "
            "positiivisesta arvosta ja on samanmuotoinen kuin paikan kuvaaja. B: käyrä alkaa nollasta ja nousee ensin positiiviseksi. "
            "C: käyrä alkaa nollasta ja laskee ensin negatiiviseksi. D: käyrä alkaa pienimmästä negatiivisesta arvosta ja on paikan "
            "kuvaajan peilikuva aika-akselin suhteen.", size=28)
    w = lambda t: 2 * math.pi * 2 * t
    top = Axes(f, (80, 200), (470, 70), x=(0, 1), y=(-1.3, 1.3), xticks=[], yticks=[], xlabel=r"t", ylabel=r"x",
               grid=False, origin_label=False, x_at=0)
    top.curve(lambda t: math.cos(w(t)), 0, 0.95, INK, 3.5, steps=160)
    _grid4(f, 260)
    shapes = {"A": lambda t: math.cos(w(t)), "B": lambda t: math.sin(w(t)),
              "C": lambda t: -math.sin(w(t)), "D": lambda t: -math.cos(w(t))}
    for i, (name, fn) in enumerate(shapes.items()):
        px, py = 300 * (i % 2), 270 + 220 * (i // 2)
        ax = Axes(f, (px + 62, py + 200), (px + 222, py + 50), x=(0, 1), y=(-1.3, 1.3), xticks=[], yticks=[],
                  xlabel=r"t", ylabel=r"v", grid=False, origin_label=False, x_at=0)
        ax.curve(fn, 0, 0.95, INK, 3.5, steps=160)
        f.tex(px + 16, py + 26, r"\text{" + name + "}", "start")
    return f.svg()


def doppler():
    """Osa 1 item i: the heard frequency of a passing siren; B (high, smooth drop through f0 at t = 0, low) is right."""
    f = Fig("fy5-k1-doppler", 480, "Neljä kuvaajaa A–D, kussakin kuultu taajuus f ajan t funktiona. Aika-akselin keskellä on "
            "ohitushetki t = 0, ja vaakasuora katkoviiva on sireenin oma taajuus f 0. A: taajuus pysyy koko ajan katkoviivan "
            "kohdalla. B: taajuus on aluksi tasaisesti katkoviivan yläpuolella, laskee ohitushetken ympärillä katkoviivan läpi ja "
            "pysyy sitten tasaisesti sen alapuolella. C: taajuus on aluksi katkoviivan kohdalla, nousee ohitushetkeä kohti huippuun "
            "ja palaa sitten katkoviivan kohdalle. D: taajuus on aluksi tasaisesti katkoviivan alapuolella, nousee ohitushetken "
            "ympärillä ja pysyy sitten sen yläpuolella.", size=28)
    _grid4(f, 10)
    cos = lambda t: -t / math.hypot(t, 0.18)                  # the angle between the velocity and the line to the listener
    B = lambda t: 1 / (1 - 0.1 * cos(t))
    shapes = {"A": lambda t: 1.0, "B": B, "C": lambda t: 1 + 0.11 * math.exp(-t * t / 0.06), "D": lambda t: 2 - B(t)}
    for i, (name, fn) in enumerate(shapes.items()):
        px, py = 300 * (i % 2), 20 + 220 * (i // 2)
        ax = Axes(f, (px + 62, py + 190), (px + 222, py + 50), x=(-1, 1), y=(0.8, 1.2), xticks=[0], yticks=[],
                  xlabel=r"t", ylabel=r"f", grid=False, origin_label=False)
        ax.line([(-1, 1), (1, 1)], MUTED, 2, dash="7 6")
        ax.curve(fn, -0.95, 0.95, INK, 3.5, steps=160)
        f.tex(px + 50, ax.Y(1.0), r"f_0", "end", MUTED)
        f.tex(px + 16, py + 22, r"\text{" + name + "}", "start")
    return f.svg()


# ---------------------------------------------------------------- Osa 2
BX0, PXM = 70, 120.0                                          # the board's back end A in the figure; px per metre


def board():
    """fy5-k2 task figure: the diving board from the side, A bolted to a stand on the pool edge, support B at 1,2 m, the diver at the tip."""
    f = Fig("fy5-k2-board", 340, "Kaaviokuva hyppylaudasta sivulta. Vasemmalla altaan reuna. Vaakasuoran laudan vasen pää A on "
            "kiinnitetty pultilla matalaan jalustaan altaan reunalla. Laudan alla on tuki B, 1,2 metrin päässä päästä A. Lauta on "
            "irti altaan reunasta muualla kuin kohdissa A ja B. Laudan oikeassa päässä, 4,0 metrin päässä päästä A, seisoo "
            "hyppääjä. Laudan alla on vesi.")
    y0, th = 150, 16
    xB, xt = BX0 + 1.2 * PXM, BX0 + 4.0 * PXM
    yd = y0 + th / 2 + 30                                      # the deck, below the board
    # the pool: water with a surface and ripples, then the concrete edge with its coping over the water
    f.defs_add(f'<linearGradient id="fy5k2-water" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{WATER_LIGHT}"/>'
               f'<stop offset="1" stop-color="#7fb4e0"/></linearGradient>')
    f.rect(236, yd + 34, 344, 66, "url(#fy5k2-water)", None)
    f.line(236, yd + 34, 580, yd + 34, "#2f74b5", 2)
    for wx, wy in ((290, 14), (372, 26), (452, 12), (520, 30), (330, 44), (486, 48)):
        f.path(f"M{wx},{yd + 34 + wy} q9,-5 18,0 t18,0", stroke=WHITE, w=2, extra='stroke-opacity="0.75" stroke-linecap="round"')
    f.rect(20, yd, 230, 100, SAND_LIGHT, INK, 2)               # the pool edge
    f.rect(20, yd, 238, 10, "#e3dccb", INK, 1.75)              # its coping, a little over the water
    f.rect(BX0 - 8, y0 + th / 2, 16, 30, "#c4ccd4", INK, 2)    # the stand at A
    f.path(f"M{xB},{y0 + th / 2} L{xB - 16},{yd} L{xB + 16},{yd} Z", "#c4ccd4", INK, 2)   # the support at B
    f.rect(BX0, y0 - th / 2, xt - BX0, th, "#f2a69c", INK, 2.5, 3)   # the board
    for k in range(1, 6): f.line(xt - 14 * k, y0 - th / 2 + 3, xt - 14 * k, y0 + th / 2 - 3, "#c92a2a", 1.25)   # grip strips at the tip
    f.circle(BX0, y0, 5, WHITE, INK, 2); f.line(BX0 - 3, y0, BX0 + 3, y0, INK, 1.5)       # the bolt
    H.person(f, xt - 16, y0 - th / 2, shirt="#2f74b5", trousers="#3a4350", sc=0.27)      # the diver, a drawn figure as in the lessons
    f.tex(BX0 + 4, y0 - 32, r"\text{A}", "middle")
    f.tex(xB, y0 - 30, r"\text{B}", "middle")
    _dim(f, BX0, xB, 318, r"1{,}2\,\text{m}", above=True)
    f.line(BX0, yd + 6, BX0, 328, MUTED, 1.5, "4 4"); f.line(xB, yd + 6, xB, 328, MUTED, 1.5, "4 4")
    _dim(f, BX0, xt, 40, r"4{,}0\,\text{m}", above=True)
    f.line(BX0, 28, BX0, y0 - 46, MUTED, 1.5, "4 4"); f.line(xt, 28, xt, y0 - 14, MUTED, 1.5, "4 4")
    return f.svg()


def board_fbd():
    """fy5-k2 a model: the board's FBD; bolt force down at A, support up at B, weight at the centre, the diver's push at the tip."""
    mb, mh = 40.0, 60.0
    Gb, Fh = mb * g, mh * g
    FA = (Gb * 0.8 + Fh * 2.8) / 1.2; NB = FA + Gb + Fh
    f = Fig("fy5-k2-fbd", 440, "Mallikuvio: hyppylaudan voimakuvio. Lauta on pitkä vaakasuora suorakulmio. Vasemmasta päästä A "
            "osoittaa alas pultin voima F A. Tuen kohdalta B, 1,2 metrin päästä päästä A, osoittaa ylös tukivoima N, joka on "
            "kuvion pisin nuoli. Laudan keskeltä osoittaa alas laudan paino G, lyhyt nuoli. Laudan oikeaan päähän osoittaa "
            "ylhäältä alas hyppääjän jalkojen voima F h. Nuolten pituudet ovat mittakaavassa.")
    s = 0.085
    cy, w, h = 262, 4.0 * PXM, 18
    cx = BX0 + w / 2
    d = FBD(f, s, body=(cx, cy, w, h), a_dir=(0, 0))
    d.force("G", (0, -Gb), (cx, cy), "gravity", lab=(24, 6))
    d.force("N", (0, NB), (BX0 + 1.2 * PXM, cy + h / 2), "normal", surface=0, lab=(26, 8))
    d.force("F_A", (0, -FA), (BX0, cy + h / 2), "other", tex=r"\overline{F}_\text{A}", lab=(34, -4))
    d.force("F_h", (0, -Fh), (BX0 + w - 10, cy - h / 2), "other", tex=r"\overline{F}_\text{h}", lab=(-34, 4), push=True)
    d.draw()
    f.tex(BX0 + 14, cy - 34, r"\text{A}", "middle", MUTED)
    f.tex(BX0 + 1.2 * PXM - 26, cy - 34, r"\text{B}", "middle", MUTED)
    return f.svg()


def camera():
    """fy5-k3 c model: the loose camera in orbit; the only force is gravity towards the Earth, v along the orbit, a with F."""
    m, a = 1.0, 8.39
    f = Fig("fy5-k3-fbd", 340, "Mallikuvio: kameran voimakuvio, kun kamera on satelliitin mukana radan ylimmässä kohdassa. Kamera on "
            "suorakulmio, jonka läpi kulkee ohut katkoviivalla piirretty kaareva rata. Ainoa voima on kameran keskipisteestä "
            "alas kohti Maan keskipistettä osoittava gravitaatiovoima F. Kameran vieressä ohut sininen nopeusnuoli osoittaa "
            "vaakasuoraan radan suuntaan ja ohut oranssi kiihtyvyysnuoli alas kohti Maan keskipistettä.")
    cx, cy, Rp = 260, 120, 760
    f.path(f"M40,{cy + Rp - math.sqrt(Rp * Rp - 220 ** 2):.1f} A{Rp},{Rp} 0 0 1 480,{cy + Rp - math.sqrt(Rp * Rp - 220 ** 2):.1f}",
           stroke=MUTED, w=2, extra='stroke-dasharray="8 7"')
    f.tex(470, cy + Rp - math.sqrt(Rp * Rp - 210 ** 2) - 26, r"\text{rata}", "middle", MUTED)
    d = FBD(f, 16, body=(cx, cy, 80, 52), m=m, a=(0, -a))
    d.force("F", (0, -m * a), (cx, cy), "gravity", lab=(22, 2))
    d.draw()
    d.motion(r"\overline{v}", (1, 0), (330, 62), 90, lab=(24, 0))
    d.motion(r"\overline{a}", (0, -1), (360, 160), 90, lab=(22, 0))
    f.tex(cx, 300, r"\text{kohti Maan keskipistettä}", "middle", MUTED)
    return f.svg()


L4 = [0.300, 0.500, 0.700, 0.900, 1.100, 1.300]
T10 = [11.40, 14.43, 17.05, 19.22, 21.27, 23.02]


def _fit(x, y):
    mx, my = sum(x) / len(x), sum(y) / len(y)
    k = sum((a - mx) * (b - my) for a, b in zip(x, y)) / sum((a - mx) ** 2 for a in x)
    return k, my - k * mx


def pendulum():
    """fy5-k4 b model: (l, T²) with the least-squares line, its intercept and the two read points."""
    T2 = [(t / 10) ** 2 for t in T10]
    k, b = _fit(L4, T2)
    f = Fig("fy5-k4-graph", 430, "Kuvaaja: jaksonajan neliö T toiseen sekunnin neliöinä langan pituuden l funktiona metreinä. "
            "Kuusi mittauspistettä ovat lähes suoralla. Pisteisiin sovitettu suora nousee tasaisesti ja leikkaa pystyakselin hieman "
            "origon yläpuolella, noin kohdassa 0,09 sekunnin neliötä. Suoralta on luettu pisteet (0,10 m; 0,49 s²) ja "
            "(1,30 m; 5,31 s²), ja kulmakerroin on noin 4,02 sekunnin neliötä metriä kohti.")
    ax = Axes(f, (90, 380), (470, 70), x=(0, 1.4), y=(0, 6), xticks=[0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4], yticks=[0, 1, 2, 3, 4, 5, 6],
              xlabel=r"l\ (\text{m})", ylabel=r"T^2\ (\text{s}^2)", xfmt=dec(1))
    ax.line([(0, b), (1.4, k * 1.4 + b)], INK, 3)
    for P in [(0.10, 0.49), (1.30, 5.31)]: ax.guide(*P)
    for x, y in zip(L4, T2): ax.point(x, y)
    f.tex(ax.X(0.72), ax.Y(0.8), r"k \approx 4{,}02\,\text{s}^2/\text{m}", "start", INK, bg=True)
    return f.svg()


def modes():
    """fy5-k5 a model: the string's fundamental (n = 1) and second mode (n = 2), nodes S and antinodes K."""
    f = Fig("fy5-k5-modes", 400, "Mallikuvio: kahdesta päästä kiinnitetyn kielen seisovat aallot. Ylhäällä perustaajuus: kieli "
            "värähtelee yhtenä kaarena, jonka ääriasennot on piirretty; solmut S ovat kielen päissä ja kupu K keskellä. Alhaalla "
            "seuraava ominaistaajuus kaksinkertaisella taajuudella: kaksi kaarta vastakkaisiin suuntiin, solmut päissä ja keskellä, "
            "kuvut neljänneksen ja kolmen neljänneksen kohdalla. Kielen pituus on L.")
    x0, x1 = 90, 510
    for row, (nmode, lab) in enumerate(((1, r"n = 1:\ f_1"), (2, r"n = 2:\ f_2 = 2f_1"))):
        yc = 110 + 170 * row
        f.tex(20, yc - 72, lab, "start")
        for xe in (x0, x1): f.rect(xe - 8, yc - 22, 16, 44, "#c4ccd4", INK, 2)
        for sgn, col in ((1, COLD), (-1, COLD)):
            pts = " ".join(f"{x0 + (x1 - x0) * i / 120:.1f},{yc - sgn * 46 * math.sin(nmode * math.pi * i / 120):.1f}" for i in range(121))
            f.add(f'<polyline points="{pts}" fill="none" stroke="{col}" stroke-width="3" stroke-linejoin="round"/>')
        f.line(x0, yc, x1, yc, MUTED, 1.5, "5 5")
        for j in range(nmode + 1):
            xs = x0 + (x1 - x0) * j / nmode
            f.circle(xs, yc, 6, INK)
            f.tex(xs + (16 if j == 0 else -16 if j == nmode else 0), yc + 30, r"\text{S}", "middle")
        for j in range(nmode):
            xk = x0 + (x1 - x0) * (j + 0.5) / nmode
            f.tex(xk + 18, yc - 62 if j % 2 == 0 else yc + 62, r"\text{K}", "start")
    _dim(f, x0, x1, 378, r"L", above=True)
    return f.svg()


D6 = [15.0, 25.0, 35.0, 45.0, 55.0, 65.0]
DT6 = [0.090, 0.148, 0.209, 0.267, 0.328, 0.386]


def echo():
    """fy5-k6 b model: (t, 2d) with a line through the origin; the slope is the speed of sound."""
    f = Fig("fy5-k6-graph", 430, "Kuvaaja: äänen kulkema matka 2d metreinä ajan t funktiona sekunteina. Kuusi mittauspistettä "
            "ovat origon kautta kulkevalla nousevalla suoralla. Suoralta on luettu piste (0,40 s; 134,5 m), ja kulmakertoimeksi eli "
            "äänen nopeudeksi on merkitty noin 336 metriä sekunnissa.")
    ax = Axes(f, (90, 380), (470, 70), x=(0, 0.45), y=(0, 140), xticks=[0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45],
              yticks=[0, 20, 40, 60, 80, 100, 120, 140], xlabel=r"t\ (\text{s})", ylabel=r"2d\ (\text{m})",
              xfmt=lambda v: fi(round(v, 1)) if abs(v * 10 - round(v * 10)) < 1e-9 else "")
    v = 134.5 / 0.40
    ax.line([(0, 0), (0.415, v * 0.415)], INK, 3)
    ax.guide(0.40, 134.5)
    for d, t in zip(D6, DT6): ax.point(t, 2 * d)
    f.tex(ax.X(0.23), ax.Y(40), r"v \approx 336\,\text{m/s}", "start", INK, bg=True)
    return f.svg()


FIGURES = {"fy5-k1-osc": osc, "fy5-k1-doppler": doppler, "fy5-k2-board": board, "fy5-k2-fbd": board_fbd,
           "fy5-k3-fbd": camera, "fy5-k4-graph": pendulum, "fy5-k5-modes": modes, "fy5-k6-graph": echo}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "fy5-k1-osc": "safe",
    "fy5-k1-doppler": "safe",
    "fy5-k2-board": "safe: the board's layout and distances, no forces",
    "fy5-k2-fbd": "reveals: the model force diagram of exam task fy5-k2 (its solution)",
    "fy5-k3-fbd": "reveals: the model force diagram of exam task fy5-k3 (its solution)",
    "fy5-k4-graph": "reveals: the model graph of exam task fy5-k4 (its solution)",
    "fy5-k5-modes": "reveals: the model drawing of exam task fy5-k5 (its solution)",
    "fy5-k6-graph": "reveals: the model graph of exam task fy5-k6 (its solution)",
}
