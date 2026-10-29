"""Numbers of the lesson text and inquiry.json for fy4-5, computed from their data (python -I lesson-answers.py); the
exercises' answers are in answers.py. x along the motion (or horizontal), y up; g = 9,81 m/s². Prints {id: number} as JSON."""
import json, math

g = 9.81
a = {}
# Worked example: sled m = 12 kg, rope T = 80 N at 35°, friction 30 N on level snow
m, T, al, Fmu = 12, 80, math.radians(35), 30
a["ex-Tx"] = T * math.cos(al)                         # T_x = T cos α = 65,5 N
a["ex-Ty"] = T * math.sin(al)                         # T_y = T sin α = 45,9 N
a["ex-G"] = m * g                                     # G = mg = 117,7 N
a["ex-a"] = (T * math.cos(al) - Fmu) / m              # x: T cos α − F_μ = ma → a = 2,96 m/s²
a["ex-N"] = m * g - T * math.sin(al)                  # y: N + T sin α − mg = 0 → N = 71,8 N
a["ex-a-nofriction"] = T * math.cos(al) / m           # Järkevyys: without friction 5,5 m/s²
# exp-1 (simulation, pull, m = 20 kg, F = 100 N): at α = 30° the rope carries G − N = F sin α
a["inq-exp1-Fy"] = 100 * math.sin(math.radians(30))   # 50 N
a["inq-exp1-N30"] = 20 * g - a["inq-exp1-Fy"]         # N = 196,2 N − 50 N = 146,2 N
a["inq-exp1-a0"] = 100 / 20                           # α = 0: a = F/m = 5,0 m/s²
a["inq-exp1-a60"] = 100 * math.cos(math.radians(60)) / 20   # α = 60°: 2,5 m/s²
# interpret (example data): block m = 0,60 kg pulled at constant velocity, spring scale 2,0 N at 30°
a["inq-data-N"] = 0.60 * g - 2.0 * math.sin(math.radians(30))     # y: N + F sin α − mg = 0 → 4,9 N
a["inq-data-N-noFy"] = 0.60 * g                                   # mistake: N = G = 5,9 N
a["inq-data-N-plus"] = 0.60 * g + 2.0 * math.sin(math.radians(30))  # mistake: sign of F_y, 6,9 N
a["inq-data-Fmu"] = 2.0 * math.cos(math.radians(30))              # x: F cos α − F_μ = 0 → 1,7 N
# siirto: fish m = 2,0 kg lifted with acceleration 1,5 m/s² up
a["inq-siirto"] = 2.0 * (g + 1.5)                     # T − mg = ma → T = m(g + a) = 22,6 N
a["inq-siirto-mg"] = 2.0 * g                          # mistake: T = mg = 19,6 N
a["inq-siirto-minus"] = 2.0 * (g - 1.5)               # mistake: T = m(g − a) = 16,6 N
a["inq-siirto-ma"] = 2.0 * 1.5                        # mistake: T = ma = 3,0 N
# check-2: sign m = 8,0 kg hung by two ropes, each 50° above the horizontal, symmetric
a["inq-check2"] = 8.0 * g / (2 * math.sin(math.radians(50)))     # y: 2T sin 50° − mg = 0 → T = 51,2 N
a["inq-check2-half"] = 8.0 * g / 2                                # mistake: T = mg/2 = 39,2 N
a["inq-check2-cos"] = 8.0 * g / (2 * math.cos(math.radians(50)))  # mistake: cos for sin, 61,0 N
a["inq-check2-one"] = 8.0 * g / math.sin(math.radians(50))       # mistake: one rope only, 102 N
# check-3 model: box m = 12 kg pushed with F = 60 N at 30° below the horizontal, constant velocity
a["inq-check3-Fmu"] = 60 * math.cos(math.radians(30))            # x: F cos α − F_μ = 0 → 52 N
a["inq-check3-N"] = 12 * g + 60 * math.sin(math.radians(30))     # y: N − mg − F sin α = 0 → 147,7 N
print(json.dumps(a))
