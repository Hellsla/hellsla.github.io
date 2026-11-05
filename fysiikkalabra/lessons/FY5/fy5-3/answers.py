"""Every answer in exercises.json for fy5-3, computed from the task data (python -I answers.py).
Uniform circular motion: f = 1/T, v = 2πr/T = 2πrf. Conversions by substitution (1 min = 60 s, 1 cm = 0,01 m).
Prints {exercise id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json, math

pi = math.pi
a = {}
# Level 1: one formula, values given
a["fy5-3-L1-01"] = 2 * pi * 2.5 / 6.0                    # carousel rim: v = 2π · 2,5 m / 6,0 s = 2,618 m/s -> 2,6 m/s
a["fy5-3-L1-02"] = 2 * pi * 0.20 * 15                    # fan blade tip: v = 2π · 0,20 m · 15 1/s = 18,85 m/s -> 19 m/s
a["fy5-3-L1-03"] = 1 / 4.0                               # windmill sails: f = 1 / 4,0 s = 0,25 1/s
a["fy5-3-L1-04"] = math.hypot(1.5, 3.0 * 2.0)            # puck after the string breaks: d = √(r² + (vt)²) = √(1,5² + 6,0²) m = 6,185 m -> 6,2 m
a["fy5-3-L1-05"] = 2 * pi * 6.78e6 / 5.55e3              # space station: v = 2π · 6,78e6 m / 5,55e3 s = 7675,6 m/s -> 7680 m/s
# Level 2: a conversion or a rearrangement
f_single = 45 / 60                                       # 45 1/min = 45 / 60 s = 0,75 1/s
a["fy5-3-L2-01"] = 2 * pi * (8.5 * 0.01) * f_single      # record rim: v = 2π · 0,085 m · 0,75 1/s = 0,4006 m/s -> 0,40 m/s
T_wheel = 2 * pi * (40 / 2) / 0.35                       # Ferris wheel: T = 2πr / v = 2π · 20 m / 0,35 m/s = 359,0 s
a["fy5-3-L2-02"] = T_wheel / 60                          # 359,0 s = 359,0 / 60 min = 5,98 min -> 6,0 min
f_cent = 45 / (2 * pi * 9.5 * 0.01)                      # centrifuge: f = v / (2πr) = 45 m/s / (2π · 0,095 m) = 75,39 1/s
a["fy5-3-L2-03"] = f_cent * 60                           # 75,39 1/s = 75,39 · 60 1/min = 4523 1/min -> 4500 1/min
a["fy5-3-L2-04"] = 65 * 20 / 52                          # same blade, same T: v ∝ r, v = 65 m/s · 20 m / 52 m = 25 m/s
# Level 3: reasoning, two ideas
a["fy5-3-L3-01"] = 7.0 * 40.2 / 36.5                     # side by side over the half circle: same time, v ∝ r: 7,0 · 40,2 / 36,5 = 7,710 m/s -> 7,7 m/s
v_car = 36 * 1000 / 3600                                 # 36 km/h = 36 · 1000 m / 3600 s = 10 m/s
a["fy5-3-L3-02"] = math.sqrt(2) * v_car                  # quarter lap: v̄₁ ⟂ v̄₂, |Δv̄| = √(v² + v²) = 14,14 m/s -> 14 m/s
v_chain = 2 * pi * 0.100 * 1.0                           # chain: v = 2π · 0,100 m · 1,0 1/s = 0,6283 m/s on both sprockets
f_rear = v_chain / (2 * pi * 0.040)                      # rear sprocket and wheel: f = 0,6283 / (2π · 0,040 m) = 2,5 1/s
v_bike = 2 * pi * 0.34 * f_rear                          # tyre around the hub = bike's speed (no slipping): 5,341 m/s
a["fy5-3-L3-03"] = v_bike * 3.6                          # 5,341 m/s = 5,341 · 3,6 km/h = 19,23 km/h -> 19 km/h
# Exercise bank additions (teacher 2026-11-04): L1-06 is multiple choice (no number)
a["fy5-3-L1-07"] = 1 / (3000 / 60)                       # crankshaft: f = 3000 / 60 s = 50 1/s, T = 1 / f = 0,020 s
a["fy5-3-L1-08"] = 2 * pi * 120 / 3600                   # minute hand: v = 2π · 120 mm / 3600 s = 0,2094 mm/s -> 0,21 mm/s
t10 = [41.2, 40.6, 41.8, 40.9, 41.5]                     # data of L2-05: ten laps, five timings
T_carousel = (sum(t10) / len(t10)) / 10                  # mean 41,2 s for ten laps -> T = 4,12 s
a["fy5-3-L2-05"] = 2 * pi * 2.1 / T_carousel             # seat: v = 2π · 2,1 m / 4,12 s = 3,203 m/s -> 3,2 m/s
sats = [(6.92e6, 95.5), (26.56e6, 717.9), (42.16e6, 1436)]   # data of L2-06: (r in m, T in min)
v_sat = [2 * pi * r / (T * 60) / 1000 for r, T in sats]  # km/s: 7,588 / 3,874 / 3,0745
a["fy5-3-L2-06"] = round(v_sat[2], 2)                    # geostationary: v = 2π · 42,16e6 m / 86160 s = 3,0745 km/s -> 3,07 km/s
a["fy5-3-L2-07"] = 2 * pi * (0.64 / 2) * 8.0             # radius = d / 2 = 0,32 m: v = 2π · 0,32 m · 8,0 1/s = 16,08 m/s -> 16 m/s
R_e, T_e = 6371e3, 86164                                 # Earth model: R = 6371 km, T = 86 164 s
v_lat = lambda phi: 2 * pi * R_e * math.cos(math.radians(phi)) / T_e   # latitude circle r = R cos φ
a["fy5-3-L3-04"] = v_lat(5.2) - v_lat(62.7)              # Kourou 462,7 m/s − Plesetsk 213,1 m/s = 249,6 m/s -> 250 m/s
N_turns = (58 - 25) / 1.6e-3                             # CD: (58 − 25) mm / 0,0016 mm = 20 625 turns
s_track = N_turns * 2 * pi * 0.0415                      # N · 2π r_ka, r_ka = 41,5 mm: 5378 m
a["fy5-3-L3-05"] = s_track / 1.2 / 60                    # t = s / v = 4482 s = 74,7 min -> 75 min
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
