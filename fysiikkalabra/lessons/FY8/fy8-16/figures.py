"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy8-16` writes them into lesson.md.
Spectral lines are drawn in their real colour (FY8 conventions, as in the chapter Spektrit paljastavat atomin
energiatasot), always with a wavelength axis or a label, so colour never carries the meaning alone. A galaxy is a
glowing ellipse; velocity arrows are blue (figure palette). Every plotted value comes from lesson-answers.py (one source);
the binding-energy points come from the chapter Massavaje ja ytimen sidosenergia (its lesson-answers.py)."""
import contextlib, importlib.util, io, math, pathlib
from figlib import (Fig, Axes, fi, n, INK, MUTED, WHITE, RULE, RULE_LIGHT, HEAT, HEAT_LIGHT, HOT, COLD, COLD_LIGHT, IRON,
                    ALUMINIUM, METAL_EDGE, GLASS, PAPER, GOOD)
import herolib as H


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(mod)   # the answers' JSON line is not needed here
    return mod


HERE = pathlib.Path(__file__).resolve().parent
LA = _load("fy816_answers", HERE / "lesson-answers.py")
EB = _load("fy810_answers", HERE.parent / "fy8-10" / "lesson-answers.py")   # E_B/A of 32 nuclides (AME2020)
BALMER = (LA.HA, LA.HB, LA.HG, LA.HD)


def wl_hex(lam):
    """The colour of light of wavelength lam (nm) on a screen (Bruton), as in the chapter Spektrit paljastavat atomin energiatasot."""
    if lam < 440: r, g, b = -(lam - 440) / 60, 0.0, 1.0
    elif lam < 490: r, g, b = 0.0, (lam - 440) / 50, 1.0
    elif lam < 510: r, g, b = 0.0, 1.0, -(lam - 510) / 20
    elif lam < 580: r, g, b = (lam - 510) / 70, 1.0, 0.0
    elif lam < 645: r, g, b = 1.0, -(lam - 645) / 65, 0.0
    else: r, g, b = 1.0, 0.0, 0.0
    f = 0.3 + 0.7 * (lam - 380) / 40 if lam < 420 else 0.3 + 0.7 * (750 - lam) / 50 if lam > 700 else 1.0
    return "#" + "".join(f"{round(255 * (max(0.0, min(1.0, v)) * f) ** 0.8):02x}" for v in (r, g, b))


def rainbow(f, gid, lo, hi, step=10):
    stops = "".join(f'<stop offset="{(l - lo) / (hi - lo):.3f}" stop-color="{wl_hex(l)}"/>' for l in range(lo, hi + 1, step))
    f.defs_add(f'<linearGradient id="{gid}" x1="0" y1="0" x2="1" y2="0">{stops}</linearGradient>')
    return f"url(#{gid})"


def galaxy(f, gid, cx, cy, rx, ry, angle=0, first=True, solid=False):
    """A galaxy: a glowing ellipse with a bright core (flat, no text); solid: an outlined disc that reads on white paper."""
    if solid:
        f.add(f'<ellipse cx="{n(cx)}" cy="{n(cy)}" rx="{n(rx)}" ry="{n(ry)}" fill="{HEAT_LIGHT}" stroke="{HEAT}" stroke-width="2" transform="rotate({angle:g} {n(cx)} {n(cy)})"/>')
        f.add(f'<ellipse cx="{n(cx)}" cy="{n(cy)}" rx="{n(rx * 0.45)}" ry="{n(ry * 0.5)}" fill="{WHITE}" transform="rotate({angle:g} {n(cx)} {n(cy)})"/>')
        return
    if first:
        f.defs_add(f'<radialGradient id="{gid}" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="{WHITE}"/>'
                   f'<stop offset="0.35" stop-color="{HEAT_LIGHT}"/><stop offset="1" stop-color="{HEAT_LIGHT}" stop-opacity="0"/></radialGradient>')
    f.add(f'<ellipse cx="{n(cx)}" cy="{n(cy)}" rx="{n(rx)}" ry="{n(ry)}" fill="url(#{gid})" transform="rotate({angle:g} {n(cx)} {n(cy)})"/>')
    f.circle(cx, cy, max(2.0, round(ry * 0.3 * 2) / 2), WHITE)


def spektri():
    """Ydinajatus: the same four hydrogen absorption lines in the laboratory and in a galaxy with z = 0,050."""
    z = LA.a["fig-z"]
    f = Fig("fy816-spektri", 350, "Kaavakuva, aallonpituusasteikko mittakaavassa 400–720 nanometriä. Ylempi värikaista on "
            "laboratoriossa vetykaasun läpi kulkeneen valon spektri: siinä on neljä tummaa absorptioviivaa aallonpituuksilla "
            "410, 434, 486 ja 656 nanometriä. Alempi värikaista on kaukaisen galaksin valon spektri, jossa samat neljä viivaa "
            "ovat siirtyneet pidempiin aallonpituuksiin eli punaiseen päin, jokainen 5,0 prosenttia omasta aallonpituudestaan. "
            "Katkoviivat yhdistävät vastinviivat. Punaisen viivan siirtymä 656,3 nanometristä 689,1 nanometriin on merkitty "
            "nuolella Δλ. Alla lukee z = Δλ / λ0 = 0,050.")
    lo, hi, x0, x1 = 400, 720, 180, 570
    X = lambda l: x0 + (l - lo) / (hi - lo) * (x1 - x0)
    rb = rainbow(f, "fy816-rb", lo, hi)
    s1, s2, h = 46, 182, 46
    for y, title in ((s1, r"\text{laboratorio}"), (s2, r"\text{galaksi}")):
        f.rect(x0, y, x1 - x0, h, rb)
        f.tex(92, y + h / 2, title, "middle", w=160)
    for l in BALMER:
        f.rect(X(l) - 2, s1, 4, h, INK)
        f.rect(X(l * (1 + z)) - 2, s2, 4, h, INK)
        f.line(X(l), s1 + h + 4, X(l * (1 + z)), s2 - 4, MUTED, 1.5, "5 4")
    for y in (s1, s2): f.rect(x0, y, x1 - x0, h, stroke=INK, sw=2)
    # λ0, λ and the shift of the red line
    xa, xb = X(LA.HA), X(LA.HA * (1 + z))
    f.tex(xa, s1 - 20, r"\lambda_0", "middle")
    f.arrow(xa, 140, xb, 140, HOT, 3, 13)
    f.tex((xa + xb) / 2, 117, r"\Delta\lambda", "middle", HOT)
    f.tex(xb + 10, 163, r"\lambda", "start")
    # wavelength axis
    yA = s2 + h + 10
    f.line(x0, yA, x1, yA, INK, 2)
    for l in range(400, 721, 20):
        f.line(X(l), yA, X(l), yA + (8 if l % 100 == 0 else 5), INK, 2 if l % 100 == 0 else 1.5)
    for l in (400, 500, 600, 700): f.tex(X(l), yA + 26, fi(l), "middle")
    f.tex(x0 - 34, yA + 26, r"\lambda\ (\text{nm})", "end")
    f.tex(375, 314, r"z = \frac{\Delta\lambda}{\lambda_0} = " + fi(z, 3), "middle")
    return f.svg()


def laajeneminen():
    """Ydinajatus: four galaxies before and after the distances have grown 1,5-fold; seen from A the displacement
    is proportional to the distance (v ∝ d)."""
    f = Fig("fy816-laajeneminen", 310, "Kaavakuva, etäisyydet mittakaavassa. Ylärivillä neljä galaksia A, B, C ja D "
            "jonossa tasavälein: B on etäisyydellä d galaksista A, C etäisyydellä 2d ja D etäisyydellä 3d. Alarivillä samat "
            "galaksit myöhemmin, kun kaikki etäisyydet ovat kasvaneet 1,5-kertaisiksi. Alimpana siniset siirtymänuolet: "
            "galaksista A katsottuna B on siirtynyt yhden, C kahden ja D kolmen yksikön verran, joten siirtymä ja nopeus v, "
            "2v ja 3v ovat suoraan verrannollisia etäisyyteen.")
    xa, step, k = 170, 80, 1.5
    old = [xa + i * step for i in range(4)]
    new = [xa + i * step * k for i in range(4)]
    f.tex(74, 78, r"\text{ennen}", "middle", w=124)
    f.tex(74, 190, r"\text{myöhemmin}", "middle", w=124)
    for i, x in enumerate(old):
        galaxy(f, "fy816-gal", x, 78, 22, 11, -18, solid=True)
        f.tex(x, 46, r"\text{" + "ABCD"[i] + "}", "middle")
        if i: f.tex(x, 110, ("" if i == 1 else str(i)) + "d", "middle", MUTED)
    for i, x in enumerate(new):
        galaxy(f, "fy816-gal", x, 190, 22, 11, -18, solid=True)
        f.tex(x, 158, r"\text{" + "ABCD"[i] + "}", "middle")
    for i in (1, 2, 3):
        f.line(old[i], 214, old[i], 252, MUTED, 1.5, "4 4")
        f.arrow(old[i] + 2, 246, new[i] - 2, 246, COLD, 3, 13)
        f.tex((old[i] + new[i]) / 2, 278, ("" if i == 1 else str(i)) + "v", "middle", COLD)
    return f.svg()


def aikajana():
    """Ydinajatus: the history of the universe as a timeline (schematic, not to scale); the bar cools from red to blue."""
    rows = [(r"t = 0", r"\text{alkuräjähdys}"),
            (r"3\text{–}20\,\text{min}", r"\text{vedyn ja heliumin ytimet}"),
            (r"380\,000\,\text{a}", r"\text{atomit ja taustasäteily}"),
            (r"\approx 2 \cdot 10^{8}\,\text{a}", r"\text{ensimmäiset tähdet}"),
            (r"9{,}2 \cdot 10^{9}\,\text{a}", r"\text{Aurinko ja Maa syntyvät}"),
            (r"13{,}8 \cdot 10^{9}\,\text{a}", r"\text{nyt: } T = 2{,}7\,\text{K}")]
    f = Fig("fy816-aikajana", 380, "Aikajana, ei mittakaavassa: maailmankaikkeuden kehitys ylhäältä alas. Pystysuora palkki "
            "vaihtuu punaisesta siniseksi, kun maailmankaikkeus jäähtyy. Aika nolla: alkuräjähdys, kuuma ja tiheä tila. 3–20 "
            "minuuttia: ensimmäiset ytimet, vety ja helium. 380 000 vuotta: atomit syntyvät ja taustasäteily vapautuu. Noin 200 "
            "miljoonaa vuotta: ensimmäiset tähdet. 9,2 miljardia vuotta: Aurinko ja Maa syntyvät. 13,8 miljardia vuotta: nyt, "
            "taustasäteilyn lämpötila 2,7 kelviniä.")
    f.defs_add(f'<linearGradient id="fy816-cool" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{HOT}"/>'
               f'<stop offset="0.45" stop-color="{HEAT_LIGHT}"/><stop offset="1" stop-color="{COLD}"/></linearGradient>')
    f.rect(52, 24, 16, 332, "url(#fy816-cool)", INK, 2, 8)
    for k, (t, ev) in enumerate(rows):
        y = 40 + k * 60
        f.circle(60, y, 9, WHITE, INK, 2.5)
        f.tex(92, y, t, "start")
        f.tex(250, y, ev, "start")
    return f.svg()


def _eb_axes(f):
    return Axes(f, (130, 330), (530, 60), x=(0, 250), y=(0, 10), xticks=[50, 100, 150, 200, 250], yticks=[2, 4, 6, 8, 10],
                xlabel="A", ylabel=r"E_\text{B}/A\ (\text{MeV})")


def alkuaineet():
    """Ydinajatus, stars: the binding-energy curve; fusion in stars builds nuclei up to the peak at iron, heavier ones
    come from neutron capture."""
    f = Fig("fy816-alkuaineet", 380, "Kuvaaja mittakaavassa: ytimen sidosenergia nukleonia kohti megaelektronivoltteina "
            "massaluvun A funktiona, A nollasta 250:een. Pisteet ovat 32 ytimen arvoja atomimassoista laskettuina, kuten "
            "luvussa Massavaje ja ytimen sidosenergia. Huippu on rauta-56:n kohdalla, noin 8,8 MeV, ja siihen on vedetty "
            "pystysuora katkoviiva. Huipun vasemmalla puolella oranssi nuoli: fuusio tähdissä tuottaa ytimiä heliumista "
            "rautaan ja vapauttaa energiaa. Huipun oikealla puolella harmaa nuoli: rautaa raskaammat ytimet syntyvät "
            "neutronisieppauksessa supernovissa ja neutronitähtien törmäyksissä.")
    ax = _eb_axes(f)
    a = EB.a
    xf = ax.X(56)
    f.line(xf, ax.Y(a["Fe56-EBA"]) + 8, xf, 152, MUTED, 1.5, "6 5")
    for s, _, Z, A, _ in EB.NUCLIDES:
        ax.point(A, a[f"{s}{A}-EBA"], HEAT, 5.5)
    fe = (ax.X(56), ax.Y(a["Fe56-EBA"]))
    f.line(fe[0] + 5, fe[1] - 5, 262, 70, MUTED, 1.5)
    f.tex(264, 62, r"{}^{56}\text{Fe}", "start")
    ya = 170
    f.block_arrow(ax.X(4), ya, xf - 6, ya, HEAT_LIGHT, 12, 28, 22)
    f.block_arrow(xf + 6, ya, ax.X(245), ya, ALUMINIUM, 12, 28, 22)
    f.tex(150, 208, r"\text{fuusio}", "start", HEAT)
    f.tex(150, 236, r"\text{tähdissä}", "start", HEAT)
    f.tex(262, 208, r"\text{neutronisieppaus}", "start")
    f.tex(262, 236, r"\text{supernovissa ja}", "start")
    f.tex(262, 264, r"\text{neutronitähtien}", "start")
    f.tex(262, 292, r"\text{törmäyksissä}", "start")
    return f.svg()


def kierto():
    """Ydinajatus, dark matter: the orbital speed of stars and gas against the distance from a galaxy's centre (schematic)."""
    f = Fig("fy816-kierto", 330, "Kaavakuva, ei mittakaavassa: tähtien ja kaasun ratanopeus v galaksin keskustasta mitatun "
            "etäisyyden r funktiona. Molemmat käyrät nousevat keskustan lähellä. Harmaa katkoviiva on nopeus, jonka näkyvän "
            "aineen painovoima selittäisi: se pienenee kaukana keskustasta. Sininen yhtenäinen käyrä mittauspisteineen on "
            "mitattu nopeus: se pysyy lähes vakiona kauas galaksin laitamille. Ero viittaa näkymättömään pimeään aineeseen.")
    ax = Axes(f, (110, 290), (420, 70), x=(0, 1), y=(0, 1), xticks=[], yticks=[], xlabel="r", ylabel="v", grid=False)
    rc = 0.16
    meas = lambda r: 0.82 * (1 - math.exp(-r / 0.07))
    expd = lambda r: 0.82 * 1.55 * (r / rc) / (1 + (r / rc) ** 2) ** 0.75 * (1 - math.exp(-r / 0.03))
    ax.curve(expd, 0, 1, MUTED, 3, dash="9 7")
    ax.curve(meas, 0, 1, COLD, 3)
    for r in (0.1, 0.25, 0.4, 0.55, 0.7, 0.85):
        ax.point(r, meas(r) + (0.02 if int(r * 20) % 2 else -0.015), COLD, 5.5)
    f.tex(ax.X(1) + 10, ax.Y(meas(1)), r"\text{mitattu}", "start", COLD)
    f.tex(ax.X(1) + 10, ax.Y(expd(1)), r"\text{näkyvä aine}", "start", MUTED)
    return f.svg()


