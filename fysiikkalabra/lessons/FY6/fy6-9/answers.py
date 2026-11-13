"""Every answer in exercises.json for fy6-9, computed from the task data (python -I answers.py).
Capacity: the charge a battery delivers, Q = I t (1 Ah = 1 A · 3600 s = 3600 C). Stored energy W = U Q with the
nominal voltage (1 Wh = 3600 J). Charging circuit (voltage law round the loop): U_lat - R I - R_s I - E = 0, so
I = (U_lat - E) / (R + R_s); terminal voltage while charging U = E + R_s I. Losses in a resistance: W = R I^2 t.
Prints {exercise id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json

a = {}
# Level 1: one formula, values given
a["fy6-9-L1-01"] = 0.25 * 8.0                             # Q = I t = 0,25 A · 8,0 h = 2,0 Ah
a["fy6-9-L1-02"] = 3000 * 0.001 * 3600                    # 3000 mAh = 3,0 Ah = 3,0 · 3600 C = 10 800 C
a["fy6-9-L1-03"] = 36 * 13                                # W = U Q = 36 V · 13 Ah = 468 Wh
a["fy6-9-L1-04"] = 2.4 / 0.15                             # t = Q : I = 2,4 Ah : 0,15 A = 16 h
# figure fy6-9/ex-current: 2,0 A for 0-1,5 h, then 1,0 A for 1,5-2,5 h; the charge is the area under the graph
a["fy6-9-L1-05"] = 2.0 * 1.5 + 1.0 * (2.5 - 1.5)          # 3,0 Ah + 1,0 Ah = 4,0 Ah
# the multiple-choice tasks fy6-9-L1-06, fy6-9-L1-07 and fy6-9-L1-09 have a text answer and no number
a["fy6-9-L1-08"] = 2600 * 0.001 / 0.50                    # 2600 mAh = 2,6 Ah; t = Q : I = 2,6 Ah : 0,50 A = 5,2 h
# Level 2: two steps, a conversion or a rearrangement
a["fy6-9-L2-01"] = (14.4 - 12.4) / (0.36 + 40 * 0.001)   # R_s = 40 mohm = 0,040 ohm; I = 2,0 V : 0,40 ohm = 5,0 A
a["fy6-9-L2-02"] = (5.0 - 3.8) / 1.2 - 0.80               # R_s = (U_lat - E) : I - R = 1,0 - 0,80 = 0,20 ohm
Q_23 = (0.80 - 0.15) * 4.5                                # 15 % -> 80 % of 4500 mAh: 0,65 · 4,5 Ah = 2,925 Ah
a["fy6-9-L2-03"] = Q_23 / 1.8 * 60                        # t = Q : I = 1,625 h = 97,5 min
W_akku = 36 * 14                                          # e-bike battery 36 V, 14 Ah: 504 Wh stored
a["fy6-9-L2-04"] = W_akku / 600 * 100                     # efficiency 504 Wh : 600 Wh = 84 %
U_5 = [4.15, 3.92, 3.80, 3.71, 3.58, 3.12]                # example discharge at 0,50 A, one reading per hour
U_mid = [(u0 + u1) / 2 for u0, u1 in zip(U_5, U_5[1:])]   # linear between readings: 4,035; 3,86; 3,755; 3,645; 3,35 V
a["fy6-9-L2-05"] = 0.50 * 1.0 * sum(U_mid)                # W = I dt sum(U_mid) = 0,50 A · 1,0 h · 18,645 V = 9,32 Wh
a["fy6-9-L2-06"] = (4.2 - 3.7) * 2.0 * 1.5                # lost energy (U_lat - E) I t = 0,5 V · 3,0 Ah = 1,5 Wh (stored E I t = 11,1 Wh)
xs = [13.0, 13.4, 13.8, 14.2, 14.6]                       # example data: U_lat (V) and charging current I (A)
ys = [1.6, 2.4, 3.5, 4.6, 5.5]
mx, my = sum(xs) / len(xs), sum(ys) / len(ys)
k = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs)   # least squares slope = 2,5 A/V
a["fy6-9-L2-07"] = 1 / k                                  # R_kok = 1 : k = 0,40 ohm (the solution reads (13,0 V; 1,5 A), (14,6 V; 5,5 A): same)
# figure fy6-9/ex-current2: 2,0 A for 0-1,0 h, 1,5 A for 1,0-3,0 h, 0,5 A for 3,0-4,0 h; nominal voltage 11,1 V
Q_28 = 2.0 * 1.0 + 1.5 * (3.0 - 1.0) + 0.5 * (4.0 - 3.0)   # 2,0 Ah + 3,0 Ah + 0,5 Ah = 5,5 Ah
a["fy6-9-L2-08"] = 11.1 * Q_28                            # W = U Q = 11,1 V · 5,5 Ah = 61,05 Wh
# Level 3: reasoning, two ideas
W_car = 0.5 * 12 * 60                                     # car battery 12 V, 60 Ah, only half usable: 360 Wh
W_sc = 36 * 7.8                                           # e-scooter battery 36 V, 7,8 Ah: 280,8 Wh
a["fy6-9-L3-01"] = W_car / W_sc                           # 1,28 times (the Ah ratio 7,7 would mislead)
I0 = (13.8 - 12.0) / 0.30                                 # start: 1,8 V : 0,30 ohm = 6,0 A
I1 = (13.8 - 12.6) / 0.30                                 # end:   1,2 V : 0,30 ohm = 4,0 A
a["fy6-9-L3-02"] = (I0 - I1) / I0 * 100                   # the current falls by 33 %
a["fy6-9-L3-03"] = 0.15 * 2.0 ** 2 * 1.5 * 3600 / 1000    # R_s I^2 t = 0,15 ohm · (2,0 A)^2 · 5400 s = 3240 J = 3,24 kJ
# fy6-9-L3-04: example discharge of a lithium cell, charging took 11,0 Wh each time
W_lo = 3.70 * (0.50 * 5.2)                                # 0,50 A for 5,2 h: 2,6 Ah, 9,62 Wh
W_hi = 3.55 * (2.0 * 1.2)                                 # 2,0 A for 1,2 h: 2,4 Ah, 8,52 Wh
a["fy6-9-L3-04"] = W_hi / 11.0 * 100                      # efficiency 8,52 : 11,0 = 77,45 % (R_s = 0,15 V : 1,5 A = 0,10 ohm)
# fy6-9-L3-05: charger 14,0 V, R_kok = 0,40 ohm, 50 Ah, three stages of 20 % = 10 Ah, E at the middle of each stage
E_mid = [(12.00 + 12.20) / 2, (12.20 + 12.40) / 2, (12.40 + 12.60) / 2]
a["fy6-9-L3-05"] = sum(10 / ((14.0 - e) / 0.40) for e in E_mid)   # 2,105 + 2,353 + 2,667 = 7,12 h (constant 5,0 A: 6,0 h)
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
