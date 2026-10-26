VERDICT: FAIL
CONTENT-HASH: 7e12e856a6b7b3cc

## Blocking
- inquiry.json:241 (johtopaatos `model`) — "248 MW eli lähes puolet kattilan tehosta" is wrong: 248 MW is 54 % of the boiler output 460 MW (more than half), and 49,7 % of the fuel power 500 MW — write "248 MW eli noin puolet polttoainetehosta" (or "yli puolet kattilan tehosta").

## Polish
- solutions.md:31 (L1-04 Järkevyys) — "kun sähkö ei ole hukassa" reads oddly — e.g. "sähköksi muuttuvan 40 %:n lisäksi loput 60 % siirtyy lämpönä…".
- inquiry.json tyypit — wind 0,40–0,45 is a peak value of the power coefficient (Betz limit 0,59); "noin 0,40–0,45 parhaimmillaan" would be more exact.

## Checked
- One Python run recomputed all 12 exercise answers; answers.py matches (90,16 / 42,0 / 4,20 / 480 / 90,0 / 108,7 / 43,08 / 166,7 / 7,160 / 205,5 / 13,64 / 87,72) and every stated answer is within 2 %.
- Formulas η = P_hyöty/P₀, P_h = P₀ − P_hyöty, η = η₁η₂η₃ (derived by substitution), η_kok, P_L = c q_m ΔT with symbols and units; heat pump ε (L3-03) is from the prerequisite chapter.
- Sankey: 500 → 460 → 211,6 → 200 MW, losses 40/248/12 MW, band widths at 40 px per 100 MW all to scale.
- Stacked CHP chart: P_s 160 → 120 MW, P_k 0 → 232 MW, waste 240 → 48 MW, axes and polygon vertices to scale.
- Bar chart P₀…P₃ and dashed loss boxes to scale (0,5 px/MW); η₃ = 0,945 gives 199,96 MW.
- Worked example: 546, 240,2, 228 MW, η = 0,380, P_h = 372 MW, condenser 306 MW, generator loss 12 MW; symbolic first.
- Misconception: mean 0,775 ≈ 0,78 vs product 0,40.
- inquiry numerics: ketju 248 MW with mistakes 270/211,6/288,4/300; kaukolampo 48 MW with 280/168/240; tarve 130 MW with 150; siirto 8,64 MW with 20/164 and 155,5 MW base; virhe 0,342/342 MW and 540 MW condenser; check-2 216 MW with 252/324; kertaus Q₂ = 520 MJ, η = 0,35.
- Predictions: correct options (steam cycle; Cem, 40 MW per 232 MW ≈ 0,17) and the wrong options' physics (transmission, generator, turbine back-pressure) are right.
- Exit ticket 0,432, 85 %/15 MW; hash identical at start and end.
