VERDICT: PASS
CONTENT-HASH: 4e8678dce2802a4d

## Blocking
(none)

## Polish
1. inquiry.json ennuste-2, johtopaatos — both rest on the meters' resistance, but the lesson text introduces resistance only in "Mittari vaikuttaa piiriin", after Tutki. The prediction states no meter resistance, so the student can only guess; the explain prompt then asks for "mittarien resistanssin avulla". Fix: one line in the ennuste-2 prompt or the sim intro ("jännitemittarin resistanssi on $10\,\text{M}\Omega$, virtamittarin alle $2\,\Omega$") and a half-sentence on what resistance means.
2. inquiry.json koe-1 intro — "kenen virtaa mittari silloin näyttää" cannot be answered: with the ammeter across the lamp on the 200 mA range the fuse blows and the table says "sulake paloi". Fix: "mitä mittari näyttää, ja mitä sille tapahtuu?".
3. inquiry.json hook — "voi sammuttaa lampun tai polttaa oman sulakkeensa" names two of ennuste-2's four options before the student commits. Fix: "voi muuttaa piirin toimintaa" and keep the fuse for later.
4. lesson.md "Kaava: Yleismittarin virheraja" — the error-limit half (formula, error-bands figure, example, siirto, check 2) has no prediction or experiment; the sim shows resolution but no error limit. It is a formula lesson half. Acceptable for the slot's "mittausalue", but consider a one-line sim readout of Δx so the student sees the 20 V / 2 V difference rather than only reading it.
5. inquiry.json siirto solution — "Alueella 200 mA sama virta näkyisi muodossa 18,6 mA" appears from nowhere; the given reading is 0,02 A. Fix: say "esimerkiksi $18{,}6\,\text{mA}$ (pyöristyy näytöllä $0{,}02\,\text{A}$:ksi)".

## Checked
- Learning path: connection, range, misuse, error limit; hook question answered by johtopaatos and tiivistelmä.
- Ennuste-1/2 can be refuted by koe-1/2 (model values 97,8 mA, 1,50 V, 4,50 V verified against 15 Ω, 30 Ω, 4,5 V).
- Each distractor's feedback repairs its misconception; reveal after min 2 rows.
- Sim at 390 px (capture 2): readout, wires, COM/V mA/10 A terminals, selector legible; no clipping.
- Figures 1–5 legible at 390 px; descriptions give the data without the answer.
- Example: 7 stages, one step each; numbers (0,0275, 0,0095, 1,8 %, 0,63 %) correct.
- Etsi virhe and siirto distractors are real slips; three hints progressive.
- Tarkistus-1 concept check with misconception distractors; tarkistus-3 criteria observable.
- Exit ticket tests OL and the formula; Finnish reads well.
- Workload about one lesson (koe-3, kertaus, pohdi, virhe, tarkistus-3 optional). Option shading in the ennusta capture assumed to be hover (gating is tested).
