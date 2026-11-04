"""Figures of fy5-8 (scripts/figlib.py, scripts/fbd.py); `python scripts/figures.py fy5-8` writes them into lesson.md.
Harmonic force: the spring's force on the body F = -k x points towards the equilibrium position; the force that stretches
or compresses the spring is F_v = k x (Newton III: it acts on the spring, not on the body). Forces are red; the
displacement x is a thin ink dimension arrow (never red); energy is the light orange area under the (x, F_v) graph.
Every force diagram is an FBD: the body alone as a plain rectangle, its arrows to scale and its physics checked."""
import math, re
from figlib import (Fig, Axes, INK, MUTED, WHITE, RULE, RULE_LIGHT, SAND_LIGHT, SAND, SAND_DARK, GRAIN, GLASS, ICE, COLD,
                    COLD_LIGHT, GOOD, GOOD_LIGHT, HEAT, HEAT_LIGHT, HOT, HOT_LIGHT, IRON, ALUMINIUM, METAL_EDGE, WATER, WATER_LIGHT, PAPER, fi, n)
from fbd import FBD, ground, FORCE, VELOCITY
import herolib as H
from herolib import grad

g = 9.81
CART, CART_EDGE = SAND_LIGHT, INK            # the cart (not blue: blue is velocity)


def spring(f, x1, x2, y, coils=10, amp=9, w=2.5, col=INK):
    """A coil spring seen from the side, from x1 to x2 at height y: straight leads, then a zigzag."""
    lead = 10
    a, b = x1 + lead, x2 - lead
    pts = [(x1, y), (a, y)]
    for i in range(coils * 2):
        pts.append((a + (b - a) * (i + 0.5) / (coils * 2), y + (amp if i % 2 else -amp)))
    pts += [(b, y), (x2, y)]
    f.path("M" + " L".join(f"{n(px)},{n(py)}" for px, py in pts), stroke=col, w=w)


def wall(f, x, y1, y2):
    """A wall on the left, its face at x, hatched behind."""
    f.rect(x - 16, y1, 16, y2 - y1, RULE_LIGHT)
    f.line(x, y1, x, y2, INK, 3)
    for y in range(int(y1) + 6, int(y2), 12):
        f.line(x - 1, y, x - 13, y + 10, MUTED, 1.5)


def cart(f, cx, y, w=90, h=44):
    """A low-friction cart: its body centred at (cx, y), two wheels on the track below."""
    f.rect(cx - w / 2, y - h / 2, w, h, CART, CART_EDGE, 2.5, 6)
    for dx in (-w * 0.28, w * 0.28):
        f.circle(cx + dx, y + h / 2 + 7, 7, INK)
        f.circle(cx + dx, y + h / 2 + 7, 2.5, WHITE)


def dim(f, x1, x2, y, lab, side="start"):
    """The displacement x as a thin ink dimension arrow from the equilibrium line to the cart (not a force)."""
    f.line(x1, y - 7, x1, y + 7, INK, 1.5)
    f.arrow(x1, y, x2, y, INK, 2, 11)
    f.tex(x2 + (10 if x2 > x1 else -10), y, lab, "start" if x2 > x1 else "end")


def hand(f, x, y, facing=-1):
    """A simple fist gripping at (x, y); facing -1: the fingers on its left side."""
    f.rect(x - 4 if facing < 0 else x - 40, y - 18, 44, 36, SAND_LIGHT, INK, 2.5, 12)
    for k in range(3):
        yy = y - 10 + k * 10
        f.line(x + 6 if facing < 0 else x - 6, yy, x + 18 if facing < 0 else x - 18, yy, INK, 1.5)
    f.rect(x + 34 if facing < 0 else x - 74, y - 12, 40, 24, SAND_LIGHT, INK, 2.5, 6)    # the wrist


