"""Figures of fy4-3 (scripts/figlib.py, scripts/fbd.py, scripts/herolib.py); `python scripts/figures.py fy4-3` writes them
into lesson.md. Every force diagram is an FBD: the object alone as a plain rectangle, each force starting at its point of
application, its physics checked as it is drawn; the situation is a separate pictorial situation picture (tilannekuva).
Forces are red, velocity blue, no point-particle diagrams (docs/force-diagrams.md)."""
import math
from figlib import (Fig, INK, MUTED, WHITE, RULE, RULE_LIGHT, GLASS, ICE, ICE_EDGE, COLD, COLD_LIGHT, HOT, HOT_LIGHT,
                    HEAT, HEAT_LIGHT, GOOD, GOOD_LIGHT, SAND_LIGHT, SAND, SAND_DARK, GRAIN, ALUMINIUM, METAL_EDGE, IRON,
                    COPPER, n, fi)
from fbd import FBD, ground
import herolib as H
from herolib import grad, rnd

# the interaction pair data of the collision graph (example data, lesson-answers.py reads the same peak)
PEAK = 4.0          # N, the largest force between the carts
T0, T1 = 0.05, 0.15  # s, the contact begins and ends


# ---------------------------------------------------------------- shared drawing pieces
def stone(f, cx, ybase, w=96, handle=HOT, gid="fy43-granite"):
    """A curling stone in side view: a granite body with a dark striking band and a coloured handle; base on ybase."""
    h = w * 0.46
    if f"id=\"{gid}\"" not in "".join(f.defs):
        f.defs_add(f'<linearGradient id="{gid}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{ALUMINIUM}"/>'
                   f'<stop offset="0.55" stop-color="{METAL_EDGE}"/><stop offset="1" stop-color="{IRON}"/></linearGradient>')
    x0, top = cx - w / 2, ybase - h
    f.path(f"M{n(x0 + w * 0.08)},{n(ybase)} Q{n(x0 - w * 0.02)},{n(ybase - h * 0.5)} {n(x0 + w * 0.1)},{n(top)} H{n(x0 + w * 0.9)} "
           f"Q{n(x0 + w * 1.02)},{n(ybase - h * 0.5)} {n(x0 + w * 0.92)},{n(ybase)} Z", f"url(#{gid})", INK, 2.5)
    f.path(f"M{n(x0 + w * 0.02)},{n(ybase - h * 0.5)} H{n(x0 + w * 0.98)}", stroke=INK, w=max(2, w * 0.05))
    for k in range(5):                                         # a few granite flecks
        f.circle(x0 + w * (0.2 + 0.15 * k), top + h * (0.22 + 0.5 * rnd(k, 3) * 0.4), max(1.2, w * 0.018), WHITE)
    f.rect(cx - w * 0.07, top - w * 0.1, w * 0.14, w * 0.1, handle, INK, 2)
    f.path(f"M{n(cx - w * 0.04)},{n(top - w * 0.1)} L{n(cx + w * 0.02)},{n(top - w * 0.2)} H{n(cx + w * 0.32)}",
           stroke=handle, w=max(4, w * 0.075), extra='stroke-linecap="round"')


