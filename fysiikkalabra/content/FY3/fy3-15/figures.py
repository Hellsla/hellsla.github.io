"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy3-15` writes them into lesson.md."""
import herolib as H


def hero():
    """The chapter's opening illustration: a combined heat and power plant in winter with district heating pipes to the town."""
    f = H.hero("fy315-hero", "Kuvitus: talvinen yhteistuotantovoimalaitos. Piipusta ja voimalasta nousee höyryä, voimalinjat "
               "vievät sähköä pois, ja kaukolämpöputket kulkevat kaupunkiin: punainen meno kuumaa vettä, sininen paluu "
               "jäähtynyttä vettä. Kerrostalojen ikkunat loistavat lämpiminä.")
    H.sky(f, "fy315h", 600, H.COLD_LIGHT, H.WHITE)
    H.forest(f, 380, 50, 26, H.ALUMINIUM, seed=11, depth=60)
    f.path("M0,420 Q600,380 1200,420 V600 H0 Z", H.WHITE)
    # chimney, plant halls, plume
    f.rect(260, 70, 50, 330, H.grad(f, "fy315h-chimney", H.WHITE, H.ALUMINIUM, horizontal=True), H.INK, 3)
    for y in (100, 130): f.rect(260, y, 50, 14, H.HOT_LIGHT)
    H.cloud(f, 330, 50, 0.9, H.WHITE, extra=f'stroke="{H.RULE}" stroke-width="2.5"')
    H.cloud(f, 460, 30, 0.7, H.WHITE, extra=f'stroke="{H.RULE}" stroke-width="2.5"')
    f.rect(120, 260, 200, 160, H.RULE_LIGHT, H.INK, 3)
    f.rect(320, 300, 220, 120, H.ALUMINIUM, H.INK, 3)
    f.path("M120,260 L220,220 L320,260 Z", H.RULE, H.INK, 3)
    for x in range(140, 300, 40): f.rect(x, 290, 24, 50, H.HEAT_LIGHT, H.INK, 2)
    f.rect(470, 210, 40, 90, H.grad(f, "fy315h-stack", H.WHITE, H.ALUMINIUM, horizontal=True), H.INK, 3)
    # power lines to the left
    for x, h in ((60, 230),):
        f.path(f"M{x},{420} L{x + 20},{420 - h} L{x + 40},420 M{x - 10},{420 - h + 30} H{x + 50}", stroke=H.INK, w=4)
    f.path("M0,240 Q40,250 70,220 M110,220 Q130,250 150,262", stroke=H.INK, w=2)
    # district heating pipes to the town
    f.path("M540,390 C700,390 760,470 1200,470", stroke=H.HOT, w=16, extra='stroke-linecap="round"')
    f.path("M540,410 C700,410 760,500 1200,500", stroke=H.COLD, w=16, extra='stroke-linecap="round"')
    for x, w, h in ((860, 120, 200), (1000, 160, 260), (1120, 100, 180)):
        f.rect(x, 440 - h, w, h, H.RULE_LIGHT, H.INK, 3)
        for wx in range(x + 16, x + w - 24, 36):
            for wy in range(440 - h + 20, 420, 44):
                f.rect(wx, wy, 22, 26, H.HEAT_LIGHT if H.rnd(wx * 7 + wy, 3) > 0.3 else H.GLASS, H.INK, 1.5)
    return f.svg()


FIGURES = {"hero": hero}
