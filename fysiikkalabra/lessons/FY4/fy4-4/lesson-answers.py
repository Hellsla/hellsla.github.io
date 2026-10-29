"""Numbers of the lesson text and inquiry.json for fy4-4, computed from their data (python -I lesson-answers.py); the
exercises' answers are in answers.py. Positive direction: up, or the cart's track to the right; g = 9,81 m/s². Prints {id: number} as JSON."""
import json

g = 9.81
a = {}
# Worked example: crane lifts a concrete element, m = 480 kg, rope T = 5,20 kN
m, T = 480, 5200
a["ex-G"] = m * g                                  # G = mg = 4708,8 N
a["ex-sumF"] = T - m * g                           # ΣF = T − G = 491,2 N
a["ex-a"] = (T - m * g) / m                        # a = (T − mg)/m = 1,023 m/s²
a["ex-a-wrong"] = T / m                            # Järkevyys: forgetting G gives 10,8 m/s²
# Simulation experiments (model values): a = ΣF/m on a track with negligible friction
a["exp1-a1"] = 1.0 / 1.0                           # F = 1,0 N, m = 1,0 kg: 1,0 m/s²
a["exp1-a2"] = 2.0 / 1.0                           # F = 2,0 N: 2,0 m/s²
a["exp2-a1"] = 1.0 / 0.50                          # F = 1,0 N, m = 0,50 kg: 2,0 m/s²
a["exp2-a2"] = 1.0 / 1.0                           # m = 1,0 kg: 1,0 m/s²
a["exp3-a"] = -2.0 / 1.0                           # pull 2,0 N to the left on 1,0 kg: −2,0 m/s²
a["exp3-tstop"] = 1.5 / 2.0                        # moving right at 1,5 m/s, it stops after 0,75 s
# Figure "kuvaaja": a against ΣF for m = 0,50 kg and m = 1,0 kg
a["fig-a-050-3N"] = 3.0 / 0.50                     # 6,0 m/s²
a["fig-a-10-3N"] = 3.0 / 1.0                       # 3,0 m/s²
# siirto: car m = 1400 kg, 72 km/h = 20 m/s, stops in 4,0 s
v0 = 72 / 3.6
a["siirto-a"] = (0 - v0) / 4.0                     # a = −5,0 m/s²
a["siirto"] = 1400 * abs(a["siirto-a"])            # |ΣF| = 7000 N
a["siirto-kmh"] = 1400 * 72 / 4.0                  # mistake: 72 km/h used as m/s, 25 200 N
a["siirto-a-only"] = abs(a["siirto-a"])            # mistake: the acceleration 5,0
a["siirto-mg"] = 1400 * g                          # mistake: the weight 13 734 N
# check-2: shopping trolley m = 18 kg, push 30 N, resistance 12 N
a["check2"] = (30 - 12) / 18                       # a = 1,0 m/s²
a["check2-nofric"] = 30 / 18                       # mistake: 1,67 m/s²
a["check2-sum"] = (30 + 12) / 18                   # mistake: 2,33 m/s²
# check-3 model: book m = 1,2 kg pushed with 5,0 N, friction 3,0 N
a["check3-G"] = 1.2 * g                            # N = G = 11,8 N
a["check3-a"] = (5.0 - 3.0) / 1.2                  # a = 1,67 m/s²
# figure "kokonaisvoima": box m = 8,0 kg pulled with 60 N against friction 20 N
a["fig-sumF"] = 60 - 20                            # ΣF = 40 N
print(json.dumps(a))
