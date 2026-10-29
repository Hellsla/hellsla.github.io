"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy2-8` writes them into lesson.md."""
import math
from figlib import (Fig, INK, MUTED, WHITE, RULE, RULE_LIGHT, HEAT, HEAT_LIGHT, GLASS, SAND, SAND_LIGHT, GRAIN,
                    ALUMINIUM, METAL_EDGE, IRON, HOT, HOT_LIGHT, n)
from figlib import GOOD, GOOD_LIGHT, ICE
import herolib as H


def hero():
    """The chapter's opening illustration: one house, one socket, and two ways to make its electricity: a coal plant under smoke or wind turbines under a clear sky."""
    f = H.hero("fy28-hero", "Kuvitus: keskellä talo, johon sähkö tulee voimalinjaa pitkin. Vasemmalla hiilivoimala, jonka savupiipusta nousee "
               "tumma savu harmaalle taivaalle; oikealla tuulivoimaloita kirkkaan taivaan alla. Talon seinässä on pistorasia.")
    f.rect(0, 0, 600, 600, H.grad(f, "fy28h-grey", ALUMINIUM, GLASS)); f.rect(600, 0, 600, 600, H.grad(f, "fy28h-sky", ICE, GLASS))
    H.sun(f, "fy28h", 760, 100, 44)
    H.forest(f, 380, 40, 30, GOOD, seed=9)
    f.rect(0, 390, 1200, 210, GOOD_LIGHT)
    # coal plant
    f.rect(60, 300, 200, 110, IRON, INK, 3)
    for k in range(4): f.rect(80 + k * 46, 330, 26, 30, GLASS, INK, 2)
    f.rect(200, 170, 34, 130, HOT_LIGHT, INK, 3)
    for k in range(2): f.rect(200, 190 + k * 46, 34, 10, WHITE)
    H.smoke(f, 222, 150, 1.0, INK, 0.55); H.smoke(f, 330, 110, 0.9, INK, 0.4); H.smoke(f, 430, 80, 0.7, INK, 0.25)
    f.path("M30,420 h70 l20,-30 h50 l20,30 h60 v20 h-220 Z", INK)
    # wind turbines
    for k, (x, h) in enumerate(((890, 210), (990, 180), (1090, 220))): H.wind_turbine(f, x, 410, h, 0.3 + 1.1 * k, 1.0)
    # the house in the middle with its socket
    H.house(f, 520, 470, 160, 120, SAND_LIGHT, HOT)
    f.rect(546, 428, 36, 36, WHITE, INK, 2, 5)
    f.circle(564, 446, 12, ALUMINIUM, INK, 2); f.circle(559, 446, 2.5, INK); f.circle(569, 446, 2.5, INK)
    # lines from both sides to the house
    a = H.pylon(f, 360, 500, 120, 0.7); b = H.pylon(f, 820, 500, 120, 0.7)
    for p in a[2:]: H.wire(f, (250, 330), p, 10, INK, 1.5); H.wire(f, p, (530, 380), 10, INK, 1.5)
    for p in b[2:]: H.wire(f, (900, 330), p, 10, INK, 1.5); H.wire(f, p, (670, 380), 10, INK, 1.5)
    return f.svg()


