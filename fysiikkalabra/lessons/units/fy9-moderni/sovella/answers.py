"""FY9 fy9-moderni, Tehtävät: every number of the worked solutions, recomputed from the task data.
Prints {"<task>-<part>[-<name>]": value} for the parts with an answer in tasks.json and the intermediate values the
solutions quote; `python scripts/practice.py check units/fy9-moderni` compares them with tasks.json."""
import json, math

h, c, e = 6.626e-34, 2.998e8, 1.602e-19        # J s, m/s, C (the values of the FY8 chapters)
u_kg, u_MeV = 1.66054e-27, 931.5               # kg, MeV/c^2
year = 3.156e7                                 # s
ln2 = math.log(2)


def fit(x, y):
    mx, my = sum(x) / len(x), sum(y) / len(y)
    k = sum((a - mx) * (b - my) for a, b in zip(x, y)) / sum((a - mx) ** 2 for a in x)
    return k, my - k * mx


out = {}
S = "fy9-moderni"

# s1: Cs-137 in forest mushrooms (example data); the decay law, A = lambda N and the dose coefficient
E_g = 662e3                                    # eV, the gamma of Ba-137m
lam_g = h * c / (E_g * e)                      # m
A90, T_cs, years = 2400.0, 30.1, 2026 - 1990   # Bq/kg in 1990, a, a
A26 = A90 * 0.5 ** (years / T_cs)              # Bq/kg in 2026
eat, coef = 5.0, 1.3e-8                        # kg a year, Sv/Bq
dose = A26 * eat * coef                        # Sv
N26 = A26 * T_cs * year / ln2                  # nuclei in 1,0 kg
m26 = N26 * 137 * u_kg                         # kg of Cs-137
out.update({f"{S}-s1-a": round(lam_g * 1e12, 4), f"{S}-s1-b": round(A26, 1), f"{S}-s1-b-n": round(years / T_cs, 4),
            f"{S}-s1-c": round(dose * 1e3, 4), f"{S}-s1-c-Bq": round(A26 * eat, 0), f"{S}-s1-c-share": round(100 * dose * 1e3 / 5.9, 2),
            f"{S}-s1-d-N": N26, f"{S}-s1-d": round(m26 * 1e12, 3), f"{S}-s1-d-lambda": ln2 / (T_cs * year)})

# s2: hydrogen lines in a galaxy (example data); E_n = -13,6 eV / n^2, z = dlambda/lambda0, v = cz, v = H0 d
E32 = 13.6 * (1 / 2 ** 2 - 1 / 3 ** 2)         # eV
lam32 = h * c / (E32 * e)                      # m
lam0a, lam_obs, lam0b, H0 = 656.3, 671.8, 486.1, 70.0
z = (lam_obs - lam0a) / lam0a
v = c / 1000 * z                               # km/s
d = v / H0                                     # Mpc
lam_b = lam0b * (1 + z)
E42 = 13.6 * (1 / 4 - 1 / 16)
out.update({f"{S}-s2-a-E": round(E32, 4), f"{S}-s2-a": round(lam32 * 1e9, 2), f"{S}-s2-b-z": round(z, 5),
            f"{S}-s2-b-v": round(v, 0), f"{S}-s2-b-d": round(d, 1), f"{S}-s2-c": round(lam_b, 2),
            f"{S}-s2-c-dl": round(lam_b - lam0b, 2), f"{S}-s2-c-check": round(h * c / (E42 * e) * 1e9, 1)})

# s3: the photoelectric effect and the stopping voltage (invented data: W 2,25 eV, h 6,626e-34, scatter about 0,01 V)
L3 = [365, 405, 436, 470, 505]                 # nm
U3 = [1.15, 0.80, 0.61, 0.38, 0.21]            # V
f3 = [c / (l * 1e-9) for l in L3]              # Hz
k3, b3 = fit(f3, U3)                           # V s, V
# read in the solution from two far-apart points of the drawn line: its U intercept (0 Hz; -2,24 V) and (8,0e14 Hz; 1,06 V)
fA, UA, fB, UB = 0.0, -2.24, 8.0e14, 1.06
k_read = (UB - UA) / (fB - fA)
h_read = e * k_read
b_read = UA - k_read * fA
f0_read = -b_read / k_read
out.update({f"{S}-s3-f": [round(x / 1e14, 3) for x in f3], f"{S}-s3-k-fit": k3, f"{S}-s3-b-fit": round(b3, 4),
            f"{S}-s3-h-fit": e * k3, f"{S}-s3-c": h_read, f"{S}-s3-k-read": k_read,
            f"{S}-s3-c-diff": round(100 * (h_read - 6.626e-34) / 6.626e-34, 2),
            f"{S}-s3-d-W": round(-b_read, 3), f"{S}-s3-d-f0": f0_read,
            f"{S}-s3-d-lam0": round(c / f0_read * 1e9, 1), f"{S}-s3-d-W-fit": round(-b3, 3),
            f"{S}-s3-d-f590": round(c / 590e-9 / 1e14, 3), f"{S}-s3-d-E590": round(h * c / 590e-9 / e, 3)})

