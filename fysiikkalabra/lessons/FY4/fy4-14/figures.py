"""Figures of fy4-14 (scripts/figlib.py, scripts/fbd.py, scripts/herolib.py); `python scripts/figures.py fy4-14` writes them into
lesson.md. Every force diagram is an FBD: the object alone as a plain rectangle, its arrows drawn to scale and its physics
checked as it is drawn (the air resistance against the velocity relative to the air: kind="drag", v_rel); the situation is a
separate pictorial situation picture (tilannekuva) above a dashed divider; no point-particle diagrams. The air resistance
starts at the face the air presses on: the lower face of a falling body, the upper face of a rising one, the top (the canopy)
once a parachute opens. Velocity is blue, acceleration orange and forces red in every figure (FBD.motion, FBD.force)."""
import math
from figlib import (Fig, Axes, INK, MUTED, WHITE, RULE, RULE_LIGHT, SAND_LIGHT, SAND, SAND_DARK, GRAIN, COPPER, ICE, GLASS,
                    COLD, COLD_LIGHT, HOT, HEAT, HEAT_LIGHT, GOOD, GOOD_LIGHT, IRON, ALUMINIUM, METAL_EDGE, WATER, WATER_LIGHT, n)
from fbd import FBD
import herolib as H
from herolib import grad, rnd

g = 9.81
SUIT, RIG, SKIN = GOOD, IRON, SAND_LIGHT
FAR = 'stroke-linecap="round" stroke-opacity="0.6"'      # the far arm and leg: the suit colour, paler
CANOPY, CANOPY2 = SAND_DARK, SAND


# ---------------------------------------------------------------- drawing helpers
def skydiver(f, x, y, sc=1.0, pose="belly"):
    """A skydiver in a green suit with the rig on the back, centred at (x, y). pose: belly (side view, falling belly down with
    the arms and legs bent up), head (head down), hang (upright, as under a canopy; the canopy is drawn by canopy())."""
    f.add(f'<g transform="translate({n(x)},{n(y)}) scale({sc:g})">')
    if pose == "belly":
        f.path("M-22,-2 Q-34,-16 -40,-34", stroke=SUIT, w=9, extra=FAR)          # far leg, bent up
        f.path("M18,-4 Q26,-18 22,-34", stroke=SUIT, w=8, extra=FAR)             # far arm
        f.rect(-28, -10, 54, 20, SUIT, INK, 2.5, 9)
        f.path("M-24,2 Q-42,-6 -50,-26", stroke=SUIT, w=10, extra='stroke-linecap="round"')                 # near leg
        f.path("M-50,-26 l-6,-6", stroke=INK, w=8, extra='stroke-linecap="round"')
        f.path("M14,2 Q30,-6 34,-26", stroke=SUIT, w=9, extra='stroke-linecap="round"')                    # near arm
        f.circle(34, -28, 5, SKIN, INK, 1.5)
        f.rect(-16, -18, 30, 10, RIG, INK, 2, 3)
        f.circle(36, 2, 10, SKIN, INK, 2)
        f.path("M27,-3 A10,10 0 0 1 46,0 Z", INK)                                                            # helmet
    elif pose == "head":
        f.rect(-10, -30, 20, 44, SUIT, INK, 2.5, 8)
        f.path("M-5,-28 L-8,-58", stroke=SUIT, w=9, extra='stroke-linecap="round"'); f.path("M5,-28 L8,-58", stroke=SUIT, w=9, extra=FAR)
        f.rect(9, -24, 8, 22, RIG, INK, 2, 2)
        f.circle(0, 24, 10, SKIN, INK, 2); f.path("M-10,24 A10,10 0 0 0 10,24 Z", INK)
    else:
        f.path("M-5,12 L-7,40", stroke=SUIT, w=9, extra='stroke-linecap="round"'); f.path("M5,12 L7,40", stroke=SUIT, w=9, extra=FAR)
        f.rect(-11, -18, 22, 34, SUIT, INK, 2.5, 7)
        f.rect(-8, -16, 16, 14, RIG, INK, 2, 2)
        f.path("M-11,-12 L-18,-34", stroke=SUIT, w=7, extra='stroke-linecap="round"'); f.path("M11,-12 L18,-34", stroke=SUIT, w=7, extra='stroke-linecap="round"')
        f.circle(0, -28, 10, SKIN, INK, 2); f.path("M-10,-28 A10,10 0 0 1 10,-28 Z", INK)
    f.add("</g>")


