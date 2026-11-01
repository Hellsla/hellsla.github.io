"""Figures of the unit fy14-classical-limits (scripts/figlib.py, herolib.py); `python3 scripts/units.py figures
fy14-classical-limits` writes them into content/en/units/fy14-classical-limits/unit.md. English: decimal point.
Every curve is computed here from Planck's law and the Rayleigh–Jeans law with the exact SI constants h, c and k_B."""
import math
import figlib
from figlib import (Fig, Axes, fi, INK, MUTED, WHITE, RULE, RULE_LIGHT, GLASS, ICE, SAND, SAND_LIGHT, SAND_DARK, ALUMINIUM,
                    METAL_EDGE, IRON, COLD, COLD_LIGHT, HOT, HOT_LIGHT, HEAT, HEAT_LIGHT, GOOD, n)
import herolib as H

figlib.set_language({}, ".")

h, c, kB = 6.62607015e-34, 2.99792458e8, 1.380649e-23
VIOLET = "#7048e8"


def planck(lam_nm, T):
    """Spectral radiance B_lambda (W / (m^2 sr m)) of a black body."""
    l = lam_nm * 1e-9
    return 2 * h * c ** 2 / l ** 5 / math.expm1(h * c / (l * kB * T))


def rayleigh_jeans(lam_nm, T):
    l = lam_nm * 1e-9
    return 2 * c * kB * T / l ** 4


def hero():
    """The Why question: classical physics in 1900 as a calm, finished building under two dark clouds (Kelvin's 1900
    lecture), and in front of it an ordinary glowing furnace. No text."""
    f = H.hero("fy14cl-hero", "Illustration: a calm blue sky over a white stone building with a wide staircase, columns and a "
               "triangular roof, like a temple of science. The sky is clear except for two heavy dark clouds that drift in over "
               "the roof. In front of the building, on the paved square, stands a small brick furnace with its door open; "
               "inside, coals glow orange and a metal bar lies in the glow.")
    H.sky(f, "cl", 600, "#bcdcf5", GLASS)
    H.sun(f, "cl", 110, 92, 44)
    H.cloud(f, 1000, 70, 0.5)
    # two dark clouds approaching the roof
    for cx, cy, sc in ((470, 92, 1.35), (790, 120, 1.15)):
        H.cloud(f, cx + 8, cy + 10, sc, fill="#3f4a56", extra='fill-opacity="0.35"')
        H.cloud(f, cx, cy, sc, fill="#56616d")
        H.cloud(f, cx - 10, cy - 6, sc * 0.7, fill="#6c7782")
    # the classical building: steps, columns, entablature, pediment
    stone, shade = "#f1ede3", "#d8d0bd"
    f.rect(300, 470, 600, 26, shade, INK, 2.5)
    f.rect(320, 446, 560, 26, stone, INK, 2.5)
    f.rect(340, 422, 520, 26, shade, INK, 2.5)
    for k in range(7):
        x = 370 + k * 76
        f.rect(x, 262, 40, 160, stone, INK, 2.5)
        for j in (1, 2):
            f.line(x + 13 * j, 268, x + 13 * j, 416, shade, 2)
        f.rect(x - 6, 250, 52, 14, shade, INK, 2)
        f.rect(x - 6, 410, 52, 12, shade, INK, 2)
    f.rect(340, 214, 520, 38, stone, INK, 2.5)
    f.line(340, 232, 860, 232, shade, 2)
    f.path("M330,214 L600,140 L870,214 Z", stone, INK, 2.5)
    f.path("M372,204 L600,152 L828,204 Z", shade)
    # the square
    f.rect(0, 496, 1200, 104, H.grad(f, "cl-square", SAND_LIGHT, SAND_DARK))
    for k in range(9):
        f.line(-60 + 160 * k, 496, -200 + 190 * k, 600, SAND, 2)
    # the furnace: brick body, open door, glowing coals and a bar
    brick, mortar = "#a8553a", "#7a3b28"
    f.rect(930, 360, 220, 176, brick, INK, 3, 6)
    for row in range(6):
        y = 372 + row * 28
        f.line(930, y, 1150, y, mortar, 2)
        off = 0 if row % 2 else 26
        for x in range(930 + off, 1150, 52):
            f.line(x, y, x, y + 28 if y + 28 < 536 else 536, mortar, 2)
    f.rect(952, 330, 176, 34, "#8d4630", INK, 3, 4)
    f.rect(1080, 250, 34, 84, "#8d4630", INK, 3)
    H.smoke(f, 1097, 230, 0.7)
    f.add('<defs><radialGradient id="cl-glow" cx="0.5" cy="0.6" r="0.6"><stop offset="0" stop-color="#ffe8a3"/><stop offset="0.5" stop-color="#ffa94d"/><stop offset="1" stop-color="#e8590c"/></radialGradient></defs>')
    f.rect(970, 412, 140, 96, "url(#cl-glow)", INK, 3, 10)
    for k in range(9):
        f.circle(984 + k * 15, 492 - 6 * (k % 2), 9, "#ff922b", "#c92a2a", 1.5)
    f.rect(960, 456, 170, 12, "#ffb15e", INK, 2, 3)
    f.add('<circle cx="1040" cy="460" r="120" fill="#ffa94d" fill-opacity="0.18"/>')
    # the open door, swung to the left
    f.path("M970,412 L928,398 L928,522 L970,508 Z", IRON, INK, 2.5)
    return f.svg()


