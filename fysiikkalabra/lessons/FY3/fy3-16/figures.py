"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy3-16` writes them into lesson.md."""
from figlib import Fig
import herolib as H


def hero():
    """The chapter's opening illustration: a cool bag with an ice pack and drinks at a beach picnic."""
    f = H.hero("fy316-hero", "Kuvitus: helteinen rantapiknik. Viltillä on avoin kylmälaukku, jossa on jääpussi ja juomapulloja. "
               "Aurinko paistaa, ja taustalla on järvi.")
    H.sky(f, "fy316h", 330)
    H.sun(f, "fy316h", 1030, 100)
    H.cloud(f, 420, 90, 0.8)
    H.forest(f, 300, 40, 24, H.METAL_EDGE, seed=4, depth=40)
    f.rect(0, 320, 1200, 100, H.grad(f, "fy316h-lake", H.WATER_LIGHT, H.WATER))
    f.path("M0,400 Q600,370 1200,410 V600 H0 Z", H.grad(f, "fy316h-sand", H.SAND_LIGHT, H.SAND))
    # picnic blanket
    f.path("M150,600 L310,440 H950 L1100,600 Z", H.WHITE, H.INK, 3)
    for k in range(1, 8):
        t = k / 8
        f.line(310 + 640 * t, 440, 150 + 950 * t, 600, H.COLD_LIGHT, 18)
    for y in (493, 547): f.line(150 + (600 - y), y, 1100 - (600 - y) * 150 / 160, y, H.COLD_LIGHT, 18)
    f.path("M150,600 L310,440 H950 L1100,600 Z", stroke=H.INK, w=3)
    # cool bag, open
    f.rect(470, 390, 300, 160, H.COLD, H.INK, 3, 12)
    f.rect(470, 450, 300, 20, H.WHITE)
    f.path("M470,390 L500,300 H800 L770,390 Z", H.grad(f, "fy316h-lid", H.COLD_LIGHT, H.COLD), H.INK, 3)
    f.path("M560,300 Q620,250 680,300", stroke=H.INK, w=8)
    f.rect(490, 380, 120, 40, H.ICE, H.ICE_EDGE, 2.5, 12)
    for x in (630, 680, 724):
        f.rect(x, 330, 34, 80, H.GLASS, H.INK, 2.5, 8)
        f.rect(x + 3, 352, 28, 56, H.WATER_LIGHT, rx=6)
        f.rect(x + 9, 316, 16, 18, H.COLD, H.INK, 2)
    H.shimmer(f, (240, 1000), 430, 70)
    return f.svg()


