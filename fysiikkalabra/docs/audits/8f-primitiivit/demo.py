"""Demo of the 8f primitives on the pictures of fy5-10/birth (work queue 8f; no lesson file is changed).
Writes demo.html (the figure with site.css, playing) and demo-still.svg; `node frames.js` captures frames/*.png,
`demo.py --gif` joins them into demo.gif:

  python docs/audits/8f-primitiivit/demo.py && node docs/audits/8f-primitiivit/frames.js && python docs/audits/8f-primitiivit/demo.py --gif
"""
import math, pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "scripts")); sys.path.insert(0, str(ROOT / "lessons" / "FY5" / "fy5-10"))
from figlib import Fig, n, INK, MUTED, COLD, SAND_DARK
import figures as L

HERE = pathlib.Path(__file__).resolve().parent
ROPE = L.ROPE


def pulse_demo(anim=True):
    """A pulse runs along the rope; one marked particle only goes up and down as it passes (travel() + motion())."""
    f = Fig("demo-pulse", 190, "Köyden pää nykäistään ylös ja alas, ja pulssi etenee narua oikealle. Yksi narun kohta on merkitty "
            "pisteellä: se nousee ja laskee paikallaan pulssin kohdalla eikä kulje mukana.", anim=anim)
    xs, xe, y0, A, wid = 90, 560, 100, 44, 120
    xb0 = xs + 70                                                      # where the pulse is drawn: just born at the hand
    bump = lambda x, c: -A * math.sin(math.pi * (x - (c - wid / 2)) / wid) ** 2 if abs(x - c) <= wid / 2 else 0.0
    run = xe - xb0 + wid / 2                                           # until the pulse has left the window
    T = 5.0
    if anim:
        f.travel(run, T, clip=(xs - 20, 0, xe - xs + 40, 190))
    xl, xr = xs - 20 - 700, xe + 20
    pts = []; x = xs - 20
    while x <= xe + 20 + 1e-9:
        pts.append(f"{n(x)},{n(y0 + bump(x, xb0))}"); x += 3
    f.add(f'<path d="M{xs - 20 - run - 10},{y0} L{" L".join(pts)}" fill="none" stroke="{ROPE}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>')
    if anim: f.end()
    f.rect(xs - 16, y0 - 9, 16, 18, SAND_DARK, INK, 2, 3)              # the hand's handle
    xp = 330                                                           # the marked particle: up and down only
    frames = [(i / 40, 0, bump(xp, xb0 + run * i / 40) - bump(xp, xb0), 0, 1) for i in range(41)]
    if anim: f.motion(frames, T)
    f.circle(xp, y0, 9, COLD, INK, 2)
    if anim: f.end()
    f.arrow(400, 175, 490, 175, COLD, 3.5, 16)
    f.tex(392, 175, r"v", "end", COLD)
    f.tex(xp, 140, r"\text{merkitty kohta}", "middle", MUTED)
    return f.svg()


def page():
    css = (ROOT / "templates" / "site.css").read_text()
    return ("<!doctype html><meta charset=utf-8><title>8f demo</title><style>" + css + "</style>"
            "<body style='background:#fff;padding:20px'><div class=fig style='max-width:640px'>" + pulse_demo() + "</div>"
            "<script>document.querySelector('svg.fig-anim').classList.add('is-playing')</script>")


if __name__ == "__main__":
    (HERE / "demo.html").write_text(page())
    (HERE / "demo-still.svg").write_text(pulse_demo(False))
    if "--gif" in sys.argv:                                            # after `node frames.js` has written frames/*.png
        from PIL import Image
        ims = [Image.open(p).convert("P", palette=Image.ADAPTIVE) for p in sorted((HERE / "frames").glob("*.png"))]
        ims[0].save(HERE / "demo.gif", save_all=True, append_images=ims[1:], duration=250, loop=0)
