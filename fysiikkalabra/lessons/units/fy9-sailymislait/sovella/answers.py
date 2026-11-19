"""FY9 fy9-sailymislait, Tehtävät: every number of the worked solutions, recomputed from the task data.
Prints {"<task>-<part>[-<name>]": value} for the parts with an answer in tasks.json and the intermediate values the
solutions quote; `python scripts/practice.py check units/fy9-sailymislait` compares them with tasks.json."""
import json, math

g = 9.81
kmh = 1000 / 3600                      # m/s per km/h, by substitution: 1 km/h = 1000 m : 3600 s

def fit(x, y):
    mx, my = sum(x) / len(x), sum(y) / len(y)
    k = sum((a - mx) * (b - my) for a, b in zip(x, y)) / sum((a - mx) ** 2 for a in x)
    return k, my - k * mx

out = {}
S = "fy9-sailymislait"

# s1: the zip line over a lake (example data)
m1, h1, L1, v_end, t_brake = 82.0, 36.0, 410.0, 15.0, 1.6
v_free = math.sqrt(2 * g * h1)                      # m/s without resistance
Ep1 = m1 * g * h1
Ek1 = 0.5 * m1 * v_end ** 2
W1 = Ek1 - Ep1                                      # J, the work of the resistive forces (negative)
F1 = -W1 / L1                                       # N, mean resistive force along the cable
F_brake = m1 * v_end / t_brake                      # N, mean horizontal force of the brake
out.update({f"{S}-s1-a": round(v_free, 3), f"{S}-s1-a-kmh": round(v_free / kmh, 1),
            f"{S}-s1-b-W": round(W1 / 1000, 3), f"{S}-s1-b-F": round(F1, 2), f"{S}-s1-Ep": round(Ep1, 1), f"{S}-s1-Ek": Ek1,
            f"{S}-s1-share": round(-W1 / Ep1, 4),
            f"{S}-s1-c": round(F_brake, 2), f"{S}-s1-weight": round(m1 * g, 1), f"{S}-s1-ratio": round(F_brake / (m1 * g), 3),
            f"{S}-s1-p": m1 * v_end})
# the resistive forces' work is negative (energy principle) and the mean force a magnitude (FY9 audit 2026-11-10):
# practice.py check compares signed values, so tasks.json must carry the same signs
assert out[f"{S}-s1-b-W"] < 0 < out[f"{S}-s1-b-F"], "s1 b: W_muut must be negative and F positive"

# s2: curling (example data); both stones 19,0 kg
m2, v0, v1, s0 = 19.0, 2.40, 0.62, 27.0
mu = (v0 ** 2 - v1 ** 2) / (2 * g * s0)
vA_after = 0.05
vB_after = (m2 * v1 - m2 * vA_after) / m2           # momentum: equal masses
Ek_before = 0.5 * m2 * v1 ** 2
Ek_after = 0.5 * m2 * vA_after ** 2 + 0.5 * m2 * vB_after ** 2
sB = vB_after ** 2 / (2 * mu * g)
W_fric = -mu * m2 * g * s0
out.update({f"{S}-s2-a": round(mu, 5), f"{S}-s2-a-W": round(W_fric, 2), f"{S}-s2-b": round(vB_after, 3),
            f"{S}-s2-b-share": round(100 * Ek_after / Ek_before, 2), f"{S}-s2-Ek-before": round(Ek_before, 3),
            f"{S}-s2-Ek-after": round(Ek_after, 3), f"{S}-s2-c": round(sB, 3)})

# s3: braking tests on a closed track, wet asphalt (invented data: t_r 0,90 s, a 6,4 m/s^2, noise about 0,7 m)
V = [30, 40, 50, 60, 70, 80, 90]                          # km/h
SP = [12.5, 20.0, 27.5, 36.5, 46.5, 58.5, 72.0]           # m
x = [vk * kmh for vk in V]                                # m/s
y = [s / v for s, v in zip(SP, x)]                        # s
k, b = fit(x, y)
# read in the solution from two far-apart points of the drawn line: (10 m/s; 1,66 s) and (25 m/s; 2,86 s)
k_read = (2.86 - 1.66) / (25 - 10)
b_read = 1.66 - k_read * 10
a_read = 1 / (2 * k_read)
mu3 = a_read / g
v100 = 100 * kmh
s100 = v100 * b_read + v100 ** 2 * k_read
out.update({f"{S}-s3-k": round(k, 5), f"{S}-s3-b0": round(b, 4), f"{S}-s3-a-fit": round(1 / (2 * k), 3),
            f"{S}-s3-kread": round(k_read, 4), f"{S}-s3-c-tr": round(b_read, 3), f"{S}-s3-c-a": round(a_read, 3),
            f"{S}-s3-d-mu": round(mu3, 4), f"{S}-s3-d-s": round(s100, 2), f"{S}-s3-s100-fit": round(v100 * b + v100 ** 2 * k, 2),
            f"{S}-s3-y": [round(t, 3) for t in y], f"{S}-s3-x": [round(t, 3) for t in x],
            f"{S}-s3-sr100": round(v100 * b_read, 2), f"{S}-s3-sj100": round(v100 ** 2 * k_read, 2)})

# s4: hydro and wind (word task; the numbers its model answer quotes)
ratio_wind = (9.0 / 6.0) ** 3
Q4, h4, eta4 = 120.0, 9.0, 0.90
P_hydro = eta4 * 1000 * Q4 * g * h4 / 1e6                 # MW
P_hydro_h12 = eta4 * 1000 * Q4 * g * 12.0 / 1e6
out.update({f"{S}-s4-ratio": round(ratio_wind, 3), f"{S}-s4-P": round(P_hydro, 2), f"{S}-s4-P12": round(P_hydro_h12, 2),
            f"{S}-s4-E1m3": round(1000 * g * h4 / 1000, 2)})

