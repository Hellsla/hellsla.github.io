"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy1-5` writes them into lesson.md."""
from figlib import Fig, Axes, INK, MUTED, WHITE, RULE, RULE_LIGHT, COLD, COLD_LIGHT, HEAT, GLASS, IRON, n
from figlib import HEAT_LIGHT
import herolib as H
import math
from figlib import COPPER, METAL_EDGE, SAND, SAND_LIGHT, WATER, WATER_LIGHT
from herolib import grad
from figstyle import Fig, Axes            # the house illustration style (docs/illustration-style.md)
import figstyle as S


def hero():
    """The chapter's opening illustration: Voyager 2 far from the Sun, its earlier positions at equal time steps equally spaced on a straight line."""
    f = S.hero("fy15-hero", "Kuvitus: Aurinko ja planeettojen radat vasemmalla, Voyager 2 -luotain oikealla kaukana avaruudessa. Luotaimen takana "
               "suoralla jäljellä tasavälein merkkejä sen aiemmista paikoista yhtä pitkin aikavälein; seuraavat paikat jatkuvat eteenpäin katkoviivana.")
    H.space(f, seed=5, count=120)
    f.circle(70, 480, 200, H.glow(f, "fy15h-glow"))
    f.circle(70, 480, 70, grad(f, "fy15h-sun", HEAT_LIGHT, HEAT))
    for r in (140, 200, 300, 420):
        f.add(f'<ellipse cx="70" cy="480" rx="{r}" ry="{n(r * 0.32)}" fill="none" stroke="{METAL_EDGE}" stroke-width="1.5" stroke-dasharray="4 7"/>')
    H.planet(f, "fy15h-earth", 70 + 140, 480 - 12, 9, WATER_LIGHT, WATER)
    H.planet(f, "fy15h-jup", 70 + 300 * math.cos(-0.5), 480 + 96 * math.sin(-0.5), 24, SAND_LIGHT, COPPER, bands=4)
    H.planet(f, "fy15h-sat", 70 + 420 * math.cos(-0.25), 480 + 134 * math.sin(-0.25), 18, SAND_LIGHT, SAND, rings=True)
    x0, y0, x1, y1 = 170, 452, 1180, 110
    def at(t): return x0 + (x1 - x0) * t, y0 + (y1 - y0) * t
    f.line(*at(0), *at(0.7), WHITE, 2.5)
    f.line(*at(0.72), *at(1), WHITE, 2.5, dash="10 10")
    for k in range(8):
        x, y = at(0.07 + k * 0.08); f.circle(x, y, 10, COLD_LIGHT, WHITE, 2)
    for k in range(3):
        x, y = at(0.79 + k * 0.08); f.add(f'<circle cx="{n(x)}" cy="{n(y)}" r="10" fill="none" stroke="{WHITE}" stroke-width="2" stroke-dasharray="4 4"/>')
    H.probe(f, *at(0.71), 0.8)
    return f.svg()


def cart(f, cx, cy):
    """A dynamics cart on the ground line y = cy: a tinted body with a darker side, a top rail and two spoked wheels."""
    body = "#4f8fd0"
    f.path(f"M{cx - 30},{cy - 34} h60 l-4,18 h-52 Z", body, S.dark(body, 0.4), S.W_OBJ)
    f.path(f"M{cx - 30},{cy - 34} h60 l-2,6 h-56 Z", S.light(body, 0.45))
    f.rect(cx - 22, cy - 40, 44, 6, "#c4ccd4", S.dark("#c4ccd4", 0.45), 1.25, 2)
    for wx in (cx - 17, cx + 17):
        f.circle(wx, cy - 9, 9, "#3a4350")
        f.circle(wx, cy - 9, 4, "#c4ccd4")
        f.circle(wx, cy - 9, 1.5, "#3a4350")


