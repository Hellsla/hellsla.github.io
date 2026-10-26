VERDICT: DONE

Drafted fy3-16 (round 1, no simulation: the topic is bookkeeping on data and graphs). `check_lesson.py fy3-16` is ok on every line (lint, latex, build, inquiry 40/40, answer positions, layout 360 px; also clean at 1280 and 1920).

- `lesson.md`: Ydinajatus (energy bookkeeping; cooler bag, sauna, coolant), Kaava "Lämpöenergian tase" (Pt = sum of Q, P = UAΔT, t = sm/(UAΔT), P = c(m/t)ΔT, Q lost = Q gained, check-whether-all-ice-melts steps), staged Esimerkki (cooler bag), misconception, summary. Three figures, all labels LaTeX in fig-tex boxes: cooler bag with to-scale energy columns, T(t) plateau graph, coolant loop (schematic).
- `inquiry.json`: Pohdinta (hook, P = UAΔT retrieval), two predictions (competing models, and a time prediction), three interpret activities (T(t) graph with energy numeric, duration table, löyly table), theory, reflect, example, error-spotting, transfer with 3 hints and mistake feedback, exercises, three checks, exit. The predictions' feedback does not disclose; the evidence is "model values".
- `exercises.json` (5/4/3), `answers.py` (all answers and inquiry numerics computed), `solutions.md`, `exit-ticket.json`.
- `meta.json`, `glossary.json`: untouched (no new term needed).

Notes: solutions.md uses LaTeX per the teacher's rule, so lint gives one standing warning ("solutions are plain text"). No lesson ids appear in student text.
