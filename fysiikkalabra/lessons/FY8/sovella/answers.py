"""FY8 Sovella itsenäisesti: every number of the worked solutions, recomputed from the task data.
Prints {"<task>-<part>": value} for the parts with an answer in tasks.json (and the intermediate values the solutions
quote); `python scripts/practice.py check FY8` compares them with tasks.json."""
import json, math

h, c, e = 6.626e-34, 2.998e8, 1.602e-19
u_kg, u_MeV = 1.66054e-27, 931.5
year = 365.25 * 24 * 3600
out = {}

# fy8-s1: aurora. Oxygen levels (NIST, rounded) read from the task figure: 0; 1,97 eV; 4,19 eV
E1, E2 = 1.97, 4.19
lam_green, lam_red = 557.7e-9, 630.0e-9
Eg = h * c / lam_green / e; Er = h * c / lam_red / e
lam3 = h * c / (E2 * e)                                   # a) the third line: upper excited state -> ground state
n_exc = 5000 / E2                                          # b) at most this many excitations from a 5 keV electron
Esi = 1.12                                                 # d) silicon band gap (eV)
lam_si = h * c / (Esi * e)
out.update({"fy8-s1-Eg-J": float(f"{h * c / lam_green:.4g}"), "fy8-s1-Eg": round(Eg, 3), "fy8-s1-Er": round(Er, 3),
            "fy8-s1-dE": round(E2 - E1, 2), "fy8-s1-E2J": float(f"{E2 * e:.4g}"), "fy8-s1-a": round(lam3 * 1e9, 1),
            "fy8-s1-lam-green-model": round(h * c / ((E2 - E1) * e) * 1e9, 1), "fy8-s1-lam-red-model": round(h * c / (E1 * e) * 1e9, 1),
            "fy8-s1-b": round(n_exc), "fy8-s1-d": round(lam_si * 1e9), "fy8-s1-EsiJ": float(f"{Esi * e:.4g}")})

# fy8-s2: the Mars rover's radioisotope generator (NASA MMRTG: 4,8 kg PuO2, about 2000 W heat, 110 W electric)
m_Pu, m_U, m_He = 238.049560, 234.040952, 4.002603        # atomic masses (u), AME2020
dm = m_Pu - m_U - m_He
Q_MeV = dm * u_MeV
Q_J = Q_MeV * 1e6 * e
P0, Pel = 2000.0, 110.0
T_Pu = 87.7 * year
A = P0 / Q_J
lam = math.log(2) / T_Pu
N = A / lam
m238 = N * m_Pu * u_kg
frac_Pu = 238.0 / (238.0 + 2 * 16.00)                      # Pu in PuO2 (atomic masses rounded)
m_Pu_fuel = 4.8 * frac_Pu
P14 = P0 * 0.5 ** (14 / 87.7)
ratio_U = 4.47e9 / 87.7                                     # activity per nucleus: Pu-238 against U-238
out.update({"fy8-s2-dm": round(dm, 6), "fy8-s2-a": round(Q_MeV, 3), "fy8-s2-QJ": float(f"{Q_J:.4g}"),
            "fy8-s2-A": float(f"{A:.4g}"), "fy8-s2-T": float(f"{T_Pu:.4g}"), "fy8-s2-lambda": float(f"{lam:.4g}"),
            "fy8-s2-N": float(f"{N:.4g}"), "fy8-s2-mnuc": float(f"{m_Pu * u_kg:.5g}"), "fy8-s2-b": round(m238, 3),
            "fy8-s2-fracPu": round(frac_Pu, 4), "fy8-s2-mPu": round(m_Pu_fuel, 3), "fy8-s2-share": round(m238 / m_Pu_fuel, 3),
            "fy8-s2-d": round(P14), "fy8-s2-d-factor": round(0.5 ** (14 / 87.7), 4), "fy8-s2-d-el": round(Pel * 0.5 ** (14 / 87.7), 1),
            "fy8-s2-Po-1a": round(0.5 ** (365.25 / 138), 4), "fy8-s2-ratioU": float(f"{ratio_U:.3g}")})
