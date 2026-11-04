"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy7-9` writes them into lesson.md.
FY7 colours (course brief): electric field #8a5f22, magnetic field #2b8a3e, current #7048e8. The visible band is drawn
in spectral colours (they are the physics here, and each band is also labelled). The black-body curves are Planck's
law with the exact SI constants, the same as the simulation."""
import math
from figlib import (Fig, Axes, fi, n, INK, MUTED, WHITE, RULE, RULE_LIGHT, HOT, HOT_LIGHT, HEAT, HEAT_LIGHT, GOOD,
                    GOOD_LIGHT, IRON, COPPER, ALUMINIUM, METAL_EDGE, SAND_LIGHT, SAND, SAND_DARK, GRAIN, COLD_LIGHT,
                    PAPER)
import herolib as H

EFIELD, BFIELD, CURRENT = "#8a5f22", GOOD, "#7048e8"
SPECTRAL = [(0, "#c81e1e"), (0.25, "#f08a1a"), (0.4, "#e6e01a"), (0.55, "#2fbf3f"), (0.7, "#1aa0e6"), (0.88, "#3b3bf0"),
            (1, "#7a1fd1")]                                   # 750 nm (red) ... 380 nm (violet)
h_, c_, k_ = 6.62607015e-34, 2.99792458e8, 1.380649e-23


def planck(lam_nm, T):
    """The black body's spectral exitance M_λ in MW/(m²·µm)."""
    lam = lam_nm * 1e-9
    x = h_ * c_ / (lam * k_ * T)
    return 0.0 if x > 700 else math.pi * 2 * h_ * c_ ** 2 / lam ** 5 / math.expm1(x) / 1e12


def spectral_grad(f, gid, x1, x2, reverse=False):
    stops = SPECTRAL[::-1] if reverse else SPECTRAL
    s = "".join(f'<stop offset="{(1 - o) if reverse else o:g}" stop-color="{col}"/>' for o, col in stops)
    f.defs_add(f'<linearGradient id="{gid}" gradientUnits="userSpaceOnUse" x1="{n(x1)}" y1="0" x2="{n(x2)}" y2="0">{s}</linearGradient>')
    return f"url(#{gid})"


def wave():
    f = Fig("fy79-wave", 340, "Periaatekuva sähkömagneettisesta aallosta yhdellä hetkellä, ei mittakaavassa. Aalto etenee "
            "vasemmalta oikealle vaakasuoraa akselia pitkin. Ruskea sähkökenttä E värähtelee pystysuunnassa ja vihreä "
            "magneettikenttä B vinosti piirretyssä vaakatasossa, kohtisuoraan sekä sähkökenttää että etenemissuuntaa "
            "vastaan. Kentät ovat samassa vaiheessa: ne ovat suurimmillaan ja nollassa samoissa kohdissa. Kahden "
            "peräkkäisen sähkökentän huipun välinen etäisyys on aallonpituus lambda. Aalto etenee nopeudella c.")
    x0, y0, lam, A, Bk = 70, 175, 210, 100, 80
    pts = [x0 + 420 * i / 168 for i in range(169)]
    s = lambda x: math.sin(2 * math.pi * (x - x0) / lam)
    bx, by = -0.62, 0.48                                     # the oblique direction of the B plane (drawn in perspective)
    # field vectors at regular steps: thin lines from the axis to the curves
    for i in range(1, 24):
        x = x0 + 420 * i / 24
        if abs(s(x)) > 0.12:
            f.line(x, y0, x, y0 - A * s(x), EFIELD, 1.5)
            f.line(x, y0, x + bx * Bk * s(x), y0 + by * Bk * s(x), BFIELD, 1.5)
    f.path("M" + " L".join(f"{n(x + bx * Bk * s(x))},{n(y0 + by * Bk * s(x))}" for x in pts), stroke=BFIELD, w=3)
    f.line(x0 - 20, y0, 520, y0, INK, 2)
    f.path("M" + " L".join(f"{n(x)},{n(y0 - A * s(x))}" for x in pts), stroke=EFIELD, w=3)
    # two labelled field vectors at the first crest
    xc = x0 + lam / 4
    f.arrow(xc, y0, xc, y0 - A, EFIELD, 3, 14)
    f.arrow(xc, y0, xc + bx * Bk, y0 + by * Bk, BFIELD, 3, 14)
    f.tex(xc + 12, y0 - A + 6, r"\overline{E}", "start", EFIELD)
    f.tex(xc + bx * Bk - 6, y0 + by * Bk + 24, r"\overline{B}", "end", BFIELD)
    # the wavelength between two E crests
    ya = y0 - A - 26
    f.line(xc, ya, xc + lam, ya, INK, 2); f.line(xc, ya - 8, xc, ya + 8, INK, 2); f.line(xc + lam, ya - 8, xc + lam, ya + 8, INK, 2)
    f.tex(xc + lam / 2, ya - 20, r"\lambda", "middle", w=34)
    # direction of travel
    f.arrow(512, y0, 576, y0, INK, 3, 16)
    f.tex(552, y0 - 26, r"c", "middle", w=30)
    return f.svg()


