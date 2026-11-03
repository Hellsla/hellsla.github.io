"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy5-17` writes them into lesson.md.
Velocity and the direction a wave travels are blue (COLD) as in the other FY5 chapters; in the seismic figures the P wave
is a solid ink line and the S wave a dashed orange one, so line style tells them apart without colour."""
import math
from figlib import (Fig, Axes, fi, n, INK, MUTED, WHITE, RULE, RULE_LIGHT, GLASS, WATER_LIGHT, WATER, SAND_LIGHT, SAND,
                    HEAT_LIGHT, HEAT, HOT_LIGHT, COLD, COLD_LIGHT, ALUMINIUM, METAL_EDGE, IRON, GOOD, GOOD_LIGHT, PAPER)
import herolib as H

V_TISSUE = 1540.0          # m/s
VP, VS = 6.0, 3.5          # km/s, upper crust


def probe(f, x, y, w=96, h=50):
    """An ultrasound probe seen from the side: a grey handle, the cable up, the face on y + h."""
    f.path(f"M{n(x + w / 2 - 6)},{n(y)} C{n(x + w / 2 - 6)},{n(y - 22)} {n(x + w / 2 + 40)},{n(y - 30)} {n(x + w / 2 + 70)},{n(y - 40)}", stroke=IRON, w=5,
           extra='stroke-linecap="round"')
    f.rect(x, y, w, h, ALUMINIUM, INK, 2.5, 10)
    f.rect(x + 4, y + h - 12, w - 8, 10, METAL_EDGE)


def kaiku():
    f = Fig("fy517-kaiku", 380, "Kaavakuva, ei mittakaavassa: ultraäänianturi on ihon päällä, ja anturin ja ihon välissä on ohut "
            "geelikerros. Ihon alla ovat allekkain rasvakerros, lihas ja luu. Sininen nuoli kuvaa anturista alaspäin etenevää "
            "pulssia ja sen nopeutta. Rasvan ja lihaksen rajapinnalta sekä lihaksen ja luun rajapinnalta palaa ylöspäin kaiku, "
            "jota kuvaavat ohuemmat siniset nuolet. Vasemmalla mittajana näyttää syvyyden d ihon pinnasta lihaksen ja luun "
            "rajapintaan.")
    f.defs_add(f'<linearGradient id="fy517-bone" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{WHITE}"/><stop offset="1" stop-color="{RULE_LIGHT}"/></linearGradient>')
    x0, x1 = 96, 420
    skin, fat, bone = 92, 150, 290
    f.rect(x0, skin, x1 - x0, fat - skin, SAND_LIGHT)
    f.rect(x0, fat, x1 - x0, bone - fat, HOT_LIGHT)
    f.rect(x0, bone, x1 - x0, 66, "url(#fy517-bone)")
    for y in (fat, bone):
        f.line(x0, y, x1, y, INK, 2)
    f.line(x0, skin, x1, skin, INK, 2.5)
    # gel and probe
    f.path(f"M182,{skin} Q186,{skin - 13} 200,{skin - 13} H292 Q306,{skin - 13} 310,{skin} Z", WATER_LIGHT)
    probe(f, 198, 28)
    # the pulse going down and the echoes coming back
    f.arrow(222, skin + 6, 222, bone - 4, COLD, 3.5, 16)
    f.tex(236, 206, r"\overline{v}", "start", COLD)
    f.arrow(262, fat - 4, 262, skin + 6, COLD, 2, 12)
    f.arrow(292, bone - 4, 292, skin + 6, COLD, 2, 12)
    f.path(f"M222,{fat} L262,{fat}", stroke=COLD, w=1.5, extra='stroke-dasharray="4 4"')
    f.path(f"M222,{bone} L292,{bone}", stroke=COLD, w=1.5, extra='stroke-dasharray="4 4"')
    f.tex(312, 222, r"\text{kaiut}", "start", COLD)
    f.tex(212, 121, r"\text{pulssi}", "end", COLD)
    # depth bracket
    f.path(f"M72,{skin} H62 V{bone} H72", stroke=INK, w=2)
    f.tex(52, (skin + bone) / 2, "d", "end")
    # layer names right of the section
    f.tex(436, skin - 8, r"\text{geeli}", "start")
    f.line(312, skin - 7, 428, skin - 8, MUTED, 1.5)
    f.tex(436, (skin + fat) / 2, r"\text{rasva}", "start")
    f.tex(436, (fat + bone) / 2, r"\text{lihas}", "start")
    f.tex(436, bone + 32, r"\text{luu}", "start")
    return f.svg()


def taajuus():
    f = Fig("fy517-taajuus", 372, "Kaavakuva: kaksi ultraäänianturia vierekkäin lähettää pulssin samaan kudokseen. Vasemmalla "
            "taajuus on 3 MHz ja aallonpituus noin 0,5 mm, oikealla taajuus 12 MHz ja aallonpituus noin 0,13 mm. Aaltorintamien "
            "välit on suurennettu, mutta niiden suhde neljä yhteen on oikea. Vasemman aallon rintamat haalistuvat hitaasti ja "
            "ulottuvat noin 17 cm:n syvyyteen, oikean aallon rintamat haalistuvat jo noin 4 cm:n syvyydellä. Syvyysasteikko "
            "vasemmalla on senttimetreinä.")
    top, per_cm = 76, 16.0                     # tissue starts at y = 76, 16 units per centimetre
    f.rect(96, top, 470, 18 * per_cm, HOT_LIGHT, extra='fill-opacity="0.45"')
    f.line(96, top, 566, top, INK, 2.5)
    # depth scale
    f.line(80, top, 80, top + 17 * per_cm, INK, 2)
    for cm in (0, 5, 10, 15):
        y = top + cm * per_cm
        f.line(74, y, 80, y, INK, 2)
        f.tex(68, y, fi(cm), "end", MUTED)
    f.tex(68, top - 36, r"\text{cm}", "end", MUTED, w=50)
    for cx, f_mhz, step, reach in ((230, 3, 24, 50 / 3), (450, 12, 6, 50 / 12)):
        probe(f, cx - 48, 20, 96, 46)
        f.tex(cx - 58, 40, fi(f_mhz) + r"\,\text{MHz}", "end", w=100)
        k, y = 0, top + 6
        while y < top + 18 * per_cm - 4:
            z = (y - top) / per_cm
            op = max(0.0, 1 - z / reach)
            if op > 0.02:
                half = 40 + 0.9 * (y - top) ** 0.85
                f.path(f"M{n(cx - half)},{n(y)} Q{n(cx)},{n(y + 10)} {n(cx + half)},{n(y)}", stroke=COLD, w=2,
                       extra=f'stroke-opacity="{op:.2f}"')
            y += step
            k += 1
        yr = top + reach * per_cm
        f.line(cx - 96, yr, cx + 96, yr, MUTED, 1.5, "6 5")
    f.tex(230, 356, r"\lambda \approx 0{,}5\,\text{mm}", "middle", w=170)
    f.tex(450, 356, r"\lambda \approx 0{,}13\,\text{mm}", "middle", w=180)
    return f.svg()


def maapallo():
    f = Fig("fy517-maapallo", 384, "Kaavakuva Maan poikkileikkauksesta, kerrosten säteet mittakaavassa, säteiden kaarevuus "
            "suuntaa antava: uloimpana vaippa, sen sisällä nestemäinen ulkoydin ja keskellä kiinteä sisäydin. Maanjäristys on "
            "ylimpänä pinnalla. Oikealle lähtee kolme P-aallon sädettä yhtenäisinä viivoina, ja yksi P-aalto kulkee ytimen läpi "
            "Maan vastakkaiselle puolelle. Vasemmalle lähtee kolme S-aallon sädettä katkoviivoina; S-aalto, joka osuu "
            "ulkoytimeen, pysähtyy sen pintaan. Maan pinnalla järistystä vastapäätä on S-aaltojen varjoalue, joka alkaa noin "
            "103 asteen kulmaetäisyydeltä järistyksestä.")
    cx, cy, R = 214, 196, 166
    rc, ri = R * 3480 / 6371, R * 1220 / 6371
    f.defs_add(f'<radialGradient id="fy517-mantle" cx="0.5" cy="0.5" r="0.5"><stop offset="0.55" stop-color="{SAND}"/><stop offset="1" stop-color="{SAND_LIGHT}"/></radialGradient>')
    f.circle(cx, cy, R, "url(#fy517-mantle)", INK, 2.5)
    f.circle(cx, cy, rc, HEAT_LIGHT, INK, 2)
    f.circle(cx, cy, ri, HEAT, INK, 2)

    def surf(deg, r=R):
        a = math.radians(deg)
        return cx + r * math.sin(a), cy - r * math.cos(a)

    ex, ey = surf(0)

    def ray(deg, dash=None, colour=INK):
        x2, y2 = surf(deg)
        mx, my = (ex + x2) / 2, (ey + y2) / 2
        dx, dy = cx - mx, cy - my
        L = math.hypot(dx, dy)
        c = 0.16 * R * abs(math.sin(math.radians(deg) / 2))
        qx, qy = mx + dx / L * c, my + dy / L * c
        extra = f'stroke-dasharray="{dash}"' if dash else ""
        f.path(f"M{n(ex)},{n(ey)} Q{n(qx)},{n(qy)} {n(x2)},{n(y2)}", stroke=colour, w=2.5, extra=extra)

    for deg in (40, 72, 100):
        ray(deg)
    f.line(ex, ey, cx, cy + R, INK, 2.5)                       # P through the core to the far side
    for deg in (40, 72, 100):
        ray(-deg, "9 6", HEAT)
    # an S ray that meets the outer core and stops there
    a = math.radians(-24)
    x2, y2 = cx + rc * math.sin(math.radians(-150)), cy - rc * math.cos(math.radians(-150))
    f.line(ex, ey, x2, y2, HEAT, 2.5, "9 6")
    f.line(x2 - 8, y2 - 8, x2 + 8, y2 + 8, HEAT, 3)
    f.line(x2 - 8, y2 + 8, x2 + 8, y2 - 8, HEAT, 3)
    # the S shadow zone on the surface from 103° to 257° (opposite the quake)
    a0, a1 = math.radians(103), math.radians(257)
    pts = " ".join(f"{n(cx + (R + 8) * math.sin(a0 + (a1 - a0) * k / 40))},{n(cy - (R + 8) * math.cos(a0 + (a1 - a0) * k / 40))}" for k in range(41))
    f.add(f'<polyline points="{pts}" fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round"/>')
    # the earthquake
    f.path(" ".join(("M" if k == 0 else "L") + f"{n(ex + (12 if k % 2 == 0 else 5) * math.sin(k * math.pi / 5))},{n(ey - (12 if k % 2 == 0 else 5) * math.cos(k * math.pi / 5))}" for k in range(10)) + " Z", HEAT, INK, 1.5)
    # labels in a column on the right, with leader lines
    lx = 396
    f.tex(lx, 40, r"\text{järistys}", "start")
    f.line(lx - 6, 40, ex + 16, ey, MUTED, 1.5)
    f.tex(lx, 112, r"\text{vaippa}", "start")
    f.line(lx - 6, 112, *surf(58, R - 20), MUTED, 1.5)
    f.tex(lx, 178, r"\text{ulkoydin (neste)}", "start", w=180)
    f.line(lx - 6, 178, *surf(80, (rc + ri) / 2 + 14), MUTED, 1.5)
    f.tex(lx, 222, r"\text{sisäydin}", "start")
    f.line(lx - 6, 222, cx + ri - 4, cy + 6, MUTED, 1.5)
    # legend
    f.line(lx, 276, lx + 44, 276, INK, 2.5)
    f.tex(lx + 54, 276, r"\text{P-aalto}", "start")
    f.line(lx, 312, lx + 44, 312, HEAT, 2.5, "9 6")
    f.tex(lx + 54, 312, r"\text{S-aalto}", "start")
    f.line(lx, 350, lx + 44, 350, MUTED, 5, cap="round")
    f.tex(lx + 54, 350, r"\text{S-varjoalue}", "start", w=150)
    return f.svg()


def kulkuaika():
    f = Fig("fy517-kulkuaika", 360, "Kuvaaja mittakaavassa: P- ja S-aallon kulkuaika t sekunteina etäisyyden d funktiona "
            "kilometreinä nollasta 300 kilometriin, kun P-aallon nopeus on 6,0 km/s ja S-aallon 3,5 km/s. Kumpikin on origosta "
            "nouseva suora; S-aallon suora on jyrkempi. Etäisyydellä 105 km P-aallon kulkuaika on 17,5 s ja S-aallon 30 s, ja "
            "niiden ero, 12,5 s, on merkitty pystysuoralla janalla.")
    ax = Axes(f, (96, 306), (480, 72), x=(0, 300), y=(0, 90), xticks=[50, 100, 150, 200, 250, 300],
              yticks=[10, 20, 30, 40, 50, 60, 70, 80, 90], xlabel=r"d\ (\text{km})", ylabel=r"t\ (\text{s})",
              yfmt=lambda v: fi(v) if v % 20 == 0 else "")
    ax.line([(0, 0), (300, 300 / VP)], INK, 3)
    ax.line([(0, 0), (300, 300 / VS)], HEAT, 3, "11 7")
    d = 105
    ax.guide(d, d / VS)
    f.line(ax.x0, ax.Y(d / VP), ax.X(d), ax.Y(d / VP), MUTED, 1.5, "6 5")
    ax.point(d, d / VP, INK)
    ax.point(d, d / VS, HEAT)
    f.path(f"M{n(ax.X(d) + 12)},{n(ax.Y(d / VS))} H{n(ax.X(d) + 20)} V{n(ax.Y(d / VP))} H{n(ax.X(d) + 12)}", stroke=INK, w=2)
    f.tex(ax.X(d) + 26, ax.Y(28), r"\Delta t", "start")   # between the lines: P is below 21 s here
    f.tex(ax.X(300) + 8, ax.Y(300 / VP), r"\text{P}", "start")
    f.tex(ax.X(300) - 30, ax.Y(300 / VS) - 4, r"\text{S}", "end", HEAT)
    return f.svg()


def tsunami():
    f = Fig("fy517-tsunami", 340, "Kuvaaja mittakaavassa: matalan veden aallon nopeus v metreinä sekunnissa veden syvyyden h "
            "funktiona metreinä nollasta 5000 metriin, kun v on neliöjuuri g kertaa h. Käyrä nousee jyrkästi matalassa vedessä "
            "ja loivenee syvemmällä. Syvyydellä 4000 m nopeus on noin 198 m/s ja syvyydellä 1000 m noin 99 m/s; molemmat "
            "pisteet on merkitty.")
    ax = Axes(f, (96, 290), (480, 72), x=(0, 5000), y=(0, 250), xticks=[1000, 2000, 3000, 4000, 5000],
              yticks=[50, 100, 150, 200, 250], xlabel=r"h\ (\text{m})", ylabel=r"v\ (\text{m/s})")
    ax.curve(lambda h: math.sqrt(9.81 * h), 0, 5000, COLD, 3, steps=200)
    for h in (1000, 4000):
        ax.guide(h, math.sqrt(9.81 * h))
        ax.point(h, math.sqrt(9.81 * h), COLD)
    f.tex(ax.X(4000) - 14, ax.Y(math.sqrt(9.81 * 4000)) - 26, r"198\,\text{m/s}", "end", bg=True, w=120)
    f.tex(ax.X(1000) + 16, ax.Y(math.sqrt(9.81 * 1000)) + 26, r"99\,\text{m/s}", "start", bg=True, w=100)
    return f.svg()


def a_scan():
    """Task figure: a model A-scan of a thigh, echoes at 20, 50 and 90 µs, nothing after the bone echo."""
    f = Fig("fy517-ascan", 330, "Kuvaaja, keksitty esimerkkiaineisto: ultraäänilaitteen A-kuvaus reidestä. Vaaka-akselilla "
            "aika t mikrosekunteina pulssin lähettämisestä nollasta 110 mikrosekuntiin, apuviivat viiden mikrosekunnin välein "
            "ja lukuarvot 20 mikrosekunnin välein. Pystyakselilla kaiun voimakkuus suhteellisena. Hetkellä nolla on korkea "
            "lähetyspulssi. Kaiut: A hetkellä 20 µs, matala; B hetkellä 50 µs, matalampi; C hetkellä 90 µs, korkea. "
            "Kaiun C jälkeen käyrä pysyy nollassa.")
    ax = Axes(f, (96, 286), (470, 60), x=(0, 110), y=(0, 1.0), xticks=list(range(5, 111, 5)), yticks=[0.25, 0.5, 0.75, 1.0],
              xlabel=r"t\ (\mu\text{s})", ylabel=r"\text{kaiun voimakkuus}", xfmt=lambda v: fi(v) if v % 20 == 0 else "",
              yfmt=lambda v: "", origin_label=True)
    peaks = [(1.0, 1.0, 0.9), (20, 0.40, 0.9), (50, 0.26, 0.9), (90, 0.82, 0.9)]
    amp = lambda t: min(0.98, sum(h * math.exp(-((t - t0) / s) ** 2) for t0, h, s in peaks))
    ax.line([(k * 0.1, amp(k * 0.1)) for k in range(0, 1101)], INK, 3)
    for t0, h, _ in peaks[1:]:
        f.tex(ax.X(t0), ax.Y(h) - 22, r"\text{" + "ABC"[peaks.index((t0, h, _)) - 1] + "}", "middle", bg=True)
    f.tex(ax.X(3) + 8, ax.Y(0.9), r"\text{lähetyspulssi}", "start", MUTED, bg=True, w=150)
    return f.svg()


def trace(f, y, t0x, sx, tP, tS, tmax, aP=9, aS=30):
    """One seismogram trace on baseline y: P from tP, S from tS (model wiggles, no noise)."""
    pts = []
    for k in range(int(tmax * 10) + 1):
        t = k / 10
        u = 0.0
        if t >= tP: u += aP * math.exp(-(t - tP) / 4.0) * math.sin(2 * math.pi * 0.6 * (t - tP))
        if t >= tS: u += aS * math.exp(-(t - tS) / 6.0) * math.sin(2 * math.pi * 0.3 * (t - tS))
        pts.append(f"{n(t0x + t * sx)},{n(y - u)}")
    f.add(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{INK}" stroke-width="2" stroke-linejoin="round"/>')


def time_axis(f, x0, x1, ytop, yax, tmax, minor=2, major=10):
    sx = (x1 - x0) / tmax
    for k in range(minor, tmax + 1, minor):
        f.line(x0 + k * sx, ytop, x0 + k * sx, yax, RULE if k % major == 0 else RULE_LIGHT, 1.5)
    f.arrow(x0 - 1, yax, x1 + 26, yax, INK, 2.5, 13)
    for k in range(major, tmax + 1, major):
        f.line(x0 + k * sx, yax, x0 + k * sx, yax + 7, INK, 2)
        f.tex(x0 + k * sx, yax + 24, fi(k), "middle")
    f.tex(x0, yax + 24, "0", "middle")
    f.tex(x1 + 32, yax, r"t\ (\text{s})", "start")
    return sx


def seismogrammit():
    """Task figure: model seismograms of three stations at 84, 168 and 252 km (vP 6,0 and vS 3,5 km/s)."""
    f = Fig("fy517-seismit", 372, "Kuvaaja, mallin laskemia arvoja: kolmen seismografiaseman seismogrammit allekkain, aika t "
            "sekunteina maanjäristyksestä nollasta 80 sekuntiin, apuviivat kahden sekunnin välein ja lukuarvot kymmenen sekunnin "
            "välein. Ylin asema on 84 km:n, keskimmäinen 168 km:n ja alin 252 km:n päässä järistyksestä. Jokaisessa käyrässä "
            "ensin alkaa pieni värähtely, P-aalto, ja myöhemmin suurempi, S-aalto; alkuhetket on merkitty kirjaimin P ja S. "
            "Ylimmässä P alkaa hetkellä 14 s ja S hetkellä 24 s, keskimmäisessä P 28 s ja S 48 s, alimmassa P 42 s ja S 72 s. "
            "Pinta-aallot on jätetty pois.")
    x0, x1, tmax = 100, 490, 80
    sx = time_axis(f, x0, x1, 36, 320, tmax)
    f.tex(14, 22, r"\text{etäisyys}", "start", MUTED, w=110)
    for y, d in ((84, 84), (180, 168), (276, 252)):
        tP, tS = d / VP, d / VS
        f.line(x0, y, x1, y, RULE, 1.5)
        trace(f, y, x0, sx, tP, tS, tmax, aP=12, aS=34)
        f.tex(88, y, fi(d) + r"\,\text{km}", "end", w=96)
        f.tex(x0 + tP * sx, y - 38, r"\text{P}", "middle", bg=True)
        f.tex(x0 + tS * sx, y - 48, r"\text{S}", "middle", HEAT, bg=True)
    return f.svg()


def seismogrammi_ex():
    """Task figure for exercise L2-01: one station's model seismogram, P from 12 s and S from 30 s after the recording starts."""
    f = Fig("fy517-seismi-ex", 236, "Kuvaaja, keksitty esimerkkiaineisto: yhden seismografiaseman seismogrammi, aika t sekunteina "
            "tallennuksen alusta nollasta 50 sekuntiin, apuviivat kahden sekunnin välein ja lukuarvot kymmenen sekunnin välein. "
            "Pieni värähtely, P-aalto, alkaa hetkellä 12 s ja suurempi, S-aalto, hetkellä 30 s; alkuhetket on merkitty "
            "kirjaimin P ja S.")
    x0, x1, tmax = 60, 490, 50
    sx = time_axis(f, x0, x1, 20, 186, tmax)
    y = 100
    f.line(x0, y, x1, y, RULE, 1.5)
    trace(f, y, x0, sx, 12, 30, tmax, aP=10, aS=38)
    f.tex(x0 + 12 * sx, y - 44, r"\text{P}", "middle", bg=True)
    f.tex(x0 + 30 * sx, y - 58, r"\text{S}", "middle", HEAT, bg=True)
    return f.svg()


