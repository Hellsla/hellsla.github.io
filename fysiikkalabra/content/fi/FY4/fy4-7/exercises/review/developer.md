VERDICT: DONE

New data task (brief FY4-A2) and one proofreading fix; fi, en, fi-easy.

- `lessons/FY4/fy4-7/answers.py`: block for `fy4-7-L2-10` (shares of part a, kinetic energies, reaction and braking distances, difference 13.3 m, speed left 52 km/h).
- `exercises/exercises.json` (three languages): `fy4-7-L2-10` appended to level 2, kind data/reasoning/model, table of Fintraffic's report *Ajonopeudet maanteillä 2025*, answer 13.3 m, tolerance 0.05.
- `exercises/solutions.md` (three languages): complete solution of L2-10; L1-07 reasonableness row corrected (9600 J = 9,6 kJ, compared with the given 9,4 kJ).

Source differs from the brief: the brief links Digitraffic's open data and asks for a station's speed distribution; the raw data needs programming and changes daily, so the task uses Fintraffic's dated annual report of the same stations, with its figures as a table. The Digitraffic page is named in the solution.

Deviations from the spec: date written "16. marraskuuta 2026" (the lint reads 16.11.2026 as a decimal point); braking distance derived from the chapter's own equations with a = −8,0 m/s² (v² = v0² − 2as is not taught); energies as 0,37 MJ and 0,49 MJ (two significant figures); the data schema has no source field.

Checks: lint 0 errors, check_solutions ok, check_lesson all ok, layout 360 px ok.
