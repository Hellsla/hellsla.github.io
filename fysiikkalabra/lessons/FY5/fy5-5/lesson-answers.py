"""Numbers of the lesson text and inquiry.json for fy5-5, computed from their data (python -I lesson-answers.py); the
exercises' answers are in answers.py. Newton's law of gravitation F = γ m1 m2 / r², field strength g = γ M / r².
Data: NASA Planetary Fact Sheet and Sun Fact Sheet (nssdc.gsfc.nasa.gov, read 2026): masses and equatorial radii.
Prints {id: number} as JSON."""
import json, math

gamma = 6.674e-11                                        # N·m²/kg²
M_E, R_E = 5.972e24, 6.378e6                             # Earth: mass (kg), equatorial radius (m)
M_M, R_M = 7.346e22, 1.738e6                             # Moon
M_Ma, R_Ma = 6.417e23, 3.396e6                           # Mars
M_J, R_J = 1.898e27, 7.149e7                             # Jupiter
M_S, R_S = 1.989e30, 6.957e8                             # Sun
d_EM, T_M = 3.844e8, 27.32 * 24 * 3600                   # Earth–Moon mean distance (m), sidereal month (s)
a = {}
# Kaava: the table of field strengths g = γM/R² at the surface (equator, without the effect of rotation)
a["g-maa"] = gamma * M_E / R_E ** 2                      # 9,80 m/s²
a["g-kuu"] = gamma * M_M / R_M ** 2                      # 1,62 m/s²
a["g-mars"] = gamma * M_Ma / R_Ma ** 2                   # 3,71 m/s²
a["g-jupiter"] = gamma * M_J / R_J ** 2                  # 24,8 m/s²
a["g-aurinko"] = gamma * M_S / R_S ** 2                  # 274 m/s²
# Ydinajatus: an apple 0,20 kg on Earth: force, apple's and Earth's accelerations
m_o = 0.20
a["omena-F"] = gamma * M_E * m_o / R_E ** 2              # 1,96 N
a["omena-a"] = a["omena-F"] / m_o                        # 9,80 m/s²
a["maa-a"] = a["omena-F"] / M_E                          # 3,3e-25 m/s²
# Two people 1,0 m apart, 70 kg and 60 kg (Ydinajatus)
a["ihmiset-F"] = gamma * 70 * 60 / 1.0 ** 2              # 2,8e-7 N = 0,28 µN
a["ihminen-G"] = 70 * gamma * M_E / R_E ** 2            # Earth's pull on the 70 kg person: 686 N, "lähes 700 N"
# Misconception: field strength at the height 300 km
a["g-300km"] = gamma * M_E / (R_E + 3.0e5) ** 2          # 8,94 m/s² -> "noin 8,9"
# Esimerkki: the force between Earth and Moon
a["ex-F"] = gamma * 5.97e24 * 7.35e22 / 3.84e8 ** 2      # with the rounded data of the text: 1,99e20 N
a["ex-F-arvio"] = 7e-11 * 6e24 * 7e22 / (4e8) ** 2       # round-number check: 1,8e20 N
a["ex-aM"] = a["ex-F"] / 7.35e22                            # the Moon's acceleration 2,702e-3 m/s²
# Simulation (model values): two boulders, masses in tonnes, F in µN, a in nm/s²
def F_uN(m1t, m2t, r): return gamma * m1t * 1e3 * m2t * 1e3 / r ** 2 * 1e6
def a_nm(m_other_t, r): return gamma * m_other_t * 1e3 / r ** 2 * 1e9
# Ennuste 1 / koe 1: m1 = 10 t, r = 4,0 m, m2 = 2, 4, 6, 8, 10 t
for m2 in (2, 4, 6, 8, 10):
    a[f"koe1-F-{m2}"] = F_uN(10, m2, 4.0)                # 83,4 … 417 µN, the same on both bodies
    a[f"koe1-a1-{m2}"] = a_nm(m2, 4.0)                   # a1 = γ m2/r²: 8,34 … 41,7 nm/s²
a["koe1-a2"] = a_nm(10, 4.0)                             # a2 = γ m1/r² = 41,7 nm/s², whatever m2 is
# Ennuste 2 / koe 2: m1 = m2 = 10 t, r = 3, 6, 9 m (and 2, 4, 8)
for r in (2, 3, 4, 6, 8, 9):
    a[f"koe2-F-{r}"] = F_uN(10, 10, r)                   # 1670, 742, 417, 185, 104, 82,4 µN
a["koe2-suhde"] = F_uN(10, 10, 3) / F_uN(10, 10, 6)      # doubling r: 4
a["koe2-Fr2"] = F_uN(10, 10, 3) * 3 ** 2                 # F·r² = 6674 µN·m², the same at every r
# Moon test (optional interpret): the Moon's normal acceleration from its orbit (previous chapter) and γM/r²
a["kuu-an-mm"] = 4 * math.pi ** 2 * d_EM / T_M ** 2 * 1e3   # 2,72 mm/s²
a["kuu-g-mm"] = gamma * M_E / d_EM ** 2 * 1e3            # 2,70 mm/s²
a["kuu-suhde"] = a["g-maa"] / (a["kuu-an-mm"] / 1e3)     # about 3600 = 60²
a["kuu-etaisyys-R"] = d_EM / R_E                         # 60,3 Earth radii
# Transfer task: height above the surface where g is half its surface value, R = 6378 km: h = R(√2 − 1)
a["siirto-h-km"] = R_E * (math.sqrt(2) - 1) / 1e3        # 2642 km -> 2640 km
a["siirto-virhe-R"] = R_E / 1e3                          # mistake: halving 1/r² by doubling r -> h = R
a["siirto-virhe-r"] = R_E * math.sqrt(2) / 1e3           # mistake: r instead of the height, 9020 km
# Check 2: F = 12 N; one mass tripled, distance doubled -> 12 · 3 / 4
a["check2"] = 12 * 3 / 2 ** 2                            # 9,0 N
a["check2-virhe-a"] = 12 * 3 / 2                         # 18 N: distance taken once, not squared
a["check2-virhe-b"] = 12 * 3 * 4                         # 144 N: multiplied by 4
# Error spotting: g at the height 300 km; the wrong solution put r = 300 km
a["virhe-oikea"] = gamma * 5.97e24 / (R_E + 3.0e5) ** 2   # 8,93 m/s²
a["virhe-vaara"] = gamma * 5.97e24 / (3.0e5) ** 2         # 4430 m/s² -> "noin 4400"
# Simulation box: how far a boulder would move in one minute at the largest acceleration (m = 10 t, r = 2,0 m)
a["sim-s-min-mm"] = 0.5 * gamma * 1e4 / 2.0 ** 2 * 60 ** 2 * 1e3   # 0,30 mm
# Check 1: astronaut 80 kg on the Moon
a["check1-G"] = 80 * a["g-kuu"]                          # 130 N
a["check1-G-maa"] = 80 * 9.81                            # 785 N, about six times
# Exit ticket: two 1,0 kg masses 1,0 m apart
a["exit-F"] = gamma * 1.0 * 1.0 / 1.0 ** 2               # 6,67e-11 N
print(json.dumps({k: round(v, 6) if abs(v) > 1e-3 else float(f"{v:.6g}") for k, v in a.items()}))
