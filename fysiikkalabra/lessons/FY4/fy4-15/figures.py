"""Figures of fy4-15 (scripts/figlib.py, scripts/herolib.py); `python scripts/figures.py fy4-15` writes them into lesson.md.
Energy flow is the heat palette (filled arrows), the wind's velocity blue as in every FY4 figure; the power curve is the
real Vestas V82-1.65 MW curve (NREL Turbine Archive, Onshore/VestasV82_1.65MW_82.csv, read 2026-10-30)."""
import math
from figlib import (Fig, Axes, fi, INK, MUTED, WHITE, RULE, RULE_LIGHT, SAND_LIGHT, SAND, SAND_DARK, GRAIN, ICE, ICE_EDGE, GLASS,
                    COLD, COLD_LIGHT, HOT, HEAT, HEAT_LIGHT, GOOD, GOOD_LIGHT, IRON, ALUMINIUM, METAL_EDGE, COPPER, WATER,
                    WATER_LIGHT, n)
import herolib as H
from herolib import grad, rnd

g, RHO_A = 9.81, 1.25
V82 = [(3, 0), (4, 28), (5, 144), (6, 309), (7, 511), (8, 758), (9, 1017), (10, 1285), (11, 1504), (12, 1637), (13, 1650),
       (14, 1650), (15, 1650), (16, 1650), (17, 1650), (18, 1650), (19, 1650), (20, 1650)]
A82 = math.pi * 41.0 ** 2


