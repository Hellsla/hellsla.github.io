VERDICT: PASS
CONTENT-HASH: a2773c26ca9d21a4

## Blocking

## Polish
- lesson.md:34 — lämpökerroin is defined only in words, yet L3-02 needs it as a formula — add a display formula ($\varepsilon = Q/W$, $Q = Q_\text{ulko} + W$) with symbols named; solutions.md:84 uses ε, which the lesson never introduces.
- lesson.md:41 — $W$ here is work *by* the gas, but *on* the gas in $\Delta U = Q + W$ (line 6) — add one sentence contrasting the two conventions.
- sim.js:22 — automoottori efficiency slider reaches 60 %, unrealistic for a car engine (≈ 40 % max) — cap it near 45 % for that mode.

## Checked
- All 12 answers recomputed with my own formulas: match answers.py and exercises.json; rounded Vastaus values (37 %, 22 %, 12 kW) stay inside the 2 % tolerance.
- Exit ticket: 100 J; 18 kW + 42 kW; heat-pump reasoning correct.
- Signs: first law with W = −pΔV used correctly (L2-03 ΔU = +500 J).
- Magnitudes realistic: steam 1,70 l/g (ideal gas 1,71); OL3 4300/1600 MW; condensing 40 %, nuclear 35 %, car 28–30 %, CHP 85–90 %, steam engine 9 %; EV 17 vs 54 kWh.
- Worked example symbolic first; 38 %/310 MW and 88 %/60 MW correct; second law qualitative, no Carnot.
- Energy-flow figure: Q₁ 60 px = W 24 px + Q₂ 36 px, η = 0,40. p–V figure: horizontal line at p, V₁→V₂, shaded rectangle = pΔV, arrow in expansion direction.
- Sim (Playwright, canvas in view): lauhde 1000/40 % → 400 + 600; 1500/25 % → 375 + 1125; CHP 300 + 550 + 150 (85 %), capped 350 + 600 + 50 (95 %), 200 + 100 + 700; car 18 + 42, 42 + 78. Balance residual 0 everywhere; etaTotal = (Puse + Pheat)/Pin.
- Heat pump: 1 kW, cop 3 → 3 = 1 + 2; 2,5 kW, cop 4,2 → 10,5 = 2,5 + 8,0; Pout/Pel = cop.
- Arrow widths: w = P·scale, scale·total = 210 px in every mode; screenshot bands 2,5 : 8,0 kW ≈ 50 : 160 px.
- Nopeus 0,4/1/2: simState identical except speed.
