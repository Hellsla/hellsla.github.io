"""Numbers of the lesson text and inquiry.json for fy8-16, computed from their data (python -I lesson-answers.py); the
exercises' answers are in answers.py. Redshift z = (λ - λ0) / λ0, for small z the recession speed v ≈ c z, the
Hubble–Lemaître law v = H0 d, and the age estimate t = d / v = 1 / H0 (constant expansion rate).
Constants as in the module: c = 2,998e8 m/s = 2,998e5 km/s, h = 6,626e-34 J s, 1 eV = 1,602e-19 J;
1 Mpc = 3,086e22 m = 3,086e19 km, 1 a = 3,156e7 s. Laboratory wavelengths of hydrogen (air, NIST, rounded to 0,1 nm):
Hα 656,3 nm, Hβ 486,1 nm, Hγ 434,0 nm, Hδ 410,2 nm; calcium K line 393,4 nm.
The eight galaxies of the simulation (GALAXIES) are invented model values: v = 70 km/s/Mpc · d plus a fixed own motion
(peculiar velocity) of a few hundred km/s, z = v / c, λ = λ0 (1 + z); the same table is in assets/sims/fy8/fy8-16/sim.js.
Prints {id: number} as JSON on the last line."""
import json

a = {}
C_KMS = 2.998e5          # km/s
MPC_KM = 3.086e19        # km
YEAR_S = 3.156e7         # s
HA, HB, HG, HD, CAK = 656.3, 486.1, 434.0, 410.2, 393.4   # nm
H0_MODEL = 70.0          # km/s/Mpc, the law hidden in the simulation's model

# ---------------------------------------------------------------- the simulation's galaxies: (number, d in Mpc, own motion in km/s)
GALAXIES = [(1, 22, 260), (2, 45, -310), (3, 78, 190), (4, 110, -140), (5, 145, 330), (6, 185, -260), (7, 230, 150), (8, 275, -220)]
for k, d, vp in GALAXIES:
    v = H0_MODEL * d + vp
    z = v / C_KMS
    a[f"g{k}-d"] = d
    a[f"g{k}-v"] = v                           # km/s
    a[f"g{k}-z"] = z
    a[f"g{k}-lam"] = HA * (1 + z)              # observed Hα, nm
# least-squares line through the origin over the eight galaxies: H0 = Σ v d / Σ d²
a["fit-H0"] = sum(a[f"g{k}-v"] * d for k, d, _ in GALAXIES) / sum(d * d for _, d, _ in GALAXIES)   # 69,7 km/s/Mpc
a["fit-age"] = MPC_KM / a["fit-H0"] / YEAR_S / 1e9          # 1/H0 in 10⁹ a: 14,0
a["model-age"] = MPC_KM / H0_MODEL / YEAR_S / 1e9           # 1/(70 km/s/Mpc) = 13,97 · 10⁹ a
a["sim-H0-start"] = 50.0
a["sim-age-start"] = MPC_KM / 50.0 / YEAR_S / 1e9           # 19,56 · 10⁹ a

# ---------------------------------------------------------------- hook: every line shifted by the same fraction z = 0,0200
z_hook = 0.0200
a["hook-Ha"] = HA * (1 + z_hook)            # 669,43 -> 669,4 nm
a["hook-Hb"] = HB * (1 + z_hook)            # 495,82 -> 495,8 nm
a["hook-dHa"] = a["hook-Ha"] - HA           # 13,1 nm
a["hook-dHb"] = a["hook-Hb"] - HB           # 9,7 nm: the shifts differ, the ratio is the same
a["hook-ratio-a"] = 669.4 / HA              # 1,0200
a["hook-ratio-b"] = 495.8 / HB              # 1,0200

# ---------------------------------------------------------------- figure "spektri": an example galaxy with z = 0,050
a["fig-z"] = 0.050
a["fig-Ha"] = HA * 1.05                     # 689,1 nm
a["fig-dHa"] = HA * 0.05                    # 32,8 nm
a["fig-Hb"] = HB * 1.05                     # 510,4 nm

