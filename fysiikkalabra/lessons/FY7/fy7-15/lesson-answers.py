"""Numbers of the lesson text and inquiry.json for fy7-15, computed from their data (python -I lesson-answers.py); the
exercises' answers are in answers.py. Ideal polariser: unpolarised I0 -> I0 / 2; Malus I = I0 cos² θ; Brewster
tan α_B = n2 / n1 with α_B + α2 = 90°. Prints {id: number} as JSON."""
import json
from math import cos, sin, tan, atan, degrees, radians

a = {}
c2 = lambda d: cos(radians(d)) ** 2
# Kaava graph and text: I / I0 at 30°, 45°, 60°, 90°
for d in (30, 45, 60, 90):
    a[f"malus-{d}"] = c2(d)                         # 0,75; 0,50; 0,25; 0
# Brewster figure and text: air -> water (1,33), air -> glass (1,50)
a["brew-water"] = degrees(atan(1.33))               # 53,06° -> 53,1°
a["brew-water-a2"] = 90 - a["brew-water"]           # refracted 36,94° -> 36,9°
a["brew-water-check"] = degrees(__import__("math").asin(sin(radians(a["brew-water"])) / 1.33))   # Snell gives the same 36,94°
a["brew-glass"] = degrees(atan(1.50))               # 56,31° -> 56,3°
a["sun-height-water"] = 90 - a["brew-water"]        # the sun 36,9° above the horizon gives glare at the Brewster angle
# worked example: unpolarised 840 W/m², two polarisers at 35°
a["ex-I1"] = 840 / 2                                # 420 W/m²
a["ex-cos2"] = c2(35)                               # 0,6710
a["ex-I2"] = 840 / 2 * c2(35)                       # 281,8 W/m² -> 282 W/m²
a["ex-share"] = c2(35) / 2                          # 33,6 % of the lamp's light
# simulation and koe-1 (θ1 = 0, two polarisers): I3 / I0 = 50 % · cos² θ3
for d in (0, 15, 30, 45, 60, 75, 90):
    a[f"sim-two-{d}"] = 50 * c2(d)                  # 50; 46,65; 37,5; 25; 12,5; 3,35; 0 %
a["koe1-q"] = 50 * c2(30)                           # 37,5 %
a["koe1-no-half"] = 100 * c2(30)                    # mistake: no halving, 75 %
a["koe1-cos"] = 50 * cos(radians(30))               # mistake: cos, not cos², 43,3 %
a["koe1-linear"] = 50 * (1 - 30 / 90)               # mistake: linear in the angle, 33,3 %
# koe-2 (optional): crossed P1 = 0°, P3 = 90°, middle at θ2: 50 % · cos² θ2 · cos²(90° − θ2)
for d in (0, 15, 30, 45, 60, 75, 90):
    a[f"sim-three-{d}"] = 50 * c2(d) * c2(90 - d)   # 0; 3,125; 9,375; 12,5; 9,375; 3,125; 0 %
# mittaus (interpret): phone screen through a polariser, light sensor; example data E (lx) against cos² θ
TH = [0, 15, 30, 45, 60, 75, 90]
E = [374, 354, 283, 197, 102, 40, 15]
X = [c2(d) for d in TH]
mx, my = sum(X) / len(X), sum(E) / len(E)
slope = sum((x - mx) * (y - my) for x, y in zip(X, E)) / sum((x - mx) ** 2 for x in X)
a["fit-slope"] = slope                              # ≈ 359 lx
a["fit-intercept"] = my - slope * mx                # ≈ 15 lx (the room's background light)
a["fit-no-bg"] = E[0]                               # mistake: the reading at cos² θ = 1 alone, 374 lx
# virhe: unpolarised 200 W/m², two polarisers at 60°
a["virhe-right"] = 200 / 2 * c2(60)                 # 25 W/m²
a["virhe-student"] = 200 * c2(60)                   # 50 W/m² (the halving forgotten)
a["virhe-cos"] = 200 / 2 * cos(radians(60))         # 50 W/m² with cos instead of cos² and halving
# siirto: camera 1,60 m above calm water (1,33): the reflection point at the Brewster angle, d = h tan α_B
a["siirto"] = 1.60 * 1.33                           # tan α_B = 1,33, d = 2,128 m -> 2,13 m
a["siirto-inv"] = 1.60 / 1.33                       # mistake: tan α_B = 1 / 1,33, 1,203 m
a["siirto-sin"] = 1.60 * sin(radians(degrees(atan(1.33))))   # mistake: sin instead of tan, 1,279 m
# tarkistus-2: polarised laser 5,00 mW through a polariser at 50,0°
a["check-P"] = 5.00 * c2(50.0)                      # 2,066 mW -> 2,07 mW
a["check-cos"] = 5.00 * cos(radians(50.0))          # mistake: cos, 3,214 mW
a["check-half"] = 5.00 / 2 * c2(50.0)               # mistake: halved although the laser is polarised, 1,033 mW
a["check-comp"] = 5.00 * c2(40.0)                   # mistake: the complement 40°, 2,934 mW
# exit ticket: glass n = 1,50 against air
a["exit-brew"] = a["brew-glass"]                    # 56,3°
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
