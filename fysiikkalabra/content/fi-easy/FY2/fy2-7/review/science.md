VERDICT: PASS
CONTENT-HASH: 0c12449dd247c7d9

## Blocking
(none left; list what you fixed under Fixed)

## Fixed
- figures.json — values were shifted: the label "koti" held the storage-figure description and "potentiaali" held the energy-flow description, so the storage figure showed a whole paragraph as the "koti" label and the sankey figure as "potentiaali" label, while their aria-labels kept the dense Finnish → fixed the four values and redrew figures (scripts/figures.py fy2-7 --lang fi-easy); lesson.md figures now show "koti"/"potentiaali" and the simplified descriptions.

## Polish
- (none)

## Checked
- Translation review against the reviewed Finnish (teacher's decision 2026-10-28): lesson.md, inquiry.json, exit-ticket.json, meta.json and figures.json against content/fi: same physics, numbers, comma decimals, formulas, chapter references, source notes. check_i18n fi-easy: 0 errors.
- Update 2026-10-28 (physics audit + figures/assessment on main): translated and checked district-heating feedback (inquiry.json) and the grid-loss Reasonableness (solutions.md) against the new Finnish.
