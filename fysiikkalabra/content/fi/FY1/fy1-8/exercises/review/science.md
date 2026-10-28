VERDICT: PASS
CONTENT-HASH: f4fca3b182c3189f

Round 2: re-check of round-1 Blocking items against the fix diff. Round 3: L2-01 tolerance raised to 0,21 after the round-2 Polish item.

## Blocking

## Polish
- exercises.json:28 L1-04 — a table that is 24 cm long is implausible. Use a book or a sheet of paper, or 124 cm.
- exercises.json:90 L3-02 — "Kuumaa vettä jäähtyy kupissa" should be "Kuuma vesi jäähtyy kupissa". The reasonableness check uses a reading error of 0,1 K that the task never gives.
- solutions.md L2-02 — "reaktioajan 0,20 s virhe" should be "ajanoton epävarmuus" (guardrail terms).
- solutions.md L3-03 — a count is exact: "tasan 4 toistoa" instead of "4,0, kaksi merkitsevää numeroa".

## Checked
- Round-1 Blocking L2-01 is resolved: the tolerance is now 0,21 (accepted range 1,975–3,025), so both 2,5 and the one-figure "3" that the solution recommends are accepted with a margin, not on the boundary; the full-range slip 5 % (0,4 s : 8,0 s) is still rejected. The solution's added sentence "Vastauskenttä hyväksyy kummankin" is true. The answer key 2,5 still equals answers.py.
- Round-1 Blocking L3-01 is resolved: the tolerance is now 0,1. The reported 0,03 is 9,1 % from 0,033 and is accepted; values outside 0,0297–0,0363 (e.g. 0,066 for the full difference) are still rejected. The added sentence is true.
- L3-02 change: the substitution now writes 80,0 °C − 68,0 °C = 12,0 K and 52,0 °C − 47,0 °C = 5,0 K. This is correct (a temperature difference in °C equals one in K), consistent with the conversion line, and the answer 1,4 K/min is unchanged.
- The diff touches only these lines. All other content is unchanged since the full review at 424b0972f9e99c5a, where every answer was recomputed (L1 5,0/12,4/0,4167/0,2/3,17; L2 2,5/10/0,42/16; L3 0,033/1,4/4,0).
- Hash identical at start and end.