def motion():
    f = Fig("fy15-motion", 330, "Liikekuva, jossa sama kärry on piirretty viidelle peräkkäiselle hetkelle 0 s, 1 s, 2 s, 3 s ja 4 s. "
            "Kärryjen välit ovat yhtä pitkät, ja jokaisen välin alla on yhtä pitkä sulku Δs: tasaisessa liikkeessä kappale kulkee yhtä pitkissä "
            "ajoissa yhtä pitkät matkat. Välit on piirretty mittakaavassa, kärryt ovat samankokoisia.")
    ground = 150
    f.hatch_ground(24, 576, ground)
    xs = [70 + 115 * i for i in range(5)]
    for i, x in enumerate(xs):
        cart(f, x, ground)
        f.line(x, ground + 12, x, ground + 20, INK, 1.25)
        f.tex(x, ground + 40, r"t = 0\,\text{s}" if i == 0 else rf"{i}\,\text{{s}}", "middle", w=100 if i == 0 else 60)
    f.arrow(xs[0] + 6, 70, xs[0] + 66, 70, COLD, 3, 14)                  # velocity is blue (NOTES.md §3)
    f.tex(xs[0] + 36, 46, "v", "middle", COLD)
    for a, b in zip(xs, xs[1:]):
        f.path(f"M{a},{ground + 62} V{ground + 74} H{b} V{ground + 62}", stroke=MUTED, w=2.5)
        f.tex((a + b) / 2, ground + 100, r"\Delta s", "middle")
    f.tex(300, 316, r"\text{yhtä pitkissä ajoissa yhtä pitkät matkat}", "middle", w=440)
    return f.svg()


def graph():
    f = Fig("fy15-graph", 360, "Kuvaaja mittakaavassa: kaksi tasaista liikettä nopeudella 3 m/s esitetään (t, s)-koordinaatistossa suorina. "
            "Alempi suora kulkee origon kautta (alkupaikka 0), ylempi alkaa paikasta s₀ = 5 m ja on alemman suoran kanssa yhdensuuntainen. "
            "Alemmalle suoralle on piirretty kulmakolmio: 2 s:n aikana paikka kasvaa 6 m, joten kulmakerroin on 3 m/s eli nopeus.")
    ax = Axes(f, (96, 300), (440, 60), x=(0, 5), y=(0, 25), xticks=[1, 2, 3, 4, 5], yticks=[10, 20],
              xlabel=r"t\ (\text{s})", ylabel=r"s\ (\text{m})")
    ax.line([(0, 0), (5, 15)], COLD, 3)
    ax.line([(0, 5), (5, 20)], INK, 3)
    # the starting position of the upper line: a tick and ring on the s axis
    f.line(ax.X(0) - 7, ax.Y(5), ax.X(0), ax.Y(5), INK, 2)
    f.tex(ax.X(0) - 12, ax.Y(5), r"s_0", "end")
    ax.point(0, 5, INK)
    # slope triangle on the lower line between t = 2 s and t = 4 s, right angle below the line
    f.line(ax.X(2), ax.Y(6), ax.X(4), ax.Y(6), MUTED, 1.5, "6 5")
    f.line(ax.X(4), ax.Y(6), ax.X(4), ax.Y(12), MUTED, 1.5, "6 5")
    ax.point(2, 6, COLD); ax.point(4, 12, COLD)
    f.tex(ax.X(3), ax.Y(6) + 24, r"\Delta t = 2\,\text{s}", "middle", w=130)
    f.tex(ax.X(4) + 12, ax.Y(9), r"\Delta s = 6\,\text{m}", "start", w=130, bg=True)
    f.tex(ax.X(5) + 8, ax.Y(15), r"s = vt", "start", COLD, w=80)
    f.tex(ax.X(5) + 8, ax.Y(20), r"s = s_0 + vt", "start", INK, w=140)
    return f.svg()


