"""Figures of fy2-2 (scripts/figlib.py); `python scripts/figures.py fy2-2` writes them into lesson.md."""
import math
from figlib import Fig, INK, MUTED, WHITE, RULE, RULE_LIGHT, HEAT_LIGHT, HEAT, HOT, HOT_LIGHT, GOOD, GOOD_LIGHT, COLD, COLD_LIGHT, SAND_LIGHT, SAND, GRAIN, ALUMINIUM, PAPER, n


def sun(f, cx, cy):
    for i in range(8):
        a = i * math.pi / 4
        f.line(cx + 31 * math.cos(a), cy + 31 * math.sin(a), cx + 45 * math.cos(a), cy + 45 * math.sin(a), HEAT, 3, cap="round")
    f.circle(cx, cy, 23, HEAT_LIGHT, HEAT, 3)


def porridge(f, cx, cy):
    # a wheat stalk beside a bowl of porridge with steam
    f.line(cx - 48, cy + 38, cx - 48, cy - 22, GRAIN, 3, cap="round")
    for dy, dx in ((-20, -9), (-8, 9), (4, -9), (16, 9)):
        f.path(f"M{n(cx - 48)},{n(cy + dy)} q{dx},-10 {dx * 0.8:.1f},-22 q{-dx * 0.8:.1f},12 {-dx * 0.8 + dx * 0.8:.1f},22 z", fill=SAND_LIGHT, stroke=GRAIN, w=2)
    f.path(f"M{n(cx - 26)},{n(cy + 6)} L{n(cx + 44)},{n(cy + 6)} A35,30 0 0 1 {n(cx - 26)},{n(cy + 6)} Z", fill=COLD_LIGHT, stroke=INK, w=2.5)
    f.path(f"M{n(cx - 20)},{n(cy + 6)} Q{n(cx + 9)},{n(cy - 8)} {n(cx + 38)},{n(cy + 6)} Z", fill=SAND_LIGHT, stroke=GRAIN, w=2)
    for dx in (-8, 9, 26):
        f.path(f"M{n(cx + dx)},{n(cy - 6)} q-7,-9 0,-17 q7,-8 0,-16", stroke=MUTED, w=2)


def bike(f, cx, cy):
    r = 24
    for x in (cx - 30, cx + 30):
        f.circle(x, cy + 14, r, "none", INK, 3)
        f.circle(x, cy + 14, 3, INK)
    f.line(cx - 30, cy + 14, cx - 6, cy - 12, INK, 3, cap="round")
    f.line(cx - 6, cy - 12, cx + 30, cy + 14, INK, 3, cap="round")
    f.line(cx - 30, cy + 14, cx, cy + 14, INK, 3, cap="round")
    f.line(cx, cy + 14, cx - 6, cy - 12, INK, 3, cap="round")
    f.line(cx + 22, cy - 18, cx + 30, cy + 14, INK, 3, cap="round")
    f.line(cx + 16, cy - 20, cx + 28, cy - 20, INK, 3, cap="round")
    f.line(cx - 12, cy - 14, cx - 2, cy - 14, INK, 3, cap="round")


def thermo(f, cx, cy):
    f.rect(cx - 8, cy - 46, 16, 72, WHITE, INK, 2.5, rx=8)
    f.circle(cx, cy + 34, 16, HOT, INK, 2.5)
    f.rect(cx - 4, cy - 12, 8, 46, HOT)
    for dy in (-34, -22, -10):
        f.line(cx + 12, cy + dy, cx + 22, cy + dy, MUTED, 2)


def ketju():
    f = Fig("fy22-ketju", 370, "Kaavakuva: energiaketju Auringosta pyöräilyyn. Aurinko lähettää säteilyenergiaa, kasvi (kaura) sitoo sen kemialliseksi "
            "energiaksi ruokaan, lihakset muuttavat osan siitä pyörän liikkeeksi ja loppu on lämpöä. Joka vaiheessa osa energiasta "
            "muuttuu lämmöksi ympäristöön (oranssit nuolet alas), ja lopuksi myös liike muuttuu lämmöksi. Nuolten pituus ei ole mittakaavassa.")
    xs = [75, 225, 375, 525]
    sun(f, xs[0], 100); porridge(f, xs[1] + 4, 108); bike(f, xs[2], 98); thermo(f, xs[3], 96)
    for x in (130, 280, 430):
        f.block_arrow(x, 100, x + 50, 100, HEAT_LIGHT, shaft=14, head=30, headlen=22)
    names = [r"\text{Aurinko}", r"\text{Puuro}", r"\text{Pyöräily}", r"\text{Ympäristö}"]
    forms = [r"\text{säteily}", r"\text{kemiallinen}", r"\text{liike}", r"\text{lämpö}"]
    f.tex(xs[1] - 44, 44, r"\text{kasvi}", "middle", w=90)
    for x, a, b in zip(xs, names, forms):
        f.tex(x, 172, a, "middle", w=140)
        f.tex(x, 206, b, "middle", MUTED, w=140)
    f.rect(30, 300, 540, 44, HOT_LIGHT, None, 0, rx=8)
    f.tex(300, 322, r"\text{lämpöä ympäristöön}", "middle", w=300)
    for x in xs[1:3]:
        f.block_arrow(x, 232, x, 296, HEAT, shaft=14, head=30, headlen=22)
    f.block_arrow(xs[3], 232, xs[3], 296, HEAT, shaft=14, head=30, headlen=22)
    return f.svg()


