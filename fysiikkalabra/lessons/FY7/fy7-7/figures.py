"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy7-7` writes them into lesson.md.
FY7 colours (course brief): force #c92a2a, velocity #1971c2, current and voltage #7048e8, magnetic field and flux #2b8a3e,
N pole #f2a69c, S pole #d0e6fb; into the page a cross, out of the page a dot in a circle."""
import math
from figlib import (Fig, Axes, fi, INK, MUTED, WHITE, RULE, RULE_LIGHT, HOT, HOT_LIGHT, COLD, COLD_LIGHT, GOOD, GOOD_LIGHT,
                    IRON, COPPER, ALUMINIUM, METAL_EDGE, SAND, SAND_LIGHT, SAND_DARK, GRAIN, GLASS, HEAT, HEAT_LIGHT, ICE,
                    WATER, WATER_LIGHT, PAPER, n)
import herolib as H

VELOCITY, CURRENT, FIELD, NPOLE, SPOLE = COLD, "#7048e8", GOOD, HOT_LIGHT, COLD_LIGHT


def into(f, x, y, r=13, colour=CURRENT):
    """Into the page: a cross in a circle."""
    f.circle(x, y, r, WHITE, colour, 2.5)
    d = r * 0.55
    f.line(x - d, y - d, x + d, y + d, colour, 2.5); f.line(x + d, y - d, x - d, y + d, colour, 2.5)


def out(f, x, y, r=13, colour=CURRENT):
    """Out of the page: a dot in a circle."""
    f.circle(x, y, r, WHITE, colour, 2.5)
    f.circle(x, y, r * 0.32, colour)


def pole(f, x, y, w, h, kind):
    f.rect(x, y, w, h, NPOLE if kind == "N" else SPOLE, INK, 2.5, 4)
    f.tex(x + w / 2, y + h / 2, r"\text{" + kind + "}", "middle")


def ellipse(f, cx, cy, rx, ry, fill, stroke=INK, w=2):
    f.add(f'<ellipse cx="{n(cx)}" cy="{n(cy)}" rx="{n(rx)}" ry="{n(ry)}" fill="{fill}" stroke="{stroke}" stroke-width="{w:g}"/>')


def generator():
    f = Fig("fy77-generator", 360, "Periaatekuva vaihtovirtageneraattorista, ei mittakaavassa. Ylhäällä on magneetin "
            "N-napa ja alhaalla S-napa, joten magneettikenttä osoittaa alaspäin. Napojen välissä on kuparinen käämi, jota "
            "pyöritetään vaakasuoran akselin ympäri. Käämin johtimen päät on kytketty akselilla oleviin kahteen "
            "liukurenkaaseen. Renkaita koskettavat hiiliharjat, ja harjoista johdot kulkevat lamppuun.")
    pole(f, 60, 26, 300, 50, "N")
    pole(f, 60, 294, 300, 50, "S")
    for x in (82, 338):
        f.arrow(x, 84, x, 286, FIELD, 2.5, 13)
    f.tex(348, 150, r"\overline{B}", "start", FIELD)
    # the coil, tilted (a parallelogram), several turns drawn as two outlines
    for o in (0, 7):
        f.path(f"M{130 + o},{116 + o} L{306 - o},{116 + o} L{290 - o},{254 - o} L{114 + o},{254 - o} Z", stroke=COPPER, w=4)
    f.tex(210, 186, r"\text{käämi}", "middle", w=90)
    # the axle: a stub on the left with the sense of rotation, and the shaft to the slip rings on the right
    f.line(54, 185, 118, 185, INK, 4)
    f.path("M64,154 A12,32 0 1 0 74,214", stroke=INK, w=2.5)
    f.path("M74,222 L68,208 L80,209 Z", INK)
    f.line(300, 185, 456, 185, INK, 4)
    # the two leads along the shaft to the rings
    f.line(298, 179, 404, 179, COPPER, 2.5); f.line(298, 191, 434, 191, COPPER, 2.5)
    ellipse(f, 410, 185, 9, 26, COPPER)
    ellipse(f, 440, 185, 9, 26, COPPER)
    # brushes: one under the first ring, one over the second
    f.rect(402, 211, 16, 20, IRON, INK, 2, 2)
    f.rect(432, 139, 16, 20, IRON, INK, 2, 2)
    # wires to a lamp on the right
    f.path("M440,139 V122 H497 V172", stroke=INK, w=2.5)
    f.path("M410,231 V248 H497 V198", stroke=INK, w=2.5)
    f.rect(488, 172, 20, 26, ALUMINIUM, INK, 2, 3)
    for a in (-50, -20, 10, 40):
        r = math.radians(a)
        f.line(530 + 36 * math.cos(r), 185 + 36 * math.sin(r), 530 + 54 * math.cos(r), 185 + 54 * math.sin(r), HEAT, 3, cap="round")
    f.circle(530, 185, 24, HEAT_LIGHT, INK, 2.5)
    f.path("M518,185 q6,-10 12,0 t12,0", stroke=HEAT, w=2)
    f.tex(440, 96, r"\text{hiiliharjat}", "middle", w=150)
    f.line(440, 112, 440, 136, MUTED, 1.5)
    f.tex(452, 282, r"\text{liukurenkaat}", "middle", w=160)
    f.line(425, 266, 425, 215, MUTED, 1.5)
    return f.svg()


