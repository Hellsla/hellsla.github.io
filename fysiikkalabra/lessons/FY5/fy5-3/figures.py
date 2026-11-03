"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy5-3` writes them into lesson.md.
Velocity is blue (COLD, as in FY4), the path and the radius ink or muted; every arrow is a filled path."""
import math
from figlib import (Fig, INK, MUTED, WHITE, RULE, RULE_LIGHT, COLD, COLD_LIGHT, GLASS, ICE, ICE_EDGE, IRON, METAL_EDGE,
                    ALUMINIUM, GOOD, GOOD_LIGHT, SAND, SAND_LIGHT, SAND_DARK, GRAIN, n)
import herolib as H

V_LIGHT = ICE_EDGE            # an earlier velocity: a lighter blue than the current one


def pos(cx, cy, R, deg):
    """A point of a circle drawn on screen (y down); deg is the angle counterclockwise from the right."""
    a = math.radians(deg)
    return cx + R * math.cos(a), cy - R * math.sin(a)


def vdir(deg):
    """The direction of the velocity at that point for counterclockwise motion (screen coordinates)."""
    a = math.radians(deg)
    return -math.sin(a), -math.cos(a)


def arc(cx, cy, R, d0, d1, steps=40):
    pts = [pos(cx, cy, R, d0 + (d1 - d0) * k / steps) for k in range(steps + 1)]
    return "M" + " L".join(f"{n(x)},{n(y)}" for x, y in pts)


def hero():
    f = H.hero("fy53-hero", "Kuvitus: leikkikentän karuselli pyörii kesäpäivänä. Toinen lapsi seisoo karusellin reunalla, "
               "toinen lähellä keskitankoa. Kummankin kohdalla on sininen nuoli liikkeen suuntaan radan tangentin suuntaisesti; "
               "reunalla seisovan lapsen nuoli on kaksi kertaa niin pitkä kuin keskellä seisovan.")
    H.sky(f, "fy53h", bottom=600)
    H.sun(f, "fy53h", 1040, 110, r=50)
    H.cloud(f, 250, 110, 1.0); H.cloud(f, 760, 80, 0.8)
    H.hills(f, "fy53h", 330, [GOOD_LIGHT], amp=36, seed=3)
    f.rect(0, 380, 1200, 220, H.grad(f, "fy53h-grass", GOOD_LIGHT, GOOD, y1=380, y2=600))
    for x, h in ((80, 230), (170, 180), (1110, 240), (1030, 170)):
        H.birch(f, x, 420, h)
    # sand under the carousel
    f.add(f'<ellipse cx="600" cy="470" rx="420" ry="110" fill="{SAND_LIGHT}"/>')
    f.add(f'<ellipse cx="600" cy="470" rx="420" ry="110" fill="none" stroke="{SAND}" stroke-width="3"/>')
    cx, cy, rx, ry = 600, 440, 330, 92
    # the platform: side, top, a ring of plates
    f.add(f'<ellipse cx="{cx}" cy="{cy + 22}" rx="{rx}" ry="{ry}" fill="{METAL_EDGE}" stroke="{INK}" stroke-width="3"/>')
    f.rect(cx - rx, cy, 2 * rx, 22, METAL_EDGE)
    f.add(f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{ALUMINIUM}" stroke="{INK}" stroke-width="3"/>')
    f.add(f'<ellipse cx="{cx}" cy="{cy}" rx="{rx * 0.5:g}" ry="{ry * 0.5:g}" fill="none" stroke="{METAL_EDGE}" stroke-width="2.5"/>')
    for k in range(8):
        a = math.radians(22.5 + 45 * k)
        f.line(cx + 0.5 * rx * math.cos(a), cy + 0.5 * ry * math.sin(a), cx + rx * math.cos(a), cy + ry * math.sin(a), METAL_EDGE, 2.5)
    # the motion: light swooshes along the rim
    for d0, d1 in ((200, 250), (300, 350)):
        pts = [(cx + (rx + 26) * math.cos(math.radians(d)), cy + (ry + 14) * math.sin(math.radians(d))) for d in range(d0, d1 + 1, 5)]
        f.path("M" + " L".join(f"{n(x)},{n(y)}" for x, y in pts), stroke=WHITE, w=6, extra='stroke-linecap="round" stroke-opacity="0.85"')
    # the centre pole and the grab bars to the rim
    top = (cx, cy - 190)
    for k in range(6):
        a = math.radians(30 + 60 * k)
        rim = (cx + 0.92 * rx * math.cos(a), cy + 0.92 * ry * math.sin(a) - 70)
        f.line(top[0], top[1], rim[0], rim[1], IRON, 6, cap="round")
        f.line(rim[0], rim[1], rim[0], rim[1] + 70, IRON, 6, cap="round")
    f.rect(cx - 10, cy - 196, 20, 196, IRON, INK, 2.5, 4)
    f.circle(cx, cy - 196, 16, METAL_EDGE, INK, 2.5)
    # two children: one at the rim (front right), one near the pole (back left)
    rim_k = (cx + 0.82 * rx * math.cos(math.radians(50)), cy + 0.82 * ry * math.sin(math.radians(50)))
    in_k = (cx + 0.41 * rx * math.cos(math.radians(200)), cy + 0.41 * ry * math.sin(math.radians(200)))
    H.person(f, in_k[0], in_k[1], shirt=SAND_DARK, sc=0.46)
    H.person(f, rim_k[0], rim_k[1], shirt=GOOD, sc=0.52)
    # their velocities: tangent to the circle in the floor's perspective, the rim's twice as long
    for (px, py), deg, length in ((rim_k, 50, 190), (in_k, 200, 95)):
        tx, ty = -rx * math.sin(math.radians(deg)), ry * math.cos(math.radians(deg))
        L = math.hypot(tx, ty); ux, uy = tx / L, ty / L
        x0, y0 = px + 30 * ux, py - 80 + 30 * uy
        f.block_arrow(x0, y0, x0 + length * ux, y0 + length * uy, COLD, shaft=12, head=30, headlen=24)
    return f.svg()


def tangent():
    f = Fig("fy53-tan", 380, "Kaavakuva: kappale kiertää ympyrärataa vastapäivään. Neljässä kohdassa on piirretty sininen "
            "nopeusvektori: kaikki ovat yhtä pitkiä ja radan tangentin suuntaisia, kohtisuorassa keskipisteestä piirrettyä sädettä "
            "vastaan. Oikealla lukee, että nopeuksien suuruudet ovat yhtä suuret mutta vektorit erisuuret.")
    cx, cy, R, L = 172, 192, 120, 82
    f.path(arc(cx, cy, R, 0, 360, 90) + " Z", stroke=INK, w=2.5)
    f.circle(cx, cy, 5, INK)
    for k, deg in enumerate((0, 90, 180, 270)):
        x, y = pos(cx, cy, R, deg); ux, uy = vdir(deg)
        f.line(cx, cy, x, y, MUTED, 1.5, "6 5")
        f.arrow(x, y, x + L * ux, y + L * uy, COLD, 3.5, 16)
        f.circle(x, y, 9, INK)
        lx, ly = x + (L + 6) * ux, y + (L + 6) * uy
        label = rf"\overline{{v}}_{k + 1}"
        if deg == 0: f.tex(lx + 10, ly + 6, label, "start", COLD)
        elif deg == 90: f.tex(lx - 4, ly - 22, label, "end", COLD)
        elif deg == 180: f.tex(lx + 12, ly + 2, label, "start", COLD)
        else: f.tex(lx + 4, ly + 22, label, "start", COLD)
    # right angle between the radius and the velocity at the right-hand point
    x, y = pos(cx, cy, R, 0)
    f.path(f"M{n(x - 14)},{n(y)} V{n(y - 14)} H{n(x)}", stroke=INK, w=2)
    f.tex(cx + R / 2, cy + 20, "r", "middle")
    # the turning direction
    f.path(arc(cx, cy, R + 22, 30, 62, 12), stroke=MUTED, w=2.5)
    ex, ey = pos(cx, cy, R + 22, 62); ux, uy = vdir(62)
    f.path(f"M{n(ex + 12 * ux)},{n(ey + 12 * uy)} L{n(ex - 6 * uy - 2 * ux)},{n(ey + 6 * ux - 2 * uy)} L{n(ex + 6 * uy - 2 * ux)},{n(ey - 6 * ux - 2 * uy)} Z", MUTED)
    f.line(362, 40, 362, 340, RULE, 2, "6 6")
    f.tex(380, 150, r"v_1 = v_2 = v_3 = v_4", "start", w=206)
    f.tex(380, 222, r"\overline{v}_1 \neq \overline{v}_2", "start", w=120)
    return f.svg()


def release():
    f = Fig("fy53-rel", 340, "Kaavakuva: naruun sidottu kiekko kiertää tappia vastapäivään katkoviivalla piirrettyä ympyrärataa. "
            "Radan alimmassa kohdassa naru katkeaa, ja kiekko jatkaa suoraan oikealle radan tangentin suuntaan. Kiekon paikat "
            "on merkitty yhtä pitkin aikavälein: välit ovat yhtä pitkät, joten vauhti pysyy samana.")
    cx, cy, R = 168, 150, 110
    f.path(arc(cx, cy, R, -90, 270, 90), stroke=RULE, w=2.5, extra='stroke-dasharray="8 7"')
    f.circle(cx, cy, 8, IRON, INK, 2)
    # the broken string: a stub at the stake
    f.line(cx, cy, cx + 10, cy + 46, MUTED, 2.5)
    f.path(f"M{cx + 10},{cy + 46} l5,4 l-6,3", stroke=MUTED, w=2)
    y = cy + R
    # positions before the break on the circle, after it on the straight line, equal time steps
    for deg in (-150, -130, -110):
        x0, y0 = pos(cx, cy, R, deg); f.circle(x0, y0, 7, INK); f.add(f'<circle cx="{n(x0)}" cy="{n(y0)}" r="7" fill="{WHITE}" fill-opacity="0.55"/>')
    step = R * math.radians(20)
    xs = [cx + step * k for k in range(0, 9)]
    f.line(cx, y, 520, y, INK, 2, "5 6")
    for x in xs[:-1]:
        f.circle(x, y, 7, INK); f.add(f'<circle cx="{n(x)}" cy="{n(y)}" r="7" fill="{WHITE}" fill-opacity="0.55"/>')
    xe = xs[-1]
    f.circle(xe, y, 10, INK)
    f.arrow(xe + 14, y, xe + 14 + 74, y, COLD, 3.5, 16)
    f.tex(xe + 52, y - 26, r"\overline{v}", "middle", COLD)
    f.tex(cx, y + 30, r"\text{naru katkeaa}", "middle")
    f.tex(292, y + 30, r"\text{suoraan, tasaisesti}", "start")
    return f.svg()


def dv():
    f = Fig("fy53-dv", 340, "Kaavakuva: vasemmalla ympyräradan kaari ja kappaleen kaksi peräkkäistä paikkaa, joissa nopeudet "
            "ovat yhtä pitkät mutta eri suuntiin. Oikealla samat vektorit on siirretty alkamaan samasta pisteestä, ja musta nuoli "
            "ensimmäisen kärjestä toisen kärkeen on nopeuden muutos. Toinen nopeus on ensimmäinen nopeus plus nopeuden muutos.")
    cx, cy, R, L = 120, 300, 170, 116
    d1, d2 = 30, 75
    f.path(arc(cx, cy, R, 0, 110, 40), stroke=INK, w=2.5)
    f.circle(cx, cy, 5, INK)
    tips = []
    for deg, col, name in ((d1, V_LIGHT, r"\overline{v}_1"), (d2, COLD, r"\overline{v}_2")):
        x, y = pos(cx, cy, R, deg); ux, uy = vdir(deg)
        f.line(cx, cy, x, y, MUTED, 1.5, "6 5")
        f.arrow(x, y, x + L * ux, y + L * uy, col, 3.5, 16)
        f.circle(x, y, 8, INK)
        tips.append((ux, uy))
        if deg == d1: f.tex(x + L * ux + 12, y + L * uy - 4, name, "start", col)
        else: f.tex(x + L * ux - 10, y + L * uy + 8, name, "end", col)
    f.line(340, 30, 340, 320, RULE, 2, "6 6")
    ox, oy = 540, 262
    (u1x, u1y), (u2x, u2y) = tips
    a1 = (ox + L * u1x, oy + L * u1y); a2 = (ox + L * u2x, oy + L * u2y)
    f.arrow(ox, oy, *a1, V_LIGHT, 3.5, 16)
    f.arrow(ox, oy, *a2, COLD, 3.5, 16)
    f.arrow(*a1, *a2, INK, 3, 14)
    f.circle(ox, oy, 5, INK)
    f.tex(a1[0] + 8, a1[1] - 10, r"\overline{v}_1", "start", V_LIGHT)
    f.tex(a2[0] - 8, a2[1] + 16, r"\overline{v}_2", "end", COLD)
    mx, my = (a1[0] + a2[0]) / 2, (a1[1] + a2[1]) / 2
    f.tex(mx - 16, my - 16, r"\Delta\overline{v}", "end")
    f.tex(466, 312, r"\overline{v}_2 = \overline{v}_1 + \Delta\overline{v}", "middle", w=200)
    return f.svg()


def two_radii():
    f = Fig("fy53-rad", 380, "Kaavakuva ylhäältä: kaksi kohtaa A ja B ovat samalla säteellä pyörivässä karusellissa, A etäisyydellä "
            "r ja B etäisyydellä 2r keskipisteestä. Samassa ajassa kumpikin kiertyy yhtä suuren osan kierroksesta, mutta B:n "
            "kulkema kaari on kaksi kertaa niin pitkä, ja B:n sininen nopeusvektori on kaksi kertaa niin pitkä kuin A:n. "
            "Mittasuhteet ovat oikeat.")
    cx, cy, ra, rb, turn = 86, 326, 140, 280, 40
    f.path(arc(cx, cy, rb, 0, 90, 40), stroke=RULE, w=2, extra='stroke-dasharray="7 6"')
    f.path(arc(cx, cy, ra, 0, 90, 40), stroke=RULE, w=2, extra='stroke-dasharray="7 6"')
    f.line(cx, cy, cx + rb, cy, MUTED, 1.5)
    xb, yb = pos(cx, cy, rb, turn); f.line(cx, cy, xb, yb, MUTED, 1.5)
    f.path(arc(cx, cy, ra, 0, turn, 20), stroke=INK, w=4.5)
    f.path(arc(cx, cy, rb, 0, turn, 30), stroke=INK, w=4.5)
    f.circle(cx, cy, 6, INK)
    for r_, name in ((ra, r"\text{A}"), (rb, r"\text{B}")):
        f.circle(cx + r_, cy, 8, WHITE, INK, 2.5)
        f.tex(cx + r_ + 14, cy + 4, name, "start")
    f.tex(cx + ra / 2, cy + 22, "r", "middle")
    f.tex(cx + ra * 1.5, cy + 22, "r", "middle")
    for r_, length, name in ((ra, 52, r"\overline{v}_\text{A}"), (rb, 104, r"\overline{v}_\text{B}")):
        x, y = pos(cx, cy, r_, turn); ux, uy = vdir(turn)
        f.arrow(x, y, x + length * ux, y + length * uy, COLD, 3.5, 16)
        f.circle(x, y, 8, WHITE, INK, 2.5)
        f.tex(x + length * ux + 8, y + length * uy - 14, name, "start", COLD)
    xa, ya = pos(cx, cy, ra + 24, turn / 2); f.tex(xa, ya, r"s_\text{A}", "start")
    xs, ys = pos(cx, cy, rb + 22, turn / 2); f.tex(xs, ys, r"s_\text{B}", "start")
    f.tex(440, 120, r"\text{sama } T", "start", w=120)
    f.tex(440, 176, r"s_\text{B} = 2\,s_\text{A}", "start", w=130)
    f.tex(440, 232, r"v_\text{B} = 2\,v_\text{A}", "start", w=130, color=COLD)
    return f.svg()


# The prediction's options: a puck on a string circles a stake counterclockwise; the string breaks at the marked point.
def _option(fid, label, kind):
    f = Fig(fid, 420, label)
    cx, cy, R, deg = 190, 170, 120, -45
    f.path(arc(cx, cy, R, 0, 360, 90) + " Z", stroke=RULE, w=2.5, extra='stroke-dasharray="8 7"')
    f.circle(cx, cy, 8, IRON, INK, 2)
    px, py = pos(cx, cy, R, deg)
    f.line(cx, cy, cx + 0.45 * (px - cx), cy + 0.45 * (py - cy), MUTED, 2.5)
    # how the puck was moving before the break
    f.path(arc(cx, cy, R + 24, -120, -70, 14), stroke=MUTED, w=3)
    ex, ey = pos(cx, cy, R + 24, -70); ux, uy = vdir(-70)
    f.path(f"M{n(ex + 14 * ux)},{n(ey + 14 * uy)} L{n(ex - 7 * uy - 2 * ux)},{n(ey + 7 * ux - 2 * uy)} L{n(ex + 7 * uy - 2 * ux)},{n(ey - 7 * ux - 2 * uy)} Z", MUTED)
    if kind == "curve":
        pts = [pos(cx, cy, R, d) for d in range(-45, 61, 5)]
        d = "M" + " L".join(f"{n(x)},{n(y)}" for x, y in pts)
        end, (dx, dy) = pts[-1], vdir(60)
    else:
        dx, dy = {"tangent": vdir(deg), "radial": (math.cos(math.radians(45)), math.sin(math.radians(45))),
                  "between": (1.0, 0.0)}[kind]
        end = (px + 200 * dx, py + 200 * dy); d = f"M{n(px)},{n(py)} L{n(end[0])},{n(end[1])}"
    f.path(d, stroke=INK, w=3, extra='stroke-dasharray="9 7"')
    hx, hy = end
    f.path(f"M{n(hx + 18 * dx)},{n(hy + 18 * dy)} L{n(hx - 9 * dy)},{n(hy + 9 * dx)} L{n(hx + 9 * dy)},{n(hy - 9 * dx)} Z", INK)
    f.circle(px, py, 11, INK)
    f.circle(px, py, 18, "none", MUTED, 2.5)
    return f.svg()



def opt_tangent():
    return _option("fy53-ot", "Vaihtoehto: naru katkeaa merkityssä kohdassa, ja kiekko jatkaa suoraa reittiä, joka on radan tangentin "
                   "suuntainen eli kohtisuorassa narun suuntaa vastaan.", "tangent")


def opt_radial():
    return _option("fy53-or", "Vaihtoehto: naru katkeaa merkityssä kohdassa, ja kiekko jatkaa suoraa reittiä poispäin tapista narun "
                   "suuntaan.", "radial")


def opt_curve():
    return _option("fy53-oc", "Vaihtoehto: naru katkeaa merkityssä kohdassa, ja kiekko jatkaa vielä jonkin matkaa samaa ympyrärataa.",
                   "curve")


def opt_between():
    return _option("fy53-ob", "Vaihtoehto: naru katkeaa merkityssä kohdassa, ja kiekko jatkaa suoraa reittiä vinosti radan tangentin "
                   "ja narun suunnan välistä.", "between")


FIGURES = {"hero": hero, "tangent": tangent, "release": release, "dv": dv, "two-radii": two_radii,
           "opt-tangent": opt_tangent, "opt-radial": opt_radial, "opt-curve": opt_curve, "opt-between": opt_between}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "tangent": "reveals: velocity tangent to the circle, equal speeds, different vectors",
    "release": "reveals: after the string breaks the puck moves straight along the tangent",
    "dv": "reveals: the change of velocity between two moments of uniform circular motion",
    "two-radii": "reveals: twice the radius at the same period gives twice the speed",
    "opt-tangent": "safe: one option of a prediction (straight along the tangent), no verdict",
    "opt-radial": "safe: one option of a prediction (straight out along the string), no verdict",
    "opt-curve": "safe: one option of a prediction (keeps circling), no verdict",
    "opt-between": "safe: one option of a prediction (between tangent and string), no verdict",
}
