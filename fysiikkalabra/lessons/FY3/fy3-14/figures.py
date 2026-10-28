"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy3-14` writes them into lesson.md."""
import herolib as H
from figlib import Fig, INK, RULE_LIGHT, HOT, HOT_LIGHT, COLD, COLD_LIGHT, ICE, ICE_EDGE, fi


def hero():
    """The chapter's opening illustration: a glass of a cold drink with ice cubes, dew on the glass."""
    f = H.hero("fy314-hero", "Kuvitus: pöydällä on korkea lasi kylmää juomaa, jossa kelluu jääpaloja ja pilli. Lasin "
               "ulkopinnalle on tiivistynyt vesipisaroita, ja lasin vieressä on jääpalarasia.")
    f.rect(0, 0, 1200, 600, H.PAPER)
    f.rect(0, 0, 1200, 380, H.grad(f, "fy314h-wall", H.WHITE, H.PAPER))
    f.rect(0, 470, 1200, 130, H.RULE)
    f.line(0, 470, 1200, 470, H.INK, 3)
    # glass, drink, ice cubes, straw
    f.path("M500,110 L520,460 Q522,474 536,474 H664 Q678,474 680,460 L700,110 Z", H.GLASS)
    drink = H.grad(f, "fy314h-drink", H.COLD_LIGHT, H.WATER_LIGHT)
    f.path("M506,190 L521,458 Q523,470 536,470 H664 Q677,470 679,458 L694,190 Z", drink)
    f.path("M640,60 L600,440", stroke=H.COLD, w=14, extra='stroke-linecap="round"')
    for x, y, a in ((540, 170, -12), (600, 184, 10), (560, 240, 24), (628, 250, -8)):
        f.add(f'<rect x="{x}" y="{y}" width="52" height="46" rx="8" transform="rotate({a} {x + 26} {y + 23})" fill="{H.ICE}" fill-opacity="0.9" stroke="{H.ICE_EDGE}" stroke-width="2.5"/>')
    f.path("M506,190 Q560,182 600,190 T694,190", stroke=H.WHITE, w=3, extra='stroke-opacity="0.8"')
    f.path("M500,110 L520,460 Q522,474 536,474 H664 Q678,474 680,460 L700,110", stroke=H.INK, w=3)
    for k in range(16):
        x = 512 + H.rnd(k, 5) * 176; y = 210 + H.rnd(k, 8) * 240
        f.add(f'<ellipse cx="{H.n(x)}" cy="{H.n(y)}" rx="4" ry="6" fill="{H.WHITE}" stroke="{H.ICE_EDGE}" stroke-width="1.5"/>')
    # ice tray beside the glass, cold air sinking
    f.rect(800, 430, 260, 40, H.COLD_LIGHT, H.INK, 3, 6)
    for x in range(816, 1040, 56): f.rect(x, 420, 42, 30, H.ICE, H.ICE_EDGE, 2, 5)
    for x in (430, 760):
        f.path(f"M{x},200 c-14,30 14,60 0,90 s14,60 0,90", stroke=H.COLD_LIGHT, w=6, extra='stroke-linecap="round"')
    return f.svg()


def energy_bars():
    """A task-only picture, to scale: three heats of one water-and-ice mixture as horizontal bars on a kJ axis, grid every
    5 kJ. The water gives off 25 kJ cooling to 0 °C, warming the ice to 0 °C needs 5 kJ and melting all of it 60 kJ."""
    f = Fig("fy314-bars", 290, "Pylväskuvaaja mittakaavassa: kolme lämpömäärää kilojouleina samasta seoksesta, jossa on vettä ja "
            "pakkasessa ollutta jäätä. Ruudukon väli on 5 kJ ja numerot joka 10 kJ:n kohdalla. Ylin pylväs, veden luovuttama "
            "lämpömäärä sen jäähtyessä 0 °C:seen, päättyy kohtaan 25 kJ. Keskimmäinen, jään lämmittämiseen 0 °C:seen tarvittava "
            "lämpömäärä, päättyy kohtaan 5 kJ. Alin, kaiken jään sulattamiseen tarvittava lämpömäärä, päättyy kohtaan 60 kJ.")
    X = lambda q: 30 + q * 6.6
    ya = 236
    for q in range(0, 71, 5):
        f.line(X(q), 20, X(q), ya, RULE_LIGHT, 1.5)
    bars = [(25, HOT_LIGHT, HOT, r"\text{vesi luovuttaa jäähtyessään } 0\,{}^\circ\text{C}\text{:seen}"),
            (5, COLD_LIGHT, COLD, r"\text{jään lämmittäminen } 0\,{}^\circ\text{C}\text{:seen}"),
            (60, ICE, ICE_EDGE, r"\text{kaiken jään sulattaminen}")]
    for k, (q, fill, edge, label) in enumerate(bars):
        y = 50 + k * 66
        f.tex(X(0) + 4, y - 16, label, "start", bg=True)
        f.rect(X(0), y, X(q) - X(0), 28, fill, edge, 2.5)
    f.arrow(X(0), ya, X(70) + 24, ya, INK, 2.5, 13)
    for q in range(0, 71, 5):
        f.line(X(q), ya, X(q), ya + 7, INK, 2)
        if q % 10 == 0:
            f.tex(X(q), ya + 26, fi(q), "middle")
    f.tex(X(70) + 30, ya, r"Q\ (\text{kJ})", "start")
    return f.svg()


FIGURES = {"hero": hero, "energy-bars": energy_bars}

REUSE = {
    "energy-bars": "safe: three heats of a water-and-ice mixture as bars, which melts and how much is to be worked out",
}
