"""FY5 Sovella itsenäisesti: every number of the worked solutions, recomputed from the task data.
Prints {"<task>-<part>": value} for the parts with an answer in tasks.json (and the intermediate values the solutions
quote); `python scripts/practice.py check FY5` compares them with tasks.json."""
import json, math

g = 9.81
gamma = 6.674e-11


def fit(x, y):
    mx, my = sum(x) / len(x), sum(y) / len(y)
    k = sum((a - mx) * (b - my) for a, b in zip(x, y)) / sum((a - mx) ** 2 for a in x)
    return k, my - k * mx


out = {}

# fy5-s1: the tower crane. Moments about the tower's axis, positive on the load side.
mp, rp = 4000.0, 12.0          # jib (with its counter-jib): mass and the distance of its centre of mass, load side
mv, rv = 9000.0, 10.0          # counterweight, on the other side
m1 = 2000.0                    # a)
rmax, Mmax = 40.0, 600e3       # b) the trolley's farthest position and the tower's moment limit (N·m, either way)
M_jib = mp * g * rp; M_cw = mv * g * rv
M0 = M_jib - M_cw                                      # unloaded: negative = towards the counterweight
r_bal = (mv * rv - mp * rp) / m1                       # a) the load's distance where the moments cancel
m_tip = (Mmax / g + mv * rv - mp * rp) / rmax          # b) the largest load at 40 m
dm_cw = (Mmax / g - (mv * rv - mp * rp)) / rv          # c) how much the counterweight could grow before the unloaded crane exceeds the limit
M0_plus2 = (mp * rp - (mv + 2000) * rv) * g             # c) "a couple of tonnes" more counterweight, unloaded
m_tip_big = (Mmax / g + (mv + dm_cw) * rv - mp * rp) / rmax
# d), e) slewing: one turn in T while the 2,0 t load hangs at r_bal on a 15 m rope
Tturn, Lrope = 90.0, 15.0
v = 2 * math.pi * r_bal / Tturn
an = v * v / r_bal
theta = math.degrees(math.atan(an / g))
shift = Lrope * math.tan(math.radians(theta))
S = m1 * math.sqrt(g * g + an * an)
out.update({"fy5-s1-Mjib": round(M_jib), "fy5-s1-Mcw": round(M_cw), "fy5-s1-M0": round(M0),
            "fy5-s1-a": round(r_bal, 3), "fy5-s1-b": round(m_tip, 1), "fy5-s1-dmcw": round(dm_cw, 1),
            "fy5-s1-M0plus2": round(M0_plus2), "fy5-s1-dM2": round(2000 * g * rv), "fy5-s1-mtipbig": round(m_tip_big, 1),
            "fy5-s1-v": round(v, 4), "fy5-s1-an": round(an, 5), "fy5-s1-e": round(theta, 4), "fy5-s1-shift": round(shift, 4),
            "fy5-s1-S": round(S), "fy5-s1-G": round(m1 * g), "fy5-s1-Fn": round(m1 * an, 1)})

# fy5-s2: Jupiter's moons (NASA JPL mean orbital radii and periods, rounded)
moons = [("Amalthea", 181.4e6, 0.4982), ("Io", 421.8e6, 1.769), ("Europa", 671.1e6, 3.551),
         ("Ganymedes", 1070e6, 7.155), ("Kallisto", 1883e6, 16.69)]   # r in m, T in d
X, Y = [], []
for name, r, Td in moons:
    T = Td * 86400
    vv = 2 * math.pi * r / T
    X.append(1 / r); Y.append(vv * vv)
    out[f"fy5-s2-v-{name}"] = round(vv)
    out[f"fy5-s2-x-{name}"] = round(1e9 / r, 3)          # 1/r in 10^-9 1/m
    out[f"fy5-s2-y-{name}"] = round(vv * vv / 1e8, 3)    # v² in 10^8 m²/s²
k0 = sum(a * b for a, b in zip(X, Y)) / sum(a * a for a in X)   # least-squares line through the origin
gM_read = 6.35e8 / 5.0e-9                                # the slope read from the model line: (5,0·10⁻⁹ 1/m; 6,35·10⁸ m²/s²)
M = gM_read / gamma
out.update({"fy5-s2-slope-fit": round(k0 / 1e17, 4), "fy5-s2-gM": round(gM_read / 1e17, 4), "fy5-s2-b": float(f"{M:.4g}"),
            "fy5-s2-M-fit": float(f"{k0 / gamma:.4g}")})
