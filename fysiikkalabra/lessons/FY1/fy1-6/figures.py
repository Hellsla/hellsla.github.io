"""Figures of this lesson (scripts/figlib.py, house style scripts/figstyle.py); `python scripts/figures.py fy1-6` writes them into lesson.md."""
import math
from figlib import INK, MUTED, WHITE, COLD, IRON, SAND, fi, n
from figstyle import Fig, Axes            # the house illustration style (docs/illustration-style.md)
import figstyle as S
from figstyle import W_OBJ, W_DETAIL, W_GUIDE, W_DATA, GRID, GUIDE_DASH, SOFT_INK, dark, light, mix

G = 9.81
STEEL = "#aab4bf"
SUIT, SUIT_SH = "#eef0f2", "#c9d0d8"
GOLD, GOLD_D = "#d9a441", "#8a5a12"
REG, REG_FAR, REG_D = "#b7bec6", "#9aa3ad", "#8b949e"
SKY1, SKY2 = "#0f1626", "#1f2a40"


def _rnd(k, seed=3): return (math.sin(k * 12.9898 + seed * 78.233) * 43758.5453) % 1


def hero():
    """The chapter's opening illustration: on the airless Moon a hammer and a feather fall side by side, level at every moment."""
    f = S.hero("fy16-hero", "Kuvitus: astronautti Kuun harmaalla pinnalla mustaa taivasta vasten, taustalla kuumoduuli ja taivaalla Maa. "
               "Astronautti on pudottanut vasaran ja höyhenen samaan aikaan; haaleat välikuvat näyttävät, että ne ovat joka hetki samalla "
               "korkeudella ja että peräkkäisten välikuvien välit kasvavat putoamisen aikana.")
    f.defs_add(f'<linearGradient id="fy16-sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{SKY1}"/><stop offset="1" stop-color="{SKY2}"/></linearGradient>')
    f.rect(0, 0, 1200, 600, "url(#fy16-sky)")
    for k in range(110):
        f.add(f'<circle cx="{n(_rnd(k) * 1200)}" cy="{n(_rnd(k + 500) * 420)}" r="{0.6 + 1.5 * _rnd(k + 900) ** 3:.2f}" fill="#ffffff" opacity="{0.35 + 0.6 * _rnd(k + 70):.2f}"/>')
    ex, ey, er = 1035, 112, 50                                   # Earth: oceans, land, cloud band, night side
    f.defs_add(f'<clipPath id="fy16-earth"><circle cx="{ex}" cy="{ey}" r="{er}"/></clipPath>')
    f.circle(ex, ey, er, "#3d7cc9")
    f.add(f'<g clip-path="url(#fy16-earth)"><path d="M{ex-30},{ey-40} q22,8 18,30 q-4,18 14,26 q8,16 -6,30 l-30,0 q-10,-30 -2,-50 q-12,-14 6,-36 Z" fill="#7fae63"/>'
          f'<path d="M{ex+14},{ey-46} q26,4 30,24 q-14,6 -26,-2 q-10,-8 -4,-22 Z" fill="#7fae63"/>'
          f'<path d="M{ex-60},{ey-20} q40,-8 90,4" stroke="#ffffff" stroke-width="7" fill="none" opacity="0.7" stroke-linecap="round"/>'
          f'<circle cx="{ex+38}" cy="{ey+30}" r="{er*1.25:.0f}" fill="{SKY1}" opacity="0.55"/></g>')
    f.path("M0,420 C180,392 330,410 470,398 C640,384 820,404 1000,392 C1100,386 1160,394 1200,398 V600 H0 Z", REG_FAR)
    f.path("M0,452 C220,428 520,438 760,430 C940,424 1080,438 1200,446 V600 H0 Z", REG)
    for k in range(260):                                         # regolith grain
        f.add(f'<circle cx="{n(_rnd(k, 7) * 1200)}" cy="{n(450 + _rnd(k + 300, 7) ** 0.7 * 150)}" r="{0.8 + 1.6 * _rnd(k + 600, 7):.1f}" fill="{REG_D}" opacity="0.45"/>')
    for cx, cy, rx in ((150, 530, 78), (930, 548, 62), (1110, 490, 40), (560, 572, 34)):   # craters: shadowed far rim, lit near rim
        ry = rx * 0.26
        f.add(f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{n(ry)}" fill="{REG_D}"/>')
        f.add(f'<path d="M{cx-rx},{cy} A{rx},{n(ry)} 0 0 0 {cx+rx},{cy} A{rx},{n(ry*0.55)} 0 0 1 {cx-rx},{cy} Z" fill="{mix(REG, "#ffffff", 0.35)}"/>')
    lx, ly = 880, 404                                            # lunar module, distant
    for dx in (-46, 46):
        f.add(f'<line x1="{n(lx + dx * 0.55)}" y1="{ly - 30}" x2="{lx + dx}" y2="{ly + 6}" stroke="#7b8591" stroke-width="3"/>')
        f.add(f'<ellipse cx="{lx+dx}" cy="{ly+7}" rx="9" ry="3" fill="#7b8591"/>')
    f.rect(lx - 34, ly - 52, 68, 28, GOLD, GOLD_D, 1.5, 2); f.rect(lx + 6, ly - 52, 28, 28, dark(GOLD, 0.12))
    f.path(f"M{lx-28},{ly-52} L{lx-20},{ly-82} H{lx+22} L{lx+30},{ly-52} Z", "#cfd5db", "#6f7a86", 1.5)
    f.rect(lx - 8, ly - 76, 14, 12, "#3b4350", None, 0, 2)
    f.add(f'<ellipse cx="{lx}" cy="{ly+10}" rx="70" ry="6" fill="{REG_D}" opacity="0.6"/>')
    for k, x in enumerate(range(150, 360, 38)):                  # footprints
        f.add(f'<ellipse cx="{x}" cy="{478 + (k % 2) * 12 - k * 2}" rx="11" ry="4" fill="{REG_D}" opacity="0.8"/>')
    x, yf, o, w = 450, 486, SOFT_INK, 2.5                        # astronaut, right arm out
    f.add(f'<ellipse cx="{x+14}" cy="{yf+4}" rx="74" ry="9" fill="#6f7882" opacity="0.6"/>')
    f.rect(x - 86, yf - 296, 50, 124, "#d7dce2", o, w, 10); f.rect(x - 86, yf - 296, 14, 124, "#bcc3cb", None, 0, 6)
    for dx, sh in ((-38, True), (2, False)):
        f.path(f"M{x+dx},{yf-150} h34 l2,118 h-38 Z", SUIT, o, w)
        if sh: f.path(f"M{x+dx+22},{yf-150} h12 l2,118 h-14 Z", SUIT_SH)
        f.path(f"M{x+dx-4},{yf-32} h42 q8,0 8,10 v18 h-54 v-20 q0,-8 4,-8 Z", "#9aa4af", o, w)
        f.add(f'<line x1="{x+dx+2}" y1="{yf-92}" x2="{x+dx+34}" y2="{yf-92}" stroke="{SUIT_SH}" stroke-width="3"/>')
    f.path(f"M{x-54},{yf-306} q54,-18 108,0 l4,160 q-58,14 -116,0 Z", SUIT, o, w)
    f.path(f"M{x+24},{yf-312} q22,4 34,6 l4,160 q-18,5 -36,6 Z", SUIT_SH)
    f.rect(x - 26, yf - 262, 50, 32, "#dfe4ea", o, 1.75, 4)
    for k, c in enumerate(("#c92a2a", "#2b8a3e", "#1971c2")): f.circle(x - 14 + 13 * k, yf - 246, 4, c)
    f.rect(x - 56, yf - 160, 112, 16, "#cfd5db", o, 1.75, 6)
    for d_, sw, c in ((f"M{x-48},{yf-292} q-26,40 -18,104", 30, o), (f"M{x-48},{yf-292} q-26,40 -18,104", 25, SUIT)):
        f.path(d_, stroke=c, w=sw, extra='stroke-linecap="round"')
    hx, hy = x + 158, yf - 286
    for sw, c in ((30, o), (25, SUIT)): f.path(f"M{x+40},{yf-282} L{hx-8},{hy}", stroke=c, w=sw, extra='stroke-linecap="round"')
    f.path(f"M{x+60},{yf-276} L{hx-10},{hy+6}", stroke=SUIT_SH, w=7, extra='stroke-linecap="round"')
    f.rect(x - 70, yf - 292, 18, 26, "#c92a2a", o, 1.5, 3)
    f.circle(hx + 6, hy, 14, "#9aa4af", o, w)
    f.circle(x + 4, yf - 344, 52, SUIT, o, w)
    f.path(f"M{x+30},{yf-388} a52,52 0 0 1 0,88 a60,60 0 0 0 0,-88 Z", SUIT_SH)
    f.rect(x - 28, yf - 374, 80, 52, GOLD, GOLD_D, 2, 22)
    f.path(f"M{x-16},{yf-362} q16,-8 34,-2", stroke="#fff6dc", w=5, extra='stroke-linecap="round" opacity="0.85"')

    def hammer(cx, cy, op):
        return (f'<g transform="translate({n(cx)},{n(cy)})" opacity="{op}">'
                f'<rect x="-4.5" y="-38" width="9" height="62" rx="3" fill="#b88a4a" stroke="{dark("#b88a4a", 0.4)}" stroke-width="1.75"/>'
                f'<rect x="-21" y="-50" width="42" height="17" rx="2.5" fill="#7b8591" stroke="{o}" stroke-width="1.75"/>'
                f'<rect x="-21" y="-50" width="42" height="5" rx="2" fill="#aab4bf"/></g>')

    def feather(cx, cy, op):
        vanes = "".join(f'<path d="M0,{y} q{s*9},-4 {s*15},-12" stroke="#c9d0d8" stroke-width="1.2" fill="none"/>' for y in (-26, -16, -6, 4, 14) for s in (-1, 1))
        return (f'<g transform="translate({n(cx)},{n(cy)}) rotate(-10)" opacity="{op}">'
                f'<path d="M0,30 C-22,6 -20,-30 0,-46 C18,-28 20,8 0,30 Z" fill="#ffffff" stroke="{o}" stroke-width="1.75"/>'
                f'{vanes}<path d="M0,42 L0,-44" stroke="{o}" stroke-width="1.75" stroke-linecap="round"/></g>')
    for t, op in ((1, 0.4), (2, 0.6), (3, 1)):                  # 20 t² below the release level: the gaps grow 1 : 3 : 5
        y = hy + 50 + 20 * t * t
        f.add(hammer(hx - 2, y, op)); f.add(feather(hx + 74, y, op))
    f.line(hx - 34, hy + 260, hx + 108, hy + 260, WHITE, 1.5, dash="6 5")
    return f.svg()


def free_fall():
    f = Fig("fy16-fall", 560, "Kaavakuva mittakaavassa: pallo putoaa levosta mittatangon vierellä, ja sen paikat on piirretty hetkillä 0, 1, 2 ja 3 sekuntia. "
            "Pudotusmatkat ovat 0; 4,9; 19,6 ja 44,1 metriä, ja peräkkäiset välit 4,9; 14,7 ja 24,5 metriä kasvavat. Pallon alla oleva nuoli näyttää "
            "nopeuden, ja sen pituus on verrannollinen nopeuteen: 0; 9,81; 19,6 ja 29,4 metriä sekunnissa eli nopeus kasvaa joka sekunti yhtä paljon.")
    top, ppm, rx, bx, k = 56, 8.6, 96, 236, 1.9                  # 0 m level, px per metre of fall, rod x, ball x, px per m/s
    f.rect(rx - 9, top - 4, 18, ppm * 50 + 8, light(SAND, 0.35), dark(SAND, 0.35), W_OBJ, 2)    # measuring rod 0…50 m
    for m in range(0, 51, 5):
        y = top + m * ppm
        f.line(rx + 9 - (12 if m % 10 == 0 else 7), y, rx + 9, y, INK, W_DETAIL)
        if m % 10 == 0: f.tex(rx - 16, y, fi(m), "end", MUTED)
    f.tex(rx - 16, top - 30, r"s\ (\text{m})", "end")
    f.rect(bx - 22, top - 38, 44, 10, IRON, dark(IRON), W_OBJ, 2)                                    # the release clamp
    f.line(bx, top - 28, bx, top - 12, dark(IRON), 3)
    prev = None
    for t in range(4):
        y = top + ppm * 0.5 * G * t * t; v = G * t; r = 12
        f.line(rx + 12, y, bx - r - 4, y, MUTED, W_GUIDE, GUIDE_DASH)
        f.ball(f"fy16-fb{t}", bx, y, r, STEEL)
        f.tex(bx - r - 8, y - 15, rf"t = {t}\,\text{{s}}", "end")
        if t:
            f.vec(bx, y + r + 2, bx, y + r + 2 + v * k, COLD)
            f.tex(bx + 16, y + r + 2 + v * k * 0.55, rf"v = {fi(v, 2 if t == 1 else 1)}\,\text{{m/s}}", "start", COLD)
            f.dim_v(480, prev, y, rf"{fi(0.5 * G * (2 * t - 1), 1)}\,\text{{m}}")
            f.line(bx + r + 4, y, 474, y, GRID, W_DETAIL)
        else:
            f.tex(bx + 22, y, r"v = 0", "start", COLD)
            f.line(bx + r + 70, y, 474, y, GRID, W_DETAIL)
        prev = y
    return f.svg()


def vt_graph():
    f = Fig("fy16-graph", 360, "(t,v)-kuvaaja mittakaavassa: vapaasti putoavan kappaleen nopeus on suora, joka alkaa origosta. Pisteet ovat "
            "9,81 m/s hetkellä 1,0 s, 19,6 m/s hetkellä 2,0 s, 29,4 m/s hetkellä 3,0 s ja 39,2 m/s hetkellä 4,0 s. Hetkien 1,0 s ja 3,0 s "
            "välillä aika kasvaa 2,0 s ja nopeus 19,6 m/s, joten suoran kulmakerroin on 9,81 m/s², putoamiskiihtyvyys g.")
    ax = Axes(f, (92, 304), (500, 70), x=(0, 4.4), y=(0, 44), xticks=[1, 2, 3, 4], yticks=[10, 20, 30, 40],
              xlabel=r"t\ (\text{s})", ylabel=r"v\ (\text{m/s})")
    X, Y = ax.X, ax.Y
    a, b = (1, G), (3, 3 * G)                                    # slope triangle: tinted, legs in the line's colour
    f.path(f"M{n(X(a[0]))},{n(Y(a[1]))} L{n(X(b[0]))},{n(Y(a[1]))} L{n(X(b[0]))},{n(Y(b[1]))} Z", fill=light(COLD, 0.85))
    f.line(X(a[0]), Y(a[1]), X(b[0]), Y(a[1]), dark(COLD, 0.1), 1.5)
    f.line(X(b[0]), Y(a[1]), X(b[0]), Y(b[1]), dark(COLD, 0.1), 1.5)
    ax.line([(0, 0), (4.25, 4.25 * G)], COLD)
    for t in (1, 2, 3, 4): ax.point(t, G * t, COLD)
    f.tex(X(2), Y(G) + 22, r"\Delta t = 2{,}0\,\text{s}", "middle")
    f.tex(X(3) + 12, Y(2 * G), r"\Delta v = 19{,}6\,\text{m/s}", "start")
    f.tex(X(4.05) + 10, Y(34.5), r"v = g\,t", "start", COLD)
    f.tex(X(0.3), Y(37), r"g = \dfrac{\Delta v}{\Delta t} = \dfrac{19{,}6\,\text{m/s}}{2{,}0\,\text{s}}", "start")
    f.tex(X(0.3) + 26, Y(26.5), r"= 9{,}81\,\text{m/s}^2", "start")
    return f.svg()


def same_fall():
    f = Fig("fy16-same", 360, "Kaavakuva: kaksi teräspalloa, 1 kg ja 5 kg, putoavat levosta yhtä aikaa ilman ilmanvastusta; raskaampi pallo on "
            "suurempi. Pallot ovat jokaisella hetkellä, 0, 1 ja 2 sekuntia, samalla korkeudella, ja niiden nopeusnuolet ovat yhtä pitkät: "
            "0; 9,81 ja 19,6 metriä sekunnissa. Katkoviiva kulkee molempien nuolten kärkien kautta.")
    top, ppm, k = 100, 7.4, 1.8
    xl, xr = 238, 392
    f.rect(xl - 40, top - 40, xr - xl + 80, 10, IRON, dark(IRON), W_OBJ, 2)
    for x in (xl, xr): f.line(x, top - 30, x, top - 21, dark(IRON), 3)
    f.tex(xl, 26, r"1\,\text{kg}", "middle"); f.tex(xr, 26, r"5\,\text{kg}", "middle")
    for t in range(3):
        y = top + ppm * 0.5 * G * t * t; v = G * t
        f.tex(xl - 56, y, rf"t = {t}\,\text{{s}}", "end")
        f.line(xl - 46, y, xr + 60, y, GRID, W_DETAIL)
        f.ball(f"fy16-sl{t}", xl, y, 11, STEEL)                   # steel: radius ∝ ∛m, 5 kg about 1,7 times wider
        f.ball(f"fy16-sh{t}", xr, y, 19, STEEL)
        if t:
            f.vec(xl, y + 13, xl, y + 13 + v * k, COLD)
            f.vec(xr, y + 21, xr, y + 21 + v * k, COLD)
            tip = y + 21 + v * k
            f.line(xl - 16, tip, xr + 46, tip, COLD, W_GUIDE, GUIDE_DASH)
    f.tex((xl + xr) / 2, tip + 24, r"\text{sama nopeus}", "middle", COLD)
    return f.svg()


def apple():
    """Task illustration (fy1-6-L1-02): an apple has come off its branch and falls towards the grass; no numbers."""
    f = S.scene("fy16-apple", "Kuvitus: omenapuun oksasta irronnut omena putoaa kohti nurmikkoa. Oksalla on lehtiä ja toinen omena; "
                "omenan kohdalla ylhäällä on katkoviivalla merkitty kohta, josta se irtosi.")
    f.rect(0, 0, 600, 360, "#e7f1f8")
    f.path("M0,300 C160,288 420,292 600,300 V360 H0 Z", "#9cc97a"); f.path("M0,318 C200,308 400,312 600,318 V360 H0 Z", "#86b866")
    for k in range(70): f.add(f'<path d="M{n(_rnd(k, 4) * 600)},{n(322 + _rnd(k + 90, 4) * 34)} l3,-9 l3,9" fill="#6fa452"/>')
    trunk = "#8a6a4a"
    f.path("M70,360 C80,250 70,170 96,110 L120,112 C104,180 112,260 118,360 Z", trunk, dark(trunk, 0.35), 1.75)
    f.path("M100,128 C200,96 300,84 420,92", stroke=dark(trunk, 0.35), w=16, extra='stroke-linecap="round"')
    f.path("M100,128 C200,96 300,84 420,92", stroke=trunk, w=12.5, extra='stroke-linecap="round"')
    f.path("M260,94 C300,60 340,50 380,48", stroke=trunk, w=7, extra='stroke-linecap="round"')
    leaf, leaf_d = "#5b9a3c", "#3f7a28"
    for k, (lx, ly, a) in enumerate(((150, 96, -30), (190, 118, 40), (232, 84, -50), (300, 104, 30), (338, 74, -20), (372, 40, 20),
                                    (404, 104, 50), (430, 80, -40), (270, 70, -10), (210, 92, 10))):
        c = leaf if k % 3 else leaf_d
        f.add(f'<path d="M0,0 C8,-10 26,-10 34,0 C26,10 8,10 0,0 Z" transform="translate({lx},{ly}) rotate({a})" fill="{c}" stroke="{dark(c, 0.3)}" stroke-width="1.25"/>')
    def fruit(cx, cy, gid):
        f.ball(gid, cx, cy, 15, "#cf3b2d")
        f.add(f'<path d="M{cx},{cy-14} q2,-8 6,-11" stroke="#6b4a2a" stroke-width="2.5" fill="none" stroke-linecap="round"/>')
    fruit(318, 128, "fy16-apple1")
    f.circle(244, 106, 3, dark(trunk, 0.35))                     # where the falling apple hung
    f.add(f'<circle cx="244" cy="124" r="15" fill="none" stroke="{MUTED}" stroke-width="1.25" stroke-dasharray="{GUIDE_DASH}"/>')
    fruit(244, 236, "fy16-apple2")
    for dy in (156, 176, 196):                                   # motion lines above the falling apple
        f.add(f'<line x1="238" y1="{dy}" x2="238" y2="{dy + 10}" stroke="{MUTED}" stroke-width="1.25" stroke-linecap="round"/>')
        f.add(f'<line x1="250" y1="{dy + 4}" x2="250" y2="{dy + 14}" stroke="{MUTED}" stroke-width="1.25" stroke-linecap="round"/>')
    f.add(f'<ellipse cx="244" cy="312" rx="20" ry="4" fill="#5d8f45" opacity="0.6"/>')
    return f.svg()


def light_gates():
    """Task illustration (fy1-6-L2-07): two light gates one under the other on a stand; a 5,0 cm body falls through them."""
    f = Fig("fy16-gates", 400, "Kaavakuva: telineessä on kaksi valoporttia pystysuunnassa toistensa alapuolella. Kummassakin portissa valo kulkee "
            "lähettimestä vastaanottimeen. Ylhäällä pidikkeessä on 5,0 cm pitkä kappale, joka pudotetaan levosta porttien läpi. Portit on "
            "kytketty kelloon, joka mittaa valon katkeamisajan kummassakin portissa.")
    base_y, px = 372, 150
    f.rect(px - 70, base_y, 140, 14, IRON, dark(IRON), W_OBJ, 3)                                     # stand
    f.rect(px - 6, 30, 12, base_y - 30, "#c4ccd4", dark("#c4ccd4", 0.45), W_OBJ, 2)
    f.rect(px, 34, 150, 10, "#c4ccd4", dark("#c4ccd4", 0.45), W_OBJ, 2)                            # arm with the release clamp
    f.rect(270, 44, 30, 12, IRON, dark(IRON), W_OBJ, 2)
    body = "#e8590c"
    f.rect(278, 56, 14, 40, light(body, 0.25), dark(body, 0.4), W_OBJ, 3)                          # the 5,0 cm body
    f.dim_v(318, 56, 96, r"5{,}0\,\text{cm}")
    gate_c = "#3b4350"
    for gy, name in ((170, r"\text{portti 1}"), (300, r"\text{portti 2}")):
        f.rect(px + 6, gy - 5, 80, 10, "#c4ccd4", dark("#c4ccd4", 0.45), W_OBJ, 2)              # clamp arm to the gate
        f.path(f"M{px + 86},{gy - 26} h28 v52 h-28 Z", gate_c, dark(gate_c, 0.3), W_OBJ)            # the U-shaped gate seen from the side
        f.path(f"M{px + 86},{gy - 26} h154 v12 h-126 v28 h126 v12 h-154 Z", gate_c, dark(gate_c, 0.3), W_OBJ)
        f.line(px + 114, gy, 390, gy, "#e03131", 2, dash="4 3")                                   # the light beam
        f.circle(px + 114, gy, 4, "#ffd43b")
        f.tex(408, gy, name, "start")
    for gy, y2 in ((170, 336), (300, 350)):                                                     # cables to the timer
        f.path(f"M{px + 100},{gy + 26} V{y2} H380", stroke=gate_c, w=2)
    f.rect(380, 318, 120, 50, "#dfe4ea", SOFT_INK, W_OBJ, 6)
    f.rect(392, 328, 96, 30, "#22303c", None, 0, 3)
    f.tex(440, 343, r"\text{kello}", "middle", "#ffffff")
    return f.svg()


def two_planets():
    """A task-only picture: the (t,v) lines of bodies dropped from rest on two planets without an atmosphere; no slope marked."""
    f = Fig("fy16-two", 340, "(t,v)-kuvaaja mittakaavassa: kaksi suoraa origosta, planeetan A ja planeetan B pinnalla levosta pudotetun kappaleen nopeus v ajan t funktiona. "
            "Ruudukon väli on 1 s ja 5 m/s. Planeetan A suora kulkee ruudukon risteyksen (5 s; 20 m/s) kautta ja planeetan B suora risteyksen (5 s; 40 m/s) kautta. "
            "Aika-akseli ulottuu 6 sekuntiin.")
    ax = Axes(f, (96, 300), (470, 60), x=(0, 6), y=(0, 40), xticks=[1, 2, 3, 4, 5, 6], yticks=[5, 10, 15, 20, 25, 30, 35, 40],
              xlabel=r"t\ (\text{s})", ylabel=r"v\ (\text{m/s})", yfmt=lambda v: fi(v) if v % 10 == 0 else "")
    ax.line([(0, 0), (6, 24)], COLD)
    ax.line([(0, 0), (5, 40)], COLD, 3, "12 7")     # both lines are velocities, so both blue; B dashed to tell them apart
    f.tex(ax.X(6) + 8, ax.Y(24), r"\text{A}", "start", COLD)
    f.tex(ax.X(5) + 8, ax.Y(40) - 14, r"\text{B}", "start", COLD)
    return f.svg()


FIGURES = {"hero": hero, "free-fall": free_fall, "vt-graph": vt_graph, "same-fall": same_fall, "two-planets": two_planets,
           "apple": apple, "light-gates": light_gates}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "free-fall": "reveals: the fall distances and speeds at 0–3 s",
    "vt-graph": "reveals: the slope g = 9,81 m/s²",
    "same-fall": "reveals: equal speeds for 1 kg and 5 kg",
    "apple": "safe: the situation only, an apple falling from its branch towards the grass; no numbers",
    "light-gates": "safe: the set-up of two light gates and the 5,0 cm body, no readings",
    "two-planets": "safe: two (t,v) lines from the origin, grid crossings to read, no slopes written (vt-graph is the lesson figure)",
}
