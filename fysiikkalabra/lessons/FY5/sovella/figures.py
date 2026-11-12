"""Figures of FY5 Sovella itsenäisesti (scripts/figlib.py, scripts/fbd.py); `python scripts/practice.py figures FY5` writes
them into solutions.md. Two are task figures (the crane's layout, the organ pipe's microphone signal) that carry no
answer; the rest are model answers. Force red, velocity blue, acceleration orange (fbd.py); the force diagram is an FBD
(the load a plain rectangle, arrows to scale, physics checked as drawn) beside its pictorial situation picture."""
import math
from figlib import Fig, Axes, INK, MUTED, WHITE, RULE, SAND_LIGHT, SAND, IRON, ALUMINIUM, METAL_EDGE, HEAT_LIGHT, HOT, n
from fbd import FBD, ground

g = 9.81

# fy5-s2 data (answers.py): NASA JPL mean orbital radii (m) and periods (d)
MOONS = [("Amalthea", 181.4e6, 0.4982), ("Io", 421.8e6, 1.769), ("Europa", 671.1e6, 3.551),
         ("Ganymedes", 1070e6, 7.155), ("Kallisto", 1883e6, 16.69)]
# fy5-s3 data (answers.py): masses (kg) and the time of ten periods (s)
MS = [0.100, 0.150, 0.200, 0.250, 0.300, 0.350]
T10 = [4.74, 5.73, 6.50, 7.25, 7.86, 8.51]


def _fit(x, y):
    mx, my = sum(x) / len(x), sum(y) / len(y)
    k = sum((a - mx) * (b - my) for a, b in zip(x, y)) / sum((a - mx) ** 2 for a in x)
    return k, my - k * mx


def _dim(f, x1, x2, y, lab, above=True):
    """A dimension line with arrowheads at both ends and its label."""
    xm = (x1 + x2) / 2
    f.arrow(xm, y, x1, y, MUTED, 2, 11); f.arrow(xm, y, x2, y, MUTED, 2, 11)
    f.tex(xm, y - 16 if above else y + 16, lab, "middle", MUTED)


def crane():
    """fy5-s1 task figure: the tower crane from the side, with the symbols of the distances the text gives (no numbers)."""
    f = Fig("fy5-s1-crane", 350, "Kaaviokuva torninosturista sivulta. Pystysuora torni, jonka akseli on merkitty katkoviivalla. Tornin "
            "huipulla vaakasuora puomi: oikealle pitkä puomi, jota pitkin vaunu liikkuu, ja vasemmalle lyhyt vastapuomi, jonka päässä "
            "riippuu betoninen vastapaino m v. Vastapainon painopisteen etäisyys tornin akselista on r v. Puomin painopiste, massa m p, "
            "on merkitty puomiin oikealle tornista etäisyydelle r p. Vaunusta riippuu vaijerissa kuorma m etäisyydellä r tornin akselista. "
            "Tornin akselin ja puomin keskiviivan leikkauskohdassa on piste A: vaakasuora momenttiakseli, joka on kohtisuorassa kuvan "
            "tasoa vastaan.")
    ax, yj = 200, 104                                             # the tower's axis, the jib's centre line
    sc = 9.5                                                      # px per metre along the jib
    ground(f, 20, 590, 318)
    # tower: a lattice
    f.rect(ax - 14, yj + 8, 28, 318 - yj - 8, "none", IRON, 2.5)
    y = yj + 8
    while y < 300:
        f.line(ax - 14, y, ax + 14, y + 22, IRON, 1.5); f.line(ax + 14, y, ax - 14, y + 22, IRON, 1.5); y += 22
    # apex and pendants
    f.path(f"M{ax - 12},{yj - 6} L{ax},{yj - 58} L{ax + 12},{yj - 6}", "none", IRON, 2.5)
    f.line(ax, yj - 58, ax - 9.5 * sc, yj - 6, IRON, 1.5); f.line(ax, yj - 58, ax + 30 * sc, yj - 6, IRON, 1.5)
    # jib and counter-jib
    f.rect(ax - 12.5 * sc, yj - 6, 12.5 * sc + 40 * sc, 12, SAND_LIGHT, INK, 2)
    # counterweight
    xv = ax - 10 * sc
    f.rect(xv - 22, yj + 6, 44, 58, ALUMINIUM, METAL_EDGE, 2.5)
    f.tex(xv, yj + 35, r"m_\text{v}", "middle")
    # the jib's centre of mass
    xp = ax + 12 * sc
    f.circle(xp, yj, 7, WHITE, INK, 2); f.path(f"M{n(xp - 7)},{yj} A7,7 0 0 1 {n(xp)},{yj - 7} V{yj} Z", INK)
    f.path(f"M{n(xp + 7)},{yj} A7,7 0 0 1 {n(xp)},{yj + 7} V{yj} Z", INK)
    f.tex(xp, yj - 26, r"m_\text{p}", "middle")
    # trolley, rope and load
    xr = ax + 28 * sc
    f.rect(xr - 14, yj + 6, 28, 10, IRON, INK, 1.5)
    f.line(xr, yj + 16, xr, 214, INK, 2)
    f.rect(xr - 30, 214, 60, 34, HEAT_LIGHT, INK, 2.5)
    f.tex(xr, 231, r"m", "middle")
    # the axis and the dimensions
    f.line(ax, yj - 70, ax, 330, MUTED, 1.5, "8 6")
    f.tex(ax + 10, 30, r"\text{tornin akseli}", "start", MUTED)
    # the horizontal moment axis A, perpendicular to the picture: a point where the tower's axis meets the jib's centre line
    f.circle(ax, yj, 6.5, WHITE, INK, 2); f.circle(ax, yj, 2.2, INK, INK, 1)
    f.tex(ax - 22, yj - 22, r"A", "middle")
    _dim(f, xv, ax, yj + 96, r"r_\text{v}")
    _dim(f, ax, xp, yj + 36, r"r_\text{p}", above=False)
    _dim(f, ax, xr, 284, r"r")
    for x, y1, y2 in ((xv, yj + 70, yj + 106), (xp, yj + 10, yj + 46), (xr, 252, 294)):     # extension lines below each mass
        f.line(x, y1, x, y2, MUTED, 1.2, "4 4")
    return f.svg()


