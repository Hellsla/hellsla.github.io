VERDICT: FAIL
CONTENT-HASH: 29e577cbf20e55f6
Round: 2

## Blocking
- [Major] L3-05 data table (open-exercises-L3-1280-7) — the table is wider than the 664 px task column because the last row holds long text ("Sääriippuvainen, ei säädettävissä"); the whole "Ydinvoimala" column (1200, 90, 6000, 60, 12) is off screen behind a sideways scroll even at 1280 px, and part a)–d) cannot be started without scrolling to it — fix: shorten the last row's cells in exercises.json to "Sääriippuvainen" and "Tasainen" (the solution already explains the control question), and shorten the first column labels if the table still overflows at 360 px.

## Polish
- [Minor] L2-05 and L2-07, "Vastaus" disclosure (L2-1280-5, L2-1280-8) — the revealed answer is the bare number "23" and "1,6" without the unit the box shows (prosenttiyksikköä, milj. t) — write the unit in the solution's Vastaus line inside the maths, e.g. "$23\,\text{prosenttiyksikköä}$" and "$1{,}6\,\text{milj. t}$".
- [Minor] all data tables — numeric column headers sit left of their right-aligned numbers — right-align numeric headers.
- [Minor] L3-05 solution, Sijoitus (L3-1280-7, -8) — a), b), c) per plant are now aligned rows, readable; no further action.

## Checked
- Round 1 Blocking (paragraph break lost in L2-06, L2-07, L3-04, L3-05): resolved; a)–d) are own bold paragraphs with the box instruction in the right part.
- Round 1 Polish: L2-05 "Anna vastaus muutoksena prosenttiyksikköinä." done; L2-06 Finnish quotes ”…” done; L3-05 Sijoitus rows done.
- L2-1280-5, -6, -8, L3-1280-4, -6, -7, -8, -9 (L2-05, L2-06, L2-07 tables and solutions; L3-04 and L3-05 text, tables, solutions).
- 1280 px only (no 360 px exercise capture; layout checks clean).

## Scores
illustrations 5 · typography 4 · Finnish 4 · accessibility 3
