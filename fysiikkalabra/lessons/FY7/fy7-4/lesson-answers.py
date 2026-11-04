"""Numbers of the lesson text and inquiry.json for fy7-4, computed from their data (python -I lesson-answers.py); the
exercises' answers are in answers.py. F = I l B sin α; B = μ0 I : (2π r) of a long straight wire (chapter 3).
Prints {id: number} as JSON."""
import json, math

mu0 = 4 * math.pi * 1e-7
g = 9.81
a = {}
# Worked example: loudspeaker voice coil, N = 60 turns of radius 1,3 cm in a radial field 0,95 T, current 1,5 A
N, r, B, I = 60, 1.3 * 0.01, 0.95, 1.5
a["ex-l"] = N * 2 * math.pi * r                     # wire length in the field: l = N · 2πr = 4,90 m
a["ex-F"] = I * a["ex-l"] * B                       # F = I l B (sin 90° = 1) = 6,98 N -> 7,0 N
a["ex-Bl"] = a["ex-l"] * B                          # Järkevyys: Bl = 4,66 T·m
a["ex-a-cone"] = a["ex-F"] / 0.010                  # Järkevyys: a 10 g cone would accelerate at about 700 m/s²
a["ex-G-cone"] = 0.010 * g                          # its weight 0,098 N
# Kaava: the 30° case in the text (F = I l B sin α halves at 30°)
a["kaava-sin30"] = math.sin(math.radians(30))       # 0,5
# Simulation (current balance): magnet A B = 0,080 T, l = 5,0 cm, zero reading 245,30 g
BA, l, m0 = 0.080, 0.050, 245.30
a["sim-F-6A"] = 6.0 * l * BA                        # F = 0,024 N at I = 6,0 A, α = 90°
a["sim-dm-6A"] = a["sim-F-6A"] / g * 1e3            # Δm = F / g = 2,4465 g -> 2,45 g
a["sim-read-6A"] = m0 + a["sim-dm-6A"]              # reading 247,75 g
a["sim-read-m6A"] = m0 - a["sim-dm-6A"]             # reading at −6,0 A: 242,85 g
a["sim-dm-3A"] = 3.0 * l * BA / g * 1e3             # Δm at 3,0 A: 1,22 g
a["sim-dm-30deg"] = a["sim-dm-6A"] * math.sin(math.radians(30))   # α = 30°: 1,22 g
a["sim-dm-60deg"] = a["sim-dm-6A"] * math.sin(math.radians(60))   # α = 60°: 2,12 g
a["sim-B-from-data"] = (a["sim-dm-6A"] / 1e3 * g) / (6.0 * l)     # conclusion: B = Δm g / (I l) = 0,080 T
BB = 0.12
a["sim-dm-6A-B"] = 6.0 * l * BB / g * 1e3           # magnet B: Δm = 3,67 g
# Retrieval: the field of a straight wire at twice the distance halves
a["kertaus-ratio"] = 1 / 2
# siirto: jumper cables, I = 150 A each way, centres 1,5 cm apart, 2,0 m side by side
Bc = mu0 * 150 / (2 * math.pi * 0.015)
a["siirto-B"] = Bc                                  # 2,0 · 10⁻³ T
a["siirto"] = 150 * 2.0 * Bc                        # F = I l B = 0,60 N
a["siirto-cm"] = 150 * 2.0 * mu0 * 150 / (2 * math.pi * 1.5)   # mistake: r = 1,5 m (cm not converted): 0,0060 N
a["siirto-nopi"] = 150 * 2.0 * mu0 * 150 / 0.015    # mistake: no 2π: 3,77 N
a["siirto-1m"] = 150 * 1.0 * Bc                     # mistake: l = 1 m: 0,30 N
# check-2: wire east–west, I = 4,0 A, l = 0,50 m, B = 0,20 T at α = 90° and α = 30°
a["check-F90"] = 4.0 * 0.50 * 0.20                  # 0,40 N
a["check-F30"] = 4.0 * 0.50 * 0.20 * math.sin(math.radians(30))   # 0,20 N
a["check-F30-cos"] = 4.0 * 0.50 * 0.20 * math.cos(math.radians(30))  # mistake cos: 0,35 N
# virhe (error-spotting): I = 5,0 A, l = 20 cm, B = 0,30 T, α = 30°
a["virhe-right"] = 5.0 * 0.20 * 0.30 * math.sin(math.radians(30))  # 0,15 N
a["virhe-cos"] = 5.0 * 0.20 * 0.30 * math.cos(math.radians(30))    # 0,26 N (the student's cos)
# Exit ticket 1: I = 2,0 A, l = 0,30 m, B = 0,50 T, α = 90°
a["exit-F"] = 2.0 * 0.30 * 0.50                     # 0,30 N
# misconception text: copper is not magnetic, but the force on a copper wire with 6,0 A is the same 0,024 N as above
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