# ---------------------------------------------------------------- the opening illustration
def hero():
    """A close-up of the lower right corner of a pinball machine seen from above, at about 2,3 px per mm so the 27 mm
    ball and the plunger's coil spring are the subject: the launch lane with the steel ball resting on the plunger tip,
    the spring compressed between the tip and the bracket inside the front wall, and a hand holding the knob from below,
    pulling it out of the machine. The right flipper and slingshot say "pinball".
    No hint of how the force or the energy depends on the pull: that is the chapter's prediction.
    The machine is drawn in its own units (1,7 px per mm) and the group is scaled by S; its stroke widths are divided by S
    afterwards so the outlines stay 2-3 px in the picture."""
    f = H.hero("fy58-hero", "Kuvitus: flipperipelin oikea alakulma läheltä ylhäältä nähtynä. Laukaisukourussa teräskuula lepää "
               "männän kärjen päällä. Männän varren ympärillä oleva kierrejousi on puristunut kärjen ja etuseinän välissä, koska "
               "käsi pitää männän nupista alta kiinni ja vetää sitä ulos koneesta. Vasemmalla näkyvät pelikentän oikea lyöntimaila "
               "ja kumireunainen kolmio, oikealla koneen puinen sivuseinä ja lattia.")
    f.rect(0, 0, 1200, 600, PAPER)
    S, tx, ty = 1.35, -585, -201
    for x in range(-30, 1200, 64):                  # the floor's boards, running towards the machine
        f.line(x, 0, x, 600, RULE_LIGHT, 2)
    first = len(f.body)
    f.add(f'<g transform="translate({tx} {ty}) scale({S})">')
    # this machine: wooden side, playfield, the launch lane between its wall and the side
    f.add(f'<path d="M1150,160 H1166 V510 H104 V496 H1150 Z" fill="{INK}" fill-opacity="0.12"/>')   # the cabinet's shadow on the floor
    f.rect(100, 150, 1050, 346, H.grad(f, "fy58h-side", SAND, GRAIN, y1=150, y2=500), INK, 3)
    f.rect(148, 150, 904, 310, H.grad(f, "fy58h-field", COLD_LIGHT, GLASS, y1=150, y2=460), INK, 3)
    lx0, lx1 = 1000, 1052
    f.rect(lx0, 150, lx1 - lx0, 310, WHITE)
    f.line(lx0, 150, lx0, 460, INK, 3)
    # inserts, a rollover lane, the right slingshot with its rubber, the inlane guide, the right flipper and the apron
    f.add('<g transform="translate(16 0)">')
    for k, (x, y, r, c1, c2) in enumerate(((520, 176, 42, HOT_LIGHT, HOT), (716, 160, 42, HEAT_LIGHT, HEAT))):   # pop bumpers at the top edge
        f.circle(x, y, r + 11, WHITE, INK, 2.5)
        f.circle(x, y, r, H.grad(f, f"fy58h-bump{k}", c1, c2), INK, 2.5)
        f.circle(x, y, r * 0.42, WHITE, INK, 2)
    for k, (x, y, c) in enumerate(((540, 256, HEAT_LIGHT), (596, 272, GOOD), (652, 278, COLD), (708, 272, HOT_LIGHT), (764, 256, HEAT_LIGHT))):
        f.circle(x, y, 13, c, INK, 2)
    f.add(f'<ellipse cx="652" cy="336" rx="40" ry="22" fill="{HEAT_LIGHT}" stroke="{INK}" stroke-width="2"/>')
    f.rect(878, 150, 44, 90, WHITE, INK, 2.5, 22); f.circle(900, 206, 9, HEAT_LIGHT, INK, 1.5)
    f.path("M876,258 L876,346 L794,380 Z", HEAT_LIGHT, INK, 2.5)
    f.path("M870,266 L802,372", stroke=INK, w=6, extra='stroke-linecap="round"')
    f.path("M940,240 V354 L788,414", stroke=INK, w=4, extra='stroke-linejoin="round"')
    f.path("M778,396 L638,430 L640,442 L778,416 Z", WHITE, INK, 2.5)
    f.circle(778, 406, 13, WHITE, INK, 2.5); f.circle(778, 406, 5, INK)
    f.path("M340,396 L480,430 L478,442 L340,416 Z", WHITE, INK, 2.5)
    f.path("M984,446 H640 L606,460 H984 Z", IRON, INK, 2.5)
    f.path("M478,446 L512,460 H400 V446 Z", IRON, INK, 2.5)
    f.add("</g>")
    # the glass over the playfield: faint reflections
    for x in (640, 900):
        f.add(f'<path d="M{x},150 L{x + 60},150 L{x - 20},460 L{x - 80},460 Z" fill="{WHITE}" fill-opacity="0.3"/>')
    # the front rail (lockdown bar)
    f.rect(92, 460, 1066, 34, H.steel(f, "fy58h-bar", vertical=True), INK, 3, 6)
    # the plunger pulled back about 30 mm: rod through the front wall, coil spring squeezed between tip and bracket
    cx, tip = (lx0 + lx1) / 2, 356
    f.rect(cx - 6, tip, 12, 190, ALUMINIUM, INK, 2)
    f.rect(cx - 24, 446, 48, 12, IRON, INK, 2.5, 2)
    coils, y0, y1 = 13, tip + 18, 446
    pts = [(cx + (-19 if i % 2 else 19), y0 + (y1 - y0) * i / (coils - 1)) for i in range(coils)]
    f.path("M" + " L".join(f"{n(x)},{n(y)}" for x, y in pts), stroke=IRON, w=4, extra='stroke-linejoin="round"')
    f.rect(cx - 22, tip, 44, 18, INK, INK, 2, 5)
    # the steel ball resting on the tip (the playfield slopes down towards the player)
    f.defs_add(f'<radialGradient id="fy58h-ball" cx="0.35" cy="0.35" r="0.7"><stop offset="0" stop-color="{WHITE}"/>'
               f'<stop offset="0.5" stop-color="{ALUMINIUM}"/><stop offset="1" stop-color="{IRON}"/></radialGradient>')
    f.circle(cx, tip - 24, 23, "url(#fy58h-ball)", INK, 2)
    # the knob pulled out of the machine; a hand from the lower right holds it from below, its thumb under the knob
    # and three fingers curled round the stem between the knob and the front rail
    ky, skin = 544, SAND_LIGHT
    def limb(x1, y1, x2, y2, w, q=None):
        d = f"M{n(x1)},{n(y1)} " + (f"Q{n(q[0])},{n(q[1])} " if q else "L") + f"{n(x2)},{n(y2)}"
        f.path(d, stroke=INK, w=w + 5, extra='stroke-linecap="round"')
        f.path(d, stroke=skin, w=w, extra='stroke-linecap="round"')
    limb(cx + 150, ky + 120, cx + 56, ky + 30, 46)                                   # forearm and wrist
    f.add(f'<ellipse cx="{n(cx + 40)}" cy="{ky + 18}" rx="38" ry="30" fill="{skin}" stroke="{INK}" stroke-width="2.5" transform="rotate(-30 {n(cx + 40)} {ky + 18})"/>')   # palm
    limb(cx + 30, ky + 34, cx - 22, ky + 20, 15, q=(cx - 6, ky + 40))               # thumb under the knob
    f.circle(cx, ky, 18, H.grad(f, "fy58h-knob", HOT_LIGHT, HOT), INK, 2.5)
    for k, y in enumerate((ky - 26, ky - 40)):                                      # fingers round the stem
        limb(cx + 44 - 4 * k, y + 22, cx - 20, y, 14, q=(cx + 18, y - 10))
    f.add(f'<path d="M{n(cx + 52)},{ky - 2} Q{n(cx + 34)},{ky - 20} {n(cx + 8)},{ky - 14}" fill="none" stroke="{INK}" stroke-width="2"/>')   # crease of the ring finger
    f.add("</g>")
    for i in range(first, len(f.body)):          # keep the outlines 2-3 px in the picture
        f.body[i] = re.sub(r'stroke-width="([\d.]+)"', lambda m: f'stroke-width="{n(float(m.group(1)) / S)}"' if float(m.group(1)) <= 6 else m.group(0), f.body[i])
    return f.svg()