# s5: the cart report (invented data: carts on a rolling track, velcro, video analysis)
mA5, mB5 = 0.520, 0.480
VA = [0.452, 0.622, 0.781, 0.901]
VP = [0.207, 0.303, 0.391, 0.455]
rel = [100 * ((mA5 + mB5) * vp - mA5 * va) / (mA5 * va) for va, vp in zip(VA, VP)]
pb, pa = mA5 * VA[1], (mA5 + mB5) * VP[1]
Ekb, Eka = 0.5 * mA5 * VA[1] ** 2, 0.5 * (mA5 + mB5) * VP[1] ** 2
v_theory = mA5 * VA[1] / (mA5 + mB5)
out.update({f"{S}-s5-a": round(100 * (pa - pb) / pb, 2), f"{S}-s5-pb": round(pb, 4), f"{S}-s5-pa": round(pa, 4),
            f"{S}-s5-rel": [round(r, 1) for r in rel], f"{S}-s5-Ek-lost": round(100 * (1 - Eka / Ekb), 1),
            f"{S}-s5-vtheory": round(v_theory, 4), f"{S}-s5-afric": round((v_theory ** 2 - VP[1] ** 2) / (2 * 0.60), 4)})

# s6: the pile driver (example data); the cross-module task with FY3 heat
M6, mp, h6, s6, frac, mh, c_steel, n_blows = 3500.0, 1100.0, 0.60, 0.018, 0.40, 30.0, 460.0, 50
v6 = math.sqrt(2 * g * h6)
vc = M6 * v6 / (M6 + mp)
Ek6 = 0.5 * M6 * v6 ** 2
Ek6c = 0.5 * (M6 + mp) * vc ** 2
lost = Ek6 - Ek6c
F_soil = Ek6c / s6 + (M6 + mp) * g
Q1 = frac * lost
dT1 = Q1 / (mh * c_steel)
out.update({f"{S}-s6-a": round(v6, 3), f"{S}-s6-Ep": round(M6 * g * h6, 1), f"{S}-s6-b-v": round(vc, 3),
            f"{S}-s6-b-E": round(lost, 1), f"{S}-s6-Ek": round(Ek6, 1), f"{S}-s6-Ekc": round(Ek6c, 1),
            f"{S}-s6-share": round(100 * lost / Ek6, 2),
            f"{S}-s6-c": round(F_soil / 1000, 2), f"{S}-s6-weight": round((M6 + mp) * g, 1),
            f"{S}-s6-Q1": round(Q1, 1), f"{S}-s6-dT1": round(dT1, 4), f"{S}-s6-d": round(n_blows * dT1, 2)})

# s7: the sled on a slope (example data; E_p0 = 40 J and E_k = 25 J read from fy4-8/palkit-asteikko)
m7, Ep7, Ek7, L7 = 2.0, 40.0, 25.0, 6.0
h7 = Ep7 / (m7 * g)
W7 = Ek7 - Ep7                                      # J, the work of friction (negative)
F7 = -W7 / L7                                       # N, friction force
v7 = math.sqrt(2 * Ek7 / m7)
v7_free = math.sqrt(2 * Ep7 / m7)
alpha7 = math.asin(h7 / L7)
mu7 = F7 / (m7 * g * math.cos(alpha7))
m7b = 3.0
Ep7b = m7b * g * h7
Ek7b = Ep7b + (-mu7 * m7b * g * math.cos(alpha7) * L7)
v7b = math.sqrt(2 * Ek7b / m7b)
out.update({f"{S}-s7-a": round(h7, 3), f"{S}-s7-b-W": round(W7, 2), f"{S}-s7-b-F": round(F7, 3),
            f"{S}-s7-c-v": round(v7, 3), f"{S}-s7-c-v0": round(v7_free, 3), f"{S}-s7-share": round(100 * -W7 / Ep7, 1),
            f"{S}-s7-alpha": round(math.degrees(alpha7), 1), f"{S}-s7-mu": round(mu7, 3),
            f"{S}-s7-d": round(v7b, 3), f"{S}-s7-d-Ep": round(Ep7b, 2), f"{S}-s7-d-W": round(Ek7b - Ep7b, 2), f"{S}-s7-d-Ek": round(Ek7b, 2),
            f"{S}-s7-d-v": round(v7b, 3), f"{S}-s7-red": round(100 * (1 - v7 / v7_free), 1)})

# s8: the kick on a football (example data; the triangle 900 N, 12 ms read from fy4-9/tarkistus-kolmio)
m8, F8, T8, h8obs = 0.43, 900.0, 0.012, 6.5
I8 = 0.5 * F8 * T8
v8 = I8 / m8
Ek8 = 0.5 * m8 * v8 ** 2
h8 = v8 ** 2 / (2 * g)
W8 = m8 * g * h8obs - Ek8                           # J, the work of air resistance (negative)
Fa8 = -W8 / h8obs
out.update({f"{S}-s8-a": round(I8, 3), f"{S}-s8-b": round(v8, 3), f"{S}-s8-c-Ek": round(Ek8, 2), f"{S}-s8-c-h": round(h8, 3),
            f"{S}-s8-d-W": round(W8, 2), f"{S}-s8-d-F": round(Fa8, 3), f"{S}-s8-Fmean": round(F8 / 2, 1),
            f"{S}-s8-share": round(100 * -W8 / Ek8, 1), f"{S}-s8-Epobs": round(m8 * g * h8obs, 2),
            f"{S}-s8-weight": round(m8 * g, 2), f"{S}-s8-sq": round(0.2 * 27, 1)})

print(json.dumps(out))
