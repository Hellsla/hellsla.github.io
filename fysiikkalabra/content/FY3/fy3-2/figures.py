"""Figures of this lesson (scripts/figlib.py); `python3 scripts/figures.py fy3-2` writes them into lesson.md."""
from figlib import Fig, Axes, INK, MUTED, WHITE, RULE, RULE_LIGHT, HEAT, HEAT_LIGHT, SAND_LIGHT, SAND, SAND_DARK, GRAIN, IRON, \
    ALUMINIUM, METAL_EDGE, WATER, WATER_LIGHT, GLASS, COPPER, fi


def backpack(f, x, y):
    """A backpack seen from the side: body, flap, pocket and carrying loop; x, y its top left corner (80 by 80)."""
    f.rect(x, y, 80, 80, SAND, INK, 2.5, 14)
    f.rect(x + 12, y + 44, 56, 26, SAND_LIGHT, INK, 2, 6)
    f.path(f"M{x},{y + 30} Q{x + 40},{y + 52} {x + 80},{y + 30}", stroke=INK, w=2)
    f.path(f"M{x + 22},{y} Q{x + 40},{y - 26} {x + 58},{y}", stroke=INK, w=3)


def carry_lift():
    f = Fig("fy32-carry", 320, "Kaavakuva kahdesta tilanteesta. Vasemmalla reppua kannetaan vaakasuoraan: kannatteleva voima F "
            "osoittaa ylös, mutta liike on sivulle, joten voima ei tee työtä, W = 0. Oikealla reppu nostetaan ylös: voima F "
            "ja liike ovat samansuuntaiset, joten voima tekee työn W = F s.")
    f.tex(150, 30, r"\text{kanto sivulle}", "middle")
    f.tex(450, 30, r"\text{nosto ylös}", "middle")
    f.line(300, 20, 300, 300, RULE, 2, "6 6")
    # left: carrying, motion sideways, force up
    backpack(f, 110, 140)
    f.arrow(150, 114, 150, 62, HEAT, 5, 22)
    f.tex(166, 84, "F", "start")
    f.arrow(70, 240, 214, 240, MUTED, 3, 18)
    f.tex(142, 266, r"\text{liike}", "middle")
    f.tex(150, 306, r"W = 0", "middle")
    # right: lifting, motion upwards, force up
    backpack(f, 410, 140)
    f.arrow(450, 114, 450, 62, HEAT, 5, 22)
    f.tex(434, 84, "F", "end")
    f.arrow(520, 232, 520, 86, MUTED, 3, 18)
    f.tex(534, 160, r"\text{liike}", "start")
    f.tex(450, 306, r"W = F\,s", "middle")
    return f.svg()


def joule():
    f = Fig("fy32-joule", 340, "Kaavakuva Joulen kokeesta. Putoava paino vetää narua, joka kulkee väkipyörän yli ja pyörittää "
            "vesiastiassa olevaa siipipyörää. Painon voima tekee työn pudotusmatkalla h, ja siipipyörä lämmittää vettä: työ "
            "muuttuu lämmöksi.")
    f.defs_add('<linearGradient id="fy32-water" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#a9d1f0"/>'
               '<stop offset="1" stop-color="#2f74b5"/></linearGradient>')
    f.tex(250, 30, r"\text{työ} \to \text{lämpö}", "middle")
    # water vessel with a paddle wheel
    f.rect(62, 170, 196, 100, "url(#fy32-water)")
    f.line(62, 170, 258, 170, WATER, 2)
    f.path("M60,130 V272 H260 V130", stroke=INK, w=3)
    f.line(160, 84, 160, 246, IRON, 4)
    for y in (200, 236):
        f.rect(110, y, 100, 12, ALUMINIUM, INK, 2)
    f.circle(160, 84, 18, GLASS, INK, 3)
    f.circle(160, 84, 3, INK)
    # belt over to the weight
    f.circle(400, 84, 18, GLASS, INK, 3)
    f.circle(400, 84, 3, INK)
    f.line(160, 66, 400, 66, INK, 2)
    f.line(160, 102, 400, 102, INK, 2)
    f.line(418, 84, 418, 150, INK, 2)
    f.rect(388, 150, 60, 60, IRON, INK, 2.5, 3)
    f.tex(374, 180, r"\text{paino}", "end")
    # the fall: ghost position and the distance h
    f.rect(388, 250, 60, 60, "none", MUTED, 2, 3, 'stroke-dasharray="6 5"')
    f.line(452, 150, 500, 150, MUTED, 1.5, "6 5")
    f.line(452, 250, 500, 250, MUTED, 1.5, "6 5")
    f.arrow(488, 200, 488, 150, INK, 2.5, 14)
    f.arrow(488, 200, 488, 250, INK, 2.5, 14)
    f.tex(500, 200, "h", "start")
    f.tex(160, 304, r"\text{vesi lämpenee}", "middle")
    return f.svg()


