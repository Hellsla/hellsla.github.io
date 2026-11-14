"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy7-16` writes them into lesson.md.
FY7 colours: magnetic field lines #2b8a3e, current #7048e8, light rays #e64980; copper #b8622d, iron and steel #6c757d.
The charger figure's field lines are computed: they are contour lines of the transmitter coil's flux through a coaxial
circle (the same thin-coil model as the simulation), at equal flux steps, so the number of lines through the receiver
is proportional to the flux through it."""
import math
from figlib import (Fig, Axes, fi, INK, MUTED, WHITE, RULE, RULE_LIGHT, GLASS, WATER_LIGHT, WATER, SAND_LIGHT, SAND,
                    GRAIN, HEAT_LIGHT, HEAT, COLD, COLD_LIGHT, ALUMINIUM, IRON, COPPER, ICE, GOOD, GOOD_LIGHT, PAPER, n)
import herolib as H

RAY = "#e64980"          # light in FY7 (chapters 10–16)
FIELD = "#2b8a3e"        # magnetic field lines
CURRENT = "#7048e8"      # electric current


# --- the thin-coil model: flux of a circular loop (radius R, at z = 0) through a coaxial circle (r, z) ---
def _ke(k):
    a, b, s, w = 1.0, math.sqrt(1 - k * k), k * k / 2, 0.5
    while abs(a - b) > 1e-14:
        c = (a - b) / 2; a, b = (a + b) / 2, math.sqrt(a * b); w *= 2; s += w * c * c
    K = math.pi / (2 * a)
    return K, K * (1 - s)


def flux(R, r, z):
    """Flux through a circle of radius r at height z per unit current (μ0 left out: only ratios are used)."""
    if r <= 0: return 0.0
    k2 = 4 * R * r / ((R + r) ** 2 + z * z); k = math.sqrt(min(k2, 1 - 1e-12)); K, E = _ke(k)
    return math.sqrt(R * r) * ((2 / k - k) * K - 2 / k * E)


def field_line(R, level, rho_max=60.0, steps=120):
    """One field line around the wire at (R, 0) as points (r, z) in mm: along each ray from the wire, the point where
    the flux equals level (the flux falls monotonically away from the wire); r ≥ 0, the line meets the axis."""
    pts = []
    for i in range(steps + 1):
        ph = 2 * math.pi * i / steps
        c, s = math.cos(ph), math.sin(ph)
        top = rho_max if c >= 0 else min(rho_max, R / -c)      # stop at the axis r = 0
        lo, hi = 0.6, top
        if flux(R, R + lo * c, lo * s) < level: continue
        if flux(R, R + hi * c, hi * s) > level: pts.append((R + hi * c, hi * s)); continue
        for _ in range(40):
            mid = (lo + hi) / 2
            if flux(R, R + mid * c, mid * s) > level: lo = mid
            else: hi = mid
        pts.append((R + lo * c, lo * s))
    return pts


def _coil_mark(f, x, y, into, r=7, fill=COPPER):
    """A wire bundle in cross-section: a copper disc with the current's direction in white (× into the page, • out
    of it); fill=CURRENT marks an eddy current in the pan bottom in violet, apart from the coil's copper."""
    f.circle(x, y, r, fill, INK, 1.5)
    if into:
        d = r * 0.55
        f.line(x - d, y - d, x + d, y + d, WHITE, 2.5); f.line(x - d, y + d, x + d, y - d, WHITE, 2.5)
    else:
        f.circle(x, y, 2.5, WHITE)


