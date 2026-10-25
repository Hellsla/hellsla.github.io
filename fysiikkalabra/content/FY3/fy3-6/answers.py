"""Every answer in exercises.json for fy3-6, computed from the task data (python -I answers.py).
Q = c m ΔT with c from the lesson's table; ΔT in K equals the difference of the celsius readings.
Prints {exercise id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json

c_vesi, c_jaa, c_al, c_hiekka, c_rauta, c_kupari = 4190, 2100, 900, 800, 450, 385   # J/(kg·K), lesson table
a = {}
# Level 1: one formula, values given
a["fy3-6-L1-01"] = c_vesi * 1.8 * (96 - 12) / 1e6        # coffee maker water heats: Q = 4190 · 1,8 kg · 84 K = 633 528 J -> 0,63 MJ
a["fy3-6-L1-02"] = c_rauta * 2.4 * (220 - 25) / 1e3      # cast-iron pan cools, heat released = 450 · 2,4 kg · 195 K = 210 600 J -> 210 kJ
a["fy3-6-L1-03"] = c_hiekka * 50 * (32 - 14) / 1e3       # beach sand heats: Q = 800 · 50 kg · 18 K = 720 000 J = 720 kJ
a["fy3-6-L1-04"] = c_vesi * 1200 * (31 - 38) / 1e6       # hot tub (palju) cools: Q = 4190 · 1200 kg · (−7 K) = −35 196 000 J -> −35 MJ
a["fy3-6-L1-05"] = c_jaa * 0.50 * (-4.0 - (-22)) / 1e3   # ice pack warms −22 -> −4,0 °C: Q = 2100 · 0,50 kg · 18 K = 18 900 J -> 19 kJ
# Level 2: two steps, one conversion or one rearrangement
a["fy3-6-L2-01"] = c_al * (450 / 1000) * (180 - 20) / 1e3   # 450 g = 0,450 kg; Q = 900 · 0,450 · 160 = 64 800 J -> 65 kJ
Q_kettle = c_vesi * 1.5 * (95 - 15)                      # kettle water: Q = 4190 · 1,5 kg · 80 K = 502 800 J
a["fy3-6-L2-02"] = Q_kettle / 2.4e3                      # P t = Q -> t = 502 800 J / 2400 W = 209,5 s -> 210 s
dT_tank = 15e6 / (c_vesi * 80)                           # water heater: ΔT = Q / (c m) = 15 000 000 J / (4190 · 80 kg) = 44,75 K
a["fy3-6-L2-03"] = 9.0 + dT_tank                         # final temperature 9,0 °C + 44,75 K = 53,75 °C -> 54 °C
a["fy3-6-L2-04"] = 172.8e3 / (3.2 * (140 - 20))         # fireplace door: c = Q / (m ΔT) = 172 800 J / (3,2 kg · 120 K) = 450 -> iron
# Level 3: reasoning or an unfamiliar context
Q_tub = c_vesi * 20 * (40 - 10)                          # tub water receives 4190 · 20 kg · 30 K = 2 514 000 J
a["fy3-6-L3-01"] = Q_tub / (c_hiekka * (300 - 40))       # stones (c = 800) cool 300 -> 40 °C: m = Q / (c ΔT) = 12,09 kg -> 12 kg
a["fy3-6-L3-02"] = 18e6 / (c_vesi * 1000 * 1.2)          # lake bay: per m² the water column is 1,2 m³ = 1200 kg; ΔT = 18 MJ / (4190 · 1200) = 3,58 K (area cancels)
m_hiekka_per_m3 = 1600                                   # sand: 1600 kg per m³
a["fy3-6-L3-03"] = (c_vesi * 1000) / (c_hiekka * m_hiekka_per_m3)   # equal Q, same ΔT: V = (4190 · 1000) / (800 · 1600) m³ = 3,27 m³ -> 3,3 m³
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
