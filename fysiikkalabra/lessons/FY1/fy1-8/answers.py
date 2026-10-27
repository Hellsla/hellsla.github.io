"""Every answer in exercises.json for fy1-8, computed from the task data (python -I answers.py).
Relative uncertainty: eps = dt / t. Mean of repeats, half of the range as the uncertainty, s = v t, slope = (s2 - s1) / (t2 - t1).
Prints {exercise id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json

a = {}
# Level 1: one formula, values given
a["fy1-8-L1-01"] = 0.2 / 4.0 * 100                        # eps = dt / t = 0,2 s / 4,0 s = 0,050 -> 5,0 %
a["fy1-8-L1-02"] = (12.3 + 12.5 + 12.2 + 12.6 + 12.4) / 5   # mean = 62,0 s / 5 = 12,4 s
a["fy1-8-L1-03"] = 1.50 / 3.6                             # v = s / t = 1,50 m / 3,6 s = 0,4167 m/s -> 0,42 m/s
l = [24.1, 24.4, 24.0, 24.3, 24.2]
a["fy1-8-L1-04"] = (max(l) - min(l)) / 2                  # half of the range = (24,4 - 24,0) cm / 2 = 0,2 cm
a["fy1-8-L1-05"] = 0.15 / 4.73 * 100                      # record row: eps = dt / mean t = 0,15 s / 4,73 s = 0,0317 -> 3,2 %
# Level 2: two steps, a conversion or a rearrangement
t = [7.8, 8.2, 7.9, 8.1, 8.0]
a["fy1-8-L2-01"] = (max(t) - min(t)) / 2 / (sum(t) / len(t)) * 100   # half-range 0,2 s, mean 8,0 s -> 0,2 / 8,0 = 2,5 %
t_run = 3.0 / 1.5                                         # t = s / v = 3,0 m / 1,5 m/s = 2,0 s
a["fy1-8-L2-02"] = 0.2 / t_run * 100                      # eps = 0,2 s / 2,0 s = 10 %
a["fy1-8-L2-03"] = (342 - 90) / (8.0 - 2.0) / 100         # slope = 252 cm / 6,0 s = 42 cm/s = 0,42 m/s
a["fy1-8-L2-04"] = abs(0.50 - 0.42) / 0.50 * 100          # |0,50 - 0,42| m/s / 0,50 m/s = 0,16 -> 16 %
# Level 3: reasoning or an unfamiliar context
a["fy1-8-L3-01"] = (0.463 - 0.397) / 2                    # uncertainty of the slope = half the gap of the steepest and shallowest line = 0,033 m/s
r1 = (80.0 - 68.0) / 5.0                                  # first 5 min: 12,0 K / 5,0 min = 2,4 K/min
r2 = (52.0 - 47.0) / 5.0                                  # last 5 min: 5,0 K / 5,0 min = 1,0 K/min
a["fy1-8-L3-02"] = r1 - r2                                # difference of the cooling rates = 1,4 K/min
a["fy1-8-L3-03"] = (60 - 12) / (6 * 2.0)                  # time for repeats 48 min / (6 distances * 2,0 min) = 4,0 repeats
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
