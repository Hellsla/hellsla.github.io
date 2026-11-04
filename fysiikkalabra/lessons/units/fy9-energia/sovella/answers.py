"""FY9 fy9-energia, Tehtävät: every number of the worked solutions, recomputed from the task data.
Prints {"<task>-<part>[-<name>]": value} for the parts with an answer in tasks.json and the intermediate values the
solutions quote; `python scripts/practice.py check units/fy9-energia` compares them with tasks.json."""
import json, math

g = 9.81
kWh = 1000 * 3600                     # J, by substitution: 1 kWh = 1000 W * 3600 s

def fit(x, y):
    mx, my = sum(x) / len(x), sum(y) / len(y)
    k = sum((a - mx) * (b - my) for a, b in zip(x, y)) / sum((a - mx) ** 2 for a in x)
    return k, my - k * mx

out = {}

# s1: the cottage's solar panels, battery and inverter (example data)
fridge = 45 * 24 / 1000               # kWh: mean power 45 W for 24 h
leds = 6 * 7.0 * 5.0 / 1000           # kWh: six 7,0 W lamps for 5,0 h
coffee = 1.0 * 15 / 60                # kWh: 1,0 kW for 15 min = 0,25 h
need = fridge + leds + coffee         # 1,54 kWh
eta_bat, eta_inv = 0.90, 0.93
panel = need / (eta_bat * eta_inv)    # 1,84 kWh from the panels
cloudy_use = 1.5 * eta_bat * eta_inv  # 1,26 kWh reach the loads on a cloudy day
full_h = 5.4 / 1.2                    # h at nominal power on the sunny day
out.update({"fy9-energia-s1-a": round(need, 3), "fy9-energia-s1-fridge": fridge, "fy9-energia-s1-leds": round(leds, 3),
            "fy9-energia-s1-coffee": coffee, "fy9-energia-s1-b": round(panel, 3), "fy9-energia-s1-eta": round(eta_bat * eta_inv, 4),
            "fy9-energia-s1-cloudy": round(cloudy_use, 3), "fy9-energia-s1-fullh": full_h, "fy9-energia-s1-sunny-use": round(5.4 * eta_bat * eta_inv, 2)})

# s2: the wood-chip CHP plant (example data)
H, mh, Ps, Pk = 9.5e6, 42e3, 30.0, 70.0      # J/kg, kg per hour, MW, MW
P0 = H * mh / 3600 / 1e6                      # MW
eta_s, eta_kok = Ps / P0, (Ps + Pk) / P0
P0_sep = Ps / 0.38 + Pk / 0.90                # MW: condensing plant + heat-only boiler
m_sep = P0_sep * 1e6 * 3600 / H / 1000        # t per hour
out.update({"fy9-energia-s2-a": round(P0, 2), "fy9-energia-s2-E-hour": H * mh / 1e9, "fy9-energia-s2-b-s": round(100 * eta_s, 2),
            "fy9-energia-s2-b-kok": round(100 * eta_kok, 2), "fy9-energia-s2-loss": round(P0 - Ps - Pk, 2),
            "fy9-energia-s2-c": round(m_sep, 2), "fy9-energia-s2-P0sep": round(P0_sep, 2), "fy9-energia-s2-Pcond": round(Ps / 0.38, 2),
            "fy9-energia-s2-Pboil": round(Pk / 0.90, 2), "fy9-energia-s2-saving": round(1 - 42 / m_sep, 3)})

# s3: daily electricity of a house with direct electric heating against the outdoor temperature (invented data:
# 12 kWh of other use + 4,8 kWh per kelvin below 17 °C, plus noise of about 3 kWh; figures.py draws the same points)
T = [-4, -10, -16, -19, -13, -7, -1, 2]               # °C, the table's order (7.–14.1.)
E = [112, 139, 174, 186, 155, 126, 100, 83]          # kWh per day
k, b = fit(T, E)
# the slope as read in the solution from two far-apart points of the drawn line: (-20 °C; 191 kWh) and (0 °C; 93 kWh)
k_read = (93 - 191) / (0 - (-20))
heat = -k / 24 * 1000                                # W/K: kWh per day and kelvin -> kW -> W
out.update({"fy9-energia-s3-k": round(k, 3), "fy9-energia-s3-b0": round(b, 2), "fy9-energia-s3-kread": k_read,
            "fy9-energia-s3-b": round(heat, 1), "fy9-energia-s3-bread": round(-k_read / 24 * 1000, 1),
            "fy9-energia-s3-c": round(b + k * (-28), 1), "fy9-energia-s3-c-cost": round(0.20 * (b + k * (-28)), 1),
            "fy9-energia-s3-Tbal": round((12 - b) / k, 2), "fy9-energia-s3-line-20": round(b + k * (-20), 1),
            "fy9-energia-s3-line0": round(b, 1)})

# s4: the island (word task; the numbers its model answer quotes)
wind = 2 * 1.0 * 0.30 * 8760 / 1000                   # GWh a year from two 1,0 MW turbines at 30 % mean power
bat_h = 2.0 / 1.2                                     # h: a 2,0 MWh battery at the 1,2 MW winter peak
diesel = 700 * 3.0e6 / 1e6                            # t CO2 a year: 700 g/kWh * 3,0 GWh
cable = 3.0 / 0.97                                    # GWh to send from the mainland for 3,0 GWh to arrive
out.update({"fy9-energia-s4-wind": round(wind, 2), "fy9-energia-s4-bat-h": round(bat_h, 2), "fy9-energia-s4-diesel": diesel,
            "fy9-energia-s4-cable": round(cable, 3)})

# s5: the kettle report (example data)
c, m, T0, T1, P, t = 4190, 1.0, 15, 96, 2200, 3 * 60 + 5
Q = c * m * (T1 - T0); Ee = P * t
eta5 = Q / Ee
out.update({"fy9-energia-s5-a": round(100 * eta5, 2), "fy9-energia-s5-Q": Q, "fy9-energia-s5-E": Ee,
            "fy9-energia-s5-P2100": round(100 * Q / (2100 * t), 1), "fy9-energia-s5-m105": round(100 * c * 1.05 * (T1 - T0) / Ee, 1),
            "fy9-energia-s5-m095": round(100 * c * 0.95 * (T1 - T0) / Ee, 1), "fy9-energia-s5-T100": round(100 * c * m * (100 - T0) / Ee, 1)})

# s6: the pumped-storage plant in a closed mine (example data)
V, rho, h = 7.50e4, 1000, 1200.0
mw = rho * V
Ep = mw * g * h                                       # J
Ep_MWh = Ep / (1000 * kWh)
eta_t, eta_p, t6 = 0.88, 0.85, 6.0
E_out = eta_t * Ep_MWh
P_out = E_out / t6
E_in = Ep_MWh / eta_p
out.update({"fy9-energia-s6-a": round(Ep_MWh, 2), "fy9-energia-s6-EpJ": Ep, "fy9-energia-s6-m": mw,
            "fy9-energia-s6-b": round(P_out, 2), "fy9-energia-s6-Eout": round(E_out, 1),
            "fy9-energia-s6-c-E": round(E_in, 1), "fy9-energia-s6-c-eta": round(100 * eta_t * eta_p, 2),
            "fy9-energia-s6-loss": round(E_in - E_out, 1)})

print(json.dumps(out))
