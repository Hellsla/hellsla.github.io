"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy3-5` writes them into lesson.md."""
from figlib import Fig, INK, MUTED, RULE, GLASS, HEAT, HEAT_LIGHT, HOT, HOT_LIGHT, COLD_LIGHT, ALUMINIUM
import herolib as H


def cylinder(f, x0, x1, ytop, ybot, piston_x, gas_fill):
    """A horizontal cylinder open at the left, closed at x1, with a piston at piston_x and gas to its right."""
    f.rect(piston_x + 16, ytop, x1 - piston_x - 16, ybot - ytop, gas_fill)
    f.path(f"M{x0},{ytop} H{x1} V{ybot} H{x0}", stroke=INK, w=3)
    f.rect(piston_x, ytop + 1.5, 16, ybot - ytop - 3, ALUMINIUM, INK, 2)


def particles(f, pts, color=HOT):
    for x, y in pts:
        f.circle(x, y, 6, color, "#ffffff", 1.5)


def two_ways():
    f = Fig("fy35-ways", 316, "Kaksi tapaa muuttaa sisäenergiaa (kaaviokuva, ei mittakaavassa). Vasemmalla mäntä työntyy "
            "sylinteriin ja tekee ilmaan työn W, ja ilman hiukkaset liikkuvat nopeammin. Oikealla kuuma ja kylmä kappale "
            "koskettavat, ja lämpömäärä Q siirtyy kuumasta kylmään.")
    f.tex(160, 28, r"\text{työ}", "middle")
    f.tex(450, 28, r"\text{lämpö}", "middle")
    # left: a piston compresses the air, the particles move faster (longer velocity arrows)
    cylinder(f, 70, 280, 112, 236, 112, HOT_LIGHT)
    f.block_arrow(22, 174, 108, 174, HEAT, 14, 30, 22)
    f.tex(60, 128, "W", "middle")
    pts = [(160, 142, 22, -8), (216, 140, 24, 8), (254, 188, -22, 12), (176, 196, 20, -18), (150, 176, 22, -10), (222, 214, -24, -4)]
    for x, y, dx, dy in pts:
        f.arrow(x, y, x + dx, y + dy, HOT, 2, 9)
    particles(f, [(x, y) for x, y, _, _ in pts])
    f.tex(175, 276, r"\text{ilma kuumenee}", "middle")
    f.line(300, 20, 300, 292, MUTED, 2, "6 6")
    # right: two blocks in contact, heat flows from the hot to the cold one
    f.rect(322, 112, 120, 124, HOT_LIGHT, INK, 3)
    f.rect(442, 112, 120, 124, COLD_LIGHT, INK, 3)
    f.tex(382, 174, r"\text{kuuma}", "middle")
    f.tex(502, 174, r"\text{kylmä}", "middle")
    f.block_arrow(352, 92, 532, 92, HEAT, 16, 34, 28)
    f.tex(442, 58, "Q", "middle")
    f.tex(442, 276, r"\text{kuumasta kylmään}", "middle")
    return f.svg()


def energy_balance():
    f = Fig("fy35-balance", 300, "Energiakaavio: systeemiin tulee lämpömäärä Q ja työ W, ja systeemin sisäenergia muuttuu "
            "niiden summan verran. Ulos siirtyvä energia on negatiivista.")
    f.rect(206, 62, 188, 160, GLASS, INK, 3, 14)
    f.tex(300, 118, r"\text{systeemi}", "middle")
    f.tex(300, 166, r"\Delta U = Q + W", "middle")
    f.block_arrow(24, 100, 200, 100, HEAT, 16, 34, 28)
    f.tex(112, 66, r"\text{lämpö}\ Q", "middle")
    f.block_arrow(24, 186, 200, 186, HEAT, 16, 34, 28)
    f.tex(112, 224, r"\text{työ}\ W", "middle")
    f.block_arrow(400, 142, 576, 142, HEAT_LIGHT, 16, 34, 28)
    f.tex(488, 102, r"Q < 0\ \text{tai}\ W < 0", "middle")
    f.tex(488, 178, r"\text{ulos}", "middle")
    f.tex(300, 262, r"\text{sisään positiivinen, ulos negatiivinen}", "middle")
    return f.svg()


