"""Figures of the FY9 unit fy9-energia (scripts/figlib.py, herolib.py); `python3 scripts/units.py figures fy9-energia`
writes them into content/fi/units/fy9-energia/unit.md. The unit is Finnish, so the decimal sign is a comma.

hero        the Why scene: a winter evening, an electric car charging at a house wall; power lines lead to a combined heat
            and power plant and wind turbines on the far shore (no text, no people)
kartta      the concept map of the review: energy is conserved, and power, efficiency, heating value and work hang on it
ketju       an energy-flow (Sankey) diagram to scale of a condensing plant: 500 MW of fuel power through three stages
tehot       the Tutki bar chart, not in unit.md: `PYTHONPATH=scripts python3 lessons/units/fy9-energia/figures.py` pastes
            it into the Tutki text of inquiry.json (figcat ids cannot name a unit's figure)
"""
import math
import figlib
from figlib import (Fig, Axes, INK, MUTED, WHITE, RULE, RULE_LIGHT, GLASS, WATER_LIGHT, WATER, SAND_LIGHT, SAND, HEAT_LIGHT, HEAT,
                    HOT, COLD, COLD_LIGHT, ICE, IRON, ALUMINIUM, METAL_EDGE, GOOD, GOOD_LIGHT, PAPER, n, fi)
import herolib as H

figlib.set_language({}, ",")

# ketju: the example plant of the theory summary (the numbers are computed here and quoted in unit.md)
P0 = 500.0                          # MW, fuel power
ETA = (0.90, 0.45, 0.98)            # boiler, steam cycle (turbine and condenser), generator and transformer
POWERS = [P0]
for e in ETA: POWERS.append(POWERS[-1] * e)          # 500, 450, 202,5, 198,45 MW
LOSSES = [POWERS[i] - POWERS[i + 1] for i in range(3)]  # 50, 247,5, 4,05 MW
ETA_TOTAL = POWERS[-1] / P0                           # 0,3969


