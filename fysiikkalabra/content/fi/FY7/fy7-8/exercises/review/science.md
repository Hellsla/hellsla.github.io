VERDICT: PASS
CONTENT-HASH: f70b284460cf3f45

## Blocking

## Polish
- solutions.md (L3-03 Järkevyys): $331\,\text{MW} : 400\,\text{kV} = 828\,\text{A}$, not $826\,\text{A}$. 826 A belongs to 330,6 MW. Write 330 MW, or 828 A.
- solutions.md (L3-04 Vastaus): two significant figures are better justified by $0{,}040\,\Omega/\text{km}$ than by "200 MW", which has an ambiguous number of significant figures.
- solutions.md (L2-06 Kaava): the assumption $P_1 = U_1 I_1$ is stated, which is right. At light load the primary current is largely magnetising current, so the low efficiency of the first row is partly an artefact of this assumption. This is a C simplification; one clause in b) could say so.
- solutions.md (L1-02 Järkevyys): $230 : 8{,}00 = 28{,}75$. "Noin 29-kertaisesti … 1160, lähellä 1150" is a valid estimate. Writing $28{,}75 \cdot 40 = 1150$ would make the check exact.

## Checked
- Round 1's Blocking item (L1-02) is fixed. The datum is now $8{,}00\,\text{V}$, so $N_1 = 40 \cdot 230 : 8{,}00 = 1150$ is justified to three significant figures by 230 V and 8,00 V. Answer 1150 with tolerance 0.02 now agrees with the stated precision. answers.py gives 1150, which is numerically unchanged. The diff since round 1 (`git diff HEAD~2`) touches only L1-02 in exercises.json and solutions.md.
- I recomputed all 20 numeric answers from the task texts with my own formulas in one script. All agree with answers.py and exercises.json: 11,5 V; 1150; 5,0 A; 36 kW; 554 MW (√3UI); 210 kW; 90 %; 826 kW; 43,5 mA; 0,992 %; 0,80 Ω; 485,7 (slope through the origin; a slope with an intercept gives 486,6, inside the 3 % tolerance); 87,7 %; 0,20 A; 6,0 Ω; 0,75 %; 4,0 Ω; 3,31; 1,515 M€; 54,3 kW.
- "lämmöksi" is gone from exercises.json, solutions.md, figures.py and the figure catalog; "sisäenergiaksi" is used throughout and agrees with the brief.
- The figures: loss-current is $0{,}8 I^2$, matching the points; loss-graph-curve is $6\,\Omega \cdot P / U^2$ through (200 kV; 3,0 %). The descriptions match the drawings, and neither gives R away.
- L2-08: the distractors $RI = 75\,\text{V}$, 9,45 MW at 690 V and $U^2 : R = 800\,\text{MW}$ are each really wrong, and their feedback is right. Exactly one option is correct (11,25 kW).
- L1-06: the "virta asettunut vakioksi" condition handles the switch-on transient. Exactly one option is correct, and the feedback is right.
- L2-06 and L3-05: the row-by-row efficiencies and losses agree. In L3-05, a from the 80 kW row and the 49–57 kW spread from the other rows are correct.
- The two-conductor model is stated in every transmission task, and the three-phase formula is used only where the task says so (L1-05). Everything is within the FY7 scope and the brief. Every solution solves symbolically before substituting.
