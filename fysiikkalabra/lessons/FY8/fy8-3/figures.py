"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy8-3` writes them into lesson.md.
Hydrogen levels E_n = -13,6 eV / n² (data, FY8 scope); wavelengths from lambda = hc / (E_y - E_a) as in lesson-answers.py."""
import math
from figlib import (Fig, INK, MUTED, WHITE, RULE, RULE_LIGHT, HEAT, HEAT_LIGHT, HOT, HOT_LIGHT, COLD, COLD_LIGHT, GLASS,
                    ALUMINIUM, METAL_EDGE, IRON, SAND, SAND_LIGHT, SAND_DARK, GRAIN, PAPER, n)

H_, C_, E_ = 6.626e-34, 2.998e8, 1.602e-19
E1 = 13.6
def En(k): return -E1 / k ** 2
def lam(a, b): return H_ * C_ / ((En(a) - En(b)) * E_) * 1e9      # nm, transition a -> b

# the real colours of the four visible hydrogen lines (FY8 brief: lines in their real colour, never colour alone)
LINE = {3: HOT, 4: "#1098ad", 5: "#4263eb", 6: "#7048e8"}            # 656 nm red, 486 nm cyan, 434 nm blue, 410 nm violet
ELECTRON = COLD


def photon(f, x1, y1, x2, y2, color=HEAT, w=3, amp=7, waves=None, head=15):
    """A photon: a wavy arrow from (x1, y1) to the tip (x2, y2), the wave along the shaft and a filled head."""
    L = math.hypot(x2 - x1, y2 - y1); ux, uy = (x2 - x1) / L, (y2 - y1) / L; px, py = -uy, ux
    shaft = L - head; waves = waves or max(2, round(shaft / 26))
    pts = []
    for i in range(0, 121):
        t = i / 120 * shaft
        s = amp * math.sin(2 * math.pi * waves * t / shaft) * min(1, t / 6, (shaft - t) / 6)
        pts.append(f"{n(x1 + ux * t + px * s)},{n(y1 + uy * t + py * s)}")
    f.path("M" + " L".join(pts), stroke=color, w=w, extra='stroke-linecap="round"')
    bx, by = x2 - ux * head, y2 - uy * head; hw = head * 0.5
    f.path(f"M{n(x2)},{n(y2)} L{n(bx + px * hw)},{n(by + py * hw)} L{n(bx - px * hw)},{n(by - py * hw)} Z", fill=color)


def electron(f, x, y, r=8, fill=ELECTRON):
    f.circle(x, y, r, fill, WHITE, 2)


def levels():
    """Ydinajatus: the hydrogen levels to scale above a shortened gap, with the Lyman and Balmer transitions."""
    f = Fig("fy83-lv", 400, "Vetyatomin energiatasokaavio. Pystysuunnassa energia; tasot n = 2, 3, 4, 5 ja 6 sekä energia nolla "
            "ylimpänä ovat mittakaavassa, mutta tasojen n = 1 ja n = 2 väliä on lyhennetty, mikä on merkitty katkoviivalla. "
            "Tasojen energiat: n = 1: −13,6 eV, n = 2: −3,40 eV, n = 3: −1,51 eV, n = 4: −0,85 eV, ylimpänä 0 eV, jossa "
            "elektroni on irti atomista. Tasot tihenevät ylöspäin. Kaksi mustaa nuolta kuvaa siirtymiä tasoille n = 1 "
            "(Lymanin sarja, ultraviolettia), neljä värillistä nuolta siirtymiä tasoilta 3, 4, 5 ja 6 tasolle n = 2 "
            "(Balmerin sarja, näkyvää valoa: punainen, syaani, sininen ja violetti).")
    k, y0 = 68, 70                                  # px per eV above the gap, y of E = 0
    Y = lambda e: y0 - k * e
    y1 = 366                                        # n = 1, below the shortened gap
    # vertical energy axis with a break mark
    f.arrow(26, 384, 26, 34, INK, 2.5, 13)
    f.tex(36, 30, "E", "start")
    f.path("M18,350 L34,344 M18,360 L34,354", stroke=WHITE, w=6)
    f.path("M18,350 L34,344 M18,360 L34,354", stroke=INK, w=2)
    # levels
    f.line(150, y0, 430, y0, INK, 2, "8 5")
    for m in range(2, 7):
        f.line(150, Y(En(m)), 430, Y(En(m)), INK, 2.5)
    f.line(150, y1, 430, y1, INK, 3)
    f.tex(140, 64, r"n \to \infty", "end")
    f.tex(140, 97, r"n = 5, 6", "end")
    f.tex(140, 131, r"n = 4", "end")
    f.tex(140, Y(En(3)), r"n = 3", "end")
    f.tex(140, Y(En(2)), r"n = 2", "end")
    f.tex(140, y1, r"n = 1", "end")
    f.tex(440, y0, r"0\,\text{eV}", "start")
    f.tex(440, 131, r"-0{,}85\,\text{eV}", "start")
    f.tex(440, Y(En(3)), r"-1{,}51\,\text{eV}", "start")
    f.tex(440, Y(En(2)), r"-3{,}40\,\text{eV}", "start")
    f.tex(440, y1, r"-13{,}6\,\text{eV}", "start")
    # Lyman: 2 -> 1 and 3 -> 1, ink (ultraviolet is not visible)
    for x, m in ((176, 2), (206, 3)):
        f.arrow(x, Y(En(m)), x, y1 - 1, INK, 3, 14)
    f.tex(216, 333, r"\text{Lyman (UV)}", "start")
    # Balmer: m -> 2 in the line's colour
    for x, m in ((262, 3), (302, 4), (342, 5), (382, 6)):
        f.arrow(x, Y(En(m)), x, Y(En(2)) - 1, LINE[m], 3.5, 15)
    f.tex(392, 238, r"\text{Balmer (näkyvä)}", "start")
    return f.svg()


def absorption():
    """Ydinajatus: three photons meet a hydrogen atom in its ground state: absorbed, passes, ionises."""
    f = Fig("fy83-ab", 400, "Kolme tilannetta vierekkäin, energia-asteikko mittakaavassa. Kussakin on vetyatomin tasot n = 1, 2 ja 3 "
            "sekä katkoviivana energia nolla, ja elektroni on aluksi perustilassa n = 1. Vasemmalla tulee fotoni, jonka "
            "energia on 10,2 eV, täsmälleen tasojen 1 ja 2 erotus: fotoni absorboituu ja elektroni siirtyy tasolle 2. "
            "Keskellä fotonin energia on 11,0 eV, joka ei ole minkään tasoparin erotus: fotoni menee läpi, ja elektroni jää "
            "tasolle 1. Oikealla fotonin energia on 14,0 eV, enemmän kuin ionisaatioenergia 13,6 eV: elektroni irtoaa atomista.")
    top, k = 60, 16                                 # y of E = 0, px per eV
    Y = lambda e: top - k * e
    f.line(200, 14, 200, 386, RULE, 2, "6 6")
    f.line(400, 14, 400, 386, RULE, 2, "6 6")
    cases = ((0, r"10{,}2", r"\text{absorboituu}"), (1, r"11{,}0", r"\text{menee läpi}"), (2, r"14{,}0", r"\text{ionisoi}"))
    for i, e, cap in cases:
        x0 = 200 * i
        a, b = x0 + 60, x0 + 182                     # level lines
        f.line(a, top, b, top, INK, 2, "7 5")
        for m in (1, 2, 3):
            f.line(a, Y(En(m)), b, Y(En(m)), INK, 2.5 if m > 1 else 3)
        if i == 0:
            f.tex(52, Y(En(1)), "1", "end"); f.tex(52, Y(En(2)), "2", "end"); f.tex(52, Y(En(3)), "3", "end"); f.tex(52, top - 6, "0", "end", MUTED)
        ex = x0 + 132
        # the photon comes in along the ground level
        if i == 1:
            photon(f, x0 + 14, 304, x0 + 188, 304, HEAT, 3)
            electron(f, ex, Y(En(1)))
        else:
            photon(f, x0 + 14, 304, ex - 18, Y(En(1)) + 12, HEAT, 3)
            f.circle(ex, Y(En(1)), 8, WHITE, ELECTRON, 2)            # where the electron was
            yt = Y(En(2)) if i == 0 else Y(14.0 - E1)    # freed: E_k = 14,0 eV - 13,6 eV = 0,4 eV, to scale
            f.arrow(ex, Y(En(1)) - 11, ex, yt + 11, ELECTRON, 2.5, 12)
            electron(f, ex, yt)
        f.tex(x0 + 100, 336, r"hf = " + e + r"\,\text{eV}", "middle", HEAT)
        f.tex(x0 + 100, 372, cap, "middle")
    return f.svg()


def bohr():
    """Ydinajatus: Bohr's model, orbits n = 1, 2, 3 with radii in the ratio 1 : 4 : 9, a jump 3 -> 2 and the photon."""
    f = Fig("fy83-bohr", 360, "Bohrin malli vetyatomista. Keskellä ydin eli protoni, sen ympärillä elektronin sallitut ympyräradat "
            "n = 1, 2 ja 3, joiden säteet ovat mittakaavassa suhteessa 1 : 4 : 9. Elektroni siirtyy radalta n = 3 radalle "
            "n = 2, ja atomista lähtee fotoni, jonka energia hf on tasojen energioiden erotus E3 − E2.")
    cx, cy, r1 = 186, 180, 16
    for m in (1, 2, 3):
        f.circle(cx, cy, r1 * m * m, "none", MUTED if m > 1 else INK, 2)
    f.circle(cx, cy, 7, HOT, INK, 2)
    a = math.radians(24)
    xa, ya = cx + 144 * math.cos(a), cy - 144 * math.sin(a)
    xb, yb = cx + 64 * math.cos(a), cy - 64 * math.sin(a)
    f.circle(xa, ya, 8, WHITE, ELECTRON, 2)          # where the electron was
    f.path(f"M{n(xa - 10)},{n(ya + 5)} Q{n((xa + xb) / 2)},{n((ya + yb) / 2 - 26)} {n(xb + 16)},{n(yb - 4)}", stroke=ELECTRON, w=2.5, extra='stroke-dasharray="6 5"')
    f.path(f"M{n(xb + 9)},{n(yb - 1)} L{n(xb + 22)},{n(yb - 10)} L{n(xb + 20)},{n(yb + 4)} Z", ELECTRON)
    electron(f, xb, yb)
    f.tex(xb - 14, yb - 12, r"e^-", "end", ELECTRON)
    photon(f, xa + 24, ya + 6, 540, 196, HEAT, 3.5, 8)
    f.tex(452, 134, "hf", "middle", HEAT)
    f.tex(452, 236, r"hf = E_3 - E_2", "middle", HEAT)
    f.tex(cx, 228, r"n = 2", "middle")
    f.tex(cx, 296, r"n = 3", "middle")
    f.line(cx - 12, cy - 11, 74, 58, MUTED, 1.5)
    f.tex(16, 40, r"n = 1", "start")
    f.tex(cx + 21, cy + 4, r"p^+", "start", HOT)
    return f.svg()


