"""Figures of the unit fy14-plasma (scripts/figlib.py, herolib.py); `python3 scripts/units.py figures fy14-plasma`
writes them into content/en/units/fy14-plasma/unit.md. The unit is written in English, so the decimal sign is a point.
Every number drawn is computed here: the pressure p = (n_i + n_e) k T of the ITER-like plasma (n = 1.0e20 m^-3 of ions
and of electrons, T = 1.5e8 K), the Sun's core 2.65e16 Pa (Wikipedia, Solar core, 2026-11-01) and air 1.013e5 Pa."""
import math
import figlib
from figlib import (Fig, INK, MUTED, WHITE, RULE, RULE_LIGHT, GLASS, ALUMINIUM, METAL_EDGE, IRON, COLD, COLD_LIGHT,
                    HOT, HOT_LIGHT, HEAT, HEAT_LIGHT, GOOD, GOOD_LIGHT, PAPER, ICE, n)
import herolib as H

figlib.set_language({}, ".")

K_B = 1.380649e-23
N_ITER, T_ITER = 1.0e20, 1.5e8
P_ITER = 2 * N_ITER * K_B * T_ITER          # 4.14e5 Pa
P_SUN, P_AIR = 2.65e16, 1.01325e5
PLASMA, PLASMA_LIGHT = "#e64980", "#fcc2d7"   # the plasma colour of the course's reactors explorer
AURORA, AURORA_LIGHT = "#40c057", "#b2f2bb"


def _panel(f, pid, x, y, w, h):
    f.defs_add(f'<clipPath id="{pid}"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="22"/></clipPath>')
    f.add(f'<g clip-path="url(#{pid})">')


def _end_panel(f, x, y, w, h):
    f.add("</g>")
    f.rect(x, y, w, h, "none", INK, 4, 22)


