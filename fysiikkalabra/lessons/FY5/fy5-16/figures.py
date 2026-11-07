"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy5-16` writes them into lesson.md."""
import math
from figlib import (Fig, Axes, fi, INK, MUTED, WHITE, RULE, RULE_LIGHT, HEAT, HEAT_LIGHT, HOT, HOT_LIGHT, COLD, COLD_LIGHT,
                    GOOD, GOOD_LIGHT, IRON, ALUMINIUM, METAL_EDGE, COPPER, SAND, SAND_LIGHT, SAND_DARK, GRAIN, GLASS, ICE, n)
import herolib as H


def t_allowed(L):
    """Allowed daily exposure in hours: 85 dB gives 8 h and every +3 dB halves it (lesson-answers.py)."""
    return 8.0 / 2 ** ((L - 85) / 3)


def scale():
    """Ydinajatus: a decibel ladder of everyday sounds, the range from 85 dB upwards marked as harmful."""
    f = Fig("fy516-scale", 372, "Kaavakuva: pystysuora desibeliasteikko 20 desibelistä 130 desibeliin, korkeus mittakaavassa. "
            "Asteikon oikealla puolella on tyypillisiä äänitasoja: kuiskaus noin 30 dB, keskustelu noin 60 dB, ruohonleikkuri "
            "noin 90 dB, rock-konsertti noin 105 dB ja kipukynnys noin 120 dB. Asteikon yläosa 85 desibelistä ylöspäin on "
            "värjätty punaiseksi ja merkitty vasemmalla hakasulkeella: pitkä altistus niin suurelle tasolle vaurioittaa kuuloa.")
    def Y(L): return 344 - (L - 20) * 2.8
    x0, x1 = 300, 326
    f.defs_add(f'<linearGradient id="fy516-ladder" x1="0" y1="1" x2="0" y2="0"><stop offset="0" stop-color="{GOOD_LIGHT}"/>'
               f'<stop offset="0.55" stop-color="{HEAT_LIGHT}"/><stop offset="1" stop-color="{HOT_LIGHT}"/></linearGradient>')
    f.rect(x0, Y(130), x1 - x0, Y(20) - Y(130), "url(#fy516-ladder)", INK, 2.5, 4)
    f.rect(x0 + 2, Y(130) + 2, x1 - x0 - 4, Y(85) - Y(130) - 2, HOT, extra='fill-opacity="0.55"')
    f.line(x0 - 8, Y(85), x1 + 8, Y(85), HOT, 2.5)
    for L in (20, 40, 60, 100, 120):
        f.line(x0 - 7, Y(L), x0, Y(L), INK, 2)
        f.tex(x0 - 12, Y(L), str(L), "end", MUTED)
    f.tex(x0 - 12, Y(85), "85", "end", HOT)
    f.tex(x0 - 8, Y(133) - 14, r"L\ (\text{dB})", "end")
    # bracket for the harmful range
    bx = 236
    f.path(f"M{bx + 10},{n(Y(85))} H{bx} V{n(Y(130))} H{bx + 10}", stroke=HOT, w=2.5)
    f.tex(bx - 8, Y(112), r"\text{kuulovaurion}", "end", HOT)
    f.tex(bx - 8, Y(101), r"\text{vaara}", "end", HOT)
    for L, name in ((30, "kuiskaus"), (60, "keskustelu"), (90, "ruohonleikkuri"), (105, "rock-konsertti"), (120, "kipukynnys")):
        f.line(x1, Y(L), x1 + 18, Y(L), INK, 2)
        f.circle(x1 + 18, Y(L), 4, INK)
        f.tex(x1 + 28, Y(L), r"\text{" + name + "}", "start")
    return f.svg()


