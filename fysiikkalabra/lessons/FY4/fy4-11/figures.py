"""Figures of fy4-11 (scripts/figlib.py, scripts/fbd.py, scripts/herolib.py); `python scripts/figures.py fy4-11` writes them into
lesson.md. The stopping model: constant speed during the reaction time, then a constant deceleration (Liikenneturva's
assumptions t_r = 1,0 s and a = 9,0 m/s² on a dry road; lesson-answers.py computes the same numbers). The collision
figures use rounded example values (a 75 kg occupant, 50 km/h, Δt 0,10 s with the belt, 0,010 s without), labelled as
such. Velocity is blue, acceleration orange and forces red (FBD.motion, FBD.force); the reaction distance is green and
the braking distance copper in every figure and in the simulation."""
import math
from figlib import (Fig, Axes, INK, MUTED, WHITE, RULE, RULE_LIGHT, SAND_LIGHT, SAND, SAND_DARK, GRAIN, COPPER, ICE, GLASS,
                    COLD, COLD_LIGHT, HOT, HOT_LIGHT, HEAT, HEAT_LIGHT, GOOD, GOOD_LIGHT, IRON, ALUMINIUM, METAL_EDGE, n, fi)
from fbd import FBD
import herolib as H
from herolib import grad, rnd

g = 9.81
REACT, BRAKE = GOOD, COPPER                 # reaction distance green, braking distance copper (also in the simulation)
MOOSE = "#8a5f22"
ASPHALT = IRON


def stop(v_kmh, tr=1.0, dec=9.0):
    v = v_kmh / 3.6
    return v * tr, v * v / (2 * dec)


# ---------------------------------------------------------------- drawing helpers
def car(f, x, yg, sc, gid, body=(WHITE, ALUMINIUM), lights=None):
    """A car in side view facing right: rear bumper at x, wheels on the ground line yg, 226 units long at sc = 1.
    lights: "head" (headlight beam forward) or "brake" (lit brake light)."""
    f.add(f'<g transform="translate({n(x)},{n(yg)}) scale({sc:g})">')
    if lights == "head":
        f.path("M218,-36 L520,-70 L520,8 Z", HEAT_LIGHT, extra='fill-opacity="0.45"')
    f.path("M2,-15 Q0,-41 24,-45 L62,-49 Q82,-77 112,-79 H156 Q178,-77 192,-51 L212,-45 Q226,-41 224,-15 Z",
           grad(f, gid, *body), INK, 2.5)
    f.path("M72,-51 Q88,-71 110,-72 H128 V-51 Z", GLASS, INK, 2)
    f.path("M136,-72 H154 Q170,-69 180,-51 H136 Z", GLASS, INK, 2)
    f.rect(208, -39, 14, 8, HEAT_LIGHT, INK, 1.5, 2)
    f.rect(2, -40, 9, 9, HOT if lights == "brake" else HOT_LIGHT, INK, 1.5, 2)
    if lights == "brake":
        f.circle(6, -36, 14, HOT_LIGHT, None); f.rect(2, -40, 9, 9, HOT, INK, 1.5, 2)
    for wx in (48, 178):
        f.circle(wx, -15, 15, INK); f.circle(wx, -15, 7, ALUMINIUM)
    f.add("</g>")


def moose(f, x, yg, sc=1.0):
    """A moose walking to the left in side view, hooves on yg."""
    f.add(f'<g transform="translate({n(x)},{n(yg)}) scale({sc:g})">')
    for lx, ph in ((-40, -8), (-22, 10), (40, 6), (58, -10)):              # legs, the far ones paler
        f.path(f"M{lx},-110 L{lx + ph},-4", stroke=MOOSE, w=11, extra='stroke-linecap="round"' + (' stroke-opacity="0.7"' if lx in (-22, 58) else ""))
        f.path(f"M{lx + ph - 6},-2 h12", stroke=INK, w=6, extra='stroke-linecap="round"')
    f.path("M-62,-150 Q-60,-190 -20,-196 Q30,-206 66,-190 Q86,-180 82,-140 Q78,-104 40,-102 L-40,-102 Q-66,-108 -62,-150 Z", MOOSE, INK, 2.5)
    f.path("M-50,-180 Q-74,-196 -86,-176 L-112,-150 Q-122,-136 -108,-130 L-92,-128 Q-80,-140 -66,-150 Z", MOOSE, INK, 2.5)  # neck and head
    f.path("M-84,-136 q-6,14 4,24", stroke=INK, w=2)                    # the bell under the throat
    f.circle(-90, -164, 3, INK)
    f.path("M-74,-188 Q-70,-214 -48,-220 M-66,-206 l-10,-14 M-58,-214 l-2,-16 M-50,-218 l8,-12", stroke=SAND, w=6, extra='stroke-linecap="round"')
    f.add("</g>")


