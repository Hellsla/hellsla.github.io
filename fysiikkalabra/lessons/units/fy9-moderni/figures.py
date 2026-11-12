"""Figures of the FY9 unit fy9-moderni (scripts/figlib.py, herolib.py); `python3 scripts/units.py figures fy9-moderni`
writes them into content/fi/units/fy9-moderni/unit.md. The unit is Finnish, so the decimal sign is a comma.

hero        the Why scene: a greenhouse on a snowy winter night, its red and blue LED grow lights glowing over rows of
            tomato plants, spruces and a starry sky behind (no text, no people)
kartta      the concept map of the review: quantised energy at the top, then photon and atom (eV), the nucleus (MeV)
            and radiation and the body (dose), each with three laws
fotonit     the hook to scale: photon energies on a logarithmic axis from 0,1 eV to 10 MeV, the visible band, the
            red LED (1,9 eV), the ionisation energy of water (12,6 eV), a dental X-ray (60 keV) and the Cs-137 gamma
            (662 keV), with the electron-level and nuclear-level ranges
puolitus    the one law of halving: the fraction left after n half-lives (decay) or n half-value layers (shielding),
            1/2, 1/4 and 1/8 marked
"""
import math
import figlib
from figlib import (Fig, INK, MUTED, WHITE, RULE, RULE_LIGHT, GLASS, SAND_LIGHT, SAND, HEAT_LIGHT, HEAT, HOT, HOT_LIGHT,
                    COLD, COLD_LIGHT, GOOD, GOOD_LIGHT, ICE, ICE_EDGE, IRON, METAL_EDGE, COPPER, n, fi)
from figlib import Axes
import herolib as H

figlib.set_language({}, ",")

# the hook (computed here and quoted in unit.md and inquiry.json)
h, c, e = 6.626e-34, 2.998e8, 1.602e-19
E_RED = h * c / 660e-9 / e          # 1,88 eV, the red grow light
E_ION = 12.6                        # eV, the ionisation energy of a water molecule (luku Ionisoiva säteily ja elimistö)
E_XRAY = 60e3                       # eV, the mean photon energy of a dental X-ray (luku Säteily lääketieteessä ja teknologiassa)
E_CS = 662e3                        # eV, the Cs-137 (Ba-137m) gamma