def phi_e():
    f = Fig("fy77-phi-e", 440, "Kaksi kuvaajaa samalla aika-akselilla yhden jaksonajan T ajalta. Ylemmässä vihreä "
            "magneettivuo Phi alkaa suurimmasta arvostaan BA, laskee nollaan neljäsosajakson kohdalla, on pienimmillään "
            "miinus BA puolen jakson kohdalla ja palaa arvoon BA. Alemmassa violetti jännite e alkaa nollasta, on suurin e0 "
            "neljäsosajakson kohdalla, nolla puolen jakson kohdalla ja pienin miinus e0 kolmen neljäsosajakson kohdalla. "
            "Katkoviiva neljäsosajakson kohdalla näyttää, että jännite on suurin, kun vuo on nolla. Alimpana pienet kuvat "
            "käämistä päästä katsottuna: kenttä osoittaa oikealle, ja käämin taso on hetkellä nolla kohtisuorassa kenttää "
            "vastaan, neljäsosajakson kohdalla kentän suuntainen ja niin edelleen.")
    xt = [0.25, 0.5, 0.75, 1.0]
    lab = {0.25: r"0{,}25\,T", 0.5: r"0{,}5\,T", 0.75: r"0{,}75\,T", 1.0: r"T"}
    top = Axes(f, (120, 170), (500, 60), x=(0, 1.08), y=(-1.25, 1.25), xticks=xt, yticks=[-1, 0, 1],
               xlabel=r"t", ylabel=r"\Phi", xfmt=lambda v: lab[v],
               yfmt=lambda v: {-1: r"-BA", 0: "0", 1: r"BA"}[v], origin_label=False)
    top.curve(lambda t: math.cos(2 * math.pi * t), 0, 1, FIELD, 3)
    f.tex(top.X(1.0) + 10, top.Y(1.0), r"\Phi", "start", FIELD)
    bot = Axes(f, (120, 330), (500, 230), x=(0, 1.08), y=(-1.25, 1.25), xticks=xt, yticks=[-1, 0, 1],
               xlabel=r"t", ylabel=r"e", xfmt=lambda v: lab[v],
               yfmt=lambda v: {-1: r"-e_0", 0: "0", 1: r"e_0"}[v], origin_label=False)
    bot.curve(lambda t: math.sin(2 * math.pi * t), 0, 1, CURRENT, 3)
    f.tex(bot.X(1.0) + 10, bot.Y(0) - 18, r"e", "start", CURRENT)
    # the quarter period: the flux is zero exactly when the voltage is largest
    xq = top.X(0.25)
    f.line(xq, top.y1, xq, top.y0, MUTED, 1.5, "6 5"); f.line(xq, bot.y1, xq, bot.y0, MUTED, 1.5, "6 5")
    # the coil seen end-on at 0, T/4, T/2, 3T/4 and T: the field to the right, the coil's plane turning
    f.tex(66, 414, r"\overline{B}", "middle", FIELD)
    for k in range(5):
        x, y, th = top.X(0.25 * k), 392, math.pi / 2 * k
        f.arrow(x - 26, 418, x + 26, 418, FIELD, 2, 9)
        dx, dy = 17 * math.sin(th), 17 * math.cos(th)
        f.line(x - dx, y - dy, x + dx, y + dy, COPPER, 4, cap="round")
        f.circle(x - dx, y - dy, 4, INK); f.circle(x + dx, y + dy, 4, INK)
    return f.svg()


