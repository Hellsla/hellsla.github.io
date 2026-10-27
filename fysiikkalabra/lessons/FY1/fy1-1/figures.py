"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy1-1` writes them into lesson.md."""
import math
from figlib import (Fig, INK, MUTED, RULE_LIGHT, WHITE, COLD, COLD_LIGHT, HEAT, HEAT_LIGHT, HOT, HOT_LIGHT, ALUMINIUM, GOOD, GOOD_LIGHT,
                    WATER, WATER_LIGHT, ICE, SAND, SAND_LIGHT, IRON, PAPER, fi, n)
import herolib as H


def hero():
    """The chapter's opening illustration: five zoom lenses side by side, each showing a larger thing than the one on its left (a schematic, not to scale)."""
    f = H.hero("fy11-hero", "Kuvitus: viisi kehystä vierekkäin, joista jokainen näyttää edellistä suuremman kohteen. Vasemmalta oikealle: "
               "atomi, punasolu, ihminen, Maa ja galaksi. Kehysten välissä oranssit nuolet osoittavat oikealle: zoomaus ulospäin.")
    f.rect(0, 0, 1200, 600, PAPER)
    cy = 300
    lens = [(68, 40), (200, 62), (382, 90), (632, 130), (982, 190)]
    for k in range(4):
        x = (lens[k][0] + lens[k][1] + lens[k + 1][0] - lens[k + 1][1]) / 2
        f.path(f"M{n(x - 9)},{cy - 16} L{n(x + 11)},{cy} L{n(x - 9)},{cy + 16} Z", HEAT)
    # 1: hydrogen atom, a cloud around a tiny nucleus
    x, r = lens[0]
    f.circle(x, cy, r, COLD_LIGHT, INK, 3)
    for rr, op in ((32, 0.25), (22, 0.35), (12, 0.5)):
        f.circle(x, cy, rr, COLD, None).body[-1] = f'<circle cx="{n(x)}" cy="{n(cy)}" r="{rr}" fill="{COLD}" fill-opacity="{op}"/>'
    f.circle(x, cy, 5, HOT, WHITE, 2)
    # 2: a red blood cell
    x, r = lens[1]
    f.circle(x, cy, r, HOT_LIGHT, INK, 3)
    f.circle(x, cy, 42, HOT, INK, 3)
    f.add(f'<ellipse cx="{n(x)}" cy="{n(cy)}" rx="22" ry="22" fill="{HOT_LIGHT}" fill-opacity="0.7"/>')
    # 3: a person under the sky
    x, r = lens[2]
    f.add(f'<clipPath id="fy11h-l3"><circle cx="{n(x)}" cy="{cy}" r="{r}"/></clipPath>')
    f.circle(x, cy, r, ICE, None)
    f.add(f'<g clip-path="url(#fy11h-l3)"><rect x="{x - r}" y="{cy + 58}" width="{2 * r}" height="40" fill="{GOOD_LIGHT}"/>'
          f'<rect x="{n(x - 34)}" y="{cy + 14}" width="14" height="46" rx="6" fill="{IRON}" stroke="{INK}" stroke-width="3"/>'
          f'<rect x="{n(x - 14)}" y="{cy + 14}" width="14" height="46" rx="6" fill="{IRON}" stroke="{INK}" stroke-width="3"/>'
          f'<rect x="{n(x - 40)}" y="{cy - 36}" width="40" height="56" rx="12" fill="{COLD}" stroke="{INK}" stroke-width="3"/>'
          f'<rect x="{n(x - 50)}" y="{cy - 32}" width="12" height="42" rx="6" fill="{COLD}" stroke="{INK}" stroke-width="3"/>'
          f'<rect x="{n(x - 2)}" y="{cy - 32}" width="12" height="42" rx="6" fill="{COLD}" stroke="{INK}" stroke-width="3"/>'
          f'<circle cx="{n(x - 20)}" cy="{cy - 56}" r="17" fill="{SAND_LIGHT}" stroke="{INK}" stroke-width="3"/></g>')
    f.circle(x, cy, r, "none", INK, 3)
    # 4: the Earth
    x, r = lens[3]
    f.add(f'<clipPath id="fy11h-l4"><circle cx="{n(x)}" cy="{cy}" r="{r}"/></clipPath>')
    f.circle(x, cy, r, WATER, None)
    land = [[(-70, -60), (-30, -88), (20, -70), (10, -30), (-30, -10), (-62, -22)], [(10, -20), (50, -42), (92, -22), (84, 20), (50, 36), (24, 18)],
            [(-30, 20), (0, 28), (10, 70), (-14, 100), (-32, 66)]]
    g = "".join(f'<path d="M' + " L".join(f"{n(x + a)},{n(cy + b)}" for a, b in poly) + f' Z" fill="{GOOD_LIGHT}" stroke="{GOOD}" stroke-width="3" stroke-linejoin="round"/>' for poly in land)
    f.add(f'<g clip-path="url(#fy11h-l4)">{g}<ellipse cx="{n(x)}" cy="{cy - r}" rx="70" ry="22" fill="{WHITE}"/><ellipse cx="{n(x)}" cy="{cy + r}" rx="60" ry="18" fill="{WHITE}"/></g>')
    f.circle(x, cy, r, "none", INK, 3)
    # 5: a spiral galaxy
    x, r = lens[4]
    f.add(f'<clipPath id="fy11h-l5"><circle cx="{n(x)}" cy="{cy}" r="{r}"/></clipPath>')
    f.circle(x, cy, r, INK, None)
    dots = []
    for arm in range(3):
        for i in range(60):
            t = i / 60; rad = 22 + 150 * t; th = arm * 2.094 + 3.2 * t * 2.2 + (H.rnd(i + arm * 60, 3) - 0.5) * 0.25 * (1 - t)
            d = 3 + 3 * H.rnd(i + arm * 60, 5)
            dots.append(f'<circle cx="{n(x + rad * math.cos(th))}" cy="{n(cy + rad * math.sin(th))}" r="{d:.1f}" fill="{ICE if i % 3 else WHITE}" fill-opacity="{0.9 - 0.4 * t:.2f}"/>')
    f.add(f'<g clip-path="url(#fy11h-l5)">{"".join(dots)}</g>')
    f.circle(x, cy, 26, HEAT_LIGHT, None); f.circle(x, cy, 13, WHITE, None)
    f.circle(x + 92, cy - 38, 7, HEAT, WHITE, 2)
    f.circle(x, cy, r, "none", INK, 3)
    return f.svg()


