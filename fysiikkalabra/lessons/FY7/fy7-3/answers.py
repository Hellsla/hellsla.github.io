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
# Level 2: a rearrangement, a conversion or two steps
a["fy7-3-L2-01"] = 20e-3 * 0.30 / (mu0 * 1200)        # current for 20 mT in 1200 turns over 0,30 m: I = B l/(mu0 N) = 3,979 A -> 4,0 A
a["fy7-3-L2-02"] = mu0 * 6.0 / (2 * math.pi * 14e-6) * 100   # where a 6,0 A wire's field equals 14 µT: r = mu0 I/(2 pi B) = 0,0857 m -> 8,6 cm
N_wound = 25 / (math.pi * 4.0 * 0.01)                 # 25 m of wire on a tube of diameter 4,0 cm: N = L/(pi d) = 198,9 turns
a["fy7-3-L2-03"] = coil(N_wound, 2.0, 0.20) * 1e3     # then B = mu0 N I / l = 2,5e-3 T = 2,5 mT
a["fy7-3-L2-04"] = (wire(10, 0.05) + wire(10, 0.05)) * 1e6   # two wires 10 cm apart, opposite 10 A currents: midpoint fields add, 2 · 40 µT = 80 µT
# Level 3: reasoning, two ideas, an unfamiliar context
B_w = 14e-6 * math.tan(math.radians(30))              # compass turns 30°: the wire's field is perpendicular to B_h, tan 30° = B_w / B_h -> 8,083e-6 T
a["fy7-3-L3-01"] = 2 * math.pi * 5.0 * 0.01 * B_w / mu0      # I = 2 pi r B_w / mu0 = 2,02 A -> 2,0 A
N_mri = 1.5 * 1.6 / (mu0 * 400)                       # MRI coil: N = B l/(mu0 I) = 4775 turns
a["fy7-3-L3-02"] = math.pi * 1.0 * N_mri / 1000       # wire length pi d N = 15 000 m = 15 km
a["fy7-3-L3-03"] = 10 * 4.0 / (4.0 + 6.0)             # zero point between parallel wires (same direction): I1/x = I2/(d - x) -> x = d I1/(I1 + I2) = 4,0 cm
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
