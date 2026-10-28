"""Every answer in exercises.json for fy2-2, computed from the task data (python -I answers.py).
Prefixes are substituted by their values: 1 kJ = 1000 J, 1 MJ = 1000 kJ, 1 GJ = 1000 MJ, 1 TJ = 1000 GJ.
Prints {exercise id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json

a = {}
# Level 1: one step, values given
a["fy2-2-L1-01"] = 54 * 1000                       # phone battery 54 kJ = 54 · 1000 J = 54 000 J
a["fy2-2-L1-02"] = 4.4 * 1000                      # chocolate bar 4,4 MJ = 4,4 · 1000 kJ = 4400 kJ
a["fy2-2-L1-03"] = 0.14 * 1000                     # 0,14 TJ = 0,14 · 1000 GJ = 140 GJ
a["fy2-2-L1-04"] = 12 - 9.0                        # stove: 12 MJ − 9,0 MJ = 3,0 MJ warms the kitchen air
a["fy2-2-L1-05"] = (10 * 1000) / 450               # day's food 10 MJ = 10 000 kJ; 10 000 kJ : 450 kJ = 22,2 bananas
# Level 2: a conversion and a second step
a["fy2-2-L2-01"] = 2.2 + 800 / 1000                # 800 kJ = 0,8 MJ, so 2,2 MJ + 0,8 MJ = 3,0 MJ
a["fy2-2-L2-02"] = 40 * 32 / 1000                  # 40 l · 32 MJ/l = 1280 MJ = 1,28 GJ -> 1,3 GJ
a["fy2-2-L2-03"] = 6.0                             # lamp: all of the 6,0 kJ ends as heat (the light is absorbed and warms the room)
a["fy2-2-L2-04"] = (1.0e9) / (4.5e5)               # lightning 1,0 GJ = 1,0 · 10^9 J; banana 450 kJ = 4,5 · 10^5 J; ratio 2222 -> 2200
# Level 3: reasoning with several energies
a["fy2-2-L3-01"] = 790 / 140                       # Finland's electricity per day 790 TJ : 140 TJ per OL3 day = 5,64
a["fy2-2-L3-02"] = 370 - 140                       # reactor heat 370 TJ − electricity 140 TJ = 230 TJ to the environment
a["fy2-2-L3-03"] = 370 / 82                        # 370 TJ : 82 TJ per kg = 4,51 kg of uranium-235
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