def antenna():
    f = Fig("fy79-antenna", 340, "Periaatekuva, ei mittakaavassa: pystysuora sauva-antenni, jonka kaksi metallisauvaa on "
            "kytketty keskeltä vaihtojännitelähteeseen. Violetti nuoli sauvojen vieressä näyttää, että virta kulkee "
            "hetkellä ylöspäin; puolen jaksonajan kuluttua se kulkee alaspäin. Antennista lähtee oikealle kaaria, jotka "
            "kuvaavat etenevän aallon harjoja. Ruskeat nuolet vaaka-akselilla näyttävät sähkökentän, joka on antennin "
            "suuntainen ja vaihtaa suuntaa puolen aallonpituuden välein. Kahden samansuuntaisen harjan välinen "
            "etäisyys on aallonpituus lambda.")
    cx, cy, lam = 110, 170, 210
    # wave crests: arcs around the antenna every half wavelength, kept inside the figure
    for k in range(1, 5):
        r = lam / 2 * k
        a = min(math.radians(68), math.asin(min(1, 138 / r)))
        x1, y1 = cx + r * math.cos(a), cy - r * math.sin(a)
        x2, y2 = cx + r * math.cos(a), cy + r * math.sin(a)
        f.path(f"M{n(x1)},{n(y1)} A{n(r)},{n(r)} 0 0 1 {n(x2)},{n(y2)}", stroke=RULE, w=2.5, extra='stroke-dasharray="8 6"')
    # the electric field on the axis: along the antenna, turning every half wavelength
    for k in range(1, 5):
        x, up = cx + lam / 2 * k, (k % 2 == 1)
        f.arrow(x, cy, x, cy - 46 if up else cy + 46, EFIELD, 3, 13)
    f.line(cx + 14, cy, 560, cy, MUTED, 1.5, "4 5")
    f.tex(cx + lam / 2 + 10, cy - 44, r"\overline{E}", "start", EFIELD)
    # the antenna: two rods fed at the middle by an AC source
    f.rect(cx - 6, 52, 12, 100, ALUMINIUM, INK, 2.5, 3)
    f.rect(cx - 6, 188, 12, 100, ALUMINIUM, INK, 2.5, 3)
    f.path(f"M{cx - 6},150 H48 V148", stroke=INK, w=2.5)
    f.path(f"M{cx - 6},190 H48 V192", stroke=INK, w=2.5)
    f.circle(48, cy, 22, WHITE, INK, 2.5)
    f.path(f"M{48 - 13},{cy} C{48 - 6.5},{cy - 15} 48,{cy - 15} 48,{cy} C48,{cy + 15} {48 + 6.5},{cy + 15} {48 + 13},{cy}", stroke=INK, w=2.5)
    f.arrow(cx + 22, 140, cx + 22, 66, CURRENT, 3, 13)
    f.arrow(cx + 22, 274, cx + 22, 200, CURRENT, 3, 13)
    f.tex(cx + 36, 104, r"I", "start", CURRENT, w=24)
    f.tex(cx + 14, 30, r"\text{antenni}", "start")
    # the wavelength between two crests with the field in the same direction
    yb = 276
    xa, xb = cx + lam / 2, cx + lam / 2 * 3
    f.line(xa, yb, xb, yb, INK, 2); f.line(xa, yb - 8, xa, yb + 8, INK, 2); f.line(xb, yb - 8, xb, yb + 8, INK, 2)
    f.tex((xa + xb) / 2, yb + 24, r"\lambda", "middle", w=34)
    f.arrow(486, 52, 566, 52, INK, 3, 16)
    f.tex(470, 52, r"c", "end", w=30)
    return f.svg()


