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
# Level 2: two steps, a conversion or a rearrangement
a["fy4-15-L2-01"] = 10.0e6 / (0.880 * rw * g * 12.0)         # Q = P/(ηρgh) = 96,56 m³/s
A82 = math.pi * (82 / 2) ** 2
a["fy4-15-L2-02"] = 758e3 / (0.5 * ra * A82 * 8.0 ** 3) * 100   # η = P/(½ρAv³) = 44,85 %
a["fy4-15-L2-03"] = 0.75 * rw * 0.850 * g * 6.5 / 1e3        # 850 l/s = 0,850 m³/s: P = 40,65 kW
a["fy4-15-L2-04"] = 0.800 * rw * 3.20 * g * 9.50 * 24.0 / 1e6   # P = 238,6 kW, E = Pt = 5,726 MWh
# Level 3: reasoning, two ideas, an unfamiliar context
a["fy4-15-L3-01"] = (9.0 / 6.0) ** 3                         # same rotor and η: P ∝ v³: 3,375
a["fy4-15-L3-02"] = (162 / 82) ** 2                          # same wind and η: P ∝ A ∝ d²: 3,903
a["fy4-15-L3-03"] = 10.0 ** 2 / (2 * g)                      # ½mv² = mgh → h = v²/(2g) = 5,097 m
print(json.dumps(a))