def derive():
    th = math.radians(50)
    f = Fig("fy77-derive", 360, "Periaatekuva, ei mittakaavassa: käämi nähdään akselin suunnasta. Vaakasuorat vihreät "
            "kenttäviivat osoittavat oikealle. Käämin taso on vinossa, ja sen kaksi sivua, joiden pituus l on kohtisuoraan "
            "paperia vastaan, ovat ympyröinä: oikean alemman sivun virta kulkee paperiin päin ja vasemman ylemmän paperista "
            "ulos. Sivujen nopeudet, siniset nuolet, ovat kohtisuorassa käämin tasoa vastaan ja vastakkaissuuntaiset. "
            "Oikean sivun nopeuden ja kentän välinen kulma on theeta, ja nopeuden kenttää vastaan kohtisuora komponentti "
            "v sin theeta on piirretty katkoviivalla. Käämin leveys on b.")
    for y in (40, 110, 180, 250, 320):
        f.line(24, y, 576, y, FIELD, 2, None)
        f.path(f"M{n(548)},{y} l-14,-7 v14 Z", FIELD)
    f.tex(560, 18, r"\overline{B}", "end", FIELD, bg=True)
    cx, cy, R = 230, 180, 100
    dxy = (math.sin(th), math.cos(th))            # along the coil's plane, screen coordinates
    nrm = (math.cos(th), -math.sin(th))           # the normal: the direction of the lower side's velocity
    p1 = (cx + R * dxy[0], cy + R * dxy[1]); p2 = (cx - R * dxy[0], cy - R * dxy[1])
    f.line(p2[0], p2[1], p1[0], p1[1], COPPER, 6, cap="round")
    f.circle(cx, cy, 6, INK)
    # the coil's width b beside it
    off = (-dxy[1] * 0, 0)
    f.tex(cx - 30, cy + 8, r"b", "end", INK, bg=True)
    # velocities of the sides
    L = 120
    f.arrow(p1[0] + nrm[0] * 16, p1[1] + nrm[1] * 16, p1[0] + nrm[0] * (16 + L), p1[1] + nrm[1] * (16 + L), VELOCITY, 3.5, 14)
    f.arrow(p2[0] - nrm[0] * 16, p2[1] - nrm[1] * 16, p2[0] - nrm[0] * (16 + L), p2[1] - nrm[1] * (16 + L), VELOCITY, 3.5, 14)
    tip = (p1[0] + nrm[0] * (16 + L), p1[1] + nrm[1] * (16 + L))
    f.tex(tip[0] + 10, tip[1] - 6, r"\overline{v}", "start", VELOCITY, bg=True)
    f.tex(p2[0] - nrm[0] * (16 + L) - 10, p2[1] - nrm[1] * (16 + L) + 4, r"\overline{v}", "end", VELOCITY, bg=True)
    # the angle θ between v and B at the lower side, and the perpendicular component v sin θ
    base = (p1[0] + nrm[0] * 16, p1[1] + nrm[1] * 16)
    f.line(base[0], base[1], base[0] + 150, base[1], MUTED, 1.5, "6 5")
    r = 70
    f.path(f"M{n(base[0] + r)},{n(base[1])} A{r},{r} 0 0 0 {n(base[0] + r * math.cos(th))},{n(base[1] - r * math.sin(th))}", stroke=INK, w=2)
    f.tex(base[0] + 48 * math.cos(th / 2), base[1] - 48 * math.sin(th / 2), r"\theta", "middle")
    cxp = tip[0]
    f.add(f'<line x1="{n(cxp)}" y1="{n(base[1])}" x2="{n(cxp)}" y2="{n(tip[1] + 10)}" stroke="{VELOCITY}" stroke-width="2.5" stroke-dasharray="7 5"/>')
    f.path(f"M{n(cxp)},{n(tip[1])} L{n(cxp - 6)},{n(tip[1] + 12)} L{n(cxp + 6)},{n(tip[1] + 12)} Z", VELOCITY)
    f.tex(cxp + 12, (base[1] + tip[1]) / 2 + 14, r"v\sin\theta", "start", VELOCITY, bg=True)
    into(f, p1[0], p1[1], 14); out(f, p2[0], p2[1], 14)
    f.tex(p1[0] - 22, p1[1] + 20, r"I", "end", CURRENT, bg=True)
    return f.svg()


