VERDICT: PASS
CONTENT-HASH: 1acfcf757217e158

## Blocking

## Polish
- exercises.json:358–361 (fy3-8-L3-04): the answer is 13,2 mm with a 3 % tolerance. A student who enters the practical, safe-side value 14 mm that the Vastaus now recommends is marked wrong (6 % off). The field could say "laskettu pienin rako", or the tolerance could be widened to take 14.
- solutions.md:268 (rail-gap task), carried over: $g_\text{max} + \alpha l_0 \Delta T_\text{talvi} \le g_\text{raja}$ would show that this is an "at most" condition. Optional.

## Checked
- I read the changed Vastaus of L3-04 on disk (solutions.md:276). "Käytännössä vähintään 14 mm" now rounds the minimum gap to the safe side: a "vähintään" value is rounded up with two figures, as the guardrail and CLAUDE.md require. The b) maximum of 18 mm is an exact 18,0 mm, so rounding it down changes nothing.
- I recomputed both limits: $12\cdot10^{-6}\cdot 25{,}0\cdot 44 = 13{,}2\,\text{mm}$ and $30 - 12\cdot10^{-6}\cdot 25{,}0\cdot 40\cdot 1000 = 18{,}0\,\text{mm}$. answers.py gives 13,2 mm, which matches.
- The model answer to c) stays consistent: $15\,\text{mm}$ lies between 13,2 and 18 mm (and above 14 mm). The summer and winter gaps are 1,8 mm and 27 mm. The case of installing in winter frost ($\Delta T = 84\,\text{K}$, 25,2 mm > 15 mm) is unchanged and correct.
- The multi-row Kaava block (solutions.md:265–271) was not changed and still solves symbolically for each limit.
- No other line of the set changed. My previous checks still hold.
- The hash was the same at the start and the end.
