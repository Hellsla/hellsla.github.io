"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy3-1` writes them into lesson.md."""
from figlib import Fig, Axes, INK, MUTED, WHITE, RULE, HEAT, HEAT_LIGHT, ALUMINIUM, METAL_EDGE, IRON, WATER, COPPER, GRAIN, fi


def forcemeter():
    f = Fig("fy31-meter", 410, "Voimamittari, periaatekuva, ei mittakaavassa. Kaksi samanlaista jousta ripustettu "
            "telineeseen: vasemmanpuoleiseen on ripustettu kappale, jonka massa on m, oikeanpuoleiseen kaksi samanlaista "
            "kappaletta. Kaksinkertainen paino venyttää jousta kaksinkertaisen matkan. Kunkin kappaleen paino G on "
            "alaspäin osoittava nuoli.")
    f.defs_add('<pattern id="fy31-hatch" width="10" height="10" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">'
               f'<line x1="0" y1="0" x2="0" y2="10" stroke="{MUTED}" stroke-width="2"/></pattern>')
    f.rect(60, 20, 420, 16, "url(#fy31-hatch)")
    f.line(60, 36, 480, 36, INK, 3)
    rest = 70                       # unloaded spring length; one load stretches it by 50
    for cx, k in ((170, 1), (370, 2)):
        top, length = 36, rest + 50 * k
        f.line(cx, top, cx, top + 12, INK, 2.5)
        coils, a, b = 8 if k == 1 else 8, top + 12, top + length - 12
        pts = [(cx, a)] + [(cx + (14 if i % 2 == 0 else -14), a + (b - a) * (i + 0.5) / coils) for i in range(coils)] + [(cx, b)]
        f.path("M" + " L".join(f"{x:g},{y:g}" for x, y in pts), stroke=IRON, w=3)
        f.line(cx, b, cx, top + length, INK, 2.5)
        hook = top + length
        f.path(f"M{cx},{hook} v6 a7,7 0 1,1 -7,7", stroke=INK, w=2.5)
        y = hook + 14
        for j in range(k):
            f.rect(cx - 30, y, 60, 42, ALUMINIUM, INK, 2.5, 5)
            f.tex(cx, y + 21, "m", "middle")
            if j < k - 1:
                f.line(cx, y + 42, cx, y + 50, INK, 2.5)
            y += 50
        bottom = y - 8
        f.arrow(cx, bottom, cx, bottom + 36 * k, HEAT, 4, 16)        # arrow length to scale: 2G is twice G
        f.tex(cx + 14, bottom + 18 * k + 4, "G" if k == 1 else "2G", "start")
    # the extension, to scale: one load 50, two loads 100
    for cx, k in ((170, 1), (370, 2)):
        x = cx + 74 if k == 1 else cx + 74
        y0, y1 = 36 + rest, 36 + rest + 50 * k
        f.line(cx + 22, y0, x + 8, y0, MUTED, 1.5, "5 4")
        f.line(cx + 22, y1, x + 8, y1, MUTED, 1.5, "5 4")
        f.path(f"M{x},{y0} h8 M{x + 4},{y0} V{y1} M{x},{y1} h8", stroke=INK, w=2)
        f.tex(x + 16, (y0 + y1) / 2, "x" if k == 1 else "2x", "start")
    return f.svg()


def force_extension():
    f = Fig("fy31-graph", 330, "Kuvaaja mittakaavassa: jousen venymä x senttimetreinä voiman F funktiona, kun F on "
            "0–11 N. Mittauspisteet 2,5 N ja 1,0 cm, 5,0 N ja 2,0 cm sekä 10 N ja 4,0 cm ovat samalla origon kautta "
            "kulkevalla suoralla; katkoviivat näyttävät pisteiden arvot akseleilla.")
    ax = Axes(f, (92, 290), (478, 70), x=(0, 11), y=(0, 5), xticks=[2.5, 5, 7.5, 10], yticks=[1, 2, 3, 4],
              xlabel=r"F\ (\text{N})", ylabel=r"x\ (\text{cm})",
              xfmt=lambda v: fi(v, 1) if v < 10 else fi(v), yfmt=lambda v: fi(v, 1))
    ax.line([(0, 0), (11, 4.4)], WATER, 3)
    for p in [(2.5, 1), (5, 2), (10, 4)]:
        ax.guide(*p)
    for p in [(2.5, 1), (5, 2), (10, 4)]:
        ax.point(*p)
    f.tex(ax.X(6.2), ax.Y(1.2), r"\text{suora origon kautta}", "start", bg=True)
    return f.svg()


def weight_mass():
    f = Fig("fy31-gm", 336, "Kuvaaja mittakaavassa: paino G newtoneina massan m funktiona, kun m on 0–100 kg. "
            "Neljä origon kautta kulkevaa suoraa, jyrkimmästä loivimpaan: Jupiter (suora jatkuu kuvan yläreunan yli), "
            "Maa (100 kg painaa 981 N), Mars (371 N) ja Kuu (162 N).")
    ax = Axes(f, (100, 300), (440, 60), x=(0, 100), y=(0, 1100), xticks=[25, 50, 75, 100], yticks=[250, 500, 750, 1000],
              xlabel=r"m\ (\text{kg})", ylabel=r"G\ (\text{N})")
    bodies = [("Jupiter", 24.8, GRAIN), ("Maa", 9.81, WATER), ("Mars", 3.71, COPPER), ("Kuu", 1.62, IRON)]
    for name, g, col in bodies:
        m_end = min(100, 1100 / g)
        ax.line([(0, 0), (m_end, g * m_end)], col, 3.5)
        x, y = ax.X(m_end), ax.Y(g * m_end)
        if m_end < 100:
            f.tex(x + 10, y + 2, r"\text{" + name + "}", "start", col)
        else:
            f.tex(x + 12, min(y, ax.y0 - 42), r"\text{" + name + "}", "start", col)   # clear of the m axis title
    return f.svg()


FIGURES = {"forcemeter": forcemeter, "force-extension": force_extension, "weight-mass": weight_mass}
