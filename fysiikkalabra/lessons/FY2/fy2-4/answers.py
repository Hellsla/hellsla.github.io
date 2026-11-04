"""Every answer in exercises.json for fy2-4, computed from the task data (python -I answers.py).
Efficiency of one device: eta = E_a / E_o = P_a / P_o; E_o = E_a + E_h; E = P t. Percentages: 1 % = 0,01.
Prints {exercise id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json

a = {}
# Level 1: one formula, values given
a["fy2-4-L1-01"] = 340 / 400 * 100                        # motor: eta = E_a / E_o = 340 J / 400 J = 0,85 = 85 %
a["fy2-4-L1-02"] = 2.4 / 8.0 * 100                        # LED lamp: eta = P_a / P_o = 2,4 W / 8,0 W = 0,30 = 30 %
a["fy2-4-L1-03"] = 0.050 * 60                             # filament lamp: P_a = eta P_o = 0,050 · 60 W = 3,0 W
a["fy2-4-L1-04"] = 1800 / 0.90                            # motor: E_o = E_a / eta = 1800 J / 0,90 = 2000 J
a["fy2-4-L1-05"] = (1 - 0.20) * 5.0                       # solar panel: E_h = E_o − E_a = 5,0 kJ − 0,20 · 5,0 kJ = 4,0 kJ
# Level 2: two steps, a conversion or a rearrangement
a["fy2-4-L2-01"] = 0.80 * (1.0 * 1000) * (2.0 * 60) / 1000   # motor: 1,0 kW = 1000 W, 2,0 min = 120 s; E_a = eta P_o t = 96 000 J = 96 kJ
a["fy2-4-L2-02"] = (0.30 * 9.0) / 0.050                   # same light: P_a = 0,30 · 9,0 W = 2,7 W; bulb P_o = P_a / 0,050 = 54 W
a["fy2-4-L2-03"] = (1 - 0.050) * (60 * 0.001) * 4.0       # bulb: 60 W = 0,060 kW; E_o = 0,060 kW · 4,0 h = 0,24 kWh; E_h = 0,95 · 0,24 kWh = 0,228 kWh
a["fy2-4-L2-04"] = 15 / 0.25 - 15                         # engine: P_o = P_a / eta = 15 kW / 0,25 = 60 kW; P_h = 60 kW − 15 kW = 45 kW
# Level 3: reasoning, two ideas, an unfamiliar context
a["fy2-4-L3-01"] = (150 / 200) / ((4.0 - 2.0) / 4.0)      # A: 150/200 = 0,75; B: (4,0 − 2,0)/4,0 = 0,50; ratio 1,5
a["fy2-4-L3-02"] = 0.50e6 / (0.20 * (1.2 * 1000))         # panel: 1,2 kW = 1200 W, 0,50 MJ = 500 000 J; t = E_a / (eta P_o) = 2083 s
a["fy2-4-L3-03"] = 240 * 6 / 8                           # read off fy2-4/grid: input 8 squares = 240 J, loss arrow 6 squares -> 180 J
# Exercise bank additions (teacher 2026-11-04): L1-06 and L2-07 are multiple choice (no number)
a["fy2-4-L1-07"] = 36 - 27                                # drill: E_h = E_o − E_a = 36 kJ − 27 kJ = 9,0 kJ
a["fy2-4-L1-08"] = 180 / 0.90                             # generator: P_o = P_a / eta = 180 kW / 0,90 = 200 kW
a["fy2-4-L2-05"] = (2.7 / 9.0) / (2.8 / 40)               # lamps: led 2,7/9,0 = 0,30; halogen 2,8/40 = 0,070; ratio 4,3
a["fy2-4-L2-06"] = 95 / 120 * 100                         # motor table, last row: eta = E_a / E_o = 95 kJ / 120 kJ = 79 %
a["fy2-4-L3-04"] = (6.0 * 32 / 3.6) / 17                  # petrol 6,0 l · 32 MJ/l = 192 MJ = 53,3 kWh (1 kWh = 3,6 MJ); / 17 kWh = 3,1
a["fy2-4-L3-05"] = (1510 / 2160) * (2160 / 240) * (3.0 * 365) / 1000   # led: P_o = 2160 J / 240 s = 9,0 W; E_o,year = 9,0 W · 1095 h = 9,855 kWh; heat share 1510/2160 = 0,70; E_h,year = 6,9 kWh (eta = 30 %, cost 1,4 EUR)
# Inquiry tasks (not in exercises.json) are in lesson-answers.py
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
