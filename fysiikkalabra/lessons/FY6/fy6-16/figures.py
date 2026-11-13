"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy6-16` writes them into lesson.md.
The home's electrical system as a schematic (supply, main fuses, groups with their breakers, the charger's own group
with its residual-current device), the evening's phase currents against the 25 A main fuse, the model charging curve
of an electric car (power from the grid against time) and a task variant with a load-managed charge; the opening
illustration is a Finnish red house on a winter evening with an electric car charging at its wall. Every label LaTeX.
Numbers: lesson-answers.py (lesson) and answers.py (tasks)."""
import math
from figlib import Fig, fi, n, INK, MUTED, WHITE, RULE, RULE_LIGHT, HEAT, HEAT_LIGHT, HOT, HOT_LIGHT, COLD, COLD_LIGHT, \
    GLASS, ICE, ALUMINIUM, METAL_EDGE, IRON, COPPER, SAND, SAND_LIGHT, SAND_DARK
import herolib as H

U = 230.0


def energy_grad(f, gid):
    f.defs_add(f'<linearGradient id="{gid}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{HEAT}"/>'
               f'<stop offset="1" stop-color="{HEAT_LIGHT}"/></linearGradient>')
    return f"url(#{gid})"


def cable(f, x1, y1, x2, y2, phases):
    """A cable drawn as its conductors: three parallel lines for a three-phase group, one for a single phase."""
    offs = (-6, 0, 6) if phases == 3 else (0,)
    for o in offs:
        if y1 == y2: f.line(x1, y1 + o, x2, y2 + o, INK, 2)
        else: f.line(x1 + o, y1, x2 + o, y2, INK, 2)


def breaker(f, x, y, w=34, h=50):
    """A miniature circuit breaker on the DIN rail: a white module with a dark toggle."""
    f.rect(x - w / 2, y - h / 2, w, h, WHITE, INK, 2.5, 4)
    f.rect(x - 6, y - 12, 12, 18, INK, None, 0, 2)


def rcd(f, x, y, w=46, h=50):
    """A residual-current device: a wider module with a toggle and a round test button."""
    f.rect(x - w / 2, y - h / 2, w, h, WHITE, INK, 2.5, 4)
    f.rect(x - 14, y - 12, 12, 18, INK, None, 0, 2)
    f.circle(x + 10, y - 2, 6, COLD, INK, 1.5)


# --- Ydinajatus: the home's electrical system -------------------------------------------------------------------
def stove_icon(f, cx, cy):
    f.rect(cx - 36, cy - 14, 72, 44, H.grad(f, "fy616s-stove", IRON, INK, horizontal=True), INK, 2.5, 5)
    for k, (dx, r) in enumerate(((-24, 11), (-4, 13), (18, 11), (-14, 9), (8, 10))):
        dy = -18 if k < 3 else -32
        f.circle(cx + dx, cy + dy, r, IRON if k % 2 else METAL_EDGE, INK, 1.5)
    f.rect(cx - 26, cy + 10, 52, 6, HOT, None, 0, 2)


def kettle_icon(f, cx, cy):
    f.rect(cx - 30, cy + 22, 60, 8, INK, None, 0, 3)
    f.path(f"M{cx - 24},{cy + 22} L{cx - 19},{cy - 22} Q{cx},{cy - 30} {cx + 19},{cy - 22} L{cx + 24},{cy + 22} Z",
           H.steel(f, "fy616s-kettle"), INK, 2.5)
    f.path(f"M{cx + 19},{cy - 18} Q{cx + 44},{cy - 12} {cx + 27},{cy + 16}", stroke=INK, w=6, extra='stroke-linecap="round"')
    f.path(f"M{cx - 20},{cy - 10} L{cx - 38},{cy - 22} L{cx - 23},{cy + 6} Z", H.steel(f, "fy616s-spout"), INK, 2)


def charger_icon(f, cx, cy):
    """A wall box with its holstered plug and a coiled cable."""
    f.rect(cx - 26, cy - 34, 52, 68, H.grad(f, "fy616s-box", WHITE, ALUMINIUM), INK, 2.5, 8)
    f.rect(cx - 14, cy - 24, 28, 12, COLD_LIGHT, INK, 1.5, 2)
    f.circle(cx, cy + 8, 9, IRON, INK, 2)
    f.path(f"M{cx + 26},{cy + 14} q22,6 20,22 q-2,12 -22,10", stroke=INK, w=5, extra='stroke-linecap="round"')


def home():
    f = Fig("fy616-koti", 380, "Kaavakuva, ei mittakaavassa: kodin sähköjärjestelmä. Vasemmalla ylhäältä tulee sähköverkosta kolmen "
            "vaihejohtimen kaapeli sähkökeskukseen. Keskuksessa ovat ensin pääsulakkeet, kolme kappaletta, 25 ampeeria kukin, ja "
            "niiden alla kiskot, joista lähtee kolme ryhmää. Ylin ryhmä on kolmivaiheinen, sen johdonsuojakatkaisija on 16 ampeeria "
            "ja se syöttää sähkökiuasta. Keskimmäinen ryhmä on yksivaiheinen, 16 ampeeria, ja se syöttää keittiön pistorasioita, "
            "joihin on kytketty vedenkeitin. Alin ryhmä on latausaseman oma kolmivaiheinen ryhmä: siinä on 16 ampeerin "
            "johdonsuojakatkaisija ja vikavirtasuoja, jonka laukaisuvirta on 30 milliampeeria. Kolmivaiheiset johdot on piirretty "
            "kolmena viivana, yksivaiheinen yhtenä.")
    # the distribution board, wide enough that every rating sits above its own module, on the board, off the conductors
    f.rect(20, 64, 276, 302, H.grad(f, "fy616s-board", WHITE, ALUMINIUM), INK, 3, 8)
    # supply from the grid: three phase conductors into the main fuses
    for k, x in enumerate((48, 72, 96)):
        f.line(x, 14, x, 82, INK, 2)
        f.rect(x - 9, 82, 18, 40, H.grad(f, f"fy616s-fuse{k}", WHITE, SAND_LIGHT), INK, 2, 4)
        f.rect(x - 9, 82, 18, 7, METAL_EDGE, INK, 1.5, 2)
        f.rect(x - 9, 115, 18, 7, METAL_EDGE, INK, 1.5, 2)
    f.tex(112, 30, r"\text{sähköverkosta}", "start", w=180)
    f.tex(120, 102, r"3 \cdot 25\,\text{A}", "start", w=98)
    # three bus bars
    for x in (48, 72, 96): f.line(x, 122, x, 344, COPPER, 3)
    rows = [(176, 3, r"3 \cdot 16\,\text{A}", r"\text{kiuas}", stove_icon),
            (262, 1, r"16\,\text{A}", r"\text{pistorasiat}", kettle_icon),
            (340, 3, r"3 \cdot 16\,\text{A}", r"\text{latausasema}", charger_icon)]
    for y, ph, rating, name, icon in rows:
        taps = (48, 72, 96) if ph == 3 else (48,)
        for x in taps:
            yo = y + ((x - 72) / 4 if ph == 3 else 0)
            f.circle(x, yo, 4, COPPER)
            f.line(x, yo, 133, yo, INK, 2)
        breaker(f, 150, y)
        f.tex(150, y - 40, rating, "middle", w=98)
        if name == r"\text{latausasema}":
            cable(f, 167, y, 227, y, 3)
            rcd(f, 250, y)
            f.tex(250, y - 40, r"30\,\text{mA}", "middle", w=74)
            cable(f, 273, y, 486, y, 3)
            f.tex(392, y - 26, name, "middle", w=150)
            icon(f, 528, y - 6)
        else:
            cable(f, 167, y, 486, y, ph)
            f.tex(392, y - 26, name, "middle", w=150)
            icon(f, 528, y + (6 if ph == 1 else 6))
    return f.svg()


# --- Ydinajatus: the evening's phase currents against the main fuse ---------------------------------------------
def phases():
    I_s, I_k, I_c = 9000 / (3 * U), 2000 / U, 16.0
    f = Fig("fy616-vaiheet", 340, "Vaakapylväskuvaaja mittakaavassa: pääsulakkeiden läpi kulkeva virta kussakin vaihejohtimessa "
            "L1, L2 ja L3, kun samaan aikaan ovat päällä 9,0 kilowatin kolmivaiheinen kiuas, 2,0 kilowatin vedenkeitin vaiheessa "
            "L1 ja 11 kilowatin kolmivaiheinen latausasema. Kiuas ottaa jokaisesta vaiheesta 13,0 ampeeria ja latausasema 16 "
            "ampeeria, vedenkeitin vaiheesta L1 8,7 ampeeria. Vaiheen L1 virta on 37,7 ampeeria ja vaiheiden L2 ja L3 29,0 "
            "ampeeria. Pystysuora katkoviiva 25 ampeerin kohdalla on pääsulakkeen koko: jokaisen vaiheen pylväs ulottuu "
            "sen yli.")
    x0, x1, imax = 76, 476, 40.0
    X = lambda i: x0 + i / imax * (x1 - x0)
    y_axis = 284
    for t in (10, 20, 30, 40):
        f.line(X(t), 56, X(t), y_axis, RULE_LIGHT, 1.5)
        f.line(X(t), y_axis, X(t), y_axis + 7, INK, 2)
        f.tex(X(t), y_axis + 24, fi(t), "middle")
    f.tex(x0 - 10, y_axis + 20, "0", "end")
    f.arrow(x0 - 1, y_axis, x1 + 26, y_axis, INK, 2.5, 13)
    f.tex(x1 + 32, y_axis, r"I\ (\text{A})", "start", w=64)
    f.line(x0, 56, x0, y_axis, INK, 2.5)
    for k, (ph, parts) in enumerate((("L1", [("kiuas", I_s, SAND_LIGHT), ("auto", I_c, ALUMINIUM), ("keitin", I_k, ICE)]),
                                     ("L2", [("kiuas", I_s, SAND_LIGHT), ("auto", I_c, ALUMINIUM)]),
                                     ("L3", [("kiuas", I_s, SAND_LIGHT), ("auto", I_c, ALUMINIUM)]))):
        yc = 96 + k * 70; h = 46; acc = 0.0
        f.tex(x0 - 12, yc, rf"\text{{{ph[0]}}}_{ph[1]}", "end", w=46)
        for name, I, col in parts:
            f.rect(X(acc), yc - h / 2, X(acc + I) - X(acc), h, col, INK, 2)
            f.tex((X(acc) + X(acc + I)) / 2, yc, rf"\text{{{name}}}", "middle", w=round((X(acc + I) - X(acc)) - 6))
            acc += I
    f.line(X(25), 34, X(25), y_axis, INK, 2.5, "8 6")
    f.tex(X(25), 22, r"\text{pääsulake}\ 25\,\text{A}", "middle", w=210)
    return f.svg()


# --- Kaava: the model charging curve ------------------------------------------------------------------------------
def curve_model():
    """Power from the grid: 11 kW while the battery charges from 20 % to 90 %, then falling exponentially until 1,1 kW (99 %)."""
    P0, Pb, W = 11.0, 0.90 * 11.0, 64.0
    t1 = 0.70 * W / Pb
    tau = 0.10 * W / Pb
    tend = t1 + tau * math.log(10)
    return t1, tau, tend, (lambda t: P0 if t <= t1 else P0 * math.exp(-(t - t1) / tau))


def axes(f, xmax, ymax, xt, yt, origin=(84, 300), corner=(480, 70)):
    from figlib import Axes
    return Axes(f, origin, corner, x=(0, xmax), y=(0, ymax), xticks=xt, yticks=yt,
                xlabel=r"t\ (\text{h})", ylabel=r"P\ (\text{kW})")


def curve():
    t1, tau, tend, P = curve_model()
    f = Fig("fy616-kayra", 360, "Kaavakuva, malli eikä mittaus: sähköauton latausasemalta verkosta otettu teho P kilowatteina ajan t "
            "funktiona tunteina, kun 64 kilowattitunnin akku ladataan 20 prosentin varaustasosta. Teho pysyy 11 kilowatissa noin "
            "4,5 tuntia, kunnes varaustaso on 90 prosenttia. Sen jälkeen teho pienenee yhä hitaammin, ja lataus päättyy noin "
            "6,0 tunnin kohdalla, kun varaustaso on 99 prosenttia. Tasaisen osan alle jäävä pinta-ala on varjostettu: se on "
            "verkosta otettu energia teho kertaa aika.")
    ax = axes(f, 7, 12, [1, 2, 3, 4, 5, 6, 7], [2, 4, 6, 8, 10, 12])
    fill = energy_grad(f, "fy616-energy")
    ax.area([(0, 0), (0, 11), (t1, 11), (t1, 0)], fill, 0.45)
    pts = [(0, 0), (0, 11)] + [(t1 + (tend - t1) * i / 80, P(t1 + (tend - t1) * i / 80)) for i in range(81)] + [(tend, 0)]
    ax.line(pts, HEAT, 3)
    f.tex(ax.X(t1 / 2), ax.Y(5.5), r"W_\text{verkko} = Pt", "middle", w=190, bg=True)
    for t, p, lab, anchor, dx, dy in ((0, 11, r"\text{varaus}\ 20\,\%", "start", 10, -22), (t1, 11, r"\text{varaus}\ 90\,\%", "middle", 0, -22),
                                      (tend, P(tend), r"\text{varaus}\ 99\,\%", "middle", 0, -30)):
        ax.point(t, p, HEAT)
        f.tex(ax.X(t) + dx, ax.Y(p) + dy, lab, anchor, w=150, bg=True)
    return f.svg()


# --- task figure: a charge whose current the load management halved ----------------------------------------------
def task_curve():
    f = Fig("fy616-lataus-ex", 340, "Kuvaaja mittakaavassa: latausaseman verkosta ottama teho P kilowatteina ajan t funktiona "
            "tunteina yhden latauksen aikana. Ruudukon pystyviivat ovat 0,5 tunnin välein, vaakaviivat kohdissa 2, 4, 5,5, 8 ja 11 kilowattia. Teho on ensin 11 kilowattia ajan "
            "0–2,0 tuntia, sitten 5,5 kilowattia ajan 2,0–3,0 tuntia, minkä jälkeen lataus päättyy ja teho on nolla.")
    from figlib import Axes
    ax = Axes(f, (84, 290), (470, 60), x=(0, 3.5), y=(0, 12), xticks=[0.5 * k for k in range(1, 8)],
              yticks=[2, 4, 5.5, 8, 11], xlabel=r"t\ (\text{h})", ylabel=r"P\ (\text{kW})",
              xfmt=lambda v: fi(v) if abs(v - round(v)) < 1e-9 or v == 0.5 else ("" if v == 3.5 else fi(v)),
              )
    ax.line([(0, 11), (2.0, 11), (2.0, 5.5), (3.0, 5.5), (3.0, 0)], HEAT, 3)
    return f.svg()


# --- opening illustration: a red house on a winter evening, an electric car charging at the wall -------------------
def car(f, x, yg, w=380):
    """A compact electric car, its nose to the left; x left end, yg the ground under the wheels."""
    s = w / 380
    X = lambda v: n(x + v * s); Y = lambda v: n(yg - v * s)
    body = (f"M{X(10)},{Y(34)} Q{X(6)},{Y(70)} {X(30)},{Y(80)} L{X(92)},{Y(90)} Q{X(140)},{Y(150)} {X(200)},{Y(152)} "
            f"L{X(270)},{Y(150)} Q{X(320)},{Y(144)} {X(350)},{Y(96)} L{X(368)},{Y(88)} Q{X(376)},{Y(60)} {X(370)},{Y(34)} Z")
    f.path(body, H.grad(f, "fy616h-car", COLD_LIGHT, COLD), INK, 3)
    f.path(f"M{X(112)},{Y(94)} Q{X(150)},{Y(140)} {X(200)},{Y(141)} L{X(204)},{Y(94)} Z", H.grad(f, "fy616h-glass1", GLASS, ICE), INK, 2.5)
    f.path(f"M{X(216)},{Y(94)} L{X(214)},{Y(141)} L{X(268)},{Y(139)} Q{X(304)},{Y(132)} {X(326)},{Y(96)} Z", H.grad(f, "fy616h-glass2", GLASS, ICE), INK, 2.5)
    f.line(x + 210 * s, yg - 94 * s, x + 208 * s, yg - 40 * s, INK, 2)
    f.rect(x + 14 * s, yg - 64 * s, 30 * s, 14 * s, HEAT_LIGHT, INK, 2, 4)     # head lamp
    f.rect(x + 352 * s, yg - 70 * s, 18 * s, 14 * s, HOT, INK, 2, 4)        # tail lamp
    for cx in (82, 300):
        f.circle(x + cx * s, yg - 30 * s, 34 * s, INK)
        f.circle(x + cx * s, yg - 30 * s, 16 * s, ALUMINIUM, METAL_EDGE, 2)
    f.rect(x + 60 * s, yg - 82 * s, 18 * s, 12 * s, IRON, INK, 1.5, 3)       # charging port by the front wheel
    return (x + 69 * s, yg - 76 * s)


def hero():
    f = H.hero("fy616-hero", "Kuvitus: talvi-ilta ja punainen omakotitalo lumen keskellä. Talon ikkunoista loistaa valo, ja "
               "saunan piipusta nousee savua. Talon päätyseinällä on latausasema, josta kiemurteleva latauskaapeli kulkee "
               "pihalla seisovan sinisen sähköauton etuoven alla olevaan latausliitäntään. Taustalla on kuusia ja sähkölinjan "
               "pylväs, josta johdot tulevat talon katolle.")
    f.rect(0, 0, 1200, 600, H.grad(f, "fy616h-sky", COLD, ICE, y1=0, y2=470))
    for k in range(30):
        x, y = 20 + H.rnd(k, 3) * 1160, 16 + H.rnd(k, 5) * 170
        f.circle(x, y, 1.5 + H.rnd(k, 7) * 2, WHITE)
    f.circle(1040, 80, 34, WHITE)
    f.circle(1054, 72, 30, H.grad(f, "fy616h-moon", COLD, ICE, y1=40, y2=110))
    for x, h in ((40, 230), (110, 180), (1150, 210), (1090, 170)):
        H.spruce(f, x, 470, h)
    arms = H.pylon(f, 1000, 470, 250, 0.8)
    f.path("M0,462 Q300,446 600,460 T1200,456 V600 H0 Z", WHITE)
    f.path("M0,520 Q380,500 760,524 T1200,514 V600 H0 Z", ICE, extra='fill-opacity="0.45"')
    # the house, its lit windows and the sauna chimney
    hx, hw, hb, hh = 170, 420, 474, 210
    f.rect(hx + 300, hb - hh - 150, 34, 70, IRON, INK, 3)
    for k in range(3):
        f.circle(hx + 318 + k * 14, hb - hh - 168 - k * 26, 14 + 5 * k, MUTED)
    H.red_house(f, hx, hb, hw, hh, snow=True)
    for k in range(int((hw - 40) / 70)):
        wx = hx + 30 + k * 70
        f.rect(wx + 3, hb - hh * 0.72 + 3, 34, hh * 0.4 - 6, HEAT_LIGHT, None, 0, 2)
        f.line(wx + 20, hb - hh * 0.72, wx + 20, hb - hh * 0.32, WHITE, 3)
    f.rect(hx + hw - 70, hb - 150, 46, 150, SAND_DARK, INK, 3, 3)       # door
    f.circle(hx + hw - 32, hb - 76, 4, INK)
    # the supply wires from the pylon to the roof
    roof = (hx + hw / 2 + 60, hb - hh - 70)
    for a in arms[:2]: H.wire(f, a, roof, 40, INK, 1.5)
    # the wall box on the house's right end and the cable to the car
    bx, by = hx + hw + 34, hb - 150
    f.rect(hx + hw + 10, hb - hh, 60, hh, HOT, INK, 3)                 # gable-end wall
    f.rect(bx - 22, by - 34, 44, 64, H.grad(f, "fy616h-box", WHITE, ALUMINIUM), INK, 2.5, 7)
    f.rect(bx - 12, by - 24, 24, 10, COLD_LIGHT, INK, 1.5, 2)
    f.circle(bx, by + 8, 7, COLD, INK, 1.5)
    port = car(f, 640, 494, 400)
    f.path(f"M{bx},{by + 30} C{bx - 6},{by + 120} {bx + 30},{by + 150} {bx + 70},{by + 140} "
           f"S{port[0] - 30},{port[1] + 60} {port[0]},{port[1] + 4}", stroke=INK, w=6, extra='stroke-linecap="round"')
    f.rect(port[0] - 9, port[1] - 4, 18, 14, IRON, INK, 1.5, 3)
    # light from the windows on the snow
    f.add(f'<path d="M{hx + 30},{hb + 6} L{hx + 10},{hb + 60} H{hx + 330} L{hx + 310},{hb + 6} Z" fill="{HEAT_LIGHT}" fill-opacity="0.22"/>')
    return f.svg()


def task_house():
    f = Fig("fy616-talo-ex", 340, "Kuvaaja mittakaavassa: omakotitalon sähköteho P kilowatteina kellonajan t funktiona illalla kello 18–22. "
            "Ruudukon pystyviivat ovat tunnin välein ja vaakaviivat kohdissa 1, 2, 3, 4, 5, 6, 7 ja 8 kilowattia. "
            "Teho on vakio kunkin tunnin ajan: 2 kilowattia kello 18–19, 5 kilowattia kello 19–20, 7 kilowattia kello 20–21 ja 3 kilowattia kello 21–22.")
    from figlib import Axes
    ax = Axes(f, (84, 290), (470, 60), x=(18, 22), y=(0, 8), xticks=[18, 19, 20, 21, 22],
              yticks=[1, 2, 3, 4, 5, 6, 7, 8], xlabel=r"t\ (\text{h})", ylabel=r"P\ (\text{kW})",
              xfmt=lambda v: str(int(round(v))))
    ax.line([(18, 2), (19, 2), (19, 5), (20, 5), (20, 7), (21, 7), (21, 3), (22, 3)], HEAT, 3)
    return f.svg()


FIGURES = {"hero": hero, "koti": home, "vaiheet": phases, "kayra": curve, "lataus-ex": task_curve, "talo-ex": task_house}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "hero": "decorative",
    "koti": "reveals: the home's groups: 3 x 25 A main fuses, the sauna stove 3 x 16 A, sockets 16 A, the charger's own 3 x 16 A group with a 30 mA RCD",
    "vaiheet": "reveals: the phase currents 37,7 / 29,0 / 29,0 A of stove, kettle and car against the 25 A main fuse",
    "kayra": "reveals: the model charging curve, 11 kW from 20 % to 90 % in about 4,5 h, then falling to 99 % at 6,0 h",
    "lataus-ex": "safe: a charge's (t, P) graph, 11 kW for 0-2,0 h and 5,5 kW for 2,0-3,0 h, no energy written",
    "talo-ex": "safe: a house's (t, P) graph 18-22 h, steps 2, 5, 7 and 3 kW, no energy or cost written",
}
