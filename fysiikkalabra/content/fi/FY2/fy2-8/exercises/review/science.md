VERDICT: PASS
CONTENT-HASH: 0d804621ffb859e2

Round 2 (round 1: PASS, Polish only). New YO-skill task L2-08 (type 10, Mittausdata); the rest of the set was PASS before and is unchanged.

## Blocking

## Polish
- exercises.json L2-08 first choice, feedback, and solutions.md L2-08 — the 2020–2021 case still compares the difference with one value's uncertainty ("5 kt on pienempi kuin 10 kt"). The conclusion is right, and the intervals 510–530 and 505–525 do overlap, so this is C. For consistency with the correct option, you could add "välit 510–530 kt ja 505–525 kt menevät päällekkäin".

## Checked
- Round-1 Polish acted on: the correct option's feedback and the solution now compare the intervals (510–530 kt and 410–430 kt do not overlap), as the data guardrail asks. The stem says "vuosittainen elinkaaripäästö". answers.py now lists L2-08 as multiple choice, and a blank line precedes the solutions heading.
- Rewritten options, judged one by one. "ero 5 kt on suurempi kuin 10 kt" is false, and its feedback says so. The biomass option claims a cause that is not in the data, and the feedback is right even though the option now adds a true clause. The 2034 extrapolation gives 420 − 25 · 10 = 170 kt, 10 years beyond 5 years of data, and the feedback is right. The "unchanged" option reads the wrong column, and the feedback is right.
- Exactly one correct option, and the answer equals its text. "todennäköisesti todellista" and "ei voi osoittaa" follow the guardrail wording.
- Recomputed from the table: differences of 100 kt and 5 kt; emission per energy goes from 520 to 420 g/kWh, which is realistic.
- Ran answers.py against exercises.json in one script: all 17 numeric answers are within tolerance.
- The data are marked as invented ("esimerkkiaineisto, ei tilasto"). Scope stays within FY2.
- The hash was unchanged at the start and at the end (0d804621ffb859e2).
