VERDICT: FAIL
CONTENT-HASH: 8c36c8b4e51792ef

## Blocking
- content/fi/FY7/fy7-8/exercises/solutions.md:18 with exercises.json:18 (fy7-8-L1-02). Category 7/6, A (assessment inconsistency). The new rounding reason says the reliable result is $1{,}2 \cdot 10^3$ turns because $8{,}0\,\text{V}$ has two significant figures. But `answer` 1150 with `tolerance` 0.02 means the box accepts only about 1127–1173 (half a unit in the last shown digit is 5, so 2 % decides). A student who follows the solution and enters 1200 is 4,3 % off and gets "Lähellä", not correct. That breaks the rule that a student who rounds to the data's precision stays inside the tolerance. Fix: write the datum as $8{,}00\,\text{V}$ so that 1150 is justified to three figures, and change the sentence to match. Or keep $8{,}0\,\text{V}$ and raise `tolerance` to 0.05 so that 1200 is accepted.

## Polish
- solutions.md:120 (L3-03 Järkevyys): $331\,\text{MW} : 400\,\text{kV} = 828\,\text{A}$, not $826\,\text{A}$. 826 A belongs to 330,6 MW. Write 330 MW, or 828 A.
- solutions.md (L3-04 Vastaus): two significant figures are better justified by $0{,}040\,\Omega/\text{km}$ than by "200 MW", which has an ambiguous number of significant figures.
- solutions.md (L2-06 Kaava): the stated assumption that current and voltage are in phase in $P_1 = U_1 I_1$ is right to state. At light load a real transformer's primary current is largely magnetising current, so the low efficiency in the first row is partly an artefact of this assumption. The task states the assumption, so this is a C simplification. One clause in b) could say so.

## Checked
- I recomputed all 20 numeric answers from the task texts with my own formulas in one script. All agree with answers.py and exercises.json: 11,5 V; 1150; 5,0 A; 36 kW; 554 MW (√3UI); 210 kW; 90 %; 826 kW; 43,5 mA; 0,992 %; 0,80 Ω; 485,7 (slope through the origin; a slope with an intercept gives 486,6, inside the 3 % tolerance); 87,7 %; 0,20 A; 6,0 Ω; 0,75 %; 4,0 Ω; 3,31; 1,515 M€; 54,3 kW.
- "lämmöksi" is gone from exercises.json, solutions.md, figures.py and the figure catalog; "sisäenergiaksi" is used throughout and agrees with the brief.
- The figures: loss-current is $0{,}8 I^2$, matching the points 0,9…20,1 W; loss-graph-curve is $6\,\Omega \cdot P / U^2$ through (200 kV; 3,0 %) and gives 12 % at 100 kV. The descriptions give the same information as the drawings, and neither gives R away.
- L2-08: the distractors $RI = 75\,\text{V}$, 9,45 MW at 690 V and $U^2 : R = 800\,\text{MW}$ are each really wrong, and their feedback is right. Exactly one option is correct (11,25 kW).
- L1-06: the "virta asettunut vakioksi" condition handles the switch-on transient. The distractors are wrong and their feedback is right.
- L2-06 and L3-05: the row-by-row efficiencies and losses agree. In L3-05, a from the 80 kW row and the 49–57 kW spread from the other rows are correct.
- The two-conductor model is stated in every transmission task, and the three-phase formula is used only where the task says so (L1-05). Everything is within the FY7 scope and the brief.
- Every solution solves symbolically before substituting, and its unit conversions are right.
