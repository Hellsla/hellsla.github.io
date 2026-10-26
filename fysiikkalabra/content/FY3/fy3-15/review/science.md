VERDICT: PASS
CONTENT-HASH: 07b47e2ad7b7704c

## Blocking

## Polish
- solutions.md (L1-04 Järkevyys) — "kun sähkö ei ole hukassa" reads oddly. The 60 % also includes generator losses, not only flue gas and condenser. — For example: "sähköksi muuttuvan 40 %:n lisäksi loput 60 % siirtyy lämpönä ympäristöön, suurin osa lauhduttimen kautta mereen".
- inquiry.json (tyypit) — wind 0,40–0,45 is a peak power coefficient (the Betz limit is 0,59). — Write "parhaimmillaan noin 0,40–0,45".

## Checked
- Round-1 blocker fixed: johtopaatos now says "248 MW eli noin puolet polttoainetehosta". 248/500 = 0,497, correct. The same wording in the ketju solution and pred-1 feedback is consistent.
- New source/source_note fields on ketju and kaukolampo label the example-plant figures correctly.
- All 12 exercise answers were recomputed independently and match answers.py and exercises.json within 2 % (90,16; 42,0; 4,20; 480; 90,0; 108,66; 43,08; 166,7; 7,160; 205,5; 13,64; 87,72). The sanity checks hold: 63 %, 4000 t/vrk, 7 m³/s, 40 % and 88 %, 273 wagons, 263 and 111 kWh.
- Worked example: P₁ = 546, P₂ = 240,2, P₃ = 228 MW, η = 0,380, P_h = 372 MW. The condenser gets 306 MW (> 50 %), the boiler loses 54 MW and the generator 12 MW.
- Inquiry numbers: ketju 248,4 MW (mistakes 270, 211,6, 288,4, 300), kaukolampo 48 MW (280, 168, 240), kaukolampo-tarve 130 MW (160, 120, 150), 40/232 = 0,17, virhe 0,342 and 540 MW, siirto 8,64 MW (20, 164; 5,6 % of 155,5), check-2 216 MW (252, 324), kertaus Q₂ = 520 MJ, exit 0,432 and 85 % / 15 MW.
- Misconception: product 0,400 vs mean 0,78, correct.
- To-scale SVGs check out: Sankey at 40 px per 100 MW (500 → 40 + 248,5 + 11,5 + 200), stacked CHP chart (160→120 electricity, 232 heat, 240→48 waste at 0,6 px/MW) and chain bars (500/460/211,6/200 at 0,5 px/MW).
- Correct options and feedback physics are right: the heat-engine limit, why a hotter condenser lowers turbine work, different denominators for wind, hydro and solar, and the different value of heat and electricity.
- Formulas η = P_hyöty/P₀, chain product, η_kok and P_L = c q_m ΔT are within FY3 contents, and their conditions are stated.
