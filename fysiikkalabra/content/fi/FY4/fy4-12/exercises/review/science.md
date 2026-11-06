VERDICT: PASS
CONTENT-HASH: bc0ea52e2d8d623c

## Blocking

## Polish
- solutions.md:199 (L2-08) — "x_A = 160 m − 64 m" skips the substitution. Insert "x_A = 20 m/s · 8,0 s + ½ · (−2,0 m/s²) · (8,0 s)²" first.
- solutions.md:207 (L2-08) — the "Kuvaajan lukeminen" block comes after the Mallivastaus. Elsewhere it comes before the calculation, so move it up.

## Checked
- New task L2-08 (Kuvaajan valinta), recomputed: v_A = 20 − 2,0t is 0 at 10 s and 12 m/s at 4,0 s. Meeting: 20t − t² = 12t gives t = 8,0 s, before the car stops, with x = 96 m for both.
- Option figures in figures.py match their descriptions: pick-kaari (v = 20 − 0,2t², 15 m/s at 5 s, crossing at √40 ≈ 6,3 s), pick-kohtaus (20 − t, crossing at 8 s, 10 m/s at 10 s) and pick-alku (12 → 0 at 6 s, then 0). Each description is complete: axes, grid and every value.
- The distractors catch the lesson's warned mistakes: the (t, v) crossing read as the meeting (2), the same place read as the same speed (4), and the curved shape of a (t, x) graph (1). Exactly one option is right.
- Sign convention: a = −2,0 m/s² with positive along the motion, as in the brief. The task stays within fy4-1, fy4-2 and fy4-12.
- The options can't be told apart by form ("Kuvaaja 1–4"). The correct feedback states the lines without hinting at a reason stage.
- Guardrail higher-line-ahead: not touched, since only (t, v) graphs appear.
- Inline formulas are split with "eli". I checked them and the figures from the text and code only, with no render (no screenshots yet).
- answers.py comment agrees; the rest of the set is unchanged since the PASS. Hash is the same at the start and at the end.
