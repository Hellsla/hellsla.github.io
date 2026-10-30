VERDICT: DONE

Draft, round 1. `check_lesson.py fy4-14`: every line ok.

- `meta.json`: unchanged (sim: true, glossary väliaineen vastus, rajanopeus).
- `lesson.md`: Miksi + hero; Ydinajatus (vastusvoima, kolme vaihetta, rajanopeus massasta ja muodosta); `## Kaava: Liikeyhtälö ilmanvastuksen kanssa` (G + F_v = ma; nouseva pallo; varjo aukeaa, example G); staged worked example (canopy opening, a = 18,4 m/s² up while moving down); misconception; summary. Figures from `figures.py` (all FBDs via fbd.py, kind="drag").
- `inquiry.json`: hook, optional retrieval, 3 predictions, sim, exp-1 (mass), exp-2 (canopy), optional exp-3 (position), conclusion, select task (rising volleyball, 4 option figures), optional transfer (snowboarder on a slope, uses *Paino, kitka ja kalteva taso*), 3 checks (identify, numeric, draw), exit. fbd plan identify/select/draw covered.
- `exit-ticket.json`: 3 questions not asked by the checks.
- `exercises/`: 5/4/3 with complete solutions; L3-03 reads a tangent off `fy4-14/ex-tangentti`.
- `lessons/FY4/fy4-14/`: answers.py, lesson-answers.py (sim model values recomputed with the sim's integrator), figures.py, sim-spec.md.
- `assets/sims/fy4/fy4-14/sim.js` (new): skydiver, drag modelled numerically F_v = k v² (said in the model box), stacked phone layout; `tests/sims/fy4-14.json` 17 assertions.
- `lang/fi.json` sims.fy4-14; `glossary.json` two terms.

Not done here: `docs/coverage/FY4.md` and the figure catalog are stale (shared docs; regenerate after the parallel drafts).
