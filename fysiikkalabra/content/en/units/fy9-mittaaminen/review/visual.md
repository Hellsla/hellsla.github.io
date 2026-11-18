VERDICT: FAIL
CONTENT-HASH: 0da2cfcc91630694
SCOPE: delta: round 2, the fixes of round 1 in s7 (Calibrating a spring) and s8 (A steel ball dropped); only changed passages and 360 px layout
Round 2: delta against the version round 1 reviewed (fix round 1).

## Blocking
- [Major] sovella/tasks.json (en), s7 c, criterion `calculation` — the formula is written with literal backslash-n sequences (`$$\\n\\begin{aligned}\\nx &= \\dfrac{4.5...`), so KaTeX shows a red error "\nx = 4.5 N / 30.0 N/m …" in the grading panel instead of three aligned rows — the model calculation is unreadable — use real line breaks (single `\n` escapes in JSON, as in s2 b / s3 e / s6 c). The same defect is in the fi and fi-easy files.

## Polish
- [Minor] s7/s8 Substitution boxes end in ";" or ","; same as older tasks, optional.

## Checked
- Round-1 polish items verified in the English solutions.md and tasks.json: s8 c Comparison now has the quantities in both rows (`\dfrac{0.54 m/s²}{9.81 m/s²} ≈ 5.5 %`); the time-scale chain is a separate block with named rows; s8 b says "circled points"; results rounded to the data (30.0 ± 1.2; 10.35 ± 0.15); decimal point and units language-neutral; English reads naturally and matches the Finnish numbers.
- Own headless-Chrome render at 360 px of s7 and s8 (English): cards, figures, parts, skill links clean, no clipping or overflow. Opened the s7 grading panel (shared structure with the Finnish render), where the `\n` error appears; the s8 panel and solution c checked from source.
- Intro read from tasks.json: true.

## Scores
illustrations 4 · typography 3 · Finnish (English text) 5 · accessibility 4
