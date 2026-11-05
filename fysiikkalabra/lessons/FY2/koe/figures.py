"""Figures of the FY2 Esimerkkikoe (scripts/figlib.py); `python scripts/practice.py figures FY2/koe` writes them into solutions.md."""
from figlib import Fig, Axes, INK, COLD

M4 = [40, 150, 420, 680, 870, 880, 860, 700, 440, 210, 60, 15]


def bars():
    f = Fig("fy2-k4-bars", 420, "Pylväskuvaaja: aurinkopaneelien sähköntuotanto kilowattitunteina kuukausittain. Tuotanto on suurinta touko-, kesä- "
            "ja heinäkuussa, noin 870 kilowattituntia, ja lähes nolla marras-, joulu- ja tammikuussa.")
    ax = Axes(f, (80, 370), (490, 70), x=(0.4, 12.6), y=(0, 1000), xticks=list(range(1, 13)), yticks=[0, 200, 400, 600, 800, 1000],
              xlabel=r"\text{kk}", ylabel=r"E\ (\text{kWh})", grid=False)
    for k, e in enumerate(M4, 1):
        x0, x1 = ax.X(k - 0.35), ax.X(k + 0.35)
        f.rect(x0, ax.Y(e), x1 - x0, ax.Y(0) - ax.Y(e), fill=COLD, stroke=INK, sw=1.5)
    return f.svg()


FIGURES = {"fy2-k4-bars": bars}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {"fy2-k4-bars": "reveals: the model graph of exam task fy2-k4 (its solution)"}
