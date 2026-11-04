"""Numbers of the lesson text and inquiry.json for fy8-11, computed from their data (python -I lesson-answers.py); the
exercises' answers are in answers.py. Reaction energy Q = (m_before - m_after) c^2 from atomic masses in u,
1 u = 931,5 MeV/c^2 (as in the chapter Massavaje ja ytimen sidosenergia); 1 u = 1,66054e-27 kg, 1 eV = 1,602e-19 J.
Atomic masses: AME2020 (Wang et al., Chinese Physics C 45, 030003, 2021), rounded to 7 decimals.
The chain-reaction model values (koe 1-2, predictions) come from the same seeded generator as
assets/sims/fy8/fy8-11/sim.js (mulberry32, seed 1000 * (series + 2) + 7): every neutron of a generation causes a fission with
probability P_f = (1,2 - 0,008 s) : 2,5 (s = control rods in, %), a fission gives 2 or 3 neutrons (mean 2,5), so
k = 1,2 - 0,008 s. Prints {id: number} as JSON on the last line."""
import json, math

U_MEV = 931.5                    # MeV/c^2 per u
U_KG = 1.66054e-27               # kg
EV = 1.602e-19                   # J
M = {"n": 1.0086649, "H-1": 1.0078250, "H-2": 2.0141018, "H-3": 3.0160493, "He-3": 3.0160293, "He-4": 4.0026033,
     "Li-6": 6.0151229, "Li-7": 7.0160034, "C-12": 12.0000000, "O-16": 15.9949146, "Ne-20": 19.9924402,
     "Si-28": 27.9769265, "Ca-40": 39.9625909, "Fe-56": 55.9349363, "Ni-62": 61.9283454, "Zr-90": 89.9046977,
     "Kr-92": 91.9261731, "Sr-94": 93.9153556, "Sn-120": 119.9022016, "Ba-141": 140.9144033, "Xe-140": 139.9216458,
     "Au-197": 196.9665688, "Pb-208": 207.9766525, "U-235": 235.0439282, "U-238": 238.0507884}
Z = {"H-1": 1, "H-2": 1, "H-3": 1, "He-3": 2, "He-4": 2, "Li-6": 3, "Li-7": 3, "C-12": 6, "O-16": 8, "Ne-20": 10,
     "Si-28": 14, "Ca-40": 20, "Fe-56": 26, "Ni-62": 28, "Zr-90": 40, "Kr-92": 36, "Sr-94": 38, "Sn-120": 50,
     "Ba-141": 56, "Xe-140": 54, "Au-197": 79, "Pb-208": 82, "U-235": 92, "U-238": 92}
a = {}

def semf(A):
    """A smooth trend of the binding energy per nucleon (MeV) for A >= 16 (drawn in the figures; read in Tarkista 2)."""
    Z_ = round(A / (1.98 + 0.0155 * A ** (2 / 3)))
    return (15.75 * A - 17.8 * A ** (2 / 3) - 0.711 * Z_ * (Z_ - 1) / A ** (1 / 3) - 23.7 * (A - 2 * Z_) ** 2 / A) / A

def bpn(name):
    """Binding energy per nucleon (MeV) from the atomic mass: Z hydrogen atoms + N neutrons - the atom."""
    A = int(name.split("-")[1]); z = Z[name]
    return (z * M["H-1"] + (A - z) * M["n"] - M[name]) * U_MEV / A

# ---------------------------------------------------------------- Ydinajatus: binding energy per nucleon (figure sidosenergia)
for k in Z:
    if k != "H-1": a[f"bpn-{k}"] = bpn(k)       # He-4 7,07; Fe-56 8,79; Ni-62 8,79; U-235 7,59 MeV
# fission estimate from the curve: 236 nucleons from about 7,6 MeV to about 8,5 MeV per nucleon
a["est-fission"] = 236 * (8.5 - 7.6)            # 212 MeV, about 200 MeV

# ---------------------------------------------------------------- Kaava figure and worked example: U-235 + n -> Ba-141 + Kr-92 + 3 n
m_before = M["U-235"] + M["n"]                  # 236,0525931 u
m_after = M["Ba-141"] + M["Kr-92"] + 3 * M["n"] # 235,8665711 u
a["ex-m-before"] = m_before
a["ex-m-after"] = m_after
a["ex-dm"] = m_before - m_after                 # 0,1860220 u
a["ex-Q"] = (m_before - m_after) * U_MEV        # 173,28 MeV -> 173 MeV
a["ex-share"] = 100 * (m_before - m_after) / m_before   # 0,079 % of the mass
a["ex-check"] = 0.19 * 900                      # 171 MeV with round numbers

