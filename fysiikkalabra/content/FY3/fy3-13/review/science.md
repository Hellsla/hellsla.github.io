VERDICT: FAIL
CONTENT-HASH: 6c8fd0c792df2e19

## Blocking
- solutions.md:47 — L2-01's check says the gap between −256 °C and −273,15 °C "johtuu kolmen numeron lukemista". False: ±0,005 bar on each reading gives θ₀ only in −266 … −246 °C; the data themselves are off (an ideal gas at 1,36 bar, 95 °C reads 1,064 bar at 15 °C). Fix: blame the measurement error of the two points, magnified by a 270 °C extrapolation (or use 1,06 bar).

## Polish
- inquiry.json:284 — the siirto item's "Toinen ryhmä käytti isompaa pulloa" implies bottle size sets the higher pressure; it depends on gas per volume — say it was filled to a higher pressure.

## Checked
- All 12 answers recomputed in one script: all match; L3-02's 67 K agrees with N₂ vapour pressure.
- Formulas p = p₀ + kθ (valid over the measured range), two-point k, θ₀ = −p₀/k = θ₁ − p₁/k, Δθ₀ = half-range; within the slot's goal.
- Least-squares line k = 0,3667 kPa/°C, p₀ = 101,26 kPa, θ₀ = −276,2 °C, residuals ≤ 0,57 kPa; the drawn best line and points A, B lie on it.
- Brute-force search confirms the printed extreme lines are the true steepest and shallowest through all bars: θ₀ −258,97 / −295,19 °C, Δθ₀ = 18,1 °C.
- Candidate line s₂ (p = 98,9 + 0,42θ) misses exactly the bars at 10, 70, 85 and 100 °C.
- Figures claimed to scale are: points, ±1 kPa bars, line ends and θ₀ crossings reproduce.
- Inquiry numbers: suora −276 °C (mistake −296), virhe −276 vs −316 °C, siirto −277 °C (mistake −307), tarkistus-2 −283 °C (mistake −298), kertaus 313/293 ≈ 1,07.
- Correct options and all feedback are right physics; liquefaction and model limits are named.
- Exit ticket: 0,36 kPa/°C, interval −282 … −258 °C contains −273,15 °C.
