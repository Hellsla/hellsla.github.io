"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy4-10` writes them into lesson.md.
Colours: velocity blue (#1971c2), force red (#c92a2a), momentum purple (#7048e8, its own colour in FY4, distinct from
velocity, force and acceleration)."""
import math
from figlib import (Fig, INK, MUTED, WHITE, RULE, RULE_LIGHT, HEAT, HEAT_LIGHT, HOT, HOT_LIGHT, COLD, COLD_LIGHT, GOOD,
                    GOOD_LIGHT, ALUMINIUM, METAL_EDGE, IRON, COPPER, SAND_LIGHT, SAND, SAND_DARK, GLASS, ICE, PAPER, n)
import herolib as H

RED = HOT              # forces
BLUE = COLD            # velocity
PURPLE = "#7048e8"     # momentum
WOOD_DARK = "#8a5f22"


def track(f, x0, x1, y):
    """An air track seen from the side: an aluminium beam with a row of air holes, its top surface at y."""
    f.rect(x0, y, x1 - x0, 14, ALUMINIUM, METAL_EDGE, 2, 2)
    for x in range(int(x0) + 14, int(x1) - 8, 18): f.circle(x, y + 7, 1.8, METAL_EDGE)


def glider(f, x, y, w, h, body, num=None, mass=None):
    """A glider on the air track: its bottom at y, centre x; a body colour and an optional LaTeX number."""
    f.rect(x - w / 2, y - h, w, h, body, INK, 2.5, 4)
    f.rect(x - w / 2 + 6, y - 6, w - 12, 6, METAL_EDGE)
    if num: f.tex(x, y - h / 2 - 2, num, "middle", INK, 24)


def spring(f, xa, xb, y, turns=5, amp=7, color=IRON):
    """A coil spring as a zigzag between xa and xb at height y."""
    pts = [(xa, y)] + [(xa + (xb - xa) * (i + 0.5) / (2 * turns), y + (amp if i % 2 else -amp)) for i in range(2 * turns)] + [(xb, y)]
    f.path("M" + " L".join(f"{n(a)},{n(b)}" for a, b in pts), stroke=color, w=2.5)


def vuorovaikutus():
    """Ydinajatus: during the collision the gliders push each other with equal and opposite forces for the same time,
    so their momentum changes are equal and opposite."""
    f = Fig("fy410-vv", 340, "Kaavakuva, ei mittakaavassa: kaksi ilmatyynyradan vaunua törmäyksen aikana. Vaunujen väliin jäävä "
            "jousipuskuri on puristunut. Ylhäällä punaiset voimanuolet: vaunu 1 työntää vaunua 2 oikealle voimalla F, ja vaunu 2 "
            "työntää vaunua 1 vasemmalle yhtä suurella vastakkaissuuntaisella voimalla −F. Molemmat voimat vaikuttavat saman ajan Δt. "
            "Alhaalla violetit nuolet ovat liikemäärien muutokset: vaunun 1 muutos Δp1 = −FΔt osoittaa vasemmalle ja vaunun 2 "
            "muutos Δp2 = FΔt oikealle, yhtä pitkinä. Niiden summa on nolla.")
    ty = 150
    track(f, 30, 570, ty)
    glider(f, 210, ty, 150, 64, SAND_LIGHT); glider(f, 400, ty, 150, 64, ALUMINIUM)
    f.tex(250, ty - 46, "1", "middle", INK, 24); f.tex(360, ty - 46, "2", "middle", INK, 24)
    spring(f, 285, 325, ty - 22, 3, 8)
    # forces from the contact: on 2 to the right, on 1 to the left
    f.arrow(325, ty - 22, 440, ty - 22, RED, 4, 15); f.arrow(285, ty - 22, 170, ty - 22, RED, 4, 15)
    f.tex(505, 60, r"\overline{F}", "middle", RED); f.tex(95, 60, r"-\overline{F}", "middle", RED)
    f.line(497, 74, 440, ty - 28, RED, 1.5); f.line(103, 74, 170, ty - 28, RED, 1.5)
    f.tex(300, 40, r"\Delta t", "middle")
    f.line(20, 196, 580, 196, RULE, 2, "6 6")
    # momentum changes, to scale with each other
    f.arrow(300, 236, 170, 236, PURPLE, 5, 16); f.arrow(300, 236, 430, 236, PURPLE, 5, 16)
    f.line(300, 222, 300, 250, INK, 2)
    f.tex(160, 272, r"\Delta\overline{p}_1 = -\overline{F}\,\Delta t", "middle", PURPLE)
    f.tex(440, 272, r"\Delta\overline{p}_2 = \overline{F}\,\Delta t", "middle", PURPLE)
    f.tex(300, 314, r"\Delta\overline{p}_1 + \Delta\overline{p}_2 = \overline{0}", "middle")
    return f.svg()


def tarra():
    """Ydinajatus: a perfectly inelastic collision of equal gliders, to scale: the velocity halves, the total momentum stays."""
    f = Fig("fy410-tarra", 360, "Kaavakuva mittakaavassa: kaksi samanmassaista vaunua ilmatyynyradalla, ylhäällä ennen törmäystä ja "
            "alhaalla sen jälkeen. Ennen törmäystä vaunu 1 liikkuu oikealle nopeudella v, ja sen liikemäärä p on violetti nuoli; vaunu 2 "
            "on levossa. Vaunujen päissä on tarranauhat. Törmäyksen jälkeen vaunut ovat tarttuneet yhteen ja liikkuvat yhdessä puolella "
            "alkuperäisestä nopeudesta, sininen nuoli on puolet lyhyempi. Yhteisen liikemäärän violetti nuoli on yhtä pitkä kuin vaunun 1 "
            "liikemäärä ennen törmäystä.")
    vs, ps = 220, 220                       # px per v and per p (v = 0,60 m/s ↔ 132 px; p = mv)
    for row, y in enumerate((150, 318)):
        track(f, 30, 570, y)
        f.tex(36, y - 128 if row == 0 else y - 118, r"\text{ennen}" if row == 0 else r"\text{jälkeen}", "start")
    # before: glider 1 moving, glider 2 at rest
    y = 150
    glider(f, 170, y, 100, 48, SAND_LIGHT, "1"); glider(f, 400, y, 100, 48, ALUMINIUM, "2")
    f.rect(220, y - 40, 5, 32, MUTED); f.rect(345, y - 40, 5, 32, MUTED)
    f.arrow(120, y - 66, 120 + 0.60 * vs, y - 66, BLUE, 3, 12); f.tex(120 + 0.60 * vs + 8, y - 66, r"\overline{v}", "start", BLUE)
    f.arrow(120, y - 98, 120 + 0.60 * ps, y - 98, PURPLE, 5, 16); f.tex(120 + 0.60 * ps + 8, y - 98, r"\overline{p}", "start", PURPLE)
    f.tex(400, y - 70, r"\overline{v}_2 = \overline{0}", "middle")
    f.line(20, 178, 580, 178, RULE, 2, "6 6")
    # after: stuck together, half the velocity, the same momentum
    y = 318
    glider(f, 250, y, 100, 48, SAND_LIGHT, "1"); glider(f, 350, y, 100, 48, ALUMINIUM, "2")
    f.arrow(200, y - 66, 200 + 0.30 * vs, y - 66, BLUE, 3, 12); f.tex(200 + 0.30 * vs + 8, y - 66, r"\tfrac{1}{2}\overline{v}", "start", BLUE)
    f.arrow(200, y - 98, 200 + 0.60 * ps, y - 98, PURPLE, 5, 16); f.tex(200 + 0.60 * ps + 8, y - 98, r"\overline{p}", "start", PURPLE)
    return f.svg()


def tyypit():
    """Kaava: three kinds of one-dimensional events with equal masses, momentum arrows to scale; what happens to E_k."""
    f = Fig("fy410-tyypit", 434, "Kaavakuva, liikemäärät mittakaavassa: kolme tapahtumaa kahdelle samanmassaiselle vaunulle, vasemmalla "
            "ennen ja oikealla jälkeen. Ylimpänä kimmoisa törmäys: ennen vaunulla 1 on liikemäärä oikealle ja vaunu 2 on levossa, jälkeen "
            "vaunu 1 on levossa ja vaunulla 2 on sama liikemäärä; liike-energia säilyy. Keskellä täysin kimmoton törmäys: vaunut tarttuvat "
            "yhteen, ja yhteinen liikemäärä on yhtä suuri kuin ennen; liike-energia pienenee. Alimpana räjähdys: ennen vaunut ovat yhdessä "
            "levossa ja kokonaisliikemäärä on nolla, jälkeen vaunuilla on yhtä suuret vastakkaissuuntaiset liikemäärät; liike-energia kasvaa.")
    rows = [(r"\text{kimmoisa: } E_\text{k}\ \text{säilyy}", 152), (r"\text{täysin kimmoton: } E_\text{k}\ \text{pienenee}", 282),
            (r"\text{räjähdys: } E_\text{k}\ \text{kasvaa}", 412)]
    P = 110                                   # px of the momentum arrow p
    for k, (title, y) in enumerate(rows):
        if k: f.line(20, y - 112, 580, y - 112, RULE, 2, "6 6")
        f.tex(300, y - 92, title, "middle", w=420)
        f.line(40, y, 270, y, METAL_EDGE, 3); f.line(330, y, 560, y, METAL_EDGE, 3)
        f.arrow(282, y - 20, 318, y - 20, MUTED, 2.5, 10)
        if k == 0:
            glider(f, 90, y, 50, 30, SAND_LIGHT); glider(f, 220, y, 50, 30, ALUMINIUM)
            f.arrow(70, y - 46, 70 + P, y - 46, PURPLE, 4, 14)
            glider(f, 360, y, 50, 30, SAND_LIGHT); glider(f, 450, y, 50, 30, ALUMINIUM)
            f.arrow(440, y - 46, 440 + P, y - 46, PURPLE, 4, 14)
        elif k == 1:
            glider(f, 90, y, 50, 30, SAND_LIGHT); glider(f, 220, y, 50, 30, ALUMINIUM)
            f.arrow(70, y - 46, 70 + P, y - 46, PURPLE, 4, 14)
            glider(f, 420, y, 50, 30, SAND_LIGHT); glider(f, 470, y, 50, 30, ALUMINIUM)
            f.arrow(390, y - 46, 390 + P, y - 46, PURPLE, 4, 14)
        else:
            glider(f, 130, y, 50, 30, SAND_LIGHT); glider(f, 180, y, 50, 30, ALUMINIUM); spring(f, 150, 160, y - 15, 1, 5)
            f.tex(155, y - 48, r"p_\text{kok} = 0", "middle", PURPLE)
            glider(f, 370, y, 50, 30, SAND_LIGHT); glider(f, 520, y, 50, 30, ALUMINIUM)
            f.arrow(390, y - 46, 390 - 0.6 * P, y - 46, PURPLE, 4, 14); f.arrow(500, y - 46, 500 + 0.6 * P, y - 46, PURPLE, 4, 14)
    f.tex(155, 18, r"\text{ennen}", "middle", MUTED); f.tex(445, 18, r"\text{jälkeen}", "middle", MUTED)
    return f.svg()


def ball(f, gid, cx, cy, r, c1, c2):
    f.defs_add(f'<radialGradient id="{gid}" cx="0.35" cy="0.3" r="0.75"><stop offset="0" stop-color="{c1}"/><stop offset="1" stop-color="{c2}"/></radialGradient>')
    f.add(f'<ellipse cx="{n(cx + r * 0.2)}" cy="{n(cy + r * 0.9)}" rx="{n(r * 0.95)}" ry="{n(r * 0.28)}" fill="{INK}" fill-opacity="0.25"/>')
    f.circle(cx, cy, r, f"url(#{gid})", INK, 2)


def hero():
    """The chapter's opening illustration: a billiard table; the cue ball has hit the red ball head-on and stopped."""
    f = H.hero("fy410-hero", "Kuvitus: biljardipöytä läheltä nähtynä pöydän yllä roikkuvan lampun valossa. Vasemmalta alhaalta pöydälle "
               "osoittaa biljardikeppi, jolla valkoista lyöntipalloa on juuri lyöty. Lyöntipallo on osunut suoraan punaiseen palloon, ja hetki törmäyksen jälkeen "
               "se on pysähtynyt pöydän keskelle; sen takana näkyy haalea jälki kuljetusta matkasta. Punainen pallo kiitää eteenpäin kohti pöydän "
               "oikeaa reunaa, ja sen takana on liikeviivoja. Pöydän takaosassa on kolme muuta palloa.")
    # the room: a warm wall with wooden wainscot
    f.rect(0, 0, 1200, 600, H.grad(f, "fy410h-wall", PAPER, SAND_DARK, y1=0, y2=420))
    f.rect(0, 150, 1200, 120, H.grad(f, "fy410h-panel", SAND, WOOD_DARK, y1=150, y2=270))
    for x in range(75, 1200, 150): f.line(x, 150, x, 270, WOOD_DARK, 3)
    f.line(0, 150, 1200, 150, WOOD_DARK, 4)
    # the lamp: a cord, a green shade and its warm light on the table
    f.line(600, 0, 600, 40, INK, 4)
    f.add(f'<path d="M420,118 L780,118 L1080,520 L120,520 Z" fill="{HEAT_LIGHT}" fill-opacity="0.16"/>')
    f.path("M430,118 L770,118 L720,44 L480,44 Z", GOOD, INK, 3)
    f.rect(450, 118, 300, 8, HEAT_LIGHT, rx=3)
    # the table in perspective: the wooden rail, the cushions, the felt and the pockets
    f.path("M20,590 L1180,590 L1040,236 L160,236 Z", COPPER, INK, 3)
    f.path("M20,590 L1180,590 L1180,600 L20,600 Z", WOOD_DARK)
    f.path("M74,566 L1126,566 L1006,256 L194,256 Z", GOOD, INK, 2.5)
    felt = H.grad(f, "fy410h-felt", GOOD_LIGHT, GOOD, y1=180, y2=640)
    f.path("M104,550 L1096,550 L986,270 L214,270 Z", felt)
    f.add(f'<ellipse cx="600" cy="400" rx="380" ry="120" fill="{WHITE}" fill-opacity="0.16"/>')
    for x, y, rx in ((64, 572, 34), (600, 576, 32), (1136, 572, 34), (180, 250, 24), (600, 248, 22), (1020, 250, 24)):
        f.add(f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{rx * 0.5:g}" fill="{INK}"/>')
    for x in (300, 900):
        f.circle(x, 578, 5, SAND_LIGHT); f.circle(x + (40 if x < 600 else -40), 244, 4, SAND_LIGHT)
    # three balls at the back of the table
    ball(f, "fy410h-yellow", 360, 300, 20, HEAT_LIGHT, HEAT)
    ball(f, "fy410h-blue", 870, 296, 20, COLD_LIGHT, COLD)
    ball(f, "fy410h-black", 914, 318, 21, METAL_EDGE, INK)
    # the cue ball's path (faint), the cue ball at rest, the red ball rolling away with speed lines
    for k in range(6): f.line(330 + k * 42, 440, 356 + k * 42, 440, WHITE, 4, cap="round")
    ball(f, "fy410h-white", 620, 432, 32, WHITE, ALUMINIUM)
    for k, dy in enumerate((-16, 0, 16)):
        f.line(700 + k * 10, 430 + dy, 760 + k * 4, 430 + dy, WHITE, 4, cap="round")
    ball(f, "fy410h-red", 812, 430, 32, HOT_LIGHT, HOT)
    # the cue from the lower left, its tip just behind where the cue ball started
    f.path("M-10,566 L4,598 L292,468 L284,452 Z", SAND, INK, 2)
    f.path("M-10,566 L4,598 L100,554 L88,524 Z", WOOD_DARK, INK, 2)
    f.path("M292,468 L284,452 L298,446 L306,462 Z", COLD_LIGHT, INK, 1.5)
    return f.svg()


FIGURES = {"hero": hero, "vuorovaikutus": vuorovaikutus, "tarra": tarra, "tyypit": tyypit}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "vuorovaikutus": "reveals: equal and opposite impulses in a collision, Δp1 = −Δp2",
    "tarra": "reveals: a perfectly inelastic collision of equal masses halves the velocity and keeps the momentum",
    "tyypit": "reveals: what happens to the momenta and to E_k in elastic, perfectly inelastic collisions and an explosion",
}
