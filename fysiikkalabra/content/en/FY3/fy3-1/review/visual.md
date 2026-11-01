VERDICT: PASS
CONTENT-HASH: 0742cd113c6b891d

## Blocking
(none) Earlier Polish resolved: every number with its unit in lesson.md, inquiry.json and exit-ticket.json is now inline KaTeX (source checked, no plain quantity left outside aria-labels); the bar chart has gridlines 50…200 up to the 248 N bar and the caption "chart scale 0–248 N" separates it clearly from the spring's 0–2500 N ruler; the readout repeats the explanation. The forcemeter figure's G and 2G arrows are now red #c92a2a, matching the simulation's weight colour and legend.

## Polish
- [Minor] lesson.md Weight, line 214 — "$1\,\text{N}$ = $1\,\text{kg}\cdot\text{m/s}^2$" sets the equals sign in body type between two formulas (visible in theory-1280-2) — write one formula: `$1\,\text{N} = 1\,\text{kg}\cdot\text{m/s}^2$`.
- [Minor] lesson.md Weight, line 223 — at 1280 px the new ratio chain "(1.62 : / 9.81 ≈ 0.17 ≈ 1 : 6)" breaks inside the formula after the colon; inline maths should stay on one line — group it (`{1.62 : 9.81} \approx 0.17 \approx {1 : 6}`) or move the parenthesis to its own short sentence.
- [Minor] inquiry.json (scale-of-a-force-meter feedbacks, Moon 12 N feedbacks) — divisions still written with a slash ("$5.6 / 1.6 \cdot 1.0\,\text{N}$", "$12\,\text{N} / 1.62\,\text{m/s}^2$") while the lesson now uses the colon — use `:` for a written division (`5.6 : 1.6`, `12\,\text{N} : 1.62\,\text{m/s}^2`).
- [Minor] sim-1280/sim-390 — two disclosures, "Assumptions of the model and explanation" and "Assumptions of the model", under the readout read as duplicates — merge them or rename one (e.g. "Explanation").
- [Minor] lesson.md / inquiry.json — "(m/s²)" and "in m/s²" remain plain-text units (no number), beside KaTeX m/s² in the same sentence — optional: `$\text{m/s}^2$` for one typeface.

## Checked
- fig-2-390 and theory-1280-1 (forcemeter figure: red G/2G arrows, labels clear, layout intact).
- theory-1280-1/2/3 (re-set quantities, colon ratio, Summary), stage-selita-390 and #17 via contact-2.
- example-390-2 (Result and Reasonableness: 1.18 kN, colon ratio stays on one line at 390 px).
- sim-1280, sim-390 (gridlines to 200, caption, decimal comma on canvas: allowed).
- open-tarkista-1280-1/2/3, open-exit-1280 (exit ticket maths), contact-2 #13–#24 (interpret-task choices as KaTeX at 390 px, exp-1 sim).

## Scores
illustrations 5 · typography 4 · Finnish (English text) 4 · accessibility 4