def cool_bag():
    """Hand-pasted figure of the lesson, kept as it was (work queue 24: moved into figures.py before the picture swap)."""
    f = Fig('fy316-cool-bag', 340, 'Kuva kylmälaukusta ja energiankulutuksesta. Vasemmalla kylmälaukun poikkileikkaus: ulkona on 28 °C, sisällä jääpussi ja juomapulloja 0 °C:ssa, ja seinien läpi virtaa sisään lämpöteho P kahdella yhtä suurella nuolella. Oikealla pylväät samassa mittakaavassa yhdelle kilogramman massalle: jään sulattaminen vaatii 334 kJ, veden lämmittäminen 10 K:lla 42 kJ ja 80 K:lla 335 kJ, joten sulaminen vie yhtä paljon energiaa kuin 80 kelvinin lämpeneminen.', width=600)
    f.defs_add('<linearGradient id="fy316a-heat" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#ffc078"/><stop offset="1" stop-color="#e8590c"/></linearGradient><linearGradient id="fy316a-heatv" x1="0" y1="1" x2="0" y2="0"><stop offset="0" stop-color="#e8590c"/><stop offset="1" stop-color="#ffc078"/></linearGradient><linearGradient id="fy316a-water" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#a9d1f0"/><stop offset="1" stop-color="#2f74b5"/></linearGradient>')
    f.add('<path d="M96,66 Q146,34 196,66" fill="none" stroke="#1f2933" stroke-width="3.5" stroke-linecap="round"/>')
    f.add('<rect x="42" y="84" width="208" height="196" rx="16" fill="#c9c2b2" stroke="#1f2933" stroke-width="3"/>')
    f.add('<rect x="58" y="100" width="176" height="164" rx="8" fill="#eef5f9" stroke="#1f2933" stroke-width="2.5"/>')
    f.add('<line x1="42" y1="100" x2="250" y2="100" stroke="#1f2933" stroke-width="2.5"/>')
    f.add('<rect x="72" y="204" width="76" height="54" rx="7" fill="#a5d8ff" stroke="#4f8fbf" stroke-width="2.5"/><path d="M82,216 L98,214 M84,230 L104,226" stroke="#ffffff" stroke-width="3" stroke-linecap="round"/>')
    f.add('<path d="M166,204 V190 Q166,184 170,184 Q174,184 174,190 V204 Q182,208 182,218 V252 Q182,258 177,258 H163 Q158,258 158,252 V218 Q158,208 166,204 Z" fill="url(#fy316a-water)" stroke="#1f2933" stroke-width="2.5"/>')
    f.add('<path d="M202,204 V190 Q202,184 206,184 Q210,184 210,190 V204 Q218,208 218,218 V252 Q218,258 213,258 H199 Q194,258 194,252 V218 Q194,208 202,204 Z" fill="url(#fy316a-water)" stroke="#1f2933" stroke-width="2.5"/>')
    f.tex(110, 188, '\\text{jää}', 'middle', w=70)
    f.tex(145, 128, '0\\,{}^\\circ\\text{C}', 'middle', color='#1971c2', w=150)
    f.add('<path d="M2,183.25 H29.0 V175.0 L56,190 L29.0,205.0 V196.75 H2 Z" fill="url(#fy316a-heat)"/>')
    f.add('<path d="M298,183.25 H271.0 V175.0 L244,190 L271.0,205.0 V196.75 H298 Z" fill="url(#fy316a-heat)"/>')
    f.tex(4, 150, 'P', 'start', w=44)
    f.tex(294, 150, 'P', 'end', w=44)
    f.tex(151, 314, '28\\,{}^\\circ\\text{C}', 'middle', color='#c92a2a', w=230)
    f.add('<line x1="304" y1="16" x2="304" y2="330" stroke="#c9c2b2" stroke-width="2" stroke-dasharray="6 6"/>')
    f.tex(318, 23, 'Q\\ (\\text{kJ}),\\ m = 1{,}0\\,\\text{kg}', 'start', w=270)
    f.add('<line x1="324" y1="286" x2="588" y2="286" stroke="#1f2933" stroke-width="2.5"/>')
    f.add('<rect x="340" y="116.5" width="52" height="169.5" rx="3" fill="url(#fy316a-heatv)" stroke="#1f2933" stroke-width="2"/>')
    f.tex(366, 100.5, '334', 'middle', w=60)
    f.tex(366, 308, '\\text{sulaa}', 'middle', w=85)
    f.add('<rect x="430" y="264.7" width="52" height="21.3" rx="3" fill="url(#fy316a-heatv)" stroke="#1f2933" stroke-width="2"/>')
    f.tex(456, 248.7, '42', 'middle', w=60)
    f.tex(456, 310, '+10\\,\\text{K}', 'middle', w=88)
    f.add('<rect x="520" y="115.9" width="52" height="170.1" rx="3" fill="url(#fy316a-heatv)" stroke="#1f2933" stroke-width="2"/>')
    f.tex(546, 99.9, '335', 'middle', w=60)
    f.tex(546, 310, '+80\\,\\text{K}', 'middle', w=88)
    f.add('<line x1="392" y1="116.5" x2="546" y2="116.5" stroke="#6b7480" stroke-width="2" stroke-dasharray="5 5"/>')
    return f.svg()


