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
n_happi = 200 * 1e5 * 10.0e-3 / (R * K(15))              # ambulance O₂ bottle: 200 bar = 2,00·10⁷ Pa, 10,0 l = 0,0100 m³, 288,15 K -> n = 83,52 mol
a["fy3-10-L2-01"] = n_happi * 0.032                      # m = nM = 83,52 mol · 0,032 kg/mol = 2,673 kg -> 2,7 kg
n_tuntematon = 101e3 * 1.00e-3 / (R * K(22))             # glass bulb 1,00 l at 101 kPa, 295,15 K: n = pV/(RT) = 0,04118 mol
a["fy3-10-L2-02"] = 1.15 / n_tuntematon                  # M = m/n = 1,15 g / 0,04118 mol = 27,93 g/mol -> 27,9 g/mol (typpi, 28)
T2_diesel = K(30) * (4.60e6 * 0.0300) / (101e3 * 0.500)  # combined law T₂ = T₁ p₂V₂/(p₁V₁) = 303,15 K · 4,60 MPa · 0,0300 l / (101 kPa · 0,500 l) = 828,3 K
a["fy3-10-L2-03"] = T2_diesel - 273.15                   # back to celsius: 555,1 °C -> 555 °C
V_mooli = 1.00 * R * K(-30) / 102e3                      # one mole at −30 °C = 243,15 K and 102 kPa: V = nRT/p = 0,01981 m³
a["fy3-10-L2-04"] = V_mooli * 1000                       # in litres: 19,81 l -> 19,8 l
# Level 3: reasoning or an unfamiliar context
n_henkays = 101e3 * 0.55e-3 / (R * K(37))                # one breath 0,55 l at 101 kPa, 310,15 K: n = pV/(RT) = 0,02155 mol
a["fy3-10-L3-01"] = n_henkays * N_A / 1e22               # N = n N_A = 1,298·10²² molecules; answer in units of 10²² -> 1,3
n_ikkuna = 101e3 * 12.0e-3 / (R * K(20))                 # window gap 12,0 l at 101 kPa, 293,15 K: same n for argon and air = 0,4975 mol
a["fy3-10-L3-02"] = n_ikkuna * (40 - 29)                 # Δm = n(M_Ar − M_ilma) = 0,4975 mol · 11 g/mol = 5,473 g -> 5,5 g
dp = (10.0 - 7.0) * 1e5                                  # gauge readings 10,0 -> 7,0 bar: Δp = 3,0 bar = 3,0·10⁵ Pa (atmospheric pressure cancels)
dn = dp * 200e-3 / (R * K(18))                           # V and T constant: Δn = ΔpV/(RT) = 3,0·10⁵ · 0,200 / (8,31 · 291,15) = 24,80 mol
a["fy3-10-L3-03"] = dn * 0.029                           # Δm = Δn M = 24,80 mol · 0,029 kg/mol = 0,7192 kg -> 0,72 kg

print(json.dumps({k: round(v, 6) for k, v in a.items()}))