def spectrum():
    """Kaava: the visible Balmer lines on a wavelength scale, with the transition below each line."""
    f = Fig("fy83-sp", 300, "Vedyn näkyvä emissiospektri mittakaavassa aallonpituusakselilla 350–700 nm: tummalla pohjalla neljä "
            "viivaa, 410 nm violetti (siirtymä 6 → 2), 434 nm sininen (5 → 2), 486 nm syaani (4 → 2) ja 656 nm punainen "
            "(3 → 2). Katkoviiva kohdassa 365 nm on sarjan raja, siirtymä äärettömyydestä tasolle 2. Viivat tihenevät "
            "lyhyitä aallonpituuksia kohti.")
    x0, x1, l0, l1 = 40, 470, 350, 700
    X = lambda l: x0 + (l - l0) / (l1 - l0) * (x1 - x0)
    f.rect(x0, 80, x1 - x0, 66, INK, rx=3)
    lim = H_ * C_ / (E1 / 4 * E_) * 1e9
    f.line(X(lim), 84, X(lim), 142, MUTED, 2, "5 4")
    for m in (3, 4, 5, 6):
        x = X(lam(m, 2))
        f.rect(x - 3, 82, 6, 62, LINE[m])
        f.line(x, 70, x, 80, INK, 1.5)
    f.line(X(lim), 70, X(lim), 80, INK, 1.5)
    for m, row in ((6, 58), (5, 28), (4, 58), (3, 58)):
        f.tex(X(lam(m, 2)), row, str(round(lam(m, 2))), "middle")
    f.tex(X(lim), 58, str(round(lim)), "middle", MUTED)
    f.arrow(x0, 160, x1 + 22, 160, INK, 2.5, 13)
    for t in (400, 500, 600, 700):
        f.line(X(t), 160, X(t), 167, INK, 2)
        f.tex(X(t), 186, str(t), "middle", MUTED)
    f.tex(x1 + 28, 160, r"\lambda\ (\text{nm})", "start")
    for m, xl in ((6, 128), (5, 204), (4, 280), (3, X(lam(3, 2)))):
        f.line(X(lam(m, 2)), 202, xl, 238, MUTED, 1.5)
        f.tex(xl, 254, f"{m} \\to 2", "middle")
    f.line(X(lim), 202, 52, 238, MUTED, 1.5)
    f.tex(52, 254, r"\infty \to 2", "middle", MUTED)
    return f.svg()