def canopy(f, x, y, sc=1.0, w=150, gid="c"):
    """A ram-air canopy over a hanging skydiver at (x, y): the lines from the shoulders to the canopy's lower edge."""
    hw, top, bot = w / 2 * sc, y - 120 * sc, y - 88 * sc
    for k in (-0.5, -0.2, 0.2, 0.5):
        f.line(x + k * 20 * sc, y - 30 * sc, x + k * w * 0.9 * sc, bot, MUTED, 1.5)
    f.path(f"M{n(x - hw)},{n(bot)} Q{n(x - hw)},{n(top)} {n(x)},{n(top)} Q{n(x + hw)},{n(top)} {n(x + hw)},{n(bot)} Z",
           grad(f, gid, CANOPY, CANOPY2), INK, 2.5)
    for k in range(1, 6):
        xx = x - hw + k * 2 * hw / 6
        f.line(xx, bot, xx, bot - (bot - top) * 0.8 * math.sin(math.pi * k / 6), GRAIN, 1.5)


def ball(f, x, y, r, gid):
    f.circle(x, y, r, grad(f, gid, WHITE, ALUMINIUM), INK, 2.5)
    f.path(f"M{n(x - r)},{n(y)} Q{n(x)},{n(y - r * 0.5)} {n(x + r)},{n(y)}", stroke=METAL_EDGE, w=1.5)
    f.path(f"M{n(x - r * 0.3)},{n(y - r * 0.95)} Q{n(x + r * 0.2)},{n(y)} {n(x - r * 0.3)},{n(y + r * 0.95)}", stroke=METAL_EDGE, w=1.5)


def vline(f, x, y1, y2, col=COLD, sym=r"\overline{v}", lab_dx=18):
    """A thin velocity or acceleration arrow with an open head beside a body in the situation picture (not a force)."""
    from fbd import open_head
    d = 1 if y2 > y1 else -1
    f.line(x, y1, x, y2 - d * 2, col, 2.5); open_head(f, x, y2, 0, d, col, 2.5)
    f.tex(x + lab_dx, (y1 + y2) / 2, sym, "start", col)


