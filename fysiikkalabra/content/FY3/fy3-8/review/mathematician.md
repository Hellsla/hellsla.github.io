VERDICT: FAIL
CONTENT-HASH: 798aafe0d452e47a

## Blocking
1. exercises.json:38 (L1-05) — α = 9 · 10⁻⁶ 1/K has 1 sf. A student who rounds by the house rule answers 0,3 mm, which is 11 % from 0.34 (tolerance 0.02), and is rejected. The lint misses this because it never extracts "· 10⁻⁶ 1/K" coefficients. — Write "α = 9,0 · 10⁻⁶ 1/K" here and in solutions.md:34 and :37. Optionally write "9,0" at lesson.md:32 too. The answer does not change.

## Polish
1. exercises.json:25 (L1-03) — tolerance 0.001 = ±0,60 mm, which is 60 % of ΔL. The answer 600,0 mm (expansion forgotten) is rejected, but it falls within 3× the limit, so the page says "Lähellä. Tarkista pyöristys", which is misleading. — Use 0.0003 (±0,18 mm). It still accepts 601,0, 601,02 and 601,1.
2. scripts/lint_lesson.py:127 — coefficients written as "N · 10⁻ⁿ 1/K" are never checked for sf. Add a rule and a NOTES line.
3. lesson.md:60 — `30\,°\text{C}` puts a raw ° in math mode. NOTES §1.5 says `^\circ`.
4. lesson.md:48 — the label "L₀ + ΔL" is at x = 260, but the warm rod's centre is x = 295.

## Checked
- Worked example: 12·10⁻⁶ · 120 · 60 = 0,0864 m ≈ 86 mm. "lähes 9 cm" and "0,07 %" are correct.
- Rod SVG: 400 → 470 px. The dashed line at x = 460 is the cold rod's end and ΔL runs 460→530. The figure is marked "liioiteltu", and no proportion is claimed.
- Tables: α (12, 23, 17, 9, 3,3) and γ (0,21, 1,1, 0,95, 3,4; air ≈ 1/293 K) are plausible at 20 °C. γ ≈ 3α is correct.
- All 12 solutions: rearrangements, conversions and end-only rounding are correct. answers.py matches.
- Sanity numbers 0,17 %, 0,42 %, 0,15 %, 1,08 mm, γ ratio 26,4 and 457 cm³ are correct.
- L1-02: the check uses |ans|, so −52 passes and 52 fails.
- L2-04 unit "· 10⁻⁶ 1/K" renders "[23] · 10⁻⁶ 1/K", which is correct. Typing 0,000023 gets the magnitude hint.
- L3-01: 0,09 mm gives 100 K and 120 °C. L3-02: 20 µm, and the strip bends toward the steel.
- Exit ticket: 0,02125 m ≈ 21 mm.
- Notation (L₀, ΔL, α, γ, V₀, T₀) is consistent across files.
