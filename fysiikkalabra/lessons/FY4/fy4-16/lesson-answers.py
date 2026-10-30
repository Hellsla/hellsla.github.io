"""Numbers of the lesson text and inquiry.json for fy4-16, computed from their data (python -I lesson-answers.py); the
exercises' answers are in answers.py. Positive direction: up in a lift, down for a falling jumper, down the slope on a
hill; g = 9,81 m/s². The sled model: straight slopes, the same friction coefficient on the slope and on the flat, air
resistance neglected, no extra loss in the short bend at the foot of the hill. Prints {id: number} as JSON."""
import json, math

g = 9.81
a = {}
# Ydinajatus, lift: a 60,0 kg person, the lift speeds up upward at 1,0 m/s²: N − mg = ma → N = m(g + a)
a["yd-hissi-N"] = 60.0 * (g + 1.0)                    # 648,6 N, about 650 N
a["yd-hissi-kg"] = a["yd-hissi-N"] / g                # the scale shows N/g = 66,1 kg
# Ydinajatus, canopy: an 80 kg jumper at the terminal speed over 100 m: F_v = mg, W_v = −F_v h = −mgh
a["yd-varjo-Fv"] = 80 * g                             # 784,8 N
a["yd-varjo-W"] = -80 * g * 100                       # −78 480 J, about −78 kJ
# Tutki 1, the lift's force plate (example data): m = 60,0 kg, 650 N while speeding up (1,0 → 3,0 s), 550 N while slowing
G60 = 60.0 * g                                        # 588,6 N at rest and at constant velocity
a["tutki-hissi-a1"] = (650 - G60) / 60.0              # 1,023 m/s² up (the numeric question's answer)
a["tutki-hissi-a2"] = (550 - G60) / 60.0              # −0,643 m/s²: down, the lift slows down
a["tutki-hissi-vmax"] = a["tutki-hissi-a1"] * 2.0     # 2,05 m/s after 2,0 s of speeding up
a["tutki-hissi-t2"] = a["tutki-hissi-vmax"] / -a["tutki-hissi-a2"]   # 3,18 s of slowing down (9,0 → 12,2 s) brings the lift to rest
a["tutki-hissi-mistake-N/m"] = 650 / 60.0             # 10,8: forgot to subtract g
# Tutki 2, three slopes of height 6,0 m, μ = 0,10: x1 = h/tan α, v² = 2g(h − μ x1), x2 = v²/(2μg), x1 + x2 = h/μ
h, mu = 6.0, 0.10
for al in (30, 20, 10):
    x1 = h / math.tan(math.radians(al))
    v = math.sqrt(2 * g * (h - mu * x1))
    x2 = v ** 2 / (2 * mu * g)
    a[f"taulu-{al}-x1"], a[f"taulu-{al}-v"], a[f"taulu-{al}-x2"], a[f"taulu-{al}-sum"] = x1, v, x2, x1 + x2
a["taulu-v-kitkaton"] = math.sqrt(2 * g * h)          # 10,85 m/s on every slope without friction
a["taulu-h/mu"] = h / mu                              # 60 m
# Kaava: friction work on a slope W = −μ mg cos α · L = −μ mg x, with x = L cos α (no number)
# Esimerkki: sled 32,0 kg, slope L = 25,0 m at 20,0°, μ = 0,200, from rest: v = √(2gL(sin α − μ cos α))
m, L, al, mu = 32.0, 25.0, math.radians(20.0), 0.200
a["esim-h"] = L * math.sin(al)                        # h = L sin α = 8,551 m
a["esim-N"] = m * g * math.cos(al)                    # N = mg cos α = 295,0 N
a["esim-Fmu"] = mu * a["esim-N"]                      # F_μ = μN = 59,00 N
a["esim-Wmu"] = -a["esim-Fmu"] * L                    # W_μ = −F_μ L = −1475 J
a["esim-mgh"] = m * g * a["esim-h"]                   # mgh = 2684 J
a["esim-v2"] = 2 * g * L * (math.sin(al) - mu * math.cos(al))   # v² = 75,58 m²/s²
a["esim-v"] = math.sqrt(a["esim-v2"])                 # 8,694 m/s → 8,69 m/s
a["esim-v-kitkaton"] = math.sqrt(2 * g * a["esim-h"]) # √(2gh) = 12,95 m/s without friction
a["esim-a"] = g * (math.sin(al) - mu * math.cos(al))  # a = g(sin α − μ cos α) = 1,512 m/s² down the slope; v² = 2aL gives the same v
a["esim-Ek"] = 0.5 * m * a["esim-v2"]                 # ½mv² = mgh + W_μ = 1209 J
# Siirto: a 78,0 kg jumper under the canopy at constant speed over 125 m: |W_v| = F_v h = mgh
a["siirto"] = 78.0 * g * 125 / 1000                   # 95,65 kJ
a["siirto-mistake-Ek"] = 0.5 * 78.0 * 5.0 ** 2 / 1000 # 0,975 kJ: the kinetic energy, which does not change
a["siirto-mistake-sum"] = a["siirto"] + a["siirto-mistake-Ek"]   # 96,6 kJ: E_k added although it does not change
# check-2: 55,0 kg on a scale in a lift that starts downward at 1,20 m/s² (positive up, a = −1,20): reading N/g
a["check-2"] = 55.0 * (g - 1.20) / g                  # 48,27 kg
a["check-2-mistake-plus"] = 55.0 * (g + 1.20) / g     # 61,7 kg: the acceleration's direction wrong
a["check-2-mistake-N"] = 55.0 * (g - 1.20)            # 473,6: the normal force in newtons, not the reading in kg
# Draw task's model figure: an 18,0 kg suitcase on a luggage scale, the lift speeds up downward at 1,5 m/s²: T = m(g − a)
a["malli-T"] = 18.0 * (g - 1.5)                       # 149,6 N < G = 176,6 N
print(json.dumps(a))
