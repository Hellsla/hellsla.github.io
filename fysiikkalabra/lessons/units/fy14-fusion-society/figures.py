"""Figures of the unit fy14-fusion-society (scripts/figlib.py, herolib.py); `python3 scripts/units.py figures
fy14-fusion-society` writes them into content/en/units/fy14-fusion-society/unit.md. English: decimal point.
hero: an electricity landscape at dusk (wind, solar, a fossil plant, a nuclear plant and a fusion building under
construction), no text and no answer to any prediction. cycle: the D–T fuel cycle with a lithium breeding blanket."""
import figlib
from figlib import (Fig, INK, MUTED, WHITE, GLASS, ALUMINIUM, METAL_EDGE, IRON, COLD, COLD_LIGHT, HOT, HEAT, HEAT_LIGHT,
                    SAND_LIGHT, SAND, GOOD, GOOD_LIGHT, RULE, n)
import herolib as H

figlib.set_language({}, ".")

SOLAR, SOLAR_EDGE = "#1f4e8c", "#0b2547"
CONCRETE, CONCRETE_DARK = "#d9d4c7", "#a8a191"
GRASS, GRASS_DARK = "#8db36b", "#5f8a45"
VIOLET, VIOLET_LIGHT = "#7048e8", "#e5dbff"
NEUTRON = "#0b7285"


def solar_panel(f, x, y, w=70, h=34):
    """A tilted solar panel on two legs: a dark blue parallelogram with a cell grid."""
    f.line(x + 12, y + h, x + 12, y + h + 22, IRON, 3); f.line(x + w - 10, y + h - 10, x + w - 10, y + h + 22, IRON, 3)
    f.path(f"M{n(x)},{n(y + h)} L{n(x + 14)},{n(y)} H{n(x + w + 14)} L{n(x + w)},{n(y + h)} Z", SOLAR, SOLAR_EDGE, 2)
    for k in (1, 2, 3):
        t = k / 4
        f.line(x + w * t, y + h, x + 14 + w * t, y, "#6c93c9", 1.2)
    f.line(x + 7, y + h / 2, x + w + 7, y + h / 2, "#6c93c9", 1.2)


def hero():
    f = H.hero("fy14fs-hero", "Illustration: a wide landscape at dusk, seen from a hill. On the left, wind turbines turn on "
               "green fields and rows of solar panels face the low sun. In the middle, a coal power station with two chimneys "
               "sends grey smoke into the sky, and beside it a nuclear power station has a large cooling tower with white "
               "steam. Transmission-line pylons carry wires across the land to a small town of houses with lit windows. "
               "On the far right, a large new building with a round top stands behind cranes: a fusion experiment that is "
               "still being built. The sky is half clear, half cloudy.")
    H.sky(f, "fs", 600, "#f7c98b", "#5b7fa8")
    H.sun(f, "fs", 250, 300, 46)
    H.cloud(f, 760, 90, 0.9, fill="#e9eef3")
    H.cloud(f, 1040, 150, 0.7, fill="#e9eef3")
    H.cloud(f, 420, 70, 0.55, fill="#f1f3f5")
    H.hills(f, "fs", 330, ["#9fb98a", GRASS], amp=30, seed=3)
    # wind turbines on the left hills
    for x, yb, h, t in ((70, 380, 190, 0.3), (180, 360, 150, 1.4), (285, 372, 120, 2.2)):
        H.wind_turbine(f, x, yb, h, turn=t, sc=1.2)
    # rows of solar panels in the foreground left
    f.path("M0,470 C200,450 380,470 520,500 L520,600 H0 Z", GRASS_DARK)
    for row, y in enumerate((468, 520)):
        for k in range(4):
            solar_panel(f, 20 + 105 * k + 30 * row, y, 78, 30)
    # the coal power station: hall and two chimneys with smoke
    f.rect(470, 360, 130, 70, CONCRETE, INK, 2.5)
    for x in (490, 560):
        f.rect(x, 230, 22, 130, CONCRETE_DARK, INK, 2.5)
        f.rect(x, 246, 22, 10, HOT)
    H.smoke(f, 500, 220, 1.2, "#8f959b", 0.75)
    H.smoke(f, 572, 214, 1.0, "#8f959b", 0.7)
    # the nuclear power station: hyperbolic cooling tower with steam and a dome reactor building
    f.path("M630,430 C650,380 650,330 640,290 H730 C720,330 720,380 740,430 Z", CONCRETE, INK, 2.5)
    H.cloud(f, 686, 262, 0.55, fill=WHITE)
    f.path("M750,430 V385 A40,40 0 0 1 830,385 V430 Z", "#eceae4", INK, 2.5)
    # pylons and wires towards the town
    a = H.pylon(f, 610, 520, 120, 0.8); b = H.pylon(f, 790, 540, 140, 0.9); c = H.pylon(f, 960, 520, 110, 0.75)
    for p, q in zip(a, b): H.wire(f, p, q, 18, INK, 1.5)
    for p, q in zip(b, c): H.wire(f, p, q, 16, INK, 1.5)
    # the small town in the middle ground
    for x, w, hh, roof in ((860, 50, 40, HOT), (918, 44, 46, IRON), (970, 52, 38, HOT)):
        H.house(f, x, 448, w, hh, wall=SAND_LIGHT, roof=roof, window="#ffd43b")
    # the fusion building under construction on the right: a cylinder with a dome, scaffolding and two cranes
    f.rect(1040, 300, 130, 150, "#e6e9ed", INK, 2.5)
    f.path("M1040,300 A65,42 0 0 1 1170,300 Z", ALUMINIUM, INK, 2.5)
    for y in range(320, 450, 26): f.line(1040, y, 1170, y, METAL_EDGE, 1.5)
    for x in range(1060, 1170, 26): f.line(x, 300, x, 450, METAL_EDGE, 1.2)
    for x0, top, jib in ((1010, 170, 160), (1185, 210, -120)):
        f.line(x0, 450, x0, top, HEAT, 5)
        f.line(x0 - 30 * (1 if jib > 0 else -1), top, x0 + jib, top, HEAT, 4)
        f.line(x0, top - 24, x0 + jib * 0.6, top, HEAT, 2)
        f.line(x0 + jib * 0.8, top, x0 + jib * 0.8, top + 60, INK, 1.5)
        f.rect(x0 + jib * 0.8 - 8, top + 60, 16, 12, IRON)
    # ground of the right half
    f.path("M520,500 C700,470 900,450 1200,450 V600 H520 Z", GRASS)
    f.path("M0,560 C300,545 800,560 1200,540 V600 H0 Z", GRASS_DARK)
    return f.svg()


