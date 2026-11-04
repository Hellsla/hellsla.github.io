VERDICT: DONE
Drafted fy8-9 *Hajoamislaki ja puoliintumisaika*; check_lesson.py all ok.
- `lesson.md`: Ydinajatus (randomness, no ageing, half-life table from NNDC NuDat 3 rounded, activity, background), `## Kaava: Hajoamislaki` (N = N0 (1/2)^(t/T½), A = λN, N = N0 e^(−λt), λ = ln 2/T½, A-law; TVT subsection: fitting y = A e^(−Ct) + B in Graphical Analysis Pro, Finnish UI words from the TVT guides), I-131 worked example in seven stages, two misconceptions, summary. Hero + 3 inline figures.
- `figures.py`: hero, ydin (100 nuclei at 0, T½, 2T½), kuvaaja, sovitus (simulated Ba-137m), task figures pa-points, aktiivisuus.
- `lesson-answers.py`: sim model (mulberry32 port, verified equal to JS), simulated Poisson data and least-squares fits (pure Python).
- `inquiry.json`: hook, retrieval, 2 predictions, sim + 3 experiments, conclusion, theory, reflect, example, error-spotting, fitting task (Pa-234m, source simulated, answer 68,4 s, tol 1 %), 3 checks, exit.
- New sim `assets/sims/fy8/fy8-9/sim.js` + `tests/sims/fy8-9.json` (23 assertions), texts in `lang/fi.json` sims.fy8-9.
- Exercises 5/4/3, `answers.py`, complete solutions; exit ticket; 4 glossary terms.
