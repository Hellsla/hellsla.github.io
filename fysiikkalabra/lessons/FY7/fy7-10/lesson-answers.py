"""Numbers of the lesson text and inquiry.json for fy7-10, computed from their data (python -I lesson-answers.py); the
exercises' answers are in answers.py. Law of reflection beta = alpha_1; Snell n1 sin a1 = n2 sin a2; n = c / v.
Refractive indices (589 nm): air 1,00, water 1,33, acrylic 1,49, glass 1,52, diamond 2,42. Prints {id: number} as JSON."""
import json, math

S, D = (lambda d: math.sin(math.radians(d))), (lambda x: math.degrees(math.asin(x)))
c = 3.00e8
a = {}
# Worked example: laser from air (1,00) into water (1,33) at 55,0°; the speed of light in water
a["ex-sin2"] = 1.00 * S(55.0) / 1.33            # sin a2 = n1 sin a1 / n2 = 0,6159
a["ex-a2"] = D(a["ex-sin2"])                    # a2 = 38,02° -> 38,0°
a["ex-v"] = c / 1.33 / 1e8                      # v = c / n = 2,256 · 10^8 m/s -> 2,26 · 10^8 m/s
# Ydinajatus: partial reflection at normal incidence, ((n - 1) / (n + 1))² (the figure only, the formula is not taught)
a["R-glass"] = ((1.52 - 1) / (1.52 + 1)) ** 2 * 100   # 4,3 % per glass surface
a["R-water"] = ((1.33 - 1) / (1.33 + 1)) ** 2 * 100   # 2,0 % at a water surface
# Ydinajatus figures: air -> water at 50°
a["fig-a2"] = D(S(50) / 1.33)                   # 35,2°
# Kaava graph: the largest refraction angle from air (a1 -> 90°)
a["graph-water-90"] = D(1 / 1.33)               # 48,8°
a["graph-diamond-90"] = D(1 / 2.42)             # 24,4°
# Kaava: speeds
a["v-water"] = c / 1.33 / 1e8                   # 2,26 · 10^8 m/s
a["v-diamond"] = c / 2.42 / 1e8                 # 1,24 · 10^8 m/s
# Simulation defaults (air -> water, a1 = 40°) and the experiments
a["sim-a2-40"] = D(S(40) / 1.33)                # 28,9°
for t in (0, 20, 30, 40, 60, 80):
    a[f"koe1-a2-{t}"] = D(S(t) / 1.33)          # 0; 14,9; 22,1; 28,9; 40,6; 47,8°
    if t: a[f"koe1-ratio-{t}"] = S(t) / S(D(S(t) / 1.33))   # sin a1 : sin a2 = 1,33 at every angle
a["koe1-double"] = a["koe1-a2-60"] / a["koe1-a2-30"]        # doubling a1 from 30° to 60°: a2 grows 1,84-fold
for name, n in (("vesi", 1.33), ("akryyli", 1.49), ("lasi", 1.52), ("timantti", 2.42)):
    a[f"koe2-a2-{name}"] = D(S(50) / n)         # a1 = 50°: 35,2; 30,9; 30,3; 18,5°
a["sim-water-air-tir"] = D(1 / 1.33)            # water -> air: no refracted ray above 48,8°
# Fresnel reflectance (unpolarised) in the simulation's readout, air -> water
def R(n1, n2, t):
    i = math.radians(t); s = n1 * math.sin(i) / n2; r = math.asin(s)
    rs = ((n1 * math.cos(i) - n2 * math.cos(r)) / (n1 * math.cos(i) + n2 * math.cos(r))) ** 2
    rp = ((n1 * math.cos(r) - n2 * math.cos(i)) / (n1 * math.cos(r) + n2 * math.cos(i))) ** 2
    return (rs + rp) / 2 * 100
a["sim-R-0"] = R(1.00, 1.33, 0)                 # 2,0 %
a["sim-R-40"] = R(1.00, 1.33, 40)               # 2,4 %
a["sim-R-80"] = R(1.00, 1.33, 80)               # 35 %
# Interpret task (example data): laser from air into an acrylic half-cylinder, protractor readings to 1°
a1 = [10, 20, 30, 40, 50, 60, 70]
a2 = [7, 13, 20, 26, 31, 36, 39]
x = [S(v) for v in a2]; y = [S(v) for v in a1]          # x = sin a2 (acrylic), y = sin a1 (air)
N = len(x); mx, my = sum(x) / N, sum(y) / N
Sxx = sum((xi - mx) ** 2 for xi in x); Sxy = sum((xi - mx) * (yi - my) for xi, yi in zip(x, y))
A = Sxy / Sxx; B = my - A * mx                          # least-squares line y = A x + B (as Graphical Analysis)
s = math.sqrt(sum((yi - A * xi - B) ** 2 for xi, yi in zip(x, y)) / (N - 2)); dA = s / math.sqrt(Sxx)
for k, (p, q) in enumerate(zip(x, y)): a[f"fit-x{k}"], a[f"fit-y{k}"] = p, q
a["fit-A"], a["fit-B"], a["fit-dA"] = A, B, dA          # 1,4895 ; -0,0041 ; 0,0162
a["mittaus"] = A * 1.00                                 # n_akryyli = A n_ilma = 1,49
a["mittaus-rel"] = dA / A * 100                         # 1,1 %
a["mittaus-inv"] = 1 / A                                # mistake: x and y swapped -> 0,674
a["nopeus"] = c / round(A, 2) / 1e8                     # v = c / n = 2,01 · 10^8 m/s
a["nopeus-c-n"] = c * round(A, 2) / 1e8                 # mistake: c · n = 4,47
# virhe: angle 30° between the ray and the water surface: a1 = 60°
a["virhe-wrong"] = D(S(30) / 1.33)              # 22,1° (the student's)
a["virhe-right"] = D(S(60) / 1.33)              # 40,6°
# siirto: aquarium, water (1,33) -> glass (1,52) -> air (1,00), a1 = 30,0° in water
a["siirto-glass"] = D(1.33 * S(30.0) / 1.52)    # 25,9° in the glass
a["siirto"] = D(1.33 * S(30.0) / 1.00)          # 41,7° in the air: the glass drops out
a["siirto-swap"] = D(S(30.0) / 1.33)            # mistake n1, n2 swapped: 22,1°
a["siirto-ratio"] = 30.0 * 1.33                 # mistake angles in proportion: 39,9° (outside 2 %)
# tarkistus-2: air -> oil, a1 = 50,0°, a2 = 31,4°
a["tarkistus-2"] = S(50.0) / S(31.4)            # n = 1,47
a["tarkistus-2-inv"] = S(31.4) / S(50.0)        # mistake inverted: 0,680
a["tarkistus-2-deg"] = 50.0 / 31.4              # mistake ratio of angles: 1,59
# Exit ticket
a["exit-beta"] = 25                             # reflection angle 25°, between the rays 50°
a["exit-n"] = c / 2.25e8                        # 1,33
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
