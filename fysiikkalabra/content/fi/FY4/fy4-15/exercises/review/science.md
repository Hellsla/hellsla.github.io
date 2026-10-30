VERDICT: PASS
CONTENT-HASH: 88089ff793c3d21f

## Blocking

## Polish
- exercises.json:82 (L3-01) — "Tuulen keskinopeus": the v³ ratio is exact for a steady wind, and for means only when the wind distribution keeps its shape. Write "tuulen nopeus" (as in L3-02).
- answers.py:16 — the comment says 96,56 m³/s, but the value is 96,53. Correct the comment.
- exercises.json (L1-02) — the same 1000 kg / 24 m / 235 kJ computation is done in the theory text (Teho kertoo energiaa sekunnissa), so the exercise repeats it. Change the data (pedagogy's call).

## Checked
- Recomputed all 12 answers with my own formulas. They agree with answers.py and exercises.json, and each rounded answer is inside the tolerance.
- Hydro tasks use P = ηρQgh with ρ and g stated in the solutions. The l → m³ conversion (L2-03) and MW·h → MWh (L1-05, L2-04) are right.
- L2-02 uses the real V82 point 758 kW at 8 m/s (verified against the NREL file). η = 44,9 % with the stated ρ = 1,25 is below Betz.
- L3-01 and L3-02 state their conditions (same η and rotor or wind, below rated power). The ratios (1,5)³ and (162/82)² are correct.
- L3-03: h = v²/(2g) = 5,10 m. Units and reasonableness are right.
- Every solution has all seven parts, solves in symbols first and justifies its rounding by the limiting datum. The reasonableness checks are real estimates.
