"""Numbers of the lesson text and inquiry.json for fy5-7, computed from their data (python -I lesson-answers.py); the
exercises' answers are in answers.py. Model: x(t) = A sin(2πt/T) = A sin(2πft), f = 1/T, the sine's argument in radians.
The simulation's data sets are generated exactly as assets/sims/fy5/fy5-7/sim.js does (Park–Miller noise of ±0,25 cm on
51 points at 0,0 … 5,0 s), so the model values quoted in predictions and the conclusion are the sim's own.
Prints {id: number} as JSON on the last line."""
import json, math

pi = math.pi
a = {}
# --- the simulation's data sets (sim.js DATA, NOISE, dataset()) ---
M, NOISE = 2147483647, 0.25
DATA = {1: (6.0, 1.60, 11), 2: (4.5, 0.80, 23), 3: (8.5, 2.20, 37)}       # A (cm), T (s), seed


def dataset(k):
    A, T, s = DATA[k]; pts = []
    for i in range(51):
        s = (s * 16807) % M; t = i / 10; e = (s / M - 0.5) * 2 * NOISE
        pts.append((t, A * math.sin(2 * pi * t / T) + e))
    return pts


def dev(k, Am, Tm):                                      # d = mean |x_i − A_m sin(2π t_i / T_m)|, cm
    P = dataset(k); return sum(abs(x - Am * math.sin(2 * pi * t / Tm)) for t, x in P) / len(P)


def full(Tm): return math.floor(5.0 / Tm + 1e-9)          # the model's full oscillations in the 5,0 s window
# on load: data set 1, model A = 2,0 cm, T = 1,00 s
a["sim-load-d"] = dev(1, 2.0, 1.00)
# koe 1 (data set 1, T locked at 1,60 s): the deviation against the model amplitude
for A in (3.0, 6.0, 12.0): a[f"koe1-d-A{A:g}"] = dev(1, A, 1.60)
# koe 2 (data set 1, A locked at 6,0 cm): the model period changes the number of oscillations
for T in (0.80, 1.60): a[f"koe2-f-T{T:g}"] = 1 / T; a[f"koe2-N-T{T:g}"] = full(T); a[f"koe2-d-T{T:g}"] = dev(1, 6.0, T)
# koe 3 (data set 3, both free): the best fit on the sliders' grid (A step 0,5 cm, T step 0,05 s)
best = min((dev(3, i / 2, j / 100), i / 2, j / 100) for i in range(1, 25) for j in range(40, 301, 5))
a["koe3-best-d"], a["koe3-best-A"], a["koe3-best-T"] = best
a["koe3-f"] = 1 / best[2]                                # 0,4545 Hz
for k in (1, 2):                                        # the other data sets' best fits are their own A and T
    b = min((dev(k, i / 2, j / 100), i / 2, j / 100) for i in range(1, 25) for j in range(40, 301, 5))
    a[f"set{k}-best-A"], a[f"set{k}-best-T"] = b[1], b[2]
# Kaava text: f = 1/T for T = 0,50 s; the quarter points of x = A sin(2πt/T)
a["text-f-T050"] = 1 / 0.50                              # 2,0 Hz
a["text-sin-quarter"] = math.sin(2 * pi * 0.25)          # t = T/4: sin(π/2) = 1, x = A
# Esimerkki: 5 full oscillations in 3,0 s, A = 4,0 cm, t = 0,25 s
T_ex = 3.0 / 5                                           # 0,60 s
a["ex-T"] = T_ex
a["ex-f"] = 1 / T_ex                                     # 1,667 Hz
a["ex-arg"] = 2 * pi * 0.25 / T_ex                       # 2,618 rad (= 5π/6)
a["ex-x"] = 4.0 * math.sin(a["ex-arg"])                  # 2,0 cm
a["ex-quarter"] = T_ex / 4                               # top at 0,15 s
a["ex-half"] = T_ex / 2                                  # equilibrium at 0,30 s
a["ex-sin-deg"] = math.sin(math.radians(a["ex-arg"]))   # calculator in degrees: sin 2,618° = 0,0457
a["ex-x-deg"] = 4.0 * a["ex-sin-deg"]                    # 0,183 cm
a["sov-T"] = 3.6 / 3                                     # fitting figure: three oscillations in 3,6 s -> 1,2 s
a["virhe-A-12"] = 12 / 2                                 # misconception text: 12 cm extreme to extreme -> A = 6,0 cm
# Etsi virhe: zero crossings at 0, 0,45, 0,90, 1,35 s
a["virhe-T-right"] = 0.90; a["virhe-f-right"] = 1 / 0.90 # 1,11 Hz
a["virhe-f-wrong"] = 1 / 0.45                            # 2,22 Hz
# Vaihe (optional): C = π/2 is a quarter of a cycle
a["vaihe-C"] = pi / 2                                    # 1,571
a["vaihe-fraction"] = (pi / 2) / (2 * pi)                # 0,25
# Siirto: bridge deck, A = 4,0 cm, f = 0,50 Hz, t = 0,40 s
arg = 2 * pi * 0.50 * 0.40                               # 1,2566 rad
a["siirto"] = 4.0 * math.sin(arg)                        # 3,804 cm -> 3,8 cm
a["siirto-deg"] = 4.0 * math.sin(math.radians(arg))      # calculator in degrees: 0,0877 cm
a["siirto-fasT"] = 4.0 * math.sin(2 * pi * 0.40 / 0.50)  # f used as T: −3,804 cm
a["siirto-T"] = 1 / 0.50                                 # 2,0 s; t = 0,40 s is a fifth of the period
# Tarkistus 1: swing, extremes 1,6 m apart, extreme to extreme and back 3,0 s
a["check1-A"] = 1.6 / 2                                  # 0,80 m
# Tarkistus 2: model graph, 3 full oscillations in 5,4 s
a["check2"] = 3 / 5.4                                    # f = 0,5556 Hz
a["check2-T"] = 5.4 / 3                                  # 1,8 s
a["check2-half"] = 1 / 0.9                               # half period read as T: 1,111 Hz
a["check2-total"] = 1 / 5.4                              # 0,185 Hz
# Tarkistus 3 (optional): fit A sin(Bt + C) + D with B = 7,85 1/s
a["check3-T"] = 2 * pi / 7.85                            # 0,8004 s
a["check3-f"] = 7.85 / (2 * pi)                          # 1,249 Hz
# Exit ticket: x = 3,0 cm · sin(2πt / 0,50 s)
a["exit-f"] = 1 / 0.50                                   # 2,0 Hz
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
