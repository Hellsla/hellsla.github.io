"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy1-8` writes them into lesson.md."""
from figlib import Fig, Axes, INK, MUTED, WHITE, RULE, SAND, SAND_DARK, SAND_LIGHT, ALUMINIUM, METAL_EDGE, COLD, GOOD, GOOD_LIGHT, HEAT, fi
from figlib import GLASS, HEAT_LIGHT, HOT, PAPER
import herolib as H
import math
from figlib import GRAIN, HOT_LIGHT, n
from herolib import grad
from figstyle import Fig, Axes            # the house illustration style (docs/illustration-style.md)
import figstyle as S


def hero():
    """The chapter's opening illustration: one toy car on a track, two groups timing it with their own tape and stopwatch."""
    f = S.hero("fy18-hero", "Kuvitus: luokan lattialla rata, jolla leluauto kulkee mittanauhan vieressä. Radan molemmin puolin on ryhmä: "
               "kummallakin on oma sekuntikello, ja kellojen viisarit ovat pysähtyneet eri kohtiin.")
    f.rect(0, 0, 1200, 600, PAPER)
    H.window(f, 120, 40, 200, 170, "fy18h-w1"); H.window(f, 880, 40, 200, 170, "fy18h-w2")
    f.rect(0, 300, 1200, 300, grad(f, "fy18h-floor", SAND, SAND_DARK, y1=300, y2=600))
    for k in range(13): f.line(600 + (k - 6) * 60, 300, 600 + (k - 6) * 240, 600, GRAIN, 1.5)
    f.line(0, 300, 1200, 300, INK, 3)
    # track board in perspective with the tape along its front
    f.path("M180,500 L1020,500 L940,400 L260,400 Z", grad(f, "fy18h-track", ALUMINIUM, METAL_EDGE), INK, 3)
    f.path("M260,400 H940", stroke=WHITE, w=2)
    for x in (300, 900): f.line(x, 400, x - 24, 500, HOT, 4, dash="10 8")         # start and finish marks
    f.rect(170, 504, 860, 30, HEAT_LIGHT, INK, 2.5, 4)
    for k in range(87): f.line(178 + k * 9.8, 504, 178 + k * 9.8, 504 + (18 if k % 10 == 0 else 12 if k % 5 == 0 else 7), INK, 1.5)
    # toy car with its motion lines
    x, y = 610, 466
    f.path(f"M{x - 80},{y + 8} V{y - 22} Q{x - 72},{y - 32} {x - 44},{y - 34} L{x - 24},{y - 66} H{x + 34} L{x + 58},{y - 34} Q{x + 82},{y - 30} {x + 84},{y - 14} V{y + 8} Z", grad(f, "fy18h-car", HOT_LIGHT, HOT), INK, 3)
    f.path(f"M{x - 16},{y - 58} H{x + 30} L{x + 46},{y - 36} H{x - 30} Z", GLASS, INK, 2)
    f.line(x + 8, y - 58, x + 8, y - 36, INK, 2)
    f.rect(x + 70, y - 22, 12, 8, HEAT_LIGHT, INK, 1.5, 2)
    for wx in (x - 46, x + 50): f.circle(wx, y + 10, 18, INK); f.circle(wx, y + 10, 8, ALUMINIUM)
    for k, (dx, dy) in enumerate(((150, -20), (130, -2), (160, 14))): f.line(x - dx, y + dy, x - dx + 40, y + dy, MUTED, 3, cap="round")
    # two groups, each with its own stopwatch held up
    for gx, shirts, turn in ((150, (COLD, GOOD), 0.27), (1050, (HEAT, COLD), 0.34)):
        sgn = 1 if gx < 600 else -1
        H.person(f, gx - 40 * sgn, 390, shirts[1], INK, 0.66)
        H.person(f, gx + 40 * sgn, 396, shirts[0], INK, 0.7)
        wx = gx + 110 * sgn
        f.line(gx + 40 * sgn + 20 * sgn, 396 - 236 * 0.7, wx, 276, shirts[0], 16, cap="round")   # the arm holds the watch out
        f.rect(wx - 12, 262, 24, 30, SAND_LIGHT, INK, 2, 10)
        H.stopwatch(f, wx, 222, 44, turn)
    return f.svg()


