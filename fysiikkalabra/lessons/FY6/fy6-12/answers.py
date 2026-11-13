"""Every answer in exercises.json for fy6-12, computed from the task data (python -I answers.py).
Homogeneous field between plates: E = U / d, potential V = E x from the negative plate; E_p = q V; the field's work
W_AB = q (V_A - V_B); with only the electric force working E_k + E_p is constant, so from rest E_k = |q| U.
1 eV = 1,602e-19 J. Constants as the tasks give them: e = 1,602e-19 C, m_p = 1,673e-27 kg, m_e = 9,109e-31 kg,
m_alpha = 6,645e-27 kg. Gravity is negligible. Prints {exercise id: number} as JSON on the last line."""
import json, math

e, m_p, m_e, m_a = 1.602e-19, 1.673e-27, 9.109e-31, 6.645e-27
a = {}
# Level 1: one formula, values given
a["fy6-12-L1-01"] = e * 240                                   # proton through 240 V: W = e U = 3,845e-17 J
a["fy6-12-L1-02"] = 3.0e-9 * 120 * 1e6                        # E_p = q V = 3,0 nC · 120 V = 3,6e-7 J = 0,36 µJ
a["fy6-12-L1-03"] = 5.0e3 * e                                 # 5,0 keV = 5000 · 1,602e-19 J = 8,01e-16 J
a["fy6-12-L1-04"] = 4.0e-6 * (60 - 15) * 1e3                  # W = q (V_A - V_B) = 4,0 µC · 45 V = 0,18 mJ
# figure fy6-12/ex-vgraph: V(x) from 0 V at x = 0 to 250 V at x = 5,0 cm; V(4,0 cm) = 200 V, V(1,0 cm) = 50 V
a["fy6-12-L1-05"] = 200 - 50                                  # proton 4,0 cm -> 1,0 cm: E_k grows e · 150 V = 150 eV
# Level 2: two steps or a conversion
a["fy6-12-L2-01"] = -(2.5e3 * 0.030)                          # along the field 3,0 cm in 2,5 kV/m: V falls 75 V; proton dE_p = -75 eV
a["fy6-12-L2-02"] = -(300 * 0.80 / 2.0)                       # V_P = U x / d = 300 V · 0,80/2,0 = 120 V; electron E_p = -120 eV
a["fy6-12-L2-03"] = math.sqrt(2 * 2 * e * 2.0e3 / m_a)        # alpha (q = 2e) from rest through 2,0 kV: v = 4,39e5 m/s
a["fy6-12-L2-04"] = m_e * (1.0e7) ** 2 / (2 * e)              # U = m v^2 / (2 e) = 284 V
# Level 3: reasoning
Ek_A = 0.5 * m_e * (2.0e6) ** 2                               # electron at A: 1,822e-18 J
Ek_B = Ek_A + e * (160 - 40)                                  # E_p falls by e (V_B - V_A) = 1,922e-17 J, E_k grows as much
a["fy6-12-L3-01"] = math.sqrt(2 * Ek_B / m_e)                 # 6,80e6 m/s
a["fy6-12-L3-02"] = math.sqrt(m_p / m_e)                      # same e U: v_e / v_p = sqrt(m_p / m_e) = 42,9
Ek0 = 0.5 * m_p * (3.0e5) ** 2                                # proton from the - plate: 7,529e-17 J = 470 eV
climb = Ek0 / e                                               # it can climb 470 V of potential
x_stop = climb / 600 * 2.0                                    # V = U x / d: x = 1,566 cm from the - plate
a["fy6-12-L3-03"] = (2.0 - x_stop) * 10                       # distance from the + plate: 4,34 mm
# Exercise bank additions (L1-06, L1-07, L2-06 are multiple choice: no number)
a["fy6-12-L1-08"] = 2 * 450                                   # E_k = q U = 2e · 450 V = 900 eV
# L2-05: V(x) table (x in cm, V in V); E = slope of the least-squares line through the origin, U = E d
x5, V5 = [1.0, 2.0, 3.0, 4.0, 5.0], [5.2, 9.7, 15.4, 19.6, 25.3]
E5 = sum(x * v for x, v in zip(x5, V5)) / sum(x * x for x in x5) * 100   # least squares through origin: 501,3 V/m
a["fy6-12-L2-05"] = E5 * 0.060                                # U = E d = 30,1 V
# L2-07: m = 2 e U / v^2 per row, then the mean; v in 1e4 m/s
U7, v7 = [100, 200, 300, 400, 500], [6.88e4, 9.95e4, 12.0e4, 13.9e4, 15.4e4]
a["fy6-12-L2-07"] = sum(2 * e * u / v ** 2 for u, v in zip(U7, v7)) / len(U7)   # 6,66e-27 kg (helium ion)
# L2-08 is a find-the-error choice (no number): row 3 uses V_B = 120 V for U; right U = 120 - 30 = 90 V, E_k = 90 eV = 1,442e-17 J
# L3-04: v = sqrt(2 e U_k / m); t = L / v; a = e U_p / (m d); y = a t^2 / 2 (= U_p L^2 / (4 d U_k))
v34 = math.sqrt(2 * e * 1800 / m_e)                           # 2,516e7 m/s
t34 = 0.050 / v34                                             # 1,987e-9 s
acc34 = e * 120 / (m_e * 0.015)                               # 1,407e15 m/s^2
a["fy6-12-L3-04"] = 0.5 * acc34 * t34 ** 2 * 1000             # 2,78 mm (< d/2 = 7,5 mm); gravity: F_e / (m g) = 1,4e14
# L3-05: share of electrons with E_k in each 20 eV bin from the retarding-voltage table, mean by bin midpoints
frac = [100, 98, 71, 22, 3, 0]                                # % passing at U_v = 0, 20, ..., 100 V
Ek5 = sum((frac[i] - frac[i + 1]) / 100 * (20 * i + 10) for i in range(5))   # 48,8 eV
a["fy6-12-L3-05"] = math.sqrt(2 * Ek5 * e / m_e)              # 4,14e6 m/s
# L2-09 (figure fy6-12/ex-vgraph): electron from rest at x = 1,0 cm (50 V) to the + plate (250 V): U = 200 V, v = sqrt(2 e U / m)
a["fy6-12-L2-09"] = math.sqrt(2 * e * (250 - 50) / m_e)      # 8,387e6 m/s
print(json.dumps({k: float(f"{v:.6g}") for k, v in a.items()}))
