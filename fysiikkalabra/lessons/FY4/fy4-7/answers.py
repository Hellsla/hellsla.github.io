"""Every answer in exercises.json for fy4-7, computed from the task data (python -I answers.py).
Kinetic energy E_k = ½ m v², gravitational potential energy E_p = m g h (h from the chosen zero level), mechanical
energy E_mek = E_k + E_p. Prints {id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json, math

g = 9.81
a = {}


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
print(json.dumps(a))
