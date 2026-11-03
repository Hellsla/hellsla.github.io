VERDICT: PASS
CONTENT-HASH: 9ee61ebb9069f1cc

## Blocking

## Polish

## Checked
- One-call recompute: L1 341 m/s, 7.56 mm, 588 Hz, 397 Hz; L2 259 Hz, 3.70 m, 697.8 Hz, 23.07 m/s; L3 27.82 m/s (f0 ≈ 437 Hz), 444 Hz; all match answers.py and the solutions.
- Tolerances now separate the tempting wrong answers: L3-02 0.002 rejects 436/440/446 Hz; L2-01 0.003 rejects 262/256 Hz; L2-03 0.003 rejects 701.6 Hz (moving-source formula).
- L2-02 is stored as 3.70, matching the solution's three significant figures.
- L3-01 has the new intermediate step v_s(f1 + f2) = v(f1 − f2), which is algebraically right.
- L2-01 and L3-02 now use "voimakas hetki" and "huojuntataajuus", consistent with f_h = |f1 − f2|.
- L3-03 split into a/b/c; the physics (odd multiples, so a closed-pipe model with the reed end as the node) is unchanged and right.
- Doppler formula choice and sign are right in L1-04, L2-03, L2-04 and L3-01; still air and the on-line geometry are stated.
- Rounding reasons (2 s.f. limited by the difference in L2-04 and L3-01) are right.
- Notation is the same as the lesson's (v_s, v_h, f_h, f_n = n f_1).
