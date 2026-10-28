VERDICT: DONE

Draft round 1; `check_lesson.py fy2-4` all ok.

- `content/fi/FY2/fy2-4/lesson.md`: Ydinajatus, Kaava: Hyötysuhde (η = E_a/E_o = P_a/P_o, E_o = E_a + E_h), kettle example in seven stages, misconceptions, summary; two to-scale Sankey figures.
- `lessons/FY2/fy2-4/figures.py`: the figures (lamp 100 J; bulb 60 W vs LED 10 W, same 3 W of light). Colours: grey in, green useful, orange loss.
- `inquiry.json`: hook, retrieval (E = Pt), two predictions (petrol engine η, time vs η), sim, two experiments, conclusion, error-spotting, transfer (panel, E to P), checks, exit. `exit-ticket.json`: 3 questions.
- `exercises/exercises.json`, `solutions.md`, `answers.py` (5/4/3, complete solutions); `lesson-answers.py` for lesson/inquiry numbers.
- Sim `assets/sims/fy2/fy2-4/sim.js`, `sim-spec.md`, `tests/sims/fy2-4.json` (53 assertions), `lang/fi.json` sims.fy2-4: one device Sankey, six devices with typical rounded η (labelled typical values, no invented source), adapter laite/Po/t.
- `glossary.json`: added hyötyenergia, häviöt; hyötysuhde definition widened to the FY2 form, lesson added.

Notes: efficiencies are typical rounded values; no source named. Useful arrow green deliberately (palette "good state").
