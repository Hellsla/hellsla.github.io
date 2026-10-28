VERDICT: PASS
CONTENT-HASH: d429e7d288d64404

## Blocking

## Polish
- exit-ticket.json:12 (answer 3) — The answer uses $t = 24\,\text{h}$ without showing that one vuorokausi is 24 h. — Write $t = 1\,\text{vrk} = 24\,\text{h}$ in the chain.
- lesson.md:283 vs inquiry.json (prior) — The text writes $P = \tfrac{E}{t}$, but the prior-knowledge list writes $P = \Delta E : \Delta t$. — Use one form in both places.
- inquiry.json (hook) — "satoja kilovoltteja" does not fit the 110 kV lines well. — Write "110–400 kilovolttia", as the lesson text does.

## Checked
- Round 7, full review. The only change since the last PASS is the Sijoitus row "(245 − 222,95) MWh" (lesson.md:322). It is correct: 245 − 222,95 = 22,05 MWh, the unit is applied to the whole difference, and the next row follows from it.
- One script recomputed every number from the task data, and all 24 keys match lesson-answers.py. Worked example: 222,95 → 223 MWh and 22,05 → 22 MWh. kl: 9,17 → 9,2 %. siirto: 15 %. tarkistus-2: 500 MWh. Exit ticket: 768 MWh and 48 kWh.
- Every mistake value lies outside its tolerance: 10,1 and 3,3; 85 and 17,6; 281 and 469. Each exact answer lies inside.
- The "jannite" model table is consistent with $P_\text{häviö} = (P/U)^2R$ for R = 3,2 Ω: 0,80, 0,026 and 0,0020 MW, or 8,0 %, 0,26 % and 0,020 %. It is marked as model values and the formula is not shown, so it stays in FY2 scope.
- The statistics: 83 TWh with about 4 % losses (about 3,3 TWh), and 36,0 → 32,7 TWh of district heat (marked as an estimate). The "sahko" conclusion holds.
- The Sankey diagram is to scale: 77 + 3 and 73 + 7 out of 80 px. The grid voltages, the district-heating flow directions and the storage figure are correct.
- Every correct option and every feedback is physically right. Energy is conserved throughout, and losses go to heat in the surroundings.
- The worked example is solved symbolically first, its rounding is justified (three figures, and two from 9,0 %), and its reasonableness check is real. The misconception section is correct ($245 : 0{,}910$).
- Scope: there is no FY3 content (no $P = I^2R$, $Q = cm\Delta T$, U-value or chain product).
- The content hash was the same at the start and at the end.
