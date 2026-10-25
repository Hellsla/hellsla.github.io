VERDICT: PASS
CONTENT-HASH: cde315864fcce489

## Blocking

## Polish
- lesson.md:61 — the energy balance (P_tulo = P_lähtö) and E = Pt are used throughout (L1-04, L1-05, siirto, worked example) but never stated in display LaTeX with their symbols named in Kaava — add them as display formulas there.
- lesson.md:33 — "noin viidesosa siitä imeytyy ilmakehään" while the Tutki table model puts all absorbed sunlight into the surface; the tase text says this, but check-2 then has the atmosphere absorb only surface radiation (290 W/m²) — fine as a model, though one line in check-2 saying "mallissa" would keep it consistent.

## Checked
- Round-1 polish all addressed: P = UAΔT condition stated (steady temperatures), "pääosin läpi", L2-04 framed as hypothetical, convection burner moved under the rising side, check-2 now has downward 150 > upward 140 W/m² with correct reason.
- All 12 exercise answers recomputed independently; identical to answers.py; rounded "Vastaus" values (430, 240, 150, 210, 980 …) within 2 % tolerance.
- Worked example: 734 W + 720 W ≈ 1,45 kW, 34,9 kWh ≈ 35 kWh; symbolic before substitution; 1/6 area vs ~5,9× U consistent.
- Energy-balance table: σ(255 K)⁴ ≈ 240, σ(288 K)⁴ ≈ 391 W/m²; tase-ennusta 150 W/m² with mistakes 390, 630.
- Imbalance table: 3,6 / 1,2 = 3,0 K; rows 236,4 → 237,6 → 238,8 consistent with 1,2 W/(m²·K); mistakes 3,6 and 4,32.
- check-2: 240 − 100 = 140 W/m²; atmosphere 290 in = 150 + 140 out.
- siirto 0,4608 kWh (mistakes 0,749, 460,8 Wh); virhe 45 W; exit ticket 300 W; retrieval item ΔU = 0 correct.
- Predictions and all feedback physically sound (no conduction to vacuum, warmer body radiates more, warming stops at new balance).
- Magnitudes realistic: CO₂ 280→420 ppm, ~1 W/m² imbalance, 90 % to oceans, U-values, COP 2,8, thermos 90→70 °C.
- Figures qualitatively correct (three modes, energy balance arrows, wall profile 21 → −15 °C with largest drop in insulation); hash identical at start and end.
