VERDICT: FAIL
CONTENT-HASH: 760022a5d3f36678

## Blocking
1. [Major] `unit.md`, *Why you understand more than you think*, strategy 3 (*Use word endings*): the endings `-ité`, `-ique`, `-ment` break after their leading hyphen. At **1280 px** the line ends "partner: -" and the next line starts "ité = -ity". At 360 px *-ique* splits the same way. This leaves a detached hyphen in the theory, at the default desktop width, on exactly the morphemes the strategy teaches. The pilot treated the same defect as blocking. Fix: write each ending with a non-breaking hyphen (U+2011, `‑ité`) or wrap it in `.nobr`, both here and in the summary table (`-ity`, `-ic`, `-ly`) and in inquiry.json wherever endings appear.

## Polish
1. [Minor] The news texts (`inquiry.json`, both articles): a number is separated from its unit at a line break ("500 / mégawatts" at 390). French typography keeps them together. Fix: put a no-break space between number and unit (`500 mégawatts`, `50 mégawatts`, `22 minutes`, `130 élèves`). Optionally add `.nobr` on *États-Unis* and *Bouches-du-Rhône*, as the other units do.
2. [Minor] The true/false prompt: "(*vrai*) … (*faux*) … (*pas dans le texte*)" is untagged French. Fix: `{fr}…{/fr}`.
3. [Minor] The false-friends and summary tables at 390: the shared `td{hyphens:auto}` rule hyphenates English ("even-tually", "construc-tion site"). This is harmless.

## Checked
- Contact sheets 1–4. At full size: tutki-390-1 (the news text, with French spacing before `:` and `?` and `1 337` intact), the theory and false-friends table, and the matches and true/false at 390 and 1280.
- The hero at 390 and 1280: the columns are lines with no readable words, and nothing gives away a prediction.
- A word-break audit at 360, 390 and 1280. A targeted capture of the `-ité` break at 1280.
- All four model answers, opened after writing.
- No console errors, no `.katex-error`. The maths ($10^{9}$, $10^{12}$) renders.
- Hash unchanged at the end.

## Scores
illustrations 4 · typography 3 · English/French 4 · accessibility 4

## Shared issues (all four units)
- `templates/site.css:327` `th,td{hyphens:auto}` below 48 rem hyphenates English in table cells and leaves untagged French words exposed. The developer's proposed `[lang=fr]` exemption is good. Also consider `hyphens:manual` for `td:first-child`.
- `scripts/screenshot.py` makes no `fig-N` captures for course units, so the cadarache map and plan had to be captured by hand.
- `templates/inquiry.js`: the reflection list repeats "Commit now; the theory summary will show you" (known from the pilot).
