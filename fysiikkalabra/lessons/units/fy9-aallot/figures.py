"""Figures of the FY9 unit fy9-aallot (scripts/figlib.py, herolib.py); `python3 scripts/units.py figures fy9-aallot`
writes them into content/fi/units/fy9-aallot/unit.md. The unit is Finnish, so the decimal sign is a comma.

hero        the Why scene: an indoor swimming hall seen in cross-section, the lifeguard's chair on the deck with a
            whistle, the sound's wavefronts closely spaced in the air and far apart under the water (to the ratio of
            the wavelengths, 350 : 1500), lane ropes and the pool floor (no text, no people)
kartta      the concept map of the review: periodic motion at the top, then the oscillators, the waves and sound,
            each with its laws
pilli       the hook to scale: the same 3,0 kHz whistle as a pressure wave in the air (0,12 m) and in the water
            (0,50 m), one metre drawn equally long in both
ominais     the standing-wave conditions: a string fixed at both ends, a pipe open at both ends and a pipe closed at
            one end, each at its fundamental, with L = lambda/2, L = lambda/2 and L = lambda/4
"""
import math
import figlib
from figlib import (Fig, INK, MUTED, WHITE, RULE, RULE_LIGHT, GLASS, SAND_LIGHT, SAND, HEAT, HOT, COLD, COLD_LIGHT,
                    WATER, WATER_LIGHT, ICE, IRON, ALUMINIUM, METAL_EDGE, n, fi)
import herolib as H

figlib.set_language({}, ",")

# the hook (computed here and quoted in unit.md and inquiry.json)
F_WHISTLE = 3000.0          # Hz
V_AIR = 350.0               # m/s, the warm air of the hall (about 28 °C)
V_WATER = 1500.0            # m/s
LAM_AIR = V_AIR / F_WHISTLE         # 0,117 m
LAM_WATER = V_WATER / F_WHISTLE     # 0,50 m


def _arcs(f, cx, cy, radii, a0, a1, colour, w, opacity):
    """Circular wavefront arcs around (cx, cy) from angle a0 to a1 (degrees, 0 = right, positive = down)."""
    for r in radii:
        x0, y0 = cx + r * math.cos(math.radians(a0)), cy + r * math.sin(math.radians(a0))
        x1, y1 = cx + r * math.cos(math.radians(a1)), cy + r * math.sin(math.radians(a1))
        f.path(f"M{n(x0)},{n(y0)} A{n(r)},{n(r)} 0 0 1 {n(x1)},{n(y1)}", "none", colour, w,
               extra=f'stroke-linecap="round" stroke-opacity="{opacity:g}"')


