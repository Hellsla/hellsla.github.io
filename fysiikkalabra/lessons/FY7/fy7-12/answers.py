"""Every answer in exercises.json for fy7-12, computed from the task data (python -I answers.py).
Critical angle sin α_r = n2 / n1 (only when n1 > n2); refraction n1 sin α1 = n2 sin α2; v = c / n; t = s / v.
Prints {exercise id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json
from math import asin, sin, tan, sqrt, degrees, radians

c = 3.00e8                                                   # speed of light in vacuum (m/s)
a = {}
# Level 1: one formula, values given
a["fy7-12-L1-01"] = degrees(asin(1.00 / 1.33))              # water -> air: α_r = 48,75° -> 48,8°
a["fy7-12-L1-02"] = degrees(asin(1.00 / 2.42))              # diamond -> air: α_r = 24,41° -> 24,4°
a["fy7-12-L1-03"] = degrees(asin(1.33 / 1.52))              # glass -> water: α_r = 61,04° -> 61,0°
a["fy7-12-L1-04"] = c / 1.47 / 1e3                          # v = c / n = 2,041 · 10^8 m/s = 2,04 · 10^5 km/s
a["fy7-12-L1-05"] = 100e3 / 2.0e8 * 1e3                     # t = s / v = 100 000 m / 2,0 · 10^8 m/s = 0,50 ms
# (fy7-12-L1-06 is multiple choice: no number)
a["fy7-12-L1-07"] = degrees(asin(1.33 / 1.49))              # acrylic -> water: α_r = 63,20° -> 63,2°
a["fy7-12-L1-08"] = c * 0.50e-3 / 1.45 / 1e3                # s = v t = c t / n = 1,034 · 10^5 m = 103 km
# Level 2: a rearrangement, a conversion or two steps
a["fy7-12-L2-01"] = 1.47 * sin(radians(82.0))               # n2 = n1 sin α_r = 1,4557 -> 1,46
a["fy7-12-L2-02"] = 1.00 / sin(radians(45.0))               # total reflection at 45° needs α_r ≤ 45°: n ≥ 1 / sin 45° = 1,414
n_plastic = 1.00 / sin(radians(42.0))                       # n = 1 / sin α_r = 1,4945
a["fy7-12-L2-03"] = c / n_plastic / 1e3                     # v = c / n = c sin α_r = 2,007 · 10^5 km/s
a["fy7-12-L2-04"] = 1.46 * 250e3 / c * 1e3                  # t = s / v = n s / c = 1,2167 ms -> 1,22 ms
alpha_r5 = [41.8, 42.6, 41.5, 42.3, 42.0]                   # data of L2-05 (critical angles of a plastic against air, degrees)
a["fy7-12-L2-05"] = 1.00 / sin(radians(sum(alpha_r5) / len(alpha_r5)))   # mean 42,04°, n = 1 / sin α_r = 1,493 -> 1,49
pulse = [(49.0, 0), (49.2, 0), (49.4, 52), (49.6, 91), (49.8, 96), (50.0, 88), (50.2, 63), (50.4, 21), (50.6, 5), (50.8, 2)]   # data of L2-06 (t in µs, I in %)
half = [t for t, i in pulse if i >= 50]                     # rows with I >= 50 %: 49,4 ... 50,2 µs
a["fy7-12-L2-06"] = (max(half) - min(half)) * 1e3           # pulse width 0,8 µs = 800 ns
a["fy7-12-L2-07"] = degrees(asin(1.00 * sin(radians(70.0)) / 1.50))   # air -> glass has no critical angle: β = 38,79° -> 38,8°
# Level 3: reasoning, two ideas or an unfamiliar context
ar = asin(1.00 / 1.33)                                      # pool lamp: light leaves the surface only where α < α_r
a["fy7-12-L3-01"] = 1.80 * tan(ar)                          # radius r = h tan α_r = 1,80 m · tan 48,75° = 2,053 m
# step-index fibre, n1 = 1,480, n2 = 1,460, 1,00 km: the ray at the critical angle travels the path L / sin α_r
t_axis = 1.480 * 1.00e3 / c                                 # axial ray: t = n1 L / c = 4,933 µs
t_zig = t_axis / (1.460 / 1.480)                            # zigzag ray: t = n1 L / (c sin α_r) = n1² L / (c n2)
a["fy7-12-L3-02"] = (t_zig - t_axis) * 1e9                  # difference 67,58 ns -> 68 ns
# glass rod (n = 1,50), ray meets the side at 60°: air (α_r = 41,8°) reflects it totally; under a water drop
# (n = 1,33) α_r = 62,46° > 60°, so it refracts out: 1,50 sin 60° = 1,33 sin β
a["fy7-12-L3-03"] = degrees(asin(1.50 * sin(radians(60.0)) / 1.33))   # β = 77,61° -> 77,6°
# fibre acceptance angle (data of L3-04, fibres A, B, C): sin θ_max = n_ydin cos α_r = sqrt(n1² - n2²); the answer is fibre B
accept = lambda n1, n2: degrees(asin(sqrt(n1 ** 2 - n2 ** 2)))
a["fy7-12-L3-04"] = accept(1.50, 1.47)                      # B: sqrt(2,25 - 2,1609) = 0,2985 -> θ_max = 17,37° -> 17,4° (A 14,0°, C 9,8°)
# bent plastic fibre (core radius a = 0,50 mm, n1 = 1,49, n2 = 1,40): the ray at the inner edge hits the outer wall at sin α = (R - a) / (R + a)
a["fy7-12-L3-05"] = 0.50 * (1.49 + 1.40) / (1.49 - 1.40)    # total reflection needs sin α >= n2 / n1: R_min = a (n1 + n2) / (n1 - n2) = 16,06 mm
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
