"""Every answer in exercises.json for fy3-15, computed from the task data (python -I answers.py).
Power-plant energy chain: stage efficiency η_k = P_k/P_(k-1), chain η = η₁·η₂·η₃ = P₃/P₀, waste power P_h = P₀ − P_hyöty.
CHP: kokonaishyötysuhde η_kok = (P_s + P_k)/P₀. Cooling water: P_h = c·q_m·ΔT (c = 4190 J/(kg·K)), q_m = m/t.
Prints {exercise id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json

a = {}
# Level 1: one formula, values given
a["fy3-15-L1-01"] = 0.920 * 0.980 * 100            # hydro: η = η_turbiini · η_generaattori = 0,920 · 0,980 = 0,9016 -> 90,2 %
a["fy3-15-L1-02"] = 1.05 / 2.50 * 100              # wind: η = P_sähkö/P_tuuli = 1,05 MW / 2,50 MW = 0,420 -> 42,0 %
a["fy3-15-L1-03"] = 0.210 * 1.00 * 20.0            # solar: P = η·I·A = 0,210 · 1,00 kW/m² · 20,0 m² = 4,20 kW
a["fy3-15-L1-04"] = 800 - 320                      # condensing: P_h = P₀ − P_s = 800 MW − 320 MW = 480 MW
a["fy3-15-L1-05"] = (75 + 150) / 250 * 100         # CHP: η_kok = (P_s + P_k)/P₀ = 225 MW / 250 MW = 0,900 -> 90 %
# Level 2: two steps or a conversion or a rearrangement
a["fy3-15-L2-01"] = 300 * 0.880 * 0.420 * 0.980    # peat plant: P₃ = η₁η₂η₃P₀ = 300 MW · 0,880 · 0,420 · 0,980 = 108,66 MW -> 109 MW
a["fy3-15-L2-02"] = 0.380 / (0.900 * 0.980) * 100  # η₂ = η/(η₁η₃) = 0,380 / (0,900 · 0,980) = 0,4308 -> 43,1 %
P0_hake = 150 / 0.360                              # wood chips: P₀ = P_s/η = 150 MW / 0,360 = 416,67 MW
qm_hake = P0_hake * 1e6 / 9.00e6                   # fuel mass flow = P₀/H = 416,67·10⁶ W / 9,00·10⁶ J/kg = 46,30 kg/s
a["fy3-15-L2-03"] = qm_hake * 3600 / 1000          # per hour: 46,30 kg/s · 3600 s = 166 700 kg = 166,7 t
a["fy3-15-L2-04"] = 270e6 / (4190 * 9.0) / 1000    # cooling water: q_m = P_h/(cΔT) = 270·10⁶ W / (4190 · 9,0) = 7160 kg/s = 7,16 t/s
# Level 3: reasoning, combining ideas, unfamiliar context
a["fy3-15-L3-01"] = 240 - (240 - 180) / 348 * 200  # CHP interpolation: P_s = 240 MW − (60/348)·200 MW = 205,5 MW
E_sahko = 36.0e9 * 3600                            # wind farm: 36,0 GWh = 36,0·10⁹ Wh · 3600 s/h = 1,296·10¹⁴ J
m_hiili = E_sahko / 0.380 / 25.0e6                 # coal: Q₁ = E/η = 3,411·10¹⁴ J, m = Q₁/H = 1,364·10⁷ kg
a["fy3-15-L3-02"] = m_hiili / 1e6                  # 1,364·10⁷ kg = 13,64 kt (1 kt = 10⁶ kg)
a["fy3-15-L3-03"] = 100 / (0.400 * 0.950 * 3.00)   # heat pump: fuel = Q/(η_voimala · η_siirto · ε) = 100 kWh / 1,14 = 87,7 kWh

print(json.dumps({k: round(v, 6) for k, v in a.items()}))