def _panel(f, cx, z_rx, tag, R=20.0, R2=20.0, s=4.0, y0=262, label=True):
    """One panel of the charger figure: transmitter coil (radius R mm) at y0, receiver (R2) at height z_rx mm."""
    f.defs_add(f'<clipPath id="fy716-clip-{tag}"><rect x="{n(cx - 136)}" y="56" width="272" height="244"/></clipPath>')
    X = lambda r: cx + r * s
    Y = lambda z: y0 - z * s
    # the pad and the phone (behind the field lines)
    f.rect(cx - 30 * s, y0 - 6, 60 * s, 30, ALUMINIUM, INK, 2, 8)
    py = Y(z_rx)
    f.rect(cx - 30 * s, py - 36, 60 * s, 30, IRON, INK, 2, 6)
    ref = flux(R, R2, 3.0)                                   # flux through the receiver at 3 mm
    step = ref / 6.5                                         # 6 lines at 3 mm, none exactly on the receiver wire
    phi_rx = flux(R, R2, z_rx)
    f.add(f'<g clip-path="url(#fy716-clip-{tag})">')
    for k in range(1, 15):
        lv = k * step
        pts = field_line(R, lv)
        if len(pts) < 2: continue
        through = lv < phi_rx                                # the line crosses height z_rx inside r < R2
        op = 1.0 if through else 0.32
        for sign in (1, -1):
            d = "M" + " L".join(f"{n(cx + sign * r * s)},{n(Y(z))}" for r, z in pts)
            f.add(f'<path d="{d}" fill="none" stroke="{FIELD}" stroke-width="{2.5 if through else 1.5}" '
                  f'stroke-opacity="{op:g}" stroke-linejoin="round"/>')
    f.add('</g>')
    # upward arrowhead on the axis line (field up through the middle at this instant)
    f.path(f"M{n(cx)},{n(Y(0) - 40)} l-7,13 h14 Z", FIELD)
    # coils: transmitter current into the page on the right, out on the left -> field up through the middle
    _coil_mark(f, X(R), Y(0), True); _coil_mark(f, X(-R), Y(0), False)
    f.circle(X(R2), py, 6, COPPER, INK, 1.5); f.circle(X(-R2), py, 6, COPPER, INK, 1.5)
    if label:
        f.tex(cx, py - 21, r"\text{puhelin}", "middle", bg=True)
    return phi_rx / ref


def charger():
    f = Fig("fy716-charger", 380, "Periaatekuva langattomasta laturista sivulta leikattuna, kentän muoto laskettu: "
            "kaksi paneelia. Kummassakin alhaalla on latausalusta, jonka sisällä lähetinkäämi, ja sen yläpuolella "
            "puhelin, jonka pohjassa on samankokoinen vastaanotinkäämi. Lähetinkäämin vaihtovirta synnyttää "
            "magneettikentän, jonka vihreät kenttäviivat kiertävät käämin johtimien ympäri ja kulkevat käämin keskeltä "
            "ylöspäin; vihreä kolmio käämin keskellä näyttää kentän suunnan. Vasemmalla puhelin on 3 millimetrin päässä, ja kuusi kenttäviivaa kulkee vastaanotinkäämin läpi. "
            "Oikealla puhelin on 20 millimetrin päässä, ja vastaanottimen läpi kulkee vain yksi viiva; muut viivat "
            "kääntyvät takaisin jo ennen puhelinta. Vastaanottimen läpi kulkevat viivat on piirretty tummemmin.")
    _panel(f, 150, 3.0, "a")
    _panel(f, 450, 20.0, "b")
    f.line(300, 24, 300, 366, RULE, 1.5, "6 5")
    f.tex(150, 32, r"z = 3\,\text{mm}", "middle", w=150)
    f.tex(450, 32, r"z = 20\,\text{mm}", "middle", w=160)
    f.tex(150, 318, r"\text{laturi}", "middle", w=100)
    f.tex(450, 318, r"\text{laturi}", "middle", w=100)
    # the two coils named once each: the transmitter in the left panel, the receiver in the right one
    f.tex(8, 352, r"\text{lähetinkäämi}", "start")
    f.line(42, 340, 66, 270, MUTED, 1.5)
    f.tex(306, 100, r"\text{vastaanotinkäämi}", "start", bg=True)
    f.line(344, 112, 367, 175, MUTED, 1.5)
    return f.svg()


