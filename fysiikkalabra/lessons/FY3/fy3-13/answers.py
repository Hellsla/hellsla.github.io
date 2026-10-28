"""Every answer in exercises.json for fy3-13, computed from the task data (python -I answers.py).
A gas in a closed rigid vessel: p = p0 + k θ; k = (p2 − p1)/(θ2 − θ1); zero pressure at θ0 = −p0/k.
Uncertainty of θ0 from the two extreme lines: Δθ0 = (θmax − θmin)/2. Prints {exercise id: number} as JSON on the last line."""
import json

a = {}
# Level 1: one formula, values given
a["fy3-13-L1-01"] = -98.0 / 0.360                       # line p = 98,0 kPa + 0,360 kPa/°C · θ: θ0 = −p0/k = −272,2 °C
a["fy3-13-L1-02"] = (127 - 105) / (80.0 - 20.0)         # k = Δp/Δθ = 22 kPa / 60 °C = 0,3667 kPa/°C
a["fy3-13-L1-03"] = abs(-267.9 - (-273.15))             # deviation from the accepted value: 5,25 °C (a difference, so K)
a["fy3-13-L1-04"] = (-258 - (-284)) / 2                 # Δθ0 = (θmax − θmin)/2 = (26 °C)/2 = 13 °C
a["fy3-13-L1-05"] = 1.0 / 112 * 100                     # relative uncertainty Δp/p = 1,0 kPa / 112 kPa = 0,893 %
# Level 2: two steps, one conversion or one rearrangement
k = (1.36 - 1.05) / (95.0 - 15.0)                       # slope in bar/°C: 0,31 bar / 80 °C = 0,003875 bar/°C
a["fy3-13-L2-01"] = 15.0 - 1.05 / k                     # θ0 = θ1 − p1/k (zero of p = p1 + k(θ − θ1)) = −255,9 °C
th_hi = -100.0 / 0.380                                  # steep line p = 100 + 0,380 θ: θ0 = −263,16 °C
th_lo = -102.0 / 0.350                                  # shallow line p = 102 + 0,350 θ: θ0 = −291,43 °C
a["fy3-13-L2-02"] = (th_hi - th_lo) / 2                 # Δθ0 = (−263,16 − (−291,43))/2 = 14,1 °C
p_a1, p_a2 = 101.0 + 9.0, 101.0 + 31.0                  # gauge + atmosphere = absolute pressure: 110,0 and 132,0 kPa
k2 = (p_a2 - p_a1) / (90.0 - 30.0)                      # k = 22,0 kPa / 60,0 °C = 0,3667 kPa/°C
a["fy3-13-L2-03"] = 30.0 - p_a1 / k2                    # θ0 = 30,0 − 110,0/0,3667 = −270,0 °C
a["L2-03-gauge-zero"] = 30.0 - 9.0 / k2                                    # gauge pressure zero at 5,45 °C
a["fy3-13-L2-04"] = 0.36 * 0.5 / 1.0 * 100              # temperature error in pressure: 0,36 · 0,5 = 0,18 kPa = 18 % of 1,0 kPa
# Level 3: reasoning or an unfamiliar context
k_s, p0_s = (138.0 - 105.0) / 80.0, 105.0 - (138.0 - 105.0) / 80.0 * 20.0   # steep end-point line: k = 0,4125, p0 = 96,75 kPa
k_l, p0_l = (136.0 - 107.0) / 80.0, 107.0 - (136.0 - 107.0) / 80.0 * 20.0   # shallow end-point line: k = 0,3625, p0 = 99,75 kPa
a["fy3-13-L3-01"] = (-p0_s / k_s - (-p0_l / k_l)) / 2  # θ0: −275,17 and −234,55 °C; Δθ0 = 20,3 °C
a["fy3-13-L3-02"] = 100.0 * 77 / 273.15                 # p proportional to T in kelvin: p(77 K) = 100 kPa · 77/273,15 = 28,2 kPa
a["fy3-13-L3-03"] = (273.15 - 262.0) / 6.0              # deviation 11,15 °C over uncertainty 6 °C = 1,86 times
print(json.dumps({key: round(v, 6) for key, v in a.items()}))
