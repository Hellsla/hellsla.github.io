"""FY2 Sovella itsenäisesti: every number of the worked solutions, recomputed from the task data.
Prints {"<task>-<part>": value} for the parts with an answer in tasks.json (and the intermediate values the
solutions show); `python scripts/practice.py check` compares them with tasks.json."""
import json, math

YEAR = 8760.0                       # h
WINTER = 90 * 24.0                  # h, December–February (31 + 31 + 28 days)
E_city = 380.0                      # GWh per year (example)
P_peak = 80.0                       # MW, winter peak (example)
# one unit of each option (example values): rated power MW, capacity factor
gas, bio, wind, solar, nuc, hydro = (50.0, 0.60), (40.0, 0.70), (5.0, 0.32), (10.0, 0.11), (60.0, 0.90), (20.0, 0.50)
# lifecycle emission factors, g/kWh (IPCC AR5 WGIII Annex III, rounded medians, as in the chapter
# "Energiantuotanto, ympäristö ja ilmastonmuutos": onshore wind 11, utility-scale solar 48)
e = {"coal": 820, "gas": 490, "bio": 230, "wind": 11, "solar": 48, "nuc": 12, "hydro": 24}
share_winter = {"city": 0.31, "wind": 0.32, "solar": 0.04}   # share of the year's energy in Dec–Feb (example)
calm = 0.05                          # wind farm output in a calm cold spell, share of rated power (example)

def annual(unit): return unit[0] * unit[1] * YEAR / 1000          # GWh per year of one unit
def tonnes(e_gkwh, E_gwh): return e_gkwh * E_gwh * 1e6 / 1e6      # g/kWh · kWh = g; g → t

# a) one wind turbine and the number needed
E1 = annual(wind)                                   # 14.016 GWh
N_exact = E_city / E1; N = math.ceil(N_exact)       # 27.1 → 28

# b) emissions of 380 GWh
m_coal, m_gas, m_wind = tonnes(e["coal"], E_city), tonnes(e["gas"], E_city), tonnes(e["wind"], E_city)
cut_gas = 1 - m_gas / m_coal; cut_wind = 1 - m_wind / m_coal

# c) the wind farm of N turbines in winter
E_farm = N * E1
P_farm_winter = share_winter["wind"] * E_farm * 1000 / WINTER     # MW
P_city_winter = share_winter["city"] * E_city * 1000 / WINTER     # MW
P_calm = calm * N * wind[0]

# d) solar parks for the same annual energy, in winter
E_sp = annual(solar); N_sp = math.ceil(E_city / E_sp)
P_solar_winter = share_winter["solar"] * N_sp * E_sp * 1000 / WINTER

# e) the model recommendation: 18 wind turbines + the hydro share + one biomass plant as the flexible part
n_w = 18
E_w = n_w * E1; E_h = annual(hydro); E_b = E_city - E_w - E_h
k_b = E_b / (bio[0] * YEAR / 1000)
m_mix = tonnes(e["wind"], E_w) + tonnes(e["hydro"], E_h) + tonnes(e["bio"], E_b)
cut_mix = 1 - m_mix / m_coal
P_peak_local = bio[0] + hydro[0] + calm * n_w * wind[0]
P_import = P_peak - P_peak_local
# other choices mentioned under "Hyväksytään myös"
E_nuc = annual(nuc); E_bio1 = annual(bio); m_bio_all = tonnes(e["bio"], E_city); m_nuc_all = tonnes(e["nuc"], E_city)
E_gas1 = annual(gas)
k_bio2 = E_city / (2 * bio[0] * YEAR / 1000)    # two biomass plants covering the whole year
P_avg = E_city * 1000 / YEAR                     # MW, the city's mean power over the year
P_farm_avg = E_farm * 1000 / YEAR                # MW, the wind farm's mean power over the year
m_parts = [tonnes(e["wind"], E_w), tonnes(e["hydro"], E_h), tonnes(e["bio"], E_b)]
fuel_ratio = k_b / bio[1]                        # chips needed compared with full use
bio_share = E_b / E_city
P_import_no_bio = P_peak - hydro[0] - calm * n_w * wind[0]
cut_bio2 = 1 - m_bio_all / m_coal
P_gap_calm = P_peak - P_calm

out = {"fy2-s1-a": N, "fy2-s1-E1": round(E1, 3), "fy2-s1-N-exact": round(N_exact, 2),
       "fy2-s1-b": round(m_gas), "fy2-s1-m-coal": round(m_coal), "fy2-s1-m-wind": round(m_wind),
       "fy2-s1-cut-gas": round(cut_gas, 3), "fy2-s1-cut-wind": round(cut_wind, 3),
       "fy2-s1-c": round(P_farm_winter, 1), "fy2-s1-E-farm": round(E_farm, 1), "fy2-s1-E-farm-winter": round(share_winter["wind"] * E_farm, 1),
       "fy2-s1-E-city-winter": round(share_winter["city"] * E_city, 1), "fy2-s1-P-city-winter": round(P_city_winter, 1), "fy2-s1-P-calm": round(P_calm, 1),
       "fy2-s1-E-solarpark": round(E_sp, 3), "fy2-s1-N-solar": N_sp, "fy2-s1-E-solar-winter": round(share_winter["solar"] * N_sp * E_sp, 1),
       "fy2-s1-P-solar-winter": round(P_solar_winter, 1),
       "fy2-s1-E-wind18": round(E_w, 1), "fy2-s1-E-hydro": round(E_h, 1), "fy2-s1-E-bio": round(E_b, 1), "fy2-s1-k-bio": round(k_b, 3),
       "fy2-s1-m-mix": round(m_mix), "fy2-s1-cut-mix": round(cut_mix, 3), "fy2-s1-P-local": round(P_peak_local, 1), "fy2-s1-P-import": round(P_import, 1),
       "fy2-s1-E-nuc": round(E_nuc, 1), "fy2-s1-E-bio1": round(E_bio1, 1), "fy2-s1-E-gas1": round(E_gas1, 1),
       "fy2-s1-m-bio-all": round(m_bio_all), "fy2-s1-m-nuc-all": round(m_nuc_all), "fy2-s1-k-bio2": round(k_bio2, 3), "fy2-s1-P-avg": round(P_avg, 1), "fy2-s1-P-farm-avg": round(P_farm_avg, 1), "fy2-s1-m-parts": [round(x) for x in m_parts], "fy2-s1-fuel-ratio": round(fuel_ratio, 3), "fy2-s1-bio-share": round(bio_share, 3), "fy2-s1-P-import-no-bio": round(P_import_no_bio, 1), "fy2-s1-cut-bio2": round(cut_bio2, 3), "fy2-s1-P-gap-calm": round(P_gap_calm, 1)}
print(json.dumps(out))