def hero():
    """A greenhouse on a snowy winter night. The sky darkens upwards with a few stars; spruces stand behind; the
    greenhouse in the middle third glows pink from rows of red and blue LED bars under its roof, and inside are rows
    of tomato plants with red fruit; the snow in front catches the light."""
    f = H.hero("fy9mo-hero", "Kuvitus: lasinen kasvihuone lumisena talviyönä. Tummalla taivaalla on tähtiä, ja taustalla on "
               "kuusimetsää. Kasvihuoneen katon alla on rivissä punaisia ja sinisiä LED-valaisimia, joiden valo täyttää "
               "kasvihuoneen vaaleanpunaisena hehkuna. Sisällä kasvaa riveittäin tomaatintaimia, joissa on punaisia tomaatteja. "
               "Valo heijastuu kasvihuoneen edessä olevalle lumelle.")
    f.rect(0, 0, 1200, 600, H.grad(f, "fy9mo-sky", INK, "#2f74b5", y1=0, y2=470))
    for k in range(46):
        x, y = H.rnd(k, 3) * 1200, H.rnd(k + 300, 3) * 300
        if 340 < x < 860 and y > 120: continue
        f.circle(x, y, 1.2 + 1.6 * H.rnd(k + 700, 3), WHITE)
    f.add(f'<circle cx="1040" cy="92" r="34" fill="{WHITE}" fill-opacity="0.9"/>')
    f.add(f'<circle cx="1056" cy="82" r="30" fill="{INK}" fill-opacity="0.85"/>')           # a crescent moon
    # spruces behind, dark against the sky
    for k, x in enumerate(range(-20, 1240, 58)):
        hh = 150 + 70 * H.rnd(k, 5)
        f.path(f"M{x - 40},430 L{x},{430 - hh} L{x + 40},430 Z", "#1f3b2d" if k % 2 else "#24452f")
    # the snow field with a soft pink light in front of the greenhouse
    f.rect(0, 420, 1200, 180, H.grad(f, "fy9mo-snow", "#eef5f9", ICE, y1=420, y2=600))
    f.add(f'<ellipse cx="600" cy="470" rx="420" ry="60" fill="{HOT_LIGHT}" fill-opacity="0.35"/>')
    # the greenhouse: a glass box with a gabled roof
    x0, x1, yb, ye, yr = 330, 870, 440, 270, 170
    f.defs_add('<linearGradient id="fy9mo-glow" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f2a69c"/>'
               '<stop offset="1" stop-color="#ffc078"/></linearGradient>')
    f.path(f"M{x0},{yb} V{ye} L600,{yr} L{x1},{ye} V{yb} Z", "url(#fy9mo-glow)", INK, 3)
    # the LED bars under the roof: red and blue alternating, with light cones
    for k, x in enumerate(range(370, 840, 52)):
        col = HOT if k % 3 else COLD
        y = ye + 6 + (abs(600 - (x + 18)) < 140) * 0
        f.add(f'<path d="M{x},{ye + 10} L{x + 36},{ye + 10} L{x + 58},{yb - 40} L{x - 22},{yb - 40} Z" fill="{col}" fill-opacity="0.12"/>')
        f.rect(x, ye + 2, 36, 9, col, INK, 1.5, 2)
    # tomato plants in three rows
    for row, (yy, sc) in enumerate(((410, 1.0), (392, 0.82), (378, 0.66))):
        for k, x in enumerate(range(360 + row * 14, 850, 46 - row * 4)):
            hgt = 80 * sc
            f.line(x, yy, x, yy - hgt, "#2b8a3e", 3 * sc + 1)
            for j in range(3):
                ly = yy - hgt * (0.3 + 0.3 * j)
                f.add(f'<ellipse cx="{n(x - 9 * sc)}" cy="{n(ly)}" rx="{n(10 * sc)}" ry="{n(5 * sc)}" fill="#2b8a3e" transform="rotate(-25 {n(x - 9 * sc)} {n(ly)})"/>')
                f.add(f'<ellipse cx="{n(x + 9 * sc)}" cy="{n(ly - 6 * sc)}" rx="{n(10 * sc)}" ry="{n(5 * sc)}" fill="#2b8a3e" transform="rotate(25 {n(x + 9 * sc)} {n(ly - 6 * sc)})"/>')
            if (k + row) % 2 == 0: f.circle(x + 6 * sc, yy - hgt * 0.45, 6.5 * sc, HOT, INK, 1)
            if (k + row) % 3 == 0: f.circle(x - 7 * sc, yy - hgt * 0.62, 5.5 * sc, HOT, INK, 1)
    # the planter boxes
    for yy, w in ((410, 520), (392, 470), (378, 430)):
        f.rect(600 - w / 2, yy, w, 8, COPPER, INK, 1.5, 2)
    # the glass frame: mullions and the ridge, drawn last over the light
    for x in range(x0, x1 + 1, 90):
        top = ye if x in (x0, x1) else ye - (yr - ye) * (abs(600 - x) / 270 - 1) * -1
        top = ye - (ye - yr) * (1 - abs(600 - x) / 270)
        f.line(x, yb, x, top, INK, 2.5)
    f.line(x0, ye, x1, ye, INK, 2.5)
    f.line(x0, 355, x1, 355, INK, 1.5)
    f.add(f'<path d="M{x0},{ye} L600,{yr} L{x1},{ye}" fill="none" stroke="{WHITE}" stroke-opacity="0.45" stroke-width="6"/>')
    f.path(f"M{x0},{yb} V{ye} L600,{yr} L{x1},{ye} V{yb} Z", "none", INK, 3)
    # snow on the roof edges and the ground line
    f.path(f"M{x0 - 6},{ye + 4} L600,{yr - 6} L{x1 + 6},{ye + 4} L{x1 - 4},{ye + 8} L600,{yr + 4} L{x0 + 4},{ye + 8} Z", WHITE, ICE_EDGE, 1.5)
    f.rect(x0 - 10, yb, x1 - x0 + 20, 10, IRON, INK, 2, 2)
    # a snow drift and footprints-free path; a small red shed on the left
    H.red_house(f, 120, 440, 150, 110, snow=True)
    f.path("M0,520 Q300,480 600,500 T1200,505 V600 H0 Z", WHITE, extra='fill-opacity="0.8"')
    return f.svg()


