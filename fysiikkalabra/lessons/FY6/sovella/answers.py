"""FY6 Sovella itsenäisesti: every number of the worked solutions, recomputed from the task data.
Prints {"<task>-<part>": value} for the parts with an answer in tasks.json (and the intermediate values the solutions
quote); `python scripts/practice.py check FY6` compares them with tasks.json."""
import json, math

k_e = 8.988e9          # Coulomb constant, N·m²/C²
g = 9.81

out = {}


def fit(x, y):
    mx, my = sum(x) / len(x), sum(y) / len(y)
    k = sum((a - mx) * (b - my) for a, b in zip(x, y)) / sum((a - mx) ** 2 for a in x)
    return k, my - k * mx


# fy6-s1: the battery measurement (simulated data: E = 4,60 V, R_s = 1,2 ohm, readings to 0,01 V and 0,01 A)
I1 = [0.10, 0.20, 0.30, 0.40, 0.50, 0.60]        # A
U1 = [4.48, 4.37, 4.22, 4.13, 3.99, 3.89]        # V
slope, icpt = fit(I1, U1)
# as read in the solution from two far-apart points of the drawn line: (0,10 A; 4,48 V) and (0,60 A; 3,88 V)
sl_read = (3.88 - 4.48) / (0.60 - 0.10)
Rs = -sl_read
E = 4.48 + Rs * 0.10
out.update({"fy6-s1-fit-slope": round(slope, 4), "fy6-s1-fit-icpt": round(icpt, 4), "fy6-s1-slope": round(sl_read, 3),
            "fy6-s1-b-E": round(E, 3), "fy6-s1-b-Rs": round(Rs, 3), "fy6-s1-Ik": round(E / Rs, 3)})
R = 8.0                                           # c) the load
I = E / (R + Rs)
P = R * I * I
P_batt = Rs * I * I
out.update({"fy6-s1-c-P": round(P, 3), "fy6-s1-c-I": round(I, 4), "fy6-s1-c-Pbatt": round(P_batt, 4),
            "fy6-s1-c-osuus": round(100 * P_batt / (P + P_batt), 2), "fy6-s1-c-U": round(R * I, 3)})
# d) the scatter of the points about the line is at most 0,02 V; extreme lines through the scatter's ends
dU = 0.02
dRs = 2 * dU / (0.60 - 0.10)
out.update({"fy6-s1-d-dRs": round(dRs, 3), "fy6-s1-d-maxres": round(max(abs(u - (icpt + slope * i)) for i, u in zip(I1, U1)), 3)})

# fy6-s2: cable and two lamps (12,0 V source, cable 0,80 ohm, lamps 12 V/24 W and 12 V/12 W, fuse 3,15 A, cable limit 4,0 A)
E2, Rc = 12.0, 0.80
RA, RB = 12.0 ** 2 / 24.0, 12.0 ** 2 / 12.0
Rp = 1 / (1 / RA + 1 / RB)
Rtot = Rc + Rp
Ia = E2 / Rtot
UL = Rp * Ia
PA, PB, Pc = UL ** 2 / RA, UL ** 2 / RB, Rc * Ia ** 2
out.update({"fy6-s2-RA": RA, "fy6-s2-RB": RB, "fy6-s2-Rp": round(Rp, 4), "fy6-s2-Rtot": round(Rtot, 4), "fy6-s2-a": round(Ia, 4),
            "fy6-s2-a-UL": round(UL, 4), "fy6-s2-b": round(PA, 3), "fy6-s2-b-PB": round(PB, 3), "fy6-s2-b-Pc": round(Pc, 3),
            "fy6-s2-b-Pbatt": round(E2 * Ia, 3), "fy6-s2-b-eff": round((PA + PB) / (E2 * Ia), 4)})
# c) lamp B removed
Ic = E2 / (Rc + RA)
UAc = RA * Ic
out.update({"fy6-s2-c-I": round(Ic, 4), "fy6-s2-c-UA": round(UAc, 4), "fy6-s2-c-PA": round(UAc ** 2 / RA, 3), "fy6-s2-c-Pc": round(Rc * Ic ** 2, 3),
            "fy6-s2-c-Ucable": round(Rc * Ic, 3), "fy6-s2-c-Ucable0": round(Rc * Ia, 3)})
# d) a third lamp 12 V/36 W in parallel
RC = 12.0 ** 2 / 36.0
Rp3 = 1 / (1 / RA + 1 / RB + 1 / RC)
Id = E2 / (Rc + Rp3)
out.update({"fy6-s2-RC": RC, "fy6-s2-d-Rp": round(Rp3, 4), "fy6-s2-d": round(Id, 4), "fy6-s2-d-UL": round(Rp3 * Id, 3),
            "fy6-s2-d-PC": round((Rp3 * Id) ** 2 / RC, 3), "fy6-s2-d-Pc": round(Rc * Id ** 2, 3)})

# fy6-s3: electrostatic spray painting (plates d = 0,20 m, U = 60 kV, droplet m = 4,0e-10 kg, q = 6,0e-13 C)
d3, U3, m3, q3 = 0.20, 60e3, 4.0e-10, 6.0e-13
E3 = U3 / d3
F3 = q3 * E3
G3 = m3 * g
out.update({"fy6-s3-a-E": round(E3), "fy6-s3-a": F3, "fy6-s3-a-G": G3, "fy6-s3-a-ratio": round(F3 / G3, 2),
            "fy6-s3-a-Eair": round(E3 / 3e6, 3), "fy6-s3-a-acc": round(F3 / m3, 1)})
W3 = q3 * U3
v3 = math.sqrt(2 * W3 / m3)
out.update({"fy6-s3-b": round(v3, 3), "fy6-s3-b-W": W3, "fy6-s3-b-Wg": G3 * d3})
v_meas = 5.0
Ek = 0.5 * m3 * v_meas ** 2
out.update({"fy6-s3-c-Ek": Ek, "fy6-s3-c-share": round(Ek / W3, 4), "fy6-s3-c-rest": W3 - Ek})
r3 = 1.0e-3
Fc = k_e * q3 ** 2 / r3 ** 2
out.update({"fy6-s3-d": Fc, "fy6-s3-d-vsF": round(Fc / F3, 4), "fy6-s3-d-vsG": round(Fc / G3, 3)})

# fy6-s4: camera flash (C = 330 uF, 300 V before, 220 V after, 1,0 ms)
C4, U4a, U4b, t4 = 330e-6, 300.0, 220.0, 1.0e-3
Ea, Eb = 0.5 * C4 * U4a ** 2, 0.5 * C4 * U4b ** 2
dE = Ea - Eb
dQ = C4 * (U4a - U4b)
out.update({"fy6-s4-a": round(Ea, 3), "fy6-s4-b": round(dE, 3), "fy6-s4-b-Eb": round(Eb, 3), "fy6-s4-b-share": round(dE / Ea, 4),
            "fy6-s4-c": round(dQ / t4, 3), "fy6-s4-c-dQ": round(dQ * 1e3, 3), "fy6-s4-c-P": round(dE / t4, 1),
            "fy6-s4-Qa": round(C4 * U4a, 4), "fy6-s4-d-I": round(U4a / 1000.0, 3), "fy6-s4-d-Ires": round(U4a / 10e3 * 1e3, 3)})
print(json.dumps(out))
