"""Every answer in exercises.json for fy6-15, computed from the task data (python -I answers.py).
The loads of a group are in parallel at U = 230 V, so I = (P1 + P2 + ...) : U and the fuse's rated current I_s allows
P_max = U I_s; a conductor heats with P = R I^2; the current through the body I = U : R (R of the whole current path,
resistances in series add up); an insulating air gap withstands U_max = E_max d (uniform field assumed).
Prints {exercise id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json

U = 230.0
a = {}
# Level 1: one formula, values given
a["fy6-15-L1-01"] = 1500 / U                               # fan heater 1500 W on 230 V: I = P : U = 6,52 A
a["fy6-15-L1-02"] = U * 10                                 # 10 A fuse: P_max = U I_s = 2300 W
a["fy6-15-L1-03"] = U / 2.3e3 * 1e3                        # 230 V over 2,3 kOhm: I = U : R = 0,100 A = 100 mA
a["fy6-15-L1-04"] = U / 50e3 * 1e3                         # dry, rubber soles: 230 V over 50 kOhm = 4,6 mA
a["fy6-15-L1-05"] = 0.20 * 16 ** 2                         # cord 0,20 Ohm at 16 A: P = R I^2 = 51,2 W
# Level 2: two steps, a conversion or a rearrangement
a["fy6-15-L2-01"] = U * 16 - (2000 + 1200)                 # 16 A group: 3680 W - 3200 W in use = 480 W left
I_heater = 2000 / U                                        # heater 2000 W: I = 8,70 A (from 230 V)
a["fy6-15-L2-02"] = 0.30 * I_heater ** 2                   # cord 0,30 Ohm: P = R I^2 = 22,7 W
a["fy6-15-L2-03"] = 90e3 / 3.0e6 * 100                     # d = U : E_max = 90 kV : 3,0 MV/m = 0,030 m = 3,0 cm
a["fy6-15-L2-04"] = 10e-3 * 1.5e3                          # I below 10 mA through 1,5 kOhm: U = R I = 15 V
# Level 3: reasoning, two ideas
P10 = 0.50 * 10 ** 2                                       # wires 0,50 Ohm at the design current 10 A: 50 W
P22 = 0.50 * 22 ** 2                                       # at 22 A behind a 25 A fuse: 242 W
a["fy6-15-L3-01"] = P22 / P10                              # (22 : 10)^2 = 4,84 times
a["fy6-15-L3-02"] = U / (1.5e3 + 100e3) * 1e3              # body 1,5 kOhm + shoes and floor 100 kOhm in series: 2,27 mA
# figure fy6-15/ex-askel: V(r) = 1200 V·m / r; feet at 2,0 m and 3,0 m read 600 V and 400 V on gridlines
U_step = 1200 / 2.0 - 1200 / 3.0                           # step voltage 200 V
a["fy6-15-L3-03"] = U_step / 4.0e3 * 1e3                   # foot to foot 4,0 kOhm: I = 200 V : 4,0 kOhm = 50 mA
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