# e) 10 Bq of Pu-238 kept in the lungs (1,2 kg) for a year; w_R = 20 (alpha), w_T = 0,12 (lungs)
E_lung = 10 * year * Q_J
D_lung = E_lung / 1.2
H_T = 20 * D_lung
H_E = 0.12 * H_T
out.update({"fy8-s2-e-E": float(f"{E_lung:.3g}"), "fy8-s2-e-D": float(f"{D_lung:.3g}"), "fy8-s2-e-HT": float(f"{H_T:.3g}"),
            "fy8-s2-e": round(H_E * 1e3, 3), "fy8-s2-e-share": round(H_E * 1e3 / 5.9, 3), "fy8-s2-e-At": float(f"{10 * year:.4g}")})

# fy8-s3: the school's Cs-137 source and a GM tube (invented data: K = 30 720 cm²/min, d = 1,2 cm, background 22,4 /min)
rs = [2.0, 3.0, 4.0, 5.0, 6.0, 8.0, 10.0, 14.0, 20.0]       # cm
Ns = [3048, 1806, 1172, 790, 617, 405, 256, 152, 94]       # pulses in 1,0 min
Rb = 112 / 5.0                                              # background, 1/min
net = [n - Rb for n in Ns]
ys = [1 / math.sqrt(v) for v in net]                        # 1/sqrt(R) in sqrt(min)
for r, v, y in zip(rs, net, ys):
    k = f"{r:g}"
    out[f"fy8-s3-R-{k}"] = round(v, 1); out[f"fy8-s3-x-{k}"] = round(1 / r ** 2, 4)
    out[f"fy8-s3-Rr2-{k}"] = round(v * r * r); out[f"fy8-s3-y-{k}"] = round(100 * y, 3)   # 10^-2 sqrt(min)
mx, my = sum(rs) / len(rs), sum(ys) / len(ys)
k_fit = sum((a - mx) * (b - my) for a, b in zip(rs, ys)) / sum((a - mx) ** 2 for a in rs)
b_fit = my - k_fit * mx
# read in the solution from the drawn line: it meets the r axis at r = -1,3 cm and passes (20,0 cm; 12,0 · 10^-2 sqrt(min))
y1, y2 = b_fit + k_fit * 2.0, b_fit + k_fit * 20.0
d_read = 1.3
slope = 0.120 / (20.0 + d_read)
K = 1 / slope ** 2
r_eq = math.sqrt(K / Rb) - d_read
dN20 = math.sqrt(94 + (math.sqrt(112) / 5) ** 2)            # c) the net count's random error at 20 cm (1/min)
out.update({"fy8-s3-Rb": Rb, "fy8-s3-fit-slope": round(100 * k_fit, 4), "fy8-s3-fit-icpt": round(100 * b_fit, 4),
            "fy8-s3-fit-d": round(b_fit / k_fit, 3), "fy8-s3-line2": round(100 * y1, 3), "fy8-s3-line20": round(100 * y2, 3),
            "fy8-s3-slope": round(100 * slope, 4), "fy8-s3-b": round(d_read, 3), "fy8-s3-K": round(K),
            "fy8-s3-dN20": round(dN20, 1), "fy8-s3-dN20-rel": round(dN20 / net[-1], 3), "fy8-s3-dN2-rel": round(math.sqrt(3048) / 3048, 3),
            "fy8-s3-dr-rel": round(2 * 0.1 / (2.0 + d_read), 3), "fy8-s3-d": round(r_eq, 2), "fy8-s3-d-rd": round(math.sqrt(K / Rb), 2),
            "fy8-s3-dRb": round(math.sqrt(112) / 5, 1), "fy8-s3-dN2": round(math.sqrt(3048 + (math.sqrt(112) / 5) ** 2)),
            "fy8-s3-H": round(3.0 * (10.0 / r_eq) ** 2, 2), "fy8-s3-dose45": round(3.0 * 0.75, 2), "fy8-s3-day": round(5.9e3 / 365, 1)})

