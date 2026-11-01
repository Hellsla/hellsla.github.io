"""Figures of the unit fy14-photoelectric (scripts/figlib.py, herolib.py); `python3 scripts/units.py figures
fy14-photoelectric` writes them into content/en/units/fy14-photoelectric/unit.md. The unit is written in English, so
the decimal sign is a point. Every number drawn is computed here from h, e and c (CODATA, exact) and the work
functions the simulation uses (sodium 2.36 eV, zinc 4.3 eV)."""
import math
import figlib
from figlib import (Fig, Axes, fi, INK, MUTED, WHITE, RULE, RULE_LIGHT, GLASS, ALUMINIUM, METAL_EDGE, IRON, COLD, COLD_LIGHT,
                    HOT, HOT_LIGHT, HEAT, HEAT_LIGHT, SAND, SAND_LIGHT, n)
import herolib as H

figlib.set_language({}, ".")

H_EV = 6.62607015e-34 / 1.602176634e-19        # h / e, in eV·s (= V·s)
HC_NM = H_EV * 2.99792458e8 * 1e9              # hc / e in eV·nm, 1239.84
W_NA, W_ZN = 2.36, 4.3
VIOLET, VIOLET_LIGHT = "#7048e8", "#d0bfff"     # the colour of violet light (not a quantity colour in this unit)
RED_LIGHT = "#ffa8a8"


def hero():
    """Opening illustration of the Why question: a dark lab, an evacuated glass tube with a sodium plate. A large, bright
    red lamp and a small, dim violet lamp shine on the plate; electrons fly out only where the violet light falls."""
    f = H.hero("fy14pe-hero", "Illustration: a darkened laboratory. On a bench stands an evacuated glass tube with a sealed tip, "
               "and a grey metal plate lies inside it. On the left, a large lamp shines a wide, bright red beam onto the left half "
               "of the plate. On the right, a small lamp shines a narrow, dim violet beam onto the right half. Small blue electrons "
               "fly up from the plate only where the violet light falls; under the bright red light the plate stays quiet.")
    f.defs_add(f'<linearGradient id="fy14pe-h-room" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2d3a46"/><stop offset="1" stop-color="{INK}"/></linearGradient>')
    f.defs_add(f'<linearGradient id="fy14pe-h-red" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{HOT}" stop-opacity="0.75"/><stop offset="1" stop-color="{HOT}" stop-opacity="0.35"/></linearGradient>')
    f.defs_add(f'<linearGradient id="fy14pe-h-vio" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{VIOLET}" stop-opacity="0.6"/><stop offset="1" stop-color="{VIOLET}" stop-opacity="0.25"/></linearGradient>')
    f.defs_add(f'<linearGradient id="fy14pe-h-plate" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{ALUMINIUM}"/><stop offset="1" stop-color="{METAL_EDGE}"/></linearGradient>')
    f.defs_add(f'<linearGradient id="fy14pe-h-bench" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{SAND}"/><stop offset="1" stop-color="#a97a35"/></linearGradient>')
    f.rect(0, 0, 1200, 600, "url(#fy14pe-h-room)")
    # a faint wall rule and the bench
    f.line(0, 120, 1200, 120, "#3a4754", 3)
    f.rect(0, 470, 1200, 130, "url(#fy14pe-h-bench)")
    f.line(0, 470, 1200, 470, "#e9c98a", 4)
    # lamps on stands: the red one large (bright), the violet one small (dim)
    def lamp(x, y, r, colour, light, stand_to):
        f.rect(x - 5, y, 10, stand_to - y, METAL_EDGE)
        f.rect(x - 40, stand_to - 10, 80, 12, METAL_EDGE, rx=4)
        f.circle(x, y, r + 8, IRON, INK, 3)
        f.circle(x, y, r, light)
        f.circle(x, y, r * 0.55, WHITE)
        f.add(f'<circle cx="{n(x)}" cy="{n(y)}" r="{n(r * 1.9)}" fill="{colour}" fill-opacity="0.18"/>')
    # beams onto the plate (drawn first, under the tube)
    f.path("M195,150 L345,118 L600,384 L430,384 Z", "url(#fy14pe-h-red)")
    f.path("M1000,190 L1012,210 L742,384 L700,384 Z", "url(#fy14pe-h-vio)")
    lamp(250, 150, 62, HOT, RED_LIGHT, 470)
    lamp(1010, 196, 26, VIOLET, VIOLET_LIGHT, 470)
    # the evacuated tube: glass body, sealed tip on top, highlight
    f.add(f'<rect x="330" y="230" width="540" height="200" rx="100" fill="{GLASS}" fill-opacity="0.22" stroke="{GLASS}" stroke-width="4"/>')
    f.path("M590,230 L590,196 Q600,178 610,196 L610,230", GLASS, extra='fill-opacity="0.35"')
    f.path("M590,230 L590,196 Q600,178 610,196 L610,230", stroke=GLASS, w=3)
    f.path("M400,252 Q600,236 800,252", stroke=WHITE, w=5, extra='stroke-linecap="round" stroke-opacity="0.5"')
    # the plate inside, with a lead wire through the glass
    f.rect(420, 384, 360, 22, "url(#fy14pe-h-plate)", INK, 2.5, 3)
    f.path("M600,406 L600,470", stroke=METAL_EDGE, w=5)
    # stands of the tube
    for x in (420, 780):
        f.rect(x - 8, 430, 16, 40, IRON)
    # electrons leaving only where the violet light falls, each with a short trail
    for k, (x, y, dx, dy) in enumerate(((712, 352, -6, 26), (744, 318, 4, 30), (690, 300, -12, 30), (760, 270, 10, 28),
                                        (724, 262, -2, 32), (700, 350, 0, 22), (770, 340, 12, 22))):
        f.line(x - dx, y + dy, x, y, COLD_LIGHT, 3, cap="round")
        f.circle(x, y, 7, COLD, WHITE, 2)
    return f.svg()


