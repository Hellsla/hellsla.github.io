"""Every answer in exercises.json for fy7-2, computed from the task data (python -I answers.py).
Magnetic force F = qvB sin α; circular path qvB = mv²/r so r = mv/(qB); velocity selector v = E/B; acceleration from
rest qU = ½mv²; uniform field between plates E = U/d (FY6). Constants as the tasks give them.
Prints {exercise id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json, math

e, mp, me, md, ma, u = 1.602e-19, 1.673e-27, 9.109e-31, 3.344e-27, 6.645e-27, 1.661e-27
a = {}
# Level 1: one formula, values given
a["fy7-2-L1-01"] = e * 3.0e5 * 0.25 / 1e-14            # proton beam: F = qvB = 1,2015e-14 N -> 1,2 (unit 10^-14 N)
a["fy7-2-L1-02"] = me * 2.0e6 / (e * 1.5e-3) * 1000     # electron in 1,5 mT: r = mv/(qB) = 7,58e-3 m = 7,6 mm
a["fy7-2-L1-03"] = 4.0e4 / 0.080 / 1000                 # velocity selector: v = E/B = 5,0e5 m/s = 500 km/s
a["fy7-2-L1-04"] = 2 * e * 1500 / 1e-16                 # alpha particle through 1500 V: W = qU = 4,806e-16 J -> 4,8 (10^-16 J)
a["fy7-2-L1-05"] = e * 5.0e6 * 0.40 * math.sin(math.radians(30)) / 1e-13   # F = qvB sin 30° = 1,602e-13 N -> 1,6 (10^-13 N)
# Level 2: two steps, a conversion or a rearrangement
v21 = math.sqrt(2 * e * 500 / mp)                       # proton from rest through 500 V: v = sqrt(2qU/m) = 3,095e5 m/s
a["fy7-2-L2-01"] = mp * v21 / (e * 0.050) * 100         # then B = 0,050 T: r = mv/(qB) = 0,0646 m = 6,5 cm
a["fy7-2-L2-02"] = e * 0.60 * 0.12 / md / 1000          # deuteron, r = 12 cm, B = 0,60 T: v = qBr/m = 3,449e6 m/s = 3,4e3 km/s
E23 = 600 / 0.020                                       # selector plates 600 V, 2,0 cm apart: E = U/d = 3,0e4 V/m
a["fy7-2-L2-03"] = E23 / 0.15 / 1000                    # v = E/B = 2,0e5 m/s = 200 km/s
a["fy7-2-L2-04"] = mp * 9.81 / (e * 50e-6) * 1000       # qvB = mg in Earth's 50 µT: v = mg/(qB) = 2,05e-3 m/s = 2,0 mm/s
# Level 3: reasoning or an unfamiliar context
r12 = 0.250                                             # C-12+ ions on r = 25,0 cm; same U, same q, so r = sqrt(2mU/q)/B ∝ sqrt(m)
r14 = r12 * math.sqrt(14.0 / 12.0)                      # C-14+: 0,27003 m
a["fy7-2-L3-01"] = 2 * (r14 - r12) * 100                # the spots are diameters apart: 2(r14 − r12) = 4,0 cm
a["fy7-2-L3-02"] = e * 1.50 / (2 * math.pi * mp) / 1e6  # cyclotron: T = 2πr/v = 2πm/(qB), f = qB/(2πm) = 22,9 MHz
a["fy7-2-L3-03"] = math.sqrt((ma / (2 * e)) / (mp / e)) # same U: r ∝ sqrt(m/q); r_α / r_p = sqrt(6,645/(2 · 1,673)) = 1,41
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
