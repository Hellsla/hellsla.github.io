"""Figures of this lesson (scripts/figlib.py); `python scripts/figures.py fy3-16` writes them into lesson.md."""
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


FIGURES = {"hero": hero}
