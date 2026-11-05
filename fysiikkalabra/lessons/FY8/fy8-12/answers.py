"""Every answer in exercises.json for fy8-12, computed from the task data (python -I answers.py).
Ion pairs n = E / W (W = 34 eV in air), photon energy E = hf = hc / λ, gamma attenuation I = I0 (1/2)^(d / d½)
(d = d½ · ln(I0 / I) / ln 2), net count = count - background. h = 6,626e-34 J s, c = 2,998e8 m/s, 1 eV = 1,602e-19 J.
Prints {exercise id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json, math

LN2 = math.log(2)
h, c, e = 6.626e-34, 2.998e8, 1.602e-19
a = {}
# Level 1: one formula, values given
a["fy8-12-L1-01"] = 100 * 0.5 ** (25.0 / 10.4)      # Co-60 gamma, lead d½ 10,4 mm, 25,0 mm: 18,93 % -> 18,9 %
a["fy8-12-L1-02"] = 5.49e6 / 34 / 1e5               # alpha 5,49 MeV, W 34 eV: 1,6147e5 ion pairs -> 1,6 · 10⁵
a["fy8-12-L1-03"] = 18 / 3                          # net count to 1/8 = (1/2)^3 behind 18 mm: d½ = 6,0 mm
a["fy8-12-L1-04"] = 100 * 0.5 ** (30 / 8.1)         # water 30 cm, d½ 8,1 cm: 7,68 % -> 7,7 %
a["fy8-12-L1-05"] = h * c / (12.6 * e) * 1e9        # longest wavelength ionising water: 98,41 nm -> 98,4 nm
# Level 2: two steps, a conversion or a rearrangement
a["fy8-12-L2-01"] = (1260 - 72) / (3.00 * 60)       # net count rate: 1188 pulses in 180 s = 6,60 1/s
a["fy8-12-L2-02"] = 100 * 0.5 ** (10 / 5.5 + 200 / 39)   # 10 mm lead (5,5 mm) + 200 mm concrete (39 mm): 0,81 %
a["fy8-12-L2-03"] = 12 * LN2 / math.log((480 - 5) / (105 - 5))   # 475 -> 100 net behind 12 mm: d½ = 5,34 mm
a["fy8-12-L2-04"] = 10 / 5.5 * 39                   # concrete with as many half-value layers as 10 mm lead: 70,9 mm
# Level 3: reasoning or an unfamiliar context
a["fy8-12-L3-01"] = (5.49e6 / 34 / 4.1) / (1.0e6 / 34 / 360)   # ion pairs per cm, alpha 4,1 cm vs beta 360 cm: 482
net0, net1 = 2400 - 30, 630 - 30                    # pulses/min without and behind 11,0 mm lead, background 30
d_half = 11.0 * LN2 / math.log(net0 / net1)         # 5,550 mm
a["fy8-12-L3-02"] = d_half * math.log(net0 / 30) / LN2   # net down to the background 30/min: 34,99 mm -> 35 mm
a["fy8-12-L3-03"] = 12.6 / (h * 2.45e9 / e) / 1e6   # 2,45 GHz photon 1,0134e-5 eV; 12,6 eV is 1,243e6 times as much
# Added exercises (L1-06..08, L2-05..07, L3-04..05); L1-06, L1-08 and L2-07 are multiple choice (no number)
a["fy8-12-L1-07"] = 1215 / (45 / 60) - 90           # 45 s count to pulses/min, minus background 90/min: 1530/min
counts = [52, 45, 49, 57, 44, 48, 51, 42, 50, 46]   # L2-05: ten 10 s counts, sum 484, mean 48,4
a["fy8-12-L2-05"] = 100 * math.sqrt(sum(counts)) / sum(counts)   # relative uncertainty of the total: 22/484 = 4,545 % -> 4,5 %
net_pb = [(d, n - 50) for d, n in [(3, 1290), (6, 890), (9, 640), (12, 440), (15, 315)]]   # L2-06: background 50 per 60 s
d_lead = [d * LN2 / math.log((1850 - 50) / n) for d, n in net_pb]   # d½ from each measurement
a["fy8-12-L2-06"] = sum(d_lead) / len(d_lead)       # mean 5,499 mm -> 5,5 mm
net_fe = [(d, n - 40) for d, n in [(6, 1895), (12, 1330), (18, 950), (24, 685), (30, 495)]]   # L3-04: background 40 per 60 s
d_fe = [d * LN2 / math.log((2640 - 40) / n) for d, n in net_fe]
a["fy8-12-L3-04"] = sum(d_fe) / len(d_fe)           # mean 11,99 mm -> 12,0 mm (iron, 12 mm)
src, bkg = [1010, 987, 1032, 1001, 1020], [24, 29, 22, 27, 28]   # L3-05: pulses per 60 s with and without the source
R = (sum(src) - sum(bkg)) / 5 / 60                  # net count rate 16,4 1/s
T = 0.5 ** (8.0 / 5.5)                              # lead wall 8,0 mm, d½ 5,5 mm: 0,3649
a["fy8-12-L3-05"] = R / (T * 0.015) / 1000          # A = R / (T eta) = 2997 Bq -> 3,0 kBq
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
