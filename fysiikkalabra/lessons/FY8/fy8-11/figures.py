"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy8-11` writes them into lesson.md.
Protons red and neutrons light grey with ink outlines (as in the chapter Atomiydin ja radioaktiivinen hajoaminen),
a free neutron a grey dot with the label n, released energy an orange block arrow. Binding energies per nucleon and
reaction energies come from lesson-answers.py (imported, one source)."""
import importlib.util, math, pathlib
from figlib import (Fig, Axes, fi, n, INK, MUTED, WHITE, RULE, RULE_LIGHT, GLASS, WATER_LIGHT, WATER, HEAT, HEAT_LIGHT, HOT,
                    COLD, COLD_LIGHT, ALUMINIUM, METAL_EDGE, IRON, COPPER, SAND, SAND_LIGHT, SAND_DARK, GRAIN, GOOD,
                    GOOD_LIGHT, PAPER)
import herolib as H

_spec = importlib.util.spec_from_file_location("fy811_answers", pathlib.Path(__file__).with_name("lesson-answers.py"))
LA = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(LA)
A_ = LA.a
PROTON, NEUTRON = HOT, ALUMINIUM


def nucleus(f, cx, cy, Z, N, r=6, seed=1, sx=1.0):
    """A nucleus: Z protons and N neutrons packed in a disc (sunflower packing); sx > 1 stretches it sideways."""
    A = Z + N
    kinds = [1] * Z + [0] * N
    order = sorted(range(A), key=lambda k: H.rnd(k, seed))
    kinds = [kinds[k] for k in order]
    g = math.pi * (3 - math.sqrt(5))
    pts = [(cx + sx * 1.02 * r * math.sqrt(k + 0.5) * math.cos(k * g), cy + 1.02 * r * math.sqrt(k + 0.5) * math.sin(k * g)) for k in range(A)]
    for (x, y), kd in sorted(zip(pts, kinds), key=lambda t: -math.hypot(t[0][0] - cx, t[0][1] - cy)):
        f.circle(x, y, r, PROTON if kd else NEUTRON, INK, 1.2)
    return 1.02 * r * math.sqrt(A) + r


def neutron(f, x, y, r=9):
    f.circle(x, y, r, NEUTRON, INK, 2)


semf = LA.semf                                       # the smooth trend of E_B/A for A >= 16 (lesson-answers.py)


NAMED = [("H-2", r"{}^{2}\text{H}", "start", 10, 0), ("He-4", r"{}^{4}\text{He}", "start", 10, 28),
         ("C-12", r"{}^{12}\text{C}", "start", 10, -24), ("Fe-56", r"{}^{56}\text{Fe}", "middle", 0, -28),
         ("Kr-92", r"{}^{92}\text{Kr}", "middle", 0, 30), ("Ba-141", r"{}^{141}\text{Ba}", "middle", 0, 30),
         ("U-235", r"{}^{235}\text{U}", "end", -10, -26)]


def sidosenergia():
    """Ydinajatus: binding energy per nucleon against A, fusion climbs from the left, fission from the right."""
    f = Fig("fy811-bpn", 380, "Kuvaaja mittakaavassa: ytimen sidosenergia nukleonia kohti megaelektronivoltteina massaluvun "
            "funktiona, massaluku nollasta 240:een. Pisteet on laskettu atomimassoista: deuterium 1,1, helium-4 7,1, "
            "hiili-12 7,7, rauta-56 8,8, krypton-92 8,5, barium-141 8,3 ja uraani-235 7,6 megaelektronivolttia. Käyrä "
            "nousee jyrkästi kevyillä ytimillä, on korkeimmillaan raudan kohdalla ja laskee loivasti raskaita ytimiä kohti. "
            "Vasemmalla nuoli kevyistä ytimistä viistosti oikealle ylöspäin kohti huippua: fuusio. Oikealla nuoli uraanista "
            "viistosti vasemmalle ylöspäin keskiraskaisiin ytimiin: fissio.")
    ax = Axes(f, (96, 318), (500, 72), x=(0, 240), y=(0, 10), xticks=[40, 80, 120, 160, 200, 240], yticks=[2, 4, 6, 8, 10],
              xlabel="A", ylabel=r"E_\text{B}/A\ (\text{MeV})")
    ax.curve(semf, 16, 240, HEAT_LIGHT, 3)
    for key, tex, anc, dx, dy in NAMED:
        A = int(key.split("-")[1]); v = A_[f"bpn-{key}"]
        ax.point(A, v, HEAT)
        f.tex(ax.X(A) + dx, ax.Y(v) + dy, tex, anc)
    # fusion: from the light nuclei up and right towards the peak; fission: from uranium up and left to the middle
    f.block_arrow(ax.X(24), ax.Y(2.4), ax.X(56), ax.Y(6.4), HEAT_LIGHT, 14, 30, 22)
    f.tex(ax.X(46), ax.Y(3.0), r"\text{fuusio}", "start", HEAT)
    f.block_arrow(ax.X(226), ax.Y(5.4), ax.X(156), ax.Y(6.1), HEAT_LIGHT, 14, 30, 22)
    f.tex(ax.X(192), ax.Y(4.5), r"\text{fissio}", "middle", HEAT)
    return f.svg()


def sidosenergia_read():
    """Tarkista 2: the same values on a finer grid, no arrows, for reading E_B/A at A = 118 and A = 236."""
    f = Fig("fy811-bpnr", 380, "Kuvaaja mittakaavassa: ytimen sidosenergia nukleonia kohti megaelektronivoltteina "
            "massaluvun funktiona, massaluku 20:stä 240:een, pystyakseli 7,0:sta 9,0:aan. Ruudukon väli on vaakasuunnassa "
            "10 ja pystysuunnassa 0,1 megaelektronivolttia. Käyrä on korkeimmillaan noin massaluvun 60 kohdalla ja laskee "
            "loivasti raskaita ytimiä kohti. Pystyakselissa on katkosmerkki, koska akseli ei ala nollasta.")
    ax = Axes(f, (96, 318), (500, 72), x=(20, 240), y=(7.0, 9.0), xticks=list(range(30, 241, 10)),
              yticks=[7.0 + 0.1 * k for k in range(1, 21)], xlabel="A", ylabel=r"E_\text{B}/A\ (\text{MeV})",
              xfmt=lambda v: fi(v) if v % 40 == 0 else "", yfmt=lambda v: fi(round(v, 1)) if abs(v * 2 - round(v * 2)) < 1e-9 else "",
              origin_label=False)
    f.tex(ax.x0 - 12, ax.y0, r"7{,}0", "end")
    brk = f"M{ax.x0 - 8},{ax.y0 - 3} L{ax.x0 + 8},{ax.y0 - 8} M{ax.x0 - 8},{ax.y0 - 9} L{ax.x0 + 8},{ax.y0 - 14}"
    f.path(brk, stroke=WHITE, w=5); f.path(brk, stroke=INK, w=2)          # break mark: the y axis starts at 7,0
    ax.curve(semf, 20, 240, HEAT, 3)
    return f.svg()


def fissio():
    """Ydinajatus: n + U-235 -> U-236 (stretched) -> Ba-141 + Kr-92 + 3 n with the fragments' kinetic energy."""
    f = Fig("fy811-fis", 340, "Kaavakuva, ei mittakaavassa: uraani-235:n fissio kolmessa vaiheessa vasemmalta oikealle. "
            "Hidas neutroni osuu uraani-235-ytimeen. Syntyy uraani-236-ydin, joka värähtelee ja venyy kuroutuvaksi. Ydin "
            "jakautuu kahdeksi keskiraskaaksi ytimeksi, bariumiksi ja kryptoniksi, jotka lentävät suurella nopeudella eri "
            "suuntiin, ja samalla vapautuu kolme uutta neutronia.")
    neutron(f, 30, 150); f.arrow(44, 150, 76, 150, INK, 2.5, 12); f.tex(30, 120, "n", "middle")
    nucleus(f, 140, 150, 20, 28, r=5.4, seed=3)
    f.tex(140, 236, r"{}^{235}\text{U}", "middle")
    f.line(212, 40, 212, 280, RULE, 2, "6 6")
    nucleus(f, 300, 150, 20, 28, r=5.4, seed=5, sx=1.45)
    f.tex(300, 236, r"{}^{236}\text{U}", "middle")
    f.line(388, 40, 388, 280, RULE, 2, "6 6")
    nucleus(f, 470, 92, 11, 15, r=5.4, seed=7)
    nucleus(f, 470, 214, 8, 11, r=5.4, seed=9)
    f.tex(520, 92, r"{}^{141}\text{Ba}", "start"); f.tex(512, 214, r"{}^{92}\text{Kr}", "start")
    f.block_arrow(470, 54, 470, 22, HEAT_LIGHT, 10, 22, 16); f.block_arrow(470, 252, 470, 290, HEAT_LIGHT, 10, 22, 16)
    for x, y in ((420, 150), (560, 140), (556, 170)):
        neutron(f, x, y, 8)
    f.arrow(410, 150, 398, 150, INK, 2, 10); f.arrow(568, 140, 584, 136, INK, 2, 10); f.arrow(564, 174, 580, 182, INK, 2, 10)
    f.tex(300, 312, r"\text{fissiossa vapautuu noin}\ 200\,\text{MeV}", "middle", HEAT)
    return f.svg()