def hero():
    """The chapter's opening illustration: an ultrasound examination, the probe on the belly, the image on the screen."""
    f = H.hero("fy517-hero", "Kuvitus: ultraäänitutkimus. Potilas makaa selällään tutkimuspöydällä. Hoitaja seisoo pöydän "
               "vieressä ja painaa ultraäänianturia potilaan vatsalle, jonka iholla on läpikuultavaa geeliä. Anturista lähtee "
               "kaarevia aaltorintamia kehon sisään. Anturin johto kulkee ultraäänilaitteeseen, jonka näytöllä on harmaa "
               "viuhkan muotoinen kuva.")
    f.rect(0, 0, 1200, 600, PAPER)
    f.rect(0, 0, 1200, 470, H.grad(f, "fy517h-wall", GLASS, COLD_LIGHT))
    f.rect(0, 470, 1200, 130, RULE_LIGHT)
    f.line(0, 470, 1200, 470, RULE, 3)
    # the nurse stands behind the bed
    x, yf = 770, 520
    f.path(f"M{x - 32},{yf - 130} Q{x - 36},{yf - 236} {x},{yf - 242} Q{x + 36},{yf - 236} {x + 32},{yf - 130} Z", GOOD)          # scrubs
    f.path(f"M{x + 28},{yf - 222} L{x + 40},{yf - 130}", stroke=GOOD, w=21, extra='stroke-linecap="round"')                           # far arm down
    f.circle(x + 40, yf - 124, 10, SAND_LIGHT)
    f.rect(x - 9, yf - 262, 18, 24, SAND_LIGHT)
    f.circle(x, yf - 281, 28, SAND_LIGHT)
    f.path(f"M{x - 29},{yf - 281} Q{x - 28},{yf - 315} {x},{yf - 313} Q{x + 30},{yf - 313} {x + 29},{yf - 285} Q{x + 6},{yf - 296} {x - 29},{yf - 281} Z", INK)
    # bed
    for x in (300, 840):
        f.rect(x, 400, 16, 120, IRON, INK, 2)
        f.circle(x + 8, 528, 10, INK)
    f.rect(240, 372, 680, 34, ALUMINIUM, INK, 3, 8)
    f.rect(240, 352, 680, 26, WHITE, INK, 2.5, 10)
    # patient lying on the back, head to the left
    f.path("M262,330 Q262,306 300,306 L326,306 Q350,306 350,330 L350,352 L262,352 Z", WHITE, INK, 2.5)      # pillow
    f.circle(318, 300, 36, SAND_LIGHT, INK, 2.5)
    f.path("M282,296 Q284,258 322,262 Q352,266 354,292 Q330,276 306,280 Q290,284 282,296 Z", INK)
    f.path("M350,318 L420,312 Q520,300 560,292 Q640,270 690,300 L700,352 L350,352 Z", SAND_LIGHT, INK, 2.5)  # bare belly
    f.path("M350,318 L460,312 L470,352 L350,352 Z", COLD, INK, 2.5)                                        # shirt pulled up
    f.path("M690,300 Q700,310 700,326 L700,352 L880,352 L884,322 Q880,306 860,304 L700,304 Z", INK)       # trousers
    f.path("M880,312 Q904,310 910,324 Q912,344 896,352 L878,352 Z", COLD_LIGHT, INK, 2)                   # feet
    # gel on the skin and the probe pressed on the belly
    f.path("M560,290 Q574,276 604,276 Q634,276 646,288 Q620,296 600,296 Q578,296 560,290 Z", WATER_LIGHT, extra='fill-opacity="0.9"')
    # wavefronts into the body (clipped to the belly by drawing them short)
    for k, r in enumerate((26, 44, 62)):
        f.path(f"M{n(603 - r * 0.7)},{n(296 + r * 0.55)} Q603,{n(296 + r * 1.15)} {n(603 + r * 0.7)},{n(296 + r * 0.55)}", stroke=COLD, w=4,
               extra=f'stroke-linecap="round" stroke-opacity="{0.9 - 0.25 * k:.2f}"')
    f.rect(578, 214, 50, 68, ALUMINIUM, INK, 3, 12)
    f.rect(582, 270, 42, 12, METAL_EDGE)
    # the nurse's arm reaching to the probe
    f.path("M746,292 Q700,272 642,240", stroke=GOOD, w=21, extra='stroke-linecap="round"')
    f.circle(632, 232, 15, SAND_LIGHT, INK, 2)
    # the cable and the ultrasound machine
    f.path("M603,214 C600,150 760,130 900,170 S1060,250 1080,300", stroke=IRON, w=5, extra='stroke-linecap="round"')
    f.rect(1040, 300, 120, 200, ALUMINIUM, INK, 3, 10)
    f.rect(1056, 320, 88, 30, METAL_EDGE, INK, 2, 6)
    for x in (1064, 1088, 1112, 1136):
        f.circle(x, 372, 6, IRON)
    for x in (1050, 1146):
        f.circle(x, 512, 11, INK)
    f.rect(1092, 230, 16, 72, IRON)
    f.rect(1010, 110, 180, 128, INK, INK, 3, 10)
    f.path("M1100,128 L1048,222 Q1100,236 1152,222 Z", MUTED)
    for k, (dx, dy) in enumerate(((-18, 160), (6, 176), (22, 196), (-30, 200), (-6, 206), (14, 214))):
        f.add(f'<ellipse cx="{1100 + dx}" cy="{dy}" rx="{10 + 4 * (k % 3)}" ry="4" fill="{RULE_LIGHT}" fill-opacity="0.8"/>')
    f.path("M1076,186 Q1100,170 1122,186 Q1100,198 1076,186 Z", INK)
    return f.svg()


