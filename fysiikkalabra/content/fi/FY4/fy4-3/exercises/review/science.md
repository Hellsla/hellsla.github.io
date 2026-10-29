VERDICT: PASS
CONTENT-HASH: b5022e34010aa2a4

## Blocking

## Polish
- solutions.md:62 — L2-01 gives $13{,}0\,\text{N}$ (three s.f.) while exercises.json answer is 13; harmless within tolerance, but make them the same.
- solutions.md (L1-04) — "newtonin tarkkuudella" for 620 N and 380 N is ambiguous (could be tens); "kymmenen newtonin tarkkuudella" matches L1-02 and siirto.

## Checked
- All 12 answers recomputed independently (18, 850, 90, 240, 6,38→6,4, 13, 65, 833,9→830, 8,94→8,9 kN, 0,27 kN up, 0,60, 1,9 N); answers.py agrees and uses the right model.
- First-law equilibria and third-law pairs correctly separated in every solution (L2-01 chain of pairs, L3-02 magnetic pair without contact, L3-03 stacked scales).
- Directions stated where asked (L3-01 drag up while moving down; L1-05 book pulls Earth upward).
- Solutions symbolic first, positive direction stated, force diagram described before the equation (rectangle, G from centre, N/T from the surface), velocity kept off the diagram.
- Rounding follows the limiting datum; reasonableness checks are real checks (tug-of-war won by ground friction, lift tension same at rest and constant speed).
- Notation: \overline{} vectors, \cdot, units in LaTeX.
