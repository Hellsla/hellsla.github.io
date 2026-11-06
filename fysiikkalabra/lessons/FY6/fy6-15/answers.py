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
# Exercise-bank additions (L1-06, L1-07 and L2-07's written part are multiple choice or text; no number)
# YO-skill form (teacher 2026-11-05): L1-09 is an ordering task (no number); I = U : R = 1,2 / 5,0 / 140 (143,75) / 40 mA for A / B / C / D
a["fy6-15-L1-08"] = 3.0e6 * 2.0e-3 / 1e3                   # air gap 2,0 mm: U_max = E_max d = 6000 V = 6,0 kV
R_55 = [55.0, 0.90]                                        # kOhm: dry skin + rubber shoes, and bathtub; same 230 V, so I_4 : I_1 = R_1 : R_4
a["fy6-15-L2-05"] = (U / (R_55[1] * 1e3)) / (U / (R_55[0] * 1e3))   # 255,6 mA : 4,18 mA = 61,1 times
P_dev = [2000, 1400, 1100, 800, 600]                       # table of devices (W) on a 10 A fuse: P_max = 2300 W
pairs = [x + y for i, x in enumerate(P_dev) for y in P_dev[i + 1:] if x + y <= U * 10]
a["fy6-15-L2-06"] = max(pairs) / U                         # best pair 1400 + 800 = 2200 W: I = 2200 : 230 = 9,565 A
a["fy6-15-L2-07"] = U / 2.00e3 * 1e3                       # fuse does not see the body: 230 V over 2,00 kOhm = 115 mA
def slope_through_origin(xs, ys):                          # least squares y = k x: k = sum(xy) : sum(x^2)
    return sum(x * y for x, y in zip(xs, ys)) / sum(x * x for x in xs)
I_cord = [4.0, 8.0, 12.0, 16.0]                            # A; measured rises of the cord's temperature (K)
dT_cord = [2.1, 7.6, 17.2, 30.4]
P_cord = [0.40 * i ** 2 for i in I_cord]                   # P = R I^2 with R = 0,40 Ohm: 6,4 ... 102,4 W
k_cord = slope_through_origin(P_cord, dT_cord)             # k = 0,2974 K/W
a["fy6-15-L3-04"] = (50.0 / (k_cord * 0.40)) ** 0.5        # dT = k R I^2 = 50 K: I = 20,5 A
a["fy6-15-L3-05"] = (U / 30e-3 - 1.5e3) / 1e3              # RCD trips above 30 mA: R_e + R_k = U : 30 mA, R_e = 7667 - 1500 = 6167 Ohm = 6,167 kOhm
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
