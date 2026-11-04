"""Every answer in exercises.json for fy7-15, computed from the task data (python -I answers.py).
Ideal polariser: unpolarised light I -> I / 2; Malus's law I = I0 cos² θ for polarised light; Brewster's law
tan α_B = n2 / n1, and at the Brewster angle the reflected and refracted rays are perpendicular (α_B + α2 = 90°).
Prints {exercise id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json
from math import cos, tan, atan, acos, sqrt, degrees, radians

a = {}
# Level 1: one formula, values given
a["fy7-15-L1-01"] = 640 / 2                                  # unpolarised 640 W/m² through one polariser: 320 W/m²
a["fy7-15-L1-02"] = 200 * cos(radians(30.0)) ** 2            # polarised 200 W/m², 30,0°: 150 W/m²
a["fy7-15-L1-03"] = 80.0 * cos(radians(70.0)) ** 2           # polarised 80,0 W/m², 70,0°: 9,358 W/m² -> 9,36
a["fy7-15-L1-04"] = degrees(atan(1.49 / 1.00))               # air -> acrylic: α_B = 56,13° -> 56,1°
a["fy7-15-L1-05"] = degrees(atan(2.42 / 1.00))               # air -> diamond: α_B = 67,548° -> 67,5°
# Level 2: two steps, a rearrangement or a conversion
a["fy7-15-L2-01"] = 900 / 2 * cos(radians(40.0)) ** 2        # unpolarised 900 W/m², two polarisers at 40,0°: 264,07 W/m²
a["fy7-15-L2-02"] = degrees(acos(sqrt(0.250)))               # I / I0 = 0,250 = cos² θ: θ = 60,0°
a["fy7-15-L2-03"] = tan(radians(57.5))                       # Brewster angle 57,5° from air: n = tan 57,5° = 1,5697 -> 1,57
a["fy7-15-L2-04"] = 90 - degrees(atan(1.50))                 # glass 1,50 at α_B = 56,31°: α2 = 90° − α_B = 33,69° -> 33,7°
# Level 3: reasoning, two ideas or an unfamiliar context
a["fy7-15-L3-01"] = 800 / 2 * cos(radians(30.0)) ** 2 * cos(radians(60.0)) ** 2   # crossed pair with a middle one at 30°: 75,0 W/m²
a["fy7-15-L3-02"] = degrees(atan(1.00 / 1.33))               # light in water reflecting off the surface: α_B = 36,94° (< α_r = 48,8°)
a["fy7-15-L3-03"] = 16 + (420 - 16) * cos(radians(60.0)) ** 2   # background 16 lx + Malus part 404 lx · cos² 60° = 117 lx
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