# ---------------------------------------------------------------- opening illustration
def hero():
    """A river valley: a hydropower station across the river, white water foaming out below it, wind turbines turning on
    the ridge behind, a power line leading away; wind streaks in the sky."""
    f = H.hero("fy415-hero", "Kuvitus: jokilaakso kesäpäivänä. Keskellä joen poikki on rakennettu vesivoimalaitos: padon takana "
               "yläpuolinen vesi on korkealla, ja voimalan alapuolelta purkautuva vesi kuohuu valkoisena alempana. Taustalla "
               "harjanteella pyörii neljä tuulivoimalaa, ja taivaalla näkyy tuulen viivoja. Voimalasta lähtee sähkölinja pylväineen.")
    H.sky(f, "fy415h", 600, ICE, GLASS)
    H.cloud(f, 200, 110, 1.0); H.cloud(f, 1030, 80, 0.8); H.cloud(f, 620, 60, 0.55, extra='fill-opacity="0.85"')
    for k in range(6):                                        # wind streaks
        x, y = 120 + 170 * k + 40 * rnd(k, 2), 150 + 50 * rnd(k, 5)
        f.path(f"M{n(x)},{n(y)} q40,-10 80,0 t80,0", stroke=WHITE, w=4, extra='stroke-linecap="round" stroke-opacity="0.9"')
    # the far ridge with the wind turbines
    f.path("M0,300 Q180,230 420,250 T820,214 T1200,238 V600 H0 Z", grad(f, "fy415h-ridge", GOOD_LIGHT, GOOD, y1=210, y2=420))
    for k, (x, yb, h, t) in enumerate(((700, 250, 120, 0.3), (840, 240, 135, 1.4), (980, 246, 115, 2.2), (1110, 254, 100, 0.9))):
        H.wind_turbine(f, x, yb, h, turn=t, sc=1.4 if k == 1 else 1.2)
    H.forest(f, 300, 34, 22, GOOD, seed=3, x0=0, x1=560, depth=30)
    # the near valley sides
    f.path("M0,330 Q200,310 360,350 L420,600 H0 Z", grad(f, "fy415h-bankl", GOOD_LIGHT, GOOD, y1=310, y2=600))
    f.path("M720,350 Q900,320 1200,336 V600 H660 Z", grad(f, "fy415h-bankr", GOOD_LIGHT, GOOD, y1=320, y2=600))
    # the upper river (behind the dam, high) and the lower river (in front, low)
    water = grad(f, "fy415h-water", WATER_LIGHT, WATER, y1=300, y2=600)
    f.path("M250,352 Q290,300 420,292 L700,290 Q830,296 870,352 Z", water)
    for x, w in ((300, 60), (720, 80), (790, 50)):
        f.path(f"M{x},326 q{n(w / 4)},-5 {n(w / 2)},0 t{n(w / 2)},0", stroke=WHITE, w=3, extra='stroke-opacity="0.8" stroke-linecap="round"')
    f.path("M400,460 Q520,450 640,456 Q760,462 800,470 L980,600 H260 Z", water)
    for x, y, w in ((420, 520, 90), (560, 560, 120), (720, 520, 100), (820, 575, 110)):
        f.path(f"M{x},{y} q{n(w / 4)},-6 {n(w / 2)},0 t{n(w / 2)},0", stroke=WHITE, w=3, extra='stroke-opacity="0.7" stroke-linecap="round"')
    # the dam and the power station across the river
    conc = grad(f, "fy415h-conc", ALUMINIUM, METAL_EDGE)
    f.path("M318,350 H812 L800,462 H330 Z", conc, INK, 3)                    # the dam wall
    for k in range(1, 8):
        x = 330 + k * 60
        f.line(x, 354, x - 2, 460, METAL_EDGE, 2)
    f.rect(400, 262, 290, 92, SAND_LIGHT, INK, 3, 4)                        # the station hall on the dam
    f.path("M392,262 L410,236 H680 L698,262 Z", HOT, INK, 3)                # roof
    for k in range(6):                                                      # tall arched windows
        x = 418 + k * 46
        f.path(f"M{x},338 V292 Q{x + 13},274 {x + 26},292 V338 Z", GLASS, INK, 2)
        f.line(x + 13, 284, x + 13, 338, INK, 1.5)
    f.rect(530, 340, 30, 14, IRON, INK, 2)
    # outlets: water foaming out of three tunnels below the station
    for k, x in enumerate((440, 545, 650)):
        f.path(f"M{x - 26},462 Q{x - 26},432 {x},432 Q{x + 26},432 {x + 26},462 Z", INK)
        for j in range(6):
            r = 10 + 8 * rnd(j + 7 * k, 4)
            f.circle(x - 30 + 12 * j, 470 + 10 * rnd(j + 3 * k, 6), r, WHITE)
        f.add(f'<ellipse cx="{x}" cy="492" rx="56" ry="10" fill="{WHITE}" fill-opacity="0.75"/>')
    # the power line from the station to the left
    a1 = H.pylon(f, 250, 360, 130, 0.9)
    a2 = H.pylon(f, 90, 400, 170, 1.1)
    for p, q in zip(a1, a2): H.wire(f, p, q, 24, INK, 1.5)
    for p in a1: H.wire(f, p, (400, 280), 14, INK, 1.5)
    # near bank: birches and a rock
    H.birch(f, 1080, 470, 150); H.birch(f, 1150, 500, 120); H.spruce(f, 170, 560, 150); H.spruce(f, 240, 590, 120)
    f.path("M880,560 Q900,520 950,522 Q990,526 996,566 Z", IRON, INK, 2.5)
    return f.svg()


