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
# Level 2: a rearrangement, a conversion or two steps
a["fy7-14-L2-01"] = 2 * 1.33 * 240 / 1              # soap film, one shift: destructive 2nd = kλ, k = 1: 638,4 nm (k = 2: 319 nm, UV)
a["fy7-14-L2-02"] = 4 * 1.38 * 110e-9 * 1e9         # coating, two shifts: destructive 2nd = λ/2, λ = 4nd = 607,2 nm
a["fy7-14-L2-03"] = 3 * 520 / (4 * 1.38)            # the next coating thickness: 2nd = (1 + 1/2)λ, d = 3λ / (4n) = 282,6 nm
a["fy7-14-L2-04"] = 550 / (4 * 2.30)                # high-index layer on glass (2,30 > 1,52): one shift, constructive 2nd = λ/2: 59,78 nm
# Level 3: reasoning, two ideas or an unfamiliar context
a["fy7-14-L3-01"] = 2 * 589 / (2 * 1.33)            # second dark band below the black top (k = 2; black top k = 0, first band k = 1): 2nd = 2λ, d = λ / n = 442,9 nm
a["fy7-14-L3-02"] = (1 - 0.013) ** 8 * 100          # 8 coated surfaces, each reflects 1,3 %: transmitted 90,06 %
# check in its solution: 8 bare surfaces reflecting 4,258 % each (lesson-answers R-bare) pass (1 - 0.04258) ** 8 = 70,6 %
kk = (1.5 * 450 - 0.5 * 630) / (630 - 450)           # consecutive maxima (k + 1/2)·630 = (k + 3/2)·450 -> k = 2
a["fy7-14-L3-03"] = (kk + 0.5) * 630 / (2 * 1.33)    # 2nd = 2,5 · 630 nm = 1575 nm, d = 592,1 nm
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
