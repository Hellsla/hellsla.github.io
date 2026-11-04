"""Numbers of the lesson text and inquiry.json for fy7-16, computed from their data (python -I lesson-answers.py); the
exercises' answers are in answers.py. Wireless charging: the flux of the transmitter coil through one turn of the
receiver coil (two coaxial circular coils, thin-coil model, the same as the simulation) and e0 = N2 · 2πf · Φ0;
fibre attenuation A = a L and P = P0 · 10^(−A / 10 dB). Prints {id: number} as JSON."""
import json
from math import pi, sqrt, log10

MU0 = 4e-7 * pi                                     # vacuum permeability (Vs/(Am))


def ke(k):
    """Complete elliptic integrals K(k), E(k) by the arithmetic-geometric mean."""
    a, b, s, w = 1.0, sqrt(1 - k * k), k * k / 2, 0.5
    while abs(a - b) > 1e-15:
        c = (a - b) / 2; a, b = (a + b) / 2, sqrt(a * b); w *= 2; s += w * c * c
    K = pi / (2 * a)
    return K, K * (1 - s)


def flux_per_amp(R1, R2, z):
    """Flux (Wb per ampere of one transmitter turn) through a coaxial circle of radius R2 at height z (all in m)."""
    k = sqrt(4 * R1 * R2 / ((R1 + R2) ** 2 + z * z)); K, E = ke(k)
    return MU0 * sqrt(R1 * R2) * ((2 / k - k) * K - 2 / k * E)


N1, N2, I0, f, R2 = 10, 10, 1.0, 140e3, 0.020     # the simulation's fixed values
e0 = lambda R1, z: N2 * 2 * pi * f * N1 * I0 * flux_per_amp(R1 / 1000, R2, z / 1000)   # R1, z in mm -> V
a = {}
# simulation, transmitter radius 20 mm: e0 at 3, 5, 10, 20, 30, 40 mm and the share of the 3 mm value
for z in (3, 5, 10, 15, 20, 30, 40):
    a[f"sim-e0-20-{z}"] = e0(20, z)                 # 4,404 / 3,321 / 1,957 / 1,273 / 0,869 / 0,445 / 0,250 V
a["sim-phi0-20-3"] = N1 * I0 * flux_per_amp(0.020, R2, 0.003) * 1e6   # Φ0 = 0,5006 µWb
a["sim-share-20"] = 100 * e0(20, 20) / e0(20, 3)    # 19,74 % at 20 mm (koe-1 question, ennuste 1)
a["sim-share-10"] = 100 * e0(20, 10) / e0(20, 3)    # 44,45 % at 10 mm
# simulation at z = 20 mm (koe-2, ennuste 2) and at 3 mm (text): transmitter radius 10 ... 40 mm
for R1 in (10, 20, 30, 35, 40):
    a[f"sim-e0-{R1}-20mm"] = e0(R1, 20)             # 0,285 / 0,869 / 1,211 / 1,247 / 1,229 V
    a[f"sim-e0-{R1}-3mm"] = e0(R1, 3)               # 0,917 / 4,404 / 2,761 / 2,248 / 1,906 V
# Ravenscraft, OneZero 2020 (Pixel 4 from empty to full, energy from the socket)
cable, pad, stand, misaligned = 14.26, 21.01, 19.8, 25.62
a["data-pad"] = 100 * (pad / cable - 1)             # 47,3 % more (interpret question)
a["data-stand"] = 100 * (stand / cable - 1)         # 38,8 %
a["data-mis"] = 100 * (misaligned / cable - 1)      # 79,7 %
a["data-ratio"] = 100 * cable / pad                 # 67,9 %: the pad's efficiency relative to the cable's
a["data-pad-mis"] = misaligned - pad                # 4,61 Wh lost to misalignment
a["data-mistake-diff"] = pad - cable                # mistake: answered the difference 6,75 Wh
a["data-mistake-ratio"] = 100 * pad / cable         # mistake: answered the ratio 147,3 %
a["data-mistake-rev"] = 100 * (1 - cable / pad)     # mistake: divided by the pad's energy, 32,1 %
# fibre: Corning SMF-28 Ultra, at most 0,18 dB/km at 1550 nm and 0,32 dB/km at 1310 nm
a["half-1550"] = 10 * log10(2) / 0.18               # power halves in 16,7 km
a["half-1310"] = 10 * log10(2) / 0.32               # 9,4 km
a["100km-1550"] = 100 * 10 ** (-0.18 * 100 / 10)    # 1,58 % after 100 km (ennuste 3)
a["100km-1310"] = 100 * 10 ** (-0.32 * 100 / 10)    # 0,063 %
for L in (5, 10, 15, 20, 25):
    a[f"graph-1550-{L}"] = 100 * 10 ** (-0.18 * L / 10)   # graph points
    a[f"graph-1310-{L}"] = 100 * 10 ** (-0.32 * L / 10)
a["delay-per-km"] = 1.47 * 1000 / 3.00e8 * 1e6      # 4,9 µs per km in glass n = 1,47
# worked example: 80 km, 0,20 dB/km, 2,0 mW
A = 0.20 * 80                                       # A = a L = 16 dB
a["ex-A"] = A
a["ex-P"] = 2.0 * 10 ** (-A / 10) * 1000            # P = P0 · 10^(−1,6) = 0,0502 mW = 50,2 µW
a["ex-share"] = 100 * 10 ** (-A / 10)               # 2,5 % of the power
# siirto: receiver N = 12, A = 11 cm², f = 140 kHz, e0 = 9,0 V; B0 = e0 / (N A 2π f)
a["siirto"] = 9.0 / (12 * 11e-4 * 2 * pi * 140e3) * 1e3        # 0,775 mT
a["siirto-phi"] = 9.0 / (12 * 2 * pi * 140e3) * 1e6            # Φ0 = 0,853 µWb
a["siirto-noN"] = 9.0 / (11e-4 * 2 * pi * 140e3) * 1e3          # mistake: N forgotten, 9,30 mT
a["siirto-no2pi"] = 9.0 / (12 * 11e-4 * 140e3) * 1e3            # mistake: 2π forgotten, 4,87 mT
a["siirto-cm2"] = 9.0 / (12 * 11 * 2 * pi * 140e3) * 1e3        # mistake: cm² not converted, 7,75 · 10^-5 mT
a["siirto-earth"] = a["siirto"] / 0.052                         # about 15 times the Earth's 52 µT
# virhe: 20 dB leaves 1 % of the power (10^-2), not 1/20
a["virhe"] = 100 * 10 ** (-20 / 10)
# check-2: 30 km at 0,20 dB/km
a["check-A"] = 0.20 * 30                            # 6,0 dB
a["check"] = 100 * 10 ** (-0.20 * 30 / 10)          # 25,1 %
a["check-lin"] = 100 * (1 - 6.0 / 10)               # mistake: 6 dB read as 60 % lost, 40 %
a["check-loss"] = 100 - a["check"]                  # mistake: answered the lost share, 74,9 %
# exit ticket: power to one hundredth -> 20 dB
a["exit-dB"] = 10 * log10(100)
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
