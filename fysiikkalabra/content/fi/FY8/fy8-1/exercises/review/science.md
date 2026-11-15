VERDICT: PASS
CONTENT-HASH: 8dc2567292c69c38
SCOPE: delta added-exercise from 5b627e2749906f73 base 5a45b28682e8

## Blocking

## Polish
- lessons/FY8/fy8-1/answers.py:368 — the comment still says "387,6 nm -> 388 nm", but the line computes 387,50 nm, which matches the answer 387 and solutions.md. — Change the comment to "387,5 nm -> 387 nm".
- solutions.md fy8-1-L2-08 Sijoitus — the chain uses f0 = 5,56 (·10^14 Hz), but the student can only read about 5,6 from the figure. With 5,6 the result is 2,65 eV, which is still inside the tolerance, so this is not an error. — Write "(12 − 5,6) ≈ 2,65 eV", or say that 5,56 is the exact value W/h behind the figure.
- solutions.md fy8-1-L2-09 Vastaus — the "±1 %" claim is still loose. A reading of 7,0 ± 0,1 (·10^14 Hz) gives 422–434 nm, which is about ±1,5 % (±6 nm). — State the reading uncertainty and the ±6 nm it gives.

## Checked
- Delta scope: I judged the three added exercises (L1-10, L2-08, L2-09) and the round-2 change to L2-08's substitution chain and reasonableness check.
- L1-10: λ0 = hc/W with W = 3,20 eV gives 387,50 nm, so the answer 387 and the 5 % tolerance are right. The UV-A remark is right ✓.
- L2-08: the figure's line A (W = 2,30 eV) at 12·10^14 Hz gives 4,963 − 2,30 = 2,663 eV. The new chain 0,4136 · (12 − 5,56) = 2,664 eV is right. The check hf = 4,96 eV > E_k,max > 0 is a real check. The reading "0,3 below the 3 eV line" (≈2,7 eV) matches the figure ✓.
- L2-09: line B (W = 2,90 eV) has f0 = 7,011·10^14 Hz, so c/f0 = 427,6 nm. The read value 7,0 gives 428,3 nm. Both are within 4 %. The remark that the vertical intercept is −W is correct ✓.
- I recomputed all three answers in one independent script and they agree with the output of answers.py.
- The hash was 8dc2567292c69c38 at the start and at the end.
