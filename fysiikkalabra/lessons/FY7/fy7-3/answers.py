"""Every answer in exercises.json for fy7-3, computed from the task data (python -I answers.py).
Straight long wire B = mu0 I / (2 pi r); long coil (inside, away from the ends) B = mu0 N I / l; mu0 = 4 pi 10^-7 Vs/(Am).
Fields of several wires add as vectors (here along one line, so with signs). Prints {exercise id: number} as JSON."""
import json, math

mu0 = 4 * math.pi * 1e-7                       # Vs/(Am)
wire = lambda I, r: mu0 * I / (2 * math.pi * r)   # T
coil = lambda N, I, l: mu0 * N * I / l             # T
a = {}
# Level 1: one formula, values given
a["fy7-3-L1-01"] = wire(12, 3.0 * 0.01) * 1e6         # 12 A at 3,0 cm: 2e-7 · 12 / 0,030 = 8,0e-5 T = 80 µT
a["fy7-3-L1-02"] = coil(500, 1.2, 25 * 0.01) * 1e3    # 500 turns, 1,2 A, 25 cm: 3,016e-3 T -> 3,0 mT
a["fy7-3-L1-03"] = wire(800, 16) * 1e6                # one overhead conductor 800 A, 16 m below: 1,0e-5 T = 10 µT
a["fy7-3-L1-04"] = wire(2.5, 5.0 * 0.001) * 1e3       # 2,5 A at 5,0 mm: 1,0e-4 T = 0,10 mT
a["fy7-3-L1-05"] = coil(300, 0.40, 15 * 0.01) * 1e3   # 300 turns, 0,40 A, 15 cm: 1,005e-3 T -> 1,0 mT
a["fy7-3-L1-07"] = coil(1000, 0.75, 0.20) * 1e3       # 400 -> 1000 turns on the same 20 cm, 0,75 A: 4,712e-3 T -> 4,7 mT
a["fy7-3-L1-08"] = coil(250, 2.0, 0.10) / wire(2.0, 2.0 * 0.01)   # coil 6,283 mT / wire 20 uT = 314 -> 310 times
# (fy7-3-L1-06 is multiple choice: no number)
# Level 2: a rearrangement, a conversion or two steps
a["fy7-3-L2-01"] = 20e-3 * 0.30 / (mu0 * 1200)        # current for 20 mT in 1200 turns over 0,30 m: I = B l/(mu0 N) = 3,979 A -> 4,0 A
a["fy7-3-L2-02"] = mu0 * 6.0 / (2 * math.pi * 14e-6) * 100   # where a 6,0 A wire's field equals 14 µT: r = mu0 I/(2 pi B) = 0,0857 m -> 8,6 cm
N_wound = 25 / (math.pi * 4.0 * 0.01)                 # 25 m of wire on a tube of diameter 4,0 cm: N = L/(pi d) = 198,9 turns
a["fy7-3-L2-03"] = coil(N_wound, 2.0, 0.20) * 1e3     # then B = mu0 N I / l = 2,5e-3 T = 2,5 mT
a["fy7-3-L2-04"] = (wire(10, 0.05) + wire(10, 0.05)) * 1e6   # two wires 10 cm apart, opposite 10 A currents: midpoint fields add, 2 · 40 µT = 80 µT
pts = [(0.0, 0.05), (0.5, 1.31), (1.0, 2.60), (1.5, 3.80), (2.0, 5.12), (2.5, 6.31), (3.0, 7.60)]   # data of L2-05 (I in A, B in mT)
mI = sum(p[0] for p in pts) / len(pts); mB = sum(p[1] for p in pts) / len(pts)
slope = sum((i - mI) * (b - mB) for i, b in pts) / sum((i - mI) ** 2 for i, b in pts)   # least squares 2,512 mT/A
a["fy7-3-L2-05"] = slope * 1e-3 * 0.300 / 600 * 1e6    # mu0 = A l / N = 1,257e-6 Vs/(Am) -> 1,26 in uVs/(Am)
Br = [r * b for r, b in [(1.0, 161), (2.0, 79), (4.0, 41)]]   # data of L2-06: B r in uT cm = 161, 158, 164 (constant -> B ~ 1/r)
I_w = (sum(Br) / 3) * 1e-6 * 1e-2 / (mu0 / (2 * math.pi))     # I = 2 pi (B r) / mu0 = 8,05 A
a["fy7-3-L2-06"] = wire(I_w, 3.0 * 0.01) * 1e6        # 3,0 cm: 53,7 uT -> 54 uT
# L2-06 d): B at 0,50 cm = 161 uT cm / 0,50 cm = 322 uT -> 320 uT (not the answer box)
# (fy7-3-L2-07 is multiple choice: no number)
# Level 3: reasoning, two ideas, an unfamiliar context
B_w = 14e-6 * math.tan(math.radians(30))              # compass turns 30°: the wire's field is perpendicular to B_h, tan 30° = B_w / B_h -> 8,083e-6 T
a["fy7-3-L3-01"] = 2 * math.pi * 5.0 * 0.01 * B_w / mu0      # I = 2 pi r B_w / mu0 = 2,02 A -> 2,0 A
N_mri = 1.5 * 1.6 / (mu0 * 400)                       # MRI coil: N = B l/(mu0 I) = 4775 turns
a["fy7-3-L3-02"] = math.pi * 1.0 * N_mri / 1000       # wire length pi d N = 15 000 m = 15 km
a["fy7-3-L3-03"] = 10 * 4.0 / (4.0 + 6.0)             # zero point between parallel wires (same direction): I1/x = I2/(d - x) -> x = d I1/(I1 + I2) = 4,0 cm
tan_pts = [(1.0, 17.5), (2.0, 32.0), (3.0, 43.5), (4.0, 51.0), (5.0, 57.5)]   # data of L3-04 (I in A, alpha in degrees)
k_c = sum(i * math.tan(math.radians(al)) for i, al in tan_pts) / sum(i * i for i, al in tan_pts)   # tan(alpha) = k I through the origin: 0,3127 1/A
a["fy7-3-L3-04"] = mu0 / (2 * math.pi * 0.040 * k_c) * 1e6   # k = mu0/(2 pi h B_h) -> B_h = 16,0 uT
R_w = 1.7e-8 * 30 / (math.pi * (0.25e-3) ** 2)        # L3-05: R = rho L / A = 2,597 ohm
N_s = 30 / (math.pi * 0.030)                          # turns of 0,030 m diameter: 318,3
a["fy7-3-L3-05"] = coil(N_s, 6.0 / R_w, N_s * 0.55e-3) * 1e3   # I = U/R = 2,31 A, l = N 0,55 mm = 0,175 m: B = 5,28 mT -> 5,3 mT
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