def spectrum():
    f = Fig("fy79-spectrum", 380, "Kaavakuva sähkömagneettisesta spektristä. Vaakasuora palkki, jonka aallonpituusasteikko on "
            "logaritminen: jokainen asteikkoväli on tuhatkertainen aallonpituus. Vasemmalta oikealle radioaallot "
            "(yli 1 m), mikroaallot (1 mm–1 m), infrapunasäteily (750 nm–1 mm), kapea näkyvän valon kaista, "
            "ultraviolettisäteily (10–380 nm), röntgensäteily (0,01–10 nm) ja gammasäteily (alle noin 0,01 nm). "
            "Näkyvän valon kaista on suurennettu palkin alle: punainen noin 750 nm:n kohdalla vasemmalla ja violetti "
            "noin 380 nm:n kohdalla oikealla.")
    xa, xb, y1, y2 = 40, 560, 136, 166
    X = lambda lam: xa + (3 - math.log10(lam)) / 16 * (xb - xa)      # λ in metres, 10³ m … 10⁻¹³ m
    bands = [(1e3, 1, GOOD_LIGHT), (1, 1e-3, SAND_LIGHT), (1e-3, 750e-9, HOT_LIGHT), (380e-9, 10e-9, COLD_LIGHT),
             (10e-9, 1e-11, ALUMINIUM), (1e-11, 1e-13, METAL_EDGE)]
    for a, b, col in bands:
        f.rect(X(a), y1, X(b) - X(a), y2 - y1, col)
    f.rect(X(750e-9), y1, X(380e-9) - X(750e-9), y2 - y1, spectral_grad(f, "fy79-band", X(750e-9), X(380e-9)))
    f.rect(xa, y1, xb - xa, y2 - y1, "none", INK, 2.5, 3)
    for a, b, col in bands[:-1]:
        f.line(X(b), y1, X(b), y2, INK, 1.5)
    # region names: one row right above the bar, a higher row with leaders
    upper = [(r"\text{radioaallot}", math.sqrt(1e3 * 1)), (r"\text{infrapuna}", math.sqrt(1e-3 * 750e-9)),
             (r"\text{UV}", math.sqrt(380e-9 * 10e-9)), (r"\text{gamma}", math.sqrt(1e-11 * 1e-13))]
    lower = [(r"\text{mikroaallot}", math.sqrt(1 * 1e-3)), (r"\text{röntgen}", math.sqrt(10e-9 * 1e-11))]
    for t, lam in upper:
        x = X(lam)
        f.line(x, 78, x, y1, MUTED, 1.5)
        f.tex(min(max(x, 92), 520), 62, t, "middle")
    for t, lam in lower:
        f.tex(X(lam), 112, t, "middle")
    # the wavelength scale under the bar
    for e, t in ((3, r"10^{3}"), (0, r"1"), (-3, r"10^{-3}"), (-6, r"10^{-6}"), (-9, r"10^{-9}"), (-12, r"10^{-12}")):
        x = X(10.0 ** e)
        f.line(x, y2, x, y2 + 8, INK, 2)
        f.tex(x, y2 + 26, t, "middle")
    f.tex(xb, 226, r"\lambda\ (\text{m})", "end")
    # the visible band enlarged
    ia, ib, iy1, iy2 = 150, 530, 262, 292
    f.path(f"M{n(X(750e-9))},{y2} L{ia},{iy1} M{n(X(380e-9))},{y2} L{ib},{iy1}", stroke=MUTED, w=1.5, extra='stroke-dasharray="5 4"')
    f.rect(ia, iy1, ib - ia, iy2 - iy1, spectral_grad(f, "fy79-vis", ia, ib), INK, 2, 3)
    XI = lambda nm: ia + (750 - nm) / 370 * (ib - ia)
    for nm in (700, 600, 500, 400):
        f.line(XI(nm), iy2, XI(nm), iy2 + 8, INK, 2)
        f.tex(XI(nm), iy2 + 26, rf"{nm}\,\text{{nm}}", "middle")
    f.tex((ia + ib) / 2, 352, r"\text{näkyvä valo}", "middle")
    return f.svg()


