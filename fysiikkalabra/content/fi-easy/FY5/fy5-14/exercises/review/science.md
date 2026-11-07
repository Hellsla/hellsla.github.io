VERDICT: PASS
CONTENT-HASH: 4f133c9649fea97d
Mode: full (translation review against the reviewed Finnish set; new task fy5-14-L1-09)
Round 1

## Blocking
(none)

## Fixed
- None needed; new task fy5-14-L1-09 was already faithful to content/fi.

## Polish
(none)

## Checked
- light delta review (teacher 2026-11-07), LOPS extension marking: diff vs origin/main: only the text prefix 'Syventävä tehtävä.' / 'Extension task.' on L1-04, L2-03, L2-04, L2-05, L2-07, L3-01, L3-04 and L2-03's core flag removed; data, answers, solutions and answers.py unchanged. The seven are exactly the tasks that calculate a Doppler frequency, so they match the lesson's move of the formulas to Lisätiedoksi; the remaining Doppler task L1-07 (core) is qualitative (constant, higher pitch; fronts denser in front) and needs no formula. No physics changed.
- fy5-14-L1-09 (true/false: violin spectrum and moving car horn): id, level, kind, answer, unit, tolerance, correct flags, choices order, data rows and every number in text, choices, feedback and solution identical to content/fi.
- Recomputed independently: fundamental 330 Hz; statements 2 and 5 true, 1, 3, 4 false; all agree with the solution and with the correct choice.
- Distractor feedback keeps the Finnish physics (each wrong option's error named correctly).
- Selkosuomi per NOTES.md section 12: short sentences, common words, glossary terms kept; same physics and numbers as fi; decimal comma in text, point in table cells as in fi.
- check_i18n.py shows nothing for fy5-14; build.py fy5-14 succeeds.
