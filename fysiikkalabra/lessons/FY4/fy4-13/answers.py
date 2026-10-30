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
print(json.dumps(a))
