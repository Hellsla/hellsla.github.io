VERDICT: PASS
CONTENT-HASH: d34a6cbbb0d46756

## Blocking

## Polish
- inquiry.json:exp-2 — the table shows W = 0 J and η = 0 % as "0,00" while other cells round to integers (fi() of 0); purely display — none needed for physics.
- solutions.md:L1-03, L1-05 — "Vastaus" rounds to 37 % / 22 % while exercises.json holds 37,2 / 21,7; both inside tolerance — optionally state 37,2 % / 21,7 % for consistency with the three-figure convention.
- lesson.md:Ydinajatus §3 — "lämpötilaero kuuman lähteen lämpötilaan nähden" is the Carnot ratio (T₁ − T₂)/T₁; it holds only for absolute temperatures — optionally add "(kelvineinä)".

## Checked
- Hash d34a6cbbb0d46756 at start and end; answers.py output matches all 12 exercise answers, my own recomputation (12,0 kJ; 172 J; 37,2 %; 170 kJ; 21,7 %; 41,0 %; 9,0 %; 500 J; 720 kW; 120 MW; 9,60 MWh; 12,0 kW) and every solution's symbolic-then-numeric chain, incl. L3-03 side numbers (43 kW, 54 kWh, 15 kWh, 17 kWh).
- Worked example: 38 %, 310 MW; 88 %, 60 MW.
- Koe 1 (Playwright): Q = 500/750/1000 J give ΔV = 1,00/1,50/2,00 l, ΔU = 300/450/600 J; readout shows p, ΔV, Q, ΔU and no W_k; answer pΔV = 400 J; mistakes 400 000 (Pa·l), 600 (p·V₂ = 200·3,0, = ΔU), 1000 (Q) all correct; solution's 2/5 share right.
- Koe 2 (Playwright): eta absent from simState in alku, ylhaalla and mid-return; record refused there ("ei anna mitattavaa arvoa"); A: Q₁ = Q₂ = 500 J, W = 0, η = 0; B: Q₁ = 650, Q₂ = 550, W = 100 J, η = 15,4 %; switching paluu resets and removes η; Qin and p₂ locked; no page errors.
- pred-1/pred-2 feedback numbers (200, 300 J; 500, 550, 650, 100 J) and exp-2 question (net area (p₁ − p₂)ΔV = 100 J) match the sim.
- suunnittele: P = (P_l + 3P_e)/(0,40 + 1,35) = 800 MW; P_pumppu = 60 MW, pump heat 180 MW (120 MW from waste water), plant heat 320 MW; 2000, 1250, 941, 667 MW mistakes correct; losses 120 MW = waste-water heat; 40 % of option 1.
- siirto: (ε − 1)P_pumppu = 2,5 · 9,0 MW = 22,5 MW; mistakes 31,5 and 2,57 MW correct.
- virhe 240 J/360 J; kertaus 250 J; check-2 450 J; exit ticket 100 J, 18 kW/42 kW.
- sim.js energy bookkeeping: Q₁ − Q₂ = W = (p₁ − p₂)ΔV, ΔU_cycle = 0, areas equal energies.
- Scope: cycles qualitative only, second law stated as experience; sign convention ΔU = Q − W_k tied to fy3-5's ΔU = Q + W.
