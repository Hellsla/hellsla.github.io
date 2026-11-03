VERDICT: PASS
CONTENT-HASH: 7e839286024975e7

## Blocking

## Polish
- exercises.json (fy6-6-L1-05), figure ex-pi and the answers.py comment — this is still open from round 1. The four points are called "mittauspisteet", yet they lie exactly on $P = 5I^2$. Call them model values, or add the guardrail sentence "Todellisissa mittaussarjoissa mittauspisteet eivät yleensä sijaitse täsmälleen samalla käyrällä …" to the solution.

## Checked
- Round-1 Blocking (L2-04) is fixed. The task now gives "lämpötila on aluksi 20 °C" and "eikä vettä höyrysty", so the model's assumptions are in the task, and the solution's "eikä olomuoto muutu" matches them. The end temperature is 20 + 17,9 ≈ 38 °C, far below boiling, so the assumption is consistent.
- Round-1 Polish is applied: L2-03 adds "vaikka koko jännite olisi vastuksen yli", and L1-03 names 230 V as three significant figures.
- All twelve answers were recomputed with independent formulas: 12 W, 1,88 W, 1,996 kW, 64,8 kJ, 5,0 Ω, 7,83 A, 3,2 W, 15,8 V, 17,9 K, 20,4 W, 287,5 Ω, 12 Ω. They agree with answers.py and exercises.json.
- The assumptions are stated where they are used: constant lamp resistance (L3-01), resistance "kun sarja palaa" (L3-02), an ideal source and wires (L2-02, L3-03), no losses (L2-04).
- Every solution is symbolic first, its conversions are right, its rounding follows the limiting datum, and its reasonableness checks are real cross-checks.
- The energy wording follows the FY6 rule: no "lämmöksi"; "sisäenergiaksi", "siirtyy ympäristöön".
