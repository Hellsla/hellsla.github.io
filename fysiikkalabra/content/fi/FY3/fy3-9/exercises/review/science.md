VERDICT: PASS
CONTENT-HASH: 2c6d0cf2ab541ab3
SCOPE: delta added-exercise from 9d2994a56073576c base 71f5784fca44

## Blocking

## Polish
- exercises/solutions.md (fy3-9-L2-10, Mallivastaus b) — "Pisteet asettuvat … mittausepävarmuuden rajoissa origon kautta kulkevalle suoralle" sits a little uneasily with the first point. It lies 51 kPa above the line, beyond the stated ±30 kPa; the sim's noise-free value there is about 777 kPa, so the reading is +47 kPa. The paragraph handles it correctly with the guardrail's outlier sentence. Optional: "kuutta pistettä seitsemästä" or "kun lukemaa ei toisteta", so that the two sentences agree.

## Checked
- Recomputed from the seven points: k = Σ(pT)/Σ(T²) = 3,924 kPa/K. The free fit gives a slope of 3,84 kPa/K and an intercept of 32 kPa. The p/T values per row are 4,18 … 3,96 kPa/K and the residuals +51; −2,7; −7,2; −18,3; −8,2; −15,5; +18,8 kPa. Every number in the solution is right.
- Check point: k · 601 K = 2358 kPa against the read 2346 kPa, a difference of 12 kPa (0,53 %) and inside ±30 kPa. The sim's noise-free value is 2369 kPa. The extrapolation is named: 90 K above the measured range.
- Answer field: p₂/p₁ = T₂/T₁ = 450/300 = 1,50 for every k, as the facts require. Tolerance 0,02, unitless. The reasonableness check, model 1177 → 1766 kPa and measured 1766 : 1170 = 1,51, was recomputed.
- Setup isolates T: volume held, N fixed (no pumping), kPa and K units, about 100 heavy particles, gauge fluctuation noted with a "middle reading" instruction. All match the verified sim facts. The example is dated, and the solution says the student's own k will differ.
- Law and conditions: isochoric and p ∝ T for a thin gas far from condensing (guardrail), with the ideal-gas sim versus a real gas stated. The fit through the origin is justified physically, plotted with axes from zero and checked by the intercept. The slope is taken from distant line points, not neighbouring raw points (guardrail).
- d) particle model: faster particles hit more often and harder, and the number density is unchanged. Temperature is tied to the mean translational kinetic energy for an ideal gas, right.
- Notation (p₁/T₁ = p₂/T₂, kelvins) as in the brief. Within FY3 central contents and its experimental work.
- Hash the same at start and end.
