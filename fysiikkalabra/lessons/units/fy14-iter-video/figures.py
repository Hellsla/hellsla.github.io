"""Figures of the unit fy14-iter-video (scripts/figlib.py, herolib.py); `python3 scripts/units.py figures
fy14-iter-video` writes them into content/en/units/fy14-iter-video/unit.md. The opening illustration is an original
drawing (no frame of the video is copied): a student's desk with a laptop playing a video of a giant assembly hall,
a notebook with empty lines and a magnifying glass, the tools of a video investigation."""
import figlib
from figlib import (Fig, INK, MUTED, WHITE, RULE, RULE_LIGHT, GLASS, ALUMINIUM, METAL_EDGE, IRON, COLD, COLD_LIGHT,
                    HOT, HEAT, HEAT_LIGHT, SAND, SAND_LIGHT, GOOD, n)
import herolib as H

figlib.set_language({}, ".")


def hero():
    f = H.hero("fy14iv-hero", "Illustration: a desk seen from the front. On it stands an open laptop. Its screen shows a video of a "
               "huge, bright assembly hall: an overhead crane on rails lifts a giant curved steel segment, and two smaller segments "
               "stand on the floor below. A large round play button sits in the middle of the screen and a progress bar runs "
               "along the bottom. Beside the laptop lie an open notebook with empty lines, a pencil and a magnifying glass.")
    f.rect(0, 0, 1200, 600, H.grad(f, "fy14iv-wall", "#e7f5ff", "#d0ebff"))
    f.rect(0, 470, 1200, 130, H.grad(f, "fy14iv-desk", SAND, "#a97a35"))
    f.line(0, 470, 1200, 470, "#e9c98a", 4)
    # laptop: screen and base
    f.rect(250, 70, 620, 380, INK, INK, 3, 16)
    f.rect(270, 90, 580, 330, H.grad(f, "fy14iv-hall", "#f8f9fa", "#ced4da"))
    # the hall on the screen: rails, crane bridge, segment on hooks, segments on the floor, floor line
    f.rect(270, 96, 580, 16, IRON)
    f.rect(270, 112, 580, 4, METAL_EDGE)
    f.rect(300, 132, 520, 22, HEAT, INK, 2)
    for k in range(10):
        f.line(310 + k * 52, 132, 336 + k * 52, 154, INK, 1.5)
    f.rect(540, 154, 36, 18, IRON, INK, 2)
    f.line(548, 172, 548, 196, INK, 2.5)
    f.line(568, 172, 568, 196, INK, 2.5)
    f.path("M500,196 L616,196 Q660,250 640,330 L600,330 Q612,262 576,232 L540,232 Q504,262 516,330 L476,330 Q456,250 500,196 Z",
           H.steel(f, "fy14iv-steel"), INK, 2.5)
    for x in (330, 710):
        f.path(f"M{x},{410} L{x + 30},{300} L{x + 80},{300} L{x + 110},{410} Z", "#adb5bd", INK, 2)
    f.line(270, 410, 850, 410, METAL_EDGE, 3)
    # play button and progress bar
    f.circle(560, 262, 54, WHITE, None)
    f.add('<circle cx="560" cy="262" r="54" fill="#1f2933" fill-opacity="0.55"/>')
    f.path("M542,232 L586,262 L542,292 Z", WHITE)
    f.rect(290, 396, 540, 8, "#495057", None, 0, 4)
    f.rect(290, 396, 200, 8, HOT, None, 0, 4)
    f.circle(490, 400, 9, HOT, WHITE, 2)
    f.path("M190,450 L930,450 L980,486 L140,486 Z", ALUMINIUM, INK, 3)
    f.rect(500, 458, 120, 14, METAL_EDGE, None, 0, 4)
    # notebook with empty lines, a pencil, a magnifying glass
    f.path("M940,500 L1150,488 L1170,590 L955,600 Z", WHITE, INK, 2.5)
    for k in range(5):
        f.line(960 + k * 0.6, 520 + k * 15, 1150 + k * 3, 509 + k * 15, COLD_LIGHT, 2)
    f.path("M1000,560 L1130,520 L1138,530 L1008,570 Z", HEAT_LIGHT, INK, 2)
    f.path("M1130,520 L1150,518 L1138,530 Z", INK)
    f.circle(100, 520, 46, GLASS, INK, 6)
    f.add('<circle cx="100" cy="520" r="40" fill="#a5d8ff" fill-opacity="0.35"/>')
    f.path("M134,552 L190,592", stroke=INK, w=14, extra='stroke-linecap="round"')
    return f.svg()


FIGURES = {"hero": hero}