def hero():
    """Opening illustration of the Why question: four windows side by side, each showing matter in the plasma state:
    the northern lights over a snowy Lapland fell, a lightning flash, the Sun, and the glowing plasma ring inside a
    cut-open fusion machine. No words; it does not show what causes any of them."""
    f = H.hero("fy14pl-hero", "Illustration: four rounded windows side by side on warm paper. First: green curtains of northern "
               "lights with red upper edges in a dark night sky above a snowy fell and dark spruces. Second: a bright, jagged "
               "lightning flash from a grey storm cloud to dark ground, with rain. Third: the glowing yellow-orange Sun in black "
               "space, with a looping prominence at its edge. Fourth: a dark hall with a cut-open ring-shaped steel vessel; inside "
               "it a thin pink ring of glowing plasma floats without touching the walls.")
    f.rect(0, 0, 1200, 600, PAPER)
    W, Hh, Y0, gap = 264, 470, 65, 24
    xs = [36 + k * (W + gap) for k in range(4)]
    # 1. northern lights over Lapland
    x = xs[0]; _panel(f, "fy14pl-p1", x, Y0, W, Hh)
    f.rect(x, Y0, W, Hh, H.grad(f, "fy14pl-night", "#0b1d3a", "#1f3b63"))
    for k in range(26):
        f.circle(x + 10 + H.rnd(k, 3) * (W - 20), Y0 + 10 + H.rnd(k + 40, 3) * 260, 1.2 + 1.4 * H.rnd(k + 80, 3), WHITE)
    f.defs_add(f'<linearGradient id="fy14pl-aur" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{HOT}" stop-opacity="0.55"/>'
               f'<stop offset="0.28" stop-color="{AURORA}" stop-opacity="0.85"/><stop offset="1" stop-color="{AURORA}" stop-opacity="0"/></linearGradient>')
    for k, (top, amp, ph) in enumerate(((90, 26, 0.0), (130, 34, 1.4), (170, 20, 2.6))):
        d = f"M{x - 10},{Y0 + top}"
        for i in range(1, 9):
            xx = x - 10 + i * (W + 20) / 8
            d += f" Q{n(xx - (W + 20) / 16)},{n(Y0 + top - amp * math.sin(i + ph))} {n(xx)},{n(Y0 + top + amp * 0.4 * math.cos(i * 1.7 + ph))}"
        d += f" L{x + W + 10},{Y0 + top + 170} L{x - 10},{Y0 + top + 170} Z"
        f.add(f'<path d="{d}" fill="url(#fy14pl-aur)" opacity="{0.9 - 0.2 * k:.2f}"/>')
    f.path(f"M{x},{Y0 + 360} Q{x + 80},{Y0 + 300} {x + 150},{Y0 + 340} Q{x + 210},{Y0 + 310} {x + W},{Y0 + 330} V{Y0 + Hh} H{x} Z", "#dfe9f3")
    f.path(f"M{x},{Y0 + 400} Q{x + 120},{Y0 + 370} {x + W},{Y0 + 395} V{Y0 + Hh} H{x} Z", WHITE)
    for k, (dx, hh) in enumerate(((22, 96), (54, 70), (200, 110), (236, 80), (120, 60))):
        H.spruce(f, x + dx, Y0 + 430, hh, "#1f4d2e")
    _end_panel(f, x, Y0, W, Hh)
    # 2. lightning
    x = xs[1]; _panel(f, "fy14pl-p2", x, Y0, W, Hh)
    f.rect(x, Y0, W, Hh, H.grad(f, "fy14pl-storm", "#495057", "#868e96"))
    for k in range(5):
        H.cloud(f, x + 30 + k * 55, Y0 + 70 + 18 * (k % 2), 0.9, "#343a40")
    for k in range(18):
        rx = x + 12 + H.rnd(k, 5) * (W - 24); ry = Y0 + 140 + H.rnd(k + 30, 5) * 260
        f.line(rx, ry, rx - 6, ry + 22, "#ced4da", 2, cap="round")
    bolt = [(x + 150, Y0 + 100), (x + 128, Y0 + 180), (x + 160, Y0 + 196), (x + 120, Y0 + 290), (x + 150, Y0 + 300), (x + 104, Y0 + 420)]
    d = "M" + " L".join(f"{n(a)},{n(b)}" for a, b in bolt)
    f.path(d, stroke=HEAT_LIGHT, w=22, extra='stroke-opacity="0.35" stroke-linecap="round"')
    f.path(d, stroke="#fff3bf", w=8, extra='stroke-linecap="round"')
    f.path(d, stroke=WHITE, w=3, extra='stroke-linecap="round"')
    f.path(f"M{x + 160},{Y0 + 196} L{x + 196},{Y0 + 250} L{x + 184},{Y0 + 262} L{x + 214},{Y0 + 320}", stroke="#fff3bf", w=4, extra='stroke-linecap="round"')
    f.rect(x, Y0 + 420, W, Hh - 420, "#2b2f33")
    _end_panel(f, x, Y0, W, Hh)
    # 3. the Sun
    x = xs[2]; _panel(f, "fy14pl-p3", x, Y0, W, Hh)
    f.rect(x, Y0, W, Hh, INK)
    for k in range(20):
        f.circle(x + 8 + H.rnd(k, 9) * (W - 16), Y0 + 8 + H.rnd(k + 50, 9) * (Hh - 16), 1 + 1.2 * H.rnd(k + 90, 9), WHITE)
    cx, cy, r = x + W / 2, Y0 + Hh / 2 + 10, 104
    f.add(f'<circle cx="{n(cx)}" cy="{n(cy)}" r="{r * 1.45:g}" fill="{HEAT_LIGHT}" fill-opacity="0.18"/>')
    f.defs_add(f'<radialGradient id="fy14pl-sun" cx="0.45" cy="0.42" r="0.65"><stop offset="0" stop-color="#fff3bf"/><stop offset="0.6" stop-color="{HEAT_LIGHT}"/><stop offset="1" stop-color="{HEAT}"/></radialGradient>')
    f.circle(cx, cy, r, "url(#fy14pl-sun)")
    for k in range(22):
        a = H.rnd(k, 11) * 2 * math.pi; rr = r * 0.85 * math.sqrt(H.rnd(k + 60, 11))
        f.add(f'<circle cx="{n(cx + rr * math.cos(a))}" cy="{n(cy + rr * math.sin(a))}" r="{4 + 4 * H.rnd(k + 7, 11):.1f}" fill="{HEAT}" fill-opacity="0.25"/>')
    f.path(f"M{n(cx + r * 0.62)},{n(cy - r * 0.79)} C{n(cx + r * 0.9)},{n(cy - r * 1.55)} {n(cx + r * 1.45)},{n(cy - r * 1.05)} {n(cx + r * 0.95)},{n(cy - r * 0.32)}",
           stroke=HEAT, w=9, extra='stroke-linecap="round" stroke-opacity="0.85"')
    _end_panel(f, x, Y0, W, Hh)
    # 4. a fusion machine: cut-open vessel with a plasma ring
    x = xs[3]; _panel(f, "fy14pl-p4", x, Y0, W, Hh)
    f.rect(x, Y0, W, Hh, H.grad(f, "fy14pl-hall", "#2d3a46", INK))
    cx, cy, RX, RY = x + W / 2, Y0 + 240, 104, 58
    def arc(a0, a1, rx, ry):
        pts = [(cx + rx * math.cos(a0 + (a1 - a0) * i / 40), cy + ry * math.sin(a0 + (a1 - a0) * i / 40)) for i in range(41)]
        return "M" + " L".join(f"{n(px)},{n(py)}" for px, py in pts)
    # back half of the vessel (the far side, upper arc) with its coils; the near half is cut away
    for k in range(7):
        a = math.pi * (1.08 + 0.84 * k / 6)
        f.add(f'<ellipse cx="{n(cx + RX * math.cos(a))}" cy="{n(cy + RY * math.sin(a))}" rx="13" ry="34" fill="none" stroke="{HEAT}" stroke-width="7"/>')
    f.path(arc(math.pi, 2 * math.pi, RX, RY), stroke=METAL_EDGE, w=40, extra='stroke-linecap="butt"')
    f.path(arc(math.pi, 2 * math.pi, RX, RY), stroke=ALUMINIUM, w=30, extra='stroke-linecap="butt"')
    f.path(arc(math.pi, 2 * math.pi, RX, RY), stroke="#3d4852", w=20, extra='stroke-linecap="butt"')
    # the cut faces of the vessel at both ends of the cut
    for sx in (-1, 1):
        f.rect(cx + sx * RX - 20, cy - 20, 40, 40, ALUMINIUM, INK, 2.5, 6)
        f.rect(cx + sx * RX - 11, cy - 11, 22, 22, "#3d4852", rx=4)
    # the plasma ring floating inside, without touching the walls
    f.add(f'<ellipse cx="{n(cx)}" cy="{n(cy)}" rx="{RX}" ry="{RY}" fill="none" stroke="{PLASMA}" stroke-width="16" stroke-opacity="0.3"/>')
    f.add(f'<ellipse cx="{n(cx)}" cy="{n(cy)}" rx="{RX}" ry="{RY}" fill="none" stroke="{PLASMA}" stroke-width="7"/>')
    f.add(f'<ellipse cx="{n(cx)}" cy="{n(cy)}" rx="{RX}" ry="{RY}" fill="none" stroke="{PLASMA_LIGHT}" stroke-width="2.5"/>')
    f.rect(cx - 70, Y0 + 360, 140, 24, IRON, INK, 2, 4)
    f.rect(cx - 12, cy + RY + 20, 24, Y0 + 360 - cy - RY - 20, IRON)
    f.rect(x, Y0 + 384, W, Hh - 384, "#3b4650")
    _end_panel(f, x, Y0, W, Hh)
    return f.svg()


