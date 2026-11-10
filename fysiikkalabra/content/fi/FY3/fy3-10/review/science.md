VERDICT: PASS
CONTENT-HASH: da7489bd041cfbff

## Blocking
- none

## Polish
- sim.js (delta 2026-11-10): while the pressure says 'mittaus tasaantuu', the hit rate is still shown as a number from the same < 0,5 s window (about ±25 % at 0,1 s with N = 100). Hiding it too, or showing it only after SETTLE, would match the pressure readout; exp-1/exp-2 use hitRate.
- lesson.md:230 — "Siksi hiukkasten välisten vuorovaikutusten energia on mallissa merkityksetön, ja kelvinlämpötila on suoraan verrannollinen hiukkasten keskimääräiseen liike-energiaan": the "Siksi" reads as if T ∝ mean kinetic energy follows from the missing interactions (it holds in real gases too). Split it into two sentences.
- lesson.md:473 (Tiivistelmä) — "Samassa paineessa, lämpötilassa ja tilavuudessa on aina yhtä monta moolia kaasua": the next bullet gives the model's limit, so this is C. "ideaalikaasun mallissa" in place of "aina" would match the Kaava section.
- inquiry.json:445 (check-1, correct feedback) — "kukin hiukkanen osuu seiniin useammin": in the sim only the right wall moves, so the hits per particle less than double. What doubles is the hits per unit wall length. Adding "seinän pituutta (pinta-alaa) kohti" would make it exact.

## Checked
- delta review 2026-11-10 (measurement window reset, teacher's FY3 brief): sim.js sync() empties the average before any state change and advance() runs after it, so every averaged hit belongs to the new (N, T, V); particles keep positions and velocities apart from the existing √T rescale, N thermalize and isothermal piston squeeze, so the reset fakes nothing: pMeasured is still impulse/perimeter/time. Measurements: ratio 0,93–1,06 at 0,7–2 s after a change, long-run means 0,987–1,019 at six states (p ∝ NT/V emerges). Bar clamped at 1,05·top and the axis frozen while settling, no number shown; simState.settling = tAvg < 0,5 s; 'Nollaa mittaus ja odota' in the inquiry stays valid. Hashes equal at start and end.
- delta review 2026-11-07 round 2 (follow-up consistency edits): inquiry 'Etsi virhe' feedbacks: pressure in Pa with m³ (1 Pa·m³ = 1 J) and litres only with kPa (1 kPa·l = 1 J) are correct and match the lesson's 1 kPa·l = 1 J; kPa with m³ gives a factor 1000 error, right; each feedback still says the error is elsewhere, consistent with the step's correct option; litre as \textsf{l} as in the lesson. Hashes equal at start and end.
- delta review 2026-11-07 (teacher's proofread replacement texts): p = absolute pressure, T kelvin temperature; unit argument Pa·m³ = N·m = J and kPa·l = 1000 Pa·0,001 m³ = 1 J are correct and consistent with R = 8,31 J/(mol·K); inquiry and exit-ticket edits are typesetting only, numbers unchanged (exit ticket n = 0,601 mol rechecked).
- One script recomputed every number: weighing masses vs n = pV/(RT) = 0,2072 mol (all within ±0,02 g); m/M 0,2075/0,2064/0,2076/0,2068; mean R 8,32 → "≈ 8,3"; laske-r 8,302 and the mistakes 121,7 / 8302 / 0,0083; example 0,2073 mol, 0,83 g, air 6,0 g, 24,1 l/mol.
- virhe 1,2 → 0,083 mol; siirto 91 200 mol, 2645 kg, the mistakes 9870 and 2,64, the reasonableness check 1,20 kg/m³ → 3366 kg · 293/373 ≈ 2640; exit ticket 0,601 mol; check-c2 1,068; check-2 3,0; exp-2 N = 50.
- sim.js: impulse 2|v⊥| over the perimeter gives NkT/A exactly in 2D; T rescales by √T; thermalize after N changes; V is isothermal by construction, and the model box says so.
- Ran the preview in Playwright: measured p/p_ref matches the prediction at the five table states and at (150, 450 K, 75 %); the scatter is about ±5 % at N = 100 and ±10 % at N = 20. The taulukko values (3,91 etc.) are within the sim's scatter.
- exp-1/exp-2 lock T and V, vary N, and the measured keys pMeasured and hitRate exist in simState.
- Figures: speed arrows He:air 32:12 ≈ 2,7 = √(29/4); mole-mass bars 14:101,5:154 = 4:29:44; the paine-ja-tekijat figure has particle counts 6/12/6/6, the 2T arrows are √2 longer, and V/2 has half the height.
- pred-n, pred-1, punnitus-vertailu, taulukko, check-1, check-c2 and virhe each have exactly one correct option, and each distractor's feedback is correct (He: rate ×2,7 and momentum ÷2,7 → same p).
- Scope: within FY3 (state variables, gas laws, the ideal-gas equation); there is no later-course physics as a requirement.
