VERDICT: PASS
CONTENT-HASH: b767859bee6529a5

## Blocking
none

## Polish
- solutions.md fy1-3-L1-08 — the heading "## fy1-3-L2-05" follows directly after the Järkevyys line with no blank line; add one so the heading renders.
- exercises.json fy1-3-L1-08 — the answer unit "kertaa" is fine; add "Anna vastaus lukuna." or keep the unit empty so a student does not type "100 kertaa" into a numeric field.
- exercises.json fy1-3-L3-04 — four asks in one task (permission, mean, no-note case, range comparison); the stored answer checks only 2,41 s. Acceptable at level 3; split the last sentence into its own numbered part if students skip it.
- solutions.md fy1-3-L2-05 — the Järkevyys line says 1,800 s lies just outside 1,820 ± 0,015 s; correct but it hints at an error the task never asks about. Keep, but phrase as "mahdollinen syy" only if the lesson has taught systematic error (it has, per L2-06).

## Checked
- L1-08 now compares two instruments (ratio 100): a new step, not a copy of L1-05; answers.py and solution agree.
- L2-05 ends with one question sentence in the form T ± ΔT; the solution's rounding (ΔT = 0,015 s, two digits) is explained.
- L2-06 no longer names instruments, removing the pipette-less-accurate misconception; A: +0,94 ml, B closer, A more repeatable; justification uses the half-ranges and means.
- L3-04 uses a logbook entry and contrasts the half-range with and without 2,97 s (0,03 against 0,30 s); numbers recomputed (2,48 s, 0,295 s).
- L3-05 asks for the interval comparison first, number as a check; the solution now says the gap exceeds the stated uncertainties and does not overclaim.
- L1-07 solution corrected to "liian tarkka" with 5,428 cm.
- Counts 8/7/5 = 20; figure task L1-03 unchanged.
