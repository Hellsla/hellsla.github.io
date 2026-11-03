VERDICT: DONE

Draft, round 1. Every check in `check_lesson.py fy7-3` passes.

- `lesson.md`: Miksi (the scrapyard electromagnet) and the hero. Ydinajatus covers Ørsted, the field circles around a wire, the right-hand rule, the coil's field and the electromagnet, with 3 figures. Kaava: Suoran johtimen ja käämin magneettikenttä gives $B = \mu_0 I/(2\pi r)$ and $B = \mu_0 NI/l$ with their conditions, the B(r) graph, the coil sketch and the measurement method. Also a seven-stage Esimerkki, the misconceptions and the summary.
- `inquiry.json`: two predictions (stretched coil, coil end). The simulation runs two experiments, then a conclusion. The LOPS measurement is an `interpret` on example data: a Graphical Analysis fit leads to μ0 and its relative uncertainty (systematic error from the coil's finite length). Then the transfer task (cancel Earth's field), error spotting, three checks and the exit ticket.
- New sim `assets/sims/fy7/fy7-3/sim.js`: a finite coil on its axis, with I, N, l, probe x, current direction and speed. The B(x) graph is stacked on phones. Its texts are in `lang/fi.json` under `sims.fy7-3` and it has 32 assertions in `tests/sims/fy7-3.json`.
- Exercises 5/4/3 with complete solutions. `answers.py`, `lesson-answers.py`, `figures.py` (7 figures) and `sim-spec.md`.
- `glossary.json`: virtajohdin, käämi, oikean käden sääntö, sähkömagneetti.
