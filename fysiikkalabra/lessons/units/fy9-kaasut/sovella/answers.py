"""FY9 fy9-kaasut, Tehtävät: every number of the worked solutions, recomputed from the task data.
Prints {"<task>-<part>[-<name>]": value} for the parts with an answer in tasks.json and the intermediate values the
solutions quote; `python scripts/practice.py check units/fy9-kaasut` compares them with tasks.json."""
import json, math

g, R, p0 = 9.81, 8.31, 101.0e3          # m/s^2, J/(mol K), Pa (the air pressure the tasks give)
K = 273.15


def fit(x, y):
    mx, my = sum(x) / len(x), sum(y) / len(y)
    k = sum((a - mx) * (b - my) for a, b in zip(x, y)) / sum((a - mx) ** 2 for a in x)
    return k, my - k * mx


out = {}

# s1: the pneumatic car lift (example data)
m1, d1, h1 = 1800.0, 0.200, 1.20        # kg (car 1600 kg + platform 200 kg), m piston diameter, m lift height
A1 = math.pi * (d1 / 2) ** 2             # m^2
dp1 = m1 * g / A1                        # Pa, overpressure under the piston at constant speed
pc = dp1 + p0                            # Pa, total pressure of the air in the cylinder
W1 = m1 * g * h1                         # J, work on the car and platform
dV1 = A1 * h1                            # m^3
Wgas = pc * dV1                          # J, work of the cylinder air (it also pushes back the outside air)
Vt, pt1 = 0.100, 900e3 + p0              # m^3 tank, Pa total
pt2 = pt1 - pc * dV1 / Vt                # isothermal: pt1 Vt = pt2 Vt + pc dV
pt3 = pt2 - pc * dV1 / Vt                # what a second full lift would need
x2 = (pt2 - pc) * Vt / pc / A1           # m: height of the second lift before the tank falls to pc
out.update({"fy9-kaasut-s1-a": round(dp1 / 1e3, 1), "fy9-kaasut-s1-A": round(A1, 5), "fy9-kaasut-s1-G": round(m1 * g, 0),
            "fy9-kaasut-s1-pc": round(pc / 1e3, 1),
            "fy9-kaasut-s1-b": round(W1 / 1e3, 2), "fy9-kaasut-s1-dV": round(dV1 * 1e3, 2), "fy9-kaasut-s1-dpdV": round(dp1 * dV1 / 1e3, 2),
            "fy9-kaasut-s1-Wgas": round(Wgas / 1e3, 2), "fy9-kaasut-s1-Wair": round(p0 * dV1 / 1e3, 2),
            "fy9-kaasut-s1-c-total": round(pt2 / 1e3, 1), "fy9-kaasut-s1-c": round((pt2 - p0) / 1e3, 1),
            "fy9-kaasut-s1-drop": round(pc * dV1 / Vt / 1e3, 1), "fy9-kaasut-s1-pt3": round(pt3 / 1e3, 1), "fy9-kaasut-s1-x2": round(x2, 2)})

# s2: the farm's biomethane engine (example data)
q2, T2, pg2, M2, H2 = 52.0, 25 + K, 104e3, 16.0e-3, 50.0e6     # m^3/h, K, Pa, kg/mol, J/kg
n2 = pg2 * q2 / (R * T2)                 # mol per hour
mh2 = n2 * M2                            # kg per hour
P0 = mh2 * H2 / 3600                     # W fuel power
Pe = 0.36 * P0
Pw = P0 - Pe                             # heat the engine gives off
Ph = 0.75 * Pw                           # recovered
eta_kok = (Pe + Ph) / P0
out.update({"fy9-kaasut-s2-n": round(n2, 1), "fy9-kaasut-s2-a": round(mh2, 2), "fy9-kaasut-s2-b": round(Pe / 1e3, 1),
            "fy9-kaasut-s2-P0": round(P0 / 1e3, 1), "fy9-kaasut-s2-Ehour": round(mh2 * H2 / 1e6, 0),
            "fy9-kaasut-s2-Pw": round(Pw / 1e3, 1), "fy9-kaasut-s2-Ph": round(Ph / 1e3, 1), "fy9-kaasut-s2-c": round(100 * eta_kok, 1),
            "fy9-kaasut-s2-Celsius-n": round(pg2 * q2 / (R * 25), 0)})

