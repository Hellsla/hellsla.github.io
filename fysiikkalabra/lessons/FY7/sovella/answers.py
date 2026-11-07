"""FY7 Sovella itsenäisesti: every number of the worked solutions, recomputed from the task data.
Prints {"<task>-<part>": value} for the parts with an answer in tasks.json (and the intermediate values the solutions
quote); `python scripts/practice.py check FY7` compares them with tasks.json."""
import json, math

e = 1.602e-19
u = 1.66054e-27
out = {}

# fy7-s1: the ion implanter. Atomic masses AME2020 (the missing electron, 0,0005 u, is left out).
m11, m10 = 11.009305 * u, 10.012937 * u
U, Bs, dpl, r11 = 30.0e3, 0.200, 0.0200, 0.400
v = math.sqrt(2 * e * U / m11)                       # b) qU = ½mv²
Us = v * Bs * dpl                                    # c) qE = qvB, E = Us : d
B = m11 * v / (e * r11)                              # d) qvB = mv²/r
r10 = m10 * v / (e * B)                              # the same speed (selector), so r ∝ m
dx = 2 * (r11 - r10)
v10 = math.sqrt(2 * e * U / m10)                     # e) a boron-10 ion from the full 30,0 kV
W10 = 0.5 * m10 * v ** 2 / e                         # e) the kinetic energy (eV) a boron-10 ion needs to pass the selector
out.update({"fy7-s1-m11": float(f"{m11:.5g}"), "fy7-s1-m10": float(f"{m10:.5g}"), "fy7-s1-b": round(v, -1),
            "fy7-s1-W": round(e * U, 25), "fy7-s1-E": round(v * Bs), "fy7-s1-c": round(Us, 1),
            "fy7-s1-d-B": round(B, 5), "fy7-s1-r10": round(r10, 5), "fy7-s1-d-dx": round(dx * 100, 3),
            "fy7-s1-v10": round(v10, -1), "fy7-s1-W10": round(W10), "fy7-s1-W10-rel": round(W10 / U, 4),
            "fy7-s1-m-ratio": round(m10 / m11, 5)})

# fy7-s2: the hub dynamo. 28 poles: 14 voltage periods per turn of the wheel. Signal: 3 periods in 90 ms, peak 14 V.
T = 0.090 / 3; f = 1 / T; e0 = 14.0
Ueff = e0 / math.sqrt(2)
D, pairs = 0.70, 14
fw = f / pairs; vb = math.pi * D * fw
e0_need = 6.0 * math.sqrt(2)                          # c) the lamp's 6,0 V as a peak value
v_min = vb * e0_need / e0
P_lamp, eta = 3.0, 0.60
P_in = P_lamp / eta; F = P_in / vb                   # e) P = Fv
out.update({"fy7-s2-T": T, "fy7-s2-a-f": round(f, 3), "fy7-s2-a-U": round(Ueff, 3), "fy7-s2-fw": round(fw, 4),
            "fy7-s2-b": round(vb * 3.6, 2), "fy7-s2-b-ms": round(vb, 4), "fy7-s2-e0need": round(e0_need, 3),
            "fy7-s2-c": round(v_min * 3.6, 2), "fy7-s2-c-ms": round(v_min, 4), "fy7-s2-Pin": P_in, "fy7-s2-e": round(F, 4)})

# fy7-s3: the mine's power line. 6,0 MW, 25 km, two aluminium conductors of 150 mm², ρ = 2,82·10⁻⁸ Ωm.
P = 6.0e6; rho = 2.82e-8; L = 2 * 25e3; A = 150e-6; dens = 2700.0
R = rho * L / A
I20 = P / 20e3; Ph20 = R * I20 ** 2
I110 = P / 110e3; Ph110 = R * I110 ** 2
dU20 = R * I20; dU110 = R * I110                  # c) the voltage drop over the line
k = (110 / 20) ** 2                                   # d) how many times smaller R must be at 20 kV
A_need = A * Ph20 / Ph110
d_need = 2 * math.sqrt(A_need / math.pi)
mass_old = dens * L * A; mass_new = dens * L * A_need
out.update({"fy7-s3-R": round(R, 3), "fy7-s3-I20": I20, "fy7-s3-a-Ph": round(Ph20 / 1e3, 2), "fy7-s3-a-rel": round(Ph20 / P * 100, 2),
            "fy7-s3-I110": round(I110, 3), "fy7-s3-b": round(Ph110 / 1e3, 3), "fy7-s3-b-rel": round(Ph110 / P * 100, 3),
            "fy7-s3-dU20": round(dU20, 1), "fy7-s3-c": round((20e3 - dU20) / 1e3, 3), "fy7-s3-c-rel": round(dU20 / 20e3 * 100, 2), "fy7-s3-dU110": round(dU110, 1), "fy7-s3-dU110-rel": round(dU110 / 110e3 * 100, 3), "fy7-s3-k": k, "fy7-s3-Aneed": round(A_need * 1e6, 1),
            "fy7-s3-dneed": round(d_need * 100, 2), "fy7-s3-mold": round(mass_old / 1e3, 2), "fy7-s3-mnew": round(mass_new / 1e3, 1)})
