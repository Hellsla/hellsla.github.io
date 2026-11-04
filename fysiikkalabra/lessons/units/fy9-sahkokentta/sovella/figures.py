"""Model graphs of the Tehtävät of fy9-sahkokentta (scripts/figlib.py); `python3 scripts/practice.py figures units/fy9-sahkokentta`
writes them into content/fi/units/fy9-sahkokentta/sovella/solutions.md. The data are the same as in answers.py."""
import math
from figlib import Fig, Axes, INK, MUTED, RULE, IRON, HOT_LIGHT, HEAT, COLD, fi, n
from fbd import FBD

# fy9-sahkokentta-s3 (answers.py): invented data, C = eps0 A / d + 22 pF of the leads, A = 0,0400 m^2, noise about 1 %
D = [1.0, 1.5, 2.0, 3.0, 4.0, 5.0, 6.0]                 # mm
C = [375, 260, 199, 140, 109, 93, 82]                   # pF
X = [1 / d for d in D]                                  # 1/mm


def _fit(x, y):
    mx, my = sum(x) / len(x), sum(y) / len(y)
    k = sum((a - mx) * (b - my) for a, b in zip(x, y)) / sum((a - mx) ** 2 for a in x)
    return k, my - k * mx


def capacitance_distance():
    """fy9-sahkokentta-s3 a: the capacitance against the plate distance, the points and the smooth curve of the fitted
    model through them (dashed): it falls steeply at small distances and levels off above zero at large ones."""
    k, b = _fit(X, C)
    f = Fig("fy9sk-s3-cd", 440, "Kuvaaja: kondensaattorin kapasitanssi C pikofaradeina levyjen etäisyyden d funktiona millimetreinä. "
            "Seitsemän mustaa pistettä etäisyyksillä 1,0–6,0 mm, kapasitanssit 375 pF:stä 82 pF:iin. Pisteiden kautta kulkee "
            "katkoviivakäyrä, joka laskee jyrkästi pienillä etäisyyksillä ja loivenee suurilla, mutta ei lähesty nollaa: "
            "kaksinkertainen etäisyys ei puolita kapasitanssia, joten pisteisiin ei sovi suora eikä pelkkä kääntäen verrannollisuus.",
            size=30)
    ax = Axes(f, (110, 380), (450, 76), x=(0, 6.5), y=(0, 400), xticks=[1, 2, 3, 4, 5, 6], yticks=[50 * i for i in range(1, 9)],
              xlabel=r"d\ (\text{mm})", ylabel=r"C\ (\text{pF})",
              xfmt=lambda v: fi(v) if v % 2 == 0 else "", yfmt=lambda v: fi(v) if v % 100 == 0 else "")
    ax.curve(lambda d: k / d + b, 0.92, 6.4, INK, 2.5, dash="8 6")
    for d, c in zip(D, C): ax.point(d, c)
    f.tex(ax.X(3.0), ax.Y(260), r"\text{ei suora}", "start", MUTED)
    return f.svg()


def linear_graph():
    """fy9-sahkokentta-s3 b, c and d: the capacitance against 1/d, the points, the fitted line (solid over the data, dashed
    back to the vertical axis), the two circled line points the slope is read from and the intercept of about 22 pF."""
    k, b = _fit(X, C)
    line = lambda x: k * x + b
    f = Fig("fy9sk-s3-lin", 440, "Kuvaaja: kapasitanssi C pikofaradeina suureen yksi jaettuna d funktiona yksikössä yksi jaettuna "
            "millimetri. Seitsemän mustaa pistettä välillä 0,17–1,00, kapasitanssit 82 pF:stä 375 pF:iin. Pisteisiin on sovitettu "
            "nouseva suora, jota on jatkettu katkoviivana pystyakselille: se leikkaa pystyakselin noin 22 pF:n kohdalla eikä "
            "kulje origon kautta. Suoralta on ympyröity kaksi pistettä, (0,20; 93) ja (1,00; 376), joista luetaan kulmakerroin "
            "noin 354 pF kertaa millimetri.", size=30)
    ax = Axes(f, (110, 380), (400, 76), x=(0, 1.1), y=(0, 400), xticks=[0.1 * i for i in range(1, 11)], yticks=[50 * i for i in range(1, 9)],
              xlabel=r"1/d\ (1/\text{mm})", ylabel=r"C\ (\text{pF})",
              xfmt=lambda v: fi(round(v, 1), 1) if round(v * 10) % 5 == 0 else "", yfmt=lambda v: fi(v) if v % 100 == 0 else "")
    ax.line([(X[-1], line(X[-1])), (X[0], line(X[0]))], INK, 3)
    ax.line([(0, line(0)), (X[-1], line(X[-1]))], INK, 2.5, dash="8 6")
    for x, y in zip(X, C): ax.point(x, y)
    for x, y in ((0.20, 93), (1.00, 376)):
        f.circle(ax.X(x), ax.Y(y), 11, "none", INK, 1.5)
        ax.guide(x, y, COLD)
    f.circle(ax.X(0), ax.Y(line(0)), 7, HEAT, None)
    f.tex(ax.X(0.04), ax.Y(line(0)) - 26, r"22\,\text{pF}", "start", HEAT, bg=True)
    f.tex(ax.X(0.30), ax.Y(330), r"k \approx 354\,\text{pF}\cdot\text{mm}", "start", INK, bg=True)
    return f.svg()


