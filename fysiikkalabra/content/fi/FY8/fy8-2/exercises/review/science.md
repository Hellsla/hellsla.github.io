VERDICT: FAIL
CONTENT-HASH: 3234dc70c5ccf41b

## Blocking
- **A (7 assessment correctness, 6 consistency): fy8-2-L3-04, part b) and the solution's Sijoitus.** The five lines (3,90; 2,80; 2,40; 1,50; 1,30 eV) fit two level schemes, not one. The solution's is 1,10/2,40/3,90 eV; its mirror 1,50/2,80/3,90 eV (missing line E3 − E2 = 1,10 eV) fits equally well. Both give the same sixth line, 1127 nm, so the answer box is right. But part b) asks the student to "päättele viritystilojen energiat", and the solution presents its diagram as the only deduction ("Pari 2,40 + 1,50 on E2 ja E3 − E2 … joten se on puuttuva viiva E1"). A student who draws the equally valid mirror diagram is marked wrong. **Fix (either):** (1) add one datum that breaks the symmetry to the task text, for example "Kylmä kaasu absorboi viivat 318 nm ja 517 nm" or "viiva D (827 nm) päättyy viritystilalle 2,40 eV"; or (2) keep the data and state in the solution (and in part b) that two mirror-image diagrams fit, show both, and add that the sixth line is 1,10 eV in either case.

## Polish
- L1-06 correct option and Periaate: "kylmän kaasun" → "viileämmän kaasun". Dark lines need the gas to be cooler than the source behind it, not cold.
- L2-06 a): the Ca line 393,4 nm is from ionised calcium (Ca II). Optionally add "(kalsiumioni)".

## Checked
- Recomputed every new answer in one script with my own formulas: L2-05 2,2698 eV (Hg lines within 0,2 nm) ✓; L2-06 hc/λ = 2,551 eV → −0,849 eV = n = 4 ✓, and lines A, B, C, D, F, G identified with E (527,1 nm) left unidentified ✓; L2-07 least-squares λ = 12,01 x + 299,6 → 496,6 nm, residuals ≤ 0,76 nm ✓; L3-04 brute-force search of all level triples, both schemes give 1,10 eV → 1127 nm ✓; L3-05 heat shares A 18,9 %, B 22,1 %, C 15,1 % → B 22,1 % ✓, and the energies agree with the solution ✓.
- MC L1-06 and L1-08: exactly one correct option, and each distractor is wrong with correct feedback ✓.
- The data are labelled esimerkkiaineisto, scope is FY8, and every new task has a complete solution. The levels fit and the tasks follow the plan in docs/exercise-bank/FY8.md.
- Spot-checked the render at 1280 px (L3-04 table and solution): clean.
- Content hash 3234dc70c5ccf41b is the same at the start and the end.
