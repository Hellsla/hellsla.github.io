"""Every answer in exercises.json for fy2-1, computed from the task data (python -I answers.py).
Energy balance of an isolated system: E_alussa = E_lopussa, with every energy form counted (mechanical, thermal, chemical, radiant,
electrical, nuclear). Prints {id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json

a = {}
# Level 1: one formula, values given
a["fy2-1-L1-01"] = 50.0 + 0.0                        # stone: E_p at the top 50 J, E_k = 0, E_p at the ground 0 -> E_k = 50 J
a["fy2-1-L1-02"] = 60.0 - 3.0                        # bulb: E_sähkö = E_säteily + E_lämpö -> 60,0 − 3,0 = 57,0 J
a["fy2-1-L1-03"] = 800.0 - 120.0                     # solar panel: 800 J of radiation -> 120 J electrical + thermal = 680 J
a["fy2-1-L1-04"] = 1800.0                            # braking: E_k 1800 J -> 0, all to thermal energy: 1800 J
a["fy2-1-L1-05"] = 600.0 - 90.0                      # sledge: E_p 600 J = E_k + 90 J -> E_k = 510 J
# Level 2: a conversion, a rearrangement or two steps
a["fy2-1-L2-01"] = 2.00 * 1000 - 450                 # toy car: 2,00 kJ = 2000 J; thermal = 2000 − 450 = 1550 J
a["fy2-1-L2-02"] = 2.4 + 0.60                        # slide: E_p = E_k + E_lämpö = 2,4 kJ + 0,60 kJ = 3,0 kJ
a["fy2-1-L2-03"] = 490 * 1e-3                        # ball: all of E_p = 490 mJ = 0,49 J ends up as thermal energy
a["fy2-1-L2-04"] = (0.360 - 0.331) * 1000            # kettle: 0,360 MJ = 360 kJ, 0,331 MJ = 331 kJ -> 29 kJ
# Level 3: reasoning or an unfamiliar context
a["fy2-1-L3-01"] = (900 - 0 - 750) - (900 - 400 - 480)   # thermal at C 150 J, at B 20 J -> 130 J between B and C
a["fy2-1-L3-02"] = 5.0 - 5.0 * 0.80 * 0.80           # after two bounces E_mek = 5,0 · 0,64 = 3,2 J -> thermal 1,8 J
a["fy2-1-L3-03"] = 3.0 * 1000 - 1.0 * 1000           # 3,0 GJ = 3000 MJ, 1,0 GJ = 1000 MJ -> 2000 MJ to the cooling water
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
