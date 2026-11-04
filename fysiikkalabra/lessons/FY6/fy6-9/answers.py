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
# Level 2: two steps, a conversion or a rearrangement
a["fy6-9-L2-01"] = (14.4 - 12.4) / (0.36 + 40 * 0.001)   # R_s = 40 mohm = 0,040 ohm; I = 2,0 V : 0,40 ohm = 5,0 A
a["fy6-9-L2-02"] = (5.0 - 3.8) / 1.2 - 0.80               # R_s = (U_lat - E) : I - R = 1,0 - 0,80 = 0,20 ohm
Q_23 = (0.80 - 0.15) * 4.5                                # 15 % -> 80 % of 4500 mAh: 0,65 · 4,5 Ah = 2,925 Ah
a["fy6-9-L2-03"] = Q_23 / 1.8 * 60                        # t = Q : I = 1,625 h = 97,5 min
W_akku = 36 * 14                                          # e-bike battery 36 V, 14 Ah: 504 Wh stored
a["fy6-9-L2-04"] = W_akku / 600 * 100                     # efficiency 504 Wh : 600 Wh = 84 %
# Level 3: reasoning, two ideas
W_car = 0.5 * 12 * 60                                     # car battery 12 V, 60 Ah, only half usable: 360 Wh
W_sc = 36 * 7.8                                           # e-scooter battery 36 V, 7,8 Ah: 280,8 Wh
a["fy6-9-L3-01"] = W_car / W_sc                           # 1,28 times (the Ah ratio 7,7 would mislead)
I0 = (13.8 - 12.0) / 0.30                                 # start: 1,8 V : 0,30 ohm = 6,0 A
I1 = (13.8 - 12.6) / 0.30                                 # end:   1,2 V : 0,30 ohm = 4,0 A
a["fy6-9-L3-02"] = (I0 - I1) / I0 * 100                   # the current falls by 33 %
a["fy6-9-L3-03"] = 0.15 * 2.0 ** 2 * 1.5 * 3600 / 1000    # R_s I^2 t = 0,15 ohm · (2,0 A)^2 · 5400 s = 3240 J = 3,24 kJ
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
