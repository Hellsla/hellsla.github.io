VERDICT: PASS
CONTENT-HASH: 9a0ede1d5297ee3f

## Blocking

## Polish
- inquiry.json:263-283 (check-2) — the toy atmosphere emits 200 W/m² up but only 150 W/m² down; a real atmosphere (warmer at the bottom) emits more downward (about 340 W/m²). The balance arithmetic is right, but the asymmetry points the wrong way — either note that the numbers are illustrative for the energy bookkeeping only, or choose values with downward ≥ upward (needs the table's surface terms to change accordingly, e.g. include convection/evaporation).
- exercises.json:72 (L2-04) — attributing a whole 1 %-point drop in planetary albedo to Arctic sea-ice loss overstates it (an ice-free Arctic is estimated at a few tenths of W/m²); phrase it as a hypothetical albedo change from "lumen ja jään väheneminen" or say the 1 % is an exaggerated assumption.
- lesson.md:55-57 — state the condition of P = UAΔT: steady state (temperatures on both sides constant) through a uniform building part.
- lesson.md:31 — "päästävät auringonvalon lähes esteettä läpi": about a fifth of sunlight is absorbed in the atmosphere; "pääosin läpi" is safer.
- lesson.md:17 (konvektio SVG burner) — the heater spans the whole pot bottom, so the drawn one-sided circulation has no visible cause; shorten the burner to the rising (left) side.

## Checked
- All 12 exercise answers recomputed independently; match answers.py and exercises.json (max diff 0.2 %); rounded answers stay inside tolerance.
- Worked example: 734 W + 720 W ≈ 1,45 kW, 34,9 kWh; symbolic first; "kuudesosa / lähes kuusinkertainen" consistent.
- Energy-balance table: σ(255 K)⁴ ≈ 240 W/m², σ(288 K)⁴ ≈ 391 W/m²; surface 240+150 = 390 balances; check-2 atmosphere 350 in = 350 out.
- Imbalance table: forcing 3,6 W/m², λ = 1,2 W/(m²·K) → 3,0 K (realistic CO₂-doubling magnitudes); mistakes 3,6 and 4,32 sensible.
- Transfer task 0,4608 kWh, mistake 0,749 (ΔT = 26 K), 460,8 Wh; error-spotting 45 W; exit ticket 300 W.
- Predictions: correct options and every wrong-option feedback physically sound (no conduction/convection to vacuum; warmer body radiates more; warming continues until balance).
- Magnitudes: CO₂ 280→420 ppm, ~1 W/m² imbalance, 90 % to oceans, 0–700 m ocean mass 2,6·10²⁰ kg, U-values, COP 2,8, thermos 90→70 °C all realistic.
- Figures: conduction/convection/radiation and wall temperature profile (largest drop in insulation, 21 → −15 °C) qualitatively correct.
- Content hash identical at start and end.
