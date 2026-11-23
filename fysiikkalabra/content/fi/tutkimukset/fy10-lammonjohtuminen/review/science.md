VERDICT: PASS
CONTENT-HASH: 74a43218f9d568c4

## Blocking
None.

## Polish
- Table header (line 122) still uses `\ ` between a symbol and its parenthesised unit, e.g. `$t\ (\text{min})$`; a word space before a bracketed unit is acceptable, change to `\,` only if the house style wants it uniform. Not physics.

## Polish (earlier rounds)
None.

## Checked (delta 2026-11-23, gate)
- Diff against HEAD: Ohjattu tuki only, `15\ \text{cm}` – `20\ \text{cm}` and `x = 3\ \text{cm}` became `15\,\text{cm}` – `20\,\text{cm}` and `x = 3\,\text{cm}`. Numbers, units and symbols unchanged; thin space between number and unit is the SI/house convention. Reads correctly.
- Diff since my last PASS (hash 192bf50dde36abe4): besides the above, only the inline SVG drawings of hero, emission and setup became teacher-approved raster images (`approve-figures`) with the same LaTeX labels and aria-labels. Viewed all three: emission still shows a strong emitted ray from the matte part, a weak own emission plus a reflected ambient ray from the shiny part, one body at one temperature; setup shows equal-depth rods taped above the water, insulating lid, thermometer in the water, x measured from the lid top, camera on a stand; hero shows five taped rods in a lidded pot. Consistent with the text; no physics change.
- investigation.json and teacher.md unchanged since the last PASS; earlier checks stand.
