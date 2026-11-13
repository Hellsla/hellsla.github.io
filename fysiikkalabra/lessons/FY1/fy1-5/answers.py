"""Every answer in exercises.json for fy1-5, computed from the task data (python -I answers.py).
Uniform motion: s = s0 + v t, so the distance travelled is v t and v = (change of s) / (change of t).
Voyager 2 (model values, sources in the lesson): d0 = 119,0 AU from the Sun on 2018-11-05 (Burlaga et al. 2019, Nature Astronomy 3),
v = 15,341 km/s relative to the Sun at the crossing (NASA/JPL), kept constant, 1 AU = 149 597 870,7 km, c = 299 792 458 m/s.
Prints {exercise id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json

AU = 149_597_870.7          # km
V_VOY = 15.341              # km/s
D0_VOY = 119.0              # AU from the Sun on 2018-11-05 (heliopause crossing)
C = 299_792_458             # m/s
DAY = 86_400                # s
a = {}
# Level 1: one formula, values given
a["fy1-5-L1-01"] = 5.5 * 20                       # s = v t = 5,5 m/s · 20 s = 110 m
a["fy1-5-L1-02"] = 360 / 45                       # v = s / t = 360 m / 45 s = 8,0 m/s
a["fy1-5-L1-03"] = 150 / (20 / 8)                  # figure fy1-5/line-read: (0; 0) and (8 s; 20 m) -> v = 2,5 m/s; t = 150 m / 2,5 m/s = 60 s
a["fy1-5-L1-04"] = 18 / 4.0 * 10                  # s0 = 0, so s / t is constant: s = (18 m / 4,0 s) · 10 s = 45 m
a["fy1-5-L1-05"] = (21 - 7.0) / (6.0 - 2.0)       # v = Δs / Δt = (21 m − 7,0 m) / (6,0 s − 2,0 s) = 3,5 m/s
# Level 2: a conversion or a rearrangement, or s = s0 + v t
a["fy1-5-L2-01"] = 54 / 3.6 * 14                  # 54 km/h = 15 m/s; s = 15 m/s · 14 s = 210 m
a["fy1-5-L2-02"] = 4500 / (36 / 3.6)              # 36 km/h = 10 m/s, 4,5 km = 4500 m; t = 4500 m / 10 m/s = 450 s
a["fy1-5-L2-03"] = (1500 + 1.5 * 600) / 1000      # s = s0 + v t = 1500 m + 1,5 m/s · 600 s = 2400 m = 2,4 km
a["fy1-5-L2-04"] = 343 * 5.0 / 1000               # light arrives at once: s = v t = 343 m/s · 5,0 s = 1715 m = 1,7 km
# Level 3: reasoning, two ideas, an unfamiliar context
v_au_day = V_VOY * DAY / AU                       # Voyager 2: 15,341 km/s · 86 400 s / 149 597 870,7 km = 0,0088602 AU per day
a["fy1-5-L3-01"] = (150 - D0_VOY) / v_au_day      # s = s0 + v t -> t = (150 − 119,0) AU / v = 3498,8 days -> 3,50·10^3 d
t_signal = 150 * AU * 1000 / C                    # one way: 150 AU = 2,2440·10^13 m; t = s / c = 74 851 s
a["fy1-5-L3-02"] = 2 * t_signal / 3600            # there and back = 149 702 s = 41,58 h -> 41,6 h
# catch-up: first friend s1 = 1,5 t, second s2 = 4,5 (t − 40); equal when 1,5 t = 4,5 t − 180 -> t = 60 s
t_meet = 4.5 * 40 / (4.5 - 1.5)
a["fy1-5-L3-03"] = 1.5 * t_meet                   # s = 1,5 m/s · 60 s = 90 m
# exercise-bank additions (L1-06..08, L2-05..07, L3-04..05)
a["fy1-5-L1-07"] = 0.80 * 12                      # area of the rectangle in the (t, v) graph: s = v t = 0,80 m/s · 12 s = 9,6 m
a["fy1-5-L1-08"] = 2400 / (16 * 60)               # 2,4 km = 2400 m, 16 min = 960 s; v = 2400 m / 960 s = 2,5 m/s
pts5 = [(0, 1.2), (1, 2.7), (2, 3.9), (3, 5.5), (4, 6.7), (5, 8.3)]   # video analysis of the walker
tm5, xm5 = sum(t for t, _ in pts5) / 6, sum(x for _, x in pts5) / 6
k5 = sum((t - tm5) * (x - xm5) for t, x in pts5) / sum((t - tm5) ** 2 for t, _ in pts5)   # least-squares slope 1,403 m/s (by eye: 1,35…1,45)
a["fy1-5-L2-05"] = round(xm5 + k5 * (12 - tm5))   # s(12 s) = 18,04 m -> 18 m (tolerance 0,04: 17,3…18,7; a by-eye line gives 17,5…18,5)
v6 = (11 - 8.0) / 2.0                             # v = Δs / Δt = 3,0 m / 2,0 s = 1,5 m/s
a["fy1-5-L2-06"] = 8.0 + v6 * 6.0                 # s = s0 + v t = 8,0 m + 1,5 m/s · 6,0 s = 17 m (not 33 m)
t7 = 0.2 / 0.020                                  # 0,2 s / t <= 2,0 % -> t >= 10 s
a["fy1-5-L2-07"] = 0.80 * t7                      # s = v t = 0,80 m/s · 10 s = 8,0 m
# L3-04: speed changes at t = 10 s (3,0 m/s then 1,0 m/s); s(5 s) = 15 m, s(35 s) = 30 m + 1,0 m/s · 25 s = 55 m
a["fy1-5-L3-04"] = (55.0 - 15.0) / (35.0 - 5.0)   # 40 m / 30 s = 1,33 m/s -> 1,3 m/s (the mean of 3,0 and 1,0 m/s would be 2,0 m/s, wrong)
# L3-05: bullet filmed every 0,010 s, 3,0 m between frames
a["fy1-5-L3-05"] = 3.0 / 0.010                    # v = 3,0 m / 0,010 s = 300 m/s
# the worked example in lesson.md (not an exercise): Voyager 2 on 2026-11-05, 2922 days after 2018-11-05
n_days = 2922                                     # 8 years with the leap days 2020 and 2024
ds_au = V_VOY * n_days * DAY / AU                 # 15,341 km/s · 252 460 800 s / 149 597 870,7 km = 25,889 AU
print(f"# model check: d(2026-02-15) = {D0_VOY + v_au_day * 2659:.2f} AU from the Sun (JPL, Feb 2026: 143,05 AU from Earth)")
print(f"# worked example: distance travelled {ds_au:.4f} AU, d = {D0_VOY + ds_au:.3f} AU, one-way signal {(D0_VOY + ds_au) * AU * 1000 / C / 3600:.2f} h")
a["fy1-5-L1-09"] = 1482.3 * 2.0 / 1000      # MAFY: sound in water at 20 °C 1482,3 m/s; s = v t = 1482,3 m/s · 2,0 s = 2964,6 m = 2,9646 km
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