def koostumus():
    """Ydinajatus, dark energy: the energy content of the universe as one bar, to scale (Planck 2018, rounded)."""
    a = LA.a
    parts = [(a["ordinary"], HEAT_LIGHT), (a["dark-matter"], IRON), (a["dark-energy"], RULE)]
    f = Fig("fy816-koostumus", 200, "Vaakapalkki mittakaavassa: maailmankaikkeuden energiasisältö Planck-satelliitin "
            "mittausten perusteella. Tavallinen aine, josta tähdet, kaasu ja me koostumme, on noin 5 prosenttia, pimeä aine "
            "noin 26 prosenttia ja pimeä energia noin 69 prosenttia.")
    x, y0, w, h = 40, 64, 520, 48
    xs = []
    for p, col in parts:
        dw = w * p / 100
        f.rect(x, y0, dw, h, col, INK, 2)
        xs.append((x, x + dw)); x += dw
    f.tex(40, 36, r"\text{tavallinen aine}\ " + fi(round(a["ordinary"])) + r"\,\%", "start")
    for (xa, xb), name, p in ((xs[1], r"\text{pimeä aine}", a["dark-matter"]), (xs[2], r"\text{pimeä energia}", a["dark-energy"])):
        f.tex((xa + xb) / 2, 140, name, "middle")
        f.tex((xa + xb) / 2, 170, fi(round(p)) + r"\,\%", "middle")
    return f.svg()


