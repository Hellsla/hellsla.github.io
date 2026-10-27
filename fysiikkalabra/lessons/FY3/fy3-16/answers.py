"""Every answer in exercises.json and the numeric activities of inquiry.json for fy3-16, computed from the task data (python -I answers.py).
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
# Inquiry numerics
P_tut = 0.90 * 28                                         # tutki graph: U A = 0,90 W/K, ΔT = 28 K -> P = 25,2 W, plateau t = 334 000 / 25,2 = 13 254 s = 3,68 h
a["tutki-energia"] = 25 * 3.7 * 3600 / 1e3                # E = P t = 25 W · 13 320 s = 333 000 J -> 333 kJ
a["tutki-loyly"] = r * 0.25 / (0.25 * (c_vesi * 90 + r)) * 100   # löyly 0,25 kg, 10 -> 100 °C: 94 275 J + 565 000 J; vaporization share 565 000 / 659 275 = 85,7 % -> 86 %
a["siirto"] = 0.15 * (c_vesi * 80 + r) / 6000             # 0,15 kg löyly, 6,0 kW: t = 0,15 (335 200 + 2 260 000) / 6000 = 64,9 s -> 65 s
a["siirto-virhe-ei-hoyrystysta"] = 0.15 * c_vesi * 80 / 6000   # 8,4 s: vaporization forgotten
a["siirto-virhe-ei-lammitysta"] = 0.15 * r / 6000          # 56,5 s: warming 20 -> 100 °C forgotten
a["check-2"] = (c_jaa * 0.60 * 10 + s * 0.60) / 1e3       # ice pack -10 °C -> water 0 °C: 12 600 + 200 400 = 213 000 J -> 210 kJ
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
