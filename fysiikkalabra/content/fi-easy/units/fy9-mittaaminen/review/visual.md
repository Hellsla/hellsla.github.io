VERDICT: FAIL
CONTENT-HASH: ce624321f2f924f1
SCOPE: delta: round 2, the fixes of round 1 in s7 (Jousen kalibrointi) and s8 (Pudotettu teräskuula videolla); only changed passages and 360 px layout
Round 2: delta against the version round 1 reviewed (fix round 1).

## Blocking
- [Major] sovella/tasks.json (fi-easy), s7 c, criterion `calculation` — the formula is written with literal backslash-n sequences (`$$\\n\\begin{aligned}\\nx &= \\dfrac{4{,}5...`), so KaTeX shows a red error "\nx = 4,5 N / 30,0 N/m …" in the grading panel instead of three aligned rows — the model calculation is unreadable — use real line breaks (single `\n` in JSON, as in s2 b / s3 e / s6 c). Same defect in the fi and en files.

## Polish
- [Minor] s7/s8 Sijoitus boxes end in ";" or ","; same as older tasks, optional.

## Checked
- Round-1 polish items verified in fi-easy solutions.md and tasks.json: s8 c Vertailu has the quantities in both rows; the time-scale chain is its own block with named rows; s8 b says "ympyröidyt" points; results rounded to the data (30,0 ± 1,2; 10,35 ± 0,15); short sentences, one idea each, same numbers as the Finnish text ("Ero on 0,54 : 0,147 ≈ 3,7-kertainen").
- Own headless-Chrome render at 360 px of s7 and s8 (fi-easy): cards, figures, parts clean, no clipping or overflow. The s7 grading panel is shared with the Finnish render, where the `\n` error appears; the s8 panel checked from source.
- Intro read from tasks.json (short sentences, eight tasks, two with a graph): true.

## Scores
illustrations 4 · typography 3 · Finnish 5 · accessibility 4
