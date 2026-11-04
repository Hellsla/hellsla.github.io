"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy5-17` writes them into lesson.md.
Velocity and the direction a wave travels are blue (COLD) as in the other FY5 chapters; in the seismic figures the P wave
is a solid ink line and the S wave a dashed orange one, so line style tells them apart without colour."""
import math
from figlib import (Fig, Axes, fi, n, INK, MUTED, WHITE, RULE, RULE_LIGHT, GLASS, WATER_LIGHT, WATER, SAND_LIGHT, SAND,
                    HEAT_LIGHT, HEAT, HOT_LIGHT, COLD, COLD_LIGHT, ALUMINIUM, METAL_EDGE, IRON, GOOD, GOOD_LIGHT, ICE, ICE_EDGE, PAPER)
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
    """The chapter's opening illustration: a pregnancy ultrasound in a dimmed room. The mother lies on the couch, head on
    a wedge pillow at the right; the sonographer sits on a stool beyond the couch's head end, between it and the machine,
    leans in and reaches past the mother's head to hold the probe on a dab of gel on the belly, her other hand on the
    controls. Pulses run from the probe into the belly, and the screen shows the fan-shaped echo image with the baby.
    The couch and the mother are drawn head-left and mirrored (x -> MIR - x). Scale about 300 px/m."""
    f = H.hero("fy517-hero", "Kuvitus: raskausajan ultraäänitutkimus hämärässä huoneessa. Odottava äiti makaa tutkimuspöydällä "
               "pää kiilatyynyllä ja katsoo näyttöä. Hoitaja istuu jakkaralla pöydän pääpuolella laitteen vieressä, kurottaa "
               "äidin pään ohi ja painaa ultraäänianturia äidin vatsalle läpikuultavan geelitäplän kohdalle. Toisella kädellä "
               "hän säätää laitetta. Anturista lähtee "
               "kaaria vatsan sisään. Laitteen näytöllä on viuhkan muotoinen harmaasävykuva, jossa näkyy vauva.")
    D = 70                                              # shifts the whole group right
    floor = 560
    # room: dim wall, floor, a window with drawn blinds and a curtain on its rail
    f.rect(0, 0, 1200, floor, H.grad(f, "fy517h-wall", COLD_LIGHT, GLASS, y1=0, y2=floor))
    f.rect(0, floor, 1200, 40, H.grad(f, "fy517h-floor", RULE_LIGHT, RULE, y1=floor, y2=600))
    f.line(0, floor, 1200, floor, RULE, 3)
    f.rect(40, 60, 170, 220, ALUMINIUM, INK, 3, 4)
    for k in range(11): f.rect(46, 66 + 19.5 * k, 158, 13, WHITE, INK, 1.5)
    f.line(14, 30, 300, 30, IRON, 5, cap="round")
    f.path("M226,32 Q238,180 224,330 Q250,326 262,330 Q276,180 270,32 Z", GOOD_LIGHT, INK, 2.5)
    f.path("M246,40 Q252,180 244,322", stroke=GOOD, w=2)
    # the machine on its cart, right of the sonographer: base, body, control panel, the screen on an arm
    mx = 1010
    f.rect(mx - 70, floor - 40, 150, 22, IRON, INK, 2.5, 6)
    for wx in (mx - 56, mx + 66): f.circle(wx, floor - 8, 9, INK)
    f.rect(mx - 50, floor - 300, 110, 262, ALUMINIUM, INK, 3, 10)
    f.rect(mx - 38, floor - 250, 86, 6, METAL_EDGE); f.rect(mx - 38, floor - 230, 86, 6, METAL_EDGE)
    f.path(f"M{mx - 92},{floor - 300} L{mx + 82},{floor - 300} L{mx + 74},{floor - 330} L{mx - 84},{floor - 330} Z", WHITE, INK, 3)
    for k in range(6): f.rect(mx - 70 + 22 * k, floor - 324, 14, 7, RULE, INK, 1)
    f.circle(mx + 52, floor - 316, 9, METAL_EDGE, INK, 1.5)
    f.rect(mx - 4, floor - 400, 14, 72, IRON, INK, 2)
    # the screen and the image on it: a fan of grey speckle with the baby's head and body as bright echoes
    sx0, sy0, sw, sh = mx - 120, 50, 260, 180
    f.rect(sx0 - 10, sy0 - 10, sw + 20, sh + 20, IRON, INK, 2.5, 10)
    f.rect(sx0, sy0, sw, sh, INK, None, 2, 4)
    ax, ay, R0, R1, half = sx0 + sw / 2, sy0 + 10, 14, sh - 16, math.radians(36)
    def fan_pt(r, a): return ax + r * math.sin(a), ay + r * math.cos(a)
    (p1x, p1y), (p2x, p2y), (p3x, p3y), (p4x, p4y) = fan_pt(R0, -half), fan_pt(R1, -half), fan_pt(R1, half), fan_pt(R0, half)
    fan = f"M{n(p1x)},{n(p1y)} L{n(p2x)},{n(p2y)} A{R1},{R1} 0 0 0 {n(p3x)},{n(p3y)} L{n(p4x)},{n(p4y)} A{R0},{R0} 0 0 1 {n(p1x)},{n(p1y)} Z"
    f.defs_add(f'<radialGradient id="fy517h-fan" gradientUnits="userSpaceOnUse" cx="{n(ax)}" cy="{n(ay)}" r="{R1}"><stop offset="0" stop-color="{METAL_EDGE}"/>'
               f'<stop offset="1" stop-color="{IRON}"/></radialGradient>')
    f.defs_add(f'<clipPath id="fy517h-fanclip"><path d="{fan}"/></clipPath>')
    f.path(fan, "url(#fy517h-fan)")
    speck = "".join(f'<circle cx="{n(fan_pt(R0 + (R1 - R0) * H.rnd(k, 3), (2 * H.rnd(k, 8) - 1) * half)[0])}" '
                    f'cy="{n(fan_pt(R0 + (R1 - R0) * H.rnd(k, 3), (2 * H.rnd(k, 8) - 1) * half)[1])}" r="1.6" fill="{ALUMINIUM}" fill-opacity="0.7"/>'
                    for k in range(90))
    cx, cy = ax + 4, ay + 98                            # amniotic fluid (dark, echo-free) with the baby inside
    f.add(f'<g clip-path="url(#fy517h-fanclip)">{speck}'
          f'<ellipse cx="{n(cx)}" cy="{n(cy)}" rx="74" ry="46" fill="{INK}"/>'
          f'<path d="M{n(cx - 76)},{n(cy - 6)} Q{n(cx)},{n(cy - 66)} {n(cx + 76)},{n(cy - 6)}" fill="none" stroke="{WHITE}" stroke-width="3" stroke-opacity="0.7"/>'
          f'<circle cx="{n(cx - 30)}" cy="{n(cy - 2)}" r="22" fill="none" stroke="{WHITE}" stroke-width="4"/>'
          f'<path d="M{n(cx - 10)},{n(cy - 16)} Q{n(cx + 30)},{n(cy - 30)} {n(cx + 46)},{n(cy - 2)} Q{n(cx + 52)},{n(cy + 22)} {n(cx + 24)},{n(cy + 26)} '
          f'Q{n(cx + 4)},{n(cy + 24)} {n(cx - 10)},{n(cy + 18)}" fill="none" stroke="{WHITE}" stroke-width="4" stroke-linecap="round"/>'
          f'<path d="M{n(cx + 10)},{n(cy + 6)} q14,-6 22,4" fill="none" stroke="{ALUMINIUM}" stroke-width="3" stroke-linecap="round"/></g>')
    f.path(fan, "none", METAL_EDGE, 1.5)

    # geometry of the mother (lying on her back, head left, knees up) and of the probe on her belly
    top = 338                                           # mattress top
    bc, br = (425 + D, top - 50), 64                    # the belly: a dome (circle) rising from the torso
    phi = math.radians(-30)                             # the probe stands square to the skin, 30° towards the head
    pc = (bc[0] + br * math.sin(phi), bc[1] - br * math.cos(phi))
    nrm = (math.sin(phi), -math.cos(phi))
    MIR = 1020                                          # mirror: drawn head-left, shown head-right
    def along(t): return MIR - (pc[0] + nrm[0] * t), pc[1] + nrm[1] * t
    grip, ptop = along(50), along(92)
    # the probe's cable, from the probe up and over to the machine (behind the sonographer)
    f.path(f"M{n(ptop[0])},{n(ptop[1])} C{n(ptop[0] + 20)},{n(ptop[1] - 110)} {mx - 120},{floor - 470} {mx - 48},{floor - 270}", stroke=INK, w=3.5)
    # the sonographer on a stool beyond the couch's head end, leaning in (drawn first: the couch covers her knees)
    scrub = GOOD
    f.rect(838, 412, 64, 14, IRON, INK, 2, 5)                                    # stool: seat, column, base on wheels
    f.rect(864, 426, 12, 104, METAL_EDGE, INK, 2)
    f.path(f"M820,{floor - 22} L870,{floor - 34} L920,{floor - 22}", stroke=INK, w=6, extra='stroke-linecap="round"')
    for wx in (822, 918): f.circle(wx, floor - 12, 8, INK)
    f.path(f"M866,404 L792,404 L782,{floor - 14}", stroke=INK, w=31, extra='stroke-linecap="round" stroke-linejoin="round"')
    f.path(f"M866,404 L792,404 L782,{floor - 14}", stroke=COLD, w=26, extra='stroke-linecap="round" stroke-linejoin="round"')
    f.path(f"M772,{floor - 6} h34", stroke=WHITE, w=14, extra='stroke-linecap="round"')
    hx, hy = 786, 168                                   # head, turned to the probe
    shl, shr = (806, 226), (826, 222)                   # shoulders: the near one reaches to the probe, the far one to the panel
    f.path(f"M820,422 Q800,330 790,228 Q812,206 844,216 Q874,300 872,422 Z", scrub, INK, 2.5)
    elbow2, hand2 = (868, 300), (mx - 60, floor - 322)
    f.path(f"M{shr[0]},{shr[1]} L{elbow2[0]},{elbow2[1]} L{n(hand2[0])},{n(hand2[1])}", stroke=scrub, w=20, extra='stroke-linecap="round" stroke-linejoin="round"')
    f.circle(hand2[0], hand2[1], 10, SAND_LIGHT)
    f.path(f"M{hx + 4},{hy + 20} L{hx + 16},{hy + 52}", stroke=SAND_LIGHT, w=20)
    f.circle(hx, hy, 32, SAND_LIGHT)
    f.path(f"M{hx + 33},{hy + 10} Q{hx + 40},{hy - 34} {hx + 2},{hy - 34} Q{hx - 30},{hy - 34} {hx - 28},{hy - 12} Q{hx + 6},{hy - 10} {hx + 14},{hy + 22} Z", INK)
    f.circle(hx + 32, hy - 16, 13, INK)                 # hair tied in a bun
    f.add(f'<g transform="translate({MIR} 0) scale(-1 1)">')
    # the couch: base on wheels, pedestal, frame and mattress, a wedge pillow
    f.rect(400 + D, top + 44, 110, floor - 34 - top - 44, IRON, INK, 2.5)
    f.rect(270 + D, floor - 34, 380, 20, METAL_EDGE, INK, 2.5, 6)
    for wx in (288 + D, 632 + D): f.circle(wx, floor - 8, 9, INK)
    f.rect(180 + D, top + 22, 600, 24, ALUMINIUM, INK, 2.5, 6)
    f.rect(170 + D, top - 4, 620, 30, WHITE, INK, 2.5, 12)
    f.path(f"M{176 + D},{top - 4} L{176 + D},{top - 52} Q{176 + D},{top - 60} {186 + D},{top - 58} L{290 + D},{top - 10} L{290 + D},{top - 4} Z", COLD_LIGHT, INK, 2.5)
    # the mother: legs with the knees up and the feet flat on the mattress
    skin, shirt, trousers = SAND_LIGHT, HOT_LIGHT, IRON
    hip, knee, heel = (500 + D, top - 26), (590 + D, top - 104), (668 + D, top - 22)
    f.path(f"M{hip[0]},{hip[1]} L{knee[0]},{knee[1]} L{heel[0]},{heel[1]}", stroke=INK, w=49, extra='stroke-linecap="round" stroke-linejoin="round"')
    f.path(f"M{hip[0]},{hip[1]} L{knee[0]},{knee[1]} L{heel[0]},{heel[1]}", stroke=trousers, w=44, extra='stroke-linecap="round" stroke-linejoin="round"')
    f.path(f"M{heel[0] - 12},{top - 4} L{heel[0] - 10},{top - 30} L{heel[0] + 14},{top - 30} Q{heel[0] + 48},{top - 22} {heel[0] + 50},{top - 4} Z", WHITE, INK, 2)  # foot in a sock
    # torso: back on the mattress, the shirt pulled up over the chest, the belly bare
    f.path(f"M{300 + D},{top - 4} L{300 + D},{top - 50} Q{320 + D},{top - 62} {372 + D},{top - 60} L{500 + D},{top - 52} Q{524 + D},{top - 30} {516 + D},{top - 4} Z", trousers, INK, 2.5)
    torso = (f"M{360 + D},{top - 4} L{360 + D},{top - 58} "
             f"A{br},{br} 0 0 1 {n(bc[0] + br * math.sin(math.radians(68)))},{n(bc[1] - br * math.cos(math.radians(68)))} "
             f"Q{500 + D},{top - 40} {492 + D},{top - 4} Z")
    f.path(torso, skin, INK, 2.5)
    f.path(f"M{482 + D},{top - 38} Q{496 + D},{top - 24} {494 + D},{top - 4}", stroke=trousers, w=12)          # waistband
    f.path(f"M{288 + D},{top - 4} L{288 + D},{top - 50} Q{300 + D},{top - 62} {340 + D},{top - 62} L{372 + D},{top - 66} "
           f"Q{378 + D},{top - 40} {372 + D},{top - 4} Z", shirt, INK, 2.5)
    # pulses going into the belly from the probe, clipped to the torso
    f.defs_add(f'<clipPath id="fy517h-belly"><path d="{torso}"/></clipPath>')
    pul = []
    for k, r in enumerate((20, 38, 56, 74)):
        a0, a1 = phi + math.pi / 2 + 0.75, phi + math.pi / 2 - 0.75 + 2 * 0.75 * 0   # an arc of ±43° around the inward direction
        ang_c = math.atan2(-nrm[1], -nrm[0])            # inward direction
        x1, y1 = pc[0] + r * math.cos(ang_c - 0.75), pc[1] + r * math.sin(ang_c - 0.75)
        x2, y2 = pc[0] + r * math.cos(ang_c + 0.75), pc[1] + r * math.sin(ang_c + 0.75)
        pul.append(f'<path d="M{n(x1)},{n(y1)} A{r},{r} 0 0 1 {n(x2)},{n(y2)}" fill="none" stroke="{WATER}" stroke-width="4" '
                   f'stroke-linecap="round" stroke-opacity="{0.95 - 0.2 * k:.2f}"/>')
    f.add(f'<g clip-path="url(#fy517h-belly)">{"".join(pul)}</g>')
    # the head on the wedge pillow (hair on the back of the head, the face up towards the screen), the near arm along the side
    f.rect(270 + D, top - 70, 34, 24, skin)
    f.circle(262 + D, top - 80, 34, skin, INK, 2)
    f.path(f"M{230 + D},{top - 66} Q{222 + D},{top - 106} {256 + D},{top - 114} Q{284 + D},{top - 118} {294 + D},{top - 96} "
           f"Q{270 + D},{top - 100} {258 + D},{top - 84} Q{250 + D},{top - 66} {246 + D},{top - 50} Q{234 + D},{top - 52} {230 + D},{top - 66} Z", INK)
    f.path(f"M{236 + D},{top - 56} Q{226 + D},{top - 40} {214 + D},{top - 36}", stroke=INK, w=10, extra='stroke-linecap="round"')   # hair on the pillow
    f.path(f"M{326 + D},{top - 44} L{372 + D},{top - 16} L{424 + D},{top - 12}", stroke=INK, w=25, extra='stroke-linecap="round" stroke-linejoin="round"')
    f.path(f"M{326 + D},{top - 44} L{372 + D},{top - 16}", stroke=shirt, w=20, extra='stroke-linecap="round"')
    f.path(f"M{372 + D},{top - 16} L{422 + D},{top - 12}", stroke=skin, w=17, extra='stroke-linecap="round"')
    # the gel on the skin and the probe square to it
    ga = math.degrees(phi)
    f.add(f'<g transform="translate({n(pc[0])} {n(pc[1])}) rotate({ga:.1f})">'
          f'<ellipse cx="0" cy="-1" rx="30" ry="8" fill="{ICE}" fill-opacity="0.85" stroke="{ICE_EDGE}" stroke-width="1.5"/>'
          f'<ellipse cx="-13" cy="-4" rx="8" ry="2.5" fill="{WHITE}" fill-opacity="0.9"/>'
          f'<path d="M-18,-4 L-16,-22 Q-12,-32 -9,-44 L-9,-82 Q0,-94 9,-82 L9,-44 Q12,-32 16,-22 L18,-4 Z" fill="{ALUMINIUM}" stroke="{INK}" stroke-width="2.5" stroke-linejoin="round"/>'
          f'<rect x="-18" y="-8" width="36" height="6" rx="2" fill="{INK}"/></g>')
    f.add('</g>')
    # the sonographer's near arm past the mother's head to the probe (bent, above the head)
    elbow1 = (704, 200)
    f.path(f"M{shl[0]},{shl[1]} L{elbow1[0]},{elbow1[1]}", stroke=scrub, w=21, extra='stroke-linecap="round"')
    f.path(f"M{elbow1[0]},{elbow1[1]} L{n(grip[0] - 6)},{n(grip[1])}", stroke=INK, w=21, extra='stroke-linecap="round"')
    f.path(f"M{elbow1[0]},{elbow1[1]} L{n(grip[0] - 6)},{n(grip[1])}", stroke=SAND_LIGHT, w=17, extra='stroke-linecap="round"')
    f.path(f"M{shl[0]},{shl[1]} L{elbow1[0] - 6},{elbow1[1]}", stroke=scrub, w=21, extra='stroke-linecap="round"')
    f.circle(grip[0] - 2, grip[1], 12, SAND_LIGHT, INK, 2)
    # a gel bottle on the cart
    f.rect(mx + 64, floor - 262, 24, 34, HEAT_LIGHT, INK, 2, 5)
    f.path(f"M{mx + 70},{floor - 262} L{mx + 76},{floor - 276} L{mx + 82},{floor - 262} Z", WHITE, INK, 2)
    f.rect(mx + 60, floor - 230, 36, 8, IRON, INK, 2, 2)
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
