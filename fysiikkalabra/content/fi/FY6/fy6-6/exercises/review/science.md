VERDICT: PASS
CONTENT-HASH: 3e04d8b6c8dc818b
Round: 2. Checked the round-1 Blocking fix and the diff since 00b2dcb54 (L1-06 options, new L1-07, L2-05 Periaate, rounding lines in L2-06, L3-04 and L3-05, L3-05 safety sentence, answers.py L1-07).

## Blocking

## Polish
- exercises.json:75 (fy6-6-L1-07) — the new task (LED strip, P = UI, mA → A) is the same method as L1-01 (USB charger, P = UI) with one conversion added. The plan's level-1 item "suurin sallittu virta vastukselle, jonka nimellisteho on 0,25 W" has left the set, and L2-03 holds only its voltage version. Update the plan, or make L1-07 a different level-1 model, for example P = U²/R or E = Pt with a unit trap.
- solutions.md:135 (fy6-6-L1-07 Vastaus) — "kaksi merkitsevää numeroa kuten jännitteessä" is right, but 350 mA (two or three significant figures) should also be named as the limiting datum, or written 0,35 A.

## Checked
- Hash 3e04d8b6c8dc818b at start and end.
- Round-1 Blocking L2-05 is resolved: the Periaate now states the condition (heat flow to the air about proportional to ΔT, small ΔT), and the origin follows from P = 0 → ΔT = 0.
- The L3-05 Vastaus now says "jäähtyy huonosti" and adds the unrolling and rated-current safety clause. That is correct.
- L1-07: 12 V · 0,350 A = 4,2 W, equal to answers.py and exercises.json (unit W). The reasonableness check (4200 W without conversion) is a real check.
- answers.py was recomputed and compared with every numeric answer; all agree (L2-05 12,1 K/W; L2-06 172 %; L3-04 822 W; L3-05 152,5 W).
- L1-06 reworded: one correct option, at position 2, and `answer` equals its text. Every distractor is wrong: two are the parallel-connection reasoning, and "teho riippuu vain virrasta" is wrong too. All feedback is right.
- L3-04 now uses R₁ = 48,09 Ω throughout. It gives the resistances in the Vastaus and notes that the 1780 W row only checks the result.
- The Sijoitus line and the Vastaus now agree (172 % / 1,7·10² %, 822 W, 152,5 W), with the rounding stated.
- The L2-07 quotation marks changed only; the physics is unchanged.
