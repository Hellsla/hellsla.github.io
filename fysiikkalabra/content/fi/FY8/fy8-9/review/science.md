VERDICT: FAIL
CONTENT-HASH: 0aa98697a3746896

## Blocking
- inquiry.json:272 (johtopaatos.model) — A: `$10^15$` renders as 10¹5, so the model answer shows a wrong number of nuclei — write `$10^{15}$`.

## Polish
- lesson.md:438 (and 443) — I-131 8,02 d is attributed to NuDat 3 rounded to three figures, but ENSDF/NuDat gives 8,0252(6) d → 8,03 d; 8,02 d matches DDEP/LNHB (8,0233 d). Either cite DDEP for this row or use 8,03 d (and rerun the worked example, tarkistus-1, exercises). Physically negligible (0,06 %).
- lesson.md:636 — intermediate `97{,}65` MBq is the rounded value of 97,648; then "noin 97,6" looks like rounding 97,65 down. Write `97{,}648` (or 97,65 → 97,6 explained).
- lessons/FY8/fy8-9/lesson-answers.py:1559–1560, 1554 — stale comments (ex-factor 0,17750 / ex-A 97,62; computed 0,17754 / 97,648; hook-tc is 370,4, not 370) and a comment about a "1,0e15 Tc-99m activity example in Kaava" that the lesson does not have — update the comments.

## Checked
- Half-lives against ENSDF: Ba-137m 2,552(1) min, Pa-234m 1,159(11) min, Tc-99m 6,007 h, F-18 109,7 min, Rn-222 3,8235 d, Cs-137 30,08 a, C-14 5700 a, U-238 4,468e9 a: all correct as rounded.
- Sim model values recomputed independently in Node (mulberry32): koe 1 1600/792/399/208, koe 2 7/12/13/7/10, koe 3 792/800/783/815/805 match every option, feedback and model answer.
- sim.js: τ = −T½/ln2·ln u gives constant hazard λ; N counts τ > t; dashed curve is the law; limits (no detector, background, daughter stable) stated.
- Pa-234m fit from the task's table (own least squares): A 376,6, C 0,010127 1/s, B 5,54 → T½ 68,45 s → 68,4 s; mistakes 1/C 98,7 s, no-B 71,8 s, literature 69,5 s all right and distinct within 1 % tolerance.
- Ba-137m figure: C 0,004564 → 151,9 s, −0,8 % from 153,1 s.
- Worked example 2,4938 half-lives, factor 0,17754, 97,6 MBq; bracket check right.
- Etsi virhe: 4,33e10 vs 6,24e10, 31 % too small; distractor feedback right.
- tarkistus-1 (memoryless ½), tarkistus-2 (720 kBq, 5,0 h; figure checked), tarkistus-3 (ratio ≈ 44 000, 1460 half-lives, Cs 97,7 % left), exit ticket, kertaus (I-131 → Xe-131).
- λ = ln2/T½, A = λN, e-form, fitting model and the meaning of A, B, C stated correctly; "käytännössä" covers environment independence.
