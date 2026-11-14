"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy5-14` writes them into lesson.md.
Colours: wavefronts and pressure ink/muted, the air's particles water blue #2f74b5, velocity arrows blue #1971c2 (FY4),
spectrum peaks orange #e8590c, the two tones of a beat orange and violet #7048e8 with their sum water blue. Force red is
never used. Numbers of the task figures: lesson-answers.py."""
import math
from figlib import (Fig, Axes, INK, MUTED, WHITE, RULE, RULE_LIGHT, GLASS, WATER_LIGHT, WATER, SAND_LIGHT, SAND, SAND_DARK,
                    GRAIN, HEAT, HEAT_LIGHT, COLD, COLD_LIGHT, ALUMINIUM, METAL_EDGE, IRON, ICE, GOOD, GOOD_LIGHT, PAPER, n)
import herolib as H

VEL, PEAK, VIOLET = COLD, HEAT, "#7048e8"


def poly(f, pts, color, w=3, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    p = " ".join(f"{n(x)},{n(y)}" for x, y in pts)
    return f.add(f'<polyline points="{p}" fill="none" stroke="{color}" stroke-width="{w:g}" stroke-linejoin="round" stroke-linecap="round"{d}/>')


def bracket(f, a, b, y, lab, up=False):
    s = -1 if up else 1
    f.path(f"M{n(a)},{n(y - 8 * s)} V{n(y)} H{n(b)} V{n(y - 8 * s)}", stroke=INK, w=2)
    f.tex((a + b) / 2, y + 20 * s, lab, "middle")


def person(f, x, yf, sc=1.0, coat=IRON):
    """A small standing person seen from the side: feet on yf."""
    s = sc
    f.line(x, yf - 26 * s, x - 7 * s, yf, INK, 3 * s); f.line(x, yf - 26 * s, x + 7 * s, yf, INK, 3 * s)
    f.rect(x - 9 * s, yf - 54 * s, 18 * s, 30 * s, coat, INK, 2, 5 * s)
    f.circle(x, yf - 64 * s, 9 * s, SAND_LIGHT, INK, 2)


def speaker(f, x, y, sc=1.0):
    """A loudspeaker facing right, its cone at (x, y)."""
    s = sc
    f.rect(x - 22 * s, y - 12 * s, 12 * s, 24 * s, INK, rx=2)
    f.path(f"M{n(x - 10 * s)},{n(y - 12 * s)} L{n(x + 6 * s)},{n(y - 26 * s)} V{n(y + 26 * s)} L{n(x - 10 * s)},{n(y + 12 * s)} Z", METAL_EDGE, INK, 2)


# --- Ydinajatus: sound as a longitudinal pressure wave --------------------------------------------------------------
def longitudinal():
    f = Fig("fy514-long", 356, "Kaavakuva, ei mittakaavassa. Ylhäällä vasemmalla kaiutin, jonka edessä on ilmaa putkessa. Ilman "
            "hiukkaset on piirretty sinisinä pisteinä, ja ne ovat paikoin tiheässä ja paikoin harvassa: tiheät kohdat ovat "
            "tihentymiä ja harvat harvennuksia. Hiukkaset värähtelevät edestakaisin aallon etenemissuunnassa, mitä esittää "
            "pieni kaksipäinen nuoli, ja aalto etenee oikealle, mitä esittää sininen nuoli. Alhaalla on saman hetken paine "
            "paikan funktiona: käyrä vaihtelee normaalin ilmanpaineen p0 molemmin puolin, ja sen huiput ovat tihentymien "
            "kohdalla. Kahden vierekkäisen tihentymän etäisyys on aallonpituus lambda.")
    x0, x1, yc, hh = 86, 556, 104, 34
    lam, A = 188.0, 9.0
    xc = x0 + 0.25 * lam                                         # a compression at x0 + λ/4 + m λ
    disp = lambda x: -A * math.sin(2 * math.pi * (x - xc) / lam)  # displacement: particles crowd at xc
    f.rect(x0, yc - hh, x1 - x0, 2 * hh, GLASS)
    i = 0
    x = x0 + 4
    while x < x1 - 2:
        xx = min(max(x + disp(x), x0 + 3), x1 - 3)
        for r in range(4):
            yy = yc - hh + 2 * hh * (r + 0.5 + (0.25 if i % 2 else -0.25)) / 4
            f.circle(xx, yy, 3.6, WATER)
        x += 9.4; i += 1
    f.line(x0, yc - hh, x1, yc - hh, INK, 3); f.line(x0, yc + hh, x1, yc + hh, INK, 3)
    speaker(f, x0 - 14, yc, 1.3)
    for m in range(3):
        xm = xc + m * lam
        if xm < x1 - 20: f.tex(xm, yc - hh - 22, r"\text{tihentymä}", "middle")
    xr = xc + lam / 2
    f.tex(xr, yc + hh + 22, r"\text{harvennus}", "middle")
    # particle oscillation and propagation
    f.arrow(xr + lam / 2 + 6, yc + hh + 22, xr + lam / 2 - 22, yc + hh + 22, INK, 2, 10)
    f.arrow(xr + lam / 2 - 16, yc + hh + 22, xr + lam / 2 + 12, yc + hh + 22, INK, 2, 10)
    f.arrow(xr + lam + 40, yc + hh + 22, xr + lam + 104, yc + hh + 22, VEL, 3, 14)
    f.tex(xr + lam + 72, yc + hh + 50, r"\text{eteneminen}", "middle")
    # pressure graph
    gy, ga = 262, 46
    f.arrow(x0 - 1, gy, x1 + 22, gy, INK, 2.5, 13)
    f.arrow(x0, gy + ga + 18, x0, gy - ga - 24, INK, 2.5, 13)
    f.line(x0, gy, x1, gy, RULE, 1.5, "6 5")
    pts = [(x, gy - ga * math.cos(2 * math.pi * (x - xc) / lam)) for x in [x0 + (x1 - x0) * k / 160 for k in range(161)]]
    poly(f, pts, INK, 3)
    f.tex(x0 - 10, gy - ga - 38, "p", "end")
    f.tex(x0 - 10, gy, "p_0", "end")
    f.tex(x1 + 28, gy, "x", "start")
    for m in range(2):
        f.line(xc + m * lam, gy - ga - 4, xc + m * lam, yc + hh + 4, MUTED, 1.5, "3 4")
    bracket(f, xc, xc + lam, gy + ga + 16, r"\lambda")
    return f.svg()


def ranges():
    f = Fig("fy514-ranges", 300, "Kaavakuva: taajuusasteikko logaritmisena yhdestä hertsistä kymmeneen miljoonaan hertsiin, jokainen "
            "kymmenkertaistus yhtä pitkänä välinä. Alle 20 hertsin taajuudet ovat infraääntä, 20 hertsistä 20 kilohertsiin on "
            "ihmisen kuuloalue ja yli 20 kilohertsin taajuudet ovat ultraääntä. Asteikon yläpuolelle on merkitty esimerkkejä: "
            "maanjäristys noin yhden hertsin kohdalla, norsujen matalat äänet noin 15 hertsin kohdalla, puhe muutamasta sadasta "
            "hertsistä muutamaan kilohertsiin, lepakon kaikuluotaus noin 50 kilohertsin kohdalla ja ultraäänikuvaus noin kolmen "
            "megahertsin kohdalla.")
    x0, dec, ya = 36, 64, 196
    X = lambda fr: x0 + dec * math.log10(fr)
    bands = ((1, 20, ICE), (20, 2e4, GOOD_LIGHT), (2e4, 1e7, COLD_LIGHT))
    for a, b, col in bands: f.rect(X(a), ya - 30, X(b) - X(a), 30, col, INK, 1.5)
    f.arrow(x0 - 1, ya, X(1e7) + 24, ya, INK, 2.5, 13)
    for k in range(8):
        f.line(X(10 ** k), ya, X(10 ** k), ya + 7, INK, 2)
        f.tex(X(10 ** k), ya + 24, "1" if k == 0 else "10" if k == 1 else f"10^{k}", "middle")
    f.tex(X(1e7) + 30, ya, r"f\ (\text{Hz})", "start")
    f.tex((X(1) + X(20)) / 2, ya + 60, r"\text{infraääni}", "middle")
    f.tex((X(20) + X(2e4)) / 2, ya + 60, r"\text{kuuloalue}", "middle")
    f.tex((X(2e4) + X(1e7)) / 2, ya + 60, r"\text{ultraääni}", "middle")
    for fr, lab in ((20, r"20\,\text{Hz}"), (2e4, r"20\,\text{kHz}")):
        f.line(X(fr), ya - 30, X(fr), ya - 44, INK, 2)
        f.tex(X(fr), ya - 56, lab, "middle")
    marks = ((1, r"\text{maanjäristys}", 34, "start", 30), (15, r"\text{norsu}", 82, "middle", None),
             (1200, r"\text{puhe}", 34, "middle", None), (5e4, r"\text{lepakko}", 82, "middle", None),
             (3e6, r"\text{ultraäänikuvaus}", 34, "end", 572))
    for fr, lab, y, anc, xl in marks:
        f.line(X(fr), y + 14, X(fr), ya - 32, MUTED, 1.5, "3 4")
        f.circle(X(fr), ya - 15, 5, INK, WHITE, 1.5)
        f.tex(xl if xl is not None else X(fr), y, lab, anc)
    return f.svg()


def timbre():
    f = Fig("fy514-timbre", 372, "Kaavakuva kahdesta äänestä, joilla on sama perustaajuus 220 hertsiä. Ylhäällä äänirauta, alhaalla "
            "kitara. Vasemmalla paine ajan funktiona: ääniraudan käyrä on siniaalto, kitaran käyrä on mutkikkaampi, mutta "
            "kummankin käyrän jaksonaika T on sama. Oikealla kummankin äänen spektri eli FFT-kuvaaja: äänirauralla on yksi "
            "piikki 220 hertsin kohdalla, kitaralla piikit 220, 440, 660, 880 ja 1100 hertsin kohdalla eli perustaajuuden "
            "monikerroilla, ja piikit pienenevät taajuuden kasvaessa.")
    amps = ((1.0,), (1.0, 0.62, 0.42, 0.24, 0.14))
    phase = (0, 0.6, 1.3, 2.1, 0.4)
    f.tex(200, 22, r"p(t)", "middle")
    f.tex(425, 22, r"\text{spektri}", "middle")
    for row, (yc, name) in enumerate(((116, r"\text{äänirauta}"), (288, r"\text{kitara}"))):
        a = amps[row]
        f.tex(16, yc - 70, name, "start")
        # waveform, three periods
        wx0, wx1, amp = 100, 300, 34
        f.arrow(wx0 - 1, yc, wx1 + 18, yc, INK, 2, 11)
        f.arrow(wx0, yc + amp + 10, wx0, yc - amp - 16, INK, 2, 11)
        f.tex(wx1 + 22, yc, "t", "start")
        norm = max(abs(sum(ak * math.sin(2 * math.pi * (k + 1) * u + phase[k]) for k, ak in enumerate(a))) for u in [i / 400 for i in range(401)])
        pts = []
        for i in range(301):
            u = 3 * i / 300
            y = sum(ak * math.sin(2 * math.pi * (k + 1) * u + phase[k]) for k, ak in enumerate(a)) / norm
            pts.append((wx0 + (wx1 - wx0 - 10) * i / 300, yc - amp * y))
        poly(f, pts, INK, 2.5)
        per = (wx1 - wx0 - 10) / 3
        f.line(wx0 + per, yc + amp + 4, wx0 + per, yc + amp + 14, MUTED, 1.5)
        f.line(wx0 + 2 * per, yc + amp + 4, wx0 + 2 * per, yc + amp + 14, MUTED, 1.5)
        f.path(f"M{n(wx0 + per)},{n(yc + amp + 18)} H{n(wx0 + 2 * per)}", stroke=INK, w=2)
        f.tex(wx0 + 1.5 * per, yc + amp + 34, "T", "middle")
        # spectrum
        sx0, sx1, sh = 350, 500, 70
        X = lambda fr: sx0 + fr / 1200 * (sx1 - sx0)
        base = yc + 34
        for t in (500, 1000):
            f.line(X(t), base, X(t), base - sh, RULE_LIGHT, 1.5)
        f.arrow(sx0 - 1, base, sx1 + 14, base, INK, 2, 11)
        f.arrow(sx0, base + 1, sx0, base - sh - 16, INK, 2, 11)
        for k, ak in enumerate(a):
            fr = 220 * (k + 1)
            f.rect(X(fr) - 3, base - sh * ak, 6, sh * ak, PEAK)
        for t in (500, 1000):
            f.line(X(t), base, X(t), base + 6, INK, 2)
            f.tex(X(t), base + 24, str(t), "middle")
        f.tex(sx1 + 18, base, r"f\ (\text{Hz})", "start")
    f.line(12, 196, 588, 196, RULE, 2, "6 6")
    return f.svg()


# --- Kaava: beats and the Doppler effect ------------------------------------------------------------------------------
def beats():
    f = Fig("fy514-beats", 336, "Kaavakuva, ei mittakaavassa: kaksi ääntä, joiden taajuudet f1 ja f2 eroavat vähän, ja niiden summa ajan "
            "funktiona. Ylhäällä oranssi aalto ja sen alla violetti aalto, jossa on kuvan aikana kaksi värähdystä enemmän. "
            "Alhaalla sininen summa-aalto: sen amplitudi kasvaa ja pienenee vuorotellen katkoviivalla piirretyn verhokäyrän "
            "mukaan. Kohdissa, joissa aallot ovat samassa vaiheessa, summa on voimakas, ja kohdissa, joissa ne ovat vastakkaisissa "
            "vaiheissa, summa on lähes nolla. Kahden peräkkäisen voimakkaan kohdan väli on huojunnan jaksonaika T H.")
    x0, x1 = 124, 560
    W = x1 - x0
    c1, c2 = 12, 14
    def wave(yc, amp, fn, col, w):
        poly(f, [(x0 + W * i / 600, yc - amp * fn(i / 600)) for i in range(601)], col, w)
    for yc, cyc, col, lab in ((44, c1, PEAK, "f_1"), (110, c2, VIOLET, "f_2")):
        f.line(x0, yc, x1, yc, RULE, 1.5, "4 5")
        wave(yc, 20, lambda u, cyc=cyc: math.cos(2 * math.pi * cyc * u), col, 2.5)
        f.tex(x0 - 14, yc, lab, "end")
    yc, amp = 228, 40
    f.line(x0, yc, x1, yc, RULE, 1.5, "4 5")
    env = lambda u: abs(math.cos(math.pi * (c2 - c1) * u))
    poly(f, [(x0 + W * i / 300, yc - amp * env(i / 300)) for i in range(301)], MUTED, 1.5, "6 5")
    poly(f, [(x0 + W * i / 300, yc + amp * env(i / 300)) for i in range(301)], MUTED, 1.5, "6 5")
    wave(yc, amp / 2, lambda u: math.cos(2 * math.pi * c1 * u) + math.cos(2 * math.pi * c2 * u), WATER, 3)
    f.tex(x0 - 14, yc, r"\text{summa}", "end")
    f.arrow(x0 - 1, 300, x1 + 20, 300, INK, 2, 11)
    f.tex(x1 + 26, 300, "t", "start")
    for u in (0, 0.5):
        f.line(x0 + W * u, yc - amp - 4, x0 + W * u, 286, MUTED, 1.5, "3 4")
    f.path(f"M{n(x0)},{n(282)} V{n(290)} H{n(x0 + W / 2)} V{n(282)}", stroke=INK, w=2)
    f.tex(x0 + W / 4, 316, r"T_\text{H}", "middle", bg=True)
    return f.svg()


def doppler():
    f = Fig("fy514-doppler", 424, "Kaavakuva ylhäältä katsottuna, kaksi tilannetta allekkain. Ylhäällä lähde liikkuu oikealle nopeudella, "
            "joka on 0,4 kertaa äänen nopeus, mitä esittää sininen nopeusnuoli. Aaltorintamat ovat ympyröitä, jotka ovat "
            "lähteneet lähteen aiemmista paikoista, joten ne ovat lähteen edessä tiheässä ja sen takana harvassa. Oikealla "
            "olevan kuulijan A suunnassa aallonpituus lambda A on lyhyt ja vasemmalla olevan kuulijan B suunnassa aallonpituus "
            "lambda B pitkä. Alhaalla lähde on paikallaan ja aaltorintamat ovat samankeskisiä ympyröitä yhtä suurin välein. "
            "Kuulija liikkuu vasemmalle kohti lähdettä, mitä esittää sininen nopeusnuoli; aallonpituus lambda on sama "
            "kaikkiin suuntiin.")
    vT, vsT = 46.0, 18.4
    f.defs_add('<clipPath id="fy514-clip1"><rect x="66" y="34" width="478" height="140"/></clipPath>'
               '<clipPath id="fy514-clip2"><rect x="26" y="262" width="548" height="118"/></clipPath>')   # below the panel's title
    # top: moving source
    xs, ys = 300, 120
    g = []
    for m in range(1, 7):
        cx, r = xs - m * vsT, m * vT
        g.append(f'<circle cx="{n(cx)}" cy="{ys}" r="{n(r)}" fill="none" stroke="{MUTED}" stroke-width="2"/>')
    f.add(f'<g clip-path="url(#fy514-clip1)">{"".join(g)}</g>')
    speaker(f, xs, ys, 0.9)
    f.arrow(xs + 14, ys - 40, xs + 76, ys - 40, VEL, 3, 14)
    f.tex(xs + 84, ys - 40, r"\overline{v}_\text{L}", "start", color=VEL)
    H.person(f, 566, ys + 34, IRON, INK, 0.2); f.tex(566, 160 + 8, r"\text{A}", "middle")   # drawn people as in the lessons
    H.person(f, 34, ys + 34, IRON, INK, 0.2); f.tex(34, 160 + 8, r"\text{B}", "middle")
    ra = [xs - m * vsT + m * vT for m in (2, 3)]
    rb = [xs - m * vsT - m * vT for m in (2, 3)]
    bracket(f, ra[0], ra[1], 184, r"\lambda_\text{A}")
    bracket(f, rb[1], rb[0], 184, r"\lambda_\text{B}")
    f.line(12, 220, 588, 220, RULE, 2, "6 6")
    # bottom: moving listener
    xs2, ys2 = 230, 316
    g = [f'<circle cx="{xs2}" cy="{ys2}" r="{n(m * vT)}" fill="none" stroke="{MUTED}" stroke-width="2"/>' for m in range(1, 8)]
    f.add(f'<g clip-path="url(#fy514-clip2)">{"".join(g)}</g>')
    speaker(f, xs2, ys2, 0.9)
    xl = 483                                                      # between two wavefronts
    H.person(f, xl, ys2 + 34, IRON, INK, 0.2)
    f.arrow(xl - 14, ys2 - 50, xl - 76, ys2 - 50, VEL, 3, 14)
    f.tex(xl - 84, ys2 - 50, r"\overline{v}_\text{H}", "end", color=VEL)
    bracket(f, xs2 + 3 * vT, xs2 + 4 * vT, 384, r"\lambda", up=False)
    f.tex(16, 18, r"\text{lähde liikkuu}", "start", bg=True)
    f.tex(16, 240, r"\text{kuulija liikkuu}", "start", bg=True)
    return f.svg()


# --- task figures (inquiry.json) ----------------------------------------------------------------------------------------
def spectrum_task():
    """The spectrum of an unknown tone: peaks at 200, 400, 600, 800 and 1000 Hz, the strongest at 400 Hz (lesson-answers
    spektri-*). No fundamental is written: the student reads it."""
    f = Fig("fy514-spek", 330, "Kuvaaja: äänen FFT-spektri. Vaaka-akselilla taajuus f hertseinä nollasta 1200 hertsiin, apuviivat "
            "sadan hertsin välein ja lukuarvot kahdensadan hertsin välein. Pystyakselilla piikin suhteellinen korkeus nollasta "
            "yhteen. Spektrissä on viisi kapeaa piikkiä 200, 400, 600, 800 ja 1000 hertsin kohdalla. Piikkien korkeudet ovat "
            "noin 0,6, 1,0, 0,45, 0,3 ja 0,15; korkein piikki on 400 hertsin kohdalla.")
    ax = Axes(f, (96, 280), (480, 52), x=(0, 1200), y=(0, 1.0), xticks=[100 * k for k in range(1, 13)], yticks=[0.25, 0.5, 0.75, 1.0],
              xlabel=r"f\ (\text{Hz})", ylabel=r"\text{korkeus}", xfmt=lambda v: (str(int(v)) if v % 200 == 0 and v < 1200 else ""),
              yfmt=lambda v: ("0{,}5" if v == 0.5 else "1" if v == 1.0 else ""))
    heights = (0.6, 1.0, 0.45, 0.3, 0.15)
    def spec(x):
        return sum(h * math.exp(-((x - 200 * (k + 1)) / 9.0) ** 2) for k, h in enumerate(heights)) + 0.012
    ax.curve(spec, 0, 1200, PEAK, 3, steps=600)
    return f.svg()


def beats_task():
    """A recording of two tuning forks, 440 Hz and 444 Hz, over 1,0 s: the vibration is too dense to draw one by one,
    so the band between the envelope ±2A|cos(π Δf t)| is filled (lesson-answers huojunta-*). Loud moments 0,25 s apart."""
    f = Fig("fy514-huoj", 300, "Kuvaaja: kahden yhtä aikaa soivan ääniraudan yhteinen ääni mikrofonilla mitattuna, paine ajan funktiona "
            "nollasta yhteen sekuntiin. Aika-akselilla apuviivat 0,1 sekunnin välein ja lukuarvot 0,2 sekunnin välein. Värähtely on niin tiheää, "
            "että se näkyy täytettynä sinisenä alueena. Alueen leveys vaihtelee: se on suurimmillaan hetkillä 0, 0,25, 0,50, "
            "0,75 ja 1,00 sekuntia ja kapenee lähes nollaan näiden puolivälissä.")
    ax = Axes(f, (80, 262), (480, 64), x=(0, 1.0), y=(-1.2, 1.2), xticks=[0.1 * k for k in range(1, 11)], yticks=[],
              xlabel=r"t\ (\text{s})", ylabel=r"p",
              xfmt=lambda v: ("0{,}" + str(round(v * 10)) if round(v * 10) < 10 else "1{,}0") if round(v * 10) % 2 == 0 else "")
    f.line(ax.x0, ax.Y(0), ax.x1, ax.Y(0), RULE, 1.5, "6 5")
    env = lambda t: abs(math.cos(math.pi * 4 * t))
    up = [(i / 400, env(i / 400)) for i in range(401)]
    ax.area(up + [(t, -e) for t, e in up[::-1]], WATER, 0.55)
    ax.line(up, WATER, 2); ax.line([(t, -e) for t, e in up], WATER, 2)
    return f.svg()


def hero():
    """The chapter's opening illustration: an ambulance with its siren on passes a pedestrian at a crossing."""
    f = H.hero("fy514-hero", "Kuvitus: kaupungin katu kesäpäivänä. Valkoinen ambulanssi, jonka katolla palaa sininen hälytysvalo, "
               "ajaa kadulla vasemmalta oikealle. Sireenistä leviää ääni kaarina, jotka ovat auton edessä tiheässä ja sen takana "
               "harvassa. Oikealla jalkakäytävällä suojatien vieressä seisoo jalankulkija, jonka ohi "
               "ambulanssi on juuri ajamassa. Taustalla on taloja ja koivu.")
    H.sky(f, "fy514h", 420)
    H.cloud(f, 220, 110, 0.8); H.cloud(f, 860, 80, 0.6)
    H.house(f, 60, 420, 220, 170, SAND_LIGHT, IRON, GLASS)
    H.house(f, 760, 420, 260, 190, ALUMINIUM, METAL_EDGE, GLASS)
    H.birch(f, 380, 420, 230)
    H.birch(f, 1110, 420, 200)
    # pavement, kerb, road with a zebra crossing
    f.rect(0, 420, 1200, 40, SAND_LIGHT); f.line(0, 460, 1200, 460, GRAIN, 4)
    f.rect(0, 462, 1200, 138, IRON)
    for k in range(6): f.rect(860 + 0 * k, 476 + 20 * k, 140, 10, WHITE, extra='fill-opacity="0.9"')
    for k in range(8): f.rect(40 + 150 * k, 586, 80, 6, WHITE, extra='fill-opacity="0.8"')
    # the siren's wavefronts: each crest left the siren from an earlier place (the van moves right at 0,4 times the
    # speed of sound, as in the doppler figure), so they crowd in front of the van and spread out behind it
    sx, sy, lam, vs = 360 + 155, 568 - 196, 100.0, 40.0   # the siren on the van's roof (x, yb below)
    f.defs_add('<clipPath id="fy514h-clip"><rect x="0" y="0" width="1200" height="458"/></clipPath>')
    rings = [f'<circle cx="{n(sx - m * vs)}" cy="{sy}" r="{n(m * lam)}" fill="none" stroke="{COLD}" stroke-width="5" '
             f'stroke-opacity="{n(0.6 - 0.05 * m)}"/>' for m in range(1, 9)]
    f.add('<g clip-path="url(#fy514h-clip)">' + "".join(rings) + "</g>")
    # ambulance
    x, yb = 360, 568
    f.path(f"M{x},{yb} V{yb - 150} Q{x},{yb - 168} {x + 18},{yb - 168} H{x + 300} L{x + 360},{yb - 110} Q{x + 380},{yb - 100} {x + 380},{yb - 80} V{yb} Z",
           WHITE, INK, 4)
    f.rect(x + 4, yb - 70, 372, 22, HEAT_LIGHT)
    f.path(f"M{x + 306},{yb - 156} L{x + 352},{yb - 108} H{x + 306} Z", GLASS, INK, 3)
    f.rect(x + 40, yb - 140, 90, 52, GLASS, INK, 3, 4)
    f.rect(x + 160, yb - 140, 90, 52, GLASS, INK, 3, 4)
    f.rect(x + 196, yb - 60, 18, 46, COLD, extra='fill-opacity="0.9"'); f.rect(x + 182, yb - 44, 46, 16, COLD, extra='fill-opacity="0.9"')
    f.rect(x + 120, yb - 190, 70, 22, COLD, INK, 3, 6)
    f.add(f'<circle cx="{x + 155}" cy="{yb - 196}" r="34" fill="{COLD_LIGHT}" fill-opacity="0.55"/>')
    for wx in (x + 80, x + 300):
        f.circle(wx, yb, 34, INK); f.circle(wx, yb, 15, ALUMINIUM, INK, 2)
    f.rect(x + 368, yb - 40, 18, 14, HEAT_LIGHT, INK, 2, 3)
    # pedestrian on the pavement, facing the street
    H.walker(f, 1010, 452, COLD, INK, 0.72, stride=0.4)
    return f.svg()


FIGURES = {"hero": hero, "pitkittainen": longitudinal, "alueet": ranges, "sointi": timbre, "huojunta": beats,
           "doppler": doppler, "spektri-tehtava": spectrum_task, "huojunta-tehtava": beats_task}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "pitkittainen": "reveals: sound is a longitudinal pressure wave, compressions λ apart, pressure maxima at compressions",
    "alueet": "reveals: infrasound below 20 Hz, hearing 20 Hz–20 kHz, ultrasound above 20 kHz, with examples",
    "sointi": "reveals: same fundamental, different overtones; a harmonic spectrum at multiples of 220 Hz",
    "huojunta": "reveals: the sum of two close frequencies swells and fades with the period T_H",
    "doppler": "reveals: wavefronts crowd ahead of a moving source; a moving listener sees the same λ",
    "spektri-tehtava": "safe: an FFT spectrum with peaks at 200…1000 Hz, the strongest at 400 Hz; no fundamental written",
    "huojunta-tehtava": "safe: an envelope of two forks over 0–1,0 s, loud moments every 0,25 s; no frequencies written",
}