def moose_sign(f, x, yg, sc=1.0):
    """The Finnish moose warning sign on its post: a red-bordered triangle with a moose silhouette."""
    f.rect(x - 4 * sc, yg - 150 * sc, 8 * sc, 150 * sc, METAL_EDGE, INK, 1.5)
    top = yg - 250 * sc
    f.path(f"M{n(x)},{n(top)} L{n(x + 60 * sc)},{n(top + 100 * sc)} L{n(x - 60 * sc)},{n(top + 100 * sc)} Z", HOT, INK, 2, extra='stroke-linejoin="round"')
    f.path(f"M{n(x)},{n(top + 22 * sc)} L{n(x + 42 * sc)},{n(top + 90 * sc)} L{n(x - 42 * sc)},{n(top + 90 * sc)} Z", SAND_LIGHT)
    moose(f, x + 6 * sc, top + 86 * sc, 0.19 * sc)


def road(f, x0, x1, y, h, dashes=True):
    f.rect(x0, y, x1 - x0, h, ASPHALT)
    f.line(x0, y, x1, y, INK, 2); f.line(x0, y + h, x1, y + h, INK, 2)
    if dashes:
        for x in range(int(x0) + 10, int(x1) - 30, 60): f.rect(x, y + h / 2 - 2.5, 30, 5, WHITE)


# ---------------------------------------------------------------- opening illustration
def hero():
    """The chapter's opening illustration: an autumn evening on a country road through a spruce forest; a car with its
    headlights on approaches a moose stepping onto the road past a moose warning sign."""
    f = H.hero("fy411-hero", "Kuvitus: syysilta maantiellä kuusimetsän keskellä. Vasemmalta tulee henkilöauto ajovalot päällä. Tien "
               "oikealla puolella on hirvivaroitusmerkki, ja sen takana hirvi astuu metsän reunasta tielle auton edessä. Auton ja "
               "hirven välinen matka on lyhyt verrattuna siihen, mitä auto tarvitsee pysähtyäkseen.")
    H.sky(f, "fy411h", 420, COLD_LIGHT, HEAT_LIGHT)
    H.sun(f, "fy411h-sun", 980, 330, 44, rays=False)
    H.hills(f, "fy411h-hill", 330, [GOOD_LIGHT, GOOD], amp=30, seed=3)
    H.forest(f, 400, 70, 26, GOOD, seed=5, x0=0, x1=1200, depth=30)
    f.rect(0, 400, 1200, 200, grad(f, "fy411h-field", GOOD_LIGHT, SAND_DARK))
    road(f, 0, 1200, 448, 88)
    f.rect(0, 536, 1200, 64, grad(f, "fy411h-verge", SAND_DARK, SAND))
    for k in range(14):                                                    # grass tufts on the verge
        x = 30 + k * 86 + 20 * rnd(k, 2)
        f.path(f"M{n(x)},560 l-8,-18 M{n(x)},560 l2,-22 M{n(x)},560 l10,-16", stroke=GOOD, w=3, extra='stroke-linecap="round"')
    for x, h in ((70, 160), (1120, 190), (1040, 150)):
        H.spruce(f, x, 420, h)
    moose_sign(f, 640, 448, 0.9)
    car(f, 210, 512, 1.25, "fy411h-car", (WHITE, ALUMINIUM), lights="head")
    moose(f, 870, 500, 1.15)
    return f.svg()


