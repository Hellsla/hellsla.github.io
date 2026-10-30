"""FY4 Sovella itsenäisesti: every number of the worked solutions, recomputed from the task data.
Prints {"<task>-<part>": value} for the parts with an answer in tasks.json (and the intermediate values the solutions
quote); `python scripts/practice.py check FY4` compares them with tasks.json."""
import json, math

g = 9.81

# fy4-s1: the ski wax test on a gentle slope (simulated data: constant acceleration + small noise, see figures.py)
alpha = math.radians(4.0)
t = list(range(9))                                                   # s
vA = [2.10, 2.52, 2.86, 3.31, 3.63, 4.06, 4.40, 4.86, 5.23]          # m/s, wax A
vB = [1.90, 2.12, 2.42, 2.62, 2.90, 3.09, 3.40, 3.59, 3.86]          # m/s, wax B


def fit(x, y):
    mx, my = sum(x) / len(x), sum(y) / len(y)
    k = sum((a - mx) * (b - my) for a, b in zip(x, y)) / sum((a - mx) ** 2 for a in x)
    return k, my - k * mx


kA, bA = fit(t, vA); kB, bB = fit(t, vB)
# the slopes as read in the solution from two far-apart points of each drawn line: (0 s; 2,10 m/s)–(8 s; 5,22 m/s), (0 s; 1,90 m/s)–(8 s; 3,86 m/s)
aA = (5.22 - 2.10) / 8; aB = (3.86 - 1.90) / 8
gs, gc = g * math.sin(alpha), g * math.cos(alpha)
muA = (gs - aA) / gc; muB = (gs - aB) / gc
dmu = 0.02 / gc                                                     # a slope read 0,02 m/s² off changes mu this much
# e: wax A again, a measured at different speeds (simulated: a = a0 - k v² with C_d A ≈ 0,5 m², rho = 1,25 kg/m³, plus noise)
vE = [2.0, 3.0, 4.5, 6.0, 7.5, 9.0]                                # m/s
aE = [0.43, 0.41, 0.36, 0.30, 0.20, 0.10]                          # m/s²
kE, a0 = fit([v * v for v in vE], aE)                              # the curve a = a0 + kE v² (kE < 0) drawn through the points
muA0 = (gs - a0) / gc                                              # wax A without air resistance

# fy4-s2: the zipline; h and s are from the start platform to the start of the brake, where the speed is measured
h, s, m1, v_meas, m2 = 15.0, 180.0, 62.0, 11.2, 95.0
v_ideal = math.sqrt(2 * g * h)
Ep1 = m1 * g * h; Ek1 = 0.5 * m1 * v_meas ** 2
F_res = (Ep1 - Ek1) / s
lost = (Ep1 - Ek1) / Ep1
Ep2 = m2 * g * h; Ek2 = Ep2 - F_res * s
v_heavy = math.sqrt(2 * Ek2 / m2)
v_heavy29 = math.sqrt(2 * (Ep2 - 29 * s) / m2)                # c with b's answer rounded to 29 N (Hyväksytään myös)

# fy4-s3: the rear-end collision
mA, mB, mu, skid, m_driver, dt = 1250.0, 1700.0, 0.75, 4.2, 68.0, 0.12
v_after = math.sqrt(2 * mu * g * skid)
vB_before = (mA + mB) * v_after / mB
Ek_before = 0.5 * mB * vB_before ** 2; Ek_after = 0.5 * (mA + mB) * v_after ** 2
F_ka = m_driver * v_after / dt
ratio = F_ka / (m_driver * g)
J_fric = mu * (mA + mB) * g * dt                               # N·s: the most friction can take during the collision
vB_max = (mB * vB_before + J_fric) / mB

out = {"fy4-s1-c-A": round(muA, 4), "fy4-s1-c-B": round(muB, 4), "fy4-s1-aA": round(aA, 4), "fy4-s1-aB": round(aB, 4),
       "fy4-s1-fitA": round(kA, 4), "fy4-s1-fitB": round(kB, 4), "fy4-s1-gsin": round(gs, 4), "fy4-s1-gcos": round(gc, 3),
       "fy4-s1-dmu": round(dmu, 4), "fy4-s1-e-a0": round(a0, 3), "fy4-s1-e-mu": round(muA0, 4), "fy4-s1-e-k": round(-kE, 5),
       "fy4-s1-e-dmu": round(muA - muA0, 4),
       "fy4-s2-a": round(v_ideal, 3), "fy4-s2-a-kmh": round(v_ideal * 3.6, 1), "fy4-s2-Ep": round(Ep1, 1), "fy4-s2-Ek": round(Ek1, 1),
       "fy4-s2-b": round(F_res, 2), "fy4-s2-lost": round(lost, 3), "fy4-s2-Ep2": round(Ep2, 1), "fy4-s2-Ek2": round(Ek2, 1),
       "fy4-s2-c": round(v_heavy, 3), "fy4-s2-c-kmh": round(v_heavy * 3.6, 1), "fy4-s2-W": round(Ep1 - Ek1, 1),
       "fy4-s2-W29": round(29 * s, 0), "fy4-s2-c29": round(v_heavy29, 3), "fy4-s2-meas-kmh": round(v_meas * 3.6, 1),
       "fy4-s3-a": round(v_after, 3), "fy4-s3-b": round(vB_before, 3), "fy4-s3-b-kmh": round(vB_before * 3.6, 1),
       "fy4-s3-p": round(mB * vB_before, 0), "fy4-s3-Ek-before": round(Ek_before, 0), "fy4-s3-Ek-after": round(Ek_after, 0),
       "fy4-s3-c": round(F_ka, 0), "fy4-s3-ratio": round(ratio, 2),
       "fy4-s3-J": round(J_fric, 0), "fy4-s3-vB-max": round(vB_max, 2), "fy4-s3-dec": round(mu * g, 2), "fy4-s3-a-kmh": round(v_after * 3.6, 1)}
print(json.dumps(out))
