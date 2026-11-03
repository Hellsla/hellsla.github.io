VERDICT: DONE

Drafted fy8-13 from scratch; check_lesson.py all ok (one lint warning: a long table cell).

- `lesson.md`: Ydinajatus (absorbed dose, weighted doses, STUK 2023 source table 5,9 mSv/a, background, radon, protection by time/distance/shield, dose limits), `## Kaava: Absorboitunut ja efektiivinen annos` (D = E/m, H_T = w_R D_T, H_E = Σ w_T H_T with ICRP 103 tables, H = Ḣt, inverse-square law, half-value layer), staged example (radon in the lungs → 4,0 mSv), misconceptions, summary. Effective dose written H_E (stated why: E is energy).
- `figures.py`: hero (house on granite, radon), lahteet, painotus, etaisyys, suoja, task figure vaimennus.
- `inquiry.json`: hook, optional retrieval, 3 predictions, sim + koe-1 (distance), koe-2 (lead), conclusion, theory, reflect, example, Etsi virhe, siirto, 3 checks, exit.
- New sim `assets/sims/fy8/fy8-13/` (+ `lang/fi.json` sims.fy8-13, `tests/sims/fy8-13.json`, sim-spec.md).
- Exercises 5/4/3, solutions.md, answers.py, lesson-answers.py, exit-ticket.json.
- glossary.json: 6 terms.

Teacher should verify STUK/legal figures (listed in the orchestrator report). `figcat.py build` not run (writes docs/).