# ---------------------------------------------------------------- theory figures
SC = 6.5                                    # px per metre in "pysahtyminen"
X0 = 60                                     # where the driver notices the danger


def _row(f, y, v_kmh, gid):
    sr, sj = stop(v_kmh)
    xr, xs = X0 + sr * SC, X0 + (sr + sj) * SC
    f.tex(16, y, rf"v_0 = {v_kmh}\,\text{{km/h}}:\ s_\text{{p}} = {fi(sr + sj, 1)}\,\text{{m}}", "start")
    road(f, 16, 584, y + 64, 24, dashes=False)
    car(f, xs - 0.32 * 226, y + 64, 0.32, gid, lights="brake")
    f.line(X0, y + 22, X0, y + 120, INK, 1.5, "5 4")
    f.rect(X0, y + 98, xr - X0, 12, REACT, INK, 1.5)
    f.rect(xr, y + 98, xs - xr, 12, BRAKE, INK, 1.5)
    f.tex((X0 + xr) / 2, y + 128, r"s_\text{r}", "middle", REACT)
    f.tex((xr + xs) / 2, y + 128, r"s_\text{j}", "middle", BRAKE)


def pysahtyminen():
    """Ydinajatus: the stopping distance at 50 and 100 km/h to scale (t_r = 1,0 s, a = 9,0 m/s²): the reaction distance
    doubles, the braking distance quadruples."""
    f = Fig("fy411-pysahtyminen", 400, "Kaksi tietä päällekkäin, matkat mittakaavassa, autot eivät. Kummassakin kuljettaja huomaa "
            "vaaran katkoviivan kohdalla. Ylhäällä nopeus on 50 kilometriä tunnissa: vihreä reaktiomatka 13,9 metriä ja ruskea "
            "jarrutusmatka 10,7 metriä, yhteensä 24,6 metriä. Alhaalla nopeus on 100 kilometriä tunnissa: reaktiomatka on kaksi "
            "kertaa pidempi, 27,8 metriä, ja jarrutusmatka neljä kertaa pidempi, 42,9 metriä, yhteensä 70,6 metriä. Reaktioaika "
            "on 1,0 sekuntia ja hidastuvuus 9,0 metriä sekunnin neliölle. Alla mittanauha metreinä.")
    _row(f, 26, 50, "fy411-p50")
    _row(f, 196, 100, "fy411-p100")
    y = 364
    f.line(X0, y, X0 + 75 * SC, y, INK, 2)
    for m in range(0, 80, 10):
        f.line(X0 + m * SC, y, X0 + m * SC, y - 8, INK, 2)
        f.tex(X0 + m * SC, y + 18, fi(m), "middle", MUTED)
    f.tex(X0 + 75 * SC + 8, y + 18, r"\text{m}", "start", MUTED)
    return f.svg()


def jarrutus():
    """Ydinajatus: a braking car on a level road; its force diagram: G, N and the road's friction backwards; a backwards."""
    m, dec = 1200.0, 9.0
    G = m * g
    f = Fig("fy411-jarrutus", 330, "Vasemmalla tilannekuva: auto jarruttaa vaakasuoralla tiellä, jarruvalot palavat. Auton yllä "
            "sininen nopeusnuoli osoittaa eteenpäin oikealle ja oranssi kiihtyvyysnuoli taaksepäin vasemmalle. Oikealla auton "
            "voimakuvio, auto suorakulmiona: paino G keskipisteestä alas, tien tukivoima N alapinnasta ylös yhtä pitkänä ja tien "
            "kitkavoima F mu alapinnan takakulmasta taaksepäin, lähes painon pituisena. Kitka on ainoa vaakasuora voima.")
    f.tex(150, 24, r"\text{tilannekuva}", "middle", MUTED)
    f.rect(16, 236, 270, 34, RULE, None)
    f.line(16, 236, 286, 236, INK, 2.5, cap="round")
    car(f, 40, 236, 1.05, "fy411-j-car", lights="brake")
    d0 = FBD(f, 1)
    d0.motion(r"\overline{v}", (1, 0), (120, 110), 80)
    d0.motion(r"\overline{a}", (-1, 0), (200, 66), 64)
    f.line(300, 20, 300, 316, RULE, 1.5, "6 6")
    f.tex(450, 24, r"\text{voimakuvio}", "middle", MUTED)
    cx, cy, w, h = 470, 170, 120, 52
    d = FBD(f, 0.007, body=(cx, cy, w, h), m=m, a=(-dec, 0))
    d.force("G", (0, -G), (cx, cy), "gravity", lab=(22, -8))
    d.force("N", (0, G), (cx + 28, cy + h / 2), "normal", surface=0, lab=(22, 8))
    d.force("F_mu", (-m * dec, 0), (cx - w / 2, cy + h / 2), "friction", surface=0, tex=r"\overline{F}_{\mu}", lab=(0, 22))
    d.draw()
    return f.svg()


