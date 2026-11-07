"""Computed ripple-tank pictures for fy5-11 (single slit) and fy5-12 (two sources), replacing two blurred photographs
(teacher 2026-11-07, FY5 correction brief C5). Water surface seen from above at one instant: crests light, troughs dark,
as in a ripple tank's shadow image. Run: python lessons/FY5/fy5-11/ripple_model.py  (writes assets/pics/fy5/*.webp).
Physics: small-amplitude linear waves of one wavelength; each source and each point of the slit is a circular
(Huygens) source whose amplitude falls as 1/sqrt(r) in two dimensions; damping and the barrier's reflection are left out."""
import pathlib
import numpy as np
from PIL import Image

OUT = pathlib.Path(__file__).resolve().parents[3] / "assets/pics/fy5"
W, H, LAM = 960, 640, 48.0                     # pixels; wavelength in pixels
K = 2 * np.pi / LAM
DARK, LIGHT = np.array([12, 38, 64]), np.array([214, 236, 248])


def shade(u):
    v = np.clip(0.5 + 0.5 * u, 0, 1)[..., None]
    return (DARK + (LIGHT - DARK) * v).astype(np.uint8)


def circ(x, y, x0, y0, phase=0.0):
    r = np.hypot(x - x0, y - y0)
    return np.exp(1j * (K * r - phase)) * np.sqrt(3 * LAM / (r + 3 * LAM))


def two_sources(d=3 * LAM):
    y, x = np.mgrid[0:H, 0:W].astype(float)
    x0, y0 = W / 2, 70.0
    f = circ(x, y, x0 - d / 2, y0) + circ(x, y, x0 + d / 2, y0)
    img = shade(0.75 * f.real)
    for sx in (x0 - d / 2, x0 + d / 2):                          # the two dippers
        m = np.hypot(x - sx, y - y0) < 7
        img[m] = (245, 245, 245)
    Image.fromarray(img).save(OUT / "ripple-model-two-sources.webp", quality=88)


def single_slit(b=1.0 * LAM, wall=380.0, thick=12.0, n=48):
    y, x = np.mgrid[0:H, 0:W].astype(float)
    yc = H / 2
    inc = np.exp(1j * K * (x - wall))                            # plane wave from the left, phase 0 at the wall
    pts = yc + (np.arange(n) + 0.5) / n * b - b / 2
    f = sum(circ(x, y, wall, p) for p in pts) / n
    f /= np.abs(f[int(yc), int(wall + LAM)])                    # display gain: the spread wave is shown with full contrast
    u = np.where(x < wall, 0.9 * inc.real, 1.1 * f.real)        # (in a real tank the wave behind the slit is weaker)
    img = shade(u)
    barrier = (np.abs(x - wall) < thick / 2) & (np.abs(y - yc) > b / 2)
    img[barrier] = (120, 112, 98)
    Image.fromarray(img).save(OUT / "ripple-model-single-slit.webp", quality=88)


if __name__ == "__main__":
    two_sources()
    single_slit()
