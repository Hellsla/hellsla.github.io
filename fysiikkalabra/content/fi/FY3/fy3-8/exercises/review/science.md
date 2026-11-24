VERDICT: PASS
CONTENT-HASH: 2668999cc1d29224

## Blocking

## Polish
- solutions.md:276 (fy3-8-L3-04 Vastaus): now that "käytännössä vähintään 14 mm" is gone, the closing sentence "tulokset kelpaavat kahteen numeroon pyöristettyinä" leaves the student to round the minimum gap 13,2 mm to 13 mm, which is on the unsafe side. The guardrail says a "vähintään" value is rounded up. Suggested wording: "pienin rako pyöristetään turvalliselle puolelle ylöspäin (noin 14 mm); laskettu arvo on 13,2 mm". The answer field stays 13,2 mm. Optional.
- solutions.md:268 (rail-gap task), carried over: $g_\text{max} + \alpha l_0 \Delta T_\text{talvi} \le g_\text{raja}$ would show that this is an "at most" condition. Optional.

## Checked
- The diff removes only the words "käytännössä vähintään 14 mm" from the Vastaus of L3-04. My earlier Polish item about the tolerance (a student entering 14 mm was marked wrong) is now moot.
- I recomputed both limits: $12\cdot10^{-6}\cdot 25{,}0\cdot 44 = 13{,}2\,\text{mm}$ and $30 - 12\cdot10^{-6}\cdot 25{,}0\cdot 40 = 18{,}0\,\text{mm}$. answers.py line 37 gives 13,2 mm, and the stated numbers are correct.
- The model answer to c) is consistent: 15 mm lies between 13,2 and 18 mm. The summer and winter gaps are 1,8 mm and 27 mm, and installing in winter frost gives 25,2 mm > 15 mm.
- The Järkevyys check (25,2 = 13,2 + 12,0; a window of 4,8 mm) is unchanged and correct.
- No other line changed. My earlier checks still hold.
- The hash was the same at the start and the end.
