VERDICT: PASS
CONTENT-HASH: d214530249e4e882

## Blocking

## Polish
- lessons/FY1/fy1-3/answers.py:31 — comment "relative error = Δt / mean" should read relative uncertainty, as solutions.md L2-01 now does (comment only; the number is right).

## Checked
- Every answer recomputed independently: L1-01 0.51 s; L1-02 +0.3 cm; L1-03 0.35 s (figure fy1-3/pendulum-dots data 12.2–12.9 s); L1-04 47.5 g; L1-05 0.5 mm; L2-01 0.09/1.865 = 4.83 %; L2-02 10.67 mm; L2-03 12.4 cm; L2-04 10; L3-01 −0.06 s; L3-02 2.0 µm; L3-03 0.26 cm.
- Answers rounded per the lesson's rule (L1-03 0.4 s, L2-01 5 %, L2-02 11 mm) stay inside the relative tolerances.
- L3-01 sign reasoning (late start shortens, late stop lengthens the reading) is correct; the check 3.44 s → 3.50 s holds.
- L3-02: reading uncertainty of the stack divided by an exact count; relative uncertainty 2 % vs 500 % for one sheet is right.
- L2-02 and L3-03 treat a worn zero end / offset as systematic and estimate it as mean − true value; the random part (±1.5 mm, 0.025 cm) is correctly compared.
- Solutions use the terms of the lesson: measurement error signed, uncertainty positive, "relative uncertainty" in L2-01 and L3-02; d/2 given with the total-uncertainty caveat (L1-05).
- Each solution has the seven parts, symbols before numbers, and a real reasonableness check.
- exercises.json numbers, answers, units and tolerances equal the Finnish source.
- Hash bde42af53c34a13e at start; re-checked after the mid-review edit (git diff: L2-04 unit "kertaa" → "times" only): d214530249e4e882 at end.
