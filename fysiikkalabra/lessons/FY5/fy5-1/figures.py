"""Figures of fy5-1 (scripts/figlib.py); `python scripts/figures.py fy5-1` writes them into lesson.md.
Forces are red filled arrows (as in FY4), the line of action a dashed muted line, the arm r an ink dimension line with
a right-angle mark, the sense of rotation an ink curved arrow. Every label is LaTeX."""
import math
from figlib import (Fig, INK, MUTED, WHITE, RULE, RULE_LIGHT, SAND_LIGHT, SAND, GRAIN, ALUMINIUM, METAL_EDGE, IRON,
                    COLD, COLD_LIGHT, GLASS, PAPER, HOT, n)
import herolib as H
from herolib import grad

FORCE = HOT          # "#c92a2a": force red, the same as FY4's force diagrams


def P(o, ang, L):
    """The point at the distance L from o in the direction ang (degrees, counterclockwise from +x, y up)."""
    return (o[0] + L * math.cos(math.radians(ang)), o[1] - L * math.sin(math.radians(ang)))


def force(f, a, b, w=4, head=18):
    f.arrow(a[0], a[1], b[0], b[1], FORCE, w, head)


def dashed(f, a, b, color=MUTED, w=1.5):
    f.line(a[0], a[1], b[0], b[1], color, w, "7 6")


def turn(f, c, R, a0, a1, color=INK, w=2.5, head=13):
    """A curved arrow around c with the radius R from the angle a0 to a1 (degrees, ccw positive), head at a1."""
    x0, y0 = P(c, a0, R); x1, y1 = P(c, a1, R)
    ccw = a1 > a0
    big = 1 if abs(a1 - a0) > 180 else 0
    tip_back = 9 if ccw else -9                      # the shaft ends a little before the head
    xb, yb = P(c, a1 - tip_back, R)
    f.path(f"M{n(x0)},{n(y0)} A{R},{R} 0 {big} {0 if ccw else 1} {n(xb)},{n(yb)}", "none", color, w)
    t = math.radians(a1)
    tx, ty = (-math.sin(t), -math.cos(t)) if ccw else (math.sin(t), math.cos(t))   # screen tangent along the motion
    nx, ny = -ty, tx
    bx, by = x1 - tx * head, y1 - ty * head
    f.path(f"M{n(x1)},{n(y1)} L{n(bx + nx * head * 0.45)},{n(by + ny * head * 0.45)} L{n(bx - nx * head * 0.45)},{n(by - ny * head * 0.45)} Z", color)


def right_angle(f, at, u, v, s=12):
    """A right-angle mark at `at` between the screen directions u and v (unit vectors)."""
    a = (at[0] + u[0] * s, at[1] + u[1] * s); b = (a[0] + v[0] * s, a[1] + v[1] * s); c = (at[0] + v[0] * s, at[1] + v[1] * s)
    f.path(f"M{n(a[0])},{n(a[1])} L{n(b[0])},{n(b[1])} L{n(c[0])},{n(c[1])}", "none", INK, 1.5)


def nut(f, c, r=22, fill=IRON):
    pts = " ".join(f"{n(c[0] + r * math.cos(math.radians(30 + 60 * k)))},{n(c[1] + r * math.sin(math.radians(30 + 60 * k)))}" for k in range(6))
    f.add(f'<polygon points="{pts}" fill="{fill}" stroke="{INK}" stroke-width="2.5" stroke-linejoin="round"/>')
    f.circle(c[0], c[1], r * 0.42, METAL_EDGE, INK, 2)


def wrench(f, o, L, ang=0, w=20, gid=None):
    """A wrench seen from the front: a ring around the nut at o and a handle of length L in the direction ang."""
    e = P(o, ang, L)
    t = math.radians(ang); nx, ny = math.sin(t) * w / 2, math.cos(t) * w / 2
    fill = grad(f, gid, ALUMINIUM, METAL_EDGE) if gid else ALUMINIUM
    f.path(f"M{n(o[0] + nx)},{n(o[1] + ny)} L{n(e[0] + nx)},{n(e[1] + ny)} L{n(e[0] - nx)},{n(e[1] - ny)} L{n(o[0] - nx)},{n(o[1] - ny)} Z", fill, INK, 2.5)
    f.circle(e[0], e[1], w / 2, fill, INK, 2.5)
    f.circle(o[0], o[1], 32, fill, INK, 2.5)
    nut(f, o)


