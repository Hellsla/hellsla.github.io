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
print(json.dumps(a))