def hero():
    """An indoor swimming hall in cross-section: a tiled wall with tall windows, the deck on the left with the
    lifeguard's high chair and a whistle hanging from it, the pool on the right seen through its glass side: water with
    a light surface, a lane rope of floats, the tiled floor with a dark lane line. Wavefronts leave the whistle closely
    spaced in the air; under the surface the same sound continues with wavefronts about 4,3 times farther apart."""
    f = H.hero("fy9aa-hero", "Kuvitus: uimahalli poikkileikkauksena. Taustalla laatoitettu seinä ja korkeat ikkunat. Vasemmalla "
               "allasreunalla on uinninvalvojan korkea tuoli, jonka käsinojalta roikkuu pilli. Pillistä lähtee ilmaan tiheästi "
               "toisiaan seuraavia aaltorintamien kaaria kohti allasta. Oikealla allas sivulta nähtynä: vesi, pinnalla ratamerkkiköysi "
               "kohoineen ja pohjalla tumma ratamerkintä. Veden alla samat aaltorintamat jatkuvat noin neljä kertaa harvempina.")
    # the hall: a light tiled wall and three tall windows
    H.tiles(f, 330, 60, RULE_LIGHT, "#f8f6f0")
    for k, x in enumerate((420, 650, 880)):
        f.rect(x, 48, 170, 200, H.grad(f, f"fy9aa-win{k}", ICE, COLD_LIGHT), INK, 3, 4)
        H.cloud(f, x + 70, 120, 0.42)
        f.line(x + 85, 48, x + 85, 248, INK, 3)
        f.line(x, 148, x + 170, 148, INK, 3)
        f.rect(x - 10, 248, 190, 12, RULE, INK, 2.5, 3)
    f.rect(0, 316, 1200, 14, RULE, INK, 2)                                  # the skirting band
    # the deck on the left (a tiled block) and the pool's glass side on the right
    f.rect(0, 330, 330, 270, "#e9e4d8", INK, 2.5)
    for y in range(360, 600, 30): f.line(0, y, 330, y, RULE, 1.5)
    for x in range(30, 330, 60): f.line(x, 330, x, 600, RULE, 1.5)
    surf = 352
    f.rect(330, 330, 870, 270, "#d7e3ea", INK, 2.5)                         # the pool shell behind the water
    f.rect(338, surf, 862, 236, H.grad(f, "fy9aa-water", WATER_LIGHT, WATER), None, 0)
    f.path(f"M338,{surf} " + " ".join(f"Q{x + 15},{surf - 5} {x + 30},{surf} T{x + 60},{surf}" for x in range(338, 1170, 60)) + f" V{surf + 8} H338 Z",
           WHITE, extra='fill-opacity="0.55"')
    f.rect(338, 560, 862, 28, "#cfe0ea", INK, 2)                            # the tiled floor
    for x in range(368, 1200, 40): f.line(x, 560, x, 588, RULE, 1.2)
    f.rect(560, 566, 480, 12, INK, None, 0, 3)                              # the dark lane line
    f.rect(1028, 548, 12, 30, INK, None, 0, 3)                              # its T end
    # the lane rope: alternating red and white floats on the surface
    for k, x in enumerate(range(360, 1200, 34)):
        f.add(f'<ellipse cx="{x}" cy="{surf + 2}" rx="15" ry="9" fill="{HOT if k % 4 < 2 else WHITE}" stroke="{INK}" stroke-width="1.5"/>')
    # the ladder at the pool's edge
    for x in (344, 372):
        f.path(f"M{x},{surf + 120} V{surf - 34} Q{x},{surf - 64} {x - 26},{surf - 64}", "none", METAL_EDGE, 6, extra='stroke-linecap="round"')
    for y in range(surf + 10, surf + 120, 34): f.line(344, y, 372, y, METAL_EDGE, 5, cap="round")
    # the lifeguard's high chair on the deck: two legs, a footrest, the seat, a back and an armrest
    f.line(120, 330, 160, 160, IRON, 9, cap="round")
    f.line(250, 330, 214, 160, IRON, 9, cap="round")
    f.line(136, 262, 236, 262, IRON, 6, cap="round")
    f.line(146, 214, 228, 214, IRON, 6, cap="round")
    f.rect(140, 148, 104, 18, "#2f74b5", INK, 2.5, 4)                      # the seat
    f.rect(140, 70, 18, 86, "#2f74b5", INK, 2.5, 4)                        # the back
    f.line(158, 112, 244, 112, IRON, 6, cap="round")                        # the armrest
    f.line(244, 112, 244, 148, IRON, 6, cap="round")
    # the whistle on its cord, hanging from the armrest's end
    f.path("M240,114 Q256,140 262,166", "none", HOT, 3)
    f.rect(252, 166, 30, 16, "#ffd43b", INK, 2.5, 6)
    f.rect(278, 168, 14, 10, "#ffd43b", INK, 2, 2)
    f.circle(262, 174, 4, INK)
    # the sound: wavefronts every 24 units in the air (lambda 0,12 m) and every 103 units under the water (0,50 m)
    wx, wy = 296, 173
    _arcs(f, wx, wy, [28 + 24 * k for k in range(7)], -38, 62, INK, 3, 0.75)
    ex, ey = 452, surf + 2
    _arcs(f, ex, ey, [44 + 103 * k for k in range(3)], 8, 86, WHITE, 4, 0.9)
    # bubbles and a beach ball on the surface
    for k, (x, y, r) in enumerate(((760, 470, 7), (772, 440, 5), (766, 414, 4), (1110, 500, 6), (1118, 470, 4))):
        f.circle(x, y, r, "none", WHITE, 2)
    f.circle(1080, surf - 26, 28, WHITE, INK, 2.5)
    f.path(f"M1052,{surf - 26} Q1080,{surf - 62} 1108,{surf - 26} Q1080,{surf - 44} 1052,{surf - 26} Z", HOT)
    f.path(f"M1052,{surf - 26} Q1080,{surf + 10} 1108,{surf - 26} Q1080,{surf - 8} 1052,{surf - 26} Z", COLD)
    # towels on the deck
    f.rect(30, 300, 70, 30, "#ffd43b", INK, 2, 4)
    f.rect(40, 286, 52, 16, HOT, INK, 2, 4)
    return f.svg()


