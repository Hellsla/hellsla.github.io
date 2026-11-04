"""Numbers of the lesson text and inquiry.json for fy7-9, computed from their data (python -I lesson-answers.py); the
exercises' answers are in answers.py. c = f λ (c = 3,00 · 10⁸ m/s); Wien λ_max T = b (b = 2,898 · 10⁻³ m·K).
The simulation's model values come from the black-body curve (Planck's law, the same constants as sim.js): its
λ_max is found as the curve's highest point, not from Wien's law. Prints {id: number} as JSON."""
import json, math

c, b = 3.00e8, 2.898e-3
H, C, K = 6.62607015e-34, 2.99792458e8, 1.380649e-23       # exact SI constants (as in sim.js)


def M(lam, T):
    """The black body's spectral exitance M_λ in W/(m²·m) (sim.js: the drawn curve)."""
    x = H * C / (lam * K * T)
    return 0.0 if x > 700 else math.pi * 2 * H * C * C / lam ** 5 / math.expm1(x)


def peak(T):
    """λ of the curve's highest point by a golden-section search between 50 nm and 50 µm (sim.js does the same)."""
    lo, hi, g = 50e-9, 50e-6, (math.sqrt(5) - 1) / 2
    for _ in range(120):
        a1, a2 = hi - g * (hi - lo), lo + g * (hi - lo)
        if M(a1, T) > M(a2, T): hi = a2
        else: lo = a1
    return (lo + hi) / 2


SIGMA = 5.670374419e-8                                      # Stefan–Boltzmann constant (the total power per area σT⁴)


def visible(T, n=740):
    """Share of the emitted power in 380–750 nm: midpoint sum on a 0,5 nm grid divided by σT⁴ (as sim.js)."""
    d = (750e-9 - 380e-9) / n
    return sum(M(380e-9 + (i + 0.5) * d, T) for i in range(n)) * d / (SIGMA * T ** 4)


a = {}
a["c"] = c                                                   # 3,00 · 10⁸ m/s
# Ydinajatus: the spectrum's examples (λ = c / f)
a["fm-100MHz"] = c / 100e6                                   # FM radio about 100 MHz: 3,0 m
a["mw-2.45GHz-cm"] = c / 2.45e9 * 100                        # microwave oven: 12 cm
a["vis-f-750nm"] = c / 750e-9                                # visible light 4,0 · 10¹⁴ Hz ...
a["vis-f-380nm"] = c / 380e-9                                # ... 7,9 · 10¹⁴ Hz
# Kaava: Wien examples in the text
a["room-300K-um"] = b / 300 * 1e6                            # 300 K: 9,66 µm -> about 9,7 µm
a["skin-307K-um"] = b / 307 * 1e6                            # skin 34 °C = 307 K: 9,44 µm -> about 9,4 µm
a["glow-800K-um"] = b / 800 * 1e6                            # dull red glow about 800 K: peak 3,6 µm, still infrared
a["sun-5772K-nm"] = b / 5772 * 1e9                           # IAU 2015: T_eff = 5772 K -> 502 nm
a["double-T"] = 0.5                                          # λ_max ∝ 1/T: twice T, half λ_max
a["sb-double"] = 2 ** 4                                      # Stefan–Boltzmann: twice T, 16 times the power per area
# Kaava figure "curves": peaks at 4000, 5000, 6000 K
for T in (4000, 5000, 6000):
    a[f"curves-{T}-nm"] = peak(T) * 1e9                      # 724, 580, 483 nm
    a[f"curves-{T}-MW"] = M(peak(T), T) / 1e12               # MW/(m²·µm): 13,2; 40,2; 100
# Worked example: λ_max = 502 nm -> T = b / λ_max
a["ex-T"] = b / 502e-9                                       # 5773 K -> 5,77 · 10³ K
a["ex-check"] = b / 5772 * 1e9                               # reverse check: 502 nm
# Simulation (model values): koe-1 (0–3000 nm), koe-2 (0–30 µm), the bulb's visible share
for T in (300, 600, 900, 1000, 2700, 3000, 4500, 5800, 6000):
    a[f"sim-lmax-{T}"] = peak(T) * 1e9                       # nm
    a[f"sim-tulo-{T}"] = peak(T) * T * 1e3                   # λ_max T in 10⁻³ m·K: 2,898 every time
for T in (800, 2700, 5800):
    a[f"sim-nakyva-{T}"] = visible(T) * 100                  # % of the power in 380–750 nm: 2700 K about 7 %, 5800 K 44 %
# virhe: hob element 900 °C; the wrong one uses 900 as if kelvins
a["virhe-wrong-um"] = b / 900 * 1e6                          # 3,22 µm
a["virhe-right-um"] = b / (900 + 273.15) * 1e6               # T = 1173,15 K: 2,47 µm
# siirto: tungsten filament 2430 °C
a["siirto-T"] = 2430 + 273.15                                # 2703,15 K
a["siirto"] = b / a["siirto-T"] * 1e9                        # λ_max = 1072 nm -> 1,07 · 10³ nm
a["siirto-celsius"] = b / 2430 * 1e9                         # mistake: °C as kelvins, 1193 nm
a["siirto-um"] = a["siirto"] / 1e3                           # mistake: answered in µm, 1,07
# tarkistus-2: lava, peak 2,1 µm
a["check-T-K"] = b / 2.1e-6                                  # 1380 K
a["check"] = b / 2.1e-6 - 273.15                             # 1107 °C -> 1,1 · 10³ °C
# exit ticket: T three times -> λ_max to a third
a["exit-third"] = 1 / 3
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
