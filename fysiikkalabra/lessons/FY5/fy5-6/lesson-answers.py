"""Numbers of the lesson text and inquiry.json for fy5-6, computed from their data (python -I lesson-answers.py); the
exercises' answers are in answers.py. Circular orbit: γMm/r² = mv²/r, v = sqrt(γM/r), T = 2πr/v, g_h = γM/r².
The simulation's runs are recomputed with its own velocity Verlet step (sim(): the same sub-step of 1/1500 of the local
circular period and the same frame chunks of T_est/360). Prints {id: number} as JSON."""
import json, math

gam, M, R = 6.674e-11, 5.97e24, 6.371e6          # γ (N·m²/kg²), the Earth's mass (kg) and radius (m)
mu = gam * M                                     # γM = 3,984·10¹⁴ m³/s²
a = {}


def sim(h_km, v_kms):
    """One launch as the simulation computes it: hmin, hmax (km), T (min) or a crash."""
    r0, v0 = R + h_km * 1e3, v_kms * 1e3
    eps = v0 * v0 / 2 - mu / r0; sa = -mu / (2 * eps); Test = 2 * math.pi * math.sqrt(sa ** 3 / mu)
    x, y, vx, vy, t, ang, sw, rmin, rmax = 0.0, r0, v0, 0.0, 0.0, math.pi / 2, 0.0, r0, r0
    def acc(x, y):
        r2 = x * x + y * y; k = -mu / (r2 * math.sqrt(r2)); return k * x, k * y
    ax, ay = acc(x, y)
    while True:
        left = Test / 360
        while left > 0:
            h = min(left, 2 * math.pi * math.sqrt(math.hypot(x, y) ** 3 / mu) / 1500); left -= h
            vx += 0.5 * h * ax; vy += 0.5 * h * ay; x += h * vx; y += h * vy
            ax, ay = acc(x, y); vx += 0.5 * h * ax; vy += 0.5 * h * ay; t += h
            r = math.hypot(x, y)
            if r <= R: return {"hmin": 0.0, "hmax": (rmax - R) / 1e3, "T": None}
            a2 = math.atan2(y, x); d = (a2 - ang + math.pi) % (2 * math.pi) - math.pi; s2 = sw + abs(d); ang = a2
            rmin, rmax = min(rmin, r), max(rmax, r)
            if s2 >= 2 * math.pi:
                f = (2 * math.pi - sw) / (s2 - sw)
                return {"hmin": (rmin - R) / 1e3, "hmax": (rmax - R) / 1e3, "T": (t - h + f * h) / 60, "close": (r - r0) / r0}
            sw = s2


# Hook and Painottomuus: g at the ISS (h = 420 km) and the astronaut's weight (70 kg)
r_iss = R + 420e3
a["g-iss"] = mu / r_iss ** 2                          # 8,64 m/s²
a["g-iss-share"] = mu / r_iss ** 2 / 9.81             # 0,88: 88 % of the surface value
a["G-70-surface"] = 70 * 9.81                         # 687 N
a["G-70-iss"] = 70 * mu / r_iss ** 2                  # 605 N
# Worked example: ISS at h = 420 km
a["ex-r"] = r_iss                                     # 6 791 000 m
a["ex-gm"] = mu                                       # γM = 3,984·10¹⁴ m³/s²
a["ex-v"] = math.sqrt(mu / r_iss)                     # v = sqrt(γM/r) = 7660 m/s
a["ex-T-s"] = 2 * math.pi * r_iss / math.sqrt(mu / r_iss)   # T = 2πr/v = 5571 s
a["ex-T-min"] = a["ex-T-s"] / 60                      # 92,8 min (ISS measured about 92,9 min)
a["ex-check-v"] = math.sqrt(9.81 * R)                 # surface orbit sqrt(gR) = 7,91 km/s: the ISS a little slower
# Kaava: the circular speed at the surface and the graph's real data (T from the sources of the table)
a["v-surface"] = math.sqrt(mu / R)                    # 7,91 km/s
a["v-iss-data"] = 2 * math.pi * 6.79e6 / (92.9 * 60)  # 7,65 km/s
a["v-gps-data"] = 2 * math.pi * 26.56e6 / (11 * 3600 + 58 * 60)   # 3,87 km/s (interpret question)
a["v-geo-data"] = 2 * math.pi * 42.164e6 / 86164      # 3,07 km/s
a["v-moon-data"] = 2 * math.pi * 384.4e6 / (27.32 * 86400)        # 1,023 km/s
a["v-moon-model"] = math.sqrt(mu / 384.4e6)           # 1,018 km/s: 0,5 % less, the Moon and the Earth orbit their common centre of mass
a["v-gps-model"] = math.sqrt(mu / 26.56e6)            # 3,873 km/s
a["v-gps-wrong-h"] = 2 * math.pi * 20.2e6 / (11 * 3600 + 58 * 60)  # mistake: height instead of r, 2,95 km/s
a["v-gps-wrong-min"] = 2 * math.pi * 26.56e6 / (11 * 60 + 58) / 1000   # mistake: T in minutes, 232 km/s
# Experiment 1 (sim, h = 400 km): the circular speed and the runs quoted in the feedback
r400 = R + 400e3
a["sim-vc-400"] = math.sqrt(mu / r400) / 1e3          # 7,671 km/s (model)
a["sim-g-400"] = mu / r400 ** 2                       # 8,69 m/s²
a["sim-T-400"] = 2 * math.pi * r400 / math.sqrt(mu / r400) / 60   # 92,4 min
s700 = sim(400, 7.00); a["sim-700-hmin"] = s700["hmin"]           # 0: crash
s760 = sim(400, 7.60); a["sim-760-hmin"] = s760["hmin"]; a["sim-760-T"] = s760["T"]   # 155 km, back up to 400 km; 89,9 min
s767 = sim(400, 7.67); a["sim-767-hmin"] = s767["hmin"]; a["sim-767-T"] = s767["T"]; a["sim-767-close"] = s767["close"]   # 396 km; 92,4 min; closes to 1e-8
s768 = sim(400, 7.68); a["sim-768-hmax"] = s768["hmax"]           # 432 km
s800 = sim(400, 8.00); a["sim-800-hmax"] = s800["hmax"]           # 1700 km
s10 = sim(400, 10.0); a["sim-10-hmax"] = s10["hmax"]; a["sim-10-close"] = s10["close"]   # 31 900 km
# Experiment 2 (sim, h = 400 km, v = 7,67 km/s): the force for each mass, the same path
for m in (1, 1000, 420000):
    a[f"sim-F-{m}"] = mu * m / r400 ** 2              # 8,69 N · 8,69 kN · 3,65 MN
