"""Every answer in exercises.json for fy5-12, computed from the task data (python -I answers.py).
Superposition: y = y1 + y2. Two in-phase sources of the same frequency: path difference Δs = |s1 − s2|;
constructive interference when Δs = nλ, destructive when Δs = (n + ½)λ, n = 0, 1, 2, …; λ = v / f.
Prints {exercise id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json, math

a = {}
# Level 1: one formula, values given
a["fy5-12-L1-01"] = 2.5 + 1.5                 # same-side pulses, peaks coincide: y = y1 + y2 = 2,5 cm + 1,5 cm = 4,0 cm
a["fy5-12-L1-02"] = 3.0 + (-1.2)              # opposite pulses, peaks coincide: y = 3,0 cm + (−1,2 cm) = 1,8 cm
# fy5-12-L1-03 is answered in words: Δs/λ = 0,60/0,60 = 1 (V), 0,90/0,60 = 1,5 (H), 1,20/0,60 = 2 (V), 1,50/0,60 = 2,5 (H)
a["fy5-12-L1-04"] = 0.68 / 2                  # smallest destructive path difference (n = 0): Δs = λ/2 = 0,34 m
a["fy5-12-L1-05"] = 2 * 1.5                   # second constructive line (n = 2): Δs = 2λ = 3,0 cm
# Level 2: two steps, one conversion or one rearrangement
s1 = math.hypot(1.20, 1.60)                   # speaker A 1,20 m to the side, listener 1,60 m in front of B: s1 = 2,00 m
a["fy5-12-L2-01"] = 2 * (s1 - 1.60)           # quiet with the largest λ when Δs = λ/2: λ = 2 Δs = 2 · 0,40 m = 0,80 m
lam = 0.30 / 15 * 100                         # ripple tank: λ = v/f = 0,30 m/s : 15 Hz = 0,020 m = 2,0 cm
a["fy5-12-L2-02"] = 9.0 + lam / 2             # first nodal line (n = 0), nearer S2: s1 = s2 + λ/2 = 9,0 cm + 1,0 cm = 10,0 cm
ratio = (14.0 - 9.0) / 2.0                    # Δs/λ = 5,0 cm : 2,0 cm = 2,5 -> destructive
a["fy5-12-L2-03"] = abs(3.0 - 2.0)            # destructive with unequal amplitudes: A = |A1 − A2| = 1,0 mm
a["fy5-12-L2-04"] = 1.20 / (2 * 0.40)         # opposite pulses, centres 1,20 m apart, each 0,40 m/s: flat when centres meet, t = 1,5 s
# Level 3: reasoning or an unfamiliar context
lam3 = 340 / 340                              # λ = v/f = 340 m/s : 340 Hz = 1,0 m; Δs < d = 3,0 m on the whole line
a["fy5-12-L3-01"] = 2 * sum(1 for n in range(10) if (n + 0.5) * lam3 < 3.0)   # Δs = 0,5; 1,5; 2,5 m on each side: 6
v = 24.0                                      # cm/s; still at 10 Hz and next at 14 Hz: (n + ½) λ1 = (n + 1 + ½) λ2
l1, l2 = v / 10, v / 14
n = round((1.5 * l2 - 0.5 * l1) / (l1 - l2))  # 2,4 n + 1,2 = 1,714 n + 2,571 -> n = 2
a["fy5-12-L3-02"] = (n + 0.5) * l1            # Δs = 2,5 · 2,4 cm = 6,0 cm (check: 6,0 / 1,714 = 3,5)
assert all(abs(a["fy5-12-L3-02"] / (v / f) - round(a["fy5-12-L3-02"] / (v / f) - 0.5) - 0.5) > 0.05 for f in (11, 12, 13))
s1h = math.hypot(16.0, 30.0)                  # harbour: gaps 16,0 m apart, boat 30,0 m out from one gap: s1 = 34,0 m
a["fy5-12-L3-03"] = 2 * (s1h - 30.0)          # first nodal line (n = 0): Δs = λ/2 -> λ = 2 · 4,0 m = 8,0 m
# Exercise bank additions (L1-06..08, L2-05..07, L3-04..05)
# fy5-12-L1-06, L1-07, L2-06 are multiple choice (answered in words): superposition only adds the displacements, Δs = 0 on the central line, energy is redistributed
a["fy5-12-L1-08"] = 340 / (2 * (5.30 - 4.45))   # Δs = 0,85 m, smallest f for destructive: λ = 2Δs = 1,70 m, f = v/λ = 200 Hz
dx = (1.63 - 0.38) / 5                        # speakers 2,00 m apart, six consecutive weakest-sound points in 0,3...1,7 m: Δs = |d − 2x|, neighbouring minima Δx = λ/2 = 0,250 m
a["fy5-12-L2-05"] = 340 / (2 * dx)            # f = v/(2Δx) = 340 m/s : 0,500 m = 680 Hz
amax = (7.9 + 8.1 + 7.8) / 3                  # maxima of the amplitude table at Δs = 0, 2,0, 4,0 cm: mean 7,93 mm = 2A
a["fy5-12-L2-07"] = round(amax / 2, 1)         # A = 3,97 mm -> 4,0 mm (λ = 2,0 cm is read from the maxima)
a["fy5-12-L3-04"] = 340 / (340 / 170 / 2)         # Δs = λ/2 = 1,00 m at 170 Hz (N at 4,00 m); loud first when Δs = λ2: f2 = v/Δs = 340 Hz
def dpath(y, L=4.00, d=1.00):                 # speakers at y = ±0,50 m, line L = 4,00 m away: Δs = s1 − s2
    return math.hypot(L, y + d / 2) - math.hypot(L, y - d / 2)
f1 = 340 / (2 * dpath(0.82))                  # first quiet point n = 0: Δs = λ/2 -> f = 852,6 Hz
f2 = 340 / (2 * dpath(3.01) / 3)              # second quiet point n = 1: Δs = 3λ/2 -> f = 850,9 Hz (agrees within 1 %)
assert abs(f1 - f2) / f1 < 0.01
a["fy5-12-L3-05"] = round((f1 + f2) / 2, -1)  # two significant figures: 850 Hz
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
