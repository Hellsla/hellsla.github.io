"""Figures of the Ahjo guide 3D-mallinnus: mitoitettu kappale (scripts/figlib.py), drawn into the page by
scripts/ahjo.py in the page's language (content/<lang>/ahjo/ahjo-3d-mallinnus.figures.json). Original drawings: a
solid minus a hole object (how a block-based modeller such as Tinkercad and a CAD program's sketch-and-cut both build
a hole), the table-edge holder in section with its clearance exaggerated, and the clearance test strip."""
from figlib import Fig, INK, MUTED, WHITE, RULE, COLD, COLD_LIGHT, SAND_LIGHT, GRAIN, n

HOLE = "#f1f3f5"


def block(f, x, y, w, h, dx=40, dy=-30, fill=COLD_LIGHT, stroke=COLD):
    """A box in oblique view: its front face (x, y, w, h) and the top and right faces dx, dy behind it."""
    f.path(f"M{n(x)},{n(y)} L{n(x + dx)},{n(y + dy)} L{n(x + w + dx)},{n(y + dy)} L{n(x + w)},{n(y)} Z", "#e3f0fc", stroke, 2.5)
    f.path(f"M{n(x + w)},{n(y)} L{n(x + w + dx)},{n(y + dy)} L{n(x + w + dx)},{n(y + h + dy)} L{n(x + w)},{n(y + h)} Z", "#a9cdee", stroke, 2.5)
    f.rect(x, y, w, h, fill, stroke, 2.5)


def ellipse(f, cx, cy, rx, ry, fill, stroke=None, w=2, dash=None):
    s = f' stroke="{stroke}" stroke-width="{w:g}"' + (f' stroke-dasharray="{dash}"' if dash else "") if stroke else ""
    f.add(f'<ellipse cx="{n(cx)}" cy="{n(cy)}" rx="{n(rx)}" ry="{n(ry)}" fill="{fill}"{s}/>')


def csg():
    f = Fig("ahjo-3dm-csg", 270, "Kaaviokuva kolmessa osassa, ei mittakaavassa. Vasemmalla on suorakulmainen "
            "särmiö, kappale. Sen jälkeen miinusmerkki ja pystysuora lieriö, joka on piirretty katkoviivalla ja harmaana: "
            "se on reikä eli kappale, joka poistetaan. Lieriö on särmiötä korkeampi, jotta reikä menee varmasti läpi. "
            "Yhtäsuuruusmerkin jälkeen oikealla on sama särmiö, jonka yläpinnassa näkyy pyöreä läpireikä: reikä on "
            "ryhmitetty kappaleen kanssa yhdeksi malliksi.")
    block(f, 24, 120, 130, 70)
    f.tex(222, 140, r"-", "middle", size=34, w=30)
    cx = 300
    f.rect(cx - 26, 70, 52, 128, HOLE)
    ellipse(f, cx, 198, 26, 9, HOLE, MUTED, 2, "6 5")
    f.line(cx - 26, 70, cx - 26, 198, MUTED, 2, "6 5"); f.line(cx + 26, 70, cx + 26, 198, MUTED, 2, "6 5")
    ellipse(f, cx, 70, 26, 9, "#e9ecef", MUTED, 2, "6 5")
    f.tex(376, 140, r"=", "middle", size=34, w=30)
    block(f, 414, 120, 130, 70)
    ellipse(f, 414 + 65 + 20, 105, 26, 9, "#495057", COLD, 2)
    f.tex(109, 236, r"\text{kappale}", "middle", size=22)
    f.tex(cx, 236, r"\text{reikä}", "middle", size=22)
    f.tex(499, 236, r"\text{ryhmitelty malli}", "middle", size=22)
    return f.svg()


def dim(f, x, y1, y2, colour=INK):
    """A vertical dimension line from y1 to y2 at x, an arrow head at each end."""
    m = (y1 + y2) / 2
    f.arrow(x, m, x, y1, colour, 2, 10); f.arrow(x, m, x, y2, colour, 2, 10)


def pidike():
    f = Fig("ahjo-3dm-pidike", 300, "Leikkauskuva sivulta, ei mittakaavassa. Vasemmalta tulee vaakasuora pöytälevy, "
            "jonka paksuus on t. Pöytälevyn oikean reunan ympärillä on U-muotoinen pidike: sen ylempi haara on levyn päällä, "
            "pystyosa levyn reunan takana ja alempi haara levyn alla. Pidikkeen haarojen väli on a, ja se on hieman "
            "suurempi kuin levyn paksuus t. Haarojen ja levyn väliin jäävä rako on välys. Kuvassa rako on piirretty "
            "paljon todellista suuremmaksi, jotta se näkyy.")
    f.rect(30, 132, 300, 72, SAND_LIGHT, GRAIN, 2)
    for y in (150, 168, 186):
        f.path(f"M40,{y} q60,-6 120,0 t120,0 t50,0", "none", "#d9b26a", 1.5)
    f.tex(128, 168, r"\text{pöytälevy}", "middle", size=20, bg=True)
    f.path("M226,108 L354,108 L354,228 L226,228 L226,212 L338,212 L338,124 L226,124 Z", COLD_LIGHT, COLD, 2.5)
    f.tex(290, 88, r"\text{pidike}", "middle", COLD, size=22)
    dim(f, 62, 132, 204); f.line(50, 132, 74, 132, INK, 1.5); f.line(50, 204, 74, 204, INK, 1.5)
    f.tex(48, 168, r"t", "end", size=24, w=24)
    f.line(338, 124, 420, 124, MUTED, 1.5, "5 4"); f.line(338, 212, 420, 212, MUTED, 1.5, "5 4")
    dim(f, 408, 124, 212)
    f.tex(422, 168, r"a = t + v", "start", size=24)
    f.tex(130, 100, r"\text{välys}", "middle", size=20)
    f.line(160, 106, 250, 127, MUTED, 1.5)
    f.line(160, 106, 250, 209, MUTED, 1.5)
    f.tex(300, 266, r"\text{rako piirretty liioitellun suureksi}", "middle", MUTED, size=18)
    return f.svg()


def sovitekoe():
    f = Fig("ahjo-3dm-sovitekoe", 230, "Kaaviokuva ylhäältä, ei mittakaavassa: pitkä kapea koekappale, jossa on "
            "rivissä neljä pyöreää reikää. Reikien halkaisijat ovat vasemmalta oikealle 10,0 mm, 10,2 mm, 10,4 mm ja "
            "10,6 mm, ja erot on piirretty todellista suuremmiksi. Jokaisen reiän alle on kirjoitettu sen halkaisija. "
            "Reikiin kokeillaan 10 millimetrin tappia, jotta nähdään, mikä reikä on sopivan väljä.")
    f.rect(36, 40, 528, 96, COLD_LIGHT, COLD, 2.5, rx=12)
    for i, d in enumerate((10.0, 10.2, 10.4, 10.6)):
        x = 108 + i * 128; r = 24 + (d - 10) * 16
        f.circle(x, 88, r, WHITE, COLD, 2.5)
        f.tex(x, 162, f"{d:.1f}".replace(".", "{,}"), "middle", size=22, w=60)
    f.tex(300, 202, r"\text{reiän halkaisija}\ (\text{mm})", "middle", MUTED, size=20)
    return f.svg()


FIGURES = {"csg": csg, "pidike": pidike, "sovitekoe": sovitekoe}
