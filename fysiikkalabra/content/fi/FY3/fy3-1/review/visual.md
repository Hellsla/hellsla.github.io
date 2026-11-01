VERDICT: FAIL
CONTENT-HASH: 62daa651fbd9a7eb

## Blocking
- [Major] lesson.md, Paino (theory-1280-2) — the edited sentence sets the equation in two pieces with a plain "=" between them: "sillä $1\,\text{N}$ = $1\,\text{kg}\cdot\text{m/s}^2$". On the page the sans "=" sits between two KaTeX halves. This is a plain-text symbol in newly edited text, and the identity defines the unit, so it has to read as one formula — fix: `sillä $1\,\text{N} = 1\,\text{kg}\cdot\text{m/s}^2$ (tämä …)`.

## Polish
- [Minor] lesson.md, Paino — the same paragraph shows the unit plain "(m/s²)", "g yksikössä m/s²" beside KaTeX "$9{,}81\,\text{m/s}^2$", so two typefaces sit side by side on one line — write the bare units as `$\text{m/s}^2$` too (the table header can stay).
- [Minor] sim-390 — canvas text still 6–9 px at phone width, and the forcemeter scale runs to 2500 N, so 98 N reads as "0". The bar-chart part is resolved (gridlines 50–200 up to the 248 N line, caption "kaavion asteikko 0–248 N" reads well and does not collide with the "G (N)" title) — make the gauge scale follow the case.
- [Minor] force-extension figure (theory-1280-1) — the solid line still runs past the last point (10 N) and past the last gridline — dash or stop it at 10 N.
- [Minor] inquiry.json feedback — the chains still divide with a slash ("$5{,}6 / 1{,}6 \cdot 1{,}0\,\text{N}$", "$12\,\text{N} / 1{,}62\,\text{m/s}^2$"), while the lesson now uses a colon — use a colon in these written divisions as well.
- [Minor] Tarkista (choice) — carried over and not re-checked at full size: a wrong selected answer has the same frame as a correct one — use a neutral selected state.

## Checked
- Captures were blank (4 KB, page hash 09e56…). I re-ran `screenshot.py fy3-1`, and the new stamp shows 62daa651fbd9a7eb, page 582f4e44….
- fig-2-390 and theory-1280-1: the weight arrows G and 2G are now red #c92a2a, matching the sim. Item resolved.
- theory-1280-1/-2/-3: every edited quantity renders as KaTeX, and the case endings ("$1\,\text{N}$:ksi", "$1180\,\text{N}$:sta") attach cleanly. "($1{,}62 : 9{,}81 \approx 0{,}17 \approx 1 : 6$)" reads well. Item resolved, apart from the Blocking issue.
- example-390-2: steps 6–7 now in maths, with the Mars ratio given as a colon. Nothing wraps badly.
- sim-390 and sim-1280: gridlines, caption and the canvas decimal comma are accepted.
- lab-1280-2 (Voimamittarin asteikko: prompt and choices in KaTeX), open-exit-1280, open-tarkista-1280-2, top-390, contact-3.

## Scores
illustrations 4 · typography 3 · Finnish 4 · accessibility 4
