VERDICT: PASS
CONTENT-HASH: 87ecc45640f9156a

## Blocking

## Polish
- sim.js:114 — `simState.eta` reads 40 at phase `ylhaalla` (W/Q₁ while only heated, W = Wₖ); not shown in the readout, but a row recorded there in exp-2 would show 40 % — report η = 0 (or omit) until `done`.
- inquiry.json siirto solution — "≈ 23 MW" fits the 2-figure data but answer is 22.5; write "= 22,5 MW ≈ 23 MW" so the stored answer is visible.
- inquiry.json exp-2 — lesson says cycles are not calculated, yet the table records η; fine as model readings, but the intro could say η is only for comparing A and B, not a formula to learn.
- lesson.md Ydinajatus "Mitä suurempi lämpötilaero…" — strictly the ratio to T₁ matters; acceptable at this level, could add "kuuman lähteen lämpötilaan nähden".

## Checked
- Sim run in Playwright: Q = 500 J → ΔV 1,00 l, Wₖ 200 J, ΔU 300 J; A: Q₁ = Q₂ = 500 J, W = 0; B (p₂ = 100 kPa): Q₁ 650, Q₂ 550, W 100 J = areaNet, η 15,4 % (readout 15 %); Q = 1000 J, p₂ = 40: 1240/920/320 J, bars fit jmax; all equal my own isochoric/isobaric monatomic formulas, dUcycle = 0.
- B weight bookkeeping: upper block (p₁ − p₂)A lifted ΔV/A from low to high shelf = (p₁ − p₂)ΔV; screenshot shows shelves, hatched return area, net rectangle correctly.
- pred-1 (750 J → 1,0→2,5 l, 300 J), exp-1 Q = ΔU + Wₖ rows, exp-2 area question and every pred-2 feedback number.
- kertaus 250 J (W/Q = 0,375, a valid ideal-gas Cp); virhe 240 J / 360 J (monatomic-consistent); L2-03 W/Q = 2/7 (air) — consistent.
- Design task: 2000, 1250 (562,5 MW el.), 800 MW (pump 60 MW el., 180 MW heat, 120 MW from wastewater, plant 320 MW heat), 15 % plant loss = 120 MW; mistakes 941, 667 correct values.
- All 12 answers.py values recomputed independently and match; solutions symbolic first; L1-02 steam volume (1,70 l/g) and L3-03 side numbers (43 kW, 54 kWh, 17 kWh) realistic.
- Worked example 38 %, 310 MW, 88 %, 60 MW; exit ticket 100 J, 18/42 kW; check-2 450 J; siirto 22,5 MW.
- SVG figures: W/Q₁ = 24/60 = 40 %, Q₁ = W + Q₂ widths; heat-pump arrows 20 + 40 = 60 = 3·E_s.
- Sign conventions: Wₖ = −W of fy3-5 stated; ΔU = Q − Wₖ used consistently.
- Scope: cycles are shown qualitatively; no exercise or check asks for a cycle calculation.
