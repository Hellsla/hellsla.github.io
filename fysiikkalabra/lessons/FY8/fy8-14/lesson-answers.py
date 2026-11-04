"""Numbers of the lesson text and inquiry.json for fy8-14, computed from their data (python -I lesson-answers.py); the
exercises' answers are in answers.py.
Attenuation through layers I = I0 (1/2)^(d1/d½1) (1/2)^(d2/d½2) (puoliintumispaksuus d½, written d_{1/2} as in the
chapter Ionisoiva säteily ja elimistö); decay law A = A0 (1/2)^(t/T½) (chapter Hajoamislaki ja puoliintumisaika);
annihilation photon E = m_e c^2, E = hf (chapters Valosähköinen ilmiö ja fotoni, Massavaje ja ytimen sidosenergia).
Data, from knowledge (the network was closed when this was written, 2026-11-04; values as published):
- NIST XCOM / Hubbell & Seltzer mass attenuation coefficients μ/ρ (cm²/g): water 30 keV 0,3756, 60 keV 0,2059,
  100 keV 0,1707; cortical bone (ICRU-44, ρ = 1,92 g/cm³) 1,331, 0,3148, 0,1855; lead (11,35 g/cm³) 100 keV 5,549,
  150 keV 2,014, 500 keV 0,1614, 600 keV 0,1248; iron (7,874 g/cm³) 60 keV 1,205. Narrow beam, d½ = ln 2 / μ.
- Half-lives: Tc-99m 6,01 h (140 keV gamma), F-18 110 min, Am-241 432,2 a, C-14 5700 a (as in the chapter
  Hajoamislaki ja puoliintumisaika).
- Effective dose coefficients ICRP 128 (2015), adult: F-18 FDG 0,019 mSv/MBq, Tc-99m MDP (bone scan) 0,0049 mSv/MBq.
  Typical effective doses (STUK, Säteily terveydenhuollossa; rounded orders of magnitude): dental X-ray under
  0,01 mSv, chest X-ray about 0,02 mSv, head CT about 2 mSv, body CT 5–10 mSv.
- Radiotherapy: 2 Gy per fraction, 60 Gy in 30 fractions (a usual curative scheme); sterilisation dose 25 kGy
  (ISO 11137 reference dose); smoke detector Am-241 about 37 kBq.
- Constants as in FY8: h = 6,626e-34 J s, c = 2,998e8 m/s, e = 1,602e-19 C, m_e = 9,109e-31 kg.
The simulation's model (assets/sims/fy8/fy8-14/sim.js) is repeated below (pet_events, pet_stats): the same seeded
generator, so the model values of koe-1 here are those the sim shows.
Prints {id: number} as JSON on the last line."""
import json, math

a = {}
LN2 = math.log(2)
h, c, e, me = 6.626e-34, 2.998e8, 1.602e-19, 9.109e-31

# ---------------------------------------------------------------- Ydinajatus: the X-ray tube
a["tube-80kV-Emax-keV"] = 80e3                               # E_max = eU = 80 keV for U = 80 kV
a["tube-80kV-Emax-J-e14"] = e * 80e3 * 1e14                # 1,28e-14 J

# ---------------------------------------------------------------- Interpret: d½ in soft tissue (water) and bone
WATER = {30: 0.3756, 60: 0.2059, 100: 0.1707}
BONE = {30: 1.331, 60: 0.3148, 100: 0.1855}
RHO_BONE = 1.92
for E in (30, 60, 100):
    a[f"hvl-water-{E}-cm"] = LN2 / WATER[E]                    # 1,85; 3,37; 4,06 cm
    a[f"hvl-bone-{E}-cm"] = LN2 / (BONE[E] * RHO_BONE)         # 0,271; 1,147; 1,946 cm
    a[f"hvl-ratio-{E}"] = a[f"hvl-water-{E}-cm"] / a[f"hvl-bone-{E}-cm"]   # 6,8; 2,9; 2,1
    # 20 cm of soft tissue (a body): share through
    a[f"body20-{E}"] = 0.5 ** (20 / a[f"hvl-water-{E}-cm"])     # 30 keV 5,6e-4; 60 keV 0,016; 100 keV 0,033

