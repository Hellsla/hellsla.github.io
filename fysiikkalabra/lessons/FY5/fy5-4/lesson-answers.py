"""Numbers of the lesson text and inquiry.json for fy5-4, computed from their data (python -I lesson-answers.py); the
exercises' answers are in answers.py. Uniform circular motion: a_n = v²/r towards the centre, ΣF = m v²/r towards the
centre; g = 9,81 m/s². Prints {id: number} as JSON."""
import json, math

g = 9.81
a = {}
# Kaava, graph a_n = v²/r: r = 50 m and r = 100 m
a["graph-50-10"] = 10 ** 2 / 50                         # 2,0 m/s²
a["graph-50-20"] = 20 ** 2 / 50                         # 8,0 m/s²: speed doubled, a_n four times
a["graph-100-20"] = 20 ** 2 / 100                       # 4,0 m/s²: radius doubled, a_n halved
# Worked example: car in a level curve, m = 1200 kg, r = 45 m, v = 54 km/h
m, r, v = 1200, 45, 54 / 3.6
a["ex-v"] = v                                           # 54/3,6 = 15 m/s
a["ex-an"] = v ** 2 / r                                 # a_n = v²/r = 5,0 m/s²
a["ex-F"] = m * v ** 2 / r                              # x: F_mu = m v²/r = 6000 N
a["ex-G"] = m * g                                       # y: N = mg = 11 772 N
a["ex-mu0"] = v ** 2 / (g * r)                          # F_mu ≤ mu0 mg → mu0 ≥ v²/(g r) = 0,510
# Simulation (model values): kuiva asfaltti mu0 = 0,80, märkä 0,50, jää 0,10
mu0 = 0.80
for vv in (5, 10, 15, 20):                               # Koe 1: r = 50 m, m = 1500 kg
    a[f"sim-an-{vv}"] = vv ** 2 / 50                    # 0,5 · 2,0 · 4,5 · 8,0 m/s²
    a[f"sim-F-{vv}"] = 1500 * vv ** 2 / 50              # 750 · 3000 · 6750 · 12 000 N
a["sim-Fmax-1500"] = mu0 * 1500 * g                     # 11 772 N
a["exp1-vmax"] = math.sqrt(mu0 * g * 50)                # m v²/r = mu0 m g → v = sqrt(mu0 g r) = 19,81 m/s
a["exp1-vmax-nomu"] = math.sqrt(g * 50)                 # mistake: without mu0, 22,1 m/s
a["exp1-vmax-nosqrt"] = mu0 * g * 50                    # mistake: no square root, 392,4
for vv in (25, 30):                                      # Koe 1, the slide: the car turns on a radius v²/(mu0 g), well over 50 m
    a[f"exp1-slide-r-{vv}"] = vv ** 2 / (mu0 * g)       # 79,6 m and 114,7 m: gentler than the track, straighter at 30 m/s
for mm in (1000, 1500, 2000):                            # Koe 2: v = 19 m/s, r = 50 m
    a[f"exp2-F-{mm}"] = mm * 19 ** 2 / 50               # 7220 · 10 830 · 14 440 N
    a[f"exp2-Fmax-{mm}"] = mu0 * mm * g                 # 7848 · 11 772 · 15 696 N
a["exp2-ratio"] = 19 ** 2 / 50 / (mu0 * g)              # needed / largest = 0,920, the same for every mass
# Siirto: roller coaster at the bottom of a dip, r = 12,0 m, N = 3G: N − mg = m v²/r → v = sqrt(2 g r)
a["siirto-v"] = math.sqrt(2 * g * 12.0)                 # 15,34 m/s
a["siirto-v-3"] = math.sqrt(3 * g * 12.0)               # mistake: N = m v²/r, 18,8 m/s
a["siirto-v-1"] = math.sqrt(g * 12.0)                   # mistake: N taken as 2G, v = sqrt(g r) = 10,8 m/s
a["siirto-G"] = 55 * g                                  # passenger 55 kg: G = 539,6 N, N = 3G = 1619 N
# check-2: child on a carousel, r = 2,0 m, T = 4,0 s, m = 30 kg
vc = 2 * math.pi * 2.0 / 4.0
a["check2-v"] = vc                                      # v = 2πr/T = 3,14 m/s
a["check2-an"] = vc ** 2 / 2.0                          # a_n = 4,93 m/s²
a["check2-F"] = 30 * vc ** 2 / 2.0                      # ΣF = m a_n = 148 N
a["check2-F-nosq"] = 30 * vc / 2.0                      # mistake m v / r = 47,1 N
# check-3 (draw): ice-hockey puck on a cord, m = 0,17 kg, v = 1,5 m/s, r = 0,50 m, no friction
a["check3-T"] = 0.17 * 1.5 ** 2 / 0.50                  # T = m v²/r = 0,765 N
a["check3-G"] = 0.17 * g                                # N = G = 1,668 N
# virhe / valitse figures: schematic units only (no numbers in the text)
print(json.dumps(a))
