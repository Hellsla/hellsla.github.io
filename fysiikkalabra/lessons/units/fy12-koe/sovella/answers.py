"""fy12-koe Tehtävät: every number of the worked solutions, recomputed from the task data.
Prints {"<task>-<part>": value}; `python scripts/practice.py check units/fy12-koe` compares them with tasks.json."""
import json, math

g = 9.81
out = {}

# fy12-koe-s1: the cyclist climbing a hill road at constant speed
m, h, s, t, F_v, eta = 82.0, 45.0, 1.20e3, 4 * 60 + 30, 18.0, 0.22   # kg, m, m, s, N, -
dEp = m * g * h                       # J, a
P_lift = dEp / t                      # W, b
W_v = F_v * s                         # J, work against the resistive forces
W = dEp + W_v                         # J, the muscles' mechanical work (kinetic energy unchanged)
P = W / t                             # W, c
E_food = W / eta                      # J, d
share = E_food / 2200e3               # e: the share of a 2200 kJ chocolate bar (about 0.12, i.e. about 8 climbs)
out.update({"fy12-koe-s1-a": dEp, "fy12-koe-s1-b": P_lift, "fy12-koe-s1-c": P, "fy12-koe-s1-d": E_food / 1000})

# fy12-koe-s2: pendulum, L measured to the top of the bob; T^2 against L
L = [0.200, 0.350, 0.500, 0.650, 0.800, 0.950]                # m
t10 = [9.33, 12.08, 14.42, 16.41, 18.08, 19.72]                # s, ten periods
T2 = [(x / 10) ** 2 for x in t10]                              # s^2


def fit(x, y):
    mx, my = sum(x) / len(x), sum(y) / len(y)
    k = sum((a - mx) * (b - my) for a, b in zip(x, y)) / sum((a - mx) ** 2 for a in x)
    return k, my - k * mx


k, b = fit(L, T2)                                              # s^2/m, s^2
# the slope as read in the solution from two points of the drawn line at L = 0,100 m and 0,900 m
y1, y2 = b + k * 0.100, b + k * 0.900
k_read = (y2 - y1) / 0.800
g_meas = 4 * math.pi ** 2 / k_read                             # c
L_axis = -b / k                                                # d: where the line meets the L axis (about -0,015 m)
g_point = 4 * math.pi ** 2 * L[0] / T2[0]                      # d: g from the first point alone (too small)
out["fy12-koe-s2-c"] = g_meas

# fy12-koe-s3: tea in a vacuum flask
c_w, m_t, dT, t_h = 4190.0, 0.50, 85.0 - 70.0, 6.0
Q = c_w * m_t * dT                                             # J
P_loss = Q / (t_h * 3600)                                      # W, c
out["fy12-koe-s3-c"] = P_loss

# fy12-koe-s4: kettle efficiency from one measurement
m_k, T1, T2k, E_kwh = 0.500, 15.0, 95.0, 0.054
Q_k = c_w * m_k * (T2k - T1)                                   # J
E_el = E_kwh * 3.6e6                                           # J
out["fy12-koe-s4-b"] = 100 * Q_k / E_el                        # %
res = 0.001 / E_kwh                                            # c: the energy meter's step as a share of the reading

if __name__ == "__main__":
    import sys
    if "-v" in sys.argv:
        print(dict(W_v=W_v, W=W, share=share, k=k, b=b, y1=y1, y2=y2, k_read=k_read, L_axis=L_axis, g_point=g_point,
                   T=[x / 10 for x in t10], T2=T2, Q=Q, Q_k=Q_k, E_el=E_el, res=res))
    print(json.dumps(out))
