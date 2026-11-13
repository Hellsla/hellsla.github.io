"""Every answer in exercises.json for fy1-6, computed from the task data (python -I answers.py).
Free fall from rest without air: v = g t with g = 9,81 m/s²; the (t,v) graph is a straight line through the origin
with slope g. Downward is the positive direction. Prints {id: number} as JSON on the last line; the lint and the gate
compare it with exercises.json."""
import json

g = 9.81                                             # m/s², putoamiskiihtyvyys Maassa
a = {}
# Level 1: one formula, values given
a["fy1-6-L1-01"] = g * 3.0                           # ball after 3,0 s: v = g t = 9,81 m/s² · 3,0 s = 29,43 m/s -> 29 m/s
a["fy1-6-L1-02"] = g * 0.80                          # apple after 0,80 s: v = 9,81 · 0,80 = 7,848 m/s -> 7,8 m/s
a["fy1-6-L1-03"] = 1.62 * 4.0                        # Moon g = 1,62 m/s²: v = 1,62 · 4,0 = 6,48 m/s -> 6,5 m/s
a["fy1-6-L1-04"] = (49 - 0) / (5.0 - 0)              # slope of the (t,v) line through (0 s; 0) and (5,0 s; 49 m/s): 9,8 m/s²
a["fy1-6-L1-05"] = 3.71 * 6.0                        # Mars g = 3,71 m/s²: v = 3,71 · 6,0 = 22,26 m/s -> 22 m/s
# Level 2: one conversion, one rearrangement or two steps
a["fy1-6-L2-01"] = 12.0 / g                          # v = g t -> t = v / g = 12,0 m/s / 9,81 m/s² = 1,223 s -> 1,22 s
a["fy1-6-L2-02"] = (20 / 5.0) * 5.0 / (40 / 5.0)       # figure fy1-6/two-planets: g_A = 20/5,0 = 4,0 and g_B = 40/5,0 = 8,0 m/s²; v_A(5,0 s) = 20 m/s; t_B = 20 / 8,0 = 2,5 s
a["fy1-6-L2-03"] = 12.0 + g * 1.50                   # speed gain in 1,50 s is g Δt = 14,715 m/s: v₂ = 12,0 + 14,715 = 26,715 m/s -> 26,7 m/s
a["fy1-6-L2-04"] = (29.3 - 9.7) / (3.0 - 1.0)        # g = Δv / Δt = (29,3 − 9,7) m/s / (3,0 − 1,0) s = 9,8 m/s²
# Level 3: reasoning or an unfamiliar context
a["fy1-6-L3-01"] = (g * 1.5) / (g * 1.5)             # vacuum: both bodies have v = g t, so the ratio is 1,0 whatever the masses 0,50 kg and 4,0 kg
g_planet = 14.8 / 4.0                                # planet: g = v / t = 14,8 m/s / 4,0 s = 3,70 m/s²
a["fy1-6-L3-02"] = 30.0 / g_planet                   # t = v / g = 30,0 m/s / 3,70 m/s² = 8,108 s -> 8,1 s
a["fy1-6-L3-03"] = g * 3.00 - 25.0                   # in vacuum v = 29,43 m/s; measured 25,0 m/s; shortfall 4,43 m/s -> 4,4 m/s
# Exercise bank additions (teacher 2026-11-04): L1-06, L1-07 are multiple choice (no number)
a["fy1-6-L1-08"] = g * 3.6                           # g = 9,81 m/s per second = 9,81 · 3,6 km/h = 35,316 km/h per second
def fit(pts):
    """Least-squares line y = k x + b through the points (a student's by-eye line lands within the tolerance)."""
    n = len(pts)
    xm, ym = sum(x for x, _ in pts) / n, sum(y for _, y in pts) / n
    k = sum((x - xm) * (y - ym) for x, y in pts) / sum((x - xm) ** 2 for x, _ in pts)
    return k, ym - k * xm
a["fy1-6-L2-05"] = fit([(0.10, 0.95), (0.20, 2.03), (0.30, 2.91), (0.40, 3.88), (0.50, 4.94), (0.60, 5.83)])[0]   # data of L2-05: slope 9,74 m/s² (0,7 % below 9,81)
k6, b6 = fit([(0.0, 1.97), (0.1, 2.93), (0.2, 3.95), (0.3, 4.89), (0.4, 5.90), (0.5, 6.86)])   # data of L2-06: k = 9,80 m/s², b = 1,97 m/s
a["fy1-6-L2-06"] = b6 / k6                           # t0 = b / k = 1,97 / 9,80 = 0,20 s before the measurement started
v1, v2 = 0.050 / 0.0250, 0.050 / 0.0111              # light gates, L = 5,0 cm: v1 = 2,00 m/s, v2 = 4,505 m/s
a["fy1-6-L2-07"] = (v2 - v1) / (0.575 - 0.320)       # g = Δv / Δt = 2,505 / 0,255 = 9,82 m/s²
a["fy1-6-L3-04"] = (g * 0.40 - 1.49) / (g * 0.40) * 100   # filter paper at 0,40 s: model 3,924 m/s vs 1,49 m/s -> 62,0 %
g5 = (24.5 - 4.9) / (2.65 - 0.65)                    # slope of the readings: 9,8 m/s² (the ratios v/t = 7,5; 8,9; 9,2 are too small because the clock started early)
a["fy1-6-L3-05"] = 0.65 - 4.9 / g5                   # clock offset t0 = t − v/g = 0,65 s − 0,50 s = 0,15 s
a["fy1-6-L1-09"] = 1.622 * 3.0                  # MAFY: Moon surface g = 1,622 m/s²; v = g t = 1,622 m/s² · 3,0 s = 4,866 m/s
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
