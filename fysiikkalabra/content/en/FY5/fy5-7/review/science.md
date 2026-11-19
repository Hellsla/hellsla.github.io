VERDICT: PASS
CONTENT-HASH: 37a367455b7f811a

## Blocking

## Polish
- inquiry.json tarkistus-3 — the fit gives $C = 0.01$, and the model answer reads it as $C \approx 0$. That is right, but one clause ("a phase this small is a negligible fraction of $2\pi$") would show the student why $0.01$ counts as zero. Not an error.
- lesson.md "Why exactly $2\pi \tfrac{t}{T}$?" — the radian angle of the reference circle is a fair aid for the sine argument (C). It introduces no ω or rad/s, so it stays inside the FY5 scope note.

## Checked
- Round-1 blocker (fixed): lesson.md:486 now says "in the calculation tasks of this chapter timing always starts like this". The only task with $C \ne 0$ is the optional *vaihe* choice ($C = \tfrac{\pi}{2}$, release at an extreme), which is a conceptual task, not a calculation. Every calculation task starts at an upward pass through equilibrium: the worked example, siirto, tarkistus-2, tarkistus-3 ($C \approx 0$), and the exercises' sine tasks (L1-09, L2-01 graph, L3-01, L3-05; none uses a release or a phase). The claim now holds.
- Definitions (periodic motion, oscillation, equilibrium position, displacement, amplitude, period, frequency, phase) match the glossary. Conditions are stated: the oscillation is undamped and sinusoidal, the pendulum swings through small angles, the calculator is in radian mode.
- One script recomputed the following from the sim's own Park–Miller data and matched lesson-answers.py and every quoted number:
  - koe-1: $d$ = 1.85 / 0.13 / 3.70 cm for $A$ = 3 / 6 / 12 cm
  - koe-2: $N$ = 6 and 3, $f$ = 1.25 and 0.625 Hz
  - koe-3: best fit $A = 8.5$ cm, $T = 2.20$ s, $d = 0.127$ cm; noise ≤ 0.250 cm
  - $d$ = 3.92 cm when the sim loads (matches the 1280 px capture)
- Worked example: $T = 0.60$ s, argument 2.618, $x = 2.0$ cm; in degree mode 0.183 cm. Solved symbolically first; the reasonableness check (between $T/4$ and $T/2$) is a real check.
- siirto: 3.804 cm. Its mistakes are 0.0877 (degree mode), −3.80 ($f$ used as $T$) and 8.0 ($2A$).
- Other answers: tarkistus-2 0.556 Hz, its distractors 1.11 and 0.185 Hz, and the pendulum length 0.805 m for $T = 1.8$ s. tarkistus-3: $T = 0.800$ s, $f = 1.25$ Hz, range 0.378–0.482 m. virhe: 1.11 vs 2.22 Hz. Exit ticket: 2.0 Hz.
- Choice items (kertaus, ennuste-1, ennuste-2, virhe, vaihe, tarkistus-1): each has exactly one correct option. Every distractor is really wrong, and its feedback says why.
- Experiments:
  - koe-1 locks the data set and $T$ and varies $A$; koe-2 locks $A$ and varies $T$; koe-3 leaves both free.
  - The measured keys `d`, `N`, `f`, `A` are in `simState`.
  - The model box states the simulated noise, an undamped oscillation and timing from an upward pass.
- Figures, compared with figures.py:
  - kuvaaja ($A = 4$ cm, $T = 0.8$ s): both $T$ arrows span a true period (peak to peak, upward pass to upward pass).
  - sovitus: $3T = 3.6$ s.
  - tarkistus-kuvaaja: upward passes at 0, 1.8, 3.6 and 5.4 s.
  - ympyra: the projection gives $x = A$ at $T/4$, 0 at $T/2$ and $−A$ at $3T/4$.
- sim.js implements $x = A\sin(2\pi t/T)$. Its $d$ (mean absolute deviation), $N$ (floor) and $f$ match the calc box. The playback weight follows the noise-free data model; the readout shows the nearest point.
