VERDICT: PASS
CONTENT-HASH: 08de94ddb6971388

## Blocking
None.

## Polish
1. solutions.md:84 (L3-02) — the subscripts are mixed: "ΔL(Cu) − ΔL(Fe) = (α_Cu − α_Fe) L₀ ΔT". It does not match ΔL(Cu) on the same line or α(teräs) at :90. — Write "(α(Cu) − α(Fe)) L₀ ΔT".
2. lesson.md:32 — the table still lists glass as "9", while L1-05 and its solution now use 9,0 · 10⁻⁶ 1/K. — Optionally write "9,0" there and in the sim's material menu.

## Checked
- Lint: 0 errors, 0 warnings. check_latex: 6 fragments OK. `build.py fy3-8` built, and `check_layout.py fy3-8` is OK at 360 px with the two-row `aligned` worked example.
- Worked example (lesson.md:60–67): ΔT = 30 °C − (−30 °C) = 60 K. 12·10⁻⁶ · 120 · 60 = 0,0864 m ≈ 86 mm and 0,072 % ≈ 0,07 % are correct. The math uses `{}^\circ`.
- L1-05: 9,0·10⁻⁶ · 1,5 · 25 = 3,375·10⁻⁴ m ≈ 0,34 mm. The 2 sf now match the data in exercises.json:38, solutions.md:34 and :37, and answers.py:7.
- L1-03 (new): 17·10⁻⁶ · 500,0 mm · 100 K = 0,85 mm (2 sf). One end is fixed, so the dial-gauge change equals ΔL. L = 500,85 ≈ 500,9 mm, and 0,17 % is correct.
- L1-01, L1-02 (ΔT = −45 K, ΔL = −51,75 mm ≈ −52 mm, sign kept), L1-04 (0,84 l, 0,42 % < 1 %): correct.
- L2-01 (52,08 m), L2-02 (3,024 cm³, 0,15 %), L2-04 (2,3·10⁻⁵ 1/K, steel 1,08 mm ≈ 1,1 mm): the rearrangements and conversions are correct, and rounding happens only at the end.
- L2-03: the new ΔL/2 argument is correct. Each gap is closed from both sides by ΔL/2, so it closes at ΔL = gap, which gives ΔT = 24 K and T = 36 °C.
- L3-01 (Δd = 0,09 mm, which gives 100 K and 120 °C), L3-02 (0,068 − 0,048 = 0,020 mm = 20 µm, bending toward the steel) and L3-03 (475 − 18 = 457 ≈ 460 cm³, with a γ ratio of 26,4 > 25) are correct.
- γ ≈ 3α: (1 + αΔT)³ ≈ 1 + 3αΔT for small αΔT, as lesson.md:25 says. Air γ ≈ 1/293 K ≈ 3,4·10⁻³ 1/K.
- SVG (lesson.md:42–55): the rods span 60–460 and 60–530. The labels are centred at 260 and 295, and ΔL runs 460→530 from the dashed end line. No labels overlap. Exit ticket: 17·10⁻⁶ · 25 · 50 = 0,02125 m ≈ 21 mm. Notation (L₀, ΔL, α, γ, V₀, T₀) is consistent.
