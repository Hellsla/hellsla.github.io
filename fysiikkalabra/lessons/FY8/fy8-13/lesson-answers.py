"""Numbers of the lesson text and inquiry.json for fy8-13, computed from their data (python -I lesson-answers.py); the
exercises' answers are in answers.py.
Absorbed dose D = E / m (Gy = J/kg); equivalent dose H_T = w_R D_T; effective dose H_E = sum of w_T H_T (Sv);
dose H = Hdot t; point source Hdot2 = Hdot1 (r1 / r2)^2; shield Hdot = Hdot0 (1/2)^(x / d½).
Weighting factors ICRP 103 (2007): w_R photons and electrons 1, alpha 20; w_T lungs 0,12, thyroid 0,04.
Finnish figures (STUK, estimate published 2023, rounded): average effective dose 5,9 mSv/a: radon 4,1, health care 0,6,
ground and building materials 0,5, radioactive substances in the body 0,4, cosmic 0,3; other sources under 0,1.
The simulation's model (assets/sims/fy8/fy8-13/sim.js): a gamma point source with 40,0 µSv/h at 1,0 m, lead half-value
layer 6,0 mm; the dosimeter's window catches the share A / (4 pi r^2) of the photons.
Prints {id: number} as JSON on the last line."""
import json, math

a = {}
# ---------------------------------------------------------------- the simulation's model (same as sim.js)
H1, D_HALF = 40.0, 6.0                                   # µSv/h at 1,0 m; mm of lead


def hdot(r, x):
    """dose rate in µSv/h at distance r (m) behind x mm of lead: the window's share A/(4 pi r^2) of the photons,
    calibrated to H1 at 1 m, times the share (1/2)^(x/d½) that gets through the lead."""
    share = 1 / (4 * math.pi * r ** 2)                   # per unit window area
    return H1 * share / (1 / (4 * math.pi)) * 0.5 ** (x / D_HALF)


# koe 1: x = 0, r = 1, 2, 3, 4 m -> 40,0; 10,0; 4,44; 2,50 µSv/h
for r in (1.0, 1.5, 2.0, 3.0, 4.0):
    a[f"koe1-r{r:g}"] = hdot(r, 0)
# koe 2: r = 1,0 m, x = 0, 6, 12, 18, 24 mm -> 40,0; 20,0; 10,0; 5,00; 2,50 µSv/h; 3 mm -> 28,3
for x in (0, 3, 6, 12, 18, 24, 30):
    a[f"koe2-x{x}"] = hdot(1.0, x)
# the sim's dose at r = 2,0 m for 30 min: 10,0 µSv/h · 0,5 h = 5,00 µSv
a["sim-dose-2m-30min"] = hdot(2.0, 0) * 30 / 60

# ---------------------------------------------------------------- Ydinajatus: the Finnish average dose (STUK 2023)
SOURCES = {"radon": 4.1, "terveydenhuolto": 0.6, "maaperä": 0.5, "elimistö": 0.4, "avaruus": 0.3}
a["total"] = sum(SOURCES.values())                         # 5,9 mSv
a["radon-share-%"] = 100 * SOURCES["radon"] / a["total"]   # 69,5 % -> about 70 %, "yli kaksi kolmasosaa"
a["natural"] = a["total"] - SOURCES["terveydenhuolto"]     # 5,3 mSv natural (other sources under 0,1 left out)
a["natural-share-%"] = 100 * a["natural"] / a["total"]     # 89,8 % -> about 90 %
# 1 Gy in water: temperature rise ΔT = D / c = 1 J/kg / 4190 J/(kg K) = 0,000239 K
a["1Gy-heating-K"] = 1 / 4190
# sum of the tissue weighting factors of ICRP 103 is 1
WT = [0.12] * 5 + [0.08] + [0.04] * 4 + [0.01] * 4 + [0.12]
a["wT-sum"] = sum(WT)

# ---------------------------------------------------------------- Esimerkki: radon decay products in the lungs
E, m = 2.0e-3, 1.2                                         # J absorbed in a year, kg of lungs
a["ex-D-mGy"] = E / m * 1e3                                # 1,667 mGy
a["ex-H-mSv"] = 20 * a["ex-D-mGy"]                         # 33,33 mSv
a["ex-HE-mSv"] = 0.12 * a["ex-H-mSv"]                      # 4,000 mSv -> 4,0 mSv
a["ex-check-HE"] = 0.1 * 20 * 2                            # estimate 0,1 · 20 · 2 mGy = 4 mSv

# ---------------------------------------------------------------- Ennusteet (sim model values)
a["ennuste1-right"] = hdot(2.0, 0)                         # 10,0 µSv/h at 2 m
a["ennuste1-linear"] = 40.0 / 2                            # 20 µSv/h (wrong: halving)
a["ennuste2-right"] = hdot(1.0, 12)                        # 10,0 µSv/h behind 12 mm
a["ennuste2-half"] = 40.0 / 2                              # 20 (wrong: only the first layer works)

# ---------------------------------------------------------------- Etsi virhe: alpha 0,50 mGy in the lungs
a["virhe-right-mSv"] = 0.12 * 20 * 0.50                    # 1,2 mSv
a["virhe-H-lung"] = 20 * 0.50                              # 10 mSv equivalent dose of the lungs
a["virhe-wrong-only-wT"] = 0.12 * 0.50                     # 0,06 mSv (w_R forgotten)

# ---------------------------------------------------------------- Siirto: 1,80 mSv/h at 1,0 m; 3,0 m, 12 mm lead, 15 min
Hs = 1800 * (1.0 / 3.0) ** 2 * 0.5 ** (12 / 6.0)           # 50,0 µSv/h
a["siirto-hdot"] = Hs
a["siirto"] = Hs * 15 / 60                                 # 12,5 µSv
a["siirto-m-linear"] = 1800 / 3 * 0.25 * 15 / 60           # 37,5: distance taken linearly
a["siirto-m-noshield"] = 1800 / 9 * 15 / 60                # 50,0: lead left out
a["siirto-m-min"] = Hs * 15                                # 750: minutes not converted to hours
a["siirto-m-shield-zero"] = 0                              # (12 mm = "two halves" -> nothing; not a listed value)
a["siirto-m-shield-half"] = 1800 / 9 / 2 * 15 / 60         # 25,0: only one halving

# ---------------------------------------------------------------- Tarkista 2: concrete curve, 80 µSv/h, d½ = 5,0 cm
CHK_H0, CHK_D = 80.0, 5.0
a["chk-half"] = CHK_H0 / 2                                 # 40 µSv/h read at 5,0 cm
a["chk-quarter-x"] = 2 * CHK_D                             # 20 µSv/h at 10 cm
a["chk-25cm"] = CHK_H0 * 0.5 ** (25 / CHK_D)               # 2,5 µSv/h at 25 cm
a["chk"] = CHK_D

# ---------------------------------------------------------------- Tarkista 3 and hook: radon
a["radon-300"] = 4.1 * 300 / 94                            # 13,1 mSv at the reference level, if dose ∝ concentration
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
