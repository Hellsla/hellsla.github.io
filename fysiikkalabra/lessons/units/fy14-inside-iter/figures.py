"""Figures of the unit fy14-inside-iter (scripts/figlib.py, herolib.py); `python3 scripts/units.py figures
fy14-inside-iter` writes them into content/en/units/fy14-inside-iter/unit.md. English: the decimal sign is a point.
The power figure is to scale: ITER's planned 50 MW of heating and 500 MW of fusion power (iter.org, What will ITER
do?), split by the D–T energies 3.5 MeV : 14.1 MeV of 17.6 MeV (computed from the NIST atomic masses: 3.54 and 14.05 MeV), and
the more than 300 MW of electrical power the plant draws to deliver the heating (Wikipedia, ITER)."""
import math
import figlib
from figlib import (Fig, INK, MUTED, WHITE, RULE, RULE_LIGHT, GLASS, ALUMINIUM, METAL_EDGE, IRON, COLD, COLD_LIGHT,
                    HOT, HOT_LIGHT, HEAT, HEAT_LIGHT, SAND, SAND_LIGHT, GOOD, GOOD_LIGHT, COPPER, n)
import herolib as H

figlib.set_language({}, ".")

PLASMA, PLASMA_LIGHT = "#e64980", "#fcc2d7"
ALPHA_SHARE = 3.5 / 17.6


def d_shape(cx, cy, a, k, delta, steps=90, side=1):
    """A D-shaped outline (Miller form) centred at (cx, cy): minor radius a, elongation k, triangularity delta;
    side = -1 mirrors it for the left half of the machine."""
    pts = []
    for i in range(steps):
        t = 2 * math.pi * i / steps
        x = cx + side * a * math.cos(t + delta * math.sin(t)); y = cy - k * a * math.sin(t)
        pts.append(f"{n(x)},{n(y)}")
    return "M" + " L".join(pts) + " Z"


def hero():
    """Opening illustration: a cut-away of a tokamak like ITER inside its cryostat, in a dark hall: the central
    solenoid stack in the middle, D-shaped coils on both sides, the double-walled vessel, a glowing pink plasma ring
    in each half, and a cold blue haze around the coils. No text."""
    f = H.hero("fy14ii-hero", "Illustration: a cut-away view of a huge doughnut-shaped machine in a dark hall. In the middle "
               "stands a tall stack of coils. On both sides, large D-shaped magnet coils surround a steel chamber with a "
               "double wall. Inside each half of the chamber a pink, glowing ring of plasma floats without touching the walls. "
               "A pale blue haze around the coils shows that they are extremely cold, while the plasma glows hot. A huge "
               "steel vessel with a domed lid encloses everything.")
    f.defs_add(f'<linearGradient id="fy14ii-h-bg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2d3a46"/><stop offset="1" stop-color="{INK}"/></linearGradient>')
    f.rect(0, 0, 1200, 600, "url(#fy14ii-h-bg)")
    glow = H.glow(f, "fy14ii-h-glow", "#fff0f6", PLASMA)
    cold = H.glow(f, "fy14ii-h-cold", "#e7f5ff", "#74c0fc")
    steel = H.steel(f, "fy14ii-h-steel")
    # floor
    f.rect(0, 540, 1200, 60, "#3a4754")
    # cryostat: walls and dome
    f.path("M140,540 L140,170 Q600,30 1060,170 L1060,540 Z", "#46525f", METAL_EDGE, 5)
    f.path("M164,540 L164,184 Q600,56 1036,184 L1036,540 Z", "#26323d")
    # cold haze around the coils
    for cx in (380, 820):
        f.add(f'<ellipse cx="{cx}" cy="320" rx="230" ry="210" fill="{cold}" fill-opacity="0.35"/>')
    # central solenoid: a stack of six modules
    for k in range(6):
        f.rect(572, 150 + k * 52, 56, 48, steel, INK, 2.5, 3)
        f.line(577, 174 + k * 52, 623, 174 + k * 52, COPPER, 3)
    for side in (-1, 1):
        c = 600 + side * 222
        # toroidal field coil: a thick D, its straight side towards the axis
        f.path(d_shape(c, 320, 160, 1.12, 0.45, side=side), "none", "#6c7a89", 30)
        f.path(d_shape(c, 320, 160, 1.12, 0.45, side=side), "none", "#9aa7b4", 9)
        # vacuum vessel (double wall) and blanket
        f.path(d_shape(c + side * 8, 326, 112, 1.3, 0.42, side=side), "#3b4a59", ALUMINIUM, 8)
        f.path(d_shape(c + side * 8, 326, 96, 1.3, 0.42, side=side), "#1c252e", "#c9a26b", 9)
        # plasma
        f.path(d_shape(c + side * 12, 318, 66, 1.5, 0.4, side=side), glow)
        f.path(d_shape(c + side * 12, 318, 40, 1.5, 0.4, side=side), "#fff0f6", extra='fill-opacity="0.55"')
        # divertor at the bottom of the vessel
        x = c + side * 4
        f.path(f"M{n(x - 40)},{n(446)} L{n(x - 18)},{n(424)} L{n(x)},{n(440)} L{n(x + 18)},{n(424)} L{n(x + 40)},{n(446)} Z", "#868e96", INK, 2)
    # poloidal field coils: small boxes outside the D coils
    for x, y in ((300, 120), (900, 120), (185, 320), (1015, 320), (300, 520), (900, 520)):
        f.rect(x - 22, y - 15, 44, 30, "#4dabf7", INK, 2.5, 4)
    # supports on the floor
    for x in (420, 780):
        f.rect(x - 30, 520, 60, 20, IRON, INK, 2)
    return f.svg()


