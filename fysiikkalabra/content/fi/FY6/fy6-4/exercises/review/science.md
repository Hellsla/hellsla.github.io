VERDICT: PASS
CONTENT-HASH: d4f5d2f5f70c4e20

## Blocking

## Polish
- lessons/FY6/fy6-4/figures.py:228 — carried over from the last round: the task-mixed figure (L3-01) still draws node dots at (xa, ym) and (R, T), which are corners where nothing branches, so they look like junctions. This is harmless to the physics. Fix: drop `node(f, xa, ym)` and `node(f, R, T)` so only the real junctions (xa, T) and (R, ym) carry dots.

## Checked
- solutions.md:34 (L1, series lamps): "energia muuttuu lampuissa valoksi ja hehkulankojen sisäenergiaksi" is right by the heat guardrail (the filament has internal energy, not heat). It matches the lesson's wording ("sisäenergiaksi, ja lampussa myös valoksi"), and the light/internal-energy split is a fair simplification (C).
- The principle still justifies U = U1 + U2 (each charge passes both lamps). No number, symbol, answer or tolerance changed, so the earlier recomputation of all 12 answers still holds.