def cooling_circuit():
    """Hand-pasted figure of the lesson, kept as it was (work queue 24: moved into figures.py before the picture swap)."""
    f = Fig('fy316-cooling-circuit', 340, 'Kaaviokuva moottorin jäähdytyspiiristä. Moottorista siirtyy hukkalämpöä lämpötehona P nesteeseen, neste kulkee yläputkea pitkin jäähdyttimelle lämpötilassa T2 ja palaa alaputkea pumpun kautta lämpötilassa T1, ja jäähdytin luovuttaa saman tehon P ilmaan. Nesteen massavirta on m/t. Kuva on kaavio eikä mittakaavassa.', width=600)
    f.defs_add('<linearGradient id="fy316c-heat" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#ffc078"/><stop offset="1" stop-color="#e8590c"/></linearGradient>')
    f.add('<path d="M190,130 H408" stroke="#1f2933" stroke-width="20" fill="none"/>')
    f.add('<path d="M190,130 H408" stroke="#c92a2a" stroke-width="13" fill="none"/>')
    f.add('<path d="M408,214 H190" stroke="#1f2933" stroke-width="20" fill="none"/>')
    f.add('<path d="M408,214 H190" stroke="#1971c2" stroke-width="13" fill="none"/>')
    f.add('<path d="M312,118 L334,130 L312,142 Z" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>')
    f.add('<path d="M252,202 L230,214 L252,226 Z" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>')
    f.add('<circle cx="330" cy="214" r="22" fill="#eef5f9" stroke="#1f2933" stroke-width="3"/><path d="M342,226 V202 L318,214 Z" fill="#1f2933"/>')
    f.add('<rect x="96" y="96" width="94" height="152" rx="8" fill="#6c757d" stroke="#1f2933" stroke-width="3"/>')
    f.add('<rect x="110" y="112" width="16" height="44" rx="3" fill="#c4ccd4" stroke="#1f2933" stroke-width="1.5"/>')
    f.add('<rect x="135" y="112" width="16" height="44" rx="3" fill="#c4ccd4" stroke="#1f2933" stroke-width="1.5"/>')
    f.add('<rect x="160" y="112" width="16" height="44" rx="3" fill="#c4ccd4" stroke="#1f2933" stroke-width="1.5"/>')
    f.add('<rect x="408" y="96" width="94" height="152" rx="8" fill="#c4ccd4" stroke="#1f2933" stroke-width="3"/>')
    f.add('<line x1="424" y1="108" x2="424" y2="236" stroke="#1f2933" stroke-width="2"/>')
    f.add('<line x1="438" y1="108" x2="438" y2="236" stroke="#1f2933" stroke-width="2"/>')
    f.add('<line x1="452" y1="108" x2="452" y2="236" stroke="#1f2933" stroke-width="2"/>')
    f.add('<line x1="466" y1="108" x2="466" y2="236" stroke="#1f2933" stroke-width="2"/>')
    f.add('<line x1="480" y1="108" x2="480" y2="236" stroke="#1f2933" stroke-width="2"/>')
    f.add('<line x1="494" y1="108" x2="494" y2="236" stroke="#1f2933" stroke-width="2"/>')
    f.tex(143, 270, '\\text{moottori}', 'middle', w=124)
    f.tex(455, 270, '\\text{jäähdytin}', 'middle', w=137)
    f.add('<path d="M106,172.8 H137.0 V164.0 L168,180 L137.0,196.0 V187.2 H106 Z" fill="url(#fy316c-heat)"/>')
    f.add('<path d="M510,164.8 H541.0 V156.0 L572,172 L541.0,188.0 V179.2 H510 Z" fill="url(#fy316c-heat)"/>')
    f.tex(112, 218, 'P', 'start', w=50)
    f.tex(520, 138, 'P', 'start', w=50)
    f.tex(299, 100, 'T_2', 'middle', color='#c92a2a', w=110)
    f.tex(271, 258, 'T_1', 'middle', color='#1971c2', w=70)
    f.tex(301, 172, 'm/t', 'middle', w=110)
    f.tex(300, 315, 'P = c\\,\\dfrac{m}{t}\\,\\Delta T', 'middle', w=300)
    return f.svg()


FIGURES = {"hero": hero, "cool-bag": cool_bag, "cooling-circuit": cooling_circuit}
