VERDICT: PASS
CONTENT-HASH: ffc9647383412788

## Blocking

## Polish
- lang/fi.json:1950 "Simulaatio osoittaa läpilyöntirajan": "näyttää" is plainer for 16-year-olds; the note is two sentences under the readout, so shorten for a phone if easy.
- lang/fi.json:1946 "Ideaalimallin laskennalliset arvot ennen läpilyöntiä" is correct but heavy; "Mallin laskemat arvot ennen läpilyöntiä" says the same.

## Checked
- Changed part: with the source connected and breakdown, the readout (lukemat_lap) now labels Q and W as the ideal model's computed values before breakdown, so a student cannot read them as the capacitor's real state; the line is consistent with the model note and the lesson's breakdown text.
- Experiment koe-5 records only E and the breakdown flag, so the relabelled Q and W do not disclose or distort its answer; koe-1 to koe-4 use the normal readout (lukemat) and are unaffected.
- Lesson text, predictions, example stages, exit ticket and figures unchanged since the last PASS; the flow and one-lesson workload stand.
- Deterministic checks (inquiry 116/0, layouts 360/768/1280) pass.
