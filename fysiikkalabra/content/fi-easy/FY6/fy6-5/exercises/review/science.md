VERDICT: PASS
CONTENT-HASH: 7411b0bebaf66c44
SCOPE: delta caption-label,md-paragraphs,numbers,reflow,teacher-figure,typography,wording from 5cfc1e1a443815c4 base a5182aa75cb9

## Blocking
- none

## Polish
- solutions.md:5 L1-01 — $\Sigma I_\text{tulo} = \Sigma I_\text{lähtö}$; the lesson's subscripts are $I_\text{tulevat}$, $I_\text{lähtevät}$.

## Checked
- L1-02 now opens with $\sum \Delta V = 0$, which is the lesson's voltage law, followed by the signed row $U - U_1 - U_2 = 0$.
- I recomputed all 14 changed solutions in one script from the task data: 1,2 A, 7,5 V, 3,5 V, 8,0 V, 0,50 A, 60 Ω, −9,0 V, 30 Ω, 1,8 V, 3,0 V, 0,59 A, 40 Ω, −3,0 V, $I_2 = 0{,}30\,\text{A}$. All agree.
- L3-04: the rows $R_1R_3I_2 = R_3(U_1 - R_2I_2) + R_1(U_2 - R_2I_2)$ give $I_2 = (U_1R_3 + U_2R_1) : D$ with $D = R_1R_3 + R_2R_3 + R_1R_2$. I re-derived this from the junction law and both loops. The numbers are 630 V·Ω and 2100 Ω², so $I_2 = 0{,}30\,\text{A}$.
- L3-05: $R_\text{p} = R_1V_P : (U - V_P)$ and $R_\text{k} = R_\text{p}R_2 : (R_2 - R_\text{p})$ re-derived.
- L3-01 and L2-07: the signs of $V_-$ and $V$ are right, with the potential falling in the direction of the current.
- L2-02, L3-01, L2-06, L2-07 substitute into the last symbolic form. The current is still given as a check.
- The paragraph splits in L1-07, L3-04, L3-05 and L2-08 change no physics.
- The task figures are teacher-approved.
- Content hash checked at start and end. It changed during the review; the cause was the L3-04 commit and the L1-02 edit, and I reviewed both.
