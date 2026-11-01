"""Figures of the unit fy14-tokamak-stellarator (scripts/figlib.py, herolib.py); `python3 scripts/units.py figures
fy14-tokamak-stellarator` writes them into content/en/units/fy14-tokamak-stellarator/unit.md. English, decimal point.
The toroidal field figure uses ITER's toroidal field coils (18 coils of 134 turns at 68 kA, US ITER fact sheet 2026)
and B = mu0 N I / (2 pi R): 5.29 T at R = 6.2 m, 7.81 T at 4.2 m and 4.00 T at 8.2 m (plasma edges, a = 2.0 m)."""
import math
import figlib
from figlib import (Fig, INK, MUTED, WHITE, RULE, RULE_LIGHT, GLASS, ALUMINIUM, METAL_EDGE, IRON, COLD, COLD_LIGHT,
                    HOT, HOT_LIGHT, HEAT, HEAT_LIGHT, GOOD, GOOD_LIGHT, PAPER, COPPER, n)
import herolib as H

figlib.set_language({}, ".")

B_COL = "#2b8a3e"
PLASMA, PLASMA_LIGHT = "#e64980", "#fcc2d7"
MU0, N_TF, I_TF = 1.25663706127e-6, 18 * 134, 68e3
B_AT = lambda R: MU0 * N_TF * I_TF / (2 * math.pi * R)


def _poly(pts):
    return "M" + " L".join(f"{n(a)},{n(b)}" for a, b in pts)


def hero():
    """Opening illustration: two fusion machines side by side on dark ground, a tokamak with flat D-shaped coils around a
    smooth plasma ring, and a stellarator with twisted, tilted coils around a wavy plasma ring. No words."""
    f = H.hero("fy14ts-hero", "Illustration: two ring-shaped fusion machines side by side in a dark hall, seen from above at an "
               "angle. Left: a smooth pink plasma ring surrounded by evenly spaced, flat orange coils, with a copper column in "
               "the middle. Right: a pink plasma ring that waves up and down and in and out as it goes round, surrounded by "
               "orange coils that are tilted and bent to follow it. No words.")
    f.rect(0, 0, 1200, 600, H.grad(f, "fy14ts-h-bg", "#22303c", INK))
    f.rect(0, 430, 1200, 170, "#2a3642")
    k, zk = 0.55, 1.0
    def machine(cx, cy, R, stell):
        wob = (lambda phi: 14 * math.cos(5 * phi)) if stell else (lambda phi: 0.0)
        hz = (lambda phi: 12 * math.sin(5 * phi)) if stell else (lambda phi: 0.0)
        P = lambda phi, dr=0.0, dz=0.0: (cx + (R + wob(phi) + dr) * math.cos(phi),
                                         cy + k * (R + wob(phi) + dr) * math.sin(phi) - zk * (dz + hz(phi)))
        f.add(f'<ellipse cx="{cx}" cy="{n(cy + 118)}" rx="{R + 70}" ry="{n(k * (R + 70) * 0.6)}" fill="#1a232c"/>')
        a = 42
        def coil(phi):
            pts = []
            for i in range(61):
                t = 2 * math.pi * i / 60
                if stell:
                    dr, dz = a * math.cos(t) * (1 + 0.15 * math.cos(2 * t + 5 * phi)), a * 1.15 * math.sin(t)
                    ph = phi + 0.45 * math.sin(5 * phi + 1.0) * math.sin(t) * a / R
                else:
                    c = math.cos(t)
                    dr, dz = a * (c if c > -0.55 else -0.55), a * 1.45 * math.sin(t)
                    ph = phi
                pts.append(P(ph, dr, dz))
            f.path(_poly(pts) + " Z", stroke=HEAT, w=7, extra='stroke-linejoin="round"')
        nc = 15 if stell else 12
        phis = [2 * math.pi * (j + 0.5) / nc for j in range(nc)]
        if not stell:
            f.rect(cx - 20, cy - 110, 40, 150, COPPER, INK, 3, 6)
        for phi in phis:
            if math.sin(phi) < 0: coil(phi)
        ring = lambda col, w, extra="": f.path(_poly([P(2 * math.pi * i / 240) for i in range(241)]), stroke=col, w=w, extra=extra)
        ring(PLASMA, 64, 'stroke-opacity="0.14" stroke-linecap="round"')
        ring(PLASMA, 38, 'stroke-opacity="0.35"')
        ring(PLASMA, 16, 'stroke-opacity="0.75"')
        ring(PLASMA_LIGHT, 5)
        if not stell:
            f.rect(cx - 20, cy - 2, 40, 74, COPPER, INK, 3, 0)
        for phi in phis:
            if math.sin(phi) >= 0: coil(phi)
    machine(300, 270, 215, False)
    machine(900, 270, 215, True)
    return f.svg()


def toroidal():
    """Top view of a tokamak: the toroidal field coils are closer together on the inside, so B falls as 1/R."""
    f = Fig("fy14ts-toroidal", 420, "Top view of a tokamak drawn to scale with ITER's dimensions. Eighteen toroidal field coils, "
            "orange, stand around the ring like the spokes of a wheel; they are close together near the centre and far apart on the "
            "outside. The plasma, pink, is a ring between 4.2 m and 8.2 m from the central axis. Green field lines go round the ring. "
            "Labels give the field: 7.8 T at the inner edge of the plasma, 5.3 T at its centre line, R = 6.2 m, and 4.0 T at the "
            "outer edge.")
    cx, cy, s = 192, 210, 17.5           # px per metre
    f.add(f'<circle cx="{cx}" cy="{cy}" r="{n(8.2 * s)}" fill="{PLASMA_LIGHT}" fill-opacity="0.6"/>')
    f.add(f'<circle cx="{cx}" cy="{cy}" r="{n(4.2 * s)}" fill="{WHITE}"/>')
    for R in (4.2, 8.2):
        f.add(f'<circle cx="{cx}" cy="{cy}" r="{n(R * s)}" fill="none" stroke="{PLASMA}" stroke-width="2"/>')
    for j in range(18):
        a = 2 * math.pi * j / 18 + math.pi / 18
        r0, r1 = 2.6 * s, 10.2 * s
        f.line(cx + r0 * math.cos(a), cy + r0 * math.sin(a), cx + r1 * math.cos(a), cy + r1 * math.sin(a), HEAT, 9, cap="round")
    for R in (4.6, 6.2, 7.8):
        f.add(f'<circle cx="{cx}" cy="{cy}" r="{n(R * s)}" fill="none" stroke="{B_COL}" stroke-width="2.5" stroke-dasharray="10 6"/>')
        f.arrow(cx - 8, cy - R * s, cx + 14, cy - R * s, B_COL, 3, 14)
    f.circle(cx, cy, 2.2 * s, COPPER, INK, 2)
    f.line(cx, cy, cx + 8.2 * s, cy, INK, 1.5, "4 4")
    for R in (4.2, 6.2, 8.2):
        f.circle(cx + R * s, cy, 8, INK, WHITE, 2)
    # labels of the field at three radii, joined to the points on the radius
    rows = ((4.2, 70), (6.2, 196), (8.2, 322))
    for R, y in rows:
        f.line(cx + R * s, cy, 398, y + 4, MUTED, 1.5)
        f.tex(404, y, rf"R = {R:.1f}\ \text{{m}}", "start", size=27)
        f.tex(404, y + 36, rf"B = {B_AT(R):.1f}\ \text{{T}}", "start", color=B_COL, size=27)
    return f.svg()


FIGURES = {"hero": hero, "toroidal": toroidal}
