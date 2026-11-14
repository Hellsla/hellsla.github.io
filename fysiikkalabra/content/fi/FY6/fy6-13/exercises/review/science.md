VERDICT: PASS
CONTENT-HASH: 33d51071fa114751
SCOPE: delta added-exercise from 6f38db9cc5bb5b1e base 8f23aa7ae3bd

## Blocking

## Polish
- exercises.json (fy6-13-L2-08) — "toisen kondensaattorin" refers to L1-05's capacitor, but the two tasks sit apart and are not linked. A reader of this task alone does not know what the "other" capacitor is. "Erään kondensaattorin" removes the dangling reference; the physics is unaffected.
- solutions.md (fy6-13-L1-10, Vastaus) — the reason "kaksi merkitsevää numeroa kuten paksuudessa" is right, but the area 250 cm² has three significant figures. Name the limiting data (d = 0,10 mm and ε_r = 2,3) so the reason is exact.

## Checked
- Hash 33d51071fa114751 at start and end; I judged only L1-10 and L2-08 (delta added-exercise).
- L1-10: C = ε₀ε_r A/d. The film fills the gap, and d = 0,10 mm is far smaller than the side of a 250 cm² plate (about 16 cm), so the brief's conditions for the formula hold.
- L1-10 recomputed: 8,854·10⁻¹² · 2,3 · 0,025 : 1,0·10⁻⁴ = 5,09 nF, which equals answers.py. Polyethylene ε_r ≈ 2,3 matches the MAFY value; with 2,25 the result is 4,98 nF, which the 5 % tolerance accepts.
- L1-10 conversions: cm² → m² (·10⁻⁴) and mm → m are right.
- L2-08: figures.py draws a line from (0; 0) to (120 µC; 8 V), both on grid lines, and the alt text gives the same point. Neither states C or W.
- L2-08 recomputed: C = 120 µC : 8 V = 15 µF and W = ½CU² = ½ · 15 µF · (7,0 V)² = 367,5 µJ, which equals answers.py. The tolerance of 2 % fits the answer to two significant figures.
- L2-08 physics: the (Q, U) line through the origin means C is constant, as the brief teaches. The energy follows from ½CU², and the check by ½QU gives the same result. 7,0 V lies inside the drawn range, so no extrapolation is needed.
- Both solutions are complete: the formula comes before the numbers, the conversions are shown, the rounding is stated (with the precision caveat above), and each has a real check (air capacitor × ε_r; ½QU < QU).
- Scope: both tasks use only the brief's formulas (capacitance, the plate capacitor, energy), all within FY6's central content *kondensaattori ja kondensaattorin energia*.
