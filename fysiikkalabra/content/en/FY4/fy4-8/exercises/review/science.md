VERDICT: PASS
CONTENT-HASH: f7a673e91042d426

## Blocking
None.

## Polish
1. solutions.md L1-05, L2-06: E_mek0 is used but the lesson defines only E_k0, E_p0; the index rule covers it, but "E_mek0 = E_p0 + E_k0" once in the solution would help.
2. solutions.md L2-05 Vastaus: the two-significant-figure reason cites h = 0,05 m (one figure); cite 0,30 m or the speeds instead.
3. answers.py comments still use W_kok, W_muut, E_mek,2 (not student-facing).

## Checked
- Every answer recomputed from the task text (own script, LSQ fits through origin for L2-05 and L2-07): L1-01…L1-07, L2-01…L2-09, L3-01…L3-05 all agree with exercises.json and answers.py (e.g. L2-05 g = 9,77, L2-06 −19,93 kJ and 94/107/157 N, L2-07 1,14 N, L2-08 1,02 m, L3-04 54,9 N and 6,87 m/s, L3-05 63,9 %).
- Added exercises (L1-07…L1-09, L2-05…L2-09, L3-04, L3-05): physics, conditions (constant friction, no air drag, tension does no work), exactly one correct option / correct true-false key, every distractor's feedback right.
- Each solution names which work W is (total in the work principle, other forces' in the energy principle); no leftover old symbol; fi, fi-easy and en answers, tolerances and keys identical.
