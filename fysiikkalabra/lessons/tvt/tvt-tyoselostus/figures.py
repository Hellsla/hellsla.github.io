"""Figures of the guide Kuvaajat ja tulokset työselostukseen (scripts/figlib.py); `python scripts/guides.py figures
tvt-tyoselostus` writes them into guide.md. A schematic report page without numbers: grey bars stand for the
student's own text and values; the section numbers and names are those of FY10's report template."""
from figlib import Fig, Axes, INK, MUTED, RULE, RULE_LIGHT, WHITE

PAGE = "#fdfcf8"


def bar(f, x1, x2, y, h=8):
    """A grey placeholder for text or a value the student writes."""
    return f.rect(x1, y - h / 2, x2 - x1, h, RULE_LIGHT, rx=h / 2)


def page():
    f = Fig("tvty-page", 730, "Kaaviokuva työselostuksen sivusta ilman lukuarvoja; harmaat palkit ovat oppilaan omaa tekstiä "
            "ja lukuja. Osassa 4, Mittaustulokset, on taulukko 1, jonka sarakkeiden otsikoissa on suure ja yksikkö: l "
            "metreinä, T sekunteina ja T toiseen sekunnin neliöinä. Osassa 5, Tulosten käsittely ja graafinen analyysi, on "
            "kuvaaja, jonka akseleilla on suureet ja yksiköt, mittauspisteet ja sovitettu suora, jonka yhtälö T toiseen on "
            "k kertaa l on kirjoitettu kuvaajan viereen. Kuvaajan alla on kuvateksti Kuva 1 ja sen alla tekstissä viittaus: "
            "Kuvasta 1 nähdään, että. Osassa 6, Tulos, on tulos muodossa g on sulkeissa lukuarvo plus miinus epävarmuus, "
            "molemmat harmaina palkkeina, ja yksikkö metriä per sekunti toiseen.")
    f.rect(36, 18, 528, 694, PAGE, RULE, 2, rx=6)
    # 4 Mittaustulokset
    f.tex(66, 56, r"4", "start"); f.tex(96, 56, r"\text{Mittaustulokset}", "start")
    f.tex(66, 96, r"\text{Taulukko 1.}", "start", MUTED); bar(f, 210, 440, 96)
    cols, top, row = [66, 216, 366, 516], 116, 36
    f.rect(cols[0], top, cols[-1] - cols[0], row, RULE_LIGHT)
    for k in range(4): f.line(cols[0], top + row * k, cols[-1], top + row * k, RULE, 1.5)
    for x in cols: f.line(x, top, x, top + row * 3, RULE, 1.5)
    for i, h in enumerate([r"l\ (\text{m})", r"T\ (\text{s})", r"T^2\ (\text{s}^2)"]):
        f.tex((cols[i] + cols[i + 1]) / 2, top + row / 2, h, "middle")
    for r in (1, 2):
        for i in range(3): bar(f, cols[i + 1] - 80, cols[i + 1] - 14, top + row * (r + 0.5))
    # 5 Tulosten käsittely ja graafinen analyysi
    f.tex(66, 264, r"5", "start"); f.tex(96, 264, r"\text{Tulosten käsittely ja}", "start")
    f.tex(96, 298, r"\text{graafinen analyysi}", "start")
    ax = Axes(f, (110, 506), (330, 380), x=(0, 8), y=(0, 6), xticks=[], yticks=[], xlabel=r"l\ (\text{m})",
              ylabel=r"T^2\ (\text{s}^2)", grid=False, origin_label=False)
    ax.line([(0, 0), (7.6, 5.7)], INK)
    for x, y in [(1.2, 1.05), (2.4, 1.7), (3.6, 2.85), (4.8, 3.5), (6.0, 4.6), (7.2, 5.3)]: ax.point(x, y, r=5.5)
    f.tex(372, 418, r"T^2 = k \cdot l", "start")
    f.tex(66, 546, r"\text{Kuva 1.}", "start", MUTED); bar(f, 166, 440, 546)
    f.tex(66, 582, r"\text{Kuvasta 1 nähdään, että}", "start", MUTED); bar(f, 380, 500, 582)
    # 6 Tulos
    f.tex(66, 630, r"6", "start"); f.tex(96, 630, r"\text{Tulos}", "start")
    f.tex(96, 674, r"g = (", "start"); bar(f, 150, 226, 674)
    f.tex(234, 674, r"\pm", "start"); bar(f, 262, 318, 674)
    f.tex(326, 674, r")\,\text{m/s}^2", "start")
    return f.svg()


FIGURES = {"page": page}
