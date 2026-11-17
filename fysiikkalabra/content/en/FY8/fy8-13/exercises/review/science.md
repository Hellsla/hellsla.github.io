VERDICT: FAIL
CONTENT-HASH: 4cb2f271025ee493

## Blocking
- exercises/solutions.md:313 (L2-10 Reasonableness) — **A, wrong causal reasoning.** The text says "the curve is convex, so the value is slightly above the midpoint (15 µSv/h)". Convexity pushes the value the other way. A convex curve runs below its chord: the chord gives 16 µSv/h at 12 cm and the curve gives 15.16. At the thickness midpoint 12.5 cm the curve gives 14.1, below 15. The value is above 15 only because 12 cm is nearer to 10 cm than to 15 cm — fix: "The thickness $12\,\text{cm}$ is closer to $10\,\text{cm}$, so reading straight across the interval would give $16\,\mu\text{Sv/h}$; the convex curve runs below that straight line, so the value is slightly under $16\,\mu\text{Sv/h}$, and the result $15\,\mu\text{Sv/h}$ is reasonable."

## Polish
- exercises/exercises.json (fy8-13-L2-10) — the round-1 note still applies: $d_{1/2} = 5.0\,\text{cm}$ differs from the lesson's Cs-137 value for concrete (about 4 cm). A short clause saying the source is not Cs-137 would stop students seeing a contradiction.

## Checked
- The hash 4cb2f271025ee493 was the same at the start and the end. I judged the diff: the L3-06 wording, the L2-10 Reasonableness line and the answers.py comment.
- L3-06: "when the distance from the source is the same as at the workstation" makes the graph apply at the workstation, so the reading at $d = 20\,\text{cm}$ is valid.
- I recomputed L3-06: $5.0\,\mu\text{Sv/h}$ and $4.0\,\text{h}$; c) $2.5\,\mu\text{Sv/h}$, which gives $25.0\,\text{cm}$. This matches answers.py.
- I recomputed L2-10: $80 \cdot 0.5^{2.4} = 15.157\,\mu\text{Sv/h}$. answers.py gives 15.157166, and its comment now says 15,16.
- The numbers and the wording of the changed lines are the same as in the fi version, and so is the error.