def curves():
    f = Fig("fy79-curves", 340, "Kuvaaja mittakaavassa: mustan kappaleen säteilyn spektri kolmessa lämpötilassa. Vaaka-"
            "akselilla aallonpituus nanometreinä nollasta 2000:een, pystyakselilla säteilyteho pinta-alaa ja "
            "aallonpituusväliä kohti megawatteina neliömetriä ja mikrometriä kohti. Näkyvän valon alue 380–750 nm on "
            "taustalla värikaistana. Musta yhtenäinen käyrä on 6000 K, oranssi katkoviiva 5000 K ja punainen "
            "pisteviiva 4000 K. Huiput ovat aallonpituuksilla 483 nm, 580 nm ja 724 nm, ja niiden korkeudet ovat noin "
            "100, 40 ja 13. Mitä kuumempi kappale, sitä korkeampi käyrä ja sitä lyhyemmällä aallonpituudella huippu on.")
    ax = Axes(f, (100, 290), (472, 62), x=(0, 2000), y=(0, 110), xticks=[250 * k for k in range(1, 9)],
              yticks=[20 * k for k in range(1, 6)], xlabel=r"\lambda\ (\text{nm})",
              ylabel=r"M_\lambda\ (\text{MW}/(\text{m}^2 \cdot \mu\text{m}))", xfmt=lambda v: fi(v) if v % 500 == 0 else "")
    # the visible band behind the curves and as a strip on the axis
    xv1, xv2 = ax.X(380), ax.X(750)
    g = spectral_grad(f, "fy79-cband", xv2, xv1)
    f.rect(xv1, 62, xv2 - xv1, 228, g, extra='fill-opacity="0.2"')
    f.rect(xv1, 280, xv2 - xv1, 9, g)
    styles = [(6000, INK, None), (5000, HEAT, "10 6"), (4000, HOT, "3 5")]
    peaks = []
    for T, col, dash in styles:
        ax.curve(lambda l, T=T: planck(max(l, 1), T), 150, 2000, col, 3, steps=200, dash=dash)
        lm = 2.897771955e-3 / T * 1e9
        peaks.append((lm, planck(lm, T)))
    for (lm, v), (T, col, dash) in zip(peaks, styles):
        f.line(ax.X(lm), ax.Y(v), ax.X(lm), 290, MUTED, 1.5, "6 5")
        ax.point(lm, v, col)
    # legend in the empty upper right, line style and colour together
    for i, (T, col, dash) in enumerate(styles):
        y = ax.Y(100 - 15 * i)
        f.line(330, y, 382, y, col, 3, dash)
        f.tex(392, y, rf"{T}\,\text{{K}}", "start", col)
    return f.svg()


def spectrum_task():
    """Task figure: one black-body curve (T = 2415 K, so that its peak sits on the gridline 1,2 µm), no peak marked."""
    f = Fig("fy79-spectrum-task", 340, "Kuvaaja mittakaavassa: hehkuvan kappaleen säteilyn spektri. Vaaka-akselilla "
            "aallonpituus mikrometreinä nollasta neljään, ruudukon väli 0,2 µm; pystyakselilla säteilyteho pinta-alaa ja "
            "aallonpituusväliä kohti megawatteina neliömetriä ja mikrometriä kohti, ruudukon väli 0,2. Käyrä nousee "
            "noin 0,4 µm:n kohdalta jyrkästi, saavuttaa huippunsa, jonka korkeus on noin 1,06, ja laskee sitten "
            "loivasti. Näkyvän valon alue 0,38–0,75 µm on merkitty värikaistalla vaaka-akselin viereen.")
    ax = Axes(f, (100, 290), (472, 62), x=(0, 4), y=(0, 1.2), xticks=[0.2 * k for k in range(1, 21)],
              yticks=[0.2 * k for k in range(1, 7)], xlabel=r"\lambda\ (\mu\text{m})",
              ylabel=r"M_\lambda\ (\text{MW}/(\text{m}^2 \cdot \mu\text{m}))",
              xfmt=lambda v: fi(round(v)) if abs(v - round(v)) < 1e-9 else "",
              yfmt=lambda v: fi(round(v, 1)) if abs(v * 5 - round(v * 5)) < 1e-9 and round(v * 10) % 4 == 0 else "")
    xv1, xv2 = ax.X(0.38), ax.X(0.75)
    f.rect(xv1, 280, xv2 - xv1, 9, spectral_grad(f, "fy79-tband", xv2, xv1))
    ax.curve(lambda l: planck(max(l, 0.05) * 1e3, 2415), 0.2, 4, INK, 3, steps=240)
    return f.svg()


