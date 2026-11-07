"""Every answer in exercises.json for fy7-13, computed from the task data (python -I answers.py).
Grating d sin θ = k λ (light perpendicular to the grating, θ from the central maximum), d = 1 mm : N, and on a screen
at distance L the maximum's distance from the central maximum x gives tan θ = x : L.
Prints {exercise id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json
from math import asin, atan, sin, tan, degrees, radians, floor

mm = 1e-3
a = {}
# Level 1: one formula, values given
a["fy7-13-L1-01"] = mm / 300 * 1e6                           # d = 1 mm : 300 = 3,333 µm
a["fy7-13-L1-02"] = degrees(asin(650e-9 / 2.00e-6))          # sin θ = λ / d = 0,325 -> 18,97°
a["fy7-13-L1-03"] = 2.50e-6 * sin(radians(30.0)) / 2 * 1e9    # λ = d sin θ / k = 625 nm
a["fy7-13-L1-04"] = degrees(atan(0.300 / 1.20))              # tan θ = x / L = 0,25 -> 14,04°
a["fy7-13-L1-05"] = 633e-9 / sin(radians(22.0)) * 1e6        # d = λ / sin θ = 1,690 µm
# Level 2: a rearrangement, a conversion or two steps
d600 = mm / 600
kmax = floor(d600 / 450e-9)                                  # k ≤ d / λ = 3,70 -> 3
a["fy7-13-L2-01"] = 2 * kmax + 1                             # k = 0, ±1, ±2, ±3: 7 spots
th = asin(650e-9 / (mm / 100))                               # 100 lines/mm: sin θ = 0,065
a["fy7-13-L2-02"] = 2.50 * tan(th) * 100                     # x = L tan θ = 16,29 cm
th = atan(0.334 / 1.00)                                      # spots ±1 are 66,8 cm apart: x = 0,334 m
a["fy7-13-L2-03"] = mm / (532e-9 / sin(th))                  # d = λ / sin θ = 1,679 µm, N = 1 mm : d = 595,5
d300 = mm / 300
x700 = 1.00 * tan(asin(700e-9 / d300))                       # 0,2147 m
x400 = 1.00 * tan(asin(400e-9 / d300))                       # 0,1209 m
a["fy7-13-L2-04"] = (x700 - x400) * 100                      # width of the first-order spectrum 9,385 cm
# Level 3: reasoning, two ideas or an unfamiliar context
a["fy7-13-L3-01"] = 2 * 700 / 3                              # 3 λ3 = 2 · 700 nm -> λ3 = 466,7 nm (any grating)
th = atan(0.089 / 2 / 0.100)                                 # CD: spots ±1 89 mm apart on a screen 10,0 cm away
a["fy7-13-L3-02"] = 650e-9 / sin(th) * 1e6                   # track pitch d = λ / sin θ = 1,599 µm
d = 650e-9 / sin(atan(0.199 / 1.00))                         # calibration with the red laser: d = 3,330 µm
a["fy7-13-L3-03"] = d * sin(atan(0.162 / 1.00)) * 1e9        # green: λ = d sin θ = 532,6 nm
# Added exercises (exercise bank P1): level 1
d500 = mm / 500
a["fy7-13-L1-07"] = degrees(asin(2 * 532e-9 / d500))         # k = 2: sin θ = 2 λ / d = 0,532 -> 32,14°
a["fy7-13-L1-08"] = floor((mm / 400) / 589e-9)               # d / λ = 4,24 -> k_max = 4
# Level 2 (example data): least-squares line through the origin for sin θ_k against k
L_ = 1.00
xk = [0.063, 0.126, 0.195, 0.260, 0.335, 0.411, 0.494, 0.590]  # x_k in m, k = 1..8, 100 lines/mm
sk = [sin(atan(x / L_)) for x in xk]
slope = sum((i + 1) * s_ for i, s_ in enumerate(sk)) / sum((i + 1) ** 2 for i in range(8))   # = λ / d
a["fy7-13-L2-05"] = slope * (mm / 100) * 1e9                 # λ = slope · d = 633,7 nm
d6 = mm / 600
lam_ok = d6 * sin(atan(0.337 / 1.00))                        # correct λ with tan θ = x / L: 532,3 nm
lam_bad = d6 * (0.337 / 1.00)                                # student: sin θ ≈ x / L: 561,7 nm
a["fy7-13-L2-06"] = (lam_bad / lam_ok - 1) * 100             # error 5,53 %
# YO-skill form (teacher 2026-11-05): L2-08 is a change prediction (no number); 100 -> 300 lines/mm, L 2,00 -> 1,00 m: x = L tan(asin(λ/d)) = 13,03 -> 19,88 cm, factor 1,53
# Level 3 (example data)
x1 = 5.0e-3                                                  # peak of the table: x_1 = 5,0 mm
a["fy7-13-L3-04"] = 0.250e-3 * sin(atan(x1 / 2.00)) * 1e9    # λ = d sin θ = 625,0 nm
dd = [532e-9 / sin(atan(x2 / 100 / 2 / (Lc / 100))) for Lc, x2 in
      [(4.0, 8.3), (6.0, 12.5), (8.0, 16.7), (10.0, 20.9)]]   # DVD: tan θ = x : L, d = λ / sin θ per row
a["fy7-13-L3-05"] = sum(dd) / len(dd) * 1e6                  # mean d = 0,7374 µm
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