# ---------------------------------------------------------------- Esimerkki: ray A 8,0 cm tissue, ray B 5,0 cm + 3,0 cm bone
DT, DB = 3.4, 1.1                                            # cm at about 60 keV (rounded from 3,37 and 1,15)
IA = 0.5 ** (8.0 / DT)                                       # 0,1957
IB = 0.5 ** (5.0 / DT) * 0.5 ** (3.0 / DB)                   # 0,3608 · 0,1510 = 0,05449
a["ex-IA"] = IA
a["ex-IB-tissue"] = 0.5 ** (5.0 / DT)
a["ex-IB-bone"] = 0.5 ** (3.0 / DB)
a["ex-IB"] = IB
a["ex-ratio"] = IA / IB                                      # 3,59 -> 3,6 (Järkevyys: 0,1957 : 0,05449)
a["ex-nA"] = 8.0 / DT                                        # 2,353 half-value thicknesses on ray A
a["ex-nB-tissue"] = 5.0 / DT                                 # 1,471
a["ex-nB-bone"] = 3.0 / DB                                   # 2,727
a["ex-nB"] = 5.0 / DT + 3.0 / DB                             # 4,198
a["ex-n-diff"] = a["ex-nB"] - a["ex-nA"]                     # 1,845
a["ex-ratio-n"] = 2 ** a["ex-n-diff"]                        # 2^1,845 = 3,59 (Sijoitus)
a["ex-check-exp"] = 3.0 / DB - 3.0 / DT                      # the bone path has 2,73 - 0,88 = 1,85 more halvings: 2^1,85 = 3,6
a["ex-check-ratio"] = 2 ** a["ex-check-exp"]

# ---------------------------------------------------------------- Kaava: annihilation photons
E511 = me * c ** 2                                           # 8,187e-14 J
a["E511-J-e14"] = E511 * 1e14                               # 8,187 (· 10^-14 J)
a["E511-keV"] = E511 / e / 1e3                               # 511,07 keV
a["f511-e20"] = E511 / h / 1e20                              # 1,2356e20 Hz (Tarkista 2)
a["f511-check-e20"] = 511e3 * e / h / 1e20                   # estimate from 511 keV
a["visible-max-ratio"] = 511e3 / 3.3                         # 1,5e5 times the most energetic visible photon

# ---------------------------------------------------------------- Ydinajatus: nuclear medicine
a["tc-left-24h-%"] = 100 * 0.5 ** (24 / 6.01)                # 6,3 % of the activity left after a day
a["f18-left-110-%"] = 50.0
a["fdg-dose-mSv"] = 300 * 0.019                              # 5,7 mSv -> about 6 mSv
a["mdp-dose-mSv"] = 600 * 0.0049                             # 2,94 mSv -> about 3 mSv
a["hvl-pb-140-mm"] = 10 * LN2 / (5.549 * (0.140 / 0.100) ** (math.log(2.014 / 5.549) / math.log(1.5)) * 11.35)   # 0,255 mm
a["hvl-pb-511-mm"] = 10 * LN2 / (0.1614 * (0.511 / 0.500) ** (math.log(0.1248 / 0.1614) / math.log(1.2)) * 11.35)  # 3,90 mm

# ---------------------------------------------------------------- Ydinajatus: radiotherapy and technology
a["rt-total-Gy"] = 30 * 2.0                                  # 60 Gy
a["rt-beam-Gy"] = 2.0 / 5                                    # 0,40 Gy per beam at the tumour with five beams
a["steril-dT-K"] = 25e3 / 4190                               # 25 kGy would warm water by only 6,0 K
a["am241-10a-%"] = 100 * 0.5 ** (10 / 432.2)                 # 98,4 % left after 10 a
a["c14-50ka-%"] = 100 * 0.5 ** (50000 / 5700)                # 0,23 % left after 50 000 a

# ---------------------------------------------------------------- Ennuste 3: radiotherapy, five beams
a["ennuste3-tumour"] = 5 * 0.40                              # 2,0 Gy at the tumour, 0,40 Gy where one beam passes

# ---------------------------------------------------------------- Siirto: FDG made 2 h 30 min before the injection
A_INJ, T_TR, T_HALF = 300.0, 150.0, 110.0                    # MBq, min, min
a["siirto"] = A_INJ * 2 ** (T_TR / T_HALF)                   # 772,0 MBq -> 770 MBq
a["siirto-m-linear"] = A_INJ * (1 + T_TR / T_HALF / 2)       # wrong: half lost per half-life taken linearly: 504,5
a["siirto-m-decay"] = A_INJ * 0.5 ** (T_TR / T_HALF)         # wrong: decayed forward instead of backward: 116,5
a["siirto-m-h"] = A_INJ * 2 ** (2.5 / T_HALF)                # wrong: 2,5 h used as 2,5 min: 304,8
a["siirto-m-double"] = A_INJ * 2                             # wrong: one half-life only: 600


