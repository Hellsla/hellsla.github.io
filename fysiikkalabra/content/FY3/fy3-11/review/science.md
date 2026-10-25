VERDICT: PASS
CONTENT-HASH: 8ade50b5ff839a29

## Blocking

## Polish
- inquiry.json siirto solution — "≈ 23 MW" while the stored answer is 22,5 MW (inside the 3 % tolerance) — write "= 22,5 MW ≈ 23 MW" so the step matches the answer.
- solutions.md fy3-11-L1-03 — Vastaus "37 %" while answer is 37,2 % and Sijoitus shows 37,2 % — give "37,2 % ≈ 37 %" for consistency (same for L1-05 21,7 → 22 %).
- lesson.md Ydinajatus §3 — "suurempi lämpötilaero → suurempi osa työksi" is right qualitatively; a half-sentence that the hot source's temperature matters (higher steam temperature) would avoid over-reading "difference" alone.

## Checked
- answers.py vs my own formulas in one script: all 12 exercise answers agree with exercises.json within tolerance (12,0 kJ; 172 J; 37,2 %; 170 kJ; 21,7 %; 41,0 %; 9,0 %; 500 J; 720 kW; 120 MW; 9,6 MWh; 12,0 kW).
- Magnitudes: 1 g steam at 100 °C, 101 kPa expands ≈ 1,70 l (ideal gas); OL3 4300/1600 MW; chainsaw 2,8 kW; car 12 kW at 80 km/h, 54 kWh fuel, EV ≈ 17 kWh — all realistic.
- Sign convention: W = pΔV (by gas) vs ΔU = Q + W (on gas) stated in Ydinajatus and Kaava; kertaus, virhe, L2-03 use −pΔV correctly (250 J, 500 J, 500 J).
- Worked example: symbolic η = P_hyöty/P_1, P_2 = P_1 − P_hyöty first; 38 %/310 MW and 88 %/60 MW correct.
- Inquiry numbers: pred-1 (600→500 MW, "kuudesosa"), pred-2, pred-3 (300/550/150 MW, 85 %), siirto 22,5 MW with mistakes 31,5 and 2,57, check-2 450 J with mistakes 450 000 and 750, exit ticket 100 J, 18/42 kW.
- Experiments run through simAdapter in Playwright (reset → set initial → vary): exp-1 gives Puse/Pwaste 400/600 and 500/500; exp-2 with η locked 30 % gives 300/0/700/30 %, 300/550/150/85 %, at max 65 %: 95 %. Initial heatShare 0 survives the mode preset (set order mode first).
- sim.js: Puse = ηPin, Pheat = hPin, Pwaste = rest, ηtot = η + h, cap 95 %; pump Pout = ε·Pel, Pambient = Pout − Pel; arrow widths ∝ power (screenshot 400/600 MW).
- SVG figures: engine arrows 60 = 24 + 36 (W = 40 % of Q1); pump arrows 60 = 20 + 40 (ε = 3); (V, p) rectangle = pΔV.
- check-3 model answer and criteria: second law, Q1 = W + Q2, friction vs principle, CHP 85–90 % — correct.
- Scope: W = pΔV only at constant pressure, no cycles, no Carnot formula — inside FY3.
