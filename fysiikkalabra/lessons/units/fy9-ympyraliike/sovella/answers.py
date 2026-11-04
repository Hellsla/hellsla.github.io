"""FY9 fy9-ympyraliike, Tehtävät: every number of the worked solutions, recomputed from the task data.
Prints {"<task>-<part>[-<name>]": value} for the parts with an answer in tasks.json and the intermediate values the
solutions quote; `python scripts/practice.py check units/fy9-ympyraliike` compares them with tasks.json."""
import json, math

g = 9.81
G = 6.674e-11                          # N m^2 / kg^2
M_E = 5.97e24                          # kg, the Earth
R_E = 6371e3                           # m
GM = G * M_E
T_DAY = 23 * 3600 + 56 * 60            # s, one turn of the Earth


def fit(x, y):
    mx, my = sum(x) / len(x), sum(y) / len(y)
    k = sum((a - mx) * (b - my) for a, b in zip(x, y)) / sum((a - mx) ** 2 for a in x)
    return k, my - k * mx


out = {}
S = "fy9-ympyraliike"

# s1: a boat trailer and its drawbar load (example data); distances forward of the axle
m_tr, x_tr, m_boat, x_boat, x_hitch = 165.0, 0.58, 430.0, 0.12, 3.25
F_hitch = g * (m_tr * x_tr + m_boat * x_boat) / x_hitch          # N, the ball's upward force on the drawbar
N_axle = (m_tr + m_boat) * g - F_hitch
dx = (60.0 * x_hitch - (m_tr * x_tr + m_boat * x_boat)) / m_boat  # m, boat forward for a 60 kg drawbar load
m_can, x_can = 30.0, -1.40                                        # a canister 1,40 m behind the axle
F_hitch_d = g * (m_tr * x_tr + m_boat * x_boat + m_can * x_can) / x_hitch
out.update({f"{S}-s1-a-F": round(F_hitch, 2), f"{S}-s1-a-m": round(F_hitch / g, 2),
            f"{S}-s1-moments": round(m_tr * x_tr + m_boat * x_boat, 3),
            f"{S}-s1-b": round(N_axle / 1000, 4), f"{S}-s1-weight": round((m_tr + m_boat) * g, 1),
            f"{S}-s1-c": round(dx * 100, 2), f"{S}-s1-d-m": round(F_hitch_d / g, 2), f"{S}-s1-d-F": round(F_hitch_d, 1)})

# s2: a polar weather satellite (example data)
h2, m2 = 830e3, 4100.0
r2 = R_E + h2
v2 = math.sqrt(GM / r2)
T2 = 2 * math.pi * r2 / v2
F2 = GM * m2 / r2 ** 2
turn = 360 * T2 / T_DAY
shift = 2 * math.pi * R_E * T2 / T_DAY
out.update({f"{S}-s2-a-v": round(v2 / 1000, 4), f"{S}-s2-a-T": round(T2 / 60, 2), f"{S}-s2-T-s": round(T2),
            f"{S}-s2-b": round(F2 / 1000, 3), f"{S}-s2-b-weight": round(m2 * g / 1000, 3), f"{S}-s2-b-ratio": round(F2 / (m2 * g), 4),
            f"{S}-s2-b-Rr2": round((R_E / r2) ** 2, 4),
            f"{S}-s2-c-deg": round(turn, 2), f"{S}-s2-c-km": round(shift / 1000), f"{S}-s2-orbits": round(86400 / T2, 2),
            f"{S}-s2-d-ratio": round((42157e3 - R_E) / h2, 1)})