def power():
    f = Fig("fy77-power", 320, "Kuvaaja: vastuksen teho p ajan t funktiona yhden jaksonajan T ajalta, kun vastukseen on "
            "kytketty sinimuotoinen vaihtojännite. Oranssi käyrä vaihtelee nollan ja huippuarvon P0 välillä ja on nolla "
            "hetkillä 0, puoli jaksoa ja T, ja huipussaan neljäsosa- ja kolmen neljäsosan jakson kohdalla. Katkoviiva "
            "korkeudella puolet P0:sta on tehon keskiarvo: käyrän huiput sen yläpuolella ovat yhtä suuret kuin kuopat sen "
            "alapuolella.")
    lab = {0.25: r"0{,}25\,T", 0.5: r"0{,}5\,T", 0.75: r"0{,}75\,T", 1.0: r"T"}
    ax = Axes(f, (120, 262), (476, 52), x=(0, 1.08), y=(0, 1.12), xticks=[0.25, 0.5, 0.75, 1.0], yticks=[0.5, 1.0],
              xlabel=r"t", ylabel=r"p", xfmt=lambda v: lab[v], yfmt=lambda v: {0.5: r"\tfrac{1}{2}P_0", 1.0: r"P_0"}[v])
    ax.area([(0, 0.5)] + [(t / 120, math.sin(2 * math.pi * t / 120) ** 2) for t in range(0, 121)] + [(1, 0.5)], HEAT_LIGHT, 0.3)
    ax.curve(lambda t: math.sin(2 * math.pi * t) ** 2, 0, 1, HEAT, 3)
    f.line(ax.X(0), ax.Y(0.5), ax.X(1.0), ax.Y(0.5), INK, 2, "8 6")
    f.tex(ax.X(1.0) + 10, ax.Y(0.5), r"\text{keskiarvo}", "start", w=110)
    return f.svg()


def trace(points=True):
    """Task figure: an oscilloscope-like e(t) of a small generator, peak 12 V, period 40 ms, 0–100 ms. No B, N or A."""
    f = Fig("fy77-trace", 340, "Kuvaaja mittakaavassa: generaattorin jännite e voltteina ajan t funktiona millisekunteina "
            "välillä 0–100 ms. Sinimuotoinen violetti käyrä alkaa nollasta, nousee huippuarvoon 12 V hetkellä 10 ms, laskee "
            "nollaan hetkellä 20 ms, pienimpään arvoon −12 V hetkellä 30 ms ja on taas nolla hetkellä 40 ms; sama toistuu. "
            "Ruudukon väli on 10 ms ja 3 V.")
    ax = Axes(f, (100, 300), (500, 66), x=(0, 100), y=(-15, 15), xticks=[10 * k for k in range(1, 11)],
              yticks=[-15 + 3 * k for k in range(0, 11)], xlabel=r"t\ (\text{ms})", ylabel=r"e\ (\text{V})",
              xfmt=lambda v: fi(v) if round(v) % 20 == 0 else "",
              yfmt=lambda v: fi(v) if round(v) % 6 == 0 else "", origin_label=False)
    f.line(ax.X(0), ax.Y(0), ax.X(100), ax.Y(0), MUTED, 2)
    ax.curve(lambda t: 12 * math.sin(2 * math.pi * t / 40), 0, 100, CURRENT, 3, steps=400)
    return f.svg()


