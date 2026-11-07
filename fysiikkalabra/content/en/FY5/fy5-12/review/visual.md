VERDICT: FAIL
CONTENT-HASH: 30988471b8c66f62

## Blocking
- [Major] fy5-12 page credits list (#credits, from assets/pics/fy5/photos.json "ripple-model-two-sources.webp" title) — the entry reads "**Laskettu mallikuva: kahden lähteen interferenssi aaltoaltaassa**. Ruukkilabra. Computed from a model for this site.": the picture's title is untranslated Finnish on the English page, the same broken-language defect the round's fix set out to remove — give Ruukkilabra's own computed pictures a title per language (e.g. a `title_en` that build.py uses on English pages: "Computed model picture: two-source interference in a ripple tank").

## Polish
- [Minor] fy5-12 credits list — the heading "Photographs" now lists only a computed image — use a neutral heading such as "Picture credits" when a computed picture is in the list.

## Checked
- light delta review (teacher 2026-11-07), after fixes: own 390 px (2×) element captures of preview/en/fy5-12.html — the ripple-model-two-sources figure (sources, checkered near field, fringes and nodal lines legible; caption matches), its credit line "Computed image: Ruukkilabra" (correct, English) and the #credits list; build.py/lang/en.json/photos.json diff; page width 390 px, no overflow.
