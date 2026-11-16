VERDICT: PASS
CONTENT-HASH: fd4fea8ed3adf8ba

## Blocking
- none

## Polish
- [Minor] inquiry.json siirto solution, Sijoitus — the numerator of the root is split by hand into two rows (2 · 1,602 · 10^-19 C / · 20 000 V); readable and unclipped at 390 px, but the radical becomes tall and the result row starts at the far left; acceptable, a cleaner shared reflow would be nicer.
- [Minor] docs/clipped-formulas.tsv — fy7-2 keeps formulas that were already clipped before this change (outside this change, work queue 5d; Major outside this change, not blocking): about a dozen Sovella chains and exercise formulas (qB, 1,602 · 10^-19 C …) are still listed.

## Checked
- Delta: only inquiry.json re-breaks. Rendered the changed items myself from the built page (preview/fy7-2.html) at 390 px with hints and solutions open; the Sovella "uuteen tilanteeseen" solution: Muunnokset, Sijoitus (v and B rows, ja), Vastaus, Järkevyys all readable, nothing clipped. 
- Opened the lesson's existing 390 px stage captures (herata, sovella, tarkista) and contact sheet; the stages around the changes keep their layout, no horizontal overflow.

## Scores
illustrations 5 · typography 4 · Finnish 5 · accessibility 4
