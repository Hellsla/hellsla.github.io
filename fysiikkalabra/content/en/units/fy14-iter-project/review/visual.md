VERDICT: PASS
CONTENT-HASH: ec0fadefefca9604

## Blocking
(none)

## Polish
1. [Minor] `schedule` figure (`figures.py`, the `+4 years` arrow; capture `stage-tutki-390-18`). The arrowhead ends inside the lower "D–T" label at 2039, so the head runs into the "D". Fix: end the arrow about 12 units earlier (at about x 512, y 200), or put the 2039 "D–T" label below or to the right of its diamond.
2. [Minor] "D–T" breaks at the en dash at 390. In the Schedule paragraph, "(D–" ends one line and "T)" starts the next. Fix: write `$\text{D–T}$` or use a non-breaking hyphen (U+2011) in running text.
3. [Minor] Investigate 2 (`inquiry.json` `site`, paragraph 1). The events are out of time order: the December 2003 withdrawal comes before the November 2003 EU choice. Fix: "In November 2003 the European Union chose Cadarache as its one candidate, and in December 2003 the Canadian offer was withdrawn."
4. [Minor] Percentages are written two ways. `unit.md` (Members) and the pair-host model use plain "45.6 %" and "9.1 %", but `check-1` uses `$45.6\ \%$`. Fix: use LaTeX everywhere.
5. [Minor] Schedule table at 390: "2034 (re-search operation)" is hyphenated over three lines. Acceptable. Optionally shorten the cell to "2034 (research)" and keep the full term in the text.
6. For science: the order task's `explain` says the conceptual design started in 1988, but `unit.md` (Why, Summary) says "In 1987 four partners started the design". Make them agree, for example: "named in 1987, conceptual design from 1988".

## Checked
- Fresh build and captures for the current hash, taken again after the timeline commits of 09:23–09:25: top and intro at 390 and 1280, every stage at 390 and 1280, contact sheets 1–9.
- The `schedule` figure at 390 with my own capture at 2× (labels 15.5 px at 390 and 18 px at 1280, measured).
- The timeline over HTTP: cards open and close, 40 events in the era. The match, order and say components. Sources and teacher notes.
- The hero has no text and no people.
- No `.katex-error`, no raw `$` and no horizontal overflow at 390 or 1280 (Playwright).
- English editing of unit.md and every inquiry text. French tips.

## Shared issues
- `fx/timeline.js`: each card shows two disclosure marks, the ▾ marker and a "−" button (`fx-1-390-1`). Keep one.
- Timeline at 390: the era *From Geneva to ITER* lists 40 cards, about 7,700 px when all are closed. The new `ids`/query option (commit 406e018c) could limit this task to its ITER cards.

## Scores
illustrations 4 · typography 4 · English/French 4 · accessibility 4
