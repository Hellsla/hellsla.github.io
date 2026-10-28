VERDICT: DONE

Draft, round 1. check_lesson.py: every line ok (lint, latex, build, inquiry 44/44, layout 360/768/1280).

- `meta.json`: added glossary term `päästökerroin`.
- `lesson.md`: Ydinajatus (greenhouse effect qualitatively, fuels and CO2, life-cycle emissions, criteria list, kestävä energiatalous), Kaava: Hiilidioksidipäästö (m = e · E, IPCC AR5 WG3 Annex III table), staged household example, two misconceptions, summary; two figures.
- `lessons/FY2/fy2-8/figures.py`: `greenhouse` (qualitative, not to scale) and `emissions` (bar chart to scale, 820 vs 12 g/kWh).
- `inquiry.json`: hook, optional retrieval, two predictions (greenhouse without gases; coal vs wind factor), three `interpret` evidence items (data table with numeric, origin of wind's emissions, what the factor does not tell), reflect, error-spotting, transfer (100 GWh), structured five-part argument task with pair prompt and model answer, three checks, exit.
- `exit-ticket.json`, `exercises/exercises.json` (5/4/3), `exercises/solutions.md` (complete), `answers.py`, `lesson-answers.py`.
- `glossary.json`: hiilidioksidipäästö, päästökerroin, ilmastonmuutos, kestävä energiatalous added; kasvihuoneilmiö lists fy2-8.

Notes: aurinkosähkö 41 (rooftop) used in L1-04; petrol/diesel factors (69, 74 g/MJ, IPCC 2006 defaults) and energy contents (32, 36 MJ/l) are given in the tasks as rounded typical values. Predictions have no reveal (no simulation), so feedback follows commitment.
