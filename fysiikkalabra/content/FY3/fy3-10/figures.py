"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy3-10` writes them into lesson.md."""
import math, random
from figlib import Fig, INK, MUTED, WHITE, RULE, ALUMINIUM, IRON, COPPER, COLD, COLD_LIGHT, HEAT, fi
import herolib as H

HE, AIR, CO2 = COLD, IRON, COPPER           # one colour per gas, the same in every figure of the lesson


def scatter(seed, n, inside, dist, tries=40000):
    """n points that satisfy inside(x, y) and keep at least dist apart (a fixed seed: the figure never changes)."""
    rnd, pts = random.Random(seed), []
    for _ in range(tries):
        x, y = rnd.uniform(-1, 1), rnd.uniform(-1, 1)
        p = inside(x, y)
        if p is None or any(math.hypot(p[0] - a, p[1] - b) < dist for a, b in pts): continue
        pts.append(p)
        if len(pts) == n: return pts
    raise RuntimeError("could not place the particles")


def particle(f, x, y, r, color, ang, speed, ok=None):
    """A particle with a highlight and an arrow to scale: its length is its speed. ok(x, y) says whether the arrow
    tip is still inside the vessel; the direction is turned until it is."""
    if ok and speed:
        for k in range(24):
            a = ang + k * 0.7
            if ok(x + math.cos(a) * (r + 2 + speed), y + math.sin(a) * (r + 2 + speed)): ang = a; break
    c, s = math.cos(ang), math.sin(ang)
    f.circle(x, y, r, color)
    f.circle(x - r * 0.3, y - r * 0.3, r * 0.3, WHITE)
    if speed:
        f.arrow(x + c * (r + 2), y + s * (r + 2), x + c * (r + 2 + speed), y + s * (r + 2 + speed), INK, 2, 9)


def glass(f, fid):
    f.defs_add(f'<radialGradient id="{fid}" cx="0.38" cy="0.32" r="0.8"><stop offset="0" stop-color="#ffffff"/>'
               f'<stop offset="0.7" stop-color="#eef5f9"/><stop offset="1" stop-color="#d0e6fb"/></radialGradient>')


def helium_air():
    f = Fig("fy310-ball", 326, "Havainnekuva, hiukkaset kuvattu suurennettuina: kaksi yhtä suurta kaasupalloa samassa paineessa ja "
            "lämpötilassa. Kummassakin on yhtä monta hiukkasta ja ainemäärä n = 0,21 mol. Heliumpallon kaasun massa on "
            "m = 0,83 g ja ilmapallon m = 6,0 g, koska ilman hiukkaset ovat raskaampia. Nuolet näyttävät hiukkasten liikkeen "
            "mittakaavassa: kevyet heliumhiukkaset liikkuvat samassa lämpötilassa nopeammin, nuolen pituus on nopeuden suhde 2,7 : 1.")
    glass(f, "fy310-glass")
    R, cy = 86, 108
    for cx, name, col, r, sp, nm, mass, seed in ((150, "helium", HE, 5.5, 32, 4, "0{,}83", 3), (450, "ilma", AIR, 8, 12, 29, "6{,}0", 5)):
        f.circle(cx, cy, R, "url(#fy310-glass)", INK, 3)
        f.path(f"M{cx - 9},{cy + R + 12} L{cx + 9},{cy + R + 12} L{cx},{cy + R} Z", INK, INK, 2)       # the tied neck
        f.path(f"M{cx},{cy + R + 12} q -9,9 0,18", stroke=INK, w=2)
        f.path(f"M{cx - 52},{cy - 52} a 72,72 0 0 1 40,-26", stroke=WHITE, w=5, extra='stroke-linecap="round" stroke-opacity="0.9"')
        ins = lambda x, y, cx=cx: math.hypot(x - cx, y - cy) < R - 10
        pts = scatter(seed, 12, lambda x, y: (cx + x * (R - 12 - r), cy + y * (R - 12 - r)) if math.hypot(x, y) < 1 else None, 2 * r + 12)
        for k, (x, y) in enumerate(pts):
            particle(f, x, y, r, col, k * 2.399, sp, ins)
        f.tex(cx, 232, r"\text{" + name + "}", "middle")
        f.tex(cx, 264, r"n = 0{,}21\,\text{mol}", "middle")
        f.tex(cx, 296, rf"m = {mass}\,\text{{g}}", "middle")
    f.tex(300, cy, r"\text{sama}", "middle", MUTED)
    f.tex(300, cy + 30, r"p,\ T", "middle", MUTED)
    return f.svg()


