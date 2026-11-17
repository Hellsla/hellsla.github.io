"""Numbers of the lesson text and inquiry.json for fy5-17, computed from their data (python -I lesson-answers.py); the
exercises' answers are in answers.py. Echo depth d = v t / 2; wavelength λ = v / f; earthquake distance from the S−P time
difference d = vP vS Δt / (vP − vS); shallow-water wave v = √(g h). Reflected fractions from typical acoustic impedances
R = ((Z2 − Z1)/(Z2 + Z1))² (the lesson gives only the rounded fractions). Prints {id: number} as JSON."""
import json, math

g = 9.81
v_tissue, v_air, v_water, v_eye = 1540.0, 343.0, 1480.0, 1550.0     # m/s; v_eye: mean speed used in eye A-scans
vP, vS = 6.0, 3.5                                                      # km/s, upper crust (IASP91: 5,8 and 3,36)
a = {}

# Kertaus (luku Mekaaninen aaltoliike): bat call 40 kHz in air, λ = v / f
a["kertaus-lambda-mm"] = v_air / 40e3 * 1e3            # 8,575 mm
a["kertaus-vf"] = v_air * 40e3                         # wrong option v·f = 1,372e7 m
a["kertaus-fv"] = 40e3 / v_air                         # wrong option f/v = 116,6

# Ennuste 1: echo after 65 µs, v = 1540 m/s
a["ennuste1-d-cm"] = v_tissue * 65e-6 / 2 * 100        # 5,005 cm
a["ennuste1-vt-cm"] = v_tissue * 65e-6 * 100           # 10,01 cm (forgetting the return trip)

# Rajapinnat: reflected fraction of the intensity, typical acoustic impedances in MRayl
Z = {"ilma": 0.0004, "geeli": 1.50, "iho": 1.63, "rasva": 1.38, "lihas": 1.70, "pehmytkudos": 1.63, "luu": 7.8}
R = lambda z1, z2: ((z2 - z1) / (z2 + z1)) ** 2
a["R-geeli-iho-%"] = 100 * R(Z["geeli"], Z["iho"])                  # 0,17 % -> "noin 0,2 %"
a["R-ilma-iho-%"] = 100 * R(Z["ilma"], Z["iho"])                    # 99,90 %
a["R-rasva-lihas-%"] = 100 * R(Z["rasva"], Z["lihas"])              # 1,08 % -> "noin 1 %"
a["R-kudos-luu-%"] = 100 * R(Z["pehmytkudos"], Z["luu"])            # 42,8 % -> "noin 40 %"

# A-kuvaus (figure a-scan): echoes A, B, C at 20, 50, 90 µs
for k, t in (("A", 20e-6), ("B", 50e-6), ("C", 90e-6)):
    a[f"ascan-{k}-cm"] = v_tissue * t / 2 * 100        # 1,54 · 3,85 · 6,93 cm
a["ascan-BC-cm"] = v_tissue * (90e-6 - 50e-6) / 2 * 100   # thickness between B and C: 3,08 cm
a["ascan-BC-noHalf-cm"] = v_tissue * 40e-6 * 100          # mistake: no halving, 6,16 cm

# Frequency table: λ = v / f in soft tissue
for f in (2.5, 5, 10, 15):
    a[f"lambda-{f}MHz-mm"] = v_tissue / (f * 1e6) * 1e3   # 0,616 · 0,308 · 0,154 · 0,103 mm
a["lambda-3MHz-mm"] = v_tissue / 3e6 * 1e3                # 0,513 mm (figure taajuus)
a["lambda-12MHz-mm"] = v_tissue / 12e6 * 1e3              # 0,128 mm

# Bats and dolphins: λ = v / f
a["bat-50kHz-mm"] = v_air / 50e3 * 1e3                 # 6,86 mm
a["dolphin-100kHz-mm"] = 1500 / 100e3 * 1e3            # 15 mm