def ionisation():
    """From gas to plasma: neutral atoms (a proton with its electron), then heating knocks electrons off, giving free
    ions and electrons that move independently."""
    f = Fig("fy14pl-ion", 330, "Diagram in three boxes from left to right, joined by arrows labelled heating. Left box, gas: "
            "six neutral hydrogen atoms, each a small red proton with a blue electron close to it. Middle box, ionisation: a fast "
            "particle hits an atom and its electron is knocked away; it takes at least 13.6 eV. Right box, plasma: red protons "
            "and blue electrons move separately in all directions; the numbers of positive and negative charges are equal.")
    boxes = ((10, r"\text{gas}"), (210, r"\text{ionisation}"), (410, r"\text{plasma}"))
    for x0, t in boxes:
        f.rect(x0, 40, 180, 220, "#fbfaf6", RULE, 2.5, 10)
        f.tex(x0 + 90, 22, t, "middle", size=24)
    for x0 in (190, 390):
        f.arrow(x0 + 2, 150, x0 + 18, 150, HEAT, 4, 12)
    f.tex(300, 296, r"\text{heating: faster collisions}", "middle", color=HEAT)
    atoms = ((50, 85), (130, 100), (70, 170), (150, 180), (100, 232), (40, 228))
    for ax, ay in atoms:
        f.circle(ax, ay, 9, HOT, WHITE, 2)
        f.circle(ax + 16, ay - 10, 5, COLD, WHITE, 1.5)
    # ionisation
    f.circle(270, 150, 9, HOT, WHITE, 2)
    f.circle(286, 140, 5, COLD, WHITE, 1.5)
    f.arrow(222, 205, 258, 165, INK, 2.5, 11)
    f.circle(220, 208, 7, HOT, WHITE, 2)
    f.arrow(292, 136, 352, 90, COLD, 3, 12)
    f.circle(356, 86, 5, COLD, WHITE, 1.5)
    f.tex(300, 232, r"\geq 13.6\ \text{eV}", "middle")
    # plasma
    pts = ((450, 80, 1, 0.4), (520, 95, -1, 0.7), (560, 150, 0.3, -1), (470, 160, 1, -0.6), (520, 215, -0.8, -0.8), (440, 230, 0.6, 1))
    for k, (px, py, dx, dy) in enumerate(pts):
        f.circle(px, py, 9, HOT, WHITE, 2)
        L = math.hypot(dx, dy)
        ex, ey = px + 28 * (-dy / L), py + 28 * (dx / L)
        f.circle(ex, ey, 5, COLD, WHITE, 1.5)
        f.arrow(ex, ey, ex + 26 * dy / L, ey - 26 * dx / L, COLD, 2, 8)
    return f.svg()


