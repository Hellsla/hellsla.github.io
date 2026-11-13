VERDICT: PASS
CONTENT-HASH: 290ca9ff5936acc5
SCOPE: delta added-exercise from 52cd5fdc12763c25 base 611fb7d5c174

## Blocking
(none)

## Polish
- solutions.md fy2-4-L1-09 Annettu/Vastaus — the hint names the table *Polttoaineiden LHV-lämpöarvoja*, but the solution says "polttoaineiden lämpöarvot". — Fix: use the table's exact name in the solution as well.

## Checked
- Hash taken at the start and at the end with `--lang fi-easy`; it did not change.
- fy2-4-L1-09: E_o = Hm = 40,6 MJ/kg × 2,5 kg = 101,5 MJ, and η = 80/101,5 = 78,8 %. My recomputation, answers.py and exercises.json agree. The useful energy is the heat delivered to the house, and the input is the heating value times the mass, which fits the FY2 scope (E = Hm). The ±4 % tolerance covers neighbouring table values. The losses go out with the flue gases, which is the right mechanism.
- fy2-4-L2-09: in `fy2-4/grid`, H = 8 squares and η = 0,25, so the useful arrow is 2 squares and the loss arrow 6 squares. Then η = 2/8 = 25 %. Energy is conserved (2 + 6 = 8, and 60 J + 180 J = 240 J). The figure does not give the answer away. The arrow thickness is proportional to energy, as both the task and the description say.
- Compared with the reviewed Finnish: answer, unit, tolerance, figure, lookup, level and every number in the task text and the solution are identical. The added explanation of H and m is correct.
