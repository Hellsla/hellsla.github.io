VERDICT: PASS
CONTENT-HASH: 241b72b62e122e9c

## Blocking

## Polish
- inquiry.json (siirto prompt) — "Toinen ryhmä käytti isompaa pulloa" suggests that bottle size raises the pressure. Pressure depends on the amount of gas per volume. — Say that the bottle was filled to a higher pressure.
- solutions.md:15 (L1-02 Järkevyys) — "lukujen 105 kPa ja 127 kPa suhde": the slope comes from their difference, not their ratio. — Write "erotus 22 kPa 60 asteen välillä".

## Checked
- Round-1 blocker fixed: L2-01's check now blames the two points' measurement error, magnified by the 270 °C extrapolation. This is correct: rounding alone (±0,005 bar) moves θ₀ by about ±9 °C, and the data are 17 °C off.
- New source/source_note fields on suora and epavarmuus correctly label the example data as simulated.
- All 12 exercise answers were recomputed independently and match answers.py and exercises.json within tolerance (−272,2; 0,3667; 5,25; 13; 0,893; −256,0; 14,1; −270,0; 18; 20,3; 28,19; 1,86).
- Least squares gives k = 0,3667 kPa/°C, p₀ = 101,26 kPa and θ₀ = −276,2 °C, which agree with the best line, points A and B, and the worked example (−276,0 °C).
- Extreme lines 100,1 + 0,387θ and 102,3 + 0,347θ give −258,7 / −294,8 °C and Δθ₀ = 18 °C. The interval contains −273,15 °C.
- Inquiry numbers: suora −275,8 (mistake −295,9), siirto −276,9 (−306,9), tarkistus-2 −282,9 (−297,9), virhe −276,1 vs −316, kertaus 1,068, exit 0,36 and −282…−258.
- s₂ in the SVG is p ≈ 98,9 + 0,42θ and misses the bars at 10, 70, 85 and 100 °C. s₁ ≈ 100,1 + 0,387θ.
- The to-scale formula figure checks out: θ₀ markers at −276, −259 and −295 °C, and the points and lines map correctly.
- L3-02: N₂ at 0,366·T kPa meets its vapour-pressure curve at ≈ 67 K, as stated.
- Formulas, their linear-range condition and the liquefaction limit are stated; everything is within FY3 scope.
