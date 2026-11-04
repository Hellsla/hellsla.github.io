"""FY9 fy9-voimat, Tehtävät: every number of the worked solutions, recomputed from the task data.
Prints {"<task>-<part>[-<name>]": value} for the parts with an answer in tasks.json and the intermediate values the
solutions quote; `python scripts/practice.py check units/fy9-voimat` compares them with tasks.json."""
import json, math

g = 9.81
rad = math.radians
out = {}


def fit(x, y):
    mx, my = sum(x) / len(x), sum(y) / len(y)
    k = sum((a - mx) * (b - my) for a, b in zip(x, y)) / sum((a - mx) ** 2 for a in x)
    return k, my - k * mx


# s1: a boat winched up a slipway (example data)
m, al, mu, mu0 = 280.0, 14.0, 0.25, 0.35
G = m * g
Gx, Gy = G * math.sin(rad(al)), G * math.cos(rad(al))
T_const = Gx + mu * Gy                                # constant speed: T = mg sin a + mu mg cos a
a_start = 0.20
T_start = T_const + m * a_start                       # speeding up 0,20 m/s^2 (still sliding: kinetic friction)
alpha0 = math.degrees(math.atan(mu0))                 # the boat slides off by itself above this angle
out.update({"fy9-voimat-s1-G": round(G, 1), "fy9-voimat-s1-Gx": round(Gx, 1), "fy9-voimat-s1-N": round(Gy, 1),
            "fy9-voimat-s1-Fmu": round(mu * Gy, 1), "fy9-voimat-s1-b": round(T_const, 1),
            "fy9-voimat-s1-Tstart": round(T_start, 1), "fy9-voimat-s1-Fmax": round(mu0 * Gy, 1),
            "fy9-voimat-s1-c": round(alpha0, 2), "fy9-voimat-s1-tan": round(math.tan(rad(al)), 4)})

# s2: a snowmobile tows two sleds in a row on level snow (example data)
mA, mB, mu2, a2 = 120.0, 80.0, 0.10, 0.50
T2 = mB * (a2 + mu2 * g)                              # the rear rope: B alone
T1 = (mA + mB) * (a2 + mu2 * g)                       # the front rope: A and B together
out.update({"fy9-voimat-s2-b": round(T2, 2), "fy9-voimat-s2-c": round(T1, 2), "fy9-voimat-s2-FmuB": round(mu2 * mB * g, 2),
            "fy9-voimat-s2-FmuA": round(mu2 * mA * g, 2), "fy9-voimat-s2-ratio": round(T2 / T1, 3)})

# s3: a cart pulled with a force sensor on a level track (invented data: a = (F - 0,24 N) / 0,850 kg plus noise)
F = [0.40, 0.60, 0.80, 1.00, 1.20, 1.40, 1.60]        # N
A = [0.20, 0.41, 0.67, 0.88, 1.14, 1.35, 1.61]        # m/s^2
k, b = fit(F, A)
M = 1 / k
F0 = -b / k                                           # the x intercept: the friction force
# read in the solution from two far-apart points of the drawn line: (0,40 N; 0,19 m/s^2) and (1,60 N; 1,60 m/s^2)
k_read = (1.60 - 0.19) / (1.60 - 0.40)
M_read = 1 / k_read
F0_read = 0.40 - 0.19 / k_read
mu3 = F0 / (M * g)
out.update({"fy9-voimat-s3-k": round(k, 4), "fy9-voimat-s3-b0": round(b, 4), "fy9-voimat-s3-kread": round(k_read, 4),
            "fy9-voimat-s3-b-M": round(M_read, 3), "fy9-voimat-s3-b-F": round(F0_read, 3), "fy9-voimat-s3-Mfit": round(M, 4),
            "fy9-voimat-s3-F0fit": round(F0, 4), "fy9-voimat-s3-d": round(F0_read / (M_read * g), 4),
            "fy9-voimat-s3-mufit": round(mu3, 4), "fy9-voimat-s3-kextra": round(1 / (M_read + 0.500), 3),
            "fy9-voimat-s3-F0extra": round(F0_read * (M_read + 0.500) / M_read, 3)})

# s4: the walking, the car and the ice (word task; numbers its model answer quotes)
mu0_ice, mu0_dry = 0.10, 0.80
out.update({"fy9-voimat-s4-aice": round(mu0_ice * g, 3), "fy9-voimat-s4-adry": round(mu0_dry * g, 2)})

# s5: tilting a book under a phone (the students' report)
angles = [22, 24, 21, 23, 33]
good = angles[:4]                                     # the fifth was lifted with a jerk (written in the log)
mean = sum(good) / len(good)
mu0_5 = math.tan(rad(mean))
lo, hi = math.tan(rad(min(good))), math.tan(rad(max(good)))
out.update({"fy9-voimat-s5-a": round(mu0_5, 4), "fy9-voimat-s5-mean": mean, "fy9-voimat-s5-lo": round(lo, 3),
            "fy9-voimat-s5-hi": round(hi, 3), "fy9-voimat-s5-report": round(math.sin(rad(33)), 3),
            "fy9-voimat-s5-tan33": round(math.tan(rad(33)), 3), "fy9-voimat-s5-mean5": round(sum(angles) / 5, 1)})

# s6: a sliding hill and the level run-out (example data; cross-module with kinematics)
al6, mu6, L6 = 12.0, 0.080, 40.0
a1 = g * (math.sin(rad(al6)) - mu6 * math.cos(rad(al6)))
v1 = math.sqrt(2 * a1 * L6)
t1 = v1 / a1
a2_6 = mu6 * g
s2_6 = v1 ** 2 / (2 * a2_6)
out.update({"fy9-voimat-s6-a1": round(a1, 4), "fy9-voimat-s6-a": round(v1, 3), "fy9-voimat-s6-t1": round(t1, 2),
            "fy9-voimat-s6-a2": round(a2_6, 4), "fy9-voimat-s6-b": round(s2_6, 2),
            "fy9-voimat-s6-vkmh": round(v1 * 3.6, 1)})

print(json.dumps(out))
