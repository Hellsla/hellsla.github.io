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
# Exercise bank additions (teacher 2026-11-04): L1-06, L1-07 and L2-07 are multiple choice (no number)


def fit(pts):
    """Least-squares line y = k x + b through the points (a student's by-eye line lands within the tolerance)."""
    n = len(pts)
    xm, ym = sum(x for x, _ in pts) / n, sum(y for _, y in pts) / n
    k = sum((x - xm) * (y - ym) for x, y in pts) / sum((x - xm) ** 2 for x, _ in pts)
    return k, ym - k * xm


a["fy6-8-L1-08"] = (1.50 - 1.31) / 0.50                   # R_s = (E - U) / I = 0,19 V : 0,50 A = 0,38 ohm
d5 = [(0.20, 1.43), (0.40, 1.31), (0.60, 1.20), (0.80, 1.10), (1.00, 0.99), (1.20, 0.86)]   # data of L2-05
k5, b5 = fit(d5)                                          # slope -0,559 ohm, intercept E = 1,54 V
a["fy6-8-L2-05"] = round(-k5, 2)                          # R_s = 0,56 ohm (tolerance 0,05: 0,53…0,59)
IA = [0.10, 0.20, 0.40, 0.60, 0.80, 1.00]                 # data of L2-06
kA, bA = fit(list(zip(IA, [1.55, 1.50, 1.40, 1.29, 1.21, 1.10])))   # A: E 1,60 V, R_s 0,50 ohm
kB, bB = fit(list(zip(IA, [1.47, 1.44, 1.40, 1.35, 1.31, 1.27])))   # B: E 1,49 V, R_s 0,22 ohm
a["fy6-8-L2-06"] = round((bA - bB) / (kB - kA), 2)        # lines cross at I = (E_A - E_B) / (R_A - R_B) = 0,40 A
I3 = [0.10, 0.20, 0.30, 0.40, 0.50]                       # data of L3-04
kN, bN = fit(list(zip(I3, [1.56, 1.53, 1.51, 1.48, 1.46])))   # new: E 1,58 V, R_s 0,25 ohm
kO, bO = fit(list(zip(I3, [1.41, 1.30, 1.19, 1.09, 0.97])))   # aged: E 1,52 V, R_s 1,09 ohm
Rold = -kO
a["fy6-8-L3-04"] = round(100 * Rold / (2.0 + Rold))       # share heating the cell: R_s / (R + R_s) = 35 % (new cell 11 %)
# part c (aged cell, P(R) = E² R / (R + R_s)²): 0,47 W, 0,53 W, 0,47 W, 0,34 W at 0,55; 1,1; 2,2; 4,4 ohm -> largest at R ≈ R_s, where 50 % heats the cell
d6 = [(0.50, 5.56), (1.00, 5.00), (1.50, 4.45), (2.00, 3.91), (2.50, 3.36), (3.00, 2.79)]   # data of L3-05
k6, b6 = fit(d6)                                          # slope -1,103 ohm (leads included), E = 6,11 V
a["fy6-8-L3-05"] = round(b6 / (-k6 - 0.30), 1)            # true R_s = 1,10 - 0,30 = 0,80 ohm: I_k = 6,11 V : 0,80 ohm = 7,6 A (the pupil's 5,6 A)
# L2-08 is multiple choice (data): U at I = 0,10...0,90 A: 1,51/1,43/1,36/1,27/1,19 V; slope (1,51 - 1,19)/0,80 = 0,40 ohm, E = 1,51 + 0,04 = 1,55 V (least squares 1,552 V, 0,400 ohm); no number
a["fy6-8-L2-09"] = (11 - 7) / (250 - 50)                    # figure fy6-8/ex-graph-car: R_s = (U1 - U2) / (I2 - I1) = 4 V : 200 A = 0,020 ohm
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