def skater(f, x, yf, s, facing, coat, trousers=INK, hand=None):
    """A skater in side view, arms stretched forward to push: feet on yf, facing +1 (right) or -1 (left).
    Returns the point of the hands."""
    d = facing
    hip, sh, head = (x, yf - 92 * s), (x + d * 10 * s, yf - 172 * s), (x + d * 16 * s, yf - 212 * s)
    for dx in (-14, 12):                                       # legs and skates
        foot = (x + d * dx * s, yf - 8 * s)
        f.path(f"M{n(hip[0])},{n(hip[1])} L{n(foot[0])},{n(foot[1])}", stroke=trousers, w=20 * s, extra='stroke-linecap="round"')
        f.path(f"M{n(foot[0] - d * 8 * s)},{n(yf - 6 * s)} h{n(d * 26 * s)}", stroke=INK, w=10 * s, extra='stroke-linecap="round"')
        f.line(foot[0] - d * 14 * s, yf, foot[0] + d * 24 * s, yf, METAL_EDGE, max(2, 3 * s), cap="round")
    f.path(f"M{n(hip[0] - 22 * s)},{n(hip[1] + 6 * s)} Q{n(x - d * 4 * s)},{n(yf - 190 * s)} {n(sh[0] + d * 16 * s)},{n(sh[1])} "
           f"L{n(hip[0] + d * 24 * s)},{n(hip[1] + 6 * s)} Z", coat, INK, 2.5)
    hand = hand or (x + d * 74 * s, yf - 150 * s)
    f.path(f"M{n(sh[0])},{n(sh[1] + 6 * s)} L{n(hand[0])},{n(hand[1])}", stroke=coat, w=16 * s, extra='stroke-linecap="round"')
    f.circle(hand[0], hand[1], 9 * s, SAND_LIGHT, INK, 1.5)
    f.circle(head[0], head[1], 24 * s, SAND_LIGHT, INK, 2)
    f.path(f"M{n(head[0] - 25 * s)},{n(head[1] + 2 * s)} Q{n(head[0] - 24 * s)},{n(head[1] - 30 * s)} {n(head[0])},{n(head[1] - 28 * s)} "
           f"Q{n(head[0] + 24 * s)},{n(head[1] - 30 * s)} {n(head[0] + 25 * s)},{n(head[1] + 2 * s)} Z", coat, INK, 2)
    return hand


