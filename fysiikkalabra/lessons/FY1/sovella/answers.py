"""FY1 Sovella itsenäisesti: every number of the worked solutions, recomputed from the task data.
Prints {"<task>-<part>": value} for the parts with an answer in tasks.json; `python scripts/practice.py check` compares them."""
import json
from statistics import mean

# fy1-s1: the ball on the floor (t >= 0,6 s; the ramp ends about 16 cm from the start)
t = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0]
s = [0.0, 38.9, 157.9, 320.9, 477.4, 640.2, 799.2, 957.3, 1120.0, 1277.2, 1439.6]   # mm
floor = [(a, b / 1000) for a, b in zip(t, s) if a >= 0.6]
tm, sm = mean(a for a, _ in floor), mean(b for _, b in floor)
k = sum((a - tm) * (b - sm) for a, b in floor) / sum((a - tm) ** 2 for a, _ in floor)   # least squares, m/s
b0 = sm - k * tm
read = (1.44 - 0.32) / (2.0 - 0.6)          # two points read off the fitted line in the solution
at10 = k * 10 + b0

# fy1-s2: the repeated measurements
steel = [2.31, 2.45, 2.38, 2.29, 2.42]
plastic = [2.40, 2.33, 2.47, 2.36, 2.44]
half = lambda xs: (max(xs) - min(xs)) / 2

out = {"fy1-s1-b": round(read, 3), "fy1-s1-fit": round(k, 4), "fy1-s1-intercept": round(b0, 4), "fy1-s1-at10": round(at10, 2),
       "fy1-s2-steel": round(mean(steel), 3), "fy1-s2-plastic": round(mean(plastic), 3),
       "fy1-s2-dsteel": round(half(steel), 3), "fy1-s2-dplastic": round(half(plastic), 3),
       "fy1-s2-b": round(mean(plastic) - mean(steel), 3)}
print(json.dumps(out))
