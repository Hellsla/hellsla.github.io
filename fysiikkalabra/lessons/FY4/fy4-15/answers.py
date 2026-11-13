"""Every answer in exercises.json for fy4-15, computed from the task data (python -I answers.py).
g = 9,81 m/s², water 1000 kg/m³, air 1,25 kg/m³. Hydro: P = η ρ Q g h; wind: P = ½ η ρ A v³. Prints {id: number} as
JSON on the last line; the lint and the gate compare it with exercises.json.
L2-02 uses a real power curve: Vestas V82-1.65 MW, rotor 82 m, 758 kW at 8 m/s (NREL Turbine Archive, read 2026-10-30)."""
import json, math

g, rw, ra = 9.81, 1000.0, 1.25
a = {}
# Level 1: one formula, values given
a["fy4-15-L1-01"] = 0.900 * rw * 120 * g * 15.0 / 1e6        # P = ηρQgh = 15,89 MW
a["fy4-15-L1-02"] = 1000 * g * 24.0 / 1e3                    # E_p = mgh = 235,44 kJ
a["fy4-15-L1-03"] = 46.0 / 50.0 * 100                        # η = P_a/P_o = 92,0 %
a["fy4-15-L1-04"] = 0.5 * ra * 1500 * 8.0 ** 3 / 1e3         # P_tuuli = ½ρAv³ = 480 kW
a["fy4-15-L1-05"] = 3.00 * 6.00                              # E = Pt = 18,0 MWh
# Exercise bank additions (teacher 2026-11-04): L1-06 is multiple choice (no number)
a["fy4-15-L1-07"] = rw * 35.0 * g * 8.50 / 1e6                # P_o = ρQgh = 2,918 MW
a["fy4-15-L1-08"] = 0.5 * 2.50e3 * 12.0 ** 2 / 1e3            # E_k = ½mv² = 180 kJ
# Level 2: two steps, a conversion or a rearrangement
a["fy4-15-L2-01"] = 10.0e6 / (0.880 * rw * g * 12.0)         # Q = P/(ηρgh) = 96,56 m³/s
A82 = math.pi * (82 / 2) ** 2
a["fy4-15-L2-02"] = 758e3 / (0.5 * ra * A82 * 8.0 ** 3) * 100   # η = P/(½ρAv³) = 44,85 %
a["fy4-15-L2-03"] = 0.75 * rw * 0.850 * g * 6.5 / 1e3        # 850 l/s = 0,850 m³/s: P = 40,65 kW
a["fy4-15-L2-04"] = 0.800 * rw * 3.20 * g * 9.50 * 24.0 / 1e6   # P = 238,6 kW, E = Pt = 5,726 MWh
# Level 2 additions
tab = [(100, 1500), (340, 2200), (850, 1800), (1650, 1000), (2000, 700)]   # table of L2-05: P in kW, t in h per year
a["fy4-15-L2-05"] = round(sum(p * t for p, t in tab) / 1e6, 1)   # Σ P t = 5 478 000 kWh = 5,478 GWh -> 5,5
qs = [85, 120, 45, 30, 28, 40]                                # table of L2-06: Q in m³/s, April-September
a["fy4-15-L2-06"] = round(0.85 * rw * g * 9.0 * sum(qs) * 720 / 1e9, 0)   # η ρ g h ΣQ · 720 h = 18,80 GWh -> 19
a["fy4-15-L2-07"] = round(0.5 * 0.40 * ra * math.pi * 30 ** 2 * 7.0 ** 3 / 1e3, -1)   # error: v instead of v³; right P = 242,5 kW -> 240
# Level 3: reasoning, two ideas, an unfamiliar context
a["fy4-15-L3-01"] = (9.0 / 6.0) ** 3                         # same rotor and η: P ∝ v³: 3,375
a["fy4-15-L3-02"] = (162 / 82) ** 2                          # same wind and η: P ∝ A ∝ d²: 3,903
a["fy4-15-L3-03"] = 10.0 ** 2 / (2 * g)                      # ½mv² = mgh → h = v²/(2g) = 5,097 m
# Level 3 additions
tab3 = [(4, 80), (5, 155), (6, 275), (7, 425), (8, 650), (9, 905)]   # table of L3-04: v in m/s, P in kW
k = sum(p / v ** 3 for v, p in tab3) / len(tab3) * 1e3        # mean P/v³ = 1,252 kW s³/m³ = 1252 W s³/m³
a["fy4-15-L3-04"] = round(2 * k / (ra * math.pi * 40 ** 2) * 100, 0)   # η = 2k/(ρA) = 39,86 % -> 40 %
surplus = [40, 52, 62, 58, 48, 40]                            # table of L3-05: surplus power in MW, one hour each
a["fy4-15-L3-05"] = round(0.800 * sum(surplus) * 3.6e9 / (g * 85.0) / rw, -4)   # V = ηE/(gh ρ) = 1,036·10⁶ m³ -> 1,04·10⁶
# Additions 2026-11-12: MAFY lookup (L1-09) and two figure tasks on tehokayra-pisteet (L2-09, L2-10)
a["fy4-15-L1-09"] = 0.5 * 0.45 * 1.29 * math.pi * 41 ** 2 * 9.0 ** 3 / 1e3   # MAFY: air 1,29 kg/m³ at 0 °C; P = ½ηρAv³ = 1117 kW
a["fy4-15-L2-09"] = 511 * 120 / 1e3                          # read P(7 m/s) = 511 kW; E = Pt = 61 320 kWh = 61,3 MWh
a["fy4-15-L2-10"] = 1637 / 1017                              # read P(9) = 1017 kW, P(12) = 1637 kW: ratio 1,610
print(json.dumps(a))