def hob():
    f = Fig("fy716-hob", 360, "Periaatekuva induktioliedestä sivulta leikattuna, ei mittakaavassa. Ylhäällä on "
            "teräskattila, jossa on vettä. Kattila seisoo lieden lasilevyllä, ja lasin alla on litteä kuparikela. "
            "Kelan vaihtovirta synnyttää vaihtuvan magneettikentän, jonka vihreät kenttäviivat kiertävät kelan "
            "johtimien ympäri; uloimmat kulkevat lasin läpi kattilan pohjaan. Kattilan pohjassa kiertää pyörrevirta "
            "vastakkaiseen suuntaan kuin kelan virta. Kelan virran suunta on merkitty kuparinvärisiin johtimiin "
            "valkoisilla pisteillä ja risteillä, pyörrevirran suunta violetteihin merkkeihin. "
            "Oranssit nuolet näyttävät, että energia siirtyy kuumenevasta pohjasta veteen. Lasilevyssä ei kulje "
            "virtaa.")
    cx = 300
    # glass top
    f.rect(40, 196, 520, 22, GLASS, INK, 2, 3)
    # the pan: steel walls and a thick bottom, water inside
    f.rect(150, 70, 300, 104, H.grad(f, "fy716-water", WATER_LIGHT, WATER))
    f.path("M138,60 V188 H462 V60 H450 V172 H150 V60 Z", IRON, INK, 2.5)
    f.line(126, 60, 150, 60, INK, 3); f.line(450, 60, 474, 60, INK, 3)
    # field lines (schematic): loops around the coil's two sides, through the glass into the pan bottom
    # closed loops around each side of the coil; the outermost runs through the pan bottom
    for w, h in ((52, 28), (80, 46), (108, 66)):
        for sgn in (1, -1):
            f.add(f'<ellipse cx="{n(cx + sgn * 118)}" cy="246" rx="{w}" ry="{h}" fill="none" stroke="{FIELD}" '
                  f'stroke-width="2"/>')
    f.add('<g>')
    # eddy currents in the pan bottom: opposite to the coil's current
    for x in (196, 232, 268):
        _coil_mark(f, 2 * cx - x, 180, False, r=6.5, fill=CURRENT)
        _coil_mark(f, x, 180, True, r=6.5, fill=CURRENT)
    f.add('</g>')
    # coil under the glass: copper turns, current out of the page on the right, into it on the left
    for x in (196, 222, 248, 274):
        _coil_mark(f, x, 250, False, r=9)
        _coil_mark(f, 2 * cx - x, 250, True, r=9)
    # energy flow from the hot bottom into the water
    for x in (230, 300, 370):
        f.block_arrow(x, 162, x, 112, H.grad(f, f"fy716-heat-{x}", HEAT_LIGHT, HEAT), shaft=12, head=26, headlen=20)
    # labels with leaders
    f.tex(470, 100, r"\text{vesi}", "start", color=INK)
    f.line(436, 100, 466, 100, MUTED, 1.5)
    f.tex(12, 120, r"\text{teräskattila}", "start")
    f.line(80, 136, 138, 160, MUTED, 1.5)
    f.tex(20, 300, r"\text{lasi}", "start")
    f.line(46, 286, 70, 218, MUTED, 1.5)
    f.tex(580, 300, r"\text{kela}", "end")
    f.line(540, 290, 413, 258, MUTED, 1.5)
    f.tex(588, 140, r"\text{pyörrevirta}", "end")
    f.line(500, 158, 412, 178, MUTED, 1.5)
    return f.svg()


def loss_graph():
    f = Fig("fy716-graph", 340, "Kuvaaja mittakaavassa: valokuidun läpi kulkevan valon teho prosentteina lähetetystä "
            "tehosta kuidun pituuden funktiona 0–25 kilometrin matkalla. Yhtenäinen käyrä on aallonpituudelle 1550 nm "
            "vaimennuksella 0,18 dB/km: teho laskee 25 kilometrissä 35 prosenttiin. Katkoviivakäyrä on aallonpituudelle "
            "1310 nm vaimennuksella 0,32 dB/km: teho laskee 16 prosenttiin. Katkoviivoilla on merkitty, että "
            "1550 nanometrin valon teho puolittuu 16,7 kilometrin matkalla.")
    ax = Axes(f, (96, 286), (430, 66), x=(0, 25), y=(0, 100), xticks=[5 * k for k in range(1, 6)],
              yticks=[20 * k for k in range(1, 6)], xlabel=r"L\ (\text{km})", ylabel=r"P : P_0\ (\%)")
    ax.curve(lambda L: 100 * 10 ** (-0.18 * L / 10), 0, 25, RAY, 3)
    ax.curve(lambda L: 100 * 10 ** (-0.32 * L / 10), 0, 25, RAY, 3, dash="9 6")
    Lh = 10 * math.log10(2) / 0.18
    ax.guide(Lh, 50)
    ax.point(Lh, 50, RAY)
    f.tex(ax.X(Lh) + 10, ax.Y(50) - 22, r"16{,}7\,\text{km}", "start", bg=True)
    f.tex(ax.X(25) + 10, ax.Y(100 * 10 ** (-0.18 * 2.5)), r"1550\,\text{nm}", "start", color=RAY)
    f.tex(ax.X(25) + 10, ax.Y(100 * 10 ** (-0.32 * 2.5)) - 6, r"1310\,\text{nm}", "start", color=RAY)
    return f.svg()