def ketju():
    """Ydinajatus, ketjureaktio: three columns of three generations, k = 0,5 / 1 / 2 (neutrons 4-2-1, 2-2-2, 1-2-4)."""
    f = Fig("fy811-ketju", 360, "Kaavakuva kolmesta ketjureaktiosta, kolme sukupolvea ylhäältä alas. Vasemmalla kasvukerroin "
            "k on 0,5: neutroneja on sukupolvissa 4, 2 ja 1, joten ketju sammuu. Keskellä k on 1: neutroneja on joka "
            "sukupolvessa 2, joten ketju pysyy tasaisena. Oikealla k on 2: neutroneja on 1, 2 ja 4, joten ketju kasvaa. "
            "Neutronit ovat harmaita pisteitä.")
    cols = ((150, (4, 2, 1), r"k = 0{,}5", r"\text{sammuu}"), (330, (2, 2, 2), r"k = 1", r"\text{tasainen}"),
            (510, (1, 2, 4), r"k = 2", r"\text{kasvaa}"))
    for i, (x, ns, kt, word) in enumerate(cols):
        f.tex(x, 28, kt, "middle")
        for j, cnt in enumerate(ns):
            y = 92 + j * 88
            if j: f.arrow(x, y - 62, x, y - 30, MUTED, 2, 10)
            for q in range(cnt):
                neutron(f, x + (q - (cnt - 1) / 2) * 30, y, 10)
        f.tex(x, 330, word, "middle", (HEAT if i == 2 else GOOD if i == 1 else MUTED))
        if i < 2: f.line(x + 90, 20, x + 90, 340, RULE, 2, "6 6")
    for j, t in enumerate(("g = 0", "g = 1", "g = 2")):
        f.tex(16, 92 + j * 88, t, "start", MUTED)
    return f.svg()


