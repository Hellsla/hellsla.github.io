VERDICT: PASS
CONTENT-HASH: a079620513e19e92

## Blocking
(none) The earlier blocking finding is resolved. The tritium task's mistake feedback now reads "the mass of a deuterium nucleus and a tritium nucleus together". I checked it in the browser with the answer 93.5, and no asterisks are left.

## Polish
1. [Minor] Fuel-cycle figure (`selita-390-2`). It is much better: the n arrow is teal and ends inside the blanket, and the nuclei have Z. The "D" label still touches the deuterium arrow near the water box. Move it about 10 units up and left.
2. [Minor] Roles and compare tables at 390. "in electric-ity (2025)" still hyphenates in a narrow cell. Write "share of electricity (2025)" on two lines, or see the shared table note.
3. [Minor] *Evaluate: result, plan or claim?* The lead and the component prompt still repeat each other ("All nine statements … decide what kind" and then "Sort each statement: is it …"). Keep one of them.
4. [Minor] The sort items now use LaTeX ($3.15\ \text{MJ}$, $1337\ \text{s}$), but the select's aria-label still carries the raw `$…\text{MJ}$` to screen readers. See Shared issues.

## Checked
- Fresh captures for this hash. At 390: tutki-390-2 and 4 (table with footnote, sort items), selita-390-2 (cycle figure, compare table), plus the contact sheets for the remaining 390 and 1280 stages.
- Opened myself at 390 and 1280:
  - the whole worked example, where the Formula rows are now spaced and the substitution shows 3.3747;
  - the tritium task with the wrong-answer feedback, its hints and the closed solution;
  - all 4 model answers after writing, and all 7 choices with their feedback.
- No `.katex-error`, no raw `$` or `*`, no overflow and no console errors. The hash was unchanged at the end.

## Scores
illustrations 4 · typography 4 · English/French 4 · accessibility 4

## Shared issues
- `assets/units/fy14/fx/match.js`: the select aria-label strips only `{fr}` and `*`. Strip `$` and `\text{…}` as well.
- `templates/inquiry.js` §4: numeric mistake feedback is set with `textContent`, so Markdown never renders. This unit no longer needs Markdown there.
- `scripts/inquiry.py`: the numeric input's `aria-label="Answer in $\text{kg}$"` is raw LaTeX.
- Narrow table cells at 390 hyphenate automatically. Consider `hyphens: manual` on `td`.
