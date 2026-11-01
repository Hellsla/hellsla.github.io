"""Figures of the unit fy14-magnetic-confinement (scripts/figlib.py, herolib.py); `python3 scripts/units.py figures
fy14-magnetic-confinement` writes them into content/en/units/fy14-magnetic-confinement/unit.md. English, decimal point.
Colours follow the course rules: velocity blue #1971c2, force red #c92a2a, magnetic field green #2b8a3e with ⊗ where it
points into the page. The mirror figure uses the simulation's mirror ratio Bmax/B0 = 4 (loss cone 30°)."""
import math
import figlib
from figlib import (Fig, INK, MUTED, WHITE, RULE, RULE_LIGHT, GLASS, ALUMINIUM, METAL_EDGE, IRON, COLD, COLD_LIGHT,
                    HOT, HOT_LIGHT, HEAT, HEAT_LIGHT, GOOD, GOOD_LIGHT, PAPER, n)
import herolib as H

figlib.set_language({}, ".")

V_COL, F_COL, B_COL = "#1971c2", "#c92a2a", "#2b8a3e"
PLASMA, PLASMA_LIGHT = "#e64980", "#fcc2d7"
ION = "#c2255c"


def otimes(f, x, y, r=9, col=B_COL):
    """⊗: the magnetic field points into the page."""
    f.circle(x, y, r, WHITE, col, 2.2)
    d = r * 0.68
    f.line(x - d, y - d, x + d, y + d, col, 2.2); f.line(x - d, y + d, x + d, y - d, col, 2.2)


def hero():
    """Opening illustration: a ring of coils around a glowing plasma torus in a dark hall; green field lines run around
    the ring, and the bright track of one particle winds around one field line. No words."""
    f = H.hero("fy14mc-hero", "Illustration: a dark experimental hall seen from above at an angle. A large ring of orange "
               "coils surrounds a glowing pink ring of plasma. Thin green lines run round and round the ring, inside the coils, "
               "and a bright white track spirals tightly around one of the green lines as it follows the ring. Nothing "
               "touches the walls.")
    f.rect(0, 0, 1200, 600, H.grad(f, "fy14mc-h-bg", "#22303c", INK))
    f.rect(0, 480, 1200, 120, "#2d3a46")
    cx, cy, R, k, zk = 600, 280, 360, 0.40, 0.92     # ring centre, major radius, squash of the view, height scale
    P = lambda phi, dr=0.0, dz=0.0: (cx + (R + dr) * math.cos(phi), cy + k * (R + dr) * math.sin(phi) - zk * dz)
    poly = lambda pts: "M" + " L".join(f"{n(a)},{n(b)}" for a, b in pts)
    def ring(dr, dz, col, w, extra=""):
        f.path(poly([P(2 * math.pi * i / 160, dr, dz) for i in range(161)]), stroke=col, w=w, extra=extra)
    def coil(phi, a=78):
        f.path(poly([P(phi, a * math.cos(2 * math.pi * i / 48), a * math.sin(2 * math.pi * i / 48)) for i in range(49)]),
               stroke=HEAT, w=12, extra='stroke-opacity="0.95"')
    f.add(f'<ellipse cx="{cx}" cy="{cy + 170}" rx="{R + 100}" ry="{n(k * (R + 100))}" fill="{INK}" fill-opacity="0.5"/>')
    f.rect(cx - 120, cy - 230, 240, 460, "none")
    phis = [2 * math.pi * (j + 0.5) / 18 for j in range(18)]
    for phi in phis:
        if math.sin(phi) < 0: coil(phi)
    ring(0, 0, PLASMA, 110, extra='stroke-opacity="0.16" stroke-linecap="round"')
    ring(0, 0, PLASMA, 62, extra='stroke-opacity="0.35"')
    ring(0, 0, PLASMA, 26, extra='stroke-opacity="0.7"')
    ring(0, 0, PLASMA_LIGHT, 8)
    for dr, dz in ((-38, 20), (38, 22), (-30, -28), (36, -24)):
        ring(dr, dz, GOOD_LIGHT, 2.5, extra='stroke-dasharray="16 10"')
    pts = []
    for i in range(520):
        phi = math.radians(25 + 125 * i / 519)
        a = i * 0.42
        pts.append(P(phi, 38 + 13 * math.cos(a), 22 + 13 * math.sin(a)))
    f.path(poly(pts), stroke=WHITE, w=2.5, extra='stroke-linecap="round"')
    f.circle(pts[-1][0], pts[-1][1], 7, WHITE)
    for phi in phis:
        if math.sin(phi) >= 0: coil(phi)
    return f.svg()


