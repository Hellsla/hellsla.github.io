"""Every answer in exercises.json for fy1-4, computed from the task data (python -I answers.py).
The slope of a line through (x1, y1) and (x2, y2) is k = (y2 - y1)/(x2 - x1); y = k x + b gives b = y1 - k x1.
Prints {exercise id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json

a = {}
# Level 1: one formula, values given
a["fy1-4-L1-01"] = (10.1 - 2.3) / (7.0 - 1.0)             # cart: k = Δs/Δt = 7,8 m / 6,0 s = 1,3 m/s
a["fy1-4-L1-02"] = 0.50 * 30 + 12                         # pool level: h = 0,50 cm/min · 30 min + 12 cm = 27 cm
a["fy1-4-L1-03"] = (10 - 4.0) / 0.60                      # grass: h = k t + b -> t = (h − b)/k = (10 − 4,0)/0,60 = 10 vrk
a["fy1-4-L1-04"] = (14.0 - 20.0) / (4.0 - 0.0)            # candle: k = (14,0 − 20,0) cm / (4,0 − 0) h = −1,5 cm/h
a["fy1-4-L1-05"] = 1.2 / 250 * 1000                       # paper: line through origin, m = k N, k = 1,2 kg/250 = 4,8 g per sheet
# Level 2: two steps, one conversion or one rearrangement
a["fy1-4-L2-01"] = (1.50 - 0.30) * 1000 / ((10.0 - 2.0) * 60)   # 1,20 km = 1200 m, 8,0 min = 480 s -> k = 2,5 m/s
pts = [(1, 0.6), (2, 0.8), (3, 1.6), (4, 2.1), (5, 2.4), (6, 2.9)]   # the points of figure fy1-4/scatter-points (figures.py CART)
tm, sm = sum(t for t, _ in pts) / 6, sum(s for _, s in pts) / 6
k2 = sum((t - tm) * (s - sm) for t, s in pts) / sum((t - tm) ** 2 for t, _ in pts)   # least-squares slope 0,48 m/s (a by-eye line: 0,47…0,50)
a["fy1-4-L2-02"] = round(sm + k2 * (8.0 - tm), 1)        # cart at 8,0 s: 1,733 + 0,48 · 4,5 = 3,89 m -> 3,9 m (tolerance 0,08: 3,6…4,2 m)
k3 = (9.9 - 3.9) / (9.0 - 3.0)                            # canister: k = 6,0 kg / 6,0 l = 1,0 kg/l
a["fy1-4-L2-03"] = 3.9 - k3 * 3.0                         # b = m1 − k V1 = 3,9 − 1,0 · 3,0 = 0,9 kg (empty canister)
a["fy1-4-L2-04"] = (4.0 + 2.5 * 10) / (4.0 + 2.5 * 5.0)   # taxi fare 29,0 € / 16,5 € = 1,757 -> 1,8
# Level 3: reasoning or an unfamiliar context
a["fy1-4-L3-01"] = -0.40 / 0.85                           # s = 0,85 t + 0,40: s = 0 at t = −b/k = −0,47 s
a["fy1-4-L3-02"] = ((72 - 90) / 10) / ((51 - 60) / 10)    # slopes −1,8 °C/min and −0,90 °C/min -> ratio 2,0
a["fy1-4-L3-03"] = (0.2 / (2.0 * (4.5 - 4.0))) / (0.2 / (2.0 * (9.0 - 1.0)))   # relative error of k: 0,2/1,0 = 0,2 vs 0,2/16 = 0,0125 -> 16
# Inquiry tasks (not in exercises.json): graph reading k = (50 − 20) km / (3,0 − 1,0) h = 15 km/h; walk tarkistus-2 k = 3,0 km/h, b = 4,0 km, t = 7,0 h (swapped k and b: (25 − 3,0)/4,0 = 5,5 h); kettle example k = (60,0 − 20,0)/5,0 = 8,0 °C/min, t(40 °C) = (40 − 20)/8,0 = 2,5 min
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