def cylinder(f, x0, level, particles, speed, r=6):
    """A gas cylinder with a piston whose underside is at `level`; returns nothing. Walls 3, interior 110 wide."""
    w, top, bottom = 110, 46, 196
    f.rect(x0, level, w, bottom - level, "url(#fy310-gas)")
    f.path(f"M{x0},{top - 10} V{bottom} H{x0 + w} V{top - 10}", stroke=INK, w=3)
    f.rect(x0 + 3, level - 10, w - 6, 10, "url(#fy310-piston)", INK, 2, 2)
    f.rect(x0 + w / 2 - 4, level - 30, 8, 20, IRON, INK, 2)
    for k, (x, y) in enumerate(particles):
        particle(f, x, y, r, AIR, (k * 2.399) % (2 * math.pi), speed,
                 lambda a, b: x0 + 8 < a < x0 + w - 8 and level + 8 < b < bottom - 8)


def pressure_factors():
    f = Fig("fy310-piston", 300, "Kaavakuva neljästä männällä suljetusta kaasusylinteristä, hiukkaset suurennettuina. Vasemmalta oikealle: "
            "lähtötilassa hiukkasmäärä N, lämpötila T ja tilavuus V, ja paine on p. Paine on 2p, kun hiukkasia on kaksi kertaa "
            "enemmän (2N), kun kelvinlämpötila on kaksinkertainen (2T) eli hiukkaset liikkuvat nopeammin, tai kun mäntä on "
            "painettu puoleen tilavuuteen (V/2). Nuolten pituus kuvaa hiukkasten nopeutta.")
    f.defs_add('<linearGradient id="fy310-gas" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#d0e6fb"/>'
               '<stop offset="0.35" stop-color="#eef5f9"/><stop offset="1" stop-color="#d0e6fb"/></linearGradient>')
    f.defs_add(f'<linearGradient id="fy310-piston" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{ALUMINIUM}"/>'
               '<stop offset="1" stop-color="#8a96a3"/></linearGradient>')
    v = 14                                                # arrow length at temperature T; speed grows as sqrt(T)
    panels = [(20, 46, 6, v, r"N,\ T,\ V", "p"), (170, 46, 12, v, r"2N,\ T,\ V", "2p"),
              (320, 46, 6, v * math.sqrt(2), r"N,\ 2T,\ V", "2p"), (470, 121, 6, v, r"N,\ T,\ V/2", "2p")]
    for i, (x0, level, n, sp, lab, pr) in enumerate(panels):
        bottom = 196
        pts = scatter(10 + i, n, lambda x, y, x0=x0, level=level: (x0 + 55 + x * 42, (level + bottom) / 2 + y * ((bottom - level) / 2 - 18))
                      , 28 if i == 0 or i == 2 else 22)
        cylinder(f, x0, level, pts, sp)
        if i == 3:
            f.rect(x0, 46, 110, 75, "none", MUTED, 1.5, 0, 'stroke-dasharray="6 5"')
        f.tex(x0 + 55, 226, lab, "middle")
        f.tex(x0 + 55, 266, pr, "middle", INK)
    return f.svg()


def mole_masses():
    f = Fig("fy310-mole", 316, "Havainnekuva, hiukkaset suurennettuina ja kaavamaisina: kolme yhtä suurta astiaa samassa paineessa ja "
            "lämpötilassa, kussakin yhtä monta hiukkasta eli ainemäärä n = 1,00 mol. Moolimassa on heliumilla 4,00 g/mol, ilmalla "
            "29,0 g/mol ja hiilidioksidilla 44,0 g/mol. Palkki jokaisen astian alla on kaasun massa mittakaavassa: yksi mooli "
            "painaa eri kaasuilla eri verran.")
    glass(f, "fy310-jar")
    scale = 3.5                                              # bar units per g
    for x0, name, col, r, M, seed in ((14, "helium", HE, 5.5, 4.0, 1), (214, "ilma", AIR, 8, 29.0, 2), (414, "hiilidioksidi", CO2, 9.5, 44.0, 3)):
        f.rect(x0, 20, 130, 124, "url(#fy310-jar)", INK, 3, 8)
        pts = scatter(seed, 8, lambda x, y: (x0 + 65 + x * (65 - 14 - r), 82 + y * (62 - 14 - r)), 2 * r + 8)
        for x, y in pts: particle(f, x, y, r, col, 0, 0)
        f.tex(x0, 168, r"\text{" + name + "}", "start")
        f.tex(x0, 198, rf"M = {fi(M, 2 if M < 10 else 1)}\,\text{{g/mol}}", "start")
        f.rect(x0, 222, M * scale, 14, col, INK, 2)
        f.tex(x0, 258, rf"m = {fi(M, 2 if M < 10 else 1)}\,\text{{g}}", "start")
    f.tex(300, 296, r"\text{kussakin astiassa }n = 1{,}00\,\text{mol},\ \text{sama }p, T", "middle", MUTED, w=560)
    return f.svg()


