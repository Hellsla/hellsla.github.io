"""Figures of the unit fy14-secret-fusion (scripts/figlib.py, herolib.py); `python3 scripts/units.py figures
fy14-secret-fusion` writes them into content/en/units/fy14-secret-fusion/unit.md. English: decimal point. The hero has
no text and does not show the answer to either prediction (why the work was secret; how ZETA's neutrons were tested).
Colours: magnetic field green (GOOD), force red (HOT), current dark ink with its own label, plasma orange (HEAT)."""
import math
import figlib
from figlib import (Fig, INK, MUTED, WHITE, RULE, RULE_LIGHT, GLASS, ALUMINIUM, METAL_EDGE, IRON, COPPER, COLD,
                    HOT, HEAT, HEAT_LIGHT, SAND, SAND_LIGHT, GOOD, n)
import herolib as H

figlib.set_language({}, ".")
NIGHT, NIGHT_LOW = "#16202b", "#2b3a4a"
BRICK, BRICK_DARK = "#7a5a48", "#5c4234"


def hero():
    """A laboratory building at night behind a locked gate in a high fence; through a large window a glowing ring of
    plasma; stars above. Secrecy, the stars and the machine, without saying why."""
    f = H.hero("fy14sf-hero", "Illustration: a brick laboratory building at night under a sky full of stars. Through a large "
               "window an orange glowing ring, a hot plasma in a ring-shaped machine, lights up the room. In the foreground a "
               "high wire fence crosses the whole picture, and its gate is closed with a chain and a heavy padlock. A narrow "
               "path leads from the gate to the dark door of the building.")
    f.rect(0, 0, 1200, 600, H.grad(f, "sf-sky", NIGHT, NIGHT_LOW))
    for k in range(80):
        x, y = H.rnd(k, 3) * 1200, H.rnd(k + 300, 3) * 300
        f.circle(x, y, round(1 + 1.8 * H.rnd(k + 700, 3), 1), WHITE)
    # one bright star (the Sun is a star): a small four-pointed glint
    sx, sy = 1060, 86
    f.path(f"M{sx},{sy - 26} L{sx + 6},{sy - 6} L{sx + 26},{sy} L{sx + 6},{sy + 6} L{sx},{sy + 26} L{sx - 6},{sy + 6} L{sx - 26},{sy} L{sx - 6},{sy - 6} Z", HEAT_LIGHT)
    # ground
    f.rect(0, 470, 1200, 130, H.grad(f, "sf-ground", "#2f3d2c", "#1d2a1c"))
    # the building
    f.rect(300, 200, 640, 280, H.grad(f, "sf-brick", BRICK, BRICK_DARK), INK, 3)
    f.rect(280, 186, 680, 22, IRON, INK, 3)
    for y in range(226, 470, 28):                      # brick courses
        f.line(304, y, 936, y, BRICK_DARK, 1.5)
    # the big window with the glowing ring inside
    f.rect(360, 240, 380, 190, H.grad(f, "sf-room", "#4a3a2a", "#2b211a"), INK, 4)
    f.add(f'<ellipse cx="550" cy="345" rx="150" ry="52" fill="none" stroke="{HEAT}" stroke-width="30" stroke-opacity="0.35"/>')
    f.add(f'<ellipse cx="550" cy="345" rx="150" ry="52" fill="none" stroke="{HEAT_LIGHT}" stroke-width="12"/>')
    for k in range(9):                                  # coils around the ring
        a = math.pi * 2 * k / 9
        x, y = 550 + 150 * math.cos(a), 345 + 52 * math.sin(a)
        f.rect(x - 9, y - 26, 18, 52, COPPER, INK, 2, 3)
    for x in (487, 613):
        f.line(x, 240, x, 430, INK, 4)                  # window frame
    f.line(360, 335, 740, 335, INK, 4)
    # the dark door and a small lit lamp above it
    f.rect(800, 330, 90, 150, "#2a1f19", INK, 3)
    f.circle(845, 312, 9, HEAT_LIGHT)
    # the path from the gate to the door
    f.path("M640,600 C700,560 790,520 830,480 L860,480 C840,520 780,560 760,600 Z", "#5b5446")
    # the fence: posts, a top rail and a wire mesh across the picture
    f.line(0, 430, 1200, 430, METAL_EDGE, 5)
    for x in range(0, 1201, 120):
        f.line(x, 425, x, 600, METAL_EDGE, 8)
    for x in range(-200, 1400, 30):
        f.line(x, 430, x + 170, 600, METAL_EDGE, 1.2)
        f.line(x + 170, 430, x, 600, METAL_EDGE, 1.2)
    # the gate in the middle: a darker frame, a chain and a padlock
    f.rect(600, 432, 240, 168, "none", ALUMINIUM, 7)
    f.line(720, 432, 720, 600, ALUMINIUM, 7)
    f.path("M690,500 Q705,520 720,505 Q735,490 750,512", stroke=ALUMINIUM, w=6)
    f.rect(700, 512, 40, 34, SAND, INK, 3, 5)
    f.path("M708,512 V500 Q720,484 732,500 V512", stroke=INK, w=5)
    f.circle(720, 528, 4, INK)
    return f.svg()