def charger_points():
    """Question-safe variant of charger: the same model with the phone at 3 mm and at 6 mm; no number of lines in the text."""
    f = Fig("fy716-charger-8", 380, "Periaatekuva langattomasta laturista sivulta leikattuna, kentän muoto laskettu: "
            "kaksi paneelia. Kummassakin alhaalla on latausalusta, jonka sisällä lähetinkäämi, ja sen yläpuolella "
            "puhelin, jonka pohjassa on samankokoinen vastaanotinkäämi. Lähetinkäämin vaihtovirta synnyttää "
            "magneettikentän, jonka vihreät kenttäviivat kiertävät käämin johtimien ympäri ja kulkevat käämin keskeltä "
            "ylöspäin. Kenttäviivat on piirretty yhtä suurin vuoaskelin, joten viivojen lukumäärä on verrannollinen "
            "vuohon. Vasemmalla puhelin on 3 millimetrin päässä ja oikealla 6 millimetrin päässä laturista. "
            "Vastaanotinkäämin kaksi johdinta näkyy puhelimen pohjassa kahtena kuparinvärisenä pisteenä, ja käämin läpi, "
            "pisteiden välistä, kulkevat viivat on piirretty tummempina ja paksumpina: ne lasketaan, ja niiden määrä on "
            "verrannollinen käämin läpi kulkevaan vuohon. Lähetinkäämin virta on kummassakin paneelissa sama.")
    _panel(f, 150, 3.0, "a", label=False)
    _panel(f, 450, 6.0, "b", label=False)
    f.line(300, 24, 300, 366, RULE, 1.5, "6 5")
    f.tex(150, 32, r"\text{puhelin}:\ z = 3\,\text{mm}", "middle", w=230)
    f.tex(450, 32, r"\text{puhelin}:\ z = 6\,\text{mm}", "middle", w=230)
    f.tex(150, 318, r"\text{laturi}", "middle", w=100)
    f.tex(450, 318, r"\text{laturi}", "middle", w=100)
    f.tex(8, 352, r"\text{lähetinkäämi}", "start")
    f.line(42, 340, 66, 270, MUTED, 1.5)
    f.tex(306, 62, r"\text{vastaanotinkäämi}", "start")
    f.line(330, 74, 366, 231, MUTED, 1.5)
    return f.svg()


def loss_curve():
    """The power curve of one fibre on a fine grid and with no marked points: a question-safe variant of graph."""
    f = Fig("fy716-curve", 340, "Kuvaaja mittakaavassa: valokuidun läpi kulkevan valon teho prosentteina lähetetystä "
            "tehosta kuidun pituuden funktiona 0–40 kilometrin matkalla. Käyrä laskee 100 prosentista ensin jyrkästi "
            "ja sitten loivemmin. Ruudukon pystyviivat ovat viiden kilometrin välein ja vaakaviivat kymmenen "
            "prosenttiyksikön välein. Kuvaajaan ei ole merkitty yhtään pistettä.")
    ax = Axes(f, (96, 286), (430, 66), x=(0, 40), y=(0, 100), xticks=[5 * k for k in range(1, 9)],
              yticks=[10 * k for k in range(1, 11)], xlabel=r"L\ (\text{km})", ylabel=r"P : P_0\ (\%)",
              xfmt=lambda v: fi(v) if round(v) % 10 == 0 else "", yfmt=lambda v: fi(v) if round(v) % 20 == 0 else "")
    ax.curve(lambda L: 100 * 10 ** (-0.30 * L / 10), 0, 40, RAY, 3)
    return f.svg()


