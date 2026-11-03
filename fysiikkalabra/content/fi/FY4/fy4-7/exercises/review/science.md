VERDICT: PASS
CONTENT-HASH: 6fe85d743b5c7179

## Blocking

## Polish
- solutions.md fy4-7-L1-05 — the stated answer −2,6 · 10² J is 1,9 % from −255 J, just inside the 2 % tolerance; fine now, but any data change would push a correctly rounded answer out — keep in mind (or widen tolerance to 0.03).
- solutions.md fy4-7-L1-01 — "kaksi merkitsevää numeroa kuten massassa 1200 kg": 1200 is ambiguous and 20,0 m/s has three; "240 kJ" is fine either way — optionally say the mass limits to 2–3 figures.
- solutions.md fy4-7-L3-03 — a roller skater's wheels also carry rotational energy; ignoring it is a fair simplification (C), no change needed.

## Checked
- All 12 answers recomputed independently (own formulas, km/h → m/s, g → kg, cos in degrees): every one agrees with exercises.json to < 1e-15 relative.
- Shown rounded answers (8,5 kJ; −2,6·10² J; 4,2·10² kJ; 54 m/s) stay inside the 2 % tolerance; units in exercises.json match the questions.
- Models: E_k = ½mv², E_p = mgh near Earth's surface with stated zero level, E_mek = E_k + E_p — the brief's notation and conditions; nothing beyond FY4 scope.
- L1-05 negative E_p below the zero level, consistent with the lesson.
- L2-03 / L1-04: only ΔE_p is zero-level independent; check 22,4 − 13,5 = 8,8 J = mg·0,75 m correct.
- L3-01: v₁ = v₂√(m₂/m₁) solved symbolically; unit-ratio argument valid; 741 kJ cross-check correct.
- L3-02: h = L(1 − cos α) = 0,281 m geometry correct; 90° limit check correct.
- L3-03: no pushing stated in task; loss = ½mv² − mgh = 214 J; 16 % height/energy check consistent (both 15,9 %); friction → internal energy per guardrails.
- Every solution symbolic before substitution, conversions right, reasonableness checks are real checks.
- Hash identical at start and end.
