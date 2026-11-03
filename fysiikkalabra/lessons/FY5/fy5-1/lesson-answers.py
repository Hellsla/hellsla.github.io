"""Numbers of the lesson text and inquiry.json for fy5-1, computed from their data (python -I lesson-answers.py); the
exercises' answers are in answers.py. Moment M = F r, arm r = d sin α (α between the force and the line from the axis
to the point of application); counterclockwise positive; g = 9,81 m/s². Prints {id: number} as JSON."""
import json, math

g = 9.81
s = lambda deg: math.sin(math.radians(deg))
c = lambda deg: math.cos(math.radians(deg))
a = {}
# Worked example: wrench, hand 0,35 m from the axis, 240 N at 65° to the handle; the nut needs 80 Nm
a["ex-r"] = 0.35 * s(65)                          # r = d sin α = 0,317 m
a["ex-M"] = 240 * 0.35 * s(65)                    # M = F d sin α = 76,1 Nm < 80 Nm
a["ex-M-perp"] = 240 * 0.35                       # Järkevyys: pulled at 90°, M = F d = 84 Nm
a["ex-F-perp-needed"] = 80 / 0.35                 # Järkevyys: at 90° the nut opens from F = 229 N up
# Simulation model: the tight nut needs 30 Nm, the rusty one 60 Nm
M_tight, M_rusty = 30, 60
# pred-1 / exp-1 (tight nut, α = 90°): the smallest opening force at each grip distance, F = M0 / d
for d in (0.10, 0.15, 0.20, 0.25, 0.30):
    a[f"exp1-F-{d:.2f}"] = M_tight / d             # 300, 200, 150, 120, 100 N (on the slider's 10 N steps)
a["exp1-question"] = 150 * 0.20                   # the row d = 0,20 m: M = F d = 30 Nm
a["exp1-mistake-ratio"] = 150 / 0.20              # mistake F/d = 750
# pred-2 / exp-2 (rusty nut, F = 200 N, d = 0,40 m): moment and arm by angle
for al in (15, 30, 45, 60, 90, 120, 135, 150):
    a[f"exp2-r-{al}"] = 0.40 * s(al)               # r = d sin α: 0,20 m at 30° and 150°, 0,40 m at 90°
    a[f"exp2-M-{al}"] = 200 * 0.40 * s(al)         # M = 80 Nm at 90°, 69 Nm at 60°, 57 Nm at 45°, 40 Nm at 30°
# kertaus: vertical component of 200 N at 30° above the horizontal
a["kertaus-Fy"] = 200 * s(30)                     # 100 N (mistake F cos α = 173 N)
a["kertaus-Fx"] = 200 * c(30)
# virhe: 50 N at 30° to a 0,40 m handle; the student wrote M = F d
a["virhe-wrong"] = 50 * 0.40                      # 20 Nm (the error)
a["virhe-right"] = 50 * 0.40 * s(30)              # 10 Nm
a["virhe-cos"] = 50 * 0.40 * c(30)                # 17,3 Nm (cos for sin)
# siirto: a 12 kg barrier arm, 3,0 m long, raised 40° above the horizontal; weight at its middle 1,5 m from the axis
G = 12 * g                                        # 117,7 N
a["siirto-G"] = G
a["siirto-r"] = 1.5 * c(40)                       # the weight is vertical, so its arm is the horizontal distance 1,149 m
a["siirto"] = G * 1.5 * c(40)                     # M = G · 1,5 m · cos 40° = 135 Nm (clockwise)
a["siirto-Gd"] = G * 1.5                          # mistake: G d = 177 Nm
a["siirto-sin"] = G * 1.5 * s(40)                 # mistake: sin for cos, 113 Nm
a["siirto-full"] = G * 3.0 * c(40)                # mistake: the whole length 3,0 m, 271 Nm
# check-2: steering wheel radius 0,19 m, 25 N counterclockwise and 15 N clockwise, both tangential
a["check2"] = 25 * 0.19 - 15 * 0.19               # ΣM = 1,9 Nm counterclockwise
a["check2-sum"] = 25 * 0.19 + 15 * 0.19           # mistake: 7,6 Nm
a["check2-rev"] = 15 * 0.19 - 25 * 0.19           # mistake: sign, −1,9 Nm
# exit ticket: 100 N at 0,20 m against 50 N at 0,50 m
a["exit-1"] = 100 * 0.20                          # 20 Nm
a["exit-2"] = 50 * 0.50                           # 25 Nm
print(json.dumps(a))
