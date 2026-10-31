"""Figures of the investigation Kaasun tilanyhtälön kokeellinen tutkiminen (scripts/figlib.py); `python
scripts/investigations.py figures fy10-kaasu` writes them into investigation.md. The graphs show models only, never
invented measurements; temperatures in the models are in kelvins."""
from figlib import Fig, Axes, INK, MUTED, WHITE, RULE, RULE_LIGHT, GLASS, WATER_LIGHT, WATER, ALUMINIUM, METAL_EDGE, IRON, \
    SAND, SAND_DARK, GRAIN, ICE, ICE_EDGE, COLD, HOT, n
import herolib as H
from herolib import grad


def beaker(f, x, ytop, w, ybot, level, water):
    """An open beaker from ytop to ybot with water up to `level`."""
    outline = f"M{x},{ytop} V{ybot - 10} Q{x},{ybot} {x + 10},{ybot} H{x + w - 10} Q{x + w},{ybot} {x + w},{ybot - 10} V{ytop}"
    f.path(outline, GLASS)
    f.path(f"M{x + 3},{level} H{x + w - 3} V{ybot - 10} Q{x + w - 3},{ybot - 3} {x + w - 10},{ybot - 3} H{x + 10} "
           f"Q{x + 3},{ybot - 3} {x + 3},{ybot - 10} Z", water)
    f.path(outline, stroke=INK, w=3)


def flask(f, cx, cy, r, neck_top, neck_w=22):
    """A round flask (gas inside: light glass) with its neck up to neck_top and a stopper."""
    f.rect(cx - neck_w / 2, neck_top, neck_w, cy - r - neck_top + 6, GLASS, INK, 3)
    f.circle(cx, cy, r, GLASS, INK, 3)
    f.rect(cx - neck_w / 2 + 2, cy - r - 4, neck_w - 4, 12, GLASS)      # hide the joint line
    f.rect(cx - neck_w / 2 - 4, neck_top - 16, neck_w + 8, 20, IRON, INK, 2.5, rx=3)


def sensor(f, x, y, w=96, h=46):
    """A pressure sensor box with a short inlet on its left side."""
    f.rect(x, y, w, h, ALUMINIUM, INK, 2.5, rx=8)
    f.rect(x + 12, y + 12, w - 24, h - 24, WHITE, METAL_EDGE, 1.5, rx=3)


def syringe(f, x0, x1, y, h, gas_from, scale=True):
    """A horizontal syringe: barrel from x0 to x1 (nozzle at x1), plunger head at gas_from, rod out to the left."""
    f.rect(gas_from, y - h / 2 + 3, x1 - gas_from - 3, h - 6, GLASS)
    f.rect(x0, y - h / 2, x1 - x0, h, "none", INK, 3, rx=4)
    f.rect(x1, y - 6, 22, 12, WHITE, INK, 2.5)                           # nozzle
    f.rect(gas_from - 12, y - h / 2 + 3, 12, h - 6, IRON, INK, 2)       # plunger head
    f.rect(x0 - 70, y - 5, gas_from - 12 - x0 + 70, 10, ALUMINIUM, INK, 2)   # rod
    f.rect(x0 - 82, y - h / 2 - 2, 12, h + 4, IRON, INK, 2.5, rx=3)     # thumb pad
    f.rect(x0 - 6, y - h / 2 - 12, 6, h + 24, ALUMINIUM, INK, 2)         # finger flange
    if scale:
        for k in range(1, int((x1 - x0) / 20)):
            xx = x0 + 20 * k
            f.line(xx, y - h / 2, xx, y - h / 2 + (12 if k % 5 == 0 else 7), INK, 1.5)


