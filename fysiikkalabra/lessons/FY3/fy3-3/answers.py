# fy3-3: computes every exercise answer; the last line printed is {exercise id: value}.
import json
C0 = 273.15                                   # T = theta + 273,15
a = {}
a["fy3-3-L1-01"] = round(21 + C0)             # 294,15 K -> 294 K
a["fy3-3-L1-02"] = round(350 - C0)            # 76,85 °C -> 77 °C
a["fy3-3-L1-03"] = round(77.4 - C0)           # -195,75 °C -> -196 °C
a["fy3-3-L1-04"] = 45 - 20                    # dT = dtheta = 25 K
a["fy3-3-L1-05"] = round(2.7 - C0, -1)        # -270,45 °C -> -270 °C
a["fy3-3-L2-01"] = round(288 + 45 - C0)       # T2 = 333 K -> 59,85 °C
k = (123 - 90.0) / 100                        # slope 0,33 kPa/°C
a["fy3-3-L2-02"] = round(90.0 + k * 35)       # 101,55 kPa
k = (102.5 - 75) / (100 - 0)               # figure fy3-3/extrapolation-points: points (0 °C; 75 kPa) ... (100 °C; 102,5 kPa), slope 0,275 kPa/°C
a["fy3-3-L2-03"] = 75 + k * (-100 - 0)        # 47,5 kPa
a["fy3-3-L2-04"] = round((127 + C0) / (-173 + C0), 1)  # 400,15 / 100,15 = 3,9955
a["fy3-3-L3-01"] = round(300 * (35 + C0) / (15 + C0))  # 320,8 kPa
a["fy3-3-L3-02"] = round((27.0 + C0) * 200 / 150 - C0)  # T2 = 400,2 K -> 127,05 °C
a["fy3-3-L3-03"] = round((20.0 + C0) / 2 - C0)          # T2 = 146,575 K -> -126,575 °C
# Exercise-bank additions (L1-06 and L1-08 are multiple choice: no number)
a["fy3-3-L1-07"] = round(-18 + C0)            # 255,15 K -> 255 K
d_ = [1.4, 1.7, 1.3, 1.6, 1.5]                 # L2-05: theta_A - theta_vert for vert 0, 20, 40, 60, 80 °C (A: 1,4; 21,7; 41,3; 61,6; 81,5); sum 7,5
a["fy3-3-L2-05"] = round(sum(d_) / 5, 1)       # mean difference 1,5 K (corrected bath 38,6 - 1,5 = 37,1 °C)
th = [80.0, 69.9, 61.3, 54.4, 48.6]            # L2-06: thermos water at 0...4 h, room 20,0 °C
a["fy3-3-L2-06"] = round((th[0] - th[1]) / (th[3] - th[4]), 1)   # 10,1 K / 5,8 K = 1,741 -> 1,7
rd = [21.0, 48.2, 56.6, 59.3, 59.9, 60.2, 60.2]   # L2-07: reading every 10 s, settles at 60,2 °C
a["fy3-3-L2-07"] = 10 * next(i for i, x in enumerate(rd) if 60.2 - x < 0.5)   # 30 s: 0,9 K, 40 s: 0,3 K -> 40 s
fore, mouth = [36.2, 36.7, 36.0, 36.5, 36.6], [37.0, 37.0, 37.1, 36.9, 37.0]   # L3-04 (ear 36,9; 37,1; 36,8; 37,0; 37,2)
a["fy3-3-L3-04"] = round(sum(mouth) / 5 - sum(fore) / 5, 1)   # 37,0 - 36,4 = 0,6 K (half ranges 0,2; 0,35; 0,1 K; 37,6 - 0,6 = 37,0 °C < 37,5 °C)
p1, p3 = 600 + 101, 900 + 101                  # L3-05: total pressures 701 kPa and 1001 kPa; T1 = 293,15 K
a["fy3-3-L3-05"] = round((20.0 + C0) * p3 / p1 - C0)   # T3 = 418,6 K -> 145,5 °C -> 145 °C (at 60,0 °C: 796,7 kPa total, 695,7 kPa gauge, KE +13,6 %)
a["fy3-3-L1-10"] = -196 + C0                       # MAFY (Aineiden olomuodon muutokset: Kaasut) N2 boiling point -196 °C -> 77,15 K -> 77 K
a["fy3-3-L2-08"] = (90 - 75) / ((102.5 - 75) / (100 - 0))   # figure fy3-3/extrapolation-points (points given in the task text): slope 0,275 kPa/°C, p = 90 kPa at theta = 15 / 0,275 = 54,5 °C
print(json.dumps(a))
