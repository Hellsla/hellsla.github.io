VERDICT: PASS
CONTENT-HASH: 1fd418b2cad4dd9b

## Blocking

## Polish
- inquiry.json:149 (suora, Vastaus) — the figures are justified by "vähennys 20,0 − 296", a step the solution never shows (it goes through p₀ = 101,26 kPa and −p₀/k) — justify from the shown step: k has three figures, so −p₀/k has three.
- inquiry.json:307 (siirto, Järkevyys) — "Suuremmassa pullossa paine ja kulmakerroin ovat suuremmat" implies that a larger volume raises the pressure, against p ∝ n/V and the solution's own "koolla ei ole väliä" — say "tämän ryhmän paine…".
- solutions.md:59 (L2-01) — "yksi bar vastaa noin 270 °C": 80/0,310 ≈ 258 °C per bar; it is 1,050 bar that matches ≈ 271 °C.
- solutions.md:119 (L3-03) — θ₀ came out too warm, so the slope was too steep. An air leak out of the bottle or the bottle expanding gives a shallower slope and a colder θ₀ — name causes that steepen it (moisture evaporating, a thermometer reading low when hot). Also 11,15 has four figures; it is 6,00 that limits.
- solutions.md:19 (L1-02) — "0,36…0,39 kPa/°C muissa tämän luvun kokeissa" is not true (siirto 0,433, L3-01 0,41) — widen the range or drop the claim.

## Checked
- All 12 exercise answers recomputed in one script: they agree with answers.py and the JSON, and each stays inside its tolerance after rounding.
- Inquiry numbers agree: suora −275,8, siirto −276,9, tarkistus-2 −282,9, Δθ₀ 18,08 (exact 18,11), virhe −276,1, 313/293 = 1,068.
- Least squares gives k 0,3667 and p₀ 101,26, so the best line is right. Residuals are at most 0,52 kPa, so the option "kaikki alle 1 kPa:n päässä" holds.
- Brute force over the lines through bar ends: the steepest and shallowest feasible lines are exactly the stated ones. s₂ misses the bars at 10, 70, 85 and 100 °C, as the feedback says.
- SVG coordinates of figures 2–6 and 8 decoded: the points, lines and marks are to scale.
- Worked example: seven stages, symbolic first. The rounding follows the difference of the extreme zeros (36 → two figures, NOTES §2), and the check is real.
- L2-03: gauge-to-absolute conversion and the 5,5 °C gauge-zero check are right. L3-02: N₂ condensing at about 67 K at about 25 kPa agrees with its vapour-pressure curve.
- Exit ticket, predictions and feedback are correct. Scope is FY3.
- The hash was the same at the start and at the end.
