VERDICT: FAIL
CONTENT-HASH: ad41a8dfa1fbe5f2

## Blocking
- [Major] lesson.md, "Kaava: Latausaika, latausteho ja johdon lämpeneminen", all "missä" lines — units are plain text: (kWh), (h), (kW), (A), (W), (m), (€), (€/kWh); rendered in the body typeface next to KaTeX symbols — breaks the FY6 rule that every unit is LaTeX, and fy6-15 sets the same lines as ($\text{A}$) — write `($\text{kWh}$)`, `($\text{h}$)`, `($\text{kW}$)`, `($\text{A}$)`, `($\text{W}$)`, `($\text{m}$)`, `($\text{€}$)`, `($\text{€/kWh}$)`. The fix is mechanical, so it should not wait.

## Polish
- [Minor] Esimerkki Sijoitus and exercise L3-1 — `\tfrac{€}{kWh}` nested in a fraction renders tiny and cramped at 390 px — write `\text{€/kWh}` as the rest of the chapter does.
- [Minor] fig 7 (kayra) — "20 %", "90 %", "99 %" have no word saying they are charge levels, the 11 kW plateau lies between the 10 and 12 ticks, and the curve beyond 4,5 h is solid although it is a model — label "$\text{varaustaso}$" once, add a tick at 11 and a "$\text{malli}$" note.
- [Minor] lesson.md, Pääsulake ja samanaikaiset kuormat — the comma after "$17\,\text{kW}$" wraps to the start of the next line at 1280 px; join the comma into the maths or reword.
- [Minor] lesson.md, Miksi latausasemalla… — "suojausluokitus, esimerkiksi IP54" clashes with fy6-15's glossary term (luokka I–III); IP is kotelointiluokka (for science: check the term).
- [Minor] fig 3 (koti) — "3 · 25 A" and "3 · 16 A" labels are stacked close together; the phase lines carry no L1–L3 labels.

## Checked
- contact-1, -2, -3, -4; fig-3 (koti), fig-5 (vaiheet), fig-7 (kayra) at 390; hero in contact-1; theory-1280-1 to -3
- example-390-1, -2; stage-ennusta-390-1; open-exercises L2-1 and L3-1 at 1280, exercise figure lataus-ex
- Not opened separately: top-390, tarkista and exit opens (seen in contact sheets only).
- Source read: lesson, exit ticket, solutions; plain-quantity scan hit only the lines above.

## Scores
illustrations 4 · typography 4 · Finnish 4 · accessibility 4
