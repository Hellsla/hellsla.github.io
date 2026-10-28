"""Every answer in exercises.json and inquiry.json for fy1-1, computed from the task data (python -I answers.py).
Sizes in metres, orders of magnitude n (the nearest power of ten 10^n), ratios k = d2 / d1 ≈ 10^(n2 - n1), light travel s = c t.
Prints {id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json, math

a = {}
# Level 1: one formula, values given
a["fy1-1-L1-01"] = 7.5e-6 / 1e-6                     # red blood cell: 7,5·10⁻⁶ m / (10⁻⁶ m/µm) = 7,5 µm
a["fy1-1-L1-02"] = -2 - (-10)                        # orders 10⁻² m (ant) and 10⁻¹⁰ m (atom): Δn = n₂ − n₁ = −2 − (−10) = 8
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

# Inquiry numbers (inquiry.json), not exercises
a["inq-exp1-dn"] = -10 - (-15)                       # hydrogen atom 10⁻¹⁰ m, its nucleus (a proton) 10⁻¹⁵ m: Δn = 5
a["inq-exp1-ratio"] = 1.1e-10 / 1.7e-15              # mistake: the factor 6,5·10⁴ is not the number of powers
a["inq-exp2-dn"] = 21 - 13                           # Neptune's orbit 10¹³ m (4,5·10¹² m radius, 9,0·10¹² m across), Milky Way 10²¹ m: Δn = 8
a["inq-exp3-mid"] = (-35 + 27) / 2                   # midpoint of the exponents: −4
a["inq-siirto"] = 360 / 7.2 * 800 / math.pi          # Earth's diameter: C = (360° / 7,2°) · 800 km = 40 000 km, d = C / π = 12 700 km
a["inq-siirto-c"] = 360 / 7.2 * 800                  # mistake: the circumference 40 000 km
a["inq-siirto-r"] = 360 / 7.2 * 800 / math.pi / 2    # mistake: the radius 6370 km
a["inq-siirto-1deg"] = 800 / 7.2                     # mistake: the length of one degree 111 km
a["inq-check2"] = 1.39e9 / 2.4e4                     # Sun / neutron star diameters: k = 1,39·10⁹ m / 2,4·10⁴ m = 5,79·10⁴
a["inq-check2-inv"] = 2.4e4 / 1.39e9                 # mistake: divided the wrong way round, 1,73·10⁻⁵
a["inq-example-k"] = 1.1e-10 / 1.7e-15               # example: k = 1,1·10⁻¹⁰ / 1,7·10⁻¹⁵ = 6,5·10⁴
a["inq-example-dn"] = -10 - (-15)                    # example: Δn = 5
print(json.dumps(a))