def scale_axis():
    f = Fig("fy11-axis", 346, "Kaavakuva, jossa koot on merkitty kymmenpotenssien akselille: vaaka-akselilla on koon d suuruusluokka "
            "kymmenpotensseina, akseli piirretty mittakaavassa. Vasemmalta oikealle protoni 10 potenssiin −15 metriä, vetyatomi −10, "
            "hius −4, ihminen 0, Maa 7, Aurinko 9, Linnunrata 21 ja maailmankaikkeus 27. Yksi askel oikealle tarkoittaa kymmenkertaista kokoa.")
    y0, x0, step = 236, 40, 11.8                      # the axis: exponent n at x0 + (n + 16) step
    X = lambda n: x0 + (n + 16) * step
    f.arrow(24, y0, 584, y0, INK, 2.5, 13)
    for n in range(-15, 28, 5):
        f.line(X(n), y0 - 4, X(n), y0 + (8 if n % 10 == 0 else 5), INK, 2 if n % 10 == 0 else 1.5)
    for n in (-10, 0, 10, 20):
        f.tex(X(n), y0 + 30, rf"10^{{{n}}}" if n else "10^{0}", "middle", MUTED)
    f.tex(584, y0 + 66, r"d\ (\text{m})", "end")
    marks = [(-15, 1, "protoni", "middle", 62), (-10, 2, "vetyatomi", "middle", 120), (-4, 1, "hius", "middle", 184),
             (0, 3, "ihminen", "middle", 232), (7, 1, "Maa", "middle", X(7)), (9, 2, "Aurinko", "middle", 352),
             (21, 1, "Linnunrata", "middle", X(21)), (27, 3, "maailmankaikkeus", "end", 586)]
    rows = {1: 188, 2: 138, 3: 88}
    for n, r, name, anchor, lx in marks:
        yl = rows[r]
        f.line(X(n), y0 - 6, X(n), yl + 18, MUTED, 1.5, "5 4")
        f.tex(lx, yl, rf"\text{{{name}}}", anchor)
        f.circle(X(n), y0, 7, INK, WHITE, 2)
    f.tex(300, 40, r"\text{yksi askel oikealle} \Rightarrow \text{koko} \times 10", "middle", COLD)
    return f.svg()


