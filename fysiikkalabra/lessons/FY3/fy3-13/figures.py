"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy3-13` writes them into lesson.md."""
from figlib import Fig
import herolib as H


def hero():
    """The chapter's opening illustration: the school experiment for absolute zero on a lab bench."""
    f = H.hero("fy313-hero", "Kuvitus: laboratoriopöydällä on kolme astiaa: jäävesi, huoneenlämpöinen vesi ja kuumalla levyllä "
               "kiehuva vesi. Keskimmäisessä hauteessa on suljettu lasipullo, joka on letkulla yhdistetty painemittariin.")
    f.rect(0, 0, 1200, 600, H.WHITE)
    for x in range(0, 1201, 80): f.line(x, 0, x, 420, H.RULE_LIGHT, 2)
    for y in range(0, 421, 80): f.line(0, y, 1200, y, H.RULE_LIGHT, 2)
    f.rect(0, 420, 1200, 26, H.RULE, H.INK, 3)
    f.rect(0, 446, 1200, 154, H.RULE_LIGHT)
    water = H.grad(f, "fy313h-water", H.WATER_LIGHT, H.WATER)

    def beaker(x, w, h, level):
        f.path(f"M{x},{420 - h} V410 Q{x},420 {x + 10},420 H{x + w - 10} Q{x + w},420 {x + w},410 V{420 - h}", H.GLASS)
        f.path(f"M{x + 3},{420 - level} H{x + w - 3} V410 Q{x + w - 3},417 {x + w - 10},417 H{x + 10} Q{x + 3},417 {x + 3},410 Z", water)
        f.path(f"M{x},{420 - h} V410 Q{x},420 {x + 10},420 H{x + w - 10} Q{x + w},420 {x + w},410 V{420 - h}", stroke=H.INK, w=3)
    # ice water
    beaker(80, 200, 170, 130)
    for k, (dx, dy) in enumerate(((30, 300), (80, 296), (130, 304), (60, 330), (110, 336))):
        f.rect(80 + dx, dy, 36, 30, H.ICE, H.ICE_EDGE, 2, 5)
    # bath with the flask and the gauge
    beaker(450, 300, 200, 160)
    f.path("M600,250 V150", stroke=H.INK, w=14)
    f.path("M600,250 V150", stroke=H.GLASS, w=8)
    f.circle(600, 320, 70, H.GLASS, H.INK, 3)
    f.circle(600, 320, 70, "none", H.WATER_LIGHT, 2)
    f.path("M600,150 Q600,96 680,96 H790", stroke=H.INK, w=10)
    f.circle(860, 120, 76, H.WHITE, H.INK, 4)
    for k in range(11):
        a = H.math.radians(140 + k * 26)
        f.line(860 + 58 * H.math.cos(a), 120 + 58 * H.math.sin(a), 860 + 68 * H.math.cos(a), 120 + 68 * H.math.sin(a), H.MUTED, 2.5)
    f.path("M860,120 L900,72", stroke=H.INK, w=5, extra='stroke-linecap="round"')
    f.circle(860, 120, 8, H.INK)
    f.rect(780, 120, 12, 300, H.IRON)
    f.rect(740, 408, 92, 12, H.IRON, rx=3)
    # boiling water on a hot plate
    f.rect(930, 400, 220, 20, H.IRON, H.INK, 3, 4)
    f.add(f'<ellipse cx="1040" cy="400" rx="120" ry="10" fill="{H.HOT}" fill-opacity="0.8"/>')
    f.path("M960,230 V380 Q960,392 972,392 H1108 Q1120,392 1120,380 V230", H.GLASS)
    f.path("M963,270 H1117 V380 Q1117,389 1108,389 H972 Q963,389 963,380 Z", water)
    for k in range(9):
        f.circle(975 + H.rnd(k, 4) * 130, 290 + H.rnd(k, 7) * 90, 4 + 5 * H.rnd(k, 9), H.WHITE, H.WATER, 1.5)
    f.path("M960,230 V380 Q960,392 972,392 H1108 Q1120,392 1120,380 V230", stroke=H.INK, w=3)
    for x in (1000, 1060):
        f.path(f"M{x},224 c14,-24 -14,-40 0,-70", stroke=H.RULE, w=20, extra='stroke-linecap="round" stroke-opacity="0.55"')
        f.path(f"M{x},224 c14,-24 -14,-40 0,-70", stroke=H.WHITE, w=14, extra='stroke-linecap="round"')
    return f.svg()


