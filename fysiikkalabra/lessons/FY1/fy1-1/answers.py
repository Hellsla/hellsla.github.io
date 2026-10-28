"""Every answer in exercises.json for fy1-1, computed from the task data (python -I answers.py).
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
print(json.dumps(a))
