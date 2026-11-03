VERDICT: FAIL
CONTENT-HASH: ba0b217d6c6cbce6

## Blocking
- [Major] fy2-8-1280-0.png, fy2-8-360-0.png (figure.unit-photo.wide) — the caption and credit collapse into a column about 120 px wide under the map (about 25 lines at 1280 px, about 20 at 360 px), because figcaption keeps display:table-caption inside a display:block figure — a caption that narrow is hard to read and breaks the page rhythm — fix in templates/site.css: figure.unit-photo.wide figcaption{display:block}; the caption and alt text wording itself is natural, factual and consistent with the map.

## Polish
- none

## Checked
- batch delta review: opened fy2-8-1280-0.png and fy2-8-360-0.png (photo floated or inline in the column, no clipping or horizontal overflow, credit line present); alt text and caption read against the picture and the neighbouring paragraph; no number with a unit in the new caption or alt text.
