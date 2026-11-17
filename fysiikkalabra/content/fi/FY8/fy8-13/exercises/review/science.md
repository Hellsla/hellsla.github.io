VERDICT: FAIL
CONTENT-HASH: 091ea2e04bc9147d

## Blocking
- exercises/solutions.md:313 (L2-10 Järkevyys) — **A, wrong causal reasoning.** The text says "kuvaaja on kupera, joten arvo on hieman välin keskikohdan (15 µSv/h) yläpuolella". Convexity pushes the value the other way. A convex curve runs below its chord: the chord gives 16 µSv/h at 12 cm and the curve gives 15,16. At the thickness midpoint 12,5 cm the curve gives 14,1, below 15. The value at 12 cm is above 15 only because 12 cm is nearer to 10 cm than to 15 cm. The check reaches the right number by a wrong argument and teaches a wrong idea of what convexity does — fix: "Paksuus $12\,\text{cm}$ on lähempänä $10\,\text{cm}$:ä, joten suoraan välistä luettuna arvo olisi $16\,\mu\text{Sv/h}$; kupera kuvaaja kulkee tämän suoran alapuolella, joten arvo on hieman alle $16\,\mu\text{Sv/h}$, ja tulos $15\,\mu\text{Sv/h}$ on järkevä."

## Polish
- exercises/exercises.json (fy8-13-L2-10) — the round-1 note still applies: $d_{1/2} = 5{,}0\,\text{cm}$ differs from the lesson's "betonissa noin $4\,\text{cm}$" for Cs-137. A short clause saying the source is not cesium-137 would stop students reading it as a contradiction.

## Checked
- The hash 091ea2e04bc9147d was the same at the start and the end. I judged the diff: the L3-06 wording, the L2-10 Järkevyys line and the answers.py comment.
- L3-06 text: "kun etäisyys lähteestä on sama kuin työpisteessä" now says clearly that the graph's curve applies at the workstation's distance, so reading off the value at $d = 20\,\text{cm}$ is valid.
- I recomputed L3-06: $80/16 = 5{,}0\,\mu\text{Sv/h}$, $t = 4{,}0\,\text{h}$; c) $2{,}5\,\mu\text{Sv/h}$, which gives $25{,}0\,\text{cm}$. This matches answers.py (4,0).
- I recomputed L2-10: $80 \cdot 0{,}5^{2{,}4} = 15{,}157\,\mu\text{Sv/h}$. answers.py gives 15,157166, and its comment now correctly says 15,16 (the round-1 polish item is done).
- The new Järkevyys bracket 10…20 µSv/h is right; only the convexity inference is wrong (above).
