"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy8-5` writes them into lesson.md."""
import math, random
from figlib import (Fig, INK, MUTED, WHITE, RULE, RULE_LIGHT, HOT, COLD, COLD_LIGHT, WATER, WATER_LIGHT, GLASS, IRON,
                    METAL_EDGE, ALUMINIUM, SAND, SAND_LIGHT, SAND_DARK, HEAT, HEAT_LIGHT, PAPER, GOOD, n)

A0 = 0.0529   # Bohr radius, nm


def sample_1s(rng):
    """One position measurement of hydrogen's 1s electron (a0 units), seen through along y: (x, z, r)."""
    r = -0.5 * math.log((1 - rng.random()) * (1 - rng.random()) * (1 - rng.random()))
    mu, ph = 2 * rng.random() - 1, 2 * math.pi * rng.random()
    return r * math.sqrt(1 - mu * mu) * math.cos(ph), r * mu, r


def wavy(f, x1, y1, x2, y2, color, waves=4, amp=7, w=3, head=14):
    """A photon: a wavy shaft from (x1, y1) and a filled head at (x2, y2)."""
    L = math.hypot(x2 - x1, y2 - y1); ux, uy = (x2 - x1) / L, (y2 - y1) / L
    px, py = -uy, ux
    shaft = L - head
    pts = []
    for k in range(121):
        s = shaft * k / 120
        a = amp * math.sin(2 * math.pi * waves * k / 120)
        pts.append((x1 + ux * s + px * a, y1 + uy * s + py * a))
    f.path("M" + " L".join(f"{n(a)},{n(b)}" for a, b in pts), stroke=color, w=w, extra='stroke-linecap="round"')
    bx, by = x2 - ux * head, y2 - uy * head
    hw = head * 0.5
    f.path(f"M{n(x2)},{n(y2)} L{n(bx - uy * hw)},{n(by + ux * hw)} L{n(bx + uy * hw)},{n(by - ux * hw)} Z", fill=color)


def string_modes():
    f = Fig("fy85-string", 330, "Kaavakuva: molemmista päistä kiinnitetyn kielen kolme ensimmäistä seisovaa aaltoa. Ylimmässä kieli "
            "värähtelee yhtenä kupuna eikä sen keskellä ole solmua, keskimmäisessä on yksi solmu ja kaksi kupua, alimmassa kaksi "
            "solmua ja kolme kupua. Muita värähtelytapoja ei synny, koska kielen päät pysyvät paikallaan. Mitä enemmän "
            "solmuja, sitä suurempi värähtelyn energia.")
    x0, x1 = 112, 452
    for row, (y, m) in enumerate(((86, 1), (186, 2), (286, 3))):
        f.rect(x0 - 16, y - 34, 12, 68, IRON, INK, 2, 2)
        f.rect(x1 + 4, y - 34, 12, 68, IRON, INK, 2, 2)
        for sgn, col, dash in ((1, WATER, None), (-1, WATER_LIGHT, "7 5")):
            d = "M" + " L".join(f"{n(x0 + (x1 - x0) * k / 100)},{n(y - sgn * 30 * math.sin(math.pi * m * k / 100))}" for k in range(101))
            f.path(d, stroke=col, w=3, extra=(f'stroke-dasharray="{dash}"' if dash else ""))
        f.line(x0, y, x1, y, RULE, 1.5, "4 4")
        for j in range(1, m):
            f.circle(x0 + (x1 - x0) * j / m, y, 6, INK)
        f.tex(x0 - 30, y, f"{m}.", "end")
        f.tex(x1 + 30, y, [r"\text{0 solmua}", r"\text{1 solmu}", r"\text{2 solmua}"][row], "start", w=110)
    f.tex(x0 + (x1 - x0) / 2, 230, r"\text{solmu}", "middle", MUTED, bg=True)
    f.line(x0 + (x1 - x0) / 2, 218, x0 + (x1 - x0) / 2, 196, MUTED, 1.5)
    return f.svg()


