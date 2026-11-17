VERDICT: PASS
CONTENT-HASH: ffb46e541b24ba0a
SCOPE: delta added-exercise from 2f696bac3aa33109 base 5b3ca4f81c77

## Blocking

## Polish
- lessons/FY8/fy8-10/answers.py:49 — the comment "(true values 216,6)" is wrong: the figure's own points give 235 · (8,5046 − 7,591) MeV = 214,7 MeV — write 214,7.
- solutions.md fy8-10-L3-06 Vastaus — the text says the ±15 % tolerance covers "kummankin lukeman ±0,1 MeV virhe", but readings of 8,4 and 7,7 (each within the stated 0,1 MeV) give 164,5 MeV, and the tolerance rejects that. Only about ±0,13 MeV in the difference is covered. Either say "noin ±0,1 MeV erotuksessa" or accept that the worst case falls outside (the typical readings 8,4/7,6 → 188 and 8,6/7,6 → 235 are accepted).

## Checked
- Recomputed in one script, in my own model. L1-09: (m_p + m_n − m_d) · 931,5 MeV = 0,0023882 u · 931,5 MeV = 2,2246 MeV. The MAFY values match docs/mafy-arvot.tsv (VERIFIED). L2-09: 120 · 8,5 MeV = 1020 MeV (Sn-120 point 8,5046 gives 1020,5). L3-06: 235 · (8,5 − 7,6) MeV = 211,5 MeV. All three agree with answers.py.
- The figure has points at A = 120 (Sn), 235 and 238 (U), 28 (Si) and 56 (Fe), at 8,505, 7,591, 7,570, 8,448 and 8,790 MeV. The solutions' readings (8,5; 7,6; 8,4; 8,8) and the grid-fraction descriptions are right. The figure description gives the same values and does not give away the answer.
- Tolerance of L1-09 (2 %) rejects the wrong mass choices: a hydrogen atom for the proton gives 2,736 MeV, the deuterium atom with a nuclear proton 1,713 MeV, and E_B/A used as E_B 1,112 MeV. It accepts 931,494 MeV, the 4-figure constants (931,9 MeV → 2,2255 MeV) and consistent atomic masses (2,2244 MeV, also correct physics).
- Tolerance of L2-09 (5 %) rejects E_B/A as E_B (8,5), the A = 238 value (912 MeV) and reading 8,0 (960 MeV). It accepts readings 8,4 and 8,6.
- Tolerance of L3-06 (15 %) rejects the difference alone (0,9 MeV), a missing ×A, a single fragment (1003 MeV) and fragments minus nuclei of the wrong size (−766 MeV). It accepts 236 nucleons (220 MeV) and the U-238 point (218,6 MeV), both reasonable.
- The fission physics is right. Q = E_B,loppu − E_B,alku holds because the nucleon number is conserved (117 + 118 = 235) and the task states its simplifications. About 200 MeV is the right order of magnitude. The Fe-56 → 2 × A = 28 case is negative (my value −19 MeV, the solution's estimate −22 MeV, same sign and size).
- L2-09 c: the larger total E_B (A = 238) and the more tightly bound nucleus (A = 120) are both right.
- L1-09 principle: MAFY's masses are nuclear masses, so no electron bookkeeping is needed. That is stated correctly and consistent with the lesson's atomic-mass formula.
- Significant figures: L1-09 has 4 (limited by 931,5), L2-09 and L3-06 have 2 (graph readings). All justified.
- All in FY8 scope (binding energy, the E_B/A curve; fission only qualitatively and as an estimate). Notation follows the lesson.
- Hash ffb46e541b24ba0a at the start and the end.
