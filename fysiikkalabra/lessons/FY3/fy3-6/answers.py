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
# L2-01 tea water: 160 g at 95 °C + 40 g at 8,0 °C, both water, so c cancels and grams need no conversion:
# c m1 (T1 − T) = c m2 (T − T2)  ->  T = (m1 T1 + m2 T2) / (m1 + m2) = (15 200 + 320) / 200 = 77,6 °C -> 78 °C
a["fy3-6-L2-01"] = (160 * 95 + 40 * 8.0) / (160 + 40)
a["fy3-6-L2-02"] = 100 * (180 - 0) / (0.50 * (60 - 20))  # figure fy3-6/heating-line: (0 s; 20 °C) to (180 s; 60 °C), c = P t/(m ΔT) = 18 000 J/(0,50 kg · 40 K) = 900 J/(kg·K)
dT_tank = 15e6 / (c_vesi * 80)                           # water heater: ΔT = Q / (c m) = 15 000 000 J / (4190 · 80 kg) = 44,75 K
a["fy3-6-L2-03"] = 9.0 + dT_tank                         # final temperature 9,0 °C + 44,75 K = 53,75 °C -> 54 °C
C_kauha = c_al * 0.25                                    # aluminium ladle: C = c m = 900 · 0,25 kg = 225 J/K, start 95 °C
C_kiulu = c_vesi * 0.40                                  # water in the bucket: C = 4190 · 0,40 kg = 1676 J/K, start 18 °C
a["fy3-6-L2-04"] = (C_kauha * 95 + C_kiulu * 18) / (C_kauha + C_kiulu)   # T = (21 375 + 30 168) J / 1901 J/K = 27,11 °C -> 27 °C
# Level 3: reasoning or an unfamiliar context
Q_tub = c_vesi * 20 * (40 - 10)                          # tub water receives 4190 · 20 kg · 30 K = 2 514 000 J
a["fy3-6-L3-01"] = Q_tub / (c_hiekka * (300 - 40))       # stones (c = 800) cool 300 -> 40 °C: m = Q / (c ΔT) = 12,09 kg -> 12 kg
a["fy3-6-L3-02"] = 18e6 / (c_vesi * 1000 * 1.2)          # lake bay: per m² the water column is 1,2 m³ = 1200 kg; ΔT = 18 MJ / (4190 · 1200) = 3,58 K (area cancels)
m_hiekka_per_m3 = 1600                                   # sand: 1600 kg per m³
a["fy3-6-L3-03"] = (c_vesi * 1000) / (c_hiekka * m_hiekka_per_m3)   # equal Q, same ΔT: V = (4190 · 1000) / (800 · 1600) m³ = 3,27 m³ -> 3,3 m³
# --- Added exercises (exercise bank) ---
a["fy3-6-L1-07"] = 15e3 / (c_kupari * 0.50)              # copper pot: ΔT = Q / (c m) = 15 000 J / (385 · 0,50 kg) = 77,9 K -> 78 K
C_alu = c_al * 0.60                                      # aluminium pan: C = c m = 900 · 0,60 kg = 540 J/K
a["fy3-6-L1-08"] = C_alu * (78 - 18) / 1e3               # Q = C ΔT = 540 J/K · 60 K = 32 400 J -> 32 kJ
dT_A = 38.1 - 20.0                                       # L2-06 liquid A after 120 s: 18,1 K
dT_B = 29.0 - 20.0                                       # liquid B (water) after 120 s: 9,0 K
a["fy3-6-L2-05"] = 100 * (300 - 0) / (0.50 * (34.5 - 20.0))   # table (0 s; 20,0 °C) to (300 s; 34,5 °C): c = P t/(m ΔT) = 30 000 J/(0,50 kg · 14,5 K) = 4138 J/(kg·K) -> 4100
a["fy3-6-L2-06"] = c_vesi * dT_B / dT_A                  # same Q and m: c_oil ΔT_A = c_water ΔT_B -> 4190 · 9,0/18,1 = 2083 J/(kg·K) -> 2100
C_k, C_v = c_kupari * 0.20, c_vesi * 0.50                # copper 77 J/K, water 2095 J/K
a["fy3-6-L2-07"] = (C_k * 100 + C_v * 20) / (C_k + C_v)  # T = 49 600 / 2172 = 22,84 °C -> 23 °C (the student's mean 60 °C is wrong)
a["fy3-6-L3-04"] = 200 - c_vesi * 0.50 * (63.6 - 56.8) / 120   # loss power 480–600 s: P − c m ΔT/t = 200 − 14 246/120 = 81,3 W -> 81 W
T5 = [90.0, 72.5, 59.6, 49.5, 42.3, 36.6, 32.5]          # L3-05 cooling water 0,300 kg, room 20,0 °C, 10 min steps
Q5 = c_vesi * 0.300 * (T5[0] - T5[1])                    # first interval: 4190 · 0,300 · 17,5 K = 21 997,5 J
a["fy3-6-L3-05"] = (Q5 / 600) / ((T5[0] + T5[1]) / 2 - 20.0)   # k = P / (T_ka − T_huone) = 36,66 W / 61,25 K = 0,599 W/K -> 0,60
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
