VERDICT: PASS
CONTENT-HASH: d5da62db5dfdd014

## Blocking

## Polish
- exercises.json fy3-8-L3-04 (answer 13.2, tolerance 0.03): the Vastaus now tells the student that the minimum gap rounds up to "vähintään 14 mm". A student who types 14 is 6 % off and is marked wrong, so the checker contradicts the model solution. The caller says the answer and tolerance stay as they are on purpose, so I list this only. A tolerance of about 0.07, or a hint that asks for the unrounded value, would fix it. Optional.
- solutions.md:268, carried over: $g_\text{max} + \alpha l_0 \Delta T_\text{talvi} \le g_\text{raja}$ would show that this is an "at most" condition. Optional.

## Checked
- Diff: only the Vastaus line of L3-04 changed. It now gives $g_\text{min} = 13{,}2\,\text{mm}$ and says it is rounded up to at least $14\,\text{mm}$. It also adds "kahden numeron tarkkuudella; alaraja pyöristetään kuitenkin aina ylöspäin". This follows the house rule and the guardrail that an "at least" value is rounded up. With two significant figures (α has two), 13,2 rounds up to 14 mm. This settles my earlier Polish item.
- b) $g_\text{max} = 30 - 12\cdot10^{-6}\cdot 25{,}0\cdot 40\,\text{mm} = 18{,}0\,\text{mm}$ is an "at most" value. It needs no rounding, so 18 mm is on the safe side.
- I recomputed: $12\cdot10^{-6}\cdot 25{,}0\cdot 44 = 13{,}2\,\text{mm}$ and $12\cdot10^{-6}\cdot 25{,}0\cdot 40 = 12{,}0\,\text{mm}$. Both match the solution and answers.py.
- The model answer to c) is still consistent. 15 mm lies between 14 and 18 mm, so it works with the rounded limit too. The gap is 1,8 mm in summer and 27 mm in winter.
- No other line changed. My earlier checks still hold.
- The hash was the same at the start and the end.
