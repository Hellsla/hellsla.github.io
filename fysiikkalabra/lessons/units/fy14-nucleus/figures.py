"""Figures of the unit fy14-nucleus (scripts/figlib.py, herolib.py); `python3 scripts/units.py figures fy14-nucleus`
writes them into content/en/units/fy14-nucleus/unit.md. English: the decimal sign is a point. Protons are drawn red and
neutrons grey, as in the Isotope Builder (assets/units/fy14/fx/isotopes.js). The ranges of the nuclear force are the
values of Wikipedia "Nuclear force" (checked 2026-11-01); the iron-56 radius is R = 1.2 fm · A^(1/3)."""
import math
import figlib
from figlib import Fig, INK, MUTED, WHITE, RULE, RULE_LIGHT, HOT, HOT_LIGHT, COLD, COLD_LIGHT, GOOD, GOOD_LIGHT, IRON, METAL_EDGE, n
import herolib as H

figlib.set_language({}, ".")

R_FE = 1.2 * 56 ** (1 / 3)      # fm, 4.59


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


def cluster(f, pre, cx, cy, r, kinds, plus=True):
    """Nucleons packed in rings around (cx, cy): kinds is a string of 'p' and 'n' in drawing order (back to front)."""
    golden = math.pi * (3 - math.sqrt(5))
    pos = [(math.sqrt(i + 0.5) * r * 1.02 * math.cos(i * golden), math.sqrt(i + 0.5) * r * 1.02 * math.sin(i * golden)) for i in range(len(kinds))]
    pos = sorted(pos, key=lambda p: -(p[0] ** 2 + p[1] ** 2))
    for (dx, dy), k in zip(pos, kinds):
        nucleon(f, pre, cx + dx, cy + dy, r, k, plus)


def hero():
    """The Why question: a whole atom as a faint electron cloud with a tiny nucleus at its centre; a magnifying circle
    shows the nucleus packed with protons and neutrons. No words, and nothing that says why they stay together."""
    f = H.hero("fy14nu-hero", "Illustration: a dark background. On the left, a large, faint blue cloud stands for the electrons "
               "of an atom; at its centre is a tiny bright dot, the nucleus. Two thin lines lead from the dot to a large "
               "magnifying circle on the right. Inside the circle the nucleus is shown enlarged: a tight cluster of red protons, "
               "each marked with a plus sign, and grey neutrons, all touching each other.")
    f.defs_add('<radialGradient id="fy14nu-h-bg" cx="30%" cy="50%" r="80%"><stop offset="0" stop-color="#2d3a46"/><stop offset="1" stop-color="#141b22"/></radialGradient>')
    f.defs_add(f'<radialGradient id="fy14nu-h-cloud" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="{COLD_LIGHT}" stop-opacity="0.55"/>'
               f'<stop offset="0.6" stop-color="{COLD}" stop-opacity="0.28"/><stop offset="1" stop-color="{COLD}" stop-opacity="0"/></radialGradient>')
    f.defs_add(f'<radialGradient id="fy14nu-h-lens" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#3b4a58"/><stop offset="1" stop-color="#1f2933"/></radialGradient>')
    nucleon_defs(f, "fy14nu-h")
    f.rect(0, 0, 1200, 600, "url(#fy14nu-h-bg)")
    for k in range(60):
        f.circle(H.rnd(k, 3) * 1200, H.rnd(k + 300, 3) * 600, 0.8 + 1.2 * H.rnd(k + 700, 3), "#55626f")
    cx, cy = 300, 300
    f.add(f'<circle cx="{cx}" cy="{cy}" r="250" fill="url(#fy14nu-h-cloud)"/>')
    # faint electron positions: a probability cloud, not orbits
    for k in range(90):
        a = 2 * math.pi * H.rnd(k, 7); rr = 220 * math.sqrt(H.rnd(k + 200, 7))
        f.circle(cx + rr * math.cos(a), cy + rr * math.sin(a), 2.2, COLD_LIGHT)
    f.circle(cx, cy, 5, HOT_LIGHT)
    f.circle(cx, cy, 2.5, WHITE)
    # the magnifier
    mx, my, mr = 860, 300, 220
    f.line(cx + 4, cy - 4, mx - mr * 0.70, my - mr * 0.71, "#9aa1a9", 2, "8 8")
    f.line(cx + 4, cy + 4, mx - mr * 0.70, my + mr * 0.71, "#9aa1a9", 2, "8 8")
    f.circle(cx, cy, 14, "none", "#9aa1a9", 2)
    f.add(f'<circle cx="{mx}" cy="{my}" r="{mr}" fill="url(#fy14nu-h-lens)" stroke="{METAL_EDGE}" stroke-width="10"/>')
    f.add(f'<circle cx="{mx}" cy="{my}" r="{mr - 10}" fill="none" stroke="#c4ccd4" stroke-width="2" stroke-opacity="0.5"/>')
    cluster(f, "fy14nu-h", mx, my, 30, "npnpnpnpnpnpnpnpnp"[:14])
    f.path(f"M{mx - 150},{my - 120} Q{mx - 60},{my - 190} {mx + 40},{my - 180}", stroke=WHITE, w=6, extra='stroke-linecap="round" stroke-opacity="0.25"')
    return f.svg()