# ---------------------------------------------------------------- Kaava: D + T -> He-4 + n
dt_dm = M["H-2"] + M["H-3"] - M["He-4"] - M["n"]
a["dt-dm"] = dt_dm                              # 0,0188829 u
a["dt-Q"] = dt_dm * U_MEV                       # 17,59 MeV -> 17,6 MeV
# energy per nucleon of fuel: fission 200 MeV / 236 = 0,85 MeV, D-T 17,6 MeV / 5 = 3,5 MeV
a["per-nucleon-fission"] = 200 / 236            # 0,847 MeV
a["per-nucleon-dt"] = dt_dm * U_MEV / 5         # 3,52 MeV
a["per-nucleon-ratio"] = (dt_dm * U_MEV / 5) / (200 / 236)   # 4,2

# ---------------------------------------------------------------- Miksi: 1,00 g of U-235 fissioned (200 MeV each) vs coal 24 MJ/kg
N_g = 1.00e-3 / (M["U-235"] * U_KG)             # 2,562e21 nuclei
E_g = N_g * 200e6 * EV                          # 8,21e10 J
a["miksi-N"] = N_g
a["miksi-E-GJ"] = E_g / 1e9                     # 82,1 GJ
a["miksi-coal-t"] = E_g / 24e6 / 1000           # 3,42 t of coal (lämpöarvo 24 MJ/kg)

# ---------------------------------------------------------------- chain reaction: N_g = N_0 k^g
a["k12-g10"] = 1000 * 1.2 ** 10                 # 6192
a["k08-g10"] = 1000 * 0.8 ** 10                 # 107
a["k104-g30"] = 1000 * 1.04 ** 30               # 3243 (ennuste 2: model)
a["k104-linear"] = 1000 + 30 * 40              # 2200 (the linear misconception)

# ---------------------------------------------------------------- Ydinvoima Suomessa: net electrical power (MW), IAEA PRIS / Fortum / TVO
plants = {"Loviisa 1": 507, "Loviisa 2": 507, "Olkiluoto 1": 890, "Olkiluoto 2": 890, "Olkiluoto 3": 1600}
a["fi-total-MW"] = sum(plants.values())         # 4394 MW
a["ol3-share-of-total"] = 100 * 1600 / sum(plants.values())   # 36 %
# OL3 thermal 4300 MW, net 1600 MW: efficiency
a["ol3-eff"] = 100 * 1600 / 4300                # 37 %
# decay heat: about 6-7 % of the thermal power right after shutdown -> OL3 about 280 MW
a["decay-heat-OL3"] = 0.065 * 4300              # 280 MW

# ---------------------------------------------------------------- Tarkista 2: read E_s/A off the curve at A = 236 and A = 118
a["chk2-236"] = semf(236)                       # 7,64 MeV (read 7,6)
a["chk2-118"] = semf(118)                       # 8,56 MeV (read 8,5-8,6)
a["chk2-curve"] = 236 * (semf(118) - semf(236)) # 217 MeV from the curve
a["chk2-read"] = 236 * (8.5 - 7.6)              # 212 MeV with the values read to 0,1 MeV -> about 210 MeV
a["chk2-mistake-perA"] = 8.5 - 7.6              # 0,9 MeV: forgot to multiply by the nucleons
a["chk2-mistake-118"] = 118 * (8.5 - 7.6)       # 106 MeV: multiplied by one fragment's nucleons

# ---------------------------------------------------------------- Sovella, siirto: ITER 500 MW of D-T fusion power
Q_dt_J = dt_dm * U_MEV * 1e6 * EV               # 2,818e-12 J
Q_given = 17.6e6 * EV                           # the task gives Q = 17,6 MeV: 2,8195e-12 J
a["siirto-Q-J"] = Q_given
a["siirto-rate"] = 500e6 / Q_given / 1e20       # 1,7734e20 reactions/s -> 1,77 (unit 10^20 1/s)
a["siirto-mistake-eV"] = 500e6 / (17.6 * EV) / 1e20             # 1 773 400: MeV taken as eV
a["siirto-mistake-fission"] = 500e6 / (200e6 * EV) / 1e20        # 0,156: 200 MeV of a fission
a["siirto-check"] = 5e8 / 3e-12 / 1e20          # 1,67 with round numbers
a["siirto-mass-per-s"] = 500e6 / Q_given * 5.0301511 * U_KG * 1e6   # mg of D-T fuel per second: 1,48 mg/s

