"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy5-13` writes them into lesson.md.
Colours: the standing wave (the sum) water blue #2f74b5 with its swing between the envelopes in light blue, the wave
travelling towards the fixed end orange #e8590c (dashed), the reflected wave violet #7048e8 (dotted), nodes ink dots.
Force red is never used for a displacement."""
import math
from figlib import (Fig, INK, MUTED, WHITE, RULE, RULE_LIGHT, GLASS, WATER_LIGHT, WATER, SAND_LIGHT, SAND, SAND_DARK, GRAIN,
                    HEAT, ALUMINIUM, METAL_EDGE, IRON, COPPER, ICE, ICE_EDGE, COLD_LIGHT, HOT, PAPER, n)
import herolib as H

WAVE, INC, REF = WATER, HEAT, "#7048e8"


def poly(f, pts, color, w=3, dash=None, extra=""):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    p = " ".join(f"{n(x)},{n(y)}" for x, y in pts)
    return f.add(f'<polyline points="{p}" fill="none" stroke="{color}" stroke-width="{w:g}" stroke-linejoin="round" stroke-linecap="round"{d}{(" " + extra) if extra else ""}/>')


def lens(f, x0, x1, yc, amp, shape, steps=160, fill=WATER_LIGHT, line=WAVE, dashed_other=True):
    """The swing of a standing wave between its two extreme shapes: light fill between +env and −env, one extreme
    solid, the other dashed. shape(u) for u in [0, 1] gives the signed shape (−1 … 1)."""
    up = [(x0 + (x1 - x0) * i / steps, yc - amp * shape(i / steps)) for i in range(steps + 1)]
    dn = [(x, 2 * yc - y) for x, y in up]
    f.add(f'<polygon points="{" ".join(f"{n(x)},{n(y)}" for x, y in up + dn[::-1])}" fill="{fill}" fill-opacity="0.55"/>')
    poly(f, up, line, 3)
    if dashed_other: poly(f, dn, line, 2, "7 6")


def clamp(f, x, yc, side):
    """A fixed end: a short ink block with hatching on its outer side."""
    w = 14
    x0 = x if side == "right" else x - w
    f.rect(x0, yc - 34, w, 68, ALUMINIUM, INK, 2.5, 2)
    for k in range(5):
        y = yc - 30 + 15 * k
        xo = x0 + w if side == "right" else x0
        f.line(xo, y, xo + (8 if side == "right" else -8), y + 8, INK, 1.5)


def superposition():
    f = Fig("fy513-sup", 386, "Kaavakuva kolmena hetkenä allekkain, ei mittakaavassa: narun oikea pää on kiinni seinässä. Oranssi "
            "katkoviiva on seinää kohti etenevä aalto ja violetti pisteviiva seinästä heijastunut aalto, jolla on sama "
            "amplitudi ja aallonpituus. Sininen yhtenäinen viiva on niiden summa eli narun todellinen muoto. Ylimmällä "
            "hetkellä tuleva ja heijastunut aalto ovat päällekkäin ja summa on suurimmillaan, keskimmäisellä pienempi ja alimmalla nolla, kun aallot kumoavat toisensa. "
            "Mustat pisteet merkitsevät kohtia, joissa summa on joka hetkellä nolla: ne ovat puolen aallonpituuden välein, "
            "ja yksi niistä on seinän kohdalla.")
    x0, x1 = 112, 540
    lam = (x1 - x0) / 2
    amp = 22
    # legend
    for x, col, dash, w, txt in ((120, INC, "8 6", 2.5, r"\text{tuleva}"), (268, REF, "2 5", 3, r"\text{heijastunut}"), (456, WAVE, None, 3.5, r"\text{summa}")):
        f.line(x, 26, x + 34, 26, col, w, dash, "round")
        f.tex(x + 42, 26, txt, "start")
    f.line(12, 50, 588, 50, RULE_LIGHT, 1.5)
    rows = ((105, 0.0, r"t = 0"), (210, math.pi / 4, r"t = \tfrac{T}{8}"), (315, math.pi / 2, r"t = \tfrac{T}{4}"))
    for yc, wt, lab in rows:
        f.line(x0, yc, x1, yc, RULE, 1.5, "4 5")
        # the wall at the fixed end
        f.rect(x1 + 4, yc - 40, 14, 80, SAND_LIGHT, INK, 2)
        for k in range(5): f.line(x1 + 6, yc - 34 + 16 * k, x1 + 16, yc - 26 + 16 * k, GRAIN, 1.5)
        k = 2 * math.pi / lam
        pts = lambda fn: [(x0 + (x1 - x0) * i / 200, yc - fn((x1 - (x0 + (x1 - x0) * i / 200)))) for i in range(201)]
        poly(f, pts(lambda s: amp * math.sin(wt + k * s)), INC, 2.5, "8 6")
        poly(f, pts(lambda s: -amp * math.sin(wt - k * s)), REF, 3, "2 5")
        poly(f, pts(lambda s: 2 * amp * math.cos(wt) * math.sin(k * s)), WAVE, 3.5)
        for m in range(5): f.circle(x1 - m * lam / 2, yc, 5.5, INK, WHITE, 1.5)
        f.tex(16, yc, lab, "start")
    for m in range(5): f.tex(x1 - m * lam / 2, 364, r"\text{S}", "middle")
    return f.svg()


def nodes():
    f = Fig("fy513-nodes", 338, "Kaavakuva seisovasta aallosta, ei mittakaavassa. Sininen yhtenäinen viiva on narun muoto yhdellä "
            "hetkellä ja sininen katkoviiva puolen jaksonajan päästä; vaalea alue niiden välissä on alue, jossa naru liikkuu. "
            "Mustat pisteet S ovat solmuja, joissa naru ei liiku. Niiden puolivälissä ovat kuvut K, joissa liike on "
            "suurin. Kahden vierekkäisen solmun etäisyys on merkitty puoleksi aallonpituudeksi ja solmun etäisyys "
            "viereisestä kuvusta neljännekseksi aallonpituudesta.")
    x0, x1, yc, amp = 60, 540, 160, 66
    lam = (x1 - x0) / 2
    f.line(x0 - 20, yc, x1 + 20, yc, RULE, 1.5, "4 5")
    lens(f, x0, x1, yc, amp, lambda u: math.sin(2 * math.pi * u * 2))
    for m in range(5):
        x = x0 + m * lam / 2
        f.circle(x, yc, 6, INK, WHITE, 2)
        f.tex(x, 252, r"\text{S}", "middle")
        f.line(x, 236, x, yc + 12, MUTED, 1.5, "3 4")
    for m in range(4):
        x = x0 + lam / 4 + m * lam / 2
        top = yc - amp if m % 2 == 0 else yc - amp
        f.tex(x, top - 22, r"\text{K}", "middle")
    # spacing brackets under the figure
    def bracket(a, b, y, lab):
        f.path(f"M{n(a)},{y - 8} V{y} H{n(b)} V{y - 8}", stroke=INK, w=2)
        f.tex((a + b) / 2, y + 22, lab, "middle")
    bracket(x0 + lam / 2, x0 + lam, 284, r"\tfrac{\lambda}{2}")
    bracket(x0 + lam, x0 + 5 * lam / 4, 284, r"\tfrac{\lambda}{4}")
    return f.svg()


def string_modes():
    f = Fig("fy513-modes", 392, "Kaavakuva: kahdesta päästä kiinnitetty kieli, jonka pituus on L, värähtelee kolmella alimmalla "
            "ominaistaajuudellaan allekkain. Ylimmässä kielen pituudelle mahtuu yksi puolikas aallonpituutta, keskimmäisessä "
            "kaksi ja alimmassa kolme. Kielen päät ovat aina solmuja. Oikealla kunkin rivin ehto: L on yksi, kaksi tai kolme "
            "kertaa puoli aallonpituutta.")
    x0, x1 = 112, 412
    for i, yc in enumerate((62, 170, 278)):
        nn = i + 1
        clamp(f, x0, yc, "left"); clamp(f, x1, yc, "right")
        lens(f, x0, x1, yc, 30, lambda u, nn=nn: math.sin(nn * math.pi * u))
        for m in range(nn + 1): f.circle(x0 + (x1 - x0) * m / nn, yc, 5.5, INK, WHITE, 1.5)
        f.tex(18, yc, rf"n = {nn}", "start")
        f.tex(448, yc, (r"L = \tfrac{\lambda_1}{2}", r"L = 2 \cdot \tfrac{\lambda_2}{2}", r"L = 3 \cdot \tfrac{\lambda_3}{2}")[i], "start", w=150)
    # the length L under the last row
    y = 352
    f.line(x0, y - 14, x0, y + 8, MUTED, 1.5); f.line(x1, y - 14, x1, y + 8, MUTED, 1.5)
    f.arrow(262, y, x0 + 1, y, INK, 2, 12); f.arrow(262, y, x1 - 1, y, INK, 2, 12)
    f.tex(262, y + 22, "L", "middle", bg=True)
    return f.svg()


def pipes():
    f = Fig("fy513-pipes", 400, "Kaavakuva neljästä samanpituisesta putkesta, joiden pituus on L. Putkien sisään on piirretty ilman "
            "siirtymän seisova aalto: vaalea alue näyttää, kuinka paljon ilma liikkuu putken suunnassa kussakin kohdassa. "
            "Ylhäällä molemmista päistä avoin putki perustaajuudella, jolloin päissä on kuvut ja keskellä solmu, ja "
            "toisella ominaistaajuudella. Alhaalla toisesta päästä suljettu putki: suljetussa päässä on aina solmu ja "
            "avoimessa kupu. Perustaajuudella putkeen mahtuu neljännes aallonpituutta ja seuraavalla ominaistaajuudella "
            "kolme neljännestä. Oikealla kunkin putken ehto.")
    x0, x1, hh = 120, 420, 26

    def pipe(yc, shape, closed, nodes_u, label_left, label_right):
        f.rect(x0, yc - hh, x1 - x0, 2 * hh, GLASS)
        lens(f, x0 + 2, x1 - 2, yc, hh - 6, shape, dashed_other=True)
        f.line(x0, yc - hh, x1, yc - hh, INK, 3); f.line(x0, yc + hh, x1, yc + hh, INK, 3)
        if closed: f.rect(x1 - 2, yc - hh - 4, 12, 2 * hh + 8, IRON, INK, 2, 2)
        for u in nodes_u: f.circle(x0 + (x1 - x0) * u, yc, 5, INK, WHITE, 1.5)
        f.tex(16, yc, label_left, "start")
        f.tex(450, yc, label_right, "start", w=130)
    f.tex(300, 24, r"\text{molemmat päät auki}", "middle", w=260)
    pipe(84, lambda u: math.cos(math.pi * u), False, (0.5,), r"f_1", r"L = \tfrac{\lambda}{2}")
    pipe(160, lambda u: math.cos(2 * math.pi * u), False, (0.25, 0.75), r"f_2", r"L = \lambda")
    f.line(12, 208, 588, 208, RULE, 2, "6 6")
    f.tex(300, 234, r"\text{toinen pää suljettu}", "middle", w=260)
    pipe(294, lambda u: math.cos(math.pi * u / 2), True, (1.0,), r"f_1", r"L = \tfrac{\lambda}{4}")
    pipe(370, lambda u: math.cos(3 * math.pi * u / 2), True, (1 / 3, 1.0), r"f_3", r"L = \tfrac{3\lambda}{4}")
    return f.svg()


def task_string():
    """Task figure (exercise L2-04): a string 1,20 m between a vibrator and a pulley in four loops; a ruler underneath.
    No wavelength or speed is written: the student counts the loops and reads the length."""
    f = Fig("fy513-task", 272, "Kuva mittakaavassa: vaakasuora naru, jonka toinen pää on kiinni täryttäjässä vasemmalla ja toinen "
            "kulkee oikealla väkipyörän yli, ja sen päässä riippuu punnus. Täryttäjän ja väkipyörän välinen osa värähtelee "
            "seisovana aaltona, jossa on neljä yhtä pitkää silmukkaa ja viisi solmua päät mukaan lukien. Narun alla on "
            "viivain, jonka asteikko on metreinä nollasta 1,20 metriin 0,20 metrin välein; täryttäjän kohta on nollassa ja "
            "väkipyörän kohta 1,20 metrin kohdalla.")
    x0, x1, yc = 84, 516, 92
    # vibrator
    f.rect(26, yc - 34, 50, 82, IRON, INK, 2.5, 6)
    f.rect(70, yc - 4, 16, 8, ALUMINIUM, INK, 1.5, 2)
    # pulley and weight
    f.circle(x1 + 14, yc + 14, 16, ALUMINIUM, INK, 2.5); f.circle(x1 + 14, yc + 14, 4, INK)
    f.line(x1 + 30, yc + 14, x1 + 30, 176, INK, 2)
    f.rect(x1 + 16, 176, 28, 34, IRON, INK, 2.5, 3)
    f.rect(x1 + 2, yc + 30, 24, 120, SAND_DARK, INK, 2, 2)
    lens(f, x0, x1, yc, 30, lambda u: math.sin(4 * math.pi * u))
    for m in range(5): f.circle(x0 + (x1 - x0) * m / 4, yc, 5.5, INK, WHITE, 1.5)
    # ruler
    ry = 196
    f.rect(x0 - 16, ry - 4, x1 - x0 + 32, 34, SAND_LIGHT, INK, 2, 3)
    per = (x1 - x0) / 1.20
    for i in range(13):
        x = x0 + per * 0.1 * i
        f.line(x, ry - 4, x, ry + (12 if i % 2 == 0 else 6), INK, 1.5)
    for v, s in ((0, "0"), (0.4, "0{,}40"), (0.8, "0{,}80"), (1.2, "1{,}20")):
        f.tex(x0 + per * v, ry + 22, s, "middle", size=20)
    for v, s in ((0.2, "0{,}20"), (0.6, "0{,}60"), (1.0, "1{,}00")):
        f.tex(x0 + per * v, ry + 22, s, "middle", size=20)
    f.tex(x1 + 26, 248, r"x\ (\text{m})", "end", size=20)
    return f.svg()


def hero():
    """The chapter's opening illustration: an acoustic guitar lies in its open case, seen from above, drawn to one scale
    (about 1040 px/m: scale length 65 cm from nut to saddle). A capo presses the strings against the fretboard just
    behind the third fret, and one plucked string vibrates in its fundamental: a standing wave with nodes at the fret
    and at the saddle, its swing (light blue) widest halfway between them. The frets sit where they really are,
    x = nut + L (1 − 2^(−k/12))."""
    f = H.hero("fy513-hero", "Kuvitus: akustinen kitara makaa avatussa kotelossaan ylhäältä katsottuna. Kaulalla on kapo, joka "
               "painaa kielet otelautaa vasten kolmannen nauhan kohdalta. Yksi kielistä on näpätty, ja se värähtelee: "
               "kieli on suurimmillaan kapon ja tallan puolivälissä ja pysyy paikallaan kummassakin päässä, ja sen "
               "liikealue näkyy vaaleansinisenä. Kotelo on puulattialla, ja sen vieressä on plektra.")
    cy, nut, L = 302, 214, 676.0
    saddle = nut + L
    fret = [nut + L * (1 - 2 ** (-k / 12)) for k in range(21)]
    # floor: wide boards
    f.rect(0, 0, 1200, 600, H.grad(f, "fy513h-floor", SAND_LIGHT, SAND, y1=0, y2=600))
    for y in range(40, 600, 92):
        f.line(0, y, 1200, y, GRAIN, 2)
        for k in range(4):
            x = (180 + 330 * k + 140 * (y // 92 % 2)) % 1200
            f.line(x, y, x, y + 92, SAND_DARK, 2)
    # the body's outline: half-widths along the body (u from the neck joint to the tail), smoothed
    x0, x1 = 588, 1108
    prof = [(0, 112), (0.08, 140), (0.18, 150), (0.3, 141), (0.42, 124), (0.5, 126), (0.6, 160), (0.72, 194), (0.83, 202),
            (0.93, 188), (1, 150)]
    def hw(u):                                                   # Catmull–Rom through the profile, rounded at both ends
        P = [prof[0]] + prof + [prof[-1]]
        for j in range(1, len(P) - 2):
            (u0, w0), (u1, w1), (u2, w2), (u3, w3) = P[j - 1], P[j], P[j + 1], P[j + 2]
            if u1 <= u <= u2:
                t = (u - u1) / (u2 - u1)
                w = 0.5 * (2 * w1 + (-w0 + w2) * t + (2 * w0 - 5 * w1 + 4 * w2 - w3) * t * t + (-w0 + 3 * w1 - 3 * w2 + w3) * t ** 3)
                break
        else:
            w = 0
        return w
    def cap(u):                                                  # rounds the shoulders and the tail
        e0, e1 = min(1, u / 0.11), min(1, (1 - u) / 0.2)
        return math.sqrt(max(0, 1 - (1 - e0) ** 2)) * math.sqrt(max(0, 1 - (1 - e1) ** 2))
    us = [i / 160 for i in range(161)]
    def outline(pad):
        xa, xb = x0 - pad * 0.8, x1 + pad
        up = [(xa + (xb - xa) * u, cy - (hw(u) + pad) * cap(u)) for u in us]
        dn = [(x, 2 * cy - y) for x, y in reversed(up)]
        return "M" + " L".join(f"{n(x)},{n(y)}" for x, y in up) + " L" + " L".join(f"{n(x)},{n(y)}" for x, y in dn[1:-1]) + " Z"
    # the open case: a dark rim and blue plush, shaped round the guitar, the neck channel and the headstock
    case_rim, plush = IRON, COLD_LIGHT
    for pad, fill, edge in ((44, case_rim, INK), (26, plush, None)):
        f.rect(40 - pad * 0.4, cy - 52 - pad * 0.6, x0 - 40 + pad, 104 + pad * 1.2, fill, edge, 3, 18)
        f.path(outline(pad), fill, edge, 3)
    # body: wood top, binding, sound hole with rosette, bridge with the saddle and pins
    f.path(outline(0), H.grad(f, "fy513h-top", SAND_DARK, COPPER, y1=cy - 210, y2=cy + 210), INK, 3.5)
    f.path(outline(-8), "none", SAND_LIGHT, 2.5)
    hole = (752, cy)
    f.circle(hole[0], hole[1], 70, "none", INK, 3); f.circle(hole[0], hole[1], 62, "none", SAND_LIGHT, 4)
    f.circle(hole[0], hole[1], 52, INK, INK, 2)
    f.path(f"M{n(saddle - 22)},{cy - 82} H{n(saddle + 26)} Q{n(saddle + 34)},{cy} {n(saddle + 26)},{cy + 82} H{n(saddle - 22)} Q{n(saddle - 30)},{cy} {n(saddle - 22)},{cy - 82} Z",
           GRAIN, INK, 2.5)
    f.rect(saddle - 3, cy - 46, 6, 92, WHITE, INK, 1.5, 2)
    # neck: fretboard with frets and dots, headstock with six tuners
    def nw(x): return 24 + (x - nut) / (fret[20] - nut) * 6           # half-width of the fretboard
    f.path(f"M{n(nut - 4)},{n(cy - 24)} L{n(x0 + 10)},{n(cy - 29)} V{n(cy + 29)} L{n(nut - 4)},{n(cy + 24)} Z", COPPER, INK, 2.5)   # neck
    f.path(f"M{n(nut)},{n(cy - nw(nut))} L{n(fret[20])},{n(cy - nw(fret[20]))} V{n(cy + nw(fret[20]))} L{n(nut)},{n(cy + nw(nut))} Z", INK, INK, 2)
    for k in range(1, 21):
        f.line(fret[k], cy - nw(fret[k]) + 1, fret[k], cy + nw(fret[k]) - 1, ALUMINIUM, 2.5)
    for k in (3, 5, 7, 9, 15, 17, 19):
        f.circle((fret[k - 1] + fret[k]) / 2, cy, 4.5, WHITE)
    for dy in (-11, 11):
        f.circle((fret[11] + fret[12]) / 2, cy + dy, 4.5, WHITE)
    f.rect(nut - 6, cy - 25, 7, 50, WHITE, INK, 1.5, 1)                             # nut
    f.path(f"M{nut - 6},{cy - 26} L74,{cy - 44} Q60,{cy} 74,{cy + 44} L{nut - 6},{cy + 26} Z", COPPER, INK, 3)   # headstock
    tx = [96, 134, 172]
    for k, x in enumerate(tx):
        for sgn in (-1, 1):
            f.line(x, cy + sgn * 38, x, cy + sgn * 52, METAL_EDGE, 5)
            f.add(f'<ellipse cx="{x}" cy="{cy + sgn * 62}" rx="10" ry="13" fill="{WHITE}" stroke="{INK}" stroke-width="2"/>')
            f.circle(x, cy + sgn * 24, 5, ALUMINIUM, INK, 1.5)
    # the strings: from the tuner posts over the nut to the saddle (wound ones a little thicker)
    sy = lambda i, x: cy + (i - 2.5) * (7.6 + (x - nut) / L * 3.8)
    posts = [(tx[2], -1), (tx[1], -1), (tx[0], -1), (tx[0], 1), (tx[1], 1), (tx[2], 1)]
    VIB = 3                                                   # the plucked string
    for i in range(6):
        px_, sg = posts[i]
        w = 2.6 - 0.3 * i
        col = COPPER if i < 3 else ALUMINIUM
        f.path(f"M{px_},{cy + sg * 24} L{nut},{n(sy(i, nut))}", stroke=col, w=w)
        if i != VIB:
            f.path(f"M{nut},{n(sy(i, nut))} L{n(saddle)},{n(sy(i, saddle))}", stroke=col, w=w, extra='stroke-linecap="round"')
    # capo just behind the third fret: a padded bar across the neck and its clamp
    capx = fret[3] - 9
    f.rect(capx - 9, cy - 44, 18, 88, INK, INK, 2, 6)
    f.rect(capx - 5, cy - 40, 10, 80, IRON, None, 2, 4)
    f.path(f"M{capx + 9},{cy - 40} Q{capx + 48},{cy - 50} {capx + 52},{cy - 18}", stroke=INK, w=8, extra='stroke-linecap="round"')
    # the plucked string: between the node at the third fret and the node at the saddle, a half wavelength
    a, b = fret[3], saddle
    A = 30
    def s_y(x, amp): return sy(VIB, x) + amp * math.sin(math.pi * (x - a) / (b - a))
    xs = [a + (b - a) * i / 80 for i in range(81)]
    lens = "M" + " L".join(f"{n(x)},{n(s_y(x, -A))}" for x in xs) + " L" + " L".join(f"{n(x)},{n(s_y(x, A))}" for x in reversed(xs)) + " Z"
    f.path(lens, WATER_LIGHT, extra='fill-opacity="0.6"')
    for amp in (-A, A):
        f.path("M" + " L".join(f"{n(x)},{n(s_y(x, amp))}" for x in xs), stroke=WATER, w=1.5, extra='stroke-opacity="0.55"')
    f.path(f"M{nut},{n(sy(VIB, nut))} L{n(a)},{n(sy(VIB, a))}", stroke=ALUMINIUM, w=1.8)
    f.path("M" + " L".join(f"{n(x)},{n(s_y(x, 0.55 * A))}" for x in xs), stroke=WATER, w=3.5, extra='stroke-linecap="round"')
    for x in (a, b): f.circle(x, sy(VIB, x), 5, INK)
    # a pick on the floor beside the case
    f.path("M1118,520 Q1150,506 1168,526 Q1160,556 1136,566 Q1112,546 1118,520 Z", HOT, INK, 2.5)
    return f.svg()


FIGURES = {"hero": hero, "superpositio": superposition, "solmut": nodes, "kieli": string_modes, "putket": pipes,
           "kuvio-tehtava": task_string}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "superpositio": "reveals: the standing wave as the sum of a wave and its reflection, nodes λ/2 apart, one at the fixed end",
    "solmut": "reveals: node to node λ/2, node to antinode λ/4",
    "kieli": "reveals: L = n·λn/2 for a string fixed at both ends, n = 1, 2, 3",
    "putket": "reveals: open pipe L = λ/2, λ; closed pipe L = λ/4, 3λ/4, closed end a node, open end an antinode",
    "kuvio-tehtava": "safe: a string 1,20 m long on a ruler in four loops, no wavelength or speed written",
}