# ---------------------------------------------------------------- theory figures
def suunta():
    """Ydinajatus: a cart on a spring stretched, at its rest length and compressed; the spring's force on the cart points
    towards the equilibrium position each time. Schematic (lengths to one scale: F = k x, 1 px of x gives 1 px of F)."""
    f = Fig("fy58-suunta", 390, "Kaavakuva, ei mittakaavassa: kolme tilannetta allekkain. Kärry on kiinni vaakasuorassa jousessa, jonka toinen "
            "pää on seinässä vasemmalla. Pystysuora katkoviiva on tasapainoasema x = 0. Ylhäällä kärry on siirretty oikealle, "
            "jousi on venynyt, ja jousen voima F osoittaa vasemmalle kohti tasapainoasemaa. Keskellä kärry on tasapainoasemassa, "
            "jousi on lepopituudessaan eikä voimaa ole. Alhaalla kärry on siirretty vasemmalle, jousi on puristunut, ja jousen "
            "voima osoittaa oikealle kohti tasapainoasemaa. Kärryn paikkaa x kuvaa ohut musta mittanuoli, voimaa punainen nuoli.")
    xeq = 300
    f.tex(xeq, 18, r"\text{tasapainoasema } x = 0", "middle")
    f.line(xeq, 34, xeq, 372, MUTED, 1.5, "6 5")
    for (y, d, word) in ((100, 70, r"\text{venytetty}"), (220, 0, r"\text{lepopituus}"), (340, -70, r"\text{puristettu}")):
        wall(f, 44, y - 42, y + 36)
        f.line(44, y + 36, 470, y + 36, INK, 2.5)
        cx = xeq + d
        spring(f, 44, cx - 45, y + 5, coils=9, amp=8)
        cart(f, cx, y)
        f.tex(585, y - 12, word, "end")
        f.tex(585, y + 20, r"x > 0" if d > 0 else (r"x = 0" if d == 0 else r"x < 0"), "end", MUTED)
        if d > 0:
            dim(f, xeq, cx, y - 46, "x")
            f.arrow(cx - 45, y - 12, cx - 45 - d, y - 12, FORCE, 4, 18)
            f.tex(cx - 45 - d - 18, y - 32, r"\overline{F}", "end", FORCE)
        elif d < 0:
            dim(f, xeq, cx, y - 46, "x")
            f.arrow(cx - 45 + d, y - 12, cx - 45, y - 12, FORCE, 4, 18)       # a push: the arrow ends on the cart's face
            f.tex(cx - 45 + d - 10, y - 32, r"\overline{F}", "end", FORCE)
        else:
            f.tex(cx - 60, y - 34, r"F = 0", "end", FORCE)
    return f.svg()


