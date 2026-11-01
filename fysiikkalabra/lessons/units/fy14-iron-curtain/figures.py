"""Figures of the unit fy14-iron-curtain (scripts/figlib.py, herolib.py); `python3 scripts/units.py figures
fy14-iron-curtain` writes them into content/en/units/fy14-iron-curtain/unit.md. English: decimal point.
The hero has no text and shows neither the visit nor the laser (prediction 1 asks how the question was settled).
The Thomson figure sits in the theory section after prediction 2 and is drawn from the Doppler width: a Gaussian of
relative width proportional to the square root of the temperature (1 keV and 0.25 keV, so the widths differ by 2)."""
import math
import figlib
from figlib import (Fig, INK, MUTED, WHITE, RULE, RULE_LIGHT, GLASS, ALUMINIUM, METAL_EDGE, IRON, COPPER, COLD,
                    HOT, HEAT, HEAT_LIGHT, SAND, SAND_LIGHT, GOOD, n)
import herolib as H

figlib.set_language({}, ".")
RUBY = "#c92a2a"


def hero():
    """A tokamak hall in winter: an early tokamak (a ring with coils on a large iron transformer core) under tall windows
    with falling snow; a table with two teacups in the foreground."""
    f = H.hero("fy14ic-hero", "Illustration: a large, dim laboratory hall in winter. Through three tall arched windows snow "
               "falls on a dark blue evening. In the middle of the hall stands an early tokamak: a ring-shaped metal chamber "
               "wrapped in copper coils, held by a massive dark iron core that passes through the ring. Cables run from it "
               "across the floor. In the front right corner stands a small wooden table with two teacups and a teapot.")
    f.rect(0, 0, 1200, 600, H.grad(f, "ic-wall", "#3d4b57", "#26313a"))
    # tall arched windows with snow
    for x in (120, 520, 920):
        f.path(f"M{x},300 V110 Q{x + 80},30 {x + 160},110 V300 Z", H.grad(f, f"ic-win{x}", "#1c3557", "#3a5f8f"), METAL_EDGE, 4)
        f.line(x + 80, 50, x + 80, 300, METAL_EDGE, 4)
        f.line(x, 200, x + 160, 200, METAL_EDGE, 4)
        for k in range(26):
            sx, sy = x + 8 + H.rnd(k, x) * 144, 70 + H.rnd(k + 50, x) * 225
            if sy > 110 or abs(sx - x - 80) < 80 - (110 - sy) * 0.9:
                f.circle(sx, sy, round(1.6 + 1.8 * H.rnd(k + 90, x), 1), WHITE)
    # floor
    f.rect(0, 430, 1200, 170, H.grad(f, "ic-floor", "#56606b", "#3a424b"))
    for x in range(-200, 1400, 140):
        f.line(x, 430, x - 160, 600, "#4a535d", 2)
    # the iron core: a big rectangular frame, the ring passes around its central leg
    f.rect(420, 150, 360, 40, IRON, INK, 3)
    f.rect(420, 150, 40, 320, IRON, INK, 3)
    f.rect(740, 150, 40, 320, IRON, INK, 3)
    f.rect(420, 430, 360, 40, IRON, INK, 3)
    # the torus behind and in front of the central leg
    f.add(f'<ellipse cx="600" cy="320" rx="230" ry="78" fill="none" stroke="{METAL_EDGE}" stroke-width="46"/>')
    f.rect(580, 150, 40, 320, IRON, INK, 3)             # central leg in front of the back half
    f.add(f'<path d="M370,320 A230,78 0 0,1 830,320" fill="none" stroke="{ALUMINIUM}" stroke-width="46"/>')
    for k in range(14):                                  # copper coils around the ring
        a = math.pi * 2 * k / 14 + 0.1
        x, y = 600 + 230 * math.cos(a), 320 + 78 * math.sin(a)
        if math.sin(a) > -0.2:
            f.rect(x - 8, y - 32, 16, 64, COPPER, INK, 2, 3)
    # cables to the right
    f.path("M800,450 C900,470 960,520 1200,520", stroke=INK, w=8)
    f.path("M800,462 C890,500 940,560 1200,566", stroke="#1a2026", w=8)
    # the tea table
    f.rect(930, 470, 220, 18, H.grad(f, "ic-wood", SAND, "#a97a35"), INK, 2, 3)
    f.rect(946, 488, 12, 100, "#8a5f2a"); f.rect(1122, 488, 12, 100, "#8a5f2a")
    for x in (975, 1055):
        f.path(f"M{x},446 h40 l-5,24 h-30 Z", WHITE, INK, 2)
        f.path(f"M{x + 40},452 q14,2 0,12", stroke=INK, w=2.5)
    f.path("M1100,430 q22,0 26,20 q2,20 -26,20 q-28,0 -26,-20 q4,-20 26,-20 Z", "#f2a69c", INK, 2)
    f.path("M1126,446 l16,-10", stroke=INK, w=3)
    f.path("M988,436 q-6,-14 4,-24 M1068,436 q-6,-14 4,-24", stroke=WHITE, w=2.5, extra='stroke-opacity="0.7"')
    return f.svg()