# s4: the radon claims (word task; the numbers its model answers quote)
out.update({f"{S}-s4-ratio": round(450 / 300, 2), f"{S}-s4-left30": round(100 * 0.5 ** (30 / 3.8), 2),
            f"{S}-s4-n30": round(30 / 3.8, 2), f"{S}-s4-xray-keV": 60, f"{S}-s4-E-red": round(h * c / 660e-9 / e, 3)})

# s5: the half-life report (invented data: Ba-137m 153 s, background 5 per 10 s, counting scatter)
t5 = [0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300]                   # s
N5 = [398, 361, 304, 276, 231, 212, 188, 163, 136, 127, 104]              # pulses / 10 s
bg5 = 5
net = [x - bg5 for x in N5]
T_two = 300 * ln2 / math.log(net[0] / net[-1])                            # the two end points, net
kl, bl = fit(t5, [math.log(x) for x in net])                              # ln(net) against t: slope -lambda
T_fit = -ln2 / kl
T_raw_two = 300 * ln2 / math.log(N5[0] / N5[-1])
t_half_group = 150 + 30 * (212 - 199) / (212 - 188)                       # the group's reading, half of 398
out.update({f"{S}-s5-a": round(T_fit, 1), f"{S}-s5-a-two": round(T_two, 2), f"{S}-s5-a-raw": round(T_raw_two, 1),
            f"{S}-s5-group": round(t_half_group, 1), f"{S}-s5-diff": round(100 * (166 - 153) / 153, 1),
            f"{S}-s5-bg-share-end": round(100 * bg5 / N5[-1], 1), f"{S}-s5-a-diff": round(100 * (T_two - T_fit) / T_fit, 1)})

# s6: a nuclear power plant (example data in the size class of a large pressurised-water unit) with FY2 and FY3
Pe, Pth = 1600e6, 4300e6                        # W
eta = Pe / Pth
Ef = 200e6 * e                                  # J per fission
rate = Pth / Ef                                 # fissions per second
m_U = rate * year * 235 * u_kg                  # kg of U-235 a year (full power all year)
dm = Pth * year / c ** 2                        # kg, the mass that becomes energy a year
P_loss = Pth - Pe
c_w, dT = 4190.0, 11.0
flow = P_loss / (c_w * dT)                      # kg/s of sea water
H_coal, eta_coal = 24e6, 0.40
coal = Pe * year / (eta_coal * H_coal)          # kg of coal a year
out.update({f"{S}-s6-a-eta": round(100 * eta, 2), f"{S}-s6-a-n": rate, f"{S}-s6-b-m": round(m_U, 0),
            f"{S}-s6-b-dm": round(dm, 3), f"{S}-s6-b-share": round(100 * dm / m_U, 3),
            f"{S}-s6-b-share-theory": round(100 * 200 / (235 * u_MeV), 3), f"{S}-s6-c": round(flow, 0),
            f"{S}-s6-c-loss": P_loss, f"{S}-s6-d": round(coal / 1e3, -3), f"{S}-s6-d-Ee": Pe * year,
            f"{S}-s6-d-ratio": round(coal / m_U, 0)})