def orbital_nodes():
    f = Fig("fy85-nodes", 360, "Periaatekuva, ei mittakaavassa: vetyatomin kolmen orbitaalin poikkileikkaukset ytimen kautta. "
            "1s-orbitaali on pallo, jossa ei ole solmua. 2s-orbitaali on pallo, jonka sisällä on solmupallo: sen kohdalla "
            "elektronia ei havaita, ja sen sisä- ja ulkopuolella aalto värähtelee vastakkaisissa vaiheissa. 2p-orbitaalissa "
            "on kaksi lohkoa, yksi ytimen kummallakin puolella, ja niiden välissä ytimen kautta kulkeva solmutaso. Ydin on punainen piste.")
    f.defs_add(f'<radialGradient id="fy85-cloud"><stop offset="0" stop-color="{COLD}" stop-opacity="0.95"/><stop offset="1" stop-color="{COLD}" stop-opacity="0.12"/></radialGradient>')
    f.defs_add(f'<radialGradient id="fy85-ring" r="0.5"><stop offset="0.42" stop-color="{COLD}" stop-opacity="0"/><stop offset="0.5" stop-color="{COLD}" stop-opacity="0.12"/>'
               f'<stop offset="0.72" stop-color="{COLD}" stop-opacity="0.55"/><stop offset="1" stop-color="{COLD}" stop-opacity="0.08"/></radialGradient>')
    cy = 150
    for x in (200, 400):
        f.line(x, 30, x, 300, RULE, 2, "6 6")
    # 1s
    f.circle(100, cy, 48, "url(#fy85-cloud)")
    f.circle(100, cy, 48, "none", COLD, 2)
    # 2s: core, node sphere (dashed), outer shell
    f.circle(300, cy, 86, "url(#fy85-ring)")
    f.circle(300, cy, 86, "none", COLD, 2)
    f.circle(300, cy, 22, "url(#fy85-cloud)")
    f.circle(300, cy, 34, "none", MUTED, 2)
    f.add(f'<circle cx="300" cy="{cy}" r="34" fill="none" stroke="{WHITE}" stroke-width="2" stroke-dasharray="6 5"/>')
    # 2p: two lobes and the nodal plane
    for sgn in (1, -1):
        pts = []
        for k in range(81):
            th = -1.54 + 3.08 * k / 80
            rr = 84 * max(math.cos(th), 0) ** 1.4
            pts.append((500 + rr * math.sin(th), cy - sgn * rr * math.cos(th)))
        f.path("M" + " L".join(f"{n(a)},{n(b)}" for a, b in pts) + " Z", "url(#fy85-cloud)", COLD, 2)
    f.line(420, cy, 580, cy, MUTED, 2, "6 5")
    for x in (100, 300, 500):
        f.circle(x, cy, 6, HOT, WHITE, 1.5)
    for x, name, nodes in ((100, "1s", r"\text{ei solmua}"), (300, "2s", r"\text{solmupallo}"), (500, "2p", r"\text{solmutaso}")):
        f.tex(x, 276, r"\text{" + name + "}", "middle")
        f.tex(x, 316, nodes, "middle", MUTED, w=150)
    return f.svg()


def cloud_panels():
    f = Fig("fy85-cloud", 372, "Pistekuva mittakaavassa: vetyatomin 1s-elektronin paikka on mitattu yhden kerran, 20 kertaa ja "
            "1000 kertaa, ja jokainen mittaustulos on merkitty pisteeksi. Yksi piste ei kerro jakaumasta mitään, 20 pistettä "
            "kasautuu ytimen ympärille, ja 1000 pisteestä muodostuu pilvi, joka on tihein ytimen lähellä ja harvenee "
            "ulospäin. Kolmanteen kuvaan on piirretty ympyrä, jonka sisällä on 90 prosenttia osumista: se on 1s-orbitaalin "
            "raja, säde 0,14 nm. Rajan ulkopuolelle jääneet osumat ovat harmaita. Ydin on punainen piste.")
    rng = random.Random(85)
    sc = 22.0                      # px per a0
    R90 = 2.66116 * sc             # lesson-answers R1s-90 = 0,1408 nm
    cy = 158
    for x in (200, 400):
        f.line(x, 24, x, 296, RULE, 2, "6 6")
    for cx, N in ((100, 1), (300, 20), (500, 1000)):
        if N == 1000:
            f.circle(cx, cy, R90, COLD_LIGHT)
        dots_in, dots_out = [], []
        while len(dots_in) + len(dots_out) < N:
            x, z, r = sample_1s(rng)
            if N == 1 and r < 1.0:
                continue                                   # one measurement drawn clear of the nucleus
            if abs(x * sc) > 90 or abs(z * sc) > 128:
                continue                                   # outside the panel (a few hits of 1000)
            (dots_in if (r < 2.66116 or N < 1000) else dots_out).append((cx + x * sc, cy - z * sc))
        rad = 5 if N < 100 else 2.2
        for x, y in dots_out:
            f.circle(x, y, rad, MUTED)
        for x, y in dots_in:
            f.circle(x, y, rad, COLD)
        if N == 1000:
            f.circle(cx, cy, R90, "none", COLD, 2.5)
            f.line(cx + R90 * 0.71, cy - R90 * 0.71, cx + 64, cy - 98, INK, 1.5)
            f.tex(cx + 66, cy - 112, r"90\,\%", "middle", w=70)
        f.circle(cx, cy, 6, HOT, WHITE, 1.5)
        f.tex(cx, 318, f"N = {N}", "middle", w=130)
    # scale bar 0,1 nm
    L = 0.1 / A0 * sc
    f.line(40, 354, 40 + L, 354, INK, 2.5)
    f.line(40, 347, 40, 361, INK, 2)
    f.line(40 + L, 347, 40 + L, 361, INK, 2)
    f.tex(40 + L + 10, 354, r"0{,}1\,\text{nm}", "start", w=90)
    return f.svg()


