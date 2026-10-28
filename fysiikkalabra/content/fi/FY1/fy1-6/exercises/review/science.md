VERDICT: PASS
CONTENT-HASH: c049419582c3b6e6

## Blocking

## Polish
- solutions.md:67 (L2-02) — "**Muunnokset:** sijoitetaan" starts lower-case; style only.
- solutions.md:90 (L2-04 Järkevyys) — divisions written as operations use `\dfrac` ("pelkällä jakolaskulla 9,7 m/s / 1,0 s"); the colon rule would give $9{,}7\,\text{m/s} : 1{,}0\,\text{s}$.
- solutions.md:19 (L1-02 Järkevyys) — "0,80 · 9,81 ≈ 8" repeats the substitution; an independent bound (under 1 s → under 9,81 m/s) is already there, drop the repeat.
- lessons/FY1/fy1-6/answers.py:17 — code uses `54.0 / 3.6`; not student-facing.

## Checked
- Round-3 change, solutions.md:67 (L2-02): 54,0 · 1000 m : 3600 s = 15,0 m/s, t = 15,0 : 9,81 = 1,529 → 1,53 s (3 s.f. from 54,0); ½gt² ≈ 11,5 m ≈ fourth floor, plausible.
- answers.py reproduces all 12, recomputed: 29,43; 7,848; 6,48; 9,8; 22,26; 1,223; 1,529; 26,715; 9,8; 1,0; 8,108; 4,43; tolerances 2 % cover the rounded answers.
- m/s → km/h estimates: 29,43 → 106 km/h, 7,8 → 28 km/h — correct.
- L2-03 Δv = gΔt from non-rest start; L2-04 slope from two non-zero points; L3-02 g = 3,70 m/s² then t₂ = 8,1 s (limited by 4,0 s); L3-03 4,4 m/s by the decimal rule, 15 % — all right.
- Scope: v = gt as a linear model, Moon/Mars g given in the tasks, no forces.
- Notation: \cdot products, no ×/\times.
- Hash identical at start and end.
