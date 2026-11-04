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
# Level 2: two steps, a conversion or a rearrangement
a["fy7-10-L2-01"] = D(1.00 * S(90 - 25.0) / 1.52)   # 25,0° from the surface -> a1 = 65,0°; air -> glass: a2 = 36,6°
n = S(40.0) / S(25.4)                               # air -> plastic: n = sin 40,0° / sin 25,4° = 1,4986
a["fy7-10-L2-02"] = c / n / 1e8                     # v = c / n = 2,00 · 10^8 m/s (factor of 10^8)
a["fy7-10-L2-03"] = 2.0e-2 * (1.52 - 1.00) / c * 1e12   # delay through 2,0 cm of glass: d n / c - d / c = 34,7 ps
# figure fy7-10/protractor: a1 = 50° (air), a2 = 30° (glass half-cylinder) read off the protractor
a["fy7-10-L2-04"] = S(50) / S(30)                   # n = sin 50° / sin 30° = 1,53
# Level 3: reasoning or an unfamiliar context
a["fy7-10-L3-01"] = 90 - 30.0                       # mirrors at 90°: beta_1 = 30,0°, the second normal is parallel to mirror 1: 60,0°
a1 = math.degrees(math.atan(1.5 / 2.0))             # pool: lamp 2,0 m deep, exit point 1,5 m aside: a1 = 36,87° in water
a["fy7-10-L3-02"] = D(1.33 * S(a1) / 1.00)          # sin a2 = 1,33 · 0,600 = 0,798: a2 = 53,0°
a["fy7-10-L3-03"] = D(1.97 / 2.25 * S(40.0))        # sin a2 = (v2 / v1) sin a1 = 0,5628: a2 = 34,2°
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
