"""Numbers of the lesson text and inquiry.json for fy7-3, computed from their data (python -I lesson-answers.py); the
exercises' answers are in answers.py. Straight long wire B = mu0 I/(2 pi r); long coil B = mu0 N I/l; mu0 = 4 pi 10^-7 Vs/(Am).
The simulation's model: a coil of radius R = 2,0 cm, N turns evenly over the length l, the field on its axis at
distance x from the centre B(x) = mu0 N I/(2 l) [ (x + l/2)/sqrt((x + l/2)^2 + R^2) - (x - l/2)/sqrt((x - l/2)^2 + R^2) ]
(the turns' fields added, no iron, no Earth's field). Prints {id: number} as JSON."""
import json, math

mu0 = 4 * math.pi * 1e-7                                  # Vs/(Am)
wire = lambda I, r: mu0 * I / (2 * math.pi * r)           # T
coil = lambda N, I, l: mu0 * N * I / l                    # T, long coil


def axis(N, I, l, x, R=0.020):                            # finite coil on its axis, T (the simulation's model)
    a1, a2 = x + l / 2, x - l / 2
    return mu0 * N * I / (2 * l) * (a1 / math.hypot(a1, R) - a2 / math.hypot(a2, R))


a = {}
# --- simulation on load: N = 200, I = 1,0 A, l = 20 cm, probe at the centre ---
a["sim-load-B"] = axis(200, 1.0, 0.20, 0) * 1e3           # 1,232 mT on the readout
a["sim-load-n"] = 200 / 0.20                              # turn density 1000 1/m
a["sim-load-long"] = coil(200, 1.0, 0.20) * 1e3           # long-coil value 1,257 mT (Laskennan selitys)
# --- koe 1 (prediction 1): N = 200, I = 2,0 A, probe at the centre, l varied ---
for l in (10, 20, 30, 40):
    a[f"koe1-l{l}-B"] = axis(200, 2.0, l * 0.01, 0) * 1e3  # 4,67 / 2,46 / 1,66 / 1,25 mT
a["koe1-ratio"] = a["koe1-l40-B"] / a["koe1-l20-B"]       # 0,507: stretching to twice the length about halves B
# --- koe 2 (prediction 2): N = 200, I = 2,0 A, l = 20 cm, probe position varied ---
for x in (0, 5, 8, 10, 12, 15, 20):
    a[f"koe2-x{x}-B"] = axis(200, 2.0, 0.20, x * 0.01) * 1e3   # centre 2,46, end (x = 10 cm) 1,25 mT
a["koe2-ratio"] = a["koe2-x10-B"] / a["koe2-x0-B"]        # 0,507: at the end about half
# --- the LOPS measurement (interpret): N = 320, l = 16,0 cm, invented example data, least squares as Graphical Analysis ---
I_m = [0.00, 0.50, 1.00, 1.50, 2.00, 2.50]                # A
B_m = [0.04, 1.27, 2.51, 3.69, 4.99, 6.20]                # mT
n_ = len(I_m); mx = sum(I_m) / n_; my = sum(B_m) / n_
sxx = sum((x - mx) ** 2 for x in I_m); sxy = sum((x - mx) * (y - my) for x, y in zip(I_m, B_m))
k = sxy / sxx; b0 = my - k * mx
s = math.sqrt(sum((y - (k * x + b0)) ** 2 for x, y in zip(I_m, B_m)) / (n_ - 2))
a["fit-slope"] = k                                        # A = 2,465 mT/A
a["fit-intercept"] = b0                                   # B0 = 0,035 mT (the sensor's zero and Earth's field)
a["fit-slope-unc"] = s / math.sqrt(sxx)                   # Delta A = 0,012 mT/A
a["mu0-meas"] = k * 1e-3 * 0.160 / 320 * 1e6              # mu0 = A l / N = 1,2326e-6 Vs/(Am), in 10^-6
a["mu0-rel-pct"] = (0.012 / 2.465 + 0.2 / 16.0) * 100     # relative uncertainty with the rounded Delta A: 0,49 % + 1,25 % = 1,74 % -> 1,7 %
a["mu0-abs"] = a["mu0-rel-pct"] / 100 * 1.23              # Delta mu0 = 0,021 · 10^-6 -> 0,02 · 10^-6
a["mu0-true"] = mu0 * 1e6                                 # 1,2566 · 10^-6
a["finite-factor"] = 0.080 / math.hypot(0.080, 0.015)     # the 1,5 cm radius coil's centre gives 98,3 % of the long-coil value
a["mu0-corrected"] = a["mu0-meas"] / a["finite-factor"]   # 1,254 · 10^-6: the systematic part explained
# --- theory figure: a 10 A wire ---
for r in (1, 2, 4):
    a[f"fig-wire-r{r}"] = wire(10, r * 0.01) * 1e6        # 200 / 100 / 50 µT
# --- worked example: N = 600, l = 15,0 cm, I = 2,50 A ---
a["ex-B"] = coil(600, 2.50, 0.150) * 1e3                  # 12,57 mT -> 12,6 mT
a["ex-ratio"] = a["ex-B"] * 1e-3 / 50e-6                  # about 250 times Earth's 50 µT
# --- error spotting: N = 500, l = 25 cm, I = 2,0 A ---
a["err-wrong"] = mu0 * 500 * 2.0 / 25                     # l in centimetres: 5,0e-5 T
a["err-right"] = coil(500, 2.0, 0.25) * 1e3               # 5,03 mT
# --- transfer: cancel Earth's 50 µT inside a coil of 120 turns, l = 0,80 m ---
a["siirto"] = 50e-6 * 0.80 / (mu0 * 120)                  # I = B l/(mu0 N) = 0,2653 A -> 0,27 A
a["siirto-cm"] = 50e-6 * 80 / (mu0 * 120)                 # mistake: l in cm, 26,5 A
a["siirto-no4pi"] = 50e-6 * 0.80 / (1e-7 * 120)           # mistake: mu0 taken as 10^-7, 3,33 A
# --- check 2: welding cable 150 A at 2,0 cm ---
a["check-2"] = wire(150, 0.020) * 1e3                     # 1,5 mT
a["check-2-cm"] = mu0 * 150 / (2 * math.pi * 2.0) * 1e3   # mistake: r in cm, 0,015 mT
a["check-2-nopi"] = mu0 * 150 / 0.020 * 1e3               # mistake: 2 pi left out, 9,42 mT
# --- exit ticket: double I, half N, same l ---
a["exit-1"] = coil(100, 2.0, 0.2) / coil(200, 1.0, 0.2)   # 1: unchanged
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
