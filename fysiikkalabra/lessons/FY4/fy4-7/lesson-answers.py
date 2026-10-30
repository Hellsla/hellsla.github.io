"""Numbers of the lesson text and inquiry.json for fy4-7, computed from their data (python -I lesson-answers.py); the
exercises' answers are in answers.py. E_k = ½ m v², E_p = m g h, E_mek = E_k + E_p; a body moving straight up (or up a
frictionless ramp) with speed v rises h = v²/(2g) (luku Kiihtyvyys ja tasaisesti kiihtyvä liike). Prints {id: number} as JSON."""
import json, math

g = 9.81
a = {}
# Hook: a skateboarder rolls up a ramp, friction and air resistance small: h = v² / (2g)
a["hook-h3"] = 3.0 ** 2 / (2 * g)                     # 0,459 m
a["hook-h6"] = 6.0 ** 2 / (2 * g)                     # 1,83 m, four times
# Retrieval: ball thrown up at 10 m/s: t = v/g, h = v t − ½ g t² = v²/(2g)
a["pr-h"] = 10 ** 2 / (2 * g)                         # 5,1 m
a["pr-noHalf"] = 10 ** 2 / g                          # mistake 10 m
a["pr-time"] = 10 / g                                 # mistake: the time 1,0 s
a["pr-noSquare"] = 10 / (2 * g)                       # mistake: v instead of v², 0,51 m


# Simulation model: cart up a ramp at angle α, friction coefficient μ (0 or 0,10); up a = g(sin α + μ cos α),
# down a = g(sin α − μ cos α); h_max = s_max sin α, v_back = a_down t_down
def ramp(v0, alpha_deg, mu):
    al = math.radians(alpha_deg)
    au, ad = g * (math.sin(al) + mu * math.cos(al)), g * (math.sin(al) - mu * math.cos(al))
    s = v0 ** 2 / (2 * au)
    return s * math.sin(al), math.sqrt(2 * ad * s)


for v0 in (1.0, 2.0, 3.0):                            # Koe 1: m = 1,0 kg, loiva 25°, no friction
    a[f"exp1-h{v0:g}"], _ = ramp(v0, 25, 0)           # 0,051 m; 0,204 m; 0,459 m
    a[f"exp1-Ek{v0:g}"] = 0.5 * 1.0 * v0 ** 2         # 0,50 J; 2,0 J; 4,5 J
a["exp1-ratio"] = a["exp1-h3"] / a["exp1-h1"]         # 9,0 (pred-1: three times the speed)
a["exp1-ratio-mistake-inv"] = a["exp1-h1"] / a["exp1-h3"]   # 0,11
a["exp1-Ep-top3"] = 1.0 * g * a["exp1-h3"]            # m g h_max = 4,5 J = E_k at the foot
for m in (0.5, 1.0, 2.0):                             # Koe 4 (optional): v0 = 3,0 m/s, loiva, no friction
    a[f"exp4-h-m{m:g}"], _ = ramp(3.0, 25, 0)         # 0,459 m for every mass
    a[f"exp4-Ek-m{m:g}"] = 0.5 * m * 3.0 ** 2         # 2,25 J; 4,5 J; 9,0 J
for name, al in (("loiva", 25), ("jyrkka", 50)):      # Koe 2: v0 = 3,0 m/s, m = 1,0 kg, no friction
    a[f"exp2-h-{name}"], a[f"exp2-vb-{name}"] = ramp(3.0, al, 0)   # 0,459 m and 3,0 m/s on both slopes
a["exp3-h"], a["exp3-vb"] = ramp(3.0, 25, 0.10)      # Koe 3, small friction: 0,378 m and 2,41 m/s
a["exp3-Emek-end"] = 0.5 * 1.0 * a["exp3-vb"] ** 2    # 2,91 J of the 4,5 J left as mechanical energy
# Ydinajatus: 50 km/h -> 70 km/h multiplies E_k by (70/50)²
a["traffic-ratio"] = (70 / 50) ** 2                   # 1,96 ≈ 2,0
# Kaava figure: E_k against v for m = 1,0 kg
a["fig-Ek2"], a["fig-Ek4"] = 0.5 * 1.0 * 2 ** 2, 0.5 * 1.0 * 4 ** 2       # 2,0 J and 8,0 J
# Zero level figure: book 0,50 kg on a shelf 1,80 m above the floor, table top 0,80 m
a["zero-shelf-floor"] = 0.50 * g * 1.80               # 8,83 J
a["zero-table-floor"] = 0.50 * g * 0.80               # 3,92 J
a["zero-shelf-table"] = 0.50 * g * (1.80 - 0.80)      # 4,91 J
a["zero-floor-table"] = 0.50 * g * (0 - 0.80)         # −3,92 J
a["zero-drop"] = a["zero-shelf-floor"] - a["zero-table-floor"]           # 4,91 J from either zero level
# Worked example: snowboarder 68 kg, 12 m/s, 25 m above the foot of the slope
a["ex-Ek"] = 0.5 * 68 * 12 ** 2                       # 4896 J
a["ex-Ep"] = 68 * g * 25                              # 16 677 J
a["ex-Emek"] = a["ex-Ek"] + a["ex-Ep"]                # 21 573 J -> 22 kJ
a["ex-check"] = 0.5 * 70 * 150 + 70 * 10 * 25         # round numbers: 5 250 J + 17 500 J ≈ 23 kJ
# Etsi virhe: car 1000 kg at 36 km/h
a["err-wrong"] = 0.5 * 1000 * 36 ** 2                 # 648 000 J with km/h
a["err-right"] = 0.5 * 1000 * (36 / 3.6) ** 2         # 36 km/h = 10 m/s: 50 000 J
# Transfer: the height whose E_p equals E_k at 50 km/h: m g h = ½ m v² -> h = v² / (2g)
v50 = 50 * 1000 / 3600
a["siirto"] = v50 ** 2 / (2 * g)                      # 9,83 m
a["siirto-kmh"] = 50 ** 2 / (2 * g)                   # mistake: no conversion, 127 m
a["siirto-noHalf"] = v50 ** 2 / g                     # mistake: no ½, 19,7 m
# Check 2: graph E_k(v) of a ball, point (4,0 m/s; 4,0 J): m = 2 E_k / v²
a["check2"] = 2 * 4.0 / 4.0 ** 2                      # 0,50 kg
a["check2-noTwo"] = 4.0 / 4.0 ** 2                    # 0,25 kg
a["check2-noSquare"] = 2 * 4.0 / 4.0                  # 2,0 kg
# Exit ticket: mass doubled, speed halved: ½ (2m)(v/2)² = ½ · ½ m v²
a["exit-ratio"] = 2 * 0.5 ** 2                        # 0,5
print(json.dumps(a))
