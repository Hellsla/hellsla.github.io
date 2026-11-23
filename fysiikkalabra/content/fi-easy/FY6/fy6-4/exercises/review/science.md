VERDICT: PASS
CONTENT-HASH: fbfd66f2dc582710
SCOPE: delta caption-label,md-paragraphs,numbers,reflow,teacher-figure,typography from edc1028be1632df7 base b5600a63ddae

## Blocking
- none

## Polish
- solutions.md:233 L2-09 — the row "$U = RI \Rightarrow R = \dots$" jumps over $\tfrac{U}{R} = U\cdot\tfrac{R_1+R_2}{R_1R_2}$. One more row would show where $R$ comes from.
- solutions.md:191 L3-05 — "$R_\text{sarja} = R_a + R_b$" opens without the step $U = R_a I + R_b I$ that L2-01 shows. Use the same row form as L2-01.

## Checked
- The Kaava steps now open with the lesson's own principle rows, $I = I_1 + I_2$ and $U = U_1 + U_2$. In mid-review they started with an unsigned $\Sigma I = 0$ and $\Sigma U = 0$; that version was edited while I reviewed it, and I re-checked the current file. No $\Sigma$ is left, and the notation matches the brief and the next chapter.
- I recomputed all 16 changed solutions in one script from the task data: 24 Ω, 110 Ω, 4,787 mA, 35 Ω, 20 Ω, 1,32 kΩ, 50 mA, 4, 150/100 Ω, 60 Ω, 1013 Ω / 102,1 Ω, 198 Ω, 36 mA, 1,32 %, 500 mA. All agree, and no Sijoitus number changed.
- Every derivation row is algebraically right: the quadratic in L3-03, $I_3 = R_{23}U : (R_3(R_1+R_{23}))$ in L3-01 and L3-04, and the $\tfrac{1}{R_x}$ rearrangements.
- Symbolic before numeric in every changed solution; the last symbolic row is the one substituted.
- The L3-05 and fallback-text paragraph splits change no content.
- The task figures are teacher-approved, and their values match Kuvan lukeminen.
- Content hash checked at start and end. It changed during the review because of the edit above.
