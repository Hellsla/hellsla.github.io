"""Every answer in exercises.json for fy2-2, computed from the task data (python -I answers.py).
Prefixes are substituted by their values: 1 kJ = 1000 J, 1 MJ = 1000 kJ, 1 GJ = 1000 MJ, 1 TJ = 1000 GJ.
Prints {exercise id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json, math

a = {}
# Level 1: one step, values given
a["fy2-2-L1-01"] = 54 * 1000                       # phone battery 54 kJ = 54 · 1000 J = 54 000 J
a["fy2-2-L1-02"] = 10 / 4.4                        # day's food 10 MJ : chocolate bar (200 g) 4,4 MJ = 2,27 -> 2,3 bars
a["fy2-2-L1-03"] = 0.14 * 1000                     # wind farm 0,14 TJ = 0,14 · 1000 GJ = 140 GJ
a["fy2-2-L1-04"] = 12 - 9.0                        # stove: 12 MJ − 9,0 MJ = 3,0 MJ warms the kitchen air
a["fy2-2-L1-05"] = 1e9 / 1e4                          # read off fy2-2/tikapuut-kohteet: lightning 1 GJ = 10^9 J, AA battery 10 kJ = 10^4 J -> 10^5 batteries
# Level 2: a conversion and a second step
a["fy2-2-L2-01"] = 2.2 + 0.80                      # 800 kJ = 0,80 · 1000 kJ = 0,80 MJ, so 2,2 MJ + 0,80 MJ = 3,0 MJ
a["fy2-2-L2-02"] = 40 * 32 / 1000                  # 40 l · 32 MJ/l = 1280 MJ = 1,28 · 1000 MJ = 1,28 GJ -> 1,3 GJ
a["fy2-2-L2-03"] = 6.0                             # lamp: all of the 6,0 kJ ends as heat (the light is absorbed and warms the room)
a["fy2-2-L2-04"] = (4.2 * 1000) / 4.4              # TNT tonne 4,2 GJ = 4,2 · 1000 MJ = 4200 MJ; 4200 MJ : 4,4 MJ per bar = 954,5 -> 950
# Level 3: reasoning with several energies
a["fy2-2-L3-01"] = math.ceil(790 / 140)            # 790 TJ : 140 TJ = 5,64 units; 5 would not cover the use, so at least 6
E_meri = 370 - 140                                 # reactor 370 TJ − electricity 140 TJ = 230 TJ of heat to the sea
a["fy2-2-L3-02"] = E_meri * 1000 / 72               # 230 TJ = 230 · 1000 GJ = 230 000 GJ; 230 000 GJ : 72 GJ per house = 3194 -> 3200 houses
a["fy2-2-L3-03"] = 370 * 1000 * 1000 / 32          # 370 TJ = 370 · 1000 · 1000 MJ = 3,7 · 10^8 MJ; : 32 MJ per litre = 1,16 · 10^7 l of petrol
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
