"""Numbers of the lesson text and inquiry.json for fy5-9, computed from their data (python -I lesson-answers.py); the
exercises' answers are in answers.py. Spring oscillator T = 2π√(m/k); mathematical pendulum: the exact period of
α'' = −(g/l) sin α is T = 2π√(l/g) / AGM(1, cos(α0/2)), which the simulation's integration reproduces, and
T = 2π√(l/g) for small swings; E = ½kA²; g = 9,81 m/s². Prints {id: number} as JSON."""
import json, math

g, pi = 9.81, math.pi
a = {}


def agm(x, y):
    for _ in range(40): x, y = (x + y) / 2, math.sqrt(x * y)
    return x


def T_spring(m, k): return 2 * pi * math.sqrt(m / k)
def T_pend(l, deg): return 2 * pi * math.sqrt(l / g) / agm(1, math.cos(math.radians(deg) / 2))


# Kertaus (luku Harmoninen voima ...): k = 40 N/m, x = 0,050 m: F = kx = 2,0 N towards the equilibrium
a["kertaus-F"] = 40 * 0.050
a["kertaus-F-cm"] = 40 * 5                                # mistake: x in centimetres, 200
# Koe 1: spring, m = 0,50 kg, k = 20 N/m, amplitude A varied
for A in (0.05, 0.10, 0.20):
    a[f"koe1-T-{A}"] = T_spring(0.50, 20)                 # 0,9935 s for every amplitude
    a[f"koe1-vmax-{A}"] = A * math.sqrt(20 / 0.50)        # v_max = A√(k/m): 0,316 · 0,632 · 1,265 m/s
    a[f"koe1-E-{A}"] = 0.5 * 20 * A ** 2                  # E = ½kA²: 0,025 · 0,100 · 0,400 J
# Koe 2: spring, k = 20 N/m, A = 0,10 m, mass varied
for m in (0.20, 0.50, 0.80, 2.00):
    a[f"koe2-T-{m}"] = T_spring(m, 20)                    # 0,628 · 0,993 · 1,257 · 1,987 s: four times the mass, twice T
# Koe 3: pendulum l = 1,00 m, α0 = 10°, mass varied: the mass cancels from α'' = −(g/l) sin α
a["koe3-T"] = T_pend(1.00, 10)                            # 2,0099 s for 0,10 · 0,50 · 1,00 kg
a["koe3-T0"] = 2 * pi * math.sqrt(1.00 / g)               # small-swing formula 2,0061 s (0,2 % less)
for m in (0.10, 0.50, 1.00):
    a[f"koe3-E-{m}"] = m * g * 1.00 * (1 - math.cos(math.radians(10)))   # E = mgl(1 − cos α0): 0,0149 · 0,0745 · 0,149 J
# Koe 4: pendulum m = 0,50 kg, α0 = 10°, length varied
for l in (0.25, 0.50, 1.00, 1.50):
    a[f"koe4-T-{l}"] = T_pend(l, 10)                      # 1,0050 · 1,4212 · 2,0099 · 2,4616 s: four times the length, twice T
# Koe 5 (optional): pendulum l = 1,00 m, release angle varied
for d in (5, 10, 20, 40, 60):
    a[f"koe5-T-{d}"] = T_pend(1.00, d)                    # 2,0071 · 2,0099 · 2,0216 · 2,0690 · 2,1529 s
    a[f"koe5-ratio-{d}"] = T_pend(1.00, d) / (2 * pi * math.sqrt(1.00 / g))   # 1,0005 · 1,0019 · 1,0077 · 1,0313 · 1,0732
