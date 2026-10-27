"""Every answer in exercises.json and inquiry.json for fy1-6, computed from the task data (python -I answers.py).
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
a["fy1-6-L2-02"] = g * 0.450 * 3.6                   # 450 ms = 0,450 s: v = 4,4145 m/s = 4,4145 · 3,6 km/h = 15,89 km/h -> 15,9 km/h
a["fy1-6-L2-03"] = 12.0 + g * 1.50                   # speed gain in 1,50 s is g Δt = 14,715 m/s: v₂ = 12,0 + 14,715 = 26,715 m/s -> 26,7 m/s
a["fy1-6-L2-04"] = (29.3 - 9.7) / (3.0 - 1.0)        # g = Δv / Δt = (29,3 − 9,7) m/s / (3,0 − 1,0) s = 9,8 m/s²
# Level 3: reasoning or an unfamiliar context
a["fy1-6-L3-01"] = (g * 1.5) / (g * 1.5)             # vacuum: both bodies have v = g t, so the ratio is 1,0 whatever the masses 0,50 kg and 4,0 kg
g_planet = 14.8 / 4.0                                # planet: g = v / t = 14,8 m/s / 4,0 s = 3,70 m/s²
a["fy1-6-L3-02"] = 30.0 / g_planet                   # t = v / g = 30,0 m/s / 3,70 m/s² = 8,108 s -> 8,1 s
a["fy1-6-L3-03"] = g * 3.0 - 25.0                    # in vacuum v = 29,43 m/s; measured 25,0 m/s; shortfall 4,43 m/s -> 4,4 m/s

# Inquiry tasks (inquiry.json), not exercises
a["inq-exp1"] = (g * 3.0 - g * 1.0) / (3.0 - 1.0)    # experiment 1, rows t = 1,0 s and 3,0 s: Δv/Δt = (29,43 − 9,81) / 2,0 = 9,81 m/s²
t_d = [0.1, 0.2, 0.3, 0.4, 0.5]; v_d = [1.1, 1.9, 3.0, 3.9, 5.0]   # example data: speed (m/s) of a dropped ball at times (s)
slope_fit = (4.9 - 0) / (0.50 - 0)                   # fitted line through the origin and (0,50 s; 4,9 m/s): slope 9,8 m/s²
a["inq-data"] = slope_fit
a["inq-siirto"] = 7.4 / 2.0 * 3.0                    # unknown planet: g = 7,4 / 2,0 = 3,7 m/s²; v(3,0 s) = 3,7 · 3,0 = 11,1 m/s -> 11 m/s
a["inq-check2"] = (108 / 3.6) / g                    # 108 km/h = 30,0 m/s; t = v / g = 30,0 / 9,81 = 3,058 s -> 3,06 s
a["inq-example"] = g * 1.5                           # worked example: v = g t = 9,81 · 1,5 = 14,715 m/s -> 15 m/s
a["inq-example-kmh"] = g * 1.5 * 3.6                 # 14,715 m/s · 3,6 = 52,97 km/h -> 53 km/h
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