def door_hinge_view():
    """Ydinajatus: a door seen from above; three equal forces at the handle, near the hinge, and along the door."""
    f = Fig("fy51-ovi", 330, "Ovi ylhäältä katsottuna. Vasemmalla seinä ja sarana, josta ovi lähtee vaakasuorana lautana oikealle. "
            "Kolme yhtä pitkää punaista voimanuolta: F1 kahvan kohdalla kohtisuoraan ovea vastaan, F2 lähellä saranaa samoin kohtisuoraan "
            "ja F3 oven päässä oven suuntaisesti kohti saranaa. Katkoviivainen kaari näyttää, mihin suuntaan ovi aukeaa. Kaavakuva, ei mittakaavassa.")
    f.rect(24, 200, 40, 110, grad(f, "fy51-ovi-wall", RULE_LIGHT, RULE), INK, 2)
    for k in range(5): f.line(26, 214 + k * 20, 62, 204 + k * 20, MUTED, 1.2)
    f.tex(44, 182, r"\text{seinä}", "middle", MUTED)
    hinge = (84, 250)
    f.path(f"M{n(hinge[0] + 440)},{hinge[1]} A440,440 0 0 0 {n(hinge[0] + 440 * math.cos(math.radians(24)))},{n(hinge[1] - 440 * math.sin(math.radians(24)))}",
           "none", MUTED, 1.5, 'stroke-dasharray="7 6"')
    f.rect(hinge[0], 242, 440, 16, grad(f, "fy51-ovi-wood", SAND_LIGHT, SAND), GRAIN, 2.5, rx=2)
    f.circle(hinge[0], hinge[1], 11, IRON, INK, 2.5)
    f.tex(hinge[0] + 26, 290, r"\text{sarana}", "middle", MUTED)
    f.rect(452, 258, 26, 12, IRON, INK, 2, rx=3)
    f.tex(465, 290, r"\text{kahva}", "middle", MUTED)
    L = 92
    force(f, (465, 242), (465, 242 - L)); f.tex(448, 156, r"\overline{F}_1", "end", FORCE)
    force(f, (150, 242), (150, 242 - L)); f.tex(167, 156, r"\overline{F}_2", "start", FORCE)
    force(f, (524 + 6 + L, 250), (530, 250)); f.tex(570, 222, r"\overline{F}_3", "middle", FORCE)
    f.tex(300, 30, r"\text{ylhäältä katsottuna}", "middle", MUTED)
    return f.svg()


def varsi():
    """Ydinajatus: the arm. A wrench, the force at 60° to the handle, its dashed line of action and the arm r."""
    f = Fig("fy51-varsi", 340, "Kiintoavain mutterin ympärillä. Mutterin keskellä on kiertoakseli O. Avaimen varsi osoittaa vaakasuoraan oikealle, "
            "ja käsi vetää sitä kohdassa, joka on etäisyyden d päässä akselista. Voima F osoittaa vinosti ylös oikealle, 60 asteen kulmassa "
            "varren jatkeeseen nähden. Voiman vaikutussuora on piirretty katkoviivalla molempiin suuntiin. Akselista vaikutussuoralle "
            "piirretty kohtisuora jana on voiman varsi r, ja se on lyhyempi kuin d. Kaavakuva.")
    O, d, al = (118, 128), 280, 60
    Pp = (O[0] + d, O[1])
    s, c = math.sin(math.radians(al)), math.cos(math.radians(al))
    foot = (O[0] + d * s * s, O[1] + d * s * c)                     # the foot of the perpendicular from O, screen coordinates
    u = (c, -s)                                                      # the force's direction on the screen
    dashed(f, (foot[0] - u[0] * 40, foot[1] - u[1] * 40), (Pp[0] + u[0] * 190, Pp[1] + u[1] * 190))
    dashed(f, Pp, (Pp[0] + 70, Pp[1]))                               # the handle's extension: α is measured from it
    wrench(f, O, d + 6, 0, gid="fy51-varsi-steel")
    # the arm r
    f.line(O[0], O[1], foot[0], foot[1], INK, 2.5)
    right_angle(f, foot, (-u[0], -u[1]), (-(foot[0] - O[0]) / (d * s), -(foot[1] - O[1]) / (d * s)))
    f.circle(foot[0], foot[1], 3.5, INK)
    mid = ((O[0] + foot[0]) / 2, (O[1] + foot[1]) / 2)
    f.tex(mid[0] - 22, mid[1] + 18, "r", "middle")
    # d along the handle, above it
    f.line(O[0], O[1] - 46, Pp[0], Pp[1] - 46, INK, 1.5); f.line(O[0], O[1] - 54, O[0], O[1] - 38, INK, 1.5); f.line(Pp[0], Pp[1] - 54, Pp[0], Pp[1] - 38, INK, 1.5)
    f.tex((O[0] + Pp[0]) / 2, O[1] - 66, "d", "middle")
    # the force and the angle
    force(f, Pp, (Pp[0] + u[0] * 112, Pp[1] + u[1] * 112))
    f.tex(Pp[0] + u[0] * 112 + 24, Pp[1] + u[1] * 112 + 4, r"\overline{F}", "middle", FORCE)
    f.path(f"M{n(Pp[0] + 40)},{Pp[1]} A40,40 0 0 0 {n(Pp[0] + 40 * c)},{n(Pp[1] - 40 * s)}", "none", INK, 1.5)
    f.tex(Pp[0] + 60 * math.cos(math.radians(26)), Pp[1] - 60 * math.sin(math.radians(26)), r"\alpha", "middle")
    f.circle(Pp[0], Pp[1], 4, INK)
    f.tex(O[0] - 40, O[1] + 42, "O", "middle")
    f.tex(foot[0] + 70, foot[1] + 30, r"\text{vaikutussuora}", "middle", MUTED)
    return f.svg()


