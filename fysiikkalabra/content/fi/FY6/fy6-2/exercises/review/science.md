VERDICT: PASS
CONTENT-HASH: dcfc3915e8b2c9f3
SCOPE: delta added-exercise from 8a721a86e7a34235 base 8f23aa7ae3bd

## Blocking

## Polish
- content/fi/FY6/fy6-2/exercises/solutions.md (fy6-2-L2-10, Vastaus) — "noin 3,0 kertaa" gives two figures although U₀ − U = 0,08 V has one; "noin 3 kertaa" matches the data's precision.

## Checked
- Hash dcfc3915e8b2c9f3 at start and end; delta round 2: only fy6-2-L2-09 and fy6-2-L2-10 judged.
- Round-1 blocking item resolved: L2-10 `tolerance` is now 0.12, so the lesson-rule route with ΔU rounded to 0,03 V (0,08 V : 0,03 V = 2,67, 10,5 % off) and the unrounded route (2,98) are both accepted.
- L2-09 recomputed: ΔU = 0,005 · 1,37 V + 2 · 0,01 V = 0,02685 V; rounded 0,03 V is 11,7 % off, inside 0.12. answers.py agrees.
- L2-10 recomputed: (1,45 V − 1,37 V) : 0,02685 V = 2,98; conclusion "not consistent" is right (1,45 V outside 1,37 ± 0,03 V); the suggested cause (lamp run at another voltage) is sound.
- Figure generator: display 1,37 V, pointer at the 20 V range (resolution 0,01 V, as the lesson's table); alt text gives reading and range, no error limit.
- Both solutions: symbolic Δx = p·x + n·r before numbers, rounding by the lesson's rule, real checks. Notation as in the lesson.
