"""Figures of the FY9 unit fy9-sahkokentta (scripts/figlib.py, herolib.py); `python3 scripts/units.py figures
fy9-sahkokentta` writes them into content/fi/units/fy9-sahkokentta/unit.md. The unit is Finnish, so the decimal sign is
a comma. Colours, one meaning each (as in the FY6 chapters): the electric field green, forces red, velocity blue; a
positive charge is a light red ball with a + sign and a negative one a light blue ball with a − sign, so a sign is
never told by colour alone.

hero        the Why scene: a winter evening in a hallway, a hand in a knitted sleeve reaching for the metal door handle
            and a small spark jumping across the gap; a wool rug on the floor, a snowy window, a radiator (no text)
kartta      the concept map of the review: charge makes a field, F = qE, then four boxes (charge and force, field and
            potential, the capacitor, components and safety), each with three laws
kipina      the hook answered: the fingertip and the handle's metal plate 3 mm apart, the induced charges and the green
            field across the gap, and the numbers U = Ed (E the breakdown strength), Q = CU and W = 1/2 C U^2 beside it
levyt       the Kaava figure: two plates at 200 V and 0 V, the green uniform field, dashed equipotentials every 50 V,
            a proton with its red force along the field and an electron with its red force against it
etuvastus   the LED circuit for "Johda itse": a source U, the series resistor R and an LED in the forward direction
            in one loop, the LED's voltage U_D and the violet current I (no numbers)
"""
import math
import figlib
from figlib import (Fig, INK, MUTED, WHITE, RULE, RULE_LIGHT, GLASS, SAND_LIGHT, SAND, SAND_DARK, GRAIN, HEAT_LIGHT, HEAT,
                    HOT, HOT_LIGHT, COLD, COLD_LIGHT, ICE, ALUMINIUM, METAL_EDGE, IRON, GOOD, GOOD_LIGHT, n, fi)
import herolib as H

figlib.set_language({}, ",")
FIELD, FORCE = GOOD, HOT
CUR = "#7048e8"     # conventional current (FY6: violet)

# the hook (computed here and quoted in unit.md, inquiry.json and teacher.md)
E_AIR = 3e6                  # V/m, the breakdown strength of air
GAP = 3.0e-3                 # m, the spark's length
C_BODY = 100e-12             # F, the order of a person's capacitance to the surroundings
U_HOOK = E_AIR * GAP         # 9,0 kV
Q_HOOK = C_BODY * U_HOOK     # 0,90 µC
W_HOOK = 0.5 * C_BODY * U_HOOK ** 2   # 4,05 mJ
Q_DANGER = 0.050 * 1.0       # C, 50 mA for about one second


def _ball(f, x, y, sign, r=15):
    """A charge: a light red ball with + or a light blue ball with −."""
    f.circle(x, y, r, HOT_LIGHT if sign > 0 else COLD_LIGHT, INK, 2)
    f.line(x - r * 0.5, y, x + r * 0.5, y, INK, 3)
    if sign > 0: f.line(x, y - r * 0.5, x, y + r * 0.5, INK, 3)