def balls_fbd():
    """fy9-sahkokentta-s1 a: the situation picture (two equal positive balls on threads from one hook, the angle alpha
    from the vertical) and the force diagram of the right ball as a plain rectangle: the weight G down from the centre,
    the thread's tension T along the thread towards the hook and the electric force F_s horizontally away from the other
    ball. The ball is at rest, so the arrows cancel. Drawn at 25 degrees instead of the task's 5,7 so that the arrows can
    be told apart."""
    deg = 25.0
    th = math.radians(deg)
    G = 0.50e-3 * 9.81 * 1000                                    # mN
    Fs = G * math.tan(th)
    f = Fig("fy9-sahkokentta-s1-fbd", 400, "Kaksi kuvaa. Vasemmalla tilannekuva: kaksi samanlaista positiivista palloa riippuu "
            "langoista samasta koukusta, ja langat muodostavat V-kirjaimen. Katkoviiva koukusta suoraan alas ja kulma alfa "
            "langan ja pystysuoran välissä. Oikealla oikeanpuoleisen pallon voimakuvio, pallo suorakulmiona: paino G keskipisteestä "
            "suoraan alas, langan jännitysvoima T yläreunasta lankaa pitkin vinosti ylös vasemmalle kohti koukkua ja sähköinen "
            "voima F s oikeasta reunasta vaakasuoraan oikealle, poispäin toisesta pallosta. Pallo on levossa, joten voimat "
            "kumoavat toisensa: T:n pystyosa on yhtä suuri kuin paino ja vaakaosa yhtä suuri kuin sähköinen voima. Kulma on "
            "piirretty suuremmaksi kuin tehtävässä, jotta nuolet erottuvat.", width=500, size=28)
    # --- the situation picture
    f.tex(115, 22, r"\text{tilannekuva}", "middle", MUTED)
    hx, hy, L = 115, 70, 220
    f.line(hx - 50, hy - 8, hx + 50, hy - 8, IRON, 5, cap="round")
    f.path(f"M{hx},{hy - 8} q0,8 0,8", "none", INK, 3)
    f.line(hx, hy, hx, hy + L + 20, MUTED, 1.5, "6 6")
    for sgn in (-1, 1):
        bx, by = hx + sgn * L * math.sin(th), hy + L * math.cos(th)
        f.line(hx, hy, bx, by, INK, 2)
        f.circle(bx, by, 17, HOT_LIGHT, INK, 2)
        f.line(bx - 8, by, bx + 8, by, INK, 3); f.line(bx, by - 8, bx, by + 8, INK, 3)
    r = 70
    f.path(f"M{hx},{hy + r} A{r},{r} 0 0 0 {n(hx + r * math.sin(th))},{n(hy + r * math.cos(th))}", "none", INK, 2)
    f.tex(hx + 20, hy + r + 22, r"\alpha", "middle", INK)
    f.line(240, 20, 240, 390, RULE, 1.5, "6 6")
    # --- the force diagram of the right ball
    f.tex(256, 22, r"\text{voimakuvio}", "start", MUTED)
    cx, cy, w, h = 370, 235, 56, 56
    s = 24.0                                                     # figure units per millinewton
    d = FBD(f, s, body=(cx, cy, w, h), a_dir=(0, 0))
    d.force("G", (0, -G), (cx, cy), "gravity", lab=(26, -6))
    d.force("T", (-Fs, G), (cx, cy - h / 2), "tension", rope=(-math.sin(th), math.cos(th)), lab=(-22, 8))
    d.force("F_s", (Fs, 0), (cx + w / 2, cy), "electric", tex=r"\overline{F}_\text{s}", lab=(2, -28))
    d.draw()
    tx, ty = cx, cy - h / 2
    f.line(tx, ty, tx, ty - 120, MUTED, 1.5, "6 6")
    r = 56
    f.path(f"M{tx},{n(ty - r)} A{r},{r} 0 0 0 {n(tx - r * math.sin(th))},{n(ty - r * math.cos(th))}", "none", INK, 2)
    f.tex(tx - 14, ty - r - 22, r"\alpha", "middle", INK)
    return f.svg()


FIGURES = {"fy9-sahkokentta-s1-fbd": balls_fbd, "fy9-sahkokentta-s3-cd": capacitance_distance, "fy9-sahkokentta-s3-lin": linear_graph}
