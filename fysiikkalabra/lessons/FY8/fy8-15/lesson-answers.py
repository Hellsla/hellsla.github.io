"""Numbers of the lesson text and inquiry.json for fy8-15, computed from their data (python -I lesson-answers.py); the
exercises' answers are in answers.py. Charges q in units of the elementary charge e (quarks +2/3 and -1/3, an
antiparticle the opposite), baryon number B = (quarks - antiquarks) / 3, lepton number L (lepton +1, antilepton -1),
energy released in a decay Q = (m_before - m_after) c^2 with masses in MeV/c^2.
Masses: Particle Data Group, Review of Particle Physics 2024 (MeV/c^2, rounded as in the text).
Prints {id: number} as JSON on the last line."""
import json
from fractions import Fraction as F

a = {}
QQ = {"u": F(2, 3), "d": F(-1, 3), "s": F(-1, 3), "c": F(2, 3)}
def charge(quarks, anti=""):
    """Charge in e of a hadron with the quarks `quarks` and the antiquarks `anti`."""
    return sum(QQ[k] for k in quarks) - sum(QQ[k] for k in anti)
def baryon(quarks, anti=""):
    return F(len(quarks) - len(anti), 3)

# ---------------------------------------------------------------- hadrons (Ydinajatus, figure, interpret table)
a["p-q"] = float(charge("uud"))              # +1
a["n-q"] = float(charge("udd"))              # 0
a["dpp-q"] = float(charge("uuu"))            # Delta++: +2 (table)
a["dm-q"] = float(charge("ddd"))             # Delta-: -1 (table)
a["pip-q"] = float(charge("u", "d"))         # pi+ = u anti-d: +1
a["pim-q"] = float(charge("d", "u"))         # pi- = d anti-u: -1
a["p-B"] = float(baryon("uud"))              # 1
a["pip-B"] = float(baryon("u", "d"))         # 0
# interpret: Delta++ = uuu has q = +2, so one u carries 2/3; Delta- = ddd has -1, so d carries -1/3
a["tutki-u"] = 2 / 3                         # 0,667 (answer of the interpret question)
a["tutki-d"] = -1 / 3
# the wrong models of the prediction: u = +1, d = 0 gives the neutron udd +1; u = +1, d = -1 gives the neutron -1
a["malli-u1d0-n"] = 1 + 0 + 0
a["malli-u1dm1-n"] = 1 - 1 - 1

# ---------------------------------------------------------------- the electric force against gravity, two protons
k, e, G, mp_kg = 8.988e9, 1.602e-19, 6.674e-11, 1.6726e-27
a["Fe/Fg"] = k * e ** 2 / (G * mp_kg ** 2)   # 1,235e36 at any distance -> "noin 10^36"

# ---------------------------------------------------------------- masses (MeV/c^2) and the muon
m_e, m_mu, m_p, m_n = 0.511, 105.658, 938.272, 939.565
a["mu/e"] = m_mu / m_e                       # 206,8 -> "noin 207 kertaa"
# quark masses u 2,16 and d 4,70 MeV/c^2 (PDG 2024): their sum in the proton is about 1 % of its mass
a["quark-share"] = 100 * (2 * 2.16 + 4.70) / m_p   # 0,961 % -> "noin 1 %"

# ---------------------------------------------------------------- annihilation and pair production
a["annih-keV"] = m_e * 1000                  # each photon 511 keV when e- and e+ annihilate at rest
a["pair-MeV"] = 2 * m_e                      # at least 1,022 MeV for gamma -> e- + e+

# ---------------------------------------------------------------- neutron decay (Kaava, worked example)
a["esim-Q"] = m_n - m_p - m_e                # 0,782 MeV
a["esim-diff"] = m_n - m_p                   # 1,293 MeV
a["n-life-min"] = 878.4 / 60                 # mean lifetime 878,4 s -> 14,6 min, "noin 15 min"

# ---------------------------------------------------------------- hook: Super-Kamiokande holds 50 000 t of water
N_A = 6.022e23
a["superk-protons"] = 50e6 / 0.018015 * N_A * 10      # all protons (2 in H, 8 in O): 1,67e34 -> "yli 10^33"
a["superk-free"] = 50e6 / 0.018015 * N_A * 2          # free protons of hydrogen: 3,3e33

# ---------------------------------------------------------------- LHC
a["lhc-ratio"] = 6.8e6 / m_p                 # a 6,8 TeV proton has about 7200 times its rest energy
a["lhc-sum"] = 2 * 6.8                       # collision energy 13,6 TeV

# ---------------------------------------------------------------- transfer task: muon decay mu- -> e- + anti-nu_e + nu_mu
a["siirto"] = m_mu - m_e                     # 105,147 MeV, to 0,001 MeV as the masses (neutrino masses below 1 eV)
a["siirto-wrong-sum"] = m_mu + m_e           # 106,169: masses added
# check 2: D+ = c anti-d: +2/3 + 1/3 = +1
a["tarkistus-2"] = float(charge("c", "d"))   # 1
a["tarkistus-2-wrong"] = float(QQ["c"] + QQ["d"])   # 0,333: antiquark's sign not flipped
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
