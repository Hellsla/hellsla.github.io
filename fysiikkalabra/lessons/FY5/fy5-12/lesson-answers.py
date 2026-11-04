"""Numbers of the lesson text and inquiry.json for fy5-12, computed from their data (python -I lesson-answers.py); the
exercises' answers are in answers.py. The simulation's values are computed exactly as assets/sims/fy5/fy5-12/sim.js
does: sources S1, S2 at (∓d/2, 0) in cm, P at (x, L) on the line L = 8,0 cm, each wave of amplitude 1,0 mm at P
(no decay with distance), y_i = A sin(2π(f t − s_i/λ)), f = v/λ with v = 20 cm/s, and the amplitude at P is the largest
|y1 + y2| over 360 samples of one period. Prints {id: number} as JSON on the last line."""
import json, math

a = {}
L, A, V, NS = 8.0, 1.0, 20.0, 360


def sim(d, lam, x):
    s1, s2 = math.hypot(x + d / 2, L), math.hypot(x - d / 2, L)
    ap = max(abs(A * math.sin(2 * math.pi * (k / NS - s1 / lam)) + A * math.sin(2 * math.pi * (k / NS - s2 / lam))) for k in range(NS))
    return s1, s2, abs(s1 - s2), abs(s1 - s2) / lam, ap


# on load: d = 6,0 cm, λ = 2,0 cm, x = 0
s1, s2, ds, r, ap = sim(6, 2, 0)
a["load-s"], a["load-ds"], a["load-AP"], a["load-f"] = s1, ds, ap, V / 2
# koe 1 (d = 6,0 cm, λ = 2,0 cm locked; P moves along the line): maxima at Δs = 0, 2, 4 cm, minima at 1, 3 cm
for x in (0, 1.4, 3.0, 4.9, 7.4):
    s1, s2, ds, r, ap = sim(6, 2, x)
    a[f"koe1-x{x:g}-ds"], a[f"koe1-x{x:g}-ratio"], a[f"koe1-x{x:g}-AP"] = ds, r, ap
a["koe1-x3-s1"], a["koe1-x3-s2"] = sim(6, 2, 3)[:2]           # 3-4-5 triangle: s1 = 10,0 cm, s2 = 8,0 cm
# koe 2 (d = 6,0 cm, x = 3,0 cm locked, Δs = 2,0 cm; λ varies)
for lam in (1.0, 1.5, 2.0, 2.5, 3.0, 4.0):
    s1, s2, ds, r, ap = sim(6, lam, 3)
    a[f"koe2-lam{lam:g}-ratio"], a[f"koe2-lam{lam:g}-AP"], a[f"koe2-lam{lam:g}-f"] = r, ap, V / lam
# kertaus: λ = v/f for 500 Hz sound
a["kertaus-lam"] = 340 / 500                                   # 0,68 m
# worked example: f = 680 Hz, v = 340 m/s, s1 = 4,25 m, s2 = 3,00 m
lam_e = 340 / 680
a["esim-lam"], a["esim-ds"], a["esim-ratio"] = lam_e, 4.25 - 3.00, (4.25 - 3.00) / lam_e   # 0,50 m; 1,25 m; 2,5
# siirto: first quiet spot beside the centre line, s1 = 5,17 m, s2 = 5,00 m, v = 340 m/s
ds_t = 5.17 - 5.00
a["siirto-ds"], a["siirto-lam"], a["siirto-f"] = ds_t, 2 * ds_t, 340 / (2 * ds_t)          # 0,17 m; 0,34 m; 1000 Hz
a["siirto-wrong-lam-eq-ds"] = 340 / ds_t                                                     # 2000 Hz
a["siirto-wrong-s1"] = 340 / (2 * 5.17)                                                      # 32,9 Hz
# tarkistus 2: ripple tank, f = 10 Hz, v = 20 cm/s, s1 = 13,0 cm, s2 = 9,0 cm, each amplitude 2,0 mm
lam_c = 20 / 10
a["tark2-lam"], a["tark2-ratio"], a["tark2-A"] = lam_c, (13.0 - 9.0) / lam_c, 2 * 2.0        # 2,0 cm; 2; 4,0 mm
# virhe: Δs = 0,80 m, λ = 0,80 m -> Δs/λ = 1, constructive
a["virhe-ratio"] = 0.80 / 0.80
# Fourier figure: f, 3f, 5f with amplitudes 1, 1/3, 1/5 (a square wave's first terms), f = 220 Hz
a["fourier-f1"], a["fourier-f3"], a["fourier-f5"] = 220, 3 * 220, 5 * 220
# exit ticket: smallest destructive Δs not asked; centre line Δs = 0
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
