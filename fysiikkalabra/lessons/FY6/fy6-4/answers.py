"""Every answer in exercises.json for fy6-4, computed from the task data (python -I answers.py).
Series: R = R1 + R2 + ..., the same current through every resistor, U = U1 + U2 + ...
Parallel: 1/R = 1/R1 + 1/R2 + ..., the same voltage over every branch, I = I1 + I2 + ...
Ohm's law in every resistor: U = R I. Prints {exercise id: number} as JSON on the last line."""
import json, math

par = lambda *R: 1 / sum(1 / r for r in R)              # total resistance of resistors in parallel
a = {}
# Level 1: one formula, values given
a["fy6-4-L1-01"] = 120 + 220 + 330                       # three resistors in series: 670 ohm
a["fy6-4-L1-02"] = par(40, 60)                           # 40 ohm || 60 ohm: 1/R = 1/40 + 1/60 = 5/120 -> 24 ohm
a["fy6-4-L1-03"] = 0.20 + 0.45 + 0.85                    # car interior lamps in parallel: I = I1 + I2 + I3 = 1,50 A
a["fy6-4-L1-04"] = 4.5 - 1.8                             # two lamps in series on 4,5 V, 1,8 V over one: U2 = 2,7 V
a["fy6-4-L1-05"] = par(330, 330, 330)                    # three equal 330 ohm in parallel: 330/3 = 110 ohm
# Level 2: two steps, a conversion or a rearrangement
R_s = 1.2 * 1000 + 680                                   # 1,2 kohm = 1,2 * 1000 ohm; series R = 1880 ohm
a["fy6-4-L2-01"] = 9.0 / R_s * 1000                      # I = U / R = 9,0 V / 1880 ohm = 4,787 mA -> 4,8 mA
a["fy6-4-L2-02"] = (6.0 - 2.5) / 0.10                    # indicator lamp 2,5 V, 0,10 A on 6,0 V: U_R = 3,5 V, R = 3,5 V : 0,10 A = 35 ohm
a["fy6-4-L2-03"] = 6.0 / (0.50 - 6.0 / 30)               # parallel 30 ohm and R2 on 6,0 V, total 0,50 A: I1 = 0,20 A, I2 = 0,30 A, R2 = 20 ohm
a["fy6-4-L2-04"] = par(2.2 * 1000, 3.3 * 1000) / 1000    # 2,2 kohm || 3,3 kohm = 1320 ohm = 1,32 kohm -> 1,3 kohm
# Level 3: reasoning or an unfamiliar context
R23 = par(60, 120)                                       # figure task-mixed: R2 = 60 ohm || R3 = 120 ohm = 40 ohm
I_tot = 12 / (40 + R23)                                  # R1 = 40 ohm in series: R = 80 ohm, I = 12 V / 80 ohm = 0,15 A
a["fy6-4-L3-01"] = I_tot * R23 / 120 * 1000              # U23 = 0,15 A * 40 ohm = 6,0 V, I3 = 6,0 V / 120 ohm = 0,050 A = 50 mA
I_series = 230 / (46 + 46)                               # heater, two 46 ohm elements in series on 230 V: 2,5 A
I_parallel = 230 / par(46, 46)                           # the same elements in parallel: 230 V / 23 ohm = 10 A
a["fy6-4-L3-02"] = I_parallel / I_series                 # 4 times the current
S, P = 250, 60                                           # series 250 ohm, parallel 60 ohm: R1 + R2 = 250, R1 R2 = 60 * 250 = 15 000
a["fy6-4-L3-03"] = (S + math.sqrt(S ** 2 - 4 * P * S)) / 2   # R^2 - 250 R + 15 000 = 0 -> R = 150 ohm or 100 ohm; the larger 150 ohm
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
