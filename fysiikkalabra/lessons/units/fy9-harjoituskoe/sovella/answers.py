"""fy9-harjoituskoe (the mock exam): every number of the worked solutions of the ten long tasks (Osa II s1–s7,
Osa III s8–s10), recomputed from the task data, and with -v also the numbers of the Osa I items of inquiry.json.
Prints {"<task>-<part>": value}; `python scripts/practice.py check units/fy9-harjoituskoe` compares them with tasks.json."""
import json, math

g = 9.81
c_w = 4190.0                     # J/(kg K), water
out = {}
extra = {}


def fit(x, y):
    """Least-squares line y = k x + b."""
    mx, my = sum(x) / len(x), sum(y) / len(y)
    k = sum((a - mx) * (b - my) for a, b in zip(x, y)) / sum((a - mx) ** 2 for a in x)
    return k, my - k * mx


def fit0(x, y):
    """Least-squares line through the origin y = k x."""
    return sum(a * b for a, b in zip(x, y)) / sum(a * a for a in x)


# ---------------------------------------------------------------- Osa II
# s1: the electric sauna stove (FY3 heat, FY2 efficiency, FY6 electric energy)
P_kiuas, t_esi = 6.0e3, 50 * 60          # W, s
m_k, c_k, T1, T2 = 25.0, 800.0, 15.0, 280.0
Q_kivet = m_k * c_k * (T2 - T1)          # J, a
E_el = P_kiuas * t_esi                   # J
share = Q_kivet / E_el                   # b
m_l, T_l, r_w = 1.2, 18.0, 2.26e6        # kg, °C, J/kg: ten ladles of water, all evaporated at 100 °C
Q_loyly = m_l * (c_w * (100 - T_l) + r_w)   # J, d
out.update({"fy9-harjoituskoe-s1-a": Q_kivet / 1e6, "fy9-harjoituskoe-s1-b": 100 * share,
            "fy9-harjoituskoe-s1-d": Q_loyly / 1e6})
extra["s1"] = dict(E_el_MJ=E_el / 1e6, E_el_kWh=E_el / 3.6e6, Q_heat=m_l * c_w * (100 - T_l), Q_vap=m_l * r_w,
                   dT_stones=Q_loyly / (m_k * c_k), t_resupply=Q_loyly / P_kiuas)

# s2: a crate on a trailer bed during braking (FY4)
mu0, v0_kmh = 0.45, 80.0
a_max = mu0 * g                          # b
v0 = v0_kmh / 3.6
s_min = v0 ** 2 / (2 * a_max)            # c
out.update({"fy9-harjoituskoe-s2-b": a_max, "fy9-harjoituskoe-s2-c": s_min})
extra["s2"] = dict(v0=v0, t_stop=v0 / a_max, s_at_7=v0 ** 2 / (2 * 7.0))

# s3: the organ pipe in a cold church (FY5 standing waves, FY3 thermal expansion)
L = 1.31                                  # m, open pipe
v20, v8 = 343.2, 336.1                    # m/s, given in the task's table
f20 = v20 / (2 * L)                       # a
f8 = v8 / (2 * L)                         # b
rel = (f8 - f20) / f20
alpha = 2.3e-5                            # 1/K, the pipe alloy
dL = alpha * L * (8.0 - 20.0)             # m, c (negative: the pipe shortens)
rel_L = dL / L                            # the frequency rises by -rel_L because f ∝ 1/L
f_closed = v20 / (4 * L)                  # d
out.update({"fy9-harjoituskoe-s3-a": f20, "fy9-harjoituskoe-s3-b": f8, "fy9-harjoituskoe-s3-c": abs(dL) * 1000})
extra["s3"] = dict(rel_percent=100 * rel, rel_L_percent=100 * rel_L, ratio=abs(rel / rel_L), f_closed=f_closed,
                   f_closed_overtones=[f_closed * k for k in (3, 5)])

# s4: an extension cable on a reel (FY6, effective values of the mains voltage)
rho_cu, l_cord, A15, A25 = 1.68e-8, 25.0, 1.5e-6, 2.5e-6
U, P1, P2 = 230.0, 1.6e3, 1.8e3
R_c = rho_cu * 2 * l_cord / A15           # a, two conductors
R_load = 1 / (P1 / U ** 2 + P2 / U ** 2)  # the grill and the kettle in parallel, resistances as at 230 V
I = U / (R_c + R_load)                    # b
P_loss = I ** 2 * R_c                     # c
U_load = I * R_load
R_c25 = rho_cu * 2 * l_cord / A25
I25 = U / (R_c25 + R_load)
P_loss25 = I25 ** 2 * R_c25               # d
out.update({"fy9-harjoituskoe-s4-a": R_c, "fy9-harjoituskoe-s4-b": I, "fy9-harjoituskoe-s4-c": P_loss,
            "fy9-harjoituskoe-s4-d": P_loss25})