def greenhouse():
    f = Fig("fy28-gh", 440, "Periaatekuva, ei mittakaavassa: kasvihuoneilmiö. Auringon säteily (oranssi nuoli), näkyvä valo ja "
            "lähi-infrapuna, kulkee suurelta osin ilmakehän läpi ja lämmittää maanpinnan. Lämmin maanpinta lähettää "
            "lämpösäteilyä ylöspäin (punaiset nuolet), ja ilmakehän kasvihuonekaasut imevät sen. Kaasut säteilevät energian "
            "uudelleen: osa palaa takaisin alas maanpinnalle ja osa karkaa avaruuteen. Nuolten paksuus havainnollistaa suuntaa, "
            "ei tarkkoja energioita.")
    f.defs_add(f'<linearGradient id="fy28-heat" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{HEAT_LIGHT}"/><stop offset="1" stop-color="{HEAT}"/></linearGradient>')
    f.defs_add(f'<linearGradient id="fy28-ir" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{HOT_LIGHT}"/><stop offset="1" stop-color="{HOT}"/></linearGradient>')
    f.defs_add(f'<radialGradient id="fy28-sun" cx="0.4" cy="0.4" r="0.7"><stop offset="0" stop-color="{HEAT_LIGHT}"/><stop offset="1" stop-color="{HEAT}"/></radialGradient>')
    f.defs_add(f'<linearGradient id="fy28-ground" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{SAND_LIGHT}"/><stop offset="1" stop-color="{SAND}"/></linearGradient>')
    # the sun with rays
    sx, sy = 76, 70
    for k in range(12):
        a = k * math.pi / 6 + math.pi / 12
        c, s_ = math.cos(a), math.sin(a)
        r0, r1, hw = 40, 56, 5
        f.path(f"M{n(sx + c * r0 - s_ * hw)},{n(sy + s_ * r0 + c * hw)} L{n(sx + c * r1)},{n(sy + s_ * r1)} "
               f"L{n(sx + c * r0 + s_ * hw)},{n(sy + s_ * r0 - c * hw)} Z", HEAT_LIGHT)
    f.circle(sx, sy, 32, "url(#fy28-sun)")
    # the atmosphere with its greenhouse gases (dashed: a layer of gas, not a lid), a few CO2 molecules drawn in
    f.rect(12, 160, 576, 60, GLASS, MUTED, 2, 10, 'stroke-dasharray="10 7"')
    for mx, my in ((46, 186), (98, 206), (512, 184), (555, 206)):
        f.circle(mx - 13, my, 5, MUTED)
        f.circle(mx + 13, my, 5, MUTED)
        f.circle(mx, my, 6.5, INK)
    f.tex(318, 190, r"\text{ilmakehä (kasvihuonekaasut)}", "middle", w=290)
    # the ground
    f.rect(12, 380, 576, 48, "url(#fy28-ground)", INK, 2.5, 6)
    f.tex(300, 404, r"\text{maanpinta}", "middle", w=140)
    # sunlight (orange) passes mostly through the layer and warms the ground
    f.block_arrow(120, 138, 196, 366, "url(#fy28-heat)", 18, 38, 30)
    f.tex(12, 292, r"\text{auringon}", "start", w=100)
    f.tex(12, 322, r"\text{säteily}", "start", w=100)
    # heat radiation of the ground (red): absorbed by the layer, then partly back and partly out
    f.block_arrow(290, 372, 290, 230, "url(#fy28-ir)", 22, 36, 28)
    f.tex(312, 300, r"\text{lämpö-}", "start", w=90)
    f.tex(312, 330, r"\text{säteily}", "start", w=100)
    f.block_arrow(460, 226, 460, 366, "url(#fy28-ir)", 14, 28, 24)
    f.tex(488, 290, r"\text{takaisin}", "start", w=100)
    f.tex(488, 320, r"\text{alas}", "start", w=60)
    f.block_arrow(460, 154, 460, 70, "url(#fy28-ir)", 8, 22, 20)
    f.tex(438, 112, r"\text{avaruuteen}", "end", w=150)
    return f.svg()


def emissions():
    f = Fig("fy28-em", 450, "Vaakapylväskaavio sähköntuotannon elinkaaren päästökertoimista yksikössä g hiilidioksidiekvivalenttia "
            "kilowattituntia kohti (IPCC AR5, työryhmä III, liite III, pyöristetyt mediaanit): kivihiili 820, maakaasu 490, "
            "biomassa 230, aurinkosähkö 41–48, vesivoima 24, ydinvoima 12 ja tuulivoima 11–12. Pylväiden pituudet ovat "
            "mittakaavassa: kivihiilen pylväs on noin 70 kertaa ydinvoiman pylvään pituinen. Fossiilisten polttoaineiden "
            "pylväät ovat tummanharmaita, muiden tuotantotapojen vaaleanharmaita; selite on kuvan alla.")
    f.tex(150, 24, r"e\ \left(\text{g}\ \text{CO}_2\text{-ekv.}/\text{kWh}\right)", "start", w=360)
    x0, per = 150, 0.44
    for t in (200, 400, 600, 800):
        f.line(x0 + t * per, 52, x0 + t * per, 352, RULE_LIGHT, 1.5)
    rows = [("kivihiili", 820, "820", IRON, None), ("maakaasu", 490, "490", IRON, None),
            ("biomassa", 230, "230", ALUMINIUM, METAL_EDGE), ("aurinko", 45, r"41\text{–}48", ALUMINIUM, METAL_EDGE),
            ("vesivoima", 24, "24", ALUMINIUM, METAL_EDGE), ("ydinvoima", 12, "12", ALUMINIUM, METAL_EDGE),
            ("tuuli", 12, r"11\text{–}12", ALUMINIUM, METAL_EDGE)]
    for i, (name, e, label, fill, edge) in enumerate(rows):
        y = 56 + 42 * i
        w = e * per
        f.rect(x0, y, w, 28, fill, edge, 1.5, 2)
        f.tex(x0 - 10, y + 14, r"\text{" + name + "}", "end", w=125)
        f.tex(x0 + w + 8, y + 14, label, "start", w=80 if "text" in label else 50)
    f.arrow(x0, 352, x0 + 800 * per + 40, 352, INK, 2.5, 13)
    f.line(x0, 50, x0, 354, INK, 2.5)
    for t in (0, 200, 400, 600, 800):
        if t: f.line(x0 + t * per, 352, x0 + t * per, 359, INK, 2)
        f.tex(x0 + t * per, 380, str(t), "middle", MUTED, w=60)
    # legend: what the two shades mean
    f.rect(150, 413, 28, 22, IRON, None, 1.5, 2)
    f.tex(186, 424, r"\text{fossiilinen}", "start", w=140)
    f.rect(350, 413, 28, 22, ALUMINIUM, METAL_EDGE, 1.5, 2)
    f.tex(386, 424, r"\text{muu}", "start", w=60)
    return f.svg()


FIGURES = {"hero": hero, "greenhouse": greenhouse, "emissions": emissions}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "emissions": "safe: the lifecycle emission factors printed at the bars; the description gives coal/nuclear ≈ 70, so do not ask that ratio",
}
