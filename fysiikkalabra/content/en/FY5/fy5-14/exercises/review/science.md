VERDICT: PASS
CONTENT-HASH: 3d819c47cdf8c4a4
SCOPE: delta added-exercise from 4d7d493e28a99432 base 81db4a6fd727

## Blocking
(none)

## Polish
- solutions.md fy5-14-L1-10 — "1400 Hz, three significant figures" is ambiguous as written — "1.40·10³ Hz (1400 Hz)".

## Checked
- fy5-14-L1-10 (seventh harmonic): figure peaks at 200, 400, …, 1000 Hz; f1 = 200 Hz (lowest, also the spacing); f7 = 7 f1 = 1400 Hz; the note that the strongest peak (400 Hz) is the second harmonic is right. answers.py and JSON agree.
- fy5-14-L2-08 (choice task): figure envelope |cos(π · 4 Hz · t)| gives loud moments every 0.25 s, f_b = 4 Hz; wax lowers f_x and the beats speed up, so f_x < 523 Hz: 519 Hz. Exactly one option correct (same as the Finnish), each distractor really wrong and its feedback names the right error (side, equal frequencies, 8 Hz from counting quiet moments).
- The model answer gives both candidates 523 ± 4 Hz and decides by the wax test, with a check.
- Figures: English description and labels (f (Hz), height; t (s) 0.2 … 1.0) give the values the solutions quote; no answer given away.
- Compared with the Finnish set by script: every number in text, choices, feedback and solution, the correct flags, unit, tolerance and figure ids identical.
- Hash unchanged at start and end.
