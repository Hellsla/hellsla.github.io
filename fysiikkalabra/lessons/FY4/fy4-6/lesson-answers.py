"""Numbers of the lesson text and inquiry.json for fy4-6, computed from their data (python -I lesson-answers.py); the
exercises' answers are in answers.py. On a slope x points down the slope (or along the motion), y away from the surface;
g = 9,81 m/s². Prints {id: number} as JSON."""
import json, math

g = 9.81
r = math.radians
a = {}
# Ydinajatus, friction graph: box with N = 100 N, mu0 = 0,50, mu = 0,35
a["fig-Fmax"] = 0.50 * 100                              # largest static friction mu0 N = 50 N
a["fig-Fkin"] = 0.35 * 100                              # kinetic friction mu N = 35 N
# Ydinajatus, box on an accelerating pickup: m = 20 kg, a = 2,0 m/s² forward
a["fig-truck-Fmu"] = 20 * 2.0                           # x: F_mu = ma = 40 N forward
# Worked example: box sliding down a ramp, m = 18 kg, alpha = 25°, mu = 0,30
m, al, mu = 18, r(25), 0.30
a["ex-G"] = m * g                                       # G = mg = 176,6 N
a["ex-Gx"] = m * g * math.sin(al)                       # G_x = mg sin α = 74,6 N
a["ex-N"] = m * g * math.cos(al)                        # y: N − mg cos α = 0 → N = 160,0 N
a["ex-Fmu"] = mu * m * g * math.cos(al)                 # F_mu = mu N = 48,0 N
a["ex-a"] = g * (math.sin(al) - mu * math.cos(al))      # x: mg sin α − mu mg cos α = ma → a = 1,48 m/s²
a["ex-a-nofriction"] = g * math.sin(al)                 # Järkevyys: without friction 4,15 m/s²
# Simulation (model values): surface "puu puulla" mu0 = 0,50, mu = 0,30; m = 2,0 kg
G2 = 2.0 * g
a["sim-G"] = G2                                         # 19,6 N
a["sim-F10"] = G2 * math.sin(r(10))                     # at rest: F_mu0 = G_x = 3,41 N
a["sim-F20"] = G2 * math.sin(r(20))                     # 6,71 N
a["sim-F26"] = G2 * math.sin(r(26))                     # 8,60 N
a["sim-slip"] = math.degrees(math.atan(0.50))           # slips above tan α = mu0: 26,6°
a["sim-F27"] = 0.30 * G2 * math.cos(r(27))              # sliding at 27°: F_mu = mu N = 5,24 N
a["sim-N0"] = G2                                        # N at 0° = 19,6 N
a["sim-N26"] = G2 * math.cos(r(26))                     # N at 26° = 17,6 N
# exp-1 question: mu0 from the slip angle, between 26° and 27°
a["inq-exp1-mu0"] = math.tan(r(26.5))                   # 0,499
a["inq-exp1-mu0-26"] = math.tan(r(26))                  # 0,488 (inside 3 %)
a["inq-exp1-mu0-27"] = math.tan(r(27))                  # 0,510 (inside 3 %)
a["inq-exp1-sin"] = math.sin(r(26.5))                   # mistake: sin α = 0,446
a["inq-exp1-cos"] = math.cos(r(26.5))                   # mistake: cos α = 0,895
# exp-2: alpha = 35°, puu puulla, masses 2, 3 and 4 kg slide with the same acceleration
a["sim-a35"] = g * (math.sin(r(35)) - 0.30 * math.cos(r(35)))   # 3,22 m/s²
a["sim-F35-2"] = 0.30 * 2 * g * math.cos(r(35))                # 4,82 N
a["sim-F35-4"] = 0.30 * 4 * g * math.cos(r(35))                # 9,64 N
# interpret (example data): block pulled at constant velocity, spring-scale readings
data = [(0.50, 1.7), (1.00, 3.5), (1.50, 5.1), (2.00, 6.9)]
ratios = [F / (mm * g) for mm, F in data]               # mu = F_mu / N, N = mg on a level table
for i, q in enumerate(ratios): a[f"inq-data-mu{i + 1}"] = q   # 0,347 0,357 0,347 0,352
a["inq-data-mu"] = sum(ratios) / len(ratios)            # mean 0,350
a["inq-data-mu-g"] = sum(F / mm for mm, F in data) / 4  # mistake: F/m without g = 3,4
# siirto: box on a conveyor belt moving up at constant velocity, m = 8,0 kg, alpha = 15°
a["inq-siirto"] = 8.0 * g * math.sin(r(15))             # x (up the belt): F_mu0 − mg sin α = 0 → 20,3 N
a["inq-siirto-cos"] = 8.0 * g * math.cos(r(15))         # mistake: 75,8 N
a["inq-siirto-mg"] = 8.0 * g                            # mistake: 78,5 N
# check-2: a book slides down at constant velocity at 17°
a["inq-check2"] = math.tan(r(17))                       # mu = tan α = 0,306
a["inq-check2-sin"] = math.sin(r(17))                   # mistake 0,292
a["inq-check2-cos"] = math.cos(r(17))                   # mistake 0,956
# check-3 (draw): box pulled up a 20° slope at constant velocity by a rope along the slope, m = 20 kg, mu = 0,25
m3, al3, mu3 = 20, r(20), 0.25
a["inq-check3-N"] = m3 * g * math.cos(al3)              # y: N − mg cos α = 0 → 184,4 N
a["inq-check3-Fmu"] = mu3 * m3 * g * math.cos(al3)      # F_mu = mu N = 46,1 N
a["inq-check3-Gx"] = m3 * g * math.sin(al3)             # 67,1 N
a["inq-check3-T"] = m3 * g * (math.sin(al3) + mu3 * math.cos(al3))   # x: T − mg sin α − mu mg cos α = 0 → 113,2 N
# exit ticket: 60 kg on the Moon
a["exit-moon"] = 60 * 1.62                              # 97,2 N
a["exit-earth"] = 60 * g                                # 588,6 N
print(json.dumps(a))