def hero():
    """The opening illustration: a wind farm on a Finnish field by the sea, a power line to red houses."""
    f = H.hero("fy77-hero", "Kuvitus: tuulivoimapuisto suomalaisella pellolla meren rannalla. Keskellä on suuri "
               "tuulivoimala, jonka siivet pyörivät, ja sen takana pienempiä voimaloita. Oikealla voimalinja kulkee "
               "pylväiden varassa punaisten talojen luo. Taivaalla on pilviä, ja tuuli taivuttaa koivujen latvoja.")
    f.rect(0, 0, 1200, 600, PAPER)
    H.sky(f, "fy77h", 470, ICE, GLASS)
    H.cloud(f, 230, 110, 1.2); H.cloud(f, 960, 80, 0.9); H.cloud(f, 760, 170, 0.7)
    f.rect(0, 380, 1200, 90, H.grad(f, "fy77h-sea", WATER_LIGHT, WATER))
    H.forest(f, 412, 40, 34, GOOD, seed=3, x0=640, x1=1200, depth=60)
    H.hills(f, "fy77h", 440, [GOOD_LIGHT, GOOD_LIGHT], amp=30, seed=2)
    f.rect(0, 500, 1200, 100, H.grad(f, "fy77h-field", SAND_LIGHT, SAND))
    for k in range(9): f.line(0, 512 + 10 * k, 1200, 508 + 11 * k, SAND_DARK, 2)
    # far turbines on the shore and at sea, then the big one in the middle
    for x, yb, h, turn in ((150, 420, 130, 0.3), (300, 412, 160, 1.1), (840, 440, 170, 0.7), (980, 432, 140, 1.6)):
        H.wind_turbine(f, x, yb, h, turn, 0.8)
    H.wind_turbine(f, 600, 520, 330, 0.2, 1.6)
    a1 = H.pylon(f, 820, 540, 150, 0.9); a2 = H.pylon(f, 1010, 545, 160, 0.95)
    for p, q in zip(a1, a2): H.wire(f, p, q, 24)
    for p in a2[:2]: H.wire(f, p, (1200, p[1] + 20), 16)
    H.red_house(f, 1060, 575, 110, 70)
    H.red_house(f, 60, 572, 120, 72)
    for x in (230, 470, 720):
        H.birch(f, x, 575, 120)
    return f.svg()


def scene():
    """A second everyday scene: a cyclist at dusk, the lamp lit by a hub dynamo in the front wheel."""
    f = H.scene("fy77-scene", "Kuvitus: pyöräilijä ajaa iltahämärässä. Etupyörän navassa on dynamo, joka tuottaa "
                "lampulle vaihtojännitteen, ja lampun valokeila valaisee tietä pyörän edessä.")
    f.rect(0, 0, 600, 360, H.grad(f, "fy77s-sky", INK, WATER))
    H.forest(f, 250, 50, 30, GOOD, seed=5, x0=0, x1=600, depth=40)
    f.rect(0, 286, 600, 74, H.grad(f, "fy77s-road", IRON, INK))
    f.add(f'<path d="M410,214 L600,250 L600,330 Z" fill="{HEAT_LIGHT}" fill-opacity="0.55"/>')
    H.rider(f, 200, 380, 286, 52, frame=HOT, shirt=COLD_LIGHT, helmet=HEAT)
    f.rect(392, 206, 22, 16, ALUMINIUM, INK, 2, 4)
    f.circle(414, 214, 6, HEAT_LIGHT, INK, 2)
    f.circle(380, 286, 11, ALUMINIUM, INK, 2.5)
    f.line(382, 280, 400, 222, INK, 2)
    return f.svg()


# Graph choice of task fy7-7-L1-09: four e(t) graphs on the same axes, U = 5,0 V (effective) and f = 40 Hz given; only
# "pick-u71-t25" is right (peak 5,0 V · √2 ≈ 7,1 V, period 1/f = 25 ms). The other three swap the peak for the effective
# value, the period for the frequency's number in ms, or both: each option shares one feature with two others, so the
# right one cannot be found by its form. The names say the drawn curve, not the answer.
PICK_DESC = ("Kuvaaja mittakaavassa: vaaka-akselilla aika t millisekunteina välillä 0–100 ms, apuviivat 5 ms:n välein ja "
             "lukuarvot 20 ms:n välein; pystyakselilla jännite e voltteina välillä −10 V … 10 V, apuviivat voltin välein ja "
             "lukuarvot kahden voltin välein. ")


