"""Every answer in exercises.json for fy7-4, computed from the task data (python -I answers.py).
F = I l B sin α on a straight wire; two parallel wires: B1 = μ0 I1 / (2π r) at the other wire, F = I2 l B1.
Prints {exercise id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json, math

mu0 = 4 * math.pi * 1e-7          # Vs/(Am)
g = 9.81                          # m/s²
a = {}
# Level 1: one formula, values given
a["fy7-4-L1-01"] = 12 * 0.40 * 0.050                                   # F = I l B = 12 A · 0,40 m · 0,050 T = 0,24 N
a["fy7-4-L1-02"] = 8.0 * 0.15 * 0.25 * math.sin(math.radians(40))     # F = I l B sin 40° = 0,3 N · 0,6428 = 0,1928 N -> 0,19 N
a["fy7-4-L1-03"] = 27e-3 / (4.5 * 6.0 * 0.01)                          # B = F / (I l) = 0,027 N / (4,5 A · 0,060 m) = 0,10 T
a["fy7-4-L1-04"] = 200 * 100 * 53e-6 * math.sin(math.radians(74))      # Earth's field 53 µT at 74° (WMM2025) to a magnetic north–south line: 1,0188 N -> 1,0 N
a["fy7-4-L1-05"] = 0.030 / (5.0 * 0.01 * 0.20)                         # I = F / (l B) = 0,030 N / (0,050 m · 0,20 T) = 3,0 A
# Level 2: two steps, one conversion or one rearrangement
B1 = mu0 * 10 / (2 * math.pi * 5.0e-3)                                  # field of wire 1 at wire 2: 4,0 · 10⁻⁴ T
a["fy7-4-L2-01"] = 10 * 0.80 * B1 * 1e3                                 # F = I2 l B1 = 10 A · 0,80 m · 4,0e-4 T = 3,2e-3 N = 3,2 mN
slope = sum(I * dm for I, dm in ((1, 0.27), (2, 0.64), (3, 0.87), (4, 1.24), (5, 1.47))) / 55  # figure points, least-squares line through the origin: 16,47 / 55 = 0,2995 g/A
F_bal = 1.50e-3 * g                                                     # figure fy7-4/balance-points: fitted line through (0; 0) and (5,0 A; 1,50 g) (5 · 0,2995 = 1,497 g): F = Δm g = 0,014715 N
a["fy7-4-L2-02"] = F_bal / (5.0 * 4.0 * 0.01)                           # B = F / (I l) = 0,014715 N / (5,0 A · 0,040 m) = 0,0736 T -> 0,074 T
a["fy7-4-L2-03"] = math.degrees(math.asin(0.50 / (5.0 * 0.50 * 0.40)))  # sin α = F / (I l B) = 0,50 / 1,0 = 0,50 -> α = 30°
F_rail = 15 * 8.0 * 0.01 * 0.30                                         # rod on rails: F = I l B = 15 A · 0,080 m · 0,30 T = 0,36 N
a["fy7-4-L2-04"] = F_rail / (20 * 1e-3)                                 # a = F / m = 0,36 N / 0,020 kg = 18 m/s²
# Level 3: reasoning or an unfamiliar context
a["fy7-4-L3-01"] = 12e-3 * g / (20 * 0.01 * 0.25)                       # threads slack when I l B = m g: I = 0,11772 N / (0,20 m · 0,25 T) = 2,354 A -> 2,4 A
B_bus = mu0 * 20e3 / (2 * math.pi * 0.30)                               # short circuit 20 kA, busbars 0,30 m apart: B = 0,01333 T
a["fy7-4-L3-02"] = -20e3 * 1.0 * B_bus                                  # force on 1,0 m: F = I l B = 266,7 N; opposite currents repel, so by the task's sign rule -> -270 N
B_h = 53e-6 * math.cos(math.radians(74))                                # horizontal component of the Earth's field (WMM2025: 53 µT, 74°): 14,61 µT
a["fy7-4-L3-03"] = 2.7e-3 * g / (1.0 * B_h) / 1e3                       # magnetic east–west wire, I l B_h = m g: I = 0,026487 N / (1,0 m · 14,61e-6 T) = 1813 A -> 1,8 kA
# Exercise-bank additions
a["fy7-4-L1-06"] = None                                                 # multiple choice (direction): no number; I east x B north = up
a["fy7-4-L1-07"] = 0.60 * 4.0 / 8.0                                     # F r is constant: F2 = F1 r1 / r2 = 0,60 N · 4,0 / 8,0 = 0,30 N
a["fy7-4-L1-08"] = 0.050 * math.sin(math.radians(40)) / math.sin(math.radians(20))  # F2 = F1 sin 40° / sin 20° = 0,05 N · 0,6428 / 0,3420 = 0,09397 N -> 0,094 N
Bs = [dm * 1e-3 * g / (2.0 * l * 0.01) for l, dm in ((2.0, 0.35), (3.0, 0.51), (4.0, 0.71), (5.0, 0.86), (6.0, 1.04))]  # B = Δm g / (I l) for each row: 0,0858 ... 0,0850 T
a["fy7-4-L2-05"] = sum(Bs) / len(Bs)                                    # mean: 0,4257 T / 5 = 0,08513 T -> 0,085 T (half range 0,0018 T)
a["fy7-4-L2-06"] = 0.31e-3 * g / (3.0 * 2.5 * 0.01)                     # only l = 2,5 cm is in the field: B = Δm g / (I l) = 3,041e-3 N / 0,075 A m = 0,04055 T -> 0,041 T
k_coil = sum(I * F for I, F in ((0.2, 1.18), (0.4, 2.27), (0.6, 3.52), (0.8, 4.58), (1.0, 5.83))) / sum(I * I for I in (0.2, 0.4, 0.6, 0.8, 1.0))  # least-squares line through the origin: k = B l = 5,795 N/A
a["fy7-4-L2-07"] = k_coil / 1.1                                         # l = k / B = 5,795 / 1,1 = 5,27 m -> 5,3 m
Is = [4.0, 6.0, 8.0, 10.0, 12.0]; acc = [1.8, 3.6, 5.6, 7.3, 9.3]       # rod on rails with friction: a = (l B / m) I − μ g
k_rod = sum((x - 8.0) * (y - sum(acc) / 5) for x, y in zip(Is, acc)) / sum((x - 8.0) ** 2 for x in Is)  # least-squares slope 0,935 (m/s²)/A
a["fy7-4-L3-04"] = k_rod * 45e-3 / (12 * 0.01)                          # B = k m / l = 0,935 · 0,045 kg / 0,12 m = 0,351 T -> 0,35 T (μ = 1,96 / 9,81 = 0,20)
a["fy7-4-L3-05"] = math.sqrt(2 * math.pi * 0.010 * 3.0e-3 * g / (mu0 * 0.50))  # levitating wire, opposite currents: mu0 I² l / (2π r) = m g -> I = 54,25 A -> 54 A
print(json.dumps({k: round(v, 6) for k, v in a.items() if v is not None}))
