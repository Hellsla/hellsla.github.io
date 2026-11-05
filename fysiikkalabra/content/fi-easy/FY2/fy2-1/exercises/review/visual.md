VERDICT: FAIL
CONTENT-HASH: 8ae898b29f00c580
Mode: delta
Round: 1

## Blocking
- [Major] L2-05, L3-04 and L3-05 solutions (Sijoitus/Substitution and Kaava equation chains) at 390 px — the `eq-chain` boxes scroll sideways with no visible cue and cut the chain: L3-04 `E_tot = 380 PJ + 290 PJ + 230 PJ + 120 …` (chain 449 px in a 302 px box), L2-05 `… + E_sauna` and `… + 4,5`, L3-05 sum of four terms (368 px) — the sum's last terms and the result are unreadable unless the student finds the scroll — break each sum over two lines at a `+` (aligned `=`/`+` rows) as the rest of the chains do, or shrink nothing but add a scroll cue. Unchanged text, found only now because exercises had no 390 px capture.
- [Major] fy2-1-L2-05 Järkevyys (reasonableness) line at 390 px — `60 % + 17,5 % + 15 % + 7,5 % = 100 %` is a display with no scroll box: it runs to x=401 in a 390 px page (page scrolls 15 px sideways) and `= 100 %`, the check result, is cut off — split the sum and result on two lines.

## Polish
- [Minor] new-task wording and layout: none found in the new task; the added L1-09 reads cleanly at 390 px.
- [Minor] 1280 px captures of the exercises exist (previous round); I did not repeat them. Exercise captures at 390 px did not exist, so these were rendered by me.

## Checked
- Own Playwright render at 390 px from preview/fi-easy/fy2-1.html (chromium, every details and every choice answered): new L1-09 (true/false, 5 statements) card at 390 px (own render, answer and solution open); L1-03, L2-04, L3-01, L3-03 cards with the split paragraphs at 390 px (own render, metrics and card shots; L3-01/L3-03 text-split only checked by DOM metrics and the L1-09/L3-05 shots, not each opened).
- DOM metrics for every KaTeX display, table and svg in #exercises at 390 px: page scroll width, boxes wider than their container.
- Solutions.md diff and the new task text read as text (editorial): the new task and its feedback are consistent in wording, units are LaTeX with thin space.
- Not opened: the 1280 px captures from the packet (same as the previous PASS), the lesson itself.

## Scores
illustrations n/a · typography 3 · Finnish 4 · accessibility 4
