"""Every answer in exercises.json for fy6-2, computed from the task data (python -I answers.py).
A multimeter's error limit ±(p % of the reading + n digits) is Δx = p · x + n · r, r the range's resolution;
the relative error limit is Δx : x. In a loop without branches the current is the same everywhere.
Prints {exercise id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json

limit = lambda x, pct, digits, res: pct / 100 * x + digits * res
a = {}
# Level 1: one formula, values given
a["fy6-2-L1-01"] = limit(12.46, 0.5, 2, 0.01)            # car battery 12,46 V on 20 V: 0,0623 + 0,02 = 0,0823 V -> 0,082 V
a["fy6-2-L1-02"] = limit(146.3, 1.0, 2, 0.1)             # LED strip 146,3 mA on 200 mA: 1,463 + 0,2 = 1,663 mA -> 1,7 mA
a["fy6-2-L1-03"] = 0.060 / 8.00 * 100                    # adapter 8,00 V, ΔU = 0,060 V: 0,75 %
a["fy6-2-L1-04"] = 0.180                                 # the same current after the lamp: 0,180 A
a["fy6-2-L1-05"] = limit(1.587, 0.5, 2, 0.001)           # AA cell 1,587 V on 2 V: 0,007935 + 0,002 = 0,009935 V -> 0,0099 V
# Level 2: two steps, a conversion or a comparison
a["fy6-2-L2-01"] = limit(0.35, 2.0, 3, 0.01) / 0.35 * 100   # 0,35 A on 10 A: 0,037 A, 10,6 % of the reading
a["fy6-2-L2-02"] = limit(0.0875, 1.0, 2, 0.0001)         # 0,0875 A on 200 mA, digit 0,1 mA = 0,0001 A: 0,000875 + 0,0002 = 0,001075 A
a["fy6-2-L2-03"] = limit(1.23, 0.5, 2, 0.01) / limit(1.234, 0.5, 2, 0.001)   # 0,02615 V : 0,00817 V = 3,2
a["fy6-2-L2-04"] = 9.0                                   # voltmeter in series with a lamp on a 9,0 V battery: about 9,0 V
# Level 3: reasoning or an unfamiliar context
a["fy6-2-L3-01"] = 1.0e-3 * 97.8 / 4.5 * 100             # burden 1,0 mV/mA at 97,8 mA: 97,8 mV of 4,5 V = 2,17 % -> 2,2 %
a["fy6-2-L3-02"] = limit(5.02, 0.5, 2, 0.01) + limit(5.14, 1.5, 3, 0.01)   # 0,0451 V + 0,1071 V = 0,1522 V -> 0,15 V
print(json.dumps({k: round(v, 8) for k, v in a.items()}))
