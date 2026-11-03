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
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
