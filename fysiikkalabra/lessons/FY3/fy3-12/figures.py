"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy3-12` writes them into lesson.md."""
from figlib import (Fig, INK, MUTED, WHITE, RULE, RULE_LIGHT, HEAT, HEAT_LIGHT, HOT, HOT_LIGHT, COLD, COLD_LIGHT,
                    ALUMINIUM, METAL_EDGE, WATER, WATER_LIGHT, SAND, SAND_LIGHT, GRAIN, GLASS)

import herolib as H

def head(f, x, y, d, color, size=14):
    """A filled arrowhead with its tip at (x, y); d is the direction: up, down, left or right."""
    h = size * 0.5
    pts = {"up": [(x, y), (x - h, y + size), (x + h, y + size)], "down": [(x, y), (x - h, y - size), (x + h, y - size)],
           "right": [(x, y), (x - size, y - h), (x - size, y + h)], "left": [(x, y), (x + size, y - h), (x + size, y + h)]}[d]
    f.path("M" + " L".join(f"{a:g},{b:g}" for a, b in pts) + " Z", fill=color)


def heat_transfer():
    f = Fig("fy312-modes", 300, "Kolme lämmön siirtymistapaa, periaatekuva. Johtuminen: lämpö kulkee metallitangon läpi "
            "kuumasta päästä kylmään. Konvektio: lämmin vesi nousee kattilassa keskellä ja jäähtynyt vajoaa reunoilla, "
            "joten vesi kiertää. Säteily: kuuma kappale lähettää säteilyä, joka kulkee tyhjän tilan läpi.")
    f.defs_add(f'<linearGradient id="fy312-rod" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{HOT}"/>'
               f'<stop offset="0.35" stop-color="{HOT_LIGHT}"/><stop offset="0.7" stop-color="{ALUMINIUM}"/>'
               f'<stop offset="1" stop-color="{ALUMINIUM}"/></linearGradient>')
    f.defs_add(f'<linearGradient id="fy312-water" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{WATER_LIGHT}"/>'
               f'<stop offset="1" stop-color="{WATER}"/></linearGradient>')
    f.defs_add(f'<radialGradient id="fy312-hot" cx="0.4" cy="0.4" r="0.7"><stop offset="0" stop-color="{HOT_LIGHT}"/>'
               f'<stop offset="1" stop-color="{HOT}"/></radialGradient>')
    # separators
    for x in (200, 400):
        f.line(x, 20, x, 284, RULE, 1.5, "6 5")
    # 1 conduction
    f.rect(14, 130, 172, 36, "url(#fy312-rod)", INK, 2.5, 3)
    f.block_arrow(30, 96, 170, 96, HEAT, 14, 30, 24)
    f.tex(14, 192, r"\text{kuuma}", "start")
    f.tex(186, 192, r"\text{kylmä}", "end")
    f.tex(100, 262, r"\text{johtuminen}", "middle")
    # 2 convection
    f.path("M238,84 V206 Q238,222 254,222 H346 Q362,222 362,206 V84", fill="url(#fy312-water)", stroke=INK, w=3)
    f.rect(236, 84, 128, 3, WATER_LIGHT)  # water surface line
    f.rect(246, 230, 108, 12, HOT, INK, 2, 3)
    for cx_up, cx_dn, s in ((310, 344, 1), (290, 256, -1)):
        f.path(f"M{cx_up},206 V138 Q{cx_up},114 {300 + s * 11},114", stroke=HEAT, w=4)
        f.path(f"M{300 + s * 11},114 Q{cx_dn},114 {cx_dn},138 V186", stroke=COLD_LIGHT if False else WHITE, w=4)
        head(f, cx_up, 150, "up", HEAT)
        head(f, cx_dn, 196, "down", WHITE)
    f.tex(300, 262, r"\text{konvektio}", "middle")
    # 3 radiation
    f.circle(448, 150, 30, "url(#fy312-hot)", INK, 2.5)
    for y in (104, 150, 196):
        f.path(f"M494,{y} q10,-9 20,0 t20,0 t20,0", stroke=HEAT, w=3)
        head(f, 572, y, "right", HEAT)
    f.tex(500, 262, r"\text{säteily}", "middle")
    return f.svg()


