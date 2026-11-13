VERDICT: PASS
CONTENT-HASH: 3b2542ea34316c42

Mode: delta (unit list now a table)

## Blocking
- none

## Polish
- [Minor] fy1-2 unit table at 360 px — the card layout repeats the label "Rakenne/Koko/Yksikkö/Yksikön arvo" six times, so the table is long on a phone (about 6 screens' worth of 4 rows each). Acceptable and a shared component's behaviour; no change needed.

## Checked
- fy1-2-theory-1280-1.png, -2.png: table at 1280 px: headers, aligned columns, LaTeX units, soft hyphen in "väli-matkat", bold row heads, figure and text around it intact.
- fy1-2-stage-selita-390-2.png, -3.png: table at 390 px as labelled cards, no clipping or overflow.
- Own captures of the table at 360 and 768 px (playwright on preview/fy1-2.html, no shipped captures exist for these widths): 768 px four columns readable and fits, 360 px stacked cards, no horizontal overflow (scrollWidth equals viewport).

## Scores
illustrations 5 · typography 5 · Finnish 5 · accessibility 4