def reaktori():
    """Ydinvoima: a pressurised-water plant: reactor with fuel and control rods, steam generator, turbine, generator,
    condenser cooled by sea water."""
    f = Fig("fy811-reak", 380, "Periaatekuva painevesireaktorilla toimivasta ydinvoimalasta, ei mittakaavassa. Vasemmalla "
            "reaktorin paineastia: vedessä on polttoainesauvoja ja niiden välissä ylhäältä laskettavia säätösauvoja. Kuuma "
            "vesi kiertää höyrystimeen, jossa toisen piirin vesi kiehuu höyryksi. Höyry pyörittää turbiinia, joka pyörittää "
            "generaattoria. Turbiinista tuleva höyry tiivistyy lauhduttimessa vedeksi, jota jäähdyttää merivesi.")
    # reactor vessel
    f.rect(40, 90, 120, 210, WATER_LIGHT, INK, 3, 30)
    for k in range(4):
        x = 62 + k * 26; f.rect(x, 150, 12, 120, HEAT_LIGHT, INK, 1.5, 3)
    for k in range(3):
        x = 79 + k * 26; f.rect(x, 64, 6, 136, IRON, INK, 1.5, 2)
    f.tex(100, 330, r"\text{reaktori}", "middle")
    f.tex(100, 40, r"\text{säätösauvat}", "middle", MUTED)
    # primary loop to the steam generator
    f.arrow(160, 140, 228, 140, HOT, 6, 18); f.arrow(230, 250, 162, 250, COLD, 6, 18)
    f.rect(230, 110, 70, 170, GLASS, INK, 3, 24)
    f.path("M246,150 Q265,190 246,230 M284,150 Q265,190 284,230", stroke=HOT, w=3)
    f.tex(265, 330, r"\text{höyrystin}", "middle")
    # steam to the turbine
    f.path("M300,130 L360,130 L360,170", stroke=MUTED, w=6)
    f.path("M360,170 L430,150 L430,230 L360,210 Z", ALUMINIUM, INK, 3)
    f.tex(442, 128, r"\text{turbiini}", "start")
    f.line(430, 190, 468, 190, INK, 5)
    f.circle(500, 190, 32, COPPER, INK, 3)
    f.tex(500, 250, r"\text{generaattori}", "middle")
    # condenser and sea water
    f.path("M395,226 L395,280", stroke=MUTED, w=6)
    f.rect(350, 280, 90, 50, COLD_LIGHT, INK, 3, 8)
    f.arrow(440, 300, 560, 300, COLD, 5, 16)
    f.tex(452, 336, r"\text{merivesi}", "start", COLD)
    f.path("M350,305 L300,305 L300,262", stroke=COLD, w=5)
    return f.svg()


