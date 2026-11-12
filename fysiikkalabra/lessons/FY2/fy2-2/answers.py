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
# Exercise bank additions (teacher 2026-11-04): L1-06 is multiple choice (no number)
a["fy2-2-L1-07"] = 50 / 100 * 2400                 # pähkinät: 0,50 · 2400 kJ = 1200 kJ
a["fy2-2-L1-08"] = 0.35 * 1000                     # 0,35 GJ = 0,35 · 1000 MJ = 350 MJ
E_aamu = 2.5 * 300 + 1.2 * 400 + 2.0 * 190         # 750 + 480 + 380 = 1610 kJ
a["fy2-2-L2-05"] = round(E_aamu / 220, 1)          # 1610 kJ : 220 kJ/km = 7,32 -> 7,3 km
a["fy2-2-L2-06"] = 0.85 + 1200 / 1000 + 450 / 1000 # 0,85 + 1,2 + 0,45 = 2,5 MJ
ws, wE = [1.0, 2.0, 3.0, 4.0, 5.0], [262, 498, 771, 1003, 1262]   # data of L2-07
sm, Em = sum(ws) / 5, sum(wE) / 5
kw = sum((x - sm) * (y - Em) for x, y in zip(ws, wE)) / sum((x - sm) ** 2 for x in ws)   # least squares 250,5 kJ/km
a["fy2-2-L2-07"] = round(1500 / kw, 1)             # 1,5 MJ = 1500 kJ : 250,5 kJ/km = 5,99 -> 6,0 km (tolerance 0,04: 5,8…6,2)
Ek = [18 * 3.6, 12 * 42, 1200 * 3.6, 3.2 * 1e6]    # GJ: 64,8; 504; 4320; 3 200 000
a["fy2-2-L3-04"] = round(max(Ek) / min(Ek), -3)    # 3,2e6 : 64,8 = 49 383 -> 49 000 (tolerance 0,03: 47 500…50 500)
E_in = 1.4 + 3200 / 1000 + 650 / 1000 + 0.0042 * 1000 + 900 / 1000   # 10,35 MJ
E_out = 10.2 + 5.0 * 250 / 1000                    # 11,45 MJ
a["fy2-2-L3-05"] = round(30 * (E_out - E_in) / 37, 2)   # 33 MJ : 37 MJ/kg = 0,89 kg of fat
a["fy2-2-L1-10"] = 180 * 1000 * 4.1868 / 1000      # 180 kcal = 180 000 cal; 1 cal = 4,1868 J (MAFY) -> 753 624 J = 753,6 kJ
a["fy2-2-L1-11"] = 1 * 10 * 10                    # read off fy2-2/tikapuut-kohteet: tea water is two decades above 1 kJ = 100 kJ
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
