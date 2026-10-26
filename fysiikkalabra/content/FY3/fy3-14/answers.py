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
a["fy3-14-L1-03"] = c_v * 0.30 * 20 / 1e3                # 0,30 kg water cools 20 -> 0 °C: Q = c m ΔT = 4190 · 0,30 · 20 = 25 140 J -> 25 kJ
a["fy3-14-L1-04"] = 60e3 / s * 1e3                       # 60 kJ melts m = Q / s = 60 000 / 334 000 = 0,1796 kg = 179,6 g (180 g)
a["fy3-14-L1-05"] = c_j * 0.20 * 12 / 1e3                # ice 0,20 kg warms −12 -> 0 °C: Q = c_j m ΔT = 2100 · 0,20 · 12 = 5040 J -> 5,0 kJ
# Level 2: two steps, one conversion or one rearrangement
Q_w = c_v * 0.35 * 30                                    # water cools 30 -> 0 °C: 4190 · 0,35 · 30 = 43 995 J
Q_m = s * 0.060                                          # melting all 0,060 kg ice: 334 000 · 0,060 = 20 040 J (< Q_w, so all melts)
a["fy3-14-L2-01"] = (Q_w - Q_m) / (c_v * (0.35 + 0.060))  # T = (43 995 − 20 040) / (4190 · 0,41) = 23 955 / 1717,9 = 13,94 °C -> 14 °C
a["fy3-14-L2-02"] = c_v * 0.30 * 18 / s * 1e3            # ice melted to cool 0,30 kg water 18 -> 0 °C: m = c m_v ΔT / s = 22 626 / 334 000 = 0,06774 kg = 67,7 g -> 68 g
Q_h = c_j * 0.40 * 10 + s * 0.40                         # ice −10 °C -> water 0 °C: 8400 J + 133 600 J = 142 000 J
a["fy3-14-L2-03"] = Q_h / 800                            # P t = Q -> t = 142 000 J / 800 W = 177,5 s -> 180 s
# calorimeter: c_v m_v (T_v − T) = s m_i + c_v m_i T  ->  s = c_v [m_v (T_v − T) − m_i T] / m_i
a["fy3-14-L2-04"] = c_v * (0.200 * (30.0 - 8.1) - 0.050 * 8.1) / 0.050 / 1e3   # 4190 · (4,38 − 0,405) / 0,050 = 333 105 J/kg -> 333 kJ/kg
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
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