def exposure():
    """Kaava: the daily reference time (the time in which the dose of the upper action value accumulates) against the level, 85 ... 100 dB in 3 dB steps (bars to scale)."""
    f = Fig("fy516-exposure", 340, "Pylväskuvaaja mittakaavassa: päivittäinen vertailuaika t tunteina melutason L funktiona. "
            "Melutasolla 85 dB aika on 8 tuntia, 88 dB 4 tuntia, 91 dB 2 tuntia, 94 dB 1 tunti, 97 dB 0,5 tuntia ja 100 dB "
            "0,25 tuntia. Jokainen kolmen desibelin nousu puolittaa pylvään korkeuden.")
    ax = Axes(f, (96, 300), (470, 56), x=(82, 101), y=(0, 9), xticks=[85, 88, 91, 94, 97, 100], yticks=[2, 4, 6, 8],
              xlabel=r"L\ (\text{dB})", ylabel=r"t\ (\text{h})", origin_label=False)
    for L in (85, 88, 91, 94, 97, 100):
        t = t_allowed(L)
        xa, xb = ax.X(L - 0.7), ax.X(L + 0.7)
        f.rect(xa, ax.Y(t), xb - xa, ax.Y(0) - ax.Y(t), COLD, INK, 1.5, 2)
        f.tex(ax.X(L), ax.Y(t) - 18, fi(t), "middle", COLD)
    f.tex(296, 94, r"+3\,\text{dB} \;\Rightarrow\; t : 2", "start")
    return f.svg()


def control():
    """Melun torjunta: source (enclosed machine), path (barrier, distance), receiver (hearing protectors)."""
    f = Fig("fy516-control", 330, "Kaavakuva, ei mittakaavassa: melun torjunnan kolme kohtaa vasemmalta oikealle. Vasemmalla "
            "kone on kotelon sisällä: lähde. Keskellä on meluseinä, jonka yli ääniaallot taipuvat heikentyneinä: kulkutie. "
            "Oikealla ihmisen päässä on kuulonsuojaimet: korva. Kunkin kohdan alla on keino: kotelointi, este ja etäisyys, "
            "kuulonsuojain.")
    for x in (200, 400):
        f.line(x, 50, x, 316, RULE, 2, "6 6")
    for x, word in ((100, "lähde"), (300, "kulkutie"), (500, "korva")):
        f.tex(x, 26, r"\text{" + word + "}", "middle")
    # source: machine in an enclosure
    f.rect(40, 130, 120, 130, SAND_LIGHT, INK, 3, 6)
    f.rect(62, 176, 76, 70, IRON, INK, 2.5, 4)
    f.circle(100, 211, 20, ALUMINIUM, INK, 2)
    f.circle(100, 211, 6, INK)
    for k in range(4):
        f.line(48 + 6 * k, 138, 48 + 6 * k, 252, GRAIN, 1.5)
    # waves leaving the enclosure: weakened
    for r, op in ((70, 0.9), (100, 0.6)):
        f.path(f"M{n(100 + r * math.cos(math.radians(-50)))},{n(195 + r * math.sin(math.radians(-50)))} "
               f"A{r},{r} 0 0 1 {n(100 + r * math.cos(math.radians(10)))},{n(195 + r * math.sin(math.radians(10)))}",
               stroke=COLD, w=3, extra=f'stroke-opacity="{op}" stroke-linecap="round"')
    # path: barrier, waves bend over its top
    f.rect(292, 120, 18, 140, ALUMINIUM, INK, 2.5, 2)
    f.line(214, 260, 386, 260, INK, 2.5)
    for r in (34, 60):
        f.path(f"M{n(301 + r)},{120} A{r},{r} 0 0 1 {n(301 + r * math.cos(math.radians(50)))},{n(120 + r * math.sin(math.radians(50)))}",
               stroke=COLD, w=3, extra='stroke-opacity="0.45" stroke-linecap="round"')
    for x in (230, 262):
        f.path(f"M{x},{110} q12,40 0,80", stroke=COLD, w=3, extra='stroke-opacity="0.7" stroke-linecap="round"')
    # receiver: head with ear muffs
    f.circle(500, 180, 52, SAND_LIGHT, INK, 2.5)
    f.path("M452,166 Q500,92 548,166", stroke=INK, w=6, extra='stroke-linecap="round"')
    f.add(f'<ellipse cx="451" cy="186" rx="16" ry="28" fill="{HOT}" stroke="{INK}" stroke-width="2.5"/>')
    f.add(f'<ellipse cx="549" cy="186" rx="16" ry="28" fill="{HOT}" stroke="{INK}" stroke-width="2.5"/>')
    f.path("M484,238 Q500,250 516,238 L522,262 H478 Z", SAND_LIGHT, INK, 2)
    for x, word in ((100, "kotelointi"), (300, "este, etäisyys"), (500, "kuulonsuojain")):
        f.tex(x, 296, r"\text{" + word + "}", "middle")
    return f.svg()