# ---------------------------------------------------------------- theory figures
def vesivoimala():
    """A hydropower station in cross-section: the upper water, the penstock, the turbine and generator, the lower water,
    the head h between the two water levels; energy flow: E_p of the water, E_k in the pipe, electric power out."""
    f = Fig("fy415-vv", 360, "Periaatekuva vesivoimalasta poikkileikkauksena, ei mittakaavassa. Vasemmalla padon takana on "
            "yläallas, jonka pinta on korkealla. Vesi virtaa padon läpi kulkevaa putkea alas turbiiniin, joka pyörittää "
            "akselin välityksellä generaattoria. Turbiinin jälkeen vesi purkautuu oikealle alaveteen. Ylä- ja alaveden "
            "pintojen korkeusero on putouskorkeus h. Veden potentiaalienergia muuttuu putkessa liike-energiaksi, turbiinissa "
            "pyörimisen energiaksi ja generaattorissa sähköksi, jota kuvaa oranssi nuoli.")
    water = grad(f, "fy415-vvw", WATER_LIGHT, WATER)
    f.path("M12,250 H200 V346 H12 Z", grad(f, "fy415-vvg", SAND_LIGHT, SAND))                  # ground under the reservoir
    f.path("M12,92 Q40,86 70,92 T130,92 T190,92 L200,92 V250 H12 Z", water)                       # upper water
    f.path("M16,92 Q40,86 70,92 T130,92 T196,92", stroke=WHITE, w=2.5, extra='stroke-opacity="0.85"')
    f.path("M200,64 H250 L330,180 H468 V346 H200 Z", grad(f, "fy415-vvc", ALUMINIUM, METAL_EDGE), INK, 3)   # dam and station
    f.path("M468,290 Q500,284 530,290 T588,290 V346 H468 Z", water)                              # lower water
    f.path("M472,290 Q500,284 530,290 T584,290", stroke=WHITE, w=2.5, extra='stroke-opacity="0.85"')
    # penstock and outlet
    f.path("M200,214 L338,292", stroke=INK, w=28, extra='stroke-linecap="butt"')
    f.path("M200,214 L338,292", stroke=WATER, w=22, extra='stroke-linecap="butt"')
    f.path("M372,300 L468,312", stroke=INK, w=28); f.path("M372,300 L470,312", stroke=WATER, w=22)
    # turbine, shaft, generator
    f.line(358, 268, 358, 222, INK, 5)
    f.circle(358, 296, 27, IRON, INK, 2.5)
    for k in range(6):
        a = k * math.pi / 3
        f.path(f"M{n(358 + 6 * math.cos(a))},{n(296 + 6 * math.sin(a))} Q{n(358 + 22 * math.cos(a + 0.5))},{n(296 + 22 * math.sin(a + 0.5))} "
               f"{n(358 + 24 * math.cos(a + 0.9))},{n(296 + 24 * math.sin(a + 0.9))}", stroke=ALUMINIUM, w=3)
    f.circle(358, 296, 6, ALUMINIUM, INK, 1.5)
    f.rect(330, 190, 56, 34, COPPER, INK, 2.5, 4)
    for k in range(4): f.line(338 + 12 * k, 194, 338 + 12 * k, 220, SAND_DARK, 2)
    # electric power out
    f.block_arrow(390, 207, 488, 207, grad(f, "fy415-vve", HEAT_LIGHT, HEAT, horizontal=True), 14, 30, 22)
    f.tex(496, 207, r"P_\text{s}", "start")
    # head h between the water levels
    f.line(272, 92, 578, 92, MUTED, 1.5, "6 5")
    f.path("M570,92 H578 V290 H570", stroke=INK, w=2.5)
    f.tex(562, 200, "h", "end")
    # labels
    f.tex(106, 60, r"\text{yläallas}", "middle")
    f.tex(106, 160, r"E_\text{p} = mgh", "middle", bg=True)
    f.tex(234, 286, r"E_\text{k}", "middle", bg=True)
    f.tex(400, 160, r"\text{generaattori}", "middle")
    f.tex(300, 330, r"\text{turbiini}", "middle", bg=True)
    f.tex(520, 322, r"\text{alavesi}", "middle", bg=True)
    return f.svg()


