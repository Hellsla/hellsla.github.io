"""Figures of the unit fy9-harjoituskoe (scripts/figlib.py, herolib.py); `python3 scripts/units.py figures fy9-harjoituskoe`
writes them into content/fi/units/fy9-harjoituskoe/unit.md. The unit is written in Finnish (decimal comma).

hero    the opening illustration: an empty school hall set up for the six-hour exam on a winter morning: rows of
        desks with laptops seen in perspective, a large wall clock, a window with snowy spruces, a water bottle and a
        squared notebook on the nearest desk (no text, no people)
plan    the time plan of the mock exam as a bar to scale: 360 minutes split into reading and choosing, Osa I, the four
        Osa II tasks, the two Osa III tasks and the final check
"""
import math
import figlib
from figlib import (Fig, fi, INK, MUTED, WHITE, RULE, RULE_LIGHT, GLASS, ALUMINIUM, METAL_EDGE, IRON, COLD, COLD_LIGHT,
                    HOT, HEAT, HEAT_LIGHT, SAND, SAND_LIGHT, GRAIN, GOOD, GOOD_LIGHT, WATER, WATER_LIGHT, ICE, PAPER, n)
import herolib as H

figlib.set_language({}, ",")

PLAN = [("Lue ja valitse", 15, GLASS), ("Osa I", 50, COLD_LIGHT), ("Osa II", 160, SAND_LIGHT), ("Osa III", 110, GOOD_LIGHT),
        ("Tarkista", 25, GLASS)]


def _desk(f, x, y, sc, k):
    """A desk seen from behind and slightly above at (x, y) (top front edge centre), scale sc, with a laptop whose
    screen shows a small graph (k: which of three screens) and a chair in front."""
    w, d, leg = 190 * sc, 46 * sc, 70 * sc
    # chair (behind the desk from the viewer: the viewer looks at the students' side)
    f.path(f"M{n(x - 40 * sc)},{n(y + d + 8 * sc)} L{n(x + 40 * sc)},{n(y + d + 8 * sc)} L{n(x + 46 * sc)},{n(y + d + 26 * sc)} "
           f"L{n(x - 46 * sc)},{n(y + d + 26 * sc)} Z", COLD, INK, 2 * sc)
    f.line(x - 40 * sc, y + d + 26 * sc, x - 40 * sc, y + d + 70 * sc, IRON, 4 * sc)
    f.line(x + 40 * sc, y + d + 26 * sc, x + 40 * sc, y + d + 70 * sc, IRON, 4 * sc)
    # the desk top and legs
    f.line(x - w / 2 + 10 * sc, y + d, x - w / 2 + 10 * sc, y + d + leg, METAL_EDGE, 5 * sc)
    f.line(x + w / 2 - 10 * sc, y + d, x + w / 2 - 10 * sc, y + d + leg, METAL_EDGE, 5 * sc)
    f.path(f"M{n(x - w / 2 + 14 * sc)},{n(y)} L{n(x + w / 2 - 14 * sc)},{n(y)} L{n(x + w / 2)},{n(y + d)} L{n(x - w / 2)},{n(y + d)} Z",
           SAND, GRAIN, 2 * sc)
    f.rect(x - w / 2, y + d, w, 8 * sc, GRAIN, None, 0)
    # the laptop: screen facing the chair (we see its back), a small graph glimpse on a reflection-free face
    sw, sh = 92 * sc, 62 * sc
    f.path(f"M{n(x - sw / 2)},{n(y + d * 0.55)} L{n(x + sw / 2)},{n(y + d * 0.55)} L{n(x + sw / 2 - 4 * sc)},{n(y + d * 0.55 - sh)} "
           f"L{n(x - sw / 2 + 4 * sc)},{n(y + d * 0.55 - sh)} Z", ALUMINIUM, INK, 2 * sc)
    f.circle(x, y + d * 0.55 - sh / 2, 5 * sc, METAL_EDGE)
    f.path(f"M{n(x - sw / 2 - 6 * sc)},{n(y + d * 0.55)} L{n(x + sw / 2 + 6 * sc)},{n(y + d * 0.55)} L{n(x + sw / 2 + 12 * sc)},{n(y + d * 0.8)} "
           f"L{n(x - sw / 2 - 12 * sc)},{n(y + d * 0.8)} Z", METAL_EDGE, INK, 1.5 * sc)
    # paper and a pencil beside the laptop
    px = x + (58 if k % 2 else -78) * sc
    f.path(f"M{n(px)},{n(y + 10 * sc)} L{n(px + 22 * sc)},{n(y + 8 * sc)} L{n(px + 26 * sc)},{n(y + 34 * sc)} L{n(px + 2 * sc)},{n(y + 36 * sc)} Z",
           WHITE, MUTED, 1.2 * sc)
    f.line(px + 6 * sc, y + 40 * sc, px + 30 * sc, y + 30 * sc, HEAT, 3 * sc, cap="round")