# ---------------------------------------------------------------- opening illustration
def hero():
    """The chapter's opening illustration: high above fields and a lake, one skydiver falls belly down at speed while another
    floats slowly under an open canopy; the plane they jumped from flies away."""
    f = H.hero("fy414-hero", "Kuvitus: korkealla peltojen, metsien ja järven yläpuolella kaksi laskuvarjohyppääjää. Vasemmalla ylempänä "
               "hyppääjä putoaa vatsa alaspäin kädet ja jalat levällään, ja hänen yläpuolellaan näkyvät ilmavirran viivat. Oikealla "
               "alempana toinen hyppääjä leijuu hitaasti avatun laskuvarjon alla. Taivaan yläreunassa lentokone, josta he hyppäsivät.")
    H.sky(f, "fy414h", 600, ICE, GLASS)
    # the ground far below: fields, a lake, forest
    f.path("M0,430 Q300,404 600,418 T1200,410 V600 H0 Z", GOOD_LIGHT)
    for k in range(9):
        x0 = k * 140 - 20 + 30 * rnd(k, 3)
        f.path(f"M{n(x0)},{n(440 + 10 * rnd(k, 4))} l120,-6 l20,40 l-130,8 Z", [SAND_LIGHT, GOOD_LIGHT, SAND_DARK][k % 3], GRAIN, 1.5)
    f.path("M760,470 Q840,446 940,462 Q1010,480 960,512 Q860,540 780,512 Q730,492 760,470 Z", grad(f, "fy414h-lake", WATER_LIGHT, WATER), INK, 2)
    H.forest(f, 500, 40, 22, GOOD, seed=4, x0=0, x1=700, depth=26)
    H.forest(f, 560, 30, 20, GOOD, seed=9, x0=600, x1=1200, depth=20)
    f.add(f'<rect x="0" y="380" width="1200" height="90" fill="{GLASS}" fill-opacity="0.55"/>')               # haze over the far ground
    H.cloud(f, 220, 330, 1.1); H.cloud(f, 1000, 300, 0.9); H.cloud(f, 640, 220, 0.6, extra='fill-opacity="0.8"')
    # the plane, small and far away
    f.add('<g transform="translate(1010,70) scale(0.9)">')
    f.path("M-80,0 Q-60,-14 40,-12 Q70,-10 84,0 Q70,10 40,10 L-70,8 Z", ALUMINIUM, INK, 2.5)
    f.path("M-10,-6 L-34,-44 L-16,-44 L16,-6 Z", METAL_EDGE, INK, 2); f.path("M-70,-4 L-86,-30 L-74,-30 L-56,-4 Z", METAL_EDGE, INK, 2)
    for k in range(4): f.rect(-40 + k * 20, -8, 10, 7, GLASS, INK, 1.5, 2)
    f.rect(30, -8, 14, 16, INK, rx=2)
    f.add("</g>")
    # the free-falling jumper: big, belly down, with air streaming past
    for k in range(5):
        x = 330 + k * 26
        f.line(x, 92 + 12 * rnd(k, 2), x, 150 + 20 * rnd(k, 5), WHITE, 4, cap="round")
    skydiver(f, 400, 220, 2.6, "belly")
    # the jumper under the canopy: lower and to the right
    canopy(f, 820, 330, 1.25, 150, "fy414h-canopy")
    skydiver(f, 820, 330, 1.25, "hang")
    return f.svg()


# ---------------------------------------------------------------- theory figures
def _phase(f, ox, title, Fv_k, a_k, vlen, m=80.0):
    """One column of the falling figure: the jumper (situation) above the divider, the force diagram below."""
    G = m * g
    f.tex(ox + 100, 22, title, "middle", MUTED)
    skydiver(f, ox + 70, 104, 0.95, "belly")
    if vlen: vline(f, ox + 150, 70, 70 + vlen)
    else: f.tex(ox + 132, 70, r"v = 0", "start", MUTED)
    cx, cy, w, h = ox + 92, 252, 64, 38
    d = FBD(f, 0.1, body=(cx, cy, w, h), m=m, a=(0, -a_k * g))
    d.force("G", (0, -G), (cx, cy), "gravity", lab=(22, -2))
    if Fv_k: d.force("F_v", (0, Fv_k * G), (cx - 16, cy + h / 2), "drag", v_rel=(0, -1), tex=r"\overline{F}_\text{v}", lab=(-30, 0), push=True)
    d.draw()
    if a_k: d.motion(r"\overline{a}", (0, -1), (ox + 168, 236), 22 + 40 * a_k)
    else: f.tex(ox + 168, 260, r"a = 0", "middle", MUTED)
    f.tex(ox + 100, 400, [r"F_\text{v} = 0", r"F_\text{v} < G", r"F_\text{v} = G"][0 if not Fv_k else 1 if Fv_k < 1 else 2], "middle")


