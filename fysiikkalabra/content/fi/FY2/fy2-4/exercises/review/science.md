VERDICT: PASS
CONTENT-HASH: be130260722cc92a

Round 3: there were no blocking items in round 2. Commit 442c889ba made two changes to fi fy2-4, both in L2-08. It split the η chain in the correct option's feedback (exercises.json) and the Rivi 2 line of the model answer (solutions.md) into shorter inline formulas joined by "eli". Nothing else in the exercise set or answers.py changed.

## Blocking
(none)

## Polish
- exercises.json:256 (fy2-4-L2-08, carried over) — η = 60 % is low for a 2,5 kW motor (typically 80–90 %). This is optional: E_a = 510 kJ (85 %) keeps the same error pattern.
- lessons/FY2/fy2-4/answers.py (carried over) — add the comment "# fy2-4-L2-08 is multiple choice: no number (η = 360 kJ : 600 kJ = 0,60)".
- solutions.md L3-05 (carried over) — write "suoraan lämmöksi": the light also ends up as thermal energy.
- docs/exercise-bank/FY2.md:29–30 (carried over) — the plan still lists c·m·ΔT and chain-efficiency tasks (FY3).

## Checked
- Diff 9fd1b2088..HEAD for fi fy2-4: only the two L2-08 lines changed. answers.py and every other task are unchanged.
- Feedback, recomputed: the split chain is η = E_a : E_o, eli η = 360 kJ : 600 kJ = 0,60, eli 60 %. The formula, the numbers and the direction of the ratio are as before and right. Splitting at "eli" leaves no false equality.
- Solution, recomputed: the Rivi 2 line is E_o = 2500 W · 240 s, eli E_o = 600 000 J = 600 kJ. 2500 · 240 = 600 000 is right, and the line still agrees with Rivi 2 of the task and with the option feedback.
- Exactly one option is still correct (Rivi 4), the wrong options' feedback is unchanged and right, and the task still says "tasaisesti".
- The hash was be130260722cc92a at the start and at the end.
