VERDICT: DONE

Round 2 fixes for fy3-3. Edited only exercises.json, lesson.md, solutions.md.

1. editor FAIL (L2-03 repeats worked example): replaced with an extrapolation task, 110 kPa at 10 °C and 130 kPa at 80 °C, linear, find p at −50 °C. Python: k = 20/70 = 0,2857 kPa/°C, p = 92,86 kPa, answer 93 kPa, unit kPa, tolerance 0,02 (band 91,0–94,7; k rounded to 0,29 gives 92,6, to 0,3 gives 92,0, all inside). No temperature conversion is needed, so 273 vs 273,15 is irrelevant. Solution in solutions.md rewritten in the usual format. Counts 5/4/3 and ids unchanged.
2. lesson.md micro model: added that a smaller volume makes the pressure grow ("joten paine kasvaa").
3. lesson.md: added one sentence that the direct proportionality of pressure to kelvin temperature is studied properly in later gas courses.
4. lesson.md Tiivistelmä: added bullet on p proportional to T at constant V and n, and that extrapolating the line gives absolute zero.
5. solutions.md L1-03 sanity check: tautology replaced with a meaningful check (below the freezing point of water, above −273 °C).
6. "pyöristyksistä" note: it was only in the old L2-03 solution, which was replaced; no such note remains, so nothing else to attribute to measurement accuracy.
7. Non-blocking editor item 3 (figure label wording) skipped: out of the allowed scope this round (no other changes).

Checks: build --all OK, check_latex OK, test_sims fy3-3 PASS.

New hash (python scripts/gate.py --hash fy3-3): 536cade809f2b051

All reviewers must run again (every edit changes the content hash).
