VERDICT: DONE

Draft of the chapter *Akut ja latauspiiri* (Finnish only); `check_lesson.py fy6-9` all ok, layout also ok at 345 px.

- `lesson.md`: Ydinajatus (paristo ja akku, virran suunta akussa purkautuessa ja latauksessa, kapasiteetti $Q = It$ in Ah, energia $W = UQ$ in Wh, why charging slows), `## Kaava: Akun kapasiteetti ja latausvirta` (latauspiiri $I = (U_\text{lat} - E) : (R + R_\text{s})$, napajännite $U = E + R_\text{s} I$, potential graph, energy and $\eta$), seven-stage example, misconceptions, summary. Energy is written $W$ in this chapter because $E$ is the source voltage (as in *Lähdejännite ja sisäinen resistanssi*, $R_\text{s}$ the same).
- `lessons/FY6/fy6-9/figures.py`: hero, purku/lataus, capacity graph, charging circuit, potential graph, energy flow to scale, task graph `ex-current`.
- `inquiry.json`: hook, retrieval, two predictions, sim + three experiments (koe-3 optional), conclusion, error-spotting, transfer, three checks, exit.
- New sim `assets/sims/fy6/fy6-9/` (static time slider, CV charger, linear E(q)), strings in `lang/fi.json` `sims.fy6-9`, 52 assertions in `tests/sims/fy6-9.json`, `sim-spec.md`.
- Exercises 5/4/3 with complete solutions; `answers.py`, `lesson-answers.py`; `exit-ticket.json`; glossary: akku, paristo, latauspiiri, akun kapasiteetti.