def _toy_car(f, x, yb, body="#e03131"):
    """A chunky battery toy car in side view, rear at x, wheels on yb, heading right: big wheels with hubcaps, a bubble
    cabin, a stripe, a headlight and an antenna."""
    ed = S.dark(body, 0.4)
    f.line(x + 22, yb - 46, x + 14, yb - 74, "#3a4350", 2, cap="round"); f.circle(x + 14, yb - 76, 3.5, "#ffd43b", "#3a4350", 1)
    f.path(f"M{x + 30},{yb - 40} Q{x + 34},{yb - 64} {x + 56},{yb - 64} H{x + 66} Q{x + 84},{yb - 64} {x + 90},{yb - 40} Z",
           "#d0ebff", "#3a4350", S.W_OBJ)                                                       # the bubble cabin
    f.line(x + 60, yb - 63, x + 60, yb - 40, "#3a4350", S.W_DETAIL)
    f.path(f"M{x + 46},{yb - 58} q6,-3 12,-2", stroke=WHITE, w=2.5, extra='stroke-linecap="round"')
    f.path(f"M{x},{yb - 16} V{yb - 34} Q{x},{yb - 42} {x + 10},{yb - 42} H{x + 98} Q{x + 112},{yb - 40} {x + 114},{yb - 26} "
           f"V{yb - 16} Q{x + 114},{yb - 12} {x + 108},{yb - 12} H{x + 6} Q{x},{yb - 12} {x},{yb - 16} Z", body, ed, S.W_OBJ)
    f.path(f"M{x + 6},{yb - 28} H{x + 108}", stroke=WHITE, w=4, extra='stroke-linecap="round"')          # racing stripe
    f.circle(x + 57, yb - 22, 7, WHITE, ed, 1.25); f.circle(x + 57, yb - 22, 3, body)              # a round sticker
    f.path(f"M{x + 108},{yb - 36} h6 v7 h-8 Z", "#ffd43b", S.dark("#ffd43b", 0.4), 1)             # headlight
    f.rect(x - 3, yb - 22, 6, 9, "#5c6670", rx=2); f.rect(x + 111, yb - 20, 6, 8, "#5c6670", rx=2)  # bumpers
    for wx in (x + 24, x + 90):
        f.circle(wx, yb - 14, 14, "#2b3138"); f.circle(wx, yb - 14, 7, "#e9ecef", "#868e96", 1)
        for k in range(4):
            a = math.pi / 4 + k * math.pi / 2
            f.circle(wx + 4 * math.cos(a), yb - 14 + 4 * math.sin(a), 1.2, "#868e96")


def setup():
    f = Fig("fy18-setup", 414, "Kaavakuva kokeen asetelmasta: paristokäyttöinen leluauto ajaa pöydällä lähtöviivalta maaliviivalle, jossa on "
            "ruutulippu. Pöydän reunassa on mittanauha, jonka asteikko on metreinä, ja lähtöviivan ja maaliviivan väli on muutettava "
            "muuttuja, matka s. Sekuntikello mittaa aikaa t, joka on mitattava muuttuja. Vakioina pysyvät auto, alusta ja paristot. "
            "Asteikko on mittakaavassa: 150 yksikköä kuvassa vastaa metriä.")
    # key of the three kinds of variable, two AA cells after "paristot"
    f.tex(24, 28, r"\text{muutettava: } s", "start")
    f.tex(24, 62, r"\text{mitattava: } t", "start")
    f.tex(24, 96, r"\text{vakiona: auto, alusta, paristot}", "start", w=420)
    for k in range(2):
        bx = 412 + 34 * k
        f.rect(bx, 88, 28, 15, "#2b3138", "#1f2933", 1, 3); f.rect(bx + 18, 88, 10, 15, "#fab005", S.dark("#fab005", 0.4), 1, 2)
        f.rect(bx + 28, 92, 3, 7, "#adb5bd", rx=1)
    H.stopwatch(f, 536, 72, 30, 0.12)
    f.tex(536, 132, "t", "middle")
    # table: top board with a tape measure on its front edge (150 units per metre, 0 at x = 72), two legs
    x0, per, yt = 72, 150, 240
    tw = "#c9935a"
    for lx in (38, 556): f.rect(lx, yt + 30, 16, 120, S.dark(tw, 0.15), S.dark(tw, 0.45), S.W_OBJ)
    f.rect(30, yt, 540, 30, tw, S.dark(tw, 0.45), S.W_OBJ, 3)
    f.rect(30, yt, 540, 5, S.light(tw, 0.3))
    f.rect(44, yt + 10, 512, 15, "#ffe066", S.dark("#ffe066", 0.45), S.W_DETAIL, 2)
    for k in range(26):
        x = x0 + per * 0.1 * k
        if x > 552: break
        f.line(x, yt + 10, x, yt + (25 if k % 5 == 0 else 17), "#3a4350", S.W_DETAIL if k % 5 else 1.5)
    for k in range(6):
        f.tex(x0 + per * 0.5 * k, yt + 52, fi(0.5 * k), "middle")
    f.tex(x0 + per * 2.5 + 28, yt + 52, r"s\ (\text{m})", "start")
    # start and finish: tape marks on the table, a chequered flag at the finish
    xe = x0 + per * 2.0
    for x in (x0, xe): f.rect(x - 3, yt - 3, 6, 6, "#1971c2", rx=1)
    f.line(xe, yt - 2, xe, yt - 60, "#5c6670", 2.5, cap="round")
    for i in range(4):
        for j in range(2):
            f.rect(xe + 1 + 8 * i, yt - 60 + 8 * j, 8, 8, "#2b3138" if (i + j) % 2 else WHITE)
    f.rect(xe + 1, yt - 60, 32, 16, "none", "#2b3138", 1)
    f.tex(x0 + 4, yt - 102, r"\text{lähtö}", "middle")
    f.tex(xe + 4, yt - 80, r"\text{maali}", "middle")
    _toy_car(f, x0 + 8, yt - 2)
    f.arrow(204, yt - 46, 270, yt - 46, COLD, 3, 14)                 # velocity is always blue
    f.tex(284, yt - 46, "v", "start", color=COLD)
    f.dim_h(x0, xe, yt + 92, r"s = 2{,}00\,\text{m}", MUTED)          # neutral grey: blue is kept for the velocity
    return f.svg()


