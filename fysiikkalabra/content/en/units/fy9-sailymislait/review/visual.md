VERDICT: PASS
CONTENT-HASH: f0692292b27bcf27
SCOPE: delta: new Sovella itsenäisesti tasks s7 (Kelkka rinteessä / Sled on a slope) and s8 (Jalkapallon potku / A kick on a football) with solutions, answers.py and the changed intro sentence, language en; s1-s6 and older text stand under the previous PASS.

## Blocking
- (none)

## Polish
- s7 b) Järkevyys and s7 d) Sijoitus carry three-figure intermediates ($37{,}5\,\%$, $3{,}75\,\text{N}$, $-22{,}5\,\text{J}$) from two-figure data; the answers are rounded to two figures, so this is only a check chain. Optional.
- s8 b) shows $12{,}56\,\text{m/s}$ in the chain and the answer $13\,\text{m/s}$, and c) then uses the unrounded $12{,}56$; the Vastaus lines say why (two figures). Readable as is.

## Checked
- Task texts s7 and s8: situation first, question last as its own sentence; nothing names the solution's structure ("kolme vaihetta", "kahdesti" absent); the s7 d) question only asks what happens to the speed and to justify by calculation.
- Figures: s7 `fy4-8/palkit-asteikko` and s8 `fy4-9/tarkistus-kolmio`, both reused from the owners' figures.py. Alt text names equal the task's names ($E_{\text{p}0}$, $E_\text{k}$, "voima, jolla jalka potkaisee palloa, ajan funktiona"); the figures are legible at 390 px, axes carry quantity and unit, the bars and the triangle are distinct from the grid, the area is not shaded (answer not given away).
- Rounding: answers are two figures like the data ($2{,}0\,\text{m}$, $15\,\text{J}$, $2{,}5\,\text{N}$, $5{,}0\,\text{m/s}$, $5{,}4\,\text{N s}$, $13\,\text{m/s}$, $34\,\text{J}$, $8{,}0\,\text{m}$, $-6{,}5\,\text{J}$, $1{,}0\,\text{N}$); each Vastaus says why. answers.py values (e.g. 2.039, 12.558, 33.91) lie inside the stated tolerances of these roundings.
- Calculation chains are aligned rows, each starting with the quantity; the long ones in s7 d) and s8 c)/d) are broken at meaningful boundaries; units upright with a thin space, decimal comma form per language, `\cdot`, colon for the written division, no `\times`.
- Intro sentence reads fluently; the number "eight" matches the eight tasks.
- 360 px with solutions open: no clipped, overlapping or overflowing s7/s8 element; the 2 known clipped formulas on the page belong to other tasks.
- No own captures exist for en; the en text is cut line for line like fi (19 aligned blocks, 67 labelled lines, same positions in s7 and s8), so the fi captures stand for the layout. `check_layout.py fy9-sailymislait --width 360` is OK for en with every solution open (only the 2 known clipped formulas, both outside s7 and s8).
- Hash at start and end of review was the same (f0692292b27bcf27).
