VERDICT: DONE

Drafted fy7-15 *Valon polarisaatio* (resumed after an interrupted run; the earlier draft was kept and completed).

- `lesson.md`: opening illustration, Ydinajatus (transverse wave, polariser/analyser, unpolarised light halves), Kaava: Malusin laki, Brewsterin laki (tan α_B = n₂ : n₁, reflected ⊥ refracted), applications (sunglasses, LCD, 3D glasses), seven-stage worked example, misconception (incl. three-polariser surprise), summary. Fix in this run: the substitution block of the worked example now opens with the solved formula in symbols (lint human rule 2).
- `inquiry.json`: prediction, sim experiment (two/three polarisers), I vs cos²θ fit graph (`fy7-15/fit`), transfer, checks.
- `exercises/exercises.json` 5/4/3 with `solutions.md` complete; every answer in `lessons/FY7/fy7-15/answers.py`; lesson numbers in `lesson-answers.py`; figures in `figures.py`.
- `exit-ticket.json`, `meta.json`.
- Sim `assets/sims/fy7/fy7-15/sim.js` (all canvas words via `__()`, keys in `lang/fi.json` `sims.fy7-15`), tests `tests/sims/fy7-15.json`, `sim-spec.md`.

`check_lesson.py fy7-15` all ok; `check_layout --width 340` OK; `check_solutions` ok. Palette warnings are the brief's ray colour #e64980 and grey normals.