# e) the force between the two conductors (opposite currents, 1,5 m apart): F/l = μ0 I² / (2π r), against the weight per metre
mu0, rc, Ik, g = 4 * math.pi * 1e-7, 1.5, 8.0e3, 9.81
B20 = mu0 * I20 / (2 * math.pi * rc); Bk = mu0 * Ik / (2 * math.pi * rc)
Fl = I20 * B20; Flk = Ik * Bk; Gl = dens * A * g
out.update({"fy7-s3-B20": round(B20 * 1e6, 2), "fy7-s3-e-F": round(Fl, 4), "fy7-s3-Bk": round(Bk * 1e3, 3), "fy7-s3-e-Fk": round(Flk, 2),
            "fy7-s3-Gl": round(Gl, 2), "fy7-s3-Fk-G": round(Flk / Gl, 2),
            "fy7-s3-F-G-pct": round(Fl / Gl * 100, 2), "fy7-s3-Ik-I": round(Ik / I20, 1), "fy7-s3-Fk-F": round(Flk / Fl)})

# fy7-s4: the mill's pyrometer. Spectrum of a black body at T where the peak is at 2,00 µm (task figure).
b = 2.898e-3
lam = 2.00e-6
Tk = b / lam; Tc = Tk - 273.15
n1, n2 = 1.44, 1.42
ar = math.degrees(math.asin(n2 / n1))
beta = 90 - ar
th = math.degrees(math.asin(n1 * math.sin(math.radians(beta))))
dlam = 0.05e-6                                         # d) how precisely the flat peak is read
dT = Tk * dlam / lam
out.update({"fy7-s4-a": round(Tc, 1), "fy7-s4-Tk": round(Tk, 1), "fy7-s4-c-ar": round(ar, 3), "fy7-s4-beta": round(beta, 3),
            "fy7-s4-sinth": round(n1 * math.sin(math.radians(beta)), 5), "fy7-s4-c-th": round(th, 3), "fy7-s4-dT": round(dT, 1),
            "fy7-s4-T-tc": 1210 + 273.15})
# e) the window's anti-reflection film (MgF2 1,38 on glass 1,50): both reflections invert, so 2nd = λ/2 for the thinnest
nf = 1.38
dfilm = lam / (4 * nf); path = 2 * nf * dfilm
vis_strong = [path / k_ for k_ in (1, 2, 3)]; vis_weak = [path / (k_ + 0.5) for k_ in (0, 1, 2)]
out.update({"fy7-s4-e": round(dfilm * 1e9, 1), "fy7-s4-lamfilm": round(lam / nf * 1e9, 1), "fy7-s4-d-onefilp": round(lam / (2 * nf) * 1e9, 1),
            "fy7-s4-d-non": round(lam / 4 * 1e9, 1), "fy7-s4-path": round(path * 1e9, 1), **{f"fy7-s4-strong-{k_}": round(x * 1e9, 1) for k_, x in enumerate(vis_strong, 1)},
            **{f"fy7-s4-weak-{k_}": round(x * 1e9, 1) for k_, x in enumerate(vis_weak)}})

# fy7-s5: the hydrogen lamp and a grating. NIST wavelengths in air (nm); angles measured to 0,1°.
data = [(656.28, 1, 23.2), (486.13, 1, 17.0), (434.05, 1, 15.1), (410.17, 1, 14.2), (656.28, 2, 52.0), (486.13, 2, 35.7)]
X = [k_ * l for l, k_, _ in data]; Y = [math.sin(math.radians(t)) for _, _, t in data]
for (l, k_, t), y in zip(data, Y): out[f"fy7-s5-sin-{int(l)}-{k_}"] = round(y, 4)
slope_fit = sum(x * y for x, y in zip(X, Y)) / sum(x * x for x in X)      # least squares through the origin (1/nm)
slope = 0.780 / 1300                                    # read from the model line: the point (1300 nm; 0,780)
dgr = 1 / slope                                         # nm
N = 1e6 / dgr                                           # lines per mm
th_y = 20.7
lam_y = dgr * math.sin(math.radians(th_y))
dth = math.radians(0.1)
dlam_y = dgr * math.cos(math.radians(th_y)) * dth
th_he = math.degrees(math.asin(587.56 / dgr)); th_na = math.degrees(math.asin(589.0 / dgr))
th_he2 = math.degrees(math.asin(2 * 587.56 / dgr)); th_na2 = math.degrees(math.asin(2 * 589.0 / dgr))
out.update({"fy7-s5-slope-fit": round(slope_fit * 1e4, 4), "fy7-s5-slope": round(slope * 1e4, 4), "fy7-s5-d": round(dgr, 1),
            "fy7-s5-b": round(N, 1), "fy7-s5-c": round(lam_y, 2), "fy7-s5-dlam": round(dlam_y, 2),
            "fy7-s5-th-he": round(th_he, 3), "fy7-s5-th-na": round(th_na, 3), "fy7-s5-th-he2": round(th_he2, 3),
            "fy7-s5-th-na2": round(th_na2, 3), "fy7-s5-lam-206": round(1667 * math.sin(math.radians(20.6)), 1), "fy7-s5-lam-208": round(1667 * math.sin(math.radians(20.8)), 1), "fy7-s5-dlam2": round(dgr * math.cos(math.radians(th_na2)) * dth / 2, 2)})
print(json.dumps(out, ensure_ascii=False))