def _hubble_axes(f, yticks, yfmt):
    return Axes(f, (130, 300), (460, 60), x=(0, 300), y=(0, 21000), xticks=[50, 100, 150, 200, 250, 300], yticks=yticks,
                xlabel=r"d\ (\text{Mpc})", ylabel=r"v\ (\text{km/s})", yfmt=yfmt)


def _kfmt(v):
    s = f"{int(v)}"
    return s if len(s) < 5 else s[:-3] + r"\," + s[-3:]


def hubble():
    """Kaava: the eight galaxies of the simulation (model values) and the line v = H0 d with H0 = 70 km/s/Mpc."""
    a = LA.a
    f = Fig("fy816-hubble", 350, "Kuvaaja mittakaavassa: galaksien etääntymisnopeus v kilometreinä sekunnissa etäisyyden d "
            "funktiona megaparsekeina, etäisyys nollasta 300 megaparsekiin ja nopeus nollasta 21 000 kilometriin sekunnissa. "
            "Kahdeksan pistettä ovat simulaation galaksien mallin arvoja; ne ovat lähellä origon kautta kulkevaa suoraa "
            "v = H0 d, jonka kulmakerroin on 70 kilometriä sekunnissa megaparsekia kohti. Katkoviivat näyttävät suoralta "
            "luettavan pisteen: etäisyydellä 200 megaparsekia nopeus on 14 000 kilometriä sekunnissa.")
    ax = _hubble_axes(f, [3500, 7000, 10500, 14000, 17500, 21000], _kfmt)
    ax.guide(200, 14000)
    ax.line([(0, 0), (300, 21000)], INK, 3)
    for k, d, _ in LA.GALAXIES:
        ax.point(d, a[f"g{k}-v"], HEAT, 6)
    f.tex(ax.X(300) + 10, ax.Y(21000) + 4, r"v = H_0\,d", "start")
    return f.svg()


