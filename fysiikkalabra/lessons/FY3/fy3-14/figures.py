"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy3-14` writes them into lesson.md."""
import herolib as H
from figlib import Fig, INK, RULE_LIGHT, HOT, HOT_LIGHT, COLD, COLD_LIGHT, ICE, ICE_EDGE, fi


def hero():
    """The chapter's opening illustration: a glass of a cold drink with ice cubes, dew on the glass."""
    f = H.hero("fy314-hero", "Kuvitus: pöydällä on korkea lasi kylmää juomaa, jossa kelluu jääpaloja ja pilli. Lasin "
               "ulkopinnalle on tiivistynyt vesipisaroita, ja lasin vieressä on jääpalarasia.")
    f.rect(0, 0, 1200, 600, H.PAPER)
    f.rect(0, 0, 1200, 430, H.grad(f, "fy314h-wall", H.WHITE, H.PAPER))
    f.rect(0, 520, 1200, 80, H.RULE)
    f.line(0, 520, 1200, 520, H.INK, 3)
    # Composition tightened (teacher 2026-11-11, illustration audit): the glass and the tray drawn 1,2 times larger and
    # closer, the table lower, so the subject fills the middle of the picture instead of a third of it.
    f.add('<g transform="matrix(1.2 0 0 1.2 -180 -46)">')
    # glass, drink, ice cubes, straw
    f.path("M500,110 L520,460 Q522,474 536,474 H664 Q678,474 680,460 L700,110 Z", H.GLASS)
    drink = H.grad(f, "fy314h-drink", H.COLD_LIGHT, H.WATER_LIGHT)
    f.path("M506,190 L521,458 Q523,470 536,470 H664 Q677,470 679,458 L694,190 Z", drink)
    f.path("M640,60 L600,440", stroke=H.COLD, w=14, extra='stroke-linecap="round"')
    for x, y, a in ((540, 170, -12), (600, 184, 10), (560, 240, 24), (628, 250, -8)):
        f.add(f'<rect x="{x}" y="{y}" width="52" height="46" rx="8" transform="rotate({a} {x + 26} {y + 23})" fill="{H.ICE}" fill-opacity="0.9" stroke="{H.ICE_EDGE}" stroke-width="2.5"/>')
    f.path("M506,190 Q560,182 600,190 T694,190", stroke=H.WHITE, w=3, extra='stroke-opacity="0.8"')
    f.path("M500,110 L520,460 Q522,474 536,474 H664 Q678,474 680,460 L700,110", stroke=H.INK, w=3)
    for k in range(16):
        x = 512 + H.rnd(k, 5) * 176; y = 210 + H.rnd(k, 8) * 240
        f.add(f'<ellipse cx="{H.n(x)}" cy="{H.n(y)}" rx="4" ry="6" fill="{H.WHITE}" stroke="{H.ICE_EDGE}" stroke-width="1.5"/>')
    # ice tray beside the glass, cold air sinking
    f.rect(760, 430, 260, 40, H.COLD_LIGHT, H.INK, 3, 6)
    for x in range(776, 1000, 56): f.rect(x, 420, 42, 30, H.ICE, H.ICE_EDGE, 2, 5)
    for x in (430, 730):
        f.path(f"M{x},200 c-14,30 14,60 0,90 s14,60 0,90", stroke=H.COLD_LIGHT, w=6, extra='stroke-linecap="round"')
    f.add('</g>')
    return f.svg()


def energy_bars():
    """A task-only picture, to scale: three heats of one water-and-ice mixture as horizontal bars on a kJ axis, grid every
    5 kJ. The water gives off 25 kJ cooling to 0 °C, warming the ice to 0 °C needs 5 kJ and melting all of it 60 kJ."""
    f = Fig("fy314-bars", 290, "Pylväskuvaaja mittakaavassa: kolme lämpömäärää kilojouleina samasta seoksesta, jossa on vettä ja "
            "pakkasessa ollutta jäätä. Ruudukon väli on 5 kJ ja numerot joka 10 kJ:n kohdalla. Ylin pylväs, veden luovuttama "
            "lämpömäärä sen jäähtyessä 0 °C:seen, päättyy kohtaan 25 kJ. Keskimmäinen, jään lämmittämiseen 0 °C:seen tarvittava "
            "lämpömäärä, päättyy kohtaan 5 kJ. Alin, kaiken jään sulattamiseen tarvittava lämpömäärä, päättyy kohtaan 60 kJ.")
    X = lambda q: 30 + q * 6.6
    ya = 236
    for q in range(0, 71, 5):
        f.line(X(q), 20, X(q), ya, RULE_LIGHT, 1.5)
    bars = [(25, HOT_LIGHT, HOT, r"\text{vesi luovuttaa jäähtyessään } 0\,{}^\circ\text{C}\text{:seen}"),
            (5, COLD_LIGHT, COLD, r"\text{jään lämmittäminen } 0\,{}^\circ\text{C}\text{:seen}"),
            (60, ICE, ICE_EDGE, r"\text{kaiken jään sulattaminen}")]
    for k, (q, fill, edge, label) in enumerate(bars):
        y = 50 + k * 66
        f.tex(X(0) + 4, y - 16, label, "start", bg=True)
        f.rect(X(0), y, X(q) - X(0), 28, fill, edge, 2.5)
    f.arrow(X(0), ya, X(70) + 24, ya, INK, 2.5, 13)
    for q in range(0, 71, 5):
        f.line(X(q), ya, X(q), ya + 7, INK, 2)
        if q % 10 == 0:
            f.tex(X(q), ya + 26, fi(q), "middle")
    f.tex(X(70) + 30, ya, r"Q\ (\text{kJ})", "start")
    return f.svg()