def kartta():
    """The concept map, stacked for a phone: periodic motion at the top, a spine down the left and three boxes
    (oscillators, waves, sound), each with three laws and a grey word beside each."""
    f = Fig("fy9aa-kartta", 704, "Käsitekartta. Ylhäällä solmu jaksollinen liike: jaksonaika T, taajuus f = 1 per T ja amplitudi A. Siitä lähtee "
            "alas kolme haaraa. Värähtelijät, toistuva liike: jousen voima F = miinus k x vektoreina, jousivärähtelijän "
            "jaksonaika T = 2 pii kertaa neliöjuuri m per k ja heilurin jaksonaika T = 2 pii kertaa neliöjuuri l per g. "
            "Aallot, värähtely etenee: aaltoliikkeen perusyhtälö v = f lambda, vahvistava interferenssi, kun matkaero on n "
            "lambda, ja kielen ominaistaajuudet f n = n v per 2 L. Ääni, aalto ilmassa: huojunta f H = f 1 miinus f 2 "
            "itseisarvona, Dopplerin ilmiö lähteen liikkuessa kohti havaitsijaa ja intensiteettitaso L = 10 desibeliä "
            "kertaa logaritmi I per I 0.", width=380, size=20)
    groups = [
        ("värähtelijät", "toistuva liike", [(r"\overline{F} = -k\overline{x}", "jousen voima"), (r"T = 2\pi\sqrt{m/k}", "jousi"), (r"T = 2\pi\sqrt{l/g}", "heiluri")]),
        ("aallot", "värähtely etenee", [(r"v = f\lambda", "eteneminen"), (r"\Delta s = n\lambda", "vahvistava"), (r"f_n = n \cdot v/(2L)", "seisova aalto")]),
        ("ääni", "aalto ilmassa", [(r"f_\text{H} = |f_1 - f_2|", "huojunta"), (r"f = f_0\,v/(v - v_\text{L})", "Doppler"),
                  (r"L = 10\,\text{dB} \cdot \lg(I/I_0)", "taso")]),
    ]
    hub_y, hub_h, x_box, gh, top = 8, 72, 44, 188, 100
    spine = 24
    f.line(spine, hub_y + hub_h, spine, top + 2 * (gh + 16) + 22, RULE, 3)
    f.rect(8, hub_y, 364, hub_h, SAND_LIGHT, SAND, 2.5, 12)
    f.tex(190, hub_y + 22, r"\text{jaksollinen liike}", "middle", INK)
    f.tex(190, hub_y + 51, r"T,\ f = 1/T,\ A", "middle", INK)
    for k, (head, sub, rows) in enumerate(groups):
        y = top + k * (gh + 16)
        f.line(spine, y + 22, x_box, y + 22, RULE, 3)
        f.rect(x_box, y, 372 - x_box, gh, WHITE, MUTED, 2, 10)
        f.tex(x_box + 14, y + 22, r"\textbf{" + head + "}", "start", INK)
        f.tex(362, y + 22, r"\text{" + sub + "}", "end", MUTED, size=17)
        f.line(x_box + 10, y + 42, 362, y + 42, RULE_LIGHT, 1.5)
        for j, (law, word) in enumerate(rows):
            yy = y + 68 + j * 52
            f.tex(x_box + 14, yy, law, "start", INK, size=18 if len(law) > 22 else None)
            if word: f.tex(362, yy, r"\text{" + word + "}", "end", MUTED, size=17)
    return f.svg()