def pudotus():
    """Ydinajatus: a skydiver just after the jump, speeding up and at the terminal speed (example situation G); the weight is the
    same in every column, the air resistance grows with the speed until it equals the weight."""
    f = Fig("fy414-pudotus", 430, "Kolme vaihetta laskuvarjohyppääjän pudotuksesta vatsa alaspäin, mittakaavassa. Ylhäällä tilannekuvat ja "
            "alhaalla voimakuviot, joissa hyppääjä on suorakulmio. Vasemmalla heti hypyn jälkeen: hyppääjä lähtee ilman suhteen levosta, nopeus on nolla, voimakuviossa on "
            "vain paino G keskipisteestä alas, ja oranssi kiihtyvyysnuoli osoittaa alas. Keskellä hyppääjä kiihtyy: sininen nopeusnuoli "
            "alas, paino G alas ja ilmanvastus F_v alhaalta ylös alapintaan asti, puolet painon pituudesta, ja kiihtyvyysnuoli on lyhyempi. "
            "Oikealla rajanopeus: pitkä nopeusnuoli alas, ilmanvastus yhtä pitkä kuin paino, ja kiihtyvyys on nolla.")
    f.line(14, 168, 586, 168, RULE, 1.5, "6 6")
    f.line(200, 36, 200, 380, RULE_LIGHT, 1.5, "4 6"); f.line(400, 36, 400, 380, RULE_LIGHT, 1.5, "4 6")
    _phase(f, 0, r"\text{alussa}", 0, 1.0, 0)
    _phase(f, 200, r"\text{kiihtyy}", 0.5, 0.5, 46)
    _phase(f, 400, r"\text{rajanopeus}", 1.0, 0, 80)
    return f.svg()


def vt():
    """Ydinajatus: the speed of a 60 kg and a 100 kg skydiver (belly down) against time, model values of the simulation (F_v = k v²,
    k = 0,26 kg/m, so v = v_T tanh(g t / v_T)); the free fall without air resistance dashed for comparison."""
    f = Fig("fy414-vt", 360, "Kuvaaja mittakaavassa, simulaation mallin arvoja: vaaka-akselilla aika 0–30 sekuntia, pystyakselilla nopeus "
            "0–70 metriä sekunnissa. Katkoviivana suora, joka nousee jyrkästi: nopeus ilman ilmanvastusta, 49 metriä sekunnissa viiden "
            "sekunnin kohdalla. Kaksi käyrää alkaa samalla jyrkkyydellä mutta loivenee ja tasaantuu vaakasuoraksi: 60 kilogramman "
            "hyppääjän nopeus noin 48 metriin sekunnissa ja 100 kilogramman hyppääjän noin 61 metriin sekunnissa.")
    ax = Axes(f, (90, 304), (430, 66), x=(0, 30), y=(0, 70), xticks=[5, 10, 15, 20, 25, 30], yticks=[10, 20, 30, 40, 50, 60, 70],
              xlabel=r"t\ (\text{s})", ylabel=r"v\ (\text{m/s})")
    ax.line([(0, 0), (70 / g, 70)], MUTED, 2.5, "8 6")
    f.tex(ax.X(70 / g) + 10, ax.Y(68), r"\text{ilman ilmanvastusta}", "start", MUTED)
    for m, col in ((100, INK), (60, COPPER)):
        vT = math.sqrt(m * g / 0.26)
        ax.curve(lambda t: vT * math.tanh(g * t / vT), 0, 30, col)
        f.tex(ax.X(30) + 12, ax.Y(vT), rf"m = {m}\,\text{{kg}}", "start", col)
    return f.svg()


