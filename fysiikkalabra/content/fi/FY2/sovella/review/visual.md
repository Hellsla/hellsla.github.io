VERDICT: FAIL
CONTENT-HASH: 383e9f5906f74bd2

## Blocking
- [Major] tasks.json fy2-s2 title / stage heading — the long word "energiakysymyksestä" sets the heading's min-content, so the points label "14 pistettä" is pushed past the viewport: clipped to "14 pis" at 360 px and "14 pistett" at 390 px, and the page scrolls sideways (check_layout: page 34 px at 360, 4 px at 390, closed state; same in fi-easy). The point total is clipped and the phone page gains horizontal scroll — fix: a title whose longest word fits beside the label, e.g. "Kaksi lähdettä samasta kysymyksestä", or a soft hyphen "energia­kysymyksestä" (or let `.pts` wrap under the title in site.css).
- [Major] tasks.json fy2-s2 "Vastauspohja" table — site.css lays `thead` and `tbody` out as two separate tables (`table thead,table tbody{display:table}`), so with empty answer cells the columns do not line up: at 360 px the heads "Lähde 1 | Lähde 2" sit at 167–328 px over the row labels while the body's two answer columns are 16 px wide each (26 px at 1280). The template's whole point, two columns to fill, is invisible and the heads float over the wrong column — fix: a shared column layout for this table (template fix: one table box with an overflow wrapper, or `table-layout:fixed` with the same column widths on thead and tbody), or, content-side, write the template as two short lists ("Lähde 1: …", "Lähde 2: …").

## Polish
- [Minor] solutions.md fy2-s2 — the unit is `\tfrac{\text{g}}{\text{kWh}}` inline (sub-script size, about 8 px on a phone) while fy2-s1 on the same page writes `\text{g/kWh}`; use `\text{g/kWh}` for one notation and legibility.
- [Minor] solutions.md fy2-s2 Yleisiä virheitä — "Lähteellä on sama julkaisija" → "Lähteillä on sama julkaisija".

## Checked
- Scope (teacher: only changed parts): intro, fy2-s2 task text, table, parts a–d, its solutions (rewritten during this review; re-captured for 383e9f…).
- stage-fy2-s2-390-1, -2; page-390-22, -23, -24; contact-2.
- Own captures at 360 and 390: s2 heading (viewport), Vastauspohja table, new Lähdemerkinnät list, the `7\text{–}56` range sentence.
- Inline formulas: none wraps (`.katex` nowrap, checked at 360/390); no inline formula overflows in open state.
- check_layout FY2-sovella at 360 and 390.

## Scores
illustrations 5 · typography 4 · Finnish 4 · accessibility 2
