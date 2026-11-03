"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy8-2` writes them into lesson.md.
Spectral lines are drawn in their real colour (FY8 conventions), always with a wavelength label or an axis, so colour
never carries the meaning alone. Hydrogen levels E_n = -13,6 eV / n² (data) and λ = hc/ΔE as in lesson-answers.py."""
import math
from figlib import (Fig, fi, INK, MUTED, WHITE, RULE, RULE_LIGHT, HEAT, HEAT_LIGHT, HOT, HOT_LIGHT, COLD, COLD_LIGHT,
                    GLASS, ICE, SAND, SAND_LIGHT, SAND_DARK, GRAIN, GOOD, GOOD_LIGHT, ALUMINIUM, METAL_EDGE, IRON, PAPER, n)
import herolib as H

HC = 6.626e-34 * 2.998e8 / 1.602e-19 * 1e9       # hc in eV·nm
E = lambda k: -13.6 / k ** 2                      # hydrogen level k in eV (data)
BALMER = [HC / (E(k) - E(2)) for k in (3, 4, 5, 6)]   # 656,5; 486,3; 434,2; 410,3 nm
MERCURY = [405, 436, 546, 577, 579]               # nm, the lines of the task figure (NIST, rounded)


def wl_hex(lam):
    """The colour of light of wavelength lam (nm) on a screen (Bruton's approximation), dimmed at the ends of the eye's range."""
    if lam < 440: r, g, b = -(lam - 440) / 60, 0.0, 1.0
    elif lam < 490: r, g, b = 0.0, (lam - 440) / 50, 1.0
    elif lam < 510: r, g, b = 0.0, 1.0, -(lam - 510) / 20
    elif lam < 580: r, g, b = (lam - 510) / 70, 1.0, 0.0
    elif lam < 645: r, g, b = 1.0, -(lam - 645) / 65, 0.0
    else: r, g, b = 1.0, 0.0, 0.0
    f = 0.3 + 0.7 * (lam - 380) / 40 if lam < 420 else 0.3 + 0.7 * (750 - lam) / 50 if lam > 700 else 1.0
    return "#" + "".join(f"{round(255 * (max(0.0, min(1.0, v)) * f) ** 0.8):02x}" for v in (r, g, b))


def rainbow(f, gid, lo=380, hi=720, step=10, vertical=False):
    stops = "".join(f'<stop offset="{(l - lo) / (hi - lo):.3f}" stop-color="{wl_hex(l)}"/>' for l in range(lo, hi + 1, step))
    xy = 'x1="0" y1="0" x2="0" y2="1"' if vertical else 'x1="0" y1="0" x2="1" y2="0"'
    f.defs_add(f'<linearGradient id="{gid}" {xy}>{stops}</linearGradient>')


def wavy(f, x1, y1, x2, y2, color, w=3, waves=3.5, amp=7, head=14):
    """A photon: a wavy line from (x1, y1) with a filled arrowhead at (x2, y2) (FY8 conventions)."""
    L = math.hypot(x2 - x1, y2 - y1); ux, uy = (x2 - x1) / L, (y2 - y1) / L; px, py = -uy, ux
    run = L - head
    pts = []
    for i in range(0, 81):
        s = run * i / 80
        o = amp * math.sin(2 * math.pi * waves * s / run) * min(1, s / 10, (run - s) / 10 + 0.2)
        pts.append(f"{n(x1 + ux * s + px * o)},{n(y1 + uy * s + py * o)}")
    f.path("M" + " L".join(pts), stroke=color, w=w, extra='stroke-linecap="round"')
    bx, by = x2 - ux * head, y2 - uy * head; hw = head * 0.5
    f.path(f"M{n(x2)},{n(y2)} L{n(bx + px * hw)},{n(by + py * hw)} L{n(bx - px * hw)},{n(by - py * hw)} Z", fill=color)


def spectra():
    f = Fig("fy82-spectra", 396, "Kaavakuva kolmesta vedyn spektristä samalla aallonpituusasteikolla 380–720 nanometriä. Ylimpänä "
            "hehkulampun jatkuva spektri: kaikki värit violetista punaiseen yhtenäisenä kaistana. Keskellä kuuman, "
            "ohuen vetykaasun emissiospektri: mustalla pohjalla neljä kirkasta viivaa aallonpituuksilla 410, 434, 486 ja "
            "656 nanometriä. Alimpana absorptiospektri, kun jatkuva valo kulkee kuuman vetykaasun läpi, kuten tähden kaasukehässä: jatkuvassa "
            "värikaistassa on tummat viivat täsmälleen samoilla aallonpituuksilla, mitä korostavat katkoviivat. "
            "Aallonpituusasteikko on mittakaavassa.")
    rainbow(f, "fy82-rb")
    x0, x1, lo, hi = 232, 572, 380, 720
    X = lambda l: x0 + (l - lo) / (hi - lo) * (x1 - x0)
    tops = (24, 118, 212)
    for y, title, kind in zip(tops, (r"\text{jatkuva spektri}", r"\text{emissiospektri}", r"\text{absorptiospektri}"), ("cont", "em", "abs")):
        f.tex(116, y + (56 if kind == "abs" else 62), title, "middle", w=210)
        if kind == "em":
            f.rect(x0, y + 4, x1 - x0, 44, INK)
            for l in BALMER: f.rect(X(l) - 2.5, y + 4, 5, 44, wl_hex(l))
        else:
            f.rect(x0, y + 4, x1 - x0, 44, "url(#fy82-rb)")
            if kind == "abs":
                for l in BALMER: f.rect(X(l) - 2, y + 4, 4, 44, INK)
        f.rect(x0, y + 4, x1 - x0, 44, stroke=INK, sw=2)
    for l in BALMER:                                   # the same wavelengths in emission and absorption
        f.line(X(l), 166, X(l), 216, MUTED, 1.5, "4 4")
    # the sources, schematic, above their titles
    cx = 116
    f.circle(cx, 22, 15, HEAT_LIGHT, INK, 2.5)         # incandescent bulb with its filament
    f.path(f"M{cx - 7},25 q3.5,-8 7,0 q3.5,-8 7,0", stroke=HEAT, w=2)
    f.rect(cx - 6, 37, 12, 8, ALUMINIUM, INK, 2, 2)
    f.rect(cx - 46, 116, 92, 22, HOT_LIGHT, INK, 2.5, 11)   # a hydrogen discharge tube glows
    f.rect(cx - 56, 120, 12, 14, IRON, INK, 2, 2); f.rect(cx + 44, 120, 12, 14, IRON, INK, 2, 2)
    f.circle(cx - 46, 228, 14, HEAT_LIGHT, INK, 2.5)   # bulb behind a cell of gas
    f.rect(cx - 22, 210, 72, 36, GLASS, INK, 2, 8)
    for dx, dy in ((-10, 220), (6, 236), (20, 222), (34, 238), (-4, 232), (28, 228)):
        f.circle(cx + dx, dy, 3, HOT)                # hot gas, as in a star's atmosphere
    f.tex(cx, 298, r"\text{(kuuma kaasu)}", "middle", MUTED, w=210)
    # wavelength axis
    yA = 308
    f.line(x0, yA, x1, yA, INK, 2)
    for l in range(400, 701, 20):
        f.line(X(l), yA, X(l), yA + (8 if l % 100 == 0 else 5), INK, 2 if l % 100 == 0 else 1.5)
    for l in (400, 500, 600, 700): f.tex(X(l), yA + 26, fi(l), "middle")
    f.tex(x0 - 14, yA + 26, r"\lambda\ (\text{nm})", "end")
    f.tex(X(656), yA + 60, r"\text{punainen}", "middle", MUTED)
    f.tex(X(425), yA + 60, r"\text{violetti}", "middle", MUTED)
    return f.svg()


def fluorescence():
    f = Fig("fy82-fluo", 352, "Energiatasokaavio fluoresenssista, energiat mittakaavassa. Väriaineen molekyyli on alussa "
            "perustilassa. Se absorboi ultraviolettifotonin, jonka aallonpituus on 365 nanometriä ja energia 3,40 "
            "elektronivolttia, ja siirtyy viritystilaan. Viritystilassa molekyyli luovuttaa pienin askelin osan "
            "energiasta lämpönä ja laskee viritystilan alimmalle tasolle. Sieltä se palaa perustilaan ja lähettää "
            "näkyvän valon fotonin, jonka aallonpituus on 520 nanometriä ja energia 2,38 elektronivolttia. "
            "Lähetetyn fotonin energia on pienempi ja aallonpituus pidempi kuin absorboidun.")
    ppe = 190 / 3.40                                    # pixels per eV: the UV photon 3,40 eV is 190 px
    yg = 290; ytop = yg - 190; ylow = yg - 2.38 * ppe   # 100 and 157
    f.rect(186, yg, 236, 6, INK)                        # ground state
    f.tex(176, yg + 3, r"\text{perustila}", "end")
    for k in range(4):                                  # the excited state's sublevels (molecular vibration)
        y = ytop + k * (ylow - ytop) / 3
        f.line(186, y, 422, y, INK, 3 if k == 3 else 2)
    f.tex(176, (ytop + ylow) / 2, r"\text{viritystila}", "end")
    uv, vis = wl_hex(400), wl_hex(520)
    f.arrow(230, yg, 230, ytop + 2, uv, 4, 16)                       # absorption: up
    wavy(f, 20, 230, 218, 230, uv, 3, 4)
    f.tex(118, 198, r"hf_\text{UV}", "middle", w=70)
    f.tex(118, 258, r"365\,\text{nm}", "middle", w=100)
    for k in range(3):                                  # small steps down: energy to heat
        y = ytop + k * (ylow - ytop) / 3
        f.arrow(300, y + 2, 300, y + (ylow - ytop) / 3 - 1, HEAT, 2.5, 10)
    f.tex(312, ytop - 26, r"\text{lämpöä}", "start", HEAT)
    f.arrow(380, ylow, 380, yg - 2, GOOD, 4, 16)                     # emission: down
    wavy(f, 392, 230, 584, 230, GOOD, 3, 4)
    f.tex(488, 198, r"hf_\text{näkyvä}", "middle", w=110)
    f.tex(488, 258, r"520\,\text{nm}", "middle", w=100)
    f.tex(230, yg + 34, r"3{,}40\,\text{eV}", "middle", w=100)
    f.tex(380, yg + 34, r"2{,}38\,\text{eV}", "middle", w=100)
    return f.svg()


def levels():
    f = Fig("fy82-levels", 380, "Vetyatomin energiatasokaavio, energia-akseli mittakaavassa. Tasot n = 1, 2, 3, 4, 5, 6 ovat "
            "energioilla −13,6; −3,40; −1,51; −0,85; −0,54 ja −0,38 elektronivolttia, ja ylimpänä on energia nolla, "
            "jossa elektroni on irti atomista. Ylimmät tasot ovat hyvin lähellä toisiaan. Neljä alaspäin osoittavaa "
            "nuolta kuvaa emissiota tasoilta 3, 4, 5 ja 6 tasolle 2; niiden fotonien aallonpituudet 656, 486, 434 ja "
            "410 nanometriä on merkitty nuolten alle, ja nuolet on väritetty valon värillä. Oikealla ylöspäin "
            "osoittava nuoli kuvaa absorptiota perustilasta tasolle 2: atomi absorboi aaltoviivana piirretyn "
            "ultraviolettifotonin, jonka aallonpituus on 122 nanometriä.")
    Y = lambda En: 48 + (-En) * 22
    xl, xr = 138, 466
    f.tex(20, 18, r"E\ (\text{eV})", "start")
    f.line(xl, Y(0), xr, Y(0), MUTED, 2, "7 5")
    for k in range(1, 7):
        f.line(xl, Y(E(k)), xr, Y(E(k)), INK, 3 if k <= 3 else 2)
    for En, s in ((0, "0"), (E(3), r"-1{,}51"), (E(2), r"-3{,}40"), (E(1), r"-13{,}6")):
        f.tex(xl - 10, Y(En), s, "end")
    f.tex(xr + 10, Y(E(1)), r"n = 1", "start")
    f.tex(xr + 10, Y(E(2)), r"n = 2", "start")
    f.tex(xr + 10, Y(E(3)) + 2, r"n = 3", "start")
    f.tex(xr + 10, Y(0) + 2, r"n = 4, 5, \ldots", "start", w=118)
    for i, k in enumerate((3, 4, 5, 6)):
        x = 196 + 62 * i; lam = HC / (E(k) - E(2))
        f.arrow(x, Y(E(k)), x, Y(E(2)) - 1, wl_hex(lam), 4, 13)
        f.tex(x, 150, fi(round(lam)), "middle")
    f.tex(289, 184, r"\text{emissio, } \lambda\ (\text{nm})", "middle", w=220)
    xa = 420
    f.arrow(xa, Y(E(1)) - 1, xa, Y(E(2)) + 2, MUTED, 4, 14)
    wavy(f, 584, 260, xa + 8, 260, MUTED, 3, 3)
    f.tex(512, 232, r"hf", "middle")
    f.tex(512, 290, r"122\,\text{nm}", "middle", w=100)
    f.tex(xa - 12, 232, r"\text{absorptio}", "end", w=140)
    f.circle(xa, Y(E(1)), 8, COLD, WHITE, 2)
    f.tex(xa - 14, Y(E(1)) - 24, r"e^-", "end", COLD)
    return f.svg()


def greenhouse():
    f = Fig("fy82-gh", 340, "Periaatekuva kasvihuoneilmiöstä, ei mittakaavassa, yksinkertaistettu. Auringon näkyvä valo kulkee ilmakehän läpi "
            "maanpinnalle, koska ilmakehän kaasut eivät juuri absorboi näkyvää valoa. Lämmennyt maanpinta säteilee "
            "infrapunaa. Hiilidioksidimolekyyli absorboi infrapunafotonin ja lähettää sitten uuden infrapunafotonin "
            "satunnaiseen suuntaan, tässä kaksi fotonia: toinen alaspäin kohti maanpintaa ja toinen ylös- ja oikealle avaruuteen päin.")
    f.defs_add(f'<linearGradient id="fy82-air" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{COLD_LIGHT}"/><stop offset="1" stop-color="{GLASS}"/></linearGradient>')
    f.rect(12, 12, 576, 262, "url(#fy82-air)")
    f.rect(12, 274, 576, 54, GOOD_LIGHT, None)
    f.line(12, 274, 588, 274, GOOD, 3)
    H.sun(f, "fy82-sun", 70, 66, r=30, rays=False)
    wavy(f, 98, 98, 214, 266, HEAT, 3.5, 4, 8)
    f.tex(170, 140, r"\text{näkyvä valo}", "start", w=150)
    wavy(f, 300, 268, 386, 150, HOT, 3.5, 5, 9)
    f.tex(350, 240, r"\text{infrapuna}", "start", w=130)
    cx, cy = 420, 118                                   # O=C=O
    f.circle(cx - 30, cy, 14, HOT_LIGHT, INK, 2); f.circle(cx + 30, cy, 14, HOT_LIGHT, INK, 2); f.circle(cx, cy, 16, IRON, INK, 2)
    f.tex(cx, cy - 40, r"\text{CO}_2", "middle")
    wavy(f, cx + 34, cy + 22, 548, 266, HOT, 3.5, 5, 9)
    wavy(f, cx + 40, cy - 10, 566, 44, HOT, 3.5, 3, 8)
    f.tex(300, 304, r"\text{maanpinta}", "middle", w=140)
    return f.svg()


def lamp_spectrum():
    """Task figure: the emission spectrum of an unknown lamp, lines at 405, 436, 546, 577 and 579 nm (mercury); the
    element is not named, the student compares the lines with a table."""
    f = Fig("fy82-lamp", 196, "Kuva mittakaavassa: tuntemattoman lampun emissiospektri mustalla pohjalla aallonpituusasteikolla "
            "380–720 nanometriä. Asteikon pienet jakoviivat ovat 10 nanometrin välein ja luvut 50 nanometrin välein. "
            "Spektrissä on violetti viiva noin 405 nanometrin kohdalla, sininen noin 436, vihreä noin 546 ja kaksi "
            "lähekkäistä keltaista viivaa noin 577 ja 579 nanometrin kohdalla.")
    x0, x1, lo, hi = 40, 560, 380, 720
    X = lambda l: x0 + (l - lo) / (hi - lo) * (x1 - x0)
    f.rect(x0, 30, x1 - x0, 70, INK)
    for l in MERCURY: f.rect(X(l) - 2, 30, 4, 70, wl_hex(l) if l >= 420 else "#a46bff")   # 405 nm lightened to read on black
    f.rect(x0, 30, x1 - x0, 70, stroke=INK, sw=2)
    yA = 110
    f.line(x0, yA, x1, yA, INK, 2)
    for l in range(380, 721, 10):
        big = l % 50 == 0
        f.line(X(l), yA, X(l), yA + (10 if big else 5), INK, 2 if big else 1.5)
        if big: f.tex(X(l), yA + 30, fi(l), "middle")
    f.tex(x1 + 2, yA + 62, r"\lambda\ (\text{nm})", "end")
    return f.svg()


def hero():
    """Opening illustration: sunlight through a slit and a glass prism spreads into the colours on a screen, and thin dark lines cross the colours."""
    f = Fig("fy82-hero", 600, "Kuvitus: pimeän huoneen ikkunaluukussa on kapea rako, josta auringonvalo tulee säteenä "
            "pöydällä olevaan lasiprismaan. Prisma hajottaa valon väreiksi punaisesta violettiin, ja värit osuvat "
            "valkoiseen varjostimeen. Värikaistan poikki kulkee kapeita tummia viivoja.", width=1200, hero=True)
    rainbow(f, "fy82h-rb", 400, 700, 5, vertical=True)
    f.rect(0, 0, 1200, 600, PAPER)
    f.rect(0, 0, 1200, 470, "#e9c98a", extra='fill-opacity="0.35"')
    f.rect(0, 470, 1200, 130, SAND_LIGHT)
    f.line(0, 470, 1200, 470, SAND, 4)
    # the window: the sky and the sun above, a closed shutter with a narrow slit below
    f.rect(60, 70, 240, 150, H.grad(f, "fy82h-sky", ICE, GLASS), INK, 5, 6)
    H.sun(f, "fy82h-sun", 180, 140, r=36)
    f.rect(60, 220, 240, 70, IRON, INK, 4, 4); f.rect(60, 304, 240, 76, IRON, INK, 4, 4)    # shutter, slit at y 290–304
    for y in (240, 260, 324, 344, 364): f.line(72, y, 288, y, METAL_EDGE, 3)
    # the beam from the slit to the prism
    f.path("M300,290 L300,304 L566,336 L560,318 Z", "#ffffff", extra='fill-opacity="0.9"')
    # the prism on a small table
    f.rect(500, 400, 200, 22, SAND_DARK, INK, 3, 4)
    f.rect(520, 422, 14, 48, SAND, INK, 3); f.rect(666, 422, 14, 48, SAND, INK, 3)
    # the fan of colours from the prism to the screen
    # apex down: glass bends light toward the base (up here), violet the most, so violet lands on top
    f.path("M633,330 L625,346 L960,360 L960,170 Z", "url(#fy82h-rb)", extra='fill-opacity="0.85"')
    f.path("M540,280 L660,280 L600,392 Z", GLASS, INK, 4, extra='fill-opacity="0.85"')
    f.path("M556,292 L592,360", stroke=WHITE, w=4, extra='stroke-linecap="round" stroke-opacity="0.9"')
    f.path("M578,400 L590,376 L610,376 L622,400 Z", SAND_DARK, INK, 3)   # the holder the apex rests in
    # the screen with the spectrum and its dark lines
    f.rect(940, 120, 210, 360, WHITE, INK, 4, 6)
    f.rect(964, 170, 162, 190, "url(#fy82h-rb)")
    for y in (196, 220, 263, 283, 324, 344): f.line(964, y, 1126, y, INK, 3)
    f.rect(964, 170, 162, 190, stroke=INK, sw=2)
    f.rect(1020, 480, 50, 10, IRON, INK, 3, 2)
    f.line(1045, 470, 1045, 480, INK, 3)
    return f.svg()


FIGURES = {"hero": hero, "spectra": spectra, "fluorescence": fluorescence, "levels": levels, "greenhouse": greenhouse,
           "lamp-spectrum": lamp_spectrum}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "spectra": "reveals: emission and absorption lines of hydrogen at the same wavelengths",
    "fluorescence": "reveals: the emitted photon has less energy than the absorbed one (3,40 eV in, 2,38 eV out)",
    "levels": "reveals: the Balmer wavelengths 656, 486, 434, 410 nm and the 122 nm absorption",
    "greenhouse": "safe: schematic of visible light passing and CO2 absorbing and re-emitting infrared",
    "lamp-spectrum": "safe: emission lines of an unknown lamp at 405, 436, 546, 577 and 579 nm, the element not named",
}
