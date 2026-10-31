"""Figures of the guide Anturit ja mittausohjelma (scripts/figlib.py); `python scripts/guides.py figures
tvt-mittausohjelma` writes them into guide.md. A schematic force pulse without numbers (force is red, the teacher's
colour rule): the same pulse sampled densely and sparsely, the sparse samples falling either side of the peak."""
import math
from figlib import Fig, Axes, INK, MUTED, WHITE

FORCE = "#c92a2a"


def pulse(t): return 0.8 + 5.4 * math.exp(-(t - 3) ** 2 / (2 * 0.45 ** 2))


def sampling():
    f = Fig("tvtm-sampling", 340, "Kaaviokuva ilman lukuarvoja: tasaisesta lukemasta nouseva lyhyt voimapulssi ajan funktiona punaisena käyränä. Tiheästi "
            "otetut näytteet, pienet mustat pisteet, seuraavat käyrää ja osuvat myös huipulle. Harvaan otetut näytteet, "
            "neliöt katkoviivalla yhdistettyinä, osuvat huipun molemmille puolille, joten niistä huippu näyttää paljon "
            "matalammalta kuin se on.")
    ax = Axes(f, (80, 290), (470, 70), x=(0, 8), y=(0, 7.5), xticks=[], yticks=[], xlabel=r"t\ (\text{s})",
              ylabel=r"F\ (\text{N})", grid=False, origin_label=False)
    ax.curve(pulse, 0.1, 7.9, FORCE, 3)
    sparse = [(k + 0.5, pulse(k + 0.5)) for k in range(8)]
    ax.line(sparse, MUTED, 2, "6 5")
    for k in range(2, 79): f.circle(ax.X(k / 10), ax.Y(pulse(k / 10)), 3, INK)
    for t, y in sparse: f.rect(ax.X(t) - 6, ax.Y(y) - 6, 12, 12, WHITE, MUTED, 2.5)
    # legend
    f.line(300, 92, 330, 92, FORCE, 3); f.tex(342, 92, r"\text{todellinen voima}", "start")
    for x in (304, 315, 326): f.circle(x, 128, 3, INK)
    f.tex(342, 128, r"\text{tiheä näytteenotto}", "start")
    f.line(300, 164, 330, 164, MUTED, 2, "6 5"); f.rect(309, 158, 12, 12, WHITE, MUTED, 2.5)
    f.tex(342, 164, r"\text{harva näytteenotto}", "start")
    return f.svg()


FIGURES = {"sampling": sampling}