def pick_curve(fid, label, peak, period):
    """One option: the same axes and the same violet sine for every option, starting from zero and rising."""
    f = Fig(fid, 406, PICK_DESC + label)
    ax = Axes(f, (100, 366), (500, 66), x=(0, 100), y=(-10, 10), xticks=[5 * k for k in range(1, 21)],
              yticks=[-10 + k for k in range(0, 21)], xlabel=r"t\ (\text{ms})", ylabel=r"e\ (\text{V})",
              xfmt=lambda v: fi(v) if round(v) % 20 == 0 else "",
              yfmt=lambda v: fi(v) if round(v) % 2 == 0 else "", origin_label=False)
    f.line(ax.X(0), ax.Y(0), ax.X(100), ax.Y(0), MUTED, 2)
    f.line(ax.x0 - 7, ax.Y(-10), ax.x0, ax.Y(-10), INK, 2)       # Axes skips the bottom tick: label −10 V by hand
    f.tex(ax.x0 - 12, ax.Y(-10), fi(-10), "end")
    ax.curve(lambda t: peak * math.sin(2 * math.pi * t / period), 0, 100, CURRENT, 3, steps=400)
    return f.svg()


def pick_u71_t25():
    return pick_curve("fy77-pick-u71-t25", "Violetti sinimuotoinen käyrä alkaa nollasta ja nousee huippuarvoon noin 7,1 V "
                      "hetkellä noin 6 ms. Se on nolla hetkillä 12,5 ms ja 25 ms, ja jaksonaika on 25 ms, joten "
                      "käyrässä on neljä täyttä jaksoa. Pienin arvo on noin −7,1 V.", 5.0 * math.sqrt(2), 25)


def pick_u50_t25():
    """The effective value drawn as the peak."""
    return pick_curve("fy77-pick-u50-t25", "Violetti sinimuotoinen käyrä alkaa nollasta ja nousee huippuarvoon 5,0 V "
                      "hetkellä noin 6 ms. Se on nolla hetkillä 12,5 ms ja 25 ms, ja jaksonaika on 25 ms, joten "
                      "käyrässä on neljä täyttä jaksoa. Pienin arvo on −5,0 V.", 5.0, 25)


def pick_u71_t40():
    """The frequency's number read as the period in ms."""
    return pick_curve("fy77-pick-u71-t40", "Violetti sinimuotoinen käyrä alkaa nollasta ja nousee huippuarvoon noin 7,1 V "
                      "hetkellä 10 ms. Se on nolla hetkillä 20 ms ja 40 ms, ja jaksonaika on 40 ms, joten käyrässä on "
                      "kaksi ja puoli jaksoa. Pienin arvo on noin −7,1 V.", 5.0 * math.sqrt(2), 40)


def pick_u50_t40():
    """Both: the effective value as the peak and the frequency's number as the period in ms."""
    return pick_curve("fy77-pick-u50-t40", "Violetti sinimuotoinen käyrä alkaa nollasta ja nousee huippuarvoon 5,0 V "
                      "hetkellä 10 ms. Se on nolla hetkillä 20 ms ja 40 ms, ja jaksonaika on 40 ms, joten käyrässä on "
                      "kaksi ja puoli jaksoa. Pienin arvo on −5,0 V.", 5.0, 40)


FIGURES = {"hero": hero, "generator": generator, "phi-e": phi_e, "derive": derive, "power": power, "scene": scene,
           "trace": trace, "pick-u71-t25": pick_u71_t25, "pick-u50-t25": pick_u50_t25, "pick-u71-t40": pick_u71_t40,
           "pick-u50-t40": pick_u50_t40}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "generator": "reveals: the parts of an AC generator (coil, slip rings, brushes) and that the coil turns in the field",
    "phi-e": "reveals: the voltage is largest when the flux is zero; Φ(t) a cosine, e(t) a sine",
    "derive": "reveals: the sides' velocity component v sin θ perpendicular to B gives the voltage",
    "power": "reveals: the mean power is half the peak power",
    "trace": "safe: e(t) of a generator, peak 12 V, period 40 ms, no N, A or B",
    "pick-u71-t25": "reveals: the right option of task fy7-7-L1-09 (U = 5,0 V, f = 40 Hz: peak 7,1 V, period 25 ms)",
    "pick-u50-t25": "safe: a wrong option of task fy7-7-L1-09 (the effective value drawn as the peak)",
    "pick-u71-t40": "safe: a wrong option of task fy7-7-L1-09 (the frequency's number read as the period in ms)",
    "pick-u50-t40": "safe: a wrong option of task fy7-7-L1-09 (both: effective value as peak, 40 ms period)",
}
