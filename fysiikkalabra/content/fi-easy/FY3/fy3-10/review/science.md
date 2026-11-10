VERDICT: PASS
CONTENT-HASH: 1f48965343916086

## Blocking
- none

## Polish
- sim.js (delta 2026-11-10): while the pressure says 'mittaus tasaantuu', the hit rate is still shown as a number from the same < 0,5 s window (about ±25 % at 0,1 s with N = 100). Hiding it too, or showing it only after SETTLE, would match the pressure readout; exp-1/exp-2 use hitRate.

## Checked
- delta review 2026-11-10 (measurement window reset, teacher's FY3 brief): sim.js sync() empties the average before any state change and advance() runs after it, so every averaged hit belongs to the new (N, T, V); particles keep positions and velocities apart from the existing √T rescale, N thermalize and isothermal piston squeeze, so the reset fakes nothing: pMeasured is still impulse/perimeter/time. Measurements: ratio 0,93–1,06 at 0,7–2 s after a change, long-run means 0,987–1,019 at six states (p ∝ NT/V emerges). Bar clamped at 1,05·top and the axis frozen while settling, no number shown; simState.settling = tAvg < 0,5 s; 'Nollaa mittaus ja odota' in the inquiry stays valid. Hashes equal at start and end.
- delta review 2026-11-07 round 2 (follow-up consistency edits): inquiry 'Etsi virhe' feedbacks: pressure in Pa with m³ (1 Pa·m³ = 1 J) and litres only with kPa (1 kPa·l = 1 J) are correct and match the lesson's 1 kPa·l = 1 J; kPa with m³ gives a factor 1000 error, right; each feedback still says the error is elsewhere, consistent with the step's correct option; litre as \textsf{l} as in the lesson. Hashes equal at start and end.
- delta review 2026-11-07 (teacher's proofread replacement texts): p = absolute pressure, T kelvin temperature; unit argument Pa·m³ = N·m = J and kPa·l = 1000 Pa·0,001 m³ = 1 J are correct and consistent with R = 8,31 J/(mol·K); inquiry and exit-ticket edits are typesetting only, numbers unchanged (exit ticket n = 0,601 mol rechecked). Selkokieli text carries the same meaning as fi.
- batch delta review: key_concepts, reworded sentences, photo captions, objective-form and level-policy edits, chapter-reference titles judged against the guardrails and the lesson text; restyled figure lines are styling only.