def line_read():
    """A task-only variant of `graph`: one uniform motion as a straight line through the origin, no slope triangle, no
    values written on it; the student reads two grid crossings (scripts/figcat.py variant)."""
    f = Fig("fy15-line-read", 360, "Kuvaaja mittakaavassa: kävelijän paikka s ajan t funktiona, suora viiva origosta. Ruudukon väli on 1 s ja 5 m. "
            "Suora kulkee ruudukon risteyskohtien (2 s; 5 m), (4 s; 10 m), (6 s; 15 m), (8 s; 20 m) ja (10 s; 25 m) kautta.")
    ax = Axes(f, (96, 300), (470, 60), x=(0, 10), y=(0, 25), xticks=list(range(1, 11)), yticks=[5, 10, 15, 20, 25],
              xlabel=r"t\ (\text{s})", ylabel=r"s\ (\text{m})", xfmt=lambda v: str(int(v)) if v % 2 == 0 else "")
    ax.line([(0, 0), (10, 25)], COLD, 3)
    return f.svg()


# Kuvaajan valinta (task fy1-5-L2-08, docs/exercise-types.md type 2): a walker stands at s = 6 m for 0–4 s, then walks
# back toward the start at 1,0 m/s and reaches it at 10 s. Four option graphs on the same grid; only "pick-back" is right.
PICK_T, PICK_S = (0, 10), (0, 12)


def pick_st(fid, label, pts, ylabel=r"s\ (\text{m})"):
    """One option of the graph choice: a (t, s) graph, t 0–10 s and s 0–12 m, with the walker's broken line."""
    f = Fig(fid, 380, label)
    ax = Axes(f, (96, 320), (470, 70), x=PICK_T, y=PICK_S, xticks=list(range(1, 11)), yticks=[2, 4, 6, 8, 10, 12],
              xlabel=r"t\ (\text{s})", ylabel=ylabel, xfmt=lambda v: str(int(v)) if v % 2 == 0 else "")
    ax.line(pts, COLD, 3)
    return f.svg()


def pick_back():
    return pick_st("fy15-pick-back", "Kuvaaja mittakaavassa: paikka s ajan t funktiona. Ruudukon väli on 1 s ja 2 m. Viiva on vaakasuora "
                   "kohdassa s = 6 m aikavälillä 0–4 s ja laskee sitten suorana kohtaan s = 0 m hetkellä 10 s.",
                   [(0, 6), (4, 6), (10, 0)])


def pick_away():
    return pick_st("fy15-pick-away", "Kuvaaja mittakaavassa: paikka s ajan t funktiona. Ruudukon väli on 1 s ja 2 m. Viiva on vaakasuora "
                   "kohdassa s = 6 m aikavälillä 0–4 s ja nousee sitten suorana kohtaan s = 12 m hetkellä 10 s.",
                   [(0, 6), (4, 6), (10, 12)])


def pick_distance():
    return pick_st("fy15-pick-distance", "Kuvaaja mittakaavassa: kuljettu matka Δs ajan t funktiona. Ruudukon väli on 1 s ja 2 m. Viiva on vaakasuora "
                   "kohdassa Δs = 0 m aikavälillä 0–4 s ja nousee sitten suorana kohtaan Δs = 6 m hetkellä 10 s.",
                   [(0, 0), (4, 0), (10, 6)], ylabel=r"\Delta s\ (\text{m})")


def pick_vt():
    """The v–t confusion: zero while standing, then a constant 1,0 m/s, drawn on (t, v) axes."""
    f = Fig("fy15-pick-vt", 380, "Kuvaaja mittakaavassa: nopeus v ajan t funktiona. Ruudukon väli on 1 s ja 0,25 m/s. Viiva on "
            "t-akselilla, v = 0, aikavälillä 0–4 s ja on sitten vaakasuora kohdassa v = 1,0 m/s aikavälillä 4–10 s.")
    ax = Axes(f, (96, 320), (470, 70), x=PICK_T, y=(0, 1.5), xticks=list(range(1, 11)), yticks=[0.25, 0.5, 0.75, 1.0, 1.25, 1.5],
              xlabel=r"t\ (\text{s})", ylabel=r"v\ (\text{m/s})", xfmt=lambda v: str(int(v)) if v % 2 == 0 else "",
              yfmt=lambda v: {0.5: "0{,}5", 1.0: "1{,}0", 1.5: "1{,}5"}.get(v, ""))
    ax.line([(0, 0), (4, 0)], COLD, 3)
    ax.line([(4, 1.0), (10, 1.0)], COLD, 3)
    return f.svg()


