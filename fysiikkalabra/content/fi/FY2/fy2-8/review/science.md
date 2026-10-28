VERDICT: FAIL
CONTENT-HASH: fe513fd7ad68b4ac

## Blocking
- lesson.md:146, 191; inquiry.json:18, 228, 307; exit-ticket.json:12 — student-visible numbers in prose still outside LaTeX, against the teacher's standing rule "everything in LaTeX" (round 2 listed them under Polish; they are a rule breach a student sees, so they block now): "noin 70-kertainen" (lesson 146), "noin 41 kertaa pienempi" (lesson 191, example check), "eli 280 molekyyliä" (hook), "noin 41 kertaa enemmän" (virhe feedback), "noin 41-kertaiset" (perustele model), "noin 70-kertaiset" (exit ticket 3). — Fix: "$70$-kertainen", "$41$ kertaa", "$280$ molekyyliä", "$41$-kertaiset", "$70$-kertaiset".

## Polish
- lesson.md:91–97, inquiry.json:107 (aineisto table) — the table values (820, 490, …, 11–12) are plain text; for consistency with the rule write them as $820$, $41\text{–}48$ etc.
- lesson.md:87 — "$1000\,\text{W} \cdot 3600\,\text{s} = 3{,}6\,\text{MJ}$" skips the joules; "$= 3\,600\,000\,\text{J} = 3{,}6 \cdot 10^{6}\,\text{J} = 3{,}6\,\text{MJ}$" shows the substitution.
- inquiry.json:307 (perustele model) — "ei tuota jätettä" overstates (blades and decommissioning are waste); say "ei tuota radioaktiivista jätettä eikä käytä polttoainetta".

## Checked
- Recomputed in one script with my own formulas: all 21 lesson-answers.py values and every inquiry number (820 kg with mistake 820 000 g; 49 000 t with mistakes 0,049 t and 4,9·10¹⁰ g; 16 kg (15,90) with mistakes 13,2 and 15 900; 43 200 g vs the student's 300; 1200 t and 41 in the model; 2,4 t, 2,5 t, 58 kg, 41, 68 in the example; ticket 120 g; 33 K) — all match, all inside tolerance.
- Round-2 blocker fixed: every unit conversion (example check, aineisto, virhe, siirto mistakes and check, tarkistus-2 check and mistake) now substitutes the factor; worked example chain ends at $2{,}352\,\text{t}$; "polttoainekuljetuksia" fixed.
- Data with sources right: IPCC AR5 WG III Annex III medians; IPCC 2006 petrol 69 g/MJ; NOAA 2023 ≈ 420 ppm vs 280 ppm (< 0,5 ‰); −18 → +15 °C.
- m = e · E correct, conditions and units stated; inside FY2 central contents; FY3 only named by chapter; no energy-balance model.
- Worked example: seven stages, symbolic first, 2 s.f. justified, check is a real check.
- Emissions chart to scale (0,440 px per g/kWh, every bar within 0,5 px); greenhouse figure marked not to scale and physically right.
- Every correct option and every feedback's physics checked (predictions, alkuperä, muut perusteet, virhe, kuljetus 400 : 50 = 8, tarkistus-1).
- Invented situations marked as examples; no ×; written division as colon.