def _rise(f, ox, title, rising):
    """A ball thrown straight up, with air resistance: rising (left) or falling back (right); situation above, diagram below."""
    m, Fv = 0.50, 2.0
    G = m * g; ay = -(G + Fv) / m if rising else -(G - Fv) / m
    f.tex(ox + 150, 22, title, "middle", MUTED)
    ball(f, ox + 120, 100, 22, f"fy414-ball{ox}")
    vline(f, ox + 170, 120 if rising else 70, 70 if rising else 120)
    cx, cy, w, h = ox + 120, 252, 64, 40
    d = FBD(f, 16.0, body=(cx, cy, w, h), m=m, a=(0, ay))
    d.force("G", (0, -G), (cx, cy), "gravity", lab=(22, -2))
    if rising: d.force("F_v", (0, -Fv), (cx - 18, cy - h / 2), "drag", v_rel=(0, 1), tex=r"\overline{F}_\text{v}", lab=(-30, 0), push=True)
    else: d.force("F_v", (0, Fv), (cx - 18, cy + h / 2), "drag", v_rel=(0, -1), tex=r"\overline{F}_\text{v}", lab=(-30, 0), push=True)
    d.draw()
    d.motion(r"\overline{a}", (0, -1), (ox + 200, 196), 26 + 2.4 * abs(ay), lab=(20, -14))
    d.net((ox + 262, 270), lab=(0, 24))


def ylos():
    """Kaava: a ball thrown up with air resistance, rising and falling back: the air resistance points against the velocity, so
    while rising it adds to the weight and while falling it subtracts from it; the net force (hollow green) is drawn apart."""
    f = Fig("fy414-ylos", 430, "Kaksi tilannetta, mittakaavassa: suoraan ylös heitetty pallo, kun ilmanvastusta ei jätetä huomiotta. Ylhäällä "
            "tilannekuvat ja alhaalla voimakuviot, joissa pallo on suorakulmio. Vasemmalla pallo nousee: sininen nopeusnuoli ylös. "
            "Voimakuviossa paino G keskipisteestä alas ja ilmanvastus F_v yläpinnasta alas. Erillään vihreä ontto kokonaisvoiman nuoli "
            "alas, painoa pidempi, ja oranssi kiihtyvyysnuoli alas. Oikealla pallo putoaa takaisin: nopeusnuoli alas. Voimakuviossa "
            "paino alas ja ilmanvastus alapinnasta ylös. Kokonaisvoiman nuoli alas on painoa lyhyempi, ja kiihtyvyysnuoli on lyhyempi kuin vasemmalla.")
    f.line(14, 160, 586, 160, RULE, 1.5, "6 6"); f.line(300, 36, 300, 420, RULE_LIGHT, 1.5, "4 6")
    _rise(f, 0, r"\text{nousee}", True)
    _rise(f, 300, r"\text{putoaa}", False)
    return f.svg()


def _chute(f, ox, title, Fv_k, vlen, stage):
    """One column of the canopy figure: stage 0 free fall at the terminal speed, 1 the canopy opening, 2 the new terminal speed."""
    m = 80.0; G = m * g; ay = (Fv_k * G - G) / m
    f.tex(ox + 100, 22, title, "middle", MUTED)
    if stage == 0: skydiver(f, ox + 82, 120, 0.95, "belly")
    else:
        canopy(f, ox + 82, 160, 0.8, 60 if stage == 1 else 116, f"fy414-ch{stage}")
        skydiver(f, ox + 82, 160, 0.8, "hang")
    vline(f, ox + 150, 70, 70 + vlen)
    cx, cy, w, h = ox + 86, 350, 60, 38
    d = FBD(f, 0.05, body=(cx, cy, w, h), m=m, a=(0, ay))
    d.force("G", (0, -G), (cx, cy), "gravity", lab=(22, -2))
    if stage == 0: d.force("F_v", (0, Fv_k * G), (cx - 16, cy + h / 2), "drag", v_rel=(0, -1), tex=r"\overline{F}_\text{v}", lab=(-30, 0), push=True)
    else: d.force("F_v", (0, Fv_k * G), (cx - 16, cy - h / 2), "drag", v_rel=(0, -1), tex=r"\overline{F}_\text{v}", lab=(-30, 12))
    d.draw()
    if stage == 1:
        d.motion(r"\overline{a}", (0, 1), (ox + 146, 300), 56, lab=(20, 4))
        d.net((ox + 178, 444), lab=(0, -20))
    else: f.tex(ox + 160, 350, r"a = 0", "middle", MUTED)


