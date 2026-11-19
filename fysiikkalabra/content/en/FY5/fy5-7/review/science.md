VERDICT: PASS
CONTENT-HASH: 37a367455b7f811a

## Blocking

## Polish
- inquiry.json tarkistus-3 — the model answer reads $C = 0.01$ as $C \approx 0$. That is right, but one clause saying it is a negligible fraction of $2\pi$ would show why. Not an error.

## Checked
- Round-1 blocker (fixed): lesson.md:486 now says "in the calculation tasks of this chapter". The only task with $C \ne 0$ is the optional conceptual *vaihe* choice ($C = \tfrac{\pi}{2}$). Every calculation task starts at an upward pass through equilibrium: the worked example, siirto, tarkistus-2, tarkistus-3 and the exercises' sine tasks (L1-09, L2-01, L3-01, L3-05). The claim holds.
- Definitions match the glossary. Conditions are stated: undamped, sinusoidal, small pendulum angles, radian mode. The reference-circle angle uses no ω (fits the FY5 scope).
- Recomputed from the sim's own data, all matching the quoted numbers and lesson-answers.py: koe-1 $d$ = 1.85 / 0.13 / 3.70 cm; koe-2 $N$ = 6 / 3 and $f$ = 1.25 / 0.625 Hz; koe-3 best fit 8.5 cm and 2.20 s with $d$ = 0.127 cm; load $d$ = 3.92 cm.
- Worked example: 0.60 s, argument 2.618, 2.0 cm; degree-mode 0.183 cm. Solved symbolically first, and the reasonableness check is real.
- siirto: 3.80 cm; mistakes 0.0877, −3.80 and 8.0 are right. tarkistus-2: 0.556 Hz; distractors 1.11 and 0.185 Hz; $L \approx 0.81$ m. tarkistus-3: 0.800 s, 1.25 Hz, range 0.378–0.482 m. virhe: 1.11 vs 2.22 Hz. Exit ticket: 2.0 Hz.
- Every choice item has exactly one correct option. Every distractor is really wrong, and its feedback says why.
- Experiments isolate their variable (koe-1 varies $A$ with $T$ locked, koe-2 the reverse). The measured keys are in `simState`.
- Figures agree with figures.py and are to scale: kuvaaja's $T$ arrows, sovitus $3T = 3.6$ s, tarkistus-kuvaaja's 1.8 s period, ympyra's quarter points.
- sim.js implements the lesson's model. Its $d$, $N$ and $f$ match the calc box, and its limits are stated in the model box.
