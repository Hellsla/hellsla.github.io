"""Every answer in exercises.json for fy7-10, computed from the task data (python -I answers.py).
Law of reflection beta = alpha_1 (angles from the normal); Snell n1 sin a1 = n2 sin a2; n = c / v, c = 3,00 · 10^8 m/s.
Prints {exercise id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json, math

S, D = (lambda d: math.sin(math.radians(d))), (lambda x: math.degrees(math.asin(x)))
c = 3.00e8
a = {}
# Level 1: one formula, values given
a["fy7-10-L1-01"] = c / 2.20e8                      # n = c / v = 3,00 · 10^8 / 2,20 · 10^8 = 1,36 (ethanol)
a["fy7-10-L1-02"] = c / 2.42 / 1e8                  # v = c / n = 1,24 · 10^8 m/s (diamond), answered as the factor of 10^8
a["fy7-10-L1-03"] = 76 / 2                          # beta = alpha and beta + alpha = 76°: alpha = 38°
a["fy7-10-L1-04"] = D(1.00 * S(60.0) / 1.52)        # air -> glass at 60,0°: sin a2 = 0,5698, a2 = 34,7°
a["fy7-10-L1-05"] = D(1.33 * S(40.0) / 1.00)        # water -> air at 40,0°: sin a2 = 0,8549, a2 = 58,8°
# L1-06 is multiple choice (no number)
a["fy7-10-L1-07"] = 633 / 1.52                      # f unchanged, v = f lambda: lambda = lambda_0 / n = 416,4 nm in glass
a["fy7-10-L1-08"] = D(1.36 * S(50.0) / 2.42)        # ethanol -> diamond: sin a2 = 0,4305, a2 = 25,5°
# Level 2: two steps, a conversion or a rearrangement
a["fy7-10-L2-01"] = D(1.00 * S(90 - 25.0) / 1.52)   # 25,0° from the surface -> a1 = 65,0°; air -> glass: a2 = 36,6°
n = S(40.0) / S(25.4)                               # air -> plastic: n = sin 40,0° / sin 25,4° = 1,4986
a["fy7-10-L2-02"] = c / n / 1e8                     # v = c / n = 2,00 · 10^8 m/s (factor of 10^8)
a["fy7-10-L2-03"] = 2.0e-2 * (1.52 - 1.00) / c * 1e12   # delay through 2,0 cm of glass: d n / c - d / c = 34,7 ps
# figure fy7-10/protractor: a1 = 50° (air), a2 = 30° (glass half-cylinder) read off the protractor
a["fy7-10-L2-04"] = S(50) / S(30)                   # n = sin 50° / sin 30° = 1,53
# L2-05 example data: sin a1 against sin a2, least squares through the origin: slope k = sum(xy) / sum(x^2) = n
x = [S(v) for v in (6.5, 13.5, 19.0, 25.5, 30.5, 36.0, 38.5)]
y = [S(v) for v in (10.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0)]
a["fy7-10-L2-05"] = sum(p * q for p, q in zip(x, y)) / sum(p * p for p in x)   # k = 1,4985, n = 1,50
a["fy7-10-L2-06"] = D(1.00 * S(50.0) / 1.33)        # error analysis: sin a2 = 0,7660 / 1,33 = 0,5760, a2 = 35,2° (not 50,0° : 1,33 = 37,6°)
n0, n_hi, n_lo = S(45.0) / S(28.0), S(45.5) / S(27.5), S(44.5) / S(28.5)   # n = 1,506; largest 1,545, smallest 1,469
a["fy7-10-L2-07"] = (n_hi - n_lo) / 2               # Delta n = (1,5447 - 1,4689) / 2 = 0,038
# L2-08 is find-the-error (no number): row 3 swaps n; glass -> air, a1 = 90° - 60,0° = 30,0°: sin a2 = 1,52 · 0,5 = 0,760, a2 = 49,5° (not 19,2°)
# Level 3: reasoning or an unfamiliar context
a["fy7-10-L3-01"] = 90 - 30.0                       # mirrors at 90°: beta_1 = 30,0°, the second normal is parallel to mirror 1: 60,0°
a1 = math.degrees(math.atan(1.5 / 2.0))             # pool: lamp 2,0 m deep, exit point 1,5 m aside: a1 = 36,87° in water
a["fy7-10-L3-02"] = D(1.33 * S(a1) / 1.00)          # sin a2 = 1,33 · 0,600 = 0,798: a2 = 53,0°
a["fy7-10-L3-03"] = D(1.97 / 2.25 * S(40.0))        # sin a2 = (v2 / v1) sin a1 = 0,5628: a2 = 34,2°
# L3-04 example data: object at d = 60,0 cm, viewed at a2 (10°, 20°, 30°, 40°) with apparent depth h'
# same surface point: x = d tan a1 = h' tan a2, so tan a1 = h' tan a2 / d; then n = sin a2 / sin a1
T = lambda d: math.tan(math.radians(d))
ns = []
for al2, h in ((10.0, 44.9), (20.0, 43.8), (30.0, 42.0), (40.0, 39.6)):
    ns.append(S(al2) / S(math.degrees(math.atan(h * T(al2) / 60.0))))   # 1,3274; 1,3319; 1,3344; 1,3268
a["fy7-10-L3-04"] = sum(ns) / len(ns)               # mean n = 5,3205 / 4 = 1,330
# L3-05 air -> glass 6,0 mm -> water 20,0 mm at 55,0°: sin a2 = sin 55,0° / 1,52 (32,61°), sin a3 = sin 55,0° / 1,33 (38,02°)
a2 = D(S(55.0) / 1.52)
a3 = D(S(55.0) / 1.33)
a["fy7-10-L3-05"] = 6.0 * T(a2) + 20.0 * T(a3)      # x = 3,839 mm + 15,636 mm = 19,5 mm
# MAFY table Taitekertoimia: water 1,333 (air given as 1,00); L1-09 air -> water at 52,0°: sin a2 = 0,7880 / 1,333 = 0,5912, a2 = 36,2°
a["fy7-10-L1-09"] = D(1.00 * S(52.0) / 1.333)
# figure fy7-10/fit: the fitted line has sin a1 = 0,294 at sin a2 = 0,20 and 0,890 at 0,60; slope k = 0,596 / 0,40 = 1,49 = n (acrylic)
k = (0.890 - 0.294) / (0.60 - 0.20)
a["fy7-10-L2-09"] = D(1.00 * S(35.0) / 1.50)        # air -> acrylic at 35,0°, n read from the graph as 1,50: sin a2 = 0,5736 / 1,50 = 0,3824, a2 = 22,5°
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
