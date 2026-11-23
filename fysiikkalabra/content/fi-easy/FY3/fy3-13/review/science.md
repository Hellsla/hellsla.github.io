VERDICT: PASS
CONTENT-HASH: fe78ef8661ba0d10

## Blocking

## Polish
- inquiry.json:62 (ennuste-1, correct option) — the right answer ("paine … on nolla jossakin selvästi 0 °C:n alapuolella") describes the line/ideal model; a real gas liquefies first (lesson.md:125 says so). Its feedback could add "mallin mukaan" / "suoran jatke" so the option does not read as a claim about a real gas.
- lesson.md:286, inquiry.json:329 (tarkistus-1) — interval written "−294 … −258 °C" (from −276 ± 18), while lesson.md:280 and the figure give the limit-line zeros as −295 and −259 °C. Both are fair roundings; one form throughout would avoid a student noticing a 1 °C mismatch.

## Checked
- Model and conditions: rigid closed vessel (V, n constant), thin gas, linear p(θ) only in the measured range, liquefaction and extrapolation stated as limits; absolute zero "pienimmillään", not motion stopping; uncertainty "todennäköisesti", not a guaranteed limit (guardrails: measurement terms, fits, outliers, broken line not a model).
- One script recomputed everything: data LSQ fit k = 0,3667 kPa/°C, p0 = 101,26 kPa, θ0 = −276,2 °C, max residual 0,57 kPa (< 1 kPa, so the aineisto correct option holds); data agree with ideal gas p = 101,3 kPa·(1 + θ/273,15) within ±0,6 kPa.
- Brute-force extreme lines through bar ends: steepest touches 10 and 85 °C (k 0,3867, p0 100,13, θ0 −259,0), shallowest 25 and 100 °C (k 0,3467, p0 102,33, θ0 −295,2) — the lesson's lines are the true extremes.
- Worked example: k 0,367, θ0 −276,02; printed-coefficient zeros −258,66 / −294,81, Δθ0 18,08 → −276 ± 18 °C; sig-fig and rounding reasons right; reasonableness check real.
- suora −275,8 (mistake −296 ✓), epavarmuus 18,1 (mistake 36,1 ✓), siirto −276,9 (−307 ✓), tarkistus-2 −282,9 (−298 ✓), virhe −316 vs −276 ✓, kertaus 313/293 = 1,068 ✓, exit ticket 0,36 kPa/°C and −282…−258 ✓.
- s2 (p = 98,9 + 0,42θ) misses bars at 10, 70, 85, 100 °C exactly as feedback and aria-label say; s1 touches 10 and 85 °C.
- Figures' pixel coordinates decoded: inquiry figures (A 20,0/108,6, B 90,0/134,3; best, s1, s2, limit lines) and the to-scale formula figure (best line zero −276,1 °C, limit zeros −259,0 / −295,2 °C, all seven points) match the data.
- Thermometer and hero pictures: rigid bulb in water bath, θ from thermometer, p from gauge, heat Q in — consistent with text.
- Each prediction/check has exactly one correct option; distractor feedback physically right.
- lesson-answers.py computes the right physics; hash same at start and end.