def cycle():
    f = Fig("fy14fs-cycle", 470, "Diagram of the fuel cycle of a deuterium–tritium fusion power plant. In the centre, "
            "a plasma ring where a deuterium nucleus and a tritium nucleus fuse into a helium-4 nucleus and a neutron. "
            "Deuterium comes in from water on the left (blue arrow). The neutron (teal arrow) flies out of the plasma into "
            "the surrounding green blanket that contains lithium-6. There the neutron and lithium-6 make a new tritium "
            "nucleus and a helium-4 nucleus, as the equation under the blanket says. A red arrow carries the new tritium "
            "back to the plasma. Heat from the blanket goes out to the right.", width=600, size=28)
    f.add(f'<ellipse cx="320" cy="190" rx="200" ry="150" fill="{GOOD_LIGHT}" stroke="{GOOD}" stroke-width="3"/>')
    f.add(f'<ellipse cx="320" cy="190" rx="140" ry="82" fill="{VIOLET_LIGHT}" stroke="{VIOLET}" stroke-width="3"/>')
    f.tex(320, 140, r"\text{plasma}", "middle", VIOLET)
    f.tex(320, 192, r"\text{D} + \text{T} \to {}^{4}_{2}\text{He} + \text{n}", "middle")
    f.tex(320, 60, r"\text{blanket}", "middle", GOOD)
    # the neutron flies into the blanket and stops inside it
    f.arrow(388, 230, 440, 278, NEUTRON, 3)
    f.tex(452, 240, r"\text{n}", "start", NEUTRON)
    # the bred tritium returns to the plasma
    f.path("M226,300 C176,286 176,250 200,234", stroke=HOT, w=3)
    f.arrow(194, 240, 206, 230, HOT, 3)
    f.tex(176, 312, r"\text{T}", "end", HOT)
    # deuterium from water
    f.rect(4, 86, 92, 44, COLD_LIGHT, COLD, 2, 4)
    f.tex(50, 108, r"\text{water}", "middle")
    f.arrow(96, 118, 186, 170, COLD, 3)
    f.tex(100, 160, r"\text{D}", "middle", COLD)     # under the arrow, outside the blanket (light correction 2026-11-11: was on its outline)
    # heat out to the right
    f.block_arrow(520, 190, 594, 190, HEAT_LIGHT, 18, 34, 18)
    f.tex(588, 150, r"\text{heat}", "end", HEAT)
    # the breeding reaction under the blanket
    f.tex(300, 400, r"\text{in the blanket:}", "middle", GOOD)
    f.tex(300, 440, r"\text{n} + {}^{6}_{3}\text{Li} \to \text{T} + {}^{4}_{2}\text{He}", "middle", GOOD)
    return f.svg()


FIGURES = {"hero": hero, "cycle": cycle}