T2 = [(30, 2500), (60, 4000), (95, 7200), (120, 8300), (160, 11900), (190, 13300), (220, 16400), (255, 18100), (285, 20800)]


def hubble_task():
    """Task figure (Tarkista 2): another invented data set with its fitted line through the origin."""
    f = Fig("fy816-hubble-t", 350, "Kuvaaja mittakaavassa: yhdeksän galaksin etääntymisnopeus v kilometreinä sekunnissa "
            "etäisyyden d funktiona megaparsekeina, etäisyys nollasta 300 megaparsekiin ja nopeus nollasta 21 000 kilometriin "
            "sekunnissa, ruudukon välit 50 megaparsekia ja 3000 kilometriä sekunnissa. Pisteisiin on sovitettu origon kautta "
            "kulkeva suora, joka kulkee ruudukon pisteen d = 250 Mpc, v = 18 000 km/s kautta.")
    ax = _hubble_axes(f, [3000, 6000, 9000, 12000, 15000, 18000, 21000], _kfmt)
    H = LA.a["t2-H0"]
    ax.line([(0, 0), (21000 / H, 21000)], INK, 3)
    for d, v in T2:
        ax.point(d, v, HEAT, 6)
    return f.svg()


def hero():
    """The chapter's opening illustration: a night sky full of galaxies above an observatory on a hill."""
    f = H.hero("fy816-hero", "Kuvitus: tähtitaivas, jolla hehkuu kymmenkunta eri kokoista galaksia, suuret lähellä ja pienet "
               "kaukana. Alhaalla mäellä on observatorio, jonka kupolin raosta kaukoputki osoittaa taivaalle.")
    H.space(f, seed=16, count=110)
    gal = [(600, 170, 120, 46, -22), (330, 120, 70, 26, 15), (870, 110, 62, 24, -35), (1010, 250, 46, 18, 20),
           (190, 260, 40, 16, -10), (760, 300, 34, 13, 30), (470, 300, 26, 10, -25), (1100, 90, 24, 9, 10),
           (90, 110, 22, 9, 30), (940, 380, 18, 7, -15), (300, 380, 16, 6, 5)]
    for i, (x, y, rx, ry, ang) in enumerate(gal):
        galaxy(f, "fy816h-gal", x, y, rx, ry, ang, first=(i == 0))
    # a hill and the observatory
    f.path("M0,600 L0,500 Q300,430 600,450 Q900,470 1200,420 L1200,600 Z", IRON)
    f.path("M0,600 L0,540 Q320,490 640,510 Q930,530 1200,490 L1200,600 Z", INK)
    f.rect(520, 410, 160, 70, ALUMINIUM, INK, 3)
    f.path("M520,412 A80,80 0 0 1 680,412 Z", WHITE, INK, 3)
    f.path("M592,334 L614,334 L622,412 L584,412 Z", IRON, INK, 2)
    f.path("M602,350 L680,220 L692,228 L616,358 Z", METAL_EDGE, INK, 2.5)
    f.rect(586, 440, 28, 40, GLASS, INK, 2)
    return f.svg()


