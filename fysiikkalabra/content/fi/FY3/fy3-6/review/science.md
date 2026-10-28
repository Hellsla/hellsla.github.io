VERDICT: PASS
CONTENT-HASH: 2cef3f149c6042e7

## Blocking

## Polish
- inquiry.json `siirto` — `answer` is 29.1 kg while the solution's Vastaus is "29 kg, kaksi merkitsevää numeroa" (ΔT = 8,0 K); both pass the tolerance, but the answer field and the solution should give the same rounded value.
- inquiry.json `tarkistus-3` criteria — "keväällä se sitoo lämpöä" uses the stored-heat wording the guardrails avoid; "keväällä siihen siirtyy lämpöä ilmasta ja se lämpenee hitaasti" matches the model answer.
- lesson.md Ydinajatus (beach) — evaporation from the water surface is a further reason the water warms less; optional, the text already names depth as a second cause.

## Checked
- Definitions: c per kilogram and kelvin, C = cm for the whole body, heat as energy transferred because of a temperature difference, equilibrium, calorimeter — the same as the glossary and fy3-5; Q = cmΔT stated with "olomuoto ei muutu" in theory, summary, example, sim box.
- Sign convention ΔT = T_loppu − T_alku and the positive "given off = taken in" form of the balance explained; T solved symbolically as the C-weighted mean.
- Recomputed in one script: example c = 374,6 J/(kg·K) (24,6 °C → 383; copper check 24,6 °C); ennuste-1 26,8 °C / 44,0 °C, Q 8,5 kJ / 30 kJ, C 160 / 838 J/K; ennuste-2 40,0 / 55,0 / 63,1 °C; virhe 6,6 °C vs 30,0 °C; siirto 29,09 kg (mistakes 220, 21,3); tarkistus-1 4500 vs 838 J/K; tarkistus-2 890,6 J/(kg·K) (mistakes 768, 501); misconception 35 °C and ×9,3; exit ticket 419 kJ, ×9, 65 °C.
- Figures to scale: c-bars 0,0933 px per J/(kg·K) for all six bars; water-sand rises 20 px vs 105 px = 4190/800; calorimeter caption numbers match the example.
- sim.js: Teq as the C-weighted mean, Q = C_B(T_B0 − Teq) = Q_W; exponential approach labelled illustration only; no phase changes (0–100 °C); speed changes pace only.
- Experiments: koe-1 locks both masses and temperatures and varies cB; koe-2 locks mW, TW0, cB, TB0 and varies mB; simState gives Teq and CB.
- Exactly one correct option in kertaus, ennuste-1, ennuste-2, virhe, tarkistus-1; every distractor's feedback right (cold does not flow, equal temperatures not equal U, Kelvin shift cancels).
- Worked example: seven stages, symbolic c_m first, 2-s.f. reason shown by the 0,1 K sensitivity, real check against copper.
- Exercise set at hash 13bc0d2daf5f4e53 already has a current science report; I spot-checked answers.py (all twelve values recomputed, same) and did not rewrite it.
