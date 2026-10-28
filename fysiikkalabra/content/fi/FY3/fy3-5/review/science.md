VERDICT: PASS
CONTENT-HASH: 106a6f42772f0a62

Round 2: re-check of round-1 Blocking items against the fix diff.

## Blocking

## Polish
- lesson.md:47 (Ydinajatus) — resolved, but the general clause "olomuodon muuttuessa sisäenergia muuttuu, vaikka lämpötila pysyy samana" still comes before the example that gives the condition. The example now names the condition (pure ice at normal pressure, 0 °C), so it does not leave a wrong picture. Tighter: "olomuodon muuttuessa sisäenergia voi muuttua lämpötilan pysyessä samana: kun esimerkiksi …".
- inquiry.json:113 `kokeile.model` — the adiabatic formula T₂ = T₁(V₁/V₂)^(γ−1) is outside FY3's central contents. It is fine in a closed box as a check on the model, but "(tätä kaavaa ei tarvitse osata)" would keep the scope clear.

## Checked
- Round-1 A, exit-ticket.json:8: now "lämpöä siirtyy, kun kiven ja sen ympäristön välillä on lämpötilaero". This is correct (radiation and the surrounding air are covered) and matches the glossary definition of heat. Resolved.
- Round-1 B, lesson.md:47: the example "puhdas jää sulaa normaalipaineessa … pysyy 0 °C:ssa" states the guardrail condition and is correct physics. The Finnish is grammatical. Resolved.
- The diff touches nothing else in the lesson. Theory, inquiry, sim and figures are unchanged from the full review at the previous hash: the simulation numbers were recomputed in node (13,14 / 19,06 / 12,37 J) and every worked number was rechecked.
- The changed lines do not affect any option, answer key or solution.
