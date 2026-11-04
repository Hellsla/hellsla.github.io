VERDICT: PASS
CONTENT-HASH: 5d7daab35c8d643b

Delta review of the course rename FY12 → FY9 (commit 3052d352). Previous all-PASS hash: d64ab1c8503f8cb7. The hash was the same at the start and the end of this review.

I checked that the change is only the rename: every file of `content/fi/units/fy9-energia/` and `lessons/units/fy9-energia/` (review/ excluded) at 3052d352 equals the file at 47782fdd with `fy12` → `fy9` and `FY12` → `FY9` replaced, and nothing else. No `fy12`/`FY12` remains in the unit's sources or in the built preview.

## Blocking

- none

## Polish

None new. The Polish items of the previous visual report still apply.

## Checked

- `python3 scripts/build.py fy9-energia` (preview only; site/ untouched). Playwright at 390 and 1280 with every details element open: no `.katex-error`, no raw `$`, no page errors, no broken images, no horizontal scroll (scrollWidth = viewport).
- SVG ids: every `url(#…)` and `href=\"#…\"` in the preview resolves to an id on the page; renamed `data-fig` ids match the generators (`python3 scripts/units.py figures fy9-energia`: up to date).
- All `*.html` links in the preview point to existing pages.

## Shared issues

None.
