VERDICT: FAIL
CONTENT-HASH: 1c47ee655224e3ab

## Blocking
- inquiry.json:116 (aineisto, feedback of the "mutkia" option) — **A, definition**: "poikkeamat vaihtelevat ylös ja alas, joten ne ovat mittausepävarmuutta" calls the deviations themselves the uncertainty. The guardrails keep the terms apart: a deviation is a (random) measurement error, while the uncertainty is the estimate of how large it may be. This lesson's own theory defines it that way (lesson.md:239) — write "joten ne ovat satunnaisia mittausvirheitä, jotka mahtuvat mittausepävarmuuden rajoihin".

## Polish
- inquiry.json:112 (aineisto, feedback of the "poistaa" option) — "kaikki pisteet ovat luotettavia" overclaims. A deviation smaller than the uncertainty gives no reason to reject a point, but it does not prove the point reliable — say "ei ole syytä hylätä yhtään pistettä".
- lesson.md:323 and inquiry.json epavarmuus — the printed steep line 100,1 + 0,387θ gives 103,97 kPa at 10 °C, just under the bar end of 104 kPa (rounding of the exact 100,13 + 0,3867θ). This is harmless, but "koskettaa janan päätä" holds only to 0,03 kPa — print 0,3867 or say "likimain".
- lessons/FY3/fy3-13/answers.py:22 — the key "L2-03-gauge-zero" is not an exercise id in the JSON that "the lint compares with exercises.json". Move it to a comment or to lesson-answers.py.

## Checked
- Recomputed in one script: the best line (0; 101,3)–(100; 138,0) gives k = 0,367 and θ₀ = −276,0 °C (a least-squares fit gives −276,2); the extreme lines give −258,66 and −294,81 °C, so Δθ₀ = 18,08 °C. The steep line touches the bars at 10 and 85 °C and the shallow one at 25 and 100 °C, and every residual of the best line is under 1 kPa. suora −275,8 °C; virhe −316 → −276 °C; siirto −276,9 °C; tarkistus-2 −282,9 °C; kertaus 313/293 = 1,068; s₂ misses the bars at 10, 70, 85 and 100 °C (measured from the SVG); the exit ticket gives 0,36 kPa/°C and −282…−258 °C.
- The SVG coordinates of all four figures match the data and the lines. The main figure is to scale: −276, −259 and −295 °C.
- Guardrails: the fit sentence ("yleensä"), uncertainty versus the manufacturer's error limit, the slope from two far points on the fitted line, the extrapolation range and its assumption, "todennäköisesti", and "the interval is an estimate, not a guaranteed limit" are all present and agree between the theory, the example, the inquiry and the summary.
- Model conditions: closed rigid vessel, thin gas, liquefaction before 0 K; the absolute zero is stated as the minimum (not zero) particle energy.
- Exactly one correct option in kertaus, ennuste-1, ennuste-2, aineisto, aariviiva, virhe and tarkistus-1. Each distractor's feedback gives the right reason.
- The data are labelled model values with added scatter (source simulated).
