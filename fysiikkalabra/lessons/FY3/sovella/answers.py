"""FY3 Sovella itsenäisesti: every number of the worked solutions, recomputed from the task data.
Prints {"<task>-<part>": value} for the parts with an answer in tasks.json (and a few intermediate values);
`python scripts/practice.py check` compares them with tasks.json."""
import json

c_w, r_w = 4190.0, 2.26e6          # water: J/(kg·K), J/kg (the course's tables)
g, rho = 9.81, 1000.0

# fy3-s1: the solar collector
m = 4.00; C = c_w * m                                  # J/K
t = list(range(0, 65, 5))
T = [20.0, 24.1, 28.0, 31.6, 35.0, 38.0, 40.9, 43.8, 46.2, 48.5, 50.7, 52.8, 54.7]
start = 0.85                                           # K/min, the tangent at the start as read in the solution
P_sun = C * start / 60                                 # W into the water
P_in = 800 * 0.50
eta = P_sun / P_in
late = (T[t.index(60)] - T[t.index(40)]) / 20          # K/min around 50 min (the chord 40–60 min)
P_loss = P_sun - C * late / 60
secant5 = (T[1] - T[0]) / 5; secant10 = (T[2] - T[0]) / 10   # the accepted range of start rates

# fy3-s2: the pressure cooker
p_tab = [70.2, 84.6, 101.3, 120.9, 143.4, 169.2, 198.7, 232.3]; T_tab = [90, 95, 100, 105, 110, 115, 120, 125]
p_abs = 101 + 80
i = next(k for k in range(len(p_tab) - 1) if p_tab[k] <= p_abs <= p_tab[k + 1])
T_boil = T_tab[i] + (T_tab[i + 1] - T_tab[i]) * (p_abs - p_tab[i]) / (p_tab[i + 1] - p_tab[i])
E = 0.80 * 300 * 20 * 60
m_evap = E / r_w
frac = c_w * (round(T_boil) - 100) / r_w
m_left = 1.50 - round(m_evap, 2); m_steam = frac * m_left
V_steam = m_steam / 0.018 * 8.314 * 373.15 / 101.3e3 * 1000   # litres of steam as an ideal gas

# fy3-s3: diving
p0 = 101e3; h = 15.0
p_deep = p0 + rho * g * h
V_bubble = 4.0 * p_deep / p0 * (20.0 + 273.15) / (6.0 + 273.15)
V_lungs = 6.0 * p_deep / p0
dp = (200 - 50) * 100e3                               # Pa, the same as the difference of absolute pressures
V_usable = dp * 12.0 / p_deep                          # litres at the depth's pressure
minutes = V_usable / 20
surface_minutes = dp * 12.0 / p0 / 20

out = {"fy3-s1-b": round(P_sun, 1), "fy3-s1-c": round(eta, 3), "fy3-s1-d": round(P_loss, 1),
       "fy3-s1-rate-late": round(late, 3), "fy3-s1-secant5": round(secant5, 3), "fy3-s1-secant10": round(secant10, 3),
       "fy3-s1-b-low": round(C * secant10 / 60, 1),
       "fy3-s2-a": round(T_boil, 2), "fy3-s2-c": round(m_evap, 4), "fy3-s2-E": E, "fy3-s2-d": round(frac, 4), "fy3-s2-steam-g": round(m_steam * 1000, 1), "fy3-s2-steam-l": round(V_steam, 1),
       "fy3-s3-p": round(p_deep / 1000, 2), "fy3-s3-a": round(V_bubble, 2), "fy3-s3-b": round(V_lungs, 2),
       "fy3-s3-usable": round(V_usable, 1), "fy3-s3-c": round(minutes, 2), "fy3-s3-surface": round(surface_minutes, 1)}
print(json.dumps(out))