def hero():
    """A winter evening in a hallway: a warm wall, a wooden door with a brass lever handle on a tall metal plate, a hand
    in a red knitted sleeve reaching from the right, a small bright spark between the fingertip and the plate; a striped
    wool rug on the plank floor, a window with a snowy night outside and a radiator below it, a woollen cap on a hook."""
    f = H.hero("fy9sk-hero", "Kuvitus: talvi-ilta eteisessä. Keskellä on puinen ulko-ovi, jossa on messinkinen kahva pitkässä "
               "metallilevyssä. Oikealta kurottaa käsi punaisessa neulehihassa kohti kahvaa, ja sormenpään ja metallilevyn välissä "
               "välähtää pieni kirkas kipinä. Lattialla on raidallinen villamatto. Vasemmalla on ikkuna, josta näkyy luminen yö, "
               "kuu ja kuusia, ja ikkunan alla patteri. Seinän naulakossa roikkuu villapipo.")
    f.rect(0, 0, 1200, 600, H.grad(f, "fy9sk-wall", "#f4e7cf", "#ead6b2"))
    # the plank floor
    f.rect(0, 470, 1200, 130, H.grad(f, "fy9sk-floor", "#c99a68", "#a9784a"))
    for k in range(1, 4):
        f.line(0, 470 + k * 34, 1200, 470 + k * 34, "#8f6238", 1.5)
    for k in range(9):
        x = 60 + k * 150 + (40 if k % 2 else 0)
        f.line(x, 470 + (k % 3) * 34, x, 504 + (k % 3) * 34, "#8f6238", 1.5)
    f.rect(0, 462, 1200, 10, "#e7d3ae", INK, 2)
    # the window with the snowy night
    wx, wy, ww, wh = 70, 80, 260, 250
    f.rect(wx, wy, ww, wh, H.grad(f, "fy9sk-night", "#1d3557", "#4f6d93"), INK, 4, 4)
    f.circle(wx + 200, wy + 52, 22, "#fff4d6")
    f.circle(wx + 210, wy + 46, 20, "#3b5a82")
    for k in range(26):
        x, y = wx + 12 + H.rnd(k, 5) * (ww - 24), wy + 12 + H.rnd(k + 60, 5) * (wh - 80)
        f.circle(x, y, 1.6 + 1.6 * H.rnd(k + 9, 5), WHITE)
    for x, h in ((wx + 40, 90), (wx + 92, 120), (wx + 150, 80), (wx + 214, 110)):
        f.path(f"M{n(x - h * 0.3)},{wy + wh - 30} L{n(x)},{n(wy + wh - 30 - h)} L{n(x + h * 0.3)},{wy + wh - 30} Z", "#203a2b")
    f.path(f"M{wx},{wy + wh - 40} Q{wx + 90},{wy + wh - 64} {wx + 160},{wy + wh - 46} T{wx + ww},{wy + wh - 50} V{wy + wh} H{wx} Z", WHITE)
    f.line(wx + ww / 2, wy, wx + ww / 2, wy + wh, "#f4efe6", 6)
    f.line(wx, wy + wh / 2 - 20, wx + ww, wy + wh / 2 - 20, "#f4efe6", 6)
    f.rect(wx, wy, ww, wh, "none", INK, 4, 4)
    f.rect(wx - 16, wy + wh, ww + 32, 16, "#f4efe6", INK, 3, 3)
    # the radiator under the window
    rx0, ry0 = 96, 368
    f.rect(rx0, ry0, 208, 82, "#f8f9fa", INK, 2.5, 6)
    for k in range(1, 10):
        f.line(rx0 + k * 20.8, ry0 + 8, rx0 + k * 20.8, ry0 + 74, RULE, 2)
    f.line(rx0 + 30, ry0 + 82, rx0 + 30, 462, IRON, 4)
    f.line(rx0 + 178, ry0 + 82, rx0 + 178, 462, IRON, 4)
    # the cap on a hook
    f.rect(392, 112, 120, 12, SAND_DARK, INK, 2, 3)
    f.line(452, 124, 452, 150, IRON, 4, cap="round")
    f.path("M404,214 Q404,146 452,142 Q500,146 500,214 Z", "#2f74b5", INK, 2.5)
    for k in range(5):
        f.line(412 + k * 20, 164, 412 + k * 20, 208, "#a9d1f0", 3)
    f.rect(398, 206, 108, 20, "#a9d1f0", INK, 2.5, 6)
    f.circle(452, 136, 12, WHITE, INK, 2)
    # the door
    dx0, dy0, dw, dh = 560, 52, 270, 410
    f.rect(dx0 - 14, dy0 - 14, dw + 28, dh + 14, "#e2cfa8", INK, 3)
    f.rect(dx0, dy0, dw, dh, H.grad(f, "fy9sk-door", "#9a6440", "#7a4a2c", horizontal=True), INK, 3)
    for (x, y, w, h) in ((dx0 + 30, dy0 + 30, dw - 60, 150), (dx0 + 30, dy0 + 214, dw - 60, 166)):
        f.rect(x, y, w, h, "none", "#5e3720", 3, 4)
        f.rect(x + 6, y + 6, w - 12, h - 12, "none", "#b07b52", 2, 3)
    for y in (dy0 + 40, dy0 + dh - 70):
        f.rect(dx0 - 6, y, 10, 40, ALUMINIUM, INK, 1.5, 2)
    # the metal plate, the lever handle and the keyhole on the right side
    px, py = dx0 + dw - 46, 232
    f.rect(px - 13, py, 26, 150, H.grad(f, "fy9sk-brass", "#f1d58f", "#c9a046", horizontal=True), INK, 2.5, 6)
    f.circle(px, py + 40, 11, "#e8c66e", INK, 2)
    f.path(f"M{n(px)},{n(py + 33)} L{n(px - 82)},{n(py + 35)} Q{n(px - 96)},{n(py + 40)} {n(px - 84)},{n(py + 47)} L{n(px)},{n(py + 47)} Z",
           H.grad(f, "fy9sk-lever", "#f4dc9c", "#c9a046"), INK, 2.5)
    f.circle(px, py + 112, 5.5, INK)
    f.path(f"M{n(px - 3)},{n(py + 114)} L{n(px - 5)},{n(py + 128)} L{n(px + 5)},{n(py + 128)} L{n(px + 3)},{n(py + 114)} Z", INK)
    # the sleeve and the hand from the right, the forefinger pointing at the plate
    hy = py + 74
    tip = px + 13 + 22                                      # the fingertip, 22 units from the plate's edge
    f.path(f"M1200,{hy - 62} L1010,{hy - 50} Q984,{hy - 30} 990,{hy + 6} Q996,{hy + 44} 1016,{hy + 54} L1200,{hy + 70} Z",
           H.grad(f, "fy9sk-sleeve", "#d64545", "#a61e1e"), INK, 3)
    for k in range(6):
        x = 1040 + k * 28
        f.path(f"M{x},{hy - 44 - k} l8,12 l8,-12", "none", "#f6d2c4", 2.5)
        f.path(f"M{x},{hy + 46 + k} l8,-12 l8,12", "none", "#f6d2c4", 2.5)
    f.path(f"M1004,{hy - 42} Q996,{hy - 6} 1010,{hy + 46}", "none", "#f6d2c4", 6, extra='stroke-linecap="round"')
    skin, skin_dark = "#f1c9a5", "#d9a47c"
    f.path(f"M996,{hy - 34} Q960,{hy - 40} 930,{hy - 22} L{tip + 6},{hy - 9} Q{tip - 2},{hy - 3} {tip + 6},{hy + 4} "
           f"L928,{hy + 6} Q920,{hy + 24} 936,{hy + 32} Q964,{hy + 46} 998,{hy + 38} Z", skin, INK, 2.5)
    for k in range(3):
        y = hy + 12 + k * 9
        f.path(f"M{944 + k * 4},{y} Q{930 + k * 3},{y + 4} {944 + k * 4},{y + 8}", "none", skin_dark, 2)
    f.path(f"M{tip + 10},{hy - 6} q4,3 0,7", "none", skin_dark, 1.5)
    # the spark: a soft glow and a bright zigzag from the fingertip to the plate's edge
    f.defs_add('<radialGradient id="fy9sk-glow"><stop offset="0" stop-color="#ffffff" stop-opacity="0.95"/>'
               '<stop offset="0.35" stop-color="#d0e6fb" stop-opacity="0.75"/><stop offset="1" stop-color="#d0e6fb" stop-opacity="0"/></radialGradient>')
    sx0, sx1 = px + 13, tip
    f.circle((sx0 + sx1) / 2, hy - 2, 36, "url(#fy9sk-glow)")
    zz = f"M{n(sx1)},{n(hy - 2)} L{n(sx1 - 7)},{n(hy - 9)} L{n(sx1 - 11)},{n(hy + 3)} L{n(sx1 - 16)},{n(hy - 6)} L{n(sx0)},{n(hy)}"
    f.path(zz, "none", COLD, 5, extra='stroke-linecap="round" stroke-opacity="0.55"')
    f.path(zz, "none", WHITE, 2.5, extra='stroke-linecap="round"')
    for a in (-40, 0, 40, 140, 180, 220):
        r0, r1 = 22, 32
        ca, sa = math.cos(math.radians(a)), math.sin(math.radians(a))
        cx = (sx0 + sx1) / 2
        f.line(cx + r0 * ca, hy - 2 + r0 * sa, cx + r1 * ca, hy - 2 + r1 * sa, "#ffe8a3", 2.5, cap="round")
    # the wool rug in front of the door
    rug = "M620,488 L1010,488 L1080,560 L560,560 Z"
    f.path(rug, "#c9d6c0", INK, 2.5)
    for k, c in enumerate(("#7a9e7e", "#e9c98a", "#7a9e7e", "#c95f4a", "#7a9e7e")):
        t0, t1 = (k + 0.6) / 5.4, (k + 1.1) / 5.4
        y0, y1 = 488 + 72 * t0, 488 + 72 * t1
        xl0, xr0 = 620 - 60 * t0, 1010 + 70 * t0
        xl1, xr1 = 620 - 60 * t1, 1010 + 70 * t1
        f.path(f"M{n(xl0)},{n(y0)} L{n(xr0)},{n(y0)} L{n(xr1)},{n(y1)} L{n(xl1)},{n(y1)} Z", c)
    f.path(rug, "none", INK, 2.5)
    for k in range(20):
        x = 566 + k * 26
        f.line(x, 560, x - 2, 572, "#c9d6c0", 3, cap="round")
    return f.svg()


