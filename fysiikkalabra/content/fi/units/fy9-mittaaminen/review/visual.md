VERDICT: FAIL
CONTENT-HASH: 0ca9f52c9bb8edae
SCOPE: delta: round 2, the fixes of round 1 in s7 (Jousen kalibrointi) and s8 (Pudotettu teräskuula videolla); only changed passages and 360 px layout
Round 2: delta against the version round 1 reviewed (fix round 1).

## Blocking
- [Major] sovella/tasks.json, s7 c, criterion `calculation` (the self-assessment panel under "Näytä mallivastaus ja pisteytys") — the formula block is written with literal backslash-n sequences (`$$\\n\\begin{aligned}\\nx &= ...\\n$$` in the JSON), so KaTeX shows a red error "\nx = 4,5 N / 30,0 N/m …" at 360 px (own render) instead of the three aligned rows — the model calculation of the task is unreadable in the grading panel — use real line breaks as in s2 b / s3 e / s6 c (`$$\n\\begin{aligned}\nx &= ...`), i.e. single backslash-n escapes in JSON, not `\\n`.

## Polish
- [Minor] s7/s8 Sijoitus boxes still end in ";" or "," between chain boxes; same as older tasks, optional.

## Checked
- Round-1 polish items verified fixed in solutions.md and tasks.json: s8 c Vertailu is now two aligned rows with the quantities (`\dfrac{0,54 m/s²}{9,81 m/s²} ≈ 5,5 %`); the time-scale chain is its own block with named rows (1,027; 0,0514 s); s8 b says "ympyröidyt" points; the s8 text no longer reveals the structure; rounding matches the data (30,0 ± 1,2; 10,35 ± 0,15 N/m, m/s²).
- Own headless-Chrome render at 360 px of the s7 and s8 task cards (opened, both figures, parts, skill links, lock note): text, graphs and parts clean, no clipping or overflow. Opened the s7 grading panel a–c: a and b fine, c shows the \n error above. The s8 grading panel and solution c were checked from source (aligned rows, no layout problem expected) because my render cut off at 12000 px.
- Intro text read from tasks.json (eight tasks, two start from a graph): true.

## Scores
illustrations 4 · typography 3 · Finnish 5 · accessibility 4
