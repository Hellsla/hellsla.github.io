VERDICT: FAIL
CONTENT-HASH: f2e7234e63be720a

## Blocking
- lesson.md:189, inquiry.json:125, 226, 291, 295, 298, 373 — unit conversions written as bare equalities, without the substitution the teacher's standing rule requires: "$2\,500\,000\,\text{g} = 2{,}5\,\text{t}$", "$12\,\text{g/kWh} \cdot 4800\,\text{kWh} \approx 58\,\text{kg}$" (example check); "$800\,000\,\text{g} = 800\,\text{kg}$" (aineisto check); "$43\,200\,\text{g} \approx 43\,\text{kg}$" (virhe correct option); "$49\,000\,\text{g} = 0{,}049\,\text{t}$" and "$4{,}9 \cdot 10^{10}\,\text{g} = 4{,}9 \cdot 10^{4}\,\text{t}$" (siirto mistake feedbacks); "$5 \cdot 10^{10}\,\text{g} = 50\,000\,\text{t}$" (siirto check); "$14\,700\,\text{g} \approx 15\,\text{kg}$" (tarkistus-2 check). — Fix: insert the substituted step in each, e.g. "$= 2\,500\,000 \cdot 10^{-6}\,\text{t} = 2{,}5\,\text{t}$", "$= 57\,600\,\text{g} = 57\,600 \cdot 0{,}001\,\text{kg} \approx 58\,\text{kg}$", "$= 49\,000 \cdot 10^{-6}\,\text{t}$", "$= 4{,}9 \cdot 10^{10} \cdot 10^{-6}\,\text{t}$".

## Polish
- lesson.md:179 — the worked example's chain ends at "$2352 \cdot 0{,}001\,\text{t}$" with no value; add "$= 2{,}352\,\text{t}$" so the step to the 2,4 t result is visible.
- inquiry.json:307 (perustele model) — "ei käytä polttoainetta, joten kuljetuksia ei tarvita" contradicts the lesson, which counts transport in wind's 11–12 g/kWh; say "polttoainekuljetuksia".
- lesson.md:146, 189; inquiry.json:18, 228, 307; exit-ticket.json:12 — dimensionless prose numbers ("41 kertaa", "70-kertainen", "280 molekyyliä") are outside LaTeX; write them as $41$.

## Checked
- Recomputed in one script: lesson-answers.py's 21 values and every inquiry numeric (820 kg, 49 000 t with mistakes 0,049 t and 4,9·10¹⁰, 16 kg with 13,2 and 15 900, 43 200 g, kWh²/g) — all match.
- Data with named sources correct: IPCC AR5 WG III Annex III medians (coal 820, gas 490, biomass dedicated 230, PV 41/48, hydro 24, nuclear 12, wind 11/12); IPCC 2006 petrol 69 g/MJ; NOAA 2023 ≈ 420 ppm vs 280 ppm; −18 → +15 °C. Biomass note now says combustion CO₂ is counted as zero — right.
- Invented situations (family, city, municipality) marked as examples.
- Greenhouse mechanism right at FY2 level (solar mostly transmitted, IR absorbed and re-emitted, part down); round-1 per-mille and sunlight wording fixed. No Stefan–Boltzmann or energy-balance model; FY3 only named by chapter.
- m = e · E correct and in scope; 1 kWh = 3,6 MJ by substitution.
- Worked example symbolic first, 2,4 t with justified figures; 58 kg and 41× correct.
- Emissions chart to scale (0,44 px per g/kWh; every bar checked); greenhouse figure marked not to scale and physically right.
- Every correct option and feedback physics right.
- No ×; written division as colon; calculations in LaTeX.
