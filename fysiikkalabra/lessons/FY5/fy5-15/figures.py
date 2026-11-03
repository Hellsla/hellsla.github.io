"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy5-15` writes them into lesson.md."""
import math
from figlib import (Fig, Axes, fi, INK, MUTED, WHITE, RULE, RULE_LIGHT, HEAT, HEAT_LIGHT, IRON, ALUMINIUM, METAL_EDGE,
                    SAND_LIGHT, GOOD, n)
import herolib as H

I0 = 1.0e-12
L_of = lambda I: 10 * math.log10(I / I0)


def kartio():
    """Ydinajatus: the power of a point source spreads over areas that grow as r²; intensity falls as 1/r²."""
    f = Fig("fy515-kartio", 340, "Kaavakuva, ei mittakaavassa: pistemäinen äänilähde vasemmalla. Siitä lähtevät säteet rajaavat "
            "kartion, joka leikkaa kolme neliötä etäisyyksillä r, 2r ja 3r. Lähin neliö on yksi ruutu, jonka pinta-ala on A. "
            "Etäisyydellä 2r sama kartio peittää neljä samankokoista ruutua eli pinta-alan 4A, ja etäisyydellä 3r yhdeksän "
            "ruutua eli 9A. Sama teho jakautuu yhä suuremmalle alalle, joten intensiteetti on I, I/4 ja I/9; ruutujen väri "
            "vaalenee samassa suhteessa.")
    sx, sy, D, s0, k = 52, 182, 150, 21, 0.42          # source, depth per r, half side at r, oblique factor

    def pt(X, Y, Z): return (sx + X + Z * k, sy - Y - Z * k)

    def square(d, opacity):
        h = s0 * d; X = D * d
        c = [pt(X, -h, -h), pt(X, h, -h), pt(X, h, h), pt(X, -h, h)]
        f.path("M" + " L".join(f"{n(a)},{n(b)}" for a, b in c) + " Z", HEAT_LIGHT, extra=f'fill-opacity="{opacity:g}"')
        for j in range(1, d):                       # the grid: d × d cells, each as large as the nearest square
            t = -h + 2 * h * j / d
            a, b = pt(X, t, -h), pt(X, t, h); f.line(a[0], a[1], b[0], b[1], HEAT, 1.5)
            a, b = pt(X, -h, t), pt(X, h, t); f.line(a[0], a[1], b[0], b[1], HEAT, 1.5)
        f.path("M" + " L".join(f"{n(a)},{n(b)}" for a, b in c) + " Z", stroke=INK, w=2)
        return c

    far = square(3, 0.3)
    for (a, b) in far:                               # rays from the source to the far corners
        f.line(sx, sy, a, b, HEAT, 1.5, "7 5")
    square(2, 0.55)
    square(1, 0.95)
    f.circle(sx, sy, 8, INK)
    f.tex(sx, sy + 30, "P", "middle")
    # labels above each square: its area and the intensity on it
    for d, txt in ((1, r"A,\ I"), (2, r"4A,\ I/4"), (3, r"9A,\ I/9")):
        top = pt(D * d, s0 * d, s0 * d)
        f.tex(top[0] - 10, top[1] - 22, txt, "middle")
    # distances along the axis below
    yb = 306
    f.line(sx, yb, sx + 3 * D + 6, yb, INK, 2)
    for d, txt in ((1, "r"), (2, "2r"), (3, "3r")):
        f.line(sx + D * d, yb - 6, sx + D * d, yb + 6, INK, 2)
        f.tex(sx + D * d, yb + 20, txt, "middle")
    f.line(sx, yb - 6, sx, yb + 6, INK, 2)
    f.tex(sx, yb + 20, "0", "middle")
    return f.svg()