def suunta():
    """Kaava: the sign. A force turning a bar counterclockwise (M > 0) and one turning it clockwise (M < 0)."""
    f = Fig("fy51-suunta", 320, "Kaksi tilannetta vierekkäin. Kummassakin vaakasuora sauva on kiinni akselissa O vasemmasta päästään. "
            "Vasemmalla voima F vaikuttaa sauvan oikeaan päähän ylöspäin, ja kaarinuoli akselin ympärillä kiertää vastapäivään: "
            "momentti on positiivinen. Oikealla voima vaikuttaa sauvan päähän alaspäin, ja kaarinuoli kiertää myötäpäivään: momentti on negatiivinen.")
    f.line(300, 14, 300, 306, RULE, 1.5, "6 6")
    for x0, up, sense, sign in ((44, True, r"\text{vastapäivään}", r"M > 0"), (344, False, r"\text{myötäpäivään}", r"M < 0")):
        O = (x0 + 26, 166)
        L = 200
        e = (O[0] + L, O[1])
        f.rect(O[0], O[1] - 9, L, 18, grad(f, f"fy51-suunta-{x0}", SAND_LIGHT, SAND), GRAIN, 2.5, rx=4)
        f.circle(O[0], O[1], 10, IRON, INK, 2.5)
        tip = (e[0] - 12, O[1] - 96) if up else (e[0] - 12, O[1] + 96)
        force(f, (e[0] - 12, O[1] - 9 if up else O[1] + 9), tip)
        f.tex(tip[0] + 22, tip[1] + (12 if up else -12), r"\overline{F}", "middle", FORCE)
        if up: turn(f, O, 46, 20, 160)
        else: turn(f, O, 46, 160, 20)
        f.tex(O[0] - 4, 34, sense, "start", INK)
        f.tex(O[0] - 4, 290, sign, "start", INK)
        f.tex(O[0] - 26, O[1] + 34, "O", "middle")
    return f.svg()


