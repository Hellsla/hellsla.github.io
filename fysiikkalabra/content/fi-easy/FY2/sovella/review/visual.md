VERDICT: FAIL
CONTENT-HASH: 6ad8e1333a0cfb00

## Blocking
- [Major] tasks.json fy2-s2 title / stage heading — the long word "energiakysymyksestä" sets the heading's min-content, so "14 pistettä" is pushed past the viewport: clipped to "14 pis" at 360 px and "14 pistett" at 390 px, and the page scrolls sideways (check_layout fi-easy: page 34 px at 360, 4 px at 390, closed state). The point total is clipped and the phone page gains horizontal scroll — fix: a title whose longest word fits beside the label, e.g. "Kaksi lähdettä samasta kysymyksestä", or a soft hyphen "energia­kysymyksestä" (or let `.pts` wrap under the title in site.css).
- [Major] tasks.json fy2-s2 "Vastauspohja" table — site.css lays `thead` and `tbody` out as two separate tables (`table thead,table tbody{display:table}`), so with empty answer cells the columns do not line up: at 360 px the heads "Lähde 1 | Lähde 2" sit at 167–328 px over the row labels while the body's two answer columns are 16 px wide each (also at 390). For an S2 reader the template's two columns to fill are invisible and the heads float over the wrong column — fix: a shared column layout for this table (template: one table box inside an overflow wrapper, or `table-layout:fixed` with equal column widths on thead and tbody), or, content-side, two short lists ("Lähde 1: …", "Lähde 2: …").

## Polish
- [Minor] solutions.md fy2-s2 — the unit is `\tfrac{\text{g}}{\text{kWh}}` inline (script size, about 8 px on a phone) while fy2-s1 on the same page writes `\text{g/kWh}`; use `\text{g/kWh}`.
- [Minor] tasks.json fy2-s2 table — "Tarkasteluraja" first appears in the table before c) explains it; add "(mitä luku sisältää)" to the row, as the intro does for "rajaus".

## Checked
- Scope (teacher: only changed parts): intro, fy2-s2 task text, Vastauspohja, parts a–d and the fy2-s2 solutions as now on disk (rewritten during the review: lähdemerkinnät, CO2-ekvivalentti, median and range explained).
- Own captures of preview/fi-easy/FY2-sovella.html at 360 and 390 px (screenshot.py captures Sovella only in fi): s2 heading, Vastauspohja table and part a).
- Table cell geometry measured at 360 and 390; check_layout fi-easy FY2-sovella at 360 and 390.
- Inline formulas: none wraps or overflows at 360/390.
- Selkeä suomi: short sentences, one idea each, terms (mediaani, vaihteluväli, hiilidioksidiekvivalentti, elinkaari) explained where they first appear in the solutions.

## Scores
illustrations 5 · typography 4 · Finnish 4 · accessibility 2
