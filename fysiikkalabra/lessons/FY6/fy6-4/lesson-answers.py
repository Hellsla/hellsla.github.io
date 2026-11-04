"""Numbers of the lesson text and inquiry.json for fy6-4, computed from their data (python -I lesson-answers.py); the
exercises' answers are in answers.py. Series: R = R1 + R2, one current I = U / R, U1 = R1 I, U2 = R2 I.
Parallel: 1/R = 1/R1 + 1/R2, each branch has the battery's voltage, I1 = U / R1, I2 = U / R2, I = I1 + I2.
The simulation's model is the same (ideal battery and wires, ideal meters). Prints {id: number} as JSON."""
import json

par = lambda *R: 1 / sum(1 / r for r in R)
a = {}

# --- simulation on load: series, U = 6,0 V, R1 = 100 ohm, R2 = 50 ohm ---
a["sim-load-R"] = 100 + 50                                # 150 ohm
a["sim-load-ImA"] = 6.0 / 150 * 1000                      # 40 mA
a["sim-load-U1"] = 100 * 6.0 / 150                        # 4,0 V
a["sim-load-U2"] = 50 * 6.0 / 150                         # 2,0 V
# --- koe 1 (series, U = 6,0 V, R1 = 100 ohm, vary R2) and prediction 1 ---
for R2 in (50, 100, 200):
    I = 6.0 / (100 + R2)
    a[f"koe1-R2-{R2}-ImA"] = I * 1000                     # 40 / 30 / 20 mA, the same through both resistors
    a[f"koe1-R2-{R2}-U1"] = 100 * I                       # 4,0 / 3,0 / 2,0 V
    a[f"koe1-R2-{R2}-U2"] = R2 * I                        # 2,0 / 3,0 / 4,0 V; U1 + U2 = 6,0 V every time
# --- prediction 2: R1 = 100 ohm alone on 6,0 V ---
a["pred2-alone-ImA"] = 6.0 / 100 * 1000                   # 60 mA
# --- koe 2 (parallel, U = 6,0 V, R1 = 100 ohm, vary R2) ---
for R2 in (50, 100, 200):
    a[f"koe2-R2-{R2}-I1mA"] = 6.0 / 100 * 1000            # 60 mA in every row: the branch keeps the battery's voltage
    a[f"koe2-R2-{R2}-I2mA"] = 6.0 / R2 * 1000             # 120 / 60 / 30 mA
    a[f"koe2-R2-{R2}-ImA"] = (6.0 / 100 + 6.0 / R2) * 1000   # 180 / 120 / 90 mA
    a[f"koe2-R2-{R2}-R"] = par(100, R2)                   # 33,3 / 50 / 66,7 ohm, always below the smaller one
# --- theory: graph kaava-graph (R1 = 100 ohm, R2 from 0 to 200 ohm) ---
a["graph-series-200"] = 100 + 200                         # 300 ohm at the right end
a["graph-par-200"] = par(100, 200)                        # 66,7 ohm
a["graph-par-100"] = par(100, 100)                        # 50 ohm: two equal resistors give half
# --- worked example: 120 ohm || 60 ohm on 9,0 V ---
a["ex-R"] = par(120, 60)                                  # 120 * 60 / 180 = 40 ohm
a["ex-I"] = 9.0 / a["ex-R"]                               # 0,225 A -> 0,23 A
a["ex-I1"] = 9.0 / 120                                    # check: 0,075 A
a["ex-I2"] = 9.0 / 60                                     # check: 0,15 A; 0,075 + 0,15 = 0,225 A
# --- error spotting: 20 ohm || 30 ohm ---
a["virhe-inv"] = 1 / 20 + 1 / 30                          # 0,0833 1/ohm (the student's "R")
a["virhe-R"] = par(20, 30)                                # 12 ohm
# --- transfer task: 60 ohm || 30 ohm, in series with 20 ohm, U = 12 V ---
a["siirto-Rpar"] = par(60, 30)                            # 20 ohm
a["siirto-R"] = 20 + a["siirto-Rpar"]                     # 40 ohm
a["siirto-I"] = 12 / a["siirto-R"]                        # 0,30 A
a["siirto-mistake-allseries"] = 12 / (60 + 30 + 20)       # 0,109 A
a["siirto-mistake-parallel-only"] = 12 / a["siirto-Rpar"] # 0,60 A
a["siirto-mistake-noinv"] = 12 / (20 + 1 / 60 + 1 / 30)  # 0,598 A: 1/R not inverted
a["siirto-U20"] = 20 * a["siirto-I"]                      # check: 6,0 V over 20 ohm, 6,0 V over the parallel part
# --- check 1: kettle added in parallel (230 V) ---
# --- check 2: series 220 ohm + 330 ohm on 9,0 V, voltage over 330 ohm ---
a["check2-I"] = 9.0 / (220 + 330)                         # 0,016364 A
a["check2-U2"] = 330 * a["check2-I"]                      # 5,4 V
a["check2-U1"] = 220 * a["check2-I"]                      # 3,6 V (mistake: the other resistor)
# --- misconception: lamps 10 ohm and 20 ohm in series on 6,0 V ---
a["virhek-I"] = 6.0 / 30                                  # 0,20 A through both
# --- exit ticket ---
a["exit-1"] = 47 + 68                                     # 115 ohm
a["exit-2"] = par(80, 80)                                 # 40 ohm
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
