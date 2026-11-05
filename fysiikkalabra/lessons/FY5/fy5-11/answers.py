"""Every answer in exercises.json for fy5-11, computed from the task data (python -I answers.py).
Reflection law: the angles are measured from the normal, β = α. Echo and rope pulses travel to the reflector and back.
λ = v/f (chapter Mekaaninen aaltoliike); diffraction is strong when the gap is about λ or narrower.
Prints {exercise id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json, math

a = {}
# Level 1: one formula, values given
a["fy5-11-L1-01"] = 35                                   # β = α = 35°
a["fy5-11-L1-02"] = 90 - 20                              # the ray makes 20° with the surface: α = 90° − 20° = 70°
a["fy5-11-L1-03"] = 0.24 / 8.0 * 100                     # λ = v/f = 0,24 m/s : 8,0 Hz = 0,030 m = 3,0 cm
# L1-04: a free end (a ring sliding on a rod) does not invert the pulse: answered in words
a["fy5-11-L1-05"] = 343 * 1.4 / 2                        # echo from a cliff: d = v t / 2 = 343 m/s · 1,4 s / 2 = 240,1 m -> 240 m
# L1-06 (words): fixed end, the wall pulls the rope down -> the pulse returns inverted
# L1-07 (words): f doubled, v same -> λ = 2,0 cm, b/λ 0,75 -> 1,5: diffraction weakens
a["fy5-11-L1-08"] = 2 * 36 / 1500 * 1000                 # t = 2d/v = 72 m / 1500 m/s = 0,048 s = 48 ms
# Level 2: two steps, a conversion or a rearrangement
a["fy5-11-L2-01"] = 0.60 * math.sin(math.radians(30)) / 0.40   # front reaches A, then B 0,60 m away: extra path d sin α = 0,30 m, Δt = 0,30 m / 0,40 m/s = 0,75 s
a["fy5-11-L2-02"] = 2 * 8.0 / 3.2                        # pulse to the fixed end and back: v = 2L/t = 16,0 m / 3,2 s = 5,0 m/s
a["fy5-11-L2-03"] = 343 * 0.40 / 2 + 343 * 0.70 / 2      # two cliffs: 68,6 m + 120,05 m = 188,65 m -> 190 m
a["fy5-11-L2-04"] = 343 / 0.90                           # λ = b = 0,90 m: f = v/λ = 381,1 Hz -> 380 Hz
a["fy5-11-L2-05"] = 2 * (80.0 - 20.0) / (0.507 - 0.157)  # the reaction time cancels in the difference: v = 2Δd/Δt = 120 m / 0,350 s = 342,9 m/s -> 343 m/s
_lam06 = 0.216 / 12                                      # λ = v/f = 0,018 m = 1,8 cm
a["fy5-11-L2-06"] = 14.4 / (_lam06 * 100)                # b/λ = 14,4 cm / 1,8 cm = 8,0
a["fy5-11-L2-07"] = 64 / 2                               # the normal splits the angle between the rays: 2α = 64°, α = 32°
# Level 3: reasoning or an unfamiliar context
# L3-01 (words): window b = 0,80 m; λ at 100 Hz = 3,43 m (b/λ 0,23), at 5000 Hz = 0,0686 m (b/λ 11,7)
lam_100, lam_5000 = 343 / 100, 343 / 5000
a["fy5-11-L3-02"] = math.degrees(math.asin(0.30 * 0.50 / 0.40))   # Huygens: sin α = vΔt/d = 0,30 · 0,50 / 0,40 = 0,375 -> 22,02°
a["fy5-11-L3-03"] = 3 * 6.0 / 4.0                        # pulse to the far end, back to the hand, to the far end again: 3L/v = 18 m / 4,0 m/s = 4,5 s
# L3-03 direction: inverted at the fixed far end, inverted again at the held end -> upward again
_d = [740 * t_ / 1000 for t_ in (54, 60, 71, 90, 97, 85)]   # d = v t / 2, v = 1480 m/s: 40,0 / 44,4 / 52,5 / 66,6 / 71,8 / 62,9 m
_slopes = [math.degrees(math.atan(abs(_d[i + 1] - _d[i]) / 20.0)) for i in range(5)]   # 12,5 / 22,1 / 35,1 / 14,5 / 23,9 degrees
a["fy5-11-L3-04"] = max(_slopes)                         # steepest section x = 40...60 m: atan(14,06 / 20,0) = 35,1°
# L3-05: λ_AM = c/f = 333 m (b/λ 1,8), λ_FM = 3,00 m, λ_tv = 0,500 m (b/λ 1200); key result b/λ_FM
a["fy5-11-L3-05"] = 600 / (3.00e8 / 100e6)               # b/λ_FM = 600 m / 3,00 m = 200
# L3-01 numbers for the model answer: b/λ at 100 Hz and at 5000 Hz
_info = {"L3-01 b/lam 100 Hz": 0.80 / lam_100, "L3-01 b/lam 5000 Hz": 0.80 / lam_5000}
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
