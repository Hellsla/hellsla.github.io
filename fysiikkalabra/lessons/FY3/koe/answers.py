"""FY3 Esimerkkikoe: every number of the worked solutions, recomputed from the task data.
Prints {"<task>-<part>": value} for the parts with an answer in tasks.json; `python scripts/practice.py check FY3/koe` compares them."""
import json
from statistics import mean


def fit(xs, ys):
    """Least-squares line (k, b)."""
    xm, ym = mean(xs), mean(ys)
    k = sum((x - xm) * (y - ym) for x, y in zip(xs, ys)) / sum((x - xm) ** 2 for x in xs)
    return k, ym - k * xm


g, R, T0 = 9.81, 8.314, 273.15
out = {}
# fy3-k1: Osa 1 checks of the options that need a number
out["k1-a"] = round(2.50 * 1.62, 2)                          # N, weight on the Moon
out["k1-b"] = {"right": 40 * 3.0 + 0.5 * 40 * 2.0, "rect": 40 * 5.0, "const": 40 * 3.0, "avg": 0.5 * 40 * 5.0}   # J
out["k1-d"] = round(101e3 / (1000 * g), 1)                    # m of water for 101 kPa
out["k1-f"] = {m: round(1000 / (c * 1.0), 2) for m, c in (("Al", 900), ("Cu", 385), ("Pb", 130))}   # K per 1,0 kJ and 1,0 kg
out["k1-g"] = {"melt": 333, "boil": 2260, "ratio": round(2260 / 333, 1)}
out["k1-i"] = round(100 * ((40 + T0) / (20 + T0) - 1), 1)      # % pressure rise
# fy3-k2: the air column and absolute zero
TH2 = [5, 20, 35, 50, 65, 80]; L2 = [59.0, 62.5, 65.5, 68.5, 72.0, 75.0]   # degC, mm
k2fit, b2fit = fit(TH2, L2); out["k2-fit"] = (round(k2fit, 4), round(b2fit, 2), round(-b2fit / k2fit, 1))
k2 = (75.0 - 58.0) / (80 - 0)                                 # the drawn line through (0 degC; 58,0 mm) and (80 degC; 75,0 mm)
out["k2-k"] = k2
out["fy3-k2-b"] = round(0 - 58.0 / k2, 1)
out["fy3-k2-d"] = round(0 - (58.0 + 2.0) / k2, 1)             # every reading 2,0 mm too large: slope unchanged
out["k2-d-shift"] = round(2.0 / k2, 1)
# fy3-k3: the piston
m3, A3, p0, h1, t1, t2, Q3 = 12.0, 40.0e-4, 101e3, 0.250, 20.0, 80.0, 93.0
dp3 = m3 * g / A3; p3 = p0 + dp3; V1 = A3 * h1
n3 = p3 * V1 / (R * (t1 + T0))
out["k3-G"] = round(m3 * g, 2); out["k3-dp"] = round(dp3, 0)
out["fy3-k3-a-p"] = round(p3 / 1000, 1); out["fy3-k3-a-n"] = round(n3, 4)
h2 = h1 * (t2 + T0) / (t1 + T0); dh3 = h2 - h1
out["k3-h2"] = round(h2 * 100, 2); out["fy3-k3-b"] = round(dh3 * 100, 2)   # cm
W3 = p3 * A3 * dh3
out["k3-F"] = round(p3 * A3, 1); out["fy3-k3-c"] = round(W3, 1)
out["fy3-k3-d"] = round(Q3 - W3, 0)
out["k3-model"] = {"dU": round(2.5 * n3 * R * (t2 - t1), 1), "Q": round(3.5 * n3 * R * (t2 - t1), 1)}   # ideal diatomic gas
# fy3-k4: snow on a camping stove
m4, tS, cI, s4, cW = 1.20, -8.0, 2.09, 333.0, 4.19            # kg, degC, kJ/(kg K), kJ/kg
Q41 = cI * m4 * (0 - tS); Q42 = s4 * m4; Q43 = cW * m4 * 100
out["k4-parts"] = (round(Q41, 2), round(Q42, 1), round(Q43, 1))
Q4 = Q41 + Q42 + Q43; out["fy3-k4-a"] = round(Q4, 1)          # kJ
mf, H = (352 - 310) / 1000, 46e3                              # kg, kJ/kg
E4 = mf * H; out["k4-E"] = round(E4, 0)
out["fy3-k4-b"] = round(100 * Q4 / E4, 1)                     # %
etamin = 100 * Q4 / ((mf + 0.002) * H); etamax = 100 * Q4 / ((mf - 0.002) * H)
out["fy3-k4-c-min"] = round(etamin, 1); out["fy3-k4-c-max"] = round(etamax, 1)
out["k4-d"] = round(0.50 * (cI * 8.0 + s4 + cW * 37), 0)      # kJ to melt 0,50 kg of snow and warm it to 37 degC
# fy3-k5: the district heating pipe
alpha, L5, dT5 = 12e-6, 120.0, 115 - 10
out["fy3-k5-a"] = round(alpha * L5 * dT5 * 100, 2)             # cm
rho5, pP, pB, h5 = 947.0, 650e3, 169e3, 35.0
out["fy3-k5-c"] = round((pP - rho5 * g * h5) / 1000, 0)        # kPa
out["k5-c-dp"] = round(rho5 * g * h5 / 1000, 1)
out["fy3-k5-d"] = round((pP - pB) / (rho5 * g), 1)             # m
# fy3-k6: melting ice with an immersion heater
T6 = list(range(0, 14)); TH6 = [0.1, 0.1, 0.2, 0.2, 0.2, 0.3, 0.3, 0.6, 3.4, 11.2, 19.1, 27.3, 35.0, 42.9]
k6fit, b6fit = fit(T6[9:], TH6[9:]); out["k6-fit"] = (round(k6fit, 3), round(b6fit, 2), round((0.2 - b6fit) / k6fit, 2))
k6 = (42.9 - 11.2) / (13.0 - 9.0)                             # the drawn line through (9,0 min; 11,2 degC) and (13,0 min; 42,9 degC)
t6 = 9.0 - (11.2 - 0.2) / k6                                  # where it meets the plateau 0,2 degC
out["k6-k"] = round(k6, 3); out["k6-t"] = round(t6, 2)
mi6, mw6, c6 = 0.400, 0.100, 4190.0
P6 = c6 * (mi6 + mw6) * k6 / 60
out["fy3-k6-c"] = round(P6, 1)                                # W
out["fy3-k6-d"] = round(P6 * t6 * 60 / mi6 / 1000, 1)         # kJ/kg
out["k6-e-dev"] = round(100 * (P6 * t6 * 60 / mi6 / 1000 - 333) / 333, 1)
# fy3-k7: heating an old house
UA = 140 * 0.40 + 100 * 0.25 + 20 * 2.0; dT7, h7, vent = 21 - 1.0, 5100, 8000.0
out["k7-UA"] = UA
P7 = UA * dT7; out["fy3-k7-a"] = round(P7, 0)                 # W
Q7 = P7 * h7 / 1000 + vent                                    # kWh
out["fy3-k7-b-Q"] = round(Q7 / 1000, 2); out["fy3-k7-b-E"] = round(Q7 / 3.0 / 1000, 2)   # MWh
dE7 = 20 * (2.0 - 0.90) * dT7 * h7 / 1000                     # kWh of heat a year
out["k7-d-heat"] = round(dE7, 0)
out["fy3-k7-d-E"] = round(dE7 / 3.0, 0); out["fy3-k7-d-eur"] = round(dE7 / 3.0 * 0.15, 0)
out["k7-d-years"] = round(9000 / (dE7 / 3.0 * 0.15), 0)
fuel_hp = 1.0 / 3.0 / 0.40 * 3600; fuel_oil = 1.0 / 0.90 * 3600   # MJ of fuel per 1,0 MWh of heat
out["k7-e-fuel"] = (round(fuel_hp, 0), round(fuel_oil, 0))
out["fy3-k7-e-pumppu"] = round(fuel_hp * 94.6 / 1000, 0); out["fy3-k7-e-oljy"] = round(fuel_oil * 74.1 / 1000, 0)   # kg CO2
print(json.dumps(out))
