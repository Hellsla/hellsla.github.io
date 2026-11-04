"""Figures of the FY9 unit fy9-liike (scripts/figlib.py, herolib.py); `python3 scripts/units.py figures fy9-liike`
writes them into content/fi/units/fy9-liike/unit.md. The unit is Finnish, so the decimal sign is a comma.

hero        the Why scene: a tram between two stops on a city street, overhead wires, apartment blocks (no text, no people)
kartta      the concept map: the (t,x), (t,v) and (t,a) graphs, slope leading down and area leading up
kuvaajat    one motion in two graphs on one time axis: accelerate from rest, constant speed, brake to a stop; the
            tangent of the (t,x) curve and the area under the (t,v) graph, symbols only
ratikka     the Tutki graph, not in unit.md: `PYTHONPATH=scripts python3 lessons/units/fy9-liike/figures.py` pastes it into
            the Tutki text of inquiry.json (figcat ids cannot name a unit's figure)
"""
import figlib
from figlib import (Fig, Axes, INK, MUTED, WHITE, RULE, RULE_LIGHT, GLASS, SAND_LIGHT, SAND, HEAT, HEAT_LIGHT, HOT, COLD,
                    COLD_LIGHT, ALUMINIUM, METAL_EDGE, IRON, GOOD, GOOD_LIGHT, n, fi)
import herolib as H

figlib.set_language({}, ",")

# ratikka: the tram of the hook and the Tutki task (the numbers are computed here and quoted in inquiry.json)
TRAM = [(0, 0), (10, 10), (40, 10), (60, 0)]      # (s, m/s): 1,0 m/s^2 for 10 s, 30 s at 10 m/s, 0,50 m/s^2 of braking
AREAS = [0.5 * 10 * 10, 30 * 10, 0.5 * 20 * 10]     # 50, 300, 100 m
DIST = sum(AREAS)                                   # 450 m
MEAN = DIST / 60                                     # 7,5 m/s


def tram(f, x, y, length=600, pre="t"):
    """A three-section low-floor tram seen from the side, facing right; (x, y) is the left end at rail level."""
    h, sec = 118, length / 3
    body = H.grad(f, f"{pre}-body", WHITE, "#dfe6ec")
    f.path(f"M{n(x + 12)},{n(y - 14)} L{n(x + 6)},{n(y - h + 18)} Q{n(x + 10)},{n(y - h)} {n(x + 34)},{n(y - h)} "
           f"L{n(x + length - 46)},{n(y - h)} Q{n(x + length - 6)},{n(y - h + 6)} {n(x + length)},{n(y - h + 46)} "
           f"L{n(x + length)},{n(y - 14)} Z", body, INK, 3)
    f.rect(x + 12, y - 44, length - 12, 18, COLD)                         # the blue band
    f.rect(x + 20, y - h - 14, length - 70, 14, ALUMINIUM, INK, 2, 3)     # roof equipment
    for k in (1, 2):                                                       # joints between the sections
        f.rect(x + k * sec - 9, y - h + 6, 18, h - 22, "#c9d2da", INK, 2)
    for k in range(3):
        x0 = x + k * sec
        for j in range(3):                                                 # windows
            wx = x0 + 26 + j * (sec - 52) / 3
            f.rect(wx, y - h + 22, (sec - 52) / 3 - 10, 46, GLASS, INK, 2, 6)
        f.rect(x0 + sec / 2 - 18, y - h + 22, 36, h - 40, "#9fb8c8", INK, 2, 4)   # door
        f.line(x0 + sec / 2, y - h + 24, x0 + sec / 2, y - 20, INK, 1.5)
    f.path(f"M{n(x + length - 40)},{n(y - h + 6)} Q{n(x + length - 8)},{n(y - h + 12)} {n(x + length - 4)},{n(y - h + 46)} "
           f"L{n(x + length - 40)},{n(y - h + 46)} Z", GLASS, INK, 2)    # driver's window
    f.circle(x + length - 10, y - 30, 6, HEAT_LIGHT, INK, 1.5)            # head light
    for k in range(3):                                                     # bogies and wheels
        cx = x + (k + 0.5) * sec
        f.rect(cx - 50, y - 18, 100, 12, IRON, INK, 2, 3)
        for dx in (-30, 30): f.circle(cx + dx, y - 6, 11, INK); f.circle(cx + dx, y - 6, 4, ALUMINIUM)
    # pantograph to the wire
    px = x + length / 2 + 40
    f.line(px - 30, y - h - 14, px, y - h - 52, INK, 2.5); f.line(px + 30, y - h - 14, px, y - h - 52, INK, 2.5)
    f.line(px - 24, y - h - 52, px + 24, y - h - 52, INK, 3, cap="round")


