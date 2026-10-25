VERDICT: PASS
CONTENT-HASH: 6206733164082a20

## Blocking
(none)

## Polish
1. solutions.md:69 — L2-04 writes the overpressure as `p = 0,85 bar` although lesson.md:27 now reserves p for total pressure and names the overpressure Δp = p − p₀; the result is right. — Write `Δp = 0,85 bar = …` and `F = Δp · A`, as L3-02 already does (solutions.md:84).
2. solutions.md:53 — `= 35,68 m` is a rounded value (35,677…). — Use `≈ 35,68 m`.
3. solutions.md:61 — `= 919,98 kg/m³` is rounded (919,979…). — Use `≈ 919,98 kg/m³`.
4. solutions.md:77 — `A = 833,85 N / 6000 Pa = 0,139 m²` is rounded (0,138975). — Use `≈ 0,139 m²`.
5. lesson.md:37 / lesson.md:34 — on the 100 px / 101 kPa scale, 199 kPa sits at y ≈ 53, not 52 (1 px, invisible). — Optional: end the line and circle at y = 53 and the label at y = 60 for an exact scale.

## Checked
- Round-1 blocking item fixed: SVG p axis is one linear scale (0 kPa at y = 250, 101 kPa at y = 150, 199 kPa at y = 52; ≈ 0,99 px/kPa), x scale 44 px/m with 10 m at x = 520; line slope 98 px per 98,1 kPa matches ρg.
- SVG labels: "p = p₀ + ρgh" (x 310–440, baseline 132) lies between the graph line (y ≈ 99–70 there) and the dashed p₀ line; "ilmanpaine p₀" below the dashed line; tick labels aligned with their values.
- Derivation lesson.md:8: V = Ah, m = ρV, G = ρAhg, G/A = ρgh; Δp = p − p₀ (line 27) consistent with all Δp uses in solutions.md.
- Example lesson.md:49–53: ρgh = 117 720 Pa = 117,72 kPa; p = 218,72 ≈ 219 kPa ≈ 2,2·p₀; F = ρgh·A = 1765,8 N ≈ 1,8 kN ≈ 180 kg weight; rounding only at the end; kPa·m² = kN.
- Dam paragraph lesson.md:14: 1000·9,81·30 = 294 300 Pa ≈ 290 kPa ≈ 290 kN per m².
- All 12 solutions recomputed step by step; rearrangements h = Δp/(ρg), ρ = Δp/(gh), A = G/p_max, F = pA, ΔF = Δp·A correct; values match answers.py output.
- Conversions: 1,5 cm² = 1,5·10⁻⁴ m², 380 cm² = 0,0380 m², 150 cm² = 0,015 m², 0,85 bar = 85 000 Pa, 7,22 kPa = 7220 Pa.
- Sanity figures: 9,2·p₀; 1,75 and 2,72·p₀; 2,97·p₀; 40·p₀; 329 kg; 3,9 N; 25 × 56 cm = 0,14 m²; 19,62 kPa.
- exit-ticket q2: 49 050 Pa ≈ 49 kPa; 150,05 ≈ 150 kPa.
- Lint 0 errors/0 warnings; hash unchanged from start to finish.