def pilli():
    """The hook to scale: one metre is 400 units in both strips. Above, the whistle's pressure wave in the air,
    lambda = 0,117 m (about 8,6 wavelengths per metre); below, the same frequency in the water, lambda = 0,50 m. A bracket
    marks one wavelength in each (ink, not the force red); a labelled blue arrow shows the direction of travel and a
    title says the curve is the pressure wave."""
    f = Fig("fy9aa-pilli", 380, "Kaavakuva mittakaavassa: saman pillin ääni paineaaltona ilmassa ja vedessä, kummassakin yhden "
            "metrin matka yhtä pitkänä. Ylempänä ilmassa aallonpituus on 0,12 metriä, joten metrille mahtuu lähes yhdeksän "
            "aaltoa. Alempana vedessä aallonpituus on 0,50 metriä, ja metrille mahtuu kaksi aaltoa. Kummassakin yksi "
            "aallonpituus on merkitty hakasulkeella, ja nuoli näyttää etenemissuunnan. Käyrä kuvaa paineen vaihtelua. Taajuus on molemmissa sama, 3,0 kilohertsiä, mutta äänen nopeus on ilmassa "
            "noin 350 ja vedessä noin 1500 metriä sekunnissa.", size=26)
    x0, M = 24, 400                               # one metre = 400 units
    f.tex(300, 20, r"\text{paineaalto, sama taajuus } f = 3{,}0\,\text{kHz}", "middle", INK)
    for k, (lam, yc, name, speed, back) in enumerate(((LAM_AIR, 118, r"\text{ilma}", r"v \approx 350\,\text{m/s}", GLASS),
                                                       (LAM_WATER, 278, r"\text{vesi}", r"v \approx 1500\,\text{m/s}", "#dcecf8"))):
        f.rect(x0 - 10, yc - 46, M + 20, 92, back, RULE, 1.5, 8)
        f.line(x0, yc, x0 + M, yc, RULE, 1.5, dash="5 5")
        pts = " ".join(f"{n(x0 + M * s / 240)},{n(yc - 30 * math.sin(2 * math.pi * (s / 240) / lam))}" for s in range(241))
        f.add(f'<polyline points="{pts}" fill="none" stroke="{INK}" stroke-width="3" stroke-linejoin="round"/>')
        f.tex(x0 + M + 22, yc - 18, name, "start", INK)
        f.tex(x0 + M + 22, yc + 16, r"\lambda \approx " + (r"0{,}12" if k == 0 else r"0{,}50") + r"\,\text{m}", "start", INK, size=24)
        # a bracket over one wavelength, from the first crest to the next
        c1 = x0 + M * lam / 4; c2 = c1 + M * lam; yb = yc - 40
        f.path(f"M{n(c1)},{n(yb + 6)} V{n(yb)} H{n(c2)} V{n(yb + 6)}", "none", INK, 2.5)
        f.tex((c1 + c2) / 2, yb - 16, r"\lambda", "middle", INK, size=24)
        f.tex(x0, yc + 64, speed, "start", COLD, size=24)
    f.arrow(446, 362, 540, 362, COLD, 3, 13)
    f.tex(446, 336, r"\text{etenee}", "start", COLD, size=24)
    f.line(x0, 360, x0 + M, 360, INK, 2)
    for x in (x0, x0 + M): f.line(x, 352, x, 368, INK, 2)
    f.tex(x0 + M / 2, 342, r"1\,\text{m}", "middle", INK, size=24)
    return f.svg()


