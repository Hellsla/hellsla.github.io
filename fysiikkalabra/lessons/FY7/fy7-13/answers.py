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
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
