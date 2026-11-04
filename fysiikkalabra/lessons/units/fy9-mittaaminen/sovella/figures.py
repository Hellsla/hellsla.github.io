"""Model graphs of the fy9-mittaaminen Tehtävät (scripts/figlib.py); `python3 scripts/practice.py figures
units/fy9-mittaaminen` writes them into content/fi/units/fy9-mittaaminen/sovella/solutions.md. The data are the
tasks' (answers.py holds the same numbers and computes the fits)."""
from figlib import Fig, Axes, fi, n, INK, MUTED, WHITE, COLD, HOT, HEAT


def _fit(x, y):
    mx, my = sum(x) / len(x), sum(y) / len(y)
    k = sum((a - mx) * (b - my) for a, b in zip(x, y)) / sum((a - mx) ** 2 for a in x)
    return k, my - k * mx


def _extremes(x, y, dy, k_lo, k_hi, step):
    ok = []
    for i in range(int(k_lo / step), int(k_hi / step) + 1):
        k = i * step
        lo = max(b - k * a - d for a, b, d in zip(x, y, dy)); hi = min(b - k * a + d for a, b, d in zip(x, y, dy))
        if lo <= hi: ok.append((k, (lo + hi) / 2))
    return ok[0], ok[-1]


# s3 (answers.py): the total mass of the cylinder and the liquid; the row 60 ml was written down from memory
V3 = [20, 30, 40, 50, 60, 70, 80, 90, 100]
m3 = [137.6, 145.7, 155.7, 163.9, 183.4, 183.0, 191.8, 202.0, 210.3]
KEEP3 = [(v, m) for v, m in zip(V3, m3) if v != 60]
DV3 = 1.0
# s5: the toy car on video; the point at 1,5 s was clicked on the wrong frame
t5 = [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0]
x5 = [0.35, 0.61, 0.83, 1.32, 1.30, 1.57, 1.78]
DX5 = 0.03
# s6: the syringe; V on the syringe scale, p from the sensor
V6 = [12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
p6 = [189.1, 164.5, 146.6, 131.9, 119.2, 109.6, 101.2, 93.5, 87.6, 81.8]


def pf(v, d):
    """A number for a figure description (plain text, not LaTeX): decimal comma and a true minus."""
    return f"{v:.{d}f}".replace(".", ",").replace("-", "−")


def _axes3(f):
    return Axes(f, (96, 384), (466, 64), x=(0, 110), y=(100, 220), xticks=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110],
                yticks=[110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220],
                xlabel=r"V\ (\text{ml})", ylabel=r"m\ (\text{g})", origin_label=False,
                xfmt=lambda v: fi(v) if v % 20 == 0 else "", yfmt=lambda v: fi(v) if v % 20 == 0 else "")


def _bars3(f, ax, k):
    for v, m in zip(V3, m3):
        if v == 60: continue
        y = ax.Y(m)
        f.line(ax.X(v - DV3), y, ax.X(v + DV3), y, COLD, 2.5)
        ax.point(v, m, COLD)
    f.circle(ax.X(60), ax.Y(183.4), 6.5, WHITE, HOT, 2.5)            # the doubtful row, drawn hollow


def s3_points():
    f = Fig("fy9m-s3-pisteet", 440, "Kuvaaja: mittalasin ja nesteen yhteismassa m grammoina nesteen tilavuuden V funktiona millilitroina. "
            "Vaaka-akseli 0–110 ml ja pystyakseli 100–220 g, jonka alkukohta on merkitty. Kahdeksan sinistä pistettä asettuu nousevaan "
            "jonoon tilavuuksilla 20–100 ml, ja jokaisella on vaakasuora epävarmuusjana ±1 ml. Rivin 60 ml piste (60 ml; 183,4 g) on "
            "piirretty ontoksi punaiseksi ympyräksi: se on selvästi muiden yläpuolella, lähes samalla korkeudella kuin piste 70 ml.", size=30)
    ax = _axes3(f)
    _bars3(f, ax, None)
    f.tex(ax.X(60) - 14, ax.Y(183.4) - 10, r"60\,\text{ml?}", "end", HOT)
    f.tex(ax.X(4), ax.Y(109), r"\text{akseli alkaa } 100\,\text{g}", "start", INK)
    return f.svg()


def s3_fit():
    k, b = _fit([v for v, _ in KEEP3], [m for _, m in KEEP3])
    (klo, blo), (khi, bhi) = _extremes([v for v, _ in KEEP3], [m for _, m in KEEP3], [k * DV3] * len(KEEP3), 0.85, 1.0, 0.0001)
    f = Fig("fy9m-s3-sovitus", 440, "Kuvaaja: sama aineisto kuin edellä. Kahdeksan luotettavan pisteen lomaan on sovitettu "
            f"yksi suora, jota on jatkettu katkoviivana pystyakselille asti; se leikkaa akselin kohdassa noin 118,6 g, joka on tyhjän "
            "mittalasin massa. Suoralta luetut kaukana toisistaan olevat pisteet (20 ml; 137,0 g) ja (100 ml; 210,5 g) on ympyröity, joten "
            f"kulmakerroin on 0,919 g/ml. Harmaat katkoviivat ovat jyrkin ja loivin suora, joiden kulmakertoimet ovat {pf(khi, 3)} ja "
            f"{pf(klo, 3)} g/ml. Onton pisteen 60 ml suora ohittaa noin 10 g:n päästä.", size=30)
    ax = _axes3(f)
    ax.line([(12, blo + 12 * klo), (106, blo + 106 * klo)], MUTED, 2, dash="8 6")
    ax.line([(12, bhi + 12 * khi), (106, bhi + 106 * khi)], MUTED, 2, dash="8 6")
    ax.line([(0, b), (15, b + 15 * k)], INK, 2.5, dash="9 6")
    ax.line([(15, b + 15 * k), (106, b + 106 * k)], INK, 3)
    _bars3(f, ax, k)
    for v, m in [(20, 137.0), (100, 210.5)]:
        f.circle(ax.X(v), ax.Y(m), 12, "none", INK, 1.5)
    f.circle(ax.X(0), ax.Y(b), 9, "none", INK, 2)
    f.tex(ax.X(4), ax.Y(b) + 30, r"m_0 \approx 118{,}6\,\text{g}", "start")
    f.tex(ax.X(56), ax.Y(206), r"k \approx 0{,}919\,\tfrac{\text{g}}{\text{ml}}", "end")
    return f.svg()


