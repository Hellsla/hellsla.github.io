VERDICT: FAIL
CONTENT-HASH: 86c8c78f68c7e9d1

## Blocking
- solutions.md:171-186 (fy6-5-L3-04) — the Kaava now states `I_2 = (U_1 R_3 + U_2 R_1) / D` and `D = R_1 R_3 + R_2 R_3 + R_1 R_2` with no derivation, and the substitution of the old solution (insert I_1 and I_3 into the node equation, solve for I_2) was removed from Sijoitus. A student who could not solve the task cannot see where the closed form comes from, which breaks rule 7 (the asked quantity solved in symbols). Fix: after the five rows, add `(U_1 - R_2 I_2)/R_1 + (U_2 - R_2 I_2)/R_3 = I_2`, multiply by `R_1 R_3`, `U_1 R_3 + U_2 R_1 = I_2 (R_1 R_3 + R_2 R_3 + R_1 R_2)`, then the result.

## Polish
- solutions.md:184 — the Sijoitus sentence runs "…= 630 V Ω Nimittäjä on $$…$$ Siten": missing full stop before Nimittäjä, and display maths inside a sentence; split into rows or sentences.
- solutions.md:185 — the power sentence ends `$$…$$.` with a stray full stop on its own after the display block.
- L2 solutions: the first Kaava row `\Sigma U = 0` followed by `U - U_1 - U_2 = 0` is fine, but the sign convention (rise positive, drop negative) is named only in Periaate; one phrase in the first row's context would help.

## Checked
- Other changed Kaava rows (node law, loop law, potential V_B = V_A - RI, voltage divider, current from U = R_1 I + R_2 I) start from the principle and are correct and followable; Sijoitus now substitutes into the last symbolic form.
- Closed-form divider results (8,0 V, -9,0 V, -3,0 V) recomputed: correct, and the current is kept as a separate sentence.
- Loaded divider task derivation (V_P (R_1 + R_p) = R_p U, then R_k) is complete.
- Split Periaate paragraphs read well, one idea each; no numbers or answers changed in the exercises.
- Two task figures (teacher-approved) unchanged.
