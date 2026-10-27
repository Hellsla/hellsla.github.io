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
V_mooli = 1.00 * R * K(-30) / 102e3                      # one mole at −30 °C = 243,15 K and 102 kPa: V = nRT/p = 0,01981 m³
a["fy3-10-L2-04"] = V_mooli * 1000                       # in litres: 19,81 l -> 19,8 l
# Level 3: reasoning or an unfamiliar context
n_henkays = 101e3 * 0.55e-3 / (R * K(37))                # one breath 0,55 l at 101 kPa, 310,15 K: n = pV/(RT) = 0,02155 mol
a["fy3-10-L3-01"] = n_henkays * N_A / 1e22               # N = n N_A = 1,298·10²² molecules; answer in units of 10²² -> 1,3
n_ikkuna = 6.0 / (40 - 29)                               # window: argon fill is 6,0 g heavier; same n for both gases, n = Δm/(M_Ar − M_ilma) = 0,5455 mol
V_ikkuna = n_ikkuna * R * K(20) / 101e3                  # gap volume V = nRT/p = 0,5455 mol · 8,31 · 293,15 K / 101 000 Pa = 0,01316 m³
a["fy3-10-L3-02"] = V_ikkuna / (1.20 * 1.00) * 1000      # thickness d = V/A = 0,01316 m³ / 1,20 m² = 0,01096 m -> 11 mm
dp = (10.0 - 7.0) * 1e5                                  # gauge readings 10,0 -> 7,0 bar: Δp = 3,0 bar = 3,0·10⁵ Pa (atmospheric pressure cancels)
dn = dp * 200e-3 / (R * K(18))                           # V and T constant: Δn = ΔpV/(RT) = 3,0·10⁵ · 0,200 / (8,31 · 291,15) = 24,80 mol
a["fy3-10-L3-03"] = dn * 0.029                           # Δm = Δn M = 24,80 mol · 0,029 kg/mol = 0,7192 kg -> 0,72 kg

# Inquiry (not exercises): the weighing table "Punnitaan pallot" and R from it.
R_tarkka = 8.314                                          # J/(mol·K), used only to make the example masses
n_pallo = 101e3 * 5.00e-3 / (R_tarkka * K(20))           # 5,00 l at 101 kPa, 293,15 K: n = pV/(RT) = 0,2072 mol
M_kaasut = {"He": 4.00, "N2": 28.0, "ilma": 29.0, "CO2": 44.0}    # g/mol
m_tarkka = {k: n_pallo * M for k, M in M_kaasut.items()}           # He 0,8288 g, N₂ 5,802 g, ilma 6,009 g, CO₂ 9,117 g
m_taulukko = {"He": 0.83, "N2": 5.78, "ilma": 6.02, "CO2": 9.10}   # example values in the table: exact masses with ±0,02 g scatter
for k in M_kaasut:
    assert abs(m_taulukko[k] - m_tarkka[k]) <= 0.025, k
    a["inq-n-" + k] = m_taulukko[k] / M_kaasut[k]         # m/M: He 0,2075, N₂ 0,2064, ilma 0,2076, CO₂ 0,2068 mol
n_ka = sum(m_taulukko[k] / M_kaasut[k] for k in M_kaasut) / 4      # mean 0,2071 mol
a["inq-n-ka"] = n_ka
a["inq-R"] = 101e3 * 5.00e-3 / (n_ka * K(20))             # R = pV/(nT) = 101 000 Pa · 0,00500 m³ / (0,2071 mol · 293,15 K) = 8,32 J/(mol·K)
a["inq-ka-ilma-He"] = m_taulukko["ilma"] / m_taulukko["He"]  # air balloon gas is 7,25 times heavier than helium
a["inq-n-He-kaanteinen"] = M_kaasut["He"] / m_taulukko["He"]  # mistake M/m = 4,82
a["inq-n-He-tulo"] = M_kaasut["He"] * m_taulukko["He"]        # mistake m·M = 3,32
# Student computes R from the helium row: pV/(nT) with n = m/M = 0,2075 mol
n_He = m_taulukko["He"] / M_kaasut["He"]
a["inq-R-He"] = 101e3 * 5.00e-3 / (n_He * K(20))           # 101 000 Pa · 0,00500 m³ / (0,2075 mol · 293,15 K) = 8,302 J/(mol·K)
a["inq-R-He-celsius"] = 101e3 * 5.00e-3 / (n_He * 20)      # mistake: T = 20 -> 121,7
a["inq-R-He-litra"] = 101e3 * 5.00 / (n_He * K(20))        # mistake: V in litres -> 8302
a["inq-R-He-kPa"] = 101 * 5.00e-3 / (n_He * K(20))         # mistake: p in kPa -> 0,008302
# Koe 2 challenge: at 600 K, V = 100 %, p/p_ref = (N/100)(T/300 K) = 1,00 needs N = 100 · 300/600 = 50
a["inq-koe2-N"] = 100 * 300 / 600
a["inq-koe2-N-sqrt"] = 100 / 2 ** 0.5                     # mistake: dividing by √2 ≈ 1,41 gives 70,7
a["inq-koe2-N-200-p"] = (200 / 100) * (600 / 300)         # mistake N = 200 at 600 K: p/p_ref = 4,00
a["inq-koe2-N-25-p"] = (25 / 100) * (600 / 300)           # mistake N = 25 at 600 K: p/p_ref = 0,50
# pred-N: N doubles at fixed T and V -> p/p_ref = 200/100 = 2
a["inq-predN"] = 200 / 100

print(json.dumps({k: round(v, 6) for k, v in a.items()}))