def lightning():
    """Task illustration (fy1-5-L2-04): lightning over a lake seen from a cabin's porch; no numbers."""
    f = S.scene("fy15-thunder", "Kuvitus: salama iskee järven toiselle puolelle tummasta ukkospilvestä. Etualalla mökin kuistilla on lyhty, "
                "ja ranta on tumma.")
    f.defs_add('<linearGradient id="fy15t-sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2a3346"/><stop offset="1" stop-color="#5d6b84"/></linearGradient>')
    f.rect(0, 0, 600, 360, "url(#fy15t-sky)")
    for cx, cy, sc, c in ((120, 60, 2.0, "#3b4458"), (360, 46, 2.4, "#343d50"), (520, 70, 1.8, "#3f495e")): H.cloud(f, cx, cy, sc, c)
    bolt = "M372,92 L352,150 L370,150 L340,214 L362,214 L330,262 L392,190 L370,190 L396,140 L378,140 L398,92 Z"
    f.add(f'<path d="{bolt}" fill="#fff7c2" stroke="#ffe066" stroke-width="2" stroke-linejoin="round"/>')
    f.add('<ellipse cx="364" cy="180" rx="70" ry="90" fill="#fff7c2" opacity="0.12"/>')
    f.path("M0,262 C80,252 200,256 300,262 C420,268 520,256 600,260 V276 H0 Z", "#1f2a33")
    f.rect(0, 276, 600, 84, "#3a4a63")
    f.add('<path d="M300,286 l40,0" stroke="#fff7c2" stroke-width="3" opacity="0.4"/><path d="M330,300 l26,0" stroke="#fff7c2" stroke-width="2" opacity="0.3"/>')
    f.path("M0,300 L120,300 L120,360 L0,360 Z", "#6b4f37")                     # the porch in the foreground
    for x in (10, 40, 70, 100): f.line(x, 300, x, 360, "#4f3a28", 1.5)
    f.rect(0, 250, 130, 8, "#6b4f37"); f.line(122, 250, 122, 300, "#4f3a28", 6)
    f.rect(84, 262, 20, 30, "#ffd8a8", "#4f3a28", 1.5, 3); f.add('<circle cx="94" cy="277" r="16" fill="#ffd8a8" opacity="0.25"/>')
    return f.svg()


def _seg(f, p, q, w1, w2, col):
    """A tapered limb part from p (width w1) to q (width w2) with round ends, outlined in a darker tint."""
    dx, dy = q[0] - p[0], q[1] - p[1]; L = math.hypot(dx, dy) or 1; ux, uy = -dy / L, dx / L
    pts = [(p[0] + ux * w1 / 2, p[1] + uy * w1 / 2), (q[0] + ux * w2 / 2, q[1] + uy * w2 / 2),
           (q[0] - ux * w2 / 2, q[1] - uy * w2 / 2), (p[0] - ux * w1 / 2, p[1] - uy * w1 / 2)]
    ed = S.dark(col, 0.35)
    f.circle(p[0], p[1], w1 / 2, col, ed, 1); f.circle(q[0], q[1], w2 / 2, col, ed, 1)
    f.path("M" + " L".join(f"{n(x)},{n(y)}" for x, y in pts) + " Z", col, ed, 1)
    f.circle(p[0], p[1], w1 / 2 - 0.6, col); f.circle(q[0], q[1], w2 / 2 - 0.6, col)      # hide the seams at the joints


