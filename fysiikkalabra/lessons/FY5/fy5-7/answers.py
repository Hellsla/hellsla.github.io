"""Every answer in exercises.json for fy5-7, computed from the task data (python -I answers.py).
Periodic motion: f = 1/T, T = t/n for n full oscillations in time t, A = half the distance between the extreme positions,
x(t) = A sin(2πt/T) = A sin(2πft) with the argument in radians; a sine fit A sin(Bt + C) + D has B = 2π/T.
Prints {exercise id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json, math

pi = math.pi
a = {}
# Level 1: one formula, values given
a["fy5-7-L1-01"] = 1 / 0.40                              # weight on a spring: f = 1 / 0,40 s = 2,5 Hz
a["fy5-7-L1-02"] = 1 / 196 * 1000                        # guitar string: T = 1 / 196 Hz = 0,005102 s = 5,10 ms
a["fy5-7-L1-03"] = 2.5                                   # graph l1-kuvaaja: the curve reaches +2,5 cm and −2,5 cm -> A = 2,5 cm
a["fy5-7-L1-04"] = 36 / 20                               # pendulum: T = t / n = 36 s / 20 = 1,8 s
a["fy5-7-L1-05"] = 4 * 4.0                               # one period: up A, down 2A, back A = 4A = 16 cm
# Level 2: two steps, a conversion or a rearrangement
a["fy5-7-L2-01"] = 3.0 * math.sin(2 * pi * 0.10 / 0.50)   # graph l2-kuvaaja: A = 3,0 cm, T = 0,50 s; x(0,10 s) = 2,853 cm -> 2,9 cm
a["fy5-7-L2-02"] = 12.6 / (2 * pi)                       # sine fit B = 2π/T: f = 1/T = B / (2π) = 2,005 Hz -> 2,01 Hz
f_needle = 900 / 60                                      # sewing machine: 900 1/min = 900 / 60 s = 15 Hz
a["fy5-7-L2-03"] = 1 / f_needle * 1000                   # T = 1 / 15 Hz = 0,0667 s = 66,7 ms -> 67 ms
a["fy5-7-L2-04"] = (47.0 - 32.0) / 2                     # motion sensor distances 32,0 … 47,0 cm: A = 15,0 cm / 2 = 7,50 cm
# Level 3: reasoning, two ideas, an unfamiliar context
a["fy5-7-L3-01"] = 1.2 * math.asin(0.5) / (2 * pi)       # x = A/2: sin(2πt/T) = 1/2, 2πt/T = π/6, t = T/12 = 0,10 s
f_disc = 45 / 60                                         # disc 45 1/min = 0,75 Hz; the shadow oscillates with A = r = 15 cm
a["fy5-7-L3-02"] = 15 * math.sin(2 * pi * f_disc * 0.20) # x = 15 cm · sin(2π · 0,75 Hz · 0,20 s) = 12,14 cm -> 12 cm
a["fy5-7-L3-03"] = 1.8                                   # in step again: the smallest time that is a whole number of both
                                                         # periods, 3 · 0,60 s = 2 · 0,90 s = 1,8 s
# Exercise-bank additions
a["fy5-7-L1-07"] = 40 / 1.6                              # n / f = 40 / 1,6 Hz = 25 s
a["fy5-7-L2-05"] = 1 / ((3.47 - 0.42) / 5)               # peaks 1…6 = five periods: T = 3,05 s / 5 = 0,61 s, f = 1,639 Hz -> 1,64 Hz
a["fy5-7-L2-06"] = (15.2 + 14.8 + 15.4 + 15.0 + 15.1) / 5 / 10   # sum 75,5 s, mean 15,1 s for 10 swings, T = 1,51 s
a["fy5-7-L2-07"] = 1 / ((1.49 - 0.00) / 2)               # upward crossings 0,00 s and 1,49 s are two periods: T = 0,745 s, f = 1,342 Hz -> 1,34 Hz
T_rest, T_ex = 4.96 / 6, 2.77 / 6                        # R peaks: six beat intervals each, T = t6 / 6
a["fy5-7-L3-04"] = (1 / T_ex - 1 / T_rest) / (1 / T_rest) * 100   # pulse 72,58 -> 129,96 1/min: +79,06 % -> 79 %
D_fit, A_fit, T_fit = (46.0 + 34.0) / 2, (46.0 - 34.0) / 2, 1.6   # table: D = 40,0 cm, A = 6,0 cm, T = 1,6 s
a["fy5-7-L3-05"] = D_fit + A_fit * math.sin(2 * pi * 5.0 / T_fit)  # t = 5,0 s = 3,125 periods: 40,0 + 6,0 · sin 45° = 44,24 cm
assert abs(3 * 0.60 - 2 * 0.90) < 1e-12 and all(abs(k * 0.60 - m * 0.90) > 1e-9 for k in (1, 2) for m in (1,))
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
