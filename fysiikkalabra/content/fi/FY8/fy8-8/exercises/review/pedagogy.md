VERDICT: PASS
CONTENT-HASH: 5d522b9e7134f99f

## Blocking
(none)

## Polish
- exercises.json fy8-8-L2-08, wrong-option feedback — each says "Rivi n on oikein" and shows the check (fair as repair), but "Jos pidät riviä virheellisenä, ajattelet ehkä ..." guesses at the student's thought. End after the check.
- stem — "Mikä rivi on väärin? Jos yhtälöissä ei ole virhettä, valitse viimeinen vaihtoehto." mixes two instructions. Put the last-option rule before the equations and end with "Mikä rivi on väärin?".
- solutions.md — the closing sentence "Opiskelija on käyttänyt beeta plus -hajoamisen sääntöä Z - 1" explains the slip well; keep it.

## Checked
- New task fy8-8-L2-08 (find the error, type 4): rows 1, 2, 4 verified (210 = 206 + 4, 84 = 82 + 2; 6 = 5 + 1; 99/43 unchanged); row 3: 52 + (-1) = 51, not 53. Iodine-131 gives xenon-131 (Z = 54).
- The error is the lesson's warned one (beta minus raises Z by 1). Distractors cover the beta plus/minus mix-up and gamma as an element change.
- "Yhtälöissä ei ole virhettä" is last, as the type requires; its feedback sends the student to check every row.
- Notation (electron, positron, antineutrino) matches the brief; stays within the chapter.
- Method: text only (packet, exercises.json, solutions.md, git diff of the new task); no renders opened. Long formula chains are wrapped by scripts/mathlayout.py per CLAUDE.md, so no separate 300 px finding.