Trot = 9.93 * 3600                                        # c) Jupiter's rotation period
r_sync = (gM_read * Trot ** 2 / (4 * math.pi ** 2)) ** (1 / 3)
RJ = 71500e3
out.update({"fy5-s2-Trot": round(Trot), "fy5-s2-c": round(r_sync / 1e3, -2), "fy5-s2-c-h": round((r_sync - RJ) / 1e3, -2),
            "fy5-s2-c-v": round(2 * math.pi * r_sync / Trot), "fy5-s2-c-r3": float(f"{gM_read * Trot ** 2 / (4 * math.pi ** 2):.4g}")})

# fy5-s3: the spring experiment (simulated: k = 20,0 N/m, a third of the spring's 45 g moving with the load, timing noise)
ms = [0.100, 0.150, 0.200, 0.250, 0.300, 0.350]           # kg
t10 = [4.74, 5.73, 6.50, 7.25, 7.86, 8.51]                # s, ten periods
T2 = [(t / 10) ** 2 for t in t10]
for m_, t2 in zip(ms, T2): out[f"fy5-s3-T2-{int(m_ * 1000)}"] = round(t2, 4)
k_fit, b_fit = fit(ms, T2)
# the slope as read in the solution from two far-apart points of the drawn line: (0,100 kg; 0,226 s²) and (0,350 kg; 0,722 s²)
slope = (0.722 - 0.226) / (0.350 - 0.100)
k_dyn = 4 * math.pi ** 2 / slope
k_stat = 0.200 * g / 0.098                                # c) 200 g stretched the spring 9,8 cm
dt = 0.2 / 10                                             # c) hand timing ±0,2 s over ten periods
out.update({"fy5-s3-fit-slope": round(k_fit, 4), "fy5-s3-fit-icpt": round(b_fit, 4), "fy5-s3-slope": round(slope, 4),
            "fy5-s3-b": round(k_dyn, 3), "fy5-s3-kstat": round(k_stat, 3), "fy5-s3-icpt-read": round(0.226 - slope * 0.100, 4),
            "fy5-s3-dT": dt, "fy5-s3-dT2-rel": round(2 * dt / 0.474, 4), "fy5-s3-meff": round((0.226 - slope * 0.100) / slope, 4),
            "fy5-s3-k-origin": round(4 * math.pi ** 2 * sum(a * a for a in ms) / sum(a * b for a, b in zip(ms, T2)), 3)})
A, m_d = 0.050, 0.250                                     # d)
vmax = A * math.sqrt(k_dyn / m_d)
out.update({"fy5-s3-d": round(vmax, 4), "fy5-s3-d-E": round(0.5 * k_dyn * A * A, 5)})

# fy5-s4: the organ pipe
T_sig = 20.0e-3 / 5                                       # a) five repeats of the signal in 20,0 ms
f = 1 / T_sig
v20 = 343.0
L = v20 / (2 * f)                                         # b) open at both ends, fundamental: L = λ/2
v8 = v20 - 0.6 * (20.0 - 8.0)                             # c) 0,6 m/s per degree
f8 = v8 / (2 * L)
df = f - f8
L4, r4, r2 = 88.0, 4.0, 2.0                               # d) level at 4,0 m, organist at 2,0 m
Lorg = L4 + 10 * math.log10((r4 / r2) ** 2)
nsteps = (Lorg - 85) / 3
t_all = 8 / 2 ** nsteps
I4 = 1e-12 * 10 ** (L4 / 10); P = I4 * 4 * math.pi * r4 ** 2
out.update({"fy5-s4-a": round(f, 2), "fy5-s4-T": T_sig, "fy5-s4-b": round(L, 4), "fy5-s4-lambda": round(2 * L, 3),
            "fy5-s4-v8": round(v8, 2), "fy5-s4-f8": round(f8, 2), "fy5-s4-c": round(df, 3), "fy5-s4-f2": round(2 * f, 1),
            "fy5-s4-Lorg": round(Lorg, 2), "fy5-s4-n": round(nsteps, 3), "fy5-s4-d": round(t_all, 3), "fy5-s4-P": round(P, 4)})
print(json.dumps(out))