def massat():
    """Kaava: the worked example's masses before and after, on a balance; the difference is Q."""
    m0, m1, Q = A_["ex-m-before"], A_["ex-m-after"], A_["ex-Q"]
    f = Fig("fy811-massat", 360, f"Periaatekuva, ei mittakaavassa: vaaka, jonka vasemmassa kupissa on uraani-235-ydin ja neutroni, "
            f"yhteensä {fi(m0, 4)} atomimassayksikköä, ja oikeassa kupissa reaktion tuotteet barium-141, krypton-92 ja kolme "
            f"neutronia, yhteensä {fi(m1, 4)} atomimassayksikköä. Vasen puoli on raskaampi. Massojen erotus "
            f"{fi(m0 - m1, 4)} atomimassayksikköä vapautuu energiana Q, noin {fi(round(Q))} megaelektronivolttia.")
    f.path("M300,90 L280,300 L320,300 Z", METAL_EDGE, INK, 2.5)
    f.rect(240, 300, 120, 14, IRON, INK, 2.5, 4)
    yl, yr = 112, 76                                    # the heavier left side lower
    f.line(110, yl, 490, yr, INK, 5, cap="round"); f.circle(300, 94, 8, INK)
    for x, y in ((110, yl), (490, yr)):
        f.line(x, y, x - 60, y + 90, INK, 2); f.line(x, y, x + 60, y + 90, INK, 2)
        f.path(f"M{x - 80},{y + 90} Q{x},{y + 130} {x + 80},{y + 90} Z", ALUMINIUM, INK, 2.5)
    nucleus(f, 92, yl + 66, 9, 13, r=4.6, seed=3); neutron(f, 150, yl + 78, 8)
    nucleus(f, 452, yr + 70, 6, 8, r=4.6, seed=7); nucleus(f, 498, yr + 74, 4, 6, r=4.6, seed=9)
    for k in range(3): neutron(f, 528 + (k % 2) * 16, yr + 58 + k * 12, 6)
    f.tex(110, yl + 152, rf"{fi(m0, 4)}\,\text{{u}}", "middle")
    f.tex(490, yr + 152, rf"{fi(m1, 4)}\,\text{{u}}", "middle")
    f.tex(110, 30, r"\text{ennen}", "middle", MUTED); f.tex(490, 30, r"\text{jälkeen}", "middle", MUTED)
    f.tex(300, 340, rf"\Delta m = {fi(m0 - m1, 4)}\,\text{{u}} \;\Rightarrow\; Q \approx {fi(round(Q))}\,\text{{MeV}}", "middle", HEAT)
    return f.svg()