def energy_balance():
    f = Fig("fy312-balance", 300, "Maapallon energiatasapaino, periaatekuva. Auringosta tuleva säteily kulkee ilmakehän "
            "läpi maanpintaan; osa siitä heijastuu takaisin avaruuteen. Maanpinta säteilee lämpösäteilyä ylöspäin, ja "
            "ilmakehän kasvihuonekaasut säteilevät osan siitä takaisin alas.")
    f.defs_add(f'<linearGradient id="fy312-ground" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{SAND}"/>'
               f'<stop offset="1" stop-color="{SAND_LIGHT}"/></linearGradient>')
    f.defs_add(f'<linearGradient id="fy312-air" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{WHITE}"/>'
               f'<stop offset="1" stop-color="{COLD_LIGHT}"/></linearGradient>')
    f.defs_add(f'<radialGradient id="fy312-sun" cx="0.4" cy="0.4" r="0.7"><stop offset="0" stop-color="{WHITE}"/>'
               f'<stop offset="1" stop-color="{HEAT_LIGHT}"/></radialGradient>')
    f.rect(12, 116, 576, 54, "url(#fy312-air)", MUTED, 2, 0, 'stroke-dasharray="7 5"')
    f.rect(12, 236, 576, 52, "url(#fy312-ground)", INK, 2.5)
    f.tex(300, 262, r"\text{maanpinta}", "middle")
    f.tex(300, 143, r"\text{ilmakehä}", "middle")
    # sunlight on the left: in, and the reflected part out
    f.circle(50, 52, 26, "url(#fy312-sun)", HEAT, 2.5)
    f.tex(88, 36, r"\text{Aurinko}", "start")
    f.block_arrow(72, 86, 132, 226, HEAT, 12, 30, 24)
    f.block_arrow(176, 112, 230, 44, HEAT_LIGHT, 10, 28, 22)
    f.tex(246, 56, r"\text{heijastuu}", "start")
    # infrared on the right: thermal radiation up, back radiation down
    f.block_arrow(390, 228, 390, 34, HOT, 12, 30, 24)
    f.tex(412, 70, r"\text{lämpösäteily}", "start")
    f.block_arrow(450, 176, 450, 226, HOT_LIGHT, 12, 30, 22)
    f.tex(472, 201, r"\text{takaisin}", "start")
    return f.svg()


def wall_temperature():
    f = Fig("fy312-wall", 300, "Seinän poikkileikkaus ja lämpötilan kulku, periaatekuva. Seinässä on ohut sisälevy, paksu "
            "eristekerros ja ohut ulkoverhous. Lämpötila laskee sisältä 21 asteesta ulos miinus 15 asteeseen eli "
            "36 kelviniä, ja suurin osa laskusta tapahtuu eristeessä. Lämpöteho P kulkee seinän läpi sisältä ulos.")
    f.defs_add(f'<pattern id="fy312-wool" width="14" height="14" patternUnits="userSpaceOnUse">'
               f'<path d="M1,4 q4,-5 6,0 t6,0 M1,11 q4,-5 6,0 t6,0" fill="none" stroke="{GRAIN}" stroke-width="1.5"/></pattern>')
    top, bot = 64, 222                        # 21 degC and -15 degC levels
    f.line(40, top, 570, top, MUTED, 1.5, "6 5")
    f.line(40, bot, 570, bot, MUTED, 1.5, "6 5")
    f.rect(220, 40, 36, 200, ALUMINIUM, INK, 2.5)
    f.rect(256, 40, 124, 200, SAND_LIGHT, INK, 2.5)
    f.rect(256, 40, 124, 200, "url(#fy312-wool)")
    f.rect(380, 40, 28, 200, ALUMINIUM, INK, 2.5)
    f.rect(302, 85, 68, 30, WHITE, None, 0, 4, 'fill-opacity="0.85"')
    f.tex(336, 100, r"\text{eriste}", "middle")
    f.path("M40,64 H220 L256,72 L380,214 L408,222 H570", stroke=HOT, w=4)
    f.tex(130, 40, r"21\,{}^\circ\text{C}", "middle")
    f.tex(130, 100, r"\text{sisällä}", "middle")
    f.tex(500, 196, r"-15\,{}^\circ\text{C}", "middle")
    f.tex(500, 150, r"\text{ulkona}", "middle")
    f.path("M30,64 H24 V222 H30", stroke=INK, w=2)
    f.tex(36, 143, r"\Delta T = 36\,\text{K}", "start", bg=True)
    f.block_arrow(120, 272, 470, 272, HEAT, 12, 32, 26)
    f.tex(484, 272, "P", "start", HEAT)
    return f.svg()


