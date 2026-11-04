"""Numbers of the lesson text and inquiry.json for fy7-13, computed from their data (python -I lesson-answers.py); the
exercises' answers are in answers.py. Grating d sin θ = k λ (light perpendicular to the grating, θ from the central
maximum), grating constant d = 1 mm : N (N lines per millimetre), on a screen at distance L: tan θ = x : L.
Prints {id: number} as JSON."""
import json
from math import asin, atan, sin, tan, degrees, radians, floor

a = {}
mm = 1e-3


def theta(N, lam, k=1):
    """Angle of order k in degrees for N lines/mm and wavelength lam (m)."""
    return degrees(asin(k * lam / (mm / N)))


def x_cm(N, lam, L, k=1):
    """Distance of the order-k maximum from the central maximum on a screen at L metres, in cm."""
    return L * tan(radians(theta(N, lam, k))) * 100


# Kaava: grating constants of school gratings
a["d-100"] = mm / 100 * 1e6                         # 10,0 µm
a["d-300"] = mm / 300 * 1e6                         # 3,333 µm
a["d-600"] = mm / 600 * 1e6                         # 1,667 µm
# highest order for 600 lines/mm and 650 nm: d / λ = 2,56 -> k = 2, five maxima
a["kmax-ratio"] = (mm / 600) / 650e-9               # 2,564
# white light, 300 lines/mm, first order: violet 400 nm and red 700 nm (figure "white")
a["white-400"] = theta(300, 400e-9)                 # 6,89°
a["white-700"] = theta(300, 700e-9)                 # 12,12°
a["white-400-2"] = theta(300, 400e-9, 2)            # 13,89°
a["white-700-2"] = theta(300, 700e-9, 2)            # 24,83°
# figure "setup" and Kaava text: 600 lines/mm, 532 nm, L = 1,00 m: koe2-theta-532 and koe2-x-532 below
# CD and DVD track pitches (IEC 60908:1999 CD 1,6 µm; ECMA-267:2001 DVD 0,74 µm) as lines per mm
a["cd-N"] = mm / 1.6e-6                             # 625 per mm
a["dvd-N"] = mm / 0.74e-6                           # 1351 per mm
# worked example: N = 300, L = 2,00 m, x1 = 39,6 cm (spots ±1 are 79,2 cm apart)
a["ex-theta"] = degrees(atan(0.396 / 2.00))         # 11,20°
a["ex-lambda"] = (mm / 300) * sin(atan(0.396 / 2.00)) * 1e9   # 647,4 nm -> 647 nm
a["ex-sin-tan"] = 0.396 / 2.00                      # tan θ = 0,198; sin θ = 0,1942
a["ex-sin"] = sin(atan(0.396 / 2.00))
a["ex-tan-lambda"] = (mm / 300) * 0.396 / 2.00 * 1e9   # with tan instead of sin: 660 nm, a little too large
# hook / predictions / sim experiments (λ = 650 nm, L = 1,00 m)
for N in (300, 600, 1000):
    a[f"koe1-theta-{N}"] = theta(N, 650e-9)          # 11,245°, 22,95°, 40,54°
    a[f"koe1-x-{N}"] = x_cm(N, 650e-9, 1.00)         # 19,88, 42,34, 85,53 cm
    a[f"koe1-sin-{N}"] = sin(radians(theta(N, 650e-9)))   # 0,195, 0,390, 0,650
for lam in (450, 532, 650):
    a[f"koe2-theta-{lam}"] = theta(600, lam * 1e-9)  # 15,664°, 18,61°, 22,95°
    a[f"koe2-x-{lam}"] = x_cm(600, lam * 1e-9, 1.00)  # 28,05, 33,69, 42,34 cm
    a[f"koe2-sin-{lam}"] = lam * 1e-9 / (mm / 600)  # 0,270, 0,3192, 0,390
a["koe2-question"] = theta(600, 532e-9)             # 18,61°
a["koe2-mistake-tan"] = degrees(atan(532e-9 / (mm / 600)))   # mistake: tan instead of sin: 17,70°
for L in (0.50, 1.00, 2.00):
    a[f"koe3-x-{L:.2f}"] = x_cm(300, 650e-9, L)       # 9,94, 19,88, 39,76 cm
a["kmax-300-650"] = floor((mm / 300) / 650e-9)       # 5
# kertaus: path difference 1,5 λ -> destructive (no number)
# mittaus (example data): green laser, 300 lines/mm, L = 1,500 m (ΔL = 0,005 m), 2x1 = 48,4 cm, 2x2 = 101,2 cm,
# Δ(2x) = 0,3 cm, so Δx = 0,15 cm
d300 = mm / 300
lam = lambda x, L, k: d300 * sin(atan(x / L)) / k * 1e9
a["mittaus-x2"] = 1.012 / 2                         # 0,506 m
a["mittaus-theta2"] = degrees(atan(0.506 / 1.500))  # 18,64°
a["mittaus"] = lam(0.506, 1.500, 2)                 # 532,7 nm -> 533 nm
a["mittaus-max"] = lam(0.5075, 1.495, 2)            # 535,7 nm
a["mittaus-min"] = lam(0.5045, 1.505, 2)            # 529,7 nm  -> Δλ ≈ 3 nm
a["mittaus-k1"] = lam(0.242, 1.500, 1)              # 530,9 nm
a["mittaus-k1-max"] = lam(0.2435, 1.495, 1)         # 535,9 nm
a["mittaus-k1-min"] = lam(0.2405, 1.505, 1)         # 526,0 nm -> Δλ ≈ 5 nm
a["mittaus-mistake-k"] = lam(0.506, 1.500, 1)       # forgot k = 2: 1065 nm
a["mittaus-mistake-2x"] = lam(1.012, 1.500, 2)      # used the spot-to-spot distance as x: 932 nm
a["mittaus-mistake-sin"] = d300 * (0.506 / 1.500) / 2 * 1e9   # sin θ = x / L: 562 nm
# virhe: 600 lines/mm: d = 1 mm : 600 = 1,667 · 10^-6 m (the student wrote 1,67 · 10^-3 m)
a["virhe-d"] = mm / 600 * 1e6                       # 1,667 µm = 1,667 · 10^-6 m
# siirto: DVD as a reflection grating, track pitch 0,74 µm, red laser 650 nm, light perpendicular to the disc
a["siirto"] = degrees(asin(650e-9 / 0.74e-6))       # 61,45°
a["siirto-cd"] = degrees(asin(650e-9 / 1.6e-6))     # mistake: CD pitch 1,6 µm: 23,97°
a["siirto-k2"] = 2 * 650e-9 / 0.74e-6               # second order: sin θ = 1,76 > 1, no maximum
a["siirto-mistake-tan"] = degrees(atan(650e-9 / 0.74e-6))   # mistake: tan: 41,3°
# tarkistus-2: sodium light 589 nm, 500 lines/mm, second order
a["tarkistus2"] = theta(500, 589e-9, 2)             # 36,08°
a["tarkistus2-k1"] = theta(500, 589e-9, 1)          # mistake: first order 17,13°
a["tarkistus2-sin"] = 2 * 589e-9 / (mm / 500)       # mistake: the sine 0,589
# exit ticket: 250 lines/mm
a["exit-d"] = mm / 250 * 1e6                        # 4,0 µm
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