# Worked example: m = 0,400 kg, 10 periods in 8,00 s: T = 0,800 s, k = 4π²m/T²
T_ex = 8.00 / 10
a["ex-T"] = T_ex
a["ex-k"] = 4 * pi ** 2 * 0.400 / T_ex ** 2               # 24,674 N/m -> 24,7 N/m
a["ex-f"] = 1 / T_ex                                      # 1,25 Hz
a["ex-check-T"] = T_spring(0.400, 25)                     # check with k = 25 N/m: 0,795 s ≈ 0,800 s
# Mittaus: pendulum l = 1,000 m, five timings of 10 periods (keksitty esimerkkiaineisto)
t10 = [20.12, 19.94, 20.21, 19.88, 20.05]
mean10 = sum(t10) / len(t10)
a["mittaus-mean10"] = mean10                              # 20,04 s
a["mittaus-T"] = mean10 / 10                              # 2,004 s
a["mittaus-dT"] = 0.2 / 10                                # hand timing ±0,2 s over ten periods: ΔT = 0,02 s
a["mittaus-halfrange"] = (max(t10) - min(t10)) / 2        # 0,165 s: the scatter agrees with the ±0,2 s estimate
a["mittaus-Tformula"] = 2 * pi * math.sqrt(1.000 / g)     # 2,006 s
a["mittaus-g"] = 4 * pi ** 2 * 1.000 / (mean10 / 10) ** 2 # g = 4π²l/T² = 9,830 m/s²
a["mittaus-g-lo"] = 4 * pi ** 2 * 1.000 / (mean10 / 10 + 0.02) ** 2   # T + ΔT: 9,64 m/s²
a["mittaus-g-hi"] = 4 * pi ** 2 * 1.000 / (mean10 / 10 - 0.02) ** 2   # T − ΔT: 10,03 m/s²
a["mittaus-g-10T"] = 4 * pi ** 2 * 1.000 / mean10 ** 2    # mistake: 10T used as T, 0,0983 m/s²
a["mittaus-g-noSq"] = 4 * pi ** 2 * 1.000 / (mean10 / 10) # mistake: T not squared, 19,7
# Virhe: l = 0,80 m with the ratio upside down
a["virhe-wrong"] = 2 * pi * math.sqrt(g / 0.80)           # 22,0 "s" (really 1/s)
a["virhe-right"] = 2 * pi * math.sqrt(0.80 / g)           # 1,794 s
# Siirto: astronaut's mass in weightlessness, chair 10,0 kg, k = 1200 N/m, 10 periods 16,6 s
T_s = 16.6 / 10
m_tot = 1200 * T_s ** 2 / (4 * pi ** 2)                   # 83,76 kg
a["siirto-m"] = m_tot - 10.0                              # 73,76 kg -> 73,8 kg
a["siirto-mtot"] = m_tot                                  # mistake: chair not subtracted, 83,8
a["siirto-10T"] = 1200 * 16.6 ** 2 / (4 * pi ** 2) - 10.0 # mistake: 10T as T, 8366
a["siirto-noSq"] = 1200 * T_s / (4 * pi ** 2) - 10.0      # mistake: T not squared, 40,5
# Tarkistus 2: figure kuvaaja-k, maxima at 0, 0,40 and 0,80 s, m = 0,25 kg: k = 4π²m/T²
a["t2-k"] = 4 * pi ** 2 * 0.25 / 0.40 ** 2               # 61,685 N/m -> 62 N/m
a["t2-half"] = 4 * pi ** 2 * 0.25 / 0.20 ** 2            # mistake: half a period read as T, 246,7
a["t2-noSq"] = 4 * pi ** 2 * 0.25 / 0.40                 # mistake: T not squared, 24,7
a["t2-f"] = 1 / 0.40                                     # 2,5 Hz
# Tarkistus 1: on the Moon (g/6) a pendulum's period grows √6 times, a spring's stays
a["t1-ratio"] = math.sqrt(6)                             # 2,45
# Figures: energy graph k = 20 N/m, A = 0,10 m; the x(t) figure T = 1,0 s
a["fig-E"] = 0.5 * 20 * 0.10 ** 2                         # 0,10 J
a["fig-Ep-half"] = 0.5 * 20 * 0.05 ** 2                   # at x = A/2: E_p = 0,025 J = E/4, so E_k = 0,075 J
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
