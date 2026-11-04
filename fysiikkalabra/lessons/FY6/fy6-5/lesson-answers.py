"""Numbers of the lesson text and inquiry.json for fy6-5, computed from their data (python -I lesson-answers.py); the
exercises' answers are in answers.py. Ideal source (no internal resistance), ideal wires (no resistance), resistors
with constant resistance. Current law: the currents into a junction equal the currents out of it. Voltage law: around
a loop the potential changes add up to zero, so the source voltage equals the voltages of the resistors along the
loop. Ohm: U = R I. The simulation's circuit: a source U, R1 in series with R2 and R3 in parallel (points A..F).
Prints {id: number} as JSON."""
import json

par = lambda a, b: 1 / (1 / a + 1 / b)                       # two resistors in parallel (chapter 4)
a = {}


def circuit(U, R1, R2, R3):
    """Currents and voltages of the sim's circuit: U -> R1 -> (R2 || R3) -> back."""
    R23 = par(R2, R3)
    I1 = U / (R1 + R23)                                       # current through R1 and the source
    U1 = R1 * I1                                              # voltage of R1
    U23 = U - U1                                              # voltage law: the rest is over the branches
    return dict(R23=R23, I1=I1, U1=U1, U23=U23, I2=U23 / R2, I3=U23 / R3)


# --- simulation on load, Ydinajatus figure, Kaava graph, experiments 1-3: U = 9,0 V, R1 = 10, R2 = 30, R3 = 60 ohm ---
c = circuit(9.0, 10, 30, 60)
a["sim-R23"] = c["R23"]                                       # 1/(1/30 + 1/60) = 20 ohm
a["sim-Rkok"] = 10 + c["R23"]                                 # 30 ohm
a["sim-I1"] = c["I1"]                                         # 9,0 V : 30 ohm = 0,30 A
a["sim-U1"] = c["U1"]                                         # 10 ohm · 0,30 A = 3,0 V
a["sim-U23"] = c["U23"]                                       # 9,0 V - 3,0 V = 6,0 V
a["sim-I2"] = c["I2"]                                         # 6,0 V : 30 ohm = 0,20 A
a["sim-I3"] = c["I3"]                                         # 6,0 V : 60 ohm = 0,10 A
a["sim-VA"] = 9.0                                             # minus pole = 0 V: A (after + pole) 9,0 V
a["sim-VB"] = 9.0 - c["U1"]                                   # B and C 6,0 V
a["sim-VF"] = 0.0                                             # D, E, F 0 V
a["koe3-VA"] = 9.0 - (9.0 - c["U1"])                          # reference moved to B: V_A = 3,0 V
a["koe3-VF"] = 0.0 - (9.0 - c["U1"])                          # V_F = -6,0 V
a["koe3-UAB"] = a["koe3-VA"] - 0.0                            # U_AB = 3,0 V either way
# experiment 1: R3 varied, U, R1, R2 locked
for R3 in (30, 60, 120):
    k = circuit(9.0, 10, 30, R3)
    a[f"koe1-R3-{R3}-I1"] = k["I1"]                           # 0,36 / 0,30 / 0,2647 A
    a[f"koe1-R3-{R3}-I2"] = k["I2"]                           # 0,18 / 0,20 / 0,2118 A
    a[f"koe1-R3-{R3}-I3"] = k["I3"]                           # 0,18 / 0,10 / 0,0529 A
    a[f"koe1-R3-{R3}-sum"] = k["I2"] + k["I3"]                # = I1 in every row

# --- worked example: U = 12 V, R1 = 20, R2 = 60, R3 = 30 ohm ---
e = circuit(12.0, 20, 60, 30)
a["ex-R23"] = e["R23"]                                        # 1/(1/60 + 1/30) = 20 ohm
a["ex-Rkok"] = 20 + e["R23"]                                  # 40 ohm
a["ex-I1"] = e["I1"]                                          # 12 V : 40 ohm = 0,30 A
a["ex-U1"] = e["U1"]                                          # 20 ohm · 0,30 A = 6,0 V
a["ex-VB"] = 12.0 - e["U1"]                                   # 6,0 V
a["ex-I3"] = e["I3"]                                          # 6,0 V : 30 ohm = 0,20 A
a["ex-I2"] = e["I2"]                                          # 6,0 V : 60 ohm = 0,10 A
a["ex-check"] = e["I2"] + e["I3"]                             # 0,30 A = I1

# --- prediction 1: 0,30 A into a junction, branches 30 and 60 ohm (same voltage) ---
a["pred1-I2"] = 0.30 * 60 / (30 + 60)                         # 0,20 A
a["pred1-I3"] = 0.30 * 30 / (30 + 60)                         # 0,10 A

# --- error spotting: I2 = U / R2 with the source voltage instead of the branch voltage ---
a["virhe-wrong-I2"] = 9.0 / 30                                # 0,30 A (wrong)
a["virhe-wrong-I3"] = 9.0 / 60                                # 0,15 A (wrong): sum 0,45 A > I1 = 0,30 A

# --- transfer task: a bird on a power line, feet 4,0 cm apart, 400 A, 0,12 ohm per km ---
R_seg = 0.12 / 1000 * 0.040                                   # 0,12 ohm/km = 0,12 · 10^-3 ohm/m; 4,0 cm = 0,040 m: 4,8e-6 ohm
a["siirto-R"] = R_seg
a["siirto"] = 400 * R_seg * 1000                              # U = R I = 1,92e-3 V = 1,92 mV
a["siirto-mistake-cm"] = 400 * 0.12 / 1000 * 4.0 * 1000       # cm not converted: 192 mV
a["siirto-mistake-km"] = 400 * 0.12 * 0.040 * 1000            # ohm/km used as ohm/m: 1920 mV

# --- check 2: reference moved from the minus pole to B; V_A was 9,0 V, V_B 6,0 V ---
a["tarkistus-2"] = 9.0 - 6.0                                  # 3,0 V
a["tarkistus-2-mistake"] = 9.0 + 6.0                          # 15 V (added instead of subtracted)

print(json.dumps({k: round(v, 6) for k, v in a.items()}))
