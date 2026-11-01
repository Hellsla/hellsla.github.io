"""Figures of the unit fy14-quantum-tunnelling (scripts/figlib.py, herolib.py); `python3 scripts/units.py figures
fy14-quantum-tunnelling` writes them into content/en/units/fy14-quantum-tunnelling/unit.md. English: decimal point.
The double-slit dots are drawn at random (fixed seed) from the two-slit intensity pattern; the Coulomb energy of two
protons is k e^2 / r with k e^2 = 1.440 MeV·fm; the Sun's core temperature is 15.7 million K (k_B T = 1.35 keV)."""
import math, random
import figlib
from figlib import (Fig, Axes, fi, INK, MUTED, WHITE, RULE, RULE_LIGHT, GLASS, ICE, COLD, COLD_LIGHT, HOT, HOT_LIGHT, HEAT,
                    HEAT_LIGHT, GOOD, GOOD_LIGHT, SAND, SAND_LIGHT, ALUMINIUM, METAL_EDGE, IRON, n)
import herolib as H

figlib.set_language({}, ".")

KE2 = 1.43996                     # k e^2 in MeV·fm
KT_KEV = 8.617333e-5 * 1.57e7 / 1e3   # k_B T at the Sun's centre, keV (1.35)


def hero():
    """The Sun rising over hills; in the sky a round magnifier shows two tiny protons approaching each other, each
    drawn as a soft blur rather than a hard ball. No text."""
    f = H.hero("fy14qt-hero", "Illustration: dawn over a dark, hilly landscape. A huge orange Sun is rising behind the hills and "
               "lights the sky in yellow and pink. High in the sky a round magnifying lens shows a dark close-up of the inside "
               "of the Sun: two tiny red particles move towards each other. Each particle is drawn as a bright centre inside "
               "soft, fading rings, as if it were not quite a solid ball.")
    f.rect(0, 0, 1200, 600, H.grad(f, "qt-sky", "#5c7cfa", "#ffd8a8"))
    f.add('<defs><radialGradient id="qt-sun" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="#fff3bf"/><stop offset="0.6" stop-color="#ffa94d"/><stop offset="1" stop-color="#e8590c"/></radialGradient>'
          '<radialGradient id="qt-halo" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="#ffe066" stop-opacity="0.7"/><stop offset="1" stop-color="#ffe066" stop-opacity="0"/></radialGradient>'
          '<radialGradient id="qt-p" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="#ff8787"/><stop offset="0.35" stop-color="#e03131" stop-opacity="0.75"/><stop offset="1" stop-color="#e03131" stop-opacity="0"/></radialGradient></defs>')
    f.add('<circle cx="760" cy="470" r="330" fill="url(#qt-halo)"/>')
    f.circle(760, 470, 190, "url(#qt-sun)")
    H.hills(f, "qt1", 430, ["#3b2f5c", "#2b2145"], amp=40, seed=3)
    H.hills(f, "qt2", 500, ["#231a38", "#181127"], amp=30, seed=8)
    # the magnifier: a lens with a dark close-up and two blurred protons
    cx, cy, r = 300, 210, 140
    f.circle(cx, cy, r + 14, "#495057", INK, 3)
    f.circle(cx, cy, r, "#2b1d0e")
    f.add(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#e8590c" fill-opacity="0.25"/>')
    for k in range(40):
        x = cx + (H.rnd(k, 5) - 0.5) * 1.7 * r
        y = cy + (H.rnd(k + 70, 5) - 0.5) * 1.7 * r
        if (x - cx) ** 2 + (y - cy) ** 2 < (r - 10) ** 2:
            f.circle(x, y, 2 + 2 * H.rnd(k + 9, 5), "#ffc078")
    for px, py in ((cx - 62, cy + 10), (cx + 58, cy - 8)):
        for rr, op in ((54, 0.12), (40, 0.18), (28, 0.3)):
            f.add(f'<circle cx="{px}" cy="{py}" r="{rr}" fill="none" stroke="#ff8787" stroke-width="3" stroke-opacity="{op}"/>')
        f.add(f'<circle cx="{px}" cy="{py}" r="30" fill="url(#qt-p)"/>')
        f.circle(px, py, 9, "#fa5252", WHITE, 1.5)
    f.arrow(cx - 30, cy + 64, cx - 4, cy + 58, "#ffd8a8", 3, 12)
    f.arrow(cx + 30, cy - 62, cx + 4, cy - 56, "#ffd8a8", 3, 12)
    # the handle of the lens
    f.path(f"M{cx + 100},{cy + 100} L{cx + 190},{cy + 190}", stroke="#495057", w=22, extra='stroke-linecap="round"')
    f.path(f"M{cx + 100},{cy + 100} L{cx + 190},{cy + 190}", stroke=INK, w=3)
    return f.svg()


def slits():
    """The two-slit pattern built up from single electrons: 30, 300 and 3000 hits (simulated)."""
    f = Fig("fy14qt-slits", 400, "Three panels of a detector screen after a double-slit experiment with single electrons, simulated. "
            "Left, after 30 electrons: scattered dots with no clear pattern. Middle, after 300 electrons: the dots begin to "
            "gather in vertical bands. Right, after 3000 electrons: clear bright bands of many dots with almost empty bands "
            "between them, an interference pattern.")
    rnd = random.Random(7)
    def sample():
        while True:
            x = rnd.uniform(-1, 1)
            env = (math.sin(3.0 * x) / (3.0 * x)) ** 2 if x else 1.0
            I = env * math.cos(9.0 * x) ** 2
            if rnd.random() < I: return x, rnd.uniform(-1, 1)
    for k, N in enumerate((30, 300, 3000)):
        x0 = 20 + k * 196
        f.rect(x0, 40, 176, 300, "#15191e", INK, 2, 4)
        for _ in range(N):
            x, y = sample()
            f.add(f'<circle cx="{n(x0 + 88 + 82 * x)}" cy="{n(190 + 142 * y)}" r="{1.6 if N == 3000 else 2.4}" fill="#a5d8ff"/>')
        f.tex(x0 + 88, 366, rf"{N}\ \text{{electrons}}", "middle")
    f.tex(300, 18, r"\text{simulated}", "middle", color=MUTED)
    return f.svg()


def barrier():
    """Schematic: a wave meets a barrier higher than its energy, decays inside it and continues, smaller, beyond it."""
    f = Fig("fy14qt-barrier", 340, "Schematic drawing, not to scale. A grey rectangle in the middle is an energy barrier whose top is "
            "higher than the particle's energy, shown as a dashed line. On the left, a blue wave of large amplitude moves "
            "towards the barrier. Inside the barrier the wave does not oscillate but shrinks smoothly. On the right of the "
            "barrier a wave with the same wavelength but a much smaller amplitude continues. The square of the amplitude "
            "tells the probability of finding the particle.")
    yE, a, b = 200, 260, 340
    f.rect(a, 70, b - a, 230, ALUMINIUM, INK, 2)
    f.line(30, 300, 570, 300, INK, 2)
    f.line(30, yE, 570, yE, MUTED, 2, "8 6")
    f.tex(36, yE - 22, r"E", "start", color=MUTED)
    f.tex((a + b) / 2, 52, r"\text{barrier}", "middle")
    A0, k = 70, 2 * math.pi / 70
    kap = math.log(A0 / 12) / (b - a)
    left = " ".join(f"{n(x)},{n(yE - A0 * math.cos(k * (x - a)))}" for x in range(30, a + 1, 2))
    inside = " ".join(f"{n(x)},{n(yE - A0 * math.exp(-kap * (x - a)))}" for x in range(a, b + 1, 2))
    At = A0 * math.exp(-kap * (b - a))
    right = " ".join(f"{n(x)},{n(yE - At * math.cos(k * (x - b)))}" for x in range(b, 571, 2))
    f.add(f'<polyline points="{left} {inside} {right}" fill="none" stroke="{COLD}" stroke-width="3.5" stroke-linejoin="round"/>')
    f.tex(140, 320, r"\text{incoming}", "middle", color=COLD)
    f.tex(460, 320, r"\text{transmitted}", "middle", color=COLD)
    f.tex(570, 24, r"\text{schematic}", "end", color=MUTED)
    return f.svg()


def sun_barrier():
    """Electric potential energy of two protons against distance, log–log, with k_B T at the Sun's centre."""
    f = Fig("fy14qt-sunbarrier", 440, "Graph with logarithmic scales on both axes. Horizontal axis: the distance r between two protons, "
            "from 1 to 3000 femtometres. Vertical axis: energy in kiloelectronvolts, from 0.1 to 10 000. A falling straight line "
            "is the electric potential energy of the two protons, which grows as they come closer: 1.44 MeV at 1 femtometre, "
            "0.72 MeV at 2 femtometres. A horizontal orange line at 1.35 keV is the typical kinetic energy at the centre of the "
            "Sun. It meets the potential energy line at about 1060 femtometres, the closest a proton with this energy could come "
            "in classical physics. A shaded strip below 2 femtometres marks where the strong nuclear force can join the protons.")
    ax = Axes(f, (96, 360), (480, 60), x=(0, math.log10(3000)), y=(-1, 4), xticks=[1, 2, 3], yticks=[0, 1, 2, 3, 4],
              xlabel=r"r\ (\text{fm})", ylabel=r"E\ (\text{keV})",
              xfmt=lambda v: {1: "10", 2: "100", 3: "1000"}[v], yfmt=lambda v: {0: "1", 1: "10", 2: "100", 3: "1000", 4: r"10^4"}[v],
              origin_label=False)
    f.tex(ax.X(0), ax.y0 + 24, "1", "middle")
    f.tex(ax.x0 - 12, ax.Y(-1), "0.1", "end")
    f.rect(ax.X(0), ax.Y(4), ax.X(math.log10(2)) - ax.X(0), ax.Y(-1) - ax.Y(4), GOOD_LIGHT, extra='fill-opacity="0.6"')
    ax.line([(0, math.log10(KE2 * 1000)), (math.log10(3000), math.log10(KE2 * 1000 / 3000))], HOT, 3.5)
    ax.line([(0, math.log10(KT_KEV)), (math.log10(3000), math.log10(KT_KEV))], HEAT, 3, dash="10 6")
    rt = KE2 * 1000 / KT_KEV
    ax.point(math.log10(rt), math.log10(KT_KEV), HEAT)
    ax.point(math.log10(2), math.log10(KE2 * 500), HOT)
    f.tex(ax.X(math.log10(2)) + 14, ax.Y(math.log10(KE2 * 500)) - 4, r"720\ \text{keV at } 2\ \text{fm}", "start", color=HOT, bg=True)
    f.tex(ax.X(1.75), ax.Y(math.log10(KT_KEV)) - 26, r"k_\text{B}T = 1.35\ \text{keV}", "middle", color=HEAT, bg=True)
    f.tex(ax.X(math.log10(rt)), ax.Y(math.log10(KT_KEV)) + 34, r"1060\ \text{fm}", "middle", color=HEAT, bg=True)
    f.tex(ax.X(1.6), ax.Y(2.2), r"\text{electric repulsion}", "start", color=HOT, bg=True)
    return f.svg()


FIGURES = {"hero": hero, "slits": slits, "barrier": barrier, "sunbarrier": sun_barrier}