def kartta():
    """The concept map, stacked for a phone: the idea at the top (charge makes a field, F = qE), a spine down the left
    and four boxes, each with three laws and a grey word beside each."""
    groups = [
        ("varaus ja voima", [(r"Q = ne", "alkeisvaraus"), (r"F_E = k\,Q_1 Q_2/r^2", "Coulomb"),
                             (r"\overline{F} = \overline{F}_1 + \overline{F}_2", "summa")]),
        ("kenttä ja potentiaali", [(r"U = Ed", "homogeeninen"), (r"W = QU", "kentän työ"),
                                   (r"E_\text{k} = \tfrac12 mv^2", "kiihdytys")]),
        ("kondensaattori", [(r"Q = CU", "kapasitanssi"), (r"C = \varepsilon_0\varepsilon_\text{r}A/d", "levyt"),
                            (r"E = \tfrac12 CU^2", "energia")]),
        ("komponentit ja turvallisuus", [(r"\Sigma \Delta V = 0", "etuvastus"),
                                         (r"\eta = P_\text{a}/P_\text{o}", "kenno"), (r"U = RI", "kehon virta")]),
    ]
    hub_y, hub_h, x_box, gh, top = 8, 72, 44, 156, 100
    height = top + 4 * (gh + 16) - 8
    f = Fig("fy9sk-kartta", height, "Käsitekartta. Ylhäällä solmu: varaus synnyttää sähkökentän, ja kenttä kohdistaa varaukseen voiman F = q E. "
            "Siitä lähtee alas neljä haaraa. Varaus ja voima: varaus Q = n e, Coulombin laki F E = k kertaa varausten tulo "
            "jaettuna r toiseen ja voimien vektorisumma. Kenttä ja potentiaali: homogeeninen kenttä U = E kertaa d, kentän "
            "työ W = Q U ja kiihdytyksessä liike-energia E k = puoli m v toiseen. Kondensaattori: kapasitanssi Q = C U, "
            "levykondensaattori C = epsilon nolla epsilon r A jaettuna d:llä ja energia E = puoli C U toiseen. Komponentit "
            "ja turvallisuus: etuvastus Kirchhoffin 2. laista, summa delta V = 0, aurinkokennon hyötysuhde eta = P a "
            "jaettuna P o:lla ja kehon läpi kulkeva virta I = U jaettuna R:llä.", width=380, size=22)
    spine = 24
    f.line(spine, hub_y + hub_h, spine, top + 3 * (gh + 16) + 22, RULE, 3)
    f.rect(8, hub_y, 364, hub_h, GOOD_LIGHT, GOOD, 2.5, 12)
    f.tex(190, hub_y + 22, r"\text{varaus synnyttää kentän}", "middle", INK)
    f.tex(190, hub_y + 51, r"\overline{F} = q\overline{E}", "middle", INK)
    for k, (head, rows) in enumerate(groups):
        y = top + k * (gh + 16)
        f.line(spine, y + 22, x_box, y + 22, RULE, 3)
        f.rect(x_box, y, 372 - x_box, gh, WHITE, MUTED, 2, 10)
        f.tex(x_box + 14, y + 22, r"\textbf{" + head + "}", "start", INK)
        f.line(x_box + 10, y + 42, 362, y + 42, RULE_LIGHT, 1.5)
        for j, (law, word) in enumerate(rows):
            yy = y + 66 + j * 37
            f.tex(x_box + 14, yy, law, "start", INK)
            f.tex(362, yy, r"\text{" + word + "}", "end", MUTED, size=17)
    return f.svg()


