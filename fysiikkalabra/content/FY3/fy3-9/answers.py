"""Every answer in exercises.json for fy3-9, computed from the task data (python -I answers.py).
Boyle: p₁V₁ = p₂V₂ (T constant). Isobaric: V₁/T₁ = V₂/T₂. Isochoric: p₁/T₁ = p₂/T₂. Temperatures in kelvins.
Hydrostatic pressure from fy3-4: p = p₀ + ρgh. Gauge pressure (ylipaine) = absolute pressure − ilmanpaine.
Prints {exercise id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json


def K(celsius):
    return celsius + 273.15        # T = θ + 273,15 K (using 273 changes no rounded answer)


g, rho_vesi, p0 = 9.81, 1000, 101   # m/s², kg/m³, kPa
a = {}
# Level 1: one formula, values given
a["fy3-9-L1-01"] = 101 * 30.0 / 45.0                     # syringe pulled 30,0 -> 45,0 ml: p₂ = p₁V₁/V₂ = 67,33 kPa -> 67,3 kPa
a["fy3-9-L1-02"] = 160 * 24.0 / 280                      # cottage pressure tank air 24,0 l, 160 -> 280 kPa: V₂ = p₁V₁/p₂ = 13,71 l -> 13,7 l
a["fy3-9-L1-03"] = 430 * 1.00 / 1.50                     # water rocket air 1,00 -> 1,50 l: p₂ = 430 kPa · 1,00 l / 1,50 l = 286,7 kPa -> 287 kPa
a["fy3-9-L1-04"] = 3.0 * K(-18) / K(22)                  # balloon, isobaric 295,15 K -> 255,15 K: V₂ = V₁T₂/T₁ = 2,593 l -> 2,6 l
a["fy3-9-L1-05"] = 101 * K(-18) / K(22)                  # chest freezer, isochoric 295,15 K -> 255,15 K: p₂ = p₁T₂/T₁ = 87,31 kPa -> 87,3 kPa
# Level 2: two steps, a conversion or a rearrangement
p_pullo = 300 * 100                                      # 300 bar = 30 000 kPa
V_ulkona_l = p_pullo * 6.8 / 101                         # Boyle: V₂ = p₁V₁/p₂ = 30 000 kPa · 6,8 l / 101 kPa = 2020 l
a["fy3-9-L2-01"] = V_ulkona_l / 1000                     # 2020 l = 2,02 m³ -> 2,0 m³
T_korkki = K(20) * 125 / 101                             # isochoric, solve T₂ = T₁p₂/p₁ = 293,15 K · 125/101 = 362,8 K
a["fy3-9-L2-02"] = T_korkki - 273.15                     # back to celsius: 89,7 °C -> 90 °C
V_ml = [10.0, 12.5, 15.0, 20.0, 25.0, 30.0]              # syringe data, ml
p_kPa = [203, 159, 134, 99, 81, 66]                      # pressures, kPa
x = [1 / v for v in V_ml]                                # new column 1/V, 1/ml
kerroin = sum(xi * pi for xi, pi in zip(x, p_kPa)) / sum(xi * xi for xi in x)   # least-squares line through origin: slope = pV = 2009 kPa·ml
a["fy3-9-L2-03"] = kerroin * 1e3 * 1e-6                        # 1 kPa·ml = 10³ Pa · 10⁻⁶ m³ = 10⁻³ J: pV = 2,01 J -> 2,0 J
V_lammin = 2800 * K(100) / K(10)                         # hot-air balloon, isobaric: V₂ = V₁T₂/T₁ = 2800 m³ · 373,15/283,15 = 3690 m³
a["fy3-9-L2-04"] = V_lammin - 2800                       # pushed out through the opening: 3690 − 2800 = 890 m³
# Level 3: reasoning or an unfamiliar context
p_syva = p0 + rho_vesi * g * 20.0 / 1000                 # pressure at 20,0 m: p = p₀ + ρgh = 101 + 196,2 = 297,2 kPa
a["fy3-9-L3-01"] = p_syva * 2.0 / p0                     # Boyle to the surface: V₂ = 297,2 kPa · 2,0 cm³ / 101 kPa = 5,885 cm³ -> 5,9 cm³
p1_rengas = 250 + p0                                     # absolute pressure = gauge + atmospheric = 351 kPa
p2_rengas = p1_rengas * K(-20) / K(20)                   # isochoric 293,15 K -> 253,15 K: p₂ = 303,1 kPa (absolute)
a["fy3-9-L3-02"] = p2_rengas - p0                        # gauge reading 303,1 − 101 = 202,1 kPa -> 202 kPa
p_rengas_abs = 300 + p0                                  # tyre absolute pressure 401 kPa
L_ilma = 40.0 * p0 / p_rengas_abs                        # uniform cylinder, V ∝ length: Boyle L₂ = 40,0 cm · 101/401 = 10,07 cm
a["fy3-9-L3-03"] = 40.0 - L_ilma                         # piston travel before the valve opens: 40,0 − 10,07 = 29,93 cm -> 29,9 cm
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
