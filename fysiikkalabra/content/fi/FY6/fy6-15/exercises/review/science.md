VERDICT: PASS
CONTENT-HASH: c650c557cc001a60

## Blocking

## Polish
- exercises.json:333 (unchanged): "vikavirtasuoja laukeaa, kun maahan kulkeva virta ylittää 30 mA" is fine for the level; strictly it senses the L–N difference. Optional (carried from the previous report).

## Checked
- Delta: the L3-05 answer, part b, last sentences.
- The RCD as an additional protective device against electric shock: right.
- "a dangerous current can flow through a person while the RCD's trip limit is not exceeded" is right and fits the task's own data: week 7 gives 17,0 mA, over the 10 mA let-go limit, below 30 mA.
- The conclusion (protective earthing and insulation intact, no use of a faulty device) is right and agrees with the task's broken-PE premise.
- Recomputed: R_e limit = 230/0,030 − 1500 = 6167 Ω = 6,17 kΩ. Currents 0,26 / 1,89 / 5,54 / 17,0 / 41,8 mA for weeks 1–9. answers.py (6,167 kΩ, tol 0,02) and the unchanged Sijoitus and Järkevyys agree.
- The removed claim ("suojaa vasta, kun virta on lähellä kammiovärinän vaaraa") is no loss; the new wording is more exact.
- Hash identical at start and end.
