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
# Exercise bank additions (teacher 2026-11-04): L1-06, L1-07 and L2-06 are multiple choice (no number)
# YO-skill form (teacher 2026-11-05): L1-09 is a true-or-false list (no number); Q = C U = 1,2 mC, W = 1/2 C U^2 = 7,2 mJ
a["fy6-13-L1-08"] = 0.5 * 1000e-6 * (18 ** 2 - 6.0 ** 2) * 1e3   # dW = 1/2 C (U2^2 - U1^2) = 1/2 · 1000 µF · (324 - 36) V^2 = 144 mJ
# L2-05 table: (U in V, Q in µC); line through the origin, slope k = Σ U Q / Σ U^2 = C in µF
uq = [(2.0, 94), (4.0, 189), (6.0, 281), (8.0, 380), (10.0, 471), (12.0, 567)]
c_fit = sum(u * q for u, q in uq) / sum(u * u for u, _ in uq)  # 47,2 µF
a["fy6-13-L2-05"] = 0.5 * c_fit * 1e-6 * 12 ** 2 * 1e3         # W = 1/2 C U^2 = 1/2 · 47,2 µF · (12 V)^2 = 3,40 mJ
a["fy6-13-L2-07"] = 0.5 * 220e-6 * 24 ** 2 * 1e3               # W = 1/2 C U^2 = 1/2 · 220 µF · (24 V)^2 = 63,4 mJ (half of QU = 127 mJ)
# L3-04 table: (t in s, U in V) at I = 15 mA; U = (I / C) t, line through the origin, slope k = Σ t U / Σ t^2
tu = [(0, 0), (2, 203), (4, 396), (6, 607), (8, 805), (10, 992), (12, 1201)]
k_fit = sum(t * u for t, u in tu) / sum(t * t for t, _ in tu)   # 100,01 V/s
c_flash = 15e-3 / k_fit                                         # C = I / k = 150 µF
a["fy6-13-L3-04"] = 0.5 * c_flash * 1800 ** 2 / 5.0e-3 / 1e3    # W = 1/2 C U^2 = 243 J, P = W : t = 243 J : 5,0 ms = 48,6 kW
def flash_w(eps_r, e_max):                                      # L3-05: A = 100 cm², d = 0,050 mm, field at most 1/2 E_max
    d_ = 0.050e-3
    u_max = 0.5 * e_max * d_                                    # teflon 1500 V, glass 350 V
    return 0.5 * (EPS0 * eps_r * 100e-4 / d_) * u_max ** 2      # W = 1/2 C U^2: teflon 4,18 mJ, glass 0,607 mJ
a["fy6-13-L3-05"] = flash_w(2.1, 60e6) / flash_w(5.6, 14e6)     # ratio 6,89
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
