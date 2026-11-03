"""Numbers of the lesson text and inquiry.json for fy5-14, computed from their data (python -I lesson-answers.py); the
exercises' answers are in answers.py. Sound in air at v = 340 m/s (about 15 °C, as in the earlier chapters); v = f λ;
harmonic series f_n = n f_1; beats f_h = |f1 − f2|; Doppler with speeds measured relative to the air at rest:
moving source f = f0 v/(v ∓ v_s) (− approaching), moving listener f = f0 (v ± v_h)/v (+ approaching).
The simulation's model is reproduced here: wavefront k leaves the source at t_k = k/f0 from x_s(t_k) and travels at v;
the time it reaches a listener at x_o(t) = x_o0 + v_o t is solved from the geometry, and the heard frequency is one over
the interval between two successive arrivals (the sim never uses the Doppler formulas). Prints {id: number} as JSON."""
import json, math

a = {}
V = 340.0                                                   # speed of sound in air used in the whole chapter, m/s


def arrivals(f0, vs, vo, side, xs0=1.5, xo0=None):
    """Heard frequency and wavelength at a listener ahead (side +1, to the right) or behind (side −1) of the source,
    as sim.js computes them: arrival times of two successive wavefronts, and their spacing at one instant."""
    xo0 = xo0 if xo0 is not None else (5.6 if side > 0 else 0.4)
    T0 = 1 / f0
    def t_arr(te):
        xe = xs0 + vs * te
        return (xo0 - xe + V * te) / (V - vo) if side > 0 else (xe - xo0 + V * te) / (V + vo)
    f = 1 / (t_arr(T0) - t_arr(0))
    lam = abs((V - side * vs) * T0)                         # fronts emitted T0 apart, seen at one instant
    return f, lam


# Sim on load: f0 = 400 Hz, u = 0: both listeners hear 400 Hz, λ = 0,85 m
a["sim-load-f"], a["sim-load-lam"] = arrivals(400, 0, 0, +1)
# Koe 1 (source moves towards A, away from B) and koe 2 (both listeners move left: A towards, B away), f0 = 400 Hz
for u in (0, 34, 68, 102, 136):
    a[f"koe1-fA-{u}"], a[f"koe1-lamA-{u}"] = arrivals(400, u, 0, +1)
    a[f"koe1-fB-{u}"], a[f"koe1-lamB-{u}"] = arrivals(400, u, 0, -1)
    a[f"koe2-fA-{u}"], a[f"koe2-lamA-{u}"] = arrivals(400, 0, -u, +1)
    a[f"koe2-fB-{u}"], a[f"koe2-lamB-{u}"] = arrivals(400, 0, -u, -1)
# the formulas agree with the sim's counting
a["check-source"] = 400 * V / (V - 34)                      # 444,4 Hz
a["check-listener"] = 400 * (V + 34) / V                    # 440 Hz
a["shift-small"] = 400 * 34 / V                              # f0 u / v = 40 Hz: both shifts at a small speed
# Prediction 2: at u = 102 m/s the moving source gives 571 Hz, the moving listener 520 Hz
a["ennuste2-source"] = 400 * V / (V - 102)
a["ennuste2-listener"] = 400 * (V + 102) / V

# Ydinajatus: wavelengths at the limits of hearing, λ = v/f
a["lambda-20Hz"] = V / 20                                   # 17 m
a["lambda-20kHz"] = V / 20000 * 100                         # 1,7 cm
a["v-15C"] = 331 + 0.6 * 15                                 # about 340 m/s at 15 °C
a["v-20C"] = 331 + 0.6 * 20                                 # 343 m/s
# Speech: pressure amplitude about 0,02 Pa against 101 kPa
a["pressure-ratio-e7"] = 0.02 / 101e3 * 1e7                 # 2,0 · 10^-7 of the air pressure
# Timbre figure: guitar-like tone at 220 Hz, harmonics 220, 440, 660, 880, 1100 Hz
for k in range(1, 6): a[f"sointi-f{k}"] = 220 * k
# FFT: a 0,10 s recording resolves 1/0,10 s = 10 Hz; 20 000 samples per second reach 10 kHz
a["fft-resolution"] = 1 / 0.10
a["fft-max"] = 20000 / 2
# Octave: A4 440 Hz, A5 880 Hz
a["octave"] = 2 * 440

# Spectrum task (figure spektri-tehtava): peaks 200, 400, 600, 800, 1000 Hz, the strongest at 400 Hz
for k in range(1, 6): a[f"spektri-f{k}"] = 200 * k
a["spektri-ratio"] = 400 / 200
# Beats task (figure huojunta-tehtava): 440 Hz and 444 Hz; loud moments 0,25 s apart; f_h = 4,0 Hz; heard pitch 442 Hz
a["huojunta-fh"] = abs(444 - 440)
a["huojunta-Th"] = 1 / a["huojunta-fh"]
a["huojunta-mean"] = (440 + 444) / 2
a["huojunta-m-period"] = 1 / 0.5                            # mistake: reading two loud moments as one period, 2 Hz

# Worked example: train horn 311 Hz, 108 km/h; before and after passing; change of pitch
vs_ex = 108 / 3.6                                           # 30,0 m/s
a["esim-vs"] = vs_ex
a["esim-f1"] = 311 * V / (V - vs_ex)                        # 341,1 Hz
a["esim-f2"] = 311 * V / (V + vs_ex)                        # 285,8 Hz
a["esim-df"] = a["esim-f1"] - a["esim-f2"]                  # 55,3 Hz
a["esim-estimate"] = 2 * 311 * vs_ex / V                    # 54,9 Hz

# Error spotting: whistle 620 Hz on a scooter approaching at 20,0 m/s; written with v + v_s
a["virhe-wrong"] = 620 * V / (V + 20)                       # 585,6 Hz
a["virhe-right"] = 620 * V / (V - 20)                       # 658,8 Hz

# Transfer: buzzer 2,00 kHz whirled on a string, r = 1,00 m, T = 0,500 s; the highest heard frequency
vs_b = 2 * math.pi * 1.00 / 0.500                           # 12,57 m/s
a["siirto-vs"] = vs_b
a["siirto"] = 2000 * V / (V - vs_b)                         # 2076,7 Hz
a["siirto-min"] = 2000 * V / (V + vs_b)                     # 1928,7 Hz
a["siirto-m-plus"] = a["siirto-min"]                        # mistake: v + v_s gives the lowest, 1929 Hz
a["siirto-m-no2pi"] = 2000 * V / (V - 1.00 / 0.500)         # mistake: v = r/T, 2011,8 Hz

# Check 2: two microphones 1,20 m apart, delay 3,50 ms
a["tark2"] = 1.20 / 3.50e-3                                 # 342,9 m/s
a["tark2-m-ms"] = 1.20 / 3.50                               # mistake: ms not converted, 0,343
a["tark2-m-double"] = 2 * 1.20 / 3.50e-3                    # mistake: doubled distance as for an echo, 686 m/s

# Retrieval: string f1 = 110 Hz, eigenfrequencies 220, 330, 440 Hz
for k in (2, 3, 4): a[f"kertaus-f{k}"] = 110 * k

# Exit ticket: 440 Hz and 437 Hz: f_h = 3 Hz, heard pitch 438,5 Hz
a["exit-fh"] = abs(440 - 437)
a["exit-mean"] = (440 + 437) / 2
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