def pari():
    """Ydinajatus: Newton III. A hand stretches a spring fixed to a wall; drawn apart, the hand's force acts on the spring
    (the stretching force F_v) and the spring's force acts on the hand (F), equal and opposite."""
    f = Fig("fy58-pari", 330, "Kaksi kuvaa allekkain. Ylhäällä käsi venyttää seinään kiinnitettyä jousta oikealle. Alhaalla jousi ja käsi on "
            "piirretty erilleen: jousen oikeaan päähän vaikuttaa käden voima F v oikealle, ja käteen vaikuttaa jousen voima F "
            "vasemmalle. Nuolet ovat yhtä pitkät: voimat ovat yhtä suuret ja vastakkaissuuntaiset, ja ne vaikuttavat eri "
            "kappaleisiin.")
    # the situation
    wall(f, 44, 40, 130)
    spring(f, 44, 330, 86, coils=11, amp=9)
    f.circle(336, 86, 6, WHITE, INK, 2.5)
    hand(f, 344, 86, -1)
    f.tex(585, 86, r"\text{tilanne}", "end", MUTED)
    f.line(20, 160, 580, 160, RULE, 2, "6 6")
    # drawn apart: the spring with the hand's force, the hand with the spring's force
    y = 236
    wall(f, 44, 196, 276)
    spring(f, 44, 250, y, coils=9, amp=9)
    f.circle(256, y, 6, WHITE, INK, 2.5)
    f.arrow(262, y, 352, y, FORCE, 4, 18)
    f.tex(307, y - 30, r"\overline{F}_\text{v}", "middle", FORCE)
    f.tex(160, y + 54, r"\text{käsi vetää jousta}", "middle")
    hand(f, 470, y, -1)
    f.arrow(462, y, 372, y, FORCE, 4, 18)
    f.tex(417, y - 30, r"\overline{F}", "middle", FORCE)
    f.tex(470, y + 54, r"\text{jousi vetää kättä}", "middle")
    return f.svg()