def kartta():
    """The concept map, stacked for a phone: quantised energy at the top, a spine down the left and three boxes
    (photon and atom, the nucleus, radiation and the body), each with three laws and a grey word beside each."""
    f = Fig("fy9mo-kartta", 744, "Käsitekartta. Ylhäällä solmu kvantittunut energia: fotonin energia E = h f ja massan ja "
            "energian yhteys E = m c toiseen. Siitä lähtee alas kolme haaraa. Fotoni ja atomi, elektronivolttien maailma: "
            "valosähköinen yhtälö h f = W + E k max, spektriviivan fotoni h f = E y miinus E a ja LEDin kynnysjännite e U k "
            "likimain h f. Ydin, megaelektronivolttien maailma: hajoamislaki N = N 0 kertaa puoli potenssiin t per T puoli, "
            "aktiivisuus A = lambda N ja reaktioenergia Q = massojen erotus kertaa c toiseen. Säteily ja ihminen, annos: "
            "absorboitunut annos D = E per m, ekvivalenttiannos H T = w R kertaa D T ja etäisyyden neliölaki. Alareunassa kaikkia haaroja yhdistävä ohje: ensin yksi hiukkanen, sitten lukumäärä.", width=380, size=20)
    groups = [
        ("fotoni ja atomi", "eV", [(r"hf = W + E_\text{k,max}", "irtoaminen"), (r"hf = E_\text{y} - E_\text{a}", "spektri"),
                                    (r"eU_\text{k} \approx hf", "LED")]),
        ("ydin", "MeV", [(r"N = N_0 e^{-\lambda t}", "hajoaminen"), (r"A = \lambda N", "aktiivisuus"),
                         (r"E = \Delta m\,c^2", "reaktio")]),
        ("säteily ja ihminen", "annos", [(r"D = E/m", "absorboitunut"), (r"H = w_\text{R} D", "painotettu"),
                                         (r"\dot{H} \propto 1/r^2", "etäisyys")]),
    ]
    hub_y, hub_h, x_box, gh, top = 8, 72, 44, 188, 100
    spine = 24
    f.line(spine, hub_y + hub_h, spine, top + 2 * (gh + 16) + 22, RULE, 3)
    f.rect(8, hub_y, 364, hub_h, SAND_LIGHT, SAND, 2.5, 12)
    f.tex(190, hub_y + 22, r"\text{kvantittunut energia}", "middle", INK)
    f.tex(190, hub_y + 51, r"E = hf,\quad E = mc^2", "middle", INK)
    for k, (head, sub, rows) in enumerate(groups):
        y = top + k * (gh + 16)
        f.line(spine, y + 22, x_box, y + 22, RULE, 3)
        f.rect(x_box, y, 372 - x_box, gh, WHITE, MUTED, 2, 10)
        f.tex(x_box + 14, y + 22, r"\textbf{" + head + "}", "start", INK)
        f.tex(362, y + 22, r"\text{" + sub + "}", "end", MUTED, size=17)
        f.line(x_box + 10, y + 42, 362, y + 42, RULE_LIGHT, 1.5)
        for j, (law, word) in enumerate(rows):
            yy = y + 68 + j * 52
            f.tex(x_box + 14, yy, law, "start", INK, size=18 if len(law) > 26 else None)
            f.tex(362, yy, r"\text{" + word + "}", "end", MUTED, size=17)
    # what joins the branches: one particle first, then the number of particles
    f.tex(190, 724, r"\text{joka haarassa: yksi hiukkanen, sitten lukumäärä}", "middle", INK, size=17)
    return f.svg().replace("max-width:100%;", "max-width:min(100%,420px);", 1)


