"""Figures of the guide Videoanalyysi (scripts/figlib.py); `python scripts/guides.py figures tvt-videoanalyysi` writes
them into guide.md. A schematic top view of the filming set-up, not to scale."""
from figlib import Fig, INK, MUTED, IRON, HEAT_LIGHT, GLASS, WHITE

TAPE = "#ffe8a3"


def setup():
    """Seen from above: the plane of motion as a line with the body's positions on it, the scale ruler lying in the same
    plane, the camera on its tripod facing the plane at right angles, and a ruler in the wrong place nearer the camera."""
    f = Fig("tvtv-setup", 360, "Kaaviokuva ylhäältä katsottuna, ei mittakaavassa. Ylhäällä on liiketaso, jossa kappale "
            "liikkuu; kappaleen peräkkäiset paikat on piirretty tason viivalle. Samassa tasossa kappaleen radan vieressä on "
            "mitta-asteikko. Alhaalla keskellä on kamera jalustalla, ja siitä kulkee katkoviiva kohtisuoraan liiketasoa "
            "kohti; viivan ja tason välissä on suoran kulman merkki. Tason ja kameran välissä on katkoviivalla piirretty "
            "toinen mitta, joka on väärässä paikassa, koska se on lähempänä kameraa kuin kappale.")
    f.line(50, 80, 550, 80, INK, 3)
    f.tex(50, 48, r"\text{liiketaso}", "start")
    for x in (130, 200, 270, 340): f.circle(x, 80, 13, HEAT_LIGHT, INK, 2.5)
    f.rect(400, 72, 130, 16, TAPE, INK, 2.5, rx=2)
    for k in range(14): f.line(404 + 9 * k, 72, 404 + 9 * k, 72 + (10 if k % 5 == 0 else 6), INK, 1.5)
    f.tex(465, 114, r"\text{mitta-asteikko}", "middle")
    # a ruler in the wrong place, nearer the camera
    f.rect(400, 196, 130, 16, "none", MUTED, 2, rx=2, extra='stroke-dasharray="7 5"')
    f.tex(465, 236, r"\text{väärä paikka}", "middle", MUTED)
    # the camera on its tripod, looking at right angles to the plane
    f.line(300, 284, 300, 82, MUTED, 2, "7 5")
    f.path("M300,94 L314,94 L314,80", stroke=INK, w=2)
    f.tex(288, 180, r"\text{kohtisuoraan}", "end", MUTED)
    for dx, dy in ((-34, 34), (34, 34), (0, -30)): f.line(300, 302, 300 + dx, 302 + dy, IRON, 3, cap="round")
    f.rect(262, 290, 76, 24, GLASS, INK, 2.5, rx=5)
    f.circle(300, 290, 8, IRON, INK, 2)
    f.tex(350, 302, r"\text{kamera jalustalla}", "start")
    f.tex(40, 330, r"\text{näkymä ylhäältä}", "start", MUTED)
    return f.svg()


FIGURES = {"setup": setup}