def levels_task():
    """Task figure: the energy levels of an imagined atom on a scale in eV, four levels; no transition drawn."""
    f = Fig("fy83-lt", 370, "Kuvitteellisen atomin energiatasokaavio mittakaavassa. Pystyakselilla energia E elektronivoltteina "
            "nollasta −9 eV:iin, ruudukon väli 1 eV. Tasot: E1 = −8,0 eV, E2 = −5,0 eV, E3 = −3,0 eV ja E4 = −2,0 eV.")
    ax, k, y0 = 150, 32, 46
    Y = lambda e: y0 - k * e
    for e in range(0, -10, -1):
        f.line(ax, Y(e), 470, Y(e), RULE_LIGHT, 1.5)
        f.line(ax - 7, Y(e), ax, Y(e), INK, 2)
        f.tex(ax - 12, Y(e), "0" if e == 0 else f"-{-e}", "end")
    f.line(ax, Y(-9) + 6, ax, Y(-9), INK, 2.5)
    f.arrow(ax, Y(-9) + 6, ax, 22, INK, 2.5, 13)
    f.tex(ax + 10, 20, r"E\ (\text{eV})", "start")
    for name, e in (("E_1", -8.0), ("E_2", -5.0), ("E_3", -3.0), ("E_4", -2.0)):
        f.line(ax + 40, Y(e), 430, Y(e), INK, 3)
        f.tex(440, Y(e), name, "start")
    return f.svg()