# s3: a cart on a rotating platform, a force sensor at the axle (invented data: m 0,200 kg, r 0,250 m, noise about 1,5 %)
m3, r3 = 0.200, 0.250
T10 = [6.0, 7.0, 8.0, 9.5, 11.0, 13.0, 15.0]                      # s, ten rounds
F3 = [5.42, 4.07, 3.05, 2.21, 1.65, 1.19, 0.88]                   # N
T3 = [t / 10 for t in T10]
X3 = [1 / t ** 2 for t in T3]                                    # 1/s^2
k3, b3 = fit(X3, F3)
# read in the solution from two far-apart points of the drawn line: (0,50; 1,01) and (2,50; 4,91)
k_read = (4.91 - 1.01) / (2.50 - 0.50)
b_read = 1.01 - k_read * 0.50
m_read = k_read / (4 * math.pi ** 2 * r3)
T_min = math.sqrt(k_read / 8.0)                                   # the solution leaves out the small intercept b_read
out.update({f"{S}-s3-T": T3, f"{S}-s3-x": [round(v, 3) for v in X3], f"{S}-s3-k-fit": round(k3, 4), f"{S}-s3-b-fit": round(b3, 4),
            f"{S}-s3-k": round(k_read, 3), f"{S}-s3-b0": round(b_read, 3), f"{S}-s3-k-model": round(4 * math.pi ** 2 * m3 * r3, 4),
            f"{S}-s3-c": round(m_read, 4), f"{S}-s3-c-diff": round(100 * (m_read - m3) / m3, 2),
            f"{S}-s3-d": round(T_min, 4), f"{S}-s3-d-rpm": round(60 / T_min, 1)})

# s4: a rotating ring station (word task; the numbers its model answer quotes)
h4, r4 = 400e3, 110.0
g4 = GM / (R_E + h4) ** 2
T4 = 2 * math.pi * math.sqrt(r4 / g)
out.update({f"{S}-s4-g400": round(g4, 3), f"{S}-s4-share": round(100 * g4 / g, 1), f"{S}-s4-T": round(T4, 2),
            f"{S}-s4-rpm": round(60 / T4, 2), f"{S}-s4-v": round(2 * math.pi * r4 / T4, 2)})

# s5: the metre-stick lever report (invented data)
m_stick, x_cm, x_piv, m_w, x_w, x_k = 120.0, 50.0, 40.0, 200.0, 10.0, 82.0   # g and cm marks
m_k = (m_w * (x_piv - x_w) - m_stick * (x_cm - x_piv)) / (x_k - x_piv)
m_k_student = m_w * (x_piv - x_w) / (x_k - x_piv)
out.update({f"{S}-s5-a": round(m_k, 2), f"{S}-s5-student": round(m_k_student, 3), f"{S}-s5-diff": round(100 * (m_k - 113) / 113, 2),
            f"{S}-s5-student-diff": round(100 * (m_k_student - 113) / 113, 1),
            f"{S}-s5-dk": round(m_w * (x_piv - x_w) / (x_k - x_piv) - m_w * (x_piv - x_w) / (x_k + 0.5 - x_piv), 2)})

# s6: a roller coaster loop (example data; the cross-module task with FY4 energy)
h6, r6, loss, m6 = 30.0, 10.0, 0.12, 60.0
vb2 = 2 * (1 - loss) * g * h6
vb = math.sqrt(vb2)
Nb = m6 * (g + vb2 / r6)
vt2 = vb2 - 2 * g * (2 * r6)
vt = math.sqrt(vt2)
Nt = m6 * (vt2 / r6 - g)
out.update({f"{S}-s6-a": round(vb, 3), f"{S}-s6-a-kmh": round(vb * 3.6, 1),
            f"{S}-s6-b": round(Nb, 1), f"{S}-s6-b-ratio": round(Nb / (m6 * g), 2), f"{S}-s6-b-an": round(vb2 / r6, 2),
            f"{S}-s6-c-v": round(vt, 3), f"{S}-s6-c-N": round(Nt, 1), f"{S}-s6-c-ratio": round(Nt / (m6 * g), 3),
            f"{S}-s6-c-an": round(vt2 / r6, 3), f"{S}-s6-vmin": round(math.sqrt(g * r6), 2)})

print(json.dumps(out))