# (s3 d: the manufacturer's dose rate 3,0 µSv/h at 10 cm, falling as 1/r²; 45 min at 10 cm; 5,9 mSv a year spread over 365 days)

# fy8-s4: helium from the first minutes (PDG 2024: neutron mean life 878,4 s -> T1/2 = 609 s; Y_P = 0,245)
mn, mp, me = 939.565, 938.272, 0.511                       # MeV/c²
Q_pe = mn - mp - me                                         # energy released in n -> p + e + antineutrino
Y = 0.245
f = Y / (2 - Y)                                             # N_n / N_p when nuclei formed
p_per_n = 1 / f
Tn = 609.0
Nn = 7 * f / (1 + f)                                        # neutrons left of the 1 + 6 nucleons
t = Tn * math.log(1 / Nn) / math.log(2)
Nn5 = 6 * f / (1 + f)                                       # d) the same with 1 : 5 at 1 s
t5 = Tn * math.log(1 / Nn5) / math.log(2)
Y_sev = 2 * (1 / 7) / (1 + 1 / 7)
out.update({"fy8-s4-Qpe": round(Q_pe, 3), "fy8-s4-f": round(f, 4), "fy8-s4-b": round(p_per_n, 3), "fy8-s4-Nn": round(Nn, 4),
            "fy8-s4-np": round(7 - Nn, 4), "fy8-s4-log": round(math.log(1 / Nn) / math.log(2), 4), "fy8-s4-dt": round(t, 1),
            "fy8-s4-c": round(t + 1, 1), "fy8-s4-Nn5": round(Nn5, 4), "fy8-s4-t5": round(t5 + 1, 1), "fy8-s4-t5min": round((t5 + 1) / 60, 2),
            "fy8-s4-cmin": round((t + 1) / 60, 2), "fy8-s4-Ysev": round(Y_sev, 3)})

# fy8-s5: the natural reactor at Oklo, Gabon (half-lives NNDC; abundances IUPAC; power and time order-of-magnitude estimates)
T235, T238 = 7.04e8, 4.47e9                                  # a
x235, x238 = 0.720, 99.274                                  # % today
t_ok = 2.0e9
g235 = 2 ** (t_ok / T235); g238 = 2 ** (t_ok / T238)
r_then = (x235 * g235) / (x238 * g238)
share = 100 * x235 * g235 / (x235 * g235 + x238 * g238)
P_ok, t_run = 100e3, 1.5e5 * year                           # c (the fissions and mass: background for the solution)
E_ok = P_ok * t_run
Ef = 200e6 * e
n_f = E_ok / Ef
m235 = 235.04 * u_kg
m_ok = n_f * m235
t_OL3 = E_ok / 4300e6
out.update({"fy8-s5-g235": round(g235, 3), "fy8-s5-g238": round(g238, 4), "fy8-s5-exp235": round(t_ok / T235, 3),
            "fy8-s5-exp238": round(t_ok / T238, 4), "fy8-s5-n235": round(x235 * g235, 3), "fy8-s5-n238": round(x238 * g238, 1),
            "fy8-s5-a": round(share, 2), "fy8-s5-ratio": round(r_then, 4), "fy8-s5-E": float(f"{E_ok:.3g}"),
            "fy8-s5-Ef": float(f"{Ef:.4g}"), "fy8-s5-nf": float(f"{n_f:.3g}"), "fy8-s5-m235": float(f"{m235:.4g}"),
            "fy8-s5-m": round(m_ok / 1000, 2), "fy8-s5-tOL3": float(f"{t_OL3:.3g}"), "fy8-s5-c": round(t_OL3 / year, 2),
            "fy8-s5-Pratio": round(4300e6 / P_ok), "fy8-s5-c-direct": round(P_ok / 4300e6 * 1.5e5, 2),
            "fy8-s5-Pu-halvings": round(2.0e9 / 24100)})
print(json.dumps(out))
