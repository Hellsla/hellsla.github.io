VERDICT: FAIL
CONTENT-HASH: 9b65aff5f585da33
Round: 1 (delta)

## Blocking
- [Major] fy2-5-L3-04 solution, Substitution — the 12-term monthly sum $2100 + 1900 + \dots + 2000 = 13\,300$ does not wrap at 390 px: in a render it is one line 638 px wide in a 302 px box, terms from $2\ldots$ on are cut off and only reachable by scrolling inside the box, with no cue — the student cannot see the whole sum on a phone (mathlayout breaks at the =, not inside the sum) — break the sum at meaningful points (e.g. by season, or a row per four months, or sum notation) so each row fits 300 px. Pre-existing and shared with fi; not introduced by this round's diff, but never visible before because the exercise captures exist only at 1280.

## Polish
- [Minor] L2-08 solution — the coal/first lines of the energy list are laid out inconsistently where a label and its formula share a line or break; harmless. (applies to fy2-5 only)
- [Minor] data tables — captions and the right-hand columns are cut at 390 px and scroll sideways (design rule, NOTES §1); header cells stay left of right-aligned numbers.

## Checked
- Render at 390 px (own Playwright, preview/en/fy2-5.html rebuilt for this check, all levels and solutions open): see Blocking for the clipped chain; no other chain clips, no page-level overflow (scrollWidth 390). Only the data-table headers exceed their box inside the scrolling .exp-table (by design).
- New L2-08 (ordering task, four short chains $E = H\cdot m$) opened as a card at 390 px: fits, order selectors usable. L2-01, L2-05, L2-07 (split task texts) only measured for overflow, cards not opened.
- Text only: solutions.md and exercises.json diffs (L2-08 choices and feedback, answers.py comment), wording, glossary use, number and unit LaTeX, decimal comma/point.
- From earlier captures (1280 px, already current for this hash): en fy2-3 open-exercises-L2-1280-9 (L2-08) opened. Contact sheets and the other 1280 captures not opened; fi-easy fy2-5 had no captures (its preview page was empty), so all of its judgement is from my own render.

## Scores
illustrations 4 · typography 3 · language 4 · accessibility 4