def ladder():
    f = Fig("fy11-ladder", 330, "Kaaviokuva, ei mittakaavassa: viisi tikapuuaskelmaa, joissa koko on kymmenkertaistunut jokaisella askeleella "
            "10 potenssiin n1, n1 plus 1, n1 plus 2 ja niin edelleen aina 10 potenssiin n2 asti. Suuruusluokkien ero on askelten lukumäärä "
            "n2 miinus n1, ja kokojen suhde d2 per d1 on noin 10 potenssiin n2 miinus n1.")
    bw, xs = 56, [28, 148, 268, 388, 508]
    hs = [34, 70, 106, 142, 178]
    labs = ["10^{n_1}", "10^{n_1+1}", "10^{n_1+2}", r"\ldots", "10^{n_2}"]
    base = 262
    for i, (x, h) in enumerate(zip(xs, hs)):
        f.rect(x, base - h, bw, h, COLD_LIGHT, COLD, 2.5, rx=3)
        f.tex(x + bw / 2, base - h - 24, labs[i], "middle", INK, w=100)
    for i in range(4):
        xm = xs[i] + bw + 32
        f.arrow(xs[i] + bw + 10, base - 56, xs[i + 1] - 10, base - 56, MUTED, 2, 10)
        f.tex(xm, base - 24, r"\times 10", "middle", HEAT, w=60)
    f.line(xs[0], base + 18, xs[4] + bw, base + 18, INK, 2.5)
    f.line(xs[0], base + 10, xs[0], base + 26, INK, 2.5); f.line(xs[4] + bw, base + 10, xs[4] + bw, base + 26, INK, 2.5)
    f.tex(300, base + 50, r"\Delta n = n_2 - n_1\ \text{askelta}", "middle")
    f.tex(584, 30, r"\text{ei mittakaavassa}", "end", MUTED)
    return f.svg()


def light_time():
    f = Fig("fy11-light", 346, "Kaaviokuva, ei mittakaavassa: valo kulkee tyhjiössä nopeudella c ja matka on s = c t. Valo kulkee Kuusta Maahan "
            "3,84 · 10 potenssiin 8 metriä noin 1,28 sekunnissa, Auringosta Maahan 1,50 · 10 potenssiin 11 metriä noin 8,3 minuutissa ja "
            "Proxima Centaurista Maahan 4,0 · 10 potenssiin 16 metriä noin 4,2 vuodessa. Nuolten pituudet kuvaavat vain järjestystä.")
    rows = [(70, "Kuu", ALUMINIUM, 290, r"s = 3{,}84\cdot10^{8}\,\text{m}", r"t = 1{,}28\,\text{s}"),
            (170, "Aurinko", HEAT_LIGHT, 400, r"s = 1{,}50\cdot10^{11}\,\text{m}", r"t = 8{,}3\,\text{min}"),
            (270, "Proxima", HOT_LIGHT, 500, r"s = 4{,}0\cdot10^{16}\,\text{m}", r"t = 4{,}2\,\text{a}")]
    for y, name, col, xe, sd, td in rows:
        f.tex(24, y - 34, rf"\text{{{name}}}", "start")
        f.circle(34, y, 12, col, INK, 2.5)
        f.block_arrow(58, y, xe - 18, y, HEAT_LIGHT, 12, 26, 22)
        f.circle(xe, y, 12, COLD_LIGHT, COLD, 2.5)
        f.tex(xe + 20, y, r"\text{Maa}", "start")
        f.tex((58 + xe) / 2 + 40, y - 34, sd, "middle")
        f.tex((58 + xe) / 2 + 40, y + 34, td, "middle", COLD)
    f.tex(584, 330, r"\text{ei mittakaavassa}", "end", MUTED)
    return f.svg()


FIGURES = {"hero": hero, "scale-axis": scale_axis, "ladder": ladder, "light-time": light_time}
