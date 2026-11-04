VERDICT: PASS
CONTENT-HASH: e9829a16b1879c5a

## Blocking

## Polish
- lessons/FY8/fy8-10/lesson-answers.py (NUCLIDES, same in sim.js) — still carried from round 1: W-184, Au-197, U-235 and U-238 may be off by up to 2 µu from AME2020. The effect is ≤ 1·10⁻⁵ MeV per nucleon, so no displayed number changes. — check against the AME2020 file when online.

## Checked
- Round-1 blocker 1, lesson.md:186: four-figure constants 1,661e-27 · (2,998e8)² / 1,602e-19 give 931,90 MeV, now stated as 931,9. "neljättä numeroa" is right (931,5 vs 931,9). Six figures give 1,49241e-10 J, 9,3149e8 eV and 931,49 MeV.
- Round-1 blocker 2, lesson.md:284: β⁻ with atomic masses now says the electron is not added separately, and the reason is right (the daughter atom has one more electron). β⁺ is not claimed.
- Round-1 blocker 3, inquiry.json:373/376: U-238 alpha decay 0,004583/238,050787 = 1,93·10⁻⁵. U-235 fission 200 MeV / (236,05 u · 931,5) = 9,1·10⁻⁴. Against carbon burning 9,95·10⁻¹¹ these are 1,9·10⁵ and 9·10⁶ times larger, so "satojatuhansia tai miljoonia" is right. The model answer and the criterion agree. The 0,8 % at lesson.md Ydinajatus is now named a binding mass defect (He 0,76 %, U-238 0,81 %).
- Δm(He-4) 0,030377 u, E_B 28,296 MeV, 7,074 MeV per nucleon. U-238 E_B 1801,7 MeV, Fe-56 492,26 MeV, Ni-62 8,795 MeV.
- U-238 α Q 4,269 MeV. Po-210 Q 5,408 MeV, and the mistakes 3734 and −5,408 are right. Etsi virhe gives 92,16 MeV.
- tarkistus-2: exactly one option is correct. A≈30 is about 8,5 MeV (Si-28 8,45), and A≈120 is 8,50 (Sn-120).
- Exit ticket: 7,85 and 8,55 MeV per nucleon. The exit ticket and the summary agree with the theory.
- lesson-answers.py adds u238-alpha-rel and fission-rel. Both are recomputed and right.
- No new error found in the changed text.
