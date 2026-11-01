"""Figures of the unit fy14-binding-energy (scripts/figlib.py, herolib.py); `python3 scripts/units.py figures
fy14-binding-energy` writes them into content/en/units/fy14-binding-energy/unit.md. English: the decimal sign is a
point. Every number is computed here from the AME2020 atomic masses of the course's data file
(assets/units/fy14/data/nuclides.json) and the CODATA 2018 value of 1 u in MeV."""
import json, math, pathlib
import figlib
from figlib import Fig, INK, MUTED, WHITE, RULE, RULE_LIGHT, HOT, HOT_LIGHT, HEAT, HEAT_LIGHT, COLD, COLD_LIGHT, GOOD, GOOD_LIGHT, n
import herolib as H

figlib.set_language({}, ".")

DATA = json.loads((pathlib.Path(__file__).resolve().parents[3] / "assets/units/fy14/data/nuclides.json").read_text())
BY = {x["id"]: x for x in DATA["nuclides"]}
U = DATA["constants"]["u_MeV"]; MH = BY["H-1"]["mass_u"]; MN = DATA["constants"]["m_n_u"]


def B(i):
    x = BY[i]
    return (x["Z"] * MH + x["N"] * MN - x["mass_u"]) * U


def nucleon_defs(f, pre):
    for k, a, b, c in (("p", "#ff8a80", "#c92a2a", "#7f1d1d"), ("n", "#e9ecef", "#9aa1a9", "#4b5259")):
        f.defs_add(f'<radialGradient id="{pre}-{k}" cx="35%" cy="32%" r="70%"><stop offset="0%" stop-color="{a}"/>'
                   f'<stop offset="55%" stop-color="{b}"/><stop offset="100%" stop-color="{c}"/></radialGradient>')


def nucleon(f, pre, x, y, r, kind, plus=True):
    f.add(f'<circle cx="{n(x)}" cy="{n(y)}" r="{r:g}" fill="url(#{pre}-{kind})" stroke="{INK}" stroke-width="1.5"/>')
    if kind == "p" and plus:
        w = r * 0.45
        f.line(x - w, y, x + w, y, WHITE, max(2, r * 0.16), cap="round")
        f.line(x, y - w, x, y + w, WHITE, max(2, r * 0.16), cap="round")


def blob(f, pre, cx, cy, r, kinds):
    golden = math.pi * (3 - math.sqrt(5))
    pos = [(math.sqrt(i + 0.5) * r * 1.02 * math.cos(i * golden), math.sqrt(i + 0.5) * r * 1.02 * math.sin(i * golden)) for i in range(len(kinds))]
    for (dx, dy), k in sorted(zip(pos, kinds), key=lambda t: -(t[0][0] ** 2 + t[0][1] ** 2)):
        nucleon(f, pre, cx + dx, cy + dy, r, k)


def flash(f, gid, cx, cy, r):
    f.defs_add(f'<radialGradient id="{gid}"><stop offset="0" stop-color="{WHITE}" stop-opacity="0.95"/><stop offset="0.35" stop-color="{HEAT_LIGHT}" stop-opacity="0.7"/>'
               f'<stop offset="1" stop-color="{HEAT}" stop-opacity="0"/></radialGradient>')
    f.add(f'<circle cx="{n(cx)}" cy="{n(cy)}" r="{r}" fill="url(#{gid})"/>')


def hero():
    """The Why question: on the left two light nuclei meet and fuse, on the right a heavy nucleus splits in two; a
    flash of released energy at each. No words, no curve (the curve answers a prediction)."""
    f = H.hero("fy14be-hero", "Illustration on a dark background, in two halves. Left: two small nuclei, made of red protons and grey "
               "neutrons, fly towards each other and meet in a bright yellow flash. Right: a large nucleus with many protons and "
               "neutrons breaks into two medium-sized pieces that fly apart, with a few single neutrons and another bright flash.")
    f.defs_add('<linearGradient id="fy14be-h-bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#26313b"/><stop offset="1" stop-color="#121820"/></linearGradient>')
    nucleon_defs(f, "fy14be-h")
    f.rect(0, 0, 1200, 600, "url(#fy14be-h-bg)")
    f.line(600, 60, 600, 540, "#3a4754", 3, "10 12")
    for k in range(50):
        f.circle(H.rnd(k, 5) * 1200, H.rnd(k + 400, 5) * 600, 0.8 + H.rnd(k + 800, 5), "#4b5866")
    # fusion
    flash(f, "fy14be-h-f1", 300, 300, 150)
    for x0, x1 in ((90, 210), (510, 390)):
        f.line(x0, 300, x1, 300, COLD_LIGHT, 4, "2 14", cap="round")
    nucleon(f, "fy14be-h", 222, 300, 26, "p"); nucleon(f, "fy14be-h", 258, 300, 26, "n")
    nucleon(f, "fy14be-h", 344, 316, 26, "n"); nucleon(f, "fy14be-h", 380, 316, 26, "n"); nucleon(f, "fy14be-h", 362, 285, 26, "p")
    # fission
    flash(f, "fy14be-h-f2", 900, 300, 170)
    blob(f, "fy14be-h", 800, 230, 15, ["p" if i % 5 in (0, 3) else "n" for i in range(40)])
    blob(f, "fy14be-h", 1010, 380, 15, ["p" if i % 5 in (1, 3) else "n" for i in range(32)])
    for (x, y), (dx, dy) in (((730, 165), (-60, -50)), ((1085, 450), (60, 50))):
        f.line(x, y, x + dx, y + dy, COLD_LIGHT, 4, "2 14", cap="round")
    for x, y in ((905, 160), (1080, 250), (860, 450)):
        nucleon(f, "fy14be-h", x, y, 15, "n")
    return f.svg()


