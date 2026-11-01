"""Figures of the unit fy14-fusion-reactions (scripts/figlib.py, herolib.py); `python3 scripts/units.py figures
fy14-fusion-reactions` writes them into content/en/units/fy14-fusion-reactions/unit.md. English: the decimal sign is a
point. The energies of the proton–proton chain are computed from the AME2020 atomic masses of the course's data file
(assets/units/fy14/data/nuclides.json); the Coulomb curve is U = k e² / r with k e² = 1.440 MeV·fm (CODATA)."""
import json, math, pathlib
import figlib
from figlib import Fig, Axes, INK, MUTED, WHITE, RULE, RULE_LIGHT, HOT, HOT_LIGHT, HEAT, HEAT_LIGHT, COLD, COLD_LIGHT, GOOD, GOOD_LIGHT, METAL_EDGE, ALUMINIUM, IRON, n
import herolib as H

figlib.set_language({}, ".")

DATA = json.loads((pathlib.Path(__file__).resolve().parents[3] / "assets/units/fy14/data/nuclides.json").read_text())
BY = {x["id"]: x["mass_u"] for x in DATA["nuclides"]}
U = DATA["constants"]["u_MeV"]
Q1 = (2 * BY["H-1"] - BY["H-2"]) * U                       # 1.442 MeV, positron annihilation included
Q2 = (BY["H-2"] + BY["H-1"] - BY["He-3"]) * U              # 5.493 MeV
Q3 = (2 * BY["He-3"] - BY["He-4"] - 2 * BY["H-1"]) * U     # 12.860 MeV
KE2 = 8.9875517923e9 * 1.602176634e-19 / 1e-15 / 1e6       # k e^2 in MeV·fm, 1.440


def nucleon_defs(f, pre):
    for k, a, b, c in (("p", "#ff8a80", "#c92a2a", "#7f1d1d"), ("n", "#e9ecef", "#9aa1a9", "#4b5259")):
        f.defs_add(f'<radialGradient id="{pre}-{k}" cx="35%" cy="32%" r="70%"><stop offset="0%" stop-color="{a}"/>'
                   f'<stop offset="55%" stop-color="{b}"/><stop offset="100%" stop-color="{c}"/></radialGradient>')


def nucleon(f, pre, x, y, r, kind, plus=True):
    f.add(f'<circle cx="{n(x)}" cy="{n(y)}" r="{r:g}" fill="url(#{pre}-{kind})" stroke="{INK}" stroke-width="1.2"/>')
    if kind == "p" and plus and r >= 8:
        w = r * 0.45
        f.line(x - w, y, x + w, y, WHITE, max(1.5, r * 0.16), cap="round")
        f.line(x, y - w, x, y + w, WHITE, max(1.5, r * 0.16), cap="round")


