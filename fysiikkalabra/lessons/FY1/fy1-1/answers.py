"""Every answer in exercises.json for fy1-1, computed from the task data (python -I answers.py).
Sizes in metres, orders of magnitude n (the nearest power of ten 10^n), ratios k = d2 / d1 ≈ 10^(n2 - n1), light travel s = c t.
Prints {id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json, math

a = {}
# Level 1: one formula, values given
a["fy1-1-L1-01"] = 7.5e-6 / 1e-6                     # red blood cell: 7,5·10⁻⁶ m / (10⁻⁶ m/µm) = 7,5 µm
a["fy1-1-L1-02"] = -2 - (-10)                        # figure fy1-1/scale-marks: ant at 10⁻² m, atom at 10⁻¹⁰ m (read off the gridlines): Δn = n₂ − n₁ = −2 − (−10) = 8
a["fy1-1-L1-03"] = 1.27e7 / 1000                     # Earth: 1,27·10⁷ m / 1000 m/km = 1,27·10⁴ km = 12 700 km
a["fy1-1-L1-04"] = 3.5e-10 / 1.4e-14                # lead atom / its nucleus: k = 3,5·10⁻¹⁰ m / 1,4·10⁻¹⁴ m = 2,5·10⁴
a["fy1-1-L1-05"] = 7.0e-5 / 7.5e-6                   # hair / red blood cell: k = 7,0·10⁻⁵ / 7,5·10⁻⁶ = 9,33
# Level 2: conversion, rearrangement or two steps
c = 2.998e8; year = 3.156e7
d_mw = 1.0e5 * 9.46e15                               # Milky Way: 1,0·10⁵ ly · 9,46·10¹⁵ m/ly = 9,46·10²⁰ m
a["fy1-1-L2-01"] = 8.8e26 / d_mw / 1e3              # observable universe / Milky Way = 9,30·10⁵ = 930 thousand
t_prox = 4.0e16 / c                                  # Proxima: t = s / c = 4,0·10¹⁶ m / 2,998·10⁸ m/s = 1,334·10⁸ s
a["fy1-1-L2-02"] = t_prox / year                     # in years: 1,334·10⁸ s / 3,156·10⁷ s = 4,23 a
a["fy1-1-L2-03"] = 4.0e7 / 1.7 / 1e6                 # people in a line round the Earth: 4,0·10⁷ m / 1,7 m = 2,35·10⁷ = 23,5 million
k_sun = 1.39e9 / 1.27e7                              # Sun / Earth diameters = 109,4
a["fy1-1-L2-04"] = k_sun ** 3 / 1e6                  # volumes ∝ d³: 109,4³ = 1,31·10⁶ = 1,31 million Earths fit in the Sun
# Level 3: reasoning and combining ideas
a["fy1-1-L3-01"] = (1.50e11 / 1.27e7) * 1.0 / 100    # Earth 1,0 cm: Sun at (1,50·10¹¹ / 1,27·10⁷) · 1,0 cm = 1,18·10⁴ cm = 118 m
n_planck, n_proton, n_human = -35, -15, 0            # 1,6·10⁻³⁵ → 10⁻³⁵ (a < 3); 1,7·10⁻¹⁵ → 10⁻¹⁵; 1,7 → 10⁰
a["fy1-1-L3-02"] = max(n_proton - n_planck, n_human - n_proton)   # 20 against 15: the larger difference is 20
magn = 5.0e-2 / 1.0e-7                               # electron micrograph: 5,0 cm / 1,0·10⁻⁷ m = 5,0·10⁵
a["fy1-1-L3-03"] = 7.5e-6 * magn * 100               # red blood cell image: 7,5·10⁻⁶ m · 5,0·10⁵ = 3,75 m = 375 cm
# Exercise bank additions (teacher 2026-11-04): L1-06 is multiple choice (no number)
a["fy1-1-L1-07"] = 3.84e8 / 2.998e8                  # Moon: t = s / c = 3,84·10⁸ m / 2,998·10⁸ m/s = 1,28 s
a["fy1-1-L1-08"] = 10 ** (-3 - (-7))                 # sand grain 10⁻³ m, virus 10⁻⁷ m: 4 steps -> 10⁴ times
# Level 2 (data)
r_au = {"Merkurius": 0.387, "Venus": 0.723, "Maa": 1.00, "Mars": 1.52, "Jupiter": 5.20, "Saturnus": 9.58, "Uranus": 19.2, "Neptunus": 30.1}   # table of L2-05 (AU)
a["fy1-1-L2-05"] = round(r_au["Jupiter"] / r_au["Neptunus"] * 200, 1)   # Neptune at 200 cm: Jupiter at 5,20 / 30,1 · 200 cm = 34,55 -> 34,6 cm
a["fy1-1-L2-06"] = 21 - 0                            # table of L2-06: Milky Way 9,46·10²⁰ m -> a > 3 -> 10²¹; human 1,7 m -> 10⁰; Δn = 21
sheets = [(50, 5.0), (100, 10.5), (150, 15.0), (200, 20.5), (250, 25.5), (300, 30.5)]   # table of L2-07: N sheets, stack height h in mm (ruler reads to 0,5 mm)
a["fy1-1-L2-07"] = round(sum(n * h for n, h in sheets) / sum(n * n for n, _ in sheets), 3)   # line through the origin: k = Σ N h / Σ N² = 23175 / 227500 = 0,1019 mm per sheet -> 0,102 (tolerance 0,05: 0,097…0,107)
# Level 3
drop = 4 / 3 * math.pi * (1.0e-3) ** 3               # raindrop d = 2,0 mm: V = (4/3) π r³ = 4,19·10⁻⁹ m³
rain = 5.0e-3 * 6.0e3 * (10 / 60)                    # 5,0 mm/h on 6,0·10³ m² for 10 min: 5,0·10⁻³ m · 6,0·10³ m² · (1/6) = 5,0 m³
a["fy1-1-L3-04"] = round(rain / drop / 1e9, 2)       # drops: 5,0 m³ / 4,19·10⁻⁹ m³ = 1,19·10⁹ -> 1,19 billion (milliard)
v_voy = 15.341; AU_km = 149597870.7; yr = 3.156e7    # Voyager 2: 15,341 km/s, 1 AU = 149 597 870,7 km, 1 a = 3,156·10⁷ s
a["fy1-1-L3-05"] = round(119.7 + v_voy * 7.25 * yr / AU_km, 1)   # model d = d0 + v t: 15,341 km/s · 7,25 a = 3,510·10⁹ km = 23,47 AU -> 143,2 AU
print(json.dumps(a))
