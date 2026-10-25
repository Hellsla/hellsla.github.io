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
k = (137 - 110) / (80 - 10)                   # slope 0,3857 kPa/°C
a["fy3-3-L2-03"] = round(110 + k * (-50 - 10))  # 86,86 kPa
a["fy3-3-L2-04"] = round((127 + C0) / (-173 + C0), 1)  # 400,15 / 100,15 = 3,9955
a["fy3-3-L3-01"] = round(300 * (35 + C0) / (15 + C0))  # 320,8 kPa
a["fy3-3-L3-02"] = round((27.0 + C0) * 200 / 150 - C0)  # T2 = 400,2 K -> 127,05 °C
a["fy3-3-L3-03"] = round((20.0 + C0) / 2 - C0)          # T2 = 146,575 K -> -126,575 °C
print(json.dumps(a))