def pressure():
    """Pressure on a logarithmic scale: air, the ITER-like plasma core and the Sun's core (bars to scale in log10 p)."""
    f = Fig("fy14pl-pressure", 300, "Bar chart with a logarithmic scale of pressure in pascals, from 10 to the power 4 to 10 to "
            "the power 17. Air at sea level: 1.0 times 10 to the 5 pascals. The core of a fusion plasma like ITER's, at 150 million "
            "kelvins and 10 to the 20 particles per cubic metre: 4.1 times 10 to the 5 pascals, about four times air pressure. "
            "The centre of the Sun: 2.7 times 10 to the 16 pascals, about 60 billion times more than the fusion plasma.")
    x0, x1, lo, hi = 190, 560, 4, 17
    X = lambda lg: x0 + (lg - lo) / (hi - lo) * (x1 - x0)
    for e in range(lo, hi + 1):
        f.line(X(e), 30, X(e), 236, RULE_LIGHT, 1.5)
        if e % 4 == 0: f.tex(X(e), 256, rf"10^{{{e}}}", "middle")
    f.arrow(x0, 236, x1 + 26, 236, INK, 2.5, 13)
    f.tex(x1 + 26, 218, r"p\ (\text{Pa})", "end", bg=True)
    rows = ((r"\text{air}", P_AIR, COLD, r"1.0 \cdot 10^{5}\ \text{Pa}"), (r"\text{fusion plasma}", P_ITER, "#c2255c", r"4.1 \cdot 10^{5}\ \text{Pa}"),
            (r"\text{Sun's core}", P_SUN, HEAT, r"2.7 \cdot 10^{16}\ \text{Pa}"))
    for k, (name, p, col, val) in enumerate(rows):
        y = 58 + k * 64
        f.tex(x0 - 10, y, name, "end")
        f.rect(x0, y - 16, X(math.log10(p)) - x0, 32, col, rx=4)
        if math.log10(p) < 10: f.tex(X(math.log10(p)) + 8, y, val, "start")
        else: f.tex(X(math.log10(p)) - 8, y, val, "end", color=WHITE)
    return f.svg()


FIGURES = {"hero": hero, "ionisation": ionisation, "pressure": pressure}
