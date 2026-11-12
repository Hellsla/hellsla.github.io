"""Every answer in exercises.json for fy4-7, computed from the task data (python -I answers.py).
Kinetic energy E_k = ½ m v², gravitational potential energy E_p = m g h (h from the chosen zero level), mechanical
energy E_mek = E_k + E_p. Prints {id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json, math

g = 9.81
a = {}


def sf(x, n):
    """x rounded to n significant figures (the answer a student gets by rounding to the data's precision)."""
    return float(f"{x:.{n - 1}e}")


def rounded_ok(x, shown, tol=0.02):
    """A student who rounds the answer to the data's figures (shown) stays inside the task's tolerance."""
    assert abs(shown - x) <= tol * abs(x), (x, shown)


# Level 1: one formula, values given
a["fy4-7-L1-01"] = 0.5 * 1200 * 20.0 ** 2 / 1000        # car: E_k = ½ m v² = 240 000 J = 240 kJ
a["fy4-7-L1-02"] = 2.50 * g * 8.00                      # flower pot on a balcony: E_p = m g h = 196 J
a["fy4-7-L1-03"] = 0.5 * 1.20 * 10.0 ** 2 + 1.20 * g * 20.0   # gull: 60,0 J + 235,4 J = 295 J
a["fy4-7-L1-04"] = 72 * g * 12 / 1000                   # climber rises 12 m: ΔE_p = m g Δh = 8,48 kJ -> 8,5 kJ
a["fy4-7-L1-05"] = 4.0 * g * (-6.5)                     # bucket 6,5 m below the ground (zero level): E_p = −255 J
rounded_ok(a["fy4-7-L1-04"], 8.5); rounded_ok(a["fy4-7-L1-05"], -260)
# Level 2: a conversion, a rearrangement or two steps
v = 90 * 1000 / 3600                                    # 90 km/h = 90 · 1000 m : 3600 s = 25 m/s
a["fy4-7-L2-01"] = 0.5 * 1350 * v ** 2 / 1000           # 421,875 kJ -> 4,2 · 10² kJ
rounded_ok(a["fy4-7-L2-01"], 420)
a["fy4-7-L2-02"] = math.sqrt(2 * 82 / 0.057)            # tennis ball 57 g with 82 J: v = √(2E_k/m) = 53,6 m/s -> 54 m/s
rounded_ok(a["fy4-7-L2-02"], 54)
a["fy4-7-L2-03"] = 1.20 * g * (1.90 - 0.75)             # book on a shelf, zero level at the table top: h = 1,15 m, 13,5 J
a["fy4-7-L2-04"] = math.sqrt(2 * (905 - 1.80 * g * 40.0) / 1.80)   # model plane: E_k = 905 J − 706,3 J = 198,7 J, v = 14,9 m/s
# Level 3: reasoning and combining ideas
a["fy4-7-L3-01"] = 40.0 * math.sqrt(12.0 / 1.20)        # same E_k: ½ m₁ v₁² = ½ m₂ v₂² -> v₁ = v₂ √(m₂/m₁) = 126 km/h
a["fy4-7-L3-02"] = 0.500 * g * 1.20 * (1 - math.cos(math.radians(40)))   # pendulum: h = L(1 − cos 40°) = 0,281 m, E_p = 1,38 J
a["fy4-7-L3-03"] = 0.5 * 55.0 * 7.00 ** 2 - 55.0 * g * 2.10   # skater: E_mek falls from 1347,5 J to 1133,1 J: 214 J to internal energy
# Added exercises (concept multiple-choice tasks L1-06 and L1-08 have no numeric answer)
a["fy4-7-L1-07"] = sf(9400 / (80 * g), 2)               # lift: ΔE_p = m g Δh -> Δh = 9400 J / (80 kg · 9,81 m/s²) = 11,98 m -> 12 m
rows = [(1.80, 0.00), (1.75, 0.98), (1.60, 1.99), (1.36, 2.91), (1.02, 3.95), (0.58, 4.88), (0.04, 5.92)]   # (h, v) of the dropped ball
emek = [0.5 * 0.057 * v ** 2 + 0.057 * g * h for h, v in rows]   # E_mek = E_k + E_p at each moment, about 1,0 J
a["fy4-7-L2-05"] = sf(sum(emek) / len(emek), 2)         # mean E_mek = 1,009 J -> 1,0 J
a["fy4-7-L2-06"] = sf(0.5 * 70 * 4.0 ** 2 + 70 * g * (-1.5), 2)   # diver: E_k = 560 J, E_p = m g h with h = −1,5 m = −1030 J, E_mek = −470 J
xs = [v ** 2 for v in (0.40, 0.80, 1.20, 1.60, 2.00)]   # v² of the cart data
ek = [0.043, 0.17, 0.37, 0.66, 1.04]
a["fy4-7-L2-07"] = sf(2 * sum(x * e for x, e in zip(xs, ek)) / sum(x * x for x in xs), 2)   # E_k = ½ m v²: slope of the line through the origin = m/2 = 0,26 -> m = 0,52 kg
rounded_ok(a["fy4-7-L2-05"], 1.0); rounded_ok(a["fy4-7-L2-06"], -470)
a["fy4-7-L3-04"] = sf(0.058 * g * (1.50 - 0.42), 2)     # bouncing ball: E_mek = m g h at the tops, ΔE = m g (h_0 − h_4) = 0,614 J -> 0,61 J
em = [0.5 * 48 * v ** 2 + 48 * g * h for h, v in [(18.0, 1.5), (14.0, 8.3), (10.0, 11.5), (6.0, 14.0), (2.0, 15.8)]]   # sledge run, E_mek at the 5 points
a["fy4-7-L3-05"] = sf((em[0] - em[4]) / 1000, 2)        # ΔE = 8530 J − 6933 J = 1597 J -> 1,6 kJ
# Added exercises (figure tasks)
a["fy4-7-L2-08"] = 9.0 - 1.0                                       # pallo-ek: E_k(6,0 m/s) = 9,0 J, E_k(2,0 m/s) = 1,0 J → ΔE_k = 8,0 J
a["fy4-7-L2-09"] = sf(39 / (g * 2.0), 2)                           # ep-kuvaaja: E_p = 39 J at h = 2,0 m → m = E_p/(g h) = 1,99 kg
print(json.dumps(a))