def work_graphs():
    f = Fig("fy32-wgraphs", 340, "Kaavakuva kahdesta (s,F)-kuvaajasta. Vasemmalla voima on vakio, ja työ on suorakulmion "
            "pinta-ala F · s. Oikealla voima ensin kasvaa tasaisesti ja pysyy sitten vakiona; työ on kolmion pinta-ala A₁ "
            "plus suorakulmion pinta-ala A₂.")
    # constant force
    a = Axes(f, (60, 240), (230, 80), x=(0, 10), y=(0, 10), xticks=[], yticks=[], xlabel="s", ylabel="F", grid=False,
             origin_label=False)
    a.area([(0, 0), (0, 6), (8, 6), (8, 0)], HEAT_LIGHT, 0.55)
    a.guide(8, 6)
    a.line([(0, 6), (8, 6)], HEAT, 4)
    f.tex(a.x0 - 12, a.Y(6), "F", "end")
    f.tex(a.X(8), a.y0 + 24, "s", "middle")
    f.tex(a.X(4), a.Y(3), r"W = F\,s", "middle")
    f.tex(a.X(4), 306, r"\text{vakiovoima}", "middle")
    # force growing then constant
    b = Axes(f, (350, 240), (520, 80), x=(0, 10), y=(0, 10), xticks=[], yticks=[], xlabel="s", ylabel="F", grid=False,
             origin_label=False)
    b.area([(0, 0), (4, 6), (4, 0)], HEAT, 0.4)
    b.area([(4, 0), (4, 6), (9, 6), (9, 0)], HEAT_LIGHT, 0.55)
    b.guide(9, 6)
    b.line([(4, 6), (4, 0)], MUTED, 1.5, "6 5")
    b.line([(0, 0), (4, 6), (9, 6)], HEAT, 4)
    f.tex(b.x0 - 12, b.Y(6), "F", "end")
    f.tex(b.X(9), b.y0 + 24, "s", "middle")
    f.tex(b.X(3), b.Y(1.6), "A_1", "middle")
    f.tex(b.X(6.5), b.Y(3), "A_2", "middle")
    f.tex(b.X(4.5), 306, r"\text{muuttuva voima}", "middle")
    return f.svg()


def spring_work():
    f = Fig("fy32-spring", 320, "(s,F)-kuvaaja mittakaavassa: voima kasvaa suoraviivaisesti nollasta 40 newtoniin matkalla "
            "0–0,20 metriä; kolmion pinta-ala on työ.")
    ax = Axes(f, (92, 270), (470, 56), x=(0, 0.25), y=(0, 50), xticks=[0.05, 0.10, 0.15, 0.20], yticks=[10, 20, 30, 40],
              xlabel=r"s\ (\text{m})", ylabel=r"F\ (\text{N})", xfmt=lambda v: fi(v, 2))
    ax.area([(0, 0), (0.2, 40), (0.2, 0)], HEAT_LIGHT, 0.6)
    ax.guide(0.2, 40)
    ax.line([(0, 0), (0.2, 40)], HEAT, 3)
    ax.point(0.2, 40, HEAT)
    f.tex(ax.X(0.14), ax.Y(7), r"W = \text{pinta-ala}", "middle")
    return f.svg()


def lift_work():
    f = Fig("fy32-lift", 330, "Kaavakuva nostotyöstä, ei mittakaavassa. Laatikko nostetaan tasaisella nopeudella maasta "
            "korkeudelle h. Nostovoima F osoittaa ylös ja laatikon paino G alas, ja nuolet ovat yhtä pitkät, F = G. "
            "Nostotyö on W = F h = G h.")
    f.defs_add('<pattern id="fy32-ground" width="12" height="12" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">'
               f'<line x1="0" y1="0" x2="0" y2="12" stroke="{MUTED}" stroke-width="1.5"/></pattern>')
    f.rect(30, 292, 300, 12, "url(#fy32-ground)")
    f.line(30, 292, 330, 292, INK, 3)

    def crate(y, dashed=False):
        if dashed:
            f.rect(140, y, 80, 60, "none", MUTED, 2, 3, 'stroke-dasharray="6 5"')
            return
        f.rect(140, y, 80, 60, SAND, INK, 2.5, 3)
        f.rect(150, y + 10, 60, 40, SAND_LIGHT, INK, 1.5)
        f.line(150, y + 10, 210, y + 50, GRAIN, 1.5)
        f.line(210, y + 10, 150, y + 50, GRAIN, 1.5)
    crate(232, True)
    crate(92)
    # forces of equal length on the raised crate
    f.arrow(180, 92, 180, 34, HEAT, 5, 22)
    f.tex(196, 54, "F", "start")
    f.arrow(180, 152, 180, 210, INK, 5, 22)
    f.tex(196, 190, "G", "start")
    # the motion, and the height h between the crate's bottoms
    f.arrow(90, 262, 90, 126, MUTED, 3, 18)
    f.tex(78, 196, r"\text{liike}", "end")
    f.line(224, 152, 290, 152, MUTED, 1.5, "6 5")
    f.line(224, 292, 290, 292, MUTED, 1.5, "6 5")
    f.arrow(276, 222, 276, 152, INK, 2.5, 14)
    f.arrow(276, 222, 276, 292, INK, 2.5, 14)
    f.tex(290, 222, "h", "start")
    # the relations
    f.tex(372, 80, r"F = G", "start")
    f.tex(372, 150, r"W = F\,h", "start")
    f.tex(372, 200, r"W = G\,h", "start")
    f.tex(372, 250, r"W = m\,g\,h", "start")
    return f.svg()


FIGURES = {"carry-lift": carry_lift, "joule": joule, "work-graphs": work_graphs, "spring-work": spring_work,
           "lift-work": lift_work}
