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


def head(f, x, y, dx, dy, color, size=20):
    """A filled arrowhead at (x, y) pointing along (dx, dy)."""
    L = math.hypot(dx, dy); ux, uy = dx / L, dy / L
    bx, by = x - size * ux, y - size * uy
    f.path(f"M{x:.1f},{y:.1f} L{bx - 0.5 * size * uy:.1f},{by + 0.5 * size * ux:.1f} L{bx + 0.5 * size * uy:.1f},{by - 0.5 * size * ux:.1f} Z", color)


def ring_point(cx, cy, rx, ry, deg):
    t = math.radians(deg)
    return cx + rx * math.cos(t), cy + ry * math.sin(t), -rx * math.sin(t), ry * math.cos(t)


# The drawing language of fy14-confinement-concepts/pinch, copied here (not imported) for the pinch below: one way to draw
# a pinch in both units (teacher 2026-11-11, illustration audit). Field green (⊙ out of / ⊗ into the page), force red,
# current violet, plasma pink.
PINCH_F, PINCH_B, PINCH_I = "#c92a2a", "#2b8a3e", "#7048e8"
PINCH_PLASMA, PINCH_PLASMA_LIGHT = "#e64980", "#fcc2d7"


def pinch_odot(f, x, y, r=9):
    f.circle(x, y, r, WHITE, PINCH_B, 2.2); f.circle(x, y, 2.6, PINCH_B)


def pinch_otimes(f, x, y, r=9):
    f.circle(x, y, r, WHITE, PINCH_B, 2.2)
    d = r * 0.68
    f.line(x - d, y - d, x + d, y + d, PINCH_B, 2.2); f.line(x - d, y + d, x + d, y - d, PINCH_B, 2.2)


def pinch():
    """Two kinds of pinch, one above the other: a Z-pinch (current along the column, field circling it) and a theta
    pinch (current in a coil around the column, field along the axis). Force arrows red and pointing inwards.
    Light correction (teacher 2026-11-11, illustration audit): drawn as fy14-confinement-concepts/pinch is (pink plasma,
    violet current, the field as ⊙ above and ⊗ below the column, the coil around a glass tube), labels at 24 px, each in a
    space of its own. The directions are the same as before: the current to the right, the field circling it (out of the
    page above, into it below); in the coil the current runs down on the front of each turn, so the field points right."""
    f = Fig("fy14sf-pinch", 500, "Diagram of two kinds of pinch. Top, the Z-pinch: a horizontal pink plasma column with a violet "
            "arrow for the current I flowing along it, from left to right. Above the column the magnetic field B points out of the "
            "page (green circles with a dot), below it into the page (green circles with a cross): the field circles the current. "
            "Red arrows above and below the column point inwards, towards its axis: the magnetic force F squeezes the plasma. "
            "Bottom, the theta pinch: the same kind of column inside a glass tube, wound with a violet coil whose turns carry the "
            "current I around the column (an arrowhead on the front of the last turn shows it flowing down). A green arrow along "
            "the axis shows the magnetic field B pointing along the column, and red arrows again point inwards.", width=600, size=24)
    f.rect(0, 0, 600, 500, WHITE)
    # --- Z-pinch
    f.tex(14, 24, r"\text{Z-pinch: current along the plasma}", "start")
    y0 = 130
    f.rect(70, y0 - 28, 460, 56, PINCH_PLASMA_LIGHT, PINCH_PLASMA, 2.5, 28)
    f.arrow(110, y0, 500, y0, PINCH_I, 4, 16)
    f.tex(544, y0, r"I", "start", color=PINCH_I)
    for x in range(100, 520, 70):
        pinch_odot(f, x, y0 - 52); pinch_otimes(f, x, y0 + 52)
    for x in (135, 275, 415):
        f.arrow(x, y0 - 82, x, y0 - 32, PINCH_F, 4, 14)
        f.arrow(x, y0 + 82, x, y0 + 32, PINCH_F, 4, 14)
    f.tex(470, y0 - 52, r"\overline{B}", "start", color=PINCH_B)
    f.tex(428, y0 - 84, r"\overline{F}", "start", color=PINCH_F)
    f.tex(300, y0 + 114, r"\text{The field circles the current.}", "middle")
    # --- theta pinch
    f.line(14, 272, 586, 272, RULE, 2)
    f.tex(14, 300, r"\text{Theta pinch: current in a coil}", "start")
    y1 = 418
    f.add(f'<rect x="50" y="{y1 - 44}" width="480" height="88" rx="44" fill="{GLASS}" stroke="{METAL_EDGE}" stroke-width="3"/>')
    f.rect(90, y1 - 18, 400, 36, PINCH_PLASMA_LIGHT, PINCH_PLASMA, 2.5, 18)
    for k in range(10):
        x = 82 + k * 46
        f.add(f'<ellipse cx="{x}" cy="{y1}" rx="9" ry="56" fill="none" stroke="{PINCH_I}" stroke-width="5"/>')
    px, py, dx, dy = ring_point(82 + 9 * 46, y1, 9, 56, 45)   # current in the front of the last turn flows down
    head(f, px + 3, py + 12, dx, dy, PINCH_I, 20)
    f.tex(372, y1 - 82, r"I\ \text{in the coil}", "start", color=PINCH_I)
    f.arrow(70, y1, 556, y1, PINCH_B, 4, 16)
    f.tex(562, y1, r"\overline{B}", "start", color=PINCH_B)
    for x in (151, 289):                                # between the turns
        f.arrow(x, y1 - 66, x, y1 - 22, PINCH_F, 4, 14)
        f.arrow(x, y1 + 66, x, y1 + 22, PINCH_F, 4, 14)
    f.tex(151, y1 - 82, r"\overline{F}", "middle", color=PINCH_F)
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
    f.tex(300, 350, r"\text{Arrows show where neutrons fly.}", "middle", size=26, w=580)
    return f.svg()


FIGURES = {"hero": hero, "pinch": pinch, "neutrons": neutrons}
