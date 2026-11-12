"""Figures of the FY9 unit fy9-magnetismi-valo (scripts/figlib.py, herolib.py); `python3 scripts/units.py figures
fy9-magnetismi-valo` writes them into content/fi/units/fy9-magnetismi-valo/unit.md. The unit is Finnish, so the
decimal sign is a comma. Colours (FY7 brief): magnetic field #2b8a3e (x into the page), electric field #8a5f22,
current #7048e8; force red, velocity blue (CLAUDE.md); heat loss dark brown-red (orange is acceleration).

hero        the Why scene: an archipelago in cross-section, the mainland's transformer kiosk on the left, a sea
            cable along the seabed, the island's kiosk and two red cottages with lit windows on the right (no text,
            no people)
kartta      the concept map of the review: the magnetic field at the top, then three boxes (forces in a field,
            induction, light), each with three laws
siirto      the hook to scale: the same 40 kW through a 0,50 ohm cable at 230 V and at 20 kV, the share lost as heat
            drawn to scale (38 % and 0,005 %) with the currents
ympyra      a positive particle in a uniform field into the page: the circular path, the velocity tangent and the
            magnetic force towards the centre at four points (counterclockwise on the page)
"""
import math
import figlib
from figlib import (Fig, INK, MUTED, WHITE, RULE, RULE_LIGHT, GLASS, SAND_LIGHT, SAND, SAND_DARK, HEAT, HEAT_LIGHT, HOT,
                    HOT_LIGHT, COLD, COLD_LIGHT, WATER, WATER_LIGHT, ICE, IRON, ALUMINIUM, METAL_EDGE, COPPER, GOOD,
                    GOOD_LIGHT, n, fi)
import herolib as H

figlib.set_language({}, ",")

FIELD, EFIELD, CURRENT, FORCE, VEL = GOOD, "#8a5f22", "#7048e8", HOT, COLD
LAMP = "#ffd43b"
LOSS = "#8f3b1b"        # power lost as heat: a dark brown-red, not the orange of acceleration

# the hook (computed here and in sovella/answers.py "inq-hook-*", quoted in unit.md and inquiry.json)
P_HOOK = 40e3          # W
R_HOOK = 0.50          # ohm, both conductors of the 1,0 km cable together
U_LOW, U_HIGH = 230.0, 20e3