def energy():
    """Energy diagram of one electron in sodium: hf = W + E_k,max (to scale, 70 units per eV)."""
    f = Fig("fy14pe-energy", 384, "Energy diagram to scale for sodium, work function 2.36 eV. Left: red light of wavelength 650 nm. "
            "The photon energy hf = 1.91 eV is drawn as an arrow from the electron in the metal; it ends below the dashed line "
            "of the energy needed to get out of the metal, so the electron stays. Right: violet light of 400 nm. The arrow "
            "hf = 3.10 eV reaches above the dashed line: the first 2.36 eV, the work function W, frees the electron, and the "
            "remaining 0.74 eV is the largest kinetic energy E_k,max the electron can have.")
    S, y0 = 70, 318                     # units per eV, the energy of the least tightly bound electron in the metal
    yv = y0 - W_NA * S                  # the level outside the metal
    f.line(300, 14, 300, 372, RULE, 2, "6 6")
    for p, lam, col in ((0, 650, HOT), (300, 400, VIOLET)):
        E = HC_NM / lam
        f.tex(p + 150, 26, rf"\lambda = {lam}\,\text{{nm}}", "middle")
        # the metal: a block whose top is the electron's energy
        f.rect(p + 14, y0, 112, 46, ALUMINIUM, INK, 2.5, 3)
        f.tex(p + 70, y0 + 23, r"\text{metal}", "middle")
        f.circle(p + 100, y0 - 1, 8, COLD, WHITE, 2)
        f.tex(p + 140, y0 + 23, rf"W = {W_NA:.2f}\,\text{{eV}}", "start", size=22)
        f.line(p + 14, yv, p + 288, yv, MUTED, 2, "8 6")
        # W bracket
        f.path(f"M{p + 46},{n(y0)} H{p + 38} V{n(yv)} H{p + 46}", stroke=INK, w=2.5)
        f.tex(p + 32, (y0 + yv) / 2, "W", "end")
        # photon energy arrow
        top = y0 - E * S
        f.block_arrow(p + 100, y0 - 10, p + 100, top, col, shaft=10, head=24, headlen=20)
        if E > W_NA:
            f.tex(p + 120, (y0 + yv) / 2 + 14, rf"hf = {E:.2f}\,\text{{eV}}", "start", size=22)
            f.path(f"M{p + 116},{n(yv)} H{p + 124} V{n(top)} H{p + 116}", stroke=INK, w=2.5)
            f.tex(p + 132, (yv + top) / 2 - 26, r"E_{\text{k,max}}", "start", size=22)
            f.tex(p + 132, (yv + top) / 2 + 2, rf"= {E - W_NA:.2f}\,\text{{eV}}", "start", size=22)
        else:
            f.tex(p + 120, (y0 + top) / 2 + 10, rf"hf = {E:.2f}\,\text{{eV}}", "start", size=22)
            f.tex(p + 120, top + 8, r"hf < W", "start", size=22)
    return f.svg()


