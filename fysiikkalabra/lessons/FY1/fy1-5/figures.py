"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy1-5` writes them into lesson.md."""
from figlib import Fig, Axes, INK, MUTED, WHITE, RULE, RULE_LIGHT, COLD, COLD_LIGHT, HEAT, GLASS, IRON, n
from figlib import HEAT_LIGHT
import herolib as H
import math
from figlib import COPPER, METAL_EDGE, SAND, SAND_LIGHT, WATER, WATER_LIGHT
from herolib import grad


def hero():
    """The chapter's opening illustration: Voyager 2 far from the Sun, its earlier positions at equal time steps equally spaced on a straight line."""
    f = H.hero("fy15-hero", "Kuvitus: Aurinko ja planeettojen radat vasemmalla, Voyager 2 -luotain oikealla kaukana avaruudessa. Luotaimen takana "
               "suoralla jäljellä tasavälein merkkejä sen aiemmista paikoista yhtä pitkin aikavälein; seuraavat paikat jatkuvat eteenpäin katkoviivana.")
    H.space(f, seed=5, count=120)
    f.circle(70, 480, 200, H.glow(f, "fy15h-glow"))
    f.circle(70, 480, 70, grad(f, "fy15h-sun", HEAT_LIGHT, HEAT))
    for r in (140, 200, 300, 420):
        f.add(f'<ellipse cx="70" cy="480" rx="{r}" ry="{n(r * 0.32)}" fill="none" stroke="{METAL_EDGE}" stroke-width="1.5" stroke-dasharray="4 7"/>')
    H.planet(f, "fy15h-earth", 70 + 140, 480 - 12, 9, WATER_LIGHT, WATER)
    H.planet(f, "fy15h-jup", 70 + 300 * math.cos(-0.5), 480 + 96 * math.sin(-0.5), 24, SAND_LIGHT, COPPER, bands=4)
    H.planet(f, "fy15h-sat", 70 + 420 * math.cos(-0.25), 480 + 134 * math.sin(-0.25), 18, SAND_LIGHT, SAND, rings=True)
    x0, y0, x1, y1 = 170, 452, 1180, 110
    def at(t): return x0 + (x1 - x0) * t, y0 + (y1 - y0) * t
    f.line(*at(0), *at(0.7), WHITE, 2.5)
    f.line(*at(0.72), *at(1), WHITE, 2.5, dash="10 10")
    for k in range(8):
        x, y = at(0.07 + k * 0.08); f.circle(x, y, 10, COLD_LIGHT, WHITE, 2)
    for k in range(3):
        x, y = at(0.79 + k * 0.08); f.add(f'<circle cx="{n(x)}" cy="{n(y)}" r="10" fill="none" stroke="{WHITE}" stroke-width="2" stroke-dasharray="4 4"/>')
    H.probe(f, *at(0.71), 0.8)
    return f.svg()


def cart(f, cx, cy):
    """A small cart on the ground line y = cy: body, cabin and two wheels."""
    f.rect(cx - 28, cy - 36, 56, 22, COLD_LIGHT, INK, 2.5, 4)
    f.rect(cx - 13, cy - 52, 26, 16, GLASS, INK, 2.5, 3)
    for wx in (cx - 16, cx + 16):
        f.circle(wx, cy - 8, 8, INK)
        f.circle(wx, cy - 8, 3, WHITE)


def motion():
    f = Fig("fy15-motion", 330, "Liikekuva, jossa sama kärry on piirretty viiden peräkkäisen sekunnin kohdalle ruudulle 0 s, 1 s, 2 s, 3 s ja 4 s. "
            "Kärryjen välit ovat yhtä pitkät, ja jokaisen välin alla on yhtä pitkä sulku Δs: tasaisessa liikkeessä kappale kulkee yhtä pitkissä "
            "ajoissa yhtä pitkät matkat. Välit on piirretty mittakaavassa, kärryt ovat samankokoisia.")
    ground = 150
    f.line(24, ground, 576, ground, INK, 2.5)
    xs = [70 + 115 * i for i in range(5)]
    for i, x in enumerate(xs):
        cart(f, x, ground)
        f.line(x, ground, x, ground + 12, INK, 2)
        f.tex(x, ground + 36, r"t = 0\,\text{s}" if i == 0 else rf"{i}\,\text{{s}}", "middle", w=100 if i == 0 else 60)
    f.arrow(xs[0] + 6, 70, xs[0] + 66, 70, INK, 3, 14)
    f.tex(xs[0] + 36, 46, "v", "middle")
    for a, b in zip(xs, xs[1:]):
        f.path(f"M{a},{ground + 62} V{ground + 74} H{b} V{ground + 62}", stroke=MUTED, w=2.5)
        f.tex((a + b) / 2, ground + 100, r"\Delta s", "middle")
    f.tex(300, 316, r"\text{yhtä pitkissä ajoissa yhtä pitkät matkat}", "middle", w=440)
    return f.svg()


