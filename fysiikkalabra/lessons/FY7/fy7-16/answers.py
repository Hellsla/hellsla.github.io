"""Every answer in exercises.json for fy7-16, computed from the task data (python -I answers.py).
Fibre attenuation A = a L, A = 10 dB · lg(P0 / P); P = R I², P = U² / R; Φ = B A; e0 = N · 2πf · Φ0; Q = c m ΔT.
Prints {exercise id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json
from math import pi, sqrt, log10, ceil

a = {}
# Level 1: one formula, values given
a["fy7-16-L1-01"] = 0.18 * 50                        # A = a L = 9,0 dB
a["fy7-16-L1-02"] = 10 * log10(2.0 / 0.50)           # A = 10 dB · lg 4 = 6,02 dB -> 6,0 dB
a["fy7-16-L1-03"] = 0.010 * 400 ** 2 / 1e3           # P = R I² = 1600 W = 1,6 kW
a["fy7-16-L1-04"] = 0.50e-3 * 12 * 0.01 ** 2 * 1e6   # Φ = B A = 0,50 mT · 12 cm² = 0,60 µWb
a["fy7-16-L1-05"] = 100 * 7.2 / 10.0                 # η = P_akku / P_otto = 72 %
# Level 2: two steps, a conversion or a rearrangement
a["fy7-16-L2-01"] = 10 * 2 * pi * 140e3 * 0.40e-6    # e0 = N 2πf Φ0 = 3,519 V -> 3,5 V
A_max = 10 * log10(1.0e-3 / 1.0e-6)                  # the largest attenuation allowed: 30 dB
a["fy7-16-L2-02"] = A_max / 0.20                     # L = A / a = 150 km
Q = 4190 * 1.5 * (100 - 15)                          # water 1,5 kg from 15 °C to 100 °C: Q = 534 225 J
a["fy7-16-L2-03"] = Q / (0.85 * 2.0e3) / 60          # t = Q / (η P) = 314,25 s = 5,24 min
a["fy7-16-L2-04"] = (21.01 - 14.26) * 365 / 1000     # extra energy in a year: 6,75 Wh · 365 = 2,46 kWh
# Level 3: reasoning across the course
span = 20 / 0.18                                     # one span may attenuate at most 20 dB: 111,1 km
spans = ceil(1172 / span)                            # 1172 km needs 11 spans (10,55 rounded up)
a["fy7-16-L3-01"] = spans - 1                        # the amplifiers sit between the spans: 10
e0 = 2 * pi * 25e3 * 4.0e-3 * pi * 0.080 ** 2        # one loop r = 8,0 cm, B0 = 4,0 mT, 25 kHz: e0 = 12,63 V
U = e0 / sqrt(2)                                     # effective value 8,93 V
a["fy7-16-L3-02"] = U ** 2 / 0.050 / 1e3             # P = U² / R = 1595 W -> 1,6 kW
A_fibre = 10 * log10(1.0e-3 / 10e-6) - 4 * 0.50      # 20 dB budget minus 4 joints · 0,50 dB = 18 dB for the fibre
L = A_fibre / 0.20 * 1e3                             # 90 km = 90 000 m
a["fy7-16-L3-03"] = 1.47 * L / 3.00e8 * 1e3          # t = n L / c = 0,441 ms
# Exercise-bank additions
# L1-06 is multiple choice (no number)
a["fy7-16-L1-07"] = 4.0 * 10 ** (-(0.20 * 45) / 10)  # A = a L = 9,0 dB; P = P0 · 10^(-A / 10 dB) = 0,504 mW
a["fy7-16-L1-08"] = 10 * log10(2) / 0.20             # A = 10 dB · lg 2 = 3,01 dB; L = A / a = 15,05 km
# L2-05: efficiency vs distance, linear interpolation between (10 mm; 58 %) and (15 mm; 44 %) at 50 %
a["fy7-16-L2-05"] = 10 + (15 - 10) * (58 - 50) / (58 - 44)  # 12,86 mm
# L2-06: attenuation of each fibre length, least-squares line through the origin (slope = sum(L A) / sum(L²))
fibre_L = [10, 20, 30, 40, 50]
fibre_P = [488, 327, 196, 129, 79.1]
fibre_A = [10 * log10(800 / q) for q in fibre_P]
a["fy7-16-L2-06"] = sum(x * y for x, y in zip(fibre_L, fibre_A)) / sum(x * x for x in fibre_L)  # 0,2003 dB/km
a["fy7-16-L2-07"] = 100 * 10 ** (-20 / 10)           # 20 dB -> power ratio 10^-2 = 1,0 %
# YO-skill form (teacher 2026-11-05): L2-08 is an order-of-magnitude choice (no number); t = 2 L n / c = 2 · 1,2e6 m · 1,47 / 3,00e8 m/s = 11,76 ms
# L3-04: charger coil, flux from e0 = N 2πf Φ0, threshold 1,0 V at 100 kHz, interpolate between 12 mm and 16 mm
N4, f4 = 15, 130e3
d4 = [4, 8, 12, 16, 20]
e4 = [4.62, 2.71, 1.52, 0.83, 0.47]
phi4 = [x / (N4 * 2 * pi * f4) * 1e6 for x in e4]    # µWb: 0,377; 0,221; 0,124; 0,0677; 0,0384
phi_min = 1.0 / (N4 * 2 * pi * 100e3) * 1e6          # 0,1061 µWb
for i in range(len(d4) - 1):
    if phi4[i] >= phi_min > phi4[i + 1]:
        a["fy7-16-L3-04"] = d4[i] + (d4[i + 1] - d4[i]) * (phi4[i] - phi_min) / (phi4[i] - phi4[i + 1])  # 13,28 mm
# L3-05: induction hob, P = (2πf B0 π r²)² / (2R) ∝ f² / R; pan C needs f_C = f sqrt(R_C / R_A)
f5, B5, r5 = 30e3, 3.0e-3, 0.090
e05 = 2 * pi * f5 * B5 * pi * r5 ** 2                # 14,39 V
P_A = e05 ** 2 / (2 * 0.040)                         # 2,59 kW (pan A), pan C 1,29 kW
a["fy7-16-L3-05"] = f5 * sqrt(0.080 / 0.040) / 1e3   # 42,43 kHz
# L2-09: figure charger-points; lines at equal flux steps: 6 lines at 3 mm, 4 lines at 6 mm (model flux ratio 0,669: 2,81 V); e0 is proportional to the flux
a["fy7-16-L2-09"] = 4.2 * 4 / 6                      # e0 = 4,2 V · 4 / 6 = 2,8 V
# L2-10: figure graph-curve; the power halves at 10 km (read), A = 10 dB · lg 2 = 3,01 dB; a = A / L = 0,301 dB/km
a_read = 10 * log10(2) / 10                          # 0,301 dB/km
a["fy7-16-L2-10"] = 100 * 10 ** (-(a_read * 70) / 10)  # A = 21,07 dB for 70 km (beyond the 40 km graph); P : P0 = 0,78 %
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
