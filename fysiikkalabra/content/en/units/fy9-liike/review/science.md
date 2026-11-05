VERDICT: PASS
CONTENT-HASH: 47fff9ff6ab0e619

Science review of the English translation of fy9-liike, round 2 (source content/fi/units/fy9-liike/, reviewed PASS).

## Checked
- Round-1 science review had no Blocking findings. The fixes since then (git diff against the checkpoint) change words only: trolley → cart, gendered pronouns → neutral wording, "average velocity" → "average speed" in s4 (round-1 Polish 1, taken), "Tasks" → "Exercises" in teacher.md, one sentence in unit.md Common mistakes, and the s3 figure label "braking distance" → "braking dist.". No number, formula, unit or answer changed.
- Structure of inquiry.json, exit-ticket.json, sovella/tasks.json and unit.json compared to the Finnish again: every non-text field (answers, correct flags, tolerances, points, ids) identical. `check_i18n.py`: en 0 errors; `practice.py check`: en/units/fy9-liike 6 tasks, 95 points, OK.
- s4 "average speed": on the straight 3.0 km road it is the displacement (= distance) divided by the time, so the wording "average speed is the displacement divided by the time" stays correct; the instantaneous quantity is still called velocity, consistent with the source's distinction.

## Blocking
(none)

## Polish
1. Coordinates such as "(12 s; 85 km/h)" still use the Finnish semicolon separator; a comma is the usual English form with a decimal point (inquiry.json, s3 task/solution, figure description). Not wrong.