def tikapuut():
    f = Fig("fy22-tikapuut", 372, "Kuvaaja mittakaavassa: energia jouleina kymmenpotenssiasteikolla 1 J:sta 10 TJ:iin ja yli. Jokainen väli on "
            "kymmenkertainen. Omena metrin ylös on noin 1 J, palava tulitikku noin 1 kJ, päivän ruoka noin 10 MJ, 50 litran bensiinitankki "
            "noin 1,6 GJ ja ydinvoimala Olkiluoto 3 tuottaa vuorokaudessa noin 140 TJ sähköä.")
    x0, dx, y0 = 96, 33.2, 292
    X = lambda k: x0 + k * dx
    f.arrow(x0 - 30, y0, 586, y0, INK, 2.5, 13)
    for k in range(0, 15):
        major = k % 3 == 0
        f.line(X(k), y0, X(k), y0 + (11 if major else 6), INK, 2 if major else 1.5)
    for k, lab in ((0, r"1\,\text{J}"), (3, r"1\,\text{kJ}"), (6, r"1\,\text{MJ}"), (9, r"1\,\text{GJ}"), (12, r"1\,\text{TJ}")):
        f.tex(X(k), y0 + 30, lab, "middle", w=90)
    f.tex(300, 350, r"\text{jokainen väli on 10-kertainen}", "middle", MUTED, w=340)
    items = [(0, 252, r"\text{omena}\ 1\,\text{J}", "start", 150), (3, 214, r"\text{tulitikku}\ 1\,\text{kJ}", "end", 190),
             (7, 176, r"\text{päivän ruoka}\ 10\,\text{MJ}", "end", 260), (9.2, 138, r"\text{bensiinitankki}\ 1{,}6\,\text{GJ}", "end", 300),
             (14.14, 100, r"\text{Olkiluoto 3, vrk}\ 140\,\text{TJ}", "end", 340)]
    for k, y, lab, anc, wd in items:
        f.line(X(k), y + 12, X(k), y0, MUTED, 1.5, "5 4")
        f.circle(X(k), y0, 7, HEAT, WHITE, 2)
        f.tex(X(k) + (10 if anc == "start" else -10), y, lab, anc, w=wd)
    return f.svg()


def sailyminen():
    f = Fig("fy22-sailyminen", 350, "Kaavakuva mittakaavassa (esimerkki): pyöräilijän aamupuuron kemiallisesta energiasta 800 kJ lihakset muuttavat "
            "liikkeeksi 200 kJ ja lämmöksi 600 kJ. Nuolten leveys on verrannollinen energiaan, ja haarojen yhteinen leveys on yhtä suuri kuin alkuperäisen nuolen leveys.")
    k = 0.12   # px per kJ
    hin, hm, hl = 800 * k, 200 * k, 600 * k
    top = 112
    f.rect(40, top, 192, hin, HEAT_LIGHT, HEAT, 2)
    f.path(f"M232,{n(top)} L400,{n(top)} L400,{n(top - 14)} L452,{n(top + hm / 2)} L400,{n(top + hm + 14)} L400,{n(top + hm)} L232,{n(top + hm)} Z", fill=HEAT_LIGHT, stroke=HEAT, w=2)
    xr = 232 + hl
    f.path(f"M232,{n(top + hm)} L{n(xr)},{n(top + hm)} L{n(xr)},262 L{n(xr + 22)},262 L{n((232 + xr) / 2)},302 L{n(232 - 22)},262 L232,262 Z", fill=HOT_LIGHT, stroke=HOT, w=2)
    f.tex(300, 38, r"800\,\text{kJ} = 200\,\text{kJ} + 600\,\text{kJ}", "middle", w=400)
    f.tex(52, 144, r"\text{kemiallinen}", "start", w=170)
    f.tex(52, 182, r"800\,\text{kJ}", "start", w=140)
    f.tex(244, 78, r"\text{liike: }200\,\text{kJ}", "start", w=220)
    f.tex(xr + 36, 232, r"\text{lämpö: }600\,\text{kJ}", "start", w=220)
    f.tex(300, 332, r"\text{nuolen leveys kuvaa energian määrää}", "middle", MUTED, w=460)
    return f.svg()


FIGURES = {"ketju": ketju, "tikapuut": tikapuut, "sailyminen": sailyminen}
