"""Numbers of the lesson text and inquiry.json for fy7-11, computed from their data (python -I lesson-answers.py); the
exercises' answers are in answers.py. Snell's law from air: sin α1 = n sin α2; n = c : v; prism α2 + α3 = A,
δ = α1 + α4 − A; rainbow θ = 4β − 2α (one internal reflection), secondary θ2 = 180° + 2α − 6β (two reflections).
Data: water 20 °C (Daimon & Masumura 2007) n = 1,3315 / 1,3334 / 1,3375 / 1,3431 at 656 / 589 / 486 / 405 nm;
crown glass N-BK7 (SCHOTT 2017) n = 1,5143 / 1,5167 / 1,5224 / 1,5302. Prints {id: number} as JSON."""
import json, math

c = 3.00e8
sin = lambda deg: math.sin(math.radians(deg))
asin = lambda x: math.degrees(math.asin(x))
WATER = {"p": 1.3315, "v": 1.3431}
CROWN = {"p": 1.5143, "v": 1.5302}
FLINT = (1.59582, 0.00791448, 0.000154174)          # sim: Cauchy fit through SCHOTT F2 at 656, 588, 486 nm
a = {}
# Ydinajatus: speeds of red and violet light in crown glass, v = c / n
a["v-p"] = c / CROWN["p"] / 1e3                     # 198 111 km/s
a["v-v"] = c / CROWN["v"] / 1e3                     # 196 053 km/s
# Worked example: white light from air into crown glass at α1 = 60,0°
a["ex-p"] = asin(sin(60.0) / CROWN["p"])            # 34,88°
a["ex-v"] = asin(sin(60.0) / CROWN["v"])            # 34,47°
a["ex-ero"] = a["ex-p"] - a["ex-v"]                 # 0,414° -> 0,41°
# Rainbow: the extreme ray, cos² α = (n² − 1) / 3 (primary) and (n² − 1) / 8 (secondary)
def bow(n, k):
    al = math.degrees(math.acos(math.sqrt((n * n - 1) / k))); be = asin(sin(al) / n)
    return al, (4 * be - 2 * al) if k == 3 else (180 + 2 * al - 6 * be)
for col, n in WATER.items():
    al, th = bow(n, 3)
    a[f"bow-alpha-{col}"] = al                       # 59,50° (p), 58,82° (v)
    a[f"bow-{col}"] = th                             # 42,30° (p), 40,63° (v)
    a[f"bow2-{col}"] = bow(n, 8)[1]                  # 50,50° (p), 53,50° (v)
a["bow-width"] = a["bow-p"] - a["bow-v"]            # 1,66°
a["sun-max"] = a["bow-p"]                           # no bow on level ground when the Sun is higher than 42°
a["sun-30-top"] = a["bow-p"] - 30.0                 # Sun 30° high: the red top 12,3° above the horizon
# Kaava graph θ(α) for red: θ at α = 30°, 80°
for al in (30.0, 80.0):
    a[f"theta-p-{int(al)}"] = 4 * asin(sin(al) / WATER["p"]) - 2 * al   # 28,2°, 30,8°
# Simulation: prism deviation δ = α1 + α4 − A
def delta(n, A, a1):
    a2 = asin(sin(a1) / n); a3 = A - a2; x = n * sin(a3)
    return None if abs(x) > 1 else a1 + asin(x) - A
nf = lambda lam: FLINT[0] + FLINT[1] / lam ** 2 + FLINT[2] / lam ** 4
FL = {"p": nf(0.6563), "v": nf(0.4047)}             # 1,6150 and 1,6499
for A in (30, 40, 50, 60, 70):                     # koe-1: crown glass, α1 = 50°
    for col in "pv":
        a[f"k1-{A}-{col}"] = delta(CROWN[col], A, 50.0)
    a[f"k1-{A}-ero"] = a[f"k1-{A}-v"] - a[f"k1-{A}-p"]          # 0,53°, ..., 1,40° (A = 60°), 4,45° (A = 70°)
for a1 in (40, 45, 49, 50, 55, 60, 70, 80):        # koe-2: crown glass, A = 60°
    a[f"k2-{a1}-p"] = delta(CROWN["p"], 60, a1)    # smallest near α1 = 49° (38,43°)
a["k2-30-v-ulos"] = 0 if delta(CROWN["v"], 60, 30.0) is None else 1   # 0: violet does not leave at α1 = 30°
for col in "pv":                                    # flint glass and water at A = 60°, α1 = 50°
    a[f"flint-{col}"] = delta(FL[col], 60, 50.0)
    a[f"vesi-{col}"] = delta(WATER[col], 60, 50.0)
a["flint-ero"] = a["flint-v"] - a["flint-p"]        # 3,92°
a["vesi-ero"] = a["vesi-v"] - a["vesi-p"]           # 0,85°
# virhe: the student's α2 = α1 / n for violet light at 60,0°
a["virhe-wrong"] = 60.0 / CROWN["v"]                # 39,2°
# siirto: pool 2,00 m deep, white light at 60,0° into water: distance of the red and violet spots on the bottom
bp, bv = asin(sin(60.0) / WATER["p"]), asin(sin(60.0) / WATER["v"])
a["siirto-bp"], a["siirto-bv"] = bp, bv             # 40,57°, 40,15°
a["siirto"] = 2.00 * (math.tan(math.radians(bp)) - math.tan(math.radians(bv))) * 1e3   # 25,4 mm
a["siirto-sin"] = 2.00 * (sin(bp) - sin(bv)) * 1e3  # mistake sin instead of tan: 11,2 mm
a["siirto-m"] = a["siirto"] / 1e3                   # answered in metres: 0,0254
a["siirto-a1"] = 2.00 * math.tan(math.radians(60.0)) * 1e3   # mistake tan α1: 3464 mm (no refraction)
# tarkistus-2: speed difference of red and violet light in water
a["check-dv"] = (c / WATER["p"] - c / WATER["v"]) / 1e3      # 1946 km/s
a["check-vp"] = c / WATER["p"] / 1e3                # 225 310 km/s
a["check-vv"] = c / WATER["v"] / 1e3                # 223 364 km/s
# Exit ticket: Sun 50° high -> the top of the red bow would be 42,3° − 50° < 0, below the horizon
a["exit-sun50"] = a["bow-p"] - 50.0                 # −7,7°
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
