"""Every answer in exercises.json for fy5-10, computed from the task data (python -I answers.py).
The wave equation v = fλ = λ/T (f = 1/T), and for a pulse or a crest v = s/t (constant speed in one medium).
Prints {exercise id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json

a = {}
# Level 1: one formula, values given
a["fy5-10-L1-01"] = 4.0 * 0.75                 # spring: v = fλ = 4,0 Hz · 0,75 m = 3,0 m/s
a["fy5-10-L1-02"] = round(343 / 440, 2)                 # loudspeaker in air: λ = v/f = 343 m/s / 440 Hz = 0,7795 m -> 0,780 m
a["fy5-10-L1-03"] = 6.0 / 1.5                  # rope: f = v/λ = 6,0 m/s / 1,5 m = 4,0 Hz
a["fy5-10-L1-04"] = 4.0 / 2.5                  # wave pool: v = λ/T = 4,0 m / 2,5 s = 1,6 m/s
a["fy5-10-L1-05"] = 1.2 / 4.8                  # rope: T = λ/v = 1,2 m / 4,8 m/s = 0,25 s
# Level 2: two steps, a conversion or a graph
T_graph = 2.0 / 5                              # figure fy5-10/yt-kuvaaja: 5 full periods in 2,0 s (upward zero crossings 0 and 0,40 s), T = 0,40 s
a["fy5-10-L2-01"] = 1.0 / T_graph              # crests 1,0 m apart: v = λ/T = 2,5 m/s
f_hand = 18 / 12.0                             # 18 full swings in 12,0 s: f = 1,5 Hz
a["fy5-10-L2-02"] = f_hand * 1.40              # v = fλ = 1,5 Hz · 1,40 m = 2,10 m/s
f_sound = 343 / 0.750                          # in air: f = v/λ = 457,3 Hz; the frequency is kept in the water
a["fy5-10-L2-03"] = 1480 / f_sound             # λ_water = v_water / f = 3,236 m -> 3,24 m
a["fy5-10-L2-04"] = 0.50 * 12 * 1000           # quake wave: v = fλ = 0,50 Hz · 12 000 m = 6000 m/s
# Level 3: reasoning or an unfamiliar context
v_crest = (1.05 - 0.60) / 0.15                 # the same crest moved 0,45 m in 0,15 s (less than one λ): v = 3,0 m/s
a["fy5-10-L3-01"] = v_crest / 1.20             # f = v/λ = 3,0 m/s / 1,20 m = 2,5 Hz
# rail: the sound in the steel arrives first; Δt = d/v_air − d/v_steel  ->  d = Δt / (1/v_air − 1/v_steel)
a["fy5-10-L3-02"] = 0.50 / (1 / 340 - 1 / 5100)   # 182,1 m -> 180 m (Δt has two figures)
v_stadium = 0.55 / 0.050                       # each spectator rises 0,050 s after the neighbour 0,55 m away: v = 11 m/s
a["fy5-10-L3-03"] = 440 / v_stadium            # once round the 440 m ring: t = s/v = 40 s
# Added exercises (L1-06 and L1-07 are multiple choice and have no number here)
a["fy5-10-L1-08"] = 343 * 4.0 / 1000                    # thunder: d = v t = 343 m/s · 4,0 s = 1372 m = 1,372 km -> 1,4 km
x = [0.10, 0.62, 1.13, 1.66, 2.17, 2.70]; tt = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
a["fy5-10-L2-05"] = round((x[-1] - x[0]) / (tt[-1] - tt[0]), 1)   # slope of the fitted line through the end points: 2,60 -> 2,6 m/s
a["fy5-10-L2-06"] = 1.5 / 0.50                          # (t,y) peaks 0,50 s = T; (x,y) crests 1,5 m = λ: v = λ/T = 3,0 m/s
a["fy5-10-L2-07"] = round((2.00 - 0.50) / ((5.9 - 1.5) * 1e-3), -1)   # slope of d(Δt): 1,50 m / 4,4 ms = 340,9 m/s -> 3,4·10² m/s (two figures)
# L3-04: v = L/t for each tension; v²/F is constant, C = mean(v²/F) = 22,0; at 30 N v = sqrt(CF), λ = v/f
Fs = [5.0, 10.0, 20.0, 40.0]; ts = [1.15, 0.800, 0.570, 0.410]
ks = [round(12.0 / t, 1) ** 2 / F for t, F in zip(ts, Fs)]
k = round(sum(ks) / 4, 1)                               # 22,0
a["fy5-10-L3-04"] = round((k * 30) ** 0.5 / 5.0, 1)     # v = 25,7 m/s, λ = 5,1 m
# L3-05: v = fλ in both parts of the rope (f is kept), t = L1/v1 + L2/v2 = 2,5 s + 2,4 s
a["fy5-10-L3-05"] = 10.0 / (5.0 * 0.80) + 6.0 / (5.0 * 0.50)   # 4,9 s
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
