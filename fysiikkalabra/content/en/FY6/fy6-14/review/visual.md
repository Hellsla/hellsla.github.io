VERDICT: PASS
CONTENT-HASH: b979acdab1019426
Mode: light (teacher 2026-11-07, "kevyt katselmointi": the editorial-correction diff since origin/main only)

## Blocking
- none

## Polish
- 'a bulb limits its own current. The current of an LED must therefore be limited' — 'therefore' is a weak link; 'An LED, in contrast, does not limit its own current, so it must be limited' reads logically. Same in inquiry model.

## Checked
- Word-level diff since origin/main of the en fy6-14 lesson files and neighbouring text; decimal convention (point), number+unit in LaTeX, \cdot, no bold in task statements, no lesson ids; wording compared with the Finnish intent for the brief's items. figures.json aria texts: all lesson aria-labels equal the figures.json entries; wording (irradiance / back to the supply, fault arrow upwards) matches the lesson text; plain units in aria are acceptable. No screenshots (aria only). Irradiance defined once with symbol G and W/m^2; eta = P/(GA) unchanged; glossary/lang valo label consistent.
- Round 2 (git diff HEAD~1): inquiry model now says an LED "does not limit its own current in this way, so its current must be limited by the circuit"; the weak "therefore" is gone. No new issues.