def hero():
    """The chapter's opening illustration: the Earth seen from space, the Sun at the edge of the picture."""
    f = H.hero("fy312-hero", "Kuvitus: Maa avaruudesta nähtynä, ympärillään ohut ilmakehä. Kuvan vasemmassa reunassa paistaa "
               "Aurinko, ja tähdet tuikkivat mustalla taivaalla.")
    H.space(f, seed=5, count=90)
    f.defs_add(f'<radialGradient id="fy312h-sun" cx="0.5" cy="0.5" r="0.5"><stop offset="0.55" stop-color="{H.HEAT_LIGHT}"/>'
               f'<stop offset="0.8" stop-color="{H.HEAT}"/><stop offset="1" stop-color="{H.HEAT}" stop-opacity="0"/></radialGradient>')
    f.circle(-60, 300, 260, "url(#fy312h-sun)")
    for y in (180, 300, 420):                                         # sunlight in ...
        f.block_arrow(290, y, 460, y, H.HEAT_LIGHT, 12, 30, 24)
    for deg in (-34, 0, 34):                                          # ... and as much radiated out: equal arrows
        c, s_ = H.math.cos(H.math.radians(deg)), H.math.sin(H.math.radians(deg))
        f.block_arrow(800 + 222 * c, 300 + 222 * s_, 800 + 392 * c * (0.96 if deg else 1), 300 + 392 * s_, H.HEAT_LIGHT, 12, 30, 24)
    H.earth(f, "fy312h", 800, 300, 210)
    return f.svg()


def scene():
    """A second everyday scene: a house on a winter night losing heat through its windows and roof."""
    f = H.scene("fy312-scene", "Kuvitus: omakotitalo talviyönä. Lämpöä karkaa ulos ikkunoiden ja katon kautta, mitä kuvaavat "
                "oranssit nuolet. Maassa on lunta.")
    f.rect(0, 0, 600, 360, H.grad(f, "fy312s-night", H.INK, H.COLD))
    for k in range(30): f.circle(H.rnd(k, 8) * 600, H.rnd(k + 40, 8) * 200, 1 + H.rnd(k + 2, 8), H.WHITE)
    f.path("M0,300 Q300,286 600,302 V360 H0 Z", H.WHITE)
    f.rect(170, 170, 260, 136, H.RULE_LIGHT, H.INK, 3)
    f.path("M150,172 L300,80 L450,172 Z", H.IRON, H.INK, 3)
    f.path("M150,172 L300,80 L450,172", stroke=H.WHITE, w=6)
    for x in (200, 340):
        f.rect(x, 200, 60, 54, H.HEAT_LIGHT, H.INK, 3, 3)
        f.line(x + 30, 200, x + 30, 254, H.INK, 2.5)
    f.rect(280, 230, 40, 76, H.SAND, H.INK, 3, 3)
    for x0, y0, x1, y1 in ((230, 226, 230 - 90, 226 + 10), (370, 226, 370 + 90, 226 + 10), (250, 120, 220, 50), (350, 120, 380, 50)):
        f.block_arrow(x0, y0, x1, y1, H.HEAT, 10, 24, 18)
    return f.svg()


def earth_flows():
    """Task figure (no lesson.md block): the radiation power per square metre at the top of the atmosphere, with the
    thermal radiation to space left as a question mark. In 341 W/m², reflected 102 W/m² (balance: 239 W/m² out)."""
    f = Fig("fy312-flows", 280, "Kaavakuva maapallon energiavirroista neliömetriä kohti ilmakehän ylärajalla. Auringosta tulee maapalloon "
            "säteilyä 341 W/m², ja siitä 102 W/m² heijastuu takaisin avaruuteen. Avaruuteen lähtevän lämpösäteilyn tehoa ei ole annettu. "
            "Maapallo on energiatasapainossa, joten sen lämpötila pysyy vakiona.", width=640)
    f.circle(56, 140, 26, "#ffe8cc", HEAT, 2.5)
    f.tex(56, 190, r"\text{Aurinko}", "middle")
    f.circle(300, 140, 62, COLD_LIGHT, INK, 3)
    f.tex(300, 140, r"\text{maapallo}", "middle")
    f.block_arrow(98, 140, 232, 140, HEAT, 14, 34, 26)
    f.tex(165, 104, r"341\,\text{W/m}^2", "middle")
    f.block_arrow(350, 90, 438, 36, HEAT_LIGHT, 12, 30, 22)
    f.tex(448, 30, r"102\,\text{W/m}^2", "start")
    f.tex(448, 64, r"\text{heijastuu}", "start")
    f.block_arrow(366, 176, 452, 214, HOT, 14, 34, 26)
    f.tex(462, 190, r"?\,\text{W/m}^2", "start")
    f.tex(462, 224, r"\text{lämpösäteily}", "start")
    return f.svg()


FIGURES = {"hero": hero, "scene": scene, "heat-transfer": heat_transfer, "energy-balance": energy_balance, "wall-temperature": wall_temperature, "earth-flows": earth_flows}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "heat-transfer": "reveals: which mechanism is which",
    "energy-balance": "safe: the Earth's energy flows, no values",
    "wall-temperature": "reveals: the temperature drop is mostly in the insulation",
    "earth-flows": "safe: incoming 341 and reflected 102 W/m2 as labels; the outgoing thermal radiation is a question mark",
}