def thomson():
    """Top: the measurement (laser beam through the plasma, light scattered sideways into a spectrometer).
    Bottom: the scattered spectra for a cooler and a hotter plasma, same area, widths in the ratio sqrt(4) = 2."""
    f = Fig("fy14ic-thomson", 720, "Diagram of Thomson scattering. Top: a red laser beam enters from the left and crosses a grey "
            "cross-section of the plasma. In the plasma, small blue dots are electrons moving in random directions. A little "
            "light is scattered upwards, at a right angle, into a box labelled spectrometer. Bottom: a graph of the intensity "
            "of the scattered light against wavelength, with both curves centred on the laser wavelength 694 nanometres. The "
            "cooler plasma gives a tall, narrow curve; the hotter plasma gives a low, wide curve, twice as wide.",
            width=600, size=28)
    f.rect(0, 0, 600, 720, WHITE)
    # --- the measurement
    f.add(f'<ellipse cx="300" cy="230" rx="150" ry="110" fill="{RULE_LIGHT}" stroke="{METAL_EDGE}" stroke-width="3"/>')
    f.line(10, 230, 590, 230, RUBY, 10)
    f.tex(14, 196, r"\text{laser}", color=RUBY, size=28)
    for k in range(16):
        x, y = 300 + (H.rnd(k, 5) - 0.5) * 220, 230 + (H.rnd(k + 40, 5) - 0.5) * 150
        a = H.rnd(k + 80, 5) * 2 * math.pi
        f.circle(x, y, 5, COLD)
        f.arrow(x, y, x + 26 * math.cos(a), y + 26 * math.sin(a), COLD, 2, 8)
    f.path("M300,222 L300,96", stroke=RUBY, w=4, extra='stroke-dasharray="10 7"')
    f.path("M300,92 l-9,16 h18 Z", RUBY)
    f.rect(200, 26, 200, 56, IRON, INK, 3, 6)
    f.tex(300, 54, r"\text{spectrometer}", "middle", color=WHITE, size=26, w=196)
    f.tex(460, 330, r"\text{plasma}", "middle", color=MUTED, size=28, w=140)
    # --- the spectra
    x0, x1, yb, yt = 70, 570, 680, 420
    f.line(x0, yb, x1, yb, INK, 2.5); f.line(x0, yb, x0, yt, INK, 2.5)
    f.path(f"M{x1},{yb} l-14,-7 v14 Z", INK); f.path(f"M{x0},{yt} l-7,14 h14 Z", INK)
    xc = (x0 + x1) / 2
    f.line(xc, yb, xc, yb + 8, INK, 2.5)
    f.tex(xc, yb + 26, r"694\ \text{nm}", "middle", size=26, w=140)
    f.tex(x1, yb - 22, r"\lambda", "end", size=30)
    f.tex(x0 + 12, yt + 4, r"\text{intensity}", size=26)
    for sig, col, dash, lab, lx, ly in ((34, COLD, None, r"\text{cooler}", xc + 52, yt + 46), (68, HEAT, "12 8", r"\text{hotter}", xc + 128, yb - 112)):
        hgt = 210 * 34 / sig
        pts = [(xc + t, yb - hgt * math.exp(-t * t / (2 * sig * sig))) for t in range(-230, 231, 5)]
        d = "M" + " L".join(f"{n(x)},{n(y)}" for x, y in pts)
        f.path(d, stroke=col, w=4, extra=(f'stroke-dasharray="{dash}"' if dash else ""))
        f.tex(lx, ly, lab, color=col, size=28)
    return f.svg()


FIGURES = {"hero": hero, "thomson": thomson}