# ---------------------------------------------------------------- the opening illustration
def hero():
    """The Miksi scene: a curling stone glides down the sheet long after the thrower has let go; nothing pushes it."""
    f = H.hero("fy43-hero", "Kuvitus: curlinghalli. Vasemmalla heittäjä on liukunut matalassa heittoasennossa ja päästänyt kivestä irti, "
               "ja hänen ojennettu kätensä on jo kaukana kivestä. Keskellä punakahvainen curlingkivi liukuu jäällä oikealle, ja sen "
               "takana näkyy ohut jälki. Kaksi harjaajaa kulkee kiven edellä harjat jäätä vasten. Oikealla jäässä on maalialueen "
               "renkaat, joissa on jo kaksi kiveä.")
    # the hall: wall, roof trusses and lamps
    f.rect(0, 0, 1200, 330, grad(f, "fy43h-wall", COLD_LIGHT, GLASS))
    f.rect(0, 0, 1200, 70, grad(f, "fy43h-roof", ALUMINIUM, COLD_LIGHT))
    for k in range(13):
        x = k * 100
        f.line(x, 70, x + 50, 8, METAL_EDGE, 2); f.line(x + 50, 8, x + 100, 70, METAL_EDGE, 2)
    f.line(0, 8, 1200, 8, METAL_EDGE, 3); f.line(0, 70, 1200, 70, METAL_EDGE, 3)
    for k in range(6):
        cx = 100 + k * 200
        f.add(f'<ellipse cx="{cx}" cy="96" rx="70" ry="22" fill="{WHITE}" fill-opacity="0.55"/>')
        f.rect(cx - 40, 82, 80, 12, WHITE, METAL_EDGE, 2, 4)
    # back wall: large flat banners and a window strip
    for k, c in enumerate((HOT_LIGHT, COLD_LIGHT, HEAT_LIGHT, GOOD_LIGHT, HOT_LIGHT, COLD_LIGHT)):
        f.rect(40 + k * 196, 150, 150, 70, c, METAL_EDGE, 2, 4)
        f.rect(56 + k * 196, 168, 70, 10, WHITE); f.rect(56 + k * 196, 188, 110, 8, WHITE, extra='fill-opacity="0.7"')
    f.rect(0, 240, 1200, 40, GLASS, METAL_EDGE, 2)
    for k in range(25): f.line(k * 50, 240, k * 50, 280, METAL_EDGE, 1.5)
    # the boards along the far side of the sheet
    f.rect(0, 300, 1200, 70, WHITE, INK, 3)
    for k, c in enumerate((COLD, HOT, GOOD, HEAT, COLD, HOT, GOOD, HEAT)):
        f.rect(18 + k * 150, 314, 116, 40, c, INK, 2, 3); f.rect(32 + k * 150, 328, 60, 10, WHITE, extra='fill-opacity="0.85"')
    f.rect(0, 296, 1200, 8, ALUMINIUM, INK, 2)
    # the ice sheet
    f.rect(0, 370, 1200, 230, grad(f, "fy43h-ice", WHITE, COLD_LIGHT, y1=370, y2=600))
    f.line(0, 371, 1200, 371, ICE_EDGE, 2)
    for k in range(160):                                       # the pebbled ice
        f.add(f'<circle cx="{n(rnd(k, 5) * 1200)}" cy="{n(380 + rnd(k, 8) * 215)}" r="{n(1 + 1.5 * rnd(k, 11))}" fill="{ICE_EDGE}" fill-opacity="0.25"/>')
    # sheet markings: centre line, hog line, tee line, back line
    f.line(0, 482, 1200, 482, RULE, 2)
    f.line(470, 374, 470, 598, HOT, 4)                         # hog line
    f.line(1040, 374, 1040, 598, RULE, 2)                      # tee line
    # the house: concentric rings seen at a low angle
    for rx, ry, c in ((180, 58, COLD), (124, 40, WHITE), (74, 24, HOT), (26, 8, WHITE)):
        f.add(f'<ellipse cx="1040" cy="482" rx="{rx}" ry="{ry}" fill="{c}" stroke="{INK}" stroke-width="2"/>')
    stone(f, 1110, 470, 58, HEAT_LIGHT, "fy43h-g1")
    stone(f, 968, 500, 62, HOT, "fy43h-g2")
    # the stone's faint track and motion marks
    f.path("M400,500 Q520,499 560,499", stroke=ICE_EDGE, w=3, extra='stroke-linecap="round" stroke-opacity="0.5"')
    for k, (x, y, L) in enumerate(((470, 468, 50), (450, 482, 70), (480, 494, 40))):
        f.path(f"M{x},{y} h{L}", stroke=MUTED, w=3, extra=f'stroke-linecap="round" stroke-opacity="{0.35 + 0.15 * k:.2f}"')
    f.add('<ellipse cx="610" cy="502" rx="74" ry="9" fill="#4f8fbf" fill-opacity="0.25"/>')
    stone(f, 608, 500, 136, HOT, "fy43h-g0")
    # the thrower: low sliding delivery, the right hand just opened, far behind the stone
    hip, knee, ff, back = (236, 452), (300, 436), (306, 498), (110, 500)
    f.path(f"M{hip[0]},{hip[1]} L{back[0] + 10},{back[1] - 8}", stroke=INK, w=26, extra='stroke-linecap="round"')
    f.path(f"M{back[0] - 4},{back[1] - 2} h34", stroke=IRON, w=14, extra='stroke-linecap="round"')
    f.path(f"M{hip[0]},{hip[1]} L{knee[0]},{knee[1]} L{ff[0]},{ff[1] - 10}", stroke=INK, w=26, extra='stroke-linecap="round" stroke-linejoin="round"')
    f.path(f"M{ff[0] - 16},{ff[1] - 4} h46", stroke=INK, w=14, extra='stroke-linecap="round"')
    f.path(f"M{hip[0] - 26},{hip[1] + 10} Q{hip[0] - 10},{hip[1] - 60} {hip[0] + 60},{hip[1] - 78} L{hip[0] + 84},{hip[1] - 50} "
           f"Q{hip[0] + 40},{hip[1] - 20} {hip[0] + 30},{hip[1] + 12} Z", COLD, INK, 3)
    sh = (hip[0] + 70, hip[1] - 64)
    hand = (sh[0] + 120, sh[1] + 50)
    f.path(f"M{sh[0]},{sh[1]} L{hand[0]},{hand[1]}", stroke=COLD, w=20, extra='stroke-linecap="round"')
    f.circle(hand[0] + 6, hand[1] + 2, 12, SAND_LIGHT, INK, 2)
    head = (sh[0] + 36, sh[1] - 36)
    f.circle(head[0], head[1], 30, SAND_LIGHT, INK, 2)
    f.path(f"M{head[0] - 31},{head[1] + 2} Q{head[0] - 30},{head[1] - 38} {head[0] + 2},{head[1] - 36} Q{head[0] + 32},{head[1] - 34} {head[0] + 31},{head[1] - 6} "
           f"Q{head[0]},{head[1] - 16} {head[0] - 31},{head[1] + 2} Z", INK)
    # the broom in the other hand, held out behind for balance
    f.path(f"M{sh[0] - 20},{sh[1] + 10} L{hip[0] - 60},{hip[1] + 20}", stroke=COLD, w=18, extra='stroke-linecap="round"')
    f.line(hip[0] - 40, hip[1] + 4, hip[0] - 150, hip[1] + 42, INK, 6, cap="round")
    f.rect(hip[0] - 182, hip[1] + 38, 60, 14, HOT, INK, 2, 4)
    # two sweepers ahead of the stone, brooms on the ice in front of it
    for x, yf, sc, coat in ((770, 452, 0.5, HOT), (850, 590, 0.6, COLD)):
        hd = (x + 64 * sc, yf - 230 * sc)
        H.walker(f, x, yf, coat, INK, sc, lean=40, hand=hd, winter=False, stride=0.8)
        tip = (712 if yf < 500 else 730, 492 if yf < 500 else 516)
        f.line(hd[0], hd[1], tip[0] + 18, tip[1] - 6, INK, 6, cap="round")
        f.rect(tip[0] - 14, tip[1] - 10, 50, 14, HEAT_LIGHT if coat == HOT else HOT, INK, 2, 4)
        for k in range(4):                                     # a little ice spray from the broom
            f.circle(tip[0] - 20 - 8 * k, tip[1] + 2 - 4 * (k % 2), 2.5, WHITE, ICE_EDGE, 1)
    return f.svg()