def tormays():
    """Ydinajatus: the speed of the occupant in a 50 km/h frontal crash (example values): belted, the occupant slows down
    with the car over 0,10 s; unbelted, the occupant keeps the speed until the head or chest hits the car's interior and
    stops in about 0,010 s. The change of speed is the same."""
    v = 50 / 3.6
    f = Fig("fy411-tormays", 340, "Kaavakuva, pyöristetyt esimerkkiarvot: matkustajan nopeus 50 kilometrin tuntinopeudesta tapahtuvassa "
            "nokkakolarissa. Vaaka-akselilla aika 0–0,12 sekuntia, pystyakselilla nopeus 0–16 metriä sekunnissa. Sininen viiva: "
            "vyöhön kiinnitetty matkustaja hidastuu tasaisesti auton mukana 13,9 metristä sekunnissa nollaan 0,10 sekunnissa. "
            "Ruskea viiva: ilman vyötä matkustaja jatkaa nopeudella 13,9 metriä sekunnissa 0,090 sekuntiin asti, osuu auton "
            "sisustaan ja pysähtyy 0,010 sekunnissa. Nopeuden muutos on molemmissa sama.")
    ax = Axes(f, (80, 290), (470, 60), x=(0, 0.12), y=(0, 16), xticks=[0.02, 0.04, 0.06, 0.08, 0.10, 0.12],
              yticks=[4, 8, 12, 16], xlabel=r"t\ (\text{s})", ylabel=r"v\ (\text{m/s})")
    ax.line([(0, v), (0.10, 0)], COLD, 3.5)
    ax.line([(0, v), (0.09, v), (0.10, 0)], COPPER, 3.5)
    f.tex(ax.X(0.005), ax.Y(15.3), r"\text{ilman vyötä: }\Delta t = 0{,}010\,\text{s}", "start", COPPER, bg=True)
    f.tex(ax.X(0.012), ax.Y(2.4), r"\text{vyössä: }\Delta t = 0{,}10\,\text{s}", "start", COLD, bg=True)
    return f.svg()


def tv():
    """Kaava: the (t, v) graph of stopping, schematic: the rectangle v0 t_r is the reaction distance and the triangle
    ½ v0 t_j the braking distance."""
    f = Fig("fy411-tv", 340, "Kaavakuva (t, v)-kuvaajasta, ei lukuarvoja. Nopeus pysyy reaktioajan t_r arvossa v_0, joten kuvaaja on "
            "vaakasuora, ja sen alle jää vihreä suorakulmio, jonka pinta-ala on reaktiomatka s_r = v_0 t_r. Sitten nopeus pienenee "
            "suoraviivaisesti nollaan jarrutusajassa t_j, ja kuvaajan alle jää ruskea kolmio, jonka pinta-ala on jarrutusmatka "
            "s_j = puolet v_0 t_j:stä. Suoran kulmakertoimen suuruus on hidastuvuus a.")
    tr, tj, v0 = 1.0, 2.2, 1.0
    ax = Axes(f, (80, 290), (500, 70), x=(0, 3.6), y=(0, 1.3), xticks=[tr, tr + tj], yticks=[v0],
              xlabel=r"t", ylabel=r"v", xfmt=lambda t: r"t_\text{r}" if t == tr else r"t_\text{r} + t_\text{j}", yfmt=lambda v: r"v_0")
    ax.area([(0, 0), (0, v0), (tr, v0), (tr, 0)], REACT, 0.35)
    ax.area([(tr, 0), (tr, v0), (tr + tj, 0)], BRAKE, 0.35)
    ax.line([(0, v0), (tr, v0), (tr + tj, 0)], COLD, 3.5)
    f.tex(ax.X(tr / 2), ax.Y(0.45), r"s_\text{r}", "middle", INK)
    f.tex(ax.X(tr + tj / 3), ax.Y(0.3), r"s_\text{j}", "middle", INK)
    f.tex(ax.X(tr + tj * 0.55) + 10, ax.Y(0.62), r"\text{kulmakerroin } {-a}", "start", COLD)
    return f.svg()


