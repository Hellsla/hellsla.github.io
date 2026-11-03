VERDICT: DONE

Draft round 1 (fy6-2 Mittaukset virtapiirissä). check_lesson.py: every line ok; check_layout also ok at 345 px.

- `lesson.md`: Ydinajatus (ammeter in series, voltmeter across, multimeter jacks/selector/range/OL, choosing the range, the meter's own resistance and wrong connections), `## Kaava: Yleismittarin virheraja` (Δx = p·x + n·r, relative limit, spec table), staged example (same voltage on 20 V and 2 V ranges), misconception (largest range is best), summary.
- `figures.py`: hero (lab bench), connections, multimeter, wrong connections, error bands to scale; IEC symbols, current arrows violet `#7048e8` (palette colour; chosen for FY6 current, siblings may want the same).
- `inquiry.json`: retrieval, two predictions (current before/after lamp; voltmeter in series), sim, three experiments (koe-3 optional), conclusion, error-spotting, transfer (10 A range on 0,02 A), three checks, exit.
- New sim `assets/sims/fy6/fy6-2/` (circuit + multimeter solved with the meter's resistance, fuse, OL, 3½-digit display; stacked 600×800 under 500 px), texts in `lang/fi.json` `sims.fy6-2`, `tests/sims/fy6-2.json` (29 assertions).
- Exercises 5/4/3 (L3-03 a word task), solutions, `answers.py`, `lesson-answers.py`, exit ticket, sim-spec.
- `glossary.json`: jännitemittari, virtamittari, yleismittari, mittausalue.