def hero():
    """The Why question: on the left a part of the Sun's glowing core, dense with particles; on the right a tokamak cut
    open, with a thin pink plasma ring inside its coils. No words, no numbers."""
    f = H.hero("fy14fr-hero", "Illustration in two halves. Left: a close view of the Sun's core, a deep orange glow packed with many "
               "small particles close together. Right: a doughnut-shaped fusion machine cut open, with grey magnet coils around a "
               "vacuum chamber; inside it floats a thin ring of faint pink glowing gas, with only a few particles far apart.")
    f.defs_add(f'<radialGradient id="fy14fr-h-sun" cx="20%" cy="50%" r="75%"><stop offset="0" stop-color="#fff3bf"/><stop offset="0.35" stop-color="{HEAT_LIGHT}"/>'
               f'<stop offset="0.75" stop-color="{HEAT}"/><stop offset="1" stop-color="#a61e1e"/></radialGradient>')
    f.defs_add('<linearGradient id="fy14fr-h-lab" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2d3a46"/><stop offset="1" stop-color="#18212a"/></linearGradient>')
    f.defs_add('<radialGradient id="fy14fr-h-pl" cx="50%" cy="50%" r="50%"><stop offset="0.55" stop-color="#f783ac" stop-opacity="0"/><stop offset="0.8" stop-color="#f783ac" stop-opacity="0.75"/><stop offset="1" stop-color="#f783ac" stop-opacity="0"/></radialGradient>')
    f.rect(0, 0, 600, 600, "url(#fy14fr-h-sun)")
    for k in range(260):
        f.circle(H.rnd(k, 9) * 590 + 5, H.rnd(k + 900, 9) * 590 + 5, 3.2, "#fff4e6" if k % 3 else "#ffd8a8")
    f.rect(600, 0, 600, 600, "url(#fy14fr-h-lab)")
    f.line(600, 0, 600, 600, INK, 4)
    cx, cy = 900, 320
    # vacuum vessel: torus seen from above at an angle (two ellipses)
    f.add(f'<ellipse cx="{cx}" cy="{cy}" rx="250" ry="130" fill="{METAL_EDGE}" stroke="{INK}" stroke-width="3"/>')
    f.add(f'<ellipse cx="{cx}" cy="{cy}" rx="235" ry="118" fill="#3b4a58"/>')
    f.add(f'<ellipse cx="{cx}" cy="{cy}" rx="215" ry="102" fill="url(#fy14fr-h-pl)"/>')
    f.add(f'<ellipse cx="{cx}" cy="{cy}" rx="110" ry="46" fill="{METAL_EDGE}" stroke="{INK}" stroke-width="3"/>')
    f.add(f'<ellipse cx="{cx}" cy="{cy}" rx="70" ry="28" fill="{IRON}" stroke="{INK}" stroke-width="2"/>')
    # magnet coils (D-shaped rings seen edge-on as bands)
    for k in range(12):
        a = 2 * math.pi * k / 12
        x, y = cx + 245 * math.cos(a), cy + 124 * math.sin(a)
        f.rect(x - 11, y - 32, 22, 64, ALUMINIUM, INK, 2, 8)
    for k in range(18):
        a = 2 * math.pi * H.rnd(k, 11); r = 0.78 + 0.12 * H.rnd(k + 40, 11)
        f.circle(cx + 162 * r / 0.84 * math.cos(a), cy + 76 * r / 0.84 * math.sin(a), 3, "#ffdeeb")
    return f.svg()


def ppchain():
    """The three steps of the proton–proton chain, with the energy released in each (AME2020)."""
    f = Fig("fy14fr-ppchain", 420, size=26, label=f"The proton–proton chain in three numbered steps. Step 1, which happens twice: "
            f"two hydrogen-1 nuclei fuse into hydrogen-2 plus a positron and a neutrino, releasing {Q1:.2f} MeV including the "
            f"annihilation of the positron. Step 2, also twice: hydrogen-2 and hydrogen-1 fuse into helium-3 and a gamma-ray "
            f"photon, {Q2:.2f} MeV. Step 3: two helium-3 nuclei fuse into helium-4 and two protons, {Q3:.2f} MeV. "
            f"Total: four protons become one helium-4 nucleus, {2 * Q1 + 2 * Q2 + Q3:.1f} MeV.")
    nucleon_defs(f, "fy14fr-pp")
    rows = ((70, "1", r"{}^{1}_{1}\text{H} + {}^{1}_{1}\text{H} \to {}^{2}_{1}\text{H} + \text{e}^{+} + \nu", Q1, r"2 \cdot", [("p", 0, 0), ("n", 18, 0)]),
            (170, "2", r"{}^{2}_{1}\text{H} + {}^{1}_{1}\text{H} \to {}^{3}_{2}\text{He} + \gamma", Q2, r"2 \cdot", [("p", -9, 8), ("p", 9, 8), ("n", 0, -8)]),
            (270, "3", r"{}^{3}_{2}\text{He} + {}^{3}_{2}\text{He} \to {}^{4}_{2}\text{He} + 2\,{}^{1}_{1}\text{H}", Q3, "", [("p", -9, 8), ("n", 9, 8), ("p", 9, -8), ("n", -9, -8)]))
    for y, k, eq, q, times, icon in rows:
        f.circle(30, y, 18, COLD)
        f.tex(30, y, rf"\textbf{{{k}}}", "middle", color=WHITE, size=24)
        f.tex(62, y - 16, eq, "start")
        f.tex(62, y + 26, rf"Q = {q:.2f}\ \text{{MeV}}" + (r"\quad (\text{twice})" if times else ""), "start", color=HEAT)
        for kind, dx, dy in sorted(icon, key=lambda t: t[2]):
            nucleon(f, "fy14fr-pp", 548 + dx, y + 4 + dy, 11, kind)
        if k != "3":
            f.line(30, y + 22, 30, y + 78, RULE, 3)
    f.line(20, 330, 580, 330, RULE, 2)
    total = 2 * Q1 + 2 * Q2 + Q3
    f.tex(300, 366, rf"4\,{{}}^{{1}}_{{1}}\text{{H}} \to {{}}^{{4}}_{{2}}\text{{He}} + 2\,\text{{e}}^{{+}} + 2\nu", "middle")
    f.tex(300, 402, rf"\text{{total}}\ Q = {total:.1f}\ \text{{MeV}}", "middle", color=HEAT)
    return f.svg()


