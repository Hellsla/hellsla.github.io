"""FY9 fy9-sahkokentta, Tehtävät: every number of the worked solutions, recomputed from the task data.
Prints {"<task>-<part>[-<name>]": value} for the parts with an answer in tasks.json and the intermediate values the
solutions quote; `python scripts/practice.py check units/fy9-sahkokentta` compares them with tasks.json."""
import json, math

g = 9.81
k = 8.988e9                            # N m^2 / C^2
e = 1.602e-19                          # C
eps0 = 8.854e-12                       # F/m


def fit(x, y):
    mx, my = sum(x) / len(x), sum(y) / len(y)
    kk = sum((a - mx) * (b - my) for a, b in zip(x, y)) / sum((a - mx) ** 2 for a in x)
    return kk, my - kk * mx


out = {}
S = "fy9-sahkokentta"

# s1: two equal charged balls on threads from one point (example data)
m1, L1, r1 = 0.50e-3, 0.400, 0.080                    # kg, m, m (centre to centre)
sin_a = (r1 / 2) / L1
alpha = math.asin(sin_a)
F1 = m1 * g * math.tan(alpha)                          # N, the electric force = horizontal part of the thread force
q1 = r1 * math.sqrt(F1 / k)                            # C, each ball
n1 = q1 / e
F1c = k * q1 * (q1 / 2) / r1 ** 2                      # c: q and q/2 at the same distance
# d: the new equilibrium, small angles (sin = tan): k q q/2 / r^2 = m g r / (2 L)  ->  r^3 = r1^3 / 2
r_new = r1 / 2 ** (1 / 3)
def _bal(r): return k * q1 * q1 / 2 / r ** 2 - m1 * g * math.tan(math.asin(r / 2 / L1))
lo, hi = 0.03, 0.08
for _ in range(80):
    mid = (lo + hi) / 2
    lo, hi = (mid, hi) if _bal(mid) > 0 else (lo, mid)
out.update({f"{S}-s1-a": round(F1 * 1000, 4), f"{S}-s1-alpha": round(math.degrees(alpha), 2), f"{S}-s1-tan": round(math.tan(alpha), 4),
            f"{S}-s1-mg": round(m1 * g * 1000, 4), f"{S}-s1-T": round(m1 * g / math.cos(alpha) * 1000, 3),
            f"{S}-s1-b": round(q1 * 1e9, 3), f"{S}-s1-b-n": round(n1 / 1e11, 3),
            f"{S}-s1-c": round(F1c * 1000, 4), f"{S}-s1-d": round(r_new * 100, 3), f"{S}-s1-d-exact": round(lo * 100, 3)})

# s2: a demonstration plate capacitor (example data); the glass from the table of fy6-13
a2, d2, U2, er_glass = 0.250, 3.00e-3, 4.50e3, 5.6
A2 = a2 * a2
C2 = eps0 * A2 / d2
Q2 = C2 * U2
W2 = 0.5 * C2 * U2 ** 2
E2 = U2 / d2
C2g = er_glass * C2
U2g = Q2 / C2g
W2g = 0.5 * Q2 * U2g
out.update({f"{S}-s2-a-C": round(C2 * 1e12, 2), f"{S}-s2-a-Q": round(Q2 * 1e6, 4), f"{S}-s2-A": A2,
            f"{S}-s2-b-W": round(W2 * 1000, 4), f"{S}-s2-b-E": round(E2 / 1e6, 3), f"{S}-s2-b-Umax": round(3e6 * d2 / 1000, 2),
            f"{S}-s2-c-C": round(C2g * 1e12, 1), f"{S}-s2-c-U": round(U2g, 1), f"{S}-s2-c-W": round(W2g * 1000, 4),
            f"{S}-s2-c-loss": round((W2 - W2g) * 1000, 4), f"{S}-s2-c-Eg": round(U2g / d2 / 1e6, 4)})