def ladder():
    """Energy (and mass) of helium-4: the free nucleons above, the nucleus 28.3 MeV lower."""
    b = B("He-4"); m_free = 2 * MH + 2 * MN; m_he = BY["He-4"]["mass_u"]
    f = Fig("fy14be-ladder", 380, size=26, label=f"Energy diagram of helium-4. An upper level: two protons and two neutrons far apart, with the total mass "
            f"{m_free:.6f} u. A lower level, {b:.1f} MeV below: the helium-4 nucleus, mass {m_he:.6f} u. An arrow up on the left is "
            f"the binding energy B = {b:.1f} MeV that must be added to separate the nucleons. An arrow down on the right is the "
            f"same energy released when they join.")
    nucleon_defs(f, "fy14be-l")
    yt, yb = 110, 300
    f.line(200, yt, 420, yt, INK, 3); f.line(200, yb, 420, yb, INK, 3)
    for x, kind in ((220, "p"), (275, "n"), (345, "p"), (400, "n")):
        nucleon(f, "fy14be-l", x, yt - 24, 17, kind)
    blob(f, "fy14be-l", 260, yb - 34, 17, ["n", "p", "p", "n"])
    f.tex(310, 34, r"\text{free nucleons}", "middle")
    f.tex(310, yb + 32, r"{}^{4}\text{He}\ \text{nucleus}", "middle")
    f.tex(432, yt, rf"{m_free:.6f}\ \text{{u}}", "start")
    f.tex(432, yb, rf"{m_he:.6f}\ \text{{u}}", "start")
    f.block_arrow(170, yb - 4, 170, yt + 4, GOOD, shaft=14, head=34, headlen=26)
    f.tex(16, 150, r"\text{add}", "start", color=GOOD)
    f.tex(16, 196, r"B =", "start")
    f.tex(16, 230, rf"{b:.1f}\ \text{{MeV}}", "start")
    f.block_arrow(330, yt + 14, 330, yb - 72, HEAT, shaft=14, head=34, headlen=26)
    f.tex(354, (yt + yb) / 2 - 12, r"\text{released}", "start", color=HEAT)
    return f.svg()


def qbars():
    """Total binding energy before and after: D–T fusion and one fission of uranium-235 (each panel on its own scale)."""
    bdt0, bdt1 = B("H-2") + B("H-3"), B("He-4")
    bu0, bu1 = B("U-235"), B("Ba-141") + B("Kr-92")
    f = Fig("fy14be-qbars", 400, size=26, label=f"Two bar charts of the total binding energy before and after a reaction; each has its own scale. "
            f"Left, D–T fusion: before, deuterium plus tritium, {bdt0:.1f} MeV; after, helium-4 plus a neutron, {bdt1:.1f} MeV; the difference "
            f"Q = {bdt1 - bdt0:.1f} MeV is released. Right, fission of uranium-235 into barium-141, krypton-92 and three neutrons: before "
            f"{bu0:.0f} MeV, after {bu1:.0f} MeV, Q = {bu1 - bu0:.0f} MeV. In both, the products are more tightly bound.")
    base = 330
    def panel(x0, b0, b1, top, lab0, lab1, title, qfmt):
        h = lambda v: v / top * 230
        f.tex(x0 + 125, 28, title, "middle")
        f.line(x0 + 10, base, x0 + 250, base, INK, 2.5)
        f.rect(x0 + 30, base - h(b0), 80, h(b0), COLD_LIGHT, COLD, 2)
        f.rect(x0 + 150, base - h(b1), 80, h(b1), COLD, INK, 2)
        f.tex(x0 + 70, base - h(b0) - 20, qfmt(b0), "middle", size=24)
        f.tex(x0 + 190, base - h(b1) - 20, qfmt(b1), "middle", size=24)
        f.tex(x0 + 70, base + 26, lab0, "middle", size=24)
        f.tex(x0 + 190, base + 26, lab1, "middle", size=24)
        f.line(x0 + 110, base - h(b0), x0 + 250, base - h(b0), MUTED, 1.5, "6 5")
        f.path(f"M{n(x0 + 240)},{n(base - h(b0))} V{n(base - h(b1))}", stroke=HEAT, w=4)
        f.tex(x0 + 244, base - (h(b0) + h(b1)) / 2, "Q", "start", color=HEAT)
    panel(20, bdt0, bdt1, 30, r"\text{D + T}", r"{}^{4}\text{He + n}", r"\text{D–T fusion}", lambda v: rf"{v:.1f}\ \text{{MeV}}")
    panel(320, bu0, bu1, 2000, r"{}^{235}\text{U + n}", r"\text{Ba + Kr}", r"{}^{235}\text{U}\ \text{fission}", lambda v: rf"{v:.0f}\ \text{{MeV}}")
    f.tex(300, 384, r"\text{total binding energy; each panel has its own scale}", "middle", size=24, color=MUTED)
    return f.svg()


FIGURES = {"hero": hero, "ladder": ladder, "qbars": qbars}
