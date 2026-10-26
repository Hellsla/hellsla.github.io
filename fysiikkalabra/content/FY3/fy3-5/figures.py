"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy3-5` writes them into lesson.md."""
from figlib import Fig, INK, MUTED, RULE, GLASS, HEAT, HEAT_LIGHT, HOT, HOT_LIGHT, COLD_LIGHT, ALUMINIUM


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


FIGURES = {"two-ways": two_ways, "energy-balance": energy_balance, "work-sign": work_sign}
