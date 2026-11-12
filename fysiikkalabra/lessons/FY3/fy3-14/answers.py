"""Every answer in exercises.json for fy3-14, computed from the task data (python -I answers.py).
Energy conservation in an insulated vessel: heat given off = heat taken in. Constants from the course tables:
c_vesi = 4190 J/(kg·K), c_jaa = 2100 J/(kg·K), s = 334 kJ/kg (water, 0 °C).
Prints {exercise id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json

c_v, c_j, s = 4190, 2100, 334e3   # J/(kg·K), J/(kg·K), J/kg
a = {}
# Level 1: one formula, values given
a["fy3-14-L1-01"] = s * 0.050 / 1e3                      # ice 0,050 kg melts at 0 °C: Q = s m = 334 000 · 0,050 = 16 700 J -> 16,7 kJ (17)
a["fy3-14-L1-02"] = s * 0.25 / 1e3                       # 0,25 kg water freezes at 0 °C: heat released = s m = 334 000 · 0,25 = 83 500 J -> 83,5 kJ (84)
Q_vb, Q_lb, Q_sb = 25e3, 5e3, 60e3                       # read off figure fy3-14/energy-bars: water gives 25 kJ, warming the ice needs 5 kJ, melting all 60 kJ
# 5 kJ <= 25 kJ < 5 kJ + 60 kJ: the ice warms to 0 °C, part of it melts, T = 0 °C; m_s = (Q_v − c_j m_j ΔT_j) / s
a["fy3-14-L1-03"] = (Q_vb - Q_lb) / s * 1e3               # (25 000 J − 5000 J) / 334 000 J/kg = 0,05988 kg = 59,9 g -> 60 g
a["fy3-14-L1-04"] = 60e3 / s * 1e3                       # 60 kJ melts m = Q / s = 60 000 / 334 000 = 0,1796 kg = 179,6 g (180 g)
a["fy3-14-L1-05"] = c_j * 0.20 * 12 / 1e3                # ice 0,20 kg warms −12 -> 0 °C: Q = c_j m ΔT = 2100 · 0,20 · 12 = 5040 J -> 5,0 kJ
a["fy3-14-L1-07"] = c_v * 0.20 * 25 / 1e3                # L1-06 and L1-08 are multiple choice; water 0,20 kg cools 25 -> 0 °C: Q = c_v m ΔT = 4190 · 0,20 · 25 = 20 950 J -> 21 kJ
# Level 2: two steps, one conversion or one rearrangement
Q_w = c_v * 0.35 * 30                                    # water cools 30 -> 0 °C: 4190 · 0,35 · 30 = 43 995 J
Q_m = s * 0.060                                          # melting all 0,060 kg ice: 334 000 · 0,060 = 20 040 J (< Q_w, so all melts)
a["fy3-14-L2-01"] = (Q_w - Q_m) / (c_v * (0.35 + 0.060))  # T = (43 995 − 20 040) / (4190 · 0,41) = 23 955 / 1717,9 = 13,94 °C -> 14 °C
a["fy3-14-L2-02"] = c_v * 0.30 * 18 / s * 1e3            # ice melted to cool 0,30 kg water 18 -> 0 °C: m = c m_v ΔT / s = 22 626 / 334 000 = 0,06774 kg = 67,7 g -> 68 g
Q_h = c_j * 0.40 * 10 + s * 0.40                         # ice −10 °C -> water 0 °C: 8400 J + 133 600 J = 142 000 J
a["fy3-14-L2-03"] = Q_h / 800                            # P t = Q -> t = 142 000 J / 800 W = 177,5 s -> 180 s
# calorimeter: c_v m_v (T_v − T) = s m_i + c_v m_i T  ->  s = c_v [m_v (T_v − T) − m_i T] / m_i
a["fy3-14-L2-04"] = c_v * (0.200 * (30.0 - 8.1) - 0.050 * 8.1) / 0.050 / 1e3   # 4190 · (4,38 − 0,405) / 0,050 = 333 105 J/kg -> 333 kJ/kg
a["fy3-14-L2-05"] = 150 / (133e-3 / 300) / 1e3           # table fit through (0 s; 0 g) and (300 s; 133 g): k = 0,4433 g/s; P t = s m -> s = P/k = 150 / 0,0004433 = 338 400 J/kg -> 338 kJ/kg
a["fy3-14-L2-06"] = (c_v * 0.30 * 20 - c_j * 0.15 * 15) / s * 1e3   # L2-07 is multiple choice; ice 0,15 kg at −15 °C warms first: (25 140 − 4725) / 334 000 = 0,06112 kg = 61,1 g -> 61 g
# Level 3: reasoning or an unfamiliar context
a["fy3-14-L3-01"] = c_v * 0.60 * 35 / (c_j * 20 + s) * 1e3   # all ice −20 °C melts, end 0 °C: m (c_j · 20 + s) = c_v m_v 35 -> 87 990 / 376 000 = 0,2340 kg = 234 g
Q_av = c_v * 0.20 * 15                                   # water 0,20 kg cools 15 -> 0 °C: 12 570 J
Q_wm = c_j * 0.30 * 10                                   # ice 0,30 kg warms −10 -> 0 °C: 6300 J (< Q_av: some ice melts, T = 0 °C)
melted = (Q_av - Q_wm) / s                               # (12 570 − 6300) / 334 000 = 0,01877 kg melted
a["fy3-14-L3-02"] = (0.30 - melted) * 1e3                # ice left = 0,30 kg − 0,01877 kg = 0,2812 kg = 281 g
# water 0,10 kg at 10 °C + ice 0,50 kg at −40 °C: water gives 4190 + 33 400 = 37 590 J down to ice at 0 °C, ice needs 2100 · 0,50 · 40 = 42 000 J
# to reach 0 °C, so all water freezes and everything ends below 0 °C:
# c_j m_j (T − T_j) = c_v m_v T_v + s m_v − c_j m_v T  ->  T = (c_v m_v T_v + s m_v + c_j m_j T_j) / (c_j (m_j + m_v))
a["fy3-14-L3-03"] = (c_v * 0.10 * 10 + s * 0.10 + c_j * 0.50 * (-40)) / (c_j * (0.50 + 0.10))   # (4190 + 33 400 − 42 000) / 1260 = −3,5 °C
# run 1 (ice 0,0 °C, T = 8,2 °C): s_1 = 4190 · (0,200 · 21,8 − 0,0500 · 8,2) / 0,0500 = 331 010 J/kg -> 331 kJ/kg
# run 2 (ice −18,0 °C, T = 6,2 °C): s = [c_v m_v (T_v − T) − c_v m_j T − c_j m_j ΔT_j] / m_j
a["fy3-14-L3-04"] = (c_v * 0.200 * (30.0 - 6.2) - c_v * 0.0500 * 6.2 - c_j * 0.0500 * 18.0) / 0.0500 / 1e3   # 4190 · 4,45 = 18 645,5 J; − 1890 J = 16 755,5 J; / 0,0500 = 335 110 J/kg -> 335 kJ/kg
# row T_v = 40 °C, T = 8,1 °C (all ice melted): Q_j = c_v m_v T_v − c_v (m_v + m_j) T = 50 280 − 13 575,6 = 36 704,4 J; ice just melts when c_v m_v T_v,min = Q_j
Q_jrow = c_v * 0.300 * 40 - c_v * 0.400 * 8.1
a["fy3-14-L3-05"] = Q_jrow / (c_v * 0.300)               # T_v,min = 36 704,4 / 1257 = 29,2 °C -> 29 °C (ice temperature (36 704 − 33 400)/210 = 15,7 K below 0 °C)
a["fy3-14-L1-09"] = 333 * 0.080                        # MAFY: s = 333 kJ/kg; Q = sm = 333 kJ/kg · 0,080 kg = 26,64 kJ
a["fy3-14-L2-09"] = (60.0 / 334 - (25.0 - 5.0) / 334) * 1000   # fy3-14/energy-bars: 25, 5, 60 kJ; ice in all 60/334 = 0,1796 kg, melted 20/334 = 0,0599 kg, left 0,1198 kg = 119,8 g
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
