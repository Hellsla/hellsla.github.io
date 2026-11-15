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

ACCENT = "#1a4d2e"                                        # the site's own dark green (site.css --accent, the buttons)

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
    """The recognition chart (teacher 2026-11-15, replaces the concept map): "Mistä tunnistan, mitä lakia käytän?". One
    card per sign in the task's own words (YO language): the sign on top, the choice it leads to and, as the result in a
    pill in the site's dark green, the law or method; no list of formulas. Stacked for a phone: a spine down the left from
    the start box. A row is (sign, choice, law, pill width, law on a line of its own)."""
    rows = [
        (r"\text{eristetty systeemi}", r"\to\ \text{energia säilyy}", r"E_\text{alussa} = E_\text{lopussa}", 220, True),
        (r"\text{energia ajan kuluessa}", r"\to\ \text{teho}", r"P = \Delta E/\Delta t", 130, False),
        (r"\text{tasainen teho, kesto tiedossa}", r"\to\ \text{energia}", r"E = Pt", 124, False),
        (r"\text{kilowattitunteja}", r"\to\ \text{muunna jouleiksi}", r"1\,\text{kWh} = 3{,}6\,\text{MJ}", 190, True),
        (r"\text{hyötyenergia ja otettu energia}", r"\to\ \text{hyötysuhde}", r"\eta = W_\text{a}/W_\text{o}", 130, False),
        (r"\text{monta laitetta peräkkäin}", r"\to\ \text{kerro hyötysuhteet}", r"\eta = \eta_1\eta_2\eta_3", 150, True),
        (r"\text{polttoaine, lämpöarvo}", r"\to\ \text{palamislämpö}", r"Q = Hm", 100, False),
        (r"\text{voima siirtää matkan}", r"\to\ \text{työ}", r"W = Fs", 124, False),
    ]
    hub_h, x0, x1, ch, gap, top = 72, 30, 372, 72, 14, 98
    heights = [ch + (30 if r[4] else 0) for r in rows]
    ys = [top + sum(heights[:k]) + gap * k for k in range(len(rows))]
    height = ys[-1] + heights[-1] + 8
    f = Fig("fy9en-kartta", height, ARIA_KARTTA, width=380, size=21)
    f.line(14, hub_h + 8, 14, ys[-1] + heights[-1] / 2, RULE, 3)
    f.rect(8, 8, 364, hub_h, SAND_LIGHT, SAND, 2.5, 12)
    f.tex(190, 8 + 26, r"\textbf{mistä tunnistan lain?}", "middle", INK, w=330)
    f.tex(190, 8 + 54, r"\text{energialajit ensin, sitten tunnusmerkki}", "middle", INK, size=17, w=340)
    for (sign, choice, law, pw, wide), y, ch_ in zip(rows, ys, heights):
        f.line(14, y + ch_ / 2, x0, y + ch_ / 2, RULE, 3)
        f.rect(x0, y, x1 - x0, ch_, WHITE, MUTED, 2, 10)
        f.tex(x0 + 14, y + 22, sign, "start", INK, size=19, w=x1 - x0 - 28)
        f.line(x0 + 10, y + 40, x1 - 10, y + 40, RULE_LIGHT, 1.5)
        yy = y + 55
        if wide:                                               # the choice on a line of its own, the law below it
            f.tex(x0 + 14, yy, choice, "start", MUTED, size=17, w=x1 - x0 - 28)
            yy += 30
        else:
            f.tex(x0 + 14, yy, choice, "start", MUTED, size=17, w=x1 - x0 - 28 - pw - 8)
        ph = 28 if "sqrt" in law else 24
        f.rect(x1 - pw - 10, yy - ph / 2 + 1, pw, ph, ACCENT, ACCENT, 2, 8)
        f.tex(x1 - 10 - pw / 2, yy + 1, law, "middle", WHITE, size=17, w=pw - 8)
    return f.svg()


