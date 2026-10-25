VERDICT: FAIL
CONTENT-HASH: 2a04ce37da7c5d3c

## Blocking
1. lesson.md:30-34 — SVG y-axis is not linear: 0 kPa at y=250, 101 kPa at y=160 (0,891 px/kPa), 199 kPa at y=52 (0,995 px/kPa). The 98 kPa rise over 10 m is drawn 108 px tall, more than the 90 px for p₀ = 101 kPa, contradicting lesson.md:12 (98,1 < 101 kPa). — Use one scale (≈1 px/kPa from y=250): p₀ at y=150; line 30 `y1="150"`, line 31 `y1="150" y2="150"`, line 32 first circle `cy="150"`, line 34 `y="157"`. Keep 199 at y=52; the x-scale (44 px/m, 10 m at x=520) is correct.

## Polish
1. lesson.md:40 — after the fix "ilmanpaine p₀" (baseline y=150) would sit on the dashed line; move it below, e.g. `y="178"`.
2. lesson.md:41 — label "p = p₀ + ρgh" (x≈330–470, y≈62–80) is crossed by the graph line; move it under the line, e.g. `x="300" y="128"`.
3. lesson.md:49 — sum uses the rounded 118 kPa; round at the end: `101\,\text{kPa} + 117{,}72\,\text{kPa} \approx 219\,\text{kPa}` (result unchanged).
4. lesson.md:54 — "kaavan p = ρgh" clashes with p = p₀ + ρgh (line 23); write "lauseke ρgh antaa vain ylipaineen".
5. solutions.md:12,36,50,52,58,60 — symbol p_h is never named in lesson.md; name it once at lesson.md:25 or write ρgh in the solutions.

## Checked
- All 12 solutions recomputed step by step; substitutions, rearrangements (h = p/(ρg), ρ = p/(gh), A = G/p, F = pA) and values match answers.py and exercises.json.
- Conversions: 1,5 cm² = 1,5·10⁻⁴ m², 380 cm² = 0,0380 m², 150 cm² = 0,015 m², 0,85 bar = 85 000 Pa, 7,22 kPa = 7220 Pa, MPa/kN prefixes.
- Solutions round only at the end (931 950 Pa, 176,58 kPa, 833,85 N, 39 240 Pa, 19 031,4 Pa shown).
- Example: ρgh = 117 720 Pa, p = 218,72 ≈ 219 kPa ≈ 2,2·p₀, F = 1765,8 N ≈ 1,8 kN ≈ 180 kg weight.
- SVG data: 101 + 9,81·10 = 199,1 → 199 kPa.
- Derivation lesson.md:8 (A cancels to ρgh); slope 9,81 kPa/m (line 25).
- Sanity figures: 9,2 p₀; 40 p₀; 329 kg; 3,92 N; 25 × 56 cm = 0,14 m²; 19,62 kPa.
- exit-ticket q2: 49 kPa, 150 kPa.
- Lint 0/0; hash unchanged start to finish.
