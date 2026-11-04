"""Numbers of the lesson text and inquiry.json for fy8-12, computed from their data (python -I lesson-answers.py); the
exercises' answers are in answers.py.
Physics data (to verify against the sources named in lesson.md):
- mean energy per ion pair in dry air W ≈ 34 eV (ICRU Report 31: 33,97 eV for electrons); ionisation energy of water
  12,6 eV (NIST Chemistry WebBook, 12,62 eV);
- Am-241 alpha 5,49 MeV (NNDC NuDat 3: 5,486 MeV), its range in air from Geiger's rule R = 0,318 cm · (E / MeV)^1,5;
- Cs-137 gamma 662 keV; narrow-beam half-value thicknesses d½ = ln 2 / μ from NIST XCOM mass attenuation coefficients
  (log-log interpolation between 0,6 and 0,8 MeV, total with coherent scattering), densities Pb 11,35, Fe 7,874,
  Al 2,699, concrete 2,30, water 1,00 g/cm³.
The simulation's model values (koe 1–3) come from the same seeded generator as assets/sims/fy8/fy8-12/sim.js
(mulberry32; seed 100003 · k + 1009 · (4 · source + material) + 31 · n + 24, k the measurement's number at one setting;
6000 time slots in a 10 s count, each slot a source hit with probability 0,1 · T and a background hit with 4 / 6000).
Prints {id: number} as JSON on the last line."""
import json, math

LN2 = math.log(2)
h, c, e = 6.626e-34, 2.998e8, 1.602e-19
a = {}

# ---------------------------------------------------------------- the simulation's model (same as sim.js)
M = 0xFFFFFFFF
def _i32(x):
    x &= M
    return x - 0x100000000 if x >= 0x80000000 else x
def _imul(x, y): return _i32((x & M) * (y & M))
def rng(seed):
    """mulberry32 exactly as sim.js: uniform numbers in (0, 1)."""
    st = [seed & M]
    def r():
        st[0] = (st[0] + 0x6D2B79F5) & M
        t = _imul(st[0] ^ (st[0] >> 15), st[0] | 1) & M
        t = _i32(t ^ (t + _imul(t ^ (t >> 7), t | 61))) & M
        return (((t ^ (t >> 14)) & M) + 0.5) / 4294967297
    return r

SOURCES = ["tausta", "alfa", "beeta", "gamma"]
MATERIALS = ["paperi", "alumiini", "lyijy"]
PLATE = {"paperi": 0.1, "alumiini": 1.0, "lyijy": 1.0}            # mm per sheet or plate
RHO = {"paperi": 0.80, "alumiini": 2.70, "lyijy": 11.35}         # g/cm³
HVL = {"paperi": 100.0, "alumiini": 34.0, "lyijy": 5.5}           # mm, Cs-137 662 keV, narrow beam
MU_BETA, R_BETA = 6.6, 1.1                                       # cm²/g and the maximum range g/cm² (E_max 2,28 MeV)
S0, B0, SLOTS = 600, 4, 6000                                     # mean counts in 10 s: source without absorber, background

def trans(src, mat, n):
    """The model's fraction of the source's radiation that reaches the tube through n sheets or plates."""
    if src == "tausta": return 0.0
    if n == 0: return 1.0
    d = n * PLATE[mat]                                           # mm
    if src == "alfa": return 0.0                                 # range in paper about 0,05 mm < one sheet 0,1 mm
    if src == "beeta":
        x = RHO[mat] * d / 10                                    # g/cm²
        return 0.0 if x >= R_BETA else math.exp(-MU_BETA * x)
    return 0.5 ** (d / HVL[mat])                                 # gamma

def count(src, mat, n, k=1):
    """Pulses in one 10 s count, the k-th measurement at this setting (as sim.js)."""
    mi = MATERIALS.index(mat) if n > 0 else 0
    R = rng(100003 * k + 1009 * (4 * SOURCES.index(src) + mi) + 31 * n + 24)
    q, qb = S0 * trans(src, mat, n) / SLOTS, B0 / SLOTS
    N = 0
    for _ in range(SLOTS):
        if R() < q: N += 1
        if R() < qb: N += 1
    return N

# Koe 1: one sheet of paper (0,1 mm), the source varied
for s in SOURCES:
    a[f"koe1-{s}"] = count(s, "paperi", 1)
    a[f"koe1-mean-{s}"] = S0 * trans(s, "paperi", 1) + B0
# Koe 2: aluminium 5 mm, the source varied
for s in SOURCES:
    a[f"koe2-{s}"] = count(s, "alumiini", 5)
    a[f"koe2-mean-{s}"] = S0 * trans(s, "alumiini", 5) + B0
# without an absorber every source gives about 600 + 4
for s in SOURCES: a[f"free-{s}"] = count(s, "paperi", 0)              # tausta: 3
# Koe 3: gamma behind lead, n = 0, 5, 10, 15, 20 mm
for n in (0, 5, 10, 15, 20):
    a[f"koe3-{n}"] = count("gamma", "lyijy", n)
    a[f"koe3-mean-{n}"] = S0 * trans("gamma", "lyijy", n) + B0