def levels():
    f = Fig("fy85-levels", 396, "Vetyatomin energiatasot mittakaavassa ja niiden orbitaalit laatikoina. Kuorella n = 1 on yksi "
            "orbitaali 1s energialla −13,6 eV. Kuorella n = 2 energialla −3,40 eV on 2s-orbitaali ja kolme 2p-orbitaalia, "
            "yhteensä neljä. Kuorella n = 3 energialla −1,51 eV ovat 3s, kolme 3p- ja viisi 3d-orbitaalia, yhteensä yhdeksän. "
            "Ylimpänä katkoviiva E = 0, jonka yläpuolella elektroni on irti atomista. Nuoli näyttää elektronin siirtymän "
            "3d-orbitaalilta 2p-orbitaalille; samalla syntyy fotoni, jonka aallonpituus on 656 nm, punaista valoa. "
            "Jokaisella orbitaalilla voi olla enintään kaksi elektronia.")
    Y = lambda E: 40 + (-E) / 13.6 * 320
    ax = 118
    f.arrow(ax, Y(-13.6) + 14, ax, 18, INK, 2.5, 13)
    f.tex(ax + 14, 22, r"E\ (\text{eV})", "start", w=90)
    f.line(ax, Y(0), 590, Y(0), MUTED, 1.5, "6 5")
    for E, lab in ((0, "0"), (-1.511, r"-1{,}51"), (-3.40, r"-3{,}40"), (-13.6, r"-13{,}6")):
        f.line(ax - 6, Y(E), ax, Y(E), INK, 2)
        f.tex(ax - 10, Y(E) + (-4 if E == 0 else 4 if E == -1.511 else 0), lab, "end", w=80)
    bw, gap = 26, 4
    rows = [(1, -13.6, [("s", 1)]), (2, -3.40, [("s", 1), ("p", 3)]), (3, -1.511, [("s", 1), ("p", 3), ("d", 5)])]
    xs = {"s": 178, "p": 262, "d": 404}
    boxes = {}
    for nq, E, groups in rows:
        y = Y(E)
        for sub, cnt in groups:
            x = xs[sub]
            f.tex(x - 6, y, r"\text{" + f"{nq}{sub}" + "}", "end", w=46)
            for j in range(cnt):
                bx = x + j * (bw + gap)
                f.rect(bx, y - 9, bw, 18, WHITE, INK, 2, 2)
                boxes[(nq, sub, j)] = (bx + bw / 2, y)
    # transition 3d -> 2p and the photon
    xa, ya = boxes[(3, "d", 0)]; xb, yb = boxes[(2, "p", 2)]
    f.arrow(xa, ya + 10, xb + 4, yb - 11, INK, 2.5, 11)
    wavy(f, xb + 30, yb + 28, 520, 230, HOT, waves=5, amp=7)
    f.tex(476, 188, "hf", "start", HOT, w=50)
    f.tex(520, 258, r"\lambda = 656\,\text{nm}", "middle", HOT, w=160)
    f.tex(160, 300, r"\text{orbitaalissa enintään } 2\ e^-", "start", w=300)
    return f.svg()


