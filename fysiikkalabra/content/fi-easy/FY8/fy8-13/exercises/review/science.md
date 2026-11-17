VERDICT: FAIL
CONTENT-HASH: 682ce6a6709579a6

## Blocking
- exercises/solutions.md:313 (L2-10 Järkevyys) — **A, wrong causal reasoning.** The text says "kuvaaja on kupera, joten arvo on hieman välin keskikohdan (15 µSv/h) yläpuolella". Convexity pushes the value the other way. A convex curve runs below its chord: the chord gives 16 at 12 cm and the curve gives 15,16. At 12,5 cm the curve gives 14,1, below 15. The value is above 15 only because 12 cm is nearer to 10 cm than to 15 cm — fix: "Paksuus $12\,\text{cm}$ on lähempänä $10\,\text{cm}$:ä. Jos arvo luettaisiin suoraan välistä, se olisi $16\,\mu\text{Sv/h}$. Kupera kuvaaja kulkee tämän suoran alapuolella, joten arvo on vähän alle $16\,\mu\text{Sv/h}$. Tulos $15\,\mu\text{Sv/h}$ on järkevä."

## Polish

## Checked
- The hash 682ce6a6709579a6 was the same at the start and the end. I judged the diff: the L3-06 wording, the L2-10 Järkevyys line and the answers.py comment.
- L3-06: "Mittaus on tehty samalla etäisyydellä lähteestä kuin työpiste on" makes the graph apply at the workstation, so the reading at $d = 20\,\text{cm}$ is valid.
- I recomputed L3-06: $5{,}0\,\mu\text{Sv/h}$ and $4{,}0\,\text{h}$; c) $2{,}5\,\mu\text{Sv/h}$, which gives $25{,}0\,\text{cm}$. This matches answers.py.
- I recomputed L2-10: $80 \cdot 0{,}5^{2{,}4} = 15{,}157\,\mu\text{Sv/h}$. answers.py gives 15,157166, and its comment now says 15,16.
- The changed lines are the same as in the fi version, and so is the error.
