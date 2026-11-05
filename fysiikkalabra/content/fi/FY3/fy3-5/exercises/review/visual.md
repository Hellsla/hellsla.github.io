VERDICT: FAIL
CONTENT-HASH: 07ff0780b71756eb

## Blocking
- [Major] fy3-5-L1-09, feedback of statement 1 (390 px render) — the display chain `\Delta U = Q + W = 0 + 60\,\text{J} = 60\,\text{J}` is wider than the 300 px box: the end is cut at "= 60" and the unit J is out of sight (reachable only by sideways scrolling) — a result without its unit, and the lesson's own chain-width rule is broken — split into two lines: `\Delta U = Q + W` and `= 0 + 60\,\text{J} = 60\,\text{J}`, or write `\Delta U = 0 + 60\,\text{J} = 60\,\text{J}`.

## Polish
- [Minor] fy3-5-L1-09 — statements 1 and 2 are the true ones and 3-5 the false ones in a block; the order is not a giveaway, but mixing (T, F, T, F, F) would remove the pattern.
- [Minor] fy3-5-L1-09 feedback 2 — "Ilmaa voi kuumentaa tekemällä siihen työtä, kuten pyöräpumpun mäntä tekee" reads loosely; "kuten pyöräpumppua käytettäessä".
- [Minor] Model answer chain (`\Delta U = Q + W = 0 + 60\,\text{J} = 60\,\text{J}`) fits at 390 px in the solution; no change.

## Checked
- Own render at 390 px with Playwright (preview/fy3-5.html), L1-09 with solution open and every feedback revealed (all five statements answered correctly; feedback unhidden), read in four tiles: task text, five statements with Tosi/Epätosi controls, feedback boxes, Vastaus/answer block, Annettu/Kysytty/Periaate/Mallivastaus.
- From text only: distractors catch the chapter's warned mistake (heat stored in a body, Q confused with W, "no heat means no change"); within what fy3-5 teaches; ΔU = Q + W signs fine. Quantities carry LaTeX units. Paragraph splits of the other changed tasks read correctly in the diff (not rendered).
- No horizontal page overflow (scrollWidth 390).

## Scores
illustrations 5 · typography 3 · Finnish 4 · accessibility 4