def kipina():
    """The hook answered, not to scale: on the left the fingertip with negative charges, on the right the metal plate of
    the handle with the induced positive charges on its near face; green field lines from the plate to the finger across
    the gap d = 3 mm; below, the three numbers from the breakdown strength, the body's capacitance and the energy."""
    f = Fig("fy9sk-kipina", 540, "Kaavakuva, ei mittakaavassa. Vasemmalla sormenpää, jonka pinnalla on negatiivisia varauksia. "
            "Oikealla oven kahvan metallilevy, jonka sormen puoleiselle pinnalle on influenssin vuoksi siirtynyt positiivisia "
            "varauksia. Niiden välissä on noin 3 millimetrin ilmaväli, jonka poikki kulkee vihreitä kenttäviivoja levystä sormeen ja "
            "kirkas sinivalkoinen kipinä; "
            "kenttä on noin 3 MV/m, ilman läpilyöntilujuus. Alla laskelma: jännite U = E kertaa d on noin 9 kV, keho on "
            "kondensaattori, jonka kapasitanssi on noin 100 pF, joten varaus Q = C U on noin 0,9 mikrocoulombia ja energia "
            "W = puoli C U toiseen noin 4 millijoulea.", size=24)
    # the fingertip (left) and the plate (right)
    fy = 140
    f.path(f"M10,{fy - 70} L190,{fy - 70} Q262,{fy - 70} 262,{fy} Q262,{fy + 70} 190,{fy + 70} L10,{fy + 70} Z", "#f1c9a5", INK, 3)
    f.path(f"M150,{fy - 40} Q200,{fy - 46} 222,{fy - 22}", "none", "#d9a47c", 2.5)
    f.rect(420, fy - 100, 170, 200, H.grad(f, "fy9sk-plate", "#e8c66e", "#c9a046", horizontal=True), INK, 3, 6)
    # charges
    for k, a in enumerate((-50, -25, 0, 25, 50)):
        x = 190 + 62 * math.cos(math.radians(a)) - 16
        y = fy + 62 * math.sin(math.radians(a))
        _ball(f, x, y, -1, 12)
    for k in range(5):
        _ball(f, 440, fy - 72 + k * 36, +1, 12)
    # field lines from the plate to the finger
    for k in range(5):
        y = fy - 60 + k * 30
        f.arrow(418, y, 268 + (4 if k in (0, 4) else 0), y, FIELD, 2.5, 13)
    f.tex(342, fy - 94, r"\overline{E}", "middle", FIELD, w=40, size=28)
    # the spark that jumps once the field reaches the breakdown strength: a soft glow and a bright zigzag
    f.defs_add('<radialGradient id="fy9sk-kglow"><stop offset="0" stop-color="#ffffff" stop-opacity="0.9"/>'
               '<stop offset="0.5" stop-color="#d0e6fb" stop-opacity="0.6"/><stop offset="1" stop-color="#d0e6fb" stop-opacity="0"/></radialGradient>')
    sy = fy + 15
    f.path(f"M{n(341 - 90)},{n(sy)} Q341,{n(sy - 16)} {n(341 + 90)},{n(sy)} Q341,{n(sy + 16)} {n(341 - 90)},{n(sy)} Z", "url(#fy9sk-kglow)")
    zz = f"M264,{sy} L292,{sy - 6} L312,{sy + 6} L338,{sy - 6} L362,{sy + 6} L388,{sy - 5} L416,{sy}"
    f.path(zz, "none", COLD, 6, extra='stroke-linecap="round" stroke-linejoin="round" stroke-opacity="0.5"')
    f.path(zz, "none", WHITE, 2.5, extra='stroke-linecap="round" stroke-linejoin="round"')
    # the gap
    f.line(262, fy + 110, 420, fy + 110, INK, 2)
    for x in (262, 420): f.line(x, fy + 98, x, fy + 122, INK, 2)
    f.tex(341, fy + 138, r"d \approx 3\,\text{mm}", "middle", INK, w=160, size=28)
    f.tex(110, fy + 100, r"\text{sormi}", "middle", MUTED, size=28)
    f.tex(505, fy + 130, r"\text{kahva}", "middle", MUTED, size=28)
    # the three numbers
    y0 = 326
    f.line(10, y0 - 24, 590, y0 - 24, RULE, 1.5, "6 6")
    f.tex(14, y0 + 14, r"U = Ed \approx 3\,\text{MV/m} \cdot 3\,\text{mm} \approx 9\,\text{kV}", "start", INK, size=34)
    f.tex(14, y0 + 76, r"Q = CU \approx 100\,\text{pF} \cdot 9\,\text{kV} \approx 0{,}9\,\mu\text{C}", "start", INK, size=34)
    f.tex(14, y0 + 158, r"W = \dfrac12 CU^2 \approx 4\,\text{mJ}", "start", INK, size=34)
    return f.svg()