def _shoe(f, ax, ay, col, tilt=0.0):
    """A trainer under the ankle (ax, ay), toe to the right; tilt lifts the heel (radians)."""
    c, s_ = math.cos(tilt), math.sin(tilt)
    def P(u, v): return f"{n(ax + u * c - v * s_)},{n(ay + u * s_ + v * c)}"
    f.path(f"M{P(-8, -4)} L{P(8, -5)} Q{P(20, -3)} {P(22, 5)} L{P(-9, 5)} Z", col, S.dark(col, 0.4), 1)
    f.path(f"M{P(-9, 5)} L{P(22, 5)}", stroke="#f1f3f5", w=3, extra='stroke-linecap="round"')


def _person(f, x, yf, coat, trousers, hair, skin, hurry=False, backpack=None):
    """A student walking to the right in side view, feet on yf, about 160 px tall, drawn from shaped parts: tapered
    legs with knees, trainers, a jacket with a collar and a zip, sleeves with hands, a profile head with an ear, a nose
    and hair. Far limbs a shade darker; the near leg is forward and the near arm back. hurry leans forward and
    lengthens the stride and the swing."""
    st, lean = (1.25, 10) if hurry else (1.0, 3)
    hip = (x, yf - 82); sh = (x + lean + 2, yf - 132); hc = (x + lean + 6, yf - 152)
    far_t, far_c, far_s = S.dark(trousers, 0.22), S.dark(coat, 0.18), S.dark(skin, 0.08)
    shoe = "#364152"
    # far leg (back), heel lifted
    kb, ab = (x - 8 * st, yf - 44), (x - 26 * st, yf - 12)
    _seg(f, hip, kb, 17, 13, far_t); _seg(f, kb, ab, 13, 10, far_t); _shoe(f, ab[0], ab[1] + 2, S.dark(shoe, 0.2), 0.45)
    # far arm (forward)
    e1, w1 = (sh[0] + 12 * st, sh[1] + 24), (sh[0] + 26 * st, sh[1] + 40)
    _seg(f, (sh[0], sh[1] + 4), e1, 11, 9, far_c); _seg(f, e1, w1, 9, 8, far_c); f.circle(w1[0] + 3, w1[1] + 3, 5, far_s, S.dark(skin, 0.35), 1)
    if backpack:
        f.path(f"M{n(sh[0] - 14)},{n(sh[1] + 4)} q-16,0 -18,14 l-2,30 q0,8 8,8 h14 Z", backpack, S.dark(backpack, 0.35), S.W_OBJ)
        f.path(f"M{n(sh[0] - 26)},{n(sh[1] + 30)} h10", stroke=S.dark(backpack, 0.35), w=1.25)
    # near leg (forward)
    kf, af = (x + 14 * st, yf - 44), (x + 18 * st, yf - 8)
    _seg(f, hip, kf, 18, 13, trousers); _seg(f, kf, af, 13, 10, trousers); _shoe(f, af[0], af[1] + 1, shoe, 0.0)
    # jacket: hem at the hips, rounded shoulders, collar, zip and pocket
    cx = x + lean / 2
    jd = S.dark(coat, 0.35)
    f.path(f"M{n(x - 15)},{n(yf - 72)} L{n(x + 16)},{n(yf - 72)} Q{n(x + 19 + lean)},{n(yf - 104)} {n(sh[0] + 13)},{n(sh[1] + 4)} "
           f"Q{n(sh[0] + 10)},{n(sh[1] - 8)} {n(sh[0])},{n(sh[1] - 8)} Q{n(sh[0] - 16)},{n(sh[1] - 8)} {n(sh[0] - 16)},{n(sh[1] + 10)} "
           f"Q{n(x - 18)},{n(yf - 100)} {n(x - 15)},{n(yf - 72)} Z", coat, jd, S.W_OBJ)
    f.path(f"M{n(x - 15)},{n(yf - 78)} H{n(x + 16)}", stroke=jd, w=1)                         # waistband
    f.path(f"M{n(sh[0] + 9)},{n(sh[1] - 4)} L{n(x + 13)},{n(yf - 74)}", stroke=jd, w=1)         # zip
    f.path(f"M{n(x + 2)},{n(yf - 98)} h9", stroke=jd, w=1.25, extra='stroke-linecap="round"')   # pocket
    f.path(f"M{n(sh[0] - 4)},{n(sh[1] - 8)} q8,-6 16,2", stroke=jd, w=1.25)                    # collar
    # neck and head
    f.path(f"M{n(hc[0] - 5)},{n(hc[1] + 10)} L{n(sh[0] - 3)},{n(sh[1] - 6)} L{n(sh[0] + 7)},{n(sh[1] - 6)} L{n(hc[0] + 4)},{n(hc[1] + 10)} Z", skin)
    hx, hy = hc; sd = S.dark(skin, 0.35)
    f.path(f"M{n(hx - 13)},{n(hy)} Q{n(hx - 13)},{n(hy - 15)} {n(hx)},{n(hy - 15)} Q{n(hx + 13)},{n(hy - 15)} {n(hx + 13)},{n(hy - 2)} "
           f"L{n(hx + 17)},{n(hy + 3)} L{n(hx + 13)},{n(hy + 5)} Q{n(hx + 12)},{n(hy + 13)} {n(hx + 3)},{n(hy + 14)} "
           f"Q{n(hx - 13)},{n(hy + 14)} {n(hx - 13)},{n(hy)} Z", skin, sd, 1)                       # profile: forehead, nose, chin
    f.path(f"M{n(hx - 15)},{n(hy + 2)} Q{n(hx - 16)},{n(hy - 19)} {n(hx + 2)},{n(hy - 18)} Q{n(hx + 15)},{n(hy - 17)} {n(hx + 14)},{n(hy - 6)} "
           f"Q{n(hx + 4)},{n(hy - 10)} {n(hx - 3)},{n(hy - 6)} Q{n(hx - 6)},{n(hy + 4)} {n(hx - 10)},{n(hy + 9)} Z", hair, S.dark(hair, 0.3), 1)
    f.add(f'<ellipse cx="{n(hx - 3)}" cy="{n(hy + 1)}" rx="3" ry="4" fill="{S.dark(skin, 0.1)}" stroke="{sd}" stroke-width="1"/>')   # ear
    f.circle(hx + 8, hy - 1, 1.6, "#2b3138")                                                     # eye
    f.path(f"M{n(hx + 6)},{n(hy + 9)} q3,1 5,0", stroke=sd, w=1.25, extra='stroke-linecap="round"')   # mouth
    # near arm (back)
    e2, w2 = (sh[0] - 8 * st, sh[1] + 26), (sh[0] - 20 * st, sh[1] + 42)
    _seg(f, (sh[0] + 1, sh[1] + 3), e2, 12, 10, coat); _seg(f, e2, w2, 10, 8, coat)
    f.circle(w2[0] - 2, w2[1] + 4, 5, skin, sd, 1)


