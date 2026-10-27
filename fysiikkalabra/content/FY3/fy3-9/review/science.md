VERDICT: PASS
CONTENT-HASH: 750672bef3a3dce1

## Blocking

## Polish
- solutions.md:75 (L2-03, Kuvaajan lukeminen) — still open from round 2: "eli sen kulmakerroin on näiden arvojen keskiarvo" says the mean of the point-wise pV values (2002 kPa·ml) is the slope of the best line through the origin, which is 2009 kPa·ml by least squares. Both give 2,0 J, so the answer is right. — Fix: "kulmakerroin on likimain näiden arvojen keskiarvo".
- solutions.md:79 (L2-03, Vastaus) — still open: the two-figure count follows the rule. But each pressure is read to 1 kPa (66 ± 0,5 kPa ≈ 0,8 %), so the data would support 2,01 J. Optionally say in one clause that the counting rule is what is applied.
- inquiry.json check-2 solution, Järkevyys — still open: "3,6/0,03 = 120" repeats the substitution. The comparison with 101 kPa is the real check and is enough on its own.

## Checked
- Round-3 diff (git 6c0c6d3..HEAD): only solutions.md:72, 75 and 77 changed. The V, pV and 1/V lists are now split into separate formulas. Every number, unit and decimal comma is the same as before, and the semicolons outside math do not change the meaning. The p list on line 72 is still one formula; that is a layout matter.
- Full pass: one script recomputed all 12 exercise answers. They match answers.py and exercises.json; the largest difference is 1,0 % (L2-01 2,02 → 2,0, inside the tolerance).
- L2-03: pV = 2030; 1987,5; 2010; 1980; 2025; 1980 kPa·ml. The sum is 12 012,5 (written 12 013), the mean 2002 and least squares 2009. The 1/V column is correct to three figures.
- The principles fit, with a correct reason for each: Boyle (L1-01/02/03, L2-01, L3-01, L3-03), isobaric (L1-04, L2-04) and isochoric (L1-05, L2-02, L3-02). The unknown is solved in symbols before substitution in every solution.
- Conversions are right: bar→kPa, kPa·ml→J, ρgh = 196,2 kPa, °C→K, and gauge→absolute in L3-02 and L3-03. The rounding reasons name the limiting datum. Differences follow NOTES §2: 90 °C, 890 m³, 202 kPa, 29,9 cm.
- The reasonableness checks are real ratio estimates, and the side estimates are right: 7 kN on the freezer lid, about 40 min of SCBA air, 1,8 m³ real-gas volume, 24 % of the hot air expelled.
- Worked example: 1,036 l → 1,0 l, limited by 0,80 l and 78 kPa. Both pV values are 80,8 kPa·l.
- inquiry.json: siirto 1,07 l (the inverted-ratio mistake gives 2,10). Ruisku pV is 5040–5050, and the 30 ml row is 5430. Pred-1 200 kPa / 5,00 J; pred-2 60,2 ml and 0,171 ml/K; virhe 250 kPa; kertaus 30 N.
- Exit ticket: 160 kPa and 308/280 = 1,1.
- sim.js, the figures and the experiment setups have not changed since the round-2 pass (pV/T is constant, exp-1 locks mode and Tc, exp-2 locks mode). The content hash was the same at the start and the end of this review.
