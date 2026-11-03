VERDICT: PASS
CONTENT-HASH: 0041bdda8d91e4b7

## Blocking

## Polish
- lesson.md:427 — the worked example's substitution keeps Finnish decimal commas (`1{,}602`, `1{,}22`, `3{,}00`, `6{,}515`) while the surrounding English text uses points — write `1.602`, `1.22`, `3.00`, `6.515`.

## Checked
- Recomputed in one script with my own formulas: worked example h = 6.515e-34 J s (−1.7 %), all inquiry numerics (aineisto 6.494e-34 J s with b = −0.050 V, koe-2 U_k = 1.879 V, siirto 953.8 nm, tarkistus-2 6.675e-34 J s), mistake values and exit ticket 3.06 V agree.
- Sim model I = (s/R) ln(1 + exp((U − U_k)/s)), s = 0.035 V, R = 18 Ω: koe-1 currents at 2.20 V (17.8 / 13.9 / 11.1 / 0.108 mA, blue and violet ≈ 0) and koe-2 values (0.188 mA at 1.80 V, 1.98 mA at 1.90 V, 28.9 mA at 2.40 V) match sim.js, lesson-answers.py and every feedback.
- Model U_k values lie 0.06–0.12 V below hc/(eλ); "about 0.1 V" and the constant-offset/slope argument are right; line intercept −0.05 V matches the fit.
- Physics: band-gap photon (hf ≈ E_g), eU_k ≈ hf, colour independent of voltage, extra energy as heat, LED band 20–40 nm vs laser diode ~1 nm, threshold from line extrapolation — correct and consistent across theory, summary, misconception, choices and model answers.
- Figure 13 (tarkistus-2): the line passes through (4.6e14 Hz; 1.80 V) and (7.0e14 Hz; 2.80 V) as the solution reads.
- Every choice item has exactly one correct option; distractor feedback correct.
- Units: C·V/Hz = J s shown; significant-figure reasons stated.
- Exercise set: reviewed separately in exercises/review/science.md (PASS).