FIGURES = {"hero": hero, "spektri": spektri, "laajeneminen": laajeneminen, "aikajana": aikajana, "alkuaineet": alkuaineet,
           "kierto": kierto, "koostumus": koostumus, "hubble": hubble, "hubble-t": hubble_task}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "hero": "decorative",
    "spektri": "reveals: lab and galaxy hydrogen lines, every line shifted by z = 0,050, Hα 656,3 -> 689,1 nm",
    "laajeneminen": "reveals: uniform expansion seen from A, displacement v, 2v, 3v at distances d, 2d, 3d",
    "aikajana": "reveals: the timeline 0, 3-20 min, 380 000 a, 2e8 a, 9,2e9 a, 13,8e9 a and its events",
    "alkuaineet": "reveals: fusion in stars up to Fe-56, heavier nuclei by neutron capture (E_B/A curve)",
    "kierto": "reveals: the flat measured rotation curve against the falling one of visible matter",
    "koostumus": "reveals: ordinary matter 5 %, dark matter 26 %, dark energy 69 %",
    "hubble": "reveals: the simulation's eight galaxies, the line v = H0 d with H0 = 70 km/s/Mpc",
    "hubble-t": "safe: nine invented galaxies with a fitted line through the origin and the grid point (250 Mpc, 18 000 km/s); H0 = 72 is read from it",
}
