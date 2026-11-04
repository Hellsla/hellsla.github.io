"""Numbers of the lesson text and inquiry.json for fy6-8, computed from their data (python -I lesson-answers.py); the
exercises' answers are in answers.py. Model of a battery: an ideal source E in series with the internal resistance
R_s (constant), ideal wires and meters (the voltmeter takes no current, the ammeter has no resistance).
U = E - R_s I, I = E / (R + R_s), I_k = E / R_s; cells in series add E and R_s, n identical cells in parallel keep E
and have R_s / n. Prints {id: number} as JSON."""
import json

a = {}


def load(E, Rs, R):
    """Current and terminal voltage of a source E, R_s with a load R."""
    I = E / (R + Rs)
    return I, E - Rs * I


# --- the simulation's batteries: new E = 1,60 V, R_s = 0,20 ohm; used E = 1,45 V, R_s = 1,2 ohm ---
NEW, USED = (1.60, 0.20), (1.45, 1.2)
combo = {"yksi": lambda E, r: (E, r), "sarja": lambda E, r: (2 * E, 2 * r), "rinnan": lambda E, r: (E, r / 2)}
I, U = load(*NEW, 2.0)                                     # on load: new, one cell, R = 2,0 ohm, switch closed
a["sim-I"], a["sim-U"] = I, U                              # 0,7273 A, 1,4545 V
a["sim-drop"] = NEW[1] * I                                 # R_s I = 0,145 V
a["sim-Ik"] = NEW[0] / NEW[1]                              # short circuit of the new cell: 8,0 A
a["sim-Ik-used"] = USED[0] / USED[1]                       # used cell: 1,21 A
# experiment 1: new cell, R = 1, 2, 4, 8 ohm
for R in (1, 2, 4, 8):
    I, U = load(*NEW, R)
    a[f"koe1-R{R}-I"], a[f"koe1-R{R}-U"] = I, U            # 1,333/1,333; 0,7273/1,4545; 0,3810/1,5238; 0,1951/1,5610
I1, U1 = load(*NEW, 1); I4, U4 = load(*NEW, 4)
a["koe1-Rs"] = (U4 - U1) / (I1 - I4)                       # slope of the line: R_s = 0,20 ohm
a["koe1-Rs-rounded"] = (round(U4, 3) - round(U1, 3)) / (round(I1, 3) - round(I4, 3))   # from the 3-decimal readings: 0,2006
a["koe1-E"] = U1 + a["koe1-Rs"] * I1                       # intercept E = 1,60 V
a["koe1-mistake-R"] = U1 / I1                              # U : I is the load R = 1,0 ohm, not R_s
a["koe1-mistake-ER"] = 1.60 / I1                           # E : I = R + R_s = 1,2 ohm
# experiment 2: new cells, R = 1,0 ohm, one / two in series / two in parallel
for k, f in combo.items():
    E, r = f(*NEW)
    I, U = load(E, r, 1.0)
    a[f"koe2-{k}-I"], a[f"koe2-{k}-U"] = I, U              # yksi 1,333/1,333; sarja 2,2857/2,2857; rinnan 1,4545/1,4545
# experiment 3: used cell, R = 1, 2, 4, 8 ohm
for R in (1, 2, 4, 8):
    I, U = load(*USED, R)
    a[f"koe3-R{R}-I"], a[f"koe3-R{R}-U"] = I, U            # 0,6591/0,6591; 0,4531/0,9063; 0,2788/1,1154; 0,1576/1,2609

