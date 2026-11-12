"""Figures of the unit fy14-fotoni (scripts/figlib.py, herolib.py); `python3 scripts/units.py figures fy14-fotoni`
writes them into content/en/units/fy14-fotoni/unit.md. The unit is written in English, so the decimal sign is a point.

The example photocell data are invented (the unit says so) and are fitted here with numpy-free least squares; the e/m
diagram is a sketch of the geometry, not to scale. Colours follow the writing guide: velocity blue, force red, the
magnetic field green with ⊙ for a field out of the page."""
import figlib
from figlib import (Fig, Axes, fi, INK, MUTED, WHITE, RULE, GLASS, ALUMINIUM, METAL_EDGE, IRON, COPPER, COLD, COLD_LIGHT,
                    HOT, HOT_LIGHT, HEAT, HEAT_LIGHT, SAND, GOOD, n)
import herolib as H

figlib.set_language({}, ".")

BEAM = "#3bc9db"                      # the glow of the electron beam in the e/m tube (not a quantity colour)
VIOLET = "#7048e8"

# invented example data of the worked example (unit.md "Worked example"): frequency in 10^14 Hz, stopping voltage in V
F14 = [4.80, 5.08, 5.71, 6.38, 7.40]
US = [0.55, 0.69, 0.93, 1.17, 1.60]


def fit(xs, ys):
    """Least-squares slope and intercept."""
    m = len(xs); sx, sy = sum(xs), sum(ys)
    sxx = sum(x * x for x in xs); sxy = sum(x * y for x, y in zip(xs, ys))
    k = (m * sxy - sx * sy) / (m * sxx - sx * sx)
    return k, (sy - k * sx) / m


