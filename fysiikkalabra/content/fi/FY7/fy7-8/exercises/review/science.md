VERDICT: FAIL
CONTENT-HASH: 5457f120f0c3d934

## Blocking
- exercises.json fy7-8-L1-02 / solutions.md:18 — A (assessment): the answer is 1150 with tolerance 0,02. The solution then says that because $8{,}0\,\text{V}$ has two significant figures the result is reliable only to $1{,}2\cdot10^3$. A student who rounds that way (1200, 4,3 % off) is outside the tolerance and is marked "Lähellä", not correct. This breaks the rule that a student rounding to the data's precision stays inside the tolerance. — Fix: give $U_2 = 8{,}00\,\text{V}$ and drop the $1{,}2\cdot10^3$ sentence (answer 1150), or raise the tolerance to 0,05.

## Polish
- solutions.md L1-02 Järkevyys — "$29 \cdot 40 \approx 1150$": $29\cdot40 = 1160$. Write $28{,}75 \cdot 40 = 1150$.
- solutions.md L2-06 — $P_1 = U_1I_1$ overstates the input power at light load, because the magnetising current is not in phase with the voltage. The task states the assumption, so this is C. One clause in b) ("osin myös oletuksen $P_1 = U_1I_1$ vuoksi") would make the low-load explanation complete.

## Checked
- Recomputed all 20 numeric answers in one script with my own formulas. All agree with exercises.json and answers.py (largest difference 0,1 %, L2-04).
- L2-04: a least-squares fit through the origin of the five plotted points gives $0{,}801\,\Omega$, and the figure's curve $0{,}8I^2$ passes through (5,0 A; 20 W). L2-09: the curve in figures.py is $RP/U^2$ with $R = 6{,}0\,\Omega$ and passes through (200 kV; 3,0 %).
- L2-05: the slope through the origin gives $N_1 = 485{,}7$, and a free fit gives 486,6. Both are inside the 3 % tolerance.
- L3-05: the data fit the model $P_0 + aP^2$ (a least-squares fit gives 54,1 kW). The stated range of 49–57 kW and the condition for maximum efficiency are right.
- L3-04: $R = 6{,}0\,\Omega$, 909 A and 500 A, 4,96 MW and 1,50 MW, 30 300 MWh, 1,51 M€.
- L1-05: three-phase $\sqrt3\,UI$ with the line-to-line voltage, and its justification are correct. L1-03 notes that three-phase does not change the current ratio.
- L2-08: exactly one correct option. Each distractor's origin ($RI$ = 75 V; 690 V giving 9,5 MW; $U^2/R$ = 800 MW) is computed correctly.
- L1-06: one correct option, and each distractor's feedback is physically right.
- Every solution starts from the basic law, solves symbolically, substitutes with units and justifies its rounding. All are within FY7 scope.
- Hash checked at the start and the end, unchanged.
