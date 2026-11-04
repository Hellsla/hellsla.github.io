"""Every answer in exercises.json for fy1-4, computed from the task data (python -I answers.py).
The slope of a line through (x1, y1) and (x2, y2) is k = (y2 - y1)/(x2 - x1); y = k x + b gives b = y1 - k x1.
Prints {exercise id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json

a = {}


def fit(pts):
    """Least-squares line y = k x + b through the points (a student's by-eye line lands within the tolerance)."""
    n = len(pts)
    xm, ym = sum(x for x, _ in pts) / n, sum(y for _, y in pts) / n
    k = sum((x - xm) * (y - ym) for x, y in pts) / sum((x - xm) ** 2 for x, _ in pts)
    return k, ym - k * xm


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
# Exercise bank additions (teacher 2026-11-04): L1-06 and L1-07 are multiple choice (no number)
a["fy1-4-L1-08"] = 7.0 - 1.5 * 3.0                        # spring: b = l1 − k m1 = 7,0 cm − 1,5 cm/kg · 3,0 kg = 2,5 cm
sp = [(50.0, 4.1), (100.0, 8.3), (150.0, 11.8), (200.0, 16.5), (250.0, 20.2), (300.0, 23.9)]   # data of L2-05
a["fy1-4-L2-05"] = round(fit(sp)[0], 3)                   # least-squares slope 0,0797 mm/g -> 0,080 (tolerance 0,05: 0,076…0,084)
cx = [(0.0, 0.82), (1.0, 1.31), (2.0, 1.68), (3.0, 2.22), (4.0, 2.57), (5.0, 3.09)]            # data of L2-06
a["fy1-4-L2-06"] = round(fit(cx)[1], 2)                   # intercept b = 0,829 m (slope 0,448 m/s) -> 0,83 m (tolerance 0,10: 0,75…0,91)
V = [10.0, 20.0, 30.0, 40.0, 50.0]                        # data of L2-07
mA, mB = [27.4, 53.8, 82.1, 108.9, 135.2], [78.6, 156.8, 237.1, 313.5, 392.0]
kA, kB = fit(list(zip(V, mA)))[0], fit(list(zip(V, mB)))[0]   # 2,707 g/cm³ and 7,835 g/cm³
a["fy1-4-L2-07"] = round(kB / kA, 1)                      # 7,835 / 2,707 = 2,89 -> 2,9 (tolerance 0,05: 2,76…3,04)
sx = [(100.0, 8.1), (200.0, 16.3), (300.0, 24.2), (400.0, 32.5), (500.0, 40.1), (600.0, 51.8), (700.0, 68.9)]   # data of L3-04
a["fy1-4-L3-04"] = round(fit(sx[:5])[0], 3)               # linear part 100…500 g: 0,0802 mm/g (the points at 600 and 700 g lie 3,5 and 12,6 mm above the line)
k_hi, k_lo = (3.50 - 0.20) / 6.0, (3.00 - 0.60) / 6.0     # steepest 0,55 m/s, shallowest 0,40 m/s
a["fy1-4-L3-05"] = ((k_hi - k_lo) / 2) / ((k_hi + k_lo) / 2) * 100   # 0,075 / 0,475 = 15,8 % -> 16 %
# Inquiry tasks (not in exercises.json): graph reading k = (50 − 20) km / (3,0 − 1,0) h = 15 km/h; walk tarkistus-2 k = 3,0 km/h, b = 4,0 km, t = 7,0 h (swapped k and b: (25 − 3,0)/4,0 = 5,5 h); kettle example k = (60,0 − 20,0)/5,0 = 8,0 °C/min, t(40 °C) = (40 − 20)/8,0 = 2,5 min
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
