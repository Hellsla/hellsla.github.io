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
# L2-08 is multiple choice (find the error): row 3 drops the sign; right v_B' = (0,24 + 0,060) / 0,50 = 0,60 m/s; no number
# Level 3 additions
vs = math.sqrt(2 * 0.60 * g * 8.0)                      # skid after the collision: ½Mv'² = μMgs → v' = √(2μgs) = 9,704 m/s
a["fy4-10-L3-04"] = (1100 + 1400) * vs / 1100 * 3.6     # momentum: v_A = (mA+mB)v'/mA = 22,06 m/s = 79,4 km/h
acc = (0.88 - 0.41) / (0.30 - 0.06)                     # deceleration from the first and last table rows: 1,958 m/s²
a["fy4-10-L3-05"] = (0.40 + 0.20) * acc                 # friction force F = (mA+mB)·a = 1,175 N
# Figure tasks (L2-09 reads fy4-10/ex-vt-kaarryt, L3-06 reads fy4-10/ex-xt-tarra)
mA, vA, vB, vA2, vB2 = 0.50, 0.8, -0.4, 0.2, 0.6      # velocity graph: A and B before and after
a["fy4-10-L2-09"] = mA * (vA - vA2) / (vB2 - vB)      # m_B = 0,30 kg (momentum before = after = 0,28 kg·m/s)
mA, v, v2 = 0.30, 0.60 / 1.0, 0.40 / 2.0              # position graph: slopes 0,60 and 0,20 m/s
mB = mA * (v / v2 - 1)                                # 0,60 kg
a["fy4-10-L3-06"] = 0.5 * mA * v**2 - 0.5 * (mA + mB) * v2**2   # 0,054 - 0,018 = 0,036 J
# L2-10 (teacher's brief FY4-A4, a data task on the PhET simulation Collision Lab, screen Explore 1D, read 16.11.2026,
# version 1.1.25): a written task, the answer is a string, so no number in `a`. Every number of its model solution,
# from the simulation's default values (right is positive; the simulation shows two decimals):
m1, v1, m2, v2 = 0.50, 1.00, 1.50, -0.50                # ball 1 and ball 2 before the collision
s10 = {"M": m1 + m2}                                    # 2,00 kg
s10["p"] = m1 * v1 + m2 * v2                            # total momentum before: 0,50 − 0,75 = −0,25 kg·m/s
s10["Ek1"], s10["Ek2"] = 0.5 * m1 * v1 ** 2, 0.5 * m2 * v2 ** 2   # 0,25 J and 0,1875 J
s10["Ek"] = s10["Ek1"] + s10["Ek2"]                     # 0,4375 J, shown as 0,44 J
u1, u2 = -1.25, 0.25                                    # elasticity 100 %: velocities read after the collision
s10["p100"] = m1 * u1 + m2 * u2                         # −0,625 + 0,375 = −0,25 kg·m/s
s10["dp1"], s10["dp2"] = m1 * (u1 - v1), m2 * (u2 - v2)    # momentum changes at 100 %: −1,125 and +1,125 kg·m/s (they cancel)
s10["Ek100"] = 0.5 * m1 * u1 ** 2 + 0.5 * m2 * u2 ** 2  # 0,3906 J + 0,0469 J = 0,4375 J, shown as 0,44 J
u1, u2 = -0.69, 0.06                                    # elasticity 50 %: shown values (exact −0,6875 and 0,0625)
s10["p50"] = m1 * u1 + m2 * u2                          # −0,345 + 0,090 = −0,255 kg·m/s (exact values: −0,25)
s10["Ek50"] = 0.5 * m1 * u1 ** 2 + 0.5 * m2 * u2 ** 2   # 0,1190 J + 0,0027 J = 0,1217 J, about 0,12 J (exact 0,1211 J)
s10["loss50"] = 100 * (s10["Ek"] - s10["Ek50"]) / s10["Ek"]    # 72 % of the kinetic energy leaves the motion
u = -0.13                                               # elasticity 0 %: common shown velocity (exact −0,125)
s10["p0"] = s10["M"] * u                                # 2,00 · (−0,13) = −0,26 kg·m/s (exact value: −0,25)
s10["Ek0"] = 0.5 * s10["M"] * u ** 2                    # 0,0169 J, about 0,02 J (exact 0,0156 J)
s10["loss0"] = 100 * (s10["Ek"] - s10["Ek0"]) / s10["Ek"]      # 96 %
s10["p0_exact"] = s10["M"] * -0.125                     # −0,25 kg·m/s: the difference above is the rounding of the display
print(json.dumps(a))