def levyt():
    """The plates of the Kaava section to scale in height: the upper plate at 200 V (+), the lower at 0 V (−), 4,0 cm
    apart; green uniform field lines down; dashed grey equipotentials at 150, 100 and 50 V; a proton with its red force
    down (along the field) and an electron with its red force up (against the field)."""
    f = Fig("fy9sk-levyt", 440, "Kaavakuva: kaksi vaakasuoraa levyä. Ylempi levy on positiivinen ja sen potentiaali on 200 V, "
            "alempi negatiivinen levy on nollakohta 0 V. Levyjen välissä on viisi vihreää pystysuoraa kenttäviivaa, jotka "
            "osoittavat alas: kenttä on homogeeninen. Harmaat katkoviivat ovat tasapotentiaalipintoja 150 V, 100 V ja 50 V. "
            "Vasemmalla protoni, jonka punainen voimanuoli osoittaa alas kentän suuntaan. Oikealla elektroni, jonka punainen "
            "voimanuoli osoittaa ylös kenttää vastaan, kohti suurempaa potentiaalia.", size=24)
    x0, x1, yt, yb = 120, 560, 70, 350
    f.rect(x0, yt - 18, x1 - x0, 18, H.grad(f, "fy9sk-pl1", "#dfe4ea", "#aeb8c2"), INK, 2.5, 3)
    f.rect(x0, yb, x1 - x0, 18, H.grad(f, "fy9sk-pl2", "#dfe4ea", "#aeb8c2"), INK, 2.5, 3)
    for k in range(7):
        _ball(f, x0 + 34 + k * 62, yt - 9, +1, 8)
        _ball(f, x0 + 34 + k * 62, yb + 9, -1, 8)
    for k, V in enumerate((150, 100, 50)):
        y = yt + (k + 1) * (yb - yt) / 4
        f.line(x0, y, x1, y, MUTED, 1.5, "6 6")
        f.tex(x0 - 10, y, fi(V) + r"\,\text{V}", "end", MUTED, size=26)
    f.tex(x0 - 10, yt - 9, r"200\,\text{V}", "end", INK, size=26)
    f.tex(x0 - 10, yb + 9, r"0\,\text{V}", "end", INK, size=26)
    for k in range(5):
        x = x0 + 50 + k * 85
        f.arrow(x, yt + 6, x, yb - 6, FIELD, 2, 12)
    f.tex(x0 + 50 + 4 * 85 + 14, yb - 50, r"\overline{E}", "start", FIELD, w=40)
    # the proton (left) and the electron (right)
    p, q = (x0 + 92, yt + 150), (x0 + 348, yt + 130)
    _ball(f, *p, +1, 15)
    f.arrow(p[0], p[1] + 17, p[0], p[1] + 92, FORCE, 4, 16)
    f.tex(p[0] + 18, p[1] + 40, r"\overline{F} = e\overline{E}", "start", FORCE, bg=True)
    _ball(f, *q, -1, 15)
    f.arrow(q[0], q[1] - 17, q[0], q[1] - 92, FORCE, 4, 16)
    f.tex(q[0] + 18, q[1] - 28, r"\overline{F} = -e\overline{E}", "start", FORCE, bg=True)
    f.tex(p[0], yb + 56, r"\text{protoni}", "middle", INK)
    f.tex(q[0], yb + 56, r"\text{elektroni}", "middle", INK)
    return f.svg()


