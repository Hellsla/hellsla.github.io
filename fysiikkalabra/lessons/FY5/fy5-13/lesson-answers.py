"""Numbers of the lesson text and inquiry.json for fy5-13, computed from their data (python -I lesson-answers.py); the
exercises' answers are in answers.py. Standing waves: a string fixed at both ends and a pipe open at both ends have
f_n = n v / (2L), a pipe closed at one end f_n = n v / (4L) with n odd; v = f λ; neighbouring nodes λ/2 apart.
The simulation's model is reproduced here: the steady state of a driven, weakly damped wave on [0, L] with the complex
wave number k = 2πf/v − iα, α = 0,06 / L, the drive at x = 0 (amplitude a = 1,0 mm) and, with s = L − x,
string U = a sin(ks)/sin(kL), open pipe U = a cos(ks)/sin(kL), closed pipe U = a sin(ks)/cos(kL); the largest
deviation A = max |U| over 301 points. Prints {id: number} as JSON."""
import json, cmath, math

a = {}
V_AIR = 340.0                                             # speed of sound used in the whole chapter, m/s


def response(mode, f, L, v):
    """A (mm) and the number of nodes of the sim's steady state, as sim.js computes them."""
    k = 2 * math.pi * f / v - 1j * 0.06 / L
    env = []
    for j in range(301):
        s = L - L * j / 300
        if mode == "kieli": U = cmath.sin(k * s) / cmath.sin(k * L)
        elif mode == "avoin": U = cmath.cos(k * s) / cmath.sin(k * L)
        else: U = cmath.sin(k * s) / cmath.cos(k * L)
        env.append(abs(U))
    A = max(env)
    nodes = 0
    for j in range(301):
        left = env[j - 1] if j > 0 else math.inf
        right = env[j + 1] if j < 300 else math.inf
        if env[j] < left and env[j] <= right and env[j] < 0.15 * A: nodes += 1
    return A, nodes


# Koe 1: string, L = 0,60 m, v = 120 m/s; f1 = v/(2L) = 100 Hz, then 200 and 300 Hz
L1, v1 = 0.60, 120.0
a["koe1-f1"] = v1 / (2 * L1)                              # 100 Hz
for f in (50, 75, 95, 100, 105, 150, 200, 250, 300):
    A, nd = response("kieli", f, L1, v1)
    a[f"koe1-A-{f}"] = A                                  # 16,7 mm at 100, 200, 300 Hz; about 1–3 mm between
    a[f"koe1-nodes-{f}"] = nd                             # n + 1 nodes at the n-th eigenfrequency: 2, 3, 4
    a[f"koe1-lambda-{f}"] = v1 / f                        # λ = v/f: 1,20 m, 0,60 m, 0,40 m at the eigenfrequencies
# Koe 2: pipe closed at one end, L = 0,85 m, v = 340 m/s; f1 = v/(4L) = 100 Hz, then 300 and 500 Hz (odd only)
L2 = 0.85
a["koe2-f1"] = V_AIR / (4 * L2)                           # 100 Hz
for f in (100, 150, 200, 250, 300, 400, 500):
    A, nd = response("suljettu", f, L2, V_AIR)
    a[f"koe2-A-{f}"] = A                                  # 16,7 mm at 100, 300, 500 Hz; 200 and 400 Hz stay about 1 mm
    a[f"koe2-nodes-{f}"] = nd
# the same pipe open at both ends (optional comparison): f1 = v/(2L) = 200 Hz, 400 Hz, 600 Hz
a["avoin-f1"] = V_AIR / (2 * L2)
for f in (200, 400):
    a[f"avoin-A-{f}"] = response("avoin", f, L2, V_AIR)[0]
# sim on load: string, f = 50 Hz, L = 0,60 m, v = 120 m/s
a["sim-load-A"], a["sim-load-nodes"] = response("kieli", 50, 0.60, 120.0)
a["sim-load-lambda"] = 120.0 / 50                         # 2,40 m
# the peak height is 1/sinh(αL) for every mode: 1/sinh(0,06) = 16,7 (A in mm with a = 1,0 mm)
a["peak-gain"] = 1 / math.sinh(0.06)

# Hook / prediction 1: a rope with one loop at f1; two loops need 2 f1 (λ halves, v unchanged)
# Prediction 2: closed pipe f1 = 100 Hz, next eigenfrequency 3 f1 = 300 Hz (wrong 200 Hz is the string's 2 f1)
a["ennuste2-next"] = 3 * a["koe2-f1"]

# Worked example: guitar A string, L = 0,650 m, f1 = 110 Hz; v = 2 L f1; pressed to f1' = 165 Hz: L' = v/(2 f1')
v_ex = 2 * 0.650 * 110
a["esim-v"] = v_ex                                        # 143 m/s
a["esim-L2"] = v_ex / (2 * 165)                           # 0,4333 m
a["esim-ratio"] = 110 / 165                               # L'/L = 2/3

# Misconception: λ1 = 2L, not L; 1,20 m string -> λ1 = 2,40 m
a["virhe-lambda"] = 2 * 1.20

# Error spotting: closed organ pipe L = 0,85 m written f1 = v/(2L) = 200 Hz; right v/(4L) = 100 Hz
a["etsi-wrong"] = V_AIR / (2 * 0.85)
a["etsi-right"] = V_AIR / (4 * 0.85)

# Transfer: didgeridoo, closed at the lips, L = 1,50 m: f1 = v/(4L) = 56,7 Hz; next eigenfrequency 3 f1 = 170 Hz
f1_d = V_AIR / (4 * 1.50)
a["siirto-f1"] = f1_d
a["siirto"] = 3 * f1_d                                    # 170 Hz
a["siirto-m-2f1"] = 2 * f1_d                              # mistake: the string pattern 2 f1 = 113 Hz
a["siirto-m-open2"] = 2 * V_AIR / (2 * 1.50)              # mistake: open pipe f2 = 227 Hz
a["siirto-m-open1"] = V_AIR / (2 * 1.50)                  # mistake: open pipe f1 = 113 Hz (same as 2 f1)

# Check 2: closed pipe, L = 0,60 m, third eigenfrequency: L = 3λ/4 -> λ = 4L/3 = 0,80 m
a["tark2"] = 4 * 0.60 / 3
a["tark2-m-open"] = 2 * 0.60 / 3                          # mistake: the string/open-pipe rule λ = 2L/3, 0,40 m
a["tark2-m-4L"] = 4 * 0.60                                # mistake: the fundamental's λ = 4L, 2,40 m
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
