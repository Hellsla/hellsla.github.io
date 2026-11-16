VERDICT: PASS
CONTENT-HASH: 4aab64de290ab785

## Blocking

## Polish
- lessons/FY7/fy7-13/answers.py:854 — the comment says λ = 629,6 nm, but the line computes 629,84 nm (and the figure draws 629,7 nm) — correct the comment to 629,8 nm.
- exercises.json fy7-13-L2-07, second option's feedback — "The error is not divided among several maxima" uses *error* where the task and the other feedback speak of *uncertainty* (guardrail: keep virhe and epävarmuus apart) — say "the reading uncertainty is not divided…".
- solutions.md fy7-13-L2-07 Principle — the relative uncertainty of λ is in fact cos²θ · Δx : x (≤ Δx : x), so "approximately Δx : x" holds at small angles; the conclusion is right either way. Optional: "at small angles approximately".

## Checked
- One script recomputed all 21 numeric answers from the task text with my own formulas (d sin θ = kλ, tan θ = x : L, d = 1 mm : N); they agree with answers.py and exercises.json to 4 decimals. Tolerances hold the rounded answers (L3-04's 6.3·10² nm is 0.8 % from 625 nm, inside 2 %).
- L2-05 (red laser): sin θₖ values, the least-squares slope through the origin 0.06337 → 634 nm, and per-point λ 625–638 nm are consistent and realistic for a red laser.
- L2-07: exactly one correct option. Every distractor really is wrong, and its feedback gives the right reason (x ∝ L, sparser grating → smaller x, intensity does not move the maxima).
- L3-04: the table follows I = cos²(πx / 5 mm) with small scatter. x₁ = 5.0 mm → 625 nm. The two significant figures (6.3·10² nm) are justified by x₁. x₂ = 10.0 mm matches the table. The comparison with the grating (same positions, narrower and brighter maxima) is right. The imaginary 4 lines/mm grating is flagged.
- L2-08: all five options and their feedback recomputed (13.03 → 19.88 cm, factor 1.53). The distractor factors 6, 3, ½ and ⅙ follow from the misconceptions their feedback names.
- Figures: setup-q spots at 31.2 and 69.98 cm (L = 1.20 m, 400 lines/mm), so reading x₂ = 70.0 cm gives 630 nm. In spectrum-q the edges are at 10.05 and 17.77 cm for 250 lines/mm. The descriptions give the same values and do not give away the answer.
- L3-05 DVD: d per row 0.7389–0.7363 µm, mean 0.7374 µm, −0.36 % from 0.74 µm. The second order has sin = 1.44 (impossible). The zeroth order goes back through the hole: the reasoning is right.
- L1-08 and L2-01: the strict k < d/λ condition is right. L3-01 overlap argument (1200 < 1400 nm) is right. L3-02: only two orders on each side (d/λ = 2.46).
- L1-09: the MAFY He yellow line is 587.56 nm, giving 20.6°.
- Scope: grating, double slit, reflection grating. This is inside FY7 "valon interferenssi ja diffraktio" and the slot's experiment. The notation matches the glossary (hilavakio d, θ from the central maximum).