def hero():
    """Opening illustration of the Why question: the exam hall waits, the clock says the long day has just begun."""
    f = H.hero("fy9hk-hero", "Kuvitus: tyhjä koulun sali talviaamuna valmiina kuuden tunnin kokeeseen. Salissa on kolme riviä "
               "pulpetteja, joilla on kannettavat tietokoneet, paperia ja kynät, ja niiden edessä tuolit. Seinällä on suuri kello, "
               "ja ikkunasta näkyy lumisia kuusia ja matalalla paistava aurinko. Etualan pulpetilla on vesipullo ja ruutuvihko, "
               "jossa on lyijykynällä piirretty kuvaaja. Kuvassa ei ole ihmisiä eikä tekstiä.")
    f.rect(0, 0, 1200, 600, PAPER)
    f.rect(0, 0, 1200, 300, H.grad(f, "fy9hk-wall", "#eef5f9", "#e3dccb"))
    f.path("M0,300 L1200,300 L1200,600 L0,600 Z", H.grad(f, "fy9hk-floor", SAND_LIGHT, SAND))
    f.line(0, 300, 1200, 300, GRAIN, 4)
    for i in range(1, 9):                                   # floor boards converging towards the far wall
        f.line(600 + (i - 4.5) * 90, 300, 600 + (i - 4.5) * 330, 600, "#d8bb83", 2)
    # the window with a winter view
    f.rect(60, 50, 300, 200, H.grad(f, "fy9hk-sky", "#d0e6fb", "#fdf1dc"), INK, 4, 4)
    H.sun(f, "fy9hk", 270, 205, 26, rays=False)
    f.path("M64,214 Q140,196 210,212 Q290,226 356,206 L356,246 L64,246 Z", WHITE)
    for k, (x, h) in enumerate([(92, 82), (128, 112), (170, 70), (312, 96), (338, 74)]):
        H.spruce(f, x, 236, h, "#2f6b3e")
        f.path(f"M{n(x - h * 0.2)},{n(236 - h * 0.35)} L{n(x)},{n(236 - h * 0.48)} L{n(x + h * 0.2)},{n(236 - h * 0.35)} Z", WHITE, extra='fill-opacity="0.85"')
    f.line(210, 50, 210, 250, INK, 4)
    f.line(60, 150, 360, 150, INK, 4)
    f.rect(50, 248, 320, 12, ALUMINIUM, INK, 2)
    # the wall clock: just past nine
    cx, cy = 820, 140
    f.circle(cx, cy, 92, ALUMINIUM, INK, 4)
    f.circle(cx, cy, 78, WHITE, INK, 2)
    for k in range(60):
        a = k * math.pi / 30
        r0 = 64 if k % 5 == 0 else 70
        f.line(cx + math.sin(a) * r0, cy - math.cos(a) * r0, cx + math.sin(a) * 74, cy - math.cos(a) * 74, INK if k % 5 == 0 else MUTED,
               4 if k % 5 == 0 else 1.5)
    ah, am = math.radians(9 * 30 + 3), math.radians(6 * 6)
    f.line(cx, cy, cx + math.sin(ah) * 40, cy - math.cos(ah) * 40, INK, 8, cap="round")
    f.line(cx, cy, cx + math.sin(am) * 60, cy - math.cos(am) * 60, INK, 5, cap="round")
    f.line(cx - math.sin(am * 3) * 12, cy + math.cos(am * 3) * 12, cx + math.sin(am * 3) * 66, cy - math.cos(am * 3) * 66, HOT, 2.5, cap="round")
    f.circle(cx, cy, 7, HOT)
    # a notice board area on the wall: a blank calendar sheet with the long day shaded (no text)
    f.rect(1010, 60, 130, 170, WHITE, INK, 2.5, 4)
    for r in range(5):
        for c in range(4):
            fill = HEAT_LIGHT if (r, c) == (2, 1) else GLASS
            f.rect(1022 + c * 28, 84 + r * 28, 22, 22, fill, RULE, 1)
    f.circle(1075, 62, 7, HOT)
    # three rows of desks, far to near
    for row, (y, sc, xs) in enumerate([(318, 0.55, [420, 600, 780, 960]), (370, 0.75, [300, 560, 820, 1080]),
                                       (450, 1.0, [430, 830])]):
        for k, x in enumerate(xs):
            _desk(f, x, y, sc, k + row)
    # the nearest desk: a water bottle and a squared notebook with a pencil graph
    f.rect(1040, 410, 40, 120, H.grad(f, "fy9hk-bottle", WATER_LIGHT, WATER), INK, 2.5, 10)
    f.rect(1047, 388, 26, 26, COLD, INK, 2.5, 5)
    f.line(1047, 450, 1073, 450, WHITE, 3, cap="round")
    f.path("M60,470 L250,452 L270,580 L82,598 Z", WHITE, INK, 2.5)
    for i in range(1, 8):
        t = i / 8
        f.line(60 + 22 * t, 470 + 128 * t, 250 + 20 * t, 452 + 128 * t, COLD_LIGHT, 1.5)
        f.line(60 + 190 * t, 470 - 18 * t, 82 + 188 * t, 598 - 18 * t, COLD_LIGHT, 1.5)
    f.arrow(100, 566, 226, 554, INK, 2.5, 11)
    f.arrow(100, 566, 90, 482, INK, 2.5, 11)
    f.path("M108,556 Q150,540 170,516 Q192,490 214,482", "none", COLD, 3.5)
    for x, y in [(118, 552), (146, 538), (172, 512), (200, 488)]:
        f.circle(x, y, 5, INK, WHITE, 1.5)
    return f.svg()


