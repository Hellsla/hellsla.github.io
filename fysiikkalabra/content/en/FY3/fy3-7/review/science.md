VERDICT: PASS
CONTENT-HASH: d7fea6532513f83e

## Blocking

## Polish
- lesson.md heating-curve figure — the horizontal parts are much shorter than to scale (at the drawn Q scale melting would be about 96 px and boiling about 650 px; drawn 36 and 186), so the picture undersells "more than five times as much as heating water". Only the aria-label says they are not to scale — add a small visible note "horizontal parts not to scale", or lengthen the boiling part.
- inquiry.json check-2 solution, Reasonableness — 180 kJ would warm the 0.597 kg that boiled away by about 72 K, so it started at about 28 °C, not 20 °C. "Same order of magnitude" holds, but the check would be sharper if it used the mass it just found.
- sim.js:865 (code comment) — "the energy breaks the bonds between particles" contradicts the guardrail wording the student sees ("changes the interactions … increases the interaction energy"). Reword it when the file is next edited (not student-facing).
- lesson.md Formula paragraph — "At constant pressure the temperature does not change during a change of state" leaves out "pure substance", which Key idea and Summary both state. Add it for consistency (C, not blocking).

## Checked
- One script recomputed every number from the task data: r/s = 6.77, r/(c·100 K) = 5.39, s/c = 79.7 K, worked example 2 343 750 J/kg (+3.7 %, Δm = 133 g), pr-lampo 210/2.1/419 kJ, 66.8 kJ, siirto 188 W (mistakes 27.8 and 11 300), check-2 0.597 kg (mistakes 0.677 and 4.04, 0.54 kg), check-3 264 J and a ratio of 9.6. All agree.
- Plateau durations in pred-1, pred-2, the conclusion and the sim (sm/P, rm/P: 1130/565 s, 83.5/167 s) match the sim's computed values. exp-1 locks m and varies P, exp-2 locks P and varies m, and simState carries tMelt and tBoil.
- Each prediction and check has exactly one correct option, and every distractor's feedback names the right mechanism (interaction energy, no change in mean kinetic energy, molecules intact).
- The worked example solves symbolically first, the significant figures are justified by 128 g, and the loss argument gives the right sign (losses → r too large).
- Sim model: the piecewise T(Q) is correct with the stated c, s and r values. The piston at 101 kPa explains the 100 °C plateau and c_p for steam, and its limits (open pan, rigid vessel) are stated in the model box. The 1280 px capture matches the readout.
- Heating-curve slopes: ice and steam are 2.0× as steep as water (c ratios 2.0 and 2.1), as stated.
- Phase diagram: the melting curve has a negative slope (correct for water), and the lower pressure on the mountain gives a lower boiling point.
- The guardrail conditions (pure substance, constant pressure) are stated in Key idea, Summary, pred-3 and the contribution. The pΔV work (about 170 kJ/kg, 7 % of r) matches "a small part". The volume ratio of 1700 is right.
- Scope: changes of state, the phase diagram and the r measurement are all within FY3's central contents and the slot.