def kulmakerroin():
    """Kaava: a calibration graph of a spring (example values, k = 40 N/m): the fitted line through the origin and a
    slope triangle between two points on the line, (0,025 m; 1,0 N) and (0,100 m; 4,0 N)."""
    f = Fig("fy58-kulmakerroin", 360, "Kuvaaja mittakaavassa, keksityt esimerkkiarvot: vaaka-akselilla venymä x metreinä nollasta 0,125:een, "
            "pystyakselilla jousta venyttävä voima F v newtoneina nollasta viiteen. Viisi mittauspistettä on lähellä origon "
            "kautta kulkevaa suoraa. Suoralta on valittu kaksi pistettä, x 0,025 metriä ja voima 1,0 newtonia sekä x 0,100 "
            "metriä ja voima 4,0 newtonia, ja niiden väliin on piirretty kulmakerroinkolmio, jonka sivut ovat Δx ja Δ F v. "
            "Suoran kulmakerroin on jousivakio k.")
    ax = Axes(f, (92, 300), (480, 64), x=(0, 0.125), y=(0, 5), xticks=[0.025, 0.050, 0.075, 0.100], yticks=[1, 2, 3, 4, 5],
              xlabel=r"x\ (\text{m})", ylabel=r"F_\text{v}\ (\text{N})", xfmt=lambda v: fi(v, 3))
    ax.line([(0, 0), (0.115, 4.6)], INK, 3)
    x1, F1, x2, F2 = 0.025, 1.0, 0.100, 4.0
    f.line(ax.X(x1), ax.Y(F1), ax.X(x2), ax.Y(F1), MUTED, 2, "6 5")
    f.line(ax.X(x2), ax.Y(F1), ax.X(x2), ax.Y(F2), MUTED, 2, "6 5")
    f.tex((ax.X(x1) + ax.X(x2)) / 2, ax.Y(F1) + 20, r"\Delta x", "middle", MUTED)
    f.tex(ax.X(x2) + 12, (ax.Y(F1) + ax.Y(F2)) / 2, r"\Delta F_\text{v}", "start", MUTED)
    for (px, py) in [(0.02, 0.85), (0.04, 1.55), (0.06, 2.45), (0.08, 3.15), (0.10, 4.05)]:
        ax.point(px, py)
    for (px, py) in [(x1, F1), (x2, F2)]:
        f.circle(ax.X(px), ax.Y(py), 8, "none", HOT, 2.5)
    f.tex(ax.X(0.003), ax.Y(4.3), r"k = \dfrac{\Delta F_\text{v}}{\Delta x}", "start")
    return f.svg()


def pinta_ala():
    """Kaava, spring potential energy: the area under the (x, F_v) line from 0 to x is a triangle 1/2 · x · kx; at twice
    the extension the triangle holds four copies of it (schematic, no numbers)."""
    f = Fig("fy58-pinta-ala", 360, "Kaavakuva ilman lukuarvoja: suora F v = kx origosta ylös. Vaaka-akselilla venymät x ja 2x, pystyakselilla "
            "voimat kx ja 2kx. Venymää x vastaava kolmio suoran alla on väritetty oranssiksi ja merkitty E p:llä: sen kanta on x ja "
            "korkeus kx. Venymää 2x vastaava suurempi kolmio on jaettu katkoviivoilla neljään samanlaiseen kolmioon, joista "
            "yksi on väritetty, joten sen pinta-ala on 4 E p.")
    ax = Axes(f, (100, 306), (440, 64), x=(0, 2.3), y=(0, 2.3), xticks=[1, 2], yticks=[1, 2],
              xlabel=r"x", ylabel=r"F_\text{v}", grid=False, origin_label=True,
              xfmt=lambda v: "x" if v == 1 else "2x", yfmt=lambda v: "kx" if v == 1 else "2kx")
    ax.area([(1, 0), (2, 0), (2, 2), (1, 1)], HEAT_LIGHT, 0.3)
    ax.area([(0, 0), (1, 0), (1, 1)], HEAT_LIGHT, 0.95)
    X, Y = ax.X, ax.Y
    for (a, b, c, d) in [(1, 0, 1, 1), (1, 1, 2, 1), (1, 0, 2, 1), (2, 0, 2, 2)]:
        f.line(X(a), Y(b), X(c), Y(d), MUTED, 1.5, "6 5")
    ax.line([(0, 0), (2.2, 2.2)], INK, 3)
    f.tex(X(0.68), Y(0.3), r"E_\text{p}", "middle", INK)
    f.tex(X(2.0) + 14, Y(0.55), r"4E_\text{p}", "start", HEAT)
    f.path(f"M{n(X(2) + 6)},{n(Y(0) - 2)} h6 V{n(Y(2) + 2)} h-6", stroke=HEAT, w=2)
    f.tex(X(1.15), Y(2.15), r"F_\text{v} = kx", "end")
    return f.svg()