def epavarmuus():
    f = Fig("fy18-eps", 340, "Kuvaaja suhteellisesta epävarmuudesta ajan funktiona, kun ajan epävarmuus on 0,2 s: "
            "kun aika on 1 s, epävarmuus on 20 %, kun aika on 4 s, se on 5,0 %, ja kun aika on 10 s, se on 2,0 %. "
            "Vihreä alue kuvaa mittauksia, joiden epävarmuus on enintään 5,0 %: ne vaativat vähintään 4 s:n ajan. "
            "Kuvaaja on mittakaavassa.")
    ax = Axes(f, (96, 286), (496, 54), x=(0, 10), y=(0, 24), xticks=[2, 4, 6, 8, 10], yticks=[5, 10, 15, 20],
              xlabel=r"t\ (\text{s})", ylabel=r"\varepsilon\ (\%)")
    ax.area([(4, 0), (10, 0), (10, 5), (4, 5)], GOOD_LIGHT, 0.7)
    f.line(ax.X(0), ax.Y(5), ax.X(10), ax.Y(5), GOOD, 2, "8 6")
    ax.curve(lambda t: 0.2 / t * 100, 1, 10, COLD, 3)
    ax.guide(4, 5)
    ax.point(4, 5, COLD)
    f.tex(ax.X(5.2), ax.Y(8.6), r"\varepsilon \le 5\,\%", "start", color=GOOD)
    f.tex(ax.X(2.2), ax.Y(19), r"\varepsilon = \dfrac{0{,}2\,\text{s}}{t}", "start", color=COLD, w=180)
    return f.svg()


def _ramp(f, gid):
    """A wooden ramp on a book stack, sloping down to the right; returns (x, y) of its top end and the slope."""
    H.wood(f, 0, 300, 600, 60, gid + "-top")
    for k, (w_, c) in enumerate(((150, "#2f74b5"), (140, "#c92a2a"), (146, "#2b8a3e"))):     # books under the top end
        f.rect(40 + (150 - w_) / 2, 300 - 22 * (k + 1), w_, 22, c, S.dark(c, 0.35), S.W_OBJ, 2)
        f.rect(46 + (150 - w_) / 2, 300 - 22 * (k + 1) + 6, w_ - 12, 4, S.light(c, 0.5))
    wood = "#d9b26a"
    f.path("M60,228 L560,296 L560,304 L60,236 Z", S.dark(wood, 0.12), S.dark(wood, 0.4), S.W_OBJ)
    f.path("M60,218 L560,286 L560,296 L60,228 Z", wood, S.dark(wood, 0.4), S.W_OBJ)
    return (60, 218), (500 / 68)


def ramp_ball():
    """Task illustration (fy1-8-L1-01): a ball rolls down a ramp, a hand holds a stopwatch; no numbers."""
    f = S.scene("fy18-ramp", "Kuvitus: kuula vierii kirjapinon varaan nojaavaa puista rinnettä alas, ja haaleat välikuvat näyttävät sen aiemmat paikat. "
                "Oikealla ylhäällä on sekuntikello.")
    f.rect(0, 0, 600, 360, "#f3efe6")
    _ramp(f, "fy18r")
    for k, (x, op) in enumerate(((150, 0.25), (230, 0.45), (330, 1))):
        y = 218 + (x - 60) * 68 / 500 - 14
        if op < 1: f.add(f'<circle cx="{x}" cy="{n(y)}" r="14" fill="#9aa3ad" opacity="{op}"/>')
        else: f.ball("fy18r-ball", x, y, 14, "#aab4bf")
    H.stopwatch(f, 500, 110, 40, 0.0)
    return f.svg()


