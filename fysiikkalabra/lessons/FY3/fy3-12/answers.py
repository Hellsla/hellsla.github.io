"""Every answer in exercises.json for fy3-12, computed from the task data (python -I answers.py).
Heat conducted through a building part P = UAΔT (U in W/(m²·K), A in m², ΔT in K); parallel parts add.
Energy E = Pt (kW · h = kWh, W · s = J), cost = price · E. Energy balance: absorbed power = emitted power.
Heating water (fy3-6): Q = cmΔT. Heat pump (fy3-11): electricity W = Q / lämpökerroin.
Prints {exercise id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json

a = {}
# Level 1: one formula, values given
dT_mokki = 22 - (-18)                                # cabin: ΔT = 22 °C − (−18 °C) = 40 K
a["fy3-12-L1-01"] = 0.24 * 45 * dT_mokki             # P = UAΔT = 0,24 · 45 · 40 = 432 W -> 430 W
dT_ovi = 21 - (-19)                                  # door: ΔT = 40 K
a["fy3-12-L1-02"] = 96 / (2.0 * dT_ovi)              # U = P/(AΔT) = 96 W / (2,0 m² · 40 K) = 1,2 W/(m²·K)
a["fy3-12-L1-03"] = 210 / (0.25 * 28)                # ΔT = P/(UA) = 210 W / (0,25 · 28 W/K) = 30 K
a["fy3-12-L1-04"] = 3.5 * 14                         # E = Pt = 3,5 kW · 14 h = 49 kWh
a["fy3-12-L1-05"] = 341 - 102                         # fy3-12/earth-flows: balance, emitted = absorbed = 341 − 102 = 239 W/m²
# Level 2: two steps, a conversion or a rearrangement
UA_mokki = 0.50 * 70 + 0.30 * 50                     # walls + ceiling in parallel: 35 + 15 = 50 W/K
dT_max = 2000 / UA_mokki                             # largest ΔT the 2,0 kW heaters can hold: 40 K
a["fy3-12-L2-01"] = 20 - dT_max                      # T_ulko = T_sisä − ΔT = 20 °C − 40 K = −20 °C
P_ylapohja = 0.090 * 130 * 21 / 1000                 # P = UAΔT = 245,7 W = 0,2457 kW
E_kausi = P_ylapohja * 230 * 24                      # E = Pt, t = 230 · 24 h = 5520 h -> 1356 kWh
a["fy3-12-L2-02"] = 0.11 * E_kausi                   # cost = 0,11 €/kWh · 1356 kWh = 149 € -> 150 €
dP_ikkuna = (2.8 - 0.80) * 14 * (21 - (-24)) / 1000  # power saved = (U_vanha − U_uusi)AΔT = 2,0 · 14 · 45 W = 1,26 kW
a["fy3-12-L2-03"] = dP_ikkuna * 7 * 24               # E = ΔP · t = 1,26 kW · 168 h = 211,7 kWh -> 210 kWh
a["fy3-12-L2-04"] = (1 - 0.29) * 340 - (1 - 0.30) * 340   # absorbed 241,4 − 238 = (0,30 − 0,29) · 340 = 3,4 W/m²
a["fy3-12-L2-05"] = 4190 * 0.25 * (73.0 - 69.0) / (10 * 60)   # P = cm(T_B − T_A)/t = 4190 J / 600 s = 6,98 W -> 7,0 W
a["fy3-12-L2-06"] = 1.0 * 1.6 * (21 - (-15))         # P = UAΔT, ΔT = 21 − (−15) = 36 K: 1,0 · 1,6 · 36 = 57,6 W -> 58 W
k_paneeli = (8.75 - 0) / (50.0 - 0)                  # slope of the fitted line through (0; 0) and (50,0 K; 8,75 W) = 0,175 W/K
a["fy3-12-L2-07"] = k_paneeli / 0.50                 # U = k/A = 0,175 W/K / 0,50 m² = 0,35 W/(m²·K)
# Level 3: reasoning, combining ideas, unfamiliar context
t_termos = 10 * 3600                                 # 10 h = 36 000 s
a["fy3-12-L3-01"] = 1.4 * t_termos / (4190 * 0.60)   # cmΔT = Pt -> ΔT = Pt/(cm) = 50 400 J / 2514 J/K = 20,0 K
t_vuosi = 365 * 24 * 3600                            # one year = 3,1536·10⁷ s
E_vuosi = 1.0 * 5.1e14 * t_vuosi                     # E = I·A·t = 1,0 W/m² · 5,1·10¹⁴ m² · 3,15·10⁷ s = 1,6·10²² J
Q_meri = 0.90 * E_vuosi * 10                         # 90 % of ten years' surplus goes into the sea: 1,45·10²³ J
a["fy3-12-L3-02"] = Q_meri / (4.0e3 * 2.6e20)        # ΔT = Q/(cm) = 1,45·10²³ J / 1,04·10²⁴ J/K = 0,139 K -> 0,14 K
Q_saasto = (0.35 - 0.10) * 100 * 19 * 5800 / 1000    # heat saved = (U₁ − U₂)AΔT·t = 475 W · 5800 h = 2755 kWh
a["fy3-12-L3-03"] = Q_saasto / 2.8                   # electricity saved = Q/lämpökerroin = 2755 kWh / 2,8 = 984 kWh -> 980 kWh
dA_jaa = (7.5 - 3.9) * 1e6 * 1e6                    # ice lost 1980–2020: 3,6·10⁶ km² = 3,6·10¹² m²
dP_jaa = 90 * dA_jaa * (0.60 - 0.06)                 # ΔP = I·ΔA·(a_jää − a_meri) = 1,75·10¹⁴ W
a["fy3-12-L3-04"] = dP_jaa / 5.1e14                  # per m² of the Earth: 0,343 W/m² -> 0,34 W/m²
S_pinta = 239 / (1 - 0.80 / 2)                       # top balance 239 = (1 − f)S + fS/2 -> S = 398,3 W/m²
assert abs(239 + 0.80 * S_pinta / 2 - S_pinta) < 1e-9   # surface balance 239 + fS/2 = S holds
T_pinta = 288 + (S_pinta - 390) / (478 - 390) * (303 - 288)   # interpolation between (288 K; 390) and (303 K; 478) = 289,4 K
a["fy3-12-L3-05"] = T_pinta - 273.15                 # 16,3 °C

# Added exercises (teacher 2026-11-12: MAFY table task, figure task)
a["fy3-12-L1-09"] = 0.14 / 0.20 * 10 * 30             # MAFY pine λ = 0,14 W/(m·K): U = λ/d = 0,70 W/(m²·K); P = UAΔT = 0,70 · 10 · 30 = 210 W
# Added exercises (teacher 2026-11-12: MAFY table task, figure task)
a["fy3-12-L2-09"] = 102 / 341 * 100                  # fy3-12/earth-flows: reflected share = 102 / 341 = 0,2991 -> 29,9 %
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
