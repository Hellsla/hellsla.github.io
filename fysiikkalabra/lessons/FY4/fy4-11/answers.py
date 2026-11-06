"""Every answer in exercises.json for fy4-11, computed from the task data (python -I answers.py).
Stopping model: the car moves at constant speed during the reaction time t_r (s_r = v0 t_r), then slows down with a
constant deceleration a until it stops (s_j = v0²/(2a), the triangle under the (t, v) graph); level road, air
resistance neglected; braking with the full grip a = μg. Collision: impulse principle F_ka Δt = m Δv (mean force).
g = 9,81 m/s². Prints {id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json, math

g = 9.81
kmh = lambda v: v / 3.6
a = {}
# Level 1: one formula, values given
a["fy4-11-L1-01"] = kmh(72.0) * 1.20                     # reaction distance s_r = v0 t_r = 20,0 m/s · 1,20 s = 24,0 m
a["fy4-11-L1-02"] = 25.0 ** 2 / (2 * 8.00)               # braking distance s_j = v0²/(2a) = 625/16 = 39,06 m
a["fy4-11-L1-03"] = 20.0 / 5.00                          # braking time t_j = v0/a = 4,00 s
a["fy4-11-L1-04"] = 70.0 * 15.0 / 0.120                  # mean force F_ka = m Δv/Δt = 1050 kg·m/s : 0,120 s = 8750 N
a["fy4-11-L1-05"] = 18.0 / 15.0                           # reaction time t_r = s_r / v0 = 18,0 m : 15,0 m/s = 1,20 s
# Level 2: two steps, a conversion or a rearrangement
v = kmh(90)                                              # 25 m/s
a["fy4-11-L2-01"] = v * 1.5 + v * v / (2 * 7.5)          # s_p = 37,5 m + 41,67 m = 79,17 m
v = kmh(100)                                             # 27,78 m/s
a["fy4-11-L2-02"] = v * v / (2 * 0.30 * g)               # snow: a = μg = 2,943 m/s², s_j = 131,1 m
a["fy4-11-L2-03"] = 75.0 * kmh(50.0) / 0.100             # 50,0 km/h = 13,89 m/s; F_ka = 10 417 N
a["fy4-11-L2-04"] = math.sqrt(2 * 8.0 * 32.0) * 3.6      # skid marks: v0 = √(2 a s_j) = 22,63 m/s = 81,46 km/h
# Level 3: reasoning, two ideas, an unfamiliar context
d = kmh(30) * 1.0 + kmh(30) ** 2 / (2 * 9.0)             # the obstacle where a car at 30 km/h just stops: 12,19 m
v = kmh(40); sr = v * 1.0                                # at 40 km/h the reaction distance is 11,11 m < d
a["fy4-11-L3-01"] = math.sqrt(v * v - 2 * 9.0 * (d - sr)) * 3.6   # impact speed √(v0² − 2a(d − s_r)) = 36,7 km/h
v = kmh(50.0)
dt = 2 * 0.600 / v                                       # constant deceleration over 0,600 m: Δt = 2s/v0 = 0,0864 s
a["fy4-11-L3-02"] = 70.0 * v / dt                        # F_ka = m v0 / Δt = 11 253 N
v = kmh(80)
a["fy4-11-L3-03"] = v * 1.0 + v * v / (2 * 6.0) - v * v / (2 * 9.0)   # gap = s_r + s_j(own) − s_j(ahead) = 22,2 + 41,2 − 27,4 = 35,9 m
# Exercise bank additions: L1-06 and L1-07 are multiple choice (no number)
a["fy4-11-L1-08"] = round(0.75 * g, 1)                   # full grip on a level road: a = μg = 0,75 · 9,81 = 7,358 m/s² → 7,4 m/s²
vv = [10.0, 15.0, 20.0, 25.0]; ss = [6.5, 14.1, 25.9, 39.6]
k = 38.2 / 600.0                                         # line through the origin read at (600 m²/s², 38,2 m): k = 0,0637 s²/m
a["fy4-11-L2-05"] = round(1 / (2 * k), 1)                # s_j = v0²/(2a) → slope k = 1/(2a), a = 7,85 → 7,9 m/s²
k = 25.0 / 20.0                                          # F_ka = mΔv · (1/Δt): line through the origin and (20,0 1/s; 25,0 kN), k = 1,25 kN·s
a["fy4-11-L2-06"] = round(k * 1000 / 75.0 * 3.6, -1)     # Δv = 1250 N·s / 75,0 kg = 16,67 m/s = 60,0 km/h → 60
a["fy4-11-L2-07"] = round(12.0 * (90 / 50) ** 2, 1)      # s_j ∝ v0²: 12,0 m · 1,8² = 38,88 m → 38,9 m (the student's 1,8 · 12,0 = 21,6 m is wrong)
# L2-08 is multiple choice (prediction): F_ka = m Δv / Δt, Δv ×2 and Δt ×4 → F_ka ×0,50; no number
tr, aw, dsee = 1.2, 5.1, 55.0                            # wet road fit of s_p/v = t_r + v/(2a): t_r = 1,2 s, a = 5,1 m/s²; sight distance 55 m
vmax = -aw * tr + math.sqrt((aw * tr) ** 2 + 2 * aw * dsee)   # t_r v + v²/(2a) = d → v = 18,34 m/s
a["fy4-11-L3-04"] = round(vmax * 3.6, 0)                 # 66,0 km/h → 66 (stopping distance at 80 km/h is 75 m > 55 m)
vd = [15.0, 13.4, 10.1, 5.6, 2.2, 0.7, 0.0]              # dummy speed every 20 ms
steps = [vd[i] - vd[i + 1] for i in range(6)]            # Δv per 20 ms interval; the largest is 4,5 m/s (40–60 ms)
a["fy4-11-L3-05"] = round(80.0 * max(steps) / 0.020 / 1000, 1)   # F_max = m Δv/Δt = 80,0 kg · 4,5 m/s : 0,020 s = 18,0 kN
print(json.dumps(a))
