"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy5-13` writes them into lesson.md.
Colours: the standing wave (the sum) water blue #2f74b5 with its swing between the envelopes in light blue, the wave
travelling towards the fixed end orange #e8590c (dashed), the reflected wave violet #7048e8 (dotted), nodes ink dots.
Force red is never used for a displacement."""
import math
from figlib import (Fig, INK, MUTED, WHITE, RULE, RULE_LIGHT, GLASS, WATER_LIGHT, WATER, SAND_LIGHT, SAND, SAND_DARK, GRAIN,
                    HEAT, ALUMINIUM, METAL_EDGE, IRON, COPPER, ICE, PAPER, n)
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
    """The chapter's opening illustration: a music room with organ pipes, an acoustic guitar on its stand and a flute."""
    f = H.hero("fy513-hero", "Kuvitus: musiikkiluokka. Vasemmalla puisen kaapin päällä on rivi eripituisia hopeanvärisiä urkupillejä, "
               "keskellä lattialla telineessä akustinen kitara, jonka kuusi kieltä kulkevat kaulalta kaikukopan tallaan, ja "
               "oikealla pöydällä poikkihuilu. Taustalla on ikkuna.")
    f.rect(0, 0, 1200, 520, PAPER)
    # window
    f.rect(830, 70, 270, 210, H.grad(f, "fy513h-sky", ICE, GLASS), INK, 4, 4)
    f.line(965, 70, 965, 280, INK, 4); f.line(830, 175, 1100, 175, INK, 4)
    H.cloud(f, 900, 130, 0.45)
    # floor
    f.rect(0, 520, 1200, 80, SAND_LIGHT)
    for y in (540, 566): f.line(0, y, 1200, y, SAND, 3)
    for k in range(9): f.line(60 + 140 * k + (40 if k % 2 else 0), 520, 60 + 140 * k + (40 if k % 2 else 0), 600, SAND, 2)
    f.line(0, 520, 1200, 520, GRAIN, 3)
    # organ pipes on a wooden case
    f.rect(70, 440, 330, 80, SAND_DARK, INK, 3, 4)
    f.rect(86, 456, 298, 48, SAND, extra='fill-opacity="0.6"')
    metal = H.grad(f, "fy513h-metal", ALUMINIUM, METAL_EDGE, horizontal=True)
    heights = (150, 190, 236, 286, 330, 286, 236, 190, 150)
    for k, h in enumerate(heights):
        x = 92 + 32 * k
        top = 440 - h
        f.path(f"M{x},{top} H{x + 24} V{440 - 34} L{x + 16},440 H{x + 8} L{x},{440 - 34} Z", metal, INK, 2.5)
        f.rect(x + 6, 440 - 58, 12, 10, INK, extra='fill-opacity="0.75"')
        f.add(f'<ellipse cx="{x + 12}" cy="{top}" rx="12" ry="3.5" fill="{METAL_EDGE}" stroke="{INK}" stroke-width="2"/>')
    # guitar stand
    f.path("M560,520 L520,580 M640,520 L680,580 M600,520 L600,585", stroke=INK, w=6, extra='stroke-linecap="round"')
    f.path("M548,512 Q600,532 652,512", stroke=INK, w=6, extra='stroke-linecap="round"')
    # guitar body
    body = ("M600,236 C650,236 680,262 678,302 C676,334 650,348 652,370 C655,394 708,404 708,454 C708,512 660,540 600,540 "
            "C540,540 492,512 492,454 C492,404 545,394 548,370 C550,348 524,334 522,302 C520,262 550,236 600,236 Z")
    f.path(body, H.grad(f, "fy513h-wood", SAND_DARK, COPPER), INK, 3.5)
    f.path("M600,248 C640,248 664,268 664,302 C662,330 638,346 640,370 C643,396 692,408 692,454 C692,504 650,526 600,526",
           stroke=SAND_LIGHT, w=3, extra='stroke-opacity="0.6"')
    f.circle(600, 340, 30, INK, SAND, 4)
    f.rect(564, 452, 72, 14, "#8a5f22", INK, 2, 3)
    # neck, frets and head
    f.rect(588, 76, 24, 172, "#8a5f22", INK, 2.5, 2)
    y = 92
    for k in range(12):
        f.line(589, y, 611, y, ALUMINIUM, 2)
        y += 16 - k * 0.6
    f.path("M584,30 H616 L620,78 H580 Z", "#8a5f22", INK, 2.5)
    for k in range(3):
        f.circle(574, 42 + 14 * k, 5, ALUMINIUM, INK, 1.5); f.circle(626, 42 + 14 * k, 5, ALUMINIUM, INK, 1.5)
    for k in range(6):
        xt, xb = 591.5 + 3.4 * k, 581 + 7.6 * k
        f.line(xt, 78, xb, 458, WHITE, 1.5)
    # table with a flute
    f.rect(840, 410, 280, 16, SAND_DARK, INK, 3, 3)
    f.path("M864,426 L852,520 M1096,426 L1108,520", stroke=INK, w=6, extra='stroke-linecap="round"')
    f.rect(862, 392, 236, 14, H.grad(f, "fy513h-flute", ALUMINIUM, METAL_EDGE), INK, 2.5, 7)
    f.add(f'<ellipse cx="886" cy="399" rx="6" ry="3.5" fill="{INK}"/>')
    for k in range(7): f.circle(960 + 18 * k, 399, 4.5, METAL_EDGE, INK, 1.5)
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