def room():
    """Tilan akustiikka: direct sound and two reflected rays (ceiling, floor) from a loudspeaker to a listener."""
    f = Fig("fy516-room", 340, "Kaavakuva huoneesta sivulta, ei mittakaavassa. Vasemmalla kaiutin, oikealla kuulijan pää samalla "
            "korkeudella. Suora ääni kulkee vaakasuoraan kaiuttimesta kuulijaan. Katkoviivoilla piirretyt heijastuneet äänet "
            "kulkevat katon ja lattian kautta: ne heijastuvat pinnoista heijastuslain mukaan ja saapuvat kuulijalle pidemmän "
            "matkan jälkeen eli myöhemmin kuin suora ääni.")
    f.rect(40, 60, 520, 240, GLASS, INK, 3, 2)
    f.rect(40, 290, 520, 10, SAND, INK, 2)
    S, Lp = (130, 220), (470, 220)
    # reflected rays (mirror images): ceiling y = 60 and floor y = 290 -> reflection points at x = 300
    for yr in (60, 290):
        f.line(S[0] + 14, S[1], 300, yr, COLD, 2.5, "8 6")
        f.arrow(300, yr, Lp[0] - 30, Lp[1] + (yr - Lp[1]) * 30 / 170, COLD, 2.5, 14)
    f.arrow(S[0] + 16, S[1], Lp[0] - 34, Lp[1], COLD, 3.5, 16)
    # loudspeaker
    f.rect(96, 186, 36, 68, IRON, INK, 2.5, 4)
    f.circle(114, 206, 10, ALUMINIUM, INK, 2)
    f.circle(114, 234, 13, ALUMINIUM, INK, 2)
    # listener's head
    f.circle(490, 214, 26, SAND_LIGHT, INK, 2.5)
    f.add(f'<ellipse cx="465" cy="218" rx="6" ry="10" fill="{SAND}" stroke="{INK}" stroke-width="2"/>')
    f.tex(300, 30, r"\text{heijastunut ääni}", "middle")
    f.tex(300, 244, r"\text{suora ääni}", "middle")
    return f.svg()


def decay():
    """Jälkikaiunta-aika: the level after the source stops, falling 60 dB in T = 1,2 s (bare room) or 0,6 s (panels)."""
    f = Fig("fy516-decay", 330, "Kuvaaja: äänitaso L desibeleinä ajan t funktiona, kun äänilähde vaikenee hetkellä nolla. "
            "Kummassakin huoneessa taso on aluksi 90 dB ja laskee tasaisesti. Paljaiden pintojen luokassa (sininen) taso "
            "on pudonnut 60 dB eli arvoon 30 dB 1,2 sekunnissa, akustiikkalevyillä vaimennetussa luokassa (vihreä) jo "
            "0,6 sekunnissa. Nämä ajat ovat jälkikaiunta-aikoja.")
    ax = Axes(f, (96, 290), (440, 50), x=(0, 1.4), y=(0, 100), xticks=[0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4],
              yticks=[20, 40, 60, 80, 100], xlabel=r"t\ (\text{s})", ylabel=r"L\ (\text{dB})")
    ax.line([(0, 30), (1.2, 30)], MUTED, 1.5, "6 5")
    for T, col in ((1.2, COLD), (0.6, GOOD)):
        ax.line([(0, 90), (T, 30)], col, 3)
        f.line(ax.X(T), ax.Y(30), ax.X(T), ax.Y(0), MUTED, 1.5, "6 5")
        ax.point(T, 30, col)
    ax.point(0, 90, INK)
    f.tex(262, 92, r"\text{paljaat pinnat: } T = 1{,}2\,\text{s}", "start", COLD)
    f.tex(262, 126, r"\text{levyt katossa: } T = 0{,}6\,\text{s}", "start", GOOD)
    f.tex(ax.X(1.2) + 10, ax.Y(30) - 18, r"90\,\text{dB} - 60\,\text{dB}", "start", MUTED)
    return f.svg()