def kulma():
    """Kaava: r = d sin α. The right triangle of the axis O, the point of application and the foot of the arm."""
    f = Fig("fy51-kulma", 340, "Suorakulmainen kolmio, jonka kärjet ovat kiertoakseli O, voiman otekohta ja akselista vaikutussuoralle piirretyn "
            "kohtisuoran kantapiste. Hypotenuusa on akselin ja otekohdan välinen etäisyys d. Kateetti akselista kantapisteeseen on voiman "
            "varsi r. Vaikutuskohdan kulma on alfa, sama kulma kuin voiman ja varren jatkeen välillä. Siksi r on d kertaa sini alfa.")
    O, d, al = (92, 104), 330, 40
    Pp = (O[0] + d, O[1])
    s, c = math.sin(math.radians(al)), math.cos(math.radians(al))
    foot = (O[0] + d * s * s, O[1] + d * s * c)
    u = (c, -s)
    f.path(f"M{n(O[0])},{n(O[1])} L{n(Pp[0])},{n(Pp[1])} L{n(foot[0])},{n(foot[1])} Z", GLASS)
    dashed(f, (foot[0] - u[0] * 36, foot[1] - u[1] * 36), (Pp[0] + u[0] * 120, Pp[1] + u[1] * 120))
    dashed(f, Pp, (Pp[0] + 64, Pp[1]))
    f.line(O[0], O[1], Pp[0], Pp[1], INK, 3)
    f.line(O[0], O[1], foot[0], foot[1], INK, 3)
    right_angle(f, foot, (-u[0], -u[1]), (-(foot[0] - O[0]) / (d * s), -(foot[1] - O[1]) / (d * s)), 14)
    force(f, Pp, (Pp[0] + u[0] * 100, Pp[1] + u[1] * 100))
    f.tex(Pp[0] + u[0] * 100 + 26, Pp[1] + u[1] * 100 + 16, r"\overline{F}", "middle", FORCE)
    f.circle(O[0], O[1], 7, IRON, INK, 2); f.circle(Pp[0], Pp[1], 4.5, INK)
    f.tex(O[0] - 26, O[1] + 4, "O", "middle")
    f.tex((O[0] + Pp[0]) / 2, O[1] - 22, "d", "middle")
    mid = ((O[0] + foot[0]) / 2, (O[1] + foot[1]) / 2)
    f.tex(mid[0] - 22, mid[1] + 16, "r", "middle")
    # the angle inside the triangle at P (between P→O and P→foot) and the equal one between the force and the extension
    f.path(f"M{n(Pp[0] - 44)},{Pp[1]} A44,44 0 0 0 {n(Pp[0] - 44 * c)},{n(Pp[1] + 44 * s)}", "none", INK, 1.5)
    f.tex(Pp[0] - 64 * math.cos(math.radians(20)), Pp[1] + 64 * math.sin(math.radians(20)), r"\alpha", "middle")
    f.path(f"M{n(Pp[0] + 38)},{Pp[1]} A38,38 0 0 0 {n(Pp[0] + 38 * c)},{n(Pp[1] - 38 * s)}", "none", INK, 1.5)
    f.tex(Pp[0] + 58 * math.cos(math.radians(20)), Pp[1] - 58 * math.sin(math.radians(20)), r"\alpha", "middle")
    f.tex(470, 286, r"r = d\sin\alpha", "middle", w=170)
    return f.svg()


def ruutu():
    """Exercise L1-04: an axis O and a bar to the point P (4 squares right, 3 up) on a grid of 0,10 m; a horizontal force at P."""
    f = Fig("fy51-ruutu", 360, "Ruudukko, jossa yksi ruutu vastaa 0,10 metriä. Kiertoakseli O on alhaalla vasemmalla. Akselista lähtee vino sauva "
            "kohtaan P, joka on neljä ruutua oikealla ja kolme ruutua ylempänä kuin O. Kohdassa P sauvaan vaikuttaa vaakasuora voima F "
            "vasemmalle. Voiman vaikutussuora on piirretty katkoviivalla.")
    sq = 48
    O = (156, 292)
    for i in range(-2, 9):
        f.line(O[0] + i * sq, 20, O[0] + i * sq, 340, RULE_LIGHT, 1.2)
    for j in range(-1, 6):
        f.line(O[0] - 2 * sq, O[1] - j * sq, O[0] + 8 * sq, O[1] - j * sq, RULE_LIGHT, 1.2)
    Pp = (O[0] + 4 * sq, O[1] - 3 * sq)
    dashed(f, (O[0] - 2 * sq, Pp[1]), (O[0] + 8 * sq, Pp[1]))
    t = math.atan2(-(Pp[1] - O[1]), Pp[0] - O[0]); nx, ny = math.sin(t) * 7, math.cos(t) * 7
    f.path(f"M{n(O[0] + nx)},{n(O[1] + ny)} L{n(Pp[0] + nx)},{n(Pp[1] + ny)} L{n(Pp[0] - nx)},{n(Pp[1] - ny)} L{n(O[0] - nx)},{n(O[1] - ny)} Z",
           grad(f, "fy51-ruutu-wood", SAND_LIGHT, SAND), GRAIN, 2)
    f.circle(O[0], O[1], 9, IRON, INK, 2.5)
    f.circle(Pp[0], Pp[1], 4.5, INK)
    force(f, Pp, (Pp[0] - 2 * sq, Pp[1]))
    f.tex(Pp[0] - 2 * sq + 4, Pp[1] - 24, r"\overline{F}", "middle", FORCE)
    f.tex(O[0] - 24, O[1] + 24, "O", "middle")
    f.tex(Pp[0] + 22, Pp[1] + 20, "P", "middle")
    f.rect(O[0] + 6 * sq, 318, sq, 4, INK); f.tex(O[0] + 7 * sq + 8, 320, r"0{,}10\,\text{m}", "start")
    return f.svg()