def before_after():
    """Hand-pasted figure of the lesson, kept as it was (work queue 24: moved into figures.py before the picture swap)."""
    f = Fig('fy314-before-after', 344, 'Kaavakuva ennen ja jälkeen: eristetyssä astiassa on aluksi 0,30 kg vettä lämpötilassa 20 °C ja 0,10 kg jäätä lämpötilassa 0 °C. Lämpöä Q siirtyy vedestä jäähän. Tasapainossa lämpömittari näyttää 0 °C, vettä on 0,375 kg ja jäätä on jäljellä enää 0,025 kg. Jääpalojen yhteenlaskettu pinta-ala on mittakaavassa jään massaan nähden.', width=600)
    f.defs_add('<linearGradient id="fy314-water" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#a9d1f0"/><stop offset="1" stop-color="#2f74b5"/></linearGradient><linearGradient id="fy314-heat" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffc078"/><stop offset="1" stop-color="#e8590c"/></linearGradient>')
    f.add('<path d="M78,96 V250 Q78,262 90,262 H216 Q228,262 228,250 V96 Z" fill="#eef5f9"/>')
    f.add('<path d="M80,138 Q98.25,131 116.5,138 T153.0,138 T189.5,138 T226,138 V250 Q226,260 214,260 H92 Q80,260 80,250 Z" fill="url(#fy314-water)"/>')
    f.add('<path d="M83,138 Q98.25,132 116.5,138 T153.0,138 T189.5,138 T223,138" fill="none" stroke="#ffffff" stroke-width="2.5" stroke-opacity="0.8"/>')
    f.add('<rect x="84.0" y="120.0" width="30" height="30" rx="4.0" fill="#a5d8ff" stroke="#4f8fbf" stroke-width="2.5"/>')
    f.add('<path d="M90.0,132.6 V126.0 H96.6" fill="none" stroke="#ffffff" stroke-width="2" stroke-linecap="round"/>')
    f.add('<rect x="120.0" y="120.0" width="30" height="30" rx="4.0" fill="#a5d8ff" stroke="#4f8fbf" stroke-width="2.5"/>')
    f.add('<path d="M126.0,132.6 V126.0 H132.6" fill="none" stroke="#ffffff" stroke-width="2" stroke-linecap="round"/>')
    f.add('<rect x="156.0" y="120.0" width="30" height="30" rx="4.0" fill="#a5d8ff" stroke="#4f8fbf" stroke-width="2.5"/>')
    f.add('<path d="M162.0,132.6 V126.0 H168.6" fill="none" stroke="#ffffff" stroke-width="2" stroke-linecap="round"/>')
    f.add('<rect x="192.0" y="120.0" width="30" height="30" rx="4.0" fill="#a5d8ff" stroke="#4f8fbf" stroke-width="2.5"/>')
    f.add('<path d="M198.0,132.6 V126.0 H204.6" fill="none" stroke="#ffffff" stroke-width="2" stroke-linecap="round"/>')
    f.add('<path d="M147.0,232 V196 H138.0 L153.0,172 L168.0,196 H159.0 V232 Z" fill="url(#fy314-heat)"/>')
    f.add('<rect x="173.0" y="192" width="40" height="36" rx="6" fill="#ffffff" fill-opacity="0.88"/>')
    f.tex(193, 210, 'Q', 'middle', size=20, w=40)
    f.add('<path d="M78,96 V250 Q78,262 90,262 H216 Q228,262 228,250 V96" fill="none" stroke="#1f2933" stroke-width="3"/>')
    f.add('<rect x="41" y="96" width="14" height="170" rx="7" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>')
    f.add('<g stroke="#6b7480" stroke-width="1.5"><line x1="35" y1="232" x2="41" y2="232"/><line x1="35" y1="192" x2="41" y2="192"/><line x1="35" y1="152" x2="41" y2="152"/><line x1="35" y1="112" x2="41" y2="112"/></g>')
    f.add('<rect x="45" y="152" width="6" height="106" fill="#c92a2a"/>')
    f.add('<circle cx="48" cy="258" r="12" fill="#c92a2a" stroke="#1f2933" stroke-width="2"/>')
    f.add('<foreignObject x="-2" y="218" width="34" height="28"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:right;color:#6b7480">$0$</div></foreignObject>')
    f.add('<foreignObject x="-2" y="178" width="34" height="28"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:right;color:#6b7480">$10$</div></foreignObject>')
    f.add('<foreignObject x="-2" y="138" width="34" height="28"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:right;color:#6b7480">$20$</div></foreignObject>')
    f.add('<foreignObject x="-2" y="98" width="34" height="28"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:right;color:#6b7480">$30$</div></foreignObject>')
    f.tex(48, 74, '20\\,{}^\\circ\\text{C}', 'middle', size=20, w=80)
    f.tex(153, 23, '\\text{alussa}', 'middle', size=20, w=200)
    f.tex(153, 293, '\\text{vesi } 0{,}30\\,\\text{kg},\\ 20\\,{}^\\circ\\text{C}', 'middle', size=20, w=244)
    f.tex(153, 326, '\\text{jää } 0{,}10\\,\\text{kg},\\ 0\\,{}^\\circ\\text{C}', 'middle', size=20, w=244)
    f.add('<path d="M252,166 H306 V152 L334,174 L306,196 V182 H252 Z" fill="#1f2933"/>')
    f.add('<path d="M400,96 V250 Q400,262 412,262 H538 Q550,262 550,250 V96 Z" fill="#eef5f9"/>')
    f.add('<path d="M402,138 Q420.25,131 438.5,138 T475.0,138 T511.5,138 T548,138 V250 Q548,260 536,260 H414 Q402,260 402,250 Z" fill="url(#fy314-water)"/>')
    f.add('<path d="M405,138 Q420.25,132 438.5,138 T475.0,138 T511.5,138 T545,138" fill="none" stroke="#ffffff" stroke-width="2.5" stroke-opacity="0.8"/>')
    f.add('<rect x="413.5" y="129.0" width="15" height="15" rx="3.8" fill="#a5d8ff" stroke="#4f8fbf" stroke-width="2.5"/>')
    f.add('<path d="M416.5,135.3 V132.0 H419.8" fill="none" stroke="#ffffff" stroke-width="2" stroke-linecap="round"/>')
    f.add('<rect x="449.5" y="129.0" width="15" height="15" rx="3.8" fill="#a5d8ff" stroke="#4f8fbf" stroke-width="2.5"/>')
    f.add('<path d="M452.5,135.3 V132.0 H455.8" fill="none" stroke="#ffffff" stroke-width="2" stroke-linecap="round"/>')
    f.add('<rect x="485.5" y="129.0" width="15" height="15" rx="3.8" fill="#a5d8ff" stroke="#4f8fbf" stroke-width="2.5"/>')
    f.add('<path d="M488.5,135.3 V132.0 H491.8" fill="none" stroke="#ffffff" stroke-width="2" stroke-linecap="round"/>')
    f.add('<rect x="521.5" y="129.0" width="15" height="15" rx="3.8" fill="#a5d8ff" stroke="#4f8fbf" stroke-width="2.5"/>')
    f.add('<path d="M524.5,135.3 V132.0 H527.8" fill="none" stroke="#ffffff" stroke-width="2" stroke-linecap="round"/>')
    f.add('<path d="M400,96 V250 Q400,262 412,262 H538 Q550,262 550,250 V96" fill="none" stroke="#1f2933" stroke-width="3"/>')
    f.add('<rect x="363" y="96" width="14" height="170" rx="7" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>')
    f.add('<g stroke="#6b7480" stroke-width="1.5"><line x1="357" y1="232" x2="363" y2="232"/><line x1="357" y1="192" x2="363" y2="192"/><line x1="357" y1="152" x2="363" y2="152"/><line x1="357" y1="112" x2="363" y2="112"/></g>')
    f.add('<rect x="367" y="232" width="6" height="26" fill="#1971c2"/>')
    f.add('<circle cx="370" cy="258" r="12" fill="#1971c2" stroke="#1f2933" stroke-width="2"/>')
    f.tex(354, 232, '0', 'end', color='#6b7480', size=20, w=34)
    f.tex(370, 74, '0\\,{}^\\circ\\text{C}', 'middle', size=20, w=80)
    f.tex(475, 23, '\\text{tasapainossa}', 'middle', size=20, w=200)
    f.tex(475, 293, '\\text{vesi } 0{,}375\\,\\text{kg},\\ 0\\,{}^\\circ\\text{C}', 'middle', size=20, w=244)
    f.tex(475, 326, '\\text{jää } 0{,}025\\,\\text{kg},\\ 0\\,{}^\\circ\\text{C}', 'middle', size=20, w=244)
    return f.svg()