def esimerkki():
    """The worked example: a 1,20 kg fish hangs at rest from a spring balance. Left the situation picture, right the
    fish's force diagram (a rectangle): weight G down from the centre, the spring's force F up from the top face."""
    m = 1.20; G = m * g
    f = Fig("fy58-esimerkki", 340, "Kaksi kuvaa vierekkäin. Vasemmalla tilannekuva: jousivaaka riippuu koukusta, ja sen alapään koukussa "
            "riippuu kala levossa. Oikealla kalan voimakuvio, kala suorakulmiona: paino G keskipisteestä alas ja jousen voima F "
            "yläpinnan keskeltä ylös, yhtä pitkänä. Nurkassa akseli y ylös.")
    # the situation: a spring balance from a hook, the fish below
    f.line(60, 22, 200, 22, INK, 3)
    f.path("M130,22 v14 q0,10 -8,10", stroke=INK, w=2.5)
    f.rect(112, 48, 36, 120, GLASS, INK, 2.5, 6)
    pts = [(130, 52)] + [(130 + (9 if i % 2 else -9), 58 + i * 7) for i in range(14)] + [(130, 160)]
    f.path("M" + " L".join(f"{n(x)},{n(y)}" for x, y in pts), stroke=INK, w=2)
    for yy in range(70, 166, 16): f.line(148, yy, 154, yy, MUTED, 1.5)
    f.line(130, 168, 130, 186, INK, 2.5)
    f.path("M130,186 q8,0 8,8 q0,8 -8,8", stroke=INK, w=2.5)
    f.path("M72,250 Q130,196 190,250 Q130,300 72,250 Z", grad(f, "fy58-fish", WATER_LIGHT, WATER), INK, 2.5)
    f.path("M190,250 L224,226 L220,274 Z", WATER, INK, 2.5)
    f.circle(92, 244, 4, INK)
    f.path("M130,202 L130,212", stroke=INK, w=2)
    f.line(270, 30, 270, 320, RULE, 2, "6 6")
    # the force diagram
    bx, by, w, h = 430, 180, 120, 60
    d = FBD(f, 100 / G, body=(bx, by, w, h), m=m, a=(0, 0))
    d.force("G", (0, -G), (bx, by), "gravity", lab=(26, -4))
    d.force("F", (0, G), (bx, by - h / 2), "spring", lab=(26, 8))
    d.draw()
    ax_, ay_, L = 312, 300, 44
    f.arrow(ax_, ay_, ax_, ay_ - L, MUTED, 2, 10)
    f.tex(ax_, ay_ - L - 14, "y", "middle", MUTED)
    return f.svg()


# ---------------------------------------------------------------- task figures (shown by id from inquiry.json and exercises.json)
def virhe():
    """Find the error: a block hanging at rest from a spring; the student drew the block's pull on the spring (F_2) on the
    block's own diagram."""
    f = Fig("fy58-virhe", 330, "Opiskelijan piirtämä voimakuvio jousesta levossa riippuvasta kappaleesta, kappale suorakulmiona. "
            "Keskipisteestä nuoli G suoraan alas. Yläpinnan keskeltä nuoli F 1 suoraan ylös, yhtä pitkänä kuin G. Yläpinnan "
            "yläpuolelta vähän sivummalta nuoli F 2 suoraan alas yläpintaan asti, yhtä pitkänä kuin G.")
    bx, by, w, h = 300, 190, 130, 64
    d = FBD(f, 1.0, body=(bx, by, w, h), wrong="F_2 is the block's pull on the spring (the Newton III partner of the spring's "
            "force F_1): it acts on the spring, not on the block, and with it the forces do not cancel although the block is at rest")
    d.force("G", (0, -100), (bx, by), "gravity", lab=(-24, -6))
    d.force("F_1", (0, 100), (bx - 30, by - h / 2), "spring", tex=r"\overline{F}_1", lab=(-24, 8))
    d.force("F_2", (0, -100), (bx + 40, by - h / 2), "other", tex=r"\overline{F}_2", lab=(26, 10), push=True)
    d.draw()
    return f.svg()