def hero():
    """An archipelago in cross-section at dusk: the mainland on the left with a lattice pylon line ending at a grey
    transformer kiosk; from it a dark sea cable runs down the rocky shore, along the sandy seabed under the water and
    up to the island on the right, where a second kiosk feeds a red cottage with a lit window, a birch and a spruce
    behind it. Far islands line the horizon; a few fish and stones on the seabed."""
    f = H.hero("fy9mv-hero", "Kuvitus: saaristomaisema poikkileikkauksena iltahämärässä. Vasemmalla mantereen rannalla "
               "voimajohdon pylväs ja harmaa muuntamo. Muuntamosta lähtee tumma merikaapeli, joka laskeutuu kalliorantaa "
               "pitkin meren pohjaan, kulkee hiekkapohjaa pitkin veden alla ja nousee oikealla saareen. Saaressa on toinen "
               "pieni muuntamo ja punainen mökki, jonka ikkunasta loistaa valo. Mökin takana koivu ja kuusi, "
               "taivaanrannassa kaukaisia saaria.")
    H.sky(f, "fy9mv", 360, "#a5c8e8", "#f6e3c8")
    H.sun(f, "fy9mv", 640, 300, 40, rays=False)
    # far islands on the horizon
    for x0, w, h in ((330, 160, 26), (520, 90, 18), (720, 150, 24)):
        f.path(f"M{x0},362 Q{x0 + w * 0.3},{362 - h} {x0 + w / 2},{362 - h} Q{x0 + w * 0.7},{362 - h} {x0 + w},362 Z", "#4c7a5a")
        H.forest(f, 362 - h * 0.7, h * 0.9, 14, "#3d6b4c", seed=x0, x0=x0 + w * 0.2, x1=x0 + w * 0.8, depth=int(h * 0.7))
    # the sea in cross-section
    surf = 362
    f.rect(0, surf, 1200, 238, H.grad(f, "fy9mv-sea", WATER_LIGHT, "#1d4f7f"), None, 0)
    for x in range(300, 900, 46):
        f.path(f"M{x},{surf + 8} q12,-6 24,0", "none", WHITE, 2, extra='stroke-opacity="0.7" stroke-linecap="round"')
    # the seabed
    bed = "M0,600 L0,540 Q200,548 300,560 Q600,580 900,558 Q1000,548 1200,540 V600 Z"
    f.path(bed, H.grad(f, "fy9mv-bed", SAND, "#b08a4a"), INK, 2.5)
    for k, (x, y, r) in enumerate(((420, 574, 9), (455, 578, 6), (760, 572, 11), (800, 575, 7))):
        f.add(f'<ellipse cx="{x}" cy="{y}" rx="{r * 1.5}" ry="{r}" fill="{IRON}" stroke="{INK}" stroke-width="2"/>')
    # the mainland: a rocky shore sloping into the sea
    land_l = "M0,330 L230,330 Q262,334 290,362 Q330,420 340,470 Q350,520 300,560 L0,560 Z"
    f.path(land_l, H.grad(f, "fy9mv-rockl", "#9aa3a8", "#6c757d"), INK, 3)
    f.path("M0,330 L230,330 Q246,331 256,338 L0,338 Z", "#5c9a5c", INK, 2)
    # the island
    land_r = "M1200,326 L960,326 Q930,330 905,362 Q868,420 862,470 Q856,520 900,558 L1200,558 Z"
    f.path(land_r, H.grad(f, "fy9mv-rockr", "#9aa3a8", "#6c757d"), INK, 3)
    f.path("M1200,326 L960,326 Q944,327 932,336 L1200,336 Z", "#5c9a5c", INK, 2)
    # the pylon line and the mainland kiosk
    arms = H.pylon(f, 60, 330, 170, 0.9)
    k_x, k_y = 150, 330
    f.rect(k_x, k_y - 70, 70, 70, ALUMINIUM, INK, 3, 3)
    f.path(f"M{k_x - 6},{k_y - 70} L{k_x + 35},{k_y - 88} L{k_x + 76},{k_y - 70} Z", IRON, INK, 3)
    f.rect(k_x + 12, k_y - 54, 22, 54, METAL_EDGE, INK, 2)
    for i in range(3): f.line(k_x + 42, k_y - 52 + 10 * i, k_x + 62, k_y - 52 + 10 * i, INK, 2)
    for a in arms[2:]: H.wire(f, a, (k_x + 35, k_y - 88), 14, INK, 2)
    # the island kiosk and the cottages
    q_x = 975
    f.rect(q_x, 326 - 52, 52, 52, ALUMINIUM, INK, 3, 3)
    f.path(f"M{q_x - 5},{326 - 52} L{q_x + 26},{326 - 66} L{q_x + 57},{326 - 52} Z", IRON, INK, 3)
    for i in range(3): f.line(q_x + 12, 326 - 40 + 9 * i, q_x + 40, 326 - 40 + 9 * i, INK, 2)
    H.spruce(f, 1150, 326, 130)
    H.birch(f, 1060, 326, 120)
    H.red_house(f, 1040, 326, 110, 70)
    # lit windows: the red_house windows painted warm
    for wx in (1070,):
        f.rect(wx, 326 - 70 * 0.72, 40, 70 * 0.4, LAMP, INK, 2)
        f.line(wx + 20, 326 - 70 * 0.72, wx + 20, 326 - 70 * 0.32, WHITE, 3)
    # the cable: underground from the kiosk, down the shore, along the seabed and up to the island kiosk
    cable = (f"M{k_x + 35},{k_y} L{k_x + 35},{k_y + 14} Q{k_x + 60},{k_y + 20} 250,350 Q305,400 318,470 Q330,535 380,552 "
             f"Q600,570 820,552 Q880,540 885,470 Q890,400 930,350 Q960,340 {q_x + 26},340 L{q_x + 26},326")
    f.path(cable, "none", INK, 9, extra='stroke-linecap="round" stroke-linejoin="round"')
    f.path(cable, "none", COPPER, 3, extra='stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="14 10"')
    # fish
    for x, y, s in ((520, 470, 1.0), (580, 500, 0.8), (690, 450, 0.9)):
        f.path(f"M{x},{y} q{18 * s},{-10 * s} {36 * s},0 q{-18 * s},{10 * s} {-36 * s},0 Z", "#8fb0c8", INK, 1.5)
        f.path(f"M{x + 36 * s},{y} l{10 * s},{-7 * s} v{14 * s} Z", "#8fb0c8", INK, 1.5)
    return f.svg()


