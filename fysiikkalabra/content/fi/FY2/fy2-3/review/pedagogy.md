VERDICT: PASS
CONTENT-HASH: 704ca126f528bedf

## Blocking

## Polish
- inquiry.json `ennuste-1` options ("Noin 15 tuntia.", "Noin 150 tuntia.", "Noin tunnin.", "Noin viisi minuuttia") and `aika` options/feedback ("24 tunnissa", "5 tunnissa") — numbers with units in plain text, against the everything-LaTeX rule — write `$15\,\text{h}$`, `$150\,\text{h}$`, `$1\,\text{h}$`, `$5\,\text{min}$`.
- inquiry.json `hook` — "lamppu on usein päällä tuntikausia" still hints that the lamp wins in time, but the prediction now asks for a number, so it can be refuted; acceptable, softer wording ("pitkään") would be tidier.
- lesson.md Esimerkki, stage Tulos — "teho ja päivittäinen käyttöaika on annettu" → "ovat annetut" (plural subject).
- lesson.md Kilowattitunti — "Joulemuodossa tunti on" → "Jouleina laskettaessa tunti on".
- Opening Miksi question ("sähkölaskua ei voi päätellä pelkästä laitteen tehosta") is answered, but the power-plant scale appears only as one OL3 sentence; fine for the slot, the later chapters carry it.

## Checked
- Round 1 blocking fixed: the `mittari` table now shows all four columns at 390 px (stage-tutki-390-1), no scrolling.
- Round 1 polish done: prediction asks for a duration, 15 h row removed from `aika`, television 80 W in both figures, table and example, OL3 line added.
- Goals: P = ΔE/Δt, W, kWh, bill; no work, force or FY3 content; opening question answered via prediction, tables, `pohdi`.
- Activities fit a simulation-free topic: committed numeric prediction, two data tables the student reads, conclusion `explain`, error-spotting, numeric transfer; one lesson of work, extras optional.
- Figures: bar chart and E–t graph legible, LaTeX labels, scaled, right after their paragraphs (fig-1/2 390 px, theory-1280).
- Worked example: seven stages, one step each, symbols before numbers, 2 s.f. justified, reasonableness check.
- Feedback repairs misconceptions with numbers; nothing disclosed before commitment.
- Exit ticket Q3 tests the core idea (power and time together); phone and 1280 px captures clean, no text wall.
- Hash unchanged at end.
