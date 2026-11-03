"""Every answer in exercises.json for fy6-7, computed from the task data (python -I answers.py).
Electrical energy E = P t (kW · h = kWh, W · s = J), with P = U I; 1 kWh = 1000 W · 3600 s = 3,6 MJ.
Cost = price per kWh · E + fixed fees. Devices run at their rated power the whole time given.
Prints {exercise id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json

a = {}
# Level 1: one formula, values given
a["fy6-7-L1-01"] = 0.045 * 4.0                            # laptop 45 W = 0,045 kW for 4,0 h: 0,18 kWh
a["fy6-7-L1-02"] = 0.15 * 3.6                             # 0,15 kWh = 0,15 · 3,6 MJ = 0,54 MJ
a["fy6-7-L1-03"] = 1200 / 230                             # iron 1200 W on 230 V: I = P : U = 5,22 A
a["fy6-7-L1-04"] = 350 * 0.150                            # 350 kWh at 15,0 snt/kWh = 0,150 EUR/kWh: 52,5 EUR
a["fy6-7-L1-05"] = 0.0060 * 5.0 * 365                     # LED 6,0 W, 5,0 h a day, 365 days: 10,95 kWh
# Level 2: two steps, a conversion or a figure
# figure fy6-7/washer: 2,0 kW for 0,25 h, 0,20 kW for 1,0 h, 0,40 kW for 0,25 h
a["fy6-7-L2-01"] = 2.0 * 0.25 + 0.20 * 1.0 + 0.40 * 0.25  # areas: 0,50 + 0,20 + 0,10 = 0,80 kWh
a["fy6-7-L2-02"] = 230 * 8.7 * 4.0 * 60 / 1000            # kettle 230 V, 8,7 A, 4,0 min = 240 s: E = U I t = 480 kJ
a["fy6-7-L2-03"] = 0.0045 * 24 * 365 * 0.17               # standby 4,5 W all year (8760 h) = 39,42 kWh at 17 snt: 6,70 EUR
a["fy6-7-L2-04"] = (0.060 - 0.0080) * 4.0 * 365           # 60 W -> 8,0 W LED, 4,0 h a day: 52 W · 1460 h = 75,9 kWh
# Level 3: reasoning
a["fy6-7-L3-01"] = 2200 * 3.0 / 15 / 60                   # same energy: 2200 W · 3,0 min = 15 W · t -> t = 440 min = 7,33 h
a["fy6-7-L3-02"] = (64.20 - 8.50) / 0.150                 # bill: 64,20 EUR - 8,50 EUR fixed = 55,70 EUR at 0,150 EUR/kWh: 371 kWh
I_el = 230 / 26.5                                         # heating element 26,5 ohm on 230 V: I = U : R = 8,68 A
a["fy6-7-L3-03"] = 230 * I_el * 2.50 / 1000               # P = U I = 1996 W; E = P t = 1,996 kW · 2,50 h = 4,99 kWh
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
