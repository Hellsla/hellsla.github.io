"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy1-1` writes them into lesson.md."""
import math
from figlib import (Fig, INK, MUTED, RULE_LIGHT, WHITE, GLASS, COLD, COLD_LIGHT, HEAT, HEAT_LIGHT, HOT, HOT_LIGHT, ALUMINIUM, GOOD, GOOD_LIGHT,
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
    f.tex(300, 40, r"\text{yksi askel oikealle} \Rightarrow \text{koko} \cdot 10", "middle", COLD)
    return f.svg()


def ladder():
    f = Fig("fy11-ladder", 372, "Kaaviokuva, ei mittakaavassa: kuusi pylvästä, joissa koko kymmenkertaistuu jokaisella askeleella. "
            "Ensimmäinen on 10 potenssiin −15 metriä, protoni, ja viimeinen 10 potenssiin −10 metriä, vetyatomi. "
            "Askelia on viisi, joten vetyatomi on noin 10 potenssiin 5 eli satatuhatta kertaa protonia suurempi.")
    bw, xs = 48, [24 + 100 * i for i in range(6)]
    hs = [30, 58, 86, 114, 142, 170]
    base = 236
    for i, (x, h) in enumerate(zip(xs, hs)):
        f.rect(x, base - h, bw, h, COLD_LIGHT, COLD, 2.5, rx=3)
        f.tex(x + bw / 2, base - h - 22, rf"10^{{{i - 15}}}", "middle", INK, w=90)
    for i in range(5):
        f.arrow(xs[i] + bw + 6, base - 14, xs[i + 1] - 6, base - 14, MUTED, 2, 9)
        f.tex((xs[i] + bw + xs[i + 1]) / 2, base + 24, r"\cdot 10", "middle", HEAT, w=56)
    f.line(xs[0], base, xs[5] + bw, base, INK, 2)
    f.tex(xs[0], base + 64, r"\text{protoni}", "start")
    f.tex(xs[5] + bw, base + 64, r"\text{vetyatomi}", "end")
    f.tex(300, base + 112, r"5\ \text{askelta} \Rightarrow 10^{5} = 100\,000\ \text{kertaa suurempi}", "middle")
    f.tex(16, 30, r"\text{ei mittakaavassa}", "start", MUTED)
    return f.svg()


# --- small pictures shared by the structure figures ---
def _ball(f, x, y, r, col, edge):
    f.circle(x, y, r, col, edge, 2)


def _proton(f, x, y, r):
    """A proton or neutron: a ball with three quarks inside."""
    f.circle(x, y, r, HEAT_LIGHT, HEAT, 2.5)
    for k, col in enumerate((HOT, GOOD, COLD)):
        a = math.radians(-90 + 120 * k)
        f.circle(x + 0.48 * r * math.cos(a), y + 0.48 * r * math.sin(a), max(3, 0.22 * r), col, WHITE, 1.5)


def _nucleus(f, x, y, r, N=12, Z=6):
    """A nucleus: N nucleons packed in a disc of radius r, protons red and neutrons grey."""
    nr = r * 0.82 / math.sqrt(N)
    for i in range(N - 1, -1, -1):
        rr = (r - nr) * math.sqrt((i + 0.5) / N); a = i * 2.39996
        pr = (i * 0.6180339) % 1 < Z / N
        f.circle(x + rr * math.cos(a), y + rr * math.sin(a), round(nr, 1), HOT if pr else ALUMINIUM, INK, 1.5)


def matter_ladder():
    f = Fig("fy11-matter", 432, "Kaaviokuva, ei mittakaavassa: aineen rakenne portaittain ylhäältä alas. Vesimolekyyli, noin 3 · 10 potenssiin −10 metriä, "
            "koostuu atomeista. Atomi, noin 10 potenssiin −10 metriä, koostuu ytimestä ja elektroneista. Ydin, 10 potenssiin −15 … −14 metriä, "
            "koostuu protoneista ja neutroneista. Protoni ja neutroni, noin 10 potenssiin −15 metriä, koostuvat kolmesta kvarkista. "
            "Kvarkit ja elektroni ovat alkeishiukkasia, pienempiä kuin noin 10 potenssiin −18 metriä. Jokaisen rivin kuva on suurennos edellisen rivin pienestä kohdasta.")
    xi, r, ys = 66, 30, [76, 154, 232, 310, 388]
    # zoom wedges: from a small spot in the picture above to the next picture
    spots = [(xi - 2, ys[0] - 4, 9), (xi, ys[1], 5), (xi - 6, ys[2] - 6, 7), (xi + 9, ys[3] - 8, 6)]
    for (sx, sy, sr), y2 in zip(spots, ys[1:]):
        f.line(sx - sr, sy, xi - r, y2, MUTED, 1.5, "4 3"); f.line(sx + sr, sy, xi + r, y2, MUTED, 1.5, "4 3")
    for (sx, sy, sr) in spots:
        f.circle(sx, sy, sr, "none", HEAT, 2)
    # 1 water molecule
    y = ys[0]
    for sg in (-1, 1):
        f.circle(xi + sg * 19, y + 13, 12, WHITE, INK, 2)
    f.circle(xi, y - 2, 19, HOT, INK, 2)
    # 2 atom: an electron cloud around a nucleus drawn far too large
    y = ys[1]
    f.circle(xi, y, r, COLD_LIGHT, COLD, 2.5)
    f.add(f'<circle cx="{n(xi)}" cy="{n(y)}" r="20" fill="{COLD}" fill-opacity="0.18"/>')
    f.circle(xi, y, 4, HOT, WHITE, 1.5)
    f.circle(xi + 21, y - 12, 4, COLD, WHITE, 1.5); f.circle(xi - 18, y + 15, 4, COLD, WHITE, 1.5)
    # 3 nucleus
    _nucleus(f, xi, ys[2], 27, 12, 6)
    # 4 proton with three quarks
    _proton(f, xi, ys[3], r)
    # 5 quark and electron: points
    y = ys[4]
    f.circle(xi - 14, y, 6, HOT, WHITE, 1.5); f.circle(xi + 14, y, 6, COLD, WHITE, 1.5)
    rows = [(r"\text{vesimolekyyli: kolme atomia yhdessä}", r"3\cdot10^{-10}\,\text{m}"),
            (r"\text{atomi: ydin ja elektronit}", r"10^{-10}\,\text{m}"),
            (r"\text{ydin: protonit ja neutronit}", r"10^{-15}\text{–}10^{-14}\,\text{m}"),
            (r"\text{protoni tai neutroni: 3 kvarkkia}", r"10^{-15}\,\text{m}"),
            (r"\text{kvarkki, elektroni: alkeishiukkasia}", r"{<}\,10^{-18}\,\text{m}")]
    for (name, size), y in zip(rows, ys):
        f.tex(116, y - 15, name, "start")
        f.tex(116, y + 17, size, "start", COLD)
    f.tex(584, 20, r"\text{ei mittakaavassa}", "end", MUTED)
    return f.svg()


def atom_stadium():
    f = Fig("fy11-stadium", 330, "Vertauskuva atomista ja sen ytimestä: jos atomi olisi jalkapallostadionin kokoinen, noin 200 metriä, "
            "sen ydin olisi keskellä herneen kokoinen, noin 5 millimetriä. Herne on kuvassa piirretty aivan liian suureksi; "
            "oikeassa suhteessa se olisi alle pikselin kokoinen. Atomin halkaisija on noin 10 potenssiin −10 metriä ja ytimen noin 10 potenssiin −15 metriä.")
    cx, cy = 300, 172
    f.add(f'<ellipse cx="{cx}" cy="{cy}" rx="250" ry="122" fill="{ALUMINIUM}" stroke="{INK}" stroke-width="2.5"/>')
    f.add(f'<ellipse cx="{cx}" cy="{cy}" rx="214" ry="96" fill="{GOOD_LIGHT}" stroke="{GOOD}" stroke-width="2"/>')
    f.rect(cx - 150, cy - 70, 300, 140, "none", WHITE, 2.5)
    f.line(cx, cy - 70, cx, cy + 70, WHITE, 2.5)
    f.add(f'<circle cx="{cx}" cy="{cy}" r="26" fill="none" stroke="{WHITE}" stroke-width="2.5"/>')
    f.circle(cx, cy, 5, HOT, WHITE, 1.5)
    f.arrow(cx + 120, cy - 40, cx + 12, cy - 4, HEAT, 2.5, 12)
    f.tex(cx + 124, cy - 48, r"\text{ydin} \approx \text{herne}", "start", INK, bg=True)
    f.tex(cx - 196, cy + 40, r"\text{atomi} \approx \text{stadion}", "start", INK, bg=True)
    f.line(cx - 250, 312, cx + 250, 312, INK, 2); f.line(cx - 250, 304, cx - 250, 320, INK, 2); f.line(cx + 250, 304, cx + 250, 320, INK, 2)
    f.tex(cx, 312, r"\approx 200\,\text{m}", "middle", INK, bg=True)
    f.tex(584, 22, r"\text{herne piirretty liian suureksi}", "end", MUTED)
    return f.svg()


def cosmic_address():
    f = Fig("fy11-address", 400, "Kaaviokuva, ei mittakaavassa: sisäkkäiset laatikot näyttävät Maan osoitteen maailmankaikkeudessa. "
            "Uloimpana havaittava maailmankaikkeus, noin 10 potenssiin 27 metriä, sen sisällä Virgon superjoukko noin 10 potenssiin 24 metriä, "
            "sen sisällä Paikallinen ryhmä noin 10 potenssiin 23 metriä, sen sisällä Linnunrata noin 10 potenssiin 21 metriä, sen sisällä "
            "Aurinkokunnan planeettojen alue noin 10 potenssiin 13 metriä ja sisimpänä Maa ja Kuun rata noin 10 potenssiin 9 metriä.")
    levels = [("havaittava maailmankaikkeus", "10^{27}", WHITE), ("Virgon superjoukko", "10^{24}", GLASS),
              ("Paikallinen ryhmä", "10^{23}", COLD_LIGHT), ("Linnunrata", "10^{21}", ICE),
              ("Aurinkokunta", "10^{13}", HEAT_LIGHT), ("Maa ja Kuu", "10^{9}", WHITE)]
    step, dx = 56, 18
    for i, (name, size, col) in enumerate(levels):
        x0, y0 = 12 + i * dx, 12 + i * step
        x1, y1 = 588 - i * dx, 388 - (0 if i == 0 else 0)
        f.rect(x0, y0, x1 - x0, y1 - y0 - i * 6, col, COLD if i < 4 else (HEAT if i == 4 else COLD), 2, rx=10)
        f.tex(x0 + 14, y0 + 26, rf"\text{{{name}}}", "start")
        f.tex(x1 - 14, y0 + 26, size + r"\,\text{m}", "end", MUTED)
    # the Earth and the Moon in the innermost box
    ex, ey = 318, 324
    f.add(f'<ellipse cx="{ex}" cy="{ey}" rx="44" ry="13" fill="none" stroke="{MUTED}" stroke-width="1.5" stroke-dasharray="4 3"/>')
    f.circle(ex, ey, 11, WATER, INK, 2); f.circle(ex + 44, ey, 5, ALUMINIUM, INK, 1.5)
    return f.svg()


def object_types():
    f = Fig("fy11-types", 340, "Kaaviokuva: tähtitieteellisten kohteiden tyyppejä kokoakselilla, jossa jokainen askel on kymmenkertainen koko. "
            "Neutronitähti noin 2 · 10 potenssiin 4 metriä, planeetta Maa 1,3 · 10 potenssiin 7 metriä, tähti Aurinko 1,4 · 10 potenssiin 9 metriä, "
            "musta aukko Sgr A* (tapahtumahorisontin halkaisija) 2,5 · 10 potenssiin 10 metriä, Orionin sumu 2 · 10 potenssiin 17 metriä ja "
            "galaksi Linnunrata 10 potenssiin 21 metriä. Akselin paikat ovat mittakaavassa, kuvakkeiden koot eivät.")
    y0, x0, st = 250, 36, 26.0
    X = lambda e: x0 + (e - 3) * st
    f.arrow(24, y0, 584, y0, INK, 2.5, 13)
    for e in range(4, 24, 2):
        f.line(X(e), y0 - 4, X(e), y0 + (8 if e % 4 == 0 else 5), INK, 2 if e % 4 == 0 else 1.5)
    for e in (4, 8, 12, 16, 20):
        f.tex(X(e), y0 + 28, rf"10^{{{e}}}", "middle", MUTED)
    f.tex(584, y0 + 64, r"d\ (\text{m})", "end")
    iy = 200
    # name labels: (exponent, name, label row y, anchor, label x); a leader runs from under the label down to the icon
    items = [(4.38, "neutronitähti", 50, "start", 14), (7.10, "planeetta", 104, "start", 96), (9.14, "tähti", 152, "end", 222),
             (10.40, "musta aukko", 104, "start", 246), (17.36, "sumu", 50, "middle", None), (20.98, "galaksi", 104, "middle", None)]
    for e, name, ly, anchor, lx in items:
        x = X(e)
        f.line(x, y0 - 6, x, iy + 12, MUTED, 1.5, "4 3")
        f.circle(x, y0, 6, INK, WHITE, 2)
        tip = iy - 18
        if name == "musta aukko": f.line(lx + 4, ly + 16, x + 4, tip, MUTED, 1.5)
        elif ly + 16 < tip - 2: f.line(x, ly + 16, x, tip, MUTED, 1.5)
        f.tex(lx if lx is not None else x, ly, rf"\text{{{name}}}", anchor)
    # icons (not to scale)
    x = X(4.38); f.circle(x, iy, 10, COLD_LIGHT, COLD, 2.5)
    x = X(7.10); f.circle(x, iy, 14, WATER, INK, 2); f.path(f"M{n(x - 7)},{iy - 5} L{n(x + 2)},{iy - 9} L{n(x + 6)},{iy - 2} L{n(x - 2)},{iy + 4} Z", GOOD_LIGHT, GOOD, 1.5)
    x = X(9.14); f.circle(x, iy, 13, HEAT_LIGHT, HEAT, 2.5)
    x = X(10.40); f.circle(x, iy, 15, HEAT_LIGHT, None); f.circle(x, iy, 10, INK, None)
    x = X(17.36); f.add(f'<ellipse cx="{n(x)}" cy="{iy}" rx="22" ry="13" fill="{HOT_LIGHT}" fill-opacity="0.8"/><ellipse cx="{n(x + 6)}" cy="{iy - 3}" rx="13" ry="8" fill="{ICE}" fill-opacity="0.8"/>')
    x = X(20.98); f.add(f'<ellipse cx="{n(x)}" cy="{iy}" rx="24" ry="8" fill="{ICE}" stroke="{COLD}" stroke-width="1.5"/>'); f.circle(x, iy, 4, HEAT_LIGHT, None)
    f.tex(16, 322, r"\text{kuvakkeet eivät ole mittakaavassa}", "start", MUTED)
    return f.svg()


def interactions():
    f = Fig("fy11-forces", 420, "Kaaviokuva, ei mittakaavassa, neljä paneelia. Gravitaatio: Maa kiertää Aurinkoa, ja voima osoittaa Maasta kohti Aurinkoa. "
            "Sähkömagneettinen vuorovaikutus: positiivinen ydin ja negatiivinen elektroni vetävät toisiaan. Vahva vuorovaikutus: protonit ja neutronit "
            "pysyvät ytimessä, ja protonin sisällä on kolme kvarkkia. Heikko vuorovaikutus: beetahajoamisessa neutroni muuttuu protoniksi, ja "
            "syntyy elektroni ja antineutriino.")
    W, H, g = 282, 196, 12
    panels = [(12, 12, "gravitaatio"), (12 + W + g, 12, "sähkömagneettinen"), (12, 12 + H + g, "vahva"), (12 + W + g, 12 + H + g, "heikko")]
    for x, y, name in panels:
        f.rect(x, y, W, H, WHITE, RULE_LIGHT, 2, rx=8)
        f.tex(x + 14, y + 22, rf"\text{{{name}}}", "start", COLD)
    # gravitation: Sun, Earth on its orbit, the force towards the Sun
    x, y = 12, 12
    sx, sy = x + 120, y + 104
    f.add(f'<ellipse cx="{sx}" cy="{sy}" rx="96" ry="44" fill="none" stroke="{MUTED}" stroke-width="1.5" stroke-dasharray="5 4"/>')
    f.circle(sx, sy, 20, HEAT_LIGHT, HEAT, 2.5)
    ex, ey = sx + 96, sy
    f.circle(ex, ey, 10, WATER, INK, 2)
    f.arrow(ex - 13, ey, sx + 32, sy, HOT, 3, 12)
    f.tex(sx + 66, sy - 22, r"\mathbf{F}", "middle", HOT, w=30)
    f.tex(x + W / 2, y + 176, r"\text{Maa kiertää Aurinkoa}", "middle")
    # electromagnetic: a nucleus (+) and an electron (−) attract
    x, y = 12 + W + g, 12
    nx, ny = x + 92, y + 92
    f.circle(nx, ny, 18, HOT, INK, 2); f.tex(nx, ny, r"+", "middle", WHITE, w=24)
    ex = x + 210
    f.circle(ex, ny, 11, COLD, INK, 2); f.tex(ex, ny, r"-", "middle", WHITE, w=20)
    f.arrow(ex - 14, ny, ex - 52, ny, HOT, 3, 12); f.arrow(nx + 21, ny, nx + 59, ny, HOT, 3, 12)
    f.tex(nx, ny + 38, r"\text{ydin}", "middle"); f.tex(ex, ny + 36, r"\text{elektroni}", "middle")
    f.tex(x + W / 2, y + 176, r"\text{atomi pysyy koossa}", "middle")
    # strong: a nucleus and, magnified, a proton with its quarks
    x, y = 12, 12 + H + g
    _nucleus(f, x + 78, y + 110, 34, 12, 6)
    f.line(x + 92, y + 96, x + 168, y + 66, MUTED, 1.5, "4 3"); f.line(x + 92, y + 104, x + 168, y + 146, MUTED, 1.5, "4 3")
    f.circle(x + 90, y + 100, 6, "none", HEAT, 2)
    _proton(f, x + 210, y + 106, 40)
    f.tex(x + W / 2, y + 174, r"\text{ydin pysyy koossa}", "middle")
    # weak: beta decay n -> p + e- + antineutrino
    x, y = 12 + W + g, 12 + H + g
    f.circle(x + 50, y + 104, 18, ALUMINIUM, INK, 2); f.tex(x + 50, y + 104, r"\text{n}", "middle", INK, w=24)
    f.arrow(x + 74, y + 104, x + 132, y + 104, INK, 2.5, 12)
    f.circle(x + 160, y + 104, 18, HOT, INK, 2); f.tex(x + 160, y + 104, r"\text{p}", "middle", WHITE, w=24)
    f.arrow(x + 176, y + 92, x + 226, y + 62, COLD, 2.5, 11); f.circle(x + 236, y + 56, 9, COLD, INK, 2)
    f.tex(x + 254, y + 56, r"\text{e}^-", "start", INK, w=34)
    f.add(f'<line x1="{n(x + 176)}" y1="{n(y + 116)}" x2="{n(x + 222)}" y2="{n(y + 144)}" stroke="{MUTED}" stroke-width="2" stroke-dasharray="4 3"/>')
    f.tex(x + 240, y + 150, r"\bar{\nu}", "middle", MUTED, w=30)
    f.tex(x + W / 2, y + 178, r"\text{beetahajoaminen}", "middle")
    return f.svg()


FIGURES = {"hero": hero, "scale-axis": scale_axis, "ladder": ladder,
           "matter-ladder": matter_ladder, "atom-stadium": atom_stadium, "cosmic-address": cosmic_address,
           "object-types": object_types, "interactions": interactions}
