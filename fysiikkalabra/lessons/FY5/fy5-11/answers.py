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
# Level 2: two steps, a conversion or a rearrangement
a["fy5-11-L2-01"] = 0.60 * math.sin(math.radians(30)) / 0.40   # front reaches A, then B 0,60 m away: extra path d sin α = 0,30 m, Δt = 0,30 m / 0,40 m/s = 0,75 s
a["fy5-11-L2-02"] = 2 * 8.0 / 3.2                        # pulse to the fixed end and back: v = 2L/t = 16,0 m / 3,2 s = 5,0 m/s
a["fy5-11-L2-03"] = 343 * 0.40 / 2 + 343 * 0.70 / 2      # two cliffs: 68,6 m + 120,05 m = 188,65 m -> 190 m
a["fy5-11-L2-04"] = 343 / 0.90                           # λ = b = 0,90 m: f = v/λ = 381,1 Hz -> 380 Hz
# Level 3: reasoning or an unfamiliar context
# L3-01 (words): window b = 0,80 m; λ at 100 Hz = 3,43 m (b/λ 0,23), at 5000 Hz = 0,0686 m (b/λ 11,7)
lam_100, lam_5000 = 343 / 100, 343 / 5000
a["fy5-11-L3-02"] = math.degrees(math.asin(0.30 * 0.50 / 0.40))   # Huygens: sin α = vΔt/d = 0,30 · 0,50 / 0,40 = 0,375 -> 22,02°
a["fy5-11-L3-03"] = 3 * 6.0 / 4.0                        # pulse to the far end, back to the hand, to the far end again: 3L/v = 18 m / 4,0 m/s = 4,5 s
# L3-03 direction: inverted at the fixed far end, inverted again at the held end -> upward again
# L3-01 numbers for the model answer: b/λ at 100 Hz and at 5000 Hz
_info = {"L3-01 b/lam 100 Hz": 0.80 / lam_100, "L3-01 b/lam 5000 Hz": 0.80 / lam_5000}
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
