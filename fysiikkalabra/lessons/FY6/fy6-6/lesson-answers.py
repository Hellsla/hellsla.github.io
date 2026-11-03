"""Numbers of the lesson text and inquiry.json for fy6-6, computed from their data (python -I lesson-answers.py); the
exercises' answers are in answers.py. P = U I; with U = R I: P = R I^2 = U^2 / R; E = P t. Ideal source and wires,
resistors of constant resistance. The simulation: two resistors R1, R2 in series or in parallel on U, each in a beaker
of 0,10 kg water (c = 4190 J/(kg K)) from 20,0 C, heat losses neglected. Prints {id: number} as JSON."""
import json

a = {}
C, M = 4190, 0.10


def circuit(U, R1, R2, mode):
    if mode == "sarja":
        I = U / (R1 + R2)
        return dict(I=I, I1=I, I2=I, U1=R1 * I, U2=R2 * I, P1=R1 * I * I, P2=R2 * I * I, P=U * I)
    I1, I2 = U / R1, U / R2
    return dict(I=I1 + I2, I1=I1, I2=I2, U1=U, U2=U, P1=U * I1, P2=U * I2, P=U * (I1 + I2))


# --- simulation on load and the predictions: U = 12 V, R1 = 4 ohm, R2 = 8 ohm ---
s = circuit(12, 4, 8, "sarja")
for k in ("I", "U1", "U2", "P1", "P2", "P"):
    a[f"sarja-{k}"] = s[k]                                    # I = 1,0 A; U1 = 4,0 V; U2 = 8,0 V; P1 = 4,0 W; P2 = 8,0 W; P = 12 W
r = circuit(12, 4, 8, "rinnan")
for k in ("I", "I1", "I2", "P1", "P2", "P"):
    a[f"rinnan-{k}"] = r[k]                                   # I1 = 3,0 A; I2 = 1,5 A; P1 = 36 W; P2 = 18 W; P = 54 W
# temperature rise in 60 s, no losses: dT = P t / (c m)
a["sarja-dT1-60s"] = s["P1"] * 60 / (C * M)                   # 0,573 K
a["sarja-dT2-60s"] = s["P2"] * 60 / (C * M)                   # 1,15 K
a["rinnan-dT1-60s"] = r["P1"] * 60 / (C * M)                  # 5,16 K
a["rinnan-dT2-60s"] = r["P2"] * 60 / (C * M)                  # 2,58 K
# experiments: R2 varied (4, 8, 16 ohm), U = 12 V and R1 = 4 ohm locked
for mode in ("sarja", "rinnan"):
    for R2 in (4, 8, 16):
        k = circuit(12, 4, R2, mode)
        for q in ("I", "I1", "I2", "U1", "U2", "P1", "P2", "P"):
            a[f"koe-{mode}-{R2}-{q}"] = k[q]
# sarja 4: I 1,5 A, P1 = P2 = 9,0 W; sarja 16: I 0,60 A, P1 1,44 W, P2 5,76 W; rinnan 16: P2 = 9,0 W

# --- Ydinajatus figure: U = 12 V, I = 0,50 A ---
a["fig-energia-P"] = 12 * 0.50                                # 6,0 W: 6,0 J each second
a["fig-energia-R"] = 12 / 0.50                                # 24 ohm
# --- Kaava graph: P = R I^2 for 4 ohm and 8 ohm at 1,0 A and 2,0 A ---
for R in (4, 8):
    for I in (1.0, 2.0):
        a[f"graph-{R}-{I}"] = R * I * I                       # 4, 16 / 8, 32 W
# --- the steady-state figure is schematic (no numbers) ---

# --- hook: toaster 230 V, 900 W; cord 0,050 ohm ---
I_t = 900 / 230                                               # 3,91 A
a["hook-R"] = 230 ** 2 / 900                                  # element 58,8 ohm
a["hook-cord-P"] = 0.050 * I_t ** 2                           # cord 0,77 W
# --- worked example: 15 ohm and 30 ohm in parallel on 12 V, 5,0 min ---
a["ex-P1"] = 12 ** 2 / 15                                     # 9,6 W
a["ex-P2"] = 12 ** 2 / 30                                     # 4,8 W
a["ex-P"] = a["ex-P1"] + a["ex-P2"]                           # 14,4 W
a["ex-t"] = 5.0 * 60                                          # 300 s
a["ex-E"] = a["ex-P"] * a["ex-t"]                             # 4320 J = 4,3 kJ
a["ex-I"] = 12 / 15 + 12 / 30                                 # 1,2 A
a["ex-UI"] = 12 * a["ex-I"]                                   # 14,4 W = P1 + P2
# --- error spotting: series 12 V, 4 and 8 ohm; P2 with the source voltage ---
a["virhe-wrong"] = 12 ** 2 / 8                                # 18 W (wrong)
a["virhe-right"] = s["P2"]                                    # 8,0 W
a["virhe-U2"] = s["U2"]                                       # 8,0 V
a["virhe-wrong-sum"] = 12 ** 2 / 4 + 12 ** 2 / 8              # 54 W > U I = 12 W
# --- transfer: 12 V travel kettle 2,4 ohm, 0,40 kg water 20 -> 100 C ---
P_k = 12 ** 2 / 2.4                                           # 60 W
E_k = C * 0.40 * (100 - 20)                                   # 134 080 J
a["siirto-P"] = P_k
a["siirto-E"] = E_k
a["siirto-t-s"] = E_k / P_k                                   # 2234,7 s
a["siirto"] = E_k / P_k / 60                                  # 37,2 min
a["siirto-mistake-R"] = E_k / (12 * 2.4) / 60                 # P = U R by mistake: 77,6 min
a["siirto-mistake-UR"] = E_k / (12 / 2.4) / 60                # P = U / R: 447 min
a["siirto-mistake-s"] = E_k / P_k                             # forgot minutes: 2235
# --- check 2: extension cord 0,20 ohm at 8,0 A ---
a["tarkistus-2"] = 0.20 * 8.0 ** 2                            # 12,8 W
a["tarkistus-2-mistake"] = 0.20 * 8.0                         # 1,6 (R I, a voltage)
# --- check 1: 230 V lamps 40 W and 100 W ---
a["t1-R40"] = 230 ** 2 / 40                                   # 1322,5 ohm
a["t1-R100"] = 230 ** 2 / 100                                 # 529 ohm
# --- exit ticket ---
a["exit-1"] = 1150 / 230                                      # 5,0 A
a["exit-2"] = 2 ** 2                                          # four times the power
# --- retrieval: Ohm 6,0 V over 30 ohm ---
a["kertaus"] = 6.0 / 30                                       # 0,20 A
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