def asteikko():
    """Ydinajatus: the decibel scale beside the intensities, ten-fold steps."""
    f = Fig("fy515-asteikko", 396, "Kaavakuva: intensiteettitason asteikko pystysuorana palkkina, joka tummuu alhaalta ylös. "
            "Alhaalla 0 dB eli intensiteetti 10 potenssiin miinus 12 wattia neliömetrille, kuulokynnys. Joka 20 desibelin "
            "välein intensiteetti on sata kertaa suurempi: 20 dB kuiskaus, 40 dB hiljainen huone, 60 dB keskustelu, "
            "80 dB vilkas katu, 100 dB moottorisaha ja ylhäällä 120 dB eli 1 watti neliömetrille, kipukynnys. "
            "Esimerkkiäänet ovat tyypillisiä suuruusluokkia.")
    f.defs_add(f'<linearGradient id="fy515-bar" x1="0" y1="1" x2="0" y2="0"><stop offset="0" stop-color="{HEAT_LIGHT}" stop-opacity="0.35"/><stop offset="1" stop-color="{HEAT}"/></linearGradient>')
    y0, per = 368, 2.5                                # 0 dB at y0, 2,5 units per dB
    bx = 236
    f.tex(bx + 48, 22, r"L\ (\text{dB})", "start")
    f.tex(400, 22, r"I\ (\text{W/m}^2)", "start", w=130)
    f.rect(bx, y0 - 120 * per, 32, 120 * per, "url(#fy515-bar)", INK, 2, 4)
    names = {0: "kuulokynnys", 20: "kuiskaus", 40: "hiljainen huone", 60: "keskustelu", 80: "vilkas katu",
             100: "moottorisaha", 120: "kipukynnys"}
    for Ldb in range(0, 121, 20):
        y = y0 - Ldb * per
        f.line(bx - 6, y, bx, y, INK, 2)
        f.line(bx + 32, y, bx + 38, y, INK, 2)
        strong = Ldb in (0, 120)
        f.tex(bx - 14, y, r"\text{" + names[Ldb] + "}", "end", INK if strong else MUTED)
        f.tex(bx + 48, y, fi(Ldb), "start")
        e = Ldb // 10 - 12
        f.tex(400, y, "1" if e == 0 else f"10^{{{e}}}".replace("-", "-"), "start")
    return f.svg()


def kuvaaja():
    """Kaava: L against r for a point source with I = 1,0e-3 W/m² at 1 m; each doubling of r gives 6 dB less."""
    P = 4 * math.pi * 1e-3
    f = Fig("fy515-kuvaaja", 420, "Kuvaaja mittakaavassa: pistemäisen äänilähteen intensiteettitaso L desibeleinä etäisyyden r "
            "funktiona nollasta kymmeneen metriin, kun lähteen teho on 12,6 milliwattia. Käyrä laskee ensin jyrkästi ja "
            "sitten loivasti. Pisteet etäisyyksillä 1, 2, 4 ja 8 metriä ovat 90,0, 84,0, 78,0 ja 71,9 dB: joka kerta, kun "
            "etäisyys kaksinkertaistuu, taso pienenee noin 6 dB.")
    ax = Axes(f, (110, 376), (500, 70), x=(0, 10), y=(0, 100), xticks=list(range(1, 11)), yticks=list(range(10, 101, 10)),
              xlabel=r"r\ (\text{m})", ylabel=r"L\ (\text{dB})", xfmt=lambda v: fi(v) if v % 2 == 0 else "",
              yfmt=lambda v: fi(v))
    ax.curve(lambda r: L_of(P / (4 * math.pi * r * r)), 0.8, 10, HEAT, 3)
    for r in (1, 2, 4, 8):
        Lr = L_of(P / (4 * math.pi * r * r))
        ax.guide(r, Lr)
        ax.point(r, Lr, HEAT)
        if r > 1: f.tex(ax.X(r) + 8, ax.Y(Lr) - 22, fi(round(Lr, 1), 1), "start", bg=True)   # r = 1 m sits on the 90 dB gridline
    return f.svg()


def summa():
    """Kaava: two equal independent sources, intensities add (bars to scale), the level rises only 3 dB."""
    f = Fig("fy515-summa", 360, "Kaksi pylväskaaviota mittakaavassa. Vasemmalla intensiteetit yksikössä 10 potenssiin miinus 4 "
            "wattia neliömetrille: kumpikin kaiutin yksin 1,0 ja yhdessä 2,0, eli yhteinen pylväs on kaksi kertaa niin "
            "korkea. Oikealla samat tilanteet intensiteettitasoina: kumpikin yksin 80 dB ja yhdessä 83 dB, joten "
            "yhteinen pylväs on vain vähän korkeampi.")
    base = 300
    f.line(300, 14, 300, 346, RULE, 2, "6 6")
    # intensities (linear, 100 units per 1,0e-4 W/m²)
    f.tex(40, 26, r"I\ (10^{-4}\,\text{W/m}^2)", "start", w=200)
    f.line(32, base, 284, base, INK, 2.5)
    for x, h, val, lab in ((52, 100, "1{,}0", "I_1"), (122, 100, "1{,}0", "I_2"), (196, 200, "2{,}0", "I_1 + I_2")):
        f.rect(x, base - h, 52, h, HEAT_LIGHT if h == 100 else HEAT, INK, 2, 3)
        f.tex(x + 26, base - h - 18, val, "middle")
        f.tex(x + 26, base + 24, lab, "middle")
    # levels (2 units per dB from 0 dB)
    f.tex(330, 26, r"L\ (\text{dB})", "start")
    f.line(318, base, 584, base, INK, 2.5)
    for x, Ldb, val, lab in ((340, 80, "80", "L_1"), (410, 80, "80", "L_2"), (486, 83.0103, "83", "L")):
        h = Ldb * 2
        f.rect(x, base - h, 52, h, ALUMINIUM if Ldb == 80 else METAL_EDGE, INK, 2, 3)
        f.tex(x + 26, base - h - 18, val, "middle")
        f.tex(x + 26, base + 24, lab, "middle")
    return f.svg()