# ---------------------------------------------------------------- theory figures
CURL = dict(G=100.0, Fmu=24.0)        # the drawn lengths (schematic: friction drawn longer than it is)


def curling():
    """Ydinajatus: a curling stone sliding after release, its situation picture and its force diagram (no forward force)."""
    f = Fig("fy43-curling", 340, "Kaksi kuvaa liukuvasta curlingkivestä. Vasemmalla tilannekuva: kivi liukuu jäällä oikealle, ja sen yllä "
            "ohut sininen nuoli v näyttää nopeuden oikealle. Heittäjän käsi on jäänyt kauas taakse. Oikealla voimakuvio: kivi "
            "suorakulmiona. Paino G osoittaa keskipisteestä alas, jään tukivoima N alapinnasta ylös yhtä pitkänä, ja jään pieni "
            "kitkavoima alapinnan takakulmasta vasemmalle. Eteenpäin osoittavaa voimaa ei ole. Kuva ei ole mittakaavassa: "
            "kitkavoiman nuoli on piirretty selvyyden vuoksi todellista pidemmäksi.")
    f.tex(150, 24, r"\text{tilannekuva}", "middle", MUTED)
    f.rect(16, 230, 270, 46, grad(f, "fy43c-ice", GLASS, COLD_LIGHT), None)
    f.line(16, 230, 286, 230, ICE_EDGE, 2.5, cap="round")
    f.circle(44, 214, 11, SAND_LIGHT, INK, 2)                  # the thrower's open hand, left behind
    f.path("M16,206 Q26,210 33,212", stroke=COLD, w=14, extra='stroke-linecap="round"')
    for k, (y, L) in enumerate(((206, 34), (216, 52), (224, 28))):
        f.path(f"M{116 - L},{y} h{L}", stroke=MUTED, w=2.5, extra=f'stroke-linecap="round" stroke-opacity="{0.4 + 0.2 * k:.1f}"')
    stone(f, 180, 230, 96, HOT, "fy43c-granite")
    FBD(f, 1).motion(r"\overline{v}", (1, 0), (146, 150), 76)
    f.line(300, 20, 300, 320, RULE, 1.5, "6 6")
    f.tex(450, 24, r"\text{voimakuvio}", "middle", MUTED)
    cx, cy, w, h = 452, 172, 110, 48
    d = FBD(f, 1.0, body=(cx, cy, w, h), a_dir=(-1, 0))
    d.force("G", (0, -CURL["G"]), (cx, cy), "gravity", lab=(20, -6))
    d.force("N", (0, CURL["G"]), (cx + 24, cy + h / 2), "normal", surface=0, lab=(20, 6))
    d.force("F_mu", (-CURL["Fmu"], 0), (cx - w / 2, cy + h / 2), "friction", surface=0, lab=(-14, 18))
    d.draw()
    return f.svg()