def barrier():
    """Potential energy of a deuteron and a triton against their distance: the Coulomb curve to scale outside 3 fm,
    the strong-force well inside (schematic), and tunnelling at 0.1 MeV."""
    r0 = 3.0
    f = Fig("fy14fr-barrier", 420, size=26, label=f"Graph of the potential energy U in MeV of two hydrogen nuclei against the distance r between "
            f"their centres in femtometres, from 0 to 20. Outside 3 fm the curve is the electric repulsion U = k e squared over r, "
            f"drawn to scale: it rises from about 0.07 MeV at 20 fm to {KE2 / r0:.2f} MeV at 3 fm. Inside 3 fm the curve drops "
            f"steeply into a deep well, the attraction of the strong force (schematic, not to scale). A horizontal line at 0.10 MeV "
            f"stands for a fast nucleus: classically it would turn back at about 14 fm, but a dashed arrow shows it tunnelling "
            f"through the barrier to the well.")
    ax = Axes(f, (70, 360), (470, 50), x=(0, 20), y=(0, 0.6), xticks=[5, 10, 15, 20], yticks=[0.2, 0.4, 0.6],
              xlabel=r"r\ (\text{fm})", ylabel=r"U\ (\text{MeV})", yfmt=lambda v: f"{v:.1f}")
    # strong-force well, schematic
    f.rect(ax.X(0) + 2, ax.Y(0) - 0.5, ax.X(r0 - 0.2) - ax.X(0) - 2, 22, GOOD_LIGHT, None)
    f.line(ax.X(r0), ax.Y(KE2 / r0), ax.X(r0 - 0.2), ax.Y(0) + 22, GOOD, 3)
    f.line(ax.X(0.2), ax.Y(0) + 22, ax.X(r0 - 0.2), ax.Y(0) + 22, GOOD, 3)
    f.tex(ax.X(r0) + 12, ax.Y(0) - 26, r"\text{strong force}", "start", color=GOOD, size=24, bg=True)
    ax.curve(lambda r: KE2 / r, r0, 20, HOT, 3.5)
    f.tex(ax.X(r0) + 8, ax.Y(KE2 / r0) - 4, rf"{KE2 / r0:.2f}\ \text{{MeV}}", "start", color=HOT, bg=True)
    f.tex(ax.X(9), ax.Y(0.30), r"U = \dfrac{ke^2}{r}", "start", color=HOT, bg=True)
    E = 0.10; rt = KE2 / E
    ax.line([(rt, E), (20, E)], COLD, 3)
    ax.point(rt, E, COLD)
    f.line(ax.X(rt), ax.Y(E), ax.X(r0) + 4, ax.Y(E), COLD, 3, "8 7")
    f.arrow(ax.X(r0 + 1.0), ax.Y(E), ax.X(r0) - 4, ax.Y(E), COLD, 3, 14)
    f.tex(ax.X(r0 + 1.6), ax.Y(E) - 24, r"\text{tunnelling}", "start", color=COLD, size=24, bg=True)
    f.tex(ax.X(20), ax.Y(E) + 26, r"\text{fast nucleus}", "end", color=COLD, size=24, bg=True)
    return f.svg()


FIGURES = {"hero": hero, "ppchain": ppchain, "barrier": barrier}
