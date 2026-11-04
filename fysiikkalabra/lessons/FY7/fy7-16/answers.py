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
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
