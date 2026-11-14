VERDICT: PASS
CONTENT-HASH: 34b802bc7a3c2838
SCOPE: delta added-exercise from 11d7d1d54e3ae477 base 81db4a6fd727

## Blocking

## Polish
- solutions.md (L2-09, Answer) — the reason "as in the speed 1540 m/s" for the rounding does not name the limiting datum. That is the time read from the figure, 90 µs, which can be read to about ±1 µs (about 1 %). — Justify the three figures by the reading precision.
- exercises.json (L2-09 and L1-01) — the calculation is almost the same: L1-01 gives the echo at 91.0 µs (7.01 cm), and L2-09 reads 90 µs from the figure (6.93 cm). L2-09 adds the graph reading, so it is not a repeat.

## Checked
- The hash was the same at the start and the end. Round 5: I reviewed the changed exercise L2-09.
- L2-09: d = vt/2 = 1540·90·10⁻⁶/2 m = 6.93 cm, as in answers.py and the Finnish version. Readings of 89 µs and 91 µs give 6.85 cm and 7.01 cm, so a reading within ±1 µs stays inside the 2 % tolerance.
- The figure, its description and the solution all put echo C at 90 µs. The figure gives no depths, so it does not give the answer away.
- Repetition: the inquiry check on this figure asks for the B–C layer (3.08 cm), and L2-05 uses a table. No other task asks for the depth of the bone surface.
- The answer, unit and tolerance of every exercise are the same as in the Finnish set. The numbers in the English solutions of L1-09 (14.0 m) and L2-09 are the same as the Finnish ones.