def spectrum():
    """The electromagnetic spectrum on a logarithmic wavelength scale, with the visible band spread out below."""
    f = Fig("fy14cl-spectrum", 330, "The electromagnetic spectrum on a logarithmic scale of wavelength, from 10 to the power minus 12 "
            "metres on the left to 10 to the power 2 metres on the right. Regions from left to right: gamma rays, X-rays, "
            "ultraviolet, visible light, infrared, microwaves and radio waves. The narrow visible band, from about 380 to "
            "750 nanometres, is drawn enlarged below as a rainbow from violet to red. An arrow pointing left says: shorter "
            "wavelength, higher frequency.")
    x0, x1, e0, e1 = 40, 560, -12, 2
    X = lambda e: x0 + (e - e0) / (e1 - e0) * (x1 - x0)
    regions = [(-12, -11, "#868e96", r"\gamma"), (-11, -8, "#adb5bd", r"\text{X-rays}"), (-8, -6.42, "#b197fc", r"\text{UV}"),
               (-6.42, -6.12, None, ""), (-6.12, -3, "#ffa8a8", r"\text{IR}"), (-3, 0, "#ffd8a8", "MW"),
               (0, 2, "#d3f9d8", r"\text{radio}")]
    for a, b, col, lab in regions:
        if col: f.rect(X(a), 70, X(b) - X(a), 56, col, INK, 1.5)
        if lab == "MW":
            f.tex((X(a) + X(b)) / 2, 84, r"\text{micro-}", "middle", size=22)
            f.tex((X(a) + X(b)) / 2, 112, r"\text{waves}", "middle", size=22)
        elif lab: f.tex((X(a) + X(b)) / 2, 98, lab, "middle")
    # the visible band on the bar
    f.defs_add('<linearGradient id="fy14cl-vis" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#7048e8"/><stop offset="0.2" stop-color="#1971c2"/>'
               '<stop offset="0.4" stop-color="#2b8a3e"/><stop offset="0.6" stop-color="#fab005"/><stop offset="0.8" stop-color="#e8590c"/><stop offset="1" stop-color="#c92a2a"/></linearGradient>')
    f.rect(X(-6.42), 70, X(-6.12) - X(-6.42), 56, "url(#fy14cl-vis)", INK, 1.5)
    for e in range(-12, 3, 2):
        f.line(X(e), 126, X(e), 136, INK, 2)
        f.tex(X(e), 156, rf"10^{{{e}}}", "middle")
    f.tex(x1 + 2, 192, r"\lambda\ (\text{m})", "end")
    f.arrow(300, 30, 60, 30, INK, 2.5, 13)
    f.tex(310, 30, r"\text{shorter } \lambda\text{, higher } f", "start")
    # the enlarged visible band
    f.line(X(-6.42), 174, 120, 230, MUTED, 1.5, "5 4")
    f.line(X(-6.12), 174, 480, 230, MUTED, 1.5, "5 4")
    f.rect(120, 230, 360, 40, "url(#fy14cl-vis)", INK, 2)
    f.tex(120, 296, r"380\ \text{nm}", "middle")
    f.tex(480, 296, r"750\ \text{nm}", "middle")
    f.tex(300, 296, r"\text{visible light}", "middle")
    return f.svg()