SK = dict(GA=90.0, GB=52.0, F=48.0)   # newtons on the drawing scale s = 1,2   # drawn lengths: the adult is heavier, the two pushes are equal


def luistelijat():
    """Ydinajatus, third law: two skaters push each other apart; the push on each, equal and opposite, on two diagrams."""
    f = Fig("fy43-luistelijat", 460, "Ylhäällä tilannekuva: kaksi luistelijaa seisoo jäällä vastakkain ja työntää toisiaan kämmenillä. "
            "Vasemmalla on suurikokoinen aikuinen A, oikealla pienempi lapsi B. Alhaalla kummankin voimakuvio erikseen, luistelija "
            "suorakulmiona. A:n kuviossa paino G A keskipisteestä alas, jään tukivoima N A alapinnasta ylös ja B:n voima A:han, "
            "F B A, joka osoittaa vasemmalle ja päättyy A:n oikeaan kylkeen. B:n kuviossa paino G B, joka on lyhyempi kuin A:n "
            "paino, tukivoima N B ja A:n voima B:hen, F A B, joka osoittaa oikealle ja päättyy B:n vasempaan kylkeen. Nuolet "
            "F B A ja F A B ovat yhtä pitkät. Kitka jätetään huomiotta.")
    f.rect(16, 172, 568, 26, grad(f, "fy43s-ice", GLASS, COLD_LIGHT), None)
    f.line(16, 172, 584, 172, ICE_EDGE, 2.5, cap="round")
    skater(f, 232, 172, 0.74, 1, COLD, hand=(292, 84))
    skater(f, 352, 172, 0.56, -1, HOT, hand=(306, 84))
    f.tex(176, 40, r"\text{A}", "middle"); f.tex(400, 70, r"\text{B}", "middle")
    f.line(16, 214, 584, 214, RULE, 1.5, "6 6")
    s = 1.2
    ax, ay, aw, ah = 160, 330, 70, 60
    a = FBD(f, s, body=(ax, ay, aw, ah), a_dir=(-1, 0))
    a.force("G_A", (0, -SK["GA"]), (ax, ay), "gravity", tex=r"\overline{G}_A", lab=(-26, -6))
    a.force("N_A", (0, SK["GA"]), (ax + 16, ay + ah / 2), "normal", surface=0, tex=r"\overline{N}_A", lab=(26, 4))
    a.force("F_BA", (-SK["F"], 0), (ax + aw / 2, ay - 14), "applied", push=True, tex=r"\overline{F}_{BA}", lab=(6, -22))
    a.draw()
    bx, by, bw, bh = 455, 345, 56, 40
    b = FBD(f, s, body=(bx, by, bw, bh), a_dir=(1, 0))
    b.force("G_B", (0, -SK["GB"]), (bx, by), "gravity", tex=r"\overline{G}_B", lab=(28, -4))
    b.force("N_B", (0, SK["GB"]), (bx - 12, by + bh / 2), "normal", surface=0, tex=r"\overline{N}_B", lab=(-30, 0))
    b.force("F_AB", (SK["F"], 0), (bx - bw / 2, by - 8), "applied", push=True, tex=r"\overline{F}_{AB}", lab=(-16, -22))
    b.draw()
    f.tex(ax - aw / 2 - 12, ay - ah / 2 + 10, r"\text{A}", "end", MUTED); f.tex(bx + bw / 2 + 12, by - bh / 2 + 10, r"\text{B}", "start", MUTED)
    return f.svg()


