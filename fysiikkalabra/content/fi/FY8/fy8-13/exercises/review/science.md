VERDICT: PASS
CONTENT-HASH: 9867eda1ac6b16d0

## Blocking

## Polish
- exercises/exercises.json (fy8-13-L2-10): the round-1 note still applies. The graph's $d_{1/2} = 5{,}0\,\text{cm}$ differs from the lesson's "betonissa noin $4\,\text{cm}$" for Cs-137. A short clause saying the source is not cesium-137 (or that the concrete is different) would stop students reading it as a contradiction.

## Checked
- The hash 9867eda1ac6b16d0 was the same at the start and the end. I judged the diff: the L2-10 Järkevyys line (the L3-06 text and the answers.py comment were already judged in round 2).
- L2-10 Järkevyys: on the chord between (10 cm, 20) and (15 cm, 10), the value at 12 cm is $20 - \tfrac{2}{5}\cdot 10 = 16\,\mu\text{Sv/h}$. The exponential curve is convex, so it runs below the chord: $80 \cdot 0{,}5^{2{,}4} = 15{,}16\,\mu\text{Sv/h} < 16$. The new causal argument is correct, and the round-2 blocking item is fixed.
- "lähempänä $10\,\text{cm}$:ä" is correct (2 cm against 3 cm).
- Recomputed: L2-10 15,157 (answers.py 15,157166); L3-06 $80 \cdot 0{,}5^{4} = 5{,}0\,\mu\text{Sv/h}$, $t = 20/5{,}0 = 4{,}0\,\text{h}$. Both match answers.py.
