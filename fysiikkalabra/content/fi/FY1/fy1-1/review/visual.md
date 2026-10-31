VERDICT: PASS
CONTENT-HASH: ecf054010b4bf591

## Blocking

## Polish
- [Minor] theory-1280-1 (Suuruusluokka kertoo karkean koon) — the round-1 split after `\cdot` is fixed everywhere I looked, but one punctuation strand remains: "…ja $10^{n+1}$" ends the line and ", kun $a$ on yli noin 3" starts the next with a comma — the template's punctuation glue does not catch a comma after a superscripted power at a line end — extend the glue to that case (or move the clause so the comma follows text).
- [Minor] sim-390 readout — "Näkyvissä 4 kohdetta: euron kolikko, jalkapallo" / ", ihminen, sinivalas" has the comma at a line start (the readout is built by the simulation script, outside the template glue) — keep the comma with the preceding name.
- [Minor] open-tarkista-1280-1 — feedback "$10^{8}/10^{3}$" and distractor "$8/3 \approx 2{,}7$" divide with a slash; the house rule asks for a colon ($8 : 3$).
- [Minor] open-exit-1280 — the heading "Exit ticket" is English on a Finnish page; use a Finnish heading (e.g. "Lopputehtävä").
- [Minor] lesson.md "Kohdetyyppejä, ei portaita" — "Kaikki tähtitieteelliset kohteet eivät ole portaita samassa sisäkkäisyydessä" can read as "not all of them are"; write "Nämä kohteet eivät ole portaita samassa sisäkkäisyydessä, vaan ne ovat galaksien sisällä…".

## Checked
- Round 2, captures current for this hash (stamp ecf054…): theory-1280-1, -2, -4, example-390-1/2, stage-ennusta-390-1, sim-390, open-tarkista-1280-1, open-exit-1280; figures seen in place: scale-axis, ladder, matter-ladder, atom-stadium, interactions (unchanged, clear, LaTeX labels, "ei mittakaavassa" stated, force red, \overline{F}); the other figure captures were judged clean in round 1 and the diff is template-only.
- Verified: every inline `a \cdot 10^{n}` value (theory, valovuosi, example Tunnetut/Tulos/Järkevyys, Ennuste 1) now stays whole; the example's Sijoitus rows and display maths are unchanged; no horizontal overflow or other regression seen.

## Scores
illustrations 5 · typography 4 · Finnish 4 · accessibility 4
