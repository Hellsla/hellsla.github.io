"""Every answer in exercises.json for fy3-8, computed from the task data (python -I answers.py).
ΔL = α L₀ ΔT (length), ΔV = γ V₀ ΔT (volume), γ ≈ 3α for a solid, L = L₀ + ΔL.
Prints {exercise id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json

# coefficients from the lesson tables, 1/K
a_teras, a_alumiini, a_kupari, a_lasi = 12e-6, 23e-6, 17e-6, 9.0e-6
g_vesi, g_bensiini = 0.21e-3, 0.95e-3
a = {}
# Level 1: one formula, values given
a["fy3-8-L1-01"] = a_teras * 6.0 * (55 - 15) * 1000          # steel gutter 6,0 m, 15 -> 55 °C: 12e-6 · 6,0 · 40 = 0,00288 m = 2,88 mm -> 2,9 mm
a["fy3-8-L1-02"] = a_alumiini * 50.0 * (-27 - 18) * 1000     # aluminium line 50,0 m, 18 -> −27 °C, ΔT = −45 K: ΔL = −0,05175 m = −51,75 mm -> −52 mm
a["fy3-8-L1-03"] = a_kupari * 500.0 * (100 - 0)              # copper tube 500,0 mm, 0 -> 100 °C: ΔL = 17e-6 · 500,0 mm · 100 = 0,85 mm (L = 500,85 mm, shown in the solution)
a["fy3-8-L1-04"] = g_vesi * 200 * (32 - 12)                  # 200 l summer-shower tank, 12 -> 32 °C: ΔV = 0,21e-3 · 200 l · 20 = 0,84 l
a["fy3-8-L1-05"] = a_lasi * 1.5 * (45 - 20) * 1000           # window glass 1,5 m, 20 -> 45 °C: 9,0e-6 · 1,5 · 25 = 0,0003375 m = 0,3375 mm -> 0,34 mm
# Level 2: two steps, one conversion or one rearrangement
a["fy3-8-L2-01"] = (50 / 1000) / (a_teras * (90 - 10))       # district-heating pipe: L₀ = ΔL / (α ΔT) = 0,050 m / (12e-6 · 80) = 52,08 m -> 52 m
gamma_teras = 3 * a_teras                                    # solid steel: γ ≈ 3α = 36e-6 1/K
a["fy3-8-L2-02"] = gamma_teras * (2.0 * 1000) * (20 - (-22)) # kettlebell 2,0 dm³ = 2000 cm³, −22 -> 20 °C: ΔV = 36e-6 · 2000 · 42 = 3,024 cm³ -> 3,0 cm³
dT_kisko = (7.2 / 1000) / (a_teras * 25.0)                   # rail gap closes when ΔL = 7,2 mm: ΔT = 0,0072 m / (12e-6 · 25,0 m) = 24 K
a["fy3-8-L2-03"] = 12 + dT_kisko                             # T = 12 °C + 24 K = 36 °C
a["fy3-8-L2-04"] = (3.0 / 1000) / (5.00 * (70 - 20)) / 1e-6   # figure fy3-8/length-graph: (20 °C; 0 mm) to (70 °C; 3,0 mm), α = ΔL / (L₀ ΔT) = 0,0030 m / (5,00 m · 50 K) = 12e-6 1/K -> steel
# Level 3: reasoning or an unfamiliar context
dT_rengas = (75.09 - 75.00) / (a_teras * 75.00)              # shrink fit: the hole must grow 0,09 mm, ΔT = 0,09 mm / (12e-6 · 75,00 mm) = 100 K
a["fy3-8-L3-01"] = 20 + dT_rengas                            # ring temperature T = 20 °C + 100 K = 120 °C
dT_liuska = 100 - 20                                         # thermostat bimetal, 20 -> 100 °C: ΔT = 80 K
a["fy3-8-L3-02"] = (a_kupari - a_teras) * 50.0 * dT_liuska * 1000   # difference (17 − 12)e-6 · 50,0 mm · 80 = 0,020 mm = 20 µm
dV_bensiini = g_bensiini * 20 * (35 - 10) * 1000             # 20 l = 20 000 cm³ petrol, 10 -> 35 °C: 0,95e-3 · 20 000 · 25 = 475 cm³
dV_kanisteri = 3 * a_teras * 20 * (35 - 10) * 1000           # steel can's inner volume grows like steel: 36e-6 · 20 000 · 25 = 18 cm³
a["fy3-8-L3-03"] = dV_bensiini - dV_kanisteri                # overflow 475 − 18 = 457 cm³ -> 460 cm³
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
