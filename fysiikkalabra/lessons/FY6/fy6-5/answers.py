"""Every answer in exercises.json for fy6-5, computed from the task data (python -I answers.py).
Ideal sources and wires, resistors of constant resistance. Current law: currents in = currents out at a junction.
Voltage law: the source voltage equals the voltages of the resistors along a loop. U = R I; U_AB = V_A - V_B.
Prints {exercise id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json

par = lambda x, y: 1 / (1 / x + 1 / y)
a = {}
# Level 1: one law, values given
a["fy6-5-L1-01"] = 2.4 + 0.6 - 1.8                        # junction: in 2,4 A + 0,6 A, out 1,8 A + I -> I = 1,2 A
a["fy6-5-L1-02"] = 12.0 - 4.5                             # series loop: U = U1 + U2 -> U2 = 12,0 V - 4,5 V = 7,5 V
a["fy6-5-L1-03"] = 5.0 - (-3.0)                           # U_AB = V_A - V_B = 5,0 V - (-3,0 V) = 8,0 V
a["fy6-5-L1-04"] = 40 * 0.15                              # potential drop over a resistor: R I = 40 ohm · 0,15 A = 6,0 V
# figure fy6-5/ex-graph: V(A) = 9,0 V, V(B) = 7,0 V, V(C) = 3,0 V, V(D) = 0 V; the middle resistor (B..C) 4,0 V
a["fy6-5-L1-05"] = 7.0 - 3.0
# Level 2: two steps
a["fy6-5-L2-01"] = 9.0 - 220 * 0.025                      # V_B = V_A - R I = 9,0 V - 5,5 V = 3,5 V
I_s = 12.0 / (200 + 400)                                  # series 12,0 V over 200 + 400 ohm: I = 0,020 A
a["fy6-5-L2-02"] = 400 * I_s                              # potential between the resistors (minus pole 0 V): R2 I = 8,0 V
# figure fy6-5/ex-branch: 6,0 V source, 20 ohm and 30 ohm in parallel: I = 0,30 A + 0,20 A = 0,50 A
a["fy6-5-L2-03"] = 6.0 / 20 + 6.0 / 30
U1 = 120 * 0.050                                          # 120 ohm at 50 mA: 6,0 V
a["fy6-5-L2-04"] = (9.0 - U1) / 0.050                     # R2 = (9,0 V - 6,0 V) : 0,050 A = 60 ohm
# Level 3: reasoning
I_3 = 12.0 / (30 + 50 + 40)                               # series 30 + 50 + 40 ohm on 12 V: 0,10 A
a["fy6-5-L3-01"] = -(50 + 40) * I_3                       # reference between R1 and R2: minus pole at -(U2 + U3) = -9,0 V
# figure fy6-5/ex-branch2: 12 V, R1 = 40 ohm, R2 = 60 ohm || R3; I1 = 0,20 A
U23 = 12.0 - 40 * 0.20                                    # 12 V - 8,0 V = 4,0 V over the branches
a["fy6-5-L3-02"] = U23 / (0.20 - U23 / 60)                # I3 = 0,20 A - 4,0 V : 60 ohm = 0,1333 A; R3 = 30 ohm
V_both = 12.0 * par(60, 60) / (20 + par(60, 60))          # both lamps: junction at 12 V · 30/50 = 7,2 V
V_one = 12.0 * 60 / (20 + 60)                             # one lamp: 12 V · 60/80 = 9,0 V
a["fy6-5-L3-03"] = V_one - V_both                         # the junction's potential rises by 1,8 V
# Exercise bank additions (teacher 2026-11-04): L1-06 and L1-07 are multiple choice (no number)
a["fy6-5-L1-08"] = 9.0 - 60 * 0.040 - 90 * 0.040          # V_C = V_A - R1 I - R2 I = 9,0 V - 2,4 V - 3,6 V = 3,0 V
a["fy6-5-L2-05"] = 12.0 / 60 + 12.0 / 80 + 12.0 / 50      # data: branch readings agree with U / R; main wire I_0 = 0,20 + 0,15 + 0,24 = 0,59 A (reading 0,50 A is wrong)
a["fy6-5-L2-06"] = (8.4 - 3.6) / 0.12                     # data: R2 between C (8,4 V) and D (3,6 V): 4,8 V : 0,12 A = 40 ohm
a["fy6-5-L2-07"] = 0 - 100 * (9.0 / (100 + 200))          # error analysis: zero at the plus pole, V = -R1 I = -3,0 V
# L3-04: two sources, three parallel branches; I1 + I3 = I2, U1 - R1 I1 - R2 I2 = 0, U2 - R3 I3 - R2 I2 = 0
I2 = (12.0 / 30 + 9.0 / 30) / (1 + 20 / 30 + 20 / 30)    # I2 (1 + R2/R1 + R2/R3) = U1/R1 + U2/R3 -> 0,30 A
I1 = (12.0 - 20 * I2) / 30                                # 0,20 A
I3 = (9.0 - 20 * I2) / 30                                 # 0,10 A
assert abs(12.0 * I1 + 9.0 * I3 - (30 * I1**2 + 20 * I2**2 + 30 * I3**2)) < 1e-9   # energy balance 3,3 W
a["fy6-5-L3-04"] = I2
# L3-05: voltage divider 12 V, R1 = R2 = 100 ohm, load Rk in parallel with R2; V_P = 5,0 V
Rp = 100 * 5.0 / (12.0 - 5.0)                             # R_p = R1 V / (U - V) = 71,4 ohm
a["fy6-5-L3-05"] = 1 / (1 / Rp - 1 / 100)                 # 1/Rk = 1/Rp - 1/R2 -> 250 ohm
# L2-08 is multiple choice with a reason: R1 20, R2 30, R3 60 ohm in parallel, I = 0,30 A; R_k = 10 ohm, U = 3,0 V, I3 = 0,050 A; no number
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
