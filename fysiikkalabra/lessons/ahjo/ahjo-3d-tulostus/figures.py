"""Figures of the Ahjo guide 3D-tulostus: ensimmäinen tuloste (scripts/figlib.py), drawn into the page by
scripts/ahjo.py in the page's language (content/<lang>/ahjo/ahjo-3d-tulostus.figures.json). Original drawings for a
generic FDM printer (Ahjo's printer is not chosen yet): a loaded beam printed in its strong and its weak orientation
(the force red, as everywhere in Ruukkilabra), and the first layer seen in section at three nozzle heights."""
from figlib import Fig, INK, MUTED, WHITE, RULE, HOT, HEAT, COLD, COLD_LIGHT, ALUMINIUM, METAL_EDGE, n

PLA = HEAT
BED = "#adb5bd"


def beam_panel(f, x0, strong):
    f.rect(x0 + 22, 56, 20, 196, RULE)
    for y in range(64, 252, 16):
        f.line(x0 + 22, y + 12, x0 + 34, y, MUTED, 1.5)
    top, bot, x1, x2 = 132, 172, x0 + 42, x0 + 252
    f.rect(x1, top, x2 - x1, bot - top, COLD_LIGHT, COLD, 2.5)
    if strong:
        for y in range(top + 8, bot, 8): f.line(x1, y, x2, y, COLD, 1)
    else:
        for x in range(x1 + 8, x2, 8): f.line(x, top, x, bot, COLD, 1)
        f.path(f"M{n(x1 + 8)},{n(top)} l3,8 l-4,8 l5,8 l-3,7", "none", INK, 3)       # the crack between two layers
    f.arrow(x2 - 14, bot + 6, x2 - 14, 246, HOT, 4, 16)
    f.tex(x2 - 2, 222, r"\overline{F}", "start", HOT, size=24, w=30)
    f.tex(x0 + 150, 286, r"\text{vahva suunta}" if strong else r"\text{heikko suunta}", "middle", size=22)
    f.tex(x0 + 150, 102, r"\text{kerrokset pitkittäin}" if strong else r"\text{kerrokset poikittain}", "middle", MUTED, size=19)


def suunta():
    f = Fig("ahjo-3dt-suunta", 310, "Kaaviokuva kahdessa osassa, ei mittakaavassa. Kummassakin vasemmalla on seinä, "
            "josta lähtee vaakasuora tulostettu palkki, ja palkin vapaaseen päähän vaikuttaa alaspäin punainen voima F. "
            "Ohuet viivat näyttävät tulostuskerrokset. Vasemmalla palkki on tulostettu makuulleen, joten kerrokset kulkevat "
            "palkin suuntaisesti: tämä on vahva suunta. Oikealla palkki on tulostettu pystyyn, joten kerrokset ovat "
            "poikittain palkkiin nähden, ja seinän vieressä kahden kerroksen väliin on auennut halkeama: tämä on heikko suunta.")
    beam_panel(f, 0, True)
    f.line(300, 30, 300, 296, RULE, 1.5, "6 6")
    beam_panel(f, 300, False)
    return f.svg()


def nozzle(f, cx, tip):
    f.path(f"M{n(cx - 26)},{n(tip - 64)} L{n(cx + 26)},{n(tip - 64)} L{n(cx + 26)},{n(tip - 34)} L{n(cx + 8)},{n(tip)} "
           f"L{n(cx - 8)},{n(tip)} L{n(cx - 26)},{n(tip - 34)} Z", ALUMINIUM, METAL_EDGE, 2)


def ensikerros():
    f = Fig("ahjo-3dt-ensikerros", 300, "Kolme leikkauskuvaa vierekkäin, ei mittakaavassa. Kussakin on harmaa "
            "tulostusalusta, sen yläpuolella suutin ja alustalla oransseja tulostuslangan poikkileikkauksia. Vasemmalla "
            "suutin on liian korkealla: langat ovat pyöreitä, niiden välissä on rakoja, ja ne ovat tuskin kiinni alustassa. "
            "Keskellä suutin on sopivalla korkeudella: langat ovat hieman litistyneitä ja koskettavat toisiaan, ja pinta on "
            "tasainen. Oikealla suutin on liian matalalla: langat ovat ohuiksi litistyneitä, ja niiden reunoille on "
            "pursunut harjanteita.")
    bed = 204
    for i, (label, tip) in enumerate(((r"\text{liian korkea}", 166), (r"\text{sopiva}", 192), (r"\text{liian matala}", 199))):
        cx = 100 + i * 200
        f.rect(cx - 90, bed, 180, 18, BED, METAL_EDGE, 1.5)
        nozzle(f, cx + 50, tip)
        for k in range(4):
            x = cx - 72 + k * (34 if i == 0 else 27 if i == 1 else 28)
            if i == 0: f.circle(x, bed - 10, 10, PLA, INK, 1.5)
            elif i == 1: f.add(f'<ellipse cx="{n(x)}" cy="{n(bed - 7)}" rx="14" ry="7" fill="{PLA}" stroke="{INK}" stroke-width="1.5"/>')
            else:
                f.add(f'<ellipse cx="{n(x)}" cy="{n(bed - 3.5)}" rx="15" ry="3.5" fill="{PLA}" stroke="{INK}" stroke-width="1.5"/>')
                f.add(f'<ellipse cx="{n(x + 14)}" cy="{n(bed - 9)}" rx="4" ry="4" fill="{PLA}" stroke="{INK}" stroke-width="1.5"/>')
        f.tex(cx, 254, label, "middle", size=21)
    for x in (200, 400): f.line(x, 30, x, 280, RULE, 1.5, "6 6")
    return f.svg()


FIGURES = {"suunta": suunta, "ensikerros": ensikerros}
