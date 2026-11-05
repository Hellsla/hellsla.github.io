VERDICT: FAIL
CONTENT-HASH: 2ed55e71f88658da
Mode: delta
Round: 1

## Blocking
- [Major] figure aria-labels of fy3-1/pick-rest, pick-long-pull, pick-extra, pick-weight-only on the en page — the four description texts are Finnish ("Voimakuvio mittakaavassa: kappale suorakulmiona ..."), because content/en/FY3/fy3-1/figures.json has no translation for them (grep finds 0); an English screen-reader user hears Finnish and cannot choose among figure-only options — add the four English descriptions to content/en/FY3/fy3-1/figures.json (G down from the centre, F up from the top face, F_k down from the bottom face, arrows equally long or F twice as long, and so on).

## Polish
[Minor] Option figures are about 250 px tall each, so the task is long on a phone (four stacked figures); consider a smaller figure width if the set is edited again.

## Checked
- New task fy3-1-L1-09 at 390 px (en), own render of preview/en/fy3-1.html: task text, every option and its feedback open, solution card open; page and card have no horizontal overflow (scrollWidth equals width).
- The four option figures (pick-rest, pick-long-pull, pick-extra, pick-weight-only) opened at 390 px: arrows G, F, F_k and the rectangle are clear, arrow lengths match the feedback, all labels LaTeX, no word inside any figure.
- Delta covers only the new task and its solution; surrounding exercises were not changed.
- Finnish inside the figure on the en page: none visible (labels are only G, F, F_k, all language neutral). Finnish appears only in the aria-label (see Blocking).

## Scores
illustrations 5 · typography 4 · Finnish n/a (English text clean) · accessibility 2