def auto():
    """Kaava, first law: a car at constant velocity; on its diagram the road's forward force and the air's drag cancel."""
    f = Fig("fy43-auto", 330, "Kaksi kuvaa autosta, joka ajaa suoralla tiellä tasaisella nopeudella. Vasemmalla tilannekuva: auto ja sen "
            "yllä ohut sininen nuoli v oikealle. Oikealla auton voimakuvio, auto suorakulmiona. Paino G keskipisteestä alas ja tien "
            "tukivoima N alapinnasta ylös, yhtä pitkinä. Tien voima F renkaisiin lähtee alapinnan etukulmasta eteenpäin, ja "
            "ilmanvastus F v lähtee auton takasivulta taaksepäin. Vaakasuorat nuolet ovat yhtä pitkät, joten voimat kumoavat toisensa.")
    f.tex(150, 24, r"\text{tilannekuva}", "middle", MUTED)
    f.rect(16, 236, 270, 34, "#c9c2b2", None)
    f.line(16, 236, 286, 236, INK, 2.5, cap="round")
    for x in range(30, 280, 56): f.rect(x, 251, 30, 5, WHITE)
    # the car: body, cabin, windows, wheels
    f.path("M52,222 Q50,196 74,192 L112,188 Q132,160 162,158 H206 Q228,160 242,186 L262,192 Q276,196 274,222 Z",
           grad(f, "fy43a-car", HOT_LIGHT, HOT), INK, 2.5)
    f.path("M122,186 Q138,166 160,165 H178 V186 Z", GLASS, INK, 2); f.path("M186,165 H204 Q220,168 230,186 H186 Z", GLASS, INK, 2)
    f.rect(258, 198, 14, 8, HEAT_LIGHT, INK, 1.5, 2)
    for x in (98, 228):
        f.circle(x, 222, 15, INK); f.circle(x, 222, 7, ALUMINIUM)
    FBD(f, 1).motion(r"\overline{v}", (1, 0), (124, 128), 76)
    f.line(300, 20, 300, 320, RULE, 1.5, "6 6")
    f.tex(450, 24, r"\text{voimakuvio}", "middle", MUTED)
    cx, cy, w, h = 446, 170, 120, 48
    d = FBD(f, 1.0, body=(cx, cy, w, h), a_dir=(0, 0))
    d.force("G", (0, -96), (cx, cy), "gravity", lab=(20, -6))
    d.force("N", (0, 96), (cx - 22, cy + h / 2), "normal", surface=0, lab=(-22, 6))
    d.force("F", (52, 0), (cx + w / 2, cy + h / 2), "friction", surface=0, lab=(14, 18))
    d.force("F_v", (-52, 0), (cx - w / 2, cy - 6), "drag", v_rel=(1, 0), tex=r"\overline{F}_\text{v}", lab=(-6, -22))
    d.draw()
    return f.svg()