extra["s4"] = dict(R_load=R_load, U_load=U_load, I_approx=(P1 + P2) / U, P_loss_approx=((P1 + P2) / U) ** 2 * R_c,
                   U_drop=I * R_c, I25=I25, ratio=P_loss25 / P_loss)

# s5: the light in the bottom of a diving pool (FY7 refraction, FY3 hydrostatic pressure)
n_w, h_pool, d_win, rho_w = 1.33, 2.40, 0.250, 1000.0
alpha_r = math.degrees(math.asin(1 / n_w))     # a
r_circle = h_pool * math.tan(math.radians(alpha_r))   # b
p_h = rho_w * g * h_pool                       # Pa, the overpressure of the water at the window
F_win = p_h * math.pi * (d_win / 2) ** 2       # d
out.update({"fy9-harjoituskoe-s5-a": alpha_r, "fy9-harjoituskoe-s5-b": r_circle, "fy9-harjoituskoe-s5-d": F_win})
extra["s5"] = dict(p_h=p_h, p_abs=101.3e3 + p_h, area=math.pi * (d_win / 2) ** 2, apparent=h_pool / n_w)

# s6: radiocarbon age of a wooden dugout (FY8 decay law, FY1 uncertainty)
T_half, A0, A, dA = 5730.0, 0.226, 0.198, 0.004       # a, Bq/g
t_age = T_half * math.log(A0 / A) / math.log(2)       # b
t_young = T_half * math.log(A0 / (A + dA)) / math.log(2)
t_old = T_half * math.log(A0 / (A - dA)) / math.log(2)
dt = (t_old - t_young) / 2                            # c
out.update({"fy9-harjoituskoe-s6-b": t_age, "fy9-harjoituskoe-s6-c": dt})
extra["s6"] = dict(ratio=A / A0, t_young=t_young, t_old=t_old, left_200ka=0.5 ** (200e3 / T_half),
                   left_50a=0.5 ** (50 / T_half))

# s7: the squash ball (experimental design; FY4 energy)
h1, h2 = 1.50, 0.36
lost = 1 - h2 / h1                        # b
v_after = math.sqrt(2 * g * h2)           # c
out.update({"fy9-harjoituskoe-s7-b": 100 * lost, "fy9-harjoituskoe-s7-c": v_after})
extra["s7"] = dict(v_before=math.sqrt(2 * g * h1), frame_30=v_after / 30, frame_dist_top=0.5 * g * (1 / 30) ** 2)

# ---------------------------------------------------------------- Osa III
# s8: stacked coffee filters falling at terminal speed (FY4 air resistance, FY1 graphs)
m_f = 1.20e-3                              # kg, one filter
N_f = [1, 2, 3, 4, 5, 6]
v_t = [1.06, 1.45, 1.84, 2.08, 2.39, 2.54]  # m/s, terminal speeds from the video
F_v = [k * m_f * g for k in N_f]           # N, at terminal speed F_v = G
v2 = [v ** 2 for v in v_t]
k_lin, b_lin = fit(v_t, F_v)               # F against v: a line that misses the origin
k_sq = fit0(v2, F_v)                       # F against v^2 through the origin
k_sq_free, b_sq = fit(v2, F_v)
# the slope as read in the solution from two points of the line through the origin
x1, x2 = 0.0, 6.0
k_read = (k_sq * x2 - k_sq * x1) / (x2 - x1)
v10 = math.sqrt(10 * m_f * g / k_sq)       # e
out.update({"fy9-harjoituskoe-s8-b": F_v[3] * 1000, "fy9-harjoituskoe-s8-d": k_read, "fy9-harjoituskoe-s8-e": v10})
extra["s8"] = dict(F_v_mN=[round(f * 1000, 2) for f in F_v], v2=[round(x, 3) for x in v2], k_lin=k_lin, b_lin=b_lin,
                   v_axis_lin=-b_lin / k_lin, k_sq_free=k_sq_free, b_sq=b_sq, F_at_6=k_sq * 6,
                   ratio_v2_v1=v_t[5] / v_t[0], sqrt6=math.sqrt(6))

