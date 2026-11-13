"""Every answer in exercises.json for fy3-10, computed from the task data (python -I answers.py).
Ideal gas: pV = nRT with R = 8,31 J/(mol·K), p in Pa, V in m³, T = θ + 273,15 K. Amount of substance n = m/M.
Combined gas law p₁V₁/T₁ = p₂V₂/T₂ (fixed amount). Avogadro N_A = 6,022 · 10²³ 1/mol. 1 bar = 100 kPa.
Prints {exercise id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json

R = 8.31          # J/(mol·K)
N_A = 6.022e23    # 1/mol


def K(celsius):
    return celsius + 273.15        # T = θ + 273,15 K


a = {}
# Level 1: one formula, values given in SI units
a["fy3-10-L1-01"] = 1.01e5 * 0.250 / (R * 278)          # fridge air: n = pV/(RT) = 1,01·10⁵ Pa · 0,250 m³ / (8,31 · 278 K) = 10,93 mol -> 10,9 mol
p_pallo = 0.460 * R * 293 / 0.00710                      # basketball: p = nRT/V = 0,460 mol · 8,31 · 293 K / 0,00710 m³ = 157 750 Pa
a["fy3-10-L1-02"] = p_pallo / 1000                       # in kPa: 157,7 kPa -> 158 kPa
a["fy3-10-L1-03"] = 0.400 * R * 283 / 1.05e5             # life jacket CO₂: V = nRT/p = 0,400 · 8,31 · 283 / 1,05·10⁵ = 0,008959 m³ -> 0,00896 m³
a["fy3-10-L1-04"] = 1.13e5 * 0.200 / (8.40 * R)          # sealed barrel in the sun: T = pV/(nR) = 1,13·10⁵ · 0,200 / (8,40 · 8,31) = 323,8 K -> 324 K
a["fy3-10-L1-05"] = 425 / 44                             # soda maker CO₂: n = m/M = 425 g / 44 g/mol = 9,659 mol -> 9,7 mol
# Level 2: two steps or conversions
n_happi = 2.40 / 0.0320                                  # ambulance O₂ bottle weighed: n = m/M = 2,40 kg / 0,0320 kg/mol = 75,0 mol
p_happi = n_happi * R * K(15) / 10.0e-3                  # p = nRT/V = 75,0 mol · 8,31 · 288,15 K / 0,0100 m³ = 1,796·10⁷ Pa
a["fy3-10-L2-01"] = p_happi / 1e5                        # 1 bar = 10⁵ Pa: 179,6 bar -> 180 bar
n_tuntematon = 101e3 * 1.00e-3 / (R * K(22))             # glass bulb 1,00 l at 101 kPa, 295,15 K: n = pV/(RT) = 0,04118 mol
a["fy3-10-L2-02"] = 1.15 / n_tuntematon                  # M = m/n = 1,15 g / 0,04118 mol = 27,93 g/mol -> 27,9 g/mol (typpi, 28)
T2_diesel = K(30) * (4.60e6 * 0.0300) / (101e3 * 0.500)  # combined law T₂ = T₁ p₂V₂/(p₁V₁) = 303,15 K · 4,60 MPa · 0,0300 l / (101 kPa · 0,500 l) = 828,4 K
a["fy3-10-L2-03"] = T2_diesel - 273.15                   # back to celsius: 555,3 °C -> 555 °C
# fy3-10/pt-suorat (2,00 l vessels): A reads (400 K; 100 kPa), B reads (400 K; 60 kPa) off the gridlines
n_A = 100e3 * 2.00e-3 / (R * 400)                        # n = pV/(RT) = 100 000 Pa · 0,00200 m³ / (8,31 · 400 K) = 0,06017 mol
n_B = 60e3 * 2.00e-3 / (R * 400)                         # B: 60 000 Pa · 0,00200 m³ / (8,31 · 400 K) = 0,03610 mol
a["fy3-10-L2-04"] = n_A - n_B                            # difference 0,02407 mol -> 0,024 mol
# Level 3: reasoning or an unfamiliar context
n_henkays = 101e3 * 0.55e-3 / (R * K(37))                # one breath 0,55 l at 101 kPa, 310,15 K: n = pV/(RT) = 0,02155 mol
a["fy3-10-L3-01"] = n_henkays * N_A / 1e22               # N = n N_A = 1,298·10²² molecules; answer in units of 10²² -> 1,3
n_ikkuna = 6.0 / (40 - 29)                               # window: argon fill is 6,0 g heavier; same n for both gases, n = Δm/(M_Ar − M_ilma) = 0,5455 mol
V_ikkuna = n_ikkuna * R * K(20) / 101e3                  # gap volume V = nRT/p = 0,5455 mol · 8,31 · 293,15 K / 101 000 Pa = 0,01316 m³
a["fy3-10-L3-02"] = V_ikkuna / (1.20 * 1.00) * 1000      # thickness d = V/A = 0,01316 m³ / 1,20 m² = 0,01096 m -> 11 mm
dp = (10.0 - 7.0) * 1e5                                  # gauge readings 10,0 -> 7,0 bar: Δp = 3,0 bar = 3,0·10⁵ Pa (atmospheric pressure cancels)
dn = dp * 200e-3 / (R * K(18))                           # V and T constant: Δn = ΔpV/(RT) = 3,0·10⁵ · 0,200 / (8,31 · 291,15) = 24,80 mol
a["fy3-10-L3-03"] = dn * 0.029                           # Δm = Δn M = 24,80 mol · 0,029 kg/mol = 0,7192 kg -> 0,72 kg
# Added exercises (bank P1)
# L1-07: balloon, n constant: V₂ = V₁ p₁T₂/(p₂T₁) = 2,50 l · 101 · 264,15 / (98 · 294,15) = 2,314 l -> 2,31 l
a["fy3-10-L1-07"] = 2.50 * 101 * K(-9) / (98 * K(21))
# L2-05: tyre, V constant: n₂/n₁ = p₂T₁/(p₁T₂) = 305 · 278,15 / (300 · 299,15) = 0,9453; leaked share 1 − 0,9453 = 5,47 %
a["fy3-10-L2-05"] = (1 - 305 * K(5.0) / (300 * K(26.0))) * 100
# L2-06: slope read from the fitted line (280 K; 115,4 cm³) and (360 K; 148,0 cm³): k = 0,4075 cm³/K, n = k p / R = 4,953 mmol
k_ruisku = (148.0 - 115.4) * 1e-6 / (360 - 280)           # m³/K
a["fy3-10-L2-06"] = k_ruisku * 101e3 / R * 1000           # mmol
# L3-04: helium cylinder 20,0 l: (5,0 °C; 14,2 bar), (21,0 °C; 11,0 bar), (21,0 °C; 6,5 bar); n = pV/(RT) at each moment
n_h1 = 14.2e5 * 0.0200 / (R * K(5.0))                     # 12,29 mol
n_h3 = 6.5e5 * 0.0200 / (R * K(21.0))                     # 5,318 mol
a["fy3-10-L3-04"] = (n_h1 - n_h3) * 4.0                   # used mass m = Δn M = 6,968 mol · 4,0 g/mol = 27,87 g -> 28 g
# (c) balloon n = 101 kPa · 5,0 l / (R 294,15 K) = 0,2066 mol: 33,7 balloons used; 21,7 more down to 101 kPa
# L3-05: weather balloon, n = p₀V₀/(RT₀) = 105,4 mol; V₁₀ = nRT/p at 10 km (26,5 kPa, −50,0 °C) = 7,379 m³ (V₁₅ = 15,69 m³ > 12,0 m³)
n_pallo = 101e3 * 2.50 / (R * K(15.0))
a["fy3-10-L3-05"] = n_pallo * R * K(-50.0) / 26.5e3
# Added exercises (teacher 2026-11-12: MAFY table task, figure task)
a["fy3-10-L1-09"] = (500 / 39.95) * R * 293 / 0.0100 / 1e6   # MAFY argon M = 39,95 g/mol: n = m/M = 12,52 mol; p = nRT/V = 3,047e6 Pa = 3,05 MPa
a["fy3-10-L2-09"] = 100e3 / 60e3                         # fy3-10/pt-suorat: same V, n ∝ p/T slope; at 400 K n_A/n_B = 100 kPa / 60 kPa = 1,667 -> 1,67
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