def s5_graph():
    keep = [(t, x) for t, x in zip(t5, x5) if t != 1.5]
    k, b = _fit([t for t, _ in keep], [x for _, x in keep])
    f = Fig("fy9m-s5-kuvaaja", 410, "Kuvaaja: leluauton paikka x metreinä ajan t funktiona sekunteina, 0–3,0 s. Kuusi sinistä pistettä "
            "on lähellä yhtä nousevaa suoraa; paikan epävarmuus ±0,03 m on pisteen kokoa pienempi, joten epävarmuusjanat jäävät pisteiden sisään. Piste (1,5 s; 1,32 m) on piirretty ontoksi punaiseksi "
            f"ympyräksi: se on noin 0,25 m suoran yläpuolella. Suora leikkaa pystyakselin kohdassa {pf(b, 2)} m, ei origossa, ja sen "
            f"kulmakerroin on {pf(k, 2)} m/s. Suoralta luetut pisteet (0 s; 0,36 m) ja (3,0 s; 1,79 m) on ympyröity.", size=30)
    ax = Axes(f, (84, 360), (480, 60), x=(0, 3.4), y=(0, 2.0), xticks=[0.5, 1.0, 1.5, 2.0, 2.5, 3.0], yticks=[0.6, 1.2, 1.8],
              xlabel=r"t\ (\text{s})", ylabel=r"x\ (\text{m})")
    ax.line([(0, b), (3.3, b + 3.3 * k)], INK, 3)
    for t, x in keep:
        f.line(ax.X(t), ax.Y(x - DX5), ax.X(t), ax.Y(x + DX5), COLD, 2.5)
        ax.point(t, x, COLD)
    f.circle(ax.X(1.5), ax.Y(1.32), 6.5, WHITE, HOT, 2.5)
    f.tex(ax.X(1.5) - 14, ax.Y(1.32) - 14, r"\text{tarkista}", "end", HOT)
    for t, x in [(0, 0.36), (3.0, 1.79)]:
        f.circle(ax.X(t), ax.Y(x), 12, "none", INK, 1.5)
    f.tex(ax.X(1.5), ax.Y(0.45), r"v = k \approx 0{,}48\,\tfrac{\text{m}}{\text{s}}", "start")
    return f.svg()


def s6_graph():
    inv = [1000 / p for p in p6]
    k, b = _fit(inv, V6)
    f = Fig("fy9m-s6-kuvaaja", 440, "Kuvaaja: ruiskun asteikon tilavuus V millilitroina paineen käänteisluvun 1/p funktiona yksikössä 1/MPa. "
            "Kymmenen sinistä pistettä välillä 5,3–12,2 1/MPa ovat yhdellä nousevalla suoralla. Suoraa on jatkettu katkoviivana "
            f"pystyakselille, jonka se leikkaa negatiivisella puolella kohdassa {pf(b, 1)} ml. Kulmakerroin on {pf(k, 2)} MPa · ml. "
            "Vaaka-akseli on piirretty kohtaan V = 0.", size=30)
    ax = Axes(f, (84, 400), (420, 60), x=(0, 14), y=(-8, 36), xticks=[2, 4, 6, 8, 10, 12, 14], yticks=[-8, -4, 0, 4, 8, 12, 16, 20, 24, 28, 32, 36],
              xlabel=r"\tfrac{1}{p}\ (\tfrac{1}{\text{MPa}})", ylabel=r"V\ (\text{ml})", x_at=0, origin_label=False,
              xfmt=lambda v: fi(v) if v % 4 == 0 else "", yfmt=lambda v: ("-" if v < 0 else "") + fi(abs(v)) if v % 8 == 0 and v != 0 else "")
    ax.line([(0, b), (4.6, b + 4.6 * k)], INK, 2.5, dash="9 6")
    ax.line([(4.6, b + 4.6 * k), (13.4, b + 13.4 * k)], INK, 3)
    for x, y in zip(inv, V6): ax.point(x, y, COLD)
    f.circle(ax.X(0), ax.Y(b), 9, "none", INK, 2)
    f.tex(ax.X(0) + 20, ax.Y(-5.2), r"-V_0 \approx " + fi(round(b, 1)) + r"\,\text{ml}", "start")
    f.tex(ax.X(0.5), ax.Y(31), r"k \approx " + fi(round(k, 2)) + r"\,\text{MPa} \cdot \text{ml}", "start")
    return f.svg()


FIGURES = {"s3-pisteet": s3_points, "s3-sovitus": s3_fit, "s5-kuvaaja": s5_graph, "s6-kuvaaja": s6_graph}