def fuusio():
    """Ydinajatus, fuusio: D + T -> He-4 + n; the nuclei repel (Coulomb) until they come very close."""
    f = Fig("fy811-fuu", 320, f"Kaavakuva, ei mittakaavassa: deuteriumin ja tritiumin fuusio. Vasemmalla deuteriumydin, jossa on "
            f"yksi protoni ja yksi neutroni, ja tritiumydin, jossa on yksi protoni ja kaksi neutronia, lähestyvät toisiaan "
            f"suurella nopeudella, vaikka niiden positiiviset varaukset hylkivät toisiaan. Oikealla niistä on syntynyt "
            f"helium-4-ydin ja vapaa neutroni, ja vapautuu energiaa {fi(A_['dt-Q'], 1)} megaelektronivolttia.")
    nucleus(f, 70, 150, 1, 1, r=12, seed=2); f.tex(70, 216, r"{}^{2}\text{H}", "middle")
    nucleus(f, 230, 150, 1, 2, r=12, seed=4); f.tex(230, 216, r"{}^{3}\text{H}", "middle")
    f.arrow(104, 150, 150, 150, COLD, 3, 13); f.arrow(196, 150, 160, 150, COLD, 3, 13)
    f.tex(150, 86, r"\text{hylkivät}", "middle", MUTED)
    f.line(300, 40, 300, 270, RULE, 2, "6 6")
    nucleus(f, 400, 150, 2, 2, r=12, seed=6); f.tex(400, 216, r"{}^{4}\text{He}", "middle")
    neutron(f, 540, 112, 12); f.tex(540, 78, "n", "middle")
    f.arrow(446, 138, 522, 116, INK, 2.5, 12)
    f.block_arrow(440, 190, 520, 236, HEAT_LIGHT, 12, 26, 20)
    f.tex(300, 296, rf"Q = {fi(A_['dt-Q'], 1)}\,\text{{MeV}}", "middle", HEAT)
    return f.svg()


def onkalo():
    """Ydinvoima Suomessa: KBS-3 cross-section: ground, bedrock, a tunnel at about 430 m, a copper canister in bentonite."""
    f = Fig("fy811-onk", 380, "Periaatekuva Olkiluodon loppusijoituslaitoksesta Onkalosta, syvyysasteikko mittakaavassa, "
            "kapseli suurennettuna. Vasemmalla maanpinta ja sen alla kallioperä, jonka läpi kulkee ajotunneli noin 430 metrin "
            "syvyyteen. Syvällä kalliossa on vaakasuora loppusijoitustunneli, jonka lattiaan poratuissa reiissä on kapselit. "
            "Oikealla suurennos: käytetty polttoaine on valurautaisen sisäosan sisällä, sen ympärillä kuparikapseli ja kapselin "
            "ympärillä bentoniittisavi kallioreiässä.")
    f.rect(100, 40, 220, 310, H.grad(f, "fy811-rock", RULE_LIGHT, RULE), INK, 2.5, 6)
    f.rect(100, 40, 220, 18, GOOD_LIGHT, INK, 2, 0)
    f.rect(130, 22, 46, 18, ALUMINIUM, INK, 2)
    y = lambda d: 58 + d / 500 * 270                   # depth (m) -> figure y, to scale
    f.path(f"M152,58 L182,{n(y(150))} L144,{n(y(300))} L196,{n(y(430))}", stroke=INK, w=4)
    f.line(196, y(430), 308, y(430), INK, 8)
    for x in (222, 256, 290):
        f.rect(x - 7, y(430) + 4, 14, 26, COPPER, INK, 1.5, 3)
    for d in (0, 100, 200, 300, 400, 500):
        f.line(100, y(d), 92, y(d), INK, 2)
    f.tex(86, y(0), r"0", "end", MUTED); f.tex(86, y(500), r"500\,\text{m}", "end", MUTED)
    f.tex(250, y(430) - 30, r"\text{noin}\ 430\,\text{m}", "middle")
    f.line(310, y(430) + 18, 340, 120, MUTED, 1.5, "5 5"); f.line(310, y(430) + 18, 340, 320, MUTED, 1.5, "5 5")
    # magnified canister
    f.rect(340, 80, 80, 260, SAND_LIGHT, INK, 2.5, 8)
    f.rect(356, 100, 48, 220, COPPER, INK, 3, 10)
    f.rect(366, 112, 28, 196, IRON, INK, 2, 6)
    for k in range(3): f.rect(370 + k * 8, 122, 4, 176, HEAT_LIGHT, None, 0, 2)
    f.tex(380, 56, r"\text{kapseli}", "middle")
    f.tex(440, 100, r"\text{bentoniitti}", "start"); f.line(420, 100, 436, 100, MUTED, 1.5)
    f.tex(440, 170, r"\text{kupari}", "start"); f.line(404, 170, 436, 170, MUTED, 1.5)
    f.tex(440, 240, r"\text{valurauta}", "start"); f.line(394, 240, 436, 240, MUTED, 1.5)
    f.tex(440, 300, r"\text{polttoaine}", "start"); f.line(382, 290, 436, 300, MUTED, 1.5)
    return f.svg()