def hero():
    """A winter evening in a Finnish suburb: an electric car charges at the wall box of a red house; power lines run to
    a combined heat and power plant (chimney, steam) and wind turbines on the far shore of a frozen lake."""
    f = H.hero("fy9en-hero", "Kuvitus: talvi-ilta. Etualalla punainen omakotitalo, jonka ikkunoista loistaa valoa, ja sen seinän "
               "latauslaitteeseen kytketty sähköauto. Talolta lähtee sähköjohto pylväiden kautta kauas järven yli. Järven toisella "
               "rannalla on voimalaitos, jonka piipusta ja jäähdytyksestä nousee höyryä, ja sen vieressä kolme tuulivoimalaa.")
    sky = H.grad(f, "fy9en-sky", "#24384d", "#6f8fae")
    f.rect(0, 0, 1200, 600, sky)
    for k in range(40):                                   # a few stars in the upper sky
        f.circle(H.rnd(k, 3) * 1200, H.rnd(k + 300, 3) * 190, 1.2 + 1.4 * H.rnd(k + 600, 3), WHITE)
    f.add(f'<circle cx="1040" cy="92" r="34" fill="{SAND_LIGHT}"/>')   # the moon
    f.add(f'<circle cx="1054" cy="84" r="30" fill="#3f5a75"/>')
    # far shore: forest line, the plant and the wind turbines
    H.forest(f, 330, 34, 36, "#2f4a3c", seed=4, depth=20)
    for x, h, t in ((880, 150, 0.3), (960, 130, 1.1), (1040, 140, 2.0)):
        H.wind_turbine(f, x, 330, h, turn=t, sc=0.8)
    # combined heat and power plant: halls, a chimney, steam
    f.rect(470, 268, 170, 62, "#8a96a3", INK, 2.5)
    f.rect(640, 290, 90, 40, "#6c757d", INK, 2.5)
    f.rect(560, 160, 26, 110, ALUMINIUM, INK, 2.5)
    f.rect(560, 170, 26, 10, HOT); f.rect(560, 196, 26, 10, HOT)
    for k in range(5):
        f.rect(486 + k * 30, 284, 16, 18, HEAT_LIGHT, INK, 1.5)
    H.smoke(f, 572, 140, 0.9, WHITE, 0.75)
    H.smoke(f, 690, 270, 0.6, WHITE, 0.6)
    # frozen lake
    f.rect(0, 330, 1200, 80, H.grad(f, "fy9en-lake", "#9fb8c8", ICE))
    for x0, x1, y in ((90, 330, 352), (420, 760, 372), (840, 1130, 360), (200, 520, 392)):
        f.line(x0, y, x1, y, WHITE, 2, cap="round")
    # near shore: snow
    f.path("M0,410 Q300,392 600,404 T1200,400 V600 H0 Z", "#f8fbfd")
    f.path("M0,470 Q320,452 640,466 T1200,462 V600 H0 Z", "#e6eff5")
    # power line from the plant over the lake to the house
    a = H.pylon(f, 330, 410, 120, 0.8)
    b = H.pylon(f, 760, 340, 70, 0.5)
    for i in range(2): H.wire(f, b[i], a[i], 18, INK, 1.5)
    H.wire(f, a[0], (190, 330), 26, INK, 2)
    # spruces
    for x, h in ((40, 150), (96, 120), (1130, 160), (1180, 120)):
        H.spruce(f, x, 470, h, "#2b6a3e")
    # the red house with lit windows (light = energy in use)
    H.red_house(f, 120, 520, 260, 150, snow=True)
    for wx in (150, 220, 290):
        f.rect(wx, 412, 40, 60, HEAT_LIGHT)
        f.rect(wx, 412, 40, 60, "none", INK, 2)
        f.line(wx + 20, 412, wx + 20, 472, WHITE, 3)
    f.add('<path d="M120,520 L380,520 L470,600 L30,600 Z" fill="#ffc078" fill-opacity="0.18"/>')
    # wall box and cable to the car
    f.rect(392, 430, 28, 40, WHITE, INK, 2.5, 4)
    f.circle(406, 444, 5, GOOD)
    f.path("M406,470 Q430,540 520,520 Q560,510 590,500", stroke=INK, w=4, extra='stroke-linecap="round"')
    # electric car (side view, facing left)
    f.path("M560,540 L566,500 Q574,482 600,478 L650,456 Q680,446 730,446 L790,446 Q826,448 850,476 L890,488 Q910,494 912,516 L912,540 Z",
           COLD, INK, 3)
    f.path("M612,478 L656,460 Q684,452 722,452 L722,478 Z", GLASS, INK, 2)
    f.path("M732,452 L786,452 Q812,456 832,478 L732,478 Z", GLASS, INK, 2)
    f.rect(582, 490, 12, 14, WHITE, INK, 1.5, 3)
    f.rect(586, 494, 8, 6, GOOD)
    for cx in (630, 840):
        f.circle(cx, 542, 26, INK); f.circle(cx, 542, 12, ALUMINIUM, INK, 2)
    f.path("M548,560 Q740,572 930,560", stroke="#c9d6e0", w=6, extra='stroke-linecap="round"')
    return f.svg()


def kartta():
    """The concept map, stacked for a phone: the conservation of energy at the top, a spine down the left and three
    branches (power, efficiency, the source of the energy), each a box of three laws with a grey word beside each."""
    f = Fig("fy9en-kartta", 596, "Käsitekartta. Ylhäällä solmu energia säilyy: E alussa on yhtä suuri kuin E lopussa. Siitä lähtee alas kolme "
            "haaraa. Teho: P = ΔE / Δt, energia tehosta E = P t ja kilowattitunti 1 kWh = 3,6 MJ. Hyötysuhde: eeta = E a / "
            "E o, häviöt E o = E a + E h ja energiaketju, jossa eeta on vaiheiden hyötysuhteiden tulo eeta 1 eeta 2 eeta 3. "
            "Energian lähde: polttoaine Q = H m, työ W = F s ja nostotyö W = m g h.", width=380, size=21)
    groups = [
        ("teho", [(r"P = \Delta E/\Delta t", "määritelmä"), (r"E = P\,t", "energia tehosta"),
                  (r"1\,\text{kWh} = 3{,}6\,\text{MJ}", "kilowattitunti")]),
        ("hyötysuhde", [(r"\eta = E_\text{a}/E_\text{o}", "määritelmä"), (r"E_\text{o} = E_\text{a} + E_\text{h}", "häviöt"),
                        (r"\eta = \eta_1\,\eta_2\,\eta_3", "energiaketju")]),
        ("energian lähde", [(r"Q = Hm", "polttoaine"), (r"W = Fs", "työ"), (r"W = mgh", "nostotyö")]),
    ]
    hub_y, hub_h, x_box, gh, top = 8, 72, 44, 150, 100
    spine = 24
    f.line(spine, hub_y + hub_h, spine, top + 2 * (gh + 16) + 22, RULE, 3)
    f.rect(8, hub_y, 364, hub_h, SAND_LIGHT, SAND, 2.5, 12)
    f.tex(190, hub_y + 21, r"\text{energia säilyy}", "middle", INK)
    f.tex(190, hub_y + 51, r"E_\text{alussa} = E_\text{lopussa}", "middle", INK)
    for k, (head, rows) in enumerate(groups):
        y = top + k * (gh + 16)
        f.line(spine, y + 22, x_box, y + 22, RULE, 3)
        f.rect(x_box, y, 372 - x_box, gh, WHITE, MUTED, 2, 10)
        f.tex(x_box + 14, y + 22, r"\textbf{" + head + "}", "start", INK)
        f.line(x_box + 10, y + 42, 362, y + 42, RULE_LIGHT, 1.5)
        for j, (law, word) in enumerate(rows):
            yy = y + 66 + j * 34
            f.tex(x_box + 14, yy, law, "start", INK)
            f.tex(362, yy, r"\text{" + word + "}", "end", MUTED, size=18)
    return f.svg()


