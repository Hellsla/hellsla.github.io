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

# s7 (FY9-A4): the winter range test of electric cars. Source: NAF and Motor, El Prix vinter 2026
# (https://www.naf.no/elbil/elprix-nytt/elprix-vinter-2026), checked 16.11.2026: stated (WLTP) and measured ranges in km
cars = {"inster": (360, 256), "tesla": (629, 359), "lucid": (960, 520)}
rel = {k: 100 * (m - s) / s for k, (s, m) in cars.items()}        # relative difference in per cent of the stated range
E7, s7, cut = 75.0, 450.0, 0.38                                    # kWh, km, the test's mean loss of range
E100 = E7 * 100 / s7                                               # kWh per 100 km in mild weather
s_cold = (1 - cut) * s7                                            # km
E100_cold = E7 * 100 / s_cold                                      # kWh per 100 km, the same usable energy assumed
F7 = E7 * kWh / (s7 * 1000)                                        # N: energy per distance is a force (W = Fs)
heat7 = 3.0 * 5.0                                                  # kWh: an example heater, 3,0 kW for 5,0 h
rho_ratio = (273.15 + 20) / (273.15 - 20)                          # n/V = p/(RT): -20 °C against +20 °C at the same pressure
out.update({"fy9-energia-s7-a-inster": round(rel["inster"], 2), "fy9-energia-s7-a-tesla": round(rel["tesla"], 2),
            "fy9-energia-s7-a-lucid": round(rel["lucid"], 2), "fy9-energia-s7-a-mean": round(-sum(rel.values()) / 3, 2),
            "fy9-energia-s7-a-wrong": round(100 * 104 / 256, 1),
            "fy9-energia-s7-b-E100": round(E100, 2), "fy9-energia-s7-b-range": round(s_cold, 1),
            "fy9-energia-s7-b-E100k": round(E100_cold, 2), "fy9-energia-s7-b-factor": round(1 / (1 - cut), 3),
            "fy9-energia-s7-b-force": round(F7, 1), "fy9-energia-s7-b-wrong": round(E100 * 1.38, 1),
            "fy9-energia-s7-c-dT-oslo": 20 - (-7), "fy9-energia-s7-c-dT-folldal": 20 - (-32),
            "fy9-energia-s7-c-dT-ratio": round((20 + 32) / (20 + 7), 2), "fy9-energia-s7-c-heat": heat7,
            "fy9-energia-s7-c-heat-share": round(heat7 / E7, 2), "fy9-energia-s7-c-density": round(100 * (rho_ratio - 1), 1)})

# s8: a skater on a half-pipe with friction (fy2-1/kitka-pylvaat; values read from the graph): (E_p, E_k) in J at A, B, C
m8, s8path = 45.0, 3.4                                            # kg, m (path from A to C along the track)
A8, B8, C8 = (700.0, 0.0), (300.0, 300.0), (0.0, 500.0)
Em8 = [sum(P) for P in (A8, B8, C8)]                              # J: mechanical energies 700, 600, 500
dB8, dC8 = Em8[0] - Em8[1], Em8[0] - Em8[2]                       # J: internal energy gained from A to B and to C
v8 = math.sqrt(2 * C8[1] / m8)                                    # m/s: E_k = 1/2 m v^2 at C
F8 = dC8 / s8path                                                 # N: internal energy gained = F s
G8 = m8 * g                                                       # N: weight
v8_0 = math.sqrt(2 * A8[0] / m8)                                  # m/s: no friction, E_p(A) -> E_k(C)
out.update({"fy9-energia-s8-a-dB": dB8, "fy9-energia-s8-a-dC": dC8, "fy9-energia-s8-b": round(v8, 3),
            "fy9-energia-s8-c": round(F8, 2), "fy9-energia-s8-c-weight": round(G8, 1), "fy9-energia-s8-c-share": round(100 * F8 / G8, 1),
            "fy9-energia-s8-d": round(v8_0, 3), "fy9-energia-s8-d-diff": round(v8_0 - v8, 2),
            "fy9-energia-s8-d-share": round(100 * dC8 / Em8[0], 1)})

# s9: two electrical devices on an energy meter (fy2-3/graph-ab; values read from the graph): E(80 s) = 120 kJ and 40 kJ
EA9, EB9, T9 = 120e3, 40e3, 80.0                                  # J, J, s
PA9, PB9 = EA9 / T9, EB9 / T9                                     # W: slopes of the lines
price9, hours9, days9 = 0.16, 3.0, 30                             # EUR/kWh, h per day, days
kWhA, kWhB = PA9 / 1000 * hours9 * days9, PB9 / 1000 * hours9 * days9   # kWh in the 30 days
cA, cB = kWhA * price9, kWhB * price9                             # EUR
m9, h9 = 150.0, 20.0                                              # kg lifted, m: hoist motor B lifts the load in 80 s
Eu9 = m9 * g * h9                                                 # J: useful energy
eta9 = Eu9 / EB9
Pu9 = Eu9 / T9                                                    # W: useful power
Pl9 = PB9 - Pu9                                                   # W: power transferred to the surroundings as heat
out.update({"fy9-energia-s9-a-PA": PA9 / 1000, "fy9-energia-s9-a-PB": PB9 / 1000,
            "fy9-energia-s9-b-cA": round(cA, 2), "fy9-energia-s9-b-cB": round(cB, 2), "fy9-energia-s9-b-kWhA": kWhA, "fy9-energia-s9-b-kWhB": kWhB,
            "fy9-energia-s9-c": round(100 * eta9, 2), "fy9-energia-s9-c-Eu": round(Eu9, 0),
            "fy9-energia-s9-d": round(Pl9 / 1000, 3), "fy9-energia-s9-d-Pu": round(Pu9, 1), "fy9-energia-s9-d-Pl": round(Pl9, 1)})

print(json.dumps(out))
