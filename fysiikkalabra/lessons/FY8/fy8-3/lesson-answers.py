"""Numbers of the lesson text and inquiry.json for fy8-3, computed from their data (python -I lesson-answers.py); the
exercises' answers are in answers.py. Same model and symbols as there. Prints {id: number} as JSON on the last line."""
import json

h, c, e = 6.626e-34, 2.998e8, 1.602e-19      # J s, m/s, J per eV
E1 = 13.6
def En(n): return -E1 / n ** 2
def lam_nm(dE_eV): return h * c / (dE_eV * e) * 1e9

a = {}
# lesson.md: levels, worked example 3 -> 2, misconception, series table
for n in (2, 3, 4, 5, 6): a[f"E{n}"] = En(n)                 # -3,40; -1,511; -0,850; -0,544; -0,378 eV
a["ex-dE-eV"] = En(3) - En(2)                               # 1,8889 eV
a["ex-dE-J-e19"] = (En(3) - En(2)) * e / 1e-19              # 3,0260e-19 J
a["ex-lambda-nm"] = lam_nm(En(3) - En(2))                   # 656,47 nm -> 656 nm
a["mis-wrong-nm"] = lam_nm(-En(4))                          # |E_4| = 0,85 eV used: 1459 nm, "noin 1460 nm"
a["bal-4"] = lam_nm(En(4) - En(2))                          # 486,3 nm
a["bal-5"] = lam_nm(En(5) - En(2))                          # 434,2 nm
a["bal-6"] = lam_nm(En(6) - En(2))                          # 410,3 nm
a["bal-7"] = lam_nm(En(7) - En(2))                          # 397,1 nm: faint, at the violet edge
a["bal-8"] = lam_nm(En(8) - En(2))                          # 389,0 nm
a["lyman-limit"] = lam_nm(E1)                               # 91,18 nm
a["lyman-2"] = lam_nm(En(2) - En(1))                        # 121,6 nm
a["balmer-limit"] = lam_nm(E1 / 4)                          # 364,7 nm
a["paschen-limit"] = lam_nm(E1 / 9)                         # 820,6 nm
a["paschen-4"] = lam_nm(En(4) - En(3))                      # 1875,6 nm
a["visible-eV-700"] = h * c / 700e-9 / e                    # 1,77 eV, "1,7 eV"
a["visible-eV-380"] = h * c / 380e-9 / e                    # 3,26 eV, "3,3 eV"
a["abs-10-2"] = En(2) - En(1)                               # 10,2 eV absorbed, n = 1 -> 2
a["abs-12-09"] = En(3) - En(1)                              # 12,09 eV
a["abs-12-75"] = En(4) - En(1)                              # 12,75 eV
a["abs-14-Ek"] = 14.0 - E1                                  # 14,0 eV photon ionises, E_k = 0,4 eV
# inquiry: kertaus (656 nm and 410 nm photons)
a["kert-656"] = h * c / 656e-9 / e                          # 1,89 eV
a["kert-410"] = h * c / 410e-9 / e                          # 3,02 eV
# koe-1: n_a = 2, n_y = 3..6 (the model values the sim shows)
for m in (3, 4, 5, 6): a[f"koe1-{m}"] = lam_nm(En(m) - En(2))
# koe-2: n_a = 1, n_y = 2..6
for m in (2, 3, 4, 5, 6): a[f"koe2-{m}"] = lam_nm(En(m) - En(1))
# koe-3: atom at n = 1, photon 10,20 / 11,00 / 12,10 / 14,00 eV
a["koe3-1209"] = En(3) - En(1)                              # 12,089 eV: the slider value 12,10 eV (step 0,05 eV) hits it within 0,03 eV
a["koe3-14-Ek"] = 14.0 - E1                                 # 0,40 eV
# sim model box: from n = 1 every slider value 13,20 ... 13,55 eV (step 0,05) is within 0,03 eV of some E_m - E_1, m <= 30
a["crowd-all-hit"] = all(any(abs(En(m) - En(1) - f / 100) <= 0.03 for m in range(2, 31)) for f in range(1320, 1356, 5))
# siirto: a 656 nm photon ionises an atom at n = 4: hf = 1,8902 eV, E_k = hf + E_4 = 1,8902 eV - 0,850 eV = 1,04 eV
a["siirto-hf"] = h * c / 656e-9 / e                         # 1,8902 eV
a["siirto"] = h * c / 656e-9 / e + En(4)                    # 1,0402 eV -> 1,04 eV
a["siirto-m-hf"] = h * c / 656e-9 / e                       # mistake: the whole photon energy, 1,89 eV
a["siirto-m-plus"] = h * c / 656e-9 / e - En(4)             # mistake: 0,850 eV added, 2,74 eV
# virhe: 4 -> 2 with |E_4| = 0,85 eV gives 1459 nm; right 486 nm
a["virhe-wrong"] = lam_nm(-En(4))
a["virhe-right"] = lam_nm(En(4) - En(2))
# tarkistus-2: 5 -> 3: dE = 0,9671 eV, lambda = 1282 nm
a["tark2"] = lam_nm(En(5) - En(3))
a["tark2-m-E5"] = lam_nm(-En(5))                            # mistake: |E_5| = 0,544 eV -> 2279 nm
a["tark2-m-E3"] = lam_nm(-En(3))                            # mistake: |E_3| = 1,511 eV -> 820,6 nm
a["tark2-dE"] = En(5) - En(3)
# exit ticket: excite n = 1 -> 3: 12,1 eV
a["exit-1"] = En(3) - En(1)
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
