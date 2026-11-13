"""Every answer in exercises.json for fy7-2, computed from the task data (python -I answers.py).
Magnetic force F = qvB sin α; circular path qvB = mv²/r so r = mv/(qB); velocity selector v = E/B; acceleration from
rest qU = ½mv²; uniform field between plates E = U/d (FY6). Constants as the tasks give them.
Prints {exercise id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json, math

e, mp, me, md, ma, u = 1.602e-19, 1.673e-27, 9.109e-31, 3.344e-27, 6.645e-27, 1.661e-27
a = {}
# Level 1: one formula, values given
a["fy7-2-L1-01"] = e * 3.0e5 * 0.25 / 1e-14            # proton beam: F = qvB = 1,2015e-14 N -> 1,2 (unit 10^-14 N)
a["fy7-2-L1-02"] = me * 2.0e6 / (e * 1.5e-3) * 1000     # electron in 1,5 mT: r = mv/(qB) = 7,58e-3 m = 7,6 mm
a["fy7-2-L1-03"] = 4.0e4 / 0.080 / 1000                 # velocity selector: v = E/B = 5,0e5 m/s = 500 km/s
a["fy7-2-L1-04"] = 2 * e * 1500 / 1e-16                 # alpha particle through 1500 V: W = qU = 4,806e-16 J -> 4,8 (10^-16 J)
a["fy7-2-L1-05"] = e * 5.0e6 * 0.40 * math.sin(math.radians(30)) / 1e-13   # F = qvB sin 30° = 1,602e-13 N -> 1,6 (10^-13 N)
# Level 2: two steps, a conversion or a rearrangement
v21 = math.sqrt(2 * e * 500 / mp)                       # proton from rest through 500 V: v = sqrt(2qU/m) = 3,095e5 m/s
a["fy7-2-L2-01"] = mp * v21 / (e * 0.050) * 100         # then B = 0,050 T: r = mv/(qB) = 0,0646 m = 6,5 cm
a["fy7-2-L2-02"] = e * 0.60 * 0.12 / md / 1000          # deuteron, r = 12 cm, B = 0,60 T: v = qBr/m = 3,449e6 m/s = 3,4e3 km/s
E23 = 600 / 0.020                                       # selector plates 600 V, 2,0 cm apart: E = U/d = 3,0e4 V/m
a["fy7-2-L2-03"] = E23 / 0.15 / 1000                    # v = E/B = 2,0e5 m/s = 200 km/s
a["fy7-2-L2-04"] = mp * 9.81 / (e * 50e-6) * 1000       # qvB = mg in Earth's 50 µT: v = mg/(qB) = 2,05e-3 m/s = 2,0 mm/s
# Level 3: reasoning or an unfamiliar context
r12 = 0.250                                             # C-12+ ions on r = 25,0 cm; same U, same q, so r = sqrt(2mU/q)/B ∝ sqrt(m)
r14 = r12 * math.sqrt(14.0 / 12.0)                      # C-14+: 0,27003 m
a["fy7-2-L3-01"] = 2 * (r14 - r12) * 100                # the spots are diameters apart: 2(r14 − r12) = 4,0 cm
a["fy7-2-L3-02"] = e * 1.50 / (2 * math.pi * mp) / 1e6  # cyclotron: T = 2πr/v = 2πm/(qB), f = qB/(2πm) = 22,9 MHz
a["fy7-2-L3-03"] = math.sqrt((ma / (2 * e)) / (mp / e)) # same U: r ∝ sqrt(m/q); r_α / r_p = sqrt(6,645/(2 · 1,673)) = 1,41
# Exercise bank additions (teacher 2026-11-04): L1-06 and L2-07 are multiple choice (no number)
a["fy7-2-L1-07"] = me * 3.0e6 / (e * 0.040) * 1000      # electron on r = 4,0 cm: B = mv/(qr) = 4,264e-4 T = 0,43 mT
a["fy7-2-L1-08"] = 2 * math.pi * me / (e * 0.020) * 1e9   # T = 2πm/(qB) = 1,786e-9 s = 1,8 ns (v cancels)
# L2-08 is a force-diagram choice (no number): electron up at 3,0e6 m/s in 0,50 mT out of the page: F_m = |q| v B = 2,4e-16 N to the left
#   (v x B points right for a positive charge), weight m g = 8,9e-30 N negligible; option C (pick-vasen)
# L2-05 (example data, ion beam in a vacuum chamber, v = 2,0e5 m/s, B = 0,050 T): track 1 r = 4,1 cm up (positive), 2 down (negative) 4,2 cm, 3 up 8,4 cm
a["fy7-2-L2-05"] = 0.041 * 0.050 / 2.0e5 / 1e-8         # m/q = rB/v = 1,025e-8 kg/C -> 1,0 (unit 10^-8 kg/C); proton m/e = 1,044e-8
# L2-06 (example data, magnesium-like): hits d = 19,2 / 20,1 / 20,7 cm, counts 7890 / 1000 / 1110; m ∝ d, so m_B = 25,1 u and m_C = 25,9 u
N26 = [7890, 1000, 1110]
a["fy7-2-L2-06"] = N26[0] / sum(N26) * 100              # abundance of the lightest isotope 7890/10000 = 78,9 %
# L3-04 (example data): r² = 2m/(qB²) · U; least-squares line through the origin
sp = [(200, 4.9), (400, 6.8), (600, 8.5), (800, 9.8), (1000, 10.8)]   # (U in V, r in cm)
k34 = sum(U * r * r for U, r in sp) / sum(U * U for U, r in sp) * 1e-4   # slope 0,1182 cm²/V = 1,182e-5 m²/V
a["fy7-2-L3-04"] = round(e * 0.200**2 * k34 / 2 / u, 3)  # m = qB²k/2 = 3,79e-26 kg = 22,8 u (sodium-23)
# L3-05 (cyclotron, B = 1,00 T): v = qBR/m, E_k = ½mv², crossings n = E_k/(qU), two per revolution, T = 2πm/(qB)
v35 = e * 1.00 * 0.20 / mp                              # 1,92e7 m/s (6,4 % of c)
n35 = round(0.5 * mp * v35**2 / (e * 60e3))             # 31,9 -> 32 crossings = 16 revolutions
a["fy7-2-L3-05"] = round(n35 / 2 * 2 * math.pi * mp / (e * 1.00) / 1e-6, 2)   # t = 16 · 65,6 ns = 1,05 µs
# Added 2026-11-13: L1-09 MAFY table task (electron mass from the table, m_e = 9,109 383 7e-31 kg; e given): r = mv/(|q|B)
a["fy7-2-L1-09"] = 9.1093837e-31 * 4.0e6 / (e * 0.80e-3) * 100   # v = 4,0e6 m/s, B = 0,80 mT: r = 2,843e-2 m = 2,8 cm
# L2-09 figure task (fy7-2/r-points): read r = 15,7 cm at v = 1,5e6 m/s, B = 0,20 T, q = e; m = |q|Br/v
a["fy7-2-L2-09"] = e * 0.20 * 0.157 / 1.5e6 / 1e-27     # 3,35e-27 kg (the figure's particle is a deuteron, 3,344e-27 kg)
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
