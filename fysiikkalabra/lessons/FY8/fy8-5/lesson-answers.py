"""Numbers of the lesson text and inquiry.json for fy8-5, computed from their data (python -I lesson-answers.py); the
exercises' answers are in answers.py. Hydrogen levels E_n = -13,6 eV / n^2 are given data (chapter Vetyatomin
energiatasot ja Bohrin malli); photon energy E = hf = hc / lambda; 1 eV = 1,602 * 10^-19 J substituted.
The orbitals of the simulation are hydrogen's 1s, 2s and 2p_z with the probability densities (lengths in units of the
Bohr radius a0 = 0,0529 nm, normalisation left out): 1s e^(-2r), 2s (2 - r)^2 e^(-r), 2p r^2 cos^2(theta) e^(-r).
An orbital's boundary at threshold p is the surface of constant density that encloses the probability p
(the region where the density is largest). Prints {id: number} as JSON."""
import json, math

h, c, e = 6.626e-34, 2.998e8, 1.602e-19                  # J s, m/s, C (J per eV)
a0 = 0.0529                                               # Bohr radius, nm
E = lambda n: -13.6 / n ** 2                              # hydrogen level, eV
a = {}

# --- shells: orbitals n^2, electrons 2 n^2 (Kaava table) ---
for n in (1, 2, 3, 4):
    a[f"orb-n{n}"] = n ** 2                               # 1, 4, 9, 16 orbitals
    a[f"el-n{n}"] = 2 * n ** 2                            # 2, 8, 18, 32 electrons
    a[f"E-n{n}"] = E(n)                                   # -13,6 / -3,40 / -1,51 / -0,85 eV

# --- worked example: hydrogen 3d -> 2p, the red line ---
a["ex-dE-eV"] = E(3) - E(2)                               # 1,8889 eV
a["ex-dE-J"] = a["ex-dE-eV"] * e                          # 3,0260e-19 J
a["ex-lambda-nm"] = h * c / a["ex-dE-J"] * 1e9            # 656,5 nm -> 656 nm
a["ex-check-3s"] = a["ex-lambda-nm"]                      # 3s -> 2p gives the same line in hydrogen

# --- 1s: radial probability P(r < R) = 1 - e^(-2x)(1 + 2x + 2x^2), x = R / a0 ---
P1s = lambda x: 1 - math.exp(-2 * x) * (1 + 2 * x + 2 * x * x)
def root(f, lo, hi):
    for _ in range(200):
        m = (lo + hi) / 2
        lo, hi = (m, hi) if f(m) < 0 else (lo, m)
    return (lo + hi) / 2
for p in (50, 90, 95):
    a[f"R1s-{p}"] = root(lambda x: P1s(x) - p / 100, 0, 30) * a0    # 0,0707 / 0,1408 / 0,1665 nm
a["R1s-90-a0"] = a["R1s-90"] / a0                         # 2,66 Bohr radii
a["peak-1s"] = a0                                         # radial probability 4 r^2 e^(-2r) is largest at r = a0
a["peak-2s"] = (3 + math.sqrt(5)) * a0                    # outer maximum of r^2 (2-r)^2 e^(-r): 0,277 nm
a["peak-2s-in"] = (3 - math.sqrt(5)) * a0                 # inner maximum 0,040 nm
a["node-2s"] = 2 * a0                                     # node sphere r = 2 a0 = 0,106 nm
a["peak-2p"] = 4 * a0                                     # r^4 e^(-r) is largest at r = 4 a0: 0,212 nm
dr = 0.002
a["node-2s-inside"] = sum(((k + 0.5) * dr) ** 2 * (2 - (k + 0.5) * dr) ** 2 * math.exp(-(k + 0.5) * dr) / 8 * dr for k in range(1000))  # 5,3 %

# --- 2s and 2p: density threshold enclosing 90 %, outer extent of the region (grid in r and mu = cos theta) ---
def threshold(dens, p, rmax=40.0, nr=2000, nmu=1):
    cells, d_r = [], rmax / nr
    for i in range(nr):
        r = (i + 0.5) * d_r
        for j in range(nmu):
            mu = -1 + (j + 0.5) * 2 / nmu
            d = dens(r, mu)
            cells.append((d, d * r * r * d_r * 2 / nmu))
    tot = sum(w for _, w in cells)
    cells.sort(reverse=True)
    acc = 0.0
    for d, w in cells:
        acc += w / tot
        if acc >= p:
            return d
d2s = lambda r, mu: (2 - r) ** 2 * math.exp(-r)
d2p = lambda r, mu: r * r * mu * mu * math.exp(-r)
t2s = threshold(d2s, 0.90, nr=8000)
a["R2s-90"] = root(lambda r: t2s - d2s(r, 1), 4, 40) * a0                 # outer edge along any direction
t2p = threshold(d2p, 0.90, nr=1500, nmu=300)
a["R2p-90"] = root(lambda r: t2p - d2p(r, 1), 2, 40) * a0                 # lobe tip on the z axis

# --- inquiry: predictions and checks ---
a["pred1-out-1000"] = 0.10 * 1000                         # 90 % boundary: about 100 of 1000 hits outside
a["siirto"] = 0.90 * 6000 / 2                             # 2p_z, 6000 hits, 90 % inside, half in the upper lobe: 2700
a["siirto-mis-all"] = 0.90 * 6000                         # forgot the two lobes: 5400
a["siirto-mis-half"] = 6000 / 2                           # forgot the threshold: 3000
a["virhe-n3"] = 2 * 3 ** 2                                # 18 electrons, not 6
a["tarkistus-2"] = E(1) * -1 - E(2) * -1                  # 2p -> 1s photon energy 13,6 - 3,40 = 10,2 eV
a["tarkistus-2-mis-sum"] = 13.6 + 3.4                     # added the levels: 17,0 eV
a["tarkistus-2-mis-E2"] = 3.4                             # took one level: 3,4 eV
a["exit-orb-n3"] = 3 ** 2                                 # 9 orbitals in shell n = 3
print(json.dumps({k: round(v, 6) if abs(v) >= 1e-3 else float(f"{v:.6g}") for k, v in a.items()}))