def fotonit():
    """The hook to scale: one decade of photon energy is 62 units on a logarithmic axis from 0,1 eV to 10 MeV. The
    visible band (1,7–3,3 eV) is a coloured strip; the red LED is a point at 1,88 eV; a dashed line at 12,6 eV, the
    ionisation energy of water, splits 'ei ionisoi' from 'ionisoi'; the dental X-ray (60 keV) and the Cs-137 gamma
    (662 keV) are points far to the right. Under the axis, brackets show where the electron levels (about 1–100 eV)
    and the nuclear levels (about 10 keV–10 MeV) lie."""
    f = Fig("fy9mo-fotonit", 392, "Kaavakuva, energia-akseli logaritmisessa mittakaavassa: fotonin energia elektronivoltteina "
            "kymmenesosasta kymmeneen miljoonaan, jokainen jakoväli kymmenkertainen. Näkyvä valo on kapea värikaista "
            "1,7–3,3 elektronivolttia, ja punaisen LED-valon fotoni on 1,9 elektronivolttia. Katkoviiva kohdassa 12,6 "
            "elektronivolttia on vesimolekyylin ionisaatioenergia: sen vasemmalla puolella fotoni ei ionisoi vettä, "
            "oikealla puolella ionisoi. Hammasröntgenin fotoni, noin 60 kiloelektronivolttia, ja cesium-137:n "
            "gammafotoni, 662 kiloelektronivolttia, ovat kaukana oikealla. Akselin alla hakasulkeet: atomin elektronien "
            "energiatasojen erot ovat elektronivolttien luokkaa, ytimen tasojen erot kilo- ja megaelektronivolttien.", size=24)
    X = lambda E: 54 + (math.log10(E) + 1) * 62
    ya = 196
    # the ionising side, lightly shaded
    f.rect(X(E_ION), 92, X(1e7) - X(E_ION) + 8, ya - 92, HOT_LIGHT, None, 0, extra='fill-opacity="0.28"')
    # the visible band
    f.defs_add('<linearGradient id="fy9mo-vis" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#c92a2a"/>'
               '<stop offset="0.35" stop-color="#e8590c"/><stop offset="0.6" stop-color="#2b8a3e"/><stop offset="1" stop-color="#1971c2"/></linearGradient>')
    f.rect(X(1.7), ya - 12, X(3.3) - X(1.7), 24, "url(#fy9mo-vis)", INK, 1.5)
    # the axis with decade ticks
    f.arrow(40, ya, 588, ya, INK, 2.5, 13)
    for p in range(-1, 8):
        f.line(X(10 ** p), ya, X(10 ** p), ya + 8, INK, 2)
        if p in (0, 2, 4, 6):
            f.tex(X(10 ** p), ya + 30, "1" if p == 0 else rf"10^{{{p}}}", "middle", INK, size=24)
    f.tex(588, ya - 20, r"E\ (\text{eV})", "end", INK)
    # the ionisation line
    f.line(X(E_ION), 54, X(E_ION), ya + 22, INK, 2, dash="7 6")
    f.tex(X(E_ION) + 8, 28, r"\text{veden ionisaatioenergia } 12{,}6\,\text{eV}", "start", INK, size=24)
    f.tex(X(E_ION) - 8, 70, r"\text{ei ionisoi}", "end", GOOD, size=24)
    f.tex(X(E_ION) + 8, 70, r"\text{ionisoi}", "start", HOT, size=24)
    # the photons
    for E, name, val, xl in ((E_RED, r"\text{punainen LED}", r"1{,}9\,\text{eV}", 0), (E_XRAY, r"\text{röntgen}", r"60\,\text{keV}", -14),
                              (E_CS, r"\text{gamma}", r"662\,\text{keV}", 22)):
        x = X(E)
        f.line(x, ya, x, 150, MUTED, 1.5)
        f.circle(x, ya, 7.5, INK, WHITE, 2)
        anchor = "start" if E == E_RED else "middle"
        xx = 12 if E == E_RED else x + xl
        f.tex(xx, 104, name, anchor, INK, size=24)
        f.tex(xx, 134, val, anchor, INK, size=24)
    # where the levels lie
    for a, b, word in ((1.0, 100.0, r"\text{elektronien tasot}"), (1e4, 1e7, r"\text{ytimen tasot}")):
        f.path(f"M{n(X(a))},{ya + 66} V{ya + 74} H{n(X(b))} V{ya + 66}", "none", INK, 2)
        f.tex((X(a) + X(b)) / 2, ya + 100, word, "middle", INK, size=24)
    f.tex(X(1.7) - 6, ya + 128, r"\text{näkyvä valo } 1{,}7\text{–}3{,}3\,\text{eV}", "start", MUTED, size=24)
    f.tex(588, ya + 166, r"\text{logaritminen asteikko}", "end", MUTED, size=24)
    return f.svg()