def hero():
    """Opening illustration: a laboratory bench with three stations (a photocell with coloured LEDs, a glowing
    electron beam between two coils, a lamp whose light a grating splits into lines) and two faceless students."""
    f = H.hero("fy14fo-hero", "Illustration: a dim university teaching laboratory. On a long bench stand three experiments. "
               "On the left, a small black box with a vacuum tube and a row of coloured LEDs, red, yellow, green, blue and violet, "
               "connected to a meter. In the middle, a round glass bulb stands between two large copper coils, and a thin "
               "glowing beam inside the bulb bends into a closed circle. On the right, a glowing gas tube shines through a "
               "grating, and four coloured lines appear on a small white screen. Two students without faces stand behind "
               "the bench, one looking at the coils and one writing on a clipboard.")
    room = H.grad(f, "fy14fo-h-room", "#2d3a46", INK)
    f.rect(0, 0, 1200, 600, room)
    f.line(0, 140, 1200, 140, "#3a4754", 3)
    # two students behind the bench (the bench hides their legs)
    H.person(f, 470, 720, shirt=HEAT, sc=1.35)
    H.person(f, 860, 720, shirt=COLD, sc=1.35)
    f.rect(790, 330, 76, 96, WHITE, MUTED, 2, 4)                # a clipboard in front of the right student
    for k in range(4):
        f.line(802, 352 + 18 * k, 854, 352 + 18 * k, RULE, 3)
    bench = H.grad(f, "fy14fo-h-bench", SAND, "#a97a35")
    f.rect(0, 430, 1200, 170, bench)
    f.line(0, 430, 1200, 430, "#e9c98a", 4)
    # left station: photocell box, vacuum tube, LEDs, meter
    f.rect(70, 330, 230, 100, "#343a40", INK, 3, 8)
    f.add(f'<rect x="120" y="250" width="110" height="80" rx="40" fill="{GLASS}" fill-opacity="0.3" stroke="{GLASS}" stroke-width="3"/>')
    f.rect(140, 272, 16, 46, ALUMINIUM, INK, 2, 2)
    f.rect(196, 272, 8, 46, METAL_EDGE)
    for k, col in enumerate((HOT, "#fab005", GOOD, COLD, VIOLET)):
        x = 96 + 40 * k
        f.add(f'<circle cx="{x}" cy="402" r="20" fill="{col}" fill-opacity="0.25"/>')
        f.circle(x, 402, 10, col, WHITE, 2)
    f.rect(320, 350, 90, 80, IRON, INK, 3, 6)
    f.rect(332, 362, 66, 34, "#e6fcf5", INK, 2, 3)
    f.line(345, 388, 380, 368, INK, 3)
    f.circle(365, 412, 6, INK)
    # middle station: two coils with the glass bulb and the glowing circle
    cx, cy = 640, 300
    f.add(f'<circle cx="{cx}" cy="{cy}" r="118" fill="none" stroke="{COPPER}" stroke-width="22"/>')
    f.add(f'<circle cx="{cx}" cy="{cy}" r="118" fill="none" stroke="#e8a272" stroke-width="4" stroke-opacity="0.7"/>')
    f.add(f'<circle cx="{cx}" cy="{cy}" r="88" fill="{GLASS}" fill-opacity="0.18" stroke="{GLASS}" stroke-width="3"/>')
    f.add(f'<circle cx="{cx}" cy="{cy + 12}" r="46" fill="none" stroke="{BEAM}" stroke-width="12" stroke-opacity="0.25"/>')
    f.add(f'<circle cx="{cx}" cy="{cy + 12}" r="46" fill="none" stroke="{BEAM}" stroke-width="4"/>')
    f.rect(cx - 8, cy + 58, 16, 22, METAL_EDGE)                 # the electron gun at the bottom of the bulb
    f.rect(cx - 70, 418, 140, 14, IRON, INK, 2, 4)
    f.rect(cx - 10, 410, 20, 12, IRON)
    # right station: gas tube, grating and screen with four lines
    f.rect(930, 220, 22, 200, "#cc5de8", None, 0, 11, extra='fill-opacity="0.85"')
    f.add('<rect x="922" y="212" width="38" height="216" rx="19" fill="#cc5de8" fill-opacity="0.18"/>')
    f.rect(920, 410, 42, 22, IRON, INK, 2, 3)
    f.path("M960,300 L1040,268 L1040,332 Z", "#e5dbff", extra='fill-opacity="0.35"')
    f.rect(1036, 262, 10, 76, METAL_EDGE, INK, 1.5, 2)
    f.rect(1080, 230, 90, 140, WHITE, MUTED, 2, 4)
    for x, col in ((1098, VIOLET), (1106, "#4263eb"), (1128, "#15aabf"), (1158, HOT)):
        f.rect(x - 2, 244, 5, 112, col)
    f.rect(1118, 370, 14, 62, METAL_EDGE)
    return f.svg()