def tF():
    """Kaava: mean force against time in the same crash (example values): the areas F_k Δt are equal, because the change
    of momentum m Δv is the same; the belt makes Δt ten times longer and the mean force a tenth."""
    m, v = 75.0, 50 / 3.6
    Fb, Fn = m * v / 0.10 / 1000, m * v / 0.010 / 1000                  # kN: 10,4 and 104
    f = Fig("fy411-tF", 360, "Kuvaaja mittakaavassa, pyöristetyt esimerkkiarvot 75 kilogramman matkustajalle 50 kilometrin "
            "tuntinopeudesta. Vaaka-akselilla aika 0–0,12 sekuntia, pystyakselilla keskimääräinen voima 0–120 kilonewtonia. "
            "Matala sininen suorakulmio: vyössä voima on noin 10 kilonewtonia 0,10 sekunnin ajan. Kapea ja korkea ruskea "
            "suorakulmio: ilman vyötä voima on noin 100 kilonewtonia 0,010 sekunnin ajan. Suorakulmioiden pinta-alat ovat yhtä suuret.")
    ax = Axes(f, (80, 310), (470, 70), x=(0, 0.12), y=(0, 120), xticks=[0.02, 0.04, 0.06, 0.08, 0.10, 0.12],
              yticks=[20, 40, 60, 80, 100, 120], xlabel=r"t\ (\text{s})", ylabel=r"F_\text{k}\ (\text{kN})")
    ax.area([(0, 0), (0, Fb), (0.10, Fb), (0.10, 0)], COLD, 0.45)
    ax.line([(0, Fb), (0.10, Fb), (0.10, 0)], COLD, 3)
    ax.area([(0.09, 0), (0.09, Fn), (0.10, Fn), (0.10, 0)], COPPER, 0.6)
    ax.line([(0.09, 0), (0.09, Fn), (0.10, Fn), (0.10, 0)], COPPER, 3)
    f.tex(ax.X(0.005), ax.Y(Fb) - 18, r"\text{vyössä: } F_\text{k} \approx 10\,\text{kN}", "start", COLD, bg=True)
    f.tex(ax.X(0.088), ax.Y(96), r"\text{ilman vyötä: } F_\text{k} \approx 100\,\text{kN}", "end", COPPER, bg=True)
    return f.svg()


FIGURES = {"hero": hero, "pysahtyminen": pysahtyminen, "jarrutus": jarrutus, "tormays": tormays, "tv": tv, "tF": tF}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "pysahtyminen": "reveals: the stopping distances at 50 and 100 km/h (t_r 1,0 s, a 9,0 m/s²): s_r doubles, s_j quadruples",
    "jarrutus": "reveals: the force diagram of a car braking on a level road (friction backwards, a backwards)",
    "tormays": "reveals: the occupant's (t, v) in a 50 km/h crash with and without a belt (same Δv, Δt 0,10 s and 0,010 s)",
    "tv": "reveals: the area derivation of s_r = v0 t_r and s_j = ½ v0 t_j",
    "tF": "reveals: the mean forces 10 kN and 100 kN with equal areas F_k Δt (example values)",
}
