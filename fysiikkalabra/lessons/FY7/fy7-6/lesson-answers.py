"""Numbers of the lesson text and inquiry.json for fy7-6, computed from their data (python -I lesson-answers.py); the
exercises' answers are in answers.py. Energy of a magnet falling through a conducting tube: Q = m g h - 1/2 m v^2;
at constant speed the braking force equals the weight, F = m g, and the heating power is P = F v = m g v.
Prints {id: number} as JSON."""
import json, math

g = 9.81
a = {}
# Worked example: magnet m = 25 g through a copper tube h = 1,20 m in t = 8,0 s, almost all the way at constant speed
m, h, t = 25e-3, 1.20, 8.0
a["ex-v"] = h / t                                   # v = h / t = 0,15 m/s
a["ex-Ep"] = m * g * h                              # m g h = 0,29430 J
a["ex-Ek"] = 0.5 * m * a["ex-v"] ** 2               # 1/2 m v^2 = 2,8125e-4 J
a["ex-Q"] = a["ex-Ep"] - a["ex-Ek"]                 # Q = 0,29402 J -> 0,29 J
a["ex-share"] = a["ex-Ek"] / a["ex-Ep"] * 100       # Järkevyys: E_k is 0,096 % of m g h, about 0,1 %
a["ex-P"] = a["ex-Q"] / t                           # Järkevyys: heating power 0,0368 W, about 37 mW
a["ex-dT"] = a["ex-Q"] / (0.30 * 385)               # Järkevyys: a 0,30 kg copper tube (c = 385 J/(kg K)) warms 0,0025 K
a["ex-F"] = m * g                                   # Järkevyys: the braking force at constant speed, 0,245 N
# Simulation: m = 20 g, tube 1,00 m; terminal speeds: copper 0,15 m/s (model choice), aluminium 0,15 · σCu/σAl, slit tube 1,5 m/s
ms, hs = 20e-3, 1.00
sCu, sAl = 5.96e7, 3.77e7                           # conductivities at 20 °C (S/m)
a["sim-ratio"] = sAl / sCu                          # aluminium conducts 0,633 of copper: k is 0,633 times as large
vt = {"kupari": 0.15, "alumiini": 0.15 * sCu / sAl, "rako": 1.5}
def fall(v):
    tau = v / g; T = hs / v + tau                   # y(t) = vt (t - tau (1 - e^(-t/tau))), tau = vt / g
    for _ in range(60):
        y = v * (T - tau * (1 - math.exp(-T / tau))); w = v * (1 - math.exp(-T / tau)); T -= (y - hs) / w
    return T, v * (1 - math.exp(-T / tau))
a["sim-t-muovi"] = math.sqrt(2 * hs / g)            # free fall: 0,45 s
a["sim-v-muovi"] = math.sqrt(2 * g * hs)            # 4,43 m/s
for k, v in vt.items():
    T, vb = fall(v)
    a[f"sim-vt-{k}"] = v                            # terminal speed: copper 0,15, aluminium 0,237, slit 1,5 m/s
    a[f"sim-t-{k}"] = T                             # fall time: copper 6,68 s, aluminium 4,24 s, slit 0,82 s
    a[f"sim-v-{k}"] = vb                            # speed at the bottom: 0,15; 0,24; 1,49 m/s
    a[f"sim-Q-{k}"] = (ms * g * hs - 0.5 * ms * vb ** 2) * 1e3   # internal energy, mJ: 196,0; 195,6; 173,9
a["sim-Ep"] = ms * g * hs * 1e3                     # 196,2 mJ
a["sim-G"] = ms * g                                 # weight 0,196 N = braking force at terminal speed
a["sim-P-kupari"] = ms * g * 0.15                   # heating power at terminal speed in copper: 0,0294 W
a["sim-Ek-share-kupari"] = 0.5 * ms * 0.15 ** 2 / (ms * g * hs) * 100   # 0,11 %
a["sim-slow-ratio"] = fall(0.15)[0] / math.sqrt(2 * hs / g)   # copper is about 15 times slower than free fall
# Kaava figure: energies at the bottom in the sim (plastic vs copper), mJ
a["fig-Ek-muovi"] = 0.5 * ms * a["sim-v-muovi"] ** 2 * 1e3      # 196,2 mJ
a["fig-Ek-kupari"] = 0.5 * ms * 0.15 ** 2 * 1e3                # 0,225 mJ
# siirto: roller-coaster car 2,4 t braked by an eddy-current brake from 25 m/s to 10 m/s over 30 m
M, v1, v2, s = 2.4 * 1000, 25.0, 10.0, 30.0
a["siirto-Q"] = 0.5 * M * (v1 ** 2 - v2 ** 2)       # 630 000 J
a["siirto"] = a["siirto-Q"] / s / 1e3               # F = Q / s = 21 000 N = 21 kN
a["siirto-nov2"] = 0.5 * M * v1 ** 2 / s / 1e3      # mistake: final speed ignored: 25 kN
a["siirto-diff"] = 0.5 * M * (v1 - v2) ** 2 / s / 1e3   # mistake: (v1 - v2)^2: 9,0 kN
a["siirto-nohalf"] = M * (v1 ** 2 - v2 ** 2) / s / 1e3  # mistake: no 1/2: 42 kN
a["siirto-a"] = a["siirto"] * 1e3 / M               # Järkevyys: deceleration 8,75 m/s², about 0,9 g
# tarkistus-2: magnet 18 g at constant speed 0,24 m/s in an aluminium tube: P = m g v
a["check-P"] = 18e-3 * g * 0.24 * 1e3               # 42,4 mW -> 42 mW
a["check-P-noG"] = 18e-3 * 0.24 * 1e3               # mistake: g forgotten: 4,3 mW
a["check-P-Ek"] = 0.5 * 18e-3 * 0.24 ** 2 * 1e3     # mistake: kinetic energy instead of power: 0,52 mJ
# Exit ticket: none numeric
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
