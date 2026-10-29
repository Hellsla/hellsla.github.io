VERDICT: DONE

Round 1 draft. check_lesson.py fy4-3 shows ok on every line; check_choices, coverage (identify plan) and check_solutions are clean.

- `content/fi/FY4/fy4-3/lesson.md`: The Miksi question is about a curling stone, with a hero image under it. Ydinajatus has three subheadings: interaction, the first law with the curling force diagram, and the third law with two skaters drawn on separate diagrams. The section `## Kaava: Newtonin ensimmäinen ja kolmas laki` gives ΣF̄ = 0̄ ⇔ v̄ vakio, F̄_AB = −F̄_BA and G = mg, with a force diagram of a car at constant velocity. The worked example is a jet at constant velocity, in 7 stages. Then the misconception section and the summary.
- `inquiry.json`: two predictions. Experiment exp-1 slides a box on different surfaces. A force-sensor collision graph serves as interpret evidence (source: example). Also an error-spotting horse-and-cart task, a trailer transfer task, three checks (check-3 is a drawing task) and the exit ticket. Tags are `identify` plus one `draw`.
- `exercises/`: 5/4/3 exercises with complete solutions. `exit-ticket.json` has 2 questions.
- `lessons/FY4/fy4-3/`: figures.py has 6 figures; all force diagrams use fbd.py, the hero uses herolib. Also answers.py, lesson-answers.py and sim-spec.md.
- New sim `assets/sims/fy4/fy4-3/sim.js`: the hand's push, then the slide, a (t, v) graph and a live force diagram. Its texts are in `lang/fi.json` under `sims.fy4-3`. `tests/sims/fy4-3.json` has 19 assertions.
- `glossary.json`: added jatkavuuden laki, voima ja vastavoima and inertia.
