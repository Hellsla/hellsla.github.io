VERDICT: PASS
CONTENT-HASH: eec42dc6115fb05b
Mode: light (teacher 2026-11-07, "kevyt katselmointi": round-2 diff since edb368de4 only)

## Blocking
- none

## Polish
- Worked example: A = (0 min; 20 °C) and B = (5,0 min; 60 °C) mix exact-style and one-decimal notation (0 min next to 5,0 min). The result k = 8,0 °C/min, t = 2,5 min is still right; writing 0,0 min would be cleaner.

## Checked
- diff lesson.md (model-type sentence, interpolation and extrapolation, example numbers), inquiry.json (cart pushed at t = 0 then uniform; cyclist clock started late: explains the 5 km intercept; figure colours), exit-ticket/meta unchanged.
- Recomputed: (60 − 20)/(5,0 − 0) = 8,0; b = 20 °C; (40 − 20)/8,0 = 2,5 min. Cart data 0,6…2,9 m at 1…6 s fit a line through the origin of about 0,49 m/s, which agrees with the new setup sentence.
