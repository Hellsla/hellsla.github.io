VERDICT: PASS
CONTENT-HASH: 0e0f5d73568bcfbf

## Blocking

## Polish
- lesson.md (Ydinajatus) — "kaasussa ne liikkuvat vapaasti ja törmäilevät vain harvoin": gas molecules collide very often; the point is that they are far apart and move freely between collisions. Suggest "liikkuvat vapaasti kaukana toisistaan". (Carried from round 1.)
- inquiry.json check-2 solution — "teho $1500\,\text{W}$ on annettu kolmella numerolla": 1500 is ambiguous (two to four figures); say that $15{,}0\,\text{min}$ limits the result to three. (Carried from round 1.)
- inquiry.json check-c2, first distractor's feedback — "irrottaa molekyylejä toisistaan" is acceptable, but for one wording everywhere (guardrails) it could say "molekyylit etääntyvät toisistaan ja niiden välinen vuorovaikutusenergia kasvaa", as check-1 does.
- sim.js:8 — the code comment still says the plateau energy "breaks the bonds between particles". Students do not see it; align it with the model at the next sim change.

## Checked
- Round-1 blocking items fixed: the pred-2 distractor now names the ratio of the durations (clearly wrong, and its feedback matches); the virhe feedback now uses the guardrail wording (interactions change, interaction energy rises).
- One script recomputed every number: retrieval 209,5 kJ (distractors 2,1 kJ and 419 kJ), pred-1 1130/565 s, pred-2 83,5/565 s and 167/1130 s, r/s = 6,77, worked example 2 343 750 J/kg, +3,7 %, 133 g, siirto 188 W (mistakes 27,8 and 11 300), check-2 0,597 kg (mistakes 0,677 and 4,04; check 0,54 kg), check-3 2260 J + 264 J, ratio 9,6, virhe 66,8 kJ, text ratios 5,39 and 79,7 K, expansion work about 7,5 % of r ("pieni osa").
- Worked example: starts from Q_kuum = Q_h, then Pt = r Δm, solved symbolically before substituting; the direction of the bias from losses (r too large) is right.
- Heating-curve figure: the ice and steam slopes are about twice the water slope (c ratios 2,0 and 2,1), as the text says. In the phase diagram the melting line leans left, as it does for water, and the mountain point boils below 100 °C.
- sim.js implements the piecewise Q(T) model with the table constants, Q = Pt, plateaus sm/P and rm/P. The model box states the piston, the constant pressure, the open-pot and rigid-vessel cases, and that the values are model values.
- exp-1 locks m and varies P; exp-2 locks P and varies m. simState gives tMelt and tBoil at those values.
- The condition "pure substance at constant pressure" is stated in the theory, the summary, the misconception section and the goals.
- Each choice has exactly one correct option, and every distractor's feedback is correct.
- The exit ticket, the summary, the johtopäätös and check-3 model answers agree with the theory and the guardrails. Scope: FY3 olomuodon muutokset.