def load_fbd():
    """fy5-s1 d: the situation picture (the load swung out on its rope while the jib turns) and the load's force diagram.
    Drawn at a rope angle of 20° so that the arrows can be told apart; in the task the angle is about 0,6°."""
    th = math.radians(20.0); m = 2000.0
    an = g * math.tan(th)                                         # the drawn acceleration that tilts the rope 20°
    G = m * g
    f = Fig("fy5-s1-fbd", 400, "Kaksi kuvaa. Vasemmalla tilannekuva sivulta: puomin osa ylhäällä, tornin akseli katkoviivana vasemmalla. "
            "Vaunusta lähtevä vaijeri on kallistunut niin, että kuorma on vaunua kauempana tornin akselista. Kuorman vieressä oranssi "
            "kiihtyvyysnuoli a n osoittaa vaakasuoraan kohti tornin akselia. Oikealla kuorman voimakuvio, kuorma vaijerin suuntaisesti "
            "kallistettuna suorakulmiona: paino G keskipisteestä suoraan alas ja vaijerin jännitysvoima S yläpinnasta vaijeria pitkin "
            "ylös ja kohti tornin akselia. Jännitysvoima on painoa hieman pidempi, ja sen pystykomponentti on yhtä suuri kuin paino. "
            "Erillään oranssi kiihtyvyysnuoli a n vasemmalle. Kulma on piirretty paljon suuremmaksi kuin tehtävässä, jotta nuolet erottuvat.")
    # --- the situation picture
    f.tex(150, 22, r"\text{tilannekuva}", "middle", MUTED)
    f.rect(20, 52, 270, 12, SAND_LIGHT, INK, 2)
    f.line(40, 34, 40, 380, MUTED, 1.5, "8 6"); f.tex(48, 370, r"\text{akseli}", "start", MUTED)
    tx, ty = 150, 64
    f.rect(tx - 14, ty, 28, 10, IRON, INK, 1.5)
    L = 200; lx, ly = tx + L * math.sin(th), ty + 10 + L * math.cos(th)
    f.line(tx, ty + 10, lx, ly, INK, 2)
    f.line(tx, ty + 10, tx, ty + 120, MUTED, 1.5, "5 5")
    f.tex(tx + 14, ty + 96, r"\theta", "middle")
    c, s = math.cos(th), math.sin(th)
    w, h = 56, 36                                                 # the load, tilted with its rope
    pts = [(-w / 2, 0), (w / 2, 0), (w / 2, h), (-w / 2, h)]
    poly = [(lx + px * c + py * s, ly - px * s + py * c) for px, py in pts]
    f.path("M" + " L".join(f"{n(a)},{n(b)}" for a, b in poly) + " Z", HEAT_LIGHT, INK, 2.5)
    FBD(f, 1).motion(r"\overline{a}_\text{n}", (-1, 0), (200, 330), 64, kind="acceleration", lab=(-10, -22))
    f.line(300, 20, 300, 390, RULE, 1.5, "6 6")
    # --- the force diagram
    f.tex(450, 22, r"\text{voimakuvio}", "middle", MUTED)
    cx, cy, bw, bh = 450, 236, 60, 44
    top = (cx - bh / 2 * s, cy - bh / 2 * c)                      # the middle of the top face, where the rope pulls
    sc = 120 / G
    d = FBD(f, sc, body=(cx, cy, bw, bh, 20), m=m, a=(-an, 0))
    d.force("G", (0, -G), (cx, cy), "gravity", lab=(24, -4))
    d.force("S", (-m * an, G), top, "tension", rope=(-s, c), lab=(-22, 0))
    d.draw()
    f.line(top[0], top[1], top[0], top[1] - 118, MUTED, 1.5, "5 5")
    d.motion(r"\overline{a}_\text{n}", (-1, 0), (575, 120), 60, lab=(-4, -22))
    ox, oy, AL = 560, 350, 40                                     # axes: x towards the tower's axis, y up
    f.arrow(ox, oy, ox - AL, oy, MUTED, 2, 10); f.arrow(ox, oy, ox, oy - AL, MUTED, 2, 10)
    f.tex(ox - AL - 14, oy, "x", "middle", MUTED); f.tex(ox, oy - AL - 14, "y", "middle", MUTED)
    return f.svg()


