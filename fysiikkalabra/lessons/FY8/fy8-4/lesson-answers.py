"""Numbers of the lesson text and inquiry.json for fy8-4, computed from their data (python -I lesson-answers.py); the
exercises' answers are in answers.py. The double-slit model is the one of the simulation (assets/sims/fy8/fy8-4/sim.js):
screen positions -12 ... 12 mm in 480 bins of 0,05 mm, intensity cos²(πx/2,0 mm)·sinc²(πx/10 mm) with both slits open
and nobody measuring the path, sinc²(πx/10 mm) with one slit or with the path measured; every hit draws four
Park–Miller numbers (bin, place in the bin, height in the strip, slit), seed 12345 after every reset.
Prints {id: number} as JSON on the last line."""
import json, math

h, c, e = 6.626e-34, 2.998e8, 1.602e-19
a = {}

# --- worked example (lesson.md Esimerkki): weak laser light, 633 nm, power 1,0e-13 W after the filters
P, lam = 1.0e-13, 633e-9
E_f = h * c / lam                                   # photon energy hc/λ = 3,138e-19 J
a["esim-E"] = E_f
a["esim-rate"] = P / E_f                            # N/t = P/(hc/λ) = 3,19e5 1/s
a["esim-d"] = c / a["esim-rate"]                    # mean distance between photons = c t / N = 940 m
a["esim-apparatus-photons"] = 1.2 / a["esim-d"]     # photons in a 1,2 m apparatus on average: 0,0013

# --- Kaava text: momentum of a 500 nm photon and of an 0,0711 nm X-ray photon
a["p-500nm"] = h / 500e-9                           # 1,33e-27 kg m/s
a["p-xray"] = h / 0.0711e-9                         # 9,32e-24 kg m/s

# --- Compton table (interpret, model values): Mo K-alpha 0,0711 nm, Δλ = h/(m_e c) (1 − cos θ)
m_e = 9.109e-31
lc = h / (m_e * c)                                  # 2,426e-12 m
for deg in (0, 45, 90, 135, 180):
    a[f"compton-{deg}"] = (0.0711e-9 + lc * (1 - math.cos(math.radians(deg)))) * 1e9   # nm: 0,0711 0,0718 0,0735 0,0752 0,0760
E0 = h * c / 0.0711e-9 / e / 1e3                    # 17,4 keV
E90 = h * c / (a["compton-90"] * 1e-9) / e / 1e3    # 16,9 keV
a["compton-E0-keV"] = E0
a["compton-E90-keV"] = E90
a["compton-Ek90-eV"] = (E0 - E90) * 1e3             # electron gets about 580 eV at 90°

# --- virhe (error spotting): 520 nm photon, λ left in nanometres vs in metres
a["virhe-wrong"] = h / 520                          # 1,27e-36 (the student's number)
a["virhe-right"] = h / 520e-9                       # 1,27e-27 kg m/s

# --- tarkistus-2: X-ray 0,0600 nm scattered to 0,0624 nm, electron's kinetic energy in eV
a["tarkistus-2"] = (h * c / 0.0600e-9 - h * c / 0.0624e-9) / e          # 795 eV
a["tarkistus-2-wrong-no-conv"] = h * c / 0.0600e-9 - h * c / 0.0624e-9  # left in joules: 1,27e-16
a["tarkistus-2-dlam"] = h * c / (0.0024e-9) / e                          # hc/Δλ: 5,2e5 eV (a wrong method)

# --- siirto: solar sail, sunlight 1361 W/m² on 32 m², reflected straight back: F = 2 I A / c
I, A = 1361, 32.0
a["siirto"] = 2 * I * A / c * 1e6                   # micronewtons: 290,5 µN
a["siirto-absorb"] = I * A / c * 1e6                # absorbed (no factor 2): 145 µN
a["siirto-no-area"] = 2 * I / c * 1e6                # area forgotten: 9,08 µN
a["siirto-mass-mg"] = a["siirto"] * 1e-6 / 9.81 * 1e6    # mass whose weight equals the force: 29,6 mg (a grain of rice)
a["siirto-per-photon-check"] = (I * A) / (h * c / 550e-9)   # photons per second at 550 nm, for the check: 1,2e23

# --- the simulation's model (tests/sims/fy8-4.json)
XMIN, BW, NB, S, A0, M = -12.0, 0.05, 480, 2.0, 10.0, 2147483647
def inten(x, both):
    u = math.pi * x / A0
    env = 1.0 if x == 0 else (math.sin(u) / u) ** 2
    return math.cos(math.pi * x / S) ** 2 * env if both else env
def centres(): return [XMIN + BW * (i + 0.5) for i in range(NB)]
def cum(both):
    C, s = [], 0.0
    for xc in centres(): s += inten(xc, both); C.append(s)
    return C
def window(x0): return [i for i, xc in enumerate(centres()) if abs(xc - x0) < 0.2]
def pw(both, x0):
    C = cum(both); w = [C[0]] + [C[i] - C[i - 1] for i in range(1, NB)]
    return sum(w[i] for i in window(x0)) / C[-1]
def hits(both, nhits, seed=12345):
    C = cum(both); W = C[-1]; s = seed; out = []
    for _ in range(nhits):
        r = []
        for _k in range(4): s = (s * 16807) % M; r.append(s / M)
        t = r[0] * W
        i = next(k for k, v in enumerate(C) if v > t)
        out.append(i)
    return out
def count(both, x0, nhits):
    win = set(window(x0)); return sum(1 for i in hits(both, nhits) if i in win)
a["sim-pw-one-1"] = pw(False, 1.0) * 100            # % of hits expected in the counting interval at 1,0 mm, one slit
a["sim-pw-both-1"] = pw(True, 1.0) * 100            # both slits: about 0,3 %
a["sim-pw-both-0"] = pw(True, 0.0) * 100            # both slits at the centre: about 8 %
a["sim-pw-one-0"] = pw(False, 0.0) * 100            # one slit at the centre: about 4 %
a["sim-n-one-1"] = count(False, 1.0, 1000)          # hits in the interval after +1000 from a reset
a["sim-n-both-1"] = count(True, 1.0, 1000)
a["sim-n-both-0"] = count(True, 0.0, 1000)
a["sim-n-one-0"] = count(False, 0.0, 1000)
a["sim-n-both-1-2000"] = count(True, 1.0, 2000)
a["sim-n-one-1-2000"] = count(False, 1.0, 2000)
print(json.dumps({k: float(f"{v:.6g}") for k, v in a.items()}))
