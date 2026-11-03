VERDICT: DONE

Draft of *Ionisoiva säteily ja elimistö*.

- `lesson.md`: Ydinajatus (ionisation threshold and E = hf, ion pairs n_i = E/W, ionisation density of α/β/γ/n, penetration table, GM tube, biological effects through ionisation, absorbed dose only qualitatively with a pointer to chapter 13), `## Kaava: Gammasäteilyn vaimeneminen` (I = I0 (1/2)^(d/d½), NIST XCOM table), staged example (lead for 5,0 %), misconceptions, summary.
- `figures.py`: hero, energy scale, tracks in tissue, penetration, GM tube, attenuation graph, task graph `tuntematon`.
- New sim `assets/sims/fy8/fy8-12/sim.js` (source × absorber × plates, seeded 10 s GM counts), texts in `lang/fi.json` `sims.fy8-12`, 26 assertions in `tests/sims/fy8-12.json`.
- `inquiry.json`: 2 predictions, 3 experiments, conclusion, Etsi virhe, transfer (lead apron), 3 checks; `exit-ticket.json` 2 questions.
- Exercises 5/4/3 with `answers.py`, complete `solutions.md`; `lesson-answers.py` replicates the sim's generator.
- `glossary.json`: ionisoiva säteily, ionisaatio, läpäisykyky, puoliintumispaksuus, Geiger-Müller-putki.

Not fixable here: chapter 13 names the same quantity *puoliarvokerros* with thickness $x$; this chapter says *puoliintumispaksuus eli puoliarvokerros* with $d$. One term should be chosen for both.
