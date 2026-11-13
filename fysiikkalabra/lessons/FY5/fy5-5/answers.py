"""Every answer in exercises.json for fy5-5, computed from the task data (python -I answers.py).
Newton's law of gravitation F = γ m1 m2 / r² and the field strength g = γ M / r², γ = 6,674 · 10⁻¹¹ N·m²/kg².
Prints {exercise id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json, math

gamma = 6.674e-11
a = {}
# Level 1: one formula, values given
a["fy5-5-L1-01"] = gamma * 70 * 55 / 0.80 ** 2 * 1e6        # two pupils on a bench: 4,01e-7 N = 0,401 µN -> 0,40 µN
a["fy5-5-L1-02"] = gamma * 5.0e7 * 3.0e7 / 200 ** 2          # two cruise ships 200 m apart: 2,50 N -> 2,5 N
a["fy5-5-L1-03"] = gamma * 3.30e23 / 2.44e6 ** 2             # Mercury's surface: g = γM/R² = 3,70 m/s²
a["fy5-5-L1-04"] = gamma * 6.42e23 * 1025 / 3.40e6 ** 2 / 1e3   # Mars rover 1025 kg on Mars: F = γMm/R² = 3799 N -> 3,80 kN
a["fy5-5-L1-05"] = 36 / 3 ** 2                               # distance tripled: F/9 = 4,0 µN
# Level 2: two steps, one conversion or one rearrangement
a["fy5-5-L2-01"] = 0.40 * math.sqrt(0.60e-6 / gamma)         # equal lead balls: m = r·sqrt(F/γ) = 37,9 kg -> 38 kg
M_venus = 8.87 * 6.052e6 ** 2 / gamma                        # Venus: M = g R²/γ = 4,868e24 kg
a["fy5-5-L2-02"] = M_venus / 5.97e24                         # compared with Earth's 5,97e24 kg: 0,815
r_probe = math.sqrt(gamma * 5.97e24 * 1200 / 1.00e3)         # probe 1200 kg, force 1,00 kN: r = sqrt(γMm/F) = 2,187e7 m
a["fy5-5-L2-03"] = (r_probe - 6.378e6) / 1e3                 # height above the surface (R = 6378 km): 15 500 km
a["fy5-5-L2-04"] = (1 - (6378 / (6378 + 11.0)) ** 2) * 100   # airliner at 11,0 km (R = 6378 km): g smaller by 0,344 %
# Level 3: reasoning or an unfamiliar context
q = math.sqrt(7.35e22 / 5.97e24)                             # neutral point: γM/x² = γm/(d − x)², x = d/(1 + sqrt(m/M))
a["fy5-5-L3-01"] = 3.84e5 / (1 + q)                          # 3,46e5 km from Earth's centre
a["fy5-5-L3-02"] = 9.81 * 2                                  # same density, double radius: M ∝ R³ so g ∝ R: 19,6 m/s²
F_sun = gamma * 1.99e30 / 1.50e11 ** 2                       # per kg of Earth: Sun 5,90e-3 m/s²
F_moon = gamma * 7.35e22 / 3.84e8 ** 2                       # Moon 3,33e-5 m/s²
a["fy5-5-L3-03"] = F_sun / F_moon                            # the Sun pulls 177 times harder
# Exercise-bank additions: L1-06, L1-07 and L1-08 are multiple choice (no number)
gs = lambda M, R: gamma * M / R ** 2                         # surface field strength
a["fy5-5-L2-05"] = gs(1.02e26, 24622e3) / gs(8.68e25, 25362e3)   # Neptune/Uranus surface field: 11,23/9,006 = 1,25
rm = [(4.0, 1.29), (5.0, 0.80), (6.0, 0.56), (8.0, 0.31)]    # (r in cm, F in nN), M = 1,50 kg, m = 20,0 g
gam = [F * 1e-9 * (r / 100) ** 2 / (1.50 * 0.0200) for r, F in rm]
a["fy5-5-L2-06"] = sum(gam) / len(gam) * 1e11                # mean gamma = 6,72e-11 (answer in 1e-11)
gh = [(0, 9.81), (400, 8.69), (1000, 7.33), (2000, 5.68), (3000, 4.53)]   # (h in km, g)
a["fy5-5-L2-07"] = sum(g * (6.378e6 + h * 1e3) ** 2 for h, g in gh) / len(gh) / 1e14   # mean of g(R+h)^2 = 3,99e14
M_earth = 9.81 * 6.371e6 ** 2 / gamma                        # Earth's mass from g and R: 5,966e24 kg
a["fy5-5-L3-04"] = M_earth / (4 / 3 * math.pi * 6.371e6 ** 3)   # mean density 5508 -> 5510 kg/m3
a["fy5-5-L3-05"] = 62.0 * (9.81 - 4 * math.pi ** 2 * 6.378e6 / (6.0 * 3600) ** 2)  # scale reading at the equator, T = 6,0 h: N = m(g - a_n) = 574,8 N
# Added batch (teacher 2026-11-12): figure tasks (fy5-5/planeetat)
a["fy5-5-L1-09"] = round(85 * 3.71, -1)                                # F = m g = 315,35 N -> 3,2e2 N (m = 85 kg, two sig. figs)
a["fy5-5-L2-09"] = 24.8 * (7.15e7) ** 2 / gamma / 1e27          # figure: g_Jupiter = 24,8 m/s²: equatorial R = 7,15e7 m: M = g R²/γ = 1,900e27 kg -> 1,90 (answer in 1e27 kg)
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