def energy_balance():
    """Hand-pasted figure of the lesson, kept as it was (work queue 24: moved into figures.py before the picture swap)."""
    f = Fig('fy314-energy-balance', 392, 'Energiataseen palkit mittakaavassa, kilojouleina: 0,30 kg vettä lämpötilassa 20 °C luovuttaa jäähtyessään 0 °C:seen 25.1 kJ. 0,10 kg jäätä lämpötilassa −10 °C tarvitsee lämpenemiseen 0 °C:seen 2.1 kJ ja sulamiseen 33.4 kJ eli yhteensä 35.5 kJ. Veden lämpö ei riitä: palkin vaalea osa kuvaa jäätä, joka ei ehdi sulaa.', width=600)
    f.defs_add('<linearGradient id="fy314-heat2" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffc078"/><stop offset="1" stop-color="#e8590c"/></linearGradient>')
    f.add('<line x1="100" y1="272.0" x2="590" y2="272.0" stroke="#e3dccb" stroke-width="1.5"/>')
    f.add('<line x1="100" y1="212.0" x2="590" y2="212.0" stroke="#e3dccb" stroke-width="1.5"/>')
    f.add('<line x1="100" y1="152.0" x2="590" y2="152.0" stroke="#e3dccb" stroke-width="1.5"/>')
    f.add('<line x1="100" y1="92.0" x2="590" y2="92.0" stroke="#e3dccb" stroke-width="1.5"/>')
    f.add('<line x1="100" y1="332" x2="590" y2="332" stroke="#1f2933" stroke-width="2.5"/><line x1="100" y1="68.0" x2="100" y2="332" stroke="#1f2933" stroke-width="2.5"/>')
    f.tex(92, 332, '0', 'end', color='#6b7480', size=20, w=56)
    f.tex(92, 272, '10', 'end', color='#6b7480', size=20, w=56)
    f.tex(92, 212, '20', 'end', color='#6b7480', size=20, w=56)
    f.tex(92, 152, '30', 'end', color='#6b7480', size=20, w=56)
    f.tex(92, 92, '40', 'end', color='#6b7480', size=20, w=56)
    f.tex(20, 23, 'Q\\ (\\text{kJ})', 'start', size=20, w=150)
    f.tex(596, 20, '\\text{vesi } 0{,}30\\,\\text{kg},\\ 20\\,{}^\\circ\\text{C}', 'end', size=20, w=306)
    f.tex(596, 56, '\\text{jää } 0{,}10\\,\\text{kg},\\ {-10}\\,{}^\\circ\\text{C}', 'end', size=20, w=306)
    f.add('<rect x="150" y="181.2" width="100" height="150.8" rx="3" fill="url(#fy314-heat2)" stroke="#1f2933" stroke-width="2"/>')
    f.add('<rect x="350" y="319.4" width="100" height="12.6" fill="#1971c2" stroke="#1f2933" stroke-width="2"/>')
    f.add('<rect x="350" y="181.2" width="100" height="138.2" fill="#a5d8ff" stroke="#4f8fbf" stroke-width="2"/>')
    f.add('<rect x="350" y="119.0" width="100" height="62.2" fill="#a5d8ff" fill-opacity="0.35" stroke="#4f8fbf" stroke-width="2" stroke-dasharray="7 5"/>')
    f.add('<line x1="250" y1="181.2" x2="460" y2="181.2" stroke="#1f2933" stroke-width="2" stroke-dasharray="7 5"/>')
    f.add('<path d="M460,119.0 H466 V181.2 H460" fill="none" stroke="#1f2933" stroke-width="2.5"/>')
    f.tex(472, 150.08, '\\text{jäätä jää}', 'start', size=20, w=128)
    f.tex(401, 170.08, 's\\,m_\\text{j}', 'middle', size=20, w=90)
    f.tex(472, 309.7, '\\text{lämmitys}', 'start', size=20, w=120)
    f.add('<line x1="450" y1="325.7" x2="468" y2="309.7" stroke="#6b7480" stroke-width="1.5"/>')
    f.tex(200, 160.16, '25{,}1\\,\\text{kJ}', 'middle', size=20, w=140)
    f.tex(400, 98, '35{,}5\\,\\text{kJ}', 'middle', size=20, w=140)
    f.tex(200, 355, '\\text{vesi luovuttaa}', 'middle', size=20, w=180)
    f.tex(400, 355, '\\text{jää tarvitsee}', 'middle', size=20, w=180)
    return f.svg()


FIGURES = {"hero": hero, "energy-bars": energy_bars, "before-after": before_after, "energy-balance": energy_balance}

REUSE = {
    "energy-bars": "safe: three heats of a water-and-ice mixture as bars, which melts and how much is to be worked out",
}
