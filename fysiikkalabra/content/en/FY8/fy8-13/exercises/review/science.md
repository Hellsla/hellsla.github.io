VERDICT: PASS
CONTENT-HASH: a5c6089260b9a4af

## Blocking

## Polish
- exercises/exercises.json (fy8-13-L2-10): the round-1 note still applies. The graph's $d_{1/2} = 5.0\,\text{cm}$ differs from the lesson's Cs-137 value for concrete (about 4 cm). A short clause saying the source is not Cs-137 would stop students seeing a contradiction.

## Checked
- The hash a5c6089260b9a4af was the same at the start and the end. I judged the diff: the L2-10 Reasonableness line (the L3-06 text and the answers.py comment were already judged in round 2).
- L2-10 Reasonableness: on the chord between (10 cm, 20) and (15 cm, 10), the value at 12 cm is $16\,\mu\text{Sv/h}$. The convex exponential curve runs below the chord: $80 \cdot 0.5^{2.4} = 15.16\,\mu\text{Sv/h} < 16$. The reasoning is now correct, and the round-2 blocking item is fixed.
- "closer to $10\,\text{cm}$" is correct (2 cm against 3 cm).
- Recomputed: L2-10 15.157 (answers.py 15.157166); L3-06 $5.0\,\mu\text{Sv/h}$, $t = 4.0\,\text{h}$. Both match answers.py.
- The changed lines have the same numbers and argument as the fi version.