def ominais():
    """The standing waves at the fundamental: a string fixed at both ends (nodes at the ends, L = lambda/2), a pipe open
    at both ends (displacement antinodes at the ends, L = lambda/2) and a pipe closed at the left end (a node at the
    closed end, an antinode at the open one, L = lambda/4). The pale band in a pipe is how far the air moves."""
    f = Fig("fy9aa-ominais", 466, "Kaavakuva, ei mittakaavassa: kolme seisovaa aaltoa perustaajuudella allekkain, kaikki pituudeltaan L. "
            "Ylimpänä kahdesta päästä kiinnitetty kieli: päissä on solmu, keskellä kupu, ja kielen pituus on puolet aallonpituudesta. "
            "Keskellä molemmista päistä avoin putki: ilman siirtymän kuvut ovat putken päissä ja solmu keskellä, ja putken pituus "
            "on puolet aallonpituudesta. Alimpana toisesta päästä suljettu putki: suljetussa päässä on solmu ja avoimessa kupu, "
            "ja putken pituus on neljäsosa aallonpituudesta.", size=26)
    x0, x1 = 40, 360
    W = x1 - x0
    # the string
    y = 70
    f.circle(x0, y, 6, INK); f.circle(x1, y, 6, INK)
    for s, dash in ((1, None), (-1, "7 6")):
        pts = " ".join(f"{n(x0 + W * t / 100)},{n(y - s * 34 * math.sin(math.pi * t / 100))}" for t in range(101))
        f.add(f'<polyline points="{pts}" fill="none" stroke="{COLD}" stroke-width="3"{(" stroke-dasharray=" + chr(34) + dash + chr(34)) if dash else ""}/>')
    f.tex(390, y - 18, r"\text{kieli}", "start", INK)
    f.tex(390, y + 20, r"L = \lambda/2", "start", INK)

    def pipe(yc, closed):
        h = 64
        f.rect(x0, yc - h / 2, W, h, GLASS, None, 0)
        f.line(x0, yc - h / 2, x1, yc - h / 2, INK, 3); f.line(x0, yc + h / 2, x1, yc + h / 2, INK, 3)
        if closed: f.rect(x0 - 12, yc - h / 2 - 4, 12, h + 8, IRON, INK, 2)
        # displacement envelope: cos for an open pipe (antinodes at both ends), cos of a quarter wave for a closed one
        amp = h / 2 - 6
        env = (lambda t: abs(math.cos(math.pi * t))) if not closed else (lambda t: math.sin(math.pi * t / 2))
        top = [(x0 + W * t / 100, yc - amp * env(t / 100)) for t in range(101)]
        bot = [(x0 + W * t / 100, yc + amp * env(t / 100)) for t in range(100, -1, -1)]
        f.path("M" + " L".join(f"{n(a)},{n(b)}" for a, b in top + bot) + " Z", COLD_LIGHT, COLD, 2)
        for t in ((0.5,) if not closed else (0.0,)):
            f.tex(x0 + W * t + (14 if closed else 0), yc + h / 2 + 20, r"\text{S}", "middle" if not closed else "start", MUTED, size=24)
        for t in ((0.0, 1.0) if not closed else (1.0,)):
            f.tex(x0 + W * t, yc + h / 2 + 20, r"\text{K}", "middle", MUTED, size=24)
    yo = 208
    pipe(yo, False)
    f.tex(390, yo - 18, r"\text{avoin putki}", "start", INK)
    f.tex(390, yo + 20, r"L = \lambda/2", "start", INK)
    yc = 342
    pipe(yc, True)
    f.tex(390, yc - 18, r"\text{suljettu putki}", "start", INK)
    f.tex(390, yc + 20, r"L = \lambda/4", "start", INK)
    # the common length L under all three
    f.line(x0, 446, x1, 446, INK, 2)
    for x in (x0, x1): f.line(x, 438, x, 454, INK, 2)
    f.tex((x0 + x1) / 2, 428, r"L", "middle", INK, size=26)
    f.tex(390, 446, r"\text{S solmu, K kupu}", "start", MUTED, size=24)
    return f.svg()


FIGURES = {"hero": hero, "kartta": kartta, "pilli": pilli, "ominais": ominais}
REUSE = {"kartta": "reveals: the key laws of FY5 oscillations, waves and sound",
         "pilli": "reveals: the frequency stays and the wavelength grows about 4,3-fold from air to water",
         "ominais": "reveals: L = lambda/2 for a string and an open pipe, L = lambda/4 for a closed pipe"}