def kartta():
    """The concept map, stacked for a phone: the magnetic field at the top, a spine down the left and three boxes
    (forces in a field, induction, light), each with three laws and a grey word beside each."""
    f = Fig("fy9mv-kartta", 704, "Käsitekartta. Ylhäällä solmu magneettikenttä: magneettivuon tiheys B ja magneettivuo fii = B A. Siitä lähtee "
            "alas kolme haaraa. Voimat kentässä, liikkuva varaus: magneettinen voima F M = Q v B kohtisuora, virtajohtimeen "
            "kohdistuva voima F M = I l B kohtisuora ja suoran johtimen kenttä B = myy nolla I per 2 pii r. Induktio, "
            "muuttuva vuo: induktiolaki e = miinus N delta fii per delta t, generaattorin huippujännite u 0 = N A B kertaa "
            "2 pii f ja muuntaja N 1 per N 2 = U 1 per U 2. Valo, sähkömagneettinen aalto: taittumislaki sini alfa 1 per "
            "sini alfa 2 = n 2 per n 1, hilayhtälö d sini alfa = n lambda ja Malusin laki I = I 0 kertaa kosini toiseen "
            "theeta.", width=380, size=20)
    groups = [
        ("voimat kentässä", "liike tai virta", [(r"F_\text{M} = QvB_\perp", "varaus"), (r"F_\text{M} = I\ell B_\perp", "johdin"),
                                                (r"B = \mu_0 I/(2\pi r)", "johtimen kenttä")]),
        ("induktio", "muuttuva vuo", [(r"e = -N\,\Delta\Phi/\Delta t", "induktiolaki"), (r"u_0 = NAB \cdot 2\pi f", "generaattori"),
                                      (r"N_1/N_2 = U_1/U_2", "muuntaja")]),
        ("valo", "sm-aalto", [(r"\sin\alpha_1/\sin\alpha_2 = n_2/n_1", "taittuminen"), (r"d\sin\alpha = n\lambda", "hila"),
                              (r"I = I_0\cos^2\theta", "polarisaatio")]),
    ]
    hub_y, hub_h, x_box, gh, top = 8, 72, 44, 188, 100
    spine = 24
    f.line(spine, hub_y + hub_h, spine, top + 2 * (gh + 16) + 22, RULE, 3)
    f.rect(8, hub_y, 364, hub_h, GOOD_LIGHT, FIELD, 2.5, 12)
    f.tex(190, hub_y + 22, r"\text{magneettikenttä}", "middle", INK)
    f.tex(190, hub_y + 51, r"\overline{B},\ \Phi = BA", "middle", INK)
    for k, (head, sub, rows) in enumerate(groups):
        y = top + k * (gh + 16)
        f.line(spine, y + 22, x_box, y + 22, RULE, 3)
        f.rect(x_box, y, 372 - x_box, gh, WHITE, MUTED, 2, 10)
        f.tex(x_box + 14, y + 22, r"\textbf{" + head + "}", "start", INK)
        f.tex(362, y + 22, r"\text{" + sub + "}", "end", MUTED, size=17)
        f.line(x_box + 10, y + 42, 362, y + 42, RULE_LIGHT, 1.5)
        for j, (law, word) in enumerate(rows):
            yy = y + 68 + j * 52
            long_law = len(law) > 28
            f.tex(x_box + 14, yy - (9 if long_law else 0), law, "start", INK, size=18 if long_law else None)
            if word: f.tex(362, yy + (13 if long_law else 0), r"\text{" + word + "}", "end", MUTED, size=17)
    return f.svg()


def siirto():
    """The hook to scale: one bar of 40 kW per transmission voltage. The brown-red part is what the cable turns into
    internal energy (R I^2), drawn to scale: 37,8 % at 230 V, 0,005 % at 20 kV (a hair line, labelled). The current
    in each case is written in the current's violet."""
    f = Fig("fy9mv-siirto", 360, "Kaavakuva mittakaavassa: sama 40 kilowatin teho siirretään kaapelilla, jonka resistanssi "
            "on 0,50 ohmia. Ylempi palkki: jännitteellä 230 volttia virta on 174 ampeeria, ja palkin ruskeanpunainen osa, "
            "kaapelissa lämmöksi muuttuva teho 15 kilowattia, on 38 prosenttia koko palkista. Alempi palkki: "
            "jännitteellä 20 kilovolttia virta on 2,0 ampeeria, ja lämmöksi muuttuu vain 2,0 wattia, 0,005 prosenttia, "
            "mikä on palkissa ohuempi kuin viiva.", size=24)
    x0, W, hbar = 24, 552, 46
    f.tex(300, 22, r"P = 40\,\text{kW},\ R = 0{,}50\,\Omega", "middle", INK)
    rows = []
    for U in (U_LOW, U_HIGH):
        I = P_HOOK / U
        rows.append((U, I, R_HOOK * I ** 2))
    for k, (U, I, Ph) in enumerate(rows):
        y = 74 + k * 140
        f.tex(x0, y, (r"U = 230\,\text{V}" if k == 0 else r"U = 20\,\text{kV}"), "start", INK)
        f.tex(x0 + W, y, (r"I \approx 174\,\text{A}" if k == 0 else r"I = 2{,}0\,\text{A}"), "end", CURRENT)
        yb = y + 26
        share = Ph / P_HOOK
        wl = max(W * share, 2)
        f.rect(x0, yb, W, hbar, GLASS, INK, 2.5, 4)
        f.rect(x0 + W - wl, yb, wl, hbar, LOSS, None, 0)
        f.rect(x0, yb, W, hbar, "none", INK, 2.5, 4)
        if k == 0:
            f.tex(x0 + 12, yb + hbar / 2, r"\text{perille } 25\,\text{kW}", "start", INK, size=24)
            f.tex(x0 + W - 12, yb + hbar / 2, r"15\,\text{kW}", "end", WHITE, size=24)
            f.tex(x0 + W, yb + hbar + 24, r"\text{lämmöksi } 38\,\%", "end", LOSS, size=24)
        else:
            f.tex(x0 + 12, yb + hbar / 2, r"\text{perille lähes } 40\,\text{kW}", "start", INK, size=24)
            f.tex(x0 + W, yb + hbar + 24, r"\text{lämmöksi } 2{,}0\,\text{W} = 0{,}005\,\%", "end", LOSS, size=24)
    return f.svg()


