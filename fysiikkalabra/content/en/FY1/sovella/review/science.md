VERDICT: PASS
CONTENT-HASH: c919622651d8c685

## Blocking
(none left)

## Fixed
- tasks.json fy1-s2 report (Hypothesis) — "gravity pulls it more" → "gravity pulls on it more" (same naive claim, correct phrasing)
- solutions.md:79 — "it tells nothing about the precision" → "it says nothing about the precision"

## Polish
- Figure alt text (Finnish source key) says "first three points" are from the ramp; the figure and model answer have two. Inherited from the Finnish figures.py (noted in the Finnish science review); fix there, then regenerate.

## Checked
- Translation review against the reviewed Finnish (teacher's decision 2026-10-28): compared tasks.json (intro, all 3 tasks, every part text, rubric criterion and detail, source notes), solutions.md (all parts of fy1-s1 and fy1-s2, Yleisiä virheitä, Hyväksytään myös) and figures.json (alt text, ramp label) line by line with content/fi/FY1/sovella.
- Physics meaning matches: floor points t ≥ 0.4 s / 0.6 s, slope 0.80 m/s, negative intercept explained (ramp slower → line crosses s-axis below the origin), extrapolation 1.6 s → 10 s, means 2.37 / 2.40 s, ±0.08 / ±0.07 s, difference 0.03 s, conclusion scoped to solid same-size balls on this ramp.
- Decimal points, \cdot/`:` notation, units in prose, step labels (Given/Find/Principle/Graph/Reading the graph/Formula/Conversions/Substitution/Answer/Reasonableness/Model answer), chapter title for fy1-8 matches content/en/courses.json. practice.py check: OK en/FY1; check_i18n en: 0 errors.
- Update 2026-10-28 (physics audit + figures/assessment on main): translated and checked the Sovella tasks.json texts and criteria (uncertainty estimate wording), solutions.md (precision principle, uncertainty estimate and conclusion in fy1-s2, extrapolation answer) and the graph description