def hero():
    """The chapter's opening illustration: an open chemistry book on a desk, one page with a planet-like orbit picture,
    the other with an electron cloud and the lobes of a p orbital; a desk lamp lights it."""
    f = Fig("fy85-hero", 600, "Kuvitus: pöydällä on avoin kirja. Vasemmalla sivulla on vanha atomikuva, jossa pieni elektroni "
            "kiertää ydintä ympyrärataa pitkin. Oikealla sivulla sama atomi on piirretty sinisenä pistepilvenä, ja sen "
            "vieressä on kaksilohkoinen p-orbitaali. Pöytävalaisin valaisee kirjaa.", width=1200, hero=True)
    f.defs_add(f'<linearGradient id="fy85h-wall" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{PAPER}"/><stop offset="1" stop-color="{SAND_LIGHT}"/></linearGradient>')
    f.defs_add(f'<linearGradient id="fy85h-desk" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{SAND}"/><stop offset="1" stop-color="#a97a35"/></linearGradient>')
    f.defs_add(f'<radialGradient id="fy85h-light" cx="0.5" cy="0" r="0.9"><stop offset="0" stop-color="{HEAT_LIGHT}" stop-opacity="0.55"/><stop offset="1" stop-color="{HEAT_LIGHT}" stop-opacity="0"/></radialGradient>')
    f.defs_add(f'<radialGradient id="fy85h-cloud"><stop offset="0" stop-color="{COLD}" stop-opacity="0.85"/><stop offset="1" stop-color="{COLD}" stop-opacity="0"/></radialGradient>')
    f.rect(0, 0, 1200, 600, "url(#fy85h-wall)")
    f.rect(0, 330, 1200, 270, "url(#fy85h-desk)")
    f.line(0, 330, 1200, 330, "#a97a35", 3)
    # lamp light cone
    f.path("M930,150 L560,560 L1140,560 Z", "url(#fy85h-light)")
    # book: two pages with a spine shadow
    f.path("M330,520 L600,540 L600,330 L360,300 Z", SAND_DARK, INK, 3)
    f.path("M870,520 L600,540 L600,330 L840,300 Z", SAND_DARK, INK, 3)
    f.path("M342,508 L600,528 L600,318 L370,290 Z", WHITE, INK, 3)
    f.path("M858,508 L600,528 L600,318 L830,290 Z", WHITE, INK, 3)
    f.path("M596,320 L604,320 L604,528 L596,528 Z", RULE)
    # left page: planet-like orbit
    f.add(f'<ellipse cx="478" cy="410" rx="88" ry="64" fill="none" stroke="{MUTED}" stroke-width="3"/>')
    f.circle(478, 410, 13, HOT, INK, 2)
    f.circle(560, 384, 9, COLD, INK, 2)
    # right page: electron cloud and a p orbital
    f.circle(686, 404, 66, "url(#fy85h-cloud)")
    rng = random.Random(7)
    for _ in range(140):
        x, z, r = sample_1s(rng)
        if r < 3.6:
            f.circle(686 + x * 17, 404 - z * 17, 2.2, COLD)
    f.circle(686, 404, 6, HOT, WHITE, 1.5)
    for sgn in (1, -1):
        pts = []
        for k in range(41):
            th = -1.2 + 2.4 * k / 40
            rr = 46 * math.cos(th) ** 0.7
            pts.append((790 + rr * math.sin(th), 412 - sgn * (4 + rr * math.cos(th))))
        f.path(f"M790,{412 - sgn * 4} L" + " L".join(f"{n(a)},{n(b)}" for a, b in pts) + " Z", COLD_LIGHT, COLD, 2.5)
    f.circle(790, 412, 5, HOT, WHITE, 1.5)
    # lamp
    f.path("M1040,560 h120 v-16 q0,-12 -12,-12 h-96 q-12,0 -12,12 Z", IRON, INK, 3)
    f.path("M1100,532 L1060,250", stroke=INK, w=8, extra='stroke-linecap="round"')
    f.path("M1060,250 L960,150", stroke=INK, w=8, extra='stroke-linecap="round"')
    f.path("M990,120 L900,190 L880,165 L960,96 Z", HOT, INK, 3)
    f.circle(1060, 250, 10, METAL_EDGE, INK, 2.5)
    # pencil and a mug
    f.path("M250,560 L420,548 L428,556 L258,570 Z", HEAT_LIGHT, INK, 2.5)
    f.path("M420,548 L446,552 L428,556 Z", SAND, INK, 2)
    f.path("M120,420 h90 v110 q0,14 -14,14 h-62 q-14,0 -14,-14 Z", COLD_LIGHT, INK, 3)
    f.path("M210,445 q34,0 34,30 q0,30 -34,30", stroke=INK, w=5)
    return f.svg()


FIGURES = {"hero": hero, "string": string_modes, "nodes": orbital_nodes, "cloud": cloud_panels, "levels": levels}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "string": "safe: three standing waves of a string with 0, 1 and 2 nodes",
    "nodes": "safe: cross-sections of 1s, 2s and 2p with their nodes",
    "cloud": "reveals: 90 % of the hits lie inside the 1s boundary of radius 0,14 nm",
    "levels": "reveals: the 3d -> 2p photon is 656 nm; orbitals per shell 1, 4, 9",
}