def lorentz():
    """A positive particle in a uniform field into the page: the velocity is tangent, the magnetic force points to the
    centre, at two points of the circle."""
    f = Fig("fy14mc-lorentz", 380, "Diagram: a uniform magnetic field into the page, shown by a grid of green crossed circles. "
            "A positive particle moves anticlockwise on a circle of radius r. At the bottom of the circle its velocity arrow, blue, "
            "points to the right and the magnetic force arrow, red, points up to the centre. At the right-hand side of the circle the "
            "velocity points up and the force points left, again to the centre. The force is always perpendicular to the velocity.")
    cx, cy, r = 300, 200, 120
    for i in range(9):
        for j in range(6):
            x, y = 34 + i * 67, 36 + j * 62
            d = math.hypot(x - cx, y - cy)
            if d < r + 40 or (x < 200 and y < 110) or (cx < x < cx + 160 and y > cy + r - 40): continue
            otimes(f, x, y, 8)
    f.add(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{INK}" stroke-width="2.5" stroke-dasharray="8 7"/>')
    f.line(cx, cy, cx + r * math.cos(math.radians(-135)), cy + r * math.sin(math.radians(-135)), MUTED, 2)
    f.tex(cx - 44, cy - 28, "r", "end", bg=True)
    f.circle(cx, cy, 4, INK)
    # bottom point
    bx, by = cx, cy + r
    f.arrow(bx, by, bx + 104, by, V_COL, 4, 16); f.tex(bx + 108, by + 2, r"\overline{v}", "start", color=V_COL, bg=True)
    f.arrow(bx, by, bx, by - 80, F_COL, 4, 16); f.tex(bx + 10, by - 60, r"\overline{F}", "start", color=F_COL, bg=True)
    f.circle(bx, by, 11, ION, WHITE, 2); f.tex(bx, by, r"+", "middle", color=WHITE, size=20)
    # right point
    rx, ry = cx + r, cy
    f.arrow(rx, ry, rx, ry - 104, V_COL, 4, 16); f.tex(rx + 10, ry - 96, r"\overline{v}", "start", color=V_COL, bg=True)
    f.arrow(rx, ry, rx - 80, ry, F_COL, 4, 16); f.tex(rx - 60, ry + 26, r"\overline{F}", "middle", color=F_COL, bg=True)
    f.circle(rx, ry, 11, ION, WHITE, 2); f.tex(rx, ry, r"+", "middle", color=WHITE, size=20)
    # direction of motion
    a0, a1 = math.radians(200), math.radians(250)
    f.path(f"M{n(cx + (r + 22) * math.cos(a1))},{n(cy + (r + 22) * math.sin(a1))} A{r + 22},{r + 22} 0 0 0 {n(cx + (r + 22) * math.cos(a0))},{n(cy + (r + 22) * math.sin(a0))}", stroke=INK, w=2.5)
    ex, ey = cx + (r + 22) * math.cos(a0), cy + (r + 22) * math.sin(a0)
    f.path(f"M{n(ex - 9)},{n(ey - 12)} L{n(ex)},{n(ey + 4)} L{n(ex + 9)},{n(ey - 10)} Z", INK)
    f.rect(6, 8, 190, 88, WHITE, RULE, 2, 8)
    otimes(f, 28, 32, 9)
    f.tex(44, 32, r"\overline{B}\ \text{into}", "start", color=B_COL)
    f.tex(20, 70, r"\text{the page}", "start", color=B_COL)
    return f.svg()


def mirror():
    """Side view of a magnetic mirror: field lines converge at both ends (B up to 4 B0); a particle with a large pitch
    angle spirals and turns back; the velocity split into v_par and v_perp at one point."""
    f = Fig("fy14mc-mirror", 360, "Side view of a magnetic mirror. Green field lines run from left to right; they are spread "
            "out in the middle and squeezed together at both ends, where two coils make the field four times stronger. A particle "
            "path spirals around the axis, moving to the right, and turns back before the right-hand coil. In the middle, the "
            "particle's velocity arrow, blue, is split into a part along the field, v parallel, and a part across it, v perpendicular; "
            "the angle between the velocity and the field is the pitch angle theta.")
    L, xm, y0 = 250, 300, 180
    w = lambda x: 1 / math.sqrt(1 + 3 * min(1, ((x - xm) / L) ** 2))      # field-line spread ∝ 1/sqrt(B), B = B0 (1 + 3 (x/L)^2)
    for s in (-1, -0.55, 0.55, 1):
        pts = [(x, y0 + s * 112 * w(x)) for x in range(20, 581, 10)]
        f.path("M" + " L".join(f"{n(a)},{n(b)}" for a, b in pts), stroke=B_COL, w=2.5)
        f.arrow(pts[20][0], pts[20][1], pts[22][0], pts[22][1], B_COL, 2.5, 12)
    f.line(20, y0, 580, y0, B_COL, 2.5)
    f.arrow(110, y0, 130, y0, B_COL, 2.5, 12)
    f.tex(560, y0 - 20, r"\overline{B}", "end", color=B_COL, bg=True)
    for xc in (xm - L, xm + L):
        f.rect(xc - 14, y0 - 104, 28, 40, HEAT, INK, 2, 4)
        f.rect(xc - 14, y0 + 64, 28, 40, HEAT, INK, 2, 4)
    f.tex(xm - L, 40, r"B_{\max}", "middle")
    f.tex(xm + L, 40, r"B_{\max}", "middle")
    f.tex(xm, 40, r"B_0", "middle")
    # the helical path: its radius shrinks as 1/sqrt(B) and it turns back where B = B0 / sin^2(55°)
    xr = xm + L * math.sqrt((1 / math.sin(math.radians(55)) ** 2 - 1) / 3)
    x_start, N, turns = xm - 190, 400, 9
    pts = []
    for i in range(N + 1):
        t_ = i / N
        xc = x_start + (xr - x_start) * math.sin(t_ * math.pi / 2)      # slows down towards the turning point
        a = t_ * 2 * math.pi * turns
        pts.append((xc + 13 * math.sin(a), y0 + 46 * w(xc) * math.cos(a)))
    f.path("M" + " L".join(f"{n(a)},{n(b)}" for a, b in pts), stroke=INK, w=2, extra='stroke-opacity="0.75"')
    f.arrow(xr + 6, y0 - 70, xr - 34, y0 - 70, INK, 2.5, 12)
    f.tex(xr - 14, y0 - 92, r"\text{turns back}", "middle", bg=True)
    # velocity components at the middle
    px, py = pts[round(2 / turns * N)]
    th = math.radians(55); vl = 92
    f.arrow(px, py, px + vl * math.cos(th), py + vl * math.sin(th), V_COL, 4, 15)
    f.line(px, py, px + vl * math.cos(th), py, V_COL, 2.5, "7 5"); f.line(px + vl * math.cos(th), py, px + vl * math.cos(th), py + vl * math.sin(th) - 2, V_COL, 2.5, "7 5")
    f.circle(px, py, 8, ION, WHITE, 2)
    f.tex(px + vl * math.cos(th) + 10, py + vl * math.sin(th) - 6, r"\overline{v}", "start", color=V_COL, bg=True)
    f.tex(px + vl * math.cos(th) / 2, py - 18, r"v_{\parallel}", "middle", color=V_COL, bg=True)
    f.tex(px + vl * math.cos(th) + 10, py + vl * math.sin(th) / 2 - 4, r"v_{\perp}", "start", color=V_COL, bg=True)
    f.path(f"M{n(px + 34)},{n(py)} A34,34 0 0 1 {n(px + 34 * math.cos(th))},{n(py + 34 * math.sin(th))}", stroke=INK, w=2)
    f.tex(px - 6, py + 40, r"\theta", "end")
    f.tex(xm, 334, r"B_{\max} = 4B_0\text{: reflected if } \sin^2\theta \geq B_0 / B_{\max}", "middle")
    return f.svg()


def torus():
    """Why a ring: in a straight field the particles leave through the ends; bent into a torus, the field lines close."""
    f = Fig("fy14mc-torus", 300, "Two diagrams. Left: a straight tube with coils around it; green field lines run along it and "
            "out of both open ends, and particles spiralling along the field lines escape through the ends. Right: the same coils "
            "bent into a ring, seen from above; the green field lines go round and round and close on themselves, so there are no "
            "ends to escape through.")
    # straight
    for x in range(40, 260, 30):
        f.add(f'<ellipse cx="{x}" cy="150" rx="9" ry="66" fill="none" stroke="{HEAT}" stroke-width="6"/>')
    for dy in (-36, 0, 36):
        f.line(10, 150 + dy, 290, 150 + dy, B_COL, 2.5)
        f.arrow(150, 150 + dy, 170, 150 + dy, B_COL, 2.5, 11)
    for xs, sgn in ((268, 1), (32, -1)):
        pts = [(xs + sgn * i * 0.9, 150 - 18 + 10 * math.sin(i * 0.5)) for i in range(0, 34)]
        f.path("M" + " L".join(f"{n(a)},{n(b)}" for a, b in pts), stroke=INK, w=2)
        f.arrow(pts[-1][0], pts[-1][1], pts[-1][0] + sgn * 16, pts[-1][1], INK, 2.5, 11)
    f.tex(150, 272, r"\text{open ends: particles leak}", "middle")
    # torus
    cx, cy = 450, 140
    for j in range(12):
        phi = 2 * math.pi * j / 12
        x, y = cx + 92 * math.cos(phi), cy + 92 * math.sin(phi)
        f.add(f'<ellipse cx="{n(x)}" cy="{n(y)}" rx="8" ry="40" fill="none" stroke="{HEAT}" stroke-width="6" transform="rotate({n(math.degrees(phi) + 90)} {n(x)} {n(y)})"/>')
    for r in (70, 92, 114):
        f.add(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{B_COL}" stroke-width="2.5"/>')
        f.arrow(cx + r, cy - 4, cx + r, cy + 10, B_COL, 2.5, 11)
    f.tex(450, 272, r"\text{a ring: no ends}", "middle")
    return f.svg()


FIGURES = {"hero": hero, "lorentz": lorentz, "mirror": mirror, "torus": torus}