# ---------------------------------------------------------------- inquiry: hook, predictions, Etsi virhe, keskustelu, tarkistus 3
a["hook-coal-t-per-day"] = 1600e6 / 0.40 * 86400 / 24e6 / 1000   # 1600 MW electric from coal at 40 %: 14 400 t/day
a["enn2-gens-to-million"] = math.log(1000) / math.log(1.04)       # 176 generations from 1000 to 10^6
a["enn2-add-at-20"] = 0.04 * 1987                                 # about 80 neutrons added per generation after g = 20
a["enn2-factor"] = 1.04 ** 30                                     # 3,24
a["virhe-wrong-dm"] = M["U-235"] - M["Ba-141"] - M["Kr-92"] - 3 * M["n"]   # -0,8226429 u (the incoming neutron forgotten)
a["virhe-wrong-Q"] = a["virhe-wrong-dm"] * U_MEV                  # -766 MeV
a["virhe-right-Q"] = a["ex-Q"]                                    # 173 MeV (the worked example)
a["xe-sr-Q"] = (M["U-235"] + M["n"] - M["Xe-140"] - M["Sr-94"] - 2 * M["n"]) * U_MEV   # 184,7 MeV (Tarkista 2 solution: 185 MeV)
a["cs-to-thousandth"] = 30.1 * math.log2(1000)                    # 300 a
a["decay-heat-6pct"] = 0.06 * 4300                                # 258 MW: "satoja megawatteja"

# ---------------------------------------------------------------- lesson text: other numbers
a["unit-example"] = 0.1 * U_MEV                 # 0,1 u -> 93,15 MeV
a["ipcc-ratio"] = 820 / 12                      # coal 820 vs nuclear 12 g/kWh (IPCC 2014 medians): about 1/68 -> "seitsemäskymmenesosa"
a["U235-natural-pct"] = 0.72                    # natural uranium U-235 share (%)
a["vir-nucleons"] = 1 + 235                     # 236 = 141 + 92 + 3

# ---------------------------------------------------------------- the simulation's model (same as sim.js)
MASK = 0xFFFFFFFF
def _i32(x):
    x &= MASK
    return x - 0x100000000 if x >= 0x80000000 else x
def _imul(x, y): return _i32((x & MASK) * (y & MASK))
def rng(seed):
    st = [seed & MASK]
    def r():
        st[0] = (st[0] + 0x6D2B79F5) & MASK
        t = _imul(st[0] ^ (st[0] >> 15), st[0] | 1) & MASK
        t = _i32(t ^ (t + _imul(t ^ (t >> 7), t | 61))) & MASK
        return (((t ^ (t >> 14)) & MASK) + 0.5) / 4294967297
    return r
GMAX, N0, CAP = 30, 1000, 3000000
def chain(s, series):
    """Neutrons N[g] and fissions F[g] of each generation g = 0 ... GMAX."""
    R = rng(1000 * (series + 2) + 7)
    pf = (1.2 - 0.008 * s) / 2.5
    N, F = [N0], []
    for g in range(GMAX):
        n, nxt, f = N[-1], 0, 0
        if n > CAP: N.append(n); F.append(0); continue
        for _ in range(n):
            if R() < pf:
                f += 1; nxt += 2 if R() < 0.5 else 3
        N.append(nxt); F.append(f)
    return N, F
def k_of(s): return 1.2 - 0.008 * s

# Koe 1: series 1, generation 20, control rods 0, 25, 50 %
for s in (0, 25, 50):
    N, F = chain(s, 1)
    a[f"koe1-k-{s}"] = k_of(s)                  # 1,20; 1,00; 0,80
    a[f"koe1-N20-{s}"] = N[20]
    a[f"koe1-model-{s}"] = N0 * k_of(s) ** 20   # 38338; 1000; 11,5
# Koe 2: series 1, rods 20 % (k = 1,04), generations 0, 10, 20, 30
N, F = chain(20, 1)
for g in (0, 10, 20, 30):
    a[f"koe2-N-{g}"] = N[g]
    a[f"koe2-model-{g}"] = N0 * 1.04 ** g       # 1000, 1480, 2191, 3243
# the other series at rods 25 % (k = 1,00), generation 30: a critical chain wanders
for sr in (1, 2, 3):
    a[f"crit-N30-s{sr}"] = chain(25, sr)[0][30]

if __name__ == "__main__":
    print(json.dumps({k: (round(v, 6) if isinstance(v, float) else v) for k, v in a.items()}))
