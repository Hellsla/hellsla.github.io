VERDICT: PASS
CONTENT-HASH: 99fba7d73147c1cf

## Blocking
(none)

## Polish
- inquiry.json check-3 model answer — "Lopulta pallon mekaaninen energia on kokonaan muuttunut lämpöenergiaksi" leaves out sound and vibration, which the data item excludes explicitly; add "(ääni ja värähtely jätetään huomiotta)" or "lähes kokonaan".
- inquiry.json check-2 — an incandescent lamp's non-visible output is largely infrared radiation; the solution says part leaves as thermal radiation, the task says "loppu muuttuu lämpöenergiaksi". Acceptable at this level (C), could say "lämpöenergiaksi ja infrapunasäteilyksi".
- sim model — friction is a constant force mu m g along the track (normal force not varied on the curve); stated in sim-spec and in the model box ("yhtä paljon per liukumetri"), a fair simplification (C).

## Checked
- Example: 840 J - 720 J = 120 J, unit conversion, rounding to tens, "alle viidesosa" (14 %) all correct.
- Figure "sailyminen" caption: 800 + 0 + 0, 300+450+50, 0+700+100 all sum to 800 J.
- Recomputed the sim independently (own RK4, 0,5 ms): no friction t=1/2/3 s gives Ep/Ek 63/918, 862/119, 424/557 J; mu=0,04 gives mech 469 J at 8 s (Eth 512) and 143 J at 16 s (Eth 838); matches inquiry.json model answer and feedback. m g h0 = 981 J.
- Pred-1 and pred-2: exactly one correct option, every distractor wrong, feedback physics correct.
- Exp-1 and exp-2 setups lock friction and h0, vary t; simState has Ep, Ek, Eth, Ekok.
- Data item 0,60-0,31 = 0,29 J; per-bounce 0,12/0,10/0,07 correct; cyclist 335 kJ; bulb 2380 J; exit ticket 3,8 kJ.
- Heat vs thermal energy wording matches guardrails (net transfer, body has thermal energy).
- Scope: no E_k/E_p formulas in the lesson text; consistent with FY2 scope.
- Summary, goals, options, exit ticket and sim boxes agree.
- Delta: the opening question now reads "Miksi pomppiva pallo pysähtyy lopulta lattialle?"; the clause that gave away the answer is gone, no physics claim changed.
- Delta 2 (option rebalancing, pred-2, exp-1, virhe): correct options still right, same one correct; distractors still wrong for the reason their feedback gives; feedback matches.
