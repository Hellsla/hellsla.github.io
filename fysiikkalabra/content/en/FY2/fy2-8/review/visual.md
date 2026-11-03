VERDICT: FAIL
CONTENT-HASH: 43b6ca4632f45589

## Blocking
- [Major] fy2-8 photo (fy2-8-1280-0, fy2-8-360-0) — the `figure.unit-photo.wide` caption collapses to a column about 100 px wide (about 25 lines at 1280 px and 360 px), so the caption and credit are a tall narrow strip under the map — the `.wide` rule sets `display:block` on the figure but the figcaption keeps `display:table-caption`; add `figure.unit-photo.wide figcaption{display:block}` in templates/site.css.
- [Major] fy2-8 caption — "There are no measurements from the grey area." refers to a grey area that the map does not show (the grey square is only the "no data" swatch in the key) — replace with: "The grey square in the key marks places with no measurements."

## Polish


## Checked
- batch delta review: opened fy2-8-1280-0, fy2-8-1280-1, fy2-8-360-0, fy2-8-360-1; photo loads, no clipping or horizontal overflow, credit line under the caption, alt text and caption natural English and consistent with the picture and the paragraph, no number with a unit in the new text. Other photo(s) on the page are untouched and only seen for layout.