def notation():
    """Nuclear notation of carbon-14 with its three parts named."""
    f = Fig("fy14nu-notation", 300, size=26, label= "Diagram of nuclear notation, using carbon-14 as the example. In the middle the large chemical "
            "symbol C. Top left, the mass number 14, with a label: mass number A, the number of protons plus neutrons. "
            "Bottom left, the atomic number 6, with a label: atomic number Z, the number of protons. A label on the right says "
            "that the symbol names the element, and that Z and the symbol always belong together. Below: N = A − Z = 8 neutrons.")
    f.tex(392, 150, r"\text{C}", "middle", size=130, w=110)
    f.tex(330, 84, "14", "end", size=56, w=80)
    f.tex(330, 214, "6", "end", size=56, w=50)
    f.tex(16, 52, r"\text{mass number}", "start")
    f.tex(16, 86, r"A = Z + N", "start")
    f.arrow(160, 86, 252, 86, INK, 2.5, 13)
    f.tex(16, 200, r"\text{atomic number}", "start")
    f.tex(16, 234, r"Z\ (\text{protons})", "start")
    f.arrow(196, 214, 282, 214, INK, 2.5, 13)
    f.arrow(480, 150, 452, 150, INK, 2.5, 13)
    f.tex(484, 118, r"\text{chemical}", "start")
    f.tex(484, 150, r"\text{symbol}", "start")
    f.tex(484, 182, r"(\text{by } Z)", "start", color=MUTED)
    f.tex(380, 278, r"N = A - Z = 8", "middle")
    return f.svg()


def hydrogen():
    """The three isotopes of hydrogen: same one proton, zero, one or two neutrons."""
    f = Fig("fy14nu-hydrogen", 300, size=26, label="Three nuclei side by side, drawn as red protons with a plus sign and grey neutrons. Left: hydrogen-1, "
            "one proton only, notation 1 over 1 H, stable. Middle: hydrogen-2 or deuterium, one proton and one neutron, 2 over 1 H, "
            "stable. Right: hydrogen-3 or tritium, one proton and two neutrons, 3 over 1 H, radioactive with a half-life of 12.3 years. "
            "All three have Z = 1, so they are the same element.")
    nucleon_defs(f, "fy14nu-hy")
    r = 22
    xs = (100, 300, 500)
    nucleon(f, "fy14nu-hy", xs[0], 92, r, "p")
    nucleon(f, "fy14nu-hy", xs[1] - 19, 92, r, "n"); nucleon(f, "fy14nu-hy", xs[1] + 19, 92, r, "p")
    nucleon(f, "fy14nu-hy", xs[2] - 19, 103, r, "n"); nucleon(f, "fy14nu-hy", xs[2] + 19, 103, r, "n"); nucleon(f, "fy14nu-hy", xs[2], 72, r, "p")
    rows = ((r"{}^{1}_{1}\text{H}", r"\text{hydrogen-1}", r"\text{stable}"),
            (r"{}^{2}_{1}\text{H}", r"\text{deuterium}", r"\text{stable}"),
            (r"{}^{3}_{1}\text{H}", r"\text{tritium}", r"T_{1/2} = 12.3\ \text{a}"))
    for x, (a, b, c) in zip(xs, rows):
        f.tex(x, 170, a, "middle", size=34)
        f.tex(x, 222, b, "middle")
        f.tex(x, 258, c, "middle", color=GOOD if "stable" in c else HOT)
    f.line(200, 30, 200, 280, RULE_LIGHT, 2); f.line(400, 30, 400, 280, RULE_LIGHT, 2)
    return f.svg()