def hero():
    """The opening illustration: a kitchen counter with an induction hob and a steel pot, a phone on a wireless
    charging pad and a fibre router on the wall with a glowing fibre end."""
    f = H.hero("fy716-hero", "Kuvitus: keittiön työtaso. Keskellä on musta induktioliesi, jonka keittoalueella on "
               "teräskattila ja kattilasta nousee höyryä. Oikealla puhelin lepää pyöreän langattoman laturin päällä. "
               "Vasemmalla seinällä on kuitureititin, johon tulee ohut valokaapeli, ja kaapelin pää hehkuu.")
    f.rect(0, 0, 1200, 600, H.grad(f, "fy716h-wall", PAPER, SAND_LIGHT))
    for k in range(5):
        f.line(0, 80 + 70 * k, 1200, 80 + 70 * k, RULE_LIGHT, 2)
    # counter
    f.rect(0, 430, 1200, 170, H.grad(f, "fy716h-counter", SAND_LIGHT, SAND))
    f.rect(0, 412, 1200, 24, SAND, INK, 3)
    # hob: black glass with two cooking zones
    f.rect(400, 392, 420, 22, INK, INK, 2, 6)
    for x in (500, 720):
        f.add(f'<ellipse cx="{x}" cy="403" rx="80" ry="8" fill="none" stroke="{MUTED}" stroke-width="2"/>')
    # steel pot on the left zone, steam
    f.path("M420,392 L432,270 H568 L580,392 Z", H.grad(f, "fy716h-pot", ALUMINIUM, IRON, horizontal=True), INK, 3)
    f.rect(412, 258, 176, 16, IRON, INK, 3, 6)
    f.line(400, 300, 432, 300, INK, 6); f.line(568, 300, 600, 300, INK, 6)
    for x in (465, 500, 535):
        f.path(f"M{x},248 q-14,-24 0,-48 t0,-48 t0,-48", stroke=WHITE, w=7, extra='stroke-linecap="round" stroke-opacity="0.85"')
    # charging pad and phone
    f.add(f'<ellipse cx="960" cy="404" rx="96" ry="14" fill="{ALUMINIUM}" stroke="{INK}" stroke-width="3"/>')
    f.add(f'<ellipse cx="960" cy="398" rx="80" ry="9" fill="{WHITE}" stroke="{INK}" stroke-width="2"/>')
    f.path("M876,392 L1048,392 L1060,376 L888,376 Z", INK, INK, 3)
    f.path("M890,378 L1042,378 L1050,368 L898,368 Z", COLD, INK, 2)
    for k in range(3):
        f.add(f'<ellipse cx="960" cy="404" rx="{112 + 22 * k}" ry="{20 + 6 * k}" fill="none" stroke="{GOOD}" '
              f'stroke-width="3" stroke-opacity="{0.6 - 0.18 * k:.2f}" stroke-dasharray="10 8"/>')
    # router on the wall with a fibre cable and a glowing end
    f.rect(130, 150, 170, 110, WHITE, INK, 3, 14)
    for k in range(4):
        f.circle(160 + 30 * k, 230, 7, GOOD if k < 3 else RAY)
    f.path("M215,150 C215,90 330,60 360,40", stroke=INK, w=6, extra='stroke-linecap="round"')
    f.path("M180,260 C180,330 60,360 40,430", stroke=RULE, w=6, extra='stroke-linecap="round"')
    f.defs_add(f'<radialGradient id="fy716h-glow"><stop offset="0" stop-color="{WHITE}"/><stop offset="0.35" '
               f'stop-color="{RAY}"/><stop offset="1" stop-color="{RAY}" stop-opacity="0"/></radialGradient>')
    f.circle(360, 40, 26, "url(#fy716h-glow)")
    return f.svg()


FIGURES = {"hero": hero, "charger": charger, "hob": hob, "graph": loss_graph,
           "charger-points": charger_points, "graph-curve": loss_curve}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "charger": "reveals: far fewer field lines thread the receiver at 20 mm than at 3 mm (coupling falls with distance)",
    "hob": "reveals: the coil's changing field induces eddy currents in the pan bottom, none in the glass",
    "graph": "reveals: fibre power against length at 0,18 and 0,32 dB/km, halving at 16,7 km for 1550 nm",
    "charger-points": "safe: the charger's field lines with the phone at 3 mm and 6 mm; REUSE of charger (no counts in the text), lines drawn at equal flux steps",
    "graph-curve": "safe: the power curve of one fibre on a fine grid, no marked points; REUSE of graph for reading P from L or L from P",
}