def usf():
    """U_s against f for sodium and zinc, from the model U_s = (h/e) f − W/e: parallel lines with the slope h/e."""
    f = Fig("fy14pe-usf", 360, "Graph of model values, to scale: the stopping voltage U_s in volts against the frequency f in units "
            "of 10^14 Hz, from 0 to 14. Two straight, parallel lines: sodium starts on the frequency axis at its threshold "
            "frequency 5.71 · 10^14 Hz and zinc at 10.4 · 10^14 Hz. Five points on the sodium line are the wavelengths 500, 450, "
            "400, 350 and 300 nm. A triangle on the sodium line shows that the stopping voltage rises by 1.65 V when the frequency "
            "rises by 4 · 10^14 Hz; this slope is h/e and is the same for both metals.")
    ax = Axes(f, (84, 300), (424, 58), x=(0, 14), y=(0, 3.5), xticks=[2, 4, 6, 8, 10, 12, 14], yticks=[0.5, 1, 1.5, 2, 2.5, 3, 3.5],
              xlabel=r"f\ (10^{14}\,\text{Hz})", ylabel=r"U_\text{s}\ (\text{V})",
              yfmt=lambda v: fi(v) if float(v).is_integer() else "")
    us = lambda f14, W: H_EV * f14 * 1e14 - W
    f0na, f0zn = W_NA / H_EV / 1e14, W_ZN / H_EV / 1e14
    ax.line([(f0na, 0), (14, us(14, W_NA))], COLD, 3)
    ax.line([(f0zn, 0), (14, us(14, W_ZN))], HEAT, 3)
    for lam in (500, 450, 400, 350, 300):
        fr = 2.99792458e8 / (lam * 1e-9) / 1e14
        ax.point(fr, us(fr, W_NA), COLD)
    # slope triangle between 9 and 13 · 10^14 Hz
    a, b = 9.0, 13.0
    f.line(ax.X(a), ax.Y(us(a, W_NA)), ax.X(b), ax.Y(us(a, W_NA)), INK, 2)
    f.line(ax.X(b), ax.Y(us(a, W_NA)), ax.X(b), ax.Y(us(b, W_NA)), INK, 2)
    f.tex(ax.X(11), ax.Y(us(a, W_NA)) + 18, r"\Delta f", "middle", size=22)
    f.tex(ax.X(b) + 8, ax.Y((us(a, W_NA) + us(b, W_NA)) / 2), r"\Delta U_\text{s}", "start", size=22)
    f.tex(ax.X(1.2), ax.Y(3.25), r"\text{model values}", "start", color=MUTED, size=22, bg=True)
    f.tex(ax.X(11.4), ax.Y(3.3), r"\text{sodium}", "end", color=COLD, size=22, bg=True)
    f.tex(ax.X(13.9), ax.Y(0.55), r"\text{zinc}", "end", color=HEAT, size=22, bg=True)
    f.tex(ax.X(1.2), ax.Y(2.6), r"\text{slope} = \dfrac{h}{e}", "start", size=22, bg=True)
    return f.svg()


FIGURES = {"hero": hero, "energy": energy, "usf": usf}