def hero():
    """The opening illustration: a car wheel; a long wrench on one wheel nut, pushed down at its far end; a short wrench on the floor."""
    f = H.hero("fy51-hero", "Kuvitus: autotalli. Auton takapyörän vanteessa on viisi pyöränmutteria. Yhteen mutteriin on asetettu pitkä "
               "ristiavain, jonka varsi ulottuu kauas vasemmalle, ja sen päätä painetaan alaspäin punaisella voimanuolella. Lattialla "
               "renkaan oikealla puolella on lyhyt kiintoavain.")
    f.rect(0, 0, 1200, 600, PAPER)
    for k in range(9): f.rect(0, 40 + k * 46, 1200, 2, RULE_LIGHT)
    f.rect(0, 470, 1200, 130, grad(f, "fy51h-floor", ALUMINIUM, METAL_EDGE))
    f.rect(0, 466, 1200, 6, RULE)
    # the car: a lower body panel with a wheel arch
    cx, cy = 770, 360
    f.path(f"M520,80 H1200 V330 H{cx + 205} A205,205 0 0 0 {cx - 205},330 H520 Q500,330 500,300 V110 Q500,80 520,80 Z", grad(f, "fy51h-car", COLD_LIGHT, COLD), INK, 3)
    f.path("M560,120 H1180", stroke=WHITE, w=4, extra='stroke-linecap="round" stroke-opacity="0.6"')
    f.rect(980, 170, 80, 18, IRON, INK, 2, rx=8)
    # the wheel: tyre, rim, five nuts
    f.circle(cx, cy, 182, INK)
    for k in range(24):
        a = math.radians(k * 15)
        f.line(cx + 168 * math.cos(a), cy + 168 * math.sin(a), cx + 180 * math.cos(a), cy + 180 * math.sin(a), IRON, 4)
    f.circle(cx, cy, 120, grad(f, "fy51h-rim", WHITE, ALUMINIUM), METAL_EDGE, 4)
    for k in range(5):
        a = math.radians(90 + k * 72 + 36)
        f.path(f"M{n(cx + 46 * math.cos(a - 0.3))},{n(cy + 46 * math.sin(a - 0.3))} L{n(cx + 108 * math.cos(a - 0.18))},{n(cy + 108 * math.sin(a - 0.18))} "
               f"L{n(cx + 108 * math.cos(a + 0.18))},{n(cy + 108 * math.sin(a + 0.18))} L{n(cx + 46 * math.cos(a + 0.3))},{n(cy + 46 * math.sin(a + 0.3))} Z", METAL_EDGE)
    f.circle(cx, cy, 34, ALUMINIUM, METAL_EDGE, 3)
    act = (cx - 64, cy)
    for k in range(5):
        a = math.radians(180 + k * 72)
        c = (cx + 64 * math.cos(a), cy + 64 * math.sin(a))
        if k: nut(f, c, 15)
    # the long wrench on the active nut, its handle to the left, pushed down at the far end
    wrench(f, act, 400, 180, w=22, gid="fy51h-steel")
    e = (act[0] - 392, act[1])
    f.rect(e[0] - 14, e[1] - 16, 90, 32, INK, INK, 2, rx=14)
    force(f, (e[0] + 30, e[1] - 150), (e[0] + 30, e[1] - 20), 7, 30)
    # the short wrench on the floor
    sw = (1010, 540)
    f.path(f"M{sw[0]},{sw[1] - 8} H{sw[0] + 130} V{sw[1] + 8} H{sw[0]} Z", ALUMINIUM, INK, 2.5)
    f.circle(sw[0], sw[1], 20, ALUMINIUM, INK, 2.5); f.circle(sw[0], sw[1], 9, METAL_EDGE, INK, 2)
    f.circle(sw[0] + 130, sw[1], 9, ALUMINIUM, INK, 2.5)
    return f.svg()


FIGURES = {"hero": hero, "ovi": door_hinge_view, "varsi": varsi, "suunta": suunta, "kulma": kulma, "ruutu": ruutu}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "hero": "decorative",
    "ovi": "safe: three equal forces on a door seen from above (at the handle, near the hinge, along the door), no moments given",
    "varsi": "reveals: the arm r of a force at 60° to a wrench's handle (a theory figure)",
    "suunta": "reveals: the sign convention, counterclockwise positive (a theory figure)",
    "kulma": "reveals: r = d sin α from the right triangle (a theory figure)",
    "ruutu": "safe: a bar from O to P (4 right, 3 up, 0,10 m squares) with a horizontal force at P; the arm is not drawn",
}
