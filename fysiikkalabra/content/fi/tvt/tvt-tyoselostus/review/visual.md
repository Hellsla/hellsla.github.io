VERDICT: FAIL
CONTENT-HASH: 3336b3617eb6b37b

## Blocking
- [Major] guide.md step 4 (page-390-2, page-1280-1) — "y = mx + b", "Ohjelman m on kulmakerroin ja b vakiotermi" and "m: 4.05 ja b: 0.02" are plain text beside the LaTeX $y = 4{,}05x + 0{,}02$; the symbols render in a different typeface in the same sentence — NOTES §1: a symbol named in the student's text is inline maths — set "$y = mx + b$", "$m$", "$b$" as maths. If the program's result box is quoted verbatim, keep it visibly as a quotation ("m = 4.05") and say so, but the explanation "$m$ on kulmakerroin ja $b$ vakiotermi" is maths.

## Polish
- [Minor] guide.md steps 2 and 5 — straight quotation marks around the caption examples ("Taulukko 1. …", "Kuvasta 1 nähdään …"); Finnish uses ”…” — use ”…”.
- [Minor] guide.md step 4 — "Jos keksityillä esimerkkiarvoilla tulosruudussa on …" is clumsy — "Jos tulosruudussa olisi esimerkiksi m: 4.05 ja b: 0.02, …".
- [Minor] fig-2-390 — the capture is an empty 28×28 element after figure 1 (inventory lists one figure) — check that no stray SVG or icon is left in step 7.
- [Minor] Figure "page" at 390 px — labels scale to about 13 px, readable but the lowest the standard allows; the graph has no ticks (acceptable as a schematic, and the aria-label says it is without values).
- [Minor] Step 8 "Mittaustaulukon voit kirjoittaa … ja koko datan voit liittää" — two ideas in a sentence with repeated "voit"; consider splitting.

## Checked
- fig-1-390 (the report-page schematic): table, graph, caption and result drawn cleanly, grey bars read as the student's own text, labels LaTeX, nothing clipped, palette consistent, the fitted line passes through the points.
- page-390-2 and page-390-3 (steps 4–8, mistakes list), page-1280-2 (figure at laptop width, steps 7–8, mistakes). Contact sheet and top captures were not opened separately.
- Figure aria-label read from the source: complete and accurate.
- No horizontal overflow or clipping seen; reading width and hierarchy fine.

## Scores
illustrations 4 · typography 3 · Finnish 4 · accessibility 4