def two_friends():
    """Task illustration (fy1-5-L3-03): two friends set off from the school door along a straight street; no numbers."""
    f = S.scene("fy15-friends", "Kuvitus: kaksi ystävää lähtee koulun ovelta samaa suoraa katua pitkin samaan suuntaan. Edellä kävelee toinen, "
                "ja ovelta lähtee perään toinen, joka pitää kiirettä.")
    H.sky(f, "fy15f", 360)
    H.cloud(f, 330, 52, 0.5, extra='opacity="0.9"'); H.cloud(f, 520, 34, 0.38, extra='opacity="0.85"')
    for tx, ty, r, c in ((272, 196, 40, "#5c9a62"), (318, 214, 30, "#4d8a55"), (470, 190, 44, "#5c9a62"), (520, 212, 32, "#4d8a55")):
        f.rect(tx - 4, ty + r - 8, 8, 286 - ty - r + 8, "#7a5a3a")                            # trees behind the street
        f.circle(tx, ty, r, c, S.dark(c, 0.3), S.W_OBJ)
        f.circle(tx - r * 0.35, ty - r * 0.3, r * 0.45, S.light(c, 0.18))
    f.path("M230,286 V262 Q250,248 268,262 Q290,250 306,264 Q330,252 348,266 Q372,254 392,268 Q420,256 440,268 "
           "Q470,256 496,268 Q526,256 548,268 Q574,256 600,266 V286 Z", "#6aa874", S.dark("#6aa874", 0.3), S.W_OBJ)    # hedge
    wall, roof = "#e5c9a3", "#9a4a3a"
    f.rect(0, 118, 230, 168, wall, S.dark(wall, 0.35), S.W_OBJ)                              # the school
    f.rect(-4, 106, 242, 16, roof, S.dark(roof, 0.3), S.W_OBJ, 2)
    for x in (18, 166):
        f.rect(x, 140, 46, 44, "#cfe3f3", S.dark(wall, 0.4), S.W_DETAIL, 2)
        f.line(x + 23, 140, x + 23, 184, S.dark(wall, 0.4), S.W_DETAIL)
    f.rect(92, 196, 60, 90, "#7a5236", S.dark("#7a5236", 0.35), S.W_OBJ, 2)                  # the door
    f.line(122, 196, 122, 286, S.dark("#7a5236", 0.35), S.W_DETAIL)
    f.circle(114, 244, 2.5, "#e9c46a"); f.circle(130, 244, 2.5, "#e9c46a")
    f.rect(84, 146, 76, 26, WHITE, S.dark(wall, 0.4), S.W_DETAIL, 3)                         # a blank sign over the door
    for x in (330, 560):                                                                      # street lamps
        f.line(x, 286, x, 150, "#5c6670", 4, cap="round")
        f.path(f"M{x},{150} q0,-14 -16,-14", stroke="#5c6670", w=4, extra='stroke-linecap="round"')
        f.path(f"M{x - 26},{140} h20 l-4,8 h-12 Z", "#ffe8a3", S.dark("#5c6670", 0.2), 1)
    for x in (18, 166): f.path(f"M{x - 4},{286} q8,-18 20,-12 q10,-12 22,0 q12,-6 12,12 Z", "#4d8a55", S.dark("#4d8a55", 0.3), 1)   # bushes by the wall
    f.rect(0, 286, 600, 74, "#c3c8ce")                                                        # pavement and kerb
    f.rect(0, 286, 600, 3, S.dark("#c3c8ce", 0.15))
    for x in range(40, 600, 80): f.line(x, 289, x - 12, 360, S.dark("#c3c8ce", 0.08), S.W_DETAIL)
    f.rect(0, 340, 600, 20, "#8d959e")
    _person(f, 430, 318, "#2b8a3e", "#3f4c5a", "#7a4b2a", "#f1d3b3", backpack="#c92a2a")
    _person(f, 200, 318, "#e8590c", "#364a63", "#2b3138", "#c99a72", hurry=True, backpack="#1971c2")
    return f.svg()


FIGURES = {"hero": hero, "lightning": lightning, "two-friends": two_friends, "motion": motion, "graph": graph, "line-read": line_read,
           "pick-back": pick_back, "pick-away": pick_away, "pick-distance": pick_distance, "pick-vt": pick_vt}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "lightning": "safe: the situation only, lightning seen across a lake; no numbers",
    "two-friends": "safe: the situation only, two friends leaving the school door; no numbers",
    "motion": "safe: equal spacing at equal times, no distances",
    "graph": "reveals: the slope 3 m/s of both lines and s0 = 5 m",
    "line-read": "safe: one straight line through the origin, grid crossings to read, no slope marked (graph is the lesson figure)",
    "pick-back": "reveals: the right option of task fy1-5-L2-08 (stands at 6 m, then back to the start)",
    "pick-away": "safe: a wrong option of task fy1-5-L2-08 (stands at 6 m, then away from the start)",
    "pick-distance": "safe: a wrong option of task fy1-5-L2-08 (the distance walked, Δs, instead of the position)",
    "pick-vt": "safe: a wrong option of task fy1-5-L2-08 (a (t, v) graph: 0, then 1,0 m/s)",
}
