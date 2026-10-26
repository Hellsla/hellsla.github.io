VERDICT: PASS
CONTENT-HASH: e282dfdc8e6d6106

## Blocking

## Polish
- sim.js:241 — the `tx` helper still carries a stray trailing comment "three significant figures" (it formats with fixed decimals) — delete it.

## Checked
- Diff since cb4b8f4: exp-1 `min` 2 → 3 (matches the intro's three volumes 50, 25, 100 ml); conclusion prompt, model answer and a new criterion on 1/V; check-2 no longer optional.
- New model numbers: 1/V = 1/50, 1/25, 1/100 ml⁻¹ = 0,020; 0,040; 0,010 ml⁻¹ correct; with p = 100, 200, 50 kPa the (1/V, p) points lie on a line through the origin with slope pV = 5000 kPa·ml = 5,0 J, as stated.
- The new criterion matches the lesson's (1/V, p) figure and theory; scope unchanged (Boyle's law verification is a FY3 kokeellisuus item).
- check-2 now core: p = k/V = 3,6 kPa·l / 0,030 l = 120 kPa; mistakes 108 (k·V in ml) and 0,12 (V left in ml) correct; solution symbolic first; 3,6 J magnitude realistic.
- Everything else (answers.py, exercises, figures, sim.js, other inquiry steps) unchanged since round 1, whose recomputations still hold.
- Hash identical at start and end.
