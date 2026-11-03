"""Numbers of the lesson text and inquiry.json for fy5-15, computed from their data (python -I lesson-answers.py); the
exercises' answers are in answers.py. Sound intensity I = P/A, a point source radiating evenly in every direction
I = P/(4πr²) (no reflections, no absorption in the air), intensity level L = 10 dB · lg(I/I0) with the hearing
threshold I0 = 1,0 · 10⁻¹² W/m², and I = I0 · 10^(L / 10 dB). Independent sources: the intensities add.
The simulation's model is the same: N equal loudspeakers of power P each at one point, the meter at distance r,
I = N P / (4π r²). Prints {id: number} as JSON."""
import json, math

I0 = 1.0e-12                                              # hearing threshold, W/m²
lg = math.log10
L = lambda I: 10 * lg(I / I0)                             # intensity level, dB
I_of = lambda Ldb: I0 * 10 ** (Ldb / 10)                  # intensity from the level, W/m²
I_point = lambda P, r: P / (4 * math.pi * r ** 2)         # point source, W/m²
a = {}

# --- simulation on load and the experiments: P = 50 mW, one speaker, r = 2,0 m ---
a["sim-load-I"] = I_point(0.050, 2.0)                     # 0,050 W / (4π · 4,0 m²) = 9,947e-4 W/m²
a["sim-load-L"] = L(a["sim-load-I"])                      # 89,98 dB -> 90,0 dB on the readout
a["sim-load-A"] = 4 * math.pi * 2.0 ** 2                  # sphere area 50,27 m²
for r in (1, 2, 4, 8):                                    # koe 1: vary r, P = 50 mW, N = 1
    a[f"koe1-r{r}-ImW"] = I_point(0.050, r) * 1e3        # 3,979 / 0,9947 / 0,2487 / 0,06217 mW/m²
    a[f"koe1-r{r}-L"] = L(I_point(0.050, r))              # 96,0 / 90,0 / 83,9(6) / 77,9(4) dB
a["koe1-step"] = L(I_point(0.050, 2)) - L(I_point(0.050, 4))   # doubling r: 10 lg 4 = 6,02 dB less
for N in (1, 2, 4, 10):                                   # koe 2: vary N, P = 50 mW, r = 2,0 m
    a[f"koe2-N{N}-L"] = L(N * I_point(0.050, 2.0))        # 90,0 / 93,0 / 96,0 / 100,0 dB
a["koe2-step2"] = 10 * lg(2)                              # doubling the intensity: +3,01 dB
a["koe2-step10"] = 10 * lg(10)                            # ten-fold: +10 dB

# --- theory: thresholds and rules ---
a["pain-L"] = L(1.0)                                      # pain threshold about 1 W/m² -> 120 dB
a["pain-ratio"] = 1.0 / I0                                # 10^12
a["L60-I"] = I_of(60)                                     # 60 dB -> 1,0e-6 W/m²
a["sum-equal-80"] = L(2 * I_of(80))                       # 80 dB + 80 dB -> 83,0 dB
a["sum-70-60"] = L(I_of(70) + I_of(60))                   # 70 dB + 60 dB -> 70,4 dB
a["sum-70-60-I"] = I_of(70) + I_of(60)                    # 1,1e-5 W/m²
a["graph-P"] = 4 * math.pi * 1.0 ** 2 * 1e-3              # Kaava graph: I(1 m) = 1,0e-3 W/m², so P = 4π · 10⁻³ W = 12,6 mW
for r in (1, 2, 4, 8):
    a[f"graph-r{r}"] = L(I_point(a["graph-P"], r))        # 90,0 / 84,0 / 78,0 / 71,9 dB

# --- worked example: 96 dB at 10 m from a loudspeaker tower ---
a["ex-ratio"] = 10 ** (96 / 10)                           # I/I0 = 10^9,6 = 3,98e9
a["ex-I"] = I_of(96)                                      # 3,981e-3 W/m²
a["ex-A"] = 4 * math.pi * 10 ** 2                         # 1256,6 m²
a["ex-P"] = a["ex-I"] * a["ex-A"]                         # 5,003 W -> 5,0 W
a["ex-check-90"] = I_of(90) * a["ex-A"]                   # 90 dB would give 1,26 W, 100 dB 12,6 W
a["ex-check-100"] = I_of(100) * a["ex-A"]

# --- misconception: doubling the decibels ---
a["mis-60-120-ratio"] = I_of(120) / I_of(60)              # 10^6

# --- inquiry: predictions use the experiments above; the transfer task (siirto) ---
I_near = I_of(80)                                         # nearer speaker 2,0 m away gives 80 dB alone: 1,0e-4 W/m²
I_far = I_near * (2.0 / 4.0) ** 2                         # the same speaker 4,0 m away: a quarter, 2,5e-5 W/m²
a["siirto-Ifar"] = I_far
a["siirto-Lfar"] = L(I_far)                               # 73,98 dB
a["siirto-Lsum"] = L(I_near + I_far)                      # 80,97 dB
a["siirto"] = L(I_near + I_far) - 80                      # answer: 0,969 dB -> 0,97 dB
a["siirto-mis-equal"] = 10 * lg(2)                        # mistake: both treated as 80 dB -> 3,0 dB
a["siirto-mis-1r"] = L(I_near + I_near * 0.5) - 80        # mistake: I ∝ 1/r -> 1,76 dB
# error spotting (virhe): 65 dB -> I = 10^6,5 · I0 = 3,16e-6 W/m² (the student wrote 6,5e-12)
a["virhe-I"] = I_of(65)
a["virhe-wrong"] = 6.5 * I0
# checks: tarkistus-2, 50 dB -> 70 dB
a["tarkistus-2"] = I_of(70) / I_of(50)                    # 100
# exit ticket: 80 dB -> 1,0e-4 W/m²; three equal 80 dB machines -> 84,8 dB
a["exit-1"] = I_of(80)
a["exit-2"] = L(3 * I_of(80))                             # 84,77 dB
print(json.dumps({k: round(v, 6) if abs(v) >= 1e-3 else float(f"{v:.6g}") for k, v in a.items()}))
