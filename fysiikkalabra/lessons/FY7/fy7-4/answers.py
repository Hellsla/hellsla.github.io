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
a["fy7-4-L1-04"] = 200 * 100 * 52e-6 * math.sin(math.radians(75))      # Earth's field 52 µT at 75° to a north–south line: 1,0046 N -> 1,0 N
a["fy7-4-L1-05"] = 0.030 / (5.0 * 0.01 * 0.20)                         # I = F / (l B) = 0,030 N / (0,050 m · 0,20 T) = 3,0 A
# Level 2: two steps, one conversion or one rearrangement
B1 = mu0 * 10 / (2 * math.pi * 5.0e-3)                                  # field of wire 1 at wire 2: 4,0 · 10⁻⁴ T
a["fy7-4-L2-01"] = 10 * 0.80 * B1 * 1e3                                 # F = I2 l B1 = 10 A · 0,80 m · 4,0e-4 T = 3,2e-3 N = 3,2 mN
F_bal = 1.50e-3 * g                                                     # figure fy7-4/balance-points: line through (0; 0) and (5,0 A; 1,50 g): F = Δm g = 0,014715 N
a["fy7-4-L2-02"] = F_bal / (5.0 * 4.0 * 0.01)                           # B = F / (I l) = 0,014715 N / (5,0 A · 0,040 m) = 0,0736 T -> 0,074 T
a["fy7-4-L2-03"] = math.degrees(math.asin(0.50 / (5.0 * 0.50 * 0.40)))  # sin α = F / (I l B) = 0,50 / 1,0 = 0,50 -> α = 30°
F_rail = 15 * 8.0 * 0.01 * 0.30                                         # rod on rails: F = I l B = 15 A · 0,080 m · 0,30 T = 0,36 N
a["fy7-4-L2-04"] = F_rail / (20 * 1e-3)                                 # a = F / m = 0,36 N / 0,020 kg = 18 m/s²
# Level 3: reasoning or an unfamiliar context
a["fy7-4-L3-01"] = 12e-3 * g / (20 * 0.01 * 0.25)                       # threads slack when I l B = m g: I = 0,11772 N / (0,20 m · 0,25 T) = 2,354 A -> 2,4 A
B_bus = mu0 * 20e3 / (2 * math.pi * 0.30)                               # short circuit 20 kA, busbars 0,30 m apart: B = 0,01333 T
a["fy7-4-L3-02"] = 20e3 * 1.0 * B_bus                                   # force on 1,0 m: F = I l B = 266,7 N -> 270 N (repulsive, opposite currents)
B_h = 52e-6 * math.cos(math.radians(75))                                # horizontal component of the Earth's field: 13,46 µT
a["fy7-4-L3-03"] = 2.7e-3 * g / (1.0 * B_h) / 1e3                       # east–west wire, I l B_h = m g: I = 0,026487 N / (1,0 m · 13,46e-6 T) = 1968 A -> 2,0 kA
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
