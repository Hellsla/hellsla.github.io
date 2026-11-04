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
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
