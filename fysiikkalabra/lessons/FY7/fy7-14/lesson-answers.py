"""Numbers of the lesson text and inquiry.json for fy7-14, computed from their data (python -I lesson-answers.py); the
exercises' answers are in answers.py. Thin film at normal incidence: path difference 2nd (n the film's refractive index,
d its thickness); a half-wavelength shift at a reflection from a medium of larger refractive index. One shift (soap film
in air, oil on water): constructive 2nd = (k + 1/2)λ, destructive 2nd = kλ; none or two (MgF2 coating on glass):
constructive 2nd = kλ, destructive 2nd = (k + 1/2)λ. Reflectance of the simulation: the exact single-layer formula
R = |(r1 + r2 e^(-iδ)) / (1 + r1 r2 e^(-iδ))|², r = (n_a - n_b) / (n_a + n_b), δ = 2π · 2nd / λ. Prints {id: number}."""
import json, cmath
from math import pi, sqrt


def R(d, lam, nf, ns):
    """Share of the light reflected by a film of index nf and thickness d (nm) on a medium ns, light from air."""
    r1, r2 = (1 - nf) / (1 + nf), (nf - ns) / (nf + ns)
    e = cmath.exp(-1j * 4 * pi * nf * d / lam)
    return abs((r1 + r2 * e) / (1 + r1 * r2 * e)) ** 2


def mgf2(l):
    """MgF2 ordinary index, Dodge (Applied Optics 23, 1984) Sellmeier formula, l in µm."""
    l2 = l * l
    return sqrt(1 + 0.48755108 * l2 / (l2 - 0.04338408 ** 2) + 0.39875031 * l2 / (l2 - 0.09461442 ** 2)
                + 2.3120353 * l2 / (l2 - 23.793604 ** 2))


def bk7(l):
    """SCHOTT N-BK7 Sellmeier formula (datasheet), l in µm."""
    l2 = l * l
    return sqrt(1 + 1.03961212 * l2 / (l2 - 0.00600069867) + 0.231792344 * l2 / (l2 - 0.0200179144)
                + 1.01046945 * l2 / (l2 - 103.560653))


a = {}
NS, NC, NG = 1.33, 1.38, 1.52                        # soap water, MgF2, ordinary (crown) glass
# data sources quoted in the text
a["mgf2-550"] = mgf2(0.550)                          # 1,3785 -> 1,38 (Dodge 1984)
a["bk7-550"] = bk7(0.550)                            # 1,5185 -> 1,52 (SCHOTT N-BK7)
# Ydinajatus: wavelength in the film, λ_n = λ : n
a["lam-in-soap"] = 550 / NS                          # 413,5 nm
# Ydinajatus: the thinnest soap film that reflects 550 nm strongly, 2nd = λ/2
a["soap-quarter"] = 550 / (4 * NS)                   # 103,38 nm
# bare glass and the quarter-wave MgF2 coating at 550 nm
a["R-bare"] = R(0, 550, NC, NG) * 100                # 4,258 % -> noin 4 %
a["R-coated"] = R(550 / (4 * NC), 550, NC, NG) * 100   # 1,260 % -> noin 1,3 %
a["coat-quarter"] = 550 / (4 * NC)                   # 99,64 nm
a["sqrt-glass"] = sqrt(NG)                           # 1,233: the ideal coating index
a["R-soap-max"] = R(550 / (4 * NS), 550, NS, 1.0) * 100   # 7,71 %: the soap film's strongest reflection
# thick film: 5 µm soap film, the number of constructive wavelengths in 400–700 nm
opd5 = 2 * NS * 5000
a["thick-count"] = sum(1 for k in range(200) if 400 <= opd5 / (k + 0.5) <= 700)   # 14
# worked example: soap bubble wall d = 380 nm
opd = 2 * NS * 380
a["ex-opd"] = opd                                    # 1010,8 nm
for k in range(4):
    a[f"ex-con-{k}"] = opd / (k + 0.5)               # 2021,6; 673,9; 404,3; 288,8 nm
for k in (1, 2, 3):
    a[f"ex-des-{k}"] = opd / k                       # 1010,8; 505,4; 336,9 nm
# hook / figure: the colour bands; koe-3 at d = 200 nm, soap film: destructive 2nd = λ
a["koe3-opd"] = 2 * NS * 200                         # 532 nm cancelled
for lam in (400, 450, 500, 532, 550, 600, 650, 700):
    a[f"koe3-R-{lam}"] = R(200, lam, NS, 1.0) * 100  # 400: 5,8 %, 532: 0, 700: 3,8 %
# koe-1: soap film, λ = 550 nm, d = 0, 50, 103, 150, 207
for d in (0, 50, 100, 103, 150, 200, 207, 310):
    a[f"koe1-R-{d}"] = R(d, 550, NS, 1.0) * 100
    a[f"koe1-ratio-{d}"] = 2 * NS * d / 550
a["koe1-dark"] = 550 / (2 * NS)                      # 206,8 nm: the next dark thickness (2nd = λ)
# koe-2: MgF2 on glass, λ = 550 nm
for d in (0, 50, 100, 150, 199):
    a[f"koe2-R-{d}"] = R(d, 550, NC, NG) * 100
a["koe2-half"] = 550 / (2 * NC)                      # 199,3 nm: the half-wave layer reflects like bare glass
# ennuste-ohut feedback: d = 20 nm soap film at 550 nm
a["thin-20"] = R(20, 550, NS, 1.0) * 100             # 0,74 %
# virhe: the student's wrong thickness λ / (2n) for the coating
a["virhe-wrong"] = 550 / (2 * NC)                    # 199,3 nm
a["virhe-right"] = 550 / (4 * NC)                    # 99,64 nm
# siirto: oil film (n = 1,47) on water, 600 nm missing, one shift -> 2nd = kλ, k = 1
a["siirto"] = 600 / (2 * 1.47)                       # 204,08 nm
a["siirto-no-n"] = 600 / 2                           # mistake: n forgotten, 300 nm
a["siirto-quarter"] = 600 / (4 * 1.47)               # mistake: constructive condition, 102,04 nm
a["siirto-lam-n"] = 600 / 1.47                       # mistake: 2nd = 2λ, 408,16 nm
a["siirto-soap"] = 600 / (2 * NS)                    # Järkevyys: the soap film that cancels 600 nm, 225,6 nm
# tarkistus-2: soap film d = 250 nm, strongest visible reflection 2nd = (k + 1/2)λ
opd250 = 2 * NS * 250
a["check-opd"] = opd250                              # 665 nm
a["check-lam"] = opd250 / 1.5                        # k = 1: 443,3 nm (k = 0: 1330 nm, infrared)
a["check-k0"] = opd250 / 0.5                         # 1330 nm
a["check-k2"] = opd250 / 2.5                         # 266 nm, ultraviolet
a["koe1-no-n"] = 550 / 4                             # koe-1 mistake: n forgotten, 137,5 nm
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
