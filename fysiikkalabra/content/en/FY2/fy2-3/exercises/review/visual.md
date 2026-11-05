VERDICT: PASS
CONTENT-HASH: 563ece0a62c60f6f
Round: 1 (delta)

## Blocking
(none)

## Polish
- [Minor] data tables — captions and the right-hand columns are cut at 390 px and scroll sideways (design rule, NOTES §1); header cells stay left of right-aligned numbers.

## Checked
- Render at 390 px (own Playwright, preview/en/fy2-3.html, all levels open, solutions open, choices answered): page scrollWidth 390, no overflow; the only chains/KaTeX wider than their box are the data-table headers inside the scrolling .exp-table (by design). New L2-08 (choice task, model answer P1, P2, P2:P1 chain) opened as a card: all chains fit, no clipping.
- L3-04, L3-05 cards (task text now split in paragraphs, a stage per paragraph) opened at 390 px (L3-05 en; L3-04 only measured).
- Text only: solutions.md and exercises.json diffs (L2-08 choices and feedback, answers.py comment), wording, glossary use, number and unit LaTeX, decimal comma/point.
- From earlier captures (1280 px, already current for this hash): en fy2-3 open-exercises-L2-1280-9 (L2-08) opened. Contact sheets and the other 1280 captures not opened; fi-easy fy2-5 had no captures (its preview page was empty), so all of its judgement is from my own render.

## Scores
illustrations 4 · typography 4 · language 4 · accessibility 4
