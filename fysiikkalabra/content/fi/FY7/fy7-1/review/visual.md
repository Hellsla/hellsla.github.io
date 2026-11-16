VERDICT: PASS
CONTENT-HASH: f23cfc4db24923ce

## Blocking
- none

## Polish
- [Minor] inquiry.json kertaus feedbacks — the chain is hand-split into a display `aligned` mid-sentence; it reads well (390 and 1280 px, the period after the 50 N stays with the formula), but NOTES §1 says never hand-split; the shared reflow would do it.
- [Minor] docs/clipped-formulas.tsv — fy7-1 keeps formulas that were already clipped before this change (outside this change, work queue 5d; Major outside this change, not blocking): three formulas with B = sqrt(...) remain in the list.

## Checked
- Delta: only inquiry.json re-breaks. Rendered the changed items myself from the built page (preview/fy7-1.html) at 390 px with hints and solutions open; the Pohdinta retrieval's feedback (sqrt row, then = 50 N on its own row, aligned) and the same at 1280 px (one row): readable, aligned, nothing clipped.
- Opened the lesson's existing 390 px stage captures (herata, sovella, tarkista) and contact sheet; the stages around the changes keep their layout, no horizontal overflow.

## Scores
illustrations 5 · typography 4 · Finnish 5 · accessibility 4
