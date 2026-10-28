VERDICT: FAIL
CONTENT-HASH: 934ee6f37f33aaf8

## Blocking
- exit-ticket.json:8 — **A**: "lämpöä siirtyy vasta, kun kivi koskettaa kylmempää kappaletta" is wrong: a hot stone transfers heat to colder surroundings by radiation and to the air around it without touching a colder solid body (guardrail "Net transfer": thermal radiation leaves both bodies) — write "lämpöä siirtyy, kun kiven ja sen ympäristön välillä on lämpötilaero".
- lesson.md:47 (Ydinajatus) — **B**: "olomuodon muuttuessa sisäenergia muuttuu, vaikka lämpötila pysyy samana" holds only for a pure substance at constant pressure (guardrail "State a law's conditions") — add the condition in a few words, e.g. "esimerkiksi kun puhdas jää sulaa normaalipaineessa, sisäenergia kasvaa, vaikka lämpötila pysyy samana".

## Polish
- inquiry.json:113 `kokeile.model` — the adiabatic formula T₂ = T₁(V₁/V₂)^(γ−1) is outside FY3's central contents; it is fine in a closed box as a check on the model, but a phrase like "(tätä kaavaa ei tarvitse osata)" keeps the scope clear.
- inquiry.json `check-1` correct feedback — "Siksi venttiilistä purkautuva ilma tuntuu viileältä" is a fair simplification (C); no change needed unless the valve case is developed further.

## Checked
- Definitions: U = particles' kinetic + interaction energy; heat as energy in transfer, never a property; work as the other route; isolated vs closed system — glossary and guardrail wording, and the FY2 "lämpöenergia" bridge stated.
- First law ΔU = Q + W with its condition (no change in the system's kinetic or potential energy) and the sign convention for Q and W stated once, used the same in figures, example, virhe, siirto, check-2, exit ticket.
- Recomputed: example 110 J; virhe 160 J; siirto 75 N·0,080 m − 0,60 J = 5,4 J (mistakes 6,6 and 599,4); check-2 30 J (mistakes 230 and 10); exit ticket 180 J.
- Simulation ported to node with the same seeded PRNG and step order: slow insulated push W = 13,14 J, T = 329,7 K (ΔT 37 K), p = 1,50 p₀; fast W = 19,06 J, ΔT 53 K; conducting W = 12,37 J, Q → −12,37 J, T → 293,2 K, p = 1,333 p₀; push time 18,8 s; seeds 1–12 give W = 11,2–15,2 J — every number in predictions, feedback, model answer and boxes agrees.
- ΔT/W = 1/0,359 = 2,79 K/J; 0,50 g · 718 J/(kg·K) = 0,359 J/K; (4/3)^0,4 · 293 K = 329 K.
- sim.js: piston reflection v' = 2w − v gives the work exactly; diffuse re-emission with equipartition (f = 5); conducting wall scales energy towards T₀ and books it as Q; ΔU = Q + W is bookkeeping, as the calc box says.
- Experiments: koe-1 locks walls, varies piston speed; koe-2 locks speed, varies walls; simState carries W, Q, dU, dT, T, p.
- Exactly one correct option in pr-mikromalli, pred-1, pred-2, koe-2 question, virhe, check-1; distractor feedback correct.
- Worked example complete in seven stages with a real limiting-case check.