def thermometer():
    """Hand-pasted figure of the lesson, kept as it was (work queue 24: moved into figures.py before the picture swap)."""
    f = Fig('fy313-thermometer', 372, 'Kaasulämpömittari: suljettu lasipullo, jossa on ilmaa, on vesihauteessa, jota lämmitetään. Pullon kaasun tilavuus ei muutu. Vesihauteen lämpötila luetaan lämpömittarista ja kaasun paine painemittarista. Kuva on kaavio eikä mittakaavassa.', width=600)
    f.defs_add('<linearGradient id="fy313-water" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#a9d1f0"/><stop offset="1" stop-color="#2f74b5"/></linearGradient><linearGradient id="fy313-heat" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffc078"/><stop offset="1" stop-color="#e8590c"/></linearGradient>')
    f.add('<path d="M60,140 V296 Q60,312 76,312 H284 Q300,312 300,296 V140 Z" fill="#eef5f9"/>')
    f.add('<path d="M62,170 Q90,162 118,170 T174,170 T230,170 T286,170 L298,170 V296 Q298,310 284,310 H76 Q62,310 62,296 Z" fill="url(#fy313-water)"/>')
    f.add('<path d="M64,170 Q90,163 118,170 T174,170 T230,170 T296,170" fill="none" stroke="#ffffff" stroke-width="2.5" stroke-opacity="0.8"/>')
    f.add('<path d="M60,140 V296 Q60,312 76,312 H284 Q300,312 300,296 V140" fill="none" stroke="#1f2933" stroke-width="3"/>')
    f.add('<rect x="192" y="60" width="246" height="16" fill="#eef5f9" stroke="#1f2933" stroke-width="3"/>')
    f.add('<path d="M192,76 V196.6 A50,50 0 1 0 208,196.6 V76" fill="#eef5f9" stroke="#1f2933" stroke-width="3"/>')
    f.add('<rect x="194" y="73" width="12" height="6" fill="#eef5f9"/>')
    f.add('<circle cx="176" cy="236" r="4" fill="#6b7480"/>')
    f.add('<circle cx="200" cy="224" r="4" fill="#6b7480"/>')
    f.add('<circle cx="222" cy="240" r="4" fill="#6b7480"/>')
    f.add('<circle cx="188" cy="262" r="4" fill="#6b7480"/>')
    f.add('<circle cx="214" cy="270" r="4" fill="#6b7480"/>')
    f.add('<circle cx="168" cy="274" r="4" fill="#6b7480"/>')
    f.add('<circle cx="238" cy="262" r="4" fill="#6b7480"/>')
    f.add('<circle cx="200" cy="248" r="4" fill="#6b7480"/>')
    f.add('<circle cx="230" cy="286" r="4" fill="#6b7480"/>')
    f.add('<circle cx="184" cy="286" r="4" fill="#6b7480"/>')
    f.add('<line x1="176" y1="236" x2="164" y2="242" stroke="#6b7480" stroke-width="2"/>')
    f.add('<line x1="222" y1="240" x2="234" y2="232" stroke="#6b7480" stroke-width="2"/>')
    f.add('<line x1="214" y1="270" x2="224" y2="280" stroke="#6b7480" stroke-width="2"/>')
    f.add('<line x1="168" y1="274" x2="158" y2="266" stroke="#6b7480" stroke-width="2"/>')
    f.add('<line x1="200" y1="224" x2="204" y2="212" stroke="#6b7480" stroke-width="2"/>')
    f.add('<rect x="100" y="122" width="10" height="158" rx="5" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>')
    f.add('<g stroke="#6b7480" stroke-width="1.5"><line x1="110" y1="140" x2="116" y2="140"/><line x1="110" y1="156" x2="116" y2="156"/><line x1="110" y1="172" x2="116" y2="172"/><line x1="110" y1="188" x2="116" y2="188"/><line x1="110" y1="204" x2="116" y2="204"/><line x1="110" y1="220" x2="116" y2="220"/><line x1="110" y1="236" x2="116" y2="236"/><line x1="110" y1="252" x2="116" y2="252"/><line x1="110" y1="268" x2="116" y2="268"/></g>')
    f.add('<rect x="103" y="196" width="4" height="86" fill="#c92a2a"/><circle cx="105" cy="288" r="11" fill="#c92a2a" stroke="#1f2933" stroke-width="2"/>')
    f.tex(105, 103, '\\theta', 'middle', w=60)
    f.add('<circle cx="490" cy="68" r="52" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>')
    f.add('<line x1="457.5" y1="100.5" x2="464.5" y2="93.5" stroke="#6b7480" stroke-width="2.5"/>')
    f.add('<line x1="445.6" y1="79.9" x2="455.2" y2="77.3" stroke="#6b7480" stroke-width="2.5"/>')
    f.add('<line x1="445.6" y1="56.1" x2="455.2" y2="58.7" stroke="#6b7480" stroke-width="2.5"/>')
    f.add('<line x1="457.5" y1="35.5" x2="464.5" y2="42.5" stroke="#6b7480" stroke-width="2.5"/>')
    f.add('<line x1="478.1" y1="23.6" x2="480.7" y2="33.2" stroke="#6b7480" stroke-width="2.5"/>')
    f.add('<line x1="501.9" y1="23.6" x2="499.3" y2="33.2" stroke="#6b7480" stroke-width="2.5"/>')
    f.add('<line x1="522.5" y1="35.5" x2="515.5" y2="42.5" stroke="#6b7480" stroke-width="2.5"/>')
    f.add('<line x1="534.4" y1="56.1" x2="524.8" y2="58.7" stroke="#6b7480" stroke-width="2.5"/>')
    f.add('<line x1="534.4" y1="79.9" x2="524.8" y2="77.3" stroke="#6b7480" stroke-width="2.5"/>')
    f.add('<line x1="522.5" y1="100.5" x2="515.5" y2="93.5" stroke="#6b7480" stroke-width="2.5"/>')
    f.add('<line x1="490" y1="68" x2="515.7" y2="37.4" stroke="#1f2933" stroke-width="3.5" stroke-linecap="round"/><circle cx="490" cy="68" r="5" fill="#1f2933"/>')
    f.tex(490, 145, 'p', 'middle', w=60)
    f.tex(490, 186, '\\text{painemittari}', 'middle', w=220)
    f.add('<rect x="60" y="316" width="240" height="14" rx="3" fill="#6c757d"/>')
    f.add('<path d="M105,362 V348 H98 L110,334 L122,348 H115 V362 Z" fill="url(#fy313-heat)"/>')
    f.add('<path d="M175,362 V348 H168 L180,334 L192,348 H185 V362 Z" fill="url(#fy313-heat)"/>')
    f.add('<path d="M245,362 V348 H238 L250,334 L262,348 H255 V362 Z" fill="url(#fy313-heat)"/>')
    f.tex(316, 353, 'Q', 'start', w=50)
    f.tex(320, 226, '\\text{vesihaude}', 'start', w=160)
    f.add('<line x1="316" y1="226" x2="272" y2="226" stroke="#1f2933" stroke-width="2"/>')
    f.tex(320, 270, '\\text{ilma},\\ V=\\text{vakio}', 'start', w=270)
    f.add('<line x1="316" y1="270" x2="254" y2="270" stroke="#1f2933" stroke-width="2"/>')
    return f.svg()


FIGURES = {"hero": hero, "thermometer": thermometer}
