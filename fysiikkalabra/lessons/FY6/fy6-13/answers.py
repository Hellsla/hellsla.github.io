"""Every answer in exercises.json for fy6-13, computed from the task data (python -I answers.py).
Capacitance C = Q / U (1 F = 1 C/V); plate capacitor C = eps0 eps_r A / d with eps0 = 8,854 · 10^-12 F/m; the
uniform field E = U / d, so the largest voltage before breakdown is U_max = E_max d; stored energy
W = 1/2 Q U = 1/2 C U^2. A capacitor disconnected from its source keeps its charge Q.
Prints {exercise id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json

EPS0 = 8.854e-12
a = {}
# Level 1: one formula, values given
a["fy6-13-L1-01"] = 4.8e-6 / 12 * 1e6                      # C = Q : U = 4,8 µC : 12 V = 0,40 µF
a["fy6-13-L1-02"] = 470e-6 * 9.0 * 1e3                     # Q = C U = 470 µF · 9,0 V = 4,23 mC
a["fy6-13-L1-03"] = 0.5 * 2200e-6 * 16 ** 2                # W = 1/2 C U^2 = 1/2 · 2200 µF · (16 V)^2 = 0,2816 J
a["fy6-13-L1-04"] = EPS0 * 1.0 * 0.025 / 1.0e-3 * 1e12     # C = eps0 A : d = 221 pF (air, eps_r = 1,0)
# figure fy6-13/ex-qu: U grows linearly with Q, (60 µC, 12 V) on the gridlines; W is the triangle's area
a["fy6-13-L1-05"] = 0.5 * 60e-6 * 12 * 1e6                 # W = 1/2 Q U = 1/2 · 60 µC · 12 V = 360 µJ
# Level 2: two steps, a conversion or a rearrangement
a["fy6-13-L2-01"] = 16e6 * 0.020e-3                        # U_max = E_max d = 16 MV/m · 0,020 mm = 320 V
a["fy6-13-L2-02"] = 3.3e-9 * 0.10e-3 / (EPS0 * 100e-4)     # eps_r = C d : (eps0 A) = 3,73 (paper)
a["fy6-13-L2-03"] = 2 * 200 / 2.0e3 ** 2 * 1e6             # C = 2 W : U^2 = 400 J : (2000 V)^2 = 100 µF
W_sc = 0.5 * 10 * 2.7 ** 2                                 # supercapacitor 10 F at 2,7 V: 36,45 J
a["fy6-13-L2-04"] = W_sc / 0.50                            # t = W : P = 72,9 s
# Level 3: reasoning, two ideas
Q = 120e-12 * 500                                          # disconnected: Q = C U = 60 nC stays
W1 = 0.5 * Q * 500                                         # 15 µJ
W2 = 0.5 * Q * (Q / (120e-12 / 2))                         # d doubled: C halves, U = 1000 V, W = 30 µJ
a["fy6-13-L3-01"] = (W2 - W1) * 1e6                        # the energy grows by 15 µJ (the work of pulling)
a["fy6-13-L3-02"] = (5.6 - 1.0) * 220e-12 * 1.5e3 * 1e6    # connected, glass in: dQ = (eps_r - 1) C U = 1,518 µC
d = 2 * 6.0e3 / 24e6                                       # only half of 24 MV/m used: d = 6,0 kV : 12 MV/m = 0,50 mm
a["fy6-13-L3-03"] = 1.0e-9 * d / (EPS0 * 2.6) * 1e4        # A = C d : (eps0 eps_r) = 217 cm^2
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
