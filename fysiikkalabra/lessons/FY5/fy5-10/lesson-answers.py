"""Numbers of the lesson text and inquiry.json for fy5-10, computed from their data (python -I lesson-answers.py); the
exercises' answers are in answers.py. Model: a wave from a source at x = 0 that starts at t = 0,
y(x, t) = A sin(2πf (t − x/v)) where t − x/v ≥ 0 (zero ahead of the front), v set by the medium, f by the source, λ = v/f.
The simulation (assets/sims/fy5/fy5-10/sim.js) uses exactly this model with A = 5,0 cm, v = 2,0 m/s (suuri jännitys)
or 1,0 m/s (pieni jännitys) and the marked point P at x = 1,00 m. Prints {id: number} as JSON on the last line."""
import json, math

a = {}
A_cm, V = 5.0, {"suuri": 2.0, "pieni": 1.0}            # sim: amplitude (cm), wave speed per tension (m/s)
xP = 1.00                                               # sim: the marked point P (m)


def y_at(x, t, f, v, pulse=False):                      # displacement (cm) of the point x at time t
    tau = t - x / v
    if tau < 0 or (pulse and tau > 1 / (2 * f)): return 0.0
    return A_cm * math.sin(2 * math.pi * f * tau)


def max_disp(f, v, t_end, dt=1 / 60):                   # largest |y| of P over a run sampled at 60 frames/s (sim draw loop)
    return max(abs(y_at(xP, k * dt, f, v)) for k in range(int(t_end / dt) + 1))


# koe 1 (f = 1,0 Hz, suuri jännitys): P's largest displacement across (poikittainen) or along (pitkittäinen) the rope
a["koe1-dmax"] = max_disp(1.0, V["suuri"], 3.0)         # 5,0 cm = A, whatever the wave type; the other direction 0
a["koe1-arrive"] = xP / V["suuri"]                      # the front reaches P after 0,50 s
a["koe1-front-3s"] = V["suuri"] * 3.0                   # in 3,0 s the front has gone 6,0 m, P has moved at most 5,0 cm
# koe 2 (suuri jännitys, v = 2,0 m/s): λ = v/f for several frequencies, and f·λ
for f in (0.5, 1.0, 2.0):
    lam = V["suuri"] / f
    a[f"koe2-lambda-f{f:g}"] = lam                      # 4,00 m, 2,00 m, 1,00 m
    a[f"koe2-flambda-f{f:g}"] = f * lam                 # 2,0 m/s on every row
# koe 3 (f = 1,0 Hz): tension changes the speed and λ, the frequency stays
for k, v in V.items():
    a[f"koe3-v-{k}"] = v
    a[f"koe3-lambda-{k}"] = v / 1.0                     # 2,00 m and 1,00 m
# ennuste 2: f from 1,0 to 2,0 Hz in the same rope
a["ennuste2-lambda1"] = V["suuri"] / 1.0                # 2,0 m
a["ennuste2-lambda2"] = V["suuri"] / 2.0                # 1,0 m
# Kaava figure "kuvaajat": λ = 1,0 m, T = 0,50 s, so v = λ/T
a["kuvaajat-v"] = 1.0 / 0.50                            # 2,0 m/s
# Esimerkki: a pulse goes 6,0 m in 2,5 s; then f = 3,0 Hz in the same rope
v_ex = 6.0 / 2.5                                        # v = s/t = 2,4 m/s
a["esim-v"] = v_ex
a["esim-lambda"] = v_ex / 3.0                           # λ = v/f = 0,80 m
a["esim-T"] = 1 / 3.0                                   # T = 0,333 s
a["esim-check"] = v_ex * (1 / 3.0)                      # v·T = 0,80 m = λ
a["esim-n-lambda"] = 6.0 / (v_ex / 3.0)                 # 7,5 wavelengths in 6,0 m
# Yleinen virhekäsitys: same rope v = 2,0 m/s, f 1,0 -> 2,0 Hz
a["virhek-l1"] = 2.0 / 1.0
a["virhek-l2"] = 2.0 / 2.0
# Kaava text: sound in air 343 m/s (20 °C) for 440 Hz is not used; water ~1500 m/s quoted as a fact only
# virhe (Etsi virhe): a (t, y) graph with peaks 0,50 s apart (so T = 0,50 s, f = 2,0 Hz); the student takes 0,50 as λ in m
a["virhe-f"] = 1 / 0.50                                 # 2,0 Hz, consistent with the source
a["virhe-wrong"] = 2.0 * 0.50                           # his v = fλ = 2,0 Hz · 0,50 m = 1,0 m/s
# siirto: slinky pushed 2,5 times a second, compressions 0,60 m apart; time for 6,0 m
v_s = 2.5 * 0.60                                        # v = fλ = 1,5 m/s
a["siirto-v"] = v_s
a["siirto"] = 6.0 / v_s                                 # t = s/v = 4,0 s
a["siirto-mist-lf"] = 6.0 / (0.60 / 2.5)                # v = λ/f = 0,24 m/s -> 25 s
a["siirto-mist-fl"] = 6.0 * 2.5 * 0.60                  # t = s·f·λ = 9,0
# tarkistus 2: snapshot figure valokuva, crests at 0,5, 2,0 and 3,5 m: λ = 1,5 m; f = 1,8 Hz
lam_c = 2.0 - 0.5
a["tarkistus2-lambda"] = lam_c
a["tarkistus2"] = 1.8 * lam_c                           # v = fλ = 2,7 m/s
a["tarkistus2-mist-half"] = 1.8 * lam_c / 2             # crest to trough 0,75 m taken as λ: 1,35 m/s
a["tarkistus2-mist-div"] = lam_c / 1.8                  # v = λ/f: 0,833
a["tarkistus2-mist-3"] = 1.8 * 3.0                      # crests at 0,5 and 3,5 m (two λ) taken as λ: 5,4 m/s
# tarkistus 1: the junction of two ropes; v 3,0 -> 1,5 m/s at f = 2,0 Hz (feedback numbers)
a["tark1-l1"] = 3.0 / 2.0                               # 1,5 m
a["tark1-l2"] = 1.5 / 2.0                               # 0,75 m
# exit ticket: f tripled in the same rope -> λ/3
a["exit-ratio"] = 1 / 3
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