def hero():
    """The chapter's opening illustration: a nuclear power plant on a rocky sea shore: a reactor building with a dome,
    a turbine hall, power lines leaving it; inside the dome a glowing core seen through a cutaway."""
    f = H.hero("fy811-hero", "Kuvitus: ydinvoimala kallioisella merenrannalla. Keskellä on lieriön muotoinen reaktorirakennus, "
               "jonka kupolista osa on piirretty auki: sisällä hehkuu reaktorin sydän vedessä. Vieressä on pitkä "
               "turbiinihalli ja sen takana voimalinjan pylväitä. Edessä on meri ja taivaalla muutama pilvi.")
    H.sky(f, "fy811h-sky", 420)
    H.cloud(f, 230, 110, 1.1); H.cloud(f, 960, 80, 0.9)
    f.rect(0, 420, 1200, 180, H.grad(f, "fy811h-sea", WATER_LIGHT, WATER))
    f.path("M0,420 L180,404 L420,410 L760,400 L1200,412 L1200,440 L0,440 Z", RULE, INK, 2.5)
    # turbine hall
    f.rect(640, 300, 330, 110, WHITE, INK, 3, 4)
    for k in range(6): f.rect(664 + k * 50, 330, 30, 22, GLASS, INK, 2, 2)
    f.rect(600, 380, 420, 30, ALUMINIUM, INK, 3, 4)
    # reactor building: a cylinder with a dome, a cutaway showing the core
    f.rect(430, 220, 220, 190, RULE_LIGHT, INK, 3)
    f.path("M430,222 Q540,110 650,222 Z", RULE_LIGHT, INK, 3)
    f.path("M470,250 L610,250 L610,400 L470,400 Z", WATER_LIGHT, INK, 3)
    f.rect(500, 300, 80, 90, H.glow(f, "fy811h-core"), None, 0, 6)
    for k in range(5): f.rect(508 + k * 15, 306, 8, 78, HEAT_LIGHT, INK, 1.5, 2)
    for k in range(4): f.rect(515 + k * 15, 262, 4, 70, IRON, INK, 1, 1)
    # pylons and wires
    p1 = H.pylon(f, 1060, 410, 170); p2 = H.pylon(f, 1160, 410, 150)
    for a, b in zip(p1, p2): H.wire(f, a, b, 18)
    H.wire(f, (970, 320), p1[0], 14)
    # a few spruces on the shore
    for x, h in ((90, 120), (140, 90), (210, 110), (300, 80)): H.spruce(f, x, 412, h)
    return f.svg()


FIGURES = {"hero": hero, "sidosenergia": sidosenergia, "fissio": fissio, "ketju": ketju, "fuusio": fuusio,
           "massat": massat, "reaktori": reaktori, "onkalo": onkalo, "sidosenergia-luku": sidosenergia_read}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "hero": "decorative",
    "sidosenergia": "reveals: E_B/A of H-2, He-4, C-12, Fe-56, Kr-92, Ba-141, U-235 and the fusion/fission directions",
    "fissio": "reveals: n + U-235 -> U-236 -> Ba-141 + Kr-92 + 3 n, about 200 MeV",
    "ketju": "reveals: k = 0,5 dies out, k = 1 steady, k = 2 grows (neutrons per generation)",
    "fuusio": "reveals: D + T -> He-4 + n, Q = 17,6 MeV",
    "massat": "reveals: the worked example's masses 236,0526 u and 235,8666 u and Q = 173 MeV",
    "reaktori": "safe: schematic of a pressurised-water plant (reactor, steam generator, turbine, generator, condenser, sea water)",
    "onkalo": "safe: schematic of the KBS-3 repository at about 430 m: copper canister, cast-iron insert, bentonite",
    "sidosenergia-luku": "safe: E_B/A trend curve for A = 20–240 on a 10 × 0,1 MeV grid, no values marked",
}