def power():
    """Power bars to scale: heating into the plasma, the fusion power split into neutrons and alphas, and the
    range of electrical power the whole plant draws from the grid (iter.org: 110 MW at least, up to 620 MW in
    30-second peaks)."""
    f = Fig("fy14ii-power", 500, "Bar chart to scale, power in megawatts. First bar: 50 MW of heating power delivered into the "
            "plasma. Second bar: 500 MW of fusion power made in the plasma, divided into about 400 MW carried by neutrons, "
            "which leave the plasma and heat the blanket, and about 100 MW carried by helium nuclei, which stay in the plasma "
            "and heat it. Third bar: the electricity that the whole ITER plant draws from the grid, at least 110 MW, drawn "
            "solid, and up to 620 MW in peaks of 30 seconds, drawn as a pale range with a dashed outline.", width=560, size=26)
    base, top = 400, 70          # 0 MW and 650 MW
    S = (base - top) / 650
    y = lambda mw: base - mw * S
    f.line(64, base, 545, base, INK, 2.5)
    for mw in (200, 400, 600):
        f.line(64, y(mw), 545, y(mw), RULE_LIGHT, 1.5)
        f.tex(56, y(mw), str(mw), "end")
    f.tex(56, base, "0", "end")
    f.tex(8, 26, r"P\ (\text{MW})", "start")
    # bar 1: heating
    f.rect(80, y(50), 90, 50 * S, HEAT, INK, 2)
    f.tex(125, y(50) - 22, r"50", "middle")
    # bar 2: fusion power, neutrons and alphas
    pa = 500 * ALPHA_SHARE
    f.rect(215, y(500), 130, pa * S, HOT, INK, 2)
    f.rect(215, y(500 - pa), 130, (500 - pa) * S, COLD, INK, 2)
    f.tex(280, y(500) + pa * S / 2, r"\alpha\text{: }100", "middle", color=WHITE)
    f.tex(280, y(200), r"\text{n: }400", "middle", color=WHITE)
    f.tex(280, y(500) - 22, r"500", "middle")
    # bar 3: grid electricity drawn by the plant, a range
    f.rect(395, y(620), 130, (620 - 110) * S, GOOD_LIGHT, None, 0, extra='fill-opacity="0.45"')
    f.path(f"M395,{n(y(110))} L395,{n(y(620))} L525,{n(y(620))} L525,{n(y(110))}", stroke=INK, w=2, extra='stroke-dasharray="6 5"')
    f.rect(395, y(110), 130, 110 * S, GOOD_LIGHT, INK, 2)
    f.tex(460, y(55), r"110", "middle")
    f.tex(460, y(620) - 22, r"620", "middle")
    f.tex(460, y(365), r"\text{peaks}", "middle")
    for x, a, b in ((125, "heating", "into plasma"), (280, "fusion", "in plasma"), (460, "grid", "electricity in")):
        f.tex(x, base + 26, rf"\text{{{a}}}", "middle")
        f.tex(x, base + 60, rf"\text{{{b}}}", "middle")
    return f.svg()


FIGURES = {"hero": hero, "power": power}
