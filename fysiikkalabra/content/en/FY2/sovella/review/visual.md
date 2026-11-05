VERDICT: FAIL
CONTENT-HASH: 58297e6f780ea8f5

## Blocking
- [Major] tasks.json fy2-s2 "Answer template" table — site.css lays `thead` and `tbody` out as two separate tables (`table thead,table tbody{display:table}`), so with empty answer cells the columns do not line up: at 360 px the heads "Source 1 | Source 2" sit at 159–328 px over the row labels while the body's two answer columns are 16 px wide each (same at 390 and 1280). The template's purpose, two columns to fill, is invisible and its heads float over the wrong column — fix: one shared column layout for this table (template: a single table box inside an overflow wrapper, or `table-layout:fixed` with the same column widths on thead and tbody), or, content-side, write the template as two short lists ("Source 1: …", "Source 2: …").

## Polish
- [Minor] solutions.md fy2-s2 — the unit is `\tfrac{\text{g}}{\text{kWh}}` inline (script size, about 8 px on a phone) while fy2-s1 on the same page writes `\text{g/kWh}`; use `\text{g/kWh}` for one notation and legibility.
- [Minor] solutions.md fy2-s2 a) — "the page tells about the advantages of wind power" → "the page describes the advantages of wind power"; c) "If the source does not tell something" → "If the source does not say something".

## Checked
- Scope (teacher: only changed parts): intro, fy2-s2 task text, Answer template, parts a–d and the fy2-s2 solutions as now on disk (rewritten during the review: references list, CO2-eq wording, the 7–56 range).
- Own captures of preview/en/FY2-sovella.html at 360 and 390 px (screenshot.py captures Sovella only in fi): s2 heading (fits: "14 points" inside at 344/374 px), Answer template table, the unit-conversion paragraph of b).
- Table cell geometry measured at 360, 390, 1280.
- Inline formulas: none wraps or overflows at 360/390; check_layout en FY2-sovella OK at 360 and 390.
- "Hyväksytään myös"/"Yleisiä virheitä" source headings render as "Also accepted"/"Common mistakes".

## Scores
illustrations 5 · typography 4 · Finnish 4 · accessibility 3
