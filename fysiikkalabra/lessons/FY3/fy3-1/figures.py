"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy3-1` writes them into lesson.md."""
from figlib import Fig, Axes, INK, MUTED, WHITE, RULE, HEAT, HEAT_LIGHT, ALUMINIUM, METAL_EDGE, IRON, WATER, COPPER, GRAIN, fi
import herolib as H


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


def hero():
    """The chapter's opening illustration: an astronaut hopping on the Moon, the Earth in the black sky."""
    f = H.hero("fy31-hero", "Kuvitus: astronautti loikkaa Kuun harmaalla pinnalla, ja hänen jalanjälkensä näkyvät pölyssä. "
               "Mustalla taivaalla näkyy Maa, jossa on meriä, mantereita ja pilviä.")
    H.space(f, seed=3)
    H.earth(f, "fy31h", 930, 150, 80)
    ground = H.grad(f, "fy31h-ground", H.ALUMINIUM, H.METAL_EDGE)
    f.path("M0,420 Q600,360 1200,430 V600 H0 Z", ground)
    for cx, cy, rx in ((180, 500, 70), (820, 470, 50), (1040, 540, 90), (520, 560, 40)):
        f.add(f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{rx * 0.28:g}" fill="{H.METAL_EDGE}" stroke="{H.ALUMINIUM}" stroke-width="3"/>')
    for k, x in enumerate(range(250, 470, 44)):
        f.add(f'<ellipse cx="{x}" cy="{440 + (k % 2) * 16 - k * 4}" rx="13" ry="6" fill="{H.IRON}" fill-opacity="0.6"/>')
    f.add(f'<ellipse cx="600" cy="440" rx="70" ry="12" fill="{H.IRON}" fill-opacity="0.6"/>')   # the shadow under the hop
    # astronaut in mid-hop: backpack, suit, helmet with visor
    x, y = 600, 360
    f.rect(x - 70, y - 190, 44, 110, H.ALUMINIUM, H.INK, 3, 10)
    f.path(f"M{x - 40},{y - 70} L{x - 70},{y + 10} L{x - 40},{y + 24} L{x - 10},{y - 50} Z", H.WHITE, H.INK, 3)
    f.path(f"M{x + 10},{y - 60} L{x + 60},{y - 10} L{x + 44},{y + 12} L{x - 6},{y - 30} Z", H.WHITE, H.INK, 3)
    f.rect(x - 52, y - 200, 104, 140, H.WHITE, H.INK, 3, 30)
    f.path(f"M{x + 46},{y - 170} L{x + 100},{y - 210}", stroke=H.INK, w=27, extra='stroke-linecap="round"')
    f.path(f"M{x + 46},{y - 170} L{x + 100},{y - 210}", stroke=H.WHITE, w=21, extra='stroke-linecap="round"')
    f.path(f"M{x - 46},{y - 160} L{x - 92},{y - 110}", stroke=H.INK, w=27, extra='stroke-linecap="round"')
    f.path(f"M{x - 46},{y - 160} L{x - 92},{y - 110}", stroke=H.WHITE, w=21, extra='stroke-linecap="round"')
    f.rect(x - 22, y - 160, 44, 30, H.COLD_LIGHT, H.INK, 2, 4)
    f.circle(x, y - 236, 50, H.WHITE, H.INK, 3)
    visor = H.grad(f, "fy31h-visor", H.HEAT_LIGHT, H.IRON)
    f.rect(x - 34, y - 262, 68, 46, visor, H.INK, 3, 20)
    f.path(f"M{x - 22},{y - 252} q14,-6 26,0", stroke=H.WHITE, w=4, extra='stroke-linecap="round"')
    return f.svg()


def scene():
    """A second everyday scene: the same backpack on a spring scale on the Earth and on the Moon."""
    f = H.scene("fy31-scene", "Kuvitus: sama reppu riippuu jousivaa'assa Maassa ja Kuussa. Maassa jousi venyy pitkäksi, Kuussa "
                "vain kuudesosan siitä, koska Kuu vetää reppua kuusi kertaa heikommin. Venymät on piirretty mittakaavassa.")
    f.rect(0, 0, 300, 360, H.grad(f, "fy31s-sky", H.ICE, H.GLASS))
    f.rect(300, 0, 300, 360, H.INK)
    for k in range(30): f.circle(310 + H.rnd(k, 2) * 280, H.rnd(k + 50, 2) * 300, 1 + H.rnd(k + 90, 2) * 1.4, H.WHITE)
    H.earth(f, "fy31s", 540, 60, 26)
    f.path("M0,320 Q150,310 300,322 V360 H0 Z", H.SAND)
    f.path("M300,322 Q450,306 600,320 V360 H300 Z", H.ALUMINIUM)
    f.line(300, 0, 300, 360, H.WHITE, 3)

    def scale(x, stretch, ink=H.INK):
        f.rect(x - 70, 20, 140, 14, H.IRON, H.INK, 2, 3)          # the beam it hangs from
        f.rect(x - 14, 34, 28, 30, H.ALUMINIUM, H.INK, 2.5, 4)
        coils = 9; top, bot = 64, 64 + 24 + stretch
        d = f"M{x},{top}"
        for k in range(coils):
            y0 = top + (bot - top) * k / coils; y1 = top + (bot - top) * (k + 0.5) / coils
            d += f" L{x + 14},{H.n(y1)} L{x - 14},{H.n(y0 + (bot - top) / coils)}"
        f.path(d + f" L{x},{H.n(bot)}", stroke=ink, w=2.5)
        f.path(f"M{x},{H.n(bot)} v12 q0,10 -10,10", stroke=ink, w=3)
        y = bot + 30
        f.rect(x - 40, y, 80, 96, H.COLD, H.INK, 3, 18)
        f.rect(x - 28, y + 46, 56, 36, H.COLD_LIGHT, H.INK, 2, 8)
        f.path(f"M{x - 20},{y} Q{x},{y - 18} {x + 20},{y}", stroke=ink, w=4)
    scale(150, 120)          # on the Earth
    scale(450, 20, H.WHITE)  # on the Moon: one sixth
    return f.svg()


def spring_points():
    """Calibration points of a spring for a task (scripts/figcat.py variant of `force-extension`): the student reads the
    points off a grid and uses the proportionality; the description lists the points, not the ratio."""
    f = Fig("fy31-spring-points", 330, "Kuvaaja mittakaavassa: erään jousen venymä x senttimetreinä voiman F funktiona. "
            "Viisi mittauspistettä ilman piirrettyä suoraa: (2 N; 1 cm), (4 N; 2 cm), (6 N; 3 cm), (8 N; 4 cm) ja (10 N; 5 cm). "
            "Ruudukon väli on 1 N ja 1 cm.")
    ax = Axes(f, (92, 290), (500, 70), x=(0, 11), y=(0, 6), xticks=list(range(1, 11)), yticks=[1, 2, 3, 4, 5],
              xlabel=r"F\ (\text{N})", ylabel=r"x\ (\text{cm})",
              xfmt=lambda v: fi(v) if v % 2 == 0 else "", yfmt=lambda v: fi(v))
    for F in [2, 4, 6, 8, 10]:
        ax.point(F, F / 2, WATER)
    return f.svg()


FIGURES = {"hero": hero, "scene": scene, "forcemeter": forcemeter, "force-extension": force_extension, "weight-mass": weight_mass, "spring-points": spring_points}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "forcemeter": "safe: double weight, double extension, no values",
    "force-extension": "reveals: the points and x/F = 0,4 cm/N",
    "weight-mass": "reveals: the weights of 100 kg on Earth, Mars and the Moon",
    "spring-points": "safe: five (F, x) calibration points of a spring without the line; the description lists the points",
}
