"""Every answer in exercises.json for fy3-16, computed from the task data (python -I answers.py).
Energy bookkeeping: Q = c m ΔT, Q = s m, Q = r m, P = U A ΔT, P = c (m/t) ΔT. Prints {id: number} as JSON on the last line."""
import json

c_vesi, c_jaa, c_kivi, c_neste = 4190, 2100, 800, 3500   # J/(kg·K): water, ice, sauna stones, glycol-water coolant (given in the tasks)
s, r = 334e3, 2260e3                                      # J/kg: melting and vaporization of water
a = {}
# Level 1: one formula, values given
a["fy3-16-L1-01"] = c_kivi * 20 * (300 - 20) / 1e6        # sauna stones: Q = 800 · 20 kg · 280 K = 4 480 000 J -> 4,5 MJ
a["fy3-16-L1-02"] = r * 0.20 / 1e3                        # löyly: Q = r m = 2 260 000 · 0,20 kg = 452 000 J -> 450 kJ
UA1 = 1.6 * 0.60                                          # cooler bag: U A = 1,6 · 0,60 = 0,96 W/K
a["fy3-16-L1-03"] = UA1 * (30 - 2.0)                      # P = 0,96 · 28 K = 26,88 W -> 27 W
a["fy3-16-L1-04"] = s * 0.75 / 1e3                        # ice pack melts: Q = s m = 334 000 · 0,75 = 250 500 J -> 250 kJ
a["fy3-16-L1-05"] = c_neste * 0.50 * 8.0 / 1e3            # coolant: P = c (m/t) ΔT = 3500 · 0,50 · 8,0 = 14 000 W -> 14 kW
# Level 2: two steps, one conversion or one rearrangement
UA2 = 2.0 * 0.50                                          # U A = 2,0 · 0,50 = 1,0 W/K; ΔT = 25 K
P2 = UA2 * 25                                             # P = 25 W
a["fy3-16-L2-01"] = P2 * 6.0 * 3600 / s                   # P t = s m -> m = 25 · 21 600 / 334 000 = 1,617 kg -> 1,6 kg
a["fy3-16-L2-02"] = (c_vesi * 0.25 * (100 - 20) + r * 0.25) / 1e3   # 83 800 + 565 000 = 648 800 J -> 650 kJ
a["fy3-16-L2-03"] = 24e3 / (c_neste * 8.0)                # m/t = P / (c ΔT) = 24 000 / (3500 · 8,0) = 0,857 kg/s -> 0,86 kg/s
a["fy3-16-L2-04"] = c_vesi * 0.33 * 22 / s * 1e3          # melted ice m = c m_j ΔT / s = 4190 · 0,33 · 22 / 334 000 = 0,0911 kg -> 91 g
# Level 3: reasoning or an unfamiliar context
Q_loyly = 0.20 * (c_vesi * 80 + r)               # 0,20 kg water 20 -> 100 °C and boiled: 0,20 · (335 200 + 2 260 000) = 519 040 J
a["fy3-16-L3-01"] = Q_loyly / (c_kivi * 25)               # stones lose it: ΔT = Q / (c m) = 519 040 / (800 · 25) = 25,95 K -> 26 K
# 0,50 kg ice (0 °C) in 2,0 kg water (30 °C): does all ice melt? water gives at most 4190·2,0·30 = 251 400 J > s·0,50 = 167 000 J: yes
# c_v 2,0 (30 - T) = s 0,50 + c_v 0,50 T  ->  T = (c_v 2,0 · 30 - s 0,50) / (c_v (2,0 + 0,50)) = 84 400 / 10 475 = 8,057 °C
a["fy3-16-L3-02"] = (c_vesi * 2.0 * 30 - s * 0.50) / (c_vesi * 2.5)
UA3 = 1.5 * 0.50                                          # bag U A = 1,5 · 0,50 = 0,75 W/K, outside 30 °C -> P = 22,5 W
E_wall = UA3 * 30 * 6.0 * 3600                            # wall energy in 6,0 h: 22,5 · 21 600 = 486 000 J
E_drinks = c_vesi * 0.50 * 24                             # 0,50 kg drinks 24 -> 0 °C: 4190 · 0,50 · 24 = 50 280 J
# freezer ice at -10 °C must warm to 0 °C and melt: (c_ice 10 + s) per kg = 21 000 + 334 000 = 355 000 J/kg
a["fy3-16-L3-03"] = (E_wall + E_drinks) / (c_jaa * 10 + s)   # m = 536 280 / 355 000 = 1,511 kg -> 1,5 kg
# Exercise bank additions (teacher 2026-11-04): L1-06 and L1-07 are multiple choice (no number)
a["fy3-16-L1-08"] = c_vesi * 1.5 * (100 - 20) / 2000      # kettle: P t = c m ΔT -> t = 4190 · 1,5 · 80 / 2000 W = 251,4 s -> 250 s
Tk = [20, 112, 196, 275]                                  # data of L2-05: stone temperature at 0, 10, 20, 30 min (40 kg, 6,0 kW)
a["fy3-16-L2-05"] = c_kivi * 40 * (Tk[-1] - Tk[0]) / (6000 * 1800) * 100   # η = 800 · 40 · 255 / (6000 · 1800) = 8,16 MJ / 10,8 MJ = 75,6 % -> 76 %
xs, Es = [8, 2, -3, -8], [1210, 1790, 2340, 2790]         # data of L2-06: outdoor °C, monthly heating energy kWh
mx, mE = sum(xs) / 4, sum(Es) / 4
k6 = sum((x - mx) * (e - mE) for x, e in zip(xs, Es)) / sum((x - mx) ** 2 for x in xs)   # least-squares slope −99,8 kWh/K (read from the fitted line: −100)
a["fy3-16-L2-06"] = round(-k6 / 720 * 1000, 0)            # UA = 99,8 kWh/K / 720 h = 0,1386 kW/K = 139 W/K (tolerance 0,05)
UA7 = 1.4 * 0.70                                          # error analysis: ΔT = 26 K (not 299 K); UA = 0,98 W/K, P = 25,48 W
a["fy3-16-L2-07"] = s * 0.80 / (UA7 * 26) / 3600          # t = 267 200 J / 25,48 W = 10 487 s = 2,913 h -> 2,9 h
dT = [18 - T for T in (5, 0, -4, -9, -7, -3)]             # data of L3-04: 13, 18, 22, 27, 25, 21 K, sum 126 K
E_season = 0.060 * 720 * sum(dT)                          # E = UA t ΣΔT = 0,060 kW/K · 720 h · 126 K = 5443 kWh
cost_A = E_season * 0.15                                  # electricity 100 %: 816,5 €
cost_B = E_season / (0.70 * 15 / 3.6) * 0.18              # wood: 5443 / (0,70 · 4,167 kWh/kg) = 1866 kg · 0,18 = 335,9 €
a["fy3-16-L3-04"] = cost_A - cost_B                       # saving 480,6 € -> 480 € (tolerance 0,03)
m_ice = 1000 * 60 * 30 * 0.030                            # 0,030 m layer of WATER (rho 1000): 54 m³ -> 54 000 kg
Q_rink = m_ice * (c_vesi * 12 + s + c_jaa * 5.0)          # 2,715 + 18,04 + 0,567 GJ = 21,32 GJ
a["fy3-16-L3-05"] = Q_rink / (10 * 3600) / 1e3            # P = 21,32 GJ / 36 000 s = 592 kW -> 590 kW (tolerance 0,03)
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