a["koe3-net-0"] = a["koe3-0"] - B0                              # net counts: background 4 subtracted
a["koe3-net-5"] = a["koe3-5"] - B0
a["koe3-ratio-5"] = a["koe3-net-5"] / a["koe3-net-0"]           # about 0,53: 5 mm is a little less than d½
a["koe3-ratio-10"] = (a["koe3-10"] - B0) / a["koe3-net-0"]      # about 0,28: roughly a quarter
a["koe3-d-half-est"] = 10 * LN2 / math.log(a["koe3-net-0"] / (a["koe3-10"] - B0))   # d½ from 0 and 10 mm
# a second count at the same setting differs (k = 2)
a["koe3-5-k2"] = count("gamma", "lyijy", 5, 2)
# beta through aluminium plates 1–4 mm (sim-spec, howto)
for n in (1, 2, 3, 4): a[f"beta-al-{n}"] = S0 * trans("beeta", "alumiini", n)
a["beta-paper-20"] = trans("beeta", "paperi", 20)               # 2 mm of paper: 0,35 of the beta gets through

# ---------------------------------------------------------------- theory: ionisation (Ydinajatus)
W = 34.0                                                         # eV per ion pair in air
E_alpha = 5.49e6                                                 # eV, Am-241
R_alpha = 0.318 * 5.49 ** 1.5                                    # cm: 4,09 cm (Geiger's rule)
a["alpha-range-cm"] = R_alpha
a["alpha-ion-pairs"] = E_alpha / W                               # 1,61e5 ion pairs
a["alpha-pairs-per-mm"] = E_alpha / W / (R_alpha * 10)           # 3,9e3 per mm
E_vis_lo, E_vis_hi = h * c / 720e-9 / e, h * c / 380e-9 / e      # visible 1,7–3,3 eV (as Vetyatomin energiatasot ...)
a["vis-lo"], a["vis-hi"] = E_vis_lo, E_vis_hi
a["water-ion-lambda-nm"] = h * c / (12.6 * e) * 1e9              # 98,4 nm: the longest ionising wavelength for water
a["uvc-254-eV"] = h * c / 254e-9 / e                             # 4,88 eV: UV-C is not ionising (but harms DNA)
a["xray-60keV-pairs"] = 60e3 / W                                 # 1,8e3 ion pairs from one 60 keV X-ray photon
a["gamma-662-pairs"] = 662e3 / W                                 # 1,9e4 ion pairs from one 662 keV photon
a["wifi-eV"] = h * 2.45e9 / e                                    # 1,0e-5 eV

# ---------------------------------------------------------------- Kaava: half-value thickness (NIST XCOM, 662 keV)
def mu_rho(m06, m08, E=0.662):
    """log-log interpolation of μ/ρ (cm²/g) between 0,6 and 0,8 MeV."""
    f = math.log(E / 0.6) / math.log(0.8 / 0.6)
    return math.exp(math.log(m06) + f * (math.log(m08) - math.log(m06)))
XCOM = {"lyijy": (0.1248, 0.08870, 11.35), "rauta": (0.07703, 0.06699, 7.874), "alumiini": (0.07802, 0.06841, 2.699),
        "betoni": (0.08055, 0.07074, 2.30), "vesi": (0.08956, 0.07865, 1.00)}
for k, (m06, m08, rho) in XCOM.items():
    a[f"hvl-{k}-mm"] = 10 * LN2 / (mu_rho(m06, m08) * rho)      # Pb 5,5; Fe 12; Al 34; concrete 39; water 81 mm
# Kaava figure: I/I0 at 1, 2, 3 half-value thicknesses of lead and lead vs aluminium at 25 mm
for k in (1, 2, 3): a[f"kaava-half-{k}"] = 0.5 ** k
a["kaava-pb-25"] = 0.5 ** (25 / 5.5)                            # 0,043
a["kaava-al-25"] = 0.5 ** (25 / 34)                             # 0,60

# ---------------------------------------------------------------- Esimerkki: lead for 5,0 % (Cs-137, d½ 5,5 mm)
a["ex-halvings"] = math.log(1 / 0.050) / LN2                    # 4,32 half-value thicknesses
a["ex-d"] = 5.5 * math.log(1 / 0.050) / LN2                     # 23,77 mm -> 24 mm
a["ex-check-4"] = 0.5 ** 4                                      # 6,25 % at 22 mm
a["ex-check-5"] = 0.5 ** 5                                      # 3,1 % at 27,5 mm

# ---------------------------------------------------------------- Ennuste 2, Etsi virhe: two half-value layers
a["two-layers"] = 0.5 ** 2                                      # a quarter passes, not zero

# ---------------------------------------------------------------- Sovella, siirto: lead apron 0,50 mm, d½ 0,12 mm
a["siirto"] = 100 * 0.5 ** (0.50 / 0.12)                        # 5,57 % passes
a["siirto-halvings"] = 0.50 / 0.12                              # 4,17
a["siirto-mistake-inv"] = 100 * 0.5 ** (0.12 / 0.50)            # 84,7 %: exponent upside down
a["siirto-mistake-absorbed"] = 100 - a["siirto"]                # 94,4 %: the absorbed share
a["siirto-mistake-div"] = 100 / (2 * 0.50 / 0.12)               # 12,0 %: halved by the number of layers
a["siirto-pb-hvl-60keV-mm"] = 10 * LN2 / (5.021 * 11.35)        # XCOM Pb 60 keV 5,021 cm²/g: 0,122 mm

# ---------------------------------------------------------------- Tarkista 2: graph of an unknown material, d½ 12 mm
CHK_R0, CHK_D = 800, 12.0                                       # pulses per minute without the plate, d½ (mm)
a["check2"] = CHK_D
a["check2-quarter"] = 2 * CHK_D                                 # 200 pulses/min at 24 mm

# ---------------------------------------------------------------- exit ticket
a["exit-vis"] = h * c / 500e-9 / e                              # 2,5 eV green light: not ionising

if __name__ == "__main__":
    print(json.dumps({k: (round(v, 6) if isinstance(v, float) and abs(v) > 1e-3 else v) for k, v in a.items()}))