def moons_graph():
    """fy5-s2 a: v² against 1/r for the five moons, a line through the origin and the point its slope is read from."""
    xs = [1e9 / r for _, r, _ in MOONS]
    ys = [(2 * math.pi * r / (T * 86400)) ** 2 / 1e8 for _, r, T in MOONS]
    f = Fig("fy5-s2-graph", 420, "Kuvaaja: kuiden ratanopeuden neliö v toiseen radan säteen käänteisarvon 1 per r funktiona. Viisi mustaa "
            "pistettä: Kallisto (0,53; 0,67), Ganymedes (0,93; 1,18), Europa (1,49; 1,89), Io (2,37; 3,01) ja Amalthea (5,51; 7,01), "
            "vaaka-akselilla yksikkönä 10 potenssiin miinus 9 per metri ja pystyakselilla 10 potenssiin 8 neliömetriä per sekunnin "
            "neliö. Pisteisiin on sovitettu origon kautta kulkeva suora, jolta on merkitty piste (5,0; 6,35). Suoran kulmakerroin on "
            "1,27 kertaa 10 potenssiin 17 kuutiometriä per sekunnin neliö.")
    ax = Axes(f, (90, 370), (390, 60), x=(0, 6), y=(0, 8), xticks=[0, 1, 2, 3, 4, 5, 6], yticks=[0, 1, 2, 3, 4, 5, 6, 7, 8],
              xlabel=r"1/r\ (10^{-9}\,\text{m}^{-1})", ylabel=r"v^2\ (10^{8}\,\text{m}^2/\text{s}^2)",
              yfmt=lambda v: str(v) if v % 2 == 0 else "")
    ax.line([(0, 0), (6, 6 * 1.27)], INK, 3)
    for (name, _, _), x, y in zip(MOONS, xs, ys):
        ax.point(x, y)
    for (name, _, _), x, y in zip(MOONS, xs, ys):
        if name in ("Amalthea", "Io", "Europa"):
            f.tex(ax.X(x) + 14, ax.Y(y) + 18, rf"\text{{{name}}}", "start", MUTED)
    ax.guide(5.0, 6.35)
    f.circle(ax.X(5.0), ax.Y(6.35), 8, "none", HOT, 2.5)
    f.tex(ax.X(5.0) - 16, ax.Y(6.35) - 22, r"(5{,}0;\ 6{,}35)", "end", INK, bg=True)
    return f.svg()


