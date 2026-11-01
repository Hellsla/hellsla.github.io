VERDICT: PASS
CONTENT-HASH: 3259381ff4df8e48

## Blocking
(none) The map canvas could not be judged, because OpenStreetMap tiles are blocked here (the coordinator expects this). Its markers, the list, the filters and the panels were judged and work.

I found one defect during the review, and commit 0f3e54ff fixed it. After typing in the search box, the first tap on a result did nothing, because the blur fired `change`, which rebuilt the list. I retested at 390 and 1280: one tap on "Model A" now opens its panel. A `#f-jet` link now scrolls to the JET panel, which sits at 72 px, just below the sticky bar. Opening an item from the list also places the panel at 71 px (scroll-margin works).

## Polish
1. [Minor] List at 390 (`fx-1-390-2`). Short names break at their hyphen or space: "T- / 1", "T- / 3", "JT- / 60SA", "Model / A". Fix: `white-space: nowrap` on the name in `.fx-map-list button` (units.css), or a non-breaking hyphen in the data.
2. [Minor] Legend at 390 (`fx-1-390-1`). The type and status keys run together in one flow ("Other magnetic concept ● Operating"). The "under construction" symbol ◐ renders as a sliver. Fix: add two short headings ("Type", "Status") and use a symbol the font draws fully, such as a half-filled SVG circle.
3. [Minor] Panel after filtering. When a year filter excludes the open facility (for example ITER with year 1985), its panel stays open beside a list that no longer contains it. Fix: close the panel, or add "Not shown with the current filters."
4. [Minor] Panel text comes from `facilities.json` and writes quantities in plain text: "500 MW … 50 MW of heating (Q = 10)". ITER's years show as "?–". Fix: use `$…$` in the data (the panel runs `md`), and show "under construction" instead of "?–".
5. [Minor] With `#f-` at 390, a Leaflet tooltip for the Culham site is cut off at the map's left edge ("TART, MAST, MAST Upgrade"). Fix: set the tooltip's `direction: 'auto'`.

## Checked
- Captures current for this hash: contact-1 and 2, intro-390, fx-1-390-1 and 2 (filters, legend, list), sovella-390-2.
- Hero: Earth with arcs, no text, nothing clipped.
- Driven myself at 390 and 1280:
  - `#f-jet` link, list → ITER panel, year 1985 → "8 of 63 facilities shown", search "Model A" → panel and note;
  - all 4 model answers after writing, and all 7 choices with their feedback (predictions locked).
- The only console errors are the failed tile requests. No `.katex-error`, no raw `$` and no horizontal overflow.
- French corner tips (*la carte du monde*, *le pays*, *La France accueille ITER*) are consistent and tagged `lang="fr"`.

## Scores
illustrations 4 · typography 4 · English/French 4 · accessibility 4

## Shared issues
- `assets/units/fy14/fx/map.js` and `units.css`: items 1, 2, 3 and 5 above. The map does not re-fit to the filtered markers either (after filtering, markers can sit outside the view). Re-fitting could be tested once tiles load.
- `assets/units/fy14/data/facilities.json`: item 4 above (plain-text units in panels).