def hero():
    """The chapter's opening illustration: an open-air concert, listeners near the stage and far away on a hill."""
    f = H.hero("fy515-hero", "Kuvitus: ulkoilmakonsertti iltapäivällä. Lavan molemmin puolin on kaiutintornit, ja niiden edessä "
               "seisoo yleisöä. Kaiuttimista leviää yhä laajempia kaaria. Kaukana oikealla rinteellä istuu kaksi kuulijaa, "
               "joihin kaaret ulottuvat vaaleina.")
    H.sky(f, "fy515h", 600)
    H.cloud(f, 200, 110, 0.9)
    H.cloud(f, 960, 80, 0.7)
    H.hills(f, "fy515h", 360, [H.GOOD_LIGHT, GOOD], amp=50, seed=4)
    # sound arcs from the stage, fading with distance
    cx, cy = 560, 330
    for k, r in enumerate(range(140, 760, 70)):
        op = max(0.12, 0.85 * (140 / r) ** 1.3)
        f.add(f'<path d="M{n(cx + r * math.cos(-0.9))},{n(cy + r * math.sin(-0.9))} A{r},{r} 0 0 1 {n(cx + r * math.cos(0.55))},{n(cy + r * math.sin(0.55))}" '
              f'fill="none" stroke="{HEAT}" stroke-width="6" stroke-linecap="round" stroke-opacity="{op:.2f}"/>')
    # the stage: floor, back wall, roof and two speaker towers
    f.rect(380, 360, 360, 40, IRON, INK, 3, 2)
    f.rect(400, 200, 320, 160, METAL_EDGE, INK, 3)
    f.path("M370,200 L560,150 L750,200 Z", INK)
    f.rect(470, 300, 60, 60, ALUMINIUM, INK, 2, 4)          # a drum kit block on the stage
    f.circle(500, 330, 18, WHITE, INK, 2)
    for x in (330, 750):
        f.rect(x, 210, 70, 190, INK, None, 2, 4)
        for j, y in enumerate((240, 300, 360)):
            f.circle(x + 35, y, 22, IRON, METAL_EDGE, 3)
            f.circle(x + 35, y, 8, METAL_EDGE)
    # the crowd in front of the stage
    shirts = [H.COLD, H.HOT, H.HEAT_LIGHT, H.WATER, H.SAND, H.GOOD_LIGHT, H.COPPER, H.ICE]
    for k in range(13):
        x = 320 + k * 42 + 14 * H.rnd(k, 3)
        H.person(f, x, 600, shirts[k % len(shirts)], INK, 0.42 + 0.06 * H.rnd(k, 7))
    # two listeners far away on the hill
    for x, sh in ((1040, H.HOT), (1090, H.COLD)):
        H.person(f, x, 400, sh, INK, 0.22)
    return f.svg()


FIGURES = {"hero": hero, "kartio": kartio, "asteikko": asteikko, "kuvaaja": kuvaaja, "summa": summa}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "kartio": "reveals: the area grows as r², so I falls to 1/4 and 1/9 at 2r and 3r",
    "asteikko": "reveals: every 10 dB is a ten-fold intensity; 0 dB = 1e-12 W/m², 120 dB = 1 W/m²",
    "kuvaaja": "reveals: L(r) of a point source falls about 6 dB per doubling of r (90, 84, 78, 72 dB)",
    "summa": "reveals: two equal sources double the intensity but raise the level from 80 to 83 dB",
}
