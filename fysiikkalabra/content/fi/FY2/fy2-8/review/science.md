VERDICT: PASS
CONTENT-HASH: 15412e00f1e4b741

## Blocking

## Polish
- inquiry.json:384, 392 (ennuste-2 feedbacks) — "kivihiilen energia tulee lähes kokonaan hiilen palamisesta" overstates: in bituminous coal hydrogen gives roughly a fifth of the heating value (carbon ~75–80 %). — Say "suurimmaksi osaksi hiilen palamisesta"; the comparison with methane (much more hydrogen) still holds.
- lesson.md:181–189, inquiry.json:405 (aineisto table) — the table values (820, 490, …, 41–48, 11–12) are plain text; write them as $820$, $41\text{–}48$ for consistency with the LaTeX rule.
- lesson.md:179 — "$1000\,\text{W} \cdot 3600\,\text{s} = 3{,}6\,\text{MJ}$" skips the joules; "$= 3\,600\,000\,\text{J} = 3{,}6\,\text{MJ}$" shows the step.

## Checked
- Recomputed in one script with my own formulas: all 21 lesson-answers.py values and every lesson/inquiry/exit-ticket number (example 2 352 000 g = 2,352 t → 2,4 t, check 2,5 t, wind 57,6 → 58 kg, 490 : 12 ≈ 41; aineisto 820 kg, mistake 820 000; virhe 43 200 g ≈ 43 kg vs the student's 300; siirto 4,9·10¹⁰ g = 49 000 t, mistakes 0,049 t and 4,9·10¹⁰; wind 1200 t; tarkistus-2 7,2 l → 230,4 MJ → 15,9 kg → 16 kg, mistakes 13,2 kg and 15 900 g, check 14,7 kg and 2,2 kg/l; ticket 120 g, ≈ 70; 33 K; 420 ppm = 0,42 ‰). All match; rounded student answers stay inside 2 % tolerance.
- Round-3 blocker fixed: no student-visible number left outside LaTeX (only years, list numbers and titles remain).
- Round-3 polish taken: "ei tuota radioaktiivista jätettä eikä käytä polttoainetta" in the perustele model.
- Data and sources right: IPCC AR5 WG III Annex III medians (coal 820, gas CC 490, dedicated biomass 230, PV rooftop 41 / utility 48, hydro 24, nuclear 12, wind onshore 11 / offshore 12); IPCC default petrol ≈ 69 g/MJ, ≈ 32 MJ/l realistic; NOAA 2023 ≈ 420 ppm vs 280 ppm; −18 → +15 °C.
- m = e · E correct, units and meaning stated; inside FY2 central contents; no radiative-balance model, FY3 named by chapter only.
- Worked example: seven stages, symbolic first, conversions shown, 2 s.f. justified, reasonableness check real.
- Emissions chart to scale (0,440 px per g/kWh, all bars within 0,5 px; solar bar at the range midpoint); greenhouse figure marked not to scale, arrows physically right (solar through, IR absorbed, re-emitted down and to space).
- Every correct option and feedback's physics checked: kertaus, both predictions, alkuperä, muut perusteet, virhe (kWh²/g unit argument), kuljetus (400 : 50 = 8), tarkistus-1, model answers of perustele and tarkistus-3.
- Biomass treatment correct: biogenic combustion CO₂ counted zero in AR5's 230, its decades-long re-uptake lag stated.
- Invented situations marked as examples; division written with a colon.