# --- theory: the U-I graph of a cell E = 1,50 V, R_s = 0,30 ohm (Kaava figure) ---
a["graph-Ik"] = 1.50 / 0.30                                # 5,0 A
a["graph-dU"] = 0.30 * 2.0                                 # over Delta I = 2,0 A the voltage falls 0,60 V
# short circuits in the text: the new AA cell 1,60 V / 0,20 ohm = 8,0 A; a car battery 12,6 V / 0,010 ohm
a["text-Ik-AA"] = 1.60 / 0.20
a["text-Ik-car"] = 12.6 / 0.010                            # 1260 A
# connections in the text: two new AA cells
a["text-series-E"], a["text-series-Rs"] = 2 * 1.60, 2 * 0.20   # 3,20 V, 0,40 ohm
a["text-par-E"], a["text-par-Rs"] = 1.60, 0.20 / 2             # 1,60 V, 0,10 ohm
a["text-flashlight"] = 3 * 1.5                              # three cells in series: about 4,5 V

# --- worked example: open circuit 1,58 V, with 4,0 ohm the terminal voltage 1,45 V ---
I = 1.45 / 4.0
a["ex-I"] = I                                              # 0,3625 A
a["ex-Rs"] = (1.58 - 1.45) / I                             # 0,3586 ohm -> 0,36 ohm
a["ex-Ik"] = 1.58 / a["ex-Rs"]                             # 4,406 A -> 4,4 A
a["ex-check-U"] = 1.58 - a["ex-Rs"] * I                    # 1,45 V back

# --- kertaus: loop with a 9,0 V source, 3,0 V over R1: R2 gets 6,0 V ---
a["kertaus"] = 9.0 - 3.0
a["kertaus-mistake"] = 9.0 + 3.0                            # 12 V (added)

# --- error spotting: E = 9,0 V, R_s = 1,5 ohm, R = 12 ohm ---
I, U = load(9.0, 1.5, 12)
a["virhe-I"], a["virhe-U"] = I, U                          # 0,6667 A, 8,0 V
a["virhe-wrong-I"] = 9.0 / 12                              # 0,75 A (internal resistance forgotten)
a["virhe-wrong-Ik"] = 9.0 / 1.5                            # 6,0 A (the short-circuit current)

# --- transfer task: car battery E = 12,6 V, R_s = 0,012 ohm, starter 180 A ---
a["siirto-drop"] = 0.012 * 180                             # 2,16 V
a["siirto"] = 12.6 - 0.012 * 180                           # 10,44 V -> 10,4 V
a["siirto-mistake-add"] = 12.6 + 0.012 * 180               # 14,76 V
a["siirto-lamp-ratio"] = (a["siirto"] / 12.6) ** 2         # a lamp of constant R gets (U/E)^2 = 0,69 of its power
a["siirto-Ik"] = 12.6 / 0.012                              # 1050 A

# --- check 2: figure check-graph, 9 V battery points with scatter; the fitted line ---
pts = [(0.25, 8.52), (0.50, 7.96), (0.75, 7.53), (1.00, 6.98), (1.25, 6.51)]
n = len(pts); sx = sum(p[0] for p in pts); sy = sum(p[1] for p in pts)
sxx = sum(p[0] ** 2 for p in pts); sxy = sum(p[0] * p[1] for p in pts)
k = (n * sxy - sx * sy) / (n * sxx - sx ** 2); b = (sy - k * sx) / n
a["check2-slope"], a["check2-E"] = k, b                    # about -2,0 V/A and 9,0 V
a["tarkistus-2"] = (9.0 - 6.0) / (1.5 - 0.0)               # read from the line: (0 A; 9,0 V) and (1,5 A; 6,0 V): 2,0 ohm
a["tarkistus-2-mistake"] = 6.0 / 1.5                       # U : I of the point (1,5 A; 6,0 V): 4,0 ohm, the load resistance
a["tarkistus-2-mistake-E"] = 9.0 / 1.5                     # E : I = 6,0 ohm
a["tarkistus-2-Ik"] = 9.0 / 2.0                            # 4,5 A
a["tarkistus-2-at1"] = 9.0 - 2.0 * 1.00                    # 7,0 V on the line at 1,00 A

# --- exit ticket: 9,0 V, R_s = 1,8 ohm short circuit ---
a["exit-Ik"] = 9.0 / 1.8                                   # 5,0 A
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
