VERDICT: FAIL
CONTENT-HASH: 90068beebaa21970

## Blocking
- [Major] fy2-8-1280-0, fy2-8-360-0 (figure.unit-photo.wide, GISTEMP map) — the caption and credit line are squeezed into a column about 130 px wide (the table-caption of the shrink-to-fit figure), so the six-line caption becomes a 20-line strip of one or two words per line, both at 1280 px and at 360 px, and the page jumps down — a reader cannot read the explanation of the colours and the grey no-data area comfortably — fix in templates/site.css: add figure.unit-photo.wide figcaption{display:block;max-width:var(--measure)} (the caption text itself is fine and needs no change).

## Polish
- none

## Checked
- batch delta review: opened fy-easy captures fy2-8-1280 and fy2-8-360 (photo, caption, credit line, alt text read against picture and neighbouring paragraph; no clipping or horizontal overflow; no plain-text quantity in new caption/alt).
