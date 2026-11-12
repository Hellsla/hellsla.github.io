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
# Exercise bank additions (L1-06 and L1-07 are multiple choice: no number)
a["fy2-3-L1-08"] = 3.6e6 / (2.0 * 60) / 1000          # 3,6 MJ : 120 s = 30 000 W = 30 kW
a["fy2-3-L2-05"] = (100 * 8.0 + 80 * 3.5 + 50 * 6.0 + 2000 * 0.20 + 1800 * 0.10) / 1000   # 800+280+300+400+180 = 1960 Wh = 1,96 kWh
a["fy2-3-L2-06"] = 2.0 * (90 / 60)                    # 90 min = 1,5 h; E = 2,0 kW · 1,5 h = 3,0 kWh
a["fy2-3-L2-07"] = (1.50 - 0.0) / (50 / 60) * 1000    # fitted line (0 min; 0 kWh)-(50 min; 1,50 kWh): 1,80 kW = 1800 W
cons = [8400, 9100, 9900, 10400, 10600, 10300, 9800, 9600]; prod = [8900, 8900, 9300, 9600, 9800, 9900, 9900, 9800]
a["fy2-3-L3-04"] = sum(c - p for c, p in zip(cons, prod) if c > p) * 1.0 / 1000   # 200+600+800+800+400 = 2800 MWh = 2,8 GWh
run = 11.5 + 12.0 + 11.5 + 12.0; off = 18.0 + 18.5 + 17.5 + 18.0
a["fy2-3-L3-05"] = (100 * run / (run + off) / 1000 * YEAR_H - 130) * PRICE   # 39,5 W; 346 kWh; (346 - 130) kWh · 0,20 €/kWh = 43,2 €
# fy2-3-L2-08 is multiple choice: no number (P doubles: 6,0 kWh : 1,5 h = 4,0 kW vs 6,0 kWh : 3,0 h = 2,0 kW)
a["fy2-3-L1-09"] = 5.0 * 735.5 * 30 * 60 / 1e6     # 5,0 hp · 735,5 W/hp (MAFY) = 3677,5 W; 30 min = 1800 s; E = Pt = 6 619 500 J = 6,6 MJ
a["fy2-3-L1-10"] = 40 * 1000 / 80                  # read off fy2-3/graph-ab: line B through (80 s; 40 kJ): P = 40 000 J : 80 s = 500 W
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