def varjo():
    """Kaava: the canopy opens (example situation G): at the terminal speed F_v = G; while the canopy opens F_v is several times G,
    the net force and the acceleration point up although the jumper still moves down; under the canopy a new, small terminal speed."""
    f = Fig("fy414-varjo", 470, "Kolme vaihetta, kun laskuvarjo avataan, voimat mittakaavassa. Ylhäällä tilannekuvat ja alhaalla hyppääjän "
            "voimakuviot, joissa hyppääjä varjoineen on suorakulmio. Vasemmalla putoaminen ennen varjon avaamista rajanopeudella: pitkä sininen nopeusnuoli "
            "alas, paino G keskipisteestä alas ja ilmanvastus F_v alhaalta ylös alapintaan asti, yhtä pitkinä, kiihtyvyys nolla. Keskellä varjo "
            "aukeaa: nopeusnuoli osoittaa yhä alas, ilmanvastus lähtee yläpinnasta ylös ja on kolme kertaa painon pituinen. Erillään "
            "vihreä ontto kokonaisvoiman nuoli ylös ja oranssi kiihtyvyysnuoli ylös. Oikealla varjo on auki: lyhyt nopeusnuoli alas, "
            "ilmanvastus yläpinnasta ylös yhtä pitkänä kuin paino, kiihtyvyys nolla.")
    f.line(14, 200, 586, 200, RULE, 1.5, "6 6")
    f.line(200, 36, 200, 450, RULE_LIGHT, 1.5, "4 6"); f.line(400, 36, 400, 450, RULE_LIGHT, 1.5, "4 6")
    _chute(f, 0, r"\text{rajanopeus}", 1.0, 92, 0)
    _chute(f, 200, r"\text{varjo aukeaa}", 3.0, 70, 1)
    _chute(f, 400, r"\text{uusi rajanopeus}", 1.0, 16, 2)
    return f.svg()


EX = dict(m=85.0, Fv=2400.0)      # the worked example's data (lesson-answers.py computes the same)


def esimerkki():
    """The worked example's force diagram: the canopy opening, F_v = 2,40 kN against G = 834 N, with the positive direction down."""
    m, Fv = EX["m"], EX["Fv"]
    G = m * g; ay = (Fv - G) / m
    f = Fig("fy414-esimerkki", 380, "Vasemmalla tilannekuva: hyppääjän laskuvarjo on aukeamassa, ja hyppääjän vieressä sininen nopeusnuoli "
            "osoittaa alas. Oikealla hyppääjän voimakuvio, hyppääjä varjoineen suorakulmiona: paino G keskipisteestä alas ja "
            "ilmanvastus F_v yläpinnasta ylös, lähes kolme kertaa painon pituisena. Erillään oranssi kiihtyvyysnuoli ylös. Oikealla "
            "pieni nuoli y alas: positiivinen suunta on alas.")
    canopy(f, 110, 220, 0.95, 90, "fy414-ex-c")
    skydiver(f, 110, 220, 0.95, "hang")
    vline(f, 180, 200, 280)
    f.tex(100, 356, r"\text{tilannekuva}", "middle", MUTED); f.tex(400, 356, r"\text{voimakuvio}", "middle", MUTED)
    f.line(232, 20, 232, 340, RULE_LIGHT, 1.5, "4 5")
    cx, cy, w, h = 360, 230, 90, 44
    d = FBD(f, 0.06, body=(cx, cy, w, h), m=m, a=(0, ay))
    d.force("F_v", (0, Fv), (cx - 18, cy - h / 2), "drag", v_rel=(0, -1), tex=r"\overline{F}_\text{v}", lab=(-34, 12))
    d.force("G", (0, -G), (cx, cy), "gravity", lab=(24, -4))
    d.draw()
    d.motion(r"\overline{a}", (0, 1), (470, 250), 70)
    f.arrow(560, 200, 560, 266, MUTED, 2, 10); f.tex(560, 284, r"y", "middle", MUTED)
    return f.svg()


