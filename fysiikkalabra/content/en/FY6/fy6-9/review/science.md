VERDICT: PASS
CONTENT-HASH: b57c3875fe94cbd2
Mode: delta (en lesson wording change in inquiry.json)
Round 2

## Blocking
(none)

## Polish
- (Minor) Fixed during review: the primary/disposable battery terminology is now one term ('disposable battery', with 'primary battery' given once in brackets), consistent in lesson, summary and exit ticket; fy6-8 uses neither term.

## Checked
- Numbers and units compared token by token against the Finnish (lesson, inquiry, exit ticket, figures, sim labels): identical multisets, decimal point used; subscripts U_ch, W_batt, Q_cap, R_tot match the Finnish U_lat, W_akku, Q_kap, R_kok.
- Every solution has all steps (Given, Find, Principle, Formula, Conversions, Substitution, Answer, Reasonableness) as in the Finnish: 97 labelled fields each.
- Physics terms: source voltage (emf), terminal voltage, internal resistance, capacity in Ah, efficiency: correct.
- Re-review after the lang-key change (sims.fy6-9.ulat_lab / ulat_eq): the sim canvas now shows U_ch (en); values and formulas unchanged.
- Re-review after the concept-review commit: howto wording (electrical energy transformed into internal energy), efficiency paragraph (often below 100 %, charging always, R and R_s), L3-03 sisäenergiaksi, matching the Finnish; no numbers changed; $ counts equal.
- Delta re-review: the simulation parameter name R in inquiry.json (three simulations) changed from 'resistance of charger and wires' to 'charger and wire resistance' (360 px overflow fix). Correct English noun phrase, same meaning as the Finnish 'laturin ja johtojen resistanssi' (resistance of the charger and the wires together, the series resistance R in R_tot = R + R_s); symbol R, units and values unchanged.
