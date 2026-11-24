VERDICT: PASS
CONTENT-HASH: e7ab328442b3a9cb
SCOPE: delta md-paragraphs,numbers,typography from 8612c63198757666 base 5b3ca4f

## Blocking

## Polish
- solutions.md:327-329 (L2-10 d) — the new paragraph break puts "Häviöteho on verrannollinen resistanssiin." in one paragraph and its example "Esimerkiksi kaksi kertaa pidempi johto…" at the start of the next one — keep the example in the same paragraph as the claim (layout only, not physics).

## Checked
- Delta from 8612c63198757666 (commit 5b3ca4f): only the solutions.md Kaava steps and paragraph breaks changed. exercises.json and answers.py did not change.
- Every new Kaava chain starts from the basic law and is simplified symbolically to the form that is substituted: L1-03 $P_1 = P_2 \Rightarrow I_1 = U_2 I_2 / U_1$; L2-01 and L2-03 $P_\text{h} = RI^2 = RP^2/U^2$, $P_\text{h}/P = RP/U^2$; L3-01 the same; L3-02 $R = 0{,}010\,U^2/P$; L3-03 $P_2/P_1 = U_2^2/U_1^2$; L1-07 $P_\text{h,2} = P_\text{h,1}U_1^2/U_2^2$; L2-09 $R = 0{,}030\,U^2/P$; L2-10 $P_\text{h} = RP^2/(U^2\cos^2\varphi)$. Every step is algebraically correct.
- L3-04: the closed form $RP^2t(1/U_\text{A}^2 - 1/U_\text{B}^2)\cdot\text{hinta}$ is correct. Recomputed, it gives $1{,}515 \cdot 10^{6}\,\text{€}$, the same as the step-by-step route.
- Recomputed in one script and compared with answers.py: 5,0 A; 826,4 kW; 0,9917 %; 0,75 %; 4,0 Ω; 3,306; 210 kW; 87,7 %; 1,5149 M€; 6,0 Ω; 13,22 MW and 1,000 MW. All agree.
- The paragraph splits (L2-06, L3-05, L2-08, L2-10 a and d) change no number, sign, unit or claim.
- The model stays the same as in the lesson: two-conductor $P = UI$, three-phase only in L2-10, and $U^2 : R$ is excluded for the right reason.
- The hash was the same at the start and the end.
