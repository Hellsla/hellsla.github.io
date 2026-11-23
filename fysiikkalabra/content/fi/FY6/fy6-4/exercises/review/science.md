VERDICT: PASS
CONTENT-HASH: 43cd3baad13c0746
SCOPE: delta caption-label,md-paragraphs,numbers,reflow,teacher-figure,typography from b76783ab2894e5cb base b5600a6

## Blocking
- none

## Polish
- content/fi/FY6/fy6-4/exercises/solutions.md:106 — L3-02 still writes $\tfrac{1}{R_\text{rinnan}} = \tfrac{2}{R_1}$ without the row $\tfrac{1}{R_\text{rinnan}} = \tfrac{1}{R_1} + \tfrac{1}{R_1}$. That row would match the series row above it (C, not blocking).
- content/fi/FY6/fy6-4/exercises/solutions.md:147 — L2-05 lists $U = U_1 + U_2 + U_3$ and $I = I_1 + I_2 + I_3$ next to the resistance formulas but does not show the $U = RI$ step that links them. L1-02 shows that step (C).

## Checked
- Hash 43cd3baad13c0746 at the start and at the end.
- My previous blocking item is fixed. No $\Sigma I = 0$ or $\Sigma U = 0$ is left in any Kaava block. Every block now opens with the lesson's own principle rows: $I = I_1 + I_2$, $U = U_1 + U_2$ and $U = R_1 I + R_{23} I$. This matches the brief, and the chapter does not need Kirchhoff's laws.
- I derived every aligned chain again (L1-02, L1-05, L2-01…L2-04, L2-06, L2-07, L1-08, L2-05, L2-09, L3-01…L3-05). Each row follows from the one before it, and the last symbolic form is the one that is substituted.
- The closed forms are right: $I_3 = R_{23}U/(R_3(R_1+R_{23}))$ gives 50 mA, $I_3 = R_{23}U/(R_3R)$ gives 36 mA, and the quadratic gives the roots 150 Ω and 100 Ω.
- One script recomputed all 19 numeric answers with my own formulas: 670, 24, 1,5, 2,7, 110, 4,787, 35, 20, 1,32, 50, 4, 150, 60, 102,1, 198, 40,37, 36, 1,318 and 500. All agree with answers.py and exercises.json, and the tolerances fit.
- L3-05 and L2-08: the paragraph splits only re-cut the text. No number or claim changed.
- The teacher-approved figures task-parallel (9,0 V, 30 Ω ∥ 45 Ω) and task-mixed (12 V, 40 Ω in series with 60 Ω ∥ 120 Ω) match the Kuvan lukeminen rows and give no answer away.
