VERDICT: DONE

Round 1, draft of *Kirchhoffin lait ja potentiaali virtapiirissä*.

- `lesson.md`: Miksi question (a bird on a power line). Ydinajatus covers the current law (charge conservation, current does not wear out), potential relative to a reference point, the voltage law as a loop, and the bird resolved. `## Kaava: Kirchhoffin lait` gives ΣI, U_AB = V_A − V_B and ΣΔV = 0 with sign rules and the potential graph. Also a seven-stage example (12 V, 20/60/30 Ω), three misconceptions and a summary.
- `figures.py`: IEC circuit helpers (in this lesson only), hero, junction (+ question variant), the circuit with the potentials of points A–F, the potential graph, and the task figures ex-graph, ex-branch and ex-branch2. Current is orange and potential is blue.
- `inquiry.json`: hook, an optional retrieval, two predictions (how the current splits; potential around the loop), the sim, experiments 1–2 (+ optional experiment 3 on the reference point), a conclusion, an error-spotting item, the bird transfer task, three checks and the exit ticket.
- New sim `assets/sims/fy6/fy6-5/sim.js` (U, R1, R2 ∥ R3, probe A–F, reference F/B, voltmeter, potential graph, stacked under 500 px). Its texts are in `lang/fi.json` under `sims.fy6-5`. `tests/sims/fy6-5.json` has 49 assertions.
- Exercises 5/4/3 with `answers.py`, `solutions.md`; `lesson-answers.py`; `exit-ticket.json`; `sim-spec.md`.
- `glossary.json`: the 5 terms added. `figcat.py build` run.