# s3: air in a glass syringe in a water bath at the constant air pressure 101,3 kPa (invented data: V = 37,5 ml at
# 0 °C, proportional to the kelvin temperature, plus reading noise of about 0,15 ml; figures.py draws the same points)
TH = [5, 15, 25, 35, 45, 55, 65, 75]                       # °C
V = [38.2, 39.9, 41.1, 42.5, 43.8, 45.1, 46.5, 47.8]      # ml
k3, b3 = fit(TH, V)
k_read = (48.5 - 37.7) / (80 - 0)                          # ml/°C from two points of the drawn line
th0_fit, th0_read = -b3 / k3, -37.7 / k_read
# the steepest and the shallowest line that still pass through every reading range +-0,3 ml: through the range ends
# (15 °C; 39,6 ml)-(75 °C; 48,1 ml) and (5 °C; 38,5 ml)-(75 °C; 47,5 ml)
k_hi = (48.1 - 39.6) / (75 - 15); b_hi = 39.6 - k_hi * 15
k_lo = (47.5 - 38.5) / (75 - 5); b_lo = 38.5 - k_lo * 5
assert all(abs(v - (k * t + b)) <= 0.3 + 1e-9 for k, b in ((k_hi, b_hi), (k_lo, b_lo)) for t, v in zip(TH, V))
th0_hi, th0_lo = -b_hi / k_hi, -b_lo / k_lo                 # -264,5 and -294,4 °C
p3 = 101.3e3
n3 = p3 * k_read * 1e-6 / R                                 # mol
out.update({"fy9-kaasut-s3-k": round(k3, 4), "fy9-kaasut-s3-b0": round(b3, 2), "fy9-kaasut-s3-kread": round(k_read, 4),
            "fy9-kaasut-s3-b": round(th0_read, 0), "fy9-kaasut-s3-b-fit": round(th0_fit, 1),
            "fy9-kaasut-s3-th0-steep": round(th0_hi, 1), "fy9-kaasut-s3-th0-flat": round(th0_lo, 1), "fy9-kaasut-s3-mid": round((th0_hi + th0_lo) / 2, 1),
            "fy9-kaasut-s3-khi": round(k_hi, 4), "fy9-kaasut-s3-bhi": round(b_hi, 2), "fy9-kaasut-s3-klo": round(k_lo, 4), "fy9-kaasut-s3-blo": round(b_lo, 2),
            "fy9-kaasut-s3-dth0": round((th0_hi - th0_lo) / 2, 1),
            "fy9-kaasut-s3-c": round(n3 * 1e3, 3), "fy9-kaasut-s3-c-fit": round(p3 * k3 * 1e-6 / R * 1e3, 3),
            "fy9-kaasut-s3-c-point": round(p3 * 41.1e-6 / (R * (25 + K)) * 1e3, 3),
            "fy9-kaasut-s3-d-shift": round(-K * 1.5 / 37.5, 1)})

# s4: the inventor's ship (word task; the numbers of b)
Q1, W4 = 500.0, 30.0                     # kW from the sea, kW of work
out.update({"fy9-kaasut-s4-b": round(100 * W4 / Q1, 1), "fy9-kaasut-s4-Q2": Q1 - W4})

# s5: the molar mass of air from weighing a bottle (example report)
m_before, m_after, dp5, V5, T5 = 52.36, 55.64, 210e3, 1.50e-3, 21 + K
dm5 = m_after - m_before                 # g
dn5 = dp5 * V5 / (R * T5)                # mol
M5 = dm5 / dn5                           # g/mol
T_warm = 30 + K                          # if the pumped air was still at 30 °C when the gauge was read
dn_warm = V5 / R * ((dp5 + p0) / T_warm - p0 / T5)
out.update({"fy9-kaasut-s5-a": round(M5, 2), "fy9-kaasut-s5-dm": round(dm5, 2), "fy9-kaasut-s5-dn": round(dn5, 4),
            "fy9-kaasut-s5-M-200": round(dm5 / (200e3 * V5 / (R * T5)), 1),
            "fy9-kaasut-s5-M-30C": round(dm5 / dn_warm, 1),
            "fy9-kaasut-s5-M-155": round(dm5 / (dp5 * 1.55e-3 / (R * T5)), 1),
            "fy9-kaasut-s5-dm-expected": round(29.0 * dn5, 2),
            "fy9-kaasut-s5-buoy": round(1.2 * 0.05, 2)})

# s6: the vacuum lifter and a glass pane (example data)
mg6 = 2.40 * 1.20 * 0.010 * 2500         # kg
A6 = math.pi * 0.150 ** 2                # m^2
a6, mu6, mu_wet = 1.2, 0.60, 0.30
dp_h = mg6 * (g + a6) / A6               # Pa, horizontal pane lifted with acceleration a
dp_v = mg6 * (g + a6) / (mu6 * A6)       # Pa, vertical pane, static friction holds it
dp_v_wet = mg6 * (g + a6) / (mu_wet * A6)
dp6 = 60e3
out.update({"fy9-kaasut-s6-m": round(mg6, 1), "fy9-kaasut-s6-A": round(A6, 5), "fy9-kaasut-s6-F": round(mg6 * (g + a6), 1),
            "fy9-kaasut-s6-a": round(dp_h / 1e3, 2), "fy9-kaasut-s6-b": round(dp_v / 1e3, 2),
            "fy9-kaasut-s6-Fp60": round(dp6 * A6, 0), "fy9-kaasut-s6-safe-h": round(dp6 / dp_h, 2),
            "fy9-kaasut-s6-safe-v": round(dp6 / dp_v, 2), "fy9-kaasut-s6-wet": round(dp_v_wet / 1e3, 1),
            "fy9-kaasut-s6-safe-wet": round(dp6 / dp_v_wet, 2)})

print(json.dumps(out))
