VERDICT: PASS
CONTENT-HASH: 6c786ed6b0783012

## Blocking
None.

## Polish
- The question does not say the limit is a maximum; the solution explains the round-down to 11 A, and both roundings pass, so no student is penalised.

## Checked
- Key 11.5 with relative tolerance 0.05 accepts 10.93-12.08 A: 11, 11.96 and 12 A pass; 13 A (26.04 A per phase, trips the 25 A fuse) and 10 A fail. Matches the round-2 fix and the teacher's decision.
- answers.py expression gives (11+12)/2 = 11.5; its comment states the reasoning and the accepted range.
- exercises.json change identical across the three languages; model answer still 11 A, consistent with the solution.
