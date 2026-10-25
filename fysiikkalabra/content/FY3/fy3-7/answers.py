"""Every answer in exercises.json for fy3-7, computed from the task data (python -I answers.py).
Q = s m (melting/freezing), Q = r m (boiling/condensing), Q = c m ΔT between them.
Prints {exercise id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json

s, r = 334e3, 2260e3                     # water: specific latent heats, J/kg (lesson)
c_vesi, c_jaa = 4190, 2100               # J/(kg·K): water, ice (fy3-6 table)
a = {}
# Level 1: one formula, values given
a["fy3-7-L1-01"] = s * 1.20 / 1e3                      # cool-box ice melts: Q = 334 kJ/kg · 1,20 kg = 400,8 kJ -> 401 kJ
a["fy3-7-L1-02"] = r * 0.40 / 1e6                      # potato pot boils off 0,40 kg: Q = 2260 kJ/kg · 0,40 kg = 904 kJ -> 0,90 MJ
a["fy3-7-L1-03"] = s * 45 / 1e6                        # lake water freezes, 45 kg per m², heat released = 334 kJ/kg · 45 kg = 15 030 kJ -> 15 MJ
a["fy3-7-L1-04"] = r * 0.030 / 1e3                     # milk-frother steam condenses: Q = 2260 kJ/kg · 0,030 kg = 67,8 kJ -> 68 kJ
a["fy3-7-L1-05"] = 186 - 19                            # heating curve: plateau at 0 °C runs from 19 kJ to 186 kJ -> melting takes 167 kJ
# Level 2: two steps, one conversion or one rearrangement
a["fy3-7-L2-01"] = r * 0.50 / 2.0e3 / 60               # hotplate: P t = r m -> t = 2260 kJ/kg · 0,50 kg / 2000 W = 565 s = 9,42 min -> 9,4 min
Q_jaa_lampenee = c_jaa * (750 / 1000) * (0 - (-18))     # 750 g = 0,750 kg ice warms −18 -> 0 °C: 2100 · 0,750 · 18 = 28 350 J
Q_jaa_sulaa = s * (750 / 1000)                          # then melts: 334 000 · 0,750 = 250 500 J
a["fy3-7-L2-02"] = (Q_jaa_lampenee + Q_jaa_sulaa) / 1e3  # total 278 850 J -> 280 kJ (2 sf from −18 °C)
a["fy3-7-L2-03"] = 12e6 / s                            # spring lake ice: m = Q / s = 12 000 000 J / 334 000 J/kg = 35,9 kg -> 36 kg
Q_kattila_lampenee = c_vesi * 2.0 * (100 - 15)          # pasta pot: 2,0 kg water heats 15 -> 100 °C: 4190 · 2,0 · 85 = 712 300 J
Q_kattila_kiehuu = r * 0.10                             # 0,10 kg boils away: 2 260 000 · 0,10 = 226 000 J
a["fy3-7-L2-04"] = (Q_kattila_lampenee + Q_kattila_kiehuu) / 1e6   # total 938 300 J -> 0,94 MJ
# Level 3: reasoning or an unfamiliar context
# Drink: 0,35 kg juice (c of water) at 25 °C, 60 g ice at 0 °C. Juice cools to T, ice melts, melt water warms 0 -> T:
# c m_j (25 − T) = s m_i + c m_i (T − 0)  ->  T = (c m_j · 25 − s m_i) / (c (m_j + m_i))
a["fy3-7-L3-01"] = (c_vesi * 0.35 * 25 - s * 0.060) / (c_vesi * (0.35 + 0.060))   # = 9,68 °C -> 9,7 °C
# Sauna: 0,25 kg löyly water at 20 °C heats to 100 °C and evaporates; energy from 30 kg of stones, c = 800 J/(kg·K)
Q_loyly = c_vesi * 0.25 * (100 - 20) + r * 0.25         # 83 800 J + 565 000 J = 648 800 J
a["fy3-7-L3-02"] = Q_loyly / (800 * 30)                  # stones cool ΔT = Q / (c m) = 648 800 / 24 000 = 27,0 K -> 27 K
# Snow at −20 °C to steam at 100 °C, per kilogram (mass cancels in the share)
Q_osat = [c_jaa * 1.0 * 20, s * 1.0, c_vesi * 1.0 * 100, r * 1.0]   # 42 000 + 334 000 + 419 000 + 2 260 000 J
a["fy3-7-L3-03"] = 100 * Q_osat[3] / sum(Q_osat)         # boiling share = 2 260 000 / 3 055 000 = 74,0 % -> 74 %
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
