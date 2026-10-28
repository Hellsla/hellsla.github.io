VERDICT: FAIL
CONTENT-HASH: d032fc6ba7d117ce

## Blocking
- lesson.md:183-188 (Esimerkki, vaihe 5 "Sijoitus") — in the 390 px capture the last row "osuus = 1598 kW : 5000 kW = 0,32" runs past the card edge and the final digit is cut ("0,3:"); the share is the second asked quantity. Fix in the shared mathlayout (wrap or align the row so it fits 360 px), not by hand-splitting the chain. Also vaihe 4: "14 ·" / "10^6 kWh" breaks mid-product; keep the factor together.

## Polish
- inquiry.json data-yksikko — the power table has no `source`/badge although it states real plants (Olkiluoto 3) and typical sizes; mark as `statistics` with a source or as `example` ("tyypillisiä, pyöristettyjä").
- Source-note box in Tutki (390 px) is still an oval pill with a multi-line note; shared component, make it a plain rounded box.
- Figure "unit-power": the axis shows 10^3 ... 10^9 W only; add "1 kW", "1 MW", "1 GW" under three ticks so a student sees the powers of ten as units.
- ennuste-1 is fact recall (which source is largest) that the table settles; acceptable, but the justify box invites "miksi", which the later data (viikko) is what really tests.
- johtopaatos model answer names "säädettäviä voimaloita" before the groups are taught; fine as an inference, but say "voimaloita, joiden tehoa voi nostaa nopeasti".

## Checked
- Round 1 blockers fixed: criteria list renders as a list; Tutki tables fit 390 px with all columns visible; the conclusion now rests on the week table (tuuli 0,4-6,4 GW vs ydin 4,3 GW, nominal 8 GW); the "maailman" claim is now safe ("kymmeniä kertoja").
- Opening question answered with evidence before the theory; slot goals covered, no FY3 content.
- Example: seven stages, one step each, symbolic first, check present.
- Figures (plants with generator and lämpö arrow, bars, log-axis dots) legible and beside their paragraphs at 390 and 1280 px.
- Badges "Tilastoaineisto" and "Keksitty esimerkkiaineisto" present on data-fi and data-viikko; chapter names, not ids.
- Exit ticket and checks test grouping, E = P t, nominal vs mean; workload one lesson.
- Finnish and number+unit cases correct (5,0 MW:n, 1600 MW).
