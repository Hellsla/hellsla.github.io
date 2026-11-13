"""Every answer in exercises.json for fy4-13, computed from the task data (python -I answers.py).
Two bodies joined by a light string over a light, frictionless pulley (or two sleds on ice), friction and air resistance neglected.
Each solution starts from the force diagram of each body; the positive direction of each body is its direction of motion;
g = 9,81 m/s². Prints {id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json, math

g = 9.81
a = {}


def within(exact, shown, tol):
    """The answer a student gets by rounding to the data's figures must stay inside the tolerance."""
    assert abs(shown - exact) / exact <= tol, (exact, shown, tol)
    return exact


# Level 1: one body's equation, or the whole chain at once
a["fy4-13-L1-01"] = within(3.0 / 1.5, 2.0, 0.02)                       # cart on a smooth table: T = m a → a = 2,0 m/s²
a["fy4-13-L1-02"] = within(0.60 * (g - 2.0), 4.7, 0.02)                # hanging body: mg − T = ma → T = m(g − a) = 4,686 N
a["fy4-13-L1-03"] = within(1.0 * 0.40 * g / (1.0 + 0.40), 2.8, 0.02)    # cart 1,0 kg, weight 0,40 kg: T = m1 m2 g/(m1 + m2) = 2,803 N
a["fy4-13-L1-04"] = within(3.0 * g, 29, 0.02)                          # equal masses at rest: T − mg = 0 → T = 29,43 N
a["fy4-13-L1-05"] = within(12 / (1.0 + 2.0), 4.0, 0.02)                # two carts pulled as one chain: a = F/(m1 + m2) = 4,0 m/s²
# Level 2: two equations, T and a unknown
m1, m2, acc = 50.0, 30.0, 1.2
a["fy4-13-L2-01"] = within((m1 + m2) * (g + acc), 880, 0.02)           # two crates one under the other, lifted with a = 1,2 m/s²: T1 = (m1 + m2)(g + a) = 880,8 N
m1, m2 = 0.50, 1.0
a["fy4-13-L2-02"] = within(2 * m1 * m2 * g / (m1 + m2), 6.5, 0.02)     # two hanging bodies: T = 2 m1 m2 g/(m1 + m2) = 6,54 N
F, m1, m2 = 20.0, 3.0, 2.0
a["fy4-13-L2-03"] = within(m2 * F / (m1 + m2), 8.0, 0.02)              # sleds: a = F/(m1 + m2) = 4,0; rope between: T = m2 a = 8,0 N
m1, acc = 0.60, 2.0
a["fy4-13-L2-04"] = within(m1 * (g + acc) / (g - acc), 0.91, 0.02)     # two hanging bodies, the lighter 0,60 kg, the heavier falls with a = 2,0 m/s²: m2 = m1 (g + a)/(g − a) = 0,9073 kg
# Level 3: reasoning with two ideas
m1, m2 = 800.0, 1200.0
a["fy4-13-L3-01"] = within(2 * (2 * m1 * m2 * g / (m1 + m2)), 19000, 0.02)  # cabin 800 kg, counterweight 1200 kg: T = 9418 N, force on the light pulley axle 2T = 18835 N
Tmax, m1 = 3.0, 1.0
a["fy4-13-L3-02"] = within(Tmax * m1 / (m1 * g - Tmax), 0.44, 0.02)    # T = m1 m2 g/(m1 + m2) ≤ Tmax → m2 ≤ Tmax m1/(m1 g − Tmax) = 0,4405 kg
m1, m2, s = 1.5, 0.50, 0.90
acc = m2 * g / (m1 + m2)                                               # a = 2,4525 m/s²
a["fy4-13-L3-03"] = within(math.sqrt(2 * s / acc), 0.86, 0.02)         # s = ½ a t² → t = √(2s/a) = 0,857 s
# Exercise bank additions: L1-06 and L1-08 are multiple choice (no number)
a["fy4-13-L1-07"] = within((0.70 - 0.30) * g / (0.30 + 0.70), 3.9, 0.02)   # two hanging bodies: a = (m2 − m1) g/(m1 + m2) = 3,924 m/s²
dm, acc_s = [0.050, 0.100, 0.150, 0.200, 0.250], [0.96, 2.02, 2.88, 3.97, 4.84]
k = sum(x * y for x, y in zip(dm, acc_s)) / sum(x * x for x in dm)          # line through the origin: a = k Δm, k = 19,53 (m/s²)/kg
a["fy4-13-L2-05"] = within(k * 0.500, 9.8, 0.03)                           # Atwood: k = g/M → g = k M = 9,77 m/s²
m1, acc_m = 1.20, 2.84
a["fy4-13-L2-06"] = within(m1 * acc_m, 3.4, 0.04)                          # cart: T = m1 a = 3,408 N (hanging body: m2 (g − a) = 3,485 N)
m1, m2 = 2.0, 0.50
a["fy4-13-L2-07"] = within(m2 * g / (m1 + m2), 2.0, 0.02)                 # error: a = m2 g/(m1 + m2) = 1,962 m/s², not m2 g/m1 = 2,45 m/s²
tv = [(0, 0.00), (5, 2.46), (10, 5.03), (15, 7.48), (20, 10.02)]
a_tr = round((tv[-1][1] - tv[0][1]) / (tv[-1][0] - tv[0][0]), 2)           # a = 10,02/20 = 0,50 m/s²
a["fy4-13-L3-04"] = within((18.0 + 12.0) * a_tr, 15, 0.04)                 # coupling 1–2 pulls wagons 2 and 3: K = (m2 + m3) a = 15 kN (t·m/s² = kN); reordered 12, 18, 24 t: (18 + 24) a = 21 kN
s_d, rows = 0.80, [(0.100, 1.29), (0.200, 0.96), (0.300, 0.80), (0.400, 0.73)]
m1_list = [m2 * (g / (2 * s_d / t**2) - 1) for m2, t in rows]              # m1 = m2 (g/a − 1), a = 2 s/t²: 0,920; 0,930; 0,877; 0,907 kg
a["fy4-13-L3-05"] = within(sum(m1_list) / len(m1_list), 0.91, 0.04)        # mean 0,9086 kg
# Figure tasks (cart's (t, v) points: (0,0), (0,5; 1,0), (1,0; 2,0), (1,5; 2,9), (2,0; 3,9), read: a = 3,9/2,0 = 1,95 m/s²)
a_fig = (3.9 - 0.0) / (2.0 - 0.0)                                           # slope of the points through the origin: 1,95 m/s²
a["fy4-13-L2-09"] = within(0.80 * a_fig, 1.6, 0.04)                         # cart 0,80 kg on a frictionless track: T = m1 a = 1,56 N (the hanging mass is not needed)
a["fy4-13-L3-06"] = within(0.20 * (g / a_fig - 1), 0.81, 0.04)             # hanging 0,20 kg: m2 g = (m1 + m2) a → m1 = m2 (g/a − 1) = 0,806 kg
print(json.dumps(a))
