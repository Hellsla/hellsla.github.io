VERDICT: FAIL
CONTENT-HASH: 520b877d2b66d96d

## Blocking
- [Major] exercises.json 342 (answer of the "negatiivinen taso" task; captures fy5-15-390-I0-05-0.png, fy5-15-1280-I0-05-0.png) — the formula was lifted to a display block in the middle of a sentence that goes on with a semicolon, so the line after the box begins "; keskimääräinen kuulija ei kuule sitä, …" at 390 and at 1280 px — a line that opens with a punctuation mark is a plain typographic error the student sees, and it was not there before the change (the full stop and the comma are drawn inside the formula elsewhere, the semicolon is not) — end the sentence at the formula and start a new one: "…kuulokynnystä pienempi, $$…\,\text{W/m}^2$$. Keskimääräinen kuulija ei kuule sitä, mutta…" (the full stop then goes inside the box), or let the shared punctuation rule take ";" as well.

## Polish
- [Minor] solutions.md 188, 1280 px — "1,0 m → 2,0 m → 4,0 m → 8,0 m | → 16 m," keeps its phone rows on a wide screen, the lone "→ 16 m" looks orphaned (known join_wide matter).
- [Minor] solutions.md 39 — "…noin 8000 m², ja" leaves "ja" alone on a line before the box at 390 px; harmless.

## Checked
- Delta: exercises.json 342; solutions.md 39, 86, 188.
- Own captures from preview/fy5-15.html?ratkaisut=1, details open, 390 (dpr 2) and 1280 px, in /tmp/claude-0/-home-user-hellsla-github-io/ec927bcd-bc65-54ed-bfcf-2386619399a5/scratchpad/vis2-fi-13/: fy5-15-{390,1280}-I0-05-0.png, fy5-15-390-2W8000-1.png, fy5-15-1280-2W8000-0.png, fy5-15-{390,1280}-85dB-0.png, fy5-15-{390,1280}-to16m-0.png (sheets sheet-fy5-15-390-1.png, -390-2.png, -1280-1.png).
- Apart from the semicolon: rows start with a relation or an arrow, 3,2 · 10^−13 W/m² stays whole, nothing clipped (right edges 202–286 px in boxes ending 333–360 px), no page overflow.

## Scores
illustrations 5 · typography 3 · Finnish 4 · accessibility 4
