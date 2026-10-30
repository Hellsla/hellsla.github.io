"""Numbers of the lesson text and inquiry.json for fy4-8, computed from their data (python -I lesson-answers.py); the
exercises' answers are in answers.py. g = 9,81 m/s²; the zero level of potential energy is the lowest point of each
situation. Prints {id: number} as JSON."""
import json, math

g = 9.81
a = {}
# The simulation's model (assets/sims/fy4/fy4-8/sim.js): a roller-coaster car released from rest at height h1 on the
# left side of a valley: a level floor of 6 m (|u| <= B = 3 m) between two ramps, either circular arcs of radius 21 m
# ("kaari") or straight 45° slopes ("suora"). u is the distance along the track from the middle of the floor. A constant
# resistive force F (rolling and air resistance together) points against the motion: a = -g dy/du - F/m.
# RK4 steps of 2 ms of simulated time; the run ends at the first stop (h2 = the height there).
B, R, ANG = 3.0, 21.0, math.radians(45)
def ramp_len(h, rata): return R * math.acos(1 - h / R) if rata == "kaari" else h / math.sin(ANG)
def geo(u, rata):
    q = abs(u) - B; sg = 1 if u >= 0 else -1
    if q <= 0: return 0.0, 0.0
    if rata == "kaari": return R * (1 - math.cos(q / R)), sg * math.sin(q / R)
    return q * math.sin(ANG), sg * math.sin(ANG)
def run(h1, m, F, rata, dt=0.002):
    u0 = -(B + ramp_len(h1, rata)); u, w = u0, 0.0; vpohja = None
    acc = lambda uu: -g * geo(uu, rata)[1] - F / m
    while True:
        k1u, k1w = w, acc(u); k2u, k2w = w + dt / 2 * k1w, acc(u + dt / 2 * k1u)
        k3u, k3w = w + dt / 2 * k2w, acc(u + dt / 2 * k2u); k4u, k4w = w + dt * k3w, acc(u + dt * k3u)
        un, wn = u + dt / 6 * (k1u + 2 * k2u + 2 * k3u + k4u), w + dt / 6 * (k1w + 2 * k2w + 2 * k3w + k4w)
        if vpohja is None and u < 0 <= un: vpohja = w + (wn - w) * (-u) / (un - u)
        if wn <= 0 and u > u0 + 0.01:
            f = w / (w - wn); u = u + f * (un - u); break
        u, w = un, wn
    s = u - u0; h2 = geo(u, rata)[0]
    return {"vpohja": vpohja, "h2": h2, "s": s, "W": -F * s, "dEm": m * g * h2 - m * g * h1, "Em0": m * g * h1}
# prediction 1 / experiment 1: no resistance, h1 = 10 m, the empty and the full car: the same speed at the bottom
for m in (400, 600, 800):
    a[f"sim-vpohja-{m}"] = run(10, m, 0, "kaari")["vpohja"]          # 14,0 m/s for every mass
a["sim-vpohja-theory"] = math.sqrt(2 * g * 10)                         # √(2gh) = 14,007 m/s
a["sim-vpohja-suora"] = run(10, 400, 0, "suora")["vpohja"]            # the straight 45° track: also 14,0 m/s
a["sim-h2-F0"] = run(10, 400, 0, "kaari")["h2"]                         # without resistance back to 10,0 m
a["sim-Em0-400"] = 400 * g * 10                                         # E_mek,1 = mgh1 = 39 240 J
# prediction 2 / experiment 2: h1 = 10 m, m = 400 kg, curved track, resistance 100 N and 200 N
for F in (100, 200, 300):
    r = run(10, 400, F, "kaari")
    a[f"sim-h2-{F}"] = r["h2"]; a[f"sim-s-{F}"] = r["s"]; a[f"sim-W-{F}"] = r["W"]; a[f"sim-dEm-{F}"] = r["dEm"]
    a[f"sim-Fh-{F}"] = -F * 10                                          # the wrong idea F·h1 for comparison
