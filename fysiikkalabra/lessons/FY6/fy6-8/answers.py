"""Every answer in exercises.json for fy6-8, computed from the task data (python -I answers.py).
Model of a battery: an ideal source E in series with the internal resistance R_s. Terminal voltage U = E - R_s I;
with a load R the voltage law gives E - R_s I - R I = 0, so I = E / (R + R_s); short circuit (R = 0): I_k = E / R_s.
Cells in series: the source voltages and the internal resistances add; n identical cells in parallel: E, R_s / n.
Prints {exercise id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json

a = {}
# Level 1: one relation, values given
a["fy6-8-L1-01"] = 1.58 - 0.25 * 0.80                     # U = E - R_s I = 1,58 V - 0,20 V = 1,38 V
a["fy6-8-L1-02"] = 1.30 / 0.040                           # NiMH cell short circuit: I_k = E / R_s = 32,5 A (33 A)
a["fy6-8-L1-03"] = 4 * 1.55                               # four cells in series: E = 4 · 1,55 V = 6,20 V
a["fy6-8-L1-04"] = 0.45 / 3                               # three identical cells in parallel: R_s / 3 = 0,15 ohm
# figure fy6-8/ex-graph: the line from (0 A; 4,5 V) to (3,0 A; 0 V): the short-circuit current is read at U = 0
a["fy6-8-L1-05"] = 4.5 / 1.5
# Level 2: two steps
a["fy6-8-L2-01"] = (4.30 - 3.70) / (0.80 - 0.20)          # two readings: R_s = (U1 - U2) / (I2 - I1) = 1,0 ohm
I = 6.0 / (5.5 + 0.50)                                    # I = E / (R + R_s) = 1,0 A
a["fy6-8-L2-02"] = 5.5 * I                                # terminal voltage U = R I = 5,5 V (= E - R_s I)
I = 4.5 / (3.0 + 1.5)                                     # lamp 3,0 ohm on 4,5 V, 1,5 ohm: I = 1,0 A
a["fy6-8-L2-03"] = (4.5 - 1.5 * I) * I                    # P = U I = 3,0 V · 1,0 A = 3,0 W
a["fy6-8-L2-04"] = 2 * 1.5 / (2.4 + 2 * 0.30)             # two cells in series on 2,4 ohm: 3,0 V : 3,0 ohm = 1,0 A
# Level 3: reasoning
I_par = 1.5 / (0.80 + 0.40 / 2)                           # two cells in parallel on 0,80 ohm: 1,5 V : 1,0 ohm = 1,5 A
a["fy6-8-L3-01"] = I_par / 2                              # each identical cell gives half: 0,75 A
a["fy6-8-L3-02"] = (1.5 + 1.5 - 1.5) / (4.0 + 3 * 0.25)   # one cell reversed: E = 1,5 V, R_s = 0,75 ohm: 0,3158 A
I1, I2 = 1.20 / 2.0, 1.44 / 6.0                           # load 2,0 ohm: 0,60 A; 6,0 ohm: 0,24 A
Rs = (1.44 - 1.20) / (I1 - I2)                            # R_s = 0,24 V : 0,36 A = 0,667 ohm
a["fy6-8-L3-03"] = 1.20 + Rs * I1                         # E = U1 + R_s I1 = 1,60 V
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