def malli_laatikko():
    """Model diagram of the drawing task: a 6,0 kg box pulled across a level floor at constant velocity by a horizontal
    spring (k = 120 N/m); kinetic friction 18 N; the spring's force 18 N to the right (lesson-answers.py check3)."""
    m = 6.0; G = m * g; Fmu = 18.0
    f = Fig("fy58-malli-laatikko", 340, "Mallikuvio: laatikko suorakulmiona vaakasuoralla lattialla. Paino G keskipisteestä alas. Lattian "
            "tukivoima N alapinnasta ylös yhtä pitkänä. Jousen voima F oikean sivun keskeltä vaakasuoraan oikealle ja "
            "liikekitka F μ alapinnan vasemmasta kulmasta vasemmalle, yhtä pitkinä, noin kolmasosa painon pituudesta. "
            "Erillään sininen nopeusnuoli v oikealle. Nurkassa akselit x oikealle ja y ylös.")
    bx, by, w, h = 300, 170, 140, 70
    ground(f, 120, 500, by + h / 2)
    d = FBD(f, 110 / G, body=(bx, by, w, h), m=m, a=(0, 0))
    d.force("G", (0, -G), (bx, by), "gravity", lab=(26, -4))
    d.force("N", (0, G), (bx - 30, by + h / 2), "normal", surface=0, lab=(-28, 8))
    d.force("F", (Fmu, 0), (bx + w / 2, by), "spring", lab=(10, -22))
    d.force("F_mu", (-Fmu, 0), (bx - w / 2, by + h / 2), "friction", surface=0, lab=(-8, 22))
    d.draw()
    d.motion(r"\overline{v}", (1, 0), (bx + 10, by - 70), 70)
    ax_, ay_, L = 52, 306, 44
    f.arrow(ax_, ay_, ax_ + L, ay_, MUTED, 2, 10); f.arrow(ax_, ay_, ax_, ay_ - L, MUTED, 2, 10)
    f.tex(ax_ + L + 14, ay_, "x", "middle", MUTED); f.tex(ax_, ay_ - L - 14, "y", "middle", MUTED)
    return f.svg()


MIT_X = [1.7, 3.2, 5.0, 6.4, 8.3, 9.8]                       # cm (lesson-answers.py "mittaus")
MIT_M = [50, 100, 150, 200, 250, 300]                        # g


def mittaus():
    """The measurement task: stretching force F_v = mg of hanging masses against the extension x (example data), points
    only: no fitted line, no slope."""
    f = Fig("fy58-mittaus", 360, "Kuvaaja mittakaavassa, keksitty esimerkkiaineisto: vaaka-akselilla jousen venymä x senttimetreinä "
            "nollasta 12:een, pystyakselilla jousta venyttävä voima F v newtoneina nollasta 3,5:een. Kuusi mittauspistettä: "
            "1,7 senttimetriä ja 0,49 newtonia, 3,2 ja 0,98, 5,0 ja 1,47, 6,4 ja 1,96, 8,3 ja 2,45 sekä 9,8 senttimetriä ja "
            "2,94 newtonia. Suoraa ei ole piirretty.")
    ax = Axes(f, (92, 304), (480, 64), x=(0, 12), y=(0, 3.5), xticks=[2, 4, 6, 8, 10, 12], yticks=[0.5, 1, 1.5, 2, 2.5, 3, 3.5],
              xlabel=r"x\ (\text{cm})", ylabel=r"F_\text{v}\ (\text{N})", yfmt=lambda v: fi(v, 1))
    for xx, mm in zip(MIT_X, MIT_M):
        ax.point(xx, mm / 1000 * g)
    return f.svg()


