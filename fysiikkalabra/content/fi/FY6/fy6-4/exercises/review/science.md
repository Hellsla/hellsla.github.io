VERDICT: FAIL
CONTENT-HASH: f3db54128b103065
SCOPE: delta caption-label,md-paragraphs,numbers,reflow,teacher-figure,typography from b76783ab2894e5cb base b5600a6

## Blocking
- content/fi/FY6/fy6-4/exercises/solutions.md:15, 45, 55, 65, 75, 85, 96, 136, 158, 169, 180, 191, 243 — (B, consistency) the new Kaava blocks open with $\Sigma I = 0 \Rightarrow I = I_1 + I_2$ and $\Sigma U = 0 \Rightarrow U = U_1 + U_2$. This chapter does not teach Kirchhoff's laws: its brief derives both rules from "jännitteet summautuvat, $U = U_1 + U_2$" and "virrat summautuvat, $I = I_1 + I_2$". Read with the chapter's positive voltages and currents, "the sum is zero" is false, because no sign convention is given. The next chapter writes the laws differently, as $\sum I_\text{tulevat} = \sum I_\text{lähtevät}$ and $\sum \Delta V = 0$ with signed potential changes, so the student meets two different forms. Fix: remove the "$\Sigma I = 0 \Rightarrow$" and "$\Sigma U = 0 \Rightarrow$" prefixes and start each block from the lesson's own principle row ($I = I_1 + I_2$, $U = U_1 + U_2$, $U = R_1 I + R_{23} I$). In L3-05 (line 191), write the series and parallel rules without $\Sigma$.

## Polish
- content/fi/FY6/fy6-4/exercises/solutions.md:106 — L3-02 states $\tfrac{1}{R_\text{rinnan}} = \tfrac{2}{R_1}$ without the row $\tfrac{1}{R_\text{rinnan}} = \tfrac{1}{R_1} + \tfrac{1}{R_1}$. That row would match the series line above it.

## Checked
- Hash f3db54128b103065 at start and end. Delta: the new Kaava blocks, the split paragraphs (L3-05, L2-08) and the figure pictures the teacher approved.
- Every new derivation is algebraically correct. The aligned rows reach the same final formula as before.
- New closed forms recomputed: L3-01 $I_3 = R_{23}U/(R_3(R_1+R_{23}))$ = 50 mA; L3-04 $I_3 = R_{23}U/(R_3R)$ = 36 mA; L2-09 R = 18 Ω, I = 0,50 A; L3-03 root 150 Ω; L2-03 20 Ω; L1-08 60 Ω.
- answers.py runs; Sijoitus numbers unchanged. The split paragraphs keep the same numbers and claims.
