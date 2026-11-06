VERDICT: PASS
CONTENT-HASH: c27fc22a4b51258e
Mode: full (translation review against the reviewed Finnish set; new task fy5-16-L2-08)
Round 1

## Blocking
(none)

## Fixed
- None needed; new task fy5-16-L2-08 was already faithful to content/fi.

## Polish
(none)

## Checked
- fy5-16-L2-08 (noise level vs distance with uncertainty): id, level, kind, answer, unit, tolerance, correct flags, choices order, data rows and every number in text, choices, feedback and solution identical to content/fi.
- Recomputed independently: drops 6, 6, 5 dB vs 10 lg 4 = 6.0 dB, difference uncertainty 2 dB; 85 dB +-1 dB action value; all agree with the solution and with the correct choice.
- Distractor feedback keeps the Finnish physics (each wrong option's error named correctly).
- Selkosuomi per NOTES.md section 12: short sentences, common words, glossary terms kept; same physics and numbers as fi; decimal comma in text, point in table cells as in fi.
- check_i18n.py shows nothing for fy5-16; build.py fy5-16 succeeds.
