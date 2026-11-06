"""Every answer in exercises.json for fy6-11, computed from the task data (python -I answers.py).
Field strength E = F / q, force F = q E; between parallel plates (a uniform field) E = U / d. A charged particle in a
uniform field has the constant acceleration a = q E / m (Newton's second law); from rest over the distance d,
v^2 = 2 a d. Prints {exercise id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json
import math

e, me, g = 1.602e-19, 9.109e-31, 9.81
a = {}
# Level 1: one relation, values given
a["fy6-11-L1-01"] = 1.2e-4 / 3.0e-9                       # E = F / q = 4,0e4 N/C
a["fy6-11-L1-02"] = 5.0e-9 * 2.0e4 * 1e6                  # F = q E = 1,0e-4 N = 100 µN
a["fy6-11-L1-03"] = 600 / 0.040                           # E = U / d = 1,5e4 V/m
a["fy6-11-L1-04"] = 1.0e7 * 7.0e-9 * 1000                 # cell membrane U = E d = 0,070 V = 70 mV
# figure fy6-11/fq-graph: the fitted line through the origin reaches (4,5 nC; 135 µN): E = 135 µN : 4,5 nC
pts = [(1.0, 31.0), (2.0, 59.0), (3.0, 91.0), (4.0, 119.0)]
fit = sum(q * F for q, F in pts) / sum(q * q for q, _ in pts)   # 29,9 µN/nC, the drawn line has 30 µN/nC
a["fy6-11-L1-05"] = 135e-6 / 4.5e-9                       # 3,0e4 N/C
# Level 2: two steps, conversions, rearranging
a["fy6-11-L2-01"] = 4.0e-9 * 4.5e3 / 9.0e-3 * 1000        # E = 5,0e5 V/m, F = 2,0e-3 N = 2,0 mN
a["fy6-11-L2-02"] = 2.4e-3 * 0.050 / 8.0e-9 / 1000        # U = E d = F d / q = 15 kV
F = 1.6e-17 * 3.0e3 / 6.0e-3                              # dust: F = q U / d = 8,0e-12 N
a["fy6-11-L2-03"] = F / (4.0e-14 * g)                     # F : G = 20,4
a["fy6-11-L2-04"] = 0.15 * 6.0 / 2.0                      # E = U / d triples: 0,15 mN -> 0,45 mN
# Level 3: reasoning
a["fy6-11-L3-01"] = 450 * 3 / 4                           # q E = m g with E = U / d: U ~ 1 / q, 3e -> 4e: 337,5 V
acc = e * 50 / (me * 0.010)                               # electron: a = e U / (m d) = 8,79e14 m/s^2
a["fy6-11-L3-02"] = math.sqrt(2 * acc * 0.010) / 1000     # v = sqrt(2 a d) = 4,19e6 m/s = 4190 km/s
a["fy6-11-L3-03"] = 2.0e-3 * g * math.tan(math.radians(10)) / 1.5e5 * 1e9   # q = m g tan(alpha) / E = 23,1 nC
# Exercise bank additions (teacher 2026-11-04): L1-06 and L1-07 are multiple choice (no number)
a["fy6-11-L1-08"] = 3.0e3 / 4.0e5 * 1000                  # d = U / E = 7,5e-3 m = 7,5 mm
dq = [2.0, 3.0, 4.0, 5.0, 6.0, 8.0]                       # L2-05: d in cm, F in µN, q = 5,0 nC
fq = [102, 65.5, 51.0, 39.0, 34.0, 24.6]
prod = [f * 1e-6 / 5.0e-9 * x / 100 for f, x in zip(fq, dq)]   # E d = 408, 393, 408, 390, 408, 393,6 V
a["fy6-11-L2-05"] = sum(prod) / len(prod)                 # sum 2400,6 V, mean 400,1 V = U
a["fy6-11-L2-06"] = 4.0e-9 * 1800 / 0.060 * 1000          # L2-06: d = 6,0 cm (not 1,5 cm): E = 3,0e4 V/m, F = 0,12 mN
fx = [60.2, 59.8, 59.5, 59.0, 58.0, 33.0]                 # L2-07: F in µN at x = 0...10 cm, q = 2,0 nC
good = [f for f in fx if abs(f - fx[0]) / fx[0] < 0.03]   # within 3 %: x = 0...6 cm (four points, sum 238,5 µN)
a["fy6-11-L2-07"] = sum(good) / len(good) * 1e-6 / 2.0e-9   # E = 59,6 µN : 2,0 nC = 2,98e4 V/m (U : d = 3,0e4 V/m)
# L2-08 is a force-diagram choice (no number): F_s = |q| E = 20e-9 C · 1,0e5 N/C = 2,0 mN down, G = m g = 1,0e-4 kg · 9,81 = 0,98 mN down
mk = [3.8, 4.6, 3.2, 5.1, 4.2]                            # L3-04: m in 1e-15 kg, hover voltages in V, d = 8,0 mm
uk = [931, 746, 1580, 627, 683]
qk = [m * 1e-15 * g * 8.0e-3 / u for m, u in zip(mk, uk)]   # q = m g d / U = 3,20; 4,84; 1,59; 6,38; 4,83 (1e-19 C)
nk = [round(q / min(qk)) for q in qk]                     # multiples of the smallest charge: 2, 3, 1, 4, 3
a["fy6-11-L3-04"] = sum(q / n for q, n in zip(qk, nk)) / len(qk)   # e = mean of q : n = 1,6017e-19 C
Ei = 2000 / 5.0e-3                                        # L3-05: E = 4,0e5 V/m, F = q E = 4,0e-7 N (1400 times the weight)
ai = 1.0e-12 * Ei / 3.0e-11                               # a = F : m = 1,33e4 m/s^2
a["fy6-11-L3-05"] = 0.5 * ai * (10e-3 / 20) ** 2 * 1000   # y = a t^2 / 2 with t = L : v0 = 0,5 ms: 1,67 mm
print(json.dumps({k: float(f"{v:.8g}") for k, v in a.items()}))