# Geostationary height (text "Geostationaarinen rata"): from T = 23 h 56 min
T_geo = 23 * 3600 + 56 * 60                           # 86 160 s
a["geo-r"] = (mu * T_geo ** 2 / (4 * math.pi ** 2)) ** (1 / 3)   # 4,216·10⁷ m
a["geo-h"] = (a["geo-r"] - R) / 1e3                   # 35 790 km
a["geo-wrong-24h"] = ((mu * 86400 ** 2 / (4 * math.pi ** 2)) ** (1 / 3) - R) / 1e3   # with 24 h: 35 860 km (inside tolerance)
a["geo-wrong-r"] = a["geo-r"] / 1e3                   # forgot to subtract R: 42 160 km
a["geo-v"] = 2 * math.pi * a["geo-r"] / T_geo         # 3,07 km/s
# Transfer task: Hubble's height from T = 95,4 min
T_hst = 95.4 * 60                                     # 5724 s
a["hst-r"] = (mu * T_hst ** 2 / (4 * math.pi ** 2)) ** (1 / 3)   # 6,915·10⁶ m
a["hst-h"] = (a["hst-r"] - R) / 1e3                   # 544 km
a["hst-wrong-r"] = a["hst-r"] / 1e3                   # mistake: r given as the height, 6915 km
a["hst-v"] = 2 * math.pi * a["hst-r"] / T_hst         # 7,59 km/s: a little slower than the ISS, as it is higher
# Error to find: the ISS speed with h instead of r
a["err-v"] = math.sqrt(mu / 420e3)                    # 30,8 km/s: far too fast
# Check 2: the mass of Mars from Phobos (r = 9376 km, T = 7 h 39 min)
T_ph = 7 * 3600 + 39 * 60                             # 27 540 s
a["check-Mmars"] = 4 * math.pi ** 2 * 9.376e6 ** 3 / (gam * T_ph ** 2)   # 6,43·10²³ kg (published 6,42·10²³)
a["check-Mmars-wrong-h"] = 4 * math.pi ** 2 * 9.376e6 ** 3 / (gam * (7.39 * 3600) ** 2)   # mistake: 7 h 39 min as 7,39 h: 6,90·10²³
a["check-v-phobos"] = 2 * math.pi * 9.376e6 / T_ph    # 2,14 km/s
# Exit ticket: speed at r = 7000 km
a["exit-v"] = math.sqrt(mu / 7.0e6)                   # 7,54 km/s
# Milloin malli pätee: the Earth's orbit, nearest and farthest 147,1 and 152,1 million km
a["earth-spread"] = (152.1 - 147.1) / ((152.1 + 147.1) / 2)        # 3,3 % of the mean distance
a["moon-spread"] = (405.5 - 363.3) / ((405.5 + 363.3) / 2)         # 11 %
print(json.dumps({k: (round(v, 6) if isinstance(v, float) else v) for k, v in a.items()}))