def anc():
    """Vastamelu: noise, the inverted anti-noise and their sum, which is zero (destructive interference)."""
    f = Fig("fy516-anc", 330, "Kaavakuva: kolme aaltoa allekkain samalla aika-akselilla. Ylimpänä sininen melu, keskellä "
            "oranssi vastamelu, joka on samanlainen mutta vastakkaisessa vaiheessa: sen huippu on melun pohjan kohdalla. "
            "Alimpana niiden summa, joka on suora viiva nollassa. Pystysuora katkoviiva näyttää, että huippu ja pohja "
            "osuvat samaan hetkeen.")
    x0, x1, A = 170, 560, 30
    rows = ((66, COLD, 1, "melu"), (166, HEAT, -1, "vastamelu"), (276, INK, 0, "summa"))
    for y, col, sgn, word in rows:
        f.line(x0, y, x1, y, RULE, 1.5)
        pts = " ".join(f"{n(x0 + k * (x1 - x0) / 240)},{n(y - sgn * A * math.sin(2 * math.pi * 2.5 * k / 240))}" for k in range(241))
        f.add(f'<polyline points="{pts}" fill="none" stroke="{col}" stroke-width="3" stroke-linejoin="round"'
              f'{" stroke-dasharray=\"10 6\"" if sgn == -1 else ""}/>')
        f.tex(150, y, r"\text{" + word + "}", "end", col)
    xc = x0 + (x1 - x0) * 0.1                     # first crest of the noise
    f.line(xc, 24, xc, 206, MUTED, 1.5, "6 5")
    f.tex(150, 116, "+", "end")
    f.tex(150, 221, "=", "end")
    return f.svg()


def transducers():
    """Kaiutin ja mikrofoni: the same parts, energy converted in opposite directions."""
    f = Fig("fy516-transducers", 380, "Kaavakuva, ei mittakaavassa, kaksi osaa vierekkäin. Vasemmalla kaiutin sivulta: "
            "kestomagneetti, jonka keskinavan ympärillä on kela, ja kelaan kiinnitetty kartio. Kelaan tulevat johtimet "
            "tuovat vaihtovirran, ja kaksipäinen nuoli kartion edessä näyttää, että kartio värähtelee. Alla energian "
            "muuttuminen: sähkö, liike, ääni. Oikealla mikrofoni: ääniaallot tulevat oikealta kalvoon, joka on kiinni kelassa "
            "magneetin navan ympärillä, ja kelan johtimista saadaan jännite. Alla: ääni, liike, sähkö.")
    f.line(300, 16, 300, 364, RULE, 2, "6 6")

    def unit(dx, mirror_cone):
        # magnet with its centre pole and the coil around the pole (cross-section)
        f.rect(dx + 40, 120, 60, 100, IRON, INK, 2.5, 3)
        f.rect(dx + 100, 155, 40, 30, IRON, INK, 2.5)
        f.rect(dx + 116, 145, 20, 10, COPPER, INK, 1.5)
        f.rect(dx + 116, 185, 20, 10, COPPER, INK, 1.5)
        for xw in (dx + 120, dx + 132):
            f.line(xw, 195, xw, 282, COPPER, 2.5)
    unit(0, True)
    unit(300, False)
    # loudspeaker cone and its vibration
    f.path("M136,145 L240,80 V260 L136,195 Z", SAND_LIGHT, INK, 2.5)
    f.arrow(262, 170, 286, 170, INK, 2.5, 11)
    f.arrow(270, 170, 248, 170, INK, 2.5, 11)
    f.tex(150, 26, r"\text{kaiutin}", "middle")
    f.tex(72, 100, r"\text{magneetti}", "middle")
    f.tex(232, 58, r"\text{kartio}", "middle")
    f.tex(146, 262, r"\text{kela}", "start")
    f.tex(126, 302, r"\text{vaihtovirta}", "middle")
    f.tex(150, 348, r"\text{sähkö} \to \text{liike} \to \text{ääni}", "middle")
    # microphone membrane and incoming sound
    f.rect(436, 100, 8, 140, ALUMINIUM, INK, 2, 2)
    for r in (56, 86, 116):
        a = math.radians(32)
        f.path(f"M{n(640 - r * math.cos(a))},{n(170 - r * math.sin(a))} A{r},{r} 0 0 0 {n(640 - r * math.cos(a))},{n(170 + r * math.sin(a))}",
               stroke=COLD, w=3, extra='stroke-linecap="round"')
    f.tex(450, 26, r"\text{mikrofoni}", "middle")
    f.tex(372, 100, r"\text{magneetti}", "middle")
    f.tex(452, 262, r"\text{kalvo}", "start")
    f.tex(426, 302, r"\text{jännite}", "middle")
    f.tex(450, 348, r"\text{ääni} \to \text{liike} \to \text{sähkö}", "middle")
    return f.svg()