def shelter(f, x, y):
    """A tram stop: a glass shelter with a roof and a pole, standing on the platform edge at (x, y)."""
    f.rect(x - 70, y - 150, 140, 12, IRON, INK, 2, 3)
    f.rect(x - 64, y - 138, 128, 138, GLASS, INK, 2.5)
    f.line(x - 64, y - 70, x + 64, y - 70, METAL_EDGE, 2)
    f.rect(x - 50, y - 44, 100, 10, SAND, INK, 1.5, 2)                    # bench
    f.rect(x + 86, y - 176, 8, 176, ALUMINIUM, INK, 2)                    # stop pole with a sign plate
    f.rect(x + 74, y - 206, 32, 32, COLD, INK, 2, 6)
    f.circle(x + 90, y - 190, 8, WHITE)


def hero():
    """A summer morning on a city street: a tram runs between two stops under the overhead wire; apartment blocks and
    birches behind. Speed streaks behind the tram say that it moves; nothing tells how far it is between the stops."""
    f = H.hero("fy9li-hero", "Kuvitus: kaupungin katu kesäaamuna. Kadun keskellä kulkee raitiovaunu kiskoja pitkin oikealle, "
               "ja sen takana on liikeviivoja. Vasemmalla ja oikealla on lasiset raitiovaunupysäkit. Vaunun yllä kulkee ajojohdin "
               "pylväiden välissä. Taustalla on kerrostaloja ja koivuja. Kuvassa ei ole tekstiä eikä ihmisiä.")
    H.sky(f, "fy9li", 420, "#bfdcf2", GLASS)
    H.cloud(f, 240, 90, 0.9); H.cloud(f, 860, 70, 1.1); H.cloud(f, 1080, 140, 0.6)
    # apartment blocks
    for x, w, h, col in ((20, 220, 250, SAND_LIGHT), (250, 180, 300, "#e9dcc8"), (450, 240, 230, "#f3e6d0"),
                         (720, 200, 280, SAND_LIGHT), (940, 240, 250, "#e9dcc8")):
        f.rect(x, 400 - h, w, h, col, INK, 2.5)
        for r in range(int((h - 40) // 52)):
            for c in range(int((w - 30) // 46)):
                f.rect(x + 22 + c * 46, 400 - h + 26 + r * 52, 26, 30, GLASS, INK, 1.5)
    for x, h in ((200, 150), (690, 170), (1160, 160)):
        H.birch(f, x, 410, h)
    # pavement, platforms, street
    f.rect(0, 400, 1200, 34, "#d8d2c4")
    f.line(0, 400, 1200, 400, INK, 2)
    f.rect(0, 434, 1200, 166, "#8a939c")
    f.rect(0, 434, 1200, 166, "none", INK, 2)
    f.rect(0, 524, 1200, 14, "#6c757d")                                     # the track bed
    for y in (528, 536): f.line(0, y, 1200, y, ALUMINIUM, 3)
    for x in range(10, 1200, 40): f.rect(x, 538, 20, 6, IRON)
    for x in range(40, 1200, 180): f.rect(x, 572, 90, 8, WHITE)             # lane marks
    # overhead wire and poles
    for x in (110, 600, 1090):
        f.rect(x - 5, 230, 10, 204, IRON, INK, 2)
        f.line(x, 318, x + (60 if x < 600 else -60), 318, INK, 3)
    H.wire(f, (0, 336), (1200, 336), 8, INK, 2.5)
    # stops on both sides
    shelter(f, 150, 434)
    shelter(f, 1040, 434)
    # the tram and its speed streaks
    tram(f, 330, 528, 560, "fy9li-tram")
    for y, x0, L in ((440, 200, 110), (468, 230, 90), (496, 190, 120)):
        f.line(x0, y, x0 + L, y, WHITE, 5, cap="round")
    return f.svg()


def kartta():
    """The concept map, stacked for a phone: three graph boxes (t,x), (t,v), (t,a), each with a sketch of uniform and
    uniformly accelerated motion; on the right the slope leads down a level, on the left the area leads up."""
    f = Fig("fy9li-kartta", 600, "Käsitekartta kolmesta kuvaajasta päällekkäin. Ylimpänä paikan kuvaaja, jossa tasaisen liikkeen "
            "suora ja tasaisesti kiihtyvän liikkeen ylöspäin kaartuva käyrä. Keskellä nopeuden kuvaaja, jossa vaakasuora suora ja "
            "nouseva suora. Alimpana kiihtyvyyden kuvaaja, jossa nolla ja vakio. Oikealla nuolet alaspäin: kuvaajan kulmakerroin on "
            "seuraavan suureen arvo, v = Δx/Δt ja a = Δv/Δt. Paikan kuvaajat ovat mustia, nopeuden sinisiä ja kiihtyvyyden oransseja; "
            "tasainen liike on yhtenäinen ja tasaisesti kiihtyvä katkoviiva. Vasemmalla nuolet ylöspäin: kuvaajan ja aika-akselin välinen pinta-ala on "
            "edellisen suureen muutos, Δx ja Δv.", width=400, size=21)
    rows = [(r"(t,x)", "paikka", lambda u: 0.75 * u, lambda u: 0.15 * u + 0.85 * u * u, INK),
            (r"(t,v)", "nopeus", lambda u: 0.55, lambda u: 0.12 + 0.8 * u, COLD),
            (r"(t,a)", "kiihtyvyys", lambda u: 0.0, lambda u: 0.55, HEAT)]
    bx, bw, bh, gap, top = 92, 216, 136, 52, 14
    for k, (name, word, flat, accel, col) in enumerate(rows):
        y = top + k * (bh + gap)
        f.rect(bx, y, bw, bh, WHITE, MUTED, 2, 10)
        f.tex(bx + 12, y + 20, name, "start", INK)
        f.tex(bx + bw - 12, y + 20, r"\text{" + word + "}", "end", MUTED, size=18)
        # a small graph: axes, then the two sketches in the quantity's colour (solid: uniform, dashed: uniformly
        # accelerated); position ink, velocity blue, acceleration orange
        ox, oy, w, h = bx + 24, y + bh - 16, bw - 52, bh - 56
        f.line(ox, oy, ox + w + 8, oy, INK, 2); f.line(ox, oy, ox, oy - h - 8, INK, 2)
        pts = lambda fn: " ".join(f"{n(ox + w * i / 20)},{n(oy - h * fn(i / 20))}" for i in range(21))
        f.add(f'<polyline points="{pts(flat)}" fill="none" stroke="{col}" stroke-width="3" stroke-linecap="round"/>')
        f.add(f'<polyline points="{pts(accel)}" fill="none" stroke="{col}" stroke-width="3" stroke-dasharray="9 6" stroke-linecap="round"/>')
        if k < 2:                                                               # the arrows to the next box
            ya, yb = y + bh + 6, y + bh + gap - 6
            f.arrow(bx + bw + 30, ya, bx + bw + 30, yb, INK, 3, 13)
            f.arrow(bx - 30, yb, bx - 30, ya, GOOD, 3, 13)
            f.tex(bx + bw + 44, (ya + yb) / 2, r"\tfrac{\Delta x}{\Delta t}" if k == 0 else r"\tfrac{\Delta v}{\Delta t}", "start", INK)
            f.tex(bx - 44, (ya + yb) / 2, r"\Delta x" if k == 0 else r"\Delta v", "end", GOOD)
    yk = top + 3 * (bh + gap) - gap + 26                                        # the key
    f.line(14, yk - 18, 386, yk - 18, RULE_LIGHT, 1.5)
    f.tex(14, yk + 6, r"\downarrow\ \text{kulmakerroin}", "start", INK)
    f.tex(386, yk + 6, r"\uparrow\ \text{pinta-ala}", "end", GOOD)
    f.line(14, yk + 38, 50, yk + 38, INK, 3)
    f.tex(58, yk + 38, r"\text{tasainen}", "start", MUTED, size=18)
    f.line(150, yk + 38, 186, yk + 38, INK, 3, "9 6")
    f.tex(194, yk + 38, r"\text{tasaisesti kiihtyvä}", "start", MUTED, size=18)
    return f.svg()


def kuvaajat():
    """One motion in two graphs that share the time axis: from rest the speed grows (0..t1), stays (t1..t2) and falls to
    zero (t2..t3). Top: the (t,x) curve with the tangent at a point of the first phase; bottom: the (t,v) graph with the
    area under it shaded green and the velocity at that point marked. Symbols only (a schematic, not to scale in x)."""
    f = Fig("fy9li-kuvaajat", 650, "Kaavakuva yhdestä liikkeestä kahtena kuvaajana, joilla on sama aika-akseli. Alhaalla nopeuden "
            "kuvaaja: nopeus kasvaa nollasta tasaisesti hetkeen t1, pysyy vakiona hetkeen t2 ja pienenee tasaisesti nollaan hetkellä "
            "t3. Kuvaajan alle jäävä alue on väritetty vihreäksi, ja sen pinta-ala on siirtymä Δx. Ylhäällä paikan kuvaaja: ensin "
            "ylöspäin kaartuva käyrä, sitten nouseva suora ja lopuksi käyrä, joka loivenee vaakasuoraksi. Paikka kasvaa koko "
            "liikkeen ajan yhteensä Δx. Käyrän pisteeseen P on piirretty sininen tangentti, jonka kulmakerroin k on nopeus v_P; sama "
            "arvo on merkitty alempaan kuvaajaan.", width=440, size=21)
    t1, t2, t3, V = 2.0, 5.0, 7.0, 4.0
    def v(t): return V * t / t1 if t < t1 else V if t < t2 else V * (t3 - t) / (t3 - t2)
    def x(t):
        if t < t1: return 0.5 * V / t1 * t * t
        x1 = 0.5 * V * t1
        if t < t2: return x1 + V * (t - t1)
        x2 = x1 + V * (t2 - t1); u = t - t2
        return x2 + V * u - 0.5 * V / (t3 - t2) * u * u
    X3 = x(t3)
    ticks = dict(xticks=[t1, t2, t3], xfmt=lambda t: "", grid=False, origin_label=False, arrow_room=22)
    top = Axes(f, (50, 280), (360, 70), x=(0, 8), y=(0, X3 * 1.08), yticks=[], xlabel=r"t", ylabel=r"x", **ticks)
    bot = Axes(f, (50, 590), (360, 410), x=(0, 8), y=(0, V * 1.3), yticks=[], xlabel=r"t", ylabel=r"v", **ticks)
    bot.area([(0, 0), (t1, V), (t2, V), (t3, 0)], GOOD_LIGHT, 0.8)
    for t in (t1, t2):                                                           # the phase borders through both graphs
        f.line(top.X(t), top.Y(x(t)), top.X(t), bot.Y(v(t)), MUTED, 1.5, "6 5")
    f.line(top.X(t3), top.Y(X3), top.X(t3), bot.y0, MUTED, 1.5, "6 5")
    top.curve(x, 0, t3, INK, 3)
    top.line([(t3, X3), (7.8, X3)], INK, 3)
    bot.line([(0, 0), (t1, V), (t2, V), (t3, 0), (7.8, 0)], COLD, 3.5)
    tp = 1.4                                                                     # the tangent at P
    s = V * tp / t1
    top.line([(tp - 0.35, x(tp) - s * 0.35), (tp + 1.4, x(tp) + s * 1.4)], COLD, 2.5, dash="8 6")   # slope = velocity: blue
    f.line(top.X(tp), top.Y(x(tp)), top.X(tp), bot.Y(v(tp)), COLD, 1.5, "3 4")
    top.point(tp, x(tp), INK, 7)
    f.tex(top.X(tp) - 12, top.Y(x(tp)) - 4, r"P", "end")
    f.tex(top.X(2.95), top.Y(X3 * 0.15), r"k = v_\text{P}", "start", COLD)                       # right of the tangent's end, under the curve
    bot.point(tp, v(tp), INK, 7)
    f.tex(bot.X(tp) - 12, bot.Y(v(tp)) - 14, r"v_\text{P}", "end", INK)
    f.tex(bot.X(3.5), bot.Y(V * 0.45), r"\Delta x", "middle", GOOD)
    # Δx on the top graph: a bracket from 0 to X3 at the right
    xb = top.X(7.9)
    f.line(xb - 6, top.Y(0), xb, top.Y(0), GOOD, 2); f.line(xb - 6, top.Y(X3), xb, top.Y(X3), GOOD, 2)
    f.line(xb, top.Y(0), xb, top.Y(X3), GOOD, 2.5)
    f.tex(xb + 8, top.Y(X3 / 2), r"\Delta x", "start", GOOD)
    for t, lab in ((t1, "t_1"), (t2, "t_2"), (t3, "t_3")):
        f.tex(bot.X(t), bot.y0 + 24, lab, "middle")
    f.tex(bot.X(0) - 10, bot.y0 + 20, "0", "end")
    f.tex(top.X(0) - 10, top.y0 + 20, "0", "end")
    return f.svg()


def ratikka():
    """The Tutki graph (pasted into inquiry.json by `python3 lessons/units/fy9-liike/figures.py`): the tram's (t,v) graph
    between two stops on 10 s and 2 m/s gridlines, every corner on a grid crossing, nothing shaded or computed."""
    f = Fig("fy9li-ratikka", 360, "Kuvaaja mittakaavassa: raitiovaunun nopeus v ajan t funktiona pysäkiltä seuraavalle. Ruudukon "
            "väli on 10 s ja 2 m/s. Nopeus kasvaa tasaisesti nollasta nopeuteen 10 m/s hetkeen 10 s, pysyy 10 metrissä sekunnissa "
            "hetkeen 40 s ja pienenee tasaisesti nollaan hetkellä 60 s.", width=440, size=21)
    ax = Axes(f, (64, 300), (336, 52), x=(0, 60), y=(0, 12), xticks=list(range(10, 61, 10)), yticks=list(range(2, 13, 2)),
              xlabel=r"t\ (\text{s})", ylabel=r"v\ (\text{m/s})", xfmt=lambda v: fi(v) if v % 20 == 0 else "")
    ax.line(TRAM, COLD, 3.5)
    for p in TRAM: ax.point(*p, COLD)
    return f.svg()


def paste_ratikka():
    """Put ratikka() into the Tutki text of inquiry.json in place of the graph there."""
    import json, pathlib, re
    p = pathlib.Path(__file__).resolve().parents[3] / "content" / "fi" / "units" / "fy9-liike" / "inquiry.json"
    raw = p.read_text(); d = json.loads(raw)
    a = next(a for a in d["activities"] if a["id"] == "aineisto")
    svg = ratikka()
    a["text"] = re.sub(r"<svg .*?</svg>", lambda m: svg, a["text"], flags=re.S) if "<svg" in a["text"] else a["text"] + "\n\n" + svg
    new = json.dumps(d, ensure_ascii=False, indent=1) + "\n"
    if new != raw: p.write_text(new); print("pasted ratikka into inquiry.json")


if __name__ == "__main__":
    paste_ratikka()


FIGURES = {"hero": hero, "kartta": kartta, "kuvaajat": kuvaajat}
REUSE = {"kartta": "reveals: slope and area links between the (t,x), (t,v) and (t,a) graphs",
         "kuvaajat": "reveals: the tangent as velocity and the area under (t,v) as displacement (schematic)"}
