"""Every answer in exercises.json for fy6-10, computed from the task data (python -I answers.py).
Charge as a whole number of elementary charges, Q = n e (e = 1,602 · 10^-19 C); current I = Q / t; conservation of
charge (identical metal spheres that touch share their total charge equally); Coulomb's law between point charges
F = k |q1 q2| / r^2, k = 8,988 · 10^9 N m^2 / C^2; forces on one charge add as vectors.
Prints {exercise id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json
import math

K, E, G, ME, MP, g = 8.988e9, 1.602e-19, 6.674e-11, 9.109e-31, 1.673e-27, 9.81
nC, uC, cm = 1e-9, 1e-6, 1e-2


def F(q1, q2, r):
    return K * abs(q1 * q2) / r ** 2


a = {}
# Level 1: one formula, values given
a["fy6-10-L1-01"] = 6.4 * nC / E                          # n = Q : e = 6,4 · 10^-9 C : 1,602 · 10^-19 C = 4,0 · 10^10
a["fy6-10-L1-02"] = F(15 * nC, 25 * nC, 4.0 * cm) * 1000  # 8,988e9 · 375e-18 C^2 : 0,0016 m^2 = 2,11 mN
a["fy6-10-L1-03"] = 5.0 / 0.20e-3 / 1000                  # I = Q : t = 5,0 C : 0,20 ms = 25 kA
a["fy6-10-L1-04"] = (12 + (-4.0)) / 2                     # touching identical spheres: (12 nC - 4,0 nC) : 2 = 4,0 nC each
a["fy6-10-L1-05"] = F(2.0 * uC, 4.0 * uC, 0.50)           # 8,988e9 · 8,0e-12 C^2 : 0,25 m^2 = 0,288 N
# Level 2: two steps, a conversion or a rearrangement
a["fy6-10-L2-01"] = (K * (30 * nC) ** 2 / 2.0e-3) ** 0.5 / cm   # r = sqrt(k q1 q2 / F) = 6,36 cm
a["fy6-10-L2-02"] = 3.6 * (4.0 / 10) ** 2                 # F2 = F1 (r1 / r2)^2 = 3,6 mN · 0,16 = 0,576 mN
q_23 = (18 + (-6.0)) / 2 * nC                             # after touching: +6,0 nC each
a["fy6-10-L2-03"] = F(q_23, q_23, 4.0 * cm) * 1000        # 8,988e9 · 36e-18 C^2 : 0,0016 m^2 = 0,202 mN
W_24 = 0.50e-3 * g                                        # the weight of 0,50 g: 4,905 mN
a["fy6-10-L2-04"] = 5.0 * cm * (W_24 / K) ** 0.5 / nC     # q = r sqrt(F / k) = 36,9 nC
# Level 3: reasoning, two ideas
F31 = F(20 * nC, 5.0 * nC, 5.0 * cm)                      # q1 = +20 nC pushes q3 = +5,0 nC towards q2: 0,360 mN
F32 = F(20 * nC, 5.0 * nC, 5.0 * cm)                      # q2 = -20 nC pulls q3 towards itself: the same direction
a["fy6-10-L3-01"] = (F31 + F32) * 1000                    # 0,719 mN towards q2
a["fy6-10-L3-02"] = K * E ** 2 / (G * ME * MP)            # F_e : F_g in hydrogen, r cancels: 2,27 · 10^39
# q1 = +4,0 nC at x = 0, q2 = +1,0 nC at x = 12 cm: k q1 / x^2 = k q2 / (12 cm - x)^2, so x / (12 cm - x) = sqrt(4) = 2
a["fy6-10-L3-03"] = 12 * 2 / (1 + 2)                      # x = 8,0 cm from q1
# Level 1 additions
a["fy6-10-L1-08"] = 0.50 * 3.0 * 60                       # Q = I t = 0,50 A · 180 s = 90 C
# Level 2 additions
r_25 = [2.0, 3.0, 4.0, 5.0, 6.0, 8.0]                     # torsion balance: r in cm
F_25 = [13.6, 6.4, 3.4, 2.3, 1.52, 0.91]                  # F in mN
x_25 = [1 / (r * cm) ** 2 for r in r_25]                  # 1 : r^2 in 1/m^2
y_25 = [f * 1e-3 for f in F_25]                           # F in N
s_25 = sum(x * y for x, y in zip(x_25, y_25)) / sum(x * x for x in x_25)   # least squares through the origin: slope = k q^2 = 5,50e-6 N m^2
a["fy6-10-L2-05"] = (s_25 / K) ** 0.5 / nC               # q = sqrt(slope / k) = 24,7 nC
FA_26 = [9.1, 3.9, 2.3, 1.0, 0.55]                        # pair A, both 20 nC (mN)
FB_26 = [31.0, 14.4, 7.6, 3.5, 1.95]                      # pair B, 20 nC and q_B (mN)
ratios = [b / x for b, x in zip(FB_26, FA_26)]            # F_B : F_A = q_B : 20 nC at every distance
a["fy6-10-L2-06"] = 20 * sum(ratios) / len(ratios)        # sum 17,45, mean 3,49, q_B = 69,8 nC
a["fy6-10-L2-07"] = F(8.0 * nC, 12 * nC, 3.0 * cm) * 1000   # 8,988e9 · 96e-18 C^2 : 9,0e-4 m^2 = 0,9587 mN (the student divided by r)
# Level 3 additions
s_34 = (6.0 / 2.5) ** 0.5                                 # x / (x - d) = sqrt(|q1| / |q2|) = 1,549 (zero point beyond q2)
a["fy6-10-L3-04"] = 12 * s_34 / (s_34 - 1)                # x = d s / (s - 1) = 33,85 cm from q1
th = math.radians(10)
F_35 = 0.80e-3 * g * math.tan(th)                         # tension balance: F = m g tan(theta) = 1,384 mN
r_35 = 2 * 0.30 * math.sin(th)                            # separation r = 2 L sin(theta) = 0,1042 m
a["fy6-10-L3-05"] = r_35 * (F_35 / K) ** 0.5 / nC         # q = r sqrt(F / k) = 40,9 nC
print(json.dumps({k: float(f"{v:.6g}") for k, v in a.items()}))