# s3: capacitance against plate distance (invented data: eps0 A / d + 22 pF of the leads, noise about 1 %)
A3 = 0.200 * 0.200
D3 = [1.0, 1.5, 2.0, 3.0, 4.0, 5.0, 6.0]                # mm
C3 = [375, 260, 199, 140, 109, 93, 82]                  # pF
X3 = [1 / d for d in D3]                                # 1/mm
k3, b3 = fit(X3, C3)
# read in the solution from two far-apart points of the drawn line
xa, xb = 0.20, 1.00
ya, yb = round(k3 * xa + b3), round(k3 * xb + b3)
k_read = (yb - ya) / (xb - xa)                          # pF mm
b_read = ya - k_read * xa
eps_read = k_read * 1e-12 * 1e-3 / A3
d_pred = k_read / (500 - b_read)                        # mm, where the line gives 500 pF
out.update({f"{S}-s3-x": [round(v, 3) for v in X3], f"{S}-s3-k-fit": round(k3, 2), f"{S}-s3-b-fit": round(b3, 2),
            f"{S}-s3-ya": ya, f"{S}-s3-yb": yb, f"{S}-s3-k": round(k_read, 1), f"{S}-s3-b0": round(b_read, 1),
            f"{S}-s3-c": round(eps_read * 1e12, 4), f"{S}-s3-c-diff": round(100 * (eps_read - eps0) / eps0, 2),
            f"{S}-s3-c-model": round(eps0 * A3 * 1e15, 2),
            f"{S}-s3-d": round(b_read, 1), f"{S}-s3-d-pred": round(d_pred, 3),
            f"{S}-s3-d-ratio": round(C3[2] / C3[0], 3)})

# s4: a power line, a bird and a fishing rod (word task; the numbers its model answer quotes)
I4, R4_per_km, foot = 100.0, 0.30, 0.05                 # A, ohm/km, m
U_feet = I4 * R4_per_km / 1000 * foot
U_earth = 20e3 / math.sqrt(3)                          # V, one conductor to earth (20 kV is between the phase conductors)
d_arc = 12e3 / 3e6                                      # m, the uniform-field estimate of the gap that breaks down (12 kV)
out.update({f"{S}-s4-feet-mV": round(U_feet * 1000, 3), f"{S}-s4-U-earth-kV": round(U_earth / 1000, 2),
            f"{S}-s4-gap-mm": round(d_arc * 1000, 2), f"{S}-s4-I-body": round(12e3 / 10e3, 2)})

# s5: a solar panel report (invented data from a ten-cell panel model, area 60 cm^2)
R5 = [10, 20, 25, 30, 40, 60, 100]                      # ohm
U5 = [2.10, 4.17, 4.97, 5.36, 5.67, 5.86, 5.97]         # V
I5 = [210, 209, 199, 179, 142, 98, 60]                  # mA
P5 = [u * i / 1000 for u, i in zip(U5, I5)]
Pmax = max(P5)
A5, G5 = 60e-4, 1000.0
eta = Pmax / (G5 * A5)
P_student = 6.10 * 0.210
out.update({f"{S}-s5-P": [round(p, 3) for p in P5], f"{S}-s5-a-P": round(Pmax, 4), f"{S}-s5-a-eta": round(100 * eta, 2),
            f"{S}-s5-student-P": round(P_student, 3), f"{S}-s5-student-eta": round(100 * P_student / (G5 * A5), 2),
            f"{S}-s5-light": round(G5 * A5, 2), f"{S}-s5-R-check": [round(u / i * 1000, 1) for u, i in zip(U5, I5)]})

# s6: an ion thruster (example data; the cross-module task with FY4 momentum)
U6, d6, I6, m_ion, M6 = 1100.0, 1.0e-3, 1.60, 2.180e-25, 650.0
v6 = math.sqrt(2 * e * U6 / m_ion)
E6 = U6 / d6
N6 = I6 / e                                             # ions per second
mdot = N6 * m_ion                                       # kg/s
F6 = mdot * v6
a6 = F6 / M6
t6 = 30 * 24 * 3600
dv6 = a6 * t6
mXe = mdot * t6
P6 = U6 * I6
Pk = 0.5 * mdot * v6 ** 2
out.update({f"{S}-s6-a": round(v6 / 1000, 3), f"{S}-s6-E": round(E6 / 1e6, 2), f"{S}-s6-Ek-eV": U6,
            f"{S}-s6-N": round(N6 / 1e18, 3), f"{S}-s6-mdot": round(mdot * 1e6, 3),
            f"{S}-s6-b": round(F6 * 1000, 2), f"{S}-s6-c-a": round(a6 * 1e4, 3),
            f"{S}-s6-c-dv": round(dv6, 1), f"{S}-s6-c-m": round(mXe, 3), f"{S}-s6-t": t6,
            f"{S}-s6-d-P": round(P6, 1), f"{S}-s6-d-Pk": round(Pk, 1), f"{S}-s6-d-F2Pv": round(2 * P6 / v6 * 1000, 2)})

print(json.dumps(out))
