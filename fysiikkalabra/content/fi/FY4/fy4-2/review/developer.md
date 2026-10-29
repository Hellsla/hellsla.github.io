VERDICT: DONE

Round 1 draft of the lesson Kiihtyvyys ja tasaisesti kiihtyvä liike. `check_lesson.py fy4-2` passes every check, including the layout at 360, 768 and 1280 px.

- `lesson.md`: the Miksi question (a stone dropped from a bridge) with its hero. Ydinajatus covers acceleration and its sign, the (t,v) graph, the tangent as instantaneous velocity, and free fall. Kaava gives a = Δv/Δt, v = v₀ + at and x = x₀ + v₀t + ½at² from the area, plus a = 2A from a polynomial fit. The worked example has seven stages and solves a quadratic. Also a misconception section and a summary.
- `figures.py`: the hero (herolib) and four theory figures: strobe, tv-graph, tangent and area. Four task figures are shown by id. Velocity is blue and acceleration orange everywhere.
- `inquiry.json`: a hook and a retrieval item, two predictions, the simulation, two experiments with a conclusion, a free-fall data task (polynomial fit to get g), theory and reflection, the example, an error-spotting item, a transfer task, three checks and the exit ticket.
- New simulation `assets/sims/fy4/fy4-2` with 36 assertions in `tests/sims/fy4-2.json`. Its texts are under `lang/fi.json` sims.fy4-2.
- Exercises 5/4/3 with complete solutions. Their answers are computed in `answers.py`; the lesson's numbers are in `lesson-answers.py`.
- `glossary.json`: three new terms.

Not fixable here: the `article svg` rule in `templates/site.css` puts a figure border and padding on KaTeX's `\sqrt` svg. The square roots in the worked example and in the L3-01 solution show as empty boxes until that file is fixed.
