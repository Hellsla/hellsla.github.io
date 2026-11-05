"""Every answer in exercises.json for fy8-11, computed from the task data (python -I answers.py).
Reaction energy Q = (m_before - m_after) c^2 from atomic masses in u, 1 u = 931,5 MeV/c^2; E = mc^2 with
c = 2,998e8 m/s; 1 u = 1,66054e-27 kg, 1 eV = 1,602e-19 J; chain reaction N_g = N_0 k^g; decay law (half-lives:
Pu-239 24 100 a). Atomic masses as given in the tasks (AME2020, rounded to 7 decimals).
Prints {exercise id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json, math

U_MEV, U_KG, EV, C = 931.5, 1.66054e-27, 1.602e-19, 2.998e8
m = {"n": 1.0086649, "H-1": 1.0078250, "H-2": 2.0141018, "H-3": 3.0160493, "He-3": 3.0160293, "He-4": 4.0026033, "Li-6": 6.0151229,
     "U-235": 235.0439282, "Xe-140": 139.9216458, "Sr-94": 93.9153556}
a = {}
# Level 1: one formula, values given
a["fy8-11-L1-01"] = (m["Li-6"] + m["n"] - m["He-4"] - m["H-3"]) * U_MEV      # Li-6 + n -> He-4 + T: 0,0051352 u -> 4,783 MeV
a["fy8-11-L1-02"] = 0.1915 * U_MEV                                             # mass decrease 0,1915 u: 178,38 MeV -> 178 MeV
a["fy8-11-L1-03"] = 1000 * 0.90 ** 10                                          # k = 0,90, N0 = 1000, 10 generations: 348,7 -> 349
a["fy8-11-L1-04"] = (2 * m["H-2"] - m["He-3"] - m["n"]) * U_MEV                # D + D -> He-3 + n: 0,0035094 u -> 3,269 MeV
a["fy8-11-L1-05"] = m["n"] * U_MEV                                            # rest energy of a neutron: 939,57 MeV -> 939,6 MeV
# Level 2: two steps, a conversion or a rearrangement
a["fy8-11-L2-01"] = 4300e6 * 365 * 24 * 3600 / C ** 2                          # OL3 4300 MW thermal, one year: dm = Pt/c^2 = 1,509 kg
dt = (m["H-2"] + m["H-3"] - m["He-4"] - m["n"]) * U_MEV * 1e6 * EV             # J per reaction
a["fy8-11-L2-02"] = dt / ((m["H-2"] + m["H-3"]) * U_KG) / 1e14                 # per kg of D-T fuel: 3,374e14 J/kg (unit 10^14 J/kg)
x_n = 235 + 1 - 140 - 94                                                       # neutrons: A conserved -> 2
a["fy8-11-L2-03"] = (m["U-235"] + m["n"] - m["Xe-140"] - m["Sr-94"] - x_n * m["n"]) * U_MEV   # 0,198262 u -> 184,7 MeV
a["fy8-11-L2-04"] = ((5000 / 1000) ** (1 / 40) - 1) * 100                      # 1000 -> 5000 in 40 generations: k = 1,0411, growth 4,11 %
# Level 3: reasoning or an unfamiliar context
P_th, Q_f = 4300e6, 200e6 * EV                                                 # W, J per fission
rate = P_th / Q_f                                                              # 1,342e20 fissions per second
a["fy8-11-L3-01"] = rate * 24 * 3600 * m["U-235"] * U_KG                        # U-235 fissioned per day: 4,53 kg -> 4,5 kg
Q_pp = (4 * m["H-1"] - m["He-4"]) * U_MEV * 1e6 * EV                            # 4 H-1 -> He-4: 26,73 MeV in J
a["fy8-11-L3-02"] = 3.83e26 / Q_pp / 1e37                                      # Sun 3,83e26 W: 8,95e37 He-4 per s (unit 10^37 1/s)
a["fy8-11-L3-03"] = 24100 * math.log2(1000) / 1e5                              # Pu-239 to 1/1000: 2,402e5 a (unit 10^5 a)
# Added exercises (MC L1-06, L1-07, L2-07 have no numeric answer)
a["fy8-11-L1-08"] = 200e6 * EV / 1e-11                                         # 200 MeV in J: 3,204e-11 J (unit 10^-11 J)
N_g = [1000, 1013, 1022, 1038, 1049, 1064]                                     # example data: neutrons per generation
k_n = (N_g[-1] / N_g[0]) ** (1 / 5)                                            # k from first and last value: 1,01248 (> 1, supercritical)
a["fy8-11-L2-05"] = N_g[0] * k_n ** 50                                         # same k to generation 50: 1859,6 -> 1860
P_fin = [890, 890, 1600, 507, 507]                                             # MW, net electric power of the five Finnish reactors (TVO:n ja Fortumin verkkosivut, tilanne 2024)
a["fy8-11-L2-06"] = 0.90 * sum(P_fin) * 365 * 24 / 1e6                         # capacity factor 0,90, 8760 h: 34,64 TWh
t_s, A_s = [0, 10, 20, 30, 40, 50], [30000, 23900, 19250, 15050, 11950, 9650]  # example data: activity (TBq/t) of spent fuel, t from ~10 a after discharge
y_s = [math.log(v) for v in A_s]                                               # least squares of ln A against t (standard library only)
mt, my = sum(t_s) / 6, sum(y_s) / 6
slope = sum((x - mt) * (y - my) for x, y in zip(t_s, y_s)) / sum((x - mt) ** 2 for x in t_s)   # -lambda = -0,02285 1/a
ln_A0 = my - slope * mt                                                        # ln A0 = 10,311 -> A0 = 30060 TBq/t
a["fy8-11-L3-04"] = (ln_A0 - math.log(100)) / -slope                           # time to 100 TBq/t: 249,7 a (T_1/2 = 30,3 a)
P_el, eta, E_th = 507e6, 0.33, 507e6 / 0.33 * 0.92 * 365 * 24 * 3600           # Loviisa unit: P_th = 1536 MW, 92 % of 365 d: 4,457e16 J
a["fy8-11-L3-05"] = E_th / Q_f * m["U-235"] * U_KG                              # fissions 1,391e27 x 3,903e-25 kg = 543,0 kg U-235 per year (stored 540: two significant figures)
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
