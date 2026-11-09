"""Figures of the LUMA-tutor workshops (scripts/figlib.py), drawn when scripts/lumatutor.py builds a workshop page, in
the page's language (content/<lang>/lumatutor/figures.json, {Finnish text: translation}). The two climate graphs are
drawn from lessons/lumatutor/ilmastodata.json, so the figure and the answers in the tutor's part come from the same
stored measurements; nothing is typed in by hand."""
import json, math, pathlib
from figlib import Fig, Axes, INK, MUTED, WHITE, RULE, HOT, COLD, GLASS, METAL_EDGE, n, fi

DATA = json.loads((pathlib.Path(__file__).resolve().parent / "ilmastodata.json").read_text())
CUR = "#7048e8"      # conventional current, violet as in FY6
FORCE = "#c92a2a"    # force red (teacher: force, velocity and acceleration always in their own colours)
CO2_LINE = "#2f74b5"
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ"


def decades(series, first=1880):
    """[(decade's first year, mean, number of years)] of a [[year, value]] series, from `first` on."""
    out = {}
    for y, v in series:
        if y >= first: out.setdefault(y // 10 * 10, []).append(v)
    return [(d, sum(v) / len(v), len(v)) for d, v in sorted(out.items())]


def y_break(f, x, y):
    """Two short slanted strokes on the y axis just above the origin: the axis does not start at zero."""
    f.rect(x - 9, y - 22, 18, 10, WHITE)
    for dy in (-22, -12):
        f.line(x - 9, y + dy + 4, x + 9, y + dy - 4, INK, 2)


def co2():
    s = DATA["co2"]["series"]; y0, y1 = s[0][0], s[-1][0]
    f = Fig("lt-co2", 380, f"Kuvaaja: hiilidioksidin vuosikeskiarvo Mauna Loalla vuosina {y0}–{y1} miljoonasosina (ppm). "
            "Vaaka-akselilla on vuosi, pystyakselilla pitoisuus, ja pystyakseli alkaa arvosta 300 ppm. Käyrä nousee koko ajan "
            "ja jyrkkenee loppua kohti. Arvot voi lukea kuvaajasta, ja ne ovat myös ladattavassa aineistossa.")
    ax = Axes(f, (96, 320), (500, 50), x=(1955, 2030), y=(300, 440), xticks=[1960, 1980, 2000, 2020], yticks=[300, 320, 340, 360, 380, 400, 420, 440],
              xlabel=r"\text{vuosi}", ylabel=r"\mathrm{CO_2}\ (\text{ppm})", origin_label=False, xfmt=lambda v: str(int(v)))
    f.tex(96 - 12, 320, "300", "end")
    y_break(f, 96, 320)
    ax.line([(y, v) for y, v in s], CO2_LINE, 3.5)
    return f.svg()


def lampotila():
    s = DATA["temp"]["series"]; y0, y1 = s[0][0], s[-1][0]
    f = Fig("lt-lampotila", 400, f"Kuvaaja: maapallon keskilämpötilan poikkeama vuosien 1951–1980 keskiarvosta vuosina {y0}–{y1} "
            "(NASA GISTEMP v4). Jokainen vuosi on pylväs: punainen pylväs on vertailujaksoa lämpimämpi vuosi, sininen kylmempi. "
            "Musta vaakaviiva on kunkin vuosikymmenen keskiarvo. Pylväät vaihtelevat vuodesta toiseen, mutta vuosikymmenten "
            "keskiarvot nousevat 1970-luvulta alkaen joka vuosikymmen.")
    ax = Axes(f, (96, 340), (500, 60), x=(1875, 2030), y=(-0.6, 1.4), xticks=[1880, 1920, 1960, 2000], yticks=[-0.6, -0.3, 0, 0.3, 0.6, 0.9, 1.2],
              xlabel=r"\text{vuosi}", ylabel=r"\Delta T\ (^\circ\text{C})", origin_label=False, xfmt=lambda v: str(int(v)), yfmt=lambda v: fi(v, 1))
    f.tex(96 - 12, 340, fi(-0.6, 1), "end")
    w = (ax.X(1) - ax.X(0)) * 0.78
    for y, v in s:
        top, bot = (ax.Y(v), ax.Y(0)) if v >= 0 else (ax.Y(0), ax.Y(v))
        f.rect(ax.X(y) - w / 2, top, w, max(bot - top, 0.5), HOT if v >= 0 else COLD)
    f.line(96, ax.Y(0), 500, ax.Y(0), INK, 1.5)
    for d, m, k in decades(s):
        ax.line([(d - 0.4, m), (d + k - 0.6, m)], INK, 3.5)
    f.line(112, 80, 140, 80, INK, 3.5); f.tex(148, 80, r"\text{vuosikymmenen keskiarvo}", size=20)
    f.rect(117, 102, 7, 18, HOT); f.rect(128, 108, 7, 12, COLD); f.tex(148, 111, r"\text{yksittäinen vuosi}", size=20)
    return f.svg()


def _battery(f, x, y):
    """A cell on a vertical wire at x, centred on y, the positive (long) plate on top."""
    f.rect(x - 24, y - 12, 48, 24, WHITE)
    f.line(x - 22, y - 7, x + 22, y - 7, INK, 3)
    f.line(x - 11, y + 7, x + 11, y + 7, INK, 6)
    f.tex(x - 30, y - 18, "+", "end", size=22); f.tex(x - 30, y + 18, "-", "end", size=22)


def _lamp(f, x, y, lit):
    if lit:
        for a in range(0, 360, 45):
            r = math.radians(a)
            f.line(x + 24 * math.cos(r), y + 24 * math.sin(r), x + 34 * math.cos(r), y + 34 * math.sin(r), "#f59f00", 3, cap="round")
    f.circle(x, y, 16, "#fff3bf" if lit else WHITE, INK, 2.5)
    d = 16 / math.sqrt(2)
    f.line(x - d, y - d, x + d, y + d, INK, 2.5); f.line(x - d, y + d, x + d, y - d, INK, 2.5)


def _head(f, x, y, d):
    s = 9
    pts = {"r": [(x + s, y), (x - s, y - s * 0.8), (x - s, y + s * 0.8)], "l": [(x - s, y), (x + s, y - s * 0.8), (x + s, y + s * 0.8)]}[d]
    f.path("M" + " L".join(f"{n(a)},{n(b)}" for a, b in pts) + " Z", CUR)


def _circuit(f, x0, closed, title):
    x1, top, bot = x0 + 210, 90, 240
    ym = (top + bot) / 2
    sw0, sw1 = x0 + 80, x0 + 130
    f.add(f'<polyline points="{n(sw0)},{top} {n(x0)},{top} {n(x0)},{bot} {n(x1)},{bot} {n(x1)},{top} {n(sw1)},{top}" fill="none" stroke="{INK}" stroke-width="3" stroke-linejoin="round"/>')
    _battery(f, x0, ym)
    _lamp(f, x1, ym, closed)
    f.circle(sw0, top, 5, WHITE, INK, 2.5); f.circle(sw1, top, 5, WHITE, INK, 2.5)
    if closed: f.line(sw0 + 4, top, sw1 - 4, top, INK, 3)
    else: f.line(sw0 + 4, top - 2, sw1 - 6, top - 28, INK, 3)
    f.tex((x0 + x1) / 2, top - 52 if not closed else top - 36, r"\text{kytkin}", "middle", size=20)
    f.tex(x1 - 40, ym, r"\text{lamppu}", "end", size=20)
    f.tex((x0 + x1) / 2, 290, title, "middle", size=22)
    if closed:
        _head(f, x0 + 40, top, "r"); _head(f, x0 + 165, top, "r"); _head(f, (x0 + x1) / 2, bot, "l")
        f.tex((x0 + x1) / 2, bot - 22, "I", "middle", CUR)


def virtapiiri():
    f = Fig("lt-virtapiiri", 320, "Kaksi virtapiiriä piirrosmerkein. Kummassakin on paristo vasemmalla, plusnapa ylhäällä, "
            "kytkin ylhäällä ja lamppu oikealla. Vasemmassa kuvassa kytkin on kiinni, piiri on suljettu ja lamppu palaa. Violetit "
            "nuolet näyttävät virran I kulkevan plusnavalta kytkimen ja lampun kautta miinusnavalle. Oikeassa kuvassa kytkin on auki, "
            "piiri on avoin, virtaa ei kulje ja lamppu on sammunut.")
    _circuit(f, 50, True, r"\text{suljettu virtapiiri}")
    _circuit(f, 360, False, r"\text{avoin virtapiiri}")
    return f.svg()


def paperisilta():
    f = Fig("lt-paperisilta", 400, "Ylhäällä sivukuva: kaksi kirjapinoa, joiden välissä on 20 senttimetrin rako, ja niiden "
            "päällä taitettu paperisilta. Sillan keskellä on muki, ja punainen nuoli osoittaa alaspäin: kolikoiden paino painaa "
            "siltaa. Alhaalla kolme poikkileikkausta samasta paperimäärästä: litteä paperi on matala ja taipuu helposti, "
            "haitariksi taitettu ja kouruksi taitettu paperi ovat korkeampia ja kantavat enemmän.")
    for x in (70, 400):
        f.rect(x, 120, 130, 90, "#e9c98a", INK, 2.5, rx=4)
        f.line(x, 150, x + 130, 150, INK, 1.5); f.line(x, 180, x + 130, 180, INK, 1.5)
    f.rect(150, 108, 330, 12, WHITE, INK, 2.5)
    for i in range(11):
        f.line(150 + i * 33, 108, 150 + i * 33, 120, INK, 1.5)
    f.path("M290,108 L296,72 L334,72 L340,108 Z", "#dee2e6", INK, 2.5)
    f.arrow(315, 88, 315, 176, FORCE, 4, 16)
    f.tex(330, 160, r"\overline{F}", "start", FORCE)
    f.line(200, 228, 400, 228, MUTED, 1.5); f.line(200, 220, 200, 236, MUTED, 1.5); f.line(400, 220, 400, 236, MUTED, 1.5)
    f.tex(300, 246, r"20\,\text{cm}", "middle", size=20)
    f.line(30, 280, 570, 280, RULE, 1.5)
    f.line(55, 330, 165, 330, INK, 3)
    f.add('<polyline points="230,345 248,315 266,345 284,315 302,345 320,315 338,345" fill="none" stroke="' + INK + '" stroke-width="3" stroke-linejoin="round"/>')
    f.add('<polyline points="430,312 430,348 510,348 510,312" fill="none" stroke="' + INK + '" stroke-width="3" stroke-linejoin="round"/>')
    for x, t in ((110, r"\text{litteä}"), (284, r"\text{haitari}"), (470, r"\text{kouru}")):
        f.tex(x, 378, t, "middle", size=20)
    f.tex(300, 296, r"\text{poikkileikkaukset samasta paperimäärästä}", "middle", MUTED, size=18)
    return f.svg()


def _disk(f, cx, cy, r_out, r_letters, r_in, label):
    f.circle(cx, cy, r_out, WHITE, INK, 2.5)
    if r_in: f.circle(cx, cy, r_in, "none", INK, 1.5)
    k = len(ALPHABET)
    for i in range(k):
        a = math.radians(-90 + (i + 0.5) * 360 / k)
        f.line(cx + (r_in or r_letters - 20) * math.cos(a), cy + (r_in or r_letters - 20) * math.sin(a), cx + r_out * math.cos(a), cy + r_out * math.sin(a), RULE, 1.2)
    for i, ch in enumerate(ALPHABET):
        a = math.radians(-90 + i * 360 / k)
        f.tex(cx + r_letters * math.cos(a), cy + r_letters * math.sin(a), r"\text{" + ch + "}", "middle", size=17, w=18)
    f.line(cx - 6, cy, cx + 6, cy, INK, 1.5); f.line(cx, cy - 6, cx, cy + 6, INK, 1.5)
    f.tex(cx, cy + r_out + 22, label, "middle", size=20)


def salakiekko():
    f = Fig("lt-salakiekko", 400, "Tulostettava salakiekko kahdessa osassa. Vasemmalla iso ulkokiekko, jonka reunalla on suomen "
            "29 kirjainta A:sta Ö:hön myötäpäivään. Oikealla pienempi sisäkiekko, jonka reunalla ovat samat kirjaimet. Kiekot "
            "leikataan irti, pieni asetetaan ison päälle ja keskelle pannaan nasta, jolloin sisäkiekkoa voi kääntää.")
    _disk(f, 165, 172, 160, 143, 126, r"\text{ulkokiekko}")
    _disk(f, 462, 172, 122, 104, 0, r"\text{sisäkiekko}")
    return f.svg()


def varit():
    f = Fig("lt-varit", 320, "Vasemmalla mustalla taustalla kolme osittain päällekkäistä valoympyrää: punainen, vihreä ja "
            "sininen. Punaisen ja vihreän päällekkäinen alue on keltainen, punaisen ja sinisen purppura, vihreän ja sinisen "
            "syaani, ja kaikkien kolmen keskellä on valkoinen. Oikealla valkoinen valo tulee punaiseen kalvoon, ja kalvon läpi "
            "pääsee vain punaista valoa.")
    f.rect(20, 16, 300, 290, "#000000", rx=10)
    f.add('<g style="isolation:isolate">'
          '<circle cx="135" cy="125" r="70" fill="#ff0000" style="mix-blend-mode:screen"/>'
          '<circle cx="205" cy="125" r="70" fill="#00ff00" style="mix-blend-mode:screen"/>'
          '<circle cx="170" cy="185" r="70" fill="#0000ff" style="mix-blend-mode:screen"/></g>')
    f.tex(170, 98, r"\text{keltainen}", "middle", size=15)
    f.tex(170, 146, r"\text{valkoinen}", "middle", size=13)
    f.line(76, 250, 116, 186, WHITE, 1.5); f.circle(116, 186, 3, WHITE)
    f.line(264, 250, 224, 186, WHITE, 1.5); f.circle(224, 186, 3, WHITE)
    f.tex(62, 266, r"\text{purppura}", "middle", WHITE, size=16)
    f.tex(278, 266, r"\text{syaani}", "middle", WHITE, size=16)
    f.tex(70, 40, r"\text{punainen}", "middle", WHITE, size=17)
    f.tex(270, 40, r"\text{vihreä}", "middle", WHITE, size=17)
    f.tex(170, 278, r"\text{sininen}", "middle", WHITE, size=17)
    f.block_arrow(345, 160, 440, 160, "#f1f3f5", 20, 34, 24)
    f.path("M345,150 L416,150 L416,142 L440,160 L416,178 L416,170 L345,170 Z", "none", INK, 1.5)
    f.rect(446, 100, 18, 120, "#ff6b6b", INK, 2, rx=3)
    f.block_arrow(470, 160, 575, 160, "#e03131", 20, 34, 24)
    f.tex(392, 200, r"\text{valkoinen}", "middle", size=18)
    f.tex(455, 240, r"\text{punainen kalvo}", "middle", size=18)
    f.tex(522, 200, r"\text{punainen}", "middle", size=18)
    return f.svg()


FIGURES = {"co2": co2, "lampotila": lampotila, "virtapiiri": virtapiiri, "paperisilta": paperisilta, "salakiekko": salakiekko, "varit": varit}
