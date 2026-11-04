"""Every answer in exercises.json for fy7-12, computed from the task data (python -I answers.py).
Critical angle sin α_r = n2 / n1 (only when n1 > n2); refraction n1 sin α1 = n2 sin α2; v = c / n; t = s / v.
Prints {exercise id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json
from math import asin, sin, tan, degrees, radians

c = 3.00e8                                                   # speed of light in vacuum (m/s)
a = {}
# Level 1: one formula, values given
a["fy7-12-L1-01"] = degrees(asin(1.00 / 1.33))              # water -> air: α_r = 48,75° -> 48,8°
a["fy7-12-L1-02"] = degrees(asin(1.00 / 2.42))              # diamond -> air: α_r = 24,41° -> 24,4°
a["fy7-12-L1-03"] = degrees(asin(1.33 / 1.52))              # glass -> water: α_r = 61,04° -> 61,0°
a["fy7-12-L1-04"] = c / 1.47 / 1e3                          # v = c / n = 2,041 · 10^8 m/s = 2,04 · 10^5 km/s
a["fy7-12-L1-05"] = 100e3 / 2.0e8 * 1e3                     # t = s / v = 100 000 m / 2,0 · 10^8 m/s = 0,50 ms
# Level 2: a rearrangement, a conversion or two steps
a["fy7-12-L2-01"] = 1.47 * sin(radians(82.0))               # n2 = n1 sin α_r = 1,4557 -> 1,46
a["fy7-12-L2-02"] = 1.00 / sin(radians(45.0))               # total reflection at 45° needs α_r ≤ 45°: n ≥ 1 / sin 45° = 1,414
n_plastic = 1.00 / sin(radians(42.0))                       # n = 1 / sin α_r = 1,4945
a["fy7-12-L2-03"] = c / n_plastic / 1e3                     # v = c / n = c sin α_r = 2,007 · 10^5 km/s
a["fy7-12-L2-04"] = 1.46 * 250e3 / c * 1e3                  # t = s / v = n s / c = 1,2167 ms -> 1,22 ms
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
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
