VERDICT: PASS
CONTENT-HASH: 309a5b315853626c

## Blocking

## Polish
- content/fi/FY1/fy1-1/exercises/exercises.json:228 (L2-07) — the task says "pisteet asettuvat suoralle". Measured points lie on the line only approximately; the residuals here are −0,28…+0,31 mm. — Write "asettuvat likimain suoralle", in line with the fits guardrail.
- content/fi/FY1/fy1-1/exercises/exercises.json:65 (L1-06) — the distractor "Malli on teoria, jota ei voi enää muuttaa" mixes up model and theory. The feedback refutes "unchangeable" correctly but leaves "a model is a theory" unanswered. — Add half a sentence: a theory too stays open to revision.

## Checked
- Round 3 diff (`git diff HEAD~1 -- content/fi/FY1`): only solutions.md:183 (L3-04 Kaava) changed, from one line with \quad separators to three formulas joined by commas and "ja".
- L3-04 formulas are unchanged: V_sade = hA, V_pisara = (4/3)πr³, N = V_sade/V_pisara. Recomputed: h = 8,33·10⁻⁴ m, V_sade = 5,0 m³, V_pisara = 4,19·10⁻⁹ m³, N = 1,19·10⁹. A 20 % larger diameter gives −42 %, so the answer and the sensitivity still hold.
- Everything else is unchanged since round 2 (PASS). The round-2 checks still apply: L2-07 fit and uncertainty, L2-05 scale model, L1-06 options, L3-05, and all 19 numeric answers against answers.py.
- The hash was the same at the start and the end.
