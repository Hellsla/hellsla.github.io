"""Numbers of the lesson text and inquiry.json for fy7-5, computed from their data (python -I lesson-answers.py); the
exercises' answers are in answers.py. Φ = B A, e = −N ΔΦ / Δt, e = v B l. Prints {id: number} as JSON."""
import json

a = {}
# Worked example: N = 250 turns, A = 4,0 cm², B grows evenly from 0,10 T to 0,50 T in 0,20 s
N, A, dB, dt = 250, 4.0e-4, 0.50 - 0.10, 0.20
a["ex-dPhi"] = dB * A                                # ΔΦ = ΔB · A = 1,6 · 10⁻⁴ Wb
a["ex-e"] = N * a["ex-dPhi"] / dt                    # |e| = N ΔΦ / Δt = 0,20 V
a["ex-e-one-turn"] = a["ex-dPhi"] / dt               # Järkevyys: one turn gives 0,80 mV, 250 turns 250 times that
# Kaava graph and the simulation's default run: N = 10, B = 0,20 T, square coil 0,10 m × 0,10 m, v = 0,10 m/s,
# field region 0,20 m wide, the leading side starts 0,05 m before the field
Ns, Bs, l, v = 10, 0.20, 0.10, 0.10
a["sim-Phi-max"] = Bs * l * l * 1e3                  # Φ = B A = 2,0 mWb when the coil is wholly inside
a["sim-e-in"] = -Ns * Bs * l * v * 1e3               # entering: e = −N ΔΦ/Δt = −N B l v = −20 mV
a["sim-e-out"] = Ns * Bs * l * v * 1e3               # leaving: +20 mV
a["sim-t-in"] = l / v                                # entering lasts l / v = 1,0 s
a["sim-slope"] = a["sim-Phi-max"] / a["sim-t-in"]    # slope of Φ(t) while entering: 2,0 mWb/s
a["sim-run"] = (0.05 + 0.20 + 0.10 + 0.05) / v       # the whole run 0,40 m : 0,10 m/s = 4,0 s
for vv in (0.20, 0.30):                              # koe-1: e ∝ v, Δt ∝ 1/v, e·Δt constant
    a[f"sim-e-in-v{vv:.2f}"] = -Ns * Bs * l * vv * 1e3       # −40 mV, −60 mV
    a[f"sim-t-in-v{vv:.2f}"] = l / vv                        # 0,50 s, 0,333 s
a["sim-e-dt"] = a["sim-e-in"] * a["sim-t-in"]        # e·Δt = −20 mV·s = −N ΔΦ = −10 · 2,0 mWb
for NN in (1, 5, 20):                                # koe-2: e ∝ N
    a[f"sim-e-in-N{NN}"] = -NN * Bs * l * v * 1e3    # −2,0 / −10 / −40 mV
# Retrieval: an electron at rest in a magnetic field, F = q v B = 0
a["kertaus-F"] = 1.602e-19 * 0 * 0.5
# virhe: N = 200, A = 6,0 cm², B 0 -> 0,30 T in 0,050 s
a["virhe-wrong"] = 200 * 0.30 * 0.060 / 0.050        # the student's area 0,060 m²: 72 V
a["virhe-right"] = 200 * 0.30 * 6.0e-4 / 0.050       # A = 6,0 · 0,0001 m²: 0,72 V
a["virhe-noN"] = 0.30 * 0.060 / 0.050                # distractor without N: 0,36 V
# siirto: shake flashlight, N = 600, ΔΦ = 0,12 mWb in 15 ms
a["siirto"] = 600 * 0.12e-3 / 0.015                  # 4,8 V
a["siirto-noN"] = 0.12e-3 / 0.015                    # mistake, no N: 0,0080 V
a["siirto-ms"] = 600 * 0.12e-3 / 15                  # mistake, 15 ms as 15 s: 0,0048 V
a["siirto-mWb"] = 600 * 0.12 / 0.015                 # mistake, mWb as Wb: 4800 V
a["siirto-one-turn"] = 0.12e-3 / 0.015 * 1e3         # Järkevyys: one turn 8,0 mV
# tarkistus-2: rod l = 50 cm, v = 4,0 m/s, B = 0,25 T
a["check-e"] = 4.0 * 0.25 * 0.50                     # 0,50 V
a["check-e-cm"] = 4.0 * 0.25 * 50                    # mistake, l in cm: 50 V
a["check-e-nol"] = 4.0 * 0.25                        # mistake, no l: 1,0 V
# Exit ticket 1: square loop, side 0,20 m, B = 0,50 T perpendicular
a["exit-Phi"] = 0.50 * 0.20 ** 2                     # 0,020 Wb = 20 mWb
print(json.dumps({k: round(v, 6) for k, v in a.items()}))