def hero():
    """The chapter's opening illustration: a helium balloon against the ceiling, an air balloon of the same size on the floor."""
    f = H.hero("fy310-hero", "Kuvitus: huoneessa kaksi samankokoista ilmapalloa. Heliumpallo on noussut kattoon ja sen naru "
               "roikkuu alas, tavallinen ilmalla täytetty pallo lepää lattialla.")
    f.rect(0, 0, 1200, 600, H.PAPER)
    f.rect(0, 0, 1200, 24, H.WHITE); f.line(0, 24, 1200, 24, H.RULE, 3)
    f.rect(0, 500, 1200, 100, H.RULE); f.line(0, 500, 1200, 500, H.INK, 3)
    for x in range(0, 1200, 120): f.line(x, 500, x - 40, 600, H.RULE_LIGHT, 2)
    # window
    f.rect(80, 110, 240, 260, H.grad(f, "fy310h-sky", H.ICE, H.GLASS), H.INK, 3, 4)
    H.cloud(f, 180, 200, 0.5)
    f.line(200, 110, 200, 370, H.INK, 3); f.line(80, 240, 320, 240, H.INK, 3)

    def balloon(cx, cy, fill, light):
        f.path(f"M{cx},{cy + 96} Q{cx - 84},{cy + 60} {cx - 80},{cy - 10} Q{cx - 74},{cy - 92} {cx},{cy - 94} Q{cx + 74},{cy - 92} {cx + 80},{cy - 10} Q{cx + 84},{cy + 60} {cx},{cy + 96} Z", fill, H.INK, 3)
        f.path(f"M{cx - 10},{cy + 108} L{cx},{cy + 94} L{cx + 10},{cy + 108} Z", fill, H.INK, 2.5)
        f.add(f'<ellipse cx="{cx - 34}" cy="{cy - 44}" rx="16" ry="26" transform="rotate(30 {cx - 34} {cy - 44})" fill="{light}" fill-opacity="0.8"/>')
    balloon(560, 122, H.COLD, H.WHITE)
    f.path("M560,230 C540,300 590,360 560,420 S570,470 556,480", stroke=H.INK, w=2.5)
    balloon(860, 398, H.SAND_DARK, H.WHITE)
    f.add(f'<ellipse cx="860" cy="500" rx="74" ry="10" fill="{H.MUTED}" fill-opacity="0.35"/>')
    f.path("M870,506 C900,520 940,512 990,522", stroke=H.INK, w=2.5)
    return f.svg()


def scene():
    """A second everyday scene: a hot air balloon over a lake, its burner heating the air inside."""
    f = H.scene("fy310-scene", "Kuvitus: kuumailmapallo leijuu järven yllä. Korin yläpuolella palava liekki lämmittää pallon sisällä "
                "olevaa ilmaa.")
    H.sky(f, "fy310s", 280)
    H.cloud(f, 110, 80, 0.6)
    H.forest(f, 270, 34, 20, H.METAL_EDGE, seed=2, depth=20)
    f.rect(0, 280, 600, 80, H.grad(f, "fy310s-lake", H.WATER_LIGHT, H.WATER))
    cx = 360
    f.path(f"M{cx - 60},220 Q{cx - 130},140 {cx - 110},90 Q{cx - 80},20 {cx},18 Q{cx + 80},20 {cx + 110},90 Q{cx + 130},140 {cx + 60},220 Z", H.HOT_LIGHT, H.INK, 3)
    for dx in (-60, 0, 60):
        f.path(f"M{cx + dx * 0.5},220 Q{cx + dx * 1.6},110 {cx + dx * 0.4},18", stroke=H.INK, w=2)
    f.path(f"M{cx - 60},220 L{cx - 22},258 M{cx + 60},220 L{cx + 22},258", stroke=H.INK, w=2)
    f.path(f"M{cx - 10},236 q10,-26 20,0 q-10,8 -20,0 Z", H.HEAT)
    f.rect(cx - 24, 256, 48, 30, H.SAND_DARK, H.INK, 2.5, 3)
    return f.svg()


FIGURES = {"hero": hero, "scene": scene, "mole-masses": mole_masses, "helium-ilma": helium_air, "paine-ja-tekijat": pressure_factors}