def plan():
    """The time plan of the mock exam to scale: one bar of 360 minutes split into five blocks, the block names inside
    the wide blocks, the minutes under the bar and the hour marks over it."""
    total = sum(m for _, m, _ in PLAN)
    f = Fig("fy9hk-plan", 270, "Kaavio mittakaavassa: kuuden tunnin eli 360 minuutin aikasuunnitelma yhtenä palkkina. Lukeminen ja "
            "valinta 15 min, Osa I 50 min, Osa II 160 min eli neljä tehtävää noin 40 min kukin, Osa III 110 min eli kaksi "
            "tehtävää noin 55 min kukin ja tarkistus 25 min. Palkin yläpuolella ovat tuntimerkit 0–6 h.", size=26)
    x0, x1, y, h = 20, 580, 70, 70
    X = lambda m: x0 + (x1 - x0) * m / total
    for hr in range(7):
        f.line(X(hr * 60), y - 10, X(hr * 60), y, MUTED, 2)
        f.tex(X(hr * 60), y - 30, rf"{hr}\,\text{{h}}", "middle" if 0 < hr < 6 else ("start" if hr == 0 else "end"), MUTED)
    t = 0
    for name, m, fill in PLAN:
        f.rect(X(t), y, X(t + m) - X(t), h, fill, INK, 2)
        cuts = [t + j * m / 4 for j in (1, 3)] if name == "Osa II" else []
        mids = [t + m / 2] if name in ("Osa II", "Osa III") else []
        for c in cuts: f.line(X(c), y + 8, X(c), y + h - 8, MUTED, 1.5, "5 4")
        for c in mids:  # stop the middle divider short of the block label
            f.line(X(c), y + 4, X(c), y + 16, MUTED, 1.5, "5 4")
            f.line(X(c), y + h - 16, X(c), y + h - 4, MUTED, 1.5, "5 4")
        if m >= 50: f.tex(X(t + m / 2), y + h / 2, rf"\text{{{name}}}", "middle")
        t += m
    t = 0
    for i, (name, m, _) in enumerate(PLAN):
        if i == 0: f.tex(X(0), y + h + 74, rf"\text{{Lue ja valitse}}\ {m}\,\text{{min}}", "start", MUTED)
        elif i == 4: f.tex(X(total), y + h + 74, rf"\text{{Tarkista}}\ {m}\,\text{{min}}", "end", MUTED)
        else: f.tex(X(t + m / 2), y + h + 30, rf"{m}\,\text{{min}}", "middle", MUTED)
        t += m
    f.line(X(7.5), y + h, X(7.5), y + h + 56, MUTED, 1.5)
    f.line(X(total - 12.5), y + h, X(total - 12.5), y + h + 56, MUTED, 1.5)
    return f.svg()


FIGURES = {"hero": hero, "plan": plan}
