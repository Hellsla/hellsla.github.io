"""FY4 Esimerkkikoe: every number of the worked solutions, recomputed from the task data.
Prints {"<task>-<part>": value} for the parts with an answer in tasks.json; `python scripts/practice.py check FY4/koe` compares them."""
import json, math

g = 9.81
out = {}


def trapezoid(xs, ys):
    return sum((xs[i + 1] - xs[i]) * (ys[i] + ys[i + 1]) / 2 for i in range(len(xs) - 1))


# fy4-k1: Osa 1 checks of the options that need a number
out["k1-b-a"] = g                                                   # the stone's acceleration at the top
out["k1-f"] = {"static": 120, "max": 0.50 * 40 * g, "G": 40 * g}    # N: friction equals the push; 196 N and 392 N are distractors
out["k1-g"] = math.sqrt(4)                                          # v ∝ sqrt(h): 4h gives 2v
I_h = 0.5 * 1500 * 8.0e-3                                           # N·s, the triangle's area
out["k1-h"] = {"I": I_h, "v": round(I_h / 0.43, 1), "no_half": round(2 * I_h / 0.43, 1),
               "ms": round(0.5 * 1500 * 8.0 / 0.43, 0), "times_m": round(I_h * 0.43, 2)}
vA, mA, mB = 3.0, 2.0, 1.0
v_i = mA * vA / (mA + mB)
out["k1-i"] = {"v": v_i, "share": round(100 * 0.5 * (mA + mB) * v_i ** 2 / (0.5 * mA * vA ** 2), 1),
               "v_ratio_sq": round(100 * (v_i / vA) ** 2, 1), "lost": round(100 - 100 * (mA + mB) * v_i ** 2 / (mA * vA ** 2), 1)}

# fy4-k2: the tram (0-8 s accelerating, then steady)
T2 = [0, 2, 4, 6, 8, 10, 12, 14]; V2 = [0.0, 1.8, 3.9, 5.7, 7.6, 7.7, 7.6, 7.6]
a2 = (7.6 - 0.0) / (8.0 - 0.0)                                     # the drawn line through (0; 0) and (8,0 s; 7,6 m/s)
out["fy4-k2-b"] = round(a2, 3)
out["k2-fit"] = round(sum(t * v for t, v in zip(T2[:5], V2[:5])) / sum(t * t for t in T2[:5]), 4)   # origin fit 0-8 s
out["fy4-k2-c"] = round(0.5 * 8.0 * 7.6 + (14 - 8.0) * 7.6, 1)     # m, area under the line
out["fy4-k2-d"] = round(32.0e3 * a2, -2)                           # N, net force on 32 t

# fy4-k3: the crate on the truck bed
mu0, mu, m3 = 0.40, 0.30, 40.0
out["fy4-k3-b"] = round(mu0 * g, 3)                                 # m/s², the largest acceleration without sliding
out["fy4-k3-c"] = round((54 / 3.6) / 3.0, 3)                        # m/s², the braking deceleration
out["fy4-k3-d"] = round(mu * g, 3); out["k3-d-friction"] = round(mu * m3 * g, 0)   # sliding: the crate slows at mu·g

# fy4-k4: the sliding block (energy principle)
v4, dv4, s4, ds4 = 1.50, 0.03, 0.46, 0.01
out["fy4-k4-a"] = round(v4 ** 2 / (2 * g * s4), 4)
out["fy4-k4-b-max"] = round((v4 + dv4) ** 2 / (2 * g * (s4 - ds4)), 4)
out["fy4-k4-b-min"] = round((v4 - dv4) ** 2 / (2 * g * (s4 + ds4)), 4)
out["k4-c"] = {"rel_v": round(100 * dv4 / v4, 2), "rel_v2": round(200 * dv4 / v4, 2), "rel_s": round(100 * ds4 / s4, 2)}

# fy4-k5: coupling railway wagons
m1, v1, m2 = 24.0e3, 1.5, 36.0e3
u5 = m1 * v1 / (m1 + m2)
E1 = 0.5 * m1 * v1 ** 2; E2 = 0.5 * (m1 + m2) * u5 ** 2
out["fy4-k5-a"] = round(u5, 3)
out["fy4-k5-b"] = round(E1 - E2, 0); out["k5-b"] = {"E1": E1, "E2": E2, "share_lost": round(100 * (E1 - E2) / E1, 1)}
out["fy4-k5-c"] = round(m2 * u5 / 0.80, 0); out["k5-c-I"] = m2 * u5
out["k5-d"] = {"dv1": round(u5 - v1, 2), "dv2": round(u5, 2)}

# fy4-k6: the jump from a force plate
T6 = [0.00, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40]
F6 = [687, 1100, 1400, 1520, 1500, 1380, 1100, 600, 0]
G6 = 687
m6 = G6 / g
area6 = trapezoid(T6, F6)
I6 = area6 - G6 * 0.40
v6 = I6 / m6
out["fy4-k6-a"] = round(m6, 2)
out["k6-c"] = {"area": round(area6, 1), "weight": round(G6 * 0.40, 1), "net": round(I6, 1)}
out["fy4-k6-c"] = round(v6, 3)
out["fy4-k6-d"] = round(v6 ** 2 / (2 * g), 3)
tf, dtf = 0.49, 1 / 30
out["fy4-k6-e"] = round(g * tf ** 2 / 8, 3)
out["k6-e"] = {"v_flight": round(g * tf / 2, 3), "h_lo": round(g * (tf - dtf) ** 2 / 8, 3), "h_hi": round(g * (tf + dtf) ** 2 / 8, 3),
               "diff_pct": round(100 * (v6 ** 2 / (2 * g) - g * tf ** 2 / 8) / (v6 ** 2 / (2 * g)), 1)}

# fy4-k7: the helmet drop test
m7, h7, peak, T7, s7, s7b, limit = 5.0, 1.50, 950.0, 9.0e-3, 0.024, 0.010, 2450.0
v7 = math.sqrt(2 * g * h7)
a7 = v7 / T7
out["fy4-k7-a"] = round(v7, 3)
out["fy4-k7-b"] = round(a7, 0); out["k7-b-ratio"] = round(peak / a7, 2)
out["k7-b-check"] = round(2 / math.pi * peak * T7, 2)              # the measured curve's area: the speed it removes
out["fy4-k7-c"] = round(m7 * (a7 + g), 0); out["k7-c-G"] = round(m7 * g, 1)
a7b = v7 ** 2 / (2 * s7b)                                           # the thinner helmet's average deceleration
a7s = v7 ** 2 / (2 * s7)                                            # the same model for the measured helmet
out["fy4-k7-d"] = round(a7b * peak / a7s, -1)
out["k7-d"] = {"avg_thin": round(a7b, 0), "avg_meas": round(a7s, 0), "ratio": round(peak / a7s, 2),
               "scaling": round(peak * s7 / s7b, 0), "margin_pct": round(100 * (limit - a7b * peak / a7s) / limit, 1)}
v25 = 25 / 3.6
out["k7-e"] = {"v": round(v25, 2), "energy_ratio": round((v25 / v7) ** 2, 2)}
print(json.dumps(out))