FIGURES = {"hero": hero, "kaiku": kaiku, "taajuus": taajuus, "maapallo": maapallo, "kulkuaika": kulkuaika, "tsunami": tsunami,
           "a-scan": a_scan, "seismogrammit": seismogrammit, "seismogrammi-ex": seismogrammi_ex}
# What each figure would give away if put into a task (scripts/figcat.py; the catalog's "reuse"): safe | reveals: … | decorative
REUSE = {
    "kaiku": "reveals: the echo travels to the boundary and back, depth d from the skin",
    "taajuus": "reveals: a higher frequency has a shorter wavelength and reaches less deep",
    "maapallo": "reveals: S waves stop at the liquid outer core, S shadow zone from about 103°",
    "kulkuaika": "reveals: t_P and t_S grow linearly with d, Δt = 12,5 s at 105 km",
    "tsunami": "reveals: v = √(gh), 198 m/s at 4000 m",
    "a-scan": "safe: a model A-scan of a thigh, echoes A 20 µs, B 50 µs, C 90 µs, nothing after C; no depths",
    "seismogrammit": "safe: model seismograms at 84, 168 and 252 km, P and S onsets marked on a 2 s grid; no speeds or ratio",
    "seismogrammi-ex": "safe: one model seismogram, P from 12 s and S from 30 s after the recording starts; no distance",
}
