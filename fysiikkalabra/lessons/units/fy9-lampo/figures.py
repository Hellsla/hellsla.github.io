"""Figures of the FY9 unit fy9-lampo (scripts/figlib.py, herolib.py); `python3 scripts/units.py figures fy9-lampo`
writes them into content/fi/units/fy9-lampo/unit.md. The unit is Finnish, so the decimal sign is a comma.

hero        the Why scene: a winter day at a lean-to shelter (laavu) in Lapland; snow melts in a sooty kettle over a
            campfire, a bucket of snow waits beside it, fells and snowy spruces behind (no text, no people)
kartta      the concept map of the review: energy is conserved, and heating, phase changes, thermal expansion and
            heat transfer hang on it, each with its laws
kayra       the heating curve of the Why question to scale: 1,00 kg of snow at -10 °C warmed, melted, the meltwater
            heated to 100 °C and the boiling begun; the melting and the heating of the water are marked as 334 kJ and 419 kJ
"""
import figlib
from figlib import (Fig, Axes, INK, MUTED, WHITE, RULE, RULE_LIGHT, GLASS, SAND_LIGHT, SAND, SAND_DARK, GRAIN, HEAT_LIGHT, HEAT,
                    HOT, COLD, COLD_LIGHT, ICE, ICE_EDGE, IRON, ALUMINIUM, METAL_EDGE, COPPER, n, fi)
import herolib as H

figlib.set_language({}, ",")

# kayra: 1,00 kg of snow at -10 °C (the FY3 tables: c of ice 2100, s 334 kJ/kg, c of water 4190); kJ
C_ICE, S_ICE, C_WATER = 2.100, 334.0, 4.190          # kJ/(kg K), kJ/kg, kJ/(kg K)
Q_ICE = C_ICE * 1.00 * 10                            # 21 kJ: the snow from -10 °C to 0 °C
Q_MELT = S_ICE * 1.00                                # 334 kJ
Q_WATER = C_WATER * 1.00 * 100                       # 419 kJ: the meltwater from 0 °C to 100 °C
Q1, Q2, Q3 = Q_ICE, Q_ICE + Q_MELT, Q_ICE + Q_MELT + Q_WATER   # 21, 355, 774 kJ


def _snowy_spruce(f, x, ybase, h):
    H.spruce(f, x, ybase, h, "#2b6a3e")
    for w, top in ((0.36, 0.5), (0.28, 0.72), (0.2, 1.0)):       # a cap of snow on each tier
        yt = ybase - h * top
        f.path(f"M{n(x - h * w * 0.42)},{n(yt + h * 0.12)} L{n(x)},{n(yt)} L{n(x + h * w * 0.42)},{n(yt + h * 0.12)} "
               f"Q{n(x)},{n(yt + h * 0.08)} {n(x - h * w * 0.42)},{n(yt + h * 0.12)} Z", WHITE, ICE_EDGE, 1.5)


