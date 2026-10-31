"""Figures of the guide Nopeuden ja matkan määrittäminen mittausdatasta (scripts/figlib.py); `python scripts/guides.py
figures tvt-nopeus-datasta` writes them into guide.md. A schematic (t, v) graph without numbers, velocity in blue
(teacher's rule: velocity, acceleration and force always in different colours): a lift-like start, steady run and stop,
with the area under it cut into narrow trapezoidal strips."""
from figlib import Fig, Axes, INK, MUTED, COLD_LIGHT, WATER_LIGHT

VEL = "#1971c2"


def v(t):
    """Speed up smoothly from t = 0,5 to 2,5, run steadily to 5,5, slow down to rest at 7,5 (schematic)."""
    def ease(u): u = min(max(u, 0), 1); return 3 * u * u - 2 * u ** 3
    return 4 * (ease((t - 0.5) / 2) - ease((t - 5.5) / 2))


def strips():
    f = Fig("tvtn-strips", 340, "Kaaviokuva ilman lukuarvoja: nopeus v ajan t funktiona sinisenä käyränä. Nopeus kasvaa "
            "nollasta, pysyy jonkin aikaa vakiona ja pienenee takaisin nollaan. Käyrän ja aika-akselin välinen alue on "
            "jaettu kapeisiin pystysuoriin suikaleisiin, joiden leveys on delta t. Yksi suikale on korostettu: sen ala on "
            "likimain v kertaa delta t eli matka, joka kuljetaan sen aikana. Koko alue on kuljettu matka s.")
    ax = Axes(f, (80, 280), (470, 70), x=(0, 8), y=(0, 5), xticks=[], yticks=[], xlabel=r"t\ (\text{s})",
              ylabel=r"v\ (\text{m/s})", grid=False, origin_label=False)
    dt = 0.5
    for i in range(14):
        a, b = 0.5 + i * dt, 0.5 + (i + 1) * dt
        pts = [(a, 0), (a, v(a)), (b, v(b)), (b, 0)]
        ax.area(pts, WATER_LIGHT if i == 2 else COLD_LIGHT, 1)
        f.add('<polygon points="' + " ".join(f"{ax.X(x):.1f},{ax.Y(y):.1f}" for x, y in pts)
              + f'" fill="none" stroke="{VEL}" stroke-width="1.5" stroke-opacity="0.6"/>')
    ax.curve(v, 0.1, 7.9, VEL, 3)
    f.line(80, 280, 470, 280, INK, 2.5)            # the time axis over the strips' bottoms
    # the highlighted strip: its width and its area
    a, b = 1.5, 2.0
    f.line(ax.X(a), 294, ax.X(b), 294, MUTED, 2); f.line(ax.X(a), 288, ax.X(a), 300, MUTED, 2); f.line(ax.X(b), 288, ax.X(b), 300, MUTED, 2)
    f.tex((ax.X(a) + ax.X(b)) / 2, 316, r"\Delta t", "middle", MUTED)
    f.tex(ax.X(0.2), ax.Y(4.6), r"\Delta s \approx v \cdot \Delta t", "start")
    f.line(ax.X(1.45), ax.Y(4.6) + 16, (ax.X(a) + ax.X(b)) / 2, ax.Y(2.2), MUTED, 1.5)
    f.tex(ax.X(4), ax.Y(2), r"s = \text{pinta-ala}", "middle", bg=True)
    return f.svg()


FIGURES = {"strips": strips}