def _loss(f, b, ybot, w, R, yend, fill, stroke):
    """A loss ribbon of width w that leaves the bottom of the main band at x = b, turns down and ends in an arrowhead."""
    cy = ybot - w / 2 + R                     # centre of the turn
    ro, ri = R + w / 2, R - w / 2
    head = max(w + 14, 20)
    xm = b + R                                # centre line of the downward part
    d = (f"M{n(b)},{n(ybot - w)} A{n(ro)},{n(ro)} 0 0 1 {n(b + ro)},{n(cy)} L{n(b + ro)},{n(yend)} "
         f"L{n(xm + head / 2)},{n(yend)} L{n(xm)},{n(yend + 16)} L{n(xm - head / 2)},{n(yend)} L{n(b + ri)},{n(yend)} "
         f"L{n(b + ri)},{n(cy)} A{n(ri)},{n(ri)} 0 0 0 {n(b)},{n(ybot)} Z")
    f.path(d, fill, stroke, 1.5)
    return xm


def ketju():
    """Sankey diagram to scale, narrow enough for a phone: 500 MW of fuel power, boiler 0,90, steam cycle 0,45,
    generator 0,98. The band narrows at each stage by the loss, which turns down as a grey ribbon with its power under
    the arrowhead; the electricity leaves to the right in green. The stage names are a key under the figure."""
    f = Fig("fy9en-ketju", 476, "Energiavirtakuvio mittakaavassa lauhdevoimalaitoksesta. Vasemmalta tulee polttoaineteho 500 MW "
            "leveänä kaistana. Ensimmäisessä vaiheessa, kattilassa, hyötysuhde on 0,90: kaistasta kääntyy alas harmaa "
            "häviökaista 50 MW, ja jäljelle jää 450 MW. Toisessa vaiheessa, höyrykierrossa, hyötysuhde on 0,45: alas kääntyy "
            "leveä häviökaista 248 MW, ja jäljelle jää 203 MW. Kolmannessa vaiheessa, generaattorissa ja muuntajassa, "
            "hyötysuhde on 0,98 ja häviö vain 4 MW. Oikealle lähtee vihreä sähkön kaista, 198 MW eli noin 40 prosenttia "
            "polttoainetehosta. Häviöt muuttuvat hukkalämmöksi.", width=420, size=20)
    s = 0.36                                  # px per MW: 500 MW = 180 px
    top, x0, xend = 56, 8, 368
    bounds = (98, 198, 298)
    radii = (22, 50, 18)
    yend = 300
    hs = [p * s for p in POWERS]
    xs = (x0,) + bounds + (xend,)
    for i in range(4):
        f.rect(xs[i], top, xs[i + 1] - xs[i], hs[i], GOOD_LIGHT if i == 3 else SAND_LIGHT)
    f.path(f"M{xend},{n(top - 10)} L{xend + 40},{n(top + hs[3] / 2)} L{xend},{n(top + hs[3] + 10)} Z", GOOD_LIGHT, GOOD, 1.5)
    f.line(x0, top, xend, top, SAND, 1.5)
    centres = [_loss(f, b, top + hs[i], LOSSES[i] * s, radii[i], yend, ALUMINIUM, IRON) for i, b in enumerate(bounds)]
    for b, e, k in zip(bounds, ETA, (1, 2, 3)):
        f.line(b, 34, b, top, MUTED, 1.5, "5 4")
        f.tex(b, 20, rf"\eta_{k} = {fi(e, 2)}", "middle", INK)
    f.tex(53, top + 100, r"500\,\text{MW}", "middle")
    f.tex(148, top + 100, r"450\,\text{MW}", "middle")
    f.tex(248, top + 36, r"203\,\text{MW}", "middle")
    f.tex(334, top + hs[3] / 2, r"198\,\text{MW}", "middle")
    f.tex(400, top + hs[3] + 30, r"\text{sähkö}", "end", GOOD)
    for xm, L in zip(centres, LOSSES):
        f.tex(xm, yend + 36, rf"{round(L):d}\,\text{{MW}}", "middle", MUTED)
    f.tex(8, yend + 36, r"\text{häviöt:}", "start", MUTED)
    f.line(8, yend + 62, 412, yend + 62, RULE_LIGHT, 1.5)
    for j, (k, name) in enumerate(((1, "kattila"), (2, "höyrykierto"), (3, "generaattori ja muuntaja"))):
        f.tex(8, yend + 88 + j * 28, rf"\eta_{k}\ \text{{{name}}}", "start", INK)
    return f.svg()


