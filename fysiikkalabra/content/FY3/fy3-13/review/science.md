VERDICT: PASS
CONTENT-HASH: 3c24eb22be807efc

## Blocking

## Polish
- solutions.md:15 (L1-02 Järkevyys) — The text says "lukujen 105 kPa ja 127 kPa suhde". The slope comes from their difference, not their ratio. — Change it to "erotus 22 kPa 60 asteen välillä".
- solutions.md:47 (L2-01 Järkevyys) — "ero johtuu kolmen numeron lukemista" overstates the cause. ±0,005 bar readings give about ±9 °C, but the result is 17 °C off. — Say that the readings' limited precision allows an error of this size (tens of degrees after extrapolation).
- lesson.md:92 aria-label — Gives −259 °C and −295 °C (exact extremes), while the text and the example give −258,7 °C and −294,8 °C (from the rounded coefficients). Both round correctly. Optional.

## Checked
- Round-1 blockers are fixed. L3-02 now says that N₂ boils at 77 K at normal pressure and condenses at about 67 K at 28 kPa. The rounding sentence in the example now reads "yhden asteen tarkkuuteen".
- All 12 answers were recomputed and match answers.py and exercises.json within tolerance (L1-01 −272,2; L1-02 0,3667; L1-03 5,25; L1-04 13; L1-05 0,893; L2-01 −256,0; L2-02 14,1; L2-03 −270,0; L2-04 18; L3-01 20,3; L3-02 28,19; L3-03 1,86). Each solution's final value equals its answer.
- Extreme lines: a brute-force search over bar-end pairs gives exactly 100,13 + 0,3867θ (−259,0 °C) and 102,33 + 0,3467θ (−295,2 °C), which are the lines the lesson quotes. Δθ₀ is 18,1 (18,07 from the printed rounded values), inside the 0,03 tolerance.
- Least squares gives θ₀ = −276,2 °C. The best line's residuals are all ≤ 0,52 kPa, so the claim in "aineisto" holds.
- Worked example: solved symbolically, then substituted. −276,0 °C, −258,7/−294,8, ±18, and the interval −294…−258 contains −273,15.
- Inquiry: suora −275,8 (mistake −295,9), siirto −276,9 (−306,9; p₀ = 120,0), tarkistus-2 −282,9 (−297,9), virhe 40 − 116/0,367 = −276,1 and the student's −316, kertaus 313/293 = 1,068, exit 0,36 and −282…−258.
- The s₂ candidate (98,9 + 0,42θ) misses the bars at 10, 70, 85 and 100 °C, as the feedback and the aria-label state. s₁ is the steepest line.
- SVG coordinates of figures 1–5 and 7 match the data and the lines. Figure 7 is to scale, as stated. All labels are LaTeX and the figures print cleanly.
- θ₀ = θ₁ − p₁/k now appears as a display formula, and Ydinajatus agrees with the glossary.
- Scope is the FY3 experiment. No lesson ids appear in student text, and solution calculations are LaTeX.
