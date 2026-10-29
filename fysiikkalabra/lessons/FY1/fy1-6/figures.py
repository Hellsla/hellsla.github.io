"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy1-6` writes them into lesson.md."""
from figlib import (Fig, Axes, INK, MUTED, RULE_LIGHT, WHITE, COLD, HEAT, ALUMINIUM, IRON, METAL_EDGE, GOOD, fi)
from figlib import HEAT_LIGHT, SAND, n
import herolib as H
from figlib import COLD_LIGHT, HOT
from herolib import grad

G = 9.81


def hero():
    """The chapter's opening illustration: on the airless Moon a hammer and a feather fall side by side, level at every moment."""
    f = H.hero("fy16-hero", "Kuvitus: astronautti Kuun harmaalla pinnalla mustaa taivasta vasten, taustalla kuumoduuli ja taivaalla Maa. "
               "Astronautti on pudottanut vasaran ja höyhenen samaan aikaan; haaleat välikuvat näyttävät, että ne ovat joka hetki samalla "
               "korkeudella ja että niiden välimatkat kasvavat putoamisen aikana.")
    H.space(f, seed=6, count=80)
    H.earth(f, "fy16h", 1060, 110, 62)
    f.path("M0,440 Q600,380 1200,450 V600 H0 Z", grad(f, "fy16h-ground", ALUMINIUM, METAL_EDGE))
    f.path("M0,440 Q600,380 1200,450", stroke=WHITE, w=2, extra='stroke-opacity="0.5"')
    for cx, cy, rx in ((140, 520, 70), (860, 540, 60), (1080, 500, 46), (420, 570, 40)):
        f.add(f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{n(rx * 0.28)}" fill="{METAL_EDGE}" stroke="{ALUMINIUM}" stroke-width="3"/>')
        f.add(f'<ellipse cx="{cx}" cy="{n(cy - rx * 0.06)}" rx="{n(rx * 0.75)}" ry="{n(rx * 0.16)}" fill="{IRON}" fill-opacity="0.4"/>')
    # lunar module in the background: gold foil descent stage on four legs
    lx, ly = 900, 430
    for dx in (-70, 70): f.line(lx + dx * 0.6, ly - 40, lx + dx, ly + 10, METAL_EDGE, 4); f.add(f'<ellipse cx="{lx + dx}" cy="{ly + 12}" rx="12" ry="4" fill="{ALUMINIUM}" stroke="{INK}" stroke-width="2"/>')
    f.rect(lx - 50, ly - 70, 100, 40, grad(f, "fy16h-foil", HEAT_LIGHT, SAND, horizontal=True), INK, 2)
    f.path(f"M{lx - 40},{ly - 70} L{lx - 30},{ly - 112} H{lx + 34} L{lx + 44},{ly - 70} Z", ALUMINIUM, INK, 2)
    f.rect(lx - 10, ly - 104, 22, 18, IRON, INK, 2, 3)
    f.line(lx + 30, ly - 112, lx + 46, ly - 140, INK, 2); f.add(f'<ellipse cx="{lx + 48}" cy="{ly - 142}" rx="10" ry="4" fill="{WHITE}" stroke="{INK}" stroke-width="2"/>')
    # footprints
    for k, x in enumerate(range(180, 380, 40)): f.add(f'<ellipse cx="{x}" cy="{454 + (k % 2) * 14 - k * 3}" rx="12" ry="5" fill="{IRON}" fill-opacity="0.55"/>')
    # astronaut standing, the right arm out at shoulder height
    x, yf = 440, 470
    f.add(f'<ellipse cx="{x + 10}" cy="{yf + 4}" rx="70" ry="10" fill="{IRON}" fill-opacity="0.55"/>')
    f.rect(x - 78, yf - 290, 46, 120, ALUMINIUM, INK, 3, 10)
    for dx in (-36, 6):
        f.rect(x + dx, yf - 130, 30, 124, WHITE, INK, 3, 10)
        f.rect(x + dx - 4, yf - 22, 38, 22, ALUMINIUM, INK, 3, 6)
        f.line(x + dx + 2, yf - 80, x + dx + 28, yf - 80, ALUMINIUM, 3)
    f.rect(x - 52, yf - 300, 104, 180, WHITE, INK, 3, 26)
    f.rect(x - 52, yf - 150, 104, 20, ALUMINIUM, INK, 2, 6)
    f.rect(x - 24, yf - 250, 48, 34, COLD_LIGHT, INK, 2, 4)
    for k in range(3): f.circle(x - 12 + 12 * k, yf - 233, 4, (HOT, GOOD, COLD)[k])
    f.rect(x - 64, yf - 288, 20, 32, HOT, INK, 2, 3)          # the flag patch on the arm
    f.path(f"M{x - 46},{yf - 270} L{x - 22},{yf - 180}", stroke=INK, w=30, extra='stroke-linecap="round"')
    f.path(f"M{x - 46},{yf - 270} L{x - 22},{yf - 180}", stroke=WHITE, w=24, extra='stroke-linecap="round"')
    hx, hy = x + 150, yf - 282
    f.path(f"M{x + 40},{yf - 270} L{hx},{hy}", stroke=INK, w=30, extra='stroke-linecap="round"')
    f.path(f"M{x + 40},{yf - 270} L{hx},{hy}", stroke=WHITE, w=24, extra='stroke-linecap="round"')
    f.circle(hx + 6, hy, 15, ALUMINIUM, INK, 3)
    f.circle(x, yf - 340, 54, WHITE, INK, 3)
    f.rect(x - 36, yf - 368, 76, 50, grad(f, "fy16h-visor", HEAT_LIGHT, IRON), INK, 3, 22)
    f.path(f"M{x - 22},{yf - 358} q14,-6 26,0", stroke=WHITE, w=4, extra='stroke-linecap="round"')
    def hammer(cx, cy, op):
        return (f'<g transform="translate({n(cx)},{n(cy)}) scale(0.85)" opacity="{op}"><rect x="-5" y="-40" width="10" height="66" rx="4" fill="{SAND}" stroke="{INK}" stroke-width="2"/>'
                f'<rect x="-24" y="-54" width="48" height="20" rx="3" fill="{IRON}" stroke="{WHITE}" stroke-width="2"/></g>')
    def feather(cx, cy, op):
        return (f'<g transform="translate({n(cx)},{n(cy)}) rotate(-12) scale(0.85)" opacity="{op}"><path d="M0,34 Q-24,-8 0,-48 Q24,-8 0,34 Z" fill="{WHITE}" stroke="{INK}" stroke-width="2"/>'
                f'<path d="M0,44 L0,-44" stroke="{INK}" stroke-width="2"/>' + "".join(f'<path d="M0,{y} l{s * 16},-12" stroke="{ALUMINIUM}" stroke-width="1.5"/>' for y in (-24, -10, 4, 18) for s in (-1, 1)) + "</g>")
    for k, (y, op) in enumerate(((hy + 34, 0.3), (hy + 106, 0.55), (hy + 226, 1))):   # 24 t² below the hand at t = 1, 2, 3: the gaps grow (3 : 5)
        f.add(hammer(hx - 4, y, op)); f.add(feather(hx + 80, y, op))
    f.line(hx - 40, hy + 226, hx + 120, hy + 226, WHITE, 2, dash="8 6")
    return f.svg()


def _ball(f, gid, cx, cy, r, light, dark):
    """A shaded metal ball: radial gradient, outline, small highlight."""
    f.defs_add(f'<radialGradient id="{gid}" cx="35%" cy="30%" r="75%"><stop offset="0" stop-color="{light}"/><stop offset="1" stop-color="{dark}"/></radialGradient>')
    f.circle(cx, cy, r, f"url(#{gid})", INK, 2.5)
    f.circle(cx - r * 0.35, cy - r * 0.38, max(2, r * 0.18), WHITE, None)


def free_fall():
    f = Fig("fy16-fall", 400, "Kaavakuva mittakaavassa: pallo putoaa levosta ja sen paikat on piirretty hetkillä 0, 1, 2 ja 3 sekuntia. "
            "Pudotusmatkat ovat 0, 4,9, 20 ja 44 metriä, joten välit kasvavat. Pallon alla oleva nuoli näyttää nopeuden, ja sen pituus on "
            "verrannollinen nopeuteen: nopeus on 0, 9,81, 19,6 ja 29,4 metriä sekunnissa eli se kasvaa joka sekunti yhtä paljon.")
    y0, ppm, cx, k = 44, 6.2, 215, 1.8                      # first ball y, pixels per metre of fall, ball x, pixels per m/s of arrow
    f.tex(112, 14, r"t\ (\text{s})", "middle")
    for t in range(4):
        d = 0.5 * G * t * t
        y = y0 + ppm * d
        v = G * t
        f.line(150, y, cx - 14, y, MUTED, 1.5, "6 5")        # the level the ball has reached
        f.tex(112, y, fi(t), "middle")
        _ball(f, f"fy16-b{t}", cx, y, 11, ALUMINIUM, IRON)
        if t:
            f.arrow(cx, y + 14, cx, y + 14 + v * k, HEAT, 4, 12)
            f.tex(cx + 24, y + 14 + v * k / 2, rf"v = {fi(v, 2 if t == 1 else 1)}\,\text{{m/s}}", "start", HEAT)
        else:
            f.tex(cx + 24, y, r"v = 0", "start", HEAT)
    # scale bar: 10 m of fall
    f.line(556, 156, 556, 156 + ppm * 10, INK, 2.5)
    f.line(548, 156, 564, 156, INK, 2); f.line(548, 156 + ppm * 10, 564, 156 + ppm * 10, INK, 2)
    f.tex(556, 134, r"10\,\text{m}", "middle")
    return f.svg()


def vt_graph():
    f = Fig("fy16-graph", 340, "(t,v)-kuvaaja mittakaavassa: vapaasti putoavan kappaleen nopeus on suora, joka alkaa origosta. Pisteet ovat "
            "9,81 m/s hetkellä 1,0 s, 19,6 m/s hetkellä 2,0 s, 29,4 m/s hetkellä 3,0 s ja 39,2 m/s hetkellä 4,0 s. Hetkien 1,0 s ja 3,0 s "
            "välillä aika kasvaa 2,0 s ja nopeus 19,6 m/s, joten suoran kulmakerroin on 9,81 m/s², putoamiskiihtyvyys g.")
    ax = Axes(f, (96, 300), (500, 60), x=(0, 4), y=(0, 40), xticks=[1, 2, 3, 4], yticks=[10, 20, 30, 40],
              xlabel=r"t\ (\text{s})", ylabel=r"v\ (\text{m/s})")
    ax.line([(0, 0), (4, G * 4)], COLD, 3.5)
    # slope triangle between t = 1 s and t = 3 s
    p1, p2 = (1, G), (3, 3 * G)
    ax.line([p1, (p2[0], p1[1]), p2], MUTED, 2, "8 6")
    f.tex(ax.X(2), ax.Y(G) + 24, r"\Delta t = 2{,}0\,\text{s}", "middle", bg=True)
    f.tex(ax.X(3) + 12, ax.Y(2 * G), r"\Delta v = 19{,}6\,\text{m/s}", "start", bg=True)
    for t in (1, 2, 3, 4): ax.point(t, G * t, COLD)
    f.tex(ax.X(0.2), ax.Y(35), r"v = g\,t", "start", COLD)
    f.tex(ax.X(0.2), ax.Y(26), r"g = \dfrac{\Delta v}{\Delta t} = 9{,}81\,\text{m/s}^2", "start", INK, bg=True)
    return f.svg()


def same_fall():
    f = Fig("fy16-same", 320, "Kaavakuva: kaksi eri massaista palloa, 1 kg ja 5 kg, putoavat yhtä aikaa ilman ilmanvastusta. Pallot ovat jokaisella "
            "hetkellä, 0, 1 ja 2 sekuntia, samalla korkeudella ja niillä on sama nopeus: 0, 9,81 ja 19,6 metriä sekunnissa. Nopeusnuolet ovat yhtä pitkiä.")
    y0, ppm, k = 74, 8, 1.8
    xl, xr = 250, 400
    f.tex(112, 14, r"t\ (\text{s})", "middle")
    f.tex(xl, 22, r"1\,\text{kg}", "middle"); f.tex(xr, 22, r"5\,\text{kg}", "middle")
    for t in range(3):
        d = 0.5 * G * t * t
        y = y0 + ppm * d
        v = G * t
        f.line(xl + 14, y, xr - 20, y, MUTED, 1.5, "6 5")
        f.tex(112, y, fi(t), "middle")
        _ball(f, f"fy16-l{t}", xl, y, 10, ALUMINIUM, IRON)
        _ball(f, f"fy16-h{t}", xr, y, 16, ALUMINIUM, IRON)
        if t:
            f.arrow(xl, y + 13, xl, y + 13 + v * k, HEAT, 4, 12)
            f.arrow(xr, y + 19, xr, y + 19 + v * k, HEAT, 4, 12)
    f.tex(xr + 38, y0 + ppm * 0.5 * G * 4 + 40, r"\text{sama nopeus}", "start", HEAT)
    return f.svg()


def two_planets():
    """A task-only picture: the (t,v) lines of bodies dropped from rest on two planets without an atmosphere; no slope marked."""
    f = Fig("fy16-two", 340, "(t,v)-kuvaaja mittakaavassa: kaksi suoraa origosta, planeetan A ja planeetan B pinnalla levosta pudotetun kappaleen nopeus v ajan t funktiona. "
            "Ruudukon väli on 1 s ja 5 m/s. Planeetan A suora kulkee ruudukon risteyksen (5 s; 20 m/s) kautta ja planeetan B suora risteyksen (5 s; 40 m/s) kautta. "
            "Aika-akseli ulottuu 6 sekuntiin.")
    ax = Axes(f, (96, 300), (470, 60), x=(0, 6), y=(0, 40), xticks=[1, 2, 3, 4, 5, 6], yticks=[5, 10, 15, 20, 25, 30, 35, 40],
              xlabel=r"t\ (\text{s})", ylabel=r"v\ (\text{m/s})", yfmt=lambda v: fi(v) if v % 10 == 0 else "")
    ax.line([(0, 0), (6, 24)], COLD, 3.5)
    ax.line([(0, 0), (5, 40)], HEAT, 3.5)
    f.tex(ax.X(6) + 8, ax.Y(24), r"\text{A}", "start", COLD)
    f.tex(ax.X(5) + 8, ax.Y(40) - 14, r"\text{B}", "start", HEAT)
    return f.svg()


FIGURES = {"hero": hero, "free-fall": free_fall, "vt-graph": vt_graph, "same-fall": same_fall, "two-planets": two_planets}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "free-fall": "reveals: the fall distances and speeds at 0–3 s",
    "vt-graph": "reveals: the slope g = 9,81 m/s²",
    "same-fall": "reveals: equal speeds for 1 kg and 5 kg",
    "two-planets": "safe: two (t,v) lines from the origin, grid crossings to read, no slopes written (vt-graph is the lesson figure)",
}