def curves():
    """Planck's law at 4000, 5000 and 6000 K, relative to the 6000 K peak, with the peaks marked."""
    f = Fig("fy14cl-curves", 400, "Graph of model values from Planck's law, to scale. The horizontal axis is the wavelength from 0 to "
            "2000 nanometres; the vertical axis is the radiated power per wavelength, relative to the highest point of the 6000 K "
            "curve. The visible band from 380 to 750 nanometres is shaded. Three curves, each rising steeply from zero, "
            "reaching one peak and falling slowly: 6000 K is the highest curve with its peak at 483 nanometres; 5000 K is lower "
            "with its peak at 580 nanometres; 4000 K is the lowest with its peak at 724 nanometres. A dashed vertical line "
            "marks each peak.")
    ax = Axes(f, (84, 330), (470, 60), x=(0, 2000), y=(0, 1.1), xticks=[500, 1000, 1500, 2000], yticks=[0.25, 0.5, 0.75, 1.0],
              xlabel=r"\lambda\ (\text{nm})", ylabel=r"\text{relative power}", yfmt=lambda v: f"{v:g}")
    f.rect(ax.X(380), ax.Y(1.1), ax.X(750) - ax.X(380), ax.Y(0) - ax.Y(1.1), "#e7f0ff", extra='fill-opacity="0.8"')
    f.tex((ax.X(380) + ax.X(750)) / 2, ax.Y(1.06), r"\text{visible}", "middle", color=MUTED)
    top = planck(2.897771955e-3 / 6000 * 1e9, 6000)
    for T, col, lx, ly in ((6000, COLD, 790, 0.97), (5000, GOOD, 940, 0.42), (4000, HOT, 600, 0.175)):
        ax.curve(lambda l: planck(max(l, 60), T) / top, 100, 2000, col, 3)
        lp = 2.897771955e-3 / T * 1e9
        yp = planck(lp, T) / top
        f.line(ax.X(lp), ax.Y(yp), ax.X(lp), ax.Y(0), col, 1.8, "6 5")
        ax.point(lp, yp, col)
        if T == 4000:     # in the gap between the 5000 K curve and the 4000 K peak, without a white box over the curves
            f.tex(ax.X(lx), ax.Y(ly), rf"{T}\ \text{{K}}", "start", color=col, size=22)
        else:
            f.tex(ax.X(lx) + 12, ax.Y(ly), rf"{T}\ \text{{K}}", "start", color=col, bg=True)
    f.tex(ax.X(1450), ax.Y(0.85), r"\text{model values}", "middle", color=MUTED, bg=True)
    return f.svg()


def catastrophe():
    """Planck's law (agrees with measurements) and the classical Rayleigh–Jeans law at 5000 K."""
    f = Fig("fy14cl-catastrophe", 400, "Graph to scale at a temperature of 5000 K. Horizontal axis: wavelength from 0 to 3000 nanometres. "
            "Vertical axis: radiated power per wavelength, relative to the peak of the measured curve. The blue curve, Planck's "
            "law, which agrees with measurements, rises to a peak near 580 nanometres and falls to zero at short wavelengths. "
            "The red dashed curve, the classical prediction of Rayleigh and Jeans, agrees with the blue curve only at long "
            "wavelengths; towards short wavelengths it rises ever more steeply and leaves the top of the graph, with an arrow "
            "pointing up: it would grow without limit.")
    ax = Axes(f, (84, 330), (470, 60), x=(0, 3000), y=(0, 2.0), xticks=[1000, 2000, 3000], yticks=[0.5, 1.0, 1.5, 2.0],
              xlabel=r"\lambda\ (\text{nm})", ylabel=r"\text{relative power}", yfmt=lambda v: f"{v:g}")
    T = 5000
    top = planck(2.897771955e-3 / T * 1e9, T)
    lmin = (2 * c * kB * T / (2.0 * top)) ** 0.25 * 1e9          # where Rayleigh–Jeans leaves the graph
    ax.curve(lambda l: rayleigh_jeans(l, T) / top, lmin, 3000, HOT, 3.5, dash="10 7")
    ax.curve(lambda l: planck(max(l, 60), T) / top, 100, 3000, COLD, 3.5)
    f.arrow(ax.X(lmin), ax.Y(2.0) + 6, ax.X(lmin), ax.Y(2.0) - 34, HOT, 3, 14)
    f.tex(ax.X(lmin) + 18, ax.Y(1.9), r"\text{classical prediction}", "start", color=HOT, bg=True)
    f.tex(ax.X(1700), ax.Y(0.95), r"\text{measured (Planck's law)}", "start", color=COLD, bg=True)
    return f.svg()


FIGURES = {"hero": hero, "spectrum": spectrum, "curves": curves, "catastrophe": catastrophe}