# s7 (FY9-A3): the fusion shot of December 2022. Yle Uutiset 12.12.2022 (https://yle.fi/a/3-12684377, checked
# 16.11.2026): 3,15 MJ released by fusion, 2,05 MJ of laser energy delivered to the fuel target. The laboratory's
# figure for the electricity the lasers took from the grid for the shot: about 300 MJ.
E_fus, E_las, E_grid = 3.15e6, 2.05e6, 300e6    # J
gain = E_fus / E_las                            # the ratio of the two energies
surplus = E_fus - E_las                         # J
c_water, T1, T2 = 4190.0, 20.0, 100.0           # J/(kg K), deg C, deg C
m_w = E_fus / (c_water * (T2 - T1))             # kg of water heated from 20 to 100 deg C
share_grid = E_fus / E_grid                     # fusion energy / electricity taken from the grid
eta_th = 1 / 3                                  # a thermal plant turns about a third into electricity
E_el = eta_th * E_fus                           # J of electricity the fusion energy could give
dm7 = E_fus / c ** 2                            # kg, the mass that corresponds to the released energy
out.update({f"{S}-s7-b-ratio": round(gain, 4), f"{S}-s7-b-diff": round(surplus / 1e6, 3),
            f"{S}-s7-b-percent": round(100 * (gain - 1), 1), f"{S}-s7-c": round(m_w, 3), f"{S}-s7-c-dT": T2 - T1,
            f"{S}-s7-c-cdT": c_water * (T2 - T1), f"{S}-s7-c-pots": round(m_w / 3.0, 2),
            f"{S}-s7-c-kWh": round(E_fus / 3.6e6, 3),
            f"{S}-s7-d-share": round(100 * share_grid, 2), f"{S}-s7-d-times": round(E_grid / E_fus, 1),
            f"{S}-s7-d-Eel": round(E_el / 1e6, 3), f"{S}-s7-d-share-el": round(100 * E_el / E_grid, 2),
            f"{S}-s7-d-share-laser": round(100 * E_las / E_grid, 2), f"{S}-s7-b-inverse": round(E_las / E_fus, 3),
            f"{S}-s7-e-dm": dm7, f"{S}-s7-e-dm-ng": round(dm7 * 1e12, 2)})

# s8: concrete wall and gamma radiation (fy8-13/vaimennus; read from the graph): H = 80 uSv/h at d = 0 and 5,0 uSv/h at d = 20 cm
H8_0, H8_20, d8_20 = 80.0, 5.0, 20.0
mu8 = math.log(H8_0 / H8_20) / d8_20                              # 1/cm
d8 = 18.0                                                         # cm, the wall
H8 = H8_0 * math.exp(-mu8 * d8)                                   # uSv/h behind the wall
hours8 = 1.5 * 220                                                # h a year in the corridor
D8 = H8 * hours8                                                  # uSv a year
Hmax8 = 1000.0 / hours8                                           # uSv/h, limit 1,0 mSv a year
dmin8 = math.log(H8_0 / Hmax8) / mu8                              # cm
out.update({f"{S}-s8-a": round(mu8, 4), f"{S}-s8-a-ln": round(math.log(H8_0 / H8_20), 4),
            f"{S}-s8-b": round(H8, 2), f"{S}-s8-b-exp": round(mu8 * d8, 3), f"{S}-s8-b-e": round(math.exp(-mu8 * d8), 4),
            f"{S}-s8-c": round(D8 / 1000, 3), f"{S}-s8-c-h": hours8, f"{S}-s8-c-uSv": round(D8, 0),
            f"{S}-s8-d": round(dmin8, 2), f"{S}-s8-d-Hmax": round(Hmax8, 3), f"{S}-s8-d-ln": round(math.log(H8_0 / Hmax8), 3),
            f"{S}-s8-d-check": round(H8_0 * math.exp(-mu8 * 24.0), 3), f"{S}-s8-d-half": round(math.log(2) / mu8, 3)})

# s9: Hubble's law (fy8-16/hubble-t; read from the graph): the fitted line passes through (250 Mpc; 18 000 km/s) and the origin
d9, v9 = 250.0, 18000.0
H9 = v9 / d9                                                      # km/s per Mpc
v9b = 8400.0                                                      # km/s, a galaxy
dist9 = v9b / H9                                                  # Mpc
Mpc_km, a_s = 3.086e19, year                                      # km, s
H9_s = H9 / Mpc_km                                                # 1/s
T9 = 1 / H9_s                                                     # s
T9_a = T9 / a_s                                                   # a
out.update({f"{S}-s9-a": round(H9, 2), f"{S}-s9-b": round(dist9, 2), f"{S}-s9-c": round(T9_a, -7),
            f"{S}-s9-c-Hs": H9_s, f"{S}-s9-c-s": T9, f"{S}-s9-c-a": T9_a})

print(json.dumps(out))