# s9: a deep geothermal well (source text; FY3 heat, FY8 radioactive heat, FY1 graphs)
z = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0]          # km
T_z = [15.4, 23.3, 32.5, 41.3, 49.2, 58.0]  # °C
k_z, b_z = fit(z, T_z)
z1, z2 = 0.0, 3.0
y1, y2 = b_z + k_z * z1, b_z + k_z * z2
k_read_z = (y2 - y1) / (z2 - z1)            # b, °C/km
T6 = b_z + k_z * 6.0                        # c
q, T_out, T_in = 30.0, 90.0, 40.0           # kg/s, °C
P_geo = c_w * q * (T_out - T_in)            # d
out.update({"fy9-harjoituskoe-s9-b": k_read_z, "fy9-harjoituskoe-s9-c": T6, "fy9-harjoituskoe-s9-d": P_geo / 1e6})
extra["s9"] = dict(k_z=k_z, b_z=b_z, y1=y1, y2=y2, q_for_10MW=10e6 / (c_w * (T_out - T_in)),
                   z_for_120=(120 - b_z) / k_z, depth_steps=[(d, b_z + k_z * d) for d in (4, 5, 6)])

# s10: a spring and its own mass (FY5 oscillator, FY1 graphs)
m_s = [0.100, 0.200, 0.300, 0.400, 0.500, 0.600]   # kg
t10 = [4.37, 5.86, 7.13, 8.19, 9.03, 9.90]         # s
T_s = [t / 10 for t in t10]
T2 = [t ** 2 for t in T_s]
k_T, b_T = fit(m_s, T2)                            # s^2/kg, s^2
xa, xb = 0.0, 0.600
ya, yb = b_T + k_T * xa, b_T + k_T * xb
k_read_T = (yb - ya) / (xb - xa)
k_spring = 4 * math.pi ** 2 / k_read_T             # b
m_eff = b_T / k_T                                  # c: the line meets the m axis at -m_eff
m_static, dx = 0.300, 0.118
k_static = m_static * g / dx                       # d
T_1kg = math.sqrt(k_T * 1.0 + b_T)
out.update({"fy9-harjoituskoe-s10-b": k_spring, "fy9-harjoituskoe-s10-c": m_eff * 1000, "fy9-harjoituskoe-s10-d": k_static})
extra["s10"] = dict(T=T_s, T2=[round(x, 4) for x in T2], k_T=k_T, b_T=b_T, ya=ya, yb=yb, k_read_T=k_read_T,
                    T_ratio_02_01=T_s[1] / T_s[0], T_ratio_06_03=T_s[5] / T_s[2], T_1kg=T_1kg, spring_mass_third=61 / 3,
                    diff_percent=100 * (k_static - k_spring) / k_spring)

# ---------------------------------------------------------------- Osa I (inquiry.json, -v only)
osa1 = {}
osa1["1 area"] = 12.40 * 3.1                        # cm^2 -> 38 cm^2 (two significant figures)
osa1["2 chain"] = 0.40 * 0.95 * 0.30                # -> 11 %
osa1["5 gas"] = (40 + 273.15) / (20 + 273.15)       # -> 1,07
osa1["8 spring T"] = 2 * math.pi * math.sqrt(0.250 / 40.0)
osa1["9 heater R"] = 230.0 ** 2 / 1500.0
osa1["10 photon eV"] = 6.626e-34 * 2.998e8 / 405e-9 / 1.602e-19
osa1["8 mistake no 2pi"] = math.sqrt(0.250 / 40.0)
osa1["8 mistake k/m"] = 2 * math.pi * math.sqrt(40.0 / 0.250)
osa1["9 mistake U/P"] = 230.0 / 1500.0
osa1["9 mistake P/U^2"] = 1500.0 / 230.0 ** 2
osa1["10 mistake J"] = 6.626e-34 * 2.998e8 / 405e-9
osa1["10 mistake hf"] = 6.626e-34 * 2.998e8 / 405 / 1.602e-19

if __name__ == "__main__":
    import sys
    if "-v" in sys.argv:
        for k_, v_ in extra.items(): print(k_, v_)
        for k_, v_ in osa1.items(): print("Osa I", k_, v_)
    print(json.dumps(out))
