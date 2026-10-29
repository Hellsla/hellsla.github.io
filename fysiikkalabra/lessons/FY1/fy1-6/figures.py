"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy1-6` writes them into lesson.md."""
from figlib import (Fig, Axes, INK, MUTED, RULE_LIGHT, WHITE, COLD, HEAT, ALUMINIUM, IRON, METAL_EDGE, GOOD, fi)
from figlib import HEAT_LIGHT, SAND, n
import herolib as H

G = 9.81


def hero():
    """The chapter's opening illustration: on the airless Moon a hammer and a feather fall side by side, level at every moment."""
    f = H.hero("fy16-hero", "Kuvitus: astronautti Kuun pinnalla mustaa taivasta vasten, Maa taivaalla. Astronautti on pudottanut vasaran ja höyhenen "
               "samaan aikaan; haaleat välikuvat näyttävät, että ne ovat joka hetki samalla korkeudella.")
    H.space(f, seed=6, count=60)
    H.earth(f, "fy16h", 1040, 120, 60)
    f.path("M0,470 Q300,440 600,462 T1200,452 V600 H0 Z", ALUMINIUM)
    for cx, cy, rx in ((180, 520, 60), (820, 540, 90), (1060, 500, 40), (460, 560, 34)):
        f.add(f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{n(rx * 0.25)}" fill="{METAL_EDGE}"/><ellipse cx="{cx}" cy="{n(cy - 3)}" rx="{n(rx * 0.8)}" ry="{n(rx * 0.17)}" fill="{IRON}" fill-opacity="0.35"/>')
    # astronaut: white suit, gold visor, arms out
    x, yf = 470, 470
    f.rect(x - 34, yf - 120, 28, 120, WHITE, INK, 3, 10); f.rect(x + 6, yf - 120, 28, 120, WHITE, INK, 3, 10)
    f.rect(x - 66, yf - 262, 30, 110, ALUMINIUM, INK, 3, 8)
    f.rect(x - 44, yf - 268, 88, 158, WHITE, INK, 3, 22)
    f.path(f"M{x + 40},{yf - 240} L{x + 128},{yf - 290}", stroke=INK, w=30, extra='stroke-linecap="round"')
    f.path(f"M{x + 40},{yf - 240} L{x + 128},{yf - 290}", stroke=WHITE, w=24, extra='stroke-linecap="round"')
    f.path(f"M{x - 40},{yf - 240} L{x - 20},{yf - 160}", stroke=INK, w=30, extra='stroke-linecap="round"')
    f.path(f"M{x - 40},{yf - 240} L{x - 20},{yf - 160}", stroke=WHITE, w=24, extra='stroke-linecap="round"')
    f.circle(x, yf - 310, 50, WHITE, INK, 3)
    f.add(f'<ellipse cx="{x + 12}" cy="{yf - 310}" rx="34" ry="28" fill="{HEAT_LIGHT}" stroke="{INK}" stroke-width="3"/>')
    f.rect(x - 22, yf - 210, 44, 30, ALUMINIUM, INK, 2, 4)
    def hammer(cx, cy, op):
        g = f'<g transform="translate({n(cx)},{n(cy)}) scale(0.85)" opacity="{op}"><rect x="-4" y="-40" width="8" height="64" rx="3" fill="{SAND}" stroke="{INK}" stroke-width="2"/>'
        return g + f'<rect x="-22" y="-52" width="44" height="18" rx="3" fill="{IRON}" stroke="{INK}" stroke-width="2"/></g>'
    def feather(cx, cy, op):
        return (f'<g transform="translate({n(cx)},{n(cy)}) rotate(-12) scale(0.85)" opacity="{op}"><path d="M0,30 Q-22,-8 0,-44 Q22,-8 0,30 Z" fill="{WHITE}" stroke="{INK}" stroke-width="2"/>'
                f'<path d="M0,40 L0,-40" stroke="{INK}" stroke-width="2"/></g>')
    for k, (y, op) in enumerate(((204, 0.3), (276, 0.55), (396, 1))):   # 24 t² below the hand at t = 1, 2, 3: the gaps grow (3 : 5)
        f.add(hammer(x + 160, y, op)); f.add(feather(x + 250, y, op))
    f.line(x + 110, 396, x + 290, 396, HEAT, 2, dash="8 6")
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
