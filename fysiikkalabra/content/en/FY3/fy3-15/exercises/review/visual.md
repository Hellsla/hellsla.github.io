VERDICT: FAIL
CONTENT-HASH: dbe8bd90ec39ffa3

## Blocking
- [Major] fy3-15-L2-05 data table (390 px) — the row header $E_\text{district heating}\,(\text{GWh})$ is wider than its cell and overprints the value (1190, 1410, 1470 read as `GWh)1190`) — a data value is partly unreadable on a phone — let the header wrap (`\text{district}\ \text{heating}` with a line break, or the short `E_\text{dh}` explained in the caption) or give the first column of the table more width.

## Polish
- [Minor] fy3-15 solution Reasonableness — "85–90 %" breaks after the dash at the line end; bind the range (`85\text{–}90\,\%` inside one formula).

## Checked
- Own 390 px and 1280 px captures of the built page with every exercise solution open (the packet's shots hold 1280 px only): every display formula in text context (about 10 per set, stitched sheets) and a DOM check of clipping, horizontal overflow and lone punctuation after a display formula in all exercises; plus the packet captures open-exercises-L*-1280.
- Changed formulas: equals signs in one column, continuation rows start with an operator, wide screens join the rows, no clipping at 390 or 1280 px, no row breaking inside a number or unit; trailing punctuation sits inside the formula in solutions.
- Hash run at start and end: unchanged.

## Scores
illustrations 5 · typography 3 · Finnish 4 · accessibility 3
