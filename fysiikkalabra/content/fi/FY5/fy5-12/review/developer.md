VERDICT: DONE

Draft, round 1. `check_lesson.py fy5-12`: every line ok; `check_layout.py --width 345`: OK.

- `meta.json`: glossary (7 terms), skills goal.
- `lesson.md`: Ydinajatus (superposition with rope pulses; two in-phase sources, nodal lines), `## Kaava: Vahvistavan ja heikentävän interferenssin ehto` (Δs, nλ, (n+½)λ, the line pattern, Δs/λ decides), optional `## Fourier-analyysi` (sum of sines, spectrum, FFT used in *Äänen ominaisuudet*), 7-stage Esimerkki (two loudspeakers), misconceptions, summary. Standing waves not taught.
- `inquiry.json`: hook (schoolyard speakers), optional retrieval v = fλ, two predictions (pulses through each other → after theory; Δs = λ/2 → after koe 1), sim, koe 1 (P along the line), koe 2 (same P, λ varies, choice question), conclusion, optional Fourier box + spectrum check, optional Etsi virhe, siirto (f from first quiet spot), three checks, exit.
- `exercises/`: 5/4/3 (one word task L1-03), complete solutions.
- `lessons/FY5/fy5-12/`: answers.py, lesson-answers.py (sim values recomputed as sim.js does), figures.py (hero, pulssit, kuvio, matkaero, ehdot, fourier; waves blue/violet/ink, never red), sim-spec.md.
- `assets/sims/fy5/fy5-12/sim.js`: ripple tank colour map of y1 + y2, P on a line, signals at P, nodal lines toggle, speed control, stacked phone layout; `tests/sims/fy5-12.json` 28 assertions.
- Shared: `lang/fi.json` sims.fy5-12, `glossary.json` 7 terms.

Open: figcat build left to the coordinator.