def graph():
    f = Fig("fy15-graph", 360, "Kuvaaja mittakaavassa: kaksi tasaista liikettä nopeudella 3 m/s esitetään (t, s)-koordinaatistossa suorina. "
            "Alempi suora kulkee origon kautta (alkupaikka 0), ylempi alkaa paikasta s₀ = 5 m ja on alemman suoran kanssa yhdensuuntainen. "
            "Alemmalle suoralle on piirretty kulmakolmio: 2 s:n aikana paikka kasvaa 6 m, joten kulmakerroin on 3 m/s eli nopeus.")
    ax = Axes(f, (96, 300), (440, 60), x=(0, 5), y=(0, 25), xticks=[1, 2, 3, 4, 5], yticks=[10, 20],
              xlabel=r"t\ (\text{s})", ylabel=r"s\ (\text{m})")
    ax.line([(0, 0), (5, 15)], COLD, 3)
    ax.line([(0, 5), (5, 20)], HEAT, 3)
    # the starting position of the upper line: a tick and ring on the s axis
    f.line(ax.X(0) - 7, ax.Y(5), ax.X(0), ax.Y(5), INK, 2)
    f.tex(ax.X(0) - 12, ax.Y(5), r"s_0", "end")
    ax.point(0, 5, HEAT)
    # slope triangle on the lower line between t = 2 s and t = 4 s, right angle below the line
    f.line(ax.X(2), ax.Y(6), ax.X(4), ax.Y(6), MUTED, 1.5, "6 5")
    f.line(ax.X(4), ax.Y(6), ax.X(4), ax.Y(12), MUTED, 1.5, "6 5")
    ax.point(2, 6, COLD); ax.point(4, 12, COLD)
    f.tex(ax.X(3), ax.Y(6) + 24, r"\Delta t = 2\,\text{s}", "middle", w=130)
    f.tex(ax.X(4) + 12, ax.Y(9), r"\Delta s = 6\,\text{m}", "start", w=130, bg=True)
    f.tex(ax.X(5) + 8, ax.Y(15), r"s = vt", "start", COLD, w=80)
    f.tex(ax.X(5) + 8, ax.Y(20), r"s = s_0 + vt", "start", HEAT, w=140)
    return f.svg()


def line_read():
    """A task-only variant of `graph`: one uniform motion as a straight line through the origin, no slope triangle, no
    values written on it; the student reads two grid crossings (scripts/figcat.py variant)."""
    f = Fig("fy15-line-read", 360, "Kuvaaja mittakaavassa: kävelijän paikka s ajan t funktiona, suora viiva origosta. Ruudukon väli on 1 s ja 5 m. "
            "Suora kulkee ruudukon risteyskohtien (2 s; 5 m), (4 s; 10 m), (6 s; 15 m), (8 s; 20 m) ja (10 s; 25 m) kautta.")
    ax = Axes(f, (96, 300), (470, 60), x=(0, 10), y=(0, 25), xticks=list(range(1, 11)), yticks=[5, 10, 15, 20, 25],
              xlabel=r"t\ (\text{s})", ylabel=r"s\ (\text{m})", xfmt=lambda v: str(int(v)) if v % 2 == 0 else "")
    ax.line([(0, 0), (10, 25)], COLD, 3)
    return f.svg()


FIGURES = {"hero": hero, "motion": motion, "graph": graph, "line-read": line_read}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "motion": "safe: equal spacing at equal times, no distances",
    "graph": "reveals: the slope 3 m/s of both lines and s0 = 5 m",
    "line-read": "safe: one straight line through the origin, grid crossings to read, no slope marked (graph is the lesson figure)",
}