# straight track, the same 200 N: a check of h2 = (m g h1 - F(h1/sin45 + 2B)) / (m g + F/sin45)
r = run(10, 400, 200, "suora")
a["sim-suora-h2-200"] = r["h2"]
a["sim-suora-h2-200-theory"] = (400 * g * 10 - 200 * (10 / math.sin(ANG) + 2 * B)) / (400 * g + 200 / math.sin(ANG))
a["sim-suora-s-200"] = r["s"]
# Figure "laakso": no resistance, a 400 kg car from 10 m: E_p at the top 39,2 kJ, at half height half of it
a["fig-laakso-Ep-top"] = 400 * g * 10
# Worked example (sled): m = 32 kg, h = 5,0 m, from rest, v = 7,6 m/s at the foot of the hill, path 24 m
m, h, v, s = 32.0, 5.0, 7.6, 24.0
a["ex-Ep1"] = m * g * h                                  # 1569,6 J
a["ex-Ek2"] = 0.5 * m * v ** 2                           # 924,16 J
a["ex-W"] = a["ex-Ek2"] - a["ex-Ep1"]                    # W_muut = −645,44 J ≈ −6,5·10² J
a["ex-v-nofriction"] = math.sqrt(2 * g * h)              # 9,90 m/s without friction
a["ex-Favg"] = -a["ex-W"] / s                            # mean resistive force 26,9 N
a["ex-ratio"] = -a["ex-W"] / a["ex-Ep1"]                 # 41 % of the potential energy to internal energy
# Kaava: the work–kinetic energy relation for a constant net force (cart): ΣF = 12 N over 3,0 m, m = 2,0 kg from rest
a["kaava-Wkok"] = 12 * 3.0                               # 36 J
a["kaava-v"] = math.sqrt(2 * 36 / 2.0)                   # 6,0 m/s
# Misconception: G does no work on a level road; a 1500 kg car's E_p on a 10 m hill etc. (none)
# Transfer task (swing): h = 1,20 m, from rest, rope perpendicular to the motion
a["siirto"] = math.sqrt(2 * g * 1.20)                    # 4,852 m/s
a["siirto-mist-2gh"] = 2 * g * 1.20                      # 23,544 (forgot the square root)
a["siirto-mist-gh"] = math.sqrt(g * 1.20)                # 3,431 (½ in the wrong place)
a["siirto-mist-gh2"] = g * 1.20                          # 11,772
# Error-spotting task: a box sliding down a ramp, m = 5,0 kg, h = 1,5 m, friction work −30 J
a["virhe-Ep"] = 5.0 * g * 1.5                            # 73,575 J
a["virhe-Ek-right"] = a["virhe-Ep"] - 30                 # 43,575 J
a["virhe-v-right"] = math.sqrt(2 * a["virhe-Ek-right"] / 5.0)   # 4,175 m/s
a["virhe-Ek-wrong"] = a["virhe-Ep"] + 30                 # 103,575 J: the sign error
a["virhe-v-wrong"] = math.sqrt(2 * a["virhe-Ek-wrong"] / 5.0)   # 6,437 m/s
a["virhe-v-nofriction"] = math.sqrt(2 * g * 1.5)         # 5,425 m/s
# Check 2: coaster from rest at 18,0 m to a hilltop at 7,0 m, no resistance
a["check-2"] = math.sqrt(2 * g * (18.0 - 7.0))           # 14,69 m/s
a["check-2-mist-h1"] = math.sqrt(2 * g * 18.0)           # 18,79 (the whole height)
a["check-2-mist-h2"] = math.sqrt(2 * g * 7.0)            # 11,72 (the hilltop height)
a["check-2-mist-nosqrt"] = 2 * g * 11.0                  # 215,82
# Hook: coaster first hill 40 m: speed at the bottom without losses √(2gh)
a["hook-v40"] = math.sqrt(2 * g * 40)                    # 28,0 m/s ≈ 101 km/h
a["hook-v40-kmh"] = a["hook-v40"] * 3.6
print(json.dumps(a))
