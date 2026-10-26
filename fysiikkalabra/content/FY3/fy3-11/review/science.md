VERDICT: PASS
CONTENT-HASH: 4d49682939903523

## Blocking

## Polish
- solutions.md:22, 38 — L1-03 and L1-05 end in "37 %" and "22 %" while exercises.json stores 37.2 and 21.7 and the substitution line shows the three-figure value (inside tolerance); make the stated and stored values agree.
- lesson.md:175 — the relative temperature difference sentence: add "(lämpötilat kelvineinä)" so no one compares °C values.

## Checked
- All 12 answers recomputed in one script: all match; L1-02's 1,70 l agrees with the ideal-gas volume of 1 g steam at 100 °C, 101 kPa (1,71 l).
- Formulas W_k = pΔV (constant p stated), ΔU = Q − W_k with the link W = −W_k to fy3-5's form, W = Q₁ − Q₂, η = W/Q₁, Q_sisälle = Q_ulko + E_s, ε = Q_sisälle/E_s; cycles kept qualitative as the slot's scope note requires.
- Worked example: symbolic first; 38 %, 310 MW, 88 %, 60 MW correct; CHP reasoning (higher condensing temperature) correct.
- Figures: heat-engine arrows 60 = 24 + 36 and heat-pump arrows 20 + 40 = 60 are to scale as their aria-labels claim; piston and (V, p) figures say they are not to scale.
- sim.js: monatomic ideal gas, ΔV = 2Q/(5p₁), A gives Q₂ = Q and W = 0; B gives the isochoric heats (3/2)V(p₁ − p₂) and (5/2)p₂ΔV, Q₁ − Q₂ = (p₁ − p₂)ΔV equals the weight moved between shelves; limits stated in the model box.
- inquiry.json model values recomputed: exp-1 rows (Q 500/750/1000 → ΔV 1,0/1,5/2,0 l, W_k 200/300/400 J, ΔU 300/450/600 J); exp-2 A (Q₁ = Q₂ = 500 J, W = 0) and B (Q₁ 650, Q₂ 550, W 100 J, η 15 %); every prediction's correct option and every feedback number agree.
- Experiments isolate their variable: exp-1 varies Q with return mode locked (p₂ irrelevant to heating); exp-2 varies the return mode with Q and p₂ locked; simState gives dV, dU, Q1, Q2, W, eta (eta only when done).
- Numeric items: kertaus 250 J, virhe 360 J, check-2 450 J, siirto 22,5 MW, suunnittele 800 MW (pump 60 MW, 180 MW heat, 120 MW from wastewater); every listed mistake value reproduces the error its feedback names.
- Magnitudes realistic (OL3, condensing 40 %, nuclear 35 %, car 12 kW, CHP 85–90 %).
- Exit ticket: 100 J, 18 kW and 42 kW, heat-pump energy balance correct.