def hero():
    """The opening illustration: a lab bench with a syringe on a pressure sensor, a flask in a water bath with a
    temperature probe, an ice bath, a kettle and a laptop."""
    f = H.hero("fy10k-hero", "Kuvitus: laboratorion työpöydällä on vasemmalla mäntäruisku, joka on liitetty lyhyellä "
               "letkulla paineanturiin. Keskellä lasikolvi on upotettu vesihauteeseen, ja sen tulpasta lähtee letku "
               "toiseen paineanturiin hauteen ulkopuolella. Hauteessa on myös lämpötila-anturi. Oikealla on astia "
               "jäävettä ja vedenkeitin. Taaempana on kannettava tietokone, johon anturit on kytketty johdoilla.")
    f.rect(0, 0, 1200, 600, grad(f, "fy10kh-wall", GLASS, "#dfe9ef"))
    f.rect(0, 470, 1200, 130, grad(f, "fy10kh-desk", SAND_DARK, SAND, horizontal=True))
    for k in range(5): f.line(0, 492 + 22 * k, 1200, 488 + 22 * k, GRAIN, 1.5)
    f.line(0, 470, 1200, 470, INK, 3)
    water = grad(f, "fy10kh-water", WATER_LIGHT, WATER)
    # laptop at the back, screen showing a blank data table (no results)
    f.path("M470,300 L760,300 L780,330 L450,330 Z", IRON, INK, 2.5)
    f.rect(490, 130, 250, 170, INK, INK, 3, rx=8)
    f.rect(504, 144, 222, 142, WHITE)
    for k in range(6): f.line(514, 166 + 20 * k, 716, 166 + 20 * k, RULE, 2)
    f.line(615, 152, 615, 278, RULE, 2)
    # syringe on the left, lying on the desk, tube to sensor 1
    syringe(f, 120, 330, 430, 40, 230)
    f.path("M352,430 C380,430 380,440 400,440", stroke=INK, w=7)
    sensor(f, 400, 418)
    f.path("M496,440 C530,440 520,380 560,340 L560,330", stroke=INK, w=3)    # cable to the laptop
    # water bath with the flask (centre)
    beaker(f, 600, 300, 230, 470, 330, water)
    flask(f, 690, 410, 48, 300)
    f.path("M690,284 V252 Q690,232 710,232 H830 Q846,232 846,252 V447 H852", stroke=INK, w=7)
    sensor(f, 852, 424)
    f.path("M900,424 C900,360 800,340 765,318", stroke=INK, w=3)              # cable to the laptop
    # temperature probe in the bath
    f.rect(781, 290, 10, 160, ALUMINIUM, INK, 2.5, rx=4)
    f.rect(776, 270, 20, 26, IRON, INK, 2.5, rx=4)
    f.path("M786,270 C786,230 760,250 740,300", stroke=INK, w=3)
    # ice water and a kettle on the right
    beaker(f, 970, 340, 120, 470, 370, water)
    for k, (dx, dy) in enumerate(((10, 372), (46, 366), (82, 374), (28, 404), (66, 410))):
        f.rect(960 + dx, dy, 32, 28, ICE, ICE_EDGE, 2, rx=5)
    f.path("M1150,392 Q1180,392 1180,420 Q1180,452 1162,456", stroke=INK, w=8)          # handle
    f.path("M1100,470 L1108,384 Q1112,364 1132,364 H1140 Q1158,364 1160,384 L1166,470 Z", ALUMINIUM, INK, 3)
    f.path("M1104,420 L1090,404", stroke=INK, w=6)                                       # spout
    f.rect(1118, 354, 34, 12, IRON, INK, 2.5, rx=4)
    # notebook
    f.add('<g transform="translate(150,530) rotate(-5)">'
          f'<rect x="-90" y="-36" width="210" height="68" rx="4" fill="{WHITE}" stroke="{INK}" stroke-width="2.5"/>'
          + "".join(f'<line x1="-74" y1="{-20 + 12 * k}" x2="104" y2="{-20 + 12 * k}" stroke="{COLD}" stroke-width="1.5" stroke-opacity="0.6"/>' for k in range(5))
          + "</g>")
    return f.svg()


