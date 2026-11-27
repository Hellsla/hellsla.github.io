VERDICT: PASS
CONTENT-HASH: b1b882276359b0a5
SCOPE: delta teacher-figure,wording from b1b882276359b0a5 base b3ee786

## Blocking

## Polish
- inquiry.json:294 — the Järkevyys line says "$4$ beeta miinus -hajoamista, ja kumpikin kasvattaa": "kumpikin" means one of two, but there are four decays — write "jokainen". This is wording only; the physics is right.

## Checked
- inquiry.json:274, task `siirto`: `"exact": true` suits it. The answer is a count of decays (an integer), and it is unchanged at 7.
- Recomputed: n_alpha = (235 - 207)/4 = 7. Beta-minus count = 82 - 78 = 4. The U-238 series: 8 alpha and 6 beta, which is correct.
- Mistake values 28, 10 and 5 are each different from 7, and their feedback is correct.
- Teacher-approved figures and pictures are carried as approved, with no physics change in the diff.
