VERDICT: PASS
CONTENT-HASH: 33b9c3bf1b8baf23
SCOPE: delta numbers,typography,teacher-figure,reflow,caption-label,wording,md-paragraphs from 22633f9efb51607f base a5182aa

## Blocking

## Polish
- solutions.md L3-04 Sijoitus: "= 630 V Ω Nimittäjä on" has no full stop and display maths sits inside the sentence. End it "…$630\,\text{V}\,\Omega$." and start "Nimittäjä on…" afresh.
- solutions.md L3-04 power sentence: drop the stray full stop after the closing `$$`.
- L2 Kaava rows: state the sign convention (rise +, drop −) beside the first row, not only in Periaate.

## Checked
- Diff `git diff a5182aa` over the exercises and lesson-answers: the Kaava blocks now start from the basic law (node law, ΣΔV = 0, U_AB = V_A − V_B, Ohm's law, divider) and end at the asked quantity. Sijoitus substitutes into the last symbolic form.
- L3-04 now derives I_2: R_1R_3 I_2 = R_3(U_1 − R_2 I_2) + R_1(U_2 − R_2 I_2), then D, then I_2 = (U_1R_3 + U_2R_1)/D. The earlier jump (I_2 appearing from nowhere) is closed. Recomputed: 630 V·Ω, D = 2100 Ω², I_2 = 0,30 A, I_1 = 0,20 A, I_3 = 0,10 A, 3,3 W on both sides.
- Kirchhoff notation (ΣΔV = 0, ΣI_tulo = ΣI_lähtö, U_AB = V_A − V_B) matches the lesson.
- L3-05 loaded-divider derivation is complete (R_p, then R_k). Periaate paragraphs are split, one idea each. L2-08 solution is split into short paragraphs.
- Table captions lost "esimerkkiaineisto"; the tasks read the same. Task figures are teacher-approved and unchanged. No exercise numbers or answers changed.
- The lesson-answers.py "kertaus" additions touch no exercise.