def hero():
    """A bright winter day in Lapland: a log lean-to on the left, a campfire in the middle with a sooty kettle full of
    snow hanging over it from a tripod, steam rising, a bucket of snow beside the fire, fells and snowy spruces."""
    f = H.hero("fy9la-hero", "Kuvitus: aurinkoinen talvipäivä Lapissa. Vasemmalla hirsinen laavu, jonka katolla on lunta. Laavun edessä "
               "palaa nuotio kivien keskellä, ja sen päällä riippuu kolmijalasta noessa musta pannu, joka on täynnä lunta. Pannusta "
               "nousee höyryä. Nuotion vieressä on sanko lunta. Taustalla on lumisia tuntureita ja kuusia.")
    f.rect(0, 0, 1200, 600, H.grad(f, "fy9la-sky", COLD_LIGHT, GLASS))
    f.add(f'<circle cx="930" cy="214" r="92" fill="{WHITE}" fill-opacity="0.55"/>')
    f.circle(930, 214, 46, SAND_LIGHT)
    H.hills(f, "fy9la-fell", 300, ["#c3d3e0", "#dfe9f1"], amp=70, seed=3)
    H.forest(f, 392, 46, 26, "#2f4a3c", seed=5, depth=16)
    f.path("M0,400 Q300,384 600,396 T1200,392 V600 H0 Z", H.grad(f, "fy9la-snow", WHITE, "#e6eff5"))
    f.path("M0,520 Q360,500 720,514 T1200,506 V600 H0 Z", "#e6eff5")
    for x, h in ((70, 190), (150, 150), (1060, 200), (1150, 160)):
        _snowy_spruce(f, x, 470, h)
    # the lean-to: back wall and roof of logs sloping down to the back, two posts, a log bench, snow on the roof
    f.path("M232,300 L560,262 L560,470 L232,470 Z", "#6b4a2b")                 # the dark inside
    for k in range(7):                                                          # logs of the back wall
        y = 330 + k * 20
        f.rect(240, y, 312, 18, H.grad(f, f"fy9la-log{k}", SAND_DARK, SAND, horizontal=False), INK, 2, 9)
    for k in range(6):                                                          # roof logs, seen from below
        y0 = 300 - k * 8; x0 = 222 + k * 2
        f.path(f"M{x0},{y0} L{570 - k * 2},{262 - k * 8} L{570 - k * 2},{276 - k * 8} L{x0},{y0 + 14} Z", COPPER if k % 2 else "#a0552a", INK, 1.5)
    f.path("M216,258 Q390,226 576,214 L576,222 Q390,236 216,268 Z", WHITE, ICE_EDGE, 2)   # snow on the roof
    for x in (236, 548):                                                         # posts
        f.rect(x - 8, 262 if x > 400 else 296, 16, 470 - (262 if x > 400 else 296), SAND, INK, 2.5, 4)
    f.rect(258, 440, 276, 22, H.grad(f, "fy9la-bench", SAND_DARK, SAND, horizontal=False), INK, 2.5, 10)
    # the fire: glow on the snow, stones, crossed logs, flames
    f.add(f'<ellipse cx="660" cy="508" rx="170" ry="34" fill="{HEAT_LIGHT}" fill-opacity="0.35"/>')
    for k in range(9):
        x = 590 + k * 17.5; f.add(f'<ellipse cx="{n(x)}" cy="{n(510 + 4 * ((k % 2) - 0.5))}" rx="13" ry="9" fill="{IRON if k % 3 else ALUMINIUM}" stroke="{INK}" stroke-width="2"/>')
    f.path("M612,500 L708,470 L714,480 L618,510 Z", COPPER, INK, 2)
    f.path("M606,472 L702,504 L696,512 L600,482 Z", "#a0552a", INK, 2)
    f.path("M624,490 Q620,450 642,424 Q644,446 656,452 Q652,420 668,396 Q676,430 690,444 Q700,428 698,410 Q718,446 704,492 Z",
           H.grad(f, "fy9la-flame", HEAT_LIGHT, HEAT), HOT, 2)
    f.path("M646,490 Q644,466 656,450 Q662,468 672,470 Q676,456 680,448 Q690,470 682,492 Z", HEAT_LIGHT)
    # the tripod and the sooty kettle full of snow, steam rising
    for x0, x1 in ((566, 664), (764, 664), (650, 664)):
        f.line(x0, 520 if x0 != 650 else 528, x1, 246, "#7a5230", 6, cap="round")
    f.line(664, 250, 664, 318, INK, 2.5)
    f.path("M624,322 Q664,300 704,322", stroke=INK, w=3)                        # the handle
    f.path("M618,330 L710,330 L702,392 Q664,404 626,392 Z", INK, INK, 2)        # the kettle
    f.path("M706,346 Q732,342 742,322", stroke=INK, w=7, extra='stroke-linecap="round"')   # spout
    f.path("M614,332 Q626,300 652,306 Q664,288 684,300 Q708,296 714,332 Z", WHITE, ICE_EDGE, 2)   # the heap of snow
    f.add(f'<ellipse cx="664" cy="331" rx="48" ry="5" fill="{ICE}" fill-opacity="0.8"/>')
    H.smoke(f, 676, 262, 0.55, WHITE, 0.85)
    H.smoke(f, 738, 300, 0.4, WHITE, 0.75)
    # a bucket of snow by the fire
    f.path("M842,454 L906,454 L898,520 L850,520 Z", H.steel(f, "fy9la-bucket"), INK, 2.5)
    f.path("M838,456 Q852,426 872,434 Q890,420 910,456 Z", WHITE, ICE_EDGE, 2)
    f.path("M844,454 Q874,404 904,454", stroke=METAL_EDGE, w=2.5)
    return f.svg()


