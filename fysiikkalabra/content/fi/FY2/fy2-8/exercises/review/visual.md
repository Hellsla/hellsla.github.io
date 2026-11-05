VERDICT: PASS
CONTENT-HASH: 29e5ecd1dc7acc04
Round: 2

## Blocking

## Polish
- [Minor] L3-05 solution, Sijoitus (L3-1280-8) — parts a) and b) carry one-line calculations ("a) Maakaasu: $490 \cdot 30 \cdot 10^{6}\,\text{g} = 14\,700\,\text{t}$") between boxed rows, so the block alternates between prose and display rows; give each source the same aligned row as the first one.
- [Minor] all data tables (L2-05, L2-06, L3-04, L3-05) — numeric column headers sit left of their right-aligned numbers — right-align numeric headers.

## Checked
- Round 1 Blocking (paragraph break lost in L2-06, L3-04, L3-05): resolved; a)–d) are own bold paragraphs, the box instruction ends the right part.
- Round 1 Polish: L1-07 "Esimerkkiväite:" label giveaway removed (options now parallel); L3-05 Sijoitus partly improved (see Polish).
- L2-1280-6, -8 (L2-05 solution, L2-07 MC and model solution), L3-1280-4, -5, -7, -8 (L3-03 end, L3-04, L3-05 text, table, solution).
- Revealed answers match the boxes (checked in the built page for all new numeric tasks).
- 1280 px only (no 360 px exercise capture; layout checks clean).

## Scores
illustrations 5 · typography 4 · Finnish 4 · accessibility 4

## Follow-up (2026-11-04, teacher's edit of L1-06: exercises.json:69, solutions.md:125)
- Own Playwright check of the built preview, L1-06 answered (option 0) and the solution open: every inline formula of the two sentences ($+15\,{}^\circ\text{C}$, $-18\,{}^\circ\text{C}$, $33\,\text{K}$) lies on one line (one line box per `.katex-html`) at 390 px and at 360 px; scrollWidth = viewport width; no raw `$`. Captures retaken (`screenshot.py fy2-8 --lang <lang>`, 1280 px) and an own 390 px capture of L1-06 opened.
- Typography: degree with thin space and upright C, K upright with thin space, minus sign rendered as a true minus; consistent with the lesson.
- Finnish: correct and natural. [Minor] "…, kun yksinkertainen säteilytasapainomalli antaa …" → "…, kun taas yksinkertainen säteilytasapainomalli antaa …" (both sentences) removes a possible causal reading.
- Scope: only these two sentences; the rest of this report stands from the earlier round.