def puolitus():
    """One law of halving: the fraction left against n, the number of half-lives (decay) or half-value layers (gamma
    shielding), 0–5. The curve 2^(-n), with guides at n = 1, 2, 3 to 1/2, 1/4 and 1/8, and a note that it never
    reaches zero."""
    f = Fig("fy9mo-puolitus", 380, "Kuvaaja mittakaavassa: jäljellä oleva osuus puoliintumisaikojen tai "
            "puoliintumispaksuuksien lukumäärän n funktiona, n nollasta viiteen. Käyrä alkaa arvosta 1 ja laskee yhä "
            "loivemmin. Katkoviivat näyttävät, että n = 1 antaa puolet, n = 2 neljäsosan ja n = 3 kahdeksasosan. Käyrä "
            "lähestyy nollaa mutta ei saavuta sitä: hajoamisella ja gammasäteilyn vaimenemisella ei ole loppupistettä.", size=26)
    ax = Axes(f, (100, 312), (470, 62), x=(0, 5), y=(0, 1.0), xticks=[1, 2, 3, 4, 5], yticks=[0.125 * i for i in range(1, 9)],
              xlabel=r"n", ylabel=r"N/N_0,\ I/I_0",
              yfmt=lambda v: {1.0: "1", 0.5: r"\tfrac12", 0.25: r"\tfrac14", 0.125: ""}.get(round(v, 3), ""))
    ax.curve(lambda x: 0.5 ** x, 0, 5, HEAT, 3)
    for k in (1, 2, 3):
        ax.guide(k, 0.5 ** k, MUTED)
        ax.point(k, 0.5 ** k, HEAT)
    ax.point(0, 1.0, HEAT)
    f.tex(ax.X(3) + 14, ax.Y(0.125) - 14, r"\tfrac18", "start", INK, size=24)
    f.tex(ax.X(2.2), ax.Y(0.86), r"n = \tfrac{t}{T_{1/2}}\ \text{tai}\ n = \tfrac{d}{d_{1/2}}", "start", INK, size=24)
    return f.svg()


FIGURES = {"hero": hero, "kartta": kartta, "fotonit": fotonit, "puolitus": puolitus}
REUSE = {"kartta": "reveals: the key laws of FY8 photons, the nucleus and radiation doses",
         "fotonit": "reveals: a red photon 1,9 eV is far below the 12,6 eV ionisation energy of water; X-rays and gamma far above",
         "puolitus": "safe: the halving curve 2^-n with 1/2, 1/4, 1/8 at n = 1, 2, 3"}