# Seismograms (figure seismogrammit): stations at 84, 168 and 252 km
k_ps = vP * vS / (vP - vS)                             # km of distance per second of S−P difference: 8,4 km/s
a["km-per-s"] = k_ps
for d in (84, 168, 252):
    a[f"seis-{d}-P"] = d / vP                          # 14, 28, 42 s
    a[f"seis-{d}-S"] = d / vS                          # 24, 48, 72 s
    a[f"seis-{d}-dt"] = d / vS - d / vP                # 10, 20, 30 s
a["seis-mistake-P"] = 84 / 14                          # mistake: distance / P time = vP = 6,0 km/s
a["seis-mistake-S"] = 84 / 24                          # mistake: distance / S time = vS = 3,5 km/s

# Esimerkki: P at 12.04.18, S at 12.04.43, Δt = 25 s
dt_ex = 25.0
a["esim-d-km"] = k_ps * dt_ex                          # 210 km
a["esim-tP-s"] = a["esim-d-km"] / vP                   # 35 s: the quake at 12.03.43
a["esim-tS-s"] = a["esim-d-km"] / vS                   # 60 s, 60 − 35 = 25 s
a["esim-1-over"] = 1 / vS - 1 / vP                     # 0,119 s/km

# Kulkuaika figure: d = 210 km as in the example (t_P 35 s, t_S 60 s)

# Tsunami: v = √(g h)
a["tsunami-4000"] = math.sqrt(g * 4000)                # 198,1 m/s
a["tsunami-4000-kmh"] = math.sqrt(g * 4000) * 3.6      # 713 km/h
a["tsunami-100"] = math.sqrt(g * 100)                  # 31,3 m/s
a["tsunami-10"] = math.sqrt(g * 10)                    # 9,90 m/s
a["tsunami-10-kmh"] = math.sqrt(g * 10) * 3.6          # 35,7 km/h

# Etsi virhe: Δt = 20 s
a["virhe-wrong-km"] = (vP - vS) * 20                   # 50 km, the student's (vP − vS) Δt
a["virhe-right-km"] = k_ps * 20                        # 168 km
a["virhe-right-tP"] = 168 / vP                          # 28 s
a["virhe-right-tS"] = 168 / vS                          # 48 s
a["virhe-mean-km"] = (vP + vS) / 2 * 20                # 95 km with the mean speed
a["virhe-mean-tP"] = a["virhe-mean-km"] / vP           # 15,8 s
a["virhe-mean-tS"] = a["virhe-mean-km"] / vS           # 27,1 s
a["virhe-mean-dt"] = a["virhe-mean-tS"] - a["virhe-mean-tP"]   # 11,3 s, not 20 s

# Siirto: tsunami 2000 km over 4,0 km deep ocean
v_ts = math.sqrt(g * 4000)
a["siirto-h"] = 2000e3 / v_ts / 3600                   # 2,804 h
a["siirto-mistake-km-depth"] = 2000e3 / math.sqrt(g * 4.0) / 3600   # depth left in km: 88,7 h
a["siirto-mistake-min"] = 2000e3 / v_ts / 60           # answered in minutes: 168,3
a["siirto-mistake-s"] = 2000e3 / v_ts                  # answered in seconds: 10 096

# Tarkistus 2: eye A-scan, echo from the retina 31,0 µs after the cornea echo, v = 1550 m/s
a["silma-cm"] = v_eye * 31.0e-6 / 2 * 100              # 2,40 cm
a["silma-noHalf-cm"] = v_eye * 31.0e-6 * 100           # 4,81 cm
a["silma-1540-cm"] = v_tissue * 31.0e-6 / 2 * 100      # 2,39 cm (with the soft-tissue speed)

# Exit ticket: bat call at 50 kHz and at 1 kHz in air
a["exit-50kHz-mm"] = v_air / 50e3 * 1e3              # 6,86 mm
a["exit-1kHz-cm"] = v_air / 1e3 * 100                  # 34,3 cm

print(json.dumps({k: round(v, 6) for k, v in a.items()}, ensure_ascii=False))
