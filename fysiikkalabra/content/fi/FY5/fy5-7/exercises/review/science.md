VERDICT: FAIL
CONTENT-HASH: 0bf9852097a178ac

## Blocking
- fy5-7/exercises/solutions.md:195 (L3-05, Järkevyys / part c) — A, new error from round 1: "ennuste ulottuu yli kolme jaksoa mittausalueen ohi". The measurement ends at 1,6 s, so 5,0 s lies 3,4 s = 2,1 periods past it; 3,125 periods is counted from t = 0. Fix: "ennuste ulottuu yli kaksi jaksoa (3,4 s) mittausalueen ohi" or "kolme jaksoa hetkestä t = 0".

## Polish
- fy5-7/exercises/solutions.md L3-05 — the c) model answer lost its note that damping would add to the error; the task assumes no damping, so this is optional.
- fy5-7/exercises/exercises.json L1-02 and L2-04 — the answer fields are now 5.1 and 7.5, but the solutions say 5,10 ms and 7,50 cm (three significant figures). The value is the same, but the fields could say 5.10 and 7.50 again.

## Checked
- Round-1 Polish items are done: L3-05 now gives 44 cm with two significant figures, justified by T read at 0,2 s steps; L3-04 says "lyönti 6 eli kuudennen lyöntivälin loppu"; L2-06's part b) is under Vastaus, with a new Järkevyys check (t10/10 = 1,48…1,54 s is correct); L3-05's "graph" kind is removed; L2-07's wording is clarified.
- In the reordered MC options of L1-06 and L1-08, exactly one option is correct. The answer string equals the correct option's text, and each feedback matches its option.
- I recomputed every new answer in one script: L1-07 25 s, L2-05 1,639 Hz, L2-06 1,51 s, L2-07 1,342 Hz, L3-04 79,06 %, L3-05 44,24 cm (field 44, inside the 2 % tolerance). All agree with answers.py.
- L3-05's c) check is right: with T = 1,62 s the prediction is 43,1 cm.
- The rest of the set is unchanged since round 1, with the same physics, scope and notation.
- The hash was identical at the start and the end.