ARIA_KARTTA = ("Tunnistuskaavio: mistä tunnistan, mitä lakia käytän? Aloita luettelemalla energialajit ja katso, mikä "
               "tehtävän tunnusmerkki sopii. Eristetty systeemi: energia säilyy, joten energia alussa on yhtä suuri kuin "
               "energia lopussa. Energia ajan kuluessa: teho on energian muutos jaettuna ajalla. Tasainen teho, kesto "
               "tiedossa: energia on teho kertaa aika. Kilowattitunteja: muunna jouleiksi, yksi kilowattitunti on 3,6 "
               "megajoulea. Hyötyenergia ja otettu energia: hyötysuhde on annettu energia jaettuna otetulla energialla. Monta "
               "laitetta peräkkäin: kerro vaiheiden hyötysuhteet keskenään. Polttoaine, lämpöarvo: palamislämpö on lämpöarvo "
               "kertaa massa. Voima siirtää matkan: työ on voima kertaa matka.")


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
            "leveänä harmaana kaistana. Ensimmäisessä vaiheessa, kattilassa, hyötysuhde on 0,90: kaistasta kääntyy alas oranssi "
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
    # the colours of the model fy2-4/lamp: the incoming energy grey, the useful energy green, the heat orange,
    # each a gradient along its flow
    def grad(gid, x1, y1, x2, y2, c0, c1):
        f.defs_add(f'<linearGradient id="{gid}" gradientUnits="userSpaceOnUse" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}">'
                   f'<stop offset="0" stop-color="{c0}"/><stop offset="1" stop-color="{c1}"/></linearGradient>')
        return f"url(#{gid})"
    g_in = grad("fy9en-in", x0, 0, bounds[2], 0, RULE_LIGHT, RULE)
    g_ok = grad("fy9en-ok", bounds[2], 0, xend + 40, 0, GOOD_LIGHT, GOOD)
    g_heat = grad("fy9en-heat", 0, top, 0, yend + 16, HEAT_LIGHT, HEAT)
    band = " ".join(f"L{xs[i + 1]},{n(top + hs[i])} L{xs[i]},{n(top + hs[i])}" for i in reversed(range(3)))
    f.path(f"M{x0},{top} L{bounds[2]},{top} " + band + " Z", g_in)
    f.path(f"M{bounds[2]},{top} L{xend},{top} L{xend},{top - 10} L{xend + 40},{n(top + hs[3] / 2)} L{xend},{n(top + hs[3] + 10)} "
           f"L{xend},{n(top + hs[3])} L{bounds[2]},{n(top + hs[3])} Z", g_ok, INK, 2)
    f.line(x0, top, bounds[2], top, INK, 2)
    f.line(x0, top, x0, top + hs[0], INK, 2)
    for i in range(3):                         # the bottom edge of the grey band, stage by stage
        f.line(xs[i], top + hs[i], xs[i + 1], top + hs[i], INK, 2)
    centres = [_loss(f, b, top + hs[i], LOSSES[i] * s, radii[i], yend, g_heat, INK) for i, b in enumerate(bounds)]
    for b, e, k in zip(bounds, ETA, (1, 2, 3)):
        f.line(b, 34, b, top - 2, MUTED, 1.5, "5 4")
        f.tex(b, 20, rf"\eta_{k} = {fi(e, 2)}", "middle", INK)
    f.tex(53, top + 100, r"500\,\text{MW}", "middle")
    f.tex(148, top + 100, r"450\,\text{MW}", "middle")
    f.tex(248, top + 36, r"203\,\text{MW}", "middle")
    # the electricity's power and name under its arrow, right of the 4 MW ribbon (size 18 keeps 'electricity' clear of it)
    f.tex(406, top + hs[3] + 32, r"198\,\text{MW}", "end", GOOD, size=18)
    f.tex(406, top + hs[3] + 60, r"\text{sähkö}", "end", GOOD, size=18)
    for i, (xm, L) in enumerate(zip(centres, LOSSES)):
        if i < 2: f.tex(xm, yend + 36, rf"{round(L):d}\,\text{{MW}}", "middle", INK)
    # the 4 MW loss is beside its own arrowhead, clear of the 248 MW under the wide ribbon
    f.tex(centres[2] + 16, yend + 4, rf"{round(LOSSES[2]):d}\,\text{{MW}}", "start", INK)
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
