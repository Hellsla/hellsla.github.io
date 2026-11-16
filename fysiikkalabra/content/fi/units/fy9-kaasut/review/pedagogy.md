VERDICT: PASS
CONTENT-HASH: 84089ae446eb257f
Round 2: delta against the version round 1 reviewed (fix round 1).

## Blocking
- (none)

## Polish
- A (carried from round 1), s7 d repeats the idea of s2 c; a cross-reference in the solution would turn it into revision.
- C (carried), `tasks.json` intro: "Ratkaise ne kuten kokeessa" follows the sentence about the last task, so "ne" points the wrong way.

## Checked
- `solutions.md` s2 c, added sentence: 485,1 − 174,6 − 232,9 = 77,6 kW and 485 − 175 − 233 = 77 kW, both recomputed; 77,6/485,1 = 16 %. The sentence explains the difference between the displayed row and the unrounded value without confusing the 16 % conclusion.
- `solutions.md` s5 common mistake: with 311 kPa the amount of substance is 1,48 times too large, so the molar mass is 210/311 = 0,68 of the right one. "moolimassaksi tulee noin kaksi kolmasosaa oikeasta" now names the quantity; the old "tulos" was ambiguous.
- `solutions.md` s7 e: "noin 21 °C" now agrees with c (10 °C + 11 K, line 573).
- `tasks.json` s7 c part text: the formula name is no longer given in the prompt, which suits an application task. "veteen aikayksikössä siirtyvä lämpö eli lämpöteho" and "sekunnissa virtaavan veden tilavuus" give a student what the derivation needs; the equation criterion and the solution (Q = cmΔT, m = ρV, Q = P₂t) still match the instruction "Johda symbolein". The situation is first, the three questions follow in the order of the criteria.
- `answers.py`: only an added check value; no content effect.
