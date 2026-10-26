"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy3-13` writes them into lesson.md."""
import herolib as H


def hero():
    """The chapter's opening illustration: the school experiment for absolute zero on a lab bench."""
    f = H.hero("fy313-hero", "Kuvitus: laboratoriopöydällä on kolme astiaa: jäävesi, huoneenlämpöinen vesi ja kuumalla levyllä "
               "kiehuva vesi. Keskimmäisessä hauteessa on suljettu lasipullo, joka on letkulla yhdistetty painemittariin.")
    f.rect(0, 0, 1200, 600, H.WHITE)
    for x in range(0, 1201, 80): f.line(x, 0, x, 420, H.RULE_LIGHT, 2)
    for y in range(0, 421, 80): f.line(0, y, 1200, y, H.RULE_LIGHT, 2)
    f.rect(0, 420, 1200, 26, H.RULE, H.INK, 3)
    f.rect(0, 446, 1200, 154, H.RULE_LIGHT)
    water = H.grad(f, "fy313h-water", H.WATER_LIGHT, H.WATER)

    def beaker(x, w, h, level):
        f.path(f"M{x},{420 - h} V410 Q{x},420 {x + 10},420 H{x + w - 10} Q{x + w},420 {x + w},410 V{420 - h}", H.GLASS)
        f.path(f"M{x + 3},{420 - level} H{x + w - 3} V410 Q{x + w - 3},417 {x + w - 10},417 H{x + 10} Q{x + 3},417 {x + 3},410 Z", water)
        f.path(f"M{x},{420 - h} V410 Q{x},420 {x + 10},420 H{x + w - 10} Q{x + w},420 {x + w},410 V{420 - h}", stroke=H.INK, w=3)
    # ice water
    beaker(80, 200, 170, 130)
    for k, (dx, dy) in enumerate(((30, 300), (80, 296), (130, 304), (60, 330), (110, 336))):
        f.rect(80 + dx, dy, 36, 30, H.ICE, H.ICE_EDGE, 2, 5)
    # bath with the flask and the gauge
    beaker(450, 300, 200, 160)
    f.path("M600,250 V150", stroke=H.INK, w=14)
    f.path("M600,250 V150", stroke=H.GLASS, w=8)
    f.circle(600, 320, 70, H.GLASS, H.INK, 3)
    f.circle(600, 320, 70, "none", H.WATER_LIGHT, 2)
    f.path("M600,150 Q600,96 680,96 H790", stroke=H.INK, w=10)
    f.circle(860, 120, 76, H.WHITE, H.INK, 4)
    for k in range(11):
        a = H.math.radians(140 + k * 26)
        f.line(860 + 58 * H.math.cos(a), 120 + 58 * H.math.sin(a), 860 + 68 * H.math.cos(a), 120 + 68 * H.math.sin(a), H.MUTED, 2.5)
    f.path("M860,120 L900,72", stroke=H.HOT, w=5, extra='stroke-linecap="round"')
    f.circle(860, 120, 8, H.INK)
    f.rect(780, 120, 12, 300, H.IRON)
    f.rect(740, 408, 92, 12, H.IRON, rx=3)
    # boiling water on a hot plate
    f.rect(930, 400, 220, 20, H.IRON, H.INK, 3, 4)
    f.add(f'<ellipse cx="1040" cy="400" rx="120" ry="10" fill="{H.HOT}" fill-opacity="0.8"/>')
    f.path("M960,230 V380 Q960,392 972,392 H1108 Q1120,392 1120,380 V230", H.GLASS)
    f.path("M963,270 H1117 V380 Q1117,389 1108,389 H972 Q963,389 963,380 Z", water)
    for k in range(9):
        f.circle(975 + H.rnd(k, 4) * 130, 290 + H.rnd(k, 7) * 90, 4 + 5 * H.rnd(k, 9), H.WHITE, H.WATER, 1.5)
    f.path("M960,230 V380 Q960,392 972,392 H1108 Q1120,392 1120,380 V230", stroke=H.INK, w=3)
    for x in (1000, 1060):
        f.path(f"M{x},224 c14,-24 -14,-40 0,-70", stroke=H.RULE, w=20, extra='stroke-linecap="round" stroke-opacity="0.55"')
        f.path(f"M{x},224 c14,-24 -14,-40 0,-70", stroke=H.WHITE, w=14, extra='stroke-linecap="round"')
    return f.svg()


FIGURES = {"hero": hero}