def ilmalierio():
    """The air that passes the rotor in time t fills a cylinder of cross-section A and length vt: m = ρAvt."""
    f = Fig("fy415-il", 360, "Periaatekuva, ei mittakaavassa: tuuli puhaltaa vasemmalta tuulivoimalan roottoria kohti. Ajassa t "
            "roottorin läpi virtaa ilma, joka täyttää lieriön. Lieriön poikkipinta-ala on roottorin pyyhkäisemä pinta-ala "
            "A = πr² ja pituus s = vt, joten ilman massa on m = ρAvt. Sininen nuoli on tuulen nopeus v.")
    cyl = grad(f, "fy415-ilc", GLASS, COLD_LIGHT)
    f.path("M150,70 H420 V270 H150 Z", cyl)
    f.add(f'<ellipse cx="150" cy="170" rx="24" ry="100" fill="{COLD_LIGHT}" stroke="{COLD}" stroke-width="2"/>')
    f.line(150, 70, 420, 70, COLD, 2, "8 6"); f.line(150, 270, 420, 270, COLD, 2, "8 6")
    for k in range(18):                                                    # air parcels
        f.circle(180 + 190 * rnd(k, 3), 90 + 160 * rnd(k, 8), 3, WHITE, COLD, 1.5)
    # the tower, nacelle and the rotor seen from the side
    f.path("M434,182 L428,340 H452 L446,182 Z", WHITE, INK, 2)
    f.add(f'<ellipse cx="420" cy="170" rx="10" ry="100" fill="none" stroke="{COLD}" stroke-width="2" stroke-dasharray="8 6"/>')
    f.path("M420,166 Q412,118 418,70 L424,70 Q428,120 424,166 Z", WHITE, INK, 2)
    f.path("M420,174 Q412,222 418,270 L424,270 Q428,220 424,174 Z", WHITE, INK, 2)
    f.rect(424, 158, 52, 24, WHITE, INK, 2, 6)
    f.circle(421, 170, 9, ALUMINIUM, INK, 2)
    f.line(12, 340, 588, 340, RULE, 2)
    # wind velocity
    f.arrow(24, 170, 116, 170, COLD, 3, 16)
    f.tex(70, 140, r"\overline{v}", "middle", COLD)
    # dimensions and labels
    f.path("M150,288 V300 H420 V288", stroke=INK, w=2)
    f.tex(285, 318, r"s = vt", "middle")
    f.tex(285, 170, r"m = \rho A v t", "middle", bg=True)
    f.line(400, 170, 400, 74, INK, 2)
    f.tex(392, 122, "r", "end", bg=True)
    f.tex(488, 108, r"A = \pi r^2", "start")
    return f.svg()


def _curve(model=True):
    f = Fig("fy415-pk" if model else "fy415-pkp", 340,
            ("Kuvaaja mittakaavassa, valmistajan ilmoittama tehokäyrä: tuulivoimalan sähköteho P kilowatteina tuulen nopeuden v "
             "funktiona, kun roottorin halkaisija on 82 m. Pisteet: 3 m/s 0 kW, 4 m/s 28 kW, 5 m/s 144 kW, 6 m/s 309 kW, "
             "7 m/s 511 kW, 8 m/s 758 kW, 9 m/s 1017 kW, 10 m/s 1285 kW, 11 m/s 1504 kW, 12 m/s 1637 kW ja 13–20 m/s 1650 kW. "
             + ("Katkoviivana mallin käyrä ½ηρAv³, kun η = 0,45: se nousee kuten pisteet mutta jatkaa nousuaan, kun pisteet "
                "tasaantuvat 1650 kilowattiin." if model else "Pisteiden välissä ei ole käyrää.")))
    ax = Axes(f, (96, 296), (470, 50), x=(0, 20), y=(0, 1800), xticks=list(range(2, 21, 2)), yticks=list(range(200, 1801, 200)),
              xlabel=r"v\ (\text{m/s})", ylabel=r"P\ (\text{kW})",
              xfmt=lambda v: fi(v) if v % 4 == 0 else "", yfmt=lambda v: fi(v) if v % 400 == 0 else "")
    if model:
        vmax = (1800e3 / (0.45 * 0.5 * RHO_A * A82)) ** (1 / 3)
        ax.curve(lambda v: 0.45 * 0.5 * RHO_A * A82 * v ** 3 / 1e3, 0, vmax, HEAT, 3, dash="9 6")
        f.tex(ax.X(vmax) - 12, ax.Y(1800) + 4, r"\tfrac{1}{2}\eta\rho A v^3", "end", HEAT, bg=True)
    for v, P in V82:
        ax.point(v, P, INK)
    f.tex(ax.X(16.5), ax.Y(1430), r"\text{tehokäyrä}", "middle", bg=True)
    return f.svg()


def tehokayra(): return _curve(True)
def tehokayra_pisteet(): return _curve(False)


FIGURES = {"hero": hero, "vesivoimala": vesivoimala, "ilmalierio": ilmalierio, "tehokayra": tehokayra,
           "tehokayra-pisteet": tehokayra_pisteet}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "vesivoimala": "safe: the parts of a hydropower station, the head h and the energy chain, no numbers",
    "ilmalierio": "reveals: the derivation m = ρAvt of the wind's mass flow",
    "tehokayra": "reveals: the model curve ½ηρAv³ beside a real power curve",
    "tehokayra-pisteet": "safe: the real V82 power curve as points only, values listed",
}
