"""Every answer in exercises.json for fy6-2, computed from the task data (python -I answers.py).
A multimeter's error limit ±(p % of the reading + n digits) is Δx = p · x + n · r, r the range's resolution;
the relative error limit is Δx : x. In a loop without branches the current is the same everywhere.
Prints {exercise id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json

limit = lambda x, pct, digits, res: pct / 100 * x + digits * res
a = {}
# Level 1: one formula, values given
a["fy6-2-L1-01"] = limit(12.46, 0.5, 2, 0.01)            # car battery 12,46 V on 20 V: 0,0623 + 0,02 = 0,0823 V -> 0,08 V (1 sf, FY1 rule)
a["fy6-2-L1-02"] = limit(146.3, 1.0, 2, 0.1)             # LED strip 146,3 mA on 200 mA: 1,463 + 0,2 = 1,663 mA -> 1,7 mA (first digit 1: 2 sf)
a["fy6-2-L1-03"] = 0.06 / 8.00 * 100                     # adapter 8,00 V, ΔU = 0,06 V: 0,75 % -> 0,8 % (1 sf like ΔU)
a["fy6-2-L1-04"] = 0.180                                 # the same current after the lamp: 0,180 A
a["fy6-2-L1-05"] = limit(1.587, 0.5, 2, 0.001)           # AA cell 1,587 V on 2 V: 0,007935 + 0,002 = 0,009935 V -> 0,01 -> 0,010 V (first digit 1: 2 sf)
# Level 2: two steps, a conversion or a comparison
a["fy6-2-L2-01"] = limit(0.35, 2.0, 3, 0.01) / 0.35 * 100   # 0,35 A on 10 A: 0,037 A ≈ 0,04 A, 10,6 % -> 11 % (first digit 1: 2 sf)
a["fy6-2-L2-02"] = limit(0.0875, 1.0, 2, 0.0001)         # 0,0875 A on 200 mA, digit 0,1 mA = 0,0001 A: 0,000875 + 0,0002 = 0,001075 A
a["fy6-2-L2-03"] = limit(1.23, 0.5, 2, 0.01) / limit(1.234, 0.5, 2, 0.001)   # 0,02615 V : 0,00817 V = 3,2
a["fy6-2-L2-04"] = 9.0                                   # voltmeter in series with a lamp on a 9,0 V battery: about 9,0 V
# Level 3: reasoning or an unfamiliar context
a["fy6-2-L3-01"] = 1.0e-3 * 97.8 / 4.5 * 100             # burden 1,0 mV/mA at 97,8 mA: 97,8 mV of 4,5 V = 2,17 % -> 2,2 %
a["fy6-2-L3-02"] = limit(5.02, 0.5, 2, 0.01) + limit(5.14, 1.5, 3, 0.01)   # 0,0451 V + 0,1071 V = 0,1522 V -> 0,15 V
# Exercise bank additions (teacher 2026-11-04): L1-06, L1-07 and L2-06 are multiple choice (no number)
a["fy6-2-L1-08"] = limit(5.98, 0.5, 2, 0.01)             # solar cell 5,98 V on 20 V: 0,0299 + 0,02 = 0,0499 V -> 0,05 V (1 sf); result 5,98 ± 0,05 V
a["fy6-2-L2-05"] = limit(1.847, 0.5, 2, 0.001) * 1000    # best range 2 V: 0,009235 + 0,002 = 0,011235 V = 11,235 mV -> 11 mV (20 V: 29,25 mV, 200 V: 209 mV)
u5 = [12.48, 12.52, 12.46, 12.50, 12.49]                 # data of L2-07: sum 62,45 V, mean 12,49 V, half range 0,03 V
a["fy6-2-L2-07"] = limit(sum(u5) / len(u5), 0.5, 2, 0.01)   # 0,06245 + 0,02 = 0,08245 V -> 0,08 V; rest voltage of a full battery 12,60 V is 0,11 V away: not consistent
u0, r1, r2, rm = 12.0, 1.0e6, 1.0e6, 10.0e6              # L3-04: 12,0 V source, R1 = R2 = 1,0 MΩ, meter 10 MΩ across R2
u_m = u0 / (1 + r1 / r2 + r1 / rm)                       # (U0 - U) / R1 = U / R2 + U / Rm -> U = 12,0 V : 2,10 = 5,714 V
a["fy6-2-L3-04"] = (u0 / 2 - u_m) / (u0 / 2) * 100       # 6,00 V -> 5,714 V: 4,76 % -> 4,8 %
ur, ir = 4.52, 38.4                                      # L3-05: U = 4,52 V, I = 38,4 mA, R = 117,71 ohm
du, di = limit(ur, 0.5, 2, 0.01), limit(ir, 1.0, 2, 0.1)   # 0,0426 V (0,94 %) and 0,584 mA (1,52 %)
a["fy6-2-L3-05"] = ur / ir * 1000 * (du / ur + di / ir)  # dR = R (0,00942 + 0,0152) = 2,90 ohm -> 3 ohm; 120 ohm is inside 118 ± 3
print(json.dumps({k: round(v, 8) for k, v in a.items()}))
