"""Numbers of the lesson text and inquiry.json for fy7-12, computed from their data (python -I lesson-answers.py); the
exercises' answers are in answers.py. Critical angle sin α_r = n2 / n1 (n1 > n2), from n1 sin α1 = n2 sin α2 with
α2 = 90°; speed in a medium v = c / n; travel time t = s / v. Prints {id: number} as JSON."""
import json
from math import asin, sin, cos, tan, sqrt, degrees, radians

a = {}
c = 3.00e8                                          # speed of light in vacuum (m/s)
# Ydinajatus figure: lamp under water (n = 1,33), rays at 30°, α_r and 65° to the normal
a["fig-water-ar"] = degrees(asin(1 / 1.33))         # α_r = 48,75° -> 48,8°
a["fig-water-30"] = degrees(asin(1.33 * sin(radians(30))))   # 30° in water -> 41,7° in air
# Kaava graph: α_r against n1 into air (n2 = 1,00)
a["graph-water"] = degrees(asin(1 / 1.33))          # 48,8°
a["graph-glass"] = degrees(asin(1 / 1.50))          # 41,8°
a["graph-diamond"] = degrees(asin(1 / 2.42))        # 24,4°
# diamond figure: back facets at 41° to the girdle, a vertical ray meets the first facet at 41° to its normal
a["dia-inc1"] = 41.0                                # 41° > 24,4° (diamond): total reflection; 41° < 41,8° (glass): leaks
# fibre speed in the text: core n = 1,47 -> v = c / n
a["v-fibre"] = c / 1.47                             # 2,04 · 10^8 m/s, "noin 2 · 10^8 m/s"
# worked example: core n1 = 1,48, cladding n2 = 1,46
a["ex-sin"] = 1.46 / 1.48                           # sin α_r = 0,9865
a["ex-ar"] = degrees(asin(1.46 / 1.48))             # α_r = 80,57° -> 80,6°
# simulation (n1 = 1,48): a ray entering the end face at θ to the axis goes on at θ1 with sin θ = n1 sin θ1 and
# meets the wall at α = 90° − θ1; the light stays in when α > α_r
for th in (10, 14, 15, 30):
    t1 = degrees(asin(sin(radians(th)) / 1.48))
    a[f"sim-alpha-{th}"] = 90 - t1                  # 10°: 83,3°, 14°: 80,59°, 15°: 79,93°, 30°: 70,25°
for n2 in (1.00, 1.20, 1.33, 1.40, 1.46):
    a[f"sim-ar-{n2:.2f}"] = degrees(asin(n2 / 1.48))   # 42,5°, 54,2°, 64,0°, 71,1°, 80,6°
# koe-1 question: largest whole θ for n2 = 1,46; at the limit θ1 = 90° − α_r = 9,43° and
# sin θ = 1,48 sin 9,43° = sqrt(n1² − n2²) = 0,2425, θ = 14,03°
a["koe1-limit"] = degrees(asin(sqrt(1.48 ** 2 - 1.46 ** 2)))   # 14,03° -> 14°
# koe-2: θ = 30°, α = 70,25°; the light leaks when α_r > α, i.e. n2 > n1 sin α
a["koe2-n2"] = 1.48 * sin(radians(90 - degrees(asin(sin(radians(30)) / 1.48))))   # 1,393
# siirto: C-Lion1, 1172 km (Cinia 2016), fibre glass n = 1,47
a["siirto"] = 1.47 * 1172e3 / c * 1e3              # t = n s / c = 5,743 ms -> 5,74 ms
a["siirto-v"] = c / 1.47                            # 2,041 · 10^8 m/s
a["siirto-no-n"] = 1172e3 / c * 1e3                 # mistake: speed c: 3,91 ms
a["siirto-cn"] = 1172e3 / (c * 1.47) * 1e3          # mistake: v = c n: 2,66 ms
a["siirto-km"] = 1.47 * 1172 / c * 1e3              # mistake: km not converted: 5,74 · 10^-3 ms
# virhe: air (1,00) -> water (1,33) at 60°: no total reflection, refraction angle 40,6°
a["virhe-beta"] = degrees(asin(sin(radians(60)) / 1.33))   # 40,6°
# check-2: light guide, core n1 = 1,49, cladding n2 = 1,40
a["check-ar"] = degrees(asin(1.40 / 1.49))          # 69,98° -> 70,0°
a["check-sin"] = 1.40 / 1.49                        # mistake: answered with the sine 0,9396
a["check-comp"] = 90 - a["check-ar"]                # mistake: the complement 20,02°, measured from the surface
# exit ticket: glass n = 1,60 against air
a["exit-ar"] = degrees(asin(1 / 1.60))              # 38,7°
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
