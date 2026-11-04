VERDICT: PASS
CONTENT-HASH: 5c03f04960bafc0e

## Blocking

## Polish
- lesson.md:3, inquiry.json:19 — "seinään, jossa ei ole sähkövarausta" (round 1, unchanged) — "joka on sähköisesti neutraali".

## Checked
- Round 3 (diff HEAD~1..HEAD): only the Esimerkki substitution is split into two aligned rows (k on one row, the fraction, prefixed by \quad \cdot, on the next); the product, values, units and result 2,397·10⁻⁴ N are unchanged and still correct.
- Round 2: k = 8,988·10⁹ in lesson.md:395/:523, inquiry.json calc, virhe, siirto, tarkistus-2, sim.js, lesson-answers.py, figures.py, sim-spec.md, glossary — round-1 blocking item resolved.
- Re-quoted model readings verified against the sim's formatting with k = 8,988·10⁹: 3,995 mN → "3,99 mN" at 3,0 cm, 0,9987 → "0,999", 0,2497 → "0,250", 1,9973 → "2,00" mN; koe-1 ratio 3,99 : 0,250 ≈ 16 (answer 16, tolerance 2 %).
- Unchanged quotes still right: Esimerkki 2,397·10⁻⁴ N, kuvaaja 4,0/1,0/0,44/0,25 mN, check-graph 8,99 mN at 3 cm and 1,0 mN at 9 cm, tarkistus-2 F/k = 1,001·10⁻¹² → 30,0 nC, siirto 9,227·10⁻⁴ N (answer 0,923 within tolerance).
- lesson.md:327 and the field-line caption now say "testivaraus", as fy6-11 and the glossary — resolved.
- lesson-answers.py virhe-ilman-nelio now computes the displayed 1,1·10⁻⁷ N (r = 2,0 unsquared).
- No new physics introduced by the diff; sim behaviour otherwise unchanged (only K).