# ---------------------------------------------------------------- inquiry: interpret, virhe, checks
a["int-ratio-30-rounded"] = 1.8 / 0.27                         # 6,7 -> "about 7"
a["int-ratio-100-rounded"] = 4.1 / 1.9                         # 2,2 -> "about 2"
a["virhe-product"] = 0.36 * 0.15                             # 0,054: through both layers
a["virhe-sum"] = 0.36 + 0.15                                 # 0,51: the wrong sum
a["virhe-quot"] = 0.36 / 0.15                                # 2,4: the wrong quotient
a["light-ns-cm"] = c * 1e-9 * 100                            # light travels 30 cm in a nanosecond
a["tof-0.3ns-cm"] = c * 0.3e-9 / 2 * 100                     # time-of-flight PET, Δt 0,3 ns: Δx = cΔt/2 = 4,5 cm ("muutama cm")
a["chk2-E-J-e14"] = 511e3 * e * 1e14                         # 8,186e-14 J
a["chk2"] = 511e3 * e / h / 1e20                             # 1,2355e20 Hz -> 1,24e20 Hz
a["chk2-m-k"] = 511 * e / h / 1e17                           # 1,24e17: the k left out
a["chk2-m-eV"] = 511e3 / h / 1e38                            # 7,71e38: eV not converted
a["chk2-ratio"] = 511e3 / 2.0                                # 2,6e5 times a 2 eV visible photon
a["chk2-est"] = 5e14 * 2.6e5 / 1e20                          # 1,3e20 Hz estimate
a["siirto-factor"] = 2 ** (150 / 110)                        # 2,5733
a["siirto-after-1"] = a["siirto"] / 2                        # 386 MBq after one half-life
a["chk3-hvl-ratio"] = 3.9 / 0.26                             # 15 times thicker lead


# ---------------------------------------------------------------- the simulation's model (same as sim.js)
RR, AB, BB, G, HALF, SIG = 34.0, 16.0, 10.5, 41, 0.6, 0.8
TUM = {1: [(5.0, -3.0)], 2: [(5.0, -3.0), (-7.0, 2.0)], 0: []}   # cm, x right, y down as on the screen
PT = {1: 0.25, 2: 0.4, 0: 0.0}


def pet_events(case, n):
    seed = [73 + 1000 * case]

    def rand():
        seed[0] = (seed[0] * 16807) % 2147483647
        return (seed[0] - 1) / 2147483646
    out, T = [], TUM[case]
    for _ in range(n):
        if T and rand() < PT[case]:
            t = T[int(rand() * len(T)) % len(T)]
            u1, u2 = max(rand(), 1e-12), rand()
            r = SIG * math.sqrt(-2 * math.log(u1))
            x, y = t[0] + r * math.cos(2 * math.pi * u2), t[1] + r * math.sin(2 * math.pi * u2)
        else:
            while True:
                x, y = (2 * rand() - 1) * AB, (2 * rand() - 1) * BB
                if (x / AB) ** 2 + (y / BB) ** 2 <= 1: break
        th = rand() * math.pi
        rand()                                               # which photon a singles detector records (picture only)
        out.append((x, y, math.cos(th), math.sin(th)))
    return out


def pet_stats(case, n):
    """brightest pixel (x, y up) in cm, its distance from the nearest tumour (cm), share of lines within 1 cm (%)."""
    ev = pet_events(case, n)
    img = [0] * (G * G)
    for (x, y, ux, uy) in ev:
        for j in range(G):
            for i in range(G):
                if abs((-20 + i - x) * uy - (-20 + j - y) * ux) < HALF: img[j * G + i] += 1
    k = img.index(max(img)); xs, ys = -20 + k % G, -20 + k // G
    T = TUM[case]
    err = min(math.hypot(xs - p, ys - q) for p, q in T) if T else -1
    nk = sum(1 for (x, y, ux, uy) in ev if T and abs((T[0][0] - x) * uy - (T[0][1] - y) * ux) < 1.0)
    return xs, -ys, err, 100 * nk / n


# Seed 73 was chosen as a typical run: over seeds 1-100 the median distance is 4,2 cm at N = 10, 1,4 cm at 20 and
# 1,0 cm at 50, 86 % of runs are within 1,5 cm at N = 50 and all at N = 150 ("kymmeniä koinsidensseja").
for N in (10, 20, 50, 200, 1000):                            # koe-1: one tumour at (5, 3) cm
    xs, ys, err, share = pet_stats(1, N)
    a[f"koe1-N{N}-x"], a[f"koe1-N{N}-y"], a[f"koe1-N{N}-virhe"], a[f"koe1-N{N}-osuus"] = xs, ys, err, share
# 10: (14, 19) 18,4 cm, 10 %; 20: (5, 7) 4,0 cm, 5 %; 50: (6, 4) 1,4 cm, 26 %; 200: (5, 3) 0 cm, 25,5 %; 1000: (5, 3) 0 cm, 27,8 %
xs, ys, err, share = pet_stats(2, 1000)
a["koe-2tum-N1000-x"], a["koe-2tum-N1000-y"] = xs, ys        # (5, 3): the first tumour is the brighter one
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
