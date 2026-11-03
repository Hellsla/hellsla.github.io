"""Every answer in exercises.json for fy6-1, computed from the task data (python -I answers.py).
Current I = Q / t, voltage U = E / Q (E the energy transferred to the charge Q), Q = N e with e = 1,602 · 10^-19 C.
Prints {id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json

e = 1.602e-19                                       # C, the elementary charge
a = {}
# Level 1: one formula
a["fy6-1-L1-01"] = 45 / 30                          # I = Q / t = 45 C : 30 s = 1,5 A
a["fy6-1-L1-02"] = 0.50 * 40                        # Q = I t = 0,50 A · 40 s = 20 C
a["fy6-1-L1-03"] = 54 / 6.0                         # U = E / Q = 54 J : 6,0 C = 9,0 V
a["fy6-1-L1-04"] = 12 * 150                         # E = U Q = 12 V · 150 C = 1800 J
a["fy6-1-L1-05"] = 2.4 / 0.080                      # t = Q / I = 2,4 C : 0,080 A = 30 s
# Level 2: a conversion, two steps or a graph
a["fy6-1-L2-01"] = 0.020 * (1.5 * 3600)             # 20 mA = 0,020 A, 1,5 h = 5400 s: Q = 108 C
a["fy6-1-L2-02"] = 0.16 * 1.0 / e                   # Q = I t = 0,16 C, N = Q / e = 9,99 · 10^17
a["fy6-1-L2-03"] = 3.7 * (3.000 * 3600) / 1000      # 3000 mAh = 3,000 A · 3600 s = 10 800 C; E = U Q = 39 960 J ≈ 40 kJ
a["fy6-1-L2-04"] = 0.40 * 20 + 0.10 * 30            # (t, I) graph: area 0,40 A · 20 s + 0,10 A · 30 s = 11 C
# Level 3: two ideas, reasoning
a["fy6-1-L3-01"] = (2.0 * 3600) / 0.25 / 3600       # 2,0 Ah = 7200 C; t = Q / I = 28 800 s = 8,0 h
a["fy6-1-L3-02"] = (9.0 * 0.50 * 3600) / (1.5 * 2.5 * 3600)   # E = U Q: 16 200 J and 13 500 J; ratio 1,2
# L3-03 (words, a drawing task): two cells in series, a switch, a lamp and an ammeter in one loop; model figure kaavio-malli
print(json.dumps(a))
