VERDICT: DONE

Draft of fy6-8 Lähdejännite ja sisäinen resistanssi (check_lesson.py all ok; check_layout 345 px ok).

- `lesson.md`: Miksi (car headlights dim at start-up), Ydinajatus (battery model E + R_s, napajännite U = E − R_s I with potential and energy view, measuring E without current, car battery, oikosulku and safety), Kaava: Napajännite ja oikosulkuvirta (U = E − R_s I, I = E/(R + R_s), I_k = E/R_s, E and R_s from the (I, U) line, experimental method, cells in series/parallel), 7-stage example, misconceptions, summary.
- `figures.py`: hero (winter-morning car), model, potential graph, (I, U) graph, series/parallel cells, task figures ex-graph and check-graph.
- New sim `assets/sims/fy6/fy6-8/sim.js` (battery new/used, one/series/parallel, switch, load R, mark points, fitted line; E and R_s hidden), texts in `lang/fi.json` sims.fy6-8, 34 assertions in `tests/sims/fy6-8.json`, `sim-spec.md`.
- `inquiry.json`: hook, retrieval, 2 predictions, 3 experiments (koe-1 with an R_s question), conclusion, Etsi virhe, car transfer task, 3 checks, exit.
- Exercises 5/4/3 with complete solutions; `answers.py`, `lesson-answers.py`.
- `glossary.json`: lähdejännite, napajännite, sisäinen resistanssi, oikosulku.