def work_sign():
    f = Fig("fy35-sign", 316, "Työn etumerkki (kaaviokuva, ei mittakaavassa). Vasemmalla mäntää työnnetään sisään ja kaasu "
            "puristuu: ympäristö tekee kaasuun työn, joten W on positiivinen. Oikealla kaasu työntää mäntää ulos ja "
            "laajenee: kaasu tekee työn ympäristöön, joten W on negatiivinen.")
    f.tex(175, 28, r"\text{puristus}", "middle")
    f.tex(455, 28, r"\text{laajeneminen}", "middle")
    cylinder(f, 70, 280, 100, 210, 126, GLASS)
    f.block_arrow(22, 155, 122, 155, HEAT, 14, 30, 22)
    particles(f, [(168, 124), (212, 130), (252, 150), (186, 160), (232, 186), (166, 192), (206, 108 + 70)])
    cylinder(f, 330, 580, 100, 210, 400, GLASS)
    f.block_arrow(396, 155, 336, 155, HEAT, 14, 30, 22)
    particles(f, [(450, 122), (520, 128), (556, 158), (478, 156), (536, 190), (448, 190), (500, 108 + 70)])
    f.line(300, 20, 300, 292, MUTED, 2, "6 6")
    f.tex(175, 246, r"W > 0", "middle")
    f.tex(455, 246, r"W < 0", "middle")
    f.tex(175, 284, r"\text{ympäristö tekee työn}", "middle")
    f.tex(455, 284, r"\text{kaasu tekee työn}", "middle")
    return f.svg()


def hero():
    """The chapter's opening illustration: hands pumping a bicycle tyre, the bottom of the pump getting hot."""
    f = H.hero("fy35-hero", "Kuvitus: kädet painavat jalkapumpun kahvaa alas, ja letku vie ilman polkupyörän renkaaseen. Pumpun "
               "alaosa on lämmennyt, mitä kuvaavat oranssi hehku ja väreilevät viivat.")
    f.rect(0, 0, 1200, 600, H.PAPER)
    f.rect(0, 520, 1200, 80, H.RULE)
    f.line(0, 520, 1200, 520, H.INK, 3)
    # tyre and wheel on the right
    f.circle(930, 330, 210, "none", H.INK, 34)
    f.circle(930, 330, 186, "none", H.METAL_EDGE, 4)
    for k in range(16):
        a = k * H.math.pi / 8
        f.line(930, 330, 930 + 184 * H.math.cos(a), 330 + 184 * H.math.sin(a), H.METAL_EDGE, 2)
    f.circle(930, 330, 22, H.ALUMINIUM, H.INK, 3)
    f.rect(764, 270, 24, 14, H.IRON, H.INK, 2, 2)
    # pump: foot, barrel with the warm bottom, rod, T-handle, hose to the valve
    f.rect(300, 500, 200, 22, H.IRON, H.INK, 3, 6)
    warm = H.grad(f, "fy35h-barrel", H.ALUMINIUM, H.HEAT_LIGHT)
    f.rect(370, 220, 60, 284, warm, H.INK, 3, 8)
    f.add(f'<rect x="370" y="400" width="60" height="104" rx="8" fill="{H.HEAT}" fill-opacity="0.55"/>')
    f.rect(370, 220, 60, 284, extra=f'rx="8" fill="none" stroke="{H.INK}" stroke-width="3"')
    f.rect(392, 140, 16, 84, H.ALUMINIUM, H.INK, 2)
    f.rect(300, 124, 200, 28, H.INK, rx=14)
    f.path("M430,470 C520,470 560,400 640,380 S740,300 776,280", stroke=H.INK, w=12, extra='stroke-linecap="round"')
    H.shimmer(f, (340, 460), 470, 80)
    # hands on the handle, sleeves
    for x in (330, 470):
        f.path(f"M{x},90 L{x - (40 if x < 400 else -40)},-10", stroke=H.COLD, w=58, extra='stroke-linecap="round"')
        f.add(f'<ellipse cx="{x}" cy="128" rx="38" ry="30" fill="{H.SAND_LIGHT}" stroke="{H.INK}" stroke-width="2.5"/>')
    f.block_arrow(560, 70, 560, 180, H.COLD, 14, 34, 26)
    return f.svg()


FIGURES = {"hero": hero, "two-ways": two_ways, "energy-balance": energy_balance, "work-sign": work_sign}