def hero():
    """The chapter's opening illustration: an outdoor concert at dusk, speaker stacks, a crowd, one listener with ear muffs."""
    f = H.hero("fy516-hero", "Kuvitus: ulkoilmakonsertti iltahämärissä. Lavan molemmin puolin on korkeat kaiutintornit, "
               "joista lähtee ääniaaltojen kaaria yleisöä kohti. Lavalla esiintyjä nostaa kädet ylös valokeilojen alla. "
               "Etualalla yleisöä selin katsojaan, ja keskellä yhdellä kuulijalla on punaiset kuulosuojaimet.")
    f.rect(0, 0, 1200, 600, H.grad(f, "fy516h-sky", COLD, HEAT_LIGHT))
    H.forest(f, 380, 60, 34, IRON, seed=4)
    f.rect(0, 380, 1200, 220, H.grad(f, "fy516h-ground", GOOD, SAND_DARK))
    # stage
    f.rect(360, 140, 480, 26, INK, rx=3)
    f.rect(372, 166, 16, 250, INK)
    f.rect(812, 166, 16, 250, INK)
    f.rect(388, 166, 424, 236, INK, extra='fill-opacity="0.85"')
    for x in (450, 600, 750):
        f.path(f"M{x - 10},166 L{x - 90},402 H{x + 90} L{x + 10},166 Z", HEAT_LIGHT, extra='fill-opacity="0.35"')
        f.circle(x, 174, 9, HEAT_LIGHT)
    f.rect(350, 398, 500, 34, IRON, INK, 2)
    H.person(f, 600, 398, shirt=HOT, sc=0.62, arms="up")
    # speaker stacks
    for x0 in (230, 870):
        for k in range(3):
            y = 230 + 68 * k
            f.rect(x0, y, 100, 64, IRON, INK, 3, 4)
            f.circle(x0 + 50, y + 32, 22, ALUMINIUM, INK, 2.5)
            f.circle(x0 + 50, y + 32, 8, INK)
    # sound arcs towards the crowd
    for x0, sgn in ((280, -1), (920, 1)):
        for r in (90, 140, 190):
            a0, a1 = math.radians(60), math.radians(120)
            xa, ya = x0 + r * math.cos(a0), 330 + r * math.sin(a0)
            xb, yb = x0 + r * math.cos(a1), 330 + r * math.sin(a1)
            f.path(f"M{n(xa)},{n(ya)} A{r},{r} 0 0 1 {n(xb)},{n(yb)}", stroke=COLD_LIGHT, w=6, extra='stroke-opacity="0.75" stroke-linecap="round"')
    # crowd, seen from behind
    cols = (INK, IRON, MUTED, COLD, METAL_EDGE, INK)
    for k in range(13):
        x = 40 + k * 94 + 20 * H.rnd(k, 2)
        if abs(x - 640) < 90: continue
        y = 540 + 30 * H.rnd(k, 3)
        f.path(f"M{n(x - 58)},600 Q{n(x - 56)},{n(y)} {n(x)},{n(y - 6)} Q{n(x + 56)},{n(y)} {n(x + 58)},600 Z", cols[k % len(cols)])
        f.circle(x, y - 40, 30, cols[(k + 2) % len(cols)])
    # the listener with ear muffs, centre front
    f.path("M560,600 Q562,500 640,494 Q718,500 720,600 Z", COLD)
    f.circle(640, 444, 44, INK)
    f.path("M594,438 Q640,370 686,438", stroke=MUTED, w=8, extra='stroke-linecap="round"')
    f.add(f'<ellipse cx="595" cy="448" rx="16" ry="26" fill="{HOT}" stroke="{INK}" stroke-width="3"/>')
    f.add(f'<ellipse cx="685" cy="448" rx="16" ry="26" fill="{HOT}" stroke="{INK}" stroke-width="3"/>')
    return f.svg()


FIGURES = {"hero": hero, "scale": scale, "exposure": exposure, "control": control, "room": room, "decay": decay,
           "anc": anc, "transducers": transducers}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "scale": "safe: typical levels of everyday sounds on a decibel ladder, harmful range from 85 dB",
    "exposure": "reveals: every +3 dB halves the allowed daily time (8 h at 85 dB)",
    "control": "safe: the three places of noise control (source, path, ear) with one measure each",
    "room": "safe: direct and reflected sound in a room (rays only)",
    "decay": "reveals: reverberation times 1,2 s and 0,6 s read off the decay lines",
    "anc": "reveals: anti-noise in opposite phase sums to zero",
    "transducers": "reveals: loudspeaker and microphone convert energy in opposite directions",
}