def etuvastus():
    """The LED with its series resistor, no numbers (IEC symbols as in fy9-tasavirta): the source U on the left (long
    plate +, at the top), the resistor R in the top wire, the LED on the right in the forward direction (the triangle
    points down, from + towards -) with two small arrows for its light; the LED's voltage U_D as a grey arrow beside it
    and the violet current I in the loop."""
    f = Fig("fy9sk-etuvastus", 300, "Kytkentäkaavio, ei lukuarvoja. Vasemmalla jännitelähde, jonka jännite on U ja plusnapa "
            "ylhäällä. Ylempään johtimeen on kytketty etuvastus R. Oikealla on LED päästösuuntaan: sen kolmio osoittaa "
            "alaspäin, plusnavan puolelta miinusnavan puolelle, ja siitä lähtee kaksi pientä valon nuolta. LEDin jännite "
            "on U D. Violetti virta I kulkee plusnavasta vastuksen ja LEDin kautta takaisin miinusnapaan.", size=24)
    xs, xR, xL, yt, yb, ys, yl = 140, 290, 440, 70, 250, 160, 160
    wire = lambda *pts: f.add('<polyline points="' + " ".join(f"{n(x)},{n(y)}" for x, y in pts) + f'" fill="none" '
                              f'stroke="{INK}" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>')
    wire((xs, ys - 8), (xs, yt), (xR - 40, yt))
    wire((xR + 40, yt), (xL, yt), (xL, yl - 18))
    wire((xL, yl + 16), (xL, yb), (xs, yb), (xs, ys + 8))
    # the source: long plate + at the top, short thick plate - below
    f.line(xs - 26, ys - 8, xs + 26, ys - 8, INK, 3)
    f.line(xs - 13, ys + 8, xs + 13, ys + 8, INK, 7)
    f.tex(xs + 34, ys - 24, r"+", "start", INK, size=22)
    f.tex(xs - 34, ys, r"U", "end", INK)
    # the series resistor
    f.rect(xR - 40, yt - 12, 80, 24, WHITE, INK, 3)
    f.tex(xR, yt - 36, r"R", "middle", INK)
    # the LED: a filled triangle pointing down and a bar, two light arrows
    f.path(f"M{xL - 18},{yl - 18} L{xL + 18},{yl - 18} L{xL},{yl + 14} Z", WHITE, INK, 3)
    f.line(xL - 20, yl + 16, xL + 20, yl + 16, INK, 3)
    f.arrow(xL + 24, yl - 4, xL + 50, yl - 30, INK, 2, 10)
    f.arrow(xL + 28, yl + 10, xL + 54, yl - 16, INK, 2, 10)
    f.tex(xL + 62, yl + 22, r"\text{LED}", "start", MUTED, size=20)
    f.arrow(xL - 40, yl + 26, xL - 40, yl - 28, MUTED, 2.5, 12)
    f.tex(xL - 52, yl, r"U_\text{D}", "end", MUTED)
    # the current
    for x, y, d in ((215, yt, "r"), (290, yb, "l")):
        s_ = 10
        pts = [(x + s_, y), (x - s_, y - 8), (x - s_, y + 8)] if d == "r" else [(x - s_, y), (x + s_, y - 8), (x + s_, y + 8)]
        f.path("M" + " L".join(f"{n(a)},{n(b)}" for a, b in pts) + " Z", CUR)
    f.tex(215, yt - 26, r"I", "middle", CUR)
    return f.svg()


FIGURES = {"hero": hero, "kartta": kartta, "kipina": kipina, "levyt": levyt, "etuvastus": etuvastus}
REUSE = {"kartta": "reveals: the key laws of FY6 charge, field, potential, capacitor, components and safety",
         "kipina": "reveals: a door-handle spark of about 3 mm means about 9 kV, 0,9 µC and 4 mJ (C about 100 pF)",
         "levyt": "reveals: a uniform field between plates at 200 V and 0 V, equipotentials, F = qE along E for a proton and against E for an electron",
         "etuvastus": "safe: a source U, a series resistor R and an LED with U_D in one loop, no numbers"}