def kone():
    """Esimerkki: an airliner in level flight at constant velocity; on its diagram the two thrusts equal the drag, lift equals weight."""
    f = Fig("fy43-kone", 330, "Kaksi kuvaa matkustajakoneesta, joka lentää vaakasuoraan tasaisella nopeudella. Vasemmalla tilannekuva: kone "
            "ja sen yllä ohut sininen nuoli v oikealle. Oikealla koneen voimakuvio, kone suorakulmiona. Paino G keskipisteestä alas ja "
            "siipien nostovoima F nosto ylös, yhtä pitkinä. Kahden moottorin työntövoimat F 1 ja F 2 lähtevät rungon etureunasta "
            "eteenpäin ja ovat yhtä pitkät. Ilmanvastus F v lähtee takareunasta taaksepäin ja on yhtä pitkä kuin työntövoimat "
            "yhteensä. Vaakasuorat voimat kumoavat toisensa, ja pystysuorat voimat kumoavat toisensa.")
    f.tex(150, 24, r"\text{tilannekuva}", "middle", MUTED)
    f.path("M44,214 Q40,196 62,192 L226,190 Q262,188 276,176 L262,214 Q150,230 44,214 Z", grad(f, "fy43k-body", WHITE, COLD_LIGHT), INK, 2.5)
    f.path("M62,192 L48,150 L74,150 L104,192 Z", COLD, INK, 2)                        # tail fin
    f.path("M138,200 L196,200 L120,250 L100,250 Z", ALUMINIUM, INK, 2)                # wing
    f.circle(160, 238, 9, IRON, INK, 2); f.circle(130, 244, 9, IRON, INK, 2)          # engines
    for x in range(150, 250, 20): f.rect(x, 198, 10, 8, GLASS, INK, 1.5, 2)
    FBD(f, 1).motion(r"\overline{v}", (1, 0), (124, 128), 76)
    f.line(300, 20, 300, 320, RULE, 1.5, "6 6")
    f.tex(450, 24, r"\text{voimakuvio}", "middle", MUTED)
    cx, cy, w, h = 470, 170, 110, 50
    d = FBD(f, 0.8, body=(cx, cy, w, h), a_dir=(0, 0))
    d.force("G", (0, -100), (cx, cy), "gravity", lab=(-22, -6))
    d.force("F_nosto", (0, 100), (cx + 30, cy), "other", tex=r"\overline{F}_\text{nosto}", lab=(34, -2))
    d.force("F_1", (48, 0), (cx + w / 2, cy - 12), "applied", tex=r"\overline{F}_1", lab=(14, -20))
    d.force("F_2", (48, 0), (cx + w / 2, cy + 12), "applied", tex=r"\overline{F}_2", lab=(14, 20))
    d.force("F_v", (-96, 0), (cx - w / 2, cy), "drag", v_rel=(1, 0), tex=r"\overline{F}_\text{v}", lab=(-8, -22))
    d.draw()
    return f.svg()


# ---------------------------------------------------------------- task figures (shown by id from inquiry.json)
def _sensor(k, seed):
    """A sensor reading's small scatter (example data), at most ±0,08 N."""
    return round(0.16 * (rnd(k, seed) - 0.5), 2)


def collision_data():
    """(t, F_A, F_B) every 0,01 s, 0–0,20 s: the force on the light cart A (positive to the right) and on the heavy cart B."""
    rows = []
    for k in range(21):
        t = k / 100
        F = PEAK * math.sin(math.pi * (t - T0) / (T1 - T0)) ** 2 if T0 <= t <= T1 else 0.0
        eA, eB = (_sensor(k, 2), _sensor(k, 7)) if F > 0 else (0.0, 0.0)
        rows.append((t, round(-F + eA, 2), round(F + eB, 2)))
    return rows


def anturit():
    """Interpret: force sensors on two colliding carts; the two readings mirror each other (example data)."""
    f = Fig("fy43-anturit", 400, "Kuvaaja mittakaavassa, keksitty esimerkkiaineisto. Vaaka-akselilla aika nollasta 0,20 sekuntiin, "
            "pystyakselilla anturin lukema newtoneina miinus viidestä viiteen, positiivinen suunta oikealle. Kaksi pistesarjaa "
            "sadasosasekunnin välein. Kevyen kärryn A anturin lukemat, tumma sarja, ovat nolla hetkeen 0,05 sekuntia, laskevat "
            "noin miinus neljään newtoniin hetkellä 0,10 sekuntia ja palaavat nollaan hetkellä 0,15 sekuntia. Raskaan kärryn B "
            "lukemat, punainen sarja, nousevat samoina hetkinä noin plus neljään newtoniin ja palaavat nollaan.")
    x0, x1, yz, ytop, ybot = 96, 480, 204, 64, 344             # plot area: t 0–0,20 s, F −5…5 N
    X = lambda t: x0 + t / 0.20 * (x1 - x0)
    Y = lambda F: yz - F / 5 * (yz - ytop)
    for t in (0.05, 0.10, 0.15, 0.20): f.line(X(t), ytop, X(t), ybot, RULE_LIGHT, 1.5)
    for F in (-4, -2, 2, 4): f.line(x0, Y(F), x1, Y(F), RULE_LIGHT, 1.5)
    f.arrow(x0, ybot + 1, x0, ytop - 26, INK, 2.5, 13)
    f.arrow(x0 - 1, yz, x1 + 26, yz, INK, 2.5, 13)
    for t in (0.05, 0.10, 0.15, 0.20):
        f.line(X(t), yz - 4, X(t), yz + 4, INK, 2); f.line(X(t), ybot, X(t), ybot + 6, INK, 2); f.tex(X(t), ybot + 22, fi(t, 2), "middle")
    for F in (-4, -2, 2, 4):
        f.line(x0 - 7, Y(F), x0, Y(F), INK, 2); f.tex(x0 - 12, Y(F), ("-" if F < 0 else "") + str(abs(F)), "end")
    f.tex(x0 - 12, yz, "0", "end")
    f.line(x0, ybot, x1, ybot, MUTED, 1.5)
    f.tex(x1 + 32, yz, r"t\ (\text{s})", "start")
    f.tex(x0 - 10, ytop - 38, r"F\ (\text{N})", "start")
    rows = collision_data()
    for col, idx in ((INK, 1), (HOT, 2)):
        pts = " ".join(f"{n(X(r[0]))},{n(Y(r[idx]))}" for r in rows)
        f.add(f'<polyline points="{pts}" fill="none" stroke="{col}" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>')
        for r in rows: f.circle(X(r[0]), Y(r[idx]), 5.5, col, WHITE, 2)
    f.tex(X(0.10) + 18, Y(-PEAK) + 4, r"F_A\ (\text{kärry A})", "start", INK)
    f.tex(X(0.10) + 18, Y(PEAK) - 4, r"F_B\ (\text{kärry B})", "start", HOT)
    return f.svg()


