VERDICT: FAIL
CONTENT-HASH: 4c93136faa33fa36

## Blocking
- [Major] fig `oscillation` (investigation.md:262–273, "Laajennus") — the label `vakiotermi` sits on the start of the data line, so the line runs through the word (seen at 1280 px and in fig-8-390). It reads as struck through, and the figure's one new idea (the intercept) is hard to read. It also has no marker for the intercept — fix: move the label below or beside the line start, with a short leader line or bracket to the point where the line meets the T² axis, and keep a 10 px gap to the line.

## Polish
- [Minor] investigation.md "Epävarmuus ja luotettavuus" and "Raportoi" — `$k = (k \pm \Delta k)\ \text{N/m}$` uses the same k for the mean and the result; write `\bar{k}` (as in the prerequisite note `\bar{x} \pm \Delta x`) — also with a thin space before `\text{N/m}` it is fine.
- [Minor] model and oscillation figures — both are schematic with no numbers on the axes; add "kaavakuva, ei mittakaavassa" to the aria-label if it is not already there.
- [Minor] "Miksi juuri nämä akselit?" box — one 150-word paragraph with three ideas (axes, swapped axes, close-coiled spring); split with a short `###` or into paragraphs. The last sentence, "Silloin suora ei kulje origon kautta, koska…", repeats an earlier point.
- [Minor] Mittaa table (390 px) — the empty example table is tiny and low-contrast in its header; acceptable, but give the rows more height.
- [Minor] setup figure — the F and G arrows start at the same body edge and overlap the spring coils; draw F ending at the hook for clarity (for science: F acts on the load, so this is fine physically).

## Checked
- contact-1; fig-1 (hero), fig-3 (setup), fig-5 (model), fig-8 (oscillation) at 390 px. fig-2, 4, 6, 7 and 9 are blank or small captures (inline formulas, not figures); I opened them and judged nothing from them.
- top-1280, page-1280-3, page-1280-7, page-390-6, page-390-7. The prediction opening (open-ennusta-1280) was judged only from the contact sheet.
- KaTeX renders cleanly everywhere I looked (no red source); fractions, \overline vectors and \Delta are fine; the table does not scroll sideways.
- Finnish is fluent and uses the right terms; no mechanical phrasing.

## Scores
illustrations 3 · typography 4 · Finnish 5 · accessibility 4