def ranges():
    """Where each force acts, along the distance r between the centres of two nucleons (Wikipedia, Nuclear force),
    with the diameter of an iron-56 nucleus for scale."""
    f = Fig("fy14nu-ranges", 350, size=26, label="Schematic bar diagram along an axis of distance r between the centres of two nucleons, from 0 to 10 "
            "femtometres. Top bar, green: the strong nuclear force attracts from about 0.7 fm and fades out by about 2.5 fm; "
            "below 0.7 fm it repels (a hatched grey part). Middle bar, red: the electric repulsion between two protons acts at "
            "every distance and continues past the end of the axis, getting weaker with distance. Bottom: a bracket shows the "
            "diameter of an iron-56 nucleus, about 9.2 fm, much wider than the reach of the strong force.")
    X0, X1 = 40, 500
    X = lambda r: X0 + (X1 - X0) * r / 10
    f.arrow(X0, 300, X1 + 26, 300, INK, 2.5, 13)
    for t in range(0, 11, 2):
        f.line(X(t), 300, X(t), 308, INK, 2)
        f.tex(X(t), 328, str(t), "middle")
    f.tex(X1 + 30, 274, r"r\ (\text{fm})", "start")
    # strong force bar
    f.defs_add(f'<linearGradient id="fy14nu-r-g" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{GOOD}"/>'
               f'<stop offset="0.6" stop-color="{GOOD}"/><stop offset="1" stop-color="{GOOD}" stop-opacity="0.05"/></linearGradient>')
    f.defs_add(f'<pattern id="fy14nu-r-h" width="10" height="10" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">'
               f'<rect width="10" height="10" fill="{RULE_LIGHT}"/><line x1="0" y1="0" x2="0" y2="10" stroke="{MUTED}" stroke-width="3"/></pattern>')
    f.rect(X(0), 56, X(0.7) - X(0), 40, "url(#fy14nu-r-h)", INK, 1.5)
    f.rect(X(0.7), 56, X(2.5) - X(0.7), 40, "url(#fy14nu-r-g)", INK, 1.5)
    f.tex(X(2.8), 62, r"\text{strong force: attracts}", "start", color=GOOD)
    f.tex(X(2.8), 92, r"\text{(any two nucleons)}", "start", color=MUTED)
    f.tex(X(0) + 2, 30, r"\text{repels}", "start", color=MUTED)
    # electric force bar
    f.defs_add(f'<linearGradient id="fy14nu-r-e" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{HOT}"/>'
               f'<stop offset="1" stop-color="{HOT}" stop-opacity="0.25"/></linearGradient>')
    f.path(f"M{n(X(0))},126 H{n(X1)} V118 L{n(X1 + 22)},146 L{n(X1)},174 V166 H{n(X(0))} Z", "url(#fy14nu-r-e)", INK, 1.5)
    f.tex(X(2.8), 146, r"\text{electric force: repels}", "start", color=WHITE)
    f.tex(X(2.8), 192, r"\text{(two protons, any distance)}", "start", color=MUTED)
    # iron-56 diameter
    d = 2 * R_FE
    f.path(f"M{n(X(0))},256 V270 H{n(X(d))} V256", stroke=INK, w=2.5)
    f.tex(X(d / 2), 236, rf"\text{{diameter of }}{{}}^{{56}}\text{{Fe}} \approx {d:.1f}\ \text{{fm}}", "middle", bg=True)
    return f.svg()


FIGURES = {"hero": hero, "notation": notation, "hydrogen": hydrogen, "ranges": ranges}
