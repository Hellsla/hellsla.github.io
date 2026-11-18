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
            "fy9-kaasut-s2-Celsius-n": round(pg2 * q2 / (R * 25), 0),
            "fy9-kaasut-s2-waste": round((P0 - Pe - Ph) / 1e3, 1)})   # unrounded waste power, kW (the row shows 485 - 175 - 233)

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

# s7 (FY9-A5): where does the energy of a nuclear power plant go? Source: TVO, Olkiluoto 3, "Rakenne ja tekniset
# tiedot", table "OL3 tekniset tiedot" (https://www.tvo.fi/tuotanto/laitosyksikot/ol3/rakennejateknisettiedot.html),
# checked 16.11.2026: net electrical power about 1600 MW, reactor thermal power 4300 MW, total efficiency about 37 %,
# steam temperature 290 °C, sea-water flow 57 m^3/s, yearly electricity about 13 TWh
P1_7, Ps_7, qV7, th_steam = 4300.0, 1600.0, 57.0, 290.0   # MW, MW, m^3/s, °C (read from the source)
rho7, c7, th_sea = 1000.0, 4190.0, 10.0                    # kg/m^3 and J/(kg K) (the task's model of sea water), °C
eta7 = Ps_7 / P1_7                                         # efficiency
P2_7 = P1_7 - Ps_7                                         # MW, heat power given to the surroundings
E7_MWh = P2_7 * 24                                         # MWh in one day
E7_J = P2_7 * 1e6 * 24 * 3600                              # J in one day (Q2 of the solution)
Es7_MWh = Ps_7 * 24                                        # MWh of electricity in one day (check: the sum is P1 * 24 h)
dT7 = P2_7 * 1e6 / (c7 * rho7 * qV7)                       # K, warming of the sea water if it takes all of P2
m7 = rho7 * qV7                                            # kg of sea water per second
T1_7, T2_7 = th_steam + K, th_sea + K                      # K
out.update({"fy9-kaasut-s7-a": round(100 * eta7, 2), "fy9-kaasut-s7-b-P2": round(P2_7, 0),
            "fy9-kaasut-s7-b-Q2": round(E7_MWh / 1e3, 1), "fy9-kaasut-s7-b-Q2J": float("%.4g" % E7_J),
            "fy9-kaasut-s7-b-share": round(100 * P2_7 / P1_7, 1), "fy9-kaasut-s7-b-Es": round(Es7_MWh / 1e3, 1),
            "fy9-kaasut-s7-b-sum": round((E7_MWh + Es7_MWh) / 1e3, 1), "fy9-kaasut-s7-b-check": round(P1_7 * 24 / 1e3, 1),
            "fy9-kaasut-s7-b-year": round(Ps_7 * 8760 / 1e6, 1),
            "fy9-kaasut-s7-c": round(dT7, 2), "fy9-kaasut-s7-c-m": round(m7, 0), "fy9-kaasut-s7-c-flow": float("%.4g" % (c7 * rho7 * qV7)),
            "fy9-kaasut-s7-c-out": round(th_sea + dT7, 0),
            "fy9-kaasut-s7-c-per-kg": round(P2_7 * 1e6 / m7 / 1e3, 1),
            "fy9-kaasut-s7-c-all": round(P1_7 * 1e6 / (c7 * rho7 * qV7), 1),
            "fy9-kaasut-s7-d-T1": round(T1_7, 0), "fy9-kaasut-s7-d-T2": round(T2_7, 0), "fy9-kaasut-s7-d-dT": round(T1_7 - T2_7, 0),
            "fy9-kaasut-s7-d-ratio": round((T1_7 - T2_7) / T1_7, 2)})

# s8 (FY9 B figure task): fy3-10/pt-suorat, p(T) lines of two rigid vessels, V = 2,0 l each (values read from the graph):
# gas A (200 K; 50 kPa), (400 K; 100 kPa); gas B (200 K; 30 kPa), (400 K; 60 kPa)
V8 = 2.0e-3                                              # m^3
pA8, pB8, T8 = 100.0e3, 60.0e3, 400.0                    # Pa, Pa, K (the points at 400 K)
nA8 = pA8 * V8 / (R * T8)                                # mol
nB8 = pB8 * V8 / (R * T8)                                # mol
ratio8 = pB8 / pA8                                       # n_B / n_A at the same V and T
T8c = -20.0 + K                                          # K
p8c = pA8 * T8c / T8                                     # Pa: p/T constant (V and n constant)
p8c_check = nA8 * R * T8c / V8                           # Pa: from pV = nRT
out.update({"fy9-kaasut-s8-a": round(nA8, 4), "fy9-kaasut-s8-a-200": round(50.0e3 * V8 / (R * 200.0), 4),
            "fy9-kaasut-s8-b-nB": round(nB8, 4), "fy9-kaasut-s8-b": round(100 * (1 - ratio8), 1),
            "fy9-kaasut-s8-c-T": round(T8c, 2), "fy9-kaasut-s8-c": round(p8c / 1e3, 1),
            "fy9-kaasut-s8-c-check": round(p8c_check / 1e3, 1)})

# s9 (FY9 B figure task): fy3-11/pv-isobaari, constant pressure 250 kPa, V from 1,0 l to 4,0 l (values read from the graph)
p9, V9a, V9b, th9 = 250.0e3, 1.0e-3, 4.0e-3, 20.0       # Pa, m^3, m^3, °C (start temperature given in the task)
W9 = p9 * (V9b - V9a)                                    # J
T9a = th9 + K                                            # K
n9 = p9 * V9a / (R * T9a)                                # mol
T9b = p9 * V9b / (n9 * R)                                # K
T9b_check = T9a * V9b / V9a                              # K: Charles's law
out.update({"fy9-kaasut-s9-a": round(W9, 0), "fy9-kaasut-s9-b-T1": round(T9a, 2), "fy9-kaasut-s9-b": round(n9, 4),
            "fy9-kaasut-s9-c": round(T9b, 1), "fy9-kaasut-s9-c-check": round(T9b_check, 1),
            "fy9-kaasut-s9-c-th": round(T9b - K, 1), "fy9-kaasut-s9-c-dT": round(T9b - T9a, 1)})

print(json.dumps(out))
