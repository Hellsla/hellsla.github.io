VERDICT: PASS
CONTENT-HASH: 4720559b0d9eefa0

## Blocking

## Polish
- lesson.md (half-life table, Esimerkki) — I-131 8,02 d is attributed to NuDat 3 rounded to three figures, but ENSDF/NuDat gives 8,0252 d → 8,03 d; 8,02 d matches DDEP (8,0233 d). Cite DDEP or use 8,03 d. Physically negligible (0,06 %).
- lesson.md (Esimerkki, Sijoitus) — `97{,}65` MBq then "noin 97,6" looks like rounding 97,65 down; write 97,648.
- lessons/FY8/fy8-9/lesson-answers.py — stale comments: ex-factor 0,17750 / ex-A 97,62 (computed 0,17754 / 97,648), hook-tc "370" (370,4), and a "1,0e15 Tc-99m activity example in Kaava" the lesson does not have.

## Checked
- Round 1 blocking fixed: johtopaatos model answer now `$10^{15}$`; no other `10^` without braces in the packet.
- Sim model values rerun from the seeded generator: koe 1 1600/792/399/208, koe 2 7/12/13/7/10, koe 3 792/800/783/815/805 — match every option, feedback and model answer.
- Experiments lock N0, T, sarja (koe 1) and N0, T, t (koe 2–3), varying only the stated parameter; simState gives N and frac.
- Pa-234m fit recomputed from the table (own grid least squares): A 376,6, C 0,010127 1/s, B 5,54 → T½ 68,45 s; mistakes 1/C 98,7 s, no-B 71,8 s, C 0,0101, literature 69,5 s distinct within 1 %.
- Ba-137m figure: C 0,004564 → 151,9 s, −0,8 %.
- Worked example 2,4938 half-lives, factor 0,17754, 97,6 MBq; bracket check 138/69 MBq right.
- Etsi virhe 4,33e10 vs 6,24e10 (31 % too small); Tc-99m λ 3,20e-5 1/s, "32 per million per second".
- tarkistus-1 memoryless ½; tarkistus-2 720 kBq, 5,0 h, 180 kBq at 10 h; tarkistus-3 ratio ≈ 43 900, ≈ 1460 half-lives, Cs 97,7 % left; exit ticket 1/8.
- λ = ln2/T½, A = λN, e-form, fitting model and meaning of A, B, C correct; law stated as large-sample behaviour; "käytännössä" covers environment independence.
