"""Every answer in exercises.json for fy2-1, computed from the task data (python -I answers.py).
Energy balance of an isolated system: E_alussa = E_lopussa, with every energy form counted (mechanical, thermal, chemical, radiant,
electrical, nuclear). Prints {id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json

a = {}
# Level 1: one formula, values given
a["fy2-1-L1-01"] = 50.0 + 0.0                        # stone: E_p at the top 50 J, E_k = 0, E_p at the ground 0 -> E_k = 50 J
a["fy2-1-L1-02"] = 245.0 - 6.0                       # leaf: 245 J of radiation = 6,0 J chemical + thermal -> 239 J
# skater, read off fy2-1/kitka-pylvaat: E_p + E_k at A 700 J + 0 J, at C 0 J + 500 J; friction turned the difference into thermal energy
a["fy2-1-L1-03"] = (700.0 + 0.0) - (0.0 + 500.0)
# fy2-1-L1-04 is answered in words (naming the forms): no number
a["fy2-1-L1-05"] = 600.0 - 90.0                      # sledge: E_p 600 J = E_k + 90 J -> E_k = 510 J
# Level 2: a conversion, a rearrangement or two steps
a["fy2-1-L2-01"] = 3.00 * 1000 - 2150                # scooter: 3,00 kJ = 3000 J; thermal = 3000 − 2150 = 850 J
a["fy2-1-L2-02"] = 2400 * 0.001 + 0.60               # slide: 2400 J = 2,4 kJ; E_p = E_k + E_lämpö = 2,4 kJ + 0,60 kJ = 3,0 kJ
a["fy2-1-L2-03"] = 0.36 * 1000                       # swing: all of E_p = 0,36 kJ = 360 J ends up as thermal energy
a["fy2-1-L2-04"] = (360 - 331) * 1000                # kettle: 360 kJ − 331 kJ = 29 kJ = 29 000 J
# Level 3: reasoning or an unfamiliar context
a["fy2-1-L3-01"] = (900 - 0 - 750) - (900 - 400 - 480)   # thermal at C 150 J, at B 20 J -> 130 J between B and C
a["fy2-1-L3-02"] = (5.00 - 4.00) - (4.00 - 3.20)     # thermal in bounce 1: 1,00 J, in bounce 2: 0,80 J -> 0,20 J more in the first
# fy2-1-L3-03 is answered in words (forms in a nuclear plant, where the other two thirds go): no number
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
