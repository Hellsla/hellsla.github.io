VERDICT: PASS
CONTENT-HASH: 3129e7b116601f43
SCOPE: delta added-exercise from ad1ab6804b19c83a base 8f23aa7ae3bd

## Blocking
(none)

## Polish
- solutions.md fy6-14-L2-09 (Reasonableness) — compares with "the maximum power of the panel in the chapter (0.92 W)", but the task never says this is the chapter's panel (it is the same model in figures.py, so the number is right) — say "the maximum power of this panel, about 0.92 W near 5 V" or drop the chapter reference.

## Checked
- Delta: only the added exercise fy6-14-L2-09 judged; the rest unchanged per `reviews.py added_exercises`.
- Figure ex-kenno (figures.py, diode model M = 0.40 V, I_sc = 200 mA, U_oc = 6.0 V): recomputed I(4.0 V) = 198.7 mA, on the 200 mA gridline as read; I(3.9–4.1 V) = 198–199 mA, so the reading is robust; the curve's knee near 5 V, max power 0.918 W at 4.96 V (matches the 0.92 W quoted). The description matches the drawing and gives no power.
- Physics: the panel as a DC source at fixed irradiance, P = UI at the operating point given by the load voltage — correct; "irradiance stays the same" stated.
- Recomputed: P = 4.0 V · 0.200 A = 0.80 W (answers.py 0.8); the exact model value 0.795 W is 0.7 % off, inside the 4 % tolerance.
- Reasonableness checks valid: I_sc·U_oc = 1.2 W is an upper bound not reached; 0.80 W < P_max.
- Solution complete: graph reading described, formula, mA → A conversion, substitution with units, rounding reason (two figures, 50 mA grid).
- Scope: solar cell as a DC source, component level (FY6 central content).