# ---------------------------------------------------------------- task figures (shown by id from inquiry.json and exercises.json)
RISE = ("Vasemmalla tilannekuva: lentopallo nousee suoraan ylös, ja sen vieressä sininen nopeusnuoli osoittaa ylös. Oikealla "
        "pallon voimakuvio, pallo suorakulmiona: paino G keskipisteestä alas")


def _select(name, desc, wrong=None, mode="right"):
    """An option of the selection task: a volleyball rising straight up after a hit, with air resistance."""
    m = 0.27; G = m * g; Fv = 1.2
    f = Fig(f"fy414-valitse-{name}", 300, desc, width=300)
    ball(f, 62, 150, 26, f"fy414-vb-{name}")
    vline(f, 112, 176, 112)
    f.line(144, 20, 144, 280, RULE, 1.5, "6 6")
    cx, cy, w, h = 214, 160, 56, 40
    d = FBD(f, 26.0, body=(cx, cy, w, h), a_dir=None if wrong else (0, -1), wrong=wrong)
    d.force("G", (0, -G), (cx, cy), "gravity", lab=(24, -2))
    if mode in ("right", "extra"): d.force("F_v", (0, -Fv), (cx - 16, cy - h / 2), "drag", v_rel=(0, 1), tex=r"\overline{F}_\text{v}", lab=(-28, 0), push=True)
    if mode == "up": d.force("F_v", (0, Fv), (cx - 16, cy + h / 2), "drag", v_rel=(0, 1), tex=r"\overline{F}_\text{v}", lab=(-28, 0), push=True)
    if mode == "extra":
        d.force("F", (0, 2.6), (cx + 16, cy - h / 2), "other", lab=(18, 6))
    d.draw()
    return f.svg()


def valitse_a(): return _select("a", RISE + " ja ilmanvastus F_v yläpinnasta alas.")
def valitse_b(): return _select("b", RISE + " ja ilmanvastus F_v alapinnasta ylös.", wrong="the air resistance points up, against the weight, not against the velocity", mode="up")
def valitse_c(): return _select("c", RISE + ", ilmanvastus F_v yläpinnasta alas ja lisäksi voima F yläpinnasta ylös.", wrong="an invented force F along the motion: the hand no longer touches the ball", mode="extra")
def valitse_d(): return _select("d", RISE + ". Muita nuolia ei ole.", wrong="the air resistance is missing although it is not neglected", mode="missing")


def malli_alas():
    """Model diagram for the drawing task: a ball thrown straight down faster than its terminal speed slows down: F_v > G."""
    m, Fv = 0.40, 6.0
    G = m * g; ay = (Fv - G) / m
    f = Fig("fy414-malli-alas", 330, "Mallikuvio: pallo on heitetty suoraan alas nopeammin kuin sen rajanopeus, ja se hidastuu. Kuviossa on "
            "vain pallo suorakulmiona. Keskipisteestä paino G alas ja alapinnasta ilmanvastus F_v ylös, selvästi painoa pidempänä. "
            "Erillään sininen nopeusnuoli alas ja oranssi kiihtyvyysnuoli ylös.")
    cx, cy, w, h = 290, 170, 100, 46
    d = FBD(f, 18.0, body=(cx, cy, w, h), m=m, a=(0, ay))
    d.force("G", (0, -G), (cx, cy), "gravity", lab=(24, -4))
    d.force("F_v", (0, Fv), (cx - 20, cy + h / 2), "drag", v_rel=(0, -1), tex=r"\overline{F}_\text{v}", lab=(-34, 0), push=True)
    d.draw()
    d.motion(r"\overline{v}", (0, -1), (420, 120), 80)
    d.motion(r"\overline{a}", (0, 1), (480, 200), 60)
    return f.svg()


