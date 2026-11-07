"""Every answer in exercises.json for fy7-14, computed from the task data (python -I answers.py).
Thin film at normal incidence: path difference 2nd; a half-wavelength shift at a reflection from a medium of larger
refractive index. One shift: constructive 2nd = (k + 1/2)λ, destructive 2nd = kλ; none or two: the other way round.
Wavelength in the film λ_n = λ / n. Prints {exercise id: number} as JSON on the last line."""
import json
from math import sqrt

a = {}
# Level 1: one formula, values given
a["fy7-14-L1-01"] = 2 * 1.33 * 420                  # path difference 2nd = 1117,2 nm
a["fy7-14-L1-02"] = 633 / 1.38                      # wavelength in MgF2: λ / n = 458,7 nm
a["fy7-14-L1-03"] = 500 / (4 * 1.38)                # quarter-wave coating d = λ / (4n) = 90,58 nm
a["fy7-14-L1-04"] = 600 / (4 * 1.33)                # thinnest strongly reflecting soap film d = λ / (4n) = 112,78 nm
a["fy7-14-L1-05"] = sqrt(1.60)                      # ideal coating index n_c = √n_glass = 1,265
# L1-06 is multiple choice (no number): only the air-film (top) reflection inverts
a["fy7-14-L1-07"] = 570 / (4 * 1.47)                # oil on water, one shift (1,00 < 1,47 > 1,33): constructive 2nd = λ/2, d = λ / (4n) = 96,94 nm
a["fy7-14-L1-08"] = 2 * 1.33 * 300 / 532            # path difference 2nd = 798 nm = 1,5 wavelengths of 532 nm
# YO-skill form (teacher 2026-11-05): L1-09 is an expression choice (no number); one shift, dark 2nd = kλ, k = 1: d = λ / (2n)
# Level 2: a rearrangement, a conversion or two steps
a["fy7-14-L2-01"] = 2 * 1.33 * 240 / 1              # soap film, one shift: destructive 2nd = kλ, k = 1: 638,4 nm (k = 2: 319 nm, UV)
a["fy7-14-L2-02"] = 4 * 1.38 * 110e-9 * 1e9         # coating, two shifts: destructive 2nd = λ/2, λ = 4nd = 607,2 nm
a["fy7-14-L2-03"] = 3 * 520 / (4 * 1.38)            # the next coating thickness: 2nd = (1 + 1/2)λ, d = 3λ / (4n) = 282,6 nm
a["fy7-14-L2-04"] = 550 / (4 * 2.30)                # high-index layer on glass (2,30 > 1,52): one shift, constructive 2nd = λ/2: 59,78 nm
a["fy7-14-L2-06"] = 2 * 1.33 * 250 / 1.5            # one shift: constructive 2nd = (k + 1/2)λ, k = 1: 665 / 1,5 = 443,3 nm (k = 0: 1330 nm, k = 2: 266 nm)
a["fy7-14-L2-07"] = 540 / (4 * 1.38)                # R minimal at 540 nm in the table, k = 0: d = λ / (4n) = 97,83 nm
# Level 3: reasoning, two ideas or an unfamiliar context
a["fy7-14-L3-01"] = 2 * 589 / (2 * 1.33)            # second dark band below the black top (k = 2; black top k = 0, first band k = 1): 2nd = 2λ, d = λ / n = 442,9 nm
a["fy7-14-L3-02"] = (1 - 0.013) ** 8 * 100          # 8 coated surfaces, each reflects 1,3 %: transmitted 90,06 %
# check in its solution: 8 bare surfaces reflecting 4,258 % each (lesson-answers R-bare) pass (1 - 0.04258) ** 8 = 70,6 %
kk = (1.5 * 450 - 0.5 * 630) / (630 - 450)           # consecutive maxima (k + 1/2)·630 = (k + 3/2)·450 -> k = 2
a["fy7-14-L3-03"] = (kk + 0.5) * 630 / (2 * 1.33)    # 2nd = 2,5 · 630 nm = 1575 nm, d = 592,1 nm

def fit(xs, ys):                                      # least-squares line y = a·x + b, returns (a, b)
    n = len(xs)
    mx, my = sum(xs) / n, sum(ys) / n
    sl = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs)
    return sl, my - sl * mx
a["fy7-14-L2-05"] = fit([90, 100, 110, 120, 130], [483, 534, 584, 640, 693])[0] / 4    # slope 5,26 = 4n (k = 0): n = 1,315
# oil film 1,00 / 1,47 / 1,33, d = 450 nm: one shift; 2nd = 1323 nm = 2,5·529,2 nm (only visible maximum); thinning: 2nd = 2·529,2 nm -> d = 360 nm
a["fy7-14-L3-04"] = 2 * (2 * 1.47 * 450 / 2.5) / (2 * 1.47)
# air wedge: one shift, dark 2d = kλ; fringe spacing = slope of x(k); foil D = (L / Δx)·λ/2 in µm
dx = fit([1, 2, 3, 4, 5, 6, 7, 8], [1.9, 3.9, 5.7, 7.7, 9.5, 11.5, 13.3, 15.2])[0]
a["fy7-14-L3-05"] = 80 / dx * 0.589 / 2
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