# ---------------------------------------------------------------- Kaava: the age estimate 1/H0 with H0 = 70 km/s/Mpc
a["age-s"] = MPC_KM / 70.0                  # 4,409e17 s
a["age-a"] = a["age-s"] / YEAR_S            # 1,397e10 a
a["mpc-ly"] = 3.086e22 / (2.998e8 * YEAR_S) # 1 Mpc = 3,26e6 light years

# ---------------------------------------------------------------- Esimerkki: Hα at 679,3 nm, d = 150 Mpc
ex_lam, ex_d = 679.3, 150
a["ex-dlam"] = ex_lam - HA                  # 23,0 nm
a["ex-z"] = (ex_lam - HA) / HA              # 0,035045
a["ex-v"] = C_KMS * a["ex-z"]               # 10 506 km/s -> 1,05 · 10⁴ km/s
a["ex-H0"] = a["ex-v"] / ex_d               # 70,04 -> 70,0 km/s/Mpc

# ---------------------------------------------------------------- the cosmic microwave background
a["cmb-stretch"] = 3000 / 2.725             # 1101: the wavelengths have grown about 1100-fold since 380 000 a
a["cmb-peak-mm"] = 2.898e-3 / 2.725 * 1e3   # Wien's law, given as data: 1,06 mm
a["cmb-E-eV"] = 6.626e-34 * 2.998e8 / 1.063e-3 / 1.602e-19   # 1,17e-3 eV per photon at 1,06 mm
a["ion-H-nm"] = 6.626e-34 * 2.998e8 / (13.6 * 1.602e-19) * 1e9  # a photon of 13,6 eV: 91,2 nm

# ---------------------------------------------------------------- Big Bang nucleosynthesis: n : p = 1 : 7, every neutron in He-4
n_, p_ = 1, 7
a["bbn-Y"] = 100 * 2 * n_ / (n_ + p_)       # 25 % of the mass in helium (n and p masses taken equal)
a["bbn-X"] = 100 - a["bbn-Y"]               # 75 % hydrogen

# ---------------------------------------------------------------- composition (Planck 2018 results VI, TT,TE,EE+lowE+lensing+BAO:
# Ω_Λ = 0,6889, Ω_m = 0,3111, Ω_b h² = 0,02242 with h = 0,6766, so Ω_b = 0,049 and dark matter 0,311 - 0,049 = 0,262)
a["ordinary"] = 100 * 0.02242 / 0.6766 ** 2                 # 4,9 %
a["dark-matter"] = 100 * 0.3111 - a["ordinary"]             # 26,2 %
a["dark-energy"] = 100 * 0.6889                             # 68,9 %

# ---------------------------------------------------------------- siirto: calcium K line 393,4 nm seen at 401,3 nm
si_dlam = 401.3 - CAK                       # 7,9 nm
a["siirto-z"] = si_dlam / CAK               # 0,020081
a["siirto-v"] = C_KMS * a["siirto-z"]       # 6020 km/s
a["siirto-d"] = a["siirto-v"] / 70          # 86,0 Mpc -> 86 Mpc (Δλ has two figures)
a["siirto-d-lam"] = C_KMS * si_dlam / 401.3 / 70   # mistake: divided by the observed λ: 84,3 Mpc
a["siirto-d-ms"] = 2.998e8 * a["siirto-z"] / 70    # mistake: c in m/s: 8,6e4

# ---------------------------------------------------------------- tarkistus-2: task figure, a line through (250 Mpc, 18 000 km/s)
a["t2-H0"] = 18000 / 250                    # 72 km/s/Mpc
a["t2-age"] = MPC_KM / 72 / YEAR_S / 1e9    # 13,6 · 10⁹ a

# ---------------------------------------------------------------- virhe: km not converted to m in 1/H0
a["virhe-wrong-s"] = 3.086e22 / 70          # 4,4e20 s: Mpc in metres over km/s
a["virhe-wrong-a"] = a["virhe-wrong-s"] / YEAR_S   # 1,4e13 a, a thousand times too long

# ---------------------------------------------------------------- tarkistus-3 / stars: triple alpha 3 He-4 -> C-12
a["3alpha-du"] = 3 * 4.002603 - 12.000000   # 0,007809 u
a["3alpha-Q"] = a["3alpha-du"] * 931.5      # 7,274 MeV
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