def spring_graph():
    """fy5-s3 a: T² against m, the fitted line (not forced through the origin), extended dashed to the T² axis, and the two
    points of the line its slope is read from."""
    T2 = [(t / 10) ** 2 for t in T10]
    k, b = _fit(MS, T2)
    f = Fig("fy5-s3-graph", 420, "Kuvaaja: jaksonajan neliö T toiseen punnuksen massan m funktiona. Kuusi mustaa pistettä massoilla 0,100–0,350 kg; "
            "T toiseen kasvaa arvosta 0,225 arvoon 0,724 sekunnin neliötä. Pisteisiin on sovitettu suora, joka kulkee pisteiden "
            "lomitse, ja sitä on jatkettu katkoviivana pystyakselille, jonka se leikkaa noin kohdassa 0,028 sekunnin neliötä origon "
            "yläpuolella. Suoralta on merkitty pisteet (0,100 kg; 0,226 s²) ja (0,350 kg; 0,722 s²).")
    ax = Axes(f, (96, 370), (480, 60), x=(0, 0.40), y=(0, 0.8), xticks=[0, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40],
              yticks=[0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8], xlabel=r"m\ (\text{kg})", ylabel=r"T^2\ (\text{s}^2)",
              xfmt=lambda v: ("0{,}" + f"{round(v * 10):d}") if round(v * 100) % 10 == 0 else "",
              yfmt=lambda v: ("0{,}" + f"{round(v * 10):d}") if round(v * 10) % 2 == 0 else "")
    ax.line([(0.07, b + 0.07 * k), (0.38, b + 0.38 * k)], INK, 3)
    ax.line([(0, b), (0.07, b + 0.07 * k)], INK, 3, dash="8 6")
    for m, t2 in zip(MS, T2): ax.point(m, t2)
    for m, t2 in [(0.100, 0.226), (0.350, 0.722)]:
        f.circle(ax.X(m), ax.Y(t2), 8, "none", HOT, 2.5)
    f.tex(ax.X(0.100) + 18, ax.Y(0.226) + 24, r"(0{,}100;\ 0{,}226)", "start", INK, bg=True)
    f.tex(ax.X(0.350) - 18, ax.Y(0.722) - 22, r"(0{,}350;\ 0{,}722)", "end", INK, bg=True)
    return f.svg()


def signal():
    """fy5-s4 task figure: the microphone signal of the organ pipe, a 250 Hz fundamental with its second harmonic, so each
    repeat has a high and a low peak 2 ms apart. Five repeats in 20 ms; the high peaks at 1, 5, 9, 13 and 17 ms."""
    T = 4.0
    p = lambda t: math.sin(2 * math.pi * t / T) - 0.7 * math.cos(4 * math.pi * t / T)
    f = Fig("fy5-s4-signal", 330, "Kuvaaja: mikrofonin signaali ajan t funktiona aikavälillä 0–20 ms, pystyakselilla signaalin suuruus ilman "
            "lukuarvoja. Signaali toistuu samanmuotoisena: jokaisessa toistossa on korkea huippu ja sen jälkeen matala huippu. Korkeat "
            "huiput ovat kohdissa 1, 5, 9, 13 ja 17 ms ja matalat huiput kohdissa 3, 7, 11, 15 ja 19 ms. Pystysuorat apuviivat ovat "
            "millisekunnin välein.")
    ax = Axes(f, (60, 290), (500, 50), x=(0, 20), y=(-2, 2), xticks=list(range(21)), yticks=[-2, -1, 0, 1, 2],
              xlabel=r"t\ (\text{ms})", ylabel=r"\text{signaali}", xfmt=lambda v: str(v) if v % 2 == 0 else "", yfmt=lambda v: "",
              origin_label=False)
    f.tex(ax.X(0), 314, "0", "middle")
    f.line(ax.X(0), ax.Y(0), ax.X(20), ax.Y(0), MUTED, 1.5, "6 5")
    ax.curve(p, 0, 20, INK, 3, steps=400)
    return f.svg()


FIGURES = {"fy5-s1-crane": crane, "fy5-s1-fbd": load_fbd, "fy5-s2-graph": moons_graph, "fy5-s3-graph": spring_graph,
           "fy5-s4-signal": signal}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "fy5-s1-crane": "safe: the crane's layout with the symbols of its distances, no numbers (task fy5-s1)",
    "fy5-s1-fbd": "reveals: the model force diagram of task fy5-s1 d (its solution)",
    "fy5-s2-graph": "reveals: the model graph and slope of task fy5-s2 (its solution)",
    "fy5-s3-graph": "reveals: the model graph and slope of task fy5-s3 (its solution)",
    "fy5-s4-signal": "safe: the microphone signal the student reads the period from (task fy5-s4)",
}