def hero():
    """The opening illustration: a forge, an iron rod glowing white, yellow, orange and red from its hot end to the
    dark iron at the cold end on the anvil."""
    f = H.hero("fy79-hero", "Kuvitus: hämärässä pajassa ahjon hiillos hehkuu. Ahjosta lähtee pitkä rautatanko kohti "
               "oikealla olevaa alasinta. Tangon kuuma pää hiilloksessa on lähes valkoinen, ja siitä poispäin tanko "
               "hehkuu keltaisena, oranssina ja punaisena, kunnes kylmä pää alasimen päällä on tumman harmaa. Tangon "
               "kuuman osan yllä väreilee lämpö.")
    f.rect(0, 0, 1200, 600, H.grad(f, "fy79h-wall", INK, IRON, y1=0, y2=470))
    for y in range(40, 440, 50):                               # stone wall courses
        f.line(0, y, 1200, y, METAL_EDGE, 1.5)
        off = 0 if (y // 50) % 2 else 60
        for x in range(off, 1200, 120):
            f.line(x, y, x, y + 50, METAL_EDGE, 1.5)
    f.rect(0, 440, 1200, 160, H.grad(f, "fy79h-floor", SAND_DARK, SAND))
    # the glow of the hearth and the hot rod on the wall
    f.add(f'<ellipse cx="540" cy="300" rx="380" ry="230" fill="{H.glow(f, "fy79h-halo", HEAT_LIGHT, HEAT)}" fill-opacity="0.5"/>')
    # hood and chimney
    f.path("M190,210 L240,90 H440 L490,210 Z", IRON, INK, 3)
    f.rect(300, 0, 80, 92, IRON, INK, 3)
    # the brick hearth
    f.rect(180, 300, 320, 170, COPPER, INK, 3, 4)
    for y in (342, 384, 426):
        f.line(180, y, 500, y, GRAIN, 2)
    for i, y in enumerate((300, 342, 384, 426)):
        for x in range(220 + (i % 2) * 40, 500, 80):
            f.line(x, y, x, y + 42, GRAIN, 2)
    # the iron rod: white-hot where it leaves the fire, then yellow, orange, red and dark iron towards the anvil
    f.add(f'<ellipse cx="620" cy="292" rx="190" ry="70" fill="{H.glow(f, "fy79h-rodglow", HEAT_LIGHT, HEAT)}" fill-opacity="0.7"/>')
    f.defs_add('<linearGradient id="fy79h-rodg" gradientUnits="userSpaceOnUse" x1="470" y1="0" x2="1050" y2="0">'
               f'<stop offset="0" stop-color="{WHITE}"/><stop offset="0.14" stop-color="{HEAT_LIGHT}"/>'
               f'<stop offset="0.3" stop-color="{HEAT}"/><stop offset="0.46" stop-color="{HOT}"/>'
               f'<stop offset="0.62" stop-color="{IRON}"/><stop offset="1" stop-color="{IRON}"/></linearGradient>')
    f.path("M330,268 L1050,312 L1048,340 L328,296 Z", "url(#fy79h-rodg)", INK, 2.5)
    # fire bed and coals over the rod's tip
    f.path("M190,300 Q340,250 490,300 Z", HEAT, INK, 3)
    for k in range(16):
        x = 204 + 18 * k + 5 * H.rnd(k, 3)
        y = 297 - 14 * math.sin(math.pi * (x - 190) / 300) + 4 * H.rnd(k + 20, 3)
        col = [INK, IRON, HOT][k % 3]
        f.circle(x, y, 9 + 4 * H.rnd(k + 40, 3), col, INK, 1.5)
    f.add(f'<ellipse cx="340" cy="286" rx="140" ry="32" fill="{H.glow(f, "fy79h-coal", HEAT_LIGHT, HEAT)}" fill-opacity="0.85"/>')
    for k in range(7):                                         # sparks
        f.circle(280 + 160 * H.rnd(k, 9), 200 + 60 * H.rnd(k + 9, 9), 3, HEAT_LIGHT)
    H.shimmer(f, [560, 620, 680, 740], 262, length=90, colour=HEAT_LIGHT)
    # the anvil with a hammer
    f.path("M900,340 H1120 Q1120,362 1090,368 L1060,372 V410 L1090,470 H930 L960,410 V372 L930,366 Q880,356 860,340 Z", IRON, INK, 3)
    f.rect(1112, 326, 76, 12, H.grad(f, "fy79h-handle", SAND, GRAIN), INK, 2.5, 6)
    f.rect(1074, 310, 42, 30, IRON, INK, 3, 4)
    return f.svg()


FIGURES = {"hero": hero, "wave": wave, "antenna": antenna, "spectrum": spectrum, "curves": curves,
           "spectrum-task": spectrum_task}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "wave": "reveals: E and B are perpendicular to each other and to the direction of travel, in phase",
    "antenna": "reveals: an AC current in an antenna sends out a wave whose field turns every half wavelength",
    "spectrum": "reveals: the order of the EM spectrum's bands and their wavelength limits",
    "curves": "reveals: the peaks of 4000, 5000 and 6000 K curves at 724, 580 and 483 nm; hotter is higher and bluer",
    "spectrum-task": "safe: one black-body curve with its peak on the gridline 1,2 µm, no peak or temperature marked",
}
