"""Every answer in exercises.json for fy2-5, computed from the task data (python -I answers.py).
E = H m with H in MJ/kg (rounded table values of the lesson); hyötysuhde eta = E_hyöty : E_sisään.
Prints {exercise id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json

H = {"bensiini": 43, "diesel": 43, "maakaasu": 48, "kivihiili": 26, "turve": 10, "polttopuu": 15, "pelletti": 17}   # MJ/kg, lesson table
a = {}
# Level 1: E = H m, values given
a["fy2-5-L1-01"] = H["bensiini"] * 2.0                    # 43 MJ/kg · 2,0 kg = 86 MJ
a["fy2-5-L1-02"] = H["maakaasu"] * 2.0                    # 48 MJ/kg · 2,0 kg = 96 MJ
a["fy2-5-L1-03"] = H["kivihiili"] * 12000                  # 26 MJ/kg · 12 000 kg = 312 000 MJ -> 310 000 MJ
a["fy2-5-L1-04"] = H["turve"] * 400                       # 10 MJ/kg · 400 kg = 4000 MJ
a["fy2-5-L1-05"] = 24 * 0.040                             # 24 MJ/kg · 0,040 kg = 0,96 MJ
# Level 2: a conversion, a rearrangement, one efficiency
H_leipa = 1200 / 1000 / 0.100                             # label 1200 kJ per 100 g: 1,2 MJ : 0,100 kg = 12 MJ/kg
a["fy2-5-L2-01"] = H_leipa * 0.040 * 1000                 # 12 MJ/kg · 0,040 kg = 0,48 MJ = 480 kJ
a["fy2-5-L2-02"] = (1.8 * 1000) / H["diesel"]             # 1,8 GJ = 1800 MJ; m = E : H = 1800 : 43 = 41,86 kg -> 42 kg
E_pelletti = H["pelletti"] * 40                           # 17 · 40 = 680 MJ released
a["fy2-5-L2-03"] = 0.85 * E_pelletti                      # E_hyöty = eta · E_sisään = 0,85 · 680 = 578 MJ -> 580 MJ
E_in_auto = 48 / 0.25                                     # E_sisään = E_hyöty : eta = 48 MJ : 0,25 = 192 MJ
a["fy2-5-L2-04"] = E_in_auto / H["bensiini"]              # m = 192 : 43 = 4,465 kg -> 4,5 kg
# Level 3: comparison, two ideas, power plant
a["fy2-5-L3-01"] = 120 / H["polttopuu"] - 120 / 43          # m_puu = 120 : 15 = 8,0 kg; m_öljy = 120 : 43 = 2,79 kg; difference = 5,21 kg -> 5,2 kg
a["fy2-5-L3-02"] = (18 * 2.4) / 12                        # E = 18 · 2,4 = 43,2 MJ; 43,2 : 12 = 3,6 daily rations
E_h = H["turve"] * 36 * 1000                              # 36 t/h = 36 000 kg per hour: 360 000 MJ per hour
a["fy2-5-L3-03"] = 0.35 * E_h / 3600                      # E_hyöty = 126 000 MJ per 3600 s = 35 MJ/s = 35 MW
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