def hero():
    """The chapter's opening illustration: a hydrogen discharge tube glows on its stand; through a grating its light
    falls on a white screen as four coloured lines on a dark background."""
    f = Fig("fy83-hero", 600, "Kuvitus: pimennetyssä luokassa pöydällä on vetyä sisältävä purkausputki jännitelähteen telineessä. "
            "Putki hehkuu vaaleanpunaisen violettina. Sen edessä on telineessä hila, ja hilan takana valkoisella varjostimella "
            "näkyy tummaa taustaa vasten neljä erillistä värillistä viivaa: punainen, syaani, sininen ja violetti.", width=1200, hero=True)
    f.defs_add(f'<linearGradient id="fy83h-wall" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{MUTED}"/><stop offset="1" stop-color="{INK}"/></linearGradient>')
    f.defs_add(f'<linearGradient id="fy83h-desk" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{SAND}"/><stop offset="1" stop-color="{GRAIN}"/></linearGradient>')
    f.defs_add(f'<radialGradient id="fy83h-glow" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="{HOT_LIGHT}" stop-opacity="0.9"/><stop offset="1" stop-color="{HOT_LIGHT}" stop-opacity="0"/></radialGradient>')
    f.defs_add(f'<linearGradient id="fy83h-tube" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{HOT_LIGHT}"/><stop offset="0.5" stop-color="{WHITE}"/><stop offset="1" stop-color="#b197fc"/></linearGradient>')
    f.defs_add(f'<linearGradient id="fy83h-beam" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{HOT_LIGHT}" stop-opacity="0.55"/><stop offset="1" stop-color="{HOT_LIGHT}" stop-opacity="0.08"/></linearGradient>')
    # dark room, desk
    f.rect(0, 0, 1200, 600, "url(#fy83h-wall)")
    f.rect(0, 430, 1200, 170, "url(#fy83h-desk)")
    f.rect(0, 430, 1200, 10, SAND_LIGHT)
    # the lamp housing and the glowing tube
    f.add('<ellipse cx="300" cy="250" rx="170" ry="210" fill="url(#fy83h-glow)"/>')
    f.rect(230, 400, 140, 34, IRON, INK, 3, 6)                 # power supply base
    f.rect(250, 380, 100, 24, METAL_EDGE, INK, 3, 4)
    f.rect(282, 70, 36, 34, METAL_EDGE, INK, 3, 4)             # upper holder
    f.rect(282, 346, 36, 34, METAL_EDGE, INK, 3, 4)            # lower holder
    f.rect(240, 70, 10, 330, ALUMINIUM, INK, 2)                # stand rod
    f.rect(250, 82, 32, 10, ALUMINIUM, INK, 2); f.rect(250, 358, 32, 10, ALUMINIUM, INK, 2)
    f.rect(290, 104, 20, 242, "url(#fy83h-tube)", INK, 2.5, 10)
    f.rect(296, 112, 4, 226, WHITE, extra='fill-opacity="0.7"')
    # the light going right towards the grating and the screen
    f.path("M318,200 L640,170 L640,290 L318,250 Z", "url(#fy83h-beam)")
    # grating on its stand
    f.rect(636, 150, 16, 160, GLASS, INK, 3, 3)
    for y in range(160, 302, 8): f.line(640, y, 648, y, MUTED, 1.5)
    f.rect(640, 310, 8, 120, ALUMINIUM, INK, 2); f.rect(612, 426, 64, 12, IRON, INK, 2.5, 3)
    # fans of coloured light behind the grating, one per line
    tips = ((HOT, 760), ("#1098ad", 900), ("#4263eb", 948), ("#7048e8", 974))
    for col, xs in tips:
        f.path(f"M652,226 L{xs - 4},120 L{xs + 4},120 Z", col, extra='fill-opacity="0.35"')
    # the screen: white board with a dark band and four lines on it
    f.rect(720, 60, 340, 360, WHITE, INK, 3, 6)
    f.rect(740, 100, 300, 70, INK, rx=3)
    for col, xs in tips:
        f.rect(xs - 5, 104, 10, 62, col)
    f.rect(880, 420, 20, 14, IRON, INK, 2.5); f.rect(840, 430, 100, 10, IRON, INK, 2.5, 3)
    # a notebook and pencil on the desk
    f.path("M120,520 L300,498 L330,560 L140,586 Z", WHITE, INK, 3)
    for t in (0.3, 0.5, 0.7):
        f.line(126 + 18 * t * 2, 520 + 66 * t, 306 + 24 * t * 1.2, 498 + 62 * t, COLD_LIGHT, 2)
    f.path("M380,560 L520,520 L526,532 L386,572 Z", HEAT_LIGHT, INK, 2.5)
    return f.svg()


FIGURES = {"hero": hero, "levels": levels, "absorption": absorption, "bohr": bohr, "spectrum": spectrum, "levels-task": levels_task}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "levels": "reveals: the hydrogen level energies and which transitions give visible light",
    "absorption": "reveals: only a photon matching a level difference is absorbed; above 13,6 eV it ionises",
    "bohr": "reveals: orbit radii 1 : 4 : 9 and that the photon carries E3 − E2",
    "spectrum": "reveals: the Balmer wavelengths 410, 434, 486, 656 nm and their transitions",
    "levels-task": "safe: four levels of an imagined atom on a 1 eV grid, no transition or wavelength",
}
