"""Every answer in exercises.json for fy4-10, computed from the task data (python -I answers.py).
Velocities are signed along the line of motion (the positive direction named in each solution). Momentum is conserved
in each collision or explosion: the external forces are negligible during it, and the motion is one-dimensional.
Prints {id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json, math

g = 9.81
a = {}
# Level 1: one formula, values given
a["fy4-10-L1-01"] = 0.40 * 0.50 + 0.25 * -0.60          # total momentum p = m1 v1 + m2 v2 = 0,20 − 0,15 = 0,050 kg·m/s
a["fy4-10-L1-02"] = 0.50 * 0.80 / (0.50 + 0.30)         # stick together: v' = m1 v1 / (m1 + m2) = 0,50 m/s
a["fy4-10-L1-03"] = 45 * 1.2 / 60                       # skaters push apart: 0 = m1 v1' + m2 v2' → |v1'| = 0,90 m/s
a["fy4-10-L1-04"] = (0.16 * 4.0 - 0.16 * -0.44) / 0.20  # puck A bounces back: v_B' = (mA vA − mA vA')/mB = 3,552 m/s
a["fy4-10-L1-05"] = (0.30 * 0.60 + 0.30 * -0.20) / 0.60  # head-on, stick together: v' = 0,20 m/s
# Level 2: two steps, a conversion or a rearrangement
a["fy4-10-L2-01"] = 0.50e-3 * 180 / 3.2                 # recoil of an air rifle: 0,50 g = 0,50·10⁻³ kg → 0,028125 m/s
m1, v1, m2 = 85, 6.0, 75
u = m1 * v1 / (m1 + m2)                                 # tackle: common speed 3,1875 m/s
a["fy4-10-L2-02"] = 0.5 * m1 * v1 ** 2 - 0.5 * (m1 + m2) * u ** 2   # E_k lost = 1530 − 812,8 = 717,2 J
m1, v1, m2, u1 = 0.20, 0.60, 0.40, -0.10
u2 = (m1 * v1 - m1 * u1) / m2                           # 0,35 m/s
a["fy4-10-L2-03"] = 100 * (0.5 * m1 * u1 ** 2 + 0.5 * m2 * u2 ** 2) / (0.5 * m1 * v1 ** 2)   # 70,83 % of E_k left
a["fy4-10-L2-04"] = 30000 * (1.8 - 1.2) / 1.2           # coupling: m2 = m1 (v1 − v')/v' = 15 000 kg
# Level 3: reasoning, two ideas, an unfamiliar context
m, v, M = 0.010, 400, 2.0
u = m * v / (m + M)                                     # ballistic pendulum: 1,99 m/s just after the bullet stops in the block
a["fy4-10-L3-01"] = u ** 2 / (2 * g) * 100              # then ½(m+M)u² = (m+M)gh → h = 0,2019 m = 20,19 cm
a["fy4-10-L3-02"] = (0.90 * 12 - 0.30 * 40) / 0.60      # firework at 12 m/s up splits; 0,30 kg up at 40 m/s → −2,0 m/s (down)
u = 3.0 * 4.0 / 120                                     # astronaut (120 kg with the suit) throws a 3,0 kg tool at 4,0 m/s: 0,10 m/s
a["fy4-10-L3-03"] = 12.0 / u                            # drifts 12,0 m back to the station: t = 120 s
# Level 1 additions: concept, recoil, elastic exchange of velocities
a["fy4-10-L1-07"] = 2.0 * 6.0 / 35                      # skater throws a ball: 0 = m v_p' + M v_l' → |v_l'| = 12/35 = 0,3429 m/s
a["fy4-10-L1-08"] = 1.8                                 # equal masses, elastic, target at rest: velocities are exchanged → 1,8 m/s
# Level 2 additions
mA, mB, v0 = 0.50, 0.30, 0.60                           # three collisions of the same carts; experiment 3: vA' = 0,25 and vB' = 0,58 m/s
a["fy4-10-L2-05"] = 100 * (0.5 * mA * 0.25 ** 2 + 0.5 * mB * 0.58 ** 2) / (0.5 * mA * v0 ** 2)   # E_k left = 0,0661 / 0,090 = 73,4 %
vA, vA2, vB2 = (0.51 - 0.00) / 1.0, (1.21 - 1.10) / 1.0, (1.54 - 1.27) / 1.0   # speeds from the position table: 0,51, 0,11 and 0,27 m/s
a["fy4-10-L2-06"] = 100 * (0.5 * 0.40 * vA2 ** 2 + 0.5 * 0.60 * vB2 ** 2) / (0.5 * 0.40 * vA ** 2)   # E_k left = 0,0243 / 0,0520 = 46,7 %
a["fy4-10-L2-07"] = (0.60 * 0.80 + 0.20 * -0.40) / (0.60 + 0.20)   # error analysis: the left-moving cart is negative → 0,50 m/s
# Level 3 additions
vs = math.sqrt(2 * 0.60 * g * 8.0)                      # skid after the collision: ½Mv'² = μMgs → v' = √(2μgs) = 9,704 m/s
a["fy4-10-L3-04"] = (1100 + 1400) * vs / 1100 * 3.6     # momentum: v_A = (mA+mB)v'/mA = 22,06 m/s = 79,4 km/h
acc = (0.88 - 0.41) / (0.30 - 0.06)                     # deceleration from the first and last table rows: 1,958 m/s²
a["fy4-10-L3-05"] = (0.40 + 0.20) * acc                 # friction force F = (mA+mB)·a = 1,175 N
print(json.dumps(a))
