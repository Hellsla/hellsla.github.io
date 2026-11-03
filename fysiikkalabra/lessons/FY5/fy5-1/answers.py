"""Every answer in exercises.json for fy5-1, computed from the task data (python -I answers.py).
Moment M = F r with the arm r the perpendicular distance from the axis to the force's line of action; r = d sin α when
the force is at the angle α to the line from the axis to its point of application; counterclockwise positive.
Prints {id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json, math

s = lambda deg: math.sin(math.radians(deg))
c = lambda deg: math.cos(math.radians(deg))
a = {}
# Level 1: one formula
a["fy5-1-L1-01"] = 150 * 0.25                       # wrench, perpendicular: M = F r = 37,5 Nm
a["fy5-1-L1-02"] = 12 * 0.80                        # door handle, perpendicular push: M = 9,6 Nm
a["fy5-1-L1-03"] = 45 / 0.30                        # force needed: F = M / r = 150 N
a["fy5-1-L1-04"] = 40 * (3 * 0.10)                  # grid figure: line of action 3 squares (0,30 m) from O → M = 12 Nm
a["fy5-1-L1-05"] = 18 / 60                          # arm: r = M / F = 0,30 m
# Level 2: an angle, a conversion or two moments
a["fy5-1-L2-01"] = 40 * 0.75 * s(35)                # door pulled by a rope at 35° to the door: M = F d sin α = 17,2 Nm
a["fy5-1-L2-02"] = 85 * (35 / 100)                  # 35 cm = 0,35 m: M = 29,75 Nm ≈ 30 Nm
a["fy5-1-L2-03"] = 30 * 0.50 - 40 * 0.20            # ΣM = 15 Nm − 8,0 Nm = 7,0 Nm (counterclockwise)
a["fy5-1-L2-04"] = 50 / (0.25 * s(60))              # valve lever: F = M / (d sin α) = 231 N
# Level 3: reasoning
a["fy5-1-L3-01"] = 500 * 0.175 * c(45)              # pedal 45° below the horizontal, force straight down: r = d cos 45° → 61,9 Nm
a["fy5-1-L3-02"] = (50 * 0.40) / 20                 # equal moments: r = F₁r₁ / F₂ = 1,0 m
a["fy5-1-L3-03"] = 120 * 0.20 + 120 * 0.20          # cross wrench, two opposite hands both turning the same way: ΣM = 48 Nm
print(json.dumps(a))