def pinch():
    """Two kinds of pinch, one above the other: a Z-pinch (current along the column, field circling it) and a theta
    pinch (current in a coil around the column, field along the axis). Force arrows red and pointing inwards."""
    f = Fig("fy14sf-pinch", 640, "Diagram of two kinds of pinch. Top, the Z-pinch: a horizontal orange plasma column with an "
            "arrow for the current I flowing along it, from left to right. Green rings around the column show the magnetic "
            "field B circling the current. Red arrows above and below the column point inwards, towards its axis: the "
            "magnetic force F squeezes the plasma. Bottom, the theta pinch: the same kind of column inside a copper coil whose "
            "turns carry the current I around the column. A green arrow along the axis shows the magnetic field B pointing "
            "along the column, and red arrows again point inwards.", width=600, size=28)
    f.rect(0, 0, 600, 640, WHITE)
    # --- Z-pinch
    f.tex(16, 30, r"\text{Z-pinch: current along the plasma}", size=28, w=568)
    cy = 170
    f.rect(60, cy - 30, 440, 60, H.grad(f, "sf-pl1", HEAT_LIGHT, HEAT), None, 2, 30)
    f.arrow(90, cy, 470, cy, INK, 4, 18)
    f.tex(512, cy, r"I", size=30)
    for x in (140, 280, 420):                           # field rings drawn as ellipses around the column
        f.add(f'<ellipse cx="{x}" cy="{cy}" rx="18" ry="62" fill="none" stroke="{GOOD}" stroke-width="3.5"/>')
        f.path(f"M{x + 18},{cy - 8} l-6,14 l12,-2 Z", GOOD)
    f.tex(96, cy - 74, r"\overline{B}", color=GOOD, size=30)
    for x in (210, 350):
        f.arrow(x, cy - 92, x, cy - 40, HOT, 4, 14)
        f.arrow(x, cy + 92, x, cy + 40, HOT, 4, 14)
    f.tex(364, cy - 84, r"\overline{F}", color=HOT, size=30)
    f.tex(300, cy + 122, r"\text{The field circles the current.}", "middle", size=28, w=580)
    # --- theta pinch
    f.line(16, 332, 584, 332, RULE, 2)
    f.tex(16, 366, r"\text{Theta pinch: current in a coil}", size=28, w=568)
    cy = 500
    f.rect(60, cy - 30, 440, 60, H.grad(f, "sf-pl2", HEAT_LIGHT, HEAT), None, 2, 30)
    for k in range(9):                                  # coil turns: copper ellipses around the column
        x = 90 + 50 * k
        f.add(f'<ellipse cx="{x}" cy="{cy}" rx="10" ry="52" fill="none" stroke="{COPPER}" stroke-width="7"/>')
    f.arrow(80, cy, 520, cy, GOOD, 4, 18)
    f.tex(530, cy, r"\overline{B}", color=GOOD, size=30)
    for x in (165, 365):
        f.arrow(x, cy - 104, x, cy - 36, HOT, 5, 14)
        f.arrow(x, cy + 104, x, cy + 36, HOT, 5, 14)
    f.tex(180, cy - 96, r"\overline{F}", color=HOT, size=30)
    f.tex(470, cy - 80, r"I\ \text{in the coil}", "middle", color=COPPER, size=28, w=180)
    return f.svg()


def neutrons():
    """Neutron directions: from a hot plasma (random ion motion) equal in all directions; from a few ions accelerated
    by an electric field mostly in one direction, and reversed when the current reverses."""
    f = Fig("fy14sf-neutrons", 380, "Diagram comparing two possible sources of neutrons. Left, a hot plasma: a round orange "
            "cloud with twelve dark arrows of equal length pointing out in all directions, labelled fusion in a hot plasma. "
            "Right, fast ions: a round cloud with a few long arrows pointing to the right and only short arrows in other "
            "directions, labelled a few accelerated ions.", width=600)
    f.rect(0, 0, 600, 380, WHITE)
    for cx, kind in ((150, "hot"), (450, "beam")):
        cy = 170
        f.circle(cx, cy, 50, H.grad(f, f"sf-n-{kind}", HEAT_LIGHT, HEAT))
        for k in range(12):
            a = 2 * math.pi * k / 12
            if kind == "hot":
                L = 80
            else:
                L = 52 + 80 * max(0.0, math.cos(a)) ** 3
            x0, y0 = cx + 54 * math.cos(a), cy + 54 * math.sin(a)
            f.arrow(x0, y0, x0 + (L - 30) * math.cos(a) + 1e-6, y0 + (L - 30) * math.sin(a), INK, 3, 12)
    f.tex(150, 300, r"\text{fusion in a hot plasma}", "middle", size=26, w=296)
    f.tex(450, 300, r"\text{a few accelerated ions}", "middle", size=26, w=296)
    f.tex(300, 350, r"\text{Arrows show where neutrons fly.}", "middle", size=26, w=580, color=MUTED)
    return f.svg()


FIGURES = {"hero": hero, "pinch": pinch, "neutrons": neutrons}