def two_balls_ramp():
    """Task illustration (fy1-8-L2-05): the same ramp is tried with two balls one at a time: the light ball waits behind a
    ruler at the start, the heavy ball waits its turn on the table; a finish line and a stopper at the bottom; no numbers."""
    f = S.scene("fy18-balls", "Kuvitus: puinen rinne nojaa kirjapinoon. Rinteen yläpäässä pystyssä olevan viivaimen takana odottaa kevyt "
                "oranssi muovipallo, ja rinteen alapäässä on sininen maaliviiva, pieni sininen lippu ja puinen pysäytin. Pöydällä rinteen vieressä odottaa "
                "vuoroaan raskas teräskuula. Oikealla ylhäällä on sekuntikello.")
    f.rect(0, 0, 600, 360, "#f3efe6")
    H.wood(f, 0, 300, 600, 60, "fy18b-top")
    for k, (w_, c) in enumerate(((150, "#2f74b5"), (140, "#c92a2a"), (146, "#2b8a3e"))):     # books under the top end
        f.rect(40 + (150 - w_) / 2, 300 - 22 * (k + 1), w_, 22, c, S.dark(c, 0.35), S.W_OBJ, 2)
        f.rect(46 + (150 - w_) / 2, 300 - 22 * (k + 1) + 6, w_ - 12, 4, S.light(c, 0.5))
    wood = "#d9b26a"                                                                       # a shorter, steeper ramp
    x1, ya, yb = 430, 214, 290
    def top(x): return ya + (x - 60) * (yb - ya) / (x1 - 60)
    f.path(f"M60,{ya + 10} L{x1},{yb + 10} L{x1},{yb + 14} L60,{ya + 14} Z", S.dark(wood, 0.12), S.dark(wood, 0.4), S.W_OBJ)
    f.path(f"M60,{ya} L{x1},{yb} L{x1},{yb + 10} L60,{ya + 10} Z", wood, S.dark(wood, 0.4), S.W_OBJ)
    f.rect(x1 + 2, 270, 22, 30, "#a87443", S.dark("#a87443", 0.4), S.W_OBJ, 2)              # stopper block
    xf = 392                                                                               # finish line: blue tape across the ramp
    f.path(f"M{xf - 4},{n(top(xf - 4))} L{xf + 4},{n(top(xf + 4))} L{xf + 4},{n(top(xf + 4) + 10)} L{xf - 4},{n(top(xf - 4) + 10)} Z", "#1971c2")
    f.line(xf, top(xf), xf, top(xf) - 44, "#5c6670", 2, cap="round")                       # a small flag marks the finish
    f.path(f"M{xf},{n(top(xf) - 44)} l22,7 l-22,7 Z", "#1971c2", S.dark("#1971c2", 0.35), 1)
    # the ruler held upright across the ramp as a start gate, the light ball behind it
    xg = 122
    f.rect(xg, top(xg) - 58, 8, 60, "#ffe066", S.dark("#ffe066", 0.45), S.W_DETAIL, 1.5)
    for k in range(1, 6): f.line(xg, top(xg) - 58 + 10 * k, xg + 4, top(xg) - 58 + 10 * k, "#3a4350", 1)
    f.ball("fy18b-light", xg - 15, top(xg - 15) - 14, 14, "#ff922b")
    # faint dashed path of the run to the finish line
    f.path(f"M{xg + 16},{n(top(xg + 16) - 14)} L{xf - 20},{n(top(xf - 20) - 14)}", stroke="#adb5bd", w=S.W_GUIDE, extra=f'stroke-dasharray="{S.GUIDE_DASH}"')
    # the heavy ball waiting its turn on the table, on a small ring so it does not roll
    f.add('<ellipse cx="530" cy="300" rx="24" ry="5" fill="#8a6a43" opacity="0.35"/>')
    f.ball("fy18b-heavy", 530, 281, 18, "#aab4bf")
    H.stopwatch(f, 520, 110, 40, 0.0)
    return f.svg()


FIGURES = {"hero": hero, "setup": setup, "epavarmuus": epavarmuus, "ramp-ball": ramp_ball, "two-balls-ramp": two_balls_ramp}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "ramp-ball": "safe: the situation only, a ball rolling down a ramp and a stopwatch; no numbers",
    "two-balls-ramp": "safe: the situation only, a light and a heavy ball at the start of one ramp; no numbers",
    "setup": "safe: the setup with its variables, no results",
    "epavarmuus": "reveals: the relative uncertainty for 1, 4 and 10 s",
}