def tehot():
    """The Tutki graph (pasted into inquiry.json by `python3 lessons/units/fy9-energia/figures.py`): the powers along a
    condensing plant's chain as four bars on 50 MW gridlines, the data of fy3-15/chain-bars in neutral colours (fuel
    and heat sand, electricity green), drawn narrow so that the labels stay large on a phone."""
    f = Fig("fy9en-tehot", 346, "Pylväskuvaaja mittakaavassa: lauhdevoimalaitoksen teho energiaketjun vaiheissa. Pylväiden "
            "korkeudet ovat P_0 = 400 MW (polttoaine), P_1 = 350 MW (kattilan jälkeen), P_2 = 150 MW (höyrykierron jälkeen) "
            "ja P_3 = 140 MW (generaattorin ja muuntajan jälkeen eli sähkö). Ruudukon väli on 50 MW.", width=400, size=21)
    ax = Axes(f, (76, 296), (390, 60), x=(0, 4), y=(0, 450), xticks=[], yticks=list(range(50, 451, 50)),
              xlabel="", ylabel=r"P\ (\text{MW})", yfmt=lambda v: fi(v) if v % 100 == 0 else "")
    for k, (name, v, col) in enumerate((("P_0", 400, SAND_LIGHT), ("P_1", 350, SAND_LIGHT), ("P_2", 150, SAND_LIGHT),
                                        ("P_3", 140, GOOD_LIGHT))):
        x0, x1 = ax.X(k + 0.18), ax.X(k + 0.82)
        f.rect(x0, ax.Y(v), x1 - x0, ax.y0 - ax.Y(v), col, INK, 2)
        f.tex((x0 + x1) / 2, ax.y0 + 24, name, "middle")
    # the x axis stops before the 400-unit viewBox edge (Axes leaves 26 units of arrow room on both axes): the arrow
    # tip at 396, clear of the last bar (right edge 375,5); the y axis keeps its room above the 450 MW gridline
    return f.svg().replace('x2="404" y2="296"', 'x2="384" y2="296"').replace('d="M416,296 L403,302 L403,290 Z"',
                                                                           'd="M396,296 L383,302 L383,290 Z"')


def paste_tehot():
    """Put tehot() into the Tutki text of inquiry.json in place of the graph there."""
    import json, pathlib, re
    p = pathlib.Path(__file__).resolve().parents[3] / "content" / "fi" / "units" / "fy9-energia" / "inquiry.json"
    raw = p.read_text(); d = json.loads(raw)
    a = next(a for a in d["activities"] if a["id"] == "aineisto")
    svg = tehot()
    a["text"] = re.sub(r"<svg .*?</svg>", lambda m: svg, a["text"], flags=re.S) if "<svg" in a["text"] else a["text"] + "\n\n" + svg
    new = json.dumps(d, ensure_ascii=False, indent=1) + "\n"
    if new != raw: p.write_text(new); print("pasted tehot into inquiry.json")


if __name__ == "__main__":
    paste_tehot()


FIGURES = {"hero": hero, "kartta": kartta, "ketju": ketju}
REUSE = {"kartta": "reveals: the key laws of FY2 energy, power and efficiency",
         "ketju": "reveals: the powers and losses of a 500 MW condensing plant and its efficiency"}