def _cross(f, x, y, a=7):
    f.line(x - a, y - a, x + a, y + a, FIELD, 2.4)
    f.line(x - a, y + a, x + a, y - a, FIELD, 2.4)


def ympyra():
    """A positive particle in a uniform magnetic field into the page (green crosses). The dashed circle is its path,
    counterclockwise on the page. At the bottom, right, top and left points the velocity (blue) is tangent and the
    magnetic force (red) points to the centre; one of each is labelled, and the radius r is marked."""
    f = Fig("fy9mv-ympyra", 420, "Kaavakuva: positiivinen hiukkanen homogeenisessa magneettikentässä, joka osoittaa "
            "paperiin sisään (vihreät ristit). Hiukkasen rata on katkoviivalla piirretty ympyrä, jota se kiertää "
            "vastapäivään. Neljässä radan kohdassa sininen nopeusnuoli on radan suuntainen ja punainen magneettisen "
            "voiman nuoli osoittaa ympyrän keskipisteeseen, kohtisuoraan nopeutta vastaan. Säde r on merkitty "
            "keskipisteestä rataan.", size=24)
    cx, cy, R = 250, 214, 140
    for i in range(8):
        for j in range(6):
            x, y = 40 + 62 * i, 34 + 72 * j
            if abs(math.hypot(x - cx, y - cy) - R) < 34 or math.hypot(x - cx, y - cy) < 26: continue
            if x > 470: continue
            _cross(f, x, y)
    f.circle(cx, cy, R, "none", INK, 2.5)
    f.add(f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="none" stroke="{GLASS}" stroke-width="2.5" stroke-dasharray="10 8"/>')
    f.circle(cx, cy, 5, INK)
    f.line(cx, cy, cx + R * math.cos(math.radians(-40)), cy + R * math.sin(math.radians(-40)), INK, 2, "6 5")
    f.tex(cx + 62, cy - 30, r"r", "middle", INK)
    # four points: (angle on the page, velocity direction) for counterclockwise motion on the page
    for deg in (90, 0, 270, 180):        # bottom, right, top, left (SVG angle: y down)
        a = math.radians(deg)
        px, py = cx + R * math.cos(a), cy + R * math.sin(a)
        tx, ty = math.sin(a), -math.cos(a)          # tangent for counterclockwise on screen
        f.arrow(px, py, px + 78 * tx, py + 78 * ty, VEL, 4, 15)
        f.arrow(px, py, px - 62 * math.cos(a), py - 62 * math.sin(a), FORCE, 4, 15)
        f.circle(px, py, 12, HOT_LIGHT, INK, 2)
        f.tex(px, py, r"+", "middle", INK, size=20)
    bx, by = cx, cy + R
    f.tex(bx + 84, by + 4, r"\overline{v}", "start", VEL)
    f.tex(bx + 14, by - 40, r"\overline{F}_\text{m}", "start", FORCE)
    f.tex(590, 402, r"\overline{B}\ \text{paperiin}", "end", FIELD, bg=True)
    f.tex(590, 40, r"r = mv/(qB)", "end", INK)
    return f.svg()


FIGURES = {"hero": hero, "kartta": kartta, "siirto": siirto, "ympyra": ympyra}
REUSE = {"kartta": "reveals: the key laws of FY7 magnetism, induction and light",
         "siirto": "reveals: 40 kW through 0,50 ohm loses 38 % at 230 V and 0,005 % at 20 kV",
         "ympyra": "reveals: the magnetic force on a positive charge points to the centre, counterclockwise in B into the page"}
