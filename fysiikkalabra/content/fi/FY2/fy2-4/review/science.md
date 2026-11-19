VERDICT: PASS
CONTENT-HASH: d1b8cf415123c2e3

## Blocking

## Polish
- None.

## Checked
- Delta review, round 2: three changes in inquiry.json.
- ennuste-1 prompt: the hint about the hot lamp and the hot exhaust pipe is removed. The physics is unchanged, and 25 % (15 kW useful, 45 kW losses of 60 kW) is still the only correct option. The 60 % distractor's feedback (24 kW losses) is right.
- ennuste-2 is now on the core path (no longer `optional`). Exactly one option is correct, and each feedback (E = P·t, so time cancels) is right physics.
- koe-2 question: the student now reads P_a from the sim's readout. The readout's `tehot` line shows P_a, and simState has `Pa`. With the lamp model's η = 0,05 at P_o = 40 W, the sim gives P_a = 2,0 W, so P_a : P_o = 5 %. This matches the correct option.
- koe-2 rows: the setup locks laite and P_o and varies only t. The slider runs 1–600 s, so the rows at 10 s and 20 s named in the feedback can be set. Recomputed values: E_o = 400 and 800 J, E_a = 20 and 40 J, ratio 5 % on every row.
- koe-2 is no longer `optional`. Its values and controlled variables are unchanged, so the experiment still isolates the varied parameter.
- Recomputed in one script with my own formulas: lamp and car rows at 10, 20 and 30 s. They agree with the feedback and with the johtopäätös model answer (600/150 kJ and 1200/300 kJ, 25 %).
- The content hash was the same at the start and the end.