# The tangent of the exercise graph: through (0 s; 2,0 m/s) and (2,0 s; 15,0 m/s), slope 6,5 m/s². The curve v = v_T tanh(g t / v_T)
# touches it where g (1 − (v/v_T)²) = 6,5, i.e. v = v_T q with q = √(1 − 6,5/g); the tangent passes (0; 2,0) when
# v_T (q − 6,5 atanh(q) / g) = 2,0.
_Q = math.sqrt(1 - 6.5 / g)
_VT = 2.0 / (_Q - 6.5 * math.atanh(_Q) / g)
_T1 = _VT / g * math.atanh(_Q)


def ex_tangentti():
    """Exercise level 3: the (t, v) graph of a falling ball with air resistance and the tangent at a point P (the task reads the
    tangent's slope off the grid)."""
    f = Fig("fy414-ex-tangentti", 380, "Kuvaaja mittakaavassa: vaaka-akselilla aika 0–3,0 sekuntia puolen sekunnin välein, pystyakselilla nopeus "
            "0–16 metriä sekunnissa metrin välein. Putoavan pallon nopeus kasvaa nollasta ensin jyrkästi ja sitten yhä loivemmin, "
            "noin 14 metriin sekunnissa. Käyrän pisteeseen P, hetkeen noin 1,0 sekuntia ja nopeuteen noin 8 metriä sekunnissa, on "
            "piirretty tangentti. Tangentti kulkee pisteiden (0 s; 2,0 m/s) ja (2,0 s; 15,0 m/s) kautta.")
    ax = Axes(f, (80, 334), (450, 64), x=(0, 3), y=(0, 16), xticks=[0.5, 1, 1.5, 2, 2.5, 3], yticks=list(range(1, 17)),
              xlabel=r"t\ (\text{s})", ylabel=r"v\ (\text{m/s})", yfmt=lambda v: str(v) if v % 2 == 0 else "")
    ax.curve(lambda t: _VT * math.tanh(g * t / _VT), 0, 3, COLD)
    ax.line([(0, 2.0), (2.0, 15.0)], HEAT, 2.5)
    ax.point(_T1, _VT * _Q, INK)
    f.tex(ax.X(_T1) - 14, ax.Y(_VT * _Q) - 18, r"P", "end")
    f.tex(ax.X(2.0) + 10, ax.Y(15.4), r"\text{tangentti}", "start", HEAT)
    return f.svg()


FIGURES = {"hero": hero, "pudotus": pudotus, "vt": vt, "ylos": ylos, "varjo": varjo, "esimerkki": esimerkki,
           "valitse-a": valitse_a, "valitse-b": valitse_b, "valitse-c": valitse_c, "valitse-d": valitse_d,
           "malli-alas": malli_alas, "ex-tangentti": ex_tangentti}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "pudotus": "reveals: the force diagrams of a skydiver just after the jump, speeding up and at the terminal speed",
    "vt": "reveals: the (t, v) curves of a 60 kg and a 100 kg skydiver levelling off at 48 and 61 m/s (model values)",
    "ylos": "reveals: the force diagrams of a ball thrown up with air resistance, rising and falling back, with the net force",
    "varjo": "reveals: the force diagrams of a skydiver at terminal speed, while the canopy opens and under the open canopy",
    "esimerkki": "reveals: the force diagram of the worked example (the canopy opening, F_v about 3 G, a up)",
    "valitse-a": "reveals: the right diagram for a ball rising with air resistance (an option figure)",
    "valitse-b": "safe: a wrong option (air resistance up) for diagram selection",
    "valitse-c": "safe: a wrong option (an invented upward force) for diagram selection",
    "valitse-d": "safe: a wrong option (air resistance missing) for diagram selection",
    "malli-alas": "reveals: the model diagram of a ball thrown down faster than its terminal speed (shown after the attempt)",
    "ex-tangentti": "safe: a (t, v) curve with a tangent on a grid; the slope is not given",
}
