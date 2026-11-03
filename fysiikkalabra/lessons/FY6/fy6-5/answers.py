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
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
