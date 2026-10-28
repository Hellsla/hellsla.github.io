"""Numbers of the lesson text and inquiry.json for fy3-10, computed from their data (python -I lesson-answers.py); the
exercises' answers are in answers.py. Same model and symbols as there. Prints {id: number} as JSON on the last line."""
import json

R = 8.31          # J/(mol·K)
N_A = 6.022e23    # 1/mol


def K(celsius):
    return celsius + 273.15        # T = θ + 273,15 K


a = {}
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
# check-c2: rigid vessel heated from 20 °C to 40 °C: p2/p1 = T2/T1 = 313,15 / 293,15 = 1,068 -> about 7 %
a["inq-c2-suhde"] = K(40) / K(20)                         # 1,068
a["inq-c2-prosentti"] = (K(40) / K(20) - 1) * 100         # 6,8 % (mistakes: 100 % doubling, 20 % from the 20 degrees)

print(json.dumps({k: round(v, 6) for k, v in a.items()}))
