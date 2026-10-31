VERDICT: PASS
CONTENT-HASH: e0f90cf823e55c4a

## Blocking

## Polish
- lesson.md:230 — "Siksi hiukkasten välisten vuorovaikutusten energia on mallissa merkityksetön, ja kelvinlämpötila on suoraan verrannollinen hiukkasten keskimääräiseen liike-energiaan": the "Siksi" reads as if T ∝ mean kinetic energy follows from the missing interactions (it holds in real gases too). Split it into two sentences.
- lesson.md:473 (Tiivistelmä) — "Samassa paineessa, lämpötilassa ja tilavuudessa on aina yhtä monta moolia kaasua": the next bullet gives the model's limit, so this is C. "ideaalikaasun mallissa" in place of "aina" would match the Kaava section.
- inquiry.json:445 (check-1, correct feedback) — "kukin hiukkanen osuu seiniin useammin": in the sim only the right wall moves, so the hits per particle less than double. What doubles is the hits per unit wall length. Adding "seinän pituutta (pinta-alaa) kohti" would make it exact.

## Checked
- One script recomputed every number: weighing masses vs n = pV/(RT) = 0,2072 mol (all within ±0,02 g); m/M 0,2075/0,2064/0,2076/0,2068; mean R 8,32 → "≈ 8,3"; laske-r 8,302 and the mistakes 121,7 / 8302 / 0,0083; example 0,2073 mol, 0,83 g, air 6,0 g, 24,1 l/mol.
- virhe 1,2 → 0,083 mol; siirto 91 200 mol, 2645 kg, the mistakes 9870 and 2,64, the reasonableness check 1,20 kg/m³ → 3366 kg · 293/373 ≈ 2640; exit ticket 0,601 mol; check-c2 1,068; check-2 3,0; exp-2 N = 50.
- sim.js: impulse 2|v⊥| over the perimeter gives NkT/A exactly in 2D; T rescales by √T; thermalize after N changes; V is isothermal by construction, and the model box says so.
- Ran the preview in Playwright: measured p/p_ref matches the prediction at the five table states and at (150, 450 K, 75 %); the scatter is about ±5 % at N = 100 and ±10 % at N = 20. The taulukko values (3,91 etc.) are within the sim's scatter.
- exp-1/exp-2 lock T and V, vary N, and the measured keys pMeasured and hitRate exist in simState.
- Figures: speed arrows He:air 32:12 ≈ 2,7 = √(29/4); mole-mass bars 14:101,5:154 = 4:29:44; the paine-ja-tekijat figure has particle counts 6/12/6/6, the 2T arrows are √2 longer, and V/2 has half the height.
- pred-n, pred-1, punnitus-vertailu, taulukko, check-1, check-c2 and virhe each have exactly one correct option, and each distractor's feedback is correct (He: rate ×2,7 and momentum ÷2,7 → same p).
- Scope: within FY3 (state variables, gas laws, the ideal-gas equation); there is no later-course physics as a requirement.
