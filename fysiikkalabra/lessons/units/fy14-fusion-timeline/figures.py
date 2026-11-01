"""Figures of the unit fy14-fusion-timeline (scripts/figlib.py, herolib.py); `python3 scripts/units.py figures
fy14-fusion-timeline` writes them into content/en/units/fy14-fusion-timeline/unit.md. The hero has no text: a long road
winding from a star on the left through four landscapes (the four eras) to a large ring machine on the right, with
milestone posts along it. It answers neither prediction (where fusion research happens; how long the steps took)."""
import math
import figlib
from figlib import (Fig, INK, MUTED, WHITE, RULE, RULE_LIGHT, GLASS, ALUMINIUM, METAL_EDGE, IRON, COPPER, COLD,
                    HOT, HEAT, HEAT_LIGHT, SAND, SAND_LIGHT, GOOD, GOOD_LIGHT, n)
import herolib as H

figlib.set_language({}, ".")
ERA_COLOURS = ("#dbe7f3", "#e9e1f3", "#f6e6d4", "#e2f0e2")   # pale bands behind the four stretches of the road


def hero():
    f = H.hero("fy14ft-hero", "Illustration: a long road winds from left to right across a landscape. At the far left a "
               "bright yellow star shines in a dark corner of the sky. The sky changes from night on the left to day on the "
               "right, over four stretches of land in pale colours. Small posts with coloured caps stand along the road "
               "like milestones, some round, some square, some diamond-shaped. At the far right, at the end of the road, "
               "stands a large ring-shaped machine with blue coils in front of a modern building.")
    f.rect(0, 0, 1200, 600, H.grad(f, "ft-sky", "#1f2b3a", "#a8cbe8", horizontal=True))
    for k in range(30):                                  # stars only in the dark left part
        x, y = H.rnd(k, 9) * 420, H.rnd(k + 70, 9) * 260
        f.circle(x, y, round(1 + 1.5 * H.rnd(k + 140, 9), 1), WHITE)
    H.sun(f, "ft", 120, 110, 44)
    # four stretches of land, one per era
    for i, c in enumerate(ERA_COLOURS):
        x0 = 300 * i
        f.path(f"M{x0},{330 + 10 * math.sin(i)} Q{x0 + 150},{300 + 20 * (i % 2)} {x0 + 300},{330 + 10 * math.sin(i + 1)} V600 H{x0} Z", c)
    f.path("M0,420 Q300,380 600,430 T1200,410 V600 H0 Z", "#cfd8c4", extra='fill-opacity="0.6"')
    # the road: a wide winding band from bottom left towards the machine on the right
    road = "M-20,560 C180,520 220,430 420,450 C620,470 600,560 800,520 C960,488 980,420 1080,410"
    f.path(road, stroke="#8a7f6d", w=54, extra='stroke-linecap="round"')
    f.path(road, stroke=SAND_LIGHT, w=4, extra='stroke-dasharray="22 18"')
    # milestone posts with shaped caps (the four theme shapes, colours as on the timeline strip)
    caps = [("circle", "#1d4ed8"), ("diamond", "#7e22ce"), ("square", "#c2410c"), ("triangle", "#0f766e"),
            ("circle", "#1d4ed8"), ("square", "#c2410c"), ("diamond", "#7e22ce"), ("square", "#c2410c")]
    posts = [(150, 505), (300, 452), (470, 420), (590, 470), (700, 552), (830, 478), (940, 442), (1010, 386)]
    for (x, y), (shape, c) in zip(posts, caps):
        f.rect(x - 4, y - 46, 8, 46, IRON)
        if shape == "circle": f.circle(x, y - 54, 12, c)
        elif shape == "square": f.rect(x - 11, y - 65, 22, 22, c)
        elif shape == "diamond": f.path(f"M{x},{y - 68} l13,13 l-13,13 l-13,-13 Z", c)
        else: f.path(f"M{x},{y - 68} l13,22 h-26 Z", c)
    # the building and the machine at the end of the road
    f.rect(1010, 220, 190, 170, WHITE, INK, 3)
    for x in range(1030, 1200, 40):
        f.rect(x, 240, 24, 40, GLASS, METAL_EDGE, 1.5)
    f.add(f'<ellipse cx="1090" cy="360" rx="96" ry="34" fill="none" stroke="{METAL_EDGE}" stroke-width="30"/>')
    for k in range(10):
        a = math.pi * 2 * k / 10
        x, y = 1090 + 96 * math.cos(a), 360 + 34 * math.sin(a)
        f.rect(x - 7, y - 26, 14, 52, COLD, INK, 1.5, 3)
    return f.svg()


FIGURES = {"hero": hero}