def ex_suora():
    """Exercise L1-04: the (x, F_v) line of a spring with k = 60 N/m through gridline points; no slope given."""
    f = Fig("fy58-ex-suora", 360, "Kuvaaja mittakaavassa: vaaka-akselilla jousen venymä x metreinä nollasta 0,25:een, pystyakselilla "
            "jousta venyttävä voima F v newtoneina nollasta 15:een. Suora alkaa origosta ja nousee tasaisesti; se kulkee "
            "ruudukon pisteiden kautta, esimerkiksi venymällä 0,10 metriä voima on 6 newtonia.")
    ax = Axes(f, (92, 304), (480, 64), x=(0, 0.25), y=(0, 15), xticks=[0.05, 0.10, 0.15, 0.20, 0.25], yticks=[3, 6, 9, 12, 15],
              xlabel=r"x\ (\text{m})", ylabel=r"F_\text{v}\ (\text{N})", xfmt=lambda v: fi(v, 2))
    ax.line([(0, 0), (0.25, 15)], INK, 3)
    return f.svg()


def ex_kaksi():
    """Exercise L2-04: two springs A (60 N/m) and B (25 N/m) as (x, F_v) lines; no slopes or energies given."""
    f = Fig("fy58-ex-kaksi", 360, "Kuvaaja mittakaavassa: vaaka-akselilla venymä x metreinä nollasta 0,12:een, pystyakselilla jousta "
            "venyttävä voima F v newtoneina nollasta kahdeksaan. Kaksi origosta alkavaa suoraa: jousen A suora on jyrkempi ja "
            "kulkee pisteen 0,10 metriä, 6,0 newtonia kautta; jousen B suora on loivempi ja kulkee pisteen 0,10 metriä, 2,5 "
            "newtonia kautta. B:n suora on katkoviiva.")
    ax = Axes(f, (92, 304), (470, 64), x=(0, 0.12), y=(0, 8), xticks=[0.02, 0.04, 0.06, 0.08, 0.10, 0.12], yticks=[1, 2, 3, 4, 5, 6, 7, 8],
              xlabel=r"x\ (\text{m})", ylabel=r"F_\text{v}\ (\text{N})", xfmt=lambda v: fi(v, 2))
    ax.line([(0, 0), (0.12, 7.2)], INK, 3)
    ax.line([(0, 0), (0.12, 3.0)], INK, 3, "9 6")
    f.tex(ax.X(0.12) - 6, ax.Y(7.2) - 18, r"\text{A}", "end")
    f.tex(ax.X(0.12) + 2, ax.Y(3.0) - 20, r"\text{B}", "end")
    return f.svg()


FIGURES = {"hero": hero, "suunta": suunta, "pari": pari, "kulmakerroin": kulmakerroin, "pinta-ala": pinta_ala,
           "esimerkki": esimerkki, "virhe": virhe, "malli-laatikko": malli_laatikko, "mittaus": mittaus,
           "ex-suora": ex_suora, "ex-kaksi": ex_kaksi}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "hero": "decorative",
    "suunta": "reveals: the spring's force points towards the equilibrium position, stretched and compressed (a theory figure)",
    "pari": "reveals: Newton III, the hand's force on the spring and the spring's force on the hand (a theory figure)",
    "kulmakerroin": "reveals: the spring constant as the slope of the (x, F_v) line, k = 40 N/m (a theory graph)",
    "pinta-ala": "reveals: E_p as the triangle under the (x, F_v) line, four times at twice the extension (a theory figure)",
    "esimerkki": "reveals: the force diagram of the worked example (a fish hanging from a spring balance)",
    "virhe": "safe: a deliberately wrong diagram (the block's pull on the spring drawn on the block) for error-finding; its description lists the arrows, not the error",
    "malli-laatikko": "reveals: the model diagram of a box pulled by a spring at constant velocity (shown after the attempt)",
    "mittaus": "safe: six measured points (x in cm, F_v = mg in N) of a hanging-mass calibration, no fitted line or slope",
    "ex-suora": "safe: the (x, F_v) line of one spring on a grid, no slope or k given",
    "ex-kaksi": "safe: the (x, F_v) lines of springs A and B on a grid, no slopes or energies given",
}