def malli_lamppu():
    """Model diagram for the drawing check: a lamp hanging at rest from a cord; its situation picture and force diagram."""
    f = Fig("fy43-malli-lamppu", 340, "Mallikuvio. Vasemmalla tilannekuva: lamppu roikkuu paikallaan katosta pystysuoran johdon varassa. "
            "Oikealla lampun voimakuvio, lamppu suorakulmiona: paino G keskipisteestä alas ja johdon jännitysvoima T yläpinnasta "
            "ylös, yhtä pitkinä. Muita voimia ei ole.")
    f.tex(150, 24, r"\text{tilannekuva}", "middle", MUTED)
    ground(f, 60, 240, 60, below=False)
    f.line(150, 60, 150, 170, INK, 2.5)
    f.rect(140, 166, 20, 16, IRON, INK, 2, 2)
    f.path("M108,232 L192,232 L172,182 L128,182 Z", grad(f, "fy43l-shade", SAND_LIGHT, SAND), INK, 2.5)
    f.add('<ellipse cx="150" cy="240" rx="16" ry="10" fill="#ffc078" stroke="#1f2933" stroke-width="2"/>')
    f.line(300, 20, 300, 320, RULE, 1.5, "6 6")
    f.tex(450, 24, r"\text{voimakuvio}", "middle", MUTED)
    cx, cy, w, h = 450, 182, 84, 52
    d = FBD(f, 1.0, body=(cx, cy, w, h), a_dir=(0, 0))
    d.force("G", (0, -100), (cx, cy), "gravity", lab=(22, -8))
    d.force("T", (0, 100), (cx + 18, cy - h / 2), "tension", rope=(0, 1), lab=(24, 10))
    d.draw()
    return f.svg()


FIGURES = {"hero": hero, "curling": curling, "luistelijat": luistelijat, "auto": auto, "kone": kone,
           "anturit": anturit, "malli-lamppu": malli_lamppu}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "hero": "decorative: the chapter's opening illustration (a curling stone gliding after release)",
    "curling": "reveals: the forces on a sliding curling stone after release (no forward force; theory figure)",
    "luistelijat": "reveals: the third-law pair of two skaters pushing apart, equal and opposite on two diagrams",
    "auto": "reveals: the force diagram of a car at constant velocity, forward force and drag equal",
    "kone": "reveals: the force diagram of an airliner in level flight (thrusts equal drag; the worked example)",
    "anturit": "safe: example force-sensor readings of two colliding carts (the student reads the equal and opposite forces)",
    "malli-lamppu": "reveals: the model diagram of a lamp hanging at rest (shown after the drawing attempt)",
}