def kartta():
    """The concept map, stacked for a phone: energy is conserved at the top (the balance of heats), a spine down the
    left and four branches, each a box of two laws or ideas with a grey word beside each."""
    f = Fig("fy9la-kartta", 636, "Käsitekartta. Ylhäällä solmu energia säilyy: eristetyssä systeemissä luovutettu lämpömäärä on yhtä suuri kuin "
            "vastaanotettu. Siitä lähtee alas neljä haaraa. Lämpeneminen: Q = c m ΔT, kun olomuoto ei muutu, ja "
            "kelvinlämpötila T = θ + 273,15. Olomuodon muutos: sulaminen Q = s m ja höyrystyminen Q = r m "
            "vakiolämpötilassa. Lämpölaajeneminen: pituus l = l0 kertaa 1 + α ΔT ja tilavuus V = V0 kertaa 1 + γ ΔT. Lämmön "
            "siirtyminen: johtuminen, konvektio ja säteily, sekä seinän läpi johtuva teho P = U A ΔT.", width=380, size=21)
    groups = [
        ("lämpeneminen", [(r"Q = cm\Delta T", "olomuoto sama"), (r"T = \theta + 273{,}15", "kelvinit")]),
        ("olomuodon muutos", [(r"Q = sm", "sulaminen"), (r"Q = rm", "höyrystyminen")]),
        ("lämpölaajeneminen", [(r"l = l_0(1 + \alpha\Delta T)", "pituus"), (r"V = V_0(1 + \gamma\Delta T)", "tilavuus")]),
        ("lämmön siirtyminen", [(r"P = UA\,\Delta T", "seinän läpi"), (r"\text{johtuminen, konvektio, säteily}", "")]),
    ]
    hub_y, hub_h, x_box, gh, top, gap = 8, 76, 44, 120, 104, 12
    spine = 24
    f.line(spine, hub_y + hub_h, spine, top + 3 * (gh + gap) + 22, RULE, 3)
    f.rect(8, hub_y, 364, hub_h, SAND_LIGHT, SAND, 2.5, 12)
    f.tex(190, hub_y + 22, r"\text{energia säilyy}", "middle", INK)
    f.tex(190, hub_y + 54, r"Q_\text{luovutettu} = Q_\text{vastaanotettu}", "middle", INK)
    for k, (head, rows) in enumerate(groups):
        y = top + k * (gh + gap)
        f.line(spine, y + 22, x_box, y + 22, RULE, 3)
        f.rect(x_box, y, 372 - x_box, gh, WHITE, MUTED, 2, 10)
        f.tex(x_box + 14, y + 22, r"\textbf{" + head + "}", "start", INK)
        f.line(x_box + 10, y + 42, 362, y + 42, RULE_LIGHT, 1.5)
        for j, (law, word) in enumerate(rows):
            yy = y + 64 + j * 34
            f.tex(x_box + 14, yy, law, "start", INK, size=19 if law.startswith(r"\text") else None)
            if word: f.tex(362, yy, r"\text{" + word + "}", "end", MUTED, size=18)
    return f.svg()


def kayra():
    """The heating curve of 1,00 kg of snow to scale: T against the energy Q in kJ. The ice warms (0–21 kJ), melts
    (21–355 kJ), the water warms to 100 °C (355–774 kJ) and boiling begins; boiling would go on for 2260 kJ more,
    so the curve ends in an arrow. Brackets mark Q = sm = 334 kJ and Q = cmΔT = 419 kJ."""
    f = Fig("fy9la-kayra", 380, "Kuvaaja mittakaavassa: kilogramman lumen lämpötila T celsiusasteina siirretyn energian Q "
            "funktiona kilojouleina. Lumi lämpenee −10 asteesta 0 asteeseen, kun energiaa on siirtynyt 21 kJ. Sitten lämpötila pysyy "
            "0 asteessa, kunnes energiaa on siirtynyt 355 kJ: sulamiseen kuluu Q = s m = 334 kJ. Sulamisvesi lämpenee 100 asteeseen, "
            "kun energiaa on siirtynyt 774 kJ: tähän kuluu Q = c m ΔT = 419 kJ. Sen jälkeen vesi kiehuu 100 asteessa, ja kuvaaja "
            "jatkuu vaakasuorana nuolena, koska höyrystyminen Q = r m vaatisi vielä 2260 kJ.")
    ax = Axes(f, (96, 318), (480, 64), x=(0, 900), y=(-30, 120), xticks=list(range(100, 901, 100)),
              yticks=list(range(-20, 121, 20)), xlabel=r"Q\ (\text{kJ})", ylabel=r"T\ ({}^\circ\text{C})",
              xfmt=lambda v: fi(v) if v % 200 == 0 else "", yfmt=lambda v: (r"-" + str(-v)) if v < 0 else fi(v),
              origin_label=False)
    f.tex(ax.X(0), ax.y0 + 24, "0", "middle")
    ax.line([(0, -10), (Q1, 0), (Q2, 0), (Q3, 100), (868, 100)], HOT, 3)
    f.arrow(ax.X(868), ax.Y(100), ax.X(900) + 4, ax.Y(100), HOT, 3, 13)
    for q, t in ((0, -10), (Q1, 0), (Q2, 0), (Q3, 100)):
        ax.point(q, t, HOT)
    # brackets: the melting (above the flat part) and the heating of the water (under the rising part)
    def bracket(a, b, t, up):
        y = ax.Y(t); s = -7 if up else 7
        f.path(f"M{n(ax.X(a))},{n(y + s)} V{n(y)} H{n(ax.X(b))} V{n(y + s)}", stroke=MUTED, w=1.5)
    bracket(Q1, Q2, 12, False)
    f.tex(ax.X((Q1 + Q2) / 2), ax.Y(44), r"Q = sm", "middle")
    f.tex(ax.X((Q1 + Q2) / 2), ax.Y(25), r"= 334\,\text{kJ}", "middle")
    bracket(Q2, Q3, -8, True)
    f.tex(ax.X((Q2 + Q3) / 2) + 20, ax.Y(-19), r"Q = cm\Delta T = 419\,\text{kJ}", "middle")
    f.tex(ax.X(900), ax.Y(114), r"Q = rm", "end", HOT)
    return f.svg()


FIGURES = {"hero": hero, "kartta": kartta, "kayra": kayra}
REUSE = {"kartta": "reveals: the key laws of FY3 heat, phase changes, thermal expansion and heat transfer",
         "kayra": "reveals: the heats of melting and heating 1,00 kg of snow, the answer to the unit's Why question"}