def setup():
    """Both arrangements: the syringe on a pressure sensor (volume read from the scale) and the flask in a water
    bath with a pressure sensor outside the bath and a temperature probe in the water."""
    f = Fig("fy10k-setup", 470, "Kaaviokuva kahdesta mittausjärjestelystä. Ylhäällä mäntäruisku, jonka tilavuus V "
            "luetaan ruiskun asteikolta, on liitetty lyhyellä letkulla paineanturiin, joka mittaa paineen p. Alhaalla "
            "lasikolvi on upotettu vesihauteeseen. Kolvin tulpasta lähtee lyhyt letku hauteen ulkopuolella olevaan "
            "paineanturiin, joka mittaa paineen p. Hauteessa kolvin vieressä on lämpötila-anturi, joka mittaa "
            "hauteen lämpötilan theta.")
    # top: syringe and sensor
    syringe(f, 150, 360, 90, 44, 230)
    f.line(230, 46, 382, 46, MUTED, 1.5); f.line(230, 38, 230, 54, MUTED, 2); f.line(382, 38, 382, 54, MUTED, 2)
    f.tex(306, 24, r"V", "middle")
    f.path("M382,90 H440", stroke=INK, w=7)
    sensor(f, 440, 67)
    f.tex(488, 136, r"\text{paineanturi}", "middle", MUTED)
    f.tex(552, 90, r"p", "start")
    f.tex(255, 140, r"\text{ruisku}", "middle", MUTED)
    f.line(20, 176, 580, 176, RULE_LIGHT, 2)
    # bottom: water bath, flask, sensors
    water = grad(f, "fy10ks-water", WATER_LIGHT, WATER)
    beaker(f, 70, 250, 280, 450, 280, water)
    flask(f, 180, 370, 58, 240)
    f.path("M180,224 V212 Q180,200 192,200 H478 Q498,200 498,220 V226", stroke=INK, w=7)
    sensor(f, 450, 226)
    f.tex(558, 249, r"p", "start")
    f.tex(498, 296, r"\text{paineanturi}", "middle", MUTED)
    f.rect(296, 260, 10, 160, ALUMINIUM, INK, 2.5, rx=4)
    f.rect(291, 236, 20, 28, IRON, INK, 2.5, rx=4)
    f.line(306, 380, 366, 380, MUTED, 1.5)
    f.tex(372, 362, r"\theta", "start")
    f.tex(372, 396, r"\text{lämpötila-anturi}", "start", MUTED)
    f.tex(210, 432, r"\text{vesihaude}", "middle", WHITE)
    return f.svg()


def boyle():
    """Boyle's law model: p against 1/V is a line through the origin with slope pV (no measured points)."""
    f = Fig("fy10k-boyle", 330, "Kuvaaja: paine p tilavuuden käänteisluvun yksi per V funktiona ideaalikaasun mallin "
            "mukaan, kun lämpötila ja kaasun määrä pysyvät samoina. Kuvaaja on origon kautta kulkeva suora, jonka "
            "kulmakerroin on tulo p kertaa V. Kuvaajassa ei ole mittauspisteitä.")
    ax = Axes(f, (90, 280), (470, 50), x=(0, 10), y=(0, 10), xticks=[], yticks=[], xlabel=r"\dfrac{1}{V}", ylabel=r"p", grid=False)
    ax.line([(0, 0), (9.5, 8.55)], INK)
    f.tex(ax.X(3.4), ax.Y(7.0), r"\text{kulmakerroin } pV", "middle")
    return f.svg()


def isokoori():
    """The isochoric model: p against the kelvin temperature is a line through the origin; measurements only cover
    the liquid-water range, the rest is a dashed extrapolation (no measured points)."""
    f = Fig("fy10k-isokoori", 340, "Kuvaaja: paine p kelvinlämpötilan T funktiona ideaalikaasun mallin mukaan, kun "
            "tilavuus ja kaasun määrä pysyvät samoina. Kuvaaja on suora, joka kulkee origon kautta. Yhtenäinen osa "
            "suorasta on alueella, jolla vesihaude on nestettä, noin 273 kelvinistä 373 kelviniin. Katkoviivalla "
            "piirretty jatke ulottuu origoon eli nollaan kelviniin. Kuvaajassa ei ole mittauspisteitä.")
    ax = Axes(f, (90, 270), (470, 50), x=(0, 400), y=(0, 10), xticks=[273, 373], yticks=[], xlabel=r"T\ (\text{K})",
              ylabel=r"p", grid=False, xfmt=lambda v: f"{v}", origin_label=False)
    f.tex(ax.x0, ax.y0 + 24, r"0", "middle")
    k = 8.6 / 390
    ax.line([(0, 0), (273, k * 273)], MUTED, 3, "10 8")
    ax.line([(273, k * 273), (373, k * 373)], INK, 3.5)
    for t in (273, 373): f.line(ax.X(t), ax.Y(k * t), ax.X(t), ax.y0, MUTED, 1.5, "6 5")
    f.tex(ax.X(323), ax.y0 + 54, r"\text{mittausalue}", "middle", MUTED)
    f.tex(ax.X(130), ax.Y(k * 130) - 30, r"\text{jatke}", "middle", MUTED)
    return f.svg()


FIGURES = {"hero": hero, "setup": setup, "boyle": boyle, "isokoori": isokoori}
