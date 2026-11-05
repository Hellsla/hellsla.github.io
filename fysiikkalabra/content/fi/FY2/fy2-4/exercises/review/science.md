VERDICT: PASS
CONTENT-HASH: 57ac81df4bc38cd2

Round 2: there were no blocking items in round 1. The fix commit 9fd1b2088 changed only the text of exercises.json L2-08. The task now says "ottaa sähköverkosta tasaisesti tehon 2,5 kW", which resolves my round-1 B item, and Rows 1–4 are shortened to "suure = kaava, eli sijoitus, joten tulos". solutions.md, answers.py and every other task are unchanged since round 1.

## Blocking
(none)

## Polish
- exercises.json:256 (fy2-4-L2-08, carried over) — η = 60 % is low for a 2,5 kW motor (typically 80–90 %), though possible for a small or old one. This is optional: E_a = 510 kJ (85 %) keeps the same error pattern.
- lessons/FY2/fy2-4/answers.py (carried over) — add the comment "# fy2-4-L2-08 is multiple choice: no number (η = 360 kJ : 600 kJ = 0,60)", as fy2-3 has.
- solutions.md L3-05 (carried over) — write "suoraan lämmöksi": the light also ends up as thermal energy.
- docs/exercise-bank/FY2.md:29–30 (carried over) — the plan still lists c·m·ΔT and chain-efficiency tasks (FY3).

## Checked
- Diff 18b454cd1..HEAD for fy2-4: only the L2-08 text line changed, and none of the other exercise or answer files did.
- I recomputed the shortened rows: 2,5 kW = 2500 W and 4,0 min = 240 s are right. E_o = 2500 W · 240 s = 600 000 J = 600 kJ is right (the 600 000 J step was dropped, and the result is still correct). E_h = 600 − 360 = 240 kJ is right. Row 4 is still the only wrong row, η = E_o : E_a = 1,67; the correct value is 360 : 600 = 0,60.
- Exactly one option is correct (Rivi 4). The feedback still matches the shortened rows, and its numbers (600 000 J, 600 kJ, 240 kJ, 60 %, 167 %) all appear in or follow from the task.
- "Tasaisesti" now gives the condition that Row 2's E = P·t and the feedback's "tasaisella teholla" need, so the task, the feedback and solutions.md agree.
- answers.py runs, and every numeric answer agrees with exercises.json within tolerance (unchanged).
- The hash was 57ac81df4bc38cd2 at the start and at the end.
