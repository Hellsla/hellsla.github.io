"""Every answer in exercises.json for fy2-3, computed from the task data (python -I answers.py).
Model: P = E : t, E = P t; 1 kWh = 1000 W · 3600 s = 3 600 000 J; a year has 365 · 24 h = 8760 h; price 20 snt/kWh = 0,20 €/kWh.
Prints {exercise id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json

KWH = 1000 * 3600            # J per kWh
YEAR_H = 365 * 24            # h per year
PRICE = 0.20                 # euro per kWh (rounded example price)
a = {}
# Level 1: one formula
a["fy2-3-L1-01"] = 1.80e5 / 90.0                      # P = E : t = 180 000 J : 90,0 s = 2000 W
a["fy2-3-L1-02"] = 8.0 * 5.0                          # E = P t = 8,0 W · 5,0 s = 40 J
a["fy2-3-L1-03"] = 72000 / 1200                       # t = E : P = 72 000 J : 1200 W = 60 s
a["fy2-3-L1-04"] = (120e3 - 60e3) / (80 - 40)          # read off fy2-3/graph-ab, line A: (40 s; 60 kJ) and (80 s; 120 kJ) -> 60 000 J : 40 s = 1500 W
a["fy2-3-L1-05"] = 1.5 * 2.0                          # E = P t = 1,5 kW · 2,0 h = 3,0 kWh
# Level 2: conversion or two steps
a["fy2-3-L2-01"] = 6.0 * (150 / 60) * PRICE               # 150 min = 2,5 h; E = 6,0 kW · 2,5 h = 15 kWh; 15 kWh · 0,20 €/kWh = 3,0 €
a["fy2-3-L2-02"] = 15 * 3600                          # 15 Wh = 15 W · 3600 s = 54 000 J
a["fy2-3-L2-03"] = 0.40 * KWH / (20 * 60)             # 0,40 kWh = 1,44e6 J; 20 min = 1200 s; P = 1200 W
a["fy2-3-L2-04"] = 6 * 1.5 / 1000 * YEAR_H            # six exit-sign lights: 6 · 1,5 W = 9,0 W = 0,0090 kW; · 8760 h = 78,84 kWh
# Level 3: reasoning, several ideas
a["fy2-3-L3-01"] = (60 - 8.0) / 1000 * 4.0 * 365 * PRICE   # (60 W - 8,0 W) = 0,052 kW; 4,0 h · 365 = 1460 h; 75,92 kWh; 15,18 €
a["fy2-3-L3-02"] = 3.0e3 / YEAR_H * 1000              # P = 3000 kWh : 8760 h = 0,3425 kW = 342,5 W
a["fy2-3-L3-03"] = 2.3 * 8.0 / 18 * 100               # 2,3 kW · 8,0 h = 18,4 kWh; 18,4 kWh : 18 kWh/100 km = 102,2 km
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
