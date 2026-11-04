VERDICT: FAIL
CONTENT-HASH: 0033aa9bfd64001a

## Blocking
- exercises.json L3-04 data, solutions.md:185, answers.py:54 — A: the table is presented as Z for "hiilidioksidille tässä lämpötilassa" (300 K). Real CO₂ at 300 K has Z ≈ 0,975 / 0,95 / 0,90 / 0,78 at 5 / 10 / 20 / 40 bar (B ≈ −122 cm³/mol); the table's 0,96 / 0,92 / 0,84 / 0,65 overstate the non-ideality by up to 17 %. This moves the asked conclusion of c), the 5 % validity limit, from about 10 bar to "noin 6 bar", and the answer from 6,5 to 6,8 mol. — Fix: use Z = 0,99; 0,975; 0,95; 0,90; 0,78. Then Z(15 bar) = 0,925 and n = 6,5 mol (answer 6.5); the limit in c) is about 10 bar. Update answers.py (`Z_15 = (0.95 + 0.90) / 2`) and the solution's c) and Järkevyys. Or keep the numbers and make the gas fictional ("eräs kaasu").

## Polish
- Scope of L3-04: the lesson does not teach Z. The task defines it, needs only pV = nRT, and the bank plan asks for it, so I count it as an unfamiliar level 3 context, not out of scope.
- solutions.md:142 (L1-07) gives 2,31 l, but the same line says "varmin … 2,3 l". Choose 2,3 l.
- solutions.md:196 (L3-05) — "lämpötilojen pyöristys rajoittaa" is weak, because −50,0 °C has three digits. A better reason: the ICAO values are rounded and the gas is not exactly at the ambient temperature.
- L2-05: 220 kPa total (≈ 1,2 bar overpressure) is a soft tyre; about 320 kPa is typical.

## Checked
- All 17 numeric answers recomputed in one script; they agree with answers.py (2,314 l; 5,33 % with 236,6 kPa without a leak; 4,95 mmol; 6,834 mol as written; 7,379 m³ and 15,69 m³).
- L2-06: least-squares slope 0,408 ± 0,010 cm³/K with intercept 1,1 ± 3,3 cm³, consistent with the origin; the points read in the solution lie on the fit; "±0,1 mmol" is fair.
- L2-07: pV is 244 (A) and 304 (B) kPa·l on every row; exactly one correct option, and the feedback is right.
- L1-06 and L1-08: one correct option each; the 1,2·10⁻⁴ → 0,12 mol arithmetic is right.
- L3-05: the ICAO values are right and the assumptions are stated.
- Kelvins, total pressures and SI units are used throughout.
- Hash unchanged at the start and the end.
