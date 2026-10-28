VERDICT: FAIL
CONTENT-HASH: 4dc487c519466405

## Blocking
- inquiry.json:71 (ennuste-1, "muutaman asteen" feedback) — "vaikka niitä on vain osa promilleista ilmakehässä" is wrong for water vapour, the gas the lesson names first: it is about 0,25–0,4 % of the air (several per mille); only CO2 (0,42 ‰) and CH4 are fractions of a per mille. A wrong magnitude in a course about magnitudes. — Fix: "alle prosentti ilmakehästä", or name CO2 ("hiilidioksidia on alle puoli promillea").

## Polish
- lesson.md:6 — "pääosin näkyvänä valona", "lähes sellaisenaan läpi": about half of sunlight is near-infrared and the atmosphere absorbs about a fifth. "näkyvänä valona ja lähi-infrapunana", "suurelta osin läpi" (also ennuste-1, tarkistus-1, exit ticket q1).
- lesson.md:59 — oil and gas formed mostly from marine plankton: "muinaisten eliöiden", not "kasvien".
- lesson.md:61, 93 — IPCC 230 g/kWh is "biomass – dedicated" and counts combustion CO2 as zero; line 61 implies regrowth time is inside the figure. Say what the number excludes.
- inquiry.json:277 (perustele model) "1{,}2·10^9 g = 1200 t" and :343 (tarkistus-2 check) "seitsemän litraa noin 16 kg" — conversion by substitution ($\cdot 10^{-6}\,\text{t}$); use 7,2 l (7 · 2,2 kg = 15,4 kg).
- inquiry.json:260 — mistake 49: keeping GWh gives 0,049 t (49 kg), so the feedback mislabels the slip; reword or set 0.049. inquiry.json:314 "ozoni-" → "otsoni-". Sig-fig reasons treat 820 as 3 figures but 490 as 2.

## Checked
- IPCC AR5 WG III Annex III medians (coal 820, gas 490, biomass dedicated 230, PV 41/48, hydro 24, nuclear 12, wind 11/12), IPCC 2006 petrol 69,3 g/MJ, NOAA 2023 ~420 ppm, pre-industrial 280 ppm, −18 → +15 °C: correct (from the published tables; no web lookup this run).
- Greenhouse mechanism (absorb, re-emit, part down; enhancement by CO2/CH4) right at FY2 level; no Stefan–Boltzmann or energy-balance model.
- m = e · E correct, in scope; 1 kWh = 3,6 MJ by substitution.
- Worked example: symbolic first, conversion by substitution, 2,4 t, check and 58 kg / 41× correct.
- lesson-answers.py: 17 values recomputed, all match.
- Inquiry numerics (820 kg, 49 000 t, 16 kg, 43 200 g, kWh²/g argument) correct.
- All correct options and feedback physics otherwise right.
- Emissions bars to scale (0,44 px per g/kWh); greenhouse figure marked not to scale.
- No ×; written division as colon; calculations in LaTeX.