def emtube():
    """The e/m tube seen along the axis of the coils: B out of the page, the beam on a circle, v and F. Redrawn on a
    600-wide canvas at the same displayed size (teacher 2026-11-11, illustration audit: the labels were twice the size
    of the series' others, 28 units in a 420-wide figure); every length is the old one times K, the labels 24."""
    K = 600 / 420
    f = Fig("fy14fo-em", 543, "Sketch, not to scale: the glass bulb of the e/m tube seen along the axis of the two coils. "
            "The magnetic field points out of the page, shown by green circles with a dot and labelled B. An electron leaves "
            "the electron gun at the bottom moving to the right and travels on a circle of radius r. At one point of the "
            "circle a blue arrow shows its velocity v along the circle and a red arrow shows the magnetic force F, which "
            "points to the centre of the circle.", width=600, size=24)
    cx, cy, R, r = 210 * K, 195 * K, 172 * K, 98 * K
    f.add(f'<circle cx="{n(cx)}" cy="{n(cy)}" r="{n(R)}" fill="{GLASS}" fill-opacity="0.5" stroke="{METAL_EDGE}" stroke-width="3"/>')
    for x, y in ((92, 108), (290, 62), (80, 230), (150, 50), (330, 290), (100, 312)):
        f.add(f'<circle cx="{n(x * K)}" cy="{n(y * K)}" r="15" fill="{WHITE}" stroke="{GOOD}" stroke-width="3"/>')
        f.circle(x * K, y * K, 5, GOOD)
    f.tex(290 * K - 24, 62 * K, r"\overline{B}", "end", color=GOOD)
    # the beam: a circle that starts at the gun's exit at the bottom
    oy = cy + 88 * K                              # the lowest point of the orbit, where the beam leaves the gun
    ocx, ocy = cx, oy - r
    f.add(f'<circle cx="{n(ocx)}" cy="{n(ocy)}" r="{n(r)}" fill="none" stroke="{BEAM}" stroke-width="12" stroke-opacity="0.3"/>')
    f.add(f'<circle cx="{n(ocx)}" cy="{n(ocy)}" r="{n(r)}" fill="none" stroke="{BEAM}" stroke-width="4"/>')
    f.rect(cx - 44 * K, oy - 9 * K, 40 * K, 18 * K, IRON, INK, 2, 3)        # the gun, firing to the right
    f.tex(cx - 24 * K, oy + 44, r"\text{gun}", "middle")
    # radius
    f.circle(ocx, ocy, 5, INK)
    f.line(ocx, ocy, ocx - r, ocy, INK, 2, "7 5")
    f.tex(ocx - r / 2, ocy - 26, "r", "middle")
    # velocity and force at the rightmost point of the orbit
    px, py = ocx + r, ocy
    f.circle(px, py, 8, COLD, WHITE, 2)
    f.arrow(px, py, px, py - 80 * K, COLD, 4, 18)
    f.tex(px + 14, py - 66 * K, r"\overline{v}", "start", color=COLD)
    f.arrow(px, py, px - 66 * K, py, HOT, 4, 18)
    f.tex(px - 36 * K, py + 34, r"\overline{F}", "middle", color=HOT)
    return f.svg()

def fitgraph():
    """The invented example data with the least-squares line, as in the worked example."""
    k, b = fit(F14, US)
    f = Fig("fy14fo-fit", 380, f"Graph of invented example data: the stopping voltage U_s in volts against the frequency f "
            f"in units of 10^14 Hz, from 4 to 8. Five points rise almost on a straight line, from 0.55 V at 4.80 to 1.60 V at "
            f"7.40. A fitted straight line runs through them; the label gives its slope, 3.96 · 10^-15 V · s. "
            f"The line is labelled fit.", width=560, size=28)
    ax = Axes(f, (90, 318), (350, 52), x=(4, 8), y=(0, 2.5), xticks=[4, 5, 6, 7, 8], yticks=[0.5, 1, 1.5, 2, 2.5],
              xlabel=r"f\ (10^{14}\,\text{Hz})", ylabel=r"U_\text{s}\ (\text{V})", origin_label=False,
              xfmt=lambda v: fi(v), yfmt=lambda v: fi(v))
    ax.line([(4.2, k * 4.2 + b), (7.9, k * 7.9 + b)], COLD, 3)
    for x, y in zip(F14, US):
        ax.point(x, y, INK)
    f.tex(ax.X(4.1), ax.Y(2.45), r"\text{example data}", "start", color=MUTED, bg=True)
    f.tex(ax.X(4.1), ax.Y(2.06), rf"\text{{fit: slope}} = {k * 1e-14 * 1e15:.2f} \cdot 10^{{-15}}\,\text{{V}} \cdot \text{{s}}", "start", color=COLD, bg=True)
    return f.svg()


FIGURES = {"hero": hero, "em": emtube, "fit": fitgraph}

if __name__ == "__main__":
    k, b = fit(F14, US)
    print("slope V s", k * 1e-14, "intercept V", b, "h", k * 1e-14 * 1.602176634e-19)
