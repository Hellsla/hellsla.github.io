VERDICT: DONE

Draft of *Sähköteho ja vastuksen lämpeneminen*.

- `meta.json`: unchanged (sim true, glossary sähköteho, Joulen laki, sähköenergia).
- `lesson.md`: Miksi (toaster wires glow, cord stays cool); Ydinajatus in five ### parts (P = UI as J/C · C/s, Joulen laki from collisions, power division series/parallel, toaster and cord, heating levels off); `## Kaava: Sähköteho ja Joulen laki` (P = UI, P = RI² = U²/R, E = Pt, rated power); seven-stage example (15 Ω ∥ 30 Ω on 12 V, 5,0 min); two misconceptions; summary.
- `figures.py`: hero (toaster), energia, jako (bars to scale), lampo (schematic T(t)), graph (P(I) for 4 and 8 Ω), task figure ex-pi.
- `assets/sims/fy6/fy6-6/sim.js` (new): two heating coils in water beakers, series/parallel, U, R1, R2, run/stop/reset, speed; powers as bars, thermometers; phone layout 600×660. `tests/sims/fy6-6.json`: 56 assertions. `lang/fi.json` sims.fy6-6.
- `inquiry.json`: hook, retrieval, two predictions, sim, two experiments (series, parallel), conclusion, theory, reflect, example, error spotting, transfer (12 V kettle), three checks, exit.
- Exercises 5/4/3 with `answers.py` and complete `solutions.md`; `lesson-answers.py`; `exit-ticket.json` (2).
- `glossary.json`: sähköteho, Joulen laki added; fy6-6 added to sähköenergia.

check_lesson.py all ok; layout ok at 345, 360, 768, 1280 px.
