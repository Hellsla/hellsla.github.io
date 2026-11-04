VERDICT: PASS
CONTENT-HASH: 44dcfc0bfd9ecb00

## Blocking

## Polish
- fy5-8/exercises/solutions.md L1-08 — "0,04 m" in the check and in the Sijoitus difference: write 0,040 m so the two significant figures of the answer are visible.

## Checked
- Round-1 Blocking 1 is fixed: L3-05 no longer assumes the string and spring are massless, and the loss explanation (kinetic energy of spring and string, vibration, sound, heat) is now consistent; the Vastaus keeps only the straight-line assumption.
- Round-1 Blocking 2 is fixed: L1-08 reads the real grid points (0,08 m; 2,0 N) and (0,12 m; 3,0 N) and checks with (0,04 m; 1,0 N); all lie on line B (25 N/m), and answers.py follows.
- The Polish items are done: "Hooken laki" is replaced by harmoninen voima F_v = kx; L1-06 feedback now says "välttämättä"; L2-05 now gives 24,4 N/m in both places (tolerance 0.03 still accepts 24); L3-04 asks for the stretching work W and states the hysteresis (the area is an upper bound for the returned energy).
- I recomputed every new answer in one script: L1-08 25 N/m, L2-05 24,40 N/m, L2-06 24,53 N/m, L2-07 0,60 J, L3-04 0,255 J (½kx² from the first point gives 0,36 J, 41 % more), L3-05 73,05 % (answers.py 73,15 %). All are within tolerance.
- In the MC tasks L1-06 (options reordered) and L1-07, exactly one option is correct and the answer string equals it.
- No new physics errors are introduced; scope and notation match the lesson.
- The hash was identical at the start and the end.
